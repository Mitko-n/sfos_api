"""Tests for StrEnum domain classes."""

from sfos_api import (
    Authentication,
    Firewall,
    FirewallHealthCheck,
    IntrusionPrevention,
    Nat,
    Network,
    Routing,
    SdWan,
    TlsInspection,
)


def test_strenum_is_string():
    assert isinstance(Network.ZONES, str)
    assert Network.ZONES == "/network/zones"
    assert str(Network.ZONES) == "/network/zones"


def test_domain_constants():
    assert Network.ADDRESSES_IPV4 == "/network/addresses/ipv4"
    assert Firewall.RULES_IPV4 == "/firewall/rules/ipv4"
    assert Nat.RULES_IPV4 == "/nat/rules/ipv4"
    assert Routing.STATIC_UNICAST_ROUTES_IPV4 == "/routing/static-unicast-routes/ipv4"
    assert SdWan.ROUTES_IPV4 == "/sd-wan/routes/ipv4"
    assert TlsInspection.RULES_IPV4 == "/tls-inspection/rules/ipv4"


def test_authentication_endpoints():
    assert Authentication.SERVERS_RADIUS == "/authentication/servers/radius"
    assert Authentication.SERVERS_LDAP_FETCH_BASE_DN == "/authentication/servers/ldap/fetch-base-dn"


def test_consolidated_endpoints():
    assert FirewallHealthCheck.POLICIES == "/firewall-health-check/policies"
    assert IntrusionPrevention.SIGNATURE_ATTRIBUTES == "/intrusion-prevention/signature-attributes"
