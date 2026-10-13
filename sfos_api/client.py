"""Lightweight SFOS API client implementation.

A zero-overhead, Python 3.11+ client that uses StrEnum domain classes for endpoints
and eliminates the Endpoint dataclass and monolithic Endpoints registry.
"""

from __future__ import annotations

import logging
import re
from collections.abc import Mapping, Sequence
from types import TracebackType
from typing import Any, Final, Self
from urllib.parse import quote

import httpx

from .exceptions import (
    AuthenticationError,
    AuthorizationError,
    BadRequestError,
    ConflictError,
    InternalServerError,
    NotFoundError,
    SFOSApiError,
    UnexpectedError,
)

# Module-level logger for audit trail and debugging
logger = logging.getLogger(__name__)

DEFAULT_TIMEOUT: Final[float] = 30.0
DEFAULT_PAGE_SIZE: Final[int] = 100


class SFOSClient:
    """Synchronous lightweight SFOS client using string-based endpoints."""

    def __init__(
        self,
        host: str,
        api_key: str,
        *,
        port: int | None = None,
        verify_ssl: bool | str = True,
        timeout: float | httpx.Timeout = DEFAULT_TIMEOUT,
    ) -> None:
        """Initialize the SFOS client with the given configuration."""
        if "://" in host:
            raise ValueError("Do not include a protocol in host; HTTPS is enforced.")
        if not host.strip():
            raise ValueError("host must not be empty")
        if not api_key:
            raise ValueError("api_key must not be empty")
        authority = f"{host}:{port}" if port is not None else host
        self.base_url = f"https://{authority}/api/firewall-config/v1/"
        self.session = httpx.Client(
            base_url=self.base_url,
            headers={"Accept": "application/json", "Authorization": f"Bearer {api_key}"},
            timeout=timeout,
            verify=verify_ssl,
        )

    def __enter__(self) -> Self:
        """Enter the runtime context and return the client instance."""
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        tb: TracebackType | None,
    ) -> None:
        """Exit the runtime context and close the HTTP session."""
        self.close()

    def close(self) -> None:
        """Close the underlying HTTP session."""
        self.session.close()

    @staticmethod
    def _clean_params(params: Mapping[str, Any] | None) -> dict[str, Any] | None:
        if params is None:
            return None
        clean = {k: v for k, v in params.items() if v is not None}
        return clean or None

    @classmethod
    def _resolve_path(cls, endpoint: str, id_or_name: str | None = None) -> str:
        base = endpoint
        if id_or_name:
            quoted = quote(id_or_name, safe="")
            if re.search(r"\{[^}]+\}", base):
                return re.sub(r"\{[^}]+\}", quoted, base, count=1)
            return f"{base.rstrip('/')}/{quoted}"
        if re.search(r"\{[^}]+\}", base):
            raise ValueError(f"Endpoint '{base}' contains path parameters that require 'id_or_name' to be specified.")
        return base

    DEFAULT_ERROR_MESSAGES: Final[dict[int, str]] = {
        400: "Bad request.",
        401: "Authentication required.",
        403: "Authorization required.",
        404: "Not found.",
        409: "Conflict.",
        500: "Internal server error or Unexpected error.",
    }

    @classmethod
    def _error_details(cls, response: httpx.Response) -> tuple[str, str | None, str | int | None, Any]:
        default_message = cls.DEFAULT_ERROR_MESSAGES.get(response.status_code, response.reason_phrase or "Unexpected error.")
        try:
            body = response.json()
        except ValueError:
            body = response.text
        if isinstance(body, dict):
            error = body.get("error")
            message = str(body.get("message") or error or default_message)
            code = body.get("code")
        else:
            error, code = None, None
            message = str(body or default_message)
        return message, error, code, body

    @classmethod
    def _raise_for_error(cls, response: httpx.Response) -> None:
        if not response.is_error:
            return
        message, error, code, body = cls._error_details(response)
        error_map: dict[int, type[SFOSApiError]] = {
            400: BadRequestError,
            401: AuthenticationError,
            403: AuthorizationError,
            404: NotFoundError,
            409: ConflictError,
            500: InternalServerError,
        }
        exc = error_map.get(response.status_code, InternalServerError if response.status_code >= 500 else SFOSApiError)
        raise exc(message, status_code=response.status_code, error=error, code=code, response_body=body)

    # =========================================================================
    # Low-Level Transport & Protocol Execution
    # =========================================================================

    def request(
        self,
        method: str,
        endpoint: str,
        *,
        params: Mapping[str, Any] | None = None,
        json_data: Any = None,
        headers: Mapping[str, str] | None = None,
    ) -> Any:
        """Send a raw HTTP request to the firewall API."""
        method = method.upper()
        clean_endpoint = endpoint.lstrip("/")
        response = self.session.request(
            method,
            clean_endpoint,
            params=self._clean_params(params),
            json=json_data,
            headers=headers,
        )
        self._raise_for_error(response)
        if response.status_code == 204 or not response.content:
            return None
        if "json" in response.headers.get("content-type", "").lower():
            return response.json()
        return response.text

    # =========================================================================
    # Core CRUD Methods
    # =========================================================================

    def create(
        self,
        endpoint: str,
        data: Mapping[str, Any] | None = None,
        *,
        id_or_name: str | None = None,
        params: Mapping[str, Any] | None = None,
    ) -> Any:
        """Create a new resource, invoke a standalone action, or execute a parameterized action.

        Args:
            endpoint: API endpoint string or StrEnum domain member (e.g. Network.ZONES, SophosCentral.REGISTER).
            data: Optional dictionary containing request payload data.
            id_or_name: Optional resource identifier for item-scoped actions or parameterized paths.
            params: Optional query parameters dictionary.

        Returns:
            Decoded response from the firewall (or None if 204 No Content).

        """
        path = self._resolve_path(endpoint, id_or_name)
        return self.request("POST", path, params=params, json_data=dict(data) if data is not None else None)


    def read(
        self,
        endpoint: str,
        id_or_name: str = "",
        params: Mapping[str, Any] | None = None,
        **kwargs: Any,
    ) -> Any:
        """Read a single resource or a collection with automatic pagination.

        Auto-pagination is enabled when neither 'page' nor 'pageTotal'
        are specified. A supplied 'pageSize' controls the batch size
        used during auto-pagination.

        Args:
            endpoint: API endpoint string or StrEnum domain member (e.g. Network.ZONES).
            id_or_name: Resource identifier or name for single resource read (default: empty string).
            params: Optional dictionary of query parameters.
            **kwargs: Optional query parameters as keyword arguments (merged with params).

        Returns:
            Single resource dictionary or combined results from all pages.

        Examples:
            # Auto-paginate all pages
            result = client.read(Network.ZONES)

            # Auto-paginate with custom batch size
            result = client.read(Firewall.RULES_IPV4, pageSize=50)

            # Read single page only
            result = client.read(Network.ZONES, page=2)

            # Read single resource
            result = client.read(Network.ZONES, "LAN")

        """
        query = {**(params or {}), **kwargs}

        # Single resource or parameterized path
        if id_or_name:
            invalid = {"page", "pageSize", "pageTotal"} & query.keys()
            if invalid:
                raise ValueError(f"Pagination parameters are not supported when reading a single resource: {sorted(invalid)}")
            path = self._resolve_path(endpoint, id_or_name)
            return self.request("GET", path, params=query or None)

        # Collection
        base_path = endpoint
        if re.search(r"\{[^}]+\}", base_path):
            raise ValueError(f"Endpoint '{base_path}' contains path parameters that require 'id_or_name' to be specified.")

        # Explicit paging requested by caller
        explicit_paging = bool({"page", "pageTotal"} & query.keys())
        if explicit_paging:
            return self.request("GET", endpoint, params=query or None)

        # Auto-pagination
        page_size = int(query.get("pageSize", DEFAULT_PAGE_SIZE))
        page_size = max(1, min(page_size, 100))

        page_query = {
            **query,
            "page": 1,
            "pageSize": page_size,
            "pageTotal": True,
        }

        first = self.request("GET", endpoint, params=page_query)
        if not isinstance(first, dict) or not isinstance(first.get("items"), list):
            return first

        items = list(first["items"])
        pages = first.get("pages") or {}
        total_pages = int(pages.get("total", 1))

        for page_num in range(2, total_pages + 1):
            page = self.request(
                "GET",
                endpoint,
                params={
                    **page_query,
                    "page": page_num,
                },
            )
            if isinstance(page, dict):
                page_items = page.get("items")
                if isinstance(page_items, list):
                    items.extend(page_items)

        result = dict(first)
        result["items"] = items
        result["pages"] = {
            "current": 1,
            "size": len(items),
            "maxSize": pages.get("maxSize", 100),
            "total": total_pages,
        }
        if "items" in pages:
            result["pages"]["items"] = pages["items"]
        return result

    def update(self, endpoint: str, id_or_name: str | None = None, *, data: Mapping[str, Any]) -> Any:
        """Update an existing resource using JSON Merge Patch (RFC 7396)."""
        if id_or_name is not None:
            if not id_or_name:
                raise ValueError("id_or_name must not be empty")
            path = self._resolve_path(endpoint, id_or_name)
        else:
            path = self._resolve_path(endpoint)
        return self.request("PATCH", path, json_data=dict(data))

    def delete(
        self,
        endpoint: str,
        id_or_name: str | None = None,
        *,
        items: Sequence[str | Mapping[str, Any]] | None = None,
        params: Mapping[str, Any] | None = None,
        batch_size: int = 50,
        **kwargs: Any,
    ) -> Any:
        """Delete an existing resource by identifier, explicit batch, or query filter.

        Supported deletion modes:
          1. Single resource deletion via HTTP DELETE (`id_or_name`).
          2. Explicit batch deletion via HTTP POST .../delete (`items`).
          3. Query-filter deletion via `params` or kwargs (`nameContains`, `nameNotEquals`, `type`).

        Args:
            endpoint: API endpoint string or StrEnum domain member (e.g. Network.ADDRESSES_IPV4).
            id_or_name: Resource identifier or name for single resource deletion.
            items: Sequence of resource identifiers (strings) or item dictionaries for batch deletion.
            params: Optional query filter parameters dictionary (e.g. {"nameContains": "Test_", "type": "ipv4Address"}).
            batch_size: Maximum items per batch request chunk (SFOS API limit is 50; clamped between 1 and 50).
            **kwargs: Optional query filter parameters (e.g. nameContains="Test_", nameNotEquals="Prod_").

        Returns:
            Decoded API response from the firewall or list of responses if chunked.

        Raises:
            ValueError: If mutually exclusive modes or filter arguments are provided.
        """
        filter_params = {**(params or {}), **kwargs}

        has_id = id_or_name is not None
        has_items = items is not None
        has_filters = bool(filter_params)

        # Enforce mutual exclusivity among the 3 modes
        selected_modes = int(has_id) + int(has_items) + int(has_filters)
        if selected_modes != 1:
            raise ValueError(
                "Provide exactly one deletion mode: single resource ('id_or_name'), "
                "explicit batch ('items'), or query filters ('params' / filter kwargs)."
            )

        base = endpoint.rstrip("/")
        delete_path = base if base.endswith("/delete") else f"{base}/delete"
        chunk_size = max(1, min(batch_size, 50))

        # Mode 1: Single Resource Deletion
        if has_id:
            assert id_or_name is not None
            if not id_or_name:
                raise ValueError("id_or_name must not be empty")
            path = self._resolve_path(endpoint, id_or_name)
            return self.request("DELETE", path)

        # Mode 2: Query Filter Deletion (via params / kwargs)
        if has_filters:
            if "nameContains" in filter_params and "nameNotEquals" in filter_params:
                raise ValueError(
                    "Sophos REST API does not allow 'nameContains' and 'nameNotEquals' together. "
                    "Specify at most one name filter per request."
                )

            discovered = self.read(endpoint, params=filter_params)
            matched_items = discovered.get("items", []) if isinstance(discovered, dict) else []

            if not matched_items:
                return {"matched_count": 0, "deleted_count": 0, "results": []}

            items = [
                {"name": x["name"]} if "name" in x else {"id": x["id"]}
                for x in matched_items
            ]

        # Mode 3: Batch Deletion (Explicit items or Discovered from Mode 2)
        assert items is not None
        if not items:
            raise ValueError("items must not be empty")

        payload_items: list[dict[str, Any]] = [
            {"name": item} if isinstance(item, str) else dict(item)
            for item in items
        ]

        responses: list[Any] = []
        for i in range(0, len(payload_items), chunk_size):
            chunk = payload_items[i : i + chunk_size]
            resp = self.request("POST", delete_path, json_data={"items": chunk})
            responses.append(resp)

        return responses[0] if len(responses) == 1 else responses


    # =========================================================================
    # Convenience Wrappers
    # =========================================================================

    def move(self, endpoint: str, data: Mapping[str, Any]) -> Any:
        """Reposition a rule or route within an ordered rulebase using the 'move' action.

        Directly issues a POST request to f"{endpoint}/move".

        Args:
            endpoint: Rule or route endpoint (e.g. Firewall.RULES_IPV4, Nat.RULES_IPV4).
            data: Move specification containing id, position, and optional targetRule.

        Returns:
            Decoded response from the firewall.

        """
        path = f"{endpoint.rstrip('/')}/move"
        return self.request("POST", path, json_data=dict(data))

    def test_connection(
        self,
        endpoint: str,
        data: Mapping[str, Any] | None = None,
        *,
        params: Mapping[str, Any] | None = None,
    ) -> Any:
        """Test connection to an authentication server, gateway, or threat feed.

        Directly issues a POST request to f"{endpoint}/test-connection".

        Args:
            endpoint: Base server or service endpoint (e.g. Authentication.SERVERS_ACTIVE_DIRECTORY,
                Authentication.SERVERS_LDAP, Authentication.SERVERS_RADIUS,
                Authentication.SERVERS_TACACS, Authentication.SERVERS_GENERIC_IDP_SSO,
                ActiveThreatResponse.THIRDPARTY_THREAT_FEEDS).
            data: Optional dictionary containing server parameters (e.g. host, port, credentials).
            params: Optional query parameters dictionary.

        Returns:
            Decoded response from the firewall indicating connection test outcome.

        """
        path = f"{endpoint.rstrip('/')}/test-connection"
        return self.request(
            "POST",
            path,
            params=params,
            json_data=dict(data) if data is not None else None,
        )




__version__ = "0.5.0-beta"
__all__ = [
    "AuthenticationError",
    "AuthorizationError",
    "BadRequestError",
    "ConflictError",
    "InternalServerError",
    "NotFoundError",
    "SFOSApiError",
    "SFOSClient",
    "UnexpectedError",
]
