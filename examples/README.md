# SFOS API - Interactive Examples & Notebooks

[![Python 3.11+](https://img.shields.io/badge/Python-3.11%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](../LICENSE)
[![Development Status: Beta 0.5.0](https://img.shields.io/badge/Status-Beta%200.5.0-orange.svg)](https://pypi.org/project/sfos-api/)

Executable Jupyter notebook examples and standalone Python scripts demonstrating the `sfos-api` client against Sophos Firewall OS (SFOS).

---

## 📁 Directory Organization

| File / Script | Description |
|---|---|
| [**`ipv4_addresses.ipynb`**](./ipv4_addresses.ipynb) | IPv4 address CRUD operations using Domain StrEnum objects |
| [**`fqdns.ipynb`**](./fqdns.ipynb) | FQDN host definitions, wildcards, and domain queries |
| [**`ipv4_address_groups.ipynb`**](./ipv4_address_groups.ipynb) | Address groups and member management |
| [**`zones.ipynb`**](./zones.ipynb) | Network zones (LAN, DMZ, WAN) creation and management |
| [**`services.ipynb`**](./services.ipynb) | TCP, UDP, ICMP custom services and port specifications |
| [**`service_groups.ipynb`**](./service_groups.ipynb) | Service group operations and membership |
| [**`ipv4_firewall_rules.ipynb`**](./ipv4_firewall_rules.ipynb) | Firewall rule creation, priority ordering, and logging |
| [**`ipv4_nat_rules.ipynb`**](./ipv4_nat_rules.ipynb) | IPv4 SNAT/DNAT rules, masquerading, and priority ordering (`client.move`) |
| [**`nested_parameterized_resources.ipynb`**](./nested_parameterized_resources.ipynb) | In-path substitution examples (syslog logs, AD groups, threat feeds, DoS) |
| [**`quickstart.py`**](./quickstart.py) | Standalone Python script for end-to-end CRUD lifecycle |
| [**`common.py`**](./common.py) | Shared helpers (config, client factory, error handling) |

---

## 🚀 Quick Setup & Prerequisites

### 1. Environment Configuration

Copy the example environment configuration into `.env` (either at the repository root or inside `examples/`):

```bash
cp examples/.env.example examples/.env
```

Edit `examples/.env` with your firewall credentials:

```ini
SFOS_HOST=192.168.1.1              # Firewall IP or hostname (no https:// prefix)
SFOS_API_KEY=your_api_key_here      # API Key with appropriate admin privileges
SFOS_PORT=4444                      # WebAdmin / API Port (default: 4444)
SFOS_VERIFY_SSL=false               # Set to true if using valid public SSL certificates
SFOS_TIMEOUT=30.0                   # HTTP timeout in seconds
```

### 2. Install Editable Package & Jupyter

```bash
# Install sfos-api in editable mode from workspace root
pip install -e .

# Install Jupyter notebook dependencies
pip install jupyter ipython
```

### 3. Launch Notebooks

You can run the notebooks directly inside **VS Code / Cursor** with the Jupyter extension, or launch the classic Jupyter server:

```bash
# Launch notebooks:
jupyter notebook examples/

# Or run the standalone script:
python examples/quickstart.py
```

---

## 📚 Example Notebooks

| Notebook | Domain | Key Operations Covered |
|---|---|---|
| [`ipv4_addresses.ipynb`](./ipv4_addresses.ipynb) | `Network` | Single IP, ranges, subnets, lists, auto-pagination, filters |
| [`fqdns.ipynb`](./fqdns.ipynb) | `Network` | FQDN host definitions, wildcards, domain queries |
| [`ipv4_address_groups.ipynb`](./ipv4_address_groups.ipynb) | `Network` | Creating and updating address group members |
| [`zones.ipynb`](./zones.ipynb) | `Network` | Creating, updating, and querying network zones (LAN, DMZ, WAN) |
| [`services.ipynb`](./services.ipynb) | `Network` | TCP, UDP, ICMP custom services and port specifications |
| [`service_groups.ipynb`](./service_groups.ipynb) | `Network` | Grouping multiple network services |
| [`ipv4_firewall_rules.ipynb`](./ipv4_firewall_rules.ipynb) | `Firewall` | Creating accept/drop rules, priority ordering (`client.move`), logging |
| [`ipv4_nat_rules.ipynb`](./ipv4_nat_rules.ipynb) | `Nat` | SNAT, DNAT, Masquerade, rule ordering (`client.move`) |
| [`nested_parameterized_resources.ipynb`](./nested_parameterized_resources.ipynb) | `Logging`, `Authentication`, `ActiveThreatResponse`, `DenialOfService` | In-path substitution: Syslog logs (`GET`/`PATCH`), AD `fetch-groups`, Threat feed `synchronize`, DoS attack stats |

---

## 🛠️ Shared Helpers (`common.py`)

All notebooks import helper functions from [`examples/common.py`](./common.py):
- `setup_client()`: Reads environment variables and initializes an `SFOSClient` instance.
- `print_data(data, keys=None)`: Pretty-prints responses as formatted JSON or a condensed indexed table.
- `handle_example_error(e, action_desc, resource_name)`: Standardized error printing with guidance.
