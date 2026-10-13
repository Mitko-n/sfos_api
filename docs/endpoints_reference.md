# SFOS API - Endpoints Reference <a id="top"></a>

[![Python 3.11+](https://img.shields.io/badge/Python-3.11%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](../LICENSE)
[![Development Status: Beta 0.5.0](https://img.shields.io/badge/Status-Beta%200.5.0-orange.svg)](https://pypi.org/project/sfos-api/)

Complete catalog of all **29 domain StrEnum classes** and **187 endpoint constants** in `sfos-api`.

### 📊 Column Schema Legend
- **Constant Name**: Enum member under `sfos_api` (e.g. `Firewall.RULES_IPV4`).
- **REST API Path**: HTTP resource path on Sophos Firewall OS WebAdmin REST API.
- **Supported Methods**: HTTP verbs (`GET`, `POST`, `PATCH`, `DELETE`) defined in OpenAPI.
- **CRUD Methods**: Corresponding `SFOSClient` methods (`read`, `create`, `update`, `delete`, `move`, `test_connection`).
- **CRUD Signatures**: Python method invocation signatures showing exact arguments (`endpoint`, `id_or_name`, `data`).
- **Parameters**: Path parameters (item ID or route param), query parameters (`nameContains` or `nameNotEquals` [mutually exclusive], `type` enums, `page`, `pageSize`), and body requirements.
- **Description**: Technical description of the resource or operation aligned with `firewall_config_openapi.yaml`.

---

## 🧭 Quick Navigation <a id="quick-navigation"></a>

| Category | Total Domains | Total Endpoints | Jump Link |
|---|:---:|:---:|---|
| [**🛡️ 1. Security, Policies & Inspection**](#1-security-policies-inspection) | 7 | 19 | [Jump to Security Section](#1-security-policies-inspection) |
| [**🌐 2. Network, Routing & Infrastructure**](#2-network-routing-infrastructure) | 6 | 52 | [Jump to Network Section](#2-network-routing-infrastructure) |
| [**🔑 3. Identity, Authentication & Certificates**](#3-identity-authentication-certificates) | 2 | 51 | [Jump to Identity Section](#3-identity-authentication-certificates) |
| [**🔒 4. VPN & Remote Connectivity**](#4-vpn-remote-connectivity) | 2 | 12 | [Jump to VPN Section](#4-vpn-remote-connectivity) |
| [**🦠 5. Threat Protection & Content Security**](#5-threat-protection-content-security) | 6 | 21 | [Jump to Threat Protection Section](#5-threat-protection-content-security) |
| [**⚙️ 6. System, Administration & Observability**](#6-system-administration-observability) | 6 | 32 | [Jump to System Section](#6-system-administration-observability) |
| **Total** | **29** | **187** | |

### 🔤 Alphabetical Index
[A](#aclexceptionrules) • [C](#certificate) • [D](#denialofservice) • [F](#firewall) • [I](#intrusionprevention) • [L](#logging) • [M](#malwareprotection) • [N](#network) • [R](#routing) • [S](#sdwan) • [T](#tlsinspection) • [W](#waf) • [Z](#zerodayprotection)

---

## 📑 Table of Domains <a id="table-of-domains"></a>

| Domain Class | Category | Endpoints | Scope & Primary Resources | Quick Import |
|---|---|:---:|---|---|
| [**`AclExceptionRules`**](#aclexceptionrules) | 🛡️ Security | 2 | IPv4 and IPv6 ACL exception bypass rules | `from sfos_api import AclExceptionRules` |
| [**`ActiveThreatResponse`**](#activethreatresponse) | 🦠 Threat Protection | 5 | MDR feeds, Sophos X-Ops, 3rd-party feeds & sync | `from sfos_api import ActiveThreatResponse` |
| [**`Administration`**](#administration) | ⚙️ System | 8 | Access permissions, profiles, API, portal, schedules | `from sfos_api import Administration` |
| [**`Application`**](#application) | 🦠 Threat Protection | 5 | App definitions, categories, attributes, policy filters | `from sfos_api import Application` |
| [**`Authentication`**](#authentication) | 🔑 Identity | 43 | Users, groups, AD/LDAP/RADIUS/TACACS, TOTP/MFA, SSO | `from sfos_api import Authentication` |
| [**`Certificate`**](#certificate) | 🔑 Identity | 8 | CAs, internal/external certificates, CSRs, CRLs | `from sfos_api import Certificate` |
| [**`DenialOfService`**](#denialofservice) | 🛡️ Security | 4 | DoS flood attack protection, thresholds, telemetry | `from sfos_api import DenialOfService` |
| [**`Firewall`**](#firewall) | 🛡️ Security | 2 | IPv4 and IPv6 stateful traffic filtering rules | `from sfos_api import Firewall` |
| [**`FirewallHealthCheck`**](#firewallhealthcheck) | 🛡️ Security | 2 | Firewall health check policies and metric summaries | `from sfos_api import FirewallHealthCheck` |
| [**`IntrusionPrevention`**](#intrusionprevention) | 🛡️ Security | 4 | IPS policies, custom signatures, engine settings | `from sfos_api import IntrusionPrevention` |
| [**`IpsecVpn`**](#ipsecvpn) | 🔒 VPN | 7 | Site-to-site (policy/route-based), profiles, failover | `from sfos_api import IpsecVpn` |
| [**`Logging`**](#logging) | ⚙️ System | 7 | Syslog servers, Central reporting, log viewer, events | `from sfos_api import Logging` |
| [**`MalwareProtection`**](#malwareprotection) | 🦠 Threat Protection | 1 | Global anti-malware scanning engine settings | `from sfos_api import MalwareProtection` |
| [**`Monitoring`**](#monitoring) | ⚙️ System | 4 | NetFlow collectors, SNMP agents, communities, users | `from sfos_api import Monitoring` |
| [**`Nat`**](#nat) | 🛡️ Security | 2 | IPv4 and IPv6 NAT (SNAT, DNAT, 1:1) rules | `from sfos_api import Nat` |
| [**`Network`**](#network) | 🌐 Network | 33 | Interfaces, IP/FQDN/MAC hosts, groups, DHCP, DNS | `from sfos_api import Network` |
| [**`Notification`**](#notification) | ⚙️ System | 1 | Alert notifications and administrative recipients | `from sfos_api import Notification` |
| [**`Routing`**](#routing) | 🌐 Network | 10 | Gateways (custom/WAN), static unicast/multicast routes | `from sfos_api import Routing` |
| [**`SdWan`**](#sdwan) | 🌐 Network | 2 | Policy-based SD-WAN routing paths for IPv4 and IPv6 | `from sfos_api import SdWan` |
| [**`SophosCentral`**](#sophoscentral) | ⚙️ System | 4 | Sophos Central registration, synchronization, status | `from sfos_api import SophosCentral` |
| [**`SpoofProtection`**](#spoofprotection) | 🌐 Network | 3 | IP/MAC spoof prevention and trusted MAC database | `from sfos_api import SpoofProtection` |
| [**`SslVpn`**](#sslvpn) | 🔒 VPN | 5 | SSL VPN remote access policies & clientless bookmarks | `from sfos_api import SslVpn` |
| [**`System`**](#system) | ⚙️ System | 4 | Backup, hotfixes, security patterns, firmware updates | `from sfos_api import System` |
| [**`TlsInspection`**](#tlsinspection) | 🛡️ Security | 3 | TLS/SSL decryption profiles, inspection rules, engine | `from sfos_api import TlsInspection` |
| [**`TrafficShaping`**](#trafficshaping) | 🌐 Network | 2 | QoS bandwidth allocation policies and limits | `from sfos_api import TrafficShaping` |
| [**`Waf`**](#waf) | 🦠 Threat Protection | 4 | Web Application Firewall protection policies & servers | `from sfos_api import Waf` |
| [**`Web`**](#web) | 🦠 Threat Protection | 8 | Web filtering policies, categories, exceptions, URLs | `from sfos_api import Web` |
| [**`Wireless`**](#wireless) | 🌐 Network | 3 | Wireless hotspots, guest voucher generation, portals | `from sfos_api import Wireless` |
| [**`ZeroDayProtection`**](#zerodayprotection) | 🦠 Threat Protection | 1 | Sandstorm cloud sandboxing analysis settings | `from sfos_api import ZeroDayProtection` |

<a id="1-security-policies-inspection"></a><a id="1-security-policies--inspection"></a>
## 1. Security, Policies & Inspection

🛡️ Security policies, rulebases, NAT translation, attack prevention, and deep packet inspection.

### <a id="aclexceptionrules"></a>`AclExceptionRules`

Import: `from sfos_api import AclExceptionRules`

| Constant Name | REST API Path | Supported Methods | CRUD Methods | CRUD Signatures | Parameters | Description |
|---|---|:---:|:---:|---|---|---|
| `AclExceptionRules.IPV4` | `/acl-exception-rules/ipv4` | `GET`, `POST`, `PATCH`, `DELETE` | `read`, `create`, `update`, `delete` | `client.read(endpoint, [id_or_name])`<br>`client.create(endpoint, data)`<br>`client.update(endpoint, id_or_name, data)`<br>`client.delete(endpoint, id_or_name)` | Path: `id_or_name` *(item)*; Query: `nameContains` or `nameNotEquals` | IPv4 ACL exception / bypass rulebase |
| `AclExceptionRules.IPV6` | `/acl-exception-rules/ipv6` | `GET`, `POST`, `PATCH`, `DELETE` | `read`, `create`, `update`, `delete` | `client.read(endpoint, [id_or_name])`<br>`client.create(endpoint, data)`<br>`client.update(endpoint, id_or_name, data)`<br>`client.delete(endpoint, id_or_name)` | Path: `id_or_name` *(item)*; Query: `nameContains` or `nameNotEquals` | IPv6 ACL exception / bypass rulebase |

[↑ Back to Table of Domains](#table-of-domains) &nbsp;•&nbsp; [↑ Back to Top](#top)

---

### <a id="denialofservice"></a>`DenialOfService`

Import: `from sfos_api import DenialOfService`

| Constant Name | REST API Path | Supported Methods | CRUD Methods | CRUD Signatures | Parameters | Description |
|---|---|:---:|:---:|---|---|---|
| `DenialOfService.ATTACKS_BY_FLOOD_ATTACK_TYPE` | `/denial-of-service/attacks/{floodAttackType}` | `GET` | `read` | `client.read(endpoint, id_or_name)` | Path: `floodAttackType` *(required)* | Flood attack telemetry filtered by attack type (SYN, UDP, ICMP) |
| `DenialOfService.ATTACKS_SUMMARY` | `/denial-of-service/attacks/summary` | `GET` | `read` | `client.read(endpoint)` | None *(singleton)* | Aggregate statistical summary of detected DoS attacks |
| `DenialOfService.POLICIES` | `/denial-of-service/policies` | `GET`, `POST`, `DELETE` | `read`, `create`, `delete` | `client.read(endpoint, [id_or_name])`<br>`client.create(endpoint, data)`<br>`client.delete(endpoint, id_or_name)` | Path: `id_or_name` *(item)*; Query: `nameContains` or `nameNotEquals` | DoS protection rate-limiting and threshold policies |
| `DenialOfService.SETTINGS` | `/denial-of-service/settings` | `GET`, `PATCH` | `read`, `update` | `client.read(endpoint)`<br>`client.update(endpoint, data=data)` | Body: JSON payload | Global DoS inspection and dropping settings |

[↑ Back to Table of Domains](#table-of-domains) &nbsp;•&nbsp; [↑ Back to Top](#top)

---

### <a id="firewall"></a>`Firewall`

Import: `from sfos_api import Firewall`

| Constant Name | REST API Path | Supported Methods | CRUD Methods | CRUD Signatures | Parameters | Description |
|---|---|:---:|:---:|---|---|---|
| `Firewall.RULES_IPV4` | `/firewall/rules/ipv4` | `GET`, `POST`, `PATCH`, `DELETE` | `read`, `create`, `update`, `delete`, `move` | `client.read(endpoint, [id_or_name])`<br>`client.create(endpoint, data)`<br>`client.update(endpoint, id_or_name, data)`<br>`client.delete(endpoint, id_or_name)`<br>`client.move(endpoint, data)` | Path: `id_or_name` *(item)*; Query: `nameContains` or `nameNotEquals` | IPv4 stateful firewall rules and policy ordering |
| `Firewall.RULES_IPV6` | `/firewall/rules/ipv6` | `GET`, `POST`, `PATCH`, `DELETE` | `read`, `create`, `update`, `delete`, `move` | `client.read(endpoint, [id_or_name])`<br>`client.create(endpoint, data)`<br>`client.update(endpoint, id_or_name, data)`<br>`client.delete(endpoint, id_or_name)`<br>`client.move(endpoint, data)` | Path: `id_or_name` *(item)*; Query: `nameContains` or `nameNotEquals` | IPv6 stateful firewall rules and policy ordering |

[↑ Back to Table of Domains](#table-of-domains) &nbsp;•&nbsp; [↑ Back to Top](#top)

---

### <a id="firewallhealthcheck"></a>`FirewallHealthCheck`

Import: `from sfos_api import FirewallHealthCheck`

| Constant Name | REST API Path | Supported Methods | CRUD Methods | CRUD Signatures | Parameters | Description |
|---|---|:---:|:---:|---|---|---|
| `FirewallHealthCheck.POLICIES` | `/firewall-health-check/policies` | `GET` | `read` | `client.read(endpoint)` | None *(singleton)* | Gateway and link health-check probe policies |
| `FirewallHealthCheck.POLICIES_SUMMARY` | `/firewall-health-check/policies/summary` | `GET` | `read` | `client.read(endpoint)` | None *(singleton)* | Real-time status summary of active health checks |

[↑ Back to Table of Domains](#table-of-domains) &nbsp;•&nbsp; [↑ Back to Top](#top)

---

### <a id="intrusionprevention"></a>`IntrusionPrevention`

Import: `from sfos_api import IntrusionPrevention`

| Constant Name | REST API Path | Supported Methods | CRUD Methods | CRUD Signatures | Parameters | Description |
|---|---|:---:|:---:|---|---|---|
| `IntrusionPrevention.CUSTOM_SIGNATURES` | `/intrusion-prevention/custom-signatures` | `GET`, `POST`, `PATCH`, `DELETE` | `read`, `create`, `update`, `delete` | `client.read(endpoint, [id_or_name])`<br>`client.create(endpoint, data)`<br>`client.update(endpoint, id_or_name, data)`<br>`client.delete(endpoint, id_or_name)` | Path: `id_or_name` *(item)*; Query: `page`, `pageSize` | User-defined custom IPS pattern signatures |
| `IntrusionPrevention.POLICIES` | `/intrusion-prevention/policies` | `GET`, `POST`, `PATCH`, `DELETE` | `read`, `create`, `update`, `delete` | `client.read(endpoint, [id_or_name])`<br>`client.create(endpoint, data)`<br>`client.update(endpoint, id_or_name, data)`<br>`client.delete(endpoint, id_or_name)` | Path: `id_or_name` *(item)*; Query: `page`, `pageSize` | IPS filtering policies and protection categories |
| `IntrusionPrevention.SETTINGS` | `/intrusion-prevention/settings` | `GET`, `PATCH` | `read`, `update` | `client.read(endpoint)`<br>`client.update(endpoint, data=data)` | Body: JSON payload | Global IPS engine configuration and fail-open settings |
| `IntrusionPrevention.SIGNATURE_ATTRIBUTES` | `/intrusion-prevention/signature-attributes` | `GET` | `read` | `client.read(endpoint)` | None *(singleton)* | Signature attribute metadata (severity, target, platform) |

[↑ Back to Table of Domains](#table-of-domains) &nbsp;•&nbsp; [↑ Back to Top](#top)

---

### <a id="nat"></a>`Nat`

Import: `from sfos_api import Nat`

| Constant Name | REST API Path | Supported Methods | CRUD Methods | CRUD Signatures | Parameters | Description |
|---|---|:---:|:---:|---|---|---|
| `Nat.RULES_IPV4` | `/nat/rules/ipv4` | `GET`, `POST`, `PATCH`, `DELETE` | `read`, `create`, `update`, `delete`, `move` | `client.read(endpoint, [id_or_name])`<br>`client.create(endpoint, data)`<br>`client.update(endpoint, id_or_name, data)`<br>`client.delete(endpoint, id_or_name)`<br>`client.move(endpoint, data)` | Path: `id_or_name` *(item)*; Query: `nameContains` or `nameNotEquals` | IPv4 SNAT, DNAT, and full NAT translation rules |
| `Nat.RULES_IPV6` | `/nat/rules/ipv6` | `GET`, `POST`, `PATCH`, `DELETE` | `read`, `create`, `update`, `delete`, `move` | `client.read(endpoint, [id_or_name])`<br>`client.create(endpoint, data)`<br>`client.update(endpoint, id_or_name, data)`<br>`client.delete(endpoint, id_or_name)`<br>`client.move(endpoint, data)` | Path: `id_or_name` *(item)*; Query: `nameContains` or `nameNotEquals` | IPv6 NAT translation rules and prefix mappings |

[↑ Back to Table of Domains](#table-of-domains) &nbsp;•&nbsp; [↑ Back to Top](#top)

---

### <a id="tlsinspection"></a>`TlsInspection`

Import: `from sfos_api import TlsInspection`

| Constant Name | REST API Path | Supported Methods | CRUD Methods | CRUD Signatures | Parameters | Description |
|---|---|:---:|:---:|---|---|---|
| `TlsInspection.DECRYPTION_PROFILES` | `/tls-inspection/decryption-profiles` | `GET`, `POST`, `PATCH`, `DELETE` | `read`, `create`, `update`, `delete` | `client.read(endpoint, [id_or_name])`<br>`client.create(endpoint, data)`<br>`client.update(endpoint, id_or_name, data)`<br>`client.delete(endpoint, id_or_name)` | Path: `id_or_name` *(item)*; Query: `nameContains` or `nameNotEquals` | TLS decryption profiles, ciphers, and protocol minimums |
| `TlsInspection.RULES_IPV4` | `/tls-inspection/rules/ipv4` | `GET`, `POST`, `PATCH`, `DELETE` | `read`, `create`, `update`, `delete` | `client.read(endpoint, [id_or_name])`<br>`client.create(endpoint, data)`<br>`client.update(endpoint, id_or_name, data)`<br>`client.delete(endpoint, id_or_name)` | Path: `id_or_name` *(item)*; Query: `nameContains` or `nameNotEquals` | IPv4 SSL/TLS inspection and bypass rules |
| `TlsInspection.SETTINGS` | `/tls-inspection/settings` | `GET`, `PATCH` | `read`, `update` | `client.read(endpoint)`<br>`client.update(endpoint, data=data)` | Body: JSON payload | Global TLS engine and hardware acceleration settings |

[↑ Back to Table of Domains](#table-of-domains) &nbsp;•&nbsp; [↑ Back to Top](#top)

<a id="2-network-routing-infrastructure"></a><a id="2-network-routing--infrastructure"></a>
## 2. Network, Routing & Infrastructure

🌐 Core network configuration, physical and virtual interfaces, DHCP, DNS, IP objects, routing, and cellular WAN.

### <a id="network"></a>`Network`

Import: `from sfos_api import Network`

| Constant Name | REST API Path | Supported Methods | CRUD Methods | CRUD Signatures | Parameters | Description |
|---|---|:---:|:---:|---|---|---|
| `Network.ADDRESSES_FQDN` | `/network/addresses/fqdn` | `GET`, `POST`, `PATCH`, `DELETE` | `read`, `create`, `update`, `delete` | `client.read(endpoint, [id_or_name])`<br>`client.create(endpoint, data)`<br>`client.update(endpoint, id_or_name, data)`<br>`client.delete(endpoint, id_or_name)` | Path: `id_or_name` *(item)*; Query: `nameContains` or `nameNotEquals` | Fully Qualified Domain Name (FQDN) network host objects |
| `Network.ADDRESSES_IPV4` | `/network/addresses/ipv4` | `GET`, `POST`, `PATCH`, `DELETE` | `read`, `create`, `update`, `delete` | `client.read(endpoint, [id_or_name])`<br>`client.create(endpoint, data)`<br>`client.update(endpoint, id_or_name, data)`<br>`client.delete(endpoint, id_or_name)` | Path: `id_or_name` *(item)*; Query: `nameContains` or `nameNotEquals`, `type` (`ipv4Address`, `ipv4Network`, `ipv4Range`, `ipv4List`) | IPv4 host, network, IP range, and IP list objects |
| `Network.ADDRESSES_IPV6` | `/network/addresses/ipv6` | `GET`, `POST`, `PATCH`, `DELETE` | `read`, `create`, `update`, `delete` | `client.read(endpoint, [id_or_name])`<br>`client.create(endpoint, data)`<br>`client.update(endpoint, id_or_name, data)`<br>`client.delete(endpoint, id_or_name)` | Path: `id_or_name` *(item)*; Query: `nameContains` or `nameNotEquals`, `type` (`ipv6Address`, `ipv6Network`, `ipv6Range`, `ipv6List`) | IPv6 host, network, and IP range objects |
| `Network.ADDRESSES_MAC` | `/network/addresses/mac` | `GET`, `POST`, `PATCH`, `DELETE` | `read`, `create`, `update`, `delete` | `client.read(endpoint, [id_or_name])`<br>`client.create(endpoint, data)`<br>`client.update(endpoint, id_or_name, data)`<br>`client.delete(endpoint, id_or_name)` | Path: `id_or_name` *(item)*; Query: `nameContains` or `nameNotEquals`, `type` (`macAddress`, `macList`) | MAC address host definitions |
| `Network.ADDRESS_GROUPS_COUNTRY` | `/network/address-groups/country` | `GET`, `POST`, `PATCH`, `DELETE` | `read`, `create`, `update`, `delete` | `client.read(endpoint, [id_or_name])`<br>`client.create(endpoint, data)`<br>`client.update(endpoint, id_or_name, data)`<br>`client.delete(endpoint, id_or_name)` | Path: `id_or_name` *(item)*; Query: `nameContains` or `nameNotEquals` | GeoIP country and regional location groups |
| `Network.ADDRESS_GROUPS_FQDN` | `/network/address-groups/fqdn` | `GET`, `POST`, `PATCH`, `DELETE` | `read`, `create`, `update`, `delete` | `client.read(endpoint, [id_or_name])`<br>`client.create(endpoint, data)`<br>`client.update(endpoint, id_or_name, data)`<br>`client.delete(endpoint, id_or_name)` | Path: `id_or_name` *(item)*; Query: `nameContains` or `nameNotEquals` | Groupings of FQDN host objects |
| `Network.ADDRESS_GROUPS_IPV4` | `/network/address-groups/ipv4` | `GET`, `POST`, `PATCH`, `DELETE` | `read`, `create`, `update`, `delete` | `client.read(endpoint, [id_or_name])`<br>`client.create(endpoint, data)`<br>`client.update(endpoint, id_or_name, data)`<br>`client.delete(endpoint, id_or_name)` | Path: `id_or_name` *(item)*; Query: `nameContains` or `nameNotEquals` | Groupings of IPv4 host and network objects |
| `Network.ADDRESS_GROUPS_IPV6` | `/network/address-groups/ipv6` | `GET`, `POST`, `PATCH`, `DELETE` | `read`, `create`, `update`, `delete` | `client.read(endpoint, [id_or_name])`<br>`client.create(endpoint, data)`<br>`client.update(endpoint, id_or_name, data)`<br>`client.delete(endpoint, id_or_name)` | Path: `id_or_name` *(item)*; Query: `nameContains` or `nameNotEquals` | Groupings of IPv6 host and network objects |
| `Network.CELLULAR_WAN_CONNECT_MODEM` | `/network/cellular-wan/connect-modem` | `POST` | `create` | `client.create(endpoint)` | None *(singleton)* | Action: Connect cellular WAN modem interface |
| `Network.CELLULAR_WAN_DISCONNECT_MODEM` | `/network/cellular-wan/disconnect-modem` | `POST` | `create` | `client.create(endpoint)` | None *(singleton)* | Action: Disconnect cellular WAN modem interface |
| `Network.CELLULAR_WAN_MODEM_SETTINGS` | `/network/cellular-wan/modem-settings` | `GET`, `PATCH` | `read`, `update` | `client.read(endpoint)`<br>`client.update(endpoint, data=data)` | Body: JSON payload | Cellular WAN modem configuration (APN, PIN, auth) |
| `Network.CELLULAR_WAN_MODEM_STATUS` | `/network/cellular-wan/modem-status` | `GET` | `read` | `client.read(endpoint)` | None *(singleton)* | Real-time signal strength, carrier, and link status |
| `Network.CELLULAR_WAN_RECOMMENDED_MODEM_SETTINGS` | `/network/cellular-wan/recommended-modem-settings` | `POST` | `create` | `client.create(endpoint)` | None *(singleton)* | Carrier profile presets and recommended parameters |
| `Network.CELLULAR_WAN_RESET_MODEM` | `/network/cellular-wan/reset-modem` | `POST` | `create` | `client.create(endpoint)` | None *(singleton)* | Action: Power cycle or soft reset cellular modem |
| `Network.CELLULAR_WAN_SETTINGS` | `/network/cellular-wan/settings` | `GET`, `PATCH` | `read`, `update` | `client.read(endpoint)`<br>`client.update(endpoint, data=data)` | Body: JSON payload | General cellular WAN daemon configuration |
| `Network.DHCP_RELAYS_IPV4` | `/network/dhcp/relays/ipv4` | `GET`, `POST`, `PATCH`, `DELETE` | `read`, `create`, `update`, `delete` | `client.read(endpoint, [id_or_name])`<br>`client.create(endpoint, data)`<br>`client.update(endpoint, id_or_name, data)`<br>`client.delete(endpoint, id_or_name)` | Path: `id_or_name` *(item)*; Query: `nameContains`, `nameNotEquals` | IPv4 DHCP relay forwarders |
| `Network.DHCP_RELAYS_IPV6` | `/network/dhcp/relays/ipv6` | `GET`, `POST`, `PATCH`, `DELETE` | `read`, `create`, `update`, `delete` | `client.read(endpoint, [id_or_name])`<br>`client.create(endpoint, data)`<br>`client.update(endpoint, id_or_name, data)`<br>`client.delete(endpoint, id_or_name)` | Path: `id_or_name` *(item)*; Query: `nameContains`, `nameNotEquals` | IPv6 DHCP relay forwarders |
| `Network.DHCP_SERVER_SERVERS_IPV4` | `/network/dhcp/server/servers/ipv4` | `GET`, `POST`, `PATCH`, `DELETE` | `read`, `create`, `update`, `delete` | `client.read(endpoint, [id_or_name])`<br>`client.create(endpoint, data)`<br>`client.update(endpoint, id_or_name, data)`<br>`client.delete(endpoint, id_or_name)` | Path: `id_or_name` *(item)*; Query: `nameContains`, `nameNotEquals` | IPv4 DHCP server scope configurations |
| `Network.DHCP_SERVER_SERVERS_IPV6` | `/network/dhcp/server/servers/ipv6` | `GET`, `POST`, `PATCH`, `DELETE` | `read`, `create`, `update`, `delete` | `client.read(endpoint, [id_or_name])`<br>`client.create(endpoint, data)`<br>`client.update(endpoint, id_or_name, data)`<br>`client.delete(endpoint, id_or_name)` | Path: `id_or_name` *(item)*; Query: `nameContains`, `nameNotEquals` | IPv6 DHCP server scope configurations |
| `Network.DHCP_SERVER_SETTINGS_IPV4` | `/network/dhcp/server/settings/ipv4` | `GET`, `PATCH` | `read`, `update` | `client.read(endpoint)`<br>`client.update(endpoint, data=data)` | Body: JSON payload | Global DHCP daemon settings for IPv4 |
| `Network.DNS_HOST_ENTRIES` | `/network/dns/host-entries` | `GET`, `POST`, `PATCH`, `DELETE` | `read`, `create`, `update`, `delete` | `client.read(endpoint, [id_or_name])`<br>`client.create(endpoint, data)`<br>`client.update(endpoint, id_or_name, data)`<br>`client.delete(endpoint, id_or_name)` | Path: `id_or_name` *(item)*; Query: `nameContains` or `nameNotEquals` | Static DNS host mappings (A, AAAA, PTR records) |
| `Network.DNS_PROTECTION_STATUS` | `/network/dns/protection/status` | `GET` | `read` | `client.read(endpoint)` | None *(singleton)* | DNS threat protection status and telemetry |
| `Network.DNS_REQUEST_ROUTES` | `/network/dns/request-routes` | `GET`, `POST`, `PATCH`, `DELETE` | `read`, `create`, `update`, `delete` | `client.read(endpoint, [id_or_name])`<br>`client.create(endpoint, data)`<br>`client.update(endpoint, id_or_name, data)`<br>`client.delete(endpoint, id_or_name)` | Path: `id_or_name` *(item)*; Query: `nameContains` or `nameNotEquals` | Conditional DNS request routing by domain |
| `Network.DNS_SETTINGS` | `/network/dns/settings` | `GET`, `PATCH` | `read`, `update` | `client.read(endpoint)`<br>`client.update(endpoint, data=data)` | Body: JSON payload | Primary, secondary, and upstream DNS servers |
| `Network.INTERFACES_NETWORK_INTERFACES` | `/network/interfaces/network-interfaces` | `GET`, `POST`, `PATCH`, `DELETE` | `read`, `create`, `update`, `delete` | `client.read(endpoint, [id_or_name])`<br>`client.create(endpoint, data)`<br>`client.update(endpoint, id_or_name, data)`<br>`client.delete(endpoint, id_or_name)` | Path: `id_or_name` *(item)*; Query: `nameContains` or `nameNotEquals` | Physical, VLAN, bridge, and LAG network interfaces |
| `Network.MDNS_REFLECTOR` | `/network/mdns-reflector` | `GET`, `PATCH` | `read`, `update` | `client.read(endpoint)`<br>`client.update(endpoint, data=data)` | Body: JSON payload | Multicast DNS (mDNS) reflector across zones |
| `Network.NEIGHBORS_SETTINGS` | `/network/neighbors/settings` | `GET`, `PATCH` | `read`, `update` | `client.read(endpoint)`<br>`client.update(endpoint, data=data)` | Body: JSON payload | ARP and IPv6 neighbor discovery cache parameters |
| `Network.NEIGHBORS_STATIC_IPV4` | `/network/neighbors/static/ipv4` | `GET`, `POST`, `PATCH`, `DELETE` | `read`, `create`, `update`, `delete` | `client.read(endpoint, [id_or_name])`<br>`client.create(endpoint, data)`<br>`client.update(endpoint, id_or_name, data)`<br>`client.delete(endpoint, id_or_name)` | Path: `id_or_name` *(item)*; Query: `nameContains` or `nameNotEquals` | Static IPv4 ARP table mappings |
| `Network.NEIGHBORS_STATIC_IPV6` | `/network/neighbors/static/ipv6` | `GET`, `POST`, `PATCH`, `DELETE` | `read`, `create`, `update`, `delete` | `client.read(endpoint, [id_or_name])`<br>`client.create(endpoint, data)`<br>`client.update(endpoint, id_or_name, data)`<br>`client.delete(endpoint, id_or_name)` | Path: `id_or_name` *(item)*; Query: `nameContains` or `nameNotEquals` | Static IPv6 neighbor cache entries |
| `Network.ROUTER_ADVERTISEMENTS` | `/network/router-advertisements` | `GET`, `POST`, `PATCH`, `DELETE` | `read`, `create`, `update`, `delete` | `client.read(endpoint, [id_or_name])`<br>`client.create(endpoint, data)`<br>`client.update(endpoint, id_or_name, data)`<br>`client.delete(endpoint, id_or_name)` | Path: `id_or_name` *(item)*; Query: `nameContains` or `nameNotEquals` | IPv6 Router Advertisement (RA) daemon daemon rules |
| `Network.SERVICES` | `/network/services` | `GET`, `POST`, `PATCH`, `DELETE` | `read`, `create`, `update`, `delete` | `client.read(endpoint, [id_or_name])`<br>`client.create(endpoint, data)`<br>`client.update(endpoint, id_or_name, data)`<br>`client.delete(endpoint, id_or_name)` | Path: `id_or_name` *(item)*; Query: `nameContains` or `nameNotEquals`, `type` (`tcpOrUdp`, `ip`, `icmp`, `icmpv6`) | Custom TCP/UDP/IP protocol service definitions |
| `Network.SERVICE_GROUPS` | `/network/service-groups` | `GET`, `POST`, `PATCH`, `DELETE` | `read`, `create`, `update`, `delete` | `client.read(endpoint, [id_or_name])`<br>`client.create(endpoint, data)`<br>`client.update(endpoint, id_or_name, data)`<br>`client.delete(endpoint, id_or_name)` | Path: `id_or_name` *(item)*; Query: `nameContains` or `nameNotEquals` | Groupings of protocol service objects |
| `Network.ZONES` | `/network/zones` | `GET`, `POST`, `PATCH`, `DELETE` | `read`, `create`, `update`, `delete` | `client.read(endpoint, [id_or_name])`<br>`client.create(endpoint, data)`<br>`client.update(endpoint, id_or_name, data)`<br>`client.delete(endpoint, id_or_name)` | Path: `id_or_name` *(item)*; Query: `nameContains` or `nameNotEquals` | Security zones (LAN, WAN, DMZ, VPN, WiFi) |

[↑ Back to Table of Domains](#table-of-domains) &nbsp;•&nbsp; [↑ Back to Top](#top)

---

### <a id="routing"></a>`Routing`

Import: `from sfos_api import Routing`

| Constant Name | REST API Path | Supported Methods | CRUD Methods | CRUD Signatures | Parameters | Description |
|---|---|:---:|:---:|---|---|---|
| `Routing.GATEWAYS_CUSTOM_IPV4` | `/routing/gateways/custom/ipv4` | `GET`, `POST`, `PATCH`, `DELETE` | `read`, `create`, `update`, `delete` | `client.read(endpoint, [id_or_name])`<br>`client.create(endpoint, data)`<br>`client.update(endpoint, id_or_name, data)`<br>`client.delete(endpoint, id_or_name)` | Path: `id_or_name` *(item)*; Query: `nameContains` or `nameNotEquals` | Custom defined IPv4 next-hop gateways |
| `Routing.GATEWAYS_CUSTOM_IPV6` | `/routing/gateways/custom/ipv6` | `GET`, `POST`, `PATCH`, `DELETE` | `read`, `create`, `update`, `delete` | `client.read(endpoint, [id_or_name])`<br>`client.create(endpoint, data)`<br>`client.update(endpoint, id_or_name, data)`<br>`client.delete(endpoint, id_or_name)` | Path: `id_or_name` *(item)*; Query: `nameContains` or `nameNotEquals` | Custom defined IPv6 next-hop gateways |
| `Routing.GATEWAYS_IPV4` | `/routing/gateways/ipv4` | `GET` | `read` | `client.read(endpoint)` | Query: `nameContains` or `nameNotEquals` | Active IPv4 gateways and routing table status |
| `Routing.GATEWAYS_IPV6` | `/routing/gateways/ipv6` | `GET` | `read` | `client.read(endpoint)` | Query: `nameContains` or `nameNotEquals` | Active IPv6 gateways and routing table status |
| `Routing.GATEWAYS_WAN_IPV4` | `/routing/gateways/wan/ipv4` | `GET`, `PATCH` | `read`, `update` | `client.read(endpoint, [id_or_name])`<br>`client.update(endpoint, id_or_name, data)` | Path: `id_or_name` *(item)*; Query: `nameContains` or `nameNotEquals` | WAN uplink IPv4 gateways and failover weights |
| `Routing.GATEWAYS_WAN_IPV6` | `/routing/gateways/wan/ipv6` | `GET`, `PATCH` | `read`, `update` | `client.read(endpoint, [id_or_name])`<br>`client.update(endpoint, id_or_name, data)` | Path: `id_or_name` *(item)*; Query: `nameContains` or `nameNotEquals` | WAN uplink IPv6 gateways and failover weights |
| `Routing.STATIC_MULTICAST_ROUTES_IPV4` | `/routing/static-multicast-routes/ipv4` | `GET`, `POST`, `PATCH`, `DELETE` | `read`, `create`, `update`, `delete` | `client.read(endpoint, [id_or_name])`<br>`client.create(endpoint, data)`<br>`client.update(endpoint, id_or_name, data)`<br>`client.delete(endpoint, id_or_name)` | Path: `id_or_name` *(item)*; Query: `page`, `pageSize` | Static multicast routes for IPv4 streams |
| `Routing.STATIC_MULTICAST_SETTINGS` | `/routing/static-multicast-settings` | `GET`, `PATCH` | `read`, `update` | `client.read(endpoint)`<br>`client.update(endpoint, data=data)` | Body: JSON payload | Global multicast routing configuration |
| `Routing.STATIC_UNICAST_ROUTES_IPV4` | `/routing/static-unicast-routes/ipv4` | `GET`, `POST`, `PATCH`, `DELETE` | `read`, `create`, `update`, `delete` | `client.read(endpoint, [id_or_name])`<br>`client.create(endpoint, data)`<br>`client.update(endpoint, id_or_name, data)`<br>`client.delete(endpoint, id_or_name)` | Path: `id_or_name` *(item)*; Query: `page`, `pageSize` | Static unicast routes for IPv4 networks |
| `Routing.STATIC_UNICAST_ROUTES_IPV6` | `/routing/static-unicast-routes/ipv6` | `GET`, `POST`, `PATCH`, `DELETE` | `read`, `create`, `update`, `delete` | `client.read(endpoint, [id_or_name])`<br>`client.create(endpoint, data)`<br>`client.update(endpoint, id_or_name, data)`<br>`client.delete(endpoint, id_or_name)` | Path: `id_or_name` *(item)*; Query: `page`, `pageSize` | Static unicast routes for IPv6 networks |

[↑ Back to Table of Domains](#table-of-domains) &nbsp;•&nbsp; [↑ Back to Top](#top)

---

### <a id="sdwan"></a>`SdWan`

Import: `from sfos_api import SdWan`

| Constant Name | REST API Path | Supported Methods | CRUD Methods | CRUD Signatures | Parameters | Description |
|---|---|:---:|:---:|---|---|---|
| `SdWan.ROUTES_IPV4` | `/sd-wan/routes/ipv4` | `GET`, `POST`, `PATCH`, `DELETE` | `read`, `create`, `update`, `delete` | `client.read(endpoint, [id_or_name])`<br>`client.create(endpoint, data)`<br>`client.update(endpoint, id_or_name, data)`<br>`client.delete(endpoint, id_or_name)` | Path: `id_or_name` *(item)*; Query: `nameContains` or `nameNotEquals` | Policy-based SD-WAN routing rules for IPv4 traffic |
| `SdWan.ROUTES_IPV6` | `/sd-wan/routes/ipv6` | `GET`, `POST`, `PATCH`, `DELETE` | `read`, `create`, `update`, `delete` | `client.read(endpoint, [id_or_name])`<br>`client.create(endpoint, data)`<br>`client.update(endpoint, id_or_name, data)`<br>`client.delete(endpoint, id_or_name)` | Path: `id_or_name` *(item)*; Query: `nameContains` or `nameNotEquals` | Policy-based SD-WAN routing rules for IPv6 traffic |

[↑ Back to Table of Domains](#table-of-domains) &nbsp;•&nbsp; [↑ Back to Top](#top)

---

### <a id="spoofprotection"></a>`SpoofProtection`

Import: `from sfos_api import SpoofProtection`

| Constant Name | REST API Path | Supported Methods | CRUD Methods | CRUD Signatures | Parameters | Description |
|---|---|:---:|:---:|---|---|---|
| `SpoofProtection.SETTINGS` | `/spoof-protection/settings` | `GET`, `PATCH` | `read`, `update` | `client.read(endpoint)`<br>`client.update(endpoint, data=data)` | Body: JSON payload | IP/MAC spoof protection filters and drop behavior |
| `SpoofProtection.TRUSTED_MACS` | `/spoof-protection/trusted-macs` | `GET`, `POST`, `PATCH`, `DELETE` | `read`, `create`, `update`, `delete` | `client.read(endpoint, [id_or_name])`<br>`client.create(endpoint, data)`<br>`client.update(endpoint, id_or_name, data)`<br>`client.delete(endpoint, id_or_name)` | Path: `id_or_name` *(item)*; Query: `nameContains` or `nameNotEquals` | Database of trusted MAC/IP address pairings |
| `SpoofProtection.TRUSTED_MACS_IMPORT` | `/spoof-protection/trusted-macs/import` | `POST` | `create` | `client.create(endpoint, data)` | Body: JSON payload | Action: Batch import trusted MAC addresses via CSV |

[↑ Back to Table of Domains](#table-of-domains) &nbsp;•&nbsp; [↑ Back to Top](#top)

---

### <a id="trafficshaping"></a>`TrafficShaping`

Import: `from sfos_api import TrafficShaping`

| Constant Name | REST API Path | Supported Methods | CRUD Methods | CRUD Signatures | Parameters | Description |
|---|---|:---:|:---:|---|---|---|
| `TrafficShaping.POLICIES` | `/traffic-shaping/policies` | `GET`, `POST`, `PATCH`, `DELETE` | `read`, `create`, `update`, `delete` | `client.read(endpoint, [id_or_name])`<br>`client.create(endpoint, data)`<br>`client.update(endpoint, id_or_name, data)`<br>`client.delete(endpoint, id_or_name)` | Path: `id_or_name` *(item)*; Query: `nameContains` or `nameNotEquals` | QoS bandwidth allocation policies, burst limits, and priorities |
| `TrafficShaping.SETTINGS` | `/traffic-shaping/settings` | `GET`, `PATCH` | `read`, `update` | `client.read(endpoint)`<br>`client.update(endpoint, data=data)` | Body: JSON payload | Global traffic shaping and total link bandwidth parameters |

[↑ Back to Table of Domains](#table-of-domains) &nbsp;•&nbsp; [↑ Back to Top](#top)

---

### <a id="wireless"></a>`Wireless`

Import: `from sfos_api import Wireless`

| Constant Name | REST API Path | Supported Methods | CRUD Methods | CRUD Signatures | Parameters | Description |
|---|---|:---:|:---:|---|---|---|
| `Wireless.HOTSPOT_HOTSPOTS` | `/wireless/hotspot/hotspots` | `GET`, `POST`, `PATCH`, `DELETE` | `read`, `create`, `update`, `delete` | `client.read(endpoint, [id_or_name])`<br>`client.create(endpoint, data)`<br>`client.update(endpoint, id_or_name, data)`<br>`client.delete(endpoint, id_or_name)` | Path: `id_or_name` *(item)*; Query: `nameContains` or `nameNotEquals` | Wireless guest hotspots and landing pages |
| `Wireless.HOTSPOT_SETTINGS` | `/wireless/hotspot/settings` | `GET`, `PATCH` | `read`, `update` | `client.read(endpoint)`<br>`client.update(endpoint, data=data)` | Body: JSON payload | Hotspot terms of service and redirect settings |
| `Wireless.HOTSPOT_VOUCHERS` | `/wireless/hotspot/vouchers` | `GET`, `POST`, `PATCH`, `DELETE` | `read`, `create`, `update`, `delete` | `client.read(endpoint, [id_or_name])`<br>`client.create(endpoint, data)`<br>`client.update(endpoint, id_or_name, data)`<br>`client.delete(endpoint, id_or_name)` | Path: `id_or_name` *(item)*; Query: `nameContains` or `nameNotEquals` | Guest access time/quota voucher generator |

[↑ Back to Table of Domains](#table-of-domains) &nbsp;•&nbsp; [↑ Back to Top](#top)

<a id="3-identity-authentication-certificates"></a><a id="3-identity-authentication--certificates"></a>
## 3. Identity, Authentication & Certificates

🔑 User directories, external identity providers, captive portal, MFA/TOTP tokens, and X.509 certificate management.

### <a id="authentication"></a>`Authentication`

Import: `from sfos_api import Authentication`

| Constant Name | REST API Path | Supported Methods | CRUD Methods | CRUD Signatures | Parameters | Description |
|---|---|:---:|:---:|---|---|---|
| `Authentication.ADMIN_USER_PASSWORD` | `/authentication/admin-user/password` | `POST` | `create` | `client.create(endpoint, data)` | Body: JSON payload | Action: Update built-in administrator account password |
| `Authentication.CAPTIVE_PORTAL_APPEARANCE` | `/authentication/captive-portal/appearance` | `GET`, `PATCH` | `read`, `update` | `client.read(endpoint)`<br>`client.update(endpoint, data=data)` | Body: JSON payload | Captive portal logo, branding, and styling settings |
| `Authentication.CLIENTS_GLOBAL_SETTINGS` | `/authentication/clients/global-settings` | `GET`, `PATCH` | `read`, `update` | `client.read(endpoint)`<br>`client.update(endpoint, data=data)` | Body: JSON payload | Authentication client software global parameters |
| `Authentication.CLIENTS_TRANSPARENT_AUTH_SUITE_COLLECTORS` | `/authentication/clients/transparent-auth-suite/collectors` | `GET`, `POST`, `DELETE` | `read`, `create`, `delete` | `client.read(endpoint, [id_or_name])`<br>`client.create(endpoint, data)`<br>`client.delete(endpoint, id_or_name)` | Path: `id_or_name` *(item)* | STAS (Sophos Transparent Authentication) collector agents |
| `Authentication.CLIENTS_TRANSPARENT_AUTH_SUITE_SETTINGS` | `/authentication/clients/transparent-auth-suite/settings` | `GET`, `PATCH` | `read`, `update` | `client.read(endpoint)`<br>`client.update(endpoint, data=data)` | Body: JSON payload | STAS transparent single sign-on settings |
| `Authentication.CLIENTS_TRANSPARENT_AUTH_SUITE_VPN_SOURCE_NETWORKS` | `/authentication/clients/transparent-auth-suite/vpn-source-networks` | `GET`, `POST`, `DELETE` | `read`, `create`, `delete` | `client.read(endpoint, [id_or_name])`<br>`client.create(endpoint, data)`<br>`client.delete(endpoint, id_or_name)` | Path: `id_or_name` *(item)*; Query: `page`, `pageSize` | STAS IP source subnets for VPN clients |
| `Authentication.GUEST_USER_SETTINGS_SMS_GATEWAYS` | `/authentication/guest-user-settings/sms-gateways` | `GET`, `POST`, `PATCH`, `DELETE` | `read`, `create`, `update`, `delete`, `test_connection` | `client.read(endpoint, [id_or_name])`<br>`client.create(endpoint, data)`<br>`client.update(endpoint, id_or_name, data)`<br>`client.delete(endpoint, id_or_name)`<br>`client.test_connection(endpoint, [data])` | Path: `id_or_name` *(item)*; Query: `nameContains`, `nameNotEquals` | SMS gateway configurations for guest OTP delivery |
| `Authentication.LIVE_USERS` | `/authentication/live-users` | `GET` | `read` | `client.read(endpoint)` | None *(singleton)* | Real-time active authenticated user sessions |
| `Authentication.LIVE_USERS_DISCONNECT` | `/authentication/live-users/disconnect` | `POST` | `create` | `client.create(endpoint, data)` | Body: JSON payload | Action: Force disconnect one or more live user sessions |
| `Authentication.LOGIN_SECURITY_SETTINGS` | `/authentication/login/security-settings` | `GET`, `PATCH` | `read`, `update` | `client.read(endpoint)`<br>`client.update(endpoint, data=data)` | Body: JSON payload | Brute-force lockout and session timeout parameters |
| `Authentication.MULTI_FACTOR_AUTHENTICATION_TOTP_SETTINGS` | `/authentication/multi-factor-authentication/totp-settings` | `GET`, `PATCH` | `read`, `update` | `client.read(endpoint)`<br>`client.update(endpoint, data=data)` | Body: JSON payload | TOTP MFA configuration and portal enrollment rules |
| `Authentication.MULTI_FACTOR_AUTHENTICATION_TOTP_TOKENS` | `/authentication/multi-factor-authentication/totp-tokens` | `GET` | `read` | `client.read(endpoint)` | Query: `page`, `pageSize` | Registered TOTP tokens inventory |
| `Authentication.MULTI_FACTOR_AUTHENTICATION_TOTP_TOKENS_HARDWARE_TOKENS` | `/authentication/multi-factor-authentication/totp-tokens/hardware-tokens` | `GET`, `POST`, `PATCH`, `DELETE` | `read`, `create`, `update`, `delete` | `client.read(endpoint, [id_or_name])`<br>`client.create(endpoint, data)`<br>`client.update(endpoint, id_or_name, data)`<br>`client.delete(endpoint, id_or_name)` | Path: `id_or_name` *(item)*; Query: `page`, `pageSize` | Pre-shared secret hardware OTP key fobs |
| `Authentication.MULTI_FACTOR_AUTHENTICATION_TOTP_TOKENS_SOFTWARE_TOKENS` | `/authentication/multi-factor-authentication/totp-tokens/software-tokens` | `GET` | `read` | `client.read(endpoint)` | Query: `page`, `pageSize` | Software authenticator apps (Sophos/Google Authenticator) |
| `Authentication.PASSWORD_COMPLEXITY_ADMINISTRATIVE_USERS` | `/authentication/password-complexity/administrative-users` | `GET`, `PATCH` | `read`, `update` | `client.read(endpoint)`<br>`client.update(endpoint, data=data)` | Body: JSON payload | Password complexity rules for firewall administrators |
| `Authentication.PASSWORD_COMPLEXITY_NETWORK_USERS` | `/authentication/password-complexity/network-users` | `GET`, `PATCH` | `read`, `update` | `client.read(endpoint)`<br>`client.update(endpoint, data=data)` | Body: JSON payload | Password complexity rules for standard network users |
| `Authentication.POLICIES_ACCESS_TIMES` | `/authentication/policies/access-times` | `GET`, `POST`, `PATCH`, `DELETE` | `read`, `create`, `update`, `delete` | `client.read(endpoint, [id_or_name])`<br>`client.create(endpoint, data)`<br>`client.update(endpoint, id_or_name, data)`<br>`client.delete(endpoint, id_or_name)` | Path: `id_or_name` *(item)*; Query: `nameContains`, `nameNotEquals` | Allowed login time schedules and restrictions |
| `Authentication.POLICIES_NETWORK_TRAFFIC_QUOTAS` | `/authentication/policies/network-traffic-quotas` | `GET`, `POST`, `PATCH`, `DELETE` | `read`, `create`, `update`, `delete` | `client.read(endpoint, [id_or_name])`<br>`client.create(endpoint, data)`<br>`client.update(endpoint, id_or_name, data)`<br>`client.delete(endpoint, id_or_name)` | Path: `id_or_name` *(item)*; Query: `nameContains`, `nameNotEquals` | Data transfer volume quota limits per user |
| `Authentication.POLICIES_SURFING_QUOTAS` | `/authentication/policies/surfing-quotas` | `GET`, `POST`, `PATCH`, `DELETE` | `read`, `create`, `update`, `delete` | `client.read(endpoint, [id_or_name])`<br>`client.create(endpoint, data)`<br>`client.update(endpoint, id_or_name, data)`<br>`client.delete(endpoint, id_or_name)` | Path: `id_or_name` *(item)*; Query: `page`, `pageSize` | Web surfing time allowance quotas |
| `Authentication.SERVERS` | `/authentication/servers` | `GET`, `POST`, `DELETE` | `read`, `create`, `delete` | `client.read(endpoint, [id_or_name])`<br>`client.create(endpoint, data)`<br>`client.delete(endpoint, id_or_name)` | Path: `id_or_name` *(item)*; Query: `nameContains` or `nameNotEquals` | Directory and authentication servers overview |
| `Authentication.SERVERS_ACTIVE_DIRECTORY` | `/authentication/servers/active-directory` | `GET`, `POST`, `PATCH`, `DELETE` | `read`, `create`, `update`, `delete`, `test_connection` | `client.read(endpoint, [id_or_name])`<br>`client.create(endpoint, data)`<br>`client.update(endpoint, id_or_name, data)`<br>`client.delete(endpoint, id_or_name)`<br>`client.test_connection(endpoint, [data])` | Path: `id_or_name` *(item)*; Query: `nameContains`, `nameNotEquals` | Microsoft Active Directory domain controller connections |
| `Authentication.SERVERS_ACTIVE_DIRECTORY_BY_ID_OR_NAME_FETCH_GROUPS` | `/authentication/servers/active-directory/{idOrName}/fetch-groups` | `POST` | `create` | `client.create(endpoint, data, id_or_name=...)` | Path: `idOrName` *(required)* | Action: Query and import AD security groups |
| `Authentication.SERVERS_GENERIC_IDP_SSO` | `/authentication/servers/generic-idp-sso` | `GET`, `POST`, `PATCH`, `DELETE` | `read`, `create`, `update`, `delete`, `test_connection` | `client.read(endpoint, [id_or_name])`<br>`client.create(endpoint, data)`<br>`client.update(endpoint, id_or_name, data)`<br>`client.delete(endpoint, id_or_name)`<br>`client.test_connection(endpoint, [data])` | Path: `id_or_name` *(item)*; Query: `nameContains`, `nameNotEquals` | OpenID Connect (OIDC) / SAML generic IdP configurations |
| `Authentication.SERVERS_GENERIC_IDP_SSO_BY_ID_OR_NAME_FETCH_GROUPS` | `/authentication/servers/generic-idp-sso/{idOrName}/fetch-groups` | `POST` | `create` | `client.create(endpoint, data, id_or_name=...)` | Path: `idOrName` *(required)* | Action: Discover and import IdP role claims / groups |
| `Authentication.SERVERS_GENERIC_IDP_SSO_OIDC_DISCOVERY` | `/authentication/servers/generic-idp-sso/oidc-discovery` | `POST` | `create` | `client.create(endpoint, data)` | Body: JSON payload | Action: Auto-discover IdP configuration via `.well-known` endpoint |
| `Authentication.SERVERS_LDAP` | `/authentication/servers/ldap` | `GET`, `POST`, `PATCH`, `DELETE` | `read`, `create`, `update`, `delete`, `test_connection` | `client.read(endpoint, [id_or_name])`<br>`client.create(endpoint, data)`<br>`client.update(endpoint, id_or_name, data)`<br>`client.delete(endpoint, id_or_name)`<br>`client.test_connection(endpoint, [data])` | Path: `id_or_name` *(item)*; Query: `nameContains`, `nameNotEquals` | OpenLDAP and standard LDAP directory connections |
| `Authentication.SERVERS_LDAP_FETCH_BASE_DN` | `/authentication/servers/ldap/fetch-base-dn` | `POST` | `create` | `client.create(endpoint, data)` | Body: JSON payload | Action: Discover and query directory Base DN from LDAP |
| `Authentication.SERVERS_RADIUS` | `/authentication/servers/radius` | `GET`, `POST`, `PATCH`, `DELETE` | `read`, `create`, `update`, `delete`, `test_connection` | `client.read(endpoint, [id_or_name])`<br>`client.create(endpoint, data)`<br>`client.update(endpoint, id_or_name, data)`<br>`client.delete(endpoint, id_or_name)`<br>`client.test_connection(endpoint, [data])` | Path: `id_or_name` *(item)*; Query: `nameContains`, `nameNotEquals` | RADIUS server definitions for AAA authentication |
| `Authentication.SERVERS_TACACS` | `/authentication/servers/tacacs` | `GET`, `POST`, `PATCH`, `DELETE` | `read`, `create`, `update`, `delete`, `test_connection` | `client.read(endpoint, [id_or_name])`<br>`client.create(endpoint, data)`<br>`client.update(endpoint, id_or_name, data)`<br>`client.delete(endpoint, id_or_name)`<br>`client.test_connection(endpoint, [data])` | Path: `id_or_name` *(item)*; Query: `nameContains`, `nameNotEquals` | TACACS+ administrative authentication servers |
| `Authentication.SERVER_PRIORITY_LIST_ADMINISTRATIVE_ACCESS` | `/authentication/server-priority-list/administrative-access` | `GET`, `PATCH` | `read`, `update` | `client.read(endpoint)`<br>`client.update(endpoint, data=data)` | Body: JSON payload | Authentication server fallback sequence for administrators |
| `Authentication.SERVER_PRIORITY_LIST_DEFAULT` | `/authentication/server-priority-list/default` | `GET`, `PATCH` | `read`, `update` | `client.read(endpoint)`<br>`client.update(endpoint, data=data)` | Body: JSON payload | Default authentication server fallback sequence |
| `Authentication.SERVER_PRIORITY_LIST_USER_PORTAL_ACCESS` | `/authentication/server-priority-list/user-portal-access` | `GET`, `PATCH` | `read`, `update` | `client.read(endpoint)`<br>`client.update(endpoint, data=data)` | Body: JSON payload | Authentication fallback sequence for User Portal |
| `Authentication.SERVER_PRIORITY_LIST_VPN_ACCESS` | `/authentication/server-priority-list/vpn-access` | `GET`, `PATCH` | `read`, `update` | `client.read(endpoint)`<br>`client.update(endpoint, data=data)` | Body: JSON payload | Authentication fallback sequence for SSL/IPsec VPN |
| `Authentication.SERVICES_CHROMEBOOK_SSO` | `/authentication/services/chromebook-sso` | `GET`, `PATCH` | `read`, `update` | `client.read(endpoint)`<br>`client.update(endpoint, data=data)` | Body: JSON payload | G Suite / Google Chromebook Single Sign-On service |
| `Authentication.SERVICES_RADIUS_ACCOUNTING_SSO` | `/authentication/services/radius-accounting-sso` | `GET`, `POST`, `PATCH`, `DELETE` | `read`, `create`, `update`, `delete` | `client.read(endpoint, [id_or_name])`<br>`client.create(endpoint, data)`<br>`client.update(endpoint, id_or_name, data)`<br>`client.delete(endpoint, id_or_name)` | Path: `id_or_name` *(item)* | RADIUS Accounting SSO integration settings |
| `Authentication.USERS` | `/authentication/users` | `GET` | `read` | `client.read(endpoint)` | Query: `page`, `pageSize` | All local and synchronized user accounts |
| `Authentication.USERS_ADMINISTRATORS` | `/authentication/users/administrators` | `GET`, `POST`, `PATCH`, `DELETE` | `read`, `create`, `update`, `delete` | `client.read(endpoint, [id_or_name])`<br>`client.create(endpoint, data)`<br>`client.update(endpoint, id_or_name, data)`<br>`client.delete(endpoint, id_or_name)` | Path: `id_or_name` *(item)*; Query: `page`, `pageSize` | Firewall administrative user accounts |
| `Authentication.USERS_NETWORK_USERS` | `/authentication/users/network-users` | `GET`, `POST`, `PATCH`, `DELETE` | `read`, `create`, `update`, `delete` | `client.read(endpoint, [id_or_name])`<br>`client.create(endpoint, data)`<br>`client.update(endpoint, id_or_name, data)`<br>`client.delete(endpoint, id_or_name)` | Path: `id_or_name` *(item)*; Query: `page`, `pageSize` | Standard network and VPN user accounts |
| `Authentication.USERS_NETWORK_USERS_LOGIN` | `/authentication/users/network-users/login` | `POST` | `create` | `client.create(endpoint, data)` | Body: JSON payload | Action: Trigger programmatic user login |
| `Authentication.USERS_NETWORK_USERS_LOGOUT` | `/authentication/users/network-users/logout` | `POST` | `create` | `client.create(endpoint, data)` | Body: JSON payload | Action: Trigger programmatic user logout |
| `Authentication.USER_GROUPS` | `/authentication/user-groups` | `GET`, `POST`, `PATCH`, `DELETE` | `read`, `create`, `update`, `delete` | `client.read(endpoint, [id_or_name])`<br>`client.create(endpoint, data)`<br>`client.update(endpoint, id_or_name, data)`<br>`client.delete(endpoint, id_or_name)` | Path: `id_or_name` *(item)*; Query: `nameContains` or `nameNotEquals` | Local and synchronized user groups |
| `Authentication.USER_GROUPS_SET_FALLBACK_GROUP` | `/authentication/user-groups/set-fallback-group` | `POST` | `create` | `client.create(endpoint, data)` | Body: JSON payload | Action: Set default fallback user group for new users |
| `Authentication.WEB_SETTINGS` | `/authentication/web-settings` | `GET`, `PATCH` | `read`, `update` | `client.read(endpoint)`<br>`client.update(endpoint, data=data)` | Body: JSON payload | Captive portal redirection and re-authentication settings |

[↑ Back to Table of Domains](#table-of-domains) &nbsp;•&nbsp; [↑ Back to Top](#top)

---

### <a id="certificate"></a>`Certificate`

Import: `from sfos_api import Certificate`

| Constant Name | REST API Path | Supported Methods | CRUD Methods | CRUD Signatures | Parameters | Description |
|---|---|:---:|:---:|---|---|---|
| `Certificate.CERTIFICATES` | `/certificate/certificates` | `GET` | `read` | `client.read(endpoint)` | Query: `nameContains` or `nameNotEquals` | All installed X.509 server and user certificates |
| `Certificate.CERTIFICATES_CERTIFICATE_SIGNING_REQUESTS` | `/certificate/certificates/certificate-signing-requests` | `GET`, `POST`, `DELETE` | `read`, `create`, `delete` | `client.read(endpoint, [id_or_name])`<br>`client.create(endpoint, data)`<br>`client.delete(endpoint, id_or_name)` | Path: `id_or_name` *(item)*; Query: `nameContains` or `nameNotEquals` | Certificate Signing Requests (CSR) management |
| `Certificate.CERTIFICATES_EXTERNAL` | `/certificate/certificates/external` | `GET`, `POST`, `DELETE` | `read`, `create`, `delete` | `client.read(endpoint, [id_or_name])`<br>`client.create(endpoint, data)`<br>`client.delete(endpoint, id_or_name)` | Path: `id_or_name` *(item)*; Query: `nameContains` or `nameNotEquals` | Third-party issued external certificates |
| `Certificate.CERTIFICATES_INTERNAL` | `/certificate/certificates/internal` | `GET`, `POST`, `DELETE` | `read`, `create`, `delete` | `client.read(endpoint, [id_or_name])`<br>`client.create(endpoint, data)`<br>`client.delete(endpoint, id_or_name)` | Path: `id_or_name` *(item)*; Query: `nameContains` or `nameNotEquals` | Locally signed internal private certificates |
| `Certificate.CERTIFICATE_AUTHORITIES` | `/certificate/certificate-authorities` | `GET`, `POST`, `DELETE` | `read`, `create`, `delete` | `client.read(endpoint, [id_or_name])`<br>`client.create(endpoint, data)`<br>`client.delete(endpoint, id_or_name)` | Path: `id_or_name` *(item)*; Query: `nameContains` or `nameNotEquals` | Trusted Root and Intermediate Certificate Authorities |
| `Certificate.CERTIFICATE_AUTHORITIES_BUILT_IN_DEFAULT_CA` | `/certificate/certificate-authorities/built-in/default-ca` | `GET` | `read` | `client.read(endpoint)` | None *(singleton)* | Sophos Appliance built-in default CA details |
| `Certificate.CERTIFICATE_AUTHORITIES_BUILT_IN_DEFAULT_CA_REGENERATE` | `/certificate/certificate-authorities/built-in/default-ca/regenerate` | `POST` | `create` | `client.create(endpoint, data)` | Body: JSON payload | Action: Regenerate built-in default CA certificate |
| `Certificate.CERTIFICATE_REVOCATION_LISTS` | `/certificate/certificate-revocation-lists` | `GET`, `POST`, `DELETE` | `read`, `create`, `delete` | `client.read(endpoint, [id_or_name])`<br>`client.create(endpoint, data)`<br>`client.delete(endpoint, id_or_name)` | Path: `id_or_name` *(item)*; Query: `nameContains` or `nameNotEquals` | Certificate Revocation Lists (CRL) and auto-sync |

[↑ Back to Table of Domains](#table-of-domains) &nbsp;•&nbsp; [↑ Back to Top](#top)

<a id="4-vpn-remote-connectivity"></a><a id="4-vpn--remote-connectivity"></a>
## 4. VPN & Remote Connectivity

🔒 Site-to-site IPsec tunnels, route/policy-based connections, and SSL VPN remote access.

### <a id="ipsecvpn"></a>`IpsecVpn`

Import: `from sfos_api import IpsecVpn`

| Constant Name | REST API Path | Supported Methods | CRUD Methods | CRUD Signatures | Parameters | Description |
|---|---|:---:|:---:|---|---|---|
| `IpsecVpn.PROFILES` | `/ipsec-vpn/profiles` | `GET`, `POST`, `PATCH`, `DELETE` | `read`, `create`, `update`, `delete` | `client.read(endpoint, [id_or_name])`<br>`client.create(endpoint, data)`<br>`client.update(endpoint, id_or_name, data)`<br>`client.delete(endpoint, id_or_name)` | Path: `id_or_name` *(item)*; Query: `nameContains` or `nameNotEquals` | IKEv1/IKEv2 cryptographic negotiation profiles |
| `IpsecVpn.REMOTE_ACCESS_SETTINGS` | `/ipsec-vpn/remote-access/settings` | `GET`, `PATCH` | `read`, `update` | `client.read(endpoint)`<br>`client.update(endpoint, data=data)` | Body: JSON payload | IPsec remote access client pool and gateway settings |
| `IpsecVpn.SITE_TO_SITE_CONNECTIONS_IPV4` | `/ipsec-vpn/site-to-site/connections/ipv4` | `GET`, `POST`, `DELETE` | `read`, `create`, `delete` | `client.read(endpoint, [id_or_name])`<br>`client.create(endpoint, data)`<br>`client.delete(endpoint, id_or_name)` | Path: `id_or_name` *(item)*; Query: `nameContains` or `nameNotEquals` | IPv4 IPsec site-to-site connection profiles |
| `IpsecVpn.SITE_TO_SITE_CONNECTIONS_POLICY_BASED_IPV4` | `/ipsec-vpn/site-to-site/connections/policy-based/ipv4` | `GET`, `POST`, `PATCH`, `DELETE` | `read`, `create`, `update`, `delete` | `client.read(endpoint, [id_or_name])`<br>`client.create(endpoint, data)`<br>`client.update(endpoint, id_or_name, data)`<br>`client.delete(endpoint, id_or_name)` | Path: `id_or_name` *(item)*; Query: `nameContains` or `nameNotEquals` | Policy-based (crypto map) IPv4 site-to-site tunnels |
| `IpsecVpn.SITE_TO_SITE_CONNECTIONS_ROUTE_BASED_IPV4` | `/ipsec-vpn/site-to-site/connections/route-based/ipv4` | `GET`, `POST`, `PATCH`, `DELETE` | `read`, `create`, `update`, `delete` | `client.read(endpoint, [id_or_name])`<br>`client.create(endpoint, data)`<br>`client.update(endpoint, id_or_name, data)`<br>`client.delete(endpoint, id_or_name)` | Path: `id_or_name` *(item)*; Query: `nameContains` or `nameNotEquals` | Route-based (XFRM tunnel interface) IPv4 IPsec connections |
| `IpsecVpn.SITE_TO_SITE_FAILOVER_GROUPS` | `/ipsec-vpn/site-to-site/failover-groups` | `GET`, `POST`, `PATCH`, `DELETE` | `read`, `create`, `update`, `delete` | `client.read(endpoint, [id_or_name])`<br>`client.create(endpoint, data)`<br>`client.update(endpoint, id_or_name, data)`<br>`client.delete(endpoint, id_or_name)` | Path: `id_or_name` *(item)*; Query: `nameContains` or `nameNotEquals` | Redundant multi-tunnel failover groups |
| `IpsecVpn.SITE_TO_SITE_LIVE_CONNECTIONS_IPV4` | `/ipsec-vpn/site-to-site/live-connections/ipv4` | `GET` | `read` | `client.read(endpoint)` | None *(singleton)* | Real-time active IPsec tunnel status and SA diagnostics |

[↑ Back to Table of Domains](#table-of-domains) &nbsp;•&nbsp; [↑ Back to Top](#top)

---

### <a id="sslvpn"></a>`SslVpn`

Import: `from sfos_api import SslVpn`

| Constant Name | REST API Path | Supported Methods | CRUD Methods | CRUD Signatures | Parameters | Description |
|---|---|:---:|:---:|---|---|---|
| `SslVpn.CLIENTLESS_BOOKMARKS` | `/ssl-vpn/clientless/bookmarks` | `GET`, `POST`, `PATCH`, `DELETE` | `read`, `create`, `update`, `delete` | `client.read(endpoint, [id_or_name])`<br>`client.create(endpoint, data)`<br>`client.update(endpoint, id_or_name, data)`<br>`client.delete(endpoint, id_or_name)` | Path: `id_or_name` *(item)*; Query: `nameContains` or `nameNotEquals` | HTML5 clientless browser bookmarks (RDP, SSH, VNC, HTTP) |
| `SslVpn.CLIENTLESS_BOOKMARK_GROUPS` | `/ssl-vpn/clientless/bookmark-groups` | `GET`, `POST`, `PATCH`, `DELETE` | `read`, `create`, `update`, `delete` | `client.read(endpoint, [id_or_name])`<br>`client.create(endpoint, data)`<br>`client.update(endpoint, id_or_name, data)`<br>`client.delete(endpoint, id_or_name)` | Path: `id_or_name` *(item)*; Query: `nameContains` or `nameNotEquals` | Bookmark group assignments for clientless access |
| `SslVpn.CLIENTLESS_POLICIES` | `/ssl-vpn/clientless/policies` | `GET`, `POST`, `PATCH`, `DELETE` | `read`, `create`, `update`, `delete` | `client.read(endpoint, [id_or_name])`<br>`client.create(endpoint, data)`<br>`client.update(endpoint, id_or_name, data)`<br>`client.delete(endpoint, id_or_name)` | Path: `id_or_name` *(item)*; Query: `nameContains` or `nameNotEquals` | Clientless SSL VPN portal access permissions |
| `SslVpn.GLOBAL_SETTINGS` | `/ssl-vpn/global-settings` | `GET`, `PATCH` | `read`, `update` | `client.read(endpoint)`<br>`client.update(endpoint, data=data)` | Body: JSON payload | OpenVPN protocol, port, cipher, and IP lease pool parameters |
| `SslVpn.REMOTE_ACCESS_POLICIES` | `/ssl-vpn/remote-access/policies` | `GET`, `POST`, `PATCH`, `DELETE` | `read`, `create`, `update`, `delete` | `client.read(endpoint, [id_or_name])`<br>`client.create(endpoint, data)`<br>`client.update(endpoint, id_or_name, data)`<br>`client.delete(endpoint, id_or_name)` | Path: `id_or_name` *(item)*; Query: `nameContains` or `nameNotEquals` | Full-tunnel and split-tunnel remote access client policies |

[↑ Back to Table of Domains](#table-of-domains) &nbsp;•&nbsp; [↑ Back to Top](#top)

<a id="5-threat-protection-content-security"></a><a id="5-threat-protection--content-security"></a>
## 5. Threat Protection & Content Security

🦠 Threat intelligence feeds, MDR, Application Control, Antivirus, Web Content Filtering, WAF, and Cloud Sandboxing.

### <a id="activethreatresponse"></a>`ActiveThreatResponse`

Import: `from sfos_api import ActiveThreatResponse`

| Constant Name | REST API Path | Supported Methods | CRUD Methods | CRUD Signatures | Parameters | Description |
|---|---|:---:|:---:|---|---|---|
| `ActiveThreatResponse.MDR_THREAT_FEED_SETTINGS` | `/active-threat-response/mdr-threat-feed/settings` | `GET`, `PATCH` | `read`, `update` | `client.read(endpoint)`<br>`client.update(endpoint, data=data)` | Body: JSON payload | Sophos MDR (Managed Detection and Response) threat feed feeds |
| `ActiveThreatResponse.SOPHOS_X_OPS_THREAT_FEED_SETTINGS` | `/active-threat-response/sophos-x-ops-threat-feed/settings` | `GET`, `PATCH` | `read`, `update` | `client.read(endpoint)`<br>`client.update(endpoint, data=data)` | Body: JSON payload | Sophos X-Ops threat intelligence feed parameters |
| `ActiveThreatResponse.THIRDPARTY_THREAT_FEEDS` | `/active-threat-response/thirdparty-threat-feeds` | `GET`, `POST`, `PATCH`, `DELETE` | `read`, `create`, `update`, `delete`, `test_connection` | `client.read(endpoint, [id_or_name])`<br>`client.create(endpoint, data)`<br>`client.update(endpoint, id_or_name, data)`<br>`client.delete(endpoint, id_or_name)`<br>`client.test_connection(endpoint, [data])` | Path: `id_or_name` *(item)* | Custom STIX/TAXII and URL third-party threat feeds |
| `ActiveThreatResponse.THIRDPARTY_THREAT_FEEDS_BY_ID_OR_NAME_SYNCHRONIZE` | `/active-threat-response/thirdparty-threat-feeds/{idOrName}/synchronize` | `POST` | `create` | `client.create(endpoint, id_or_name=...)` | Path: `idOrName` *(required)* | Action: Trigger immediate threat feed pull and synchronization |
| `ActiveThreatResponse.THREAT_EXCLUSIONS` | `/active-threat-response/threat-exclusions` | `GET`, `PATCH` | `read`, `update` | `client.read(endpoint)`<br>`client.update(endpoint, data=data)` | Body: JSON payload | Whitelisted IOCs and IP/domain threat exclusions |

[↑ Back to Table of Domains](#table-of-domains) &nbsp;•&nbsp; [↑ Back to Top](#top)

---

### <a id="application"></a>`Application`

Import: `from sfos_api import Application`

| Constant Name | REST API Path | Supported Methods | CRUD Methods | CRUD Signatures | Parameters | Description |
|---|---|:---:|:---:|---|---|---|
| `Application.APPS` | `/application/apps` | `GET` | `read` | `client.read(endpoint)` | Query: `page`, `pageSize` | Known application signature definitions catalog |
| `Application.ATTRIBUTES` | `/application/attributes` | `GET` | `read` | `client.read(endpoint)` | None *(singleton)* | Application risk levels, categories, and technology tags |
| `Application.CATEGORIES` | `/application/categories` | `GET` | `read` | `client.read(endpoint)` | Query: `page`, `pageSize` | High-level application categories (P2P, Streaming, Games) |
| `Application.OBJECTS` | `/application/objects` | `GET`, `POST`, `PATCH`, `DELETE` | `read`, `create`, `update`, `delete` | `client.read(endpoint, [id_or_name])`<br>`client.create(endpoint, data)`<br>`client.update(endpoint, id_or_name, data)`<br>`client.delete(endpoint, id_or_name)` | Path: `id_or_name` *(item)*; Query: `page`, `pageSize` | Application filter objects and custom signatures |
| `Application.POLICIES` | `/application/policies` | `GET`, `POST`, `PATCH`, `DELETE` | `read`, `create`, `update`, `delete` | `client.read(endpoint, [id_or_name])`<br>`client.create(endpoint, data)`<br>`client.update(endpoint, id_or_name, data)`<br>`client.delete(endpoint, id_or_name)` | Path: `id_or_name` *(item)*; Query: `page`, `pageSize` | Application control filtering policies and actions |

[↑ Back to Table of Domains](#table-of-domains) &nbsp;•&nbsp; [↑ Back to Top](#top)

---

### <a id="malwareprotection"></a>`MalwareProtection`

Import: `from sfos_api import MalwareProtection`

| Constant Name | REST API Path | Supported Methods | CRUD Methods | CRUD Signatures | Parameters | Description |
|---|---|:---:|:---:|---|---|---|
| `MalwareProtection.SETTINGS` | `/malware-protection/settings` | `GET`, `PATCH` | `read`, `update` | `client.read(endpoint)`<br>`client.update(endpoint, data=data)` | Body: JSON payload | Dual-engine antivirus scanning settings and file size limits |

[↑ Back to Table of Domains](#table-of-domains) &nbsp;•&nbsp; [↑ Back to Top](#top)

---

### <a id="waf"></a>`Waf`

Import: `from sfos_api import Waf`

| Constant Name | REST API Path | Supported Methods | CRUD Methods | CRUD Signatures | Parameters | Description |
|---|---|:---:|:---:|---|---|---|
| `Waf.AUTHENTICATION_POLICIES` | `/waf/authentication/policies` | `GET`, `POST`, `PATCH`, `DELETE` | `read`, `create`, `update`, `delete` | `client.read(endpoint, [id_or_name])`<br>`client.create(endpoint, data)`<br>`client.update(endpoint, id_or_name, data)`<br>`client.delete(endpoint, id_or_name)` | Path: `id_or_name` *(item)*; Query: `page`, `pageSize` | Reverse proxy client authentication policies |
| `Waf.AUTHENTICATION_TEMPLATES` | `/waf/authentication/templates` | `GET`, `POST`, `PATCH`, `DELETE` | `read`, `create`, `update`, `delete` | `client.read(endpoint, [id_or_name])`<br>`client.create(endpoint, data)`<br>`client.update(endpoint, id_or_name, data)`<br>`client.delete(endpoint, id_or_name)` | Path: `id_or_name` *(item)*; Query: `page`, `pageSize` | Reverse proxy login form templates |
| `Waf.PROTECTION_POLICIES` | `/waf/protection/policies` | `GET`, `POST`, `PATCH`, `DELETE` | `read`, `create`, `update`, `delete` | `client.read(endpoint, [id_or_name])`<br>`client.create(endpoint, data)`<br>`client.update(endpoint, id_or_name, data)`<br>`client.delete(endpoint, id_or_name)` | Path: `id_or_name` *(item)*; Query: `nameContains` or `nameNotEquals` | Web Application Firewall SQLi, XSS, and cookie protection |
| `Waf.SERVERS` | `/waf/servers` | `GET`, `POST`, `PATCH`, `DELETE` | `read`, `create`, `update`, `delete` | `client.read(endpoint, [id_or_name])`<br>`client.create(endpoint, data)`<br>`client.update(endpoint, id_or_name, data)`<br>`client.delete(endpoint, id_or_name)` | Path: `id_or_name` *(item)*; Query: `page`, `pageSize` | Backend web servers and host farm configurations |

[↑ Back to Table of Domains](#table-of-domains) &nbsp;•&nbsp; [↑ Back to Top](#top)

---

### <a id="web"></a>`Web`

Import: `from sfos_api import Web`

| Constant Name | REST API Path | Supported Methods | CRUD Methods | CRUD Signatures | Parameters | Description |
|---|---|:---:|:---:|---|---|---|
| `Web.CATEGORIES` | `/web/categories` | `GET`, `POST`, `PATCH`, `DELETE` | `read`, `create`, `update`, `delete` | `client.read(endpoint, [id_or_name])`<br>`client.create(endpoint, data)`<br>`client.update(endpoint, id_or_name, data)`<br>`client.delete(endpoint, id_or_name)` | Path: `id_or_name` *(item)*; Query: `nameContains` or `nameNotEquals` | Web filtering categories (standard and custom) |
| `Web.CONTENT_FILTERS` | `/web/content-filters` | `GET`, `POST`, `PATCH`, `DELETE` | `read`, `create`, `update`, `delete` | `client.read(endpoint, [id_or_name])`<br>`client.create(endpoint, data)`<br>`client.update(endpoint, id_or_name, data)`<br>`client.delete(endpoint, id_or_name)` | Path: `id_or_name` *(item)*; Query: `nameContains` or `nameNotEquals` | File extension, MIME type, and keyword content filters |
| `Web.EXCEPTIONS` | `/web/exceptions` | `GET`, `POST`, `PATCH`, `DELETE` | `read`, `create`, `update`, `delete` | `client.read(endpoint, [id_or_name])`<br>`client.create(endpoint, data)`<br>`client.update(endpoint, id_or_name, data)`<br>`client.delete(endpoint, id_or_name)` | Path: `id_or_name` *(item)*; Query: `nameContains` or `nameNotEquals` | URL bypass and scanning exception lists |
| `Web.POLICIES` | `/web/policies` | `GET`, `POST`, `PATCH`, `DELETE` | `read`, `create`, `update`, `delete` | `client.read(endpoint, [id_or_name])`<br>`client.create(endpoint, data)`<br>`client.update(endpoint, id_or_name, data)`<br>`client.delete(endpoint, id_or_name)` | Path: `id_or_name` *(item)*; Query: `nameContains` or `nameNotEquals` | Web protection rules, user quotas, and schedule assignments |
| `Web.SCAN_SETTINGS` | `/web/scan-settings` | `GET`, `PATCH` | `read`, `update` | `client.read(endpoint)`<br>`client.update(endpoint, data=data)` | Body: JSON payload | HTTP/HTTPS proxy inspection modes and block page settings |
| `Web.URL_GROUPS` | `/web/url-groups` | `GET`, `POST`, `PATCH`, `DELETE` | `read`, `create`, `update`, `delete` | `client.read(endpoint, [id_or_name])`<br>`client.create(endpoint, data)`<br>`client.update(endpoint, id_or_name, data)`<br>`client.delete(endpoint, id_or_name)` | Path: `id_or_name` *(item)*; Query: `nameContains` or `nameNotEquals` | Custom URL and domain groups for filtering |
| `Web.USER_ACTIVITIES` | `/web/user-activities` | `GET`, `POST`, `PATCH`, `DELETE` | `read`, `create`, `update`, `delete` | `client.read(endpoint, [id_or_name])`<br>`client.create(endpoint, data)`<br>`client.update(endpoint, id_or_name, data)`<br>`client.delete(endpoint, id_or_name)` | Path: `id_or_name` *(item)*; Query: `nameContains` or `nameNotEquals` | Productive vs. unproductive user browsing classification |
| `Web.USER_NOTIFICATIONS` | `/web/user-notifications` | `GET`, `PATCH` | `read`, `update` | `client.read(endpoint)`<br>`client.update(endpoint, data=data)` | Body: JSON payload | Block page banners and warning notification pages |

[↑ Back to Table of Domains](#table-of-domains) &nbsp;•&nbsp; [↑ Back to Top](#top)

---

### <a id="zerodayprotection"></a>`ZeroDayProtection`

Import: `from sfos_api import ZeroDayProtection`

| Constant Name | REST API Path | Supported Methods | CRUD Methods | CRUD Signatures | Parameters | Description |
|---|---|:---:|:---:|---|---|---|
| `ZeroDayProtection.SETTINGS` | `/zero-day-protection/settings` | `GET`, `PATCH` | `read`, `update` | `client.read(endpoint)`<br>`client.update(endpoint, data=data)` | Body: JSON payload | Sophos Sandstorm cloud sandboxing analysis parameters |

[↑ Back to Table of Domains](#table-of-domains) &nbsp;•&nbsp; [↑ Back to Top](#top)

<a id="6-system-administration-observability"></a><a id="6-system-administration--observability"></a>
## 6. System, Administration & Observability

⚙️ Appliance configuration, administrative profiles, API access, system schedules, logging, SNMP, and Sophos Central.

### <a id="administration"></a>`Administration`

Import: `from sfos_api import Administration`

| Constant Name | REST API Path | Supported Methods | CRUD Methods | CRUD Signatures | Parameters | Description |
|---|---|:---:|:---:|---|---|---|
| `Administration.ACCESS_PERMISSIONS` | `/administration/access/permissions` | `GET` | `read` | `client.read(endpoint)` | None *(singleton)* | Granular role-based access control permissions |
| `Administration.ACCESS_PROFILES` | `/administration/access/profiles` | `GET`, `POST`, `PATCH`, `DELETE` | `read`, `create`, `update`, `delete` | `client.read(endpoint, [id_or_name])`<br>`client.create(endpoint, data)`<br>`client.update(endpoint, id_or_name, data)`<br>`client.delete(endpoint, id_or_name)` | Path: `id_or_name` *(item)* | Administrator privilege profiles (Read/Write/None) |
| `Administration.API_SETTINGS` | `/administration/api-settings` | `GET`, `PATCH` | `read`, `update` | `client.read(endpoint)`<br>`client.update(endpoint, data=data)` | Body: JSON payload | SFOS WebAdmin REST API access, allowed IPs, and API client status |
| `Administration.MESSAGES` | `/administration/messages` | `GET`, `PATCH` | `read`, `update` | `client.read(endpoint)`<br>`client.update(endpoint, data=data)` | Body: JSON payload | Custom administrator login and legal disclaimer banners |
| `Administration.PORTAL_SETTINGS` | `/administration/portal-settings` | `GET`, `PATCH` | `read`, `update` | `client.read(endpoint)`<br>`client.update(endpoint, data=data)` | Body: JSON payload | WebAdmin and User Portal listening ports and protocols |
| `Administration.SCHEDULES` | `/administration/schedules` | `GET`, `POST`, `PATCH`, `DELETE` | `read`, `create`, `update`, `delete` | `client.read(endpoint, [id_or_name])`<br>`client.create(endpoint, data)`<br>`client.update(endpoint, id_or_name, data)`<br>`client.delete(endpoint, id_or_name)` | Path: `id_or_name` *(item)*; Query: `nameContains` or `nameNotEquals` | Time periods (one-time and recurring) for policy rules |
| `Administration.SUPPORT_ACCESS` | `/administration/support-access` | `GET`, `PATCH` | `read`, `update` | `client.read(endpoint)`<br>`client.update(endpoint, data=data)` | Body: JSON payload | Sophos technical support secure reverse-SSH tunnel |
| `Administration.SYSTEM_SETTINGS` | `/administration/system-settings` | `GET`, `PATCH` | `read`, `update` | `client.read(endpoint)`<br>`client.update(endpoint, data=data)` | Body: JSON payload | Hostname, time zone, NTP servers, and language settings |

[↑ Back to Table of Domains](#table-of-domains) &nbsp;•&nbsp; [↑ Back to Top](#top)

---

### <a id="logging"></a>`Logging`

Import: `from sfos_api import Logging`

| Constant Name | REST API Path | Supported Methods | CRUD Methods | CRUD Signatures | Parameters | Description |
|---|---|:---:|:---:|---|---|---|
| `Logging.LOG_ATTRIBUTES_COMPONENTS` | `/logging/log-attributes/components` | `GET` | `read` | `client.read(endpoint)` | None *(singleton)* | Logging subsystem components (Firewall, IPS, Web, VPN) |
| `Logging.LOG_ATTRIBUTES_TYPES` | `/logging/log-attributes/types` | `GET` | `read` | `client.read(endpoint)` | None *(singleton)* | Log severity levels and message categories |
| `Logging.LOG_DESTINATIONS_CENTRAL_FIREWALL_REPORTING` | `/logging/log-destinations/central-firewall-reporting` | `GET`, `PATCH` | `read`, `update` | `client.read(endpoint)`<br>`client.update(endpoint, data=data)` | Body: JSON payload | Sophos Central Cloud Firewall Reporting forwarding |
| `Logging.LOG_DESTINATIONS_LOG_VIEWER` | `/logging/log-destinations/log-viewer` | `GET`, `PATCH` | `read`, `update` | `client.read(endpoint)`<br>`client.update(endpoint, data=data)` | Body: JSON payload | Local Log Viewer retention and query settings |
| `Logging.LOG_DESTINATIONS_SYSLOG_SERVERS` | `/logging/log-destinations/syslog-servers` | `GET`, `POST`, `PATCH`, `DELETE` | `read`, `create`, `update`, `delete` | `client.read(endpoint, [id_or_name])`<br>`client.create(endpoint, data)`<br>`client.update(endpoint, id_or_name, data)`<br>`client.delete(endpoint, id_or_name)` | Path: `id_or_name` *(item)* | Remote Syslog SIEM targets (UDP/TCP/TLS) |
| `Logging.LOG_DESTINATIONS_SYSLOG_SERVERS_BY_ID_OR_NAME_LOGS` | `/logging/log-destinations/syslog-servers/{idOrName}/logs` | `GET`, `PATCH` | `read`, `update` | `client.read(endpoint, id_or_name)`<br>`client.update(endpoint, id_or_name, data)` | Path: `idOrName` *(required)* | Facility and log category filters per Syslog server |
| `Logging.LOG_SETTINGS` | `/logging/log-settings` | `GET`, `PATCH` | `read`, `update` | `client.read(endpoint)`<br>`client.update(endpoint, data=data)` | Body: JSON payload | Global log buffer sizes and local disk archiving policies |

[↑ Back to Table of Domains](#table-of-domains) &nbsp;•&nbsp; [↑ Back to Top](#top)

---

### <a id="monitoring"></a>`Monitoring`

Import: `from sfos_api import Monitoring`

| Constant Name | REST API Path | Supported Methods | CRUD Methods | CRUD Signatures | Parameters | Description |
|---|---|:---:|:---:|---|---|---|
| `Monitoring.NETFLOW_COLLECTORS` | `/monitoring/netflow/collectors` | `GET`, `POST`, `PATCH`, `DELETE` | `read`, `create`, `update`, `delete` | `client.read(endpoint, [id_or_name])`<br>`client.create(endpoint, data)`<br>`client.update(endpoint, id_or_name, data)`<br>`client.delete(endpoint, id_or_name)` | Path: `id_or_name` *(item)* | NetFlow / IPFIX flow export collectors and sampling rates |
| `Monitoring.SNMP_AGENT_CONFIGURATION` | `/monitoring/snmp/agent-configuration` | `GET`, `PATCH` | `read`, `update` | `client.read(endpoint)`<br>`client.update(endpoint, data=data)` | Body: JSON payload | SNMPv1/v2c/v3 agent listener configuration |
| `Monitoring.SNMP_COMMUNITIES` | `/monitoring/snmp/communities` | `GET`, `POST`, `PATCH`, `DELETE` | `read`, `create`, `update`, `delete` | `client.read(endpoint, [id_or_name])`<br>`client.create(endpoint, data)`<br>`client.update(endpoint, id_or_name, data)`<br>`client.delete(endpoint, id_or_name)` | Path: `id_or_name` *(item)* | SNMPv1/v2c community strings and permitted source hosts |
| `Monitoring.SNMP_USERS` | `/monitoring/snmp/users` | `GET`, `POST`, `PATCH`, `DELETE` | `read`, `create`, `update`, `delete` | `client.read(endpoint, [id_or_name])`<br>`client.create(endpoint, data)`<br>`client.update(endpoint, id_or_name, data)`<br>`client.delete(endpoint, id_or_name)` | Path: `id_or_name` *(item)* | SNMPv3 USM user accounts, authentication, and privacy keys |

[↑ Back to Table of Domains](#table-of-domains) &nbsp;•&nbsp; [↑ Back to Top](#top)

---

### <a id="notification"></a>`Notification`

Import: `from sfos_api import Notification`

| Constant Name | REST API Path | Supported Methods | CRUD Methods | CRUD Signatures | Parameters | Description |
|---|---|:---:|:---:|---|---|---|
| `Notification.NOTIFICATIONS` | `/notification/notifications` | `GET`, `PATCH` | `read`, `update` | `client.read(endpoint)`<br>`client.update(endpoint, data=data)` | Body: JSON payload | Email notifications, SMTP mail server, and alert recipients |

[↑ Back to Table of Domains](#table-of-domains) &nbsp;•&nbsp; [↑ Back to Top](#top)

---

### <a id="sophoscentral"></a>`SophosCentral`

Import: `from sfos_api import SophosCentral`

| Constant Name | REST API Path | Supported Methods | CRUD Methods | CRUD Signatures | Parameters | Description |
|---|---|:---:|:---:|---|---|---|
| `SophosCentral.DEREGISTER` | `/sophos-central/deregister` | `POST` | `create` | `client.create(endpoint, data)` | Body: JSON payload | Action: Deregister appliance from Sophos Central |
| `SophosCentral.REGISTER` | `/sophos-central/register` | `POST` | `create` | `client.create(endpoint, data)` | Body: JSON payload | Action: Register appliance using Sophos Central OTP |
| `SophosCentral.SETTINGS` | `/sophos-central/settings` | `GET`, `PATCH` | `read`, `update` | `client.read(endpoint)`<br>`client.update(endpoint, data=data)` | Body: JSON payload | Sophos Central management, telemetry, and backup settings |
| `SophosCentral.STATUS` | `/sophos-central/status` | `GET` | `read` | `client.read(endpoint)` | None *(singleton)* | Current Sophos Central connection status and last sync time |

[↑ Back to Table of Domains](#table-of-domains) &nbsp;•&nbsp; [↑ Back to Top](#top)

---

### <a id="system"></a>`System`

Import: `from sfos_api import System`

| Constant Name | REST API Path | Supported Methods | CRUD Methods | CRUD Signatures | Parameters | Description |
|---|---|:---:|:---:|---|---|---|
| `System.BACKUP_SETTINGS` | `/system/backup/settings` | `GET`, `PATCH` | `read`, `update` | `client.read(endpoint)`<br>`client.update(endpoint, data=data)` | Body: JSON payload | Scheduled automated backup settings (FTP/Email/Local) |
| `System.HOTFIX_SETTINGS` | `/system/hotfix/settings` | `GET` | `read` | `client.read(endpoint)` | None *(singleton)* | Automatic hotfix and critical patch installation policy |
| `System.PATTERN_UPDATES_SETTINGS` | `/system/pattern-updates/settings` | `GET`, `PATCH` | `read`, `update` | `client.read(endpoint)`<br>`client.update(endpoint, data=data)` | Body: JSON payload | Threat intelligence and pattern update schedules |
| `System.SECURITY_UPDATES` | `/system/security-updates` | `GET` | `read` | `client.read(endpoint)` | None *(singleton)* | Available firmware upgrades and security release status |

[↑ Back to Table of Domains](#table-of-domains) &nbsp;•&nbsp; [↑ Back to Top](#top)

---
