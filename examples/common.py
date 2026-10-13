"""Common utilities and configuration for SFOS API examples."""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path
from typing import Any, Sequence

from dotenv import load_dotenv

# Ensure repository root is in sys.path so examples work without requiring pip install -e .
_REPO_ROOT = str(Path(__file__).resolve().parent.parent)
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)


from sfos_api import NotFoundError, SFOSApiError, SFOSApiErrorInfo, SFOSClient, parse_error  # noqa: E402


def handle_example_error(e: Any, action_desc: str = "operation", resource_name: str | None = None) -> None:
    """Print an informative and structured error message for examples."""
    info = parse_error(e)
    if isinstance(e, NotFoundError) or info.status_code == 404:
        target = f" '{resource_name or info.resource_id}'" if (resource_name or info.resource_id) else ""
        print(f"❌ Not Found (HTTP 404): Resource{target} does not exist on the firewall.")
        print(f"   Guidance: Ensure the target resource exists before attempting {action_desc}.")
    elif isinstance(e, SFOSApiError) or info.status_code is not None:
        status = f" [HTTP {info.status_code}]" if info.status_code else ""
        code_str = f" (Code: {info.code})" if info.code else ""
        err_str = f" ({info.error})" if info.error else ""
        print(f"❌ SFOS API Error{status}{code_str}{err_str} during {action_desc}: {info.message}")
        if info.details and info.details != info.message:
            print_data(info.details)
    else:
        print(f"❌ Error during {action_desc} ({info.error or type(e).__name__}): {info.message}")


def print_data(data: Any, keys: Sequence[str] | None = None) -> None:
    """Print data in pretty formatted output."""

    def filter_keys(obj: Any, key_list: Sequence[str]) -> Any:
        if isinstance(obj, dict):
            return {k: v for k, v in obj.items() if k in key_list}
        return obj

    if isinstance(data, dict):
        output = filter_keys(data, keys) if keys else data
        print(json.dumps(output, indent=2))
        return

    if isinstance(data, list):
        total = len(data)
        if total == 1:
            output = filter_keys(data[0], keys) if keys else data[0]
            print(json.dumps(output, indent=2))
            return

        num_width = len(str(total))
        for i, item in enumerate(data):
            item_num = str(i + 1).zfill(num_width)
            total_str = str(total).zfill(num_width)
            item_data = filter_keys(item, keys) if keys else item
            item_json = json.dumps(item_data, separators=(",", ": "), ensure_ascii=False)
            print(f"{item_num}/{total_str} : {item_json}")
        return

    print(data)


def get_config() -> dict[str, Any]:
    """Load configuration dictionary from environment variables."""
    load_dotenv()
    api_key = os.getenv("SFOS_API_KEY")
    if not api_key:
        raise ValueError("SFOS_API_KEY environment variable not set. Please set it in your .env file or environment.")

    host = os.getenv("SFOS_HOST", "localhost")
    if not host.strip():
        raise ValueError("SFOS_HOST cannot be empty")

    port_str = os.getenv("SFOS_PORT", "4444")
    port = int(port_str) if port_str else 4444

    verify_ssl_str = os.getenv("SFOS_VERIFY_SSL", "true").lower()
    verify_ssl = verify_ssl_str not in ("false", "0", "no")

    timeout = float(os.getenv("SFOS_TIMEOUT", "30.0"))

    return {
        "HOST": host,
        "PORT": port,
        "VERIFY_SSL": verify_ssl,
        "TIMEOUT": timeout,
        "API_KEY": api_key,
    }


def setup_client() -> SFOSClient:
    """Initialize and return an SFOSClient using environment variables."""
    config = get_config()
    return SFOSClient(
        config["HOST"],
        config["API_KEY"],
        port=config["PORT"],
        verify_ssl=config["VERIFY_SSL"],
        timeout=config["TIMEOUT"],
    )
