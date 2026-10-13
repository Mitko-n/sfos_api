# SFOS API - API Reference <a id="top"></a>

[![Python 3.11+](https://img.shields.io/badge/Python-3.11%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](../LICENSE)
[![Development Status: Beta 0.5.0](https://img.shields.io/badge/Status-Beta%200.5.0-orange.svg)](https://pypi.org/project/sfos-api/)

Complete technical reference for the `SFOSClient` class, methods, parameters, invocation variants, and exception hierarchy.

---

## 🧭 Quick Navigation <a id="quick-navigation"></a>

| Category | Method / Topic | Description | Link |
|---|---|---|---|
| **Lifecycle** | **Client Initialization** | Configuration options, SSL, timeout, context manager | [Jump to Client Init](#client-initialization) |
| **Core CRUD** | **`client.read()`** | Auto-pagination, filtering, single-page, single-resource | [Jump to read()](#1-read) |
| **Core CRUD & Actions** | **`client.create()`** | Standard creation, standalone actions, and parameterized RPCs | [Jump to create()](#2-create) |
| **Core CRUD** | **`client.update()`** | RFC 7396 JSON Merge Patch, singletons, clearing fields | [Jump to update()](#3-update) |
| **Core CRUD** | **`client.delete()`** | Single resource deletion, batch deletion | [Jump to delete()](#4-delete) |
| **Convenience Wrapper** | **`client.move()`** | Direct rulebase reordering (`top`, `bottom`, `before`, `after`) | [Jump to move()](#5-move) |
| **Convenience Wrapper** | **`client.test_connection()`** | Direct connectivity & credential testing for directory/AAA servers | [Jump to test_connection()](#6-test_connection) |
| **Low-Level Transport** | **`client.request()`** | Low-level HTTP invocation, custom headers | [Jump to request()](#7-request) |
| **Session Lifecycle** | **`client.close()`** | Session lifecycle management | [Jump to close()](#8-close) |
| **Exceptions** | **Exception Hierarchy** | HTTP error mappings, error codes, structured handling | [Jump to Exceptions](#exception-hierarchy) |

**Jump to Section:** [🛠️ Client Initialization](#client-initialization) &nbsp;•&nbsp; [📌 Core CRUD & Actions](#core-crud-methods) &nbsp;•&nbsp; [⚡ Convenience Wrappers](#convenience-wrappers) &nbsp;•&nbsp; [🔌 Low-Level & Lifecycle](#low-level-lifecycle-methods) &nbsp;•&nbsp; [🚨 Exception Hierarchy](#exception-hierarchy)

---

<a id="client-initialization"></a>
## 🛠️ Client Initialization & Lifecycle

```python
from sfos_api import SFOSClient

client = SFOSClient(
    host="192.168.1.1",
    api_key="your-api-key",
    port=4444,
    verify_ssl=False,
    timeout=30.0,
)
```

### Constructor Parameters

| Parameter | Type | Default | Description |
|---|---|:---:|---|
| `host` | `str` | *Required* | Firewall IP address or FQDN. **Do not include protocol** (`https://` is automatically enforced). |
| `api_key` | `str` | *Required* | API token generated in Sophos Firewall OS (SFOS) WebAdmin (`Administration > API`). |
| `port` | `int \| None` | `None` | WebAdmin REST API port. Typically `4444`. When `None`, standard HTTPS port (`443`) is used. |
| `verify_ssl` | `bool \| str` | `True` | SSL certificate verification. Set to `False` for self-signed certificates or pass path to a trusted CA bundle file. |
| `timeout` | `float \| httpx.Timeout` | `30.0` | HTTP request timeout in seconds or an explicit `httpx.Timeout` instance. |

### Context Manager Pattern (Recommended)

`SFOSClient` supports Python's context manager protocol (`with` statement) to automatically close the underlying HTTP transport:

```python
from sfos_api import SFOSClient, Network

with SFOSClient("192.168.1.1", "your-api-key", port=4444, verify_ssl=False) as client:
    zones = client.read(Network.ZONES)
    print(f"Total zones: {len(zones['items'])}")
# Session is automatically closed upon block exit
```

[↑ Back to Quick Navigation](#quick-navigation) &nbsp;•&nbsp; [↑ Back to Top](#top)

---

<a id="core-crud-methods"></a>
<a id="client-methods"></a>
## 📌 Core CRUD Methods

The four fundamental CRUD primitives (`read`, `create`, `update`, `delete`) manage the complete lifecycle of SFOS configuration objects. They automatically handle base URL construction, RFC 3986 path encoding, query parameter filtering, transparent auto-pagination, and RFC 7396 merge patch semantics.

<a id="1-read"></a>
### 1. `client.read()`

Fetch a single resource, a filtered query, or an auto-paginated collection.

```python
client.read(
    endpoint: str,
    id_or_name: str = "",
    params: Mapping[str, Any] | None = None,
    **kwargs: Any,
) -> dict[str, Any]
```

#### Parameters

| Parameter | Type | Default | Description |
|---|---|:---:|---|
| `endpoint` | `str` | *Required* | Domain endpoint constant (e.g. `Network.ZONES`) or raw API path string. |
| `id_or_name` | `str` | `""` | Identifier or name of a single resource. When provided, single resource lookup is performed. |
| `params` | `Mapping[str, Any] \| None` | `None` | Optional query parameters dictionary (e.g. `{"nameContains": "Server"}`). |
| `**kwargs` | `Any` | — | Additional query parameters passed as keyword arguments (merged with `params`). |

#### Supported Variants

##### Variant A: Transparent Auto-Pagination (Default for Collections)
When reading a collection without specifying `page`, `client.read()` automatically requests page 1, discovers the total page count, fetches all remaining pages sequentially, and aggregates all results into a single consolidated `items` list:

```python
# Fetches all network zones across all pages automatically
zones = client.read(Network.ZONES)
print(f"Retrieved {len(zones['items'])} zones across {zones['pages']['total']} page(s)")
```

##### Variant B: Auto-Pagination with Custom Batch Size
Controls the chunk size per HTTP request during auto-pagination (SFOS supports `1` to `100` per page):

```python
# Fetches all IPv4 firewall rules in chunks of 50 per request
rules = client.read(Firewall.RULES_IPV4, pageSize=50)
```

##### Variant C: Server-Side Query Filtering
Pass filter criteria via `params` or direct keyword arguments:

```python
# Filter using keyword arguments
servers = client.read(Network.ADDRESSES_IPV4, nameContains="Server")

# Filter using params dictionary
active_rules = client.read(
    Firewall.RULES_IPV4,
    params={"status": "enabled", "pageSize": 25},
)
```

##### Variant D: Explicit Single-Page Fetch (Disables Auto-Pagination)
Specify `page` to retrieve only a specific single page:

```python
# Retrieves page 2 only (no subsequent pages fetched)
page_2 = client.read(Network.ADDRESSES_IPV4, page=2, pageSize=25)
print(f"Items on page 2: {len(page_2['items'])}")
```

##### Variant E: Single Resource Read by Name or ID
Pass the resource identifier or name as the second argument:

```python
# Fetch single zone
zone = client.read(Network.ZONES, "LAN")
print(f"Zone type: {zone['type']}")

# Fetch single host object
host = client.read(Network.ADDRESSES_IPV4, "Database_Master")
```

##### Variant F: Parameterized Path Sub-Resource Read
When an endpoint template contains path variables (e.g. `Logging.SERVERS_SYSLOG_LOGS` which maps to `/logging/servers/syslog/{idOrName}/logs`), pass the parent identifier as `id_or_name`:

```python
logs_config = client.read(Logging.SERVERS_SYSLOG_LOGS, "syslog-server-1")
```

[↑ Back to Quick Navigation](#quick-navigation) &nbsp;•&nbsp; [↑ Back to Top](#top)

---

<a id="2-create"></a>
### 2. `client.create()`

Create a new configuration resource on the firewall, invoke a standalone action, or execute a parameterized RPC action.

```python
client.create(
    endpoint: str,
    data: Mapping[str, Any] | None = None,
    *,
    id_or_name: str | None = None,
    params: Mapping[str, Any] | None = None,
) -> Any
```

#### Parameters

| Parameter | Type | Default | Description |
|---|---|:---:|---|
| `endpoint` | `str` | *Required* | Domain endpoint constant (e.g. `Network.ADDRESSES_IPV4`, `SophosCentral.REGISTER`) or raw path. |
| `data` | `Mapping[str, Any] \| None` | `None` | Optional resource attributes or action parameters sent as JSON body. |
| `id_or_name` | `str \| None` | `None` | Optional identifier for parameterized/nested paths (e.g. `{idOrName}`). |
| `params` | `Mapping[str, Any] \| None` | `None` | Optional query string parameters dictionary. |

#### Supported Variants

##### Variant A: Standard Collection Resource Creation
```python
new_host = client.create(Network.ADDRESSES_IPV4, {
    "name": "Web_Server_01",
    "ipAddress": "192.168.10.50",
    "type": "IPv4",
    "description": "Primary web frontend",
})
print("Host created successfully")
```

##### Variant B: Standalone Action RPC Execution
For action endpoints that perform operational commands directly via `POST`:

```python
# Register appliance with Sophos Central
client.create(
    SophosCentral.REGISTER,
    data={"registrationToken": "central-token-xyz"},
)

# Hardware reset for cellular modem (no payload required)
client.create(Network.CELLULAR_WAN_RESET_MODEM)
```

##### Variant C: Parameterized In-Path Action RPC Execution
Substitutes `{idOrName}` in action templates seamlessly:

```python
# Query security groups from a specific Active Directory server
groups = client.create(
    Authentication.SERVERS_ACTIVE_DIRECTORY_BY_ID_OR_NAME_FETCH_GROUPS,
    id_or_name="HQ_Active_Directory",
)

# Trigger synchronization on a specific threat feed
client.create(
    ActiveThreatResponse.THIRDPARTY_THREAT_FEEDS_BY_ID_OR_NAME_SYNCHRONIZE,
    id_or_name="feed-01",
)
```

[↑ Back to Quick Navigation](#quick-navigation) &nbsp;•&nbsp; [↑ Back to Top](#top)


---

<a id="3-update"></a>
### 3. `client.update()`

Update an existing resource using **JSON Merge Patch (RFC 7396)** semantics via HTTP `PATCH`.

```python
client.update(
    endpoint: str,
    id_or_name: str | None = None,
    *,
    data: Mapping[str, Any],
) -> dict[str, Any]
```

#### RFC 7396 Rules:
- Attributes present in `data` are overwritten or added.
- Attributes set to `None` (JSON `null`) are deleted or reset to firewall defaults.
- Omitted attributes remain completely untouched.

#### Parameters

| Parameter | Type | Default | Description |
|---|---|:---:|---|
| `endpoint` | `str` | *Required* | Domain endpoint constant (e.g. `Network.ADDRESSES_IPV4`) or raw path. |
| `id_or_name` | `str \| None` | `None` | Resource identifier or name. Required for collection items; omitted for singletons. |
| `data` | `Mapping[str, Any]` | *Required* | Dictionary of attributes to update. |

#### Supported Variants

##### Variant A: Update Identified Collection Resource
```python
# Updates only the description without overwriting IP address or other fields
client.update(
    Network.ADDRESSES_IPV4,
    "Web_Server_01",
    data={"description": "Staging frontend node"},
)
```

##### Variant B: Reset / Clear Specific Fields
Pass `None` to clear optional attributes:

```python
client.update(
    Network.ADDRESSES_IPV4,
    "Web_Server_01",
    data={"description": None},  # Clears description on firewall
)
```

##### Variant C: Singleton Resource Update (No ID)
For global singleton settings endpoints that don't have separate sub-items:

```python
client.update(
    System.BACKUP,
    data={"mode": "scheduled", "frequency": "daily"},
)
```

[↑ Back to Quick Navigation](#quick-navigation) &nbsp;•&nbsp; [↑ Back to Top](#top)

---

<a id="4-delete"></a>
### 4. `client.delete()`

Delete one or multiple resources from the firewall.

```python
client.delete(
    endpoint: str,
    id_or_name: str | None = None,
    *,
    items: Sequence[str | Mapping[str, Any]] | None = None,
    params: Mapping[str, Any] | None = None,
    batch_size: int = 50,
    **kwargs: Any,
) -> Any
```

> [!IMPORTANT]
> Exactly one deletion mode must be provided:
> 1. Single resource identifier (`id_or_name`).
> 2. Explicit batch list (`items`).
> 3. Query filters (`params` or filter kwargs such as `nameContains`, `nameNotEquals`, `type`).
>
> Providing more or less than one deletion mode raises a `ValueError`.
>
> **Filter Rule:** `nameContains` and `nameNotEquals` are **mutually exclusive** per Sophos REST API specification and cannot be combined together.

#### Parameters

| Parameter | Type | Default | Description |
|---|---|:---:|---|
| `endpoint` | `str` | *Required* | Domain endpoint constant or raw API path. |
| `id_or_name` | `str \| None` | `None` | Identifier or name of a single resource to delete via `DELETE /{endpoint}/{id}`. |
| `items` | `Sequence[str \| Mapping] \| None` | `None` | List of item strings (names/IDs) or item dictionaries for batch deletion via `POST /{endpoint}/delete`. Automatically chunked into batches of $\le 50$. |
| `params` | `Mapping[str, Any] \| None` | `None` | Optional query filter parameters dictionary (e.g. `{"nameContains": "Temp_", "type": "ipv4Address"}`). |
| `batch_size` | `int` | `50` | Maximum items per batch request chunk (SFOS API limit is 50; clamped between 1 and 50). |
| `**kwargs` | `Any` | — | Additional query filter keyword arguments (e.g. `nameContains="Temp_"`, `nameNotEquals="Prod_"`). |

#### Supported Variants

##### Variant A: Single Resource Deletion
```python
# Sends HTTP DELETE /network/addresses/ipv4/Web_Server_01
client.delete(Network.ADDRESSES_IPV4, "Web_Server_01")
print("Host deleted")
```

##### Variant B: Batch Multi-Resource Deletion (Strings or Dictionaries)
Accepts either simple name/ID strings or dictionaries. If more than 50 items are passed, `delete()` automatically splits requests into chunks of $\le 50$:

```python
# Pass simple string names/IDs:
client.delete(
    Network.ADDRESSES_IPV4,
    items=["Old_Host_1", "Old_Host_2", "Old_Host_3"],
)

# Or pass dictionaries:
client.delete(
    Network.ADDRESSES_IPV4,
    items=[{"name": "Old_Host_1"}, {"name": "Old_Host_2"}],
)
print("Batch delete completed")
```

##### Variant C: Query Filter Deletion (`nameContains`, `nameNotEquals`, `type`)
Discovers matching resources on the firewall using auto-pagination and server-side filtering, then executes batch deletion:

```python
# Delete all IPv4 address objects containing "Temp_" in their name
client.delete(Network.ADDRESSES_IPV4, nameContains="Temp_")

# Combine name filter with object type:
client.delete(
    Network.ADDRESSES_IPV4,
    nameContains="Test_",
    type="ipv4Range",
)

# Or pass filter criteria via params dict:
client.delete(
    Network.SERVICES,
    params={"nameContains": "Legacy_", "type": "tcpOrUdp"},
)
```

##### Variant D: Parameterized Resource Deletion
```python
# Deletes a nested sub-resource using template substitution
client.delete("/logging/servers/syslog/{idOrName}", "syslog-deprecated")
```

[↑ Back to Quick Navigation](#quick-navigation) &nbsp;•&nbsp; [↑ Back to Top](#top)

---

<a id="convenience-wrappers"></a>
## ⚡ Convenience Wrappers

Convenience wrappers are high-level, domain-specific Python helpers for recurring administrative tasks. Instead of constructing raw URL strings and nested payloads manually, convenience wrappers provide typed arguments, validation, and intuitive parameter syntax. Under the hood, convenience wrappers issue HTTP requests directly via `client.request("POST", ...)`.

| Wrapper Method | Direct Wire Route | Purpose | Supported Domains |
|---|---|---|---|
| **`client.move()`** | `POST {endpoint}/move` | Atomic rulebase priority reordering | `Firewall`, `Nat`, `SdWan`, `TlsInspection` |
| **`client.test_connection()`** | `POST {endpoint}/test-connection` | Non-persisting reachability & credential tests | `Authentication`, `ActiveThreatResponse` |

---

<a id="5-move"></a>
### 5. `client.move()`

Reposition an ordered rule or route within an SFOS rulebase. SFOS evaluates rules sequentially from top to bottom; `move` allows precise, atomic rule priority reordering.

```python
client.move(endpoint: str, data: Mapping[str, Any]) -> Any
```

> [!NOTE]
> `client.move(endpoint, data)` directly issues an HTTP POST request to `f"{endpoint.rstrip('/')}/move"`.


#### Parameters

| Parameter | Type | Default | Description |
|---|---|:---:|---|
| `endpoint` | `str` | *Required* | Ordered rulebase endpoint constant (see supported list below). |
| `data` | `Mapping[str, Any]` | *Required* | Move specification dictionary containing rule `id`, `position`, and optional `targetRule`. |

#### Move Payload Fields

| Field | Type | Allowed Values | Description |
|---|---|---|---|
| `id` | `str` | Rule identifier | The ID or name of the rule to move. |
| `position` | `str` | `"top"`, `"bottom"`, `"before"`, `"after"` | New position target. |
| `targetRule` | `str` | Rule identifier | Target rule ID (required when `position` is `"before"` or `"after"`). |

#### Supported Rulebase Endpoints

| Domain | Supported Endpoints |
|---|---|
| **Firewall** | `Firewall.RULES_IPV4`, `Firewall.RULES_IPV6` |
| **NAT** | `Nat.RULES_IPV4`, `Nat.RULES_IPV6` |
| **SD-WAN** | `SdWan.ROUTES_IPV4`, `SdWan.ROUTES_IPV6` |
| **TLS Inspection** | `TlsInspection.RULES_IPV4` |

#### Supported Variants

##### Variant A: Move to Boundary (`"top"` or `"bottom"`)
```python
# Move urgent high-priority rule to the top
client.move(Firewall.RULES_IPV4, {
    "id": "rule-block-malware",
    "position": "top",
})

# Move default catch-all rule to the bottom
client.move(Firewall.RULES_IPV4, {
    "id": "rule-default-drop",
    "position": "bottom",
})
```

##### Variant B: Move Relative to Another Rule (`"before"` or `"after"`)
```python
# Place new rule immediately ahead of an existing rule
client.move(Firewall.RULES_IPV4, {
    "id": "rule-web-traffic",
    "position": "before",
    "targetRule": "rule-general-outbound",
})
```

[↑ Back to Quick Navigation](#quick-navigation) &nbsp;•&nbsp; [↑ Back to Top](#top)

---

<a id="6-test_connection"></a>
### 6. `client.test_connection()`

Execute an on-demand connectivity and credential verification test against an external authentication server, SMS gateway, or third-party threat feed.

```python
client.test_connection(
    endpoint: str,
    data: Mapping[str, Any] | None = None,
    *,
    params: Mapping[str, Any] | None = None,
) -> Any
```

> [!NOTE]
> `client.test_connection(endpoint, data=data, params=params)` directly issues an HTTP POST request to `f"{endpoint.rstrip('/')}/test-connection"`.

#### Parameters

| Parameter | Type | Default | Description |
|---|---|:---:|---|
| `endpoint` | `str` | *Required* | Server or service endpoint constant (see supported list below). |
| `data` | `Mapping[str, Any] \| None` | `None` | Optional server parameters (e.g. host, port, credentials). |
| `params` | `Mapping[str, Any] \| None` | `None` | Optional query parameters. |

#### Supported Service Endpoints

| Domain | Supported Endpoints | Description |
|---|---|---|
| **Active Directory** | `Authentication.SERVERS_ACTIVE_DIRECTORY` | Test Active Directory domain controller authentication & LDAP bind |
| **LDAP** | `Authentication.SERVERS_LDAP` | Test OpenLDAP / directory server connection and search base |
| **RADIUS** | `Authentication.SERVERS_RADIUS` | Test RADIUS server port reachability and shared secret |
| **TACACS+** | `Authentication.SERVERS_TACACS` | Test TACACS+ server connection and admin authorization |
| **Generic IdP SSO** | `Authentication.SERVERS_GENERIC_IDP_SSO` | Test SAML / OIDC identity provider token endpoint |
| **SMS Gateway** | `Authentication.GUEST_USER_SETTINGS_SMS_GATEWAYS` | Test guest user OTP SMS delivery gateway |
| **Threat Feed** | `ActiveThreatResponse.THIRDPARTY_THREAT_FEEDS` | Test third-party threat feed URL reachability and format |

#### Example Usage

```python
# Test connection to an Active Directory domain controller
result = client.test_connection(
    Authentication.SERVERS_ACTIVE_DIRECTORY,
    data={
        "serverIp": "10.0.1.10",
        "port": 389,
        "netbiosName": "CORP",
        "domainName": "corp.local",
    },
)
print("AD Test Result:", result)

# Test connection to an LDAP server
result = client.test_connection(
    Authentication.SERVERS_LDAP,
    data={"serverIp": "10.0.2.20", "port": 636},
)
```

[↑ Back to Quick Navigation](#quick-navigation) &nbsp;•&nbsp; [↑ Back to Top](#top)

---

<a id="low-level-lifecycle-methods"></a>
## 🔌 Low-Level Transport & Session Lifecycle

Methods for direct HTTP protocol interaction, custom header injection, unmodeled endpoint execution, and explicit socket disposal.

<a id="7-request"></a>
### 7. `client.request()`

Send a raw HTTP request directly to the firewall. Used for endpoints not covered by higher-level methods or for custom HTTP debugging.

```python
client.request(
    method: str,
    endpoint: str,
    *,
    params: Mapping[str, Any] | None = None,
    json_data: Any = None,
    headers: Mapping[str, str] | None = None,
) -> Any
```

#### Features:
- Automatically prefixes the firewall base URL (`https://{host}:{port}/api/firewall-config/v1/`).
- Strips `None` values from `params`.
- Handles `204 No Content` gracefully by returning `None`.
- Parses JSON responses automatically or returns raw text if content is not JSON.
- Evaluates HTTP response codes and raises appropriate `SFOSApiError` subclasses.

#### Supported Variants

##### Variant A: Low-Level GET with Custom Headers
```python
status = client.request(
    "GET",
    "system/status",
    headers={"X-Custom-Tracking": "audit-run-42"},
)
```

##### Variant B: Direct Custom POST / PUT
```python
raw_resp = client.request(
    "POST",
    "/network/custom-endpoint",
    json_data={"setting": True},
)
```

[↑ Back to Quick Navigation](#quick-navigation) &nbsp;•&nbsp; [↑ Back to Top](#top)

---

<a id="8-close"></a>
### 8. `client.close()`

Explicitly close the underlying `httpx.Client` connection pool.

```python
client = SFOSClient("192.168.1.1", "your-api-key", verify_ssl=False)
try:
    data = client.read(Network.ZONES)
finally:
    client.close()
```

[↑ Back to Quick Navigation](#quick-navigation) &nbsp;•&nbsp; [↑ Back to Top](#top)

---

<a id="exception-hierarchy"></a>
## 🚨 Exception Hierarchy

All errors raised by `SFOSClient` derive from `SFOSApiError`:

```text
SFOSApiError
 ├── BadRequestError         (HTTP 400)
 ├── AuthenticationError     (HTTP 401)
 ├── AuthorizationError      (HTTP 403)
 ├── NotFoundError           (HTTP 404)
 ├── ConflictError           (HTTP 409)
 └── InternalServerError     (HTTP 500+)
      └── UnexpectedError
```

### Exception Attributes

Every `SFOSApiError` instance exposes structured attributes extracted directly from the firewall's error payload:

| Attribute | Type | Description |
|---|---|---|
| `e.message` | `str` | Human-readable error description. |
| `e.status_code` | `int \| None` | HTTP response status code (e.g. `404`, `409`). |
| `e.code` | `str \| int \| None` | SFOS-specific internal error code returned by the firewall. |
| `e.error` | `str \| None` | Short error identifier or category from firewall response. |
| `e.response_body` | `Any` | Full decoded JSON response body (or raw text) for deep debugging. |

### HTTP Status Code Mapping Table

| Status Code | Exception Class | Typical Cause |
|---|---|---|
| **`400`** | `BadRequestError` | Invalid JSON syntax, missing required fields, or value schema validation failure. |
| **`401`** | `AuthenticationError` | Missing, expired, or invalid API key. |
| **`403`** | `AuthorizationError` | API key lacks administrator permissions for the requested domain. |
| **`404`** | `NotFoundError` | The requested host, rule, or sub-resource does not exist on the firewall. |
| **`409`** | `ConflictError` | Resource with the same name already exists or is referenced by an active policy. |
| **`500+`** | `InternalServerError` | Firewall internal system error, database timeout, or service unavailability. |
| **`500`** | `UnexpectedError` | Specific subtype for unexpected server-side conditions. |

### Recommended Error Handling Pattern

```python
from sfos_api import (
    BadRequestError,
    ConflictError,
    NotFoundError,
    SFOSApiError,
    SFOSClient,
    Network,
)

with SFOSClient("192.168.1.1", "api-key", verify_ssl=False) as client:
    try:
        client.create(Network.ADDRESSES_IPV4, {
            "name": "Branch_Gateway",
            "ipAddress": "10.0.0.1",
            "type": "IPv4",
        })
    except ConflictError as e:
        print(f"⚠️ Resource already exists (Code: {e.code}): {e}")
        # Graceful fallback: update existing resource instead
        client.update(Network.ADDRESSES_IPV4, "Branch_Gateway", data={"ipAddress": "10.0.0.1"})
    except BadRequestError as e:
        print(f"❌ Invalid parameters: {e}")
        print("Firewall response:", e.response_body)
    except NotFoundError as e:
        print(f"❌ Target not found: {e}")
    except SFOSApiError as e:
        print(f"❌ General SFOS API error [HTTP {e.status_code}]: {e}")
```

[↑ Back to Quick Navigation](#quick-navigation) &nbsp;•&nbsp; [↑ Back to Top](#top)
