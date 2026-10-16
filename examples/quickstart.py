"""End-to-end quickstart demonstration for sfos_api.

Demonstrates:
- Client initialization
- Domain-scoped StrEnum endpoints (Network, Firewall, Nat, Authentication)
- Full CRUD operations (create, read, update, delete)
- Rule reordering (move)
- Standalone and parameterized actions (create)
- Structured error handling
"""

import sys

from common import handle_example_error, print_data, setup_client

from sfos_api import (
    Authentication,
    Firewall,
    Network,
    NotFoundError,
)


def main() -> None:
    """End-to-end quickstart demonstration for sfos_api."""
    print("==================================================")
    print(" Sophos Firewall OS (SFOS) REST API - Demo")
    print(" Using StrEnum Domain Classes")
    print("==================================================\n")

    try:
        client = setup_client()
    except Exception as e:
        print(f"Configuration error: {e}")
        print("Please ensure your .env file contains SFOS_HOST and SFOS_API_KEY.")
        sys.exit(1)

    with client:
        # 1. READ COLLECTION (Auto-paginated)
        print("1. Reading network zones...")
        try:
            zones = client.read(Network.ZONES)
            print("Successfully retrieved zones:")
            print_data(zones)
        except Exception as e:
            handle_example_error(e, "reading network zones")

        # 2. READ WITH FILTER
        print("\n2. Reading IPv4 firewall rules with query parameters...")
        try:
            rules = client.read(Firewall.RULES_IPV4, pageSize=10)
            print("Firewall rules summary:")
            print_data(rules)
        except Exception as e:
            handle_example_error(e, "reading firewall rules")

        # 3. CREATE RESOURCE
        test_host = {
            "name": "Demo_Host_Light",
            "type": "ipv4Address",
            "ipv4Address": "198.51.100.42",
        }
        print(f"\n3. Creating IPv4 host object '{test_host['name']}'...")
        try:
            res = client.create(Network.ADDRESSES_IPV4, test_host)
            print("Host created:")
            print_data(res)
        except Exception as e:
            handle_example_error(e, "creating host object", test_host["name"])

        # 4. READ SINGLE RESOURCE
        print(f"\n4. Reading host object '{test_host['name']}'...")
        try:
            host_info = client.read(Network.ADDRESSES_IPV4, test_host["name"])
            print("Host details:")
            print_data(host_info)
        except Exception as e:
            handle_example_error(e, "reading host object", test_host["name"])

        # 5. UPDATE RESOURCE (JSON Merge Patch)
        print(f"\n5. Updating host object '{test_host['name']}'...")
        try:
            res = client.update(
                Network.ADDRESSES_IPV4,
                test_host["name"],
                data={"description": "Provisioned via sfos_api"},
            )
            print("Host updated successfully.")
        except Exception as e:
            handle_example_error(e, "updating host object", test_host["name"])

        # 6. RULE REORDERING (Convenience Wrapper)
        print("\n6. Demonstrating rule reordering (move)...")
        try:
            client.move(
                Firewall.RULES_IPV4,
                {"id": "rule-42", "position": "top"},
            )
            print("Rule moved successfully.")
        except NotFoundError:
            print("Note: Example rule 'rule-42' not found on firewall; move syntax verified.")
        except Exception as e:
            handle_example_error(e, "moving firewall rule")

        # 7. SERVICE CONNECTIVITY TEST (test_connection)
        print("\n7. Testing Active Directory connection diagnostics...")
        try:
            test_res = client.test_connection(
                Authentication.SERVERS_ACTIVE_DIRECTORY,
                data={
                    "name": "AD",
                    "serverAddress": {"ipv4Address": "192.168.10.50"},
                    "connectionSecurity": "none",
                    "port": 389,
                    "netBIOSDomain": "sfos",
                    "adminUsername": "adread",
                    "password": "Sophos1985!!",
                    "domainName": "sfos.local",
                    "searchQueries": ["dc=sfos,dc=local"],
                },
            )
            print("Connection test result:")
            print_data(test_res)
        except Exception as e:
            handle_example_error(e, "testing Active Directory connection")

        # 8. CLEANUP / DELETE
        print(f"\n8. Deleting host object '{test_host['name']}'...")
        try:
            client.delete(Network.ADDRESSES_IPV4, test_host["name"])
            print("Host deleted successfully.")
        except Exception as e:
            handle_example_error(e, "deleting host object", test_host["name"])

    print("\nDemo completed successfully!")


if __name__ == "__main__":
    main()
