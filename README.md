# SFOS API - Sophos Firewall OS REST API Client

[![Python 3.11+](https://img.shields.io/badge/Python-3.11%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![Development Status: Beta](https://img.shields.io/badge/Status-Beta%200.5.0-orange.svg)](https://pypi.org/project/sfos-api/)

A  Python 3.11+ client for Sophos Firewall OS (SFOS) REST API using domain-grouped `StrEnum` classes.

---

## 🌟 Key Architecture & Features

`sfos_api` offers a lightweight architecture designed for developers who want IDE auto-completion and type safety without the overhead of heavy metadata classes.

| Feature | SFOS API (`sfos-api`) |
|---|---|
| **Architecture** | **Domain `StrEnum` classes** |
| **Endpoint Registry** | **29 Domain Classes** (`Network.*`, `Firewall.*`, `Nat.*`, etc.) |
| **Endpoint Types** | **Native `str` singletons via `StrEnum`** |
| **Runtime Overhead** | **Zero runtime overhead (strings)** |
| **IDE Autocomplete** | **Organized by domain: type `Firewall.` or `Network.`** |
| **JSON Serialization** | **Directly serializable as `str`** |
| **Core CRUD & Actions** | **`create` (resources & actions), `read`, `update`, `delete`** |
| **Convenience Wrappers** | **`move` (rule priority), `test_connection` (service diagnostics)** |
| **Low-Level & Lifecycle** | **`request` (custom HTTP), `close` (session teardown)** |
| **Auto-Pagination** | **Transparent multi-page fetch** |


---

## 📦 Installation

```bash
pip install sfos-api
```

Or install in editable mode for local development:

```bash
git clone https://github.com/Mitko-n/sfos_api.git
cd sfos_api
pip install -e .
```

---

## 🚀 Quick Start

```python
from sfos_api import SFOSClient, Network, Firewall, Nat, Authentication

# Initialize client
with SFOSClient("192.168.1.1", "your-api-key", verify_ssl=False) as client:
    # --- 1. Core CRUD Operations ---
    # Read zones (auto-paginated)
    zones = client.read(Network.ZONES)
    print(f"Total zones: {len(zones['items'])}")

    # Read firewall rules (custom page size)
    rules = client.read(Firewall.RULES_IPV4, pageSize=25)

    # Create a new host
    client.create(Network.ADDRESSES_IPV4, {"name": "Branch_Router", "ipAddress": "10.200.1.1", "type": "IPv4"})

    # Update host description (RFC 7396 JSON Merge Patch)
    client.update(Network.ADDRESSES_IPV4, "Branch_Router", data={"description": "Primary edge gateway"})

    # --- 2. Convenience Wrappers (Rule Reordering & Service Testing) ---
    # Move a firewall rule to the top of the rulebase
    client.move(Firewall.RULES_IPV4, {"id": "rule-42", "position": "top"})

    # Test LDAP server connectivity and credentials
    client.test_connection(
        Authentication.SERVERS_LDAP,
        data={"serverAddress": "10.0.10.5", "port": 389},
    )

    # --- 3. Resource Cleanup (Delete) ---
    client.delete(Network.ADDRESSES_IPV4, "Branch_Router")
```

---

## 📚 Domain StrEnum Organization

All 187 REST API endpoints are grouped into 29 domain classes:

| Domain Class | Description | Example Endpoints |
|---|---|---|
| `Network` | Interfaces, IP addresses, zones, DNS, DHCP | `Network.ZONES`, `Network.ADDRESSES_IPV4`, `Network.INTERFACES_NETWORK_INTERFACES` |
| `Firewall` | IPv4 & IPv6 firewall rules and policy ordering | `Firewall.RULES_IPV4`, `Firewall.RULES_IPV6` |
| `Nat` | Source and destination NAT rules | `Nat.RULES_IPV4`, `Nat.RULES_IPV6` |
| `Authentication` | Users, groups, AD, LDAP, RADIUS, MFA | `Authentication.SERVERS_ACTIVE_DIRECTORY`, `Authentication.SERVERS_LDAP` |
| `Routing` | Static unicast/multicast routes, WAN gateways | `Routing.STATIC_UNICAST_ROUTES_IPV4`, `Routing.GATEWAYS_WAN_IPV4` |
| `SdWan` | Policy-based SD-WAN routing paths | `SdWan.ROUTES_IPV4`, `SdWan.ROUTES_IPV6` |
| `TlsInspection` | SSL/TLS decryption and inspection rules | `TlsInspection.RULES_IPV4`, `TlsInspection.DECRYPTION_PROFILES` |
| `SophosCentral` | Central management, registration, and status | `SophosCentral.REGISTER`, `SophosCentral.STATUS` |
| `System` | Backups, firmware, hotfixes, pattern updates | `System.BACKUP_SETTINGS`, `System.SECURITY_UPDATES` |
| ... and 20 more! | IPS, WAF, Wireless, VPN, DoS, Malware | See [Endpoints Reference](./docs/endpoints_reference.md) |

---

## 📖 Documentation Index

- [**API Reference**](./docs/api_reference.md) — Comprehensive technical reference: core CRUD methods (`read`, `create`, `update`, `delete`), dedicated convenience wrappers (`move`, `test_connection`), low-level transport (`request`, `close`), and the exception hierarchy.

- [**Endpoints Reference**](./docs/endpoints_reference.md) — Complete catalog of all 29 domains and 187 endpoint constants.
- [**Architecture & UML Specification**](./docs/architecture.md) — System architecture, Class, Use Case, Sequence, Activity, and State UML diagrams with Mermaid.

---

## 🧪 Running Tests

```bash
pytest tests/ -v
```

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.
