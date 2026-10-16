"""Tests for SFOSClient in sfos_api."""

import httpx
import pytest

from sfos_api import (
    Authentication,
    AuthenticationError,
    AuthorizationError,
    BadRequestError,
    ConflictError,
    Firewall,
    InternalServerError,
    Logging,
    Network,
    NotFoundError,
    SFOSClient,
    SophosCentral,
)


def test_client_init_validation():
    # Invalid host containing scheme
    with pytest.raises(ValueError, match="Do not include a protocol in host"):
        SFOSClient("https://192.168.1.1", "secret")

    # Empty host
    with pytest.raises(ValueError, match="host must not be empty"):
        SFOSClient("", "secret")

    # Empty API key
    with pytest.raises(ValueError, match="api_key must not be empty"):
        SFOSClient("192.168.1.1", "")


def test_client_base_url():
    client_default = SFOSClient("192.168.1.1", "secret")
    assert str(client_default.session.base_url) == "https://192.168.1.1/api/firewall-config/v1/"
    client_default.close()

    client_port = SFOSClient("192.168.1.1", "secret", port=4444)
    assert str(client_port.session.base_url) == "https://192.168.1.1:4444/api/firewall-config/v1/"
    client_port.close()


def test_client_context_manager():
    with SFOSClient("192.168.1.1", "secret") as client:
        assert client.session.headers["Authorization"] == "Bearer secret"
        assert client.session.headers["Accept"] == "application/json"


def test_clean_params():
    params = {"a": 1, "b": None, "c": "val"}
    cleaned = SFOSClient._clean_params(params)
    assert cleaned == {"a": 1, "c": "val"}
    assert SFOSClient._clean_params(None) is None
    assert SFOSClient._clean_params({"a": None}) is None


def test_success_responses():
    req = httpx.Request("GET", "https://example.com")
    resp_200 = httpx.Response(200, request=req, json={"status": "ok"})
    resp_201 = httpx.Response(201, request=req, json={"id": "new-1"})

    SFOSClient._raise_for_error(resp_200)
    SFOSClient._raise_for_error(resp_201)


def test_raise_for_error_custom_messages():
    req = httpx.Request("GET", "https://example.com")

    resp_400 = httpx.Response(400, request=req, json={"message": "Invalid IP", "error": "validationError"})
    with pytest.raises(BadRequestError) as exc_400:
        SFOSClient._raise_for_error(resp_400)
    assert exc_400.value.status_code == 400
    assert str(exc_400.value) == "Invalid IP"
    assert exc_400.value.error == "validationError"

    resp_401 = httpx.Response(401, request=req, json={"message": "Token expired"})
    with pytest.raises(AuthenticationError) as exc_401:
        SFOSClient._raise_for_error(resp_401)
    assert exc_401.value.status_code == 401
    assert str(exc_401.value) == "Token expired"

    resp_403 = httpx.Response(403, request=req, json={"message": "Access denied"})
    with pytest.raises(AuthorizationError) as exc_403:
        SFOSClient._raise_for_error(resp_403)
    assert exc_403.value.status_code == 403
    assert str(exc_403.value) == "Access denied"

    resp_404 = httpx.Response(404, request=req, json={"message": "Resource missing"})
    with pytest.raises(NotFoundError) as exc_404:
        SFOSClient._raise_for_error(resp_404)
    assert exc_404.value.status_code == 404
    assert str(exc_404.value) == "Resource missing"

    resp_409 = httpx.Response(409, request=req, json={"message": "Resource already exists"})
    with pytest.raises(ConflictError) as exc_409:
        SFOSClient._raise_for_error(resp_409)
    assert exc_409.value.status_code == 409
    assert str(exc_409.value) == "Resource already exists"

    resp_500 = httpx.Response(500, request=req, json={"message": "Internal failure"})
    with pytest.raises(InternalServerError) as exc_500:
        SFOSClient._raise_for_error(resp_500)
    assert exc_500.value.status_code == 500
    assert str(exc_500.value) == "Internal failure"


def test_raise_for_error_default_messages():
    req = httpx.Request("GET", "https://example.com")

    resp_400 = httpx.Response(400, request=req, content=b"")
    with pytest.raises(BadRequestError) as exc_400:
        SFOSClient._raise_for_error(resp_400)
    assert str(exc_400.value) == "Bad request."

    resp_401 = httpx.Response(401, request=req, content=b"")
    with pytest.raises(AuthenticationError) as exc_401:
        SFOSClient._raise_for_error(resp_401)
    assert str(exc_401.value) == "Authentication required."

    resp_403 = httpx.Response(403, request=req, content=b"")
    with pytest.raises(AuthorizationError) as exc_403:
        SFOSClient._raise_for_error(resp_403)
    assert str(exc_403.value) == "Authorization required."

    resp_404 = httpx.Response(404, request=req, content=b"")
    with pytest.raises(NotFoundError) as exc_404:
        SFOSClient._raise_for_error(resp_404)
    assert str(exc_404.value) == "Not found."

    resp_409 = httpx.Response(409, request=req, content=b"")
    with pytest.raises(ConflictError) as exc_409:
        SFOSClient._raise_for_error(resp_409)
    assert str(exc_409.value) == "Conflict."

    resp_500 = httpx.Response(500, request=req, content=b"")
    with pytest.raises(InternalServerError) as exc_500:
        SFOSClient._raise_for_error(resp_500)
    assert str(exc_500.value) == "Internal server error or Unexpected error."


def test_path_resolution():
    client = SFOSClient("sfos.example.com", "test-api-key")

    # Direct resolution
    assert client._resolve_path(Network.ZONES) == "/network/zones"
    assert client._resolve_path(Network.ZONES, "LAN") == "/network/zones/LAN"

    # With special chars in name
    assert client._resolve_path(Network.ZONES, "DMZ 1") == "/network/zones/DMZ%201"
    assert client._resolve_path(Network.ZONES, "branch/1") == "/network/zones/branch%2F1"

    # Parameterized item and action path resolution
    assert client._resolve_path("/network/zones/{idOrName}", "LAN") == "/network/zones/LAN"
    assert client._resolve_path(Logging.LOG_DESTINATIONS_SYSLOG_SERVERS_BY_ID_OR_NAME_LOGS, "server-1") == "/logging/log-destinations/syslog-servers/server-1/logs"

    # Error when parameter is missing
    with pytest.raises(ValueError, match="require 'id_or_name'"):
        client._resolve_path(Logging.LOG_DESTINATIONS_SYSLOG_SERVERS_BY_ID_OR_NAME_LOGS)


def test_crud_mock_calls():
    def handler(request: httpx.Request) -> httpx.Response:
        method = request.method
        path = request.url.path
        if "auto-page" in path:
            page = int(request.url.params.get("page", 1))
            if page == 1:
                return httpx.Response(200, json={
                    "items": [{"id": "1"}, {"id": "2"}],
                    "pages": {"current": 1, "size": 2, "total": 2, "maxSize": 100}
                })
            else:
                return httpx.Response(200, json={
                    "items": [{"id": "3"}],
                    "pages": {"current": 2, "size": 1, "total": 2, "maxSize": 100}
                })
        if method == "GET" and "nameContains" in request.url.query.decode():
            return httpx.Response(200, json={
                "items": [{"id": "rule-1", "name": "rule-1"}],
                "pages": {"current": 1, "size": 1, "total": 1, "maxSize": 100}
            })
        return httpx.Response(200, json={"path": path, "method": method})

    client = SFOSClient("sfos.example.com", "api-key")
    client.session._transport = httpx.MockTransport(handler)

    # 1. create
    res = client.create(Network.ZONES, {"name": "testZone"})
    assert res["path"] == "/api/firewall-config/v1/network/zones"
    assert res["method"] == "POST"

    # 2. read single item
    res = client.read(Network.ZONES, "LAN")
    assert res["path"] == "/api/firewall-config/v1/network/zones/LAN"
    assert res["method"] == "GET"

    # 3. read collection with auto-pagination
    res = client.read("/auto-page")
    assert len(res["items"]) == 3
    assert res["items"][0]["id"] == "1"
    assert res["items"][2]["id"] == "3"
    assert res["pages"]["total"] == 2

    # 4. update
    res = client.update(Firewall.RULES_IPV4, "rule-1", data={"description": "Updated"})
    assert res["path"] == "/api/firewall-config/v1/firewall/rules/ipv4/rule-1"
    assert res["method"] == "PATCH"

    # 5. delete single
    res = client.delete(Firewall.RULES_IPV4, "rule-1")
    assert res["path"] == "/api/firewall-config/v1/firewall/rules/ipv4/rule-1"
    assert res["method"] == "DELETE"

    # 6. delete batch (with dicts)
    res = client.delete(Firewall.RULES_IPV4, items=[{"id": "rule-1"}, {"id": "rule-2"}])
    assert res["path"] == "/api/firewall-config/v1/firewall/rules/ipv4/delete"
    assert res["method"] == "POST"

    # 6b. delete batch (with strings)
    res = client.delete(Firewall.RULES_IPV4, items=["rule-1", "rule-2"])
    assert res["path"] == "/api/firewall-config/v1/firewall/rules/ipv4/delete"
    assert res["method"] == "POST"

    # 6c. delete with query filter (e.g. nameContains)
    res = client.delete(Firewall.RULES_IPV4, nameContains="rule")
    assert res["path"] == "/api/firewall-config/v1/firewall/rules/ipv4/delete"

    # 6d. delete with params dict
    res = client.delete(Firewall.RULES_IPV4, params={"nameContains": "rule", "type": "ipv4Network"})
    assert res["path"] == "/api/firewall-config/v1/firewall/rules/ipv4/delete"

    # 6e. validation: mutually exclusive nameContains and nameNotEquals
    with pytest.raises(ValueError, match="does not allow 'nameContains' and 'nameNotEquals' together"):
        client.delete(Firewall.RULES_IPV4, nameContains="a", nameNotEquals="b")

    # 6f. validation: multiple modes (id_or_name + items)
    with pytest.raises(ValueError, match="Provide exactly one deletion mode"):
        client.delete(Firewall.RULES_IPV4, "rule-1", items=["rule-2"])


    # 7. create standalone action with payload
    res = client.create(SophosCentral.REGISTER, data={"token": "abc"})
    assert res["path"] == "/api/firewall-config/v1/sophos-central/register"
    assert res["method"] == "POST"

    # 8. create standalone action without payload
    res = client.create(Network.CELLULAR_WAN_RESET_MODEM)
    assert res["path"] == "/api/firewall-config/v1/network/cellular-wan/reset-modem"
    assert res["method"] == "POST"

    # 9. create parameterized action with in-path placeholder
    res = client.create(Authentication.SERVERS_ACTIVE_DIRECTORY_BY_ID_OR_NAME_FETCH_GROUPS, id_or_name="ad-1")
    assert res["path"] == "/api/firewall-config/v1/authentication/servers/active-directory/ad-1/fetch-groups"
    assert res["method"] == "POST"

    # 10. move (direct convenience wrapper)
    res = client.move(Firewall.RULES_IPV4, {"id": "rule-2", "position": "top"})
    assert res["path"] == "/api/firewall-config/v1/firewall/rules/ipv4/move"
    assert res["method"] == "POST"

    # 11. test_connection (direct convenience wrapper)
    res = client.test_connection(Authentication.SERVERS_ACTIVE_DIRECTORY, data={"serverIp": "10.0.0.1"})
    assert res["path"] == "/api/firewall-config/v1/authentication/servers/active-directory/test-connection"
    assert res["method"] == "POST"

