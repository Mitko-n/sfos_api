"""Lightweight SFOS REST API endpoint definitions using StrEnum."""

from __future__ import annotations

from enum import StrEnum


class AclExceptionRules(StrEnum):
    """Endpoints for the AclExceptionRules domain."""

    IPV4 = "/acl-exception-rules/ipv4"
    IPV6 = "/acl-exception-rules/ipv6"


class ActiveThreatResponse(StrEnum):
    """Endpoints for the ActiveThreatResponse domain."""

    MDR_THREAT_FEED_SETTINGS = "/active-threat-response/mdr-threat-feed/settings"
    SOPHOS_X_OPS_THREAT_FEED_SETTINGS = "/active-threat-response/sophos-x-ops-threat-feed/settings"
    THIRDPARTY_THREAT_FEEDS = "/active-threat-response/thirdparty-threat-feeds"
    THIRDPARTY_THREAT_FEEDS_BY_ID_OR_NAME_SYNCHRONIZE = "/active-threat-response/thirdparty-threat-feeds/{idOrName}/synchronize"
    THREAT_EXCLUSIONS = "/active-threat-response/threat-exclusions"


class Administration(StrEnum):
    """Endpoints for the Administration domain."""

    ACCESS_PERMISSIONS = "/administration/access/permissions"
    ACCESS_PROFILES = "/administration/access/profiles"
    API_SETTINGS = "/administration/api-settings"
    MESSAGES = "/administration/messages"
    PORTAL_SETTINGS = "/administration/portal-settings"
    SCHEDULES = "/administration/schedules"
    SUPPORT_ACCESS = "/administration/support-access"
    SYSTEM_SETTINGS = "/administration/system-settings"


class Application(StrEnum):
    """Endpoints for the Application domain."""

    APPS = "/application/apps"
    ATTRIBUTES = "/application/attributes"
    CATEGORIES = "/application/categories"
    OBJECTS = "/application/objects"
    POLICIES = "/application/policies"


class Authentication(StrEnum):
    """Endpoints for the Authentication domain."""

    ADMIN_USER_PASSWORD = "/authentication/admin-user/password"
    CAPTIVE_PORTAL_APPEARANCE = "/authentication/captive-portal/appearance"
    CLIENTS_GLOBAL_SETTINGS = "/authentication/clients/global-settings"
    CLIENTS_TRANSPARENT_AUTH_SUITE_COLLECTORS = "/authentication/clients/transparent-auth-suite/collectors"
    CLIENTS_TRANSPARENT_AUTH_SUITE_SETTINGS = "/authentication/clients/transparent-auth-suite/settings"
    CLIENTS_TRANSPARENT_AUTH_SUITE_VPN_SOURCE_NETWORKS = "/authentication/clients/transparent-auth-suite/vpn-source-networks"
    GUEST_USER_SETTINGS_SMS_GATEWAYS = "/authentication/guest-user-settings/sms-gateways"
    LIVE_USERS = "/authentication/live-users"
    LIVE_USERS_DISCONNECT = "/authentication/live-users/disconnect"
    LOGIN_SECURITY_SETTINGS = "/authentication/login/security-settings"
    MULTI_FACTOR_AUTHENTICATION_TOTP_SETTINGS = "/authentication/multi-factor-authentication/totp-settings"
    MULTI_FACTOR_AUTHENTICATION_TOTP_TOKENS = "/authentication/multi-factor-authentication/totp-tokens"
    MULTI_FACTOR_AUTHENTICATION_TOTP_TOKENS_HARDWARE_TOKENS = "/authentication/multi-factor-authentication/totp-tokens/hardware-tokens"
    MULTI_FACTOR_AUTHENTICATION_TOTP_TOKENS_SOFTWARE_TOKENS = "/authentication/multi-factor-authentication/totp-tokens/software-tokens"
    PASSWORD_COMPLEXITY_ADMINISTRATIVE_USERS = "/authentication/password-complexity/administrative-users"
    PASSWORD_COMPLEXITY_NETWORK_USERS = "/authentication/password-complexity/network-users"
    POLICIES_ACCESS_TIMES = "/authentication/policies/access-times"
    POLICIES_NETWORK_TRAFFIC_QUOTAS = "/authentication/policies/network-traffic-quotas"
    POLICIES_SURFING_QUOTAS = "/authentication/policies/surfing-quotas"
    SERVERS = "/authentication/servers"
    SERVERS_ACTIVE_DIRECTORY = "/authentication/servers/active-directory"
    SERVERS_ACTIVE_DIRECTORY_BY_ID_OR_NAME_FETCH_GROUPS = "/authentication/servers/active-directory/{idOrName}/fetch-groups"
    SERVERS_GENERIC_IDP_SSO = "/authentication/servers/generic-idp-sso"
    SERVERS_GENERIC_IDP_SSO_BY_ID_OR_NAME_FETCH_GROUPS = "/authentication/servers/generic-idp-sso/{idOrName}/fetch-groups"
    SERVERS_GENERIC_IDP_SSO_OIDC_DISCOVERY = "/authentication/servers/generic-idp-sso/oidc-discovery"
    SERVERS_LDAP = "/authentication/servers/ldap"
    SERVERS_LDAP_FETCH_BASE_DN = "/authentication/servers/ldap/fetch-base-dn"
    SERVERS_RADIUS = "/authentication/servers/radius"
    SERVERS_TACACS = "/authentication/servers/tacacs"
    SERVER_PRIORITY_LIST_ADMINISTRATIVE_ACCESS = "/authentication/server-priority-list/administrative-access"
    SERVER_PRIORITY_LIST_DEFAULT = "/authentication/server-priority-list/default"
    SERVER_PRIORITY_LIST_USER_PORTAL_ACCESS = "/authentication/server-priority-list/user-portal-access"
    SERVER_PRIORITY_LIST_VPN_ACCESS = "/authentication/server-priority-list/vpn-access"
    SERVICES_CHROMEBOOK_SSO = "/authentication/services/chromebook-sso"
    SERVICES_RADIUS_ACCOUNTING_SSO = "/authentication/services/radius-accounting-sso"
    USERS = "/authentication/users"
    USERS_ADMINISTRATORS = "/authentication/users/administrators"
    USERS_NETWORK_USERS = "/authentication/users/network-users"
    USERS_NETWORK_USERS_LOGIN = "/authentication/users/network-users/login"
    USERS_NETWORK_USERS_LOGOUT = "/authentication/users/network-users/logout"
    USER_GROUPS = "/authentication/user-groups"
    USER_GROUPS_SET_FALLBACK_GROUP = "/authentication/user-groups/set-fallback-group"
    WEB_SETTINGS = "/authentication/web-settings"


class Certificate(StrEnum):
    """Endpoints for the Certificate domain."""

    CERTIFICATES = "/certificate/certificates"
    CERTIFICATES_CERTIFICATE_SIGNING_REQUESTS = "/certificate/certificates/certificate-signing-requests"
    CERTIFICATES_EXTERNAL = "/certificate/certificates/external"
    CERTIFICATES_INTERNAL = "/certificate/certificates/internal"
    CERTIFICATE_AUTHORITIES = "/certificate/certificate-authorities"
    CERTIFICATE_AUTHORITIES_BUILT_IN_DEFAULT_CA = "/certificate/certificate-authorities/built-in/default-ca"
    CERTIFICATE_AUTHORITIES_BUILT_IN_DEFAULT_CA_REGENERATE = "/certificate/certificate-authorities/built-in/default-ca/regenerate"
    CERTIFICATE_REVOCATION_LISTS = "/certificate/certificate-revocation-lists"


class DenialOfService(StrEnum):
    """Endpoints for the DenialOfService domain."""

    ATTACKS_BY_FLOOD_ATTACK_TYPE = "/denial-of-service/attacks/{floodAttackType}"
    ATTACKS_SUMMARY = "/denial-of-service/attacks/summary"
    POLICIES = "/denial-of-service/policies"
    SETTINGS = "/denial-of-service/settings"


class Firewall(StrEnum):
    """Endpoints for the Firewall domain."""

    RULES_IPV4 = "/firewall/rules/ipv4"
    RULES_IPV6 = "/firewall/rules/ipv6"


class FirewallHealthCheck(StrEnum):
    """Endpoints for the FirewallHealthCheck domain."""

    POLICIES = "/firewall-health-check/policies"
    POLICIES_SUMMARY = "/firewall-health-check/policies/summary"


class IntrusionPrevention(StrEnum):
    """Endpoints for the IntrusionPrevention domain."""

    CUSTOM_SIGNATURES = "/intrusion-prevention/custom-signatures"
    POLICIES = "/intrusion-prevention/policies"
    SETTINGS = "/intrusion-prevention/settings"
    SIGNATURE_ATTRIBUTES = "/intrusion-prevention/signature-attributes"


class IpsecVpn(StrEnum):
    """Endpoints for the IpsecVpn domain."""

    PROFILES = "/ipsec-vpn/profiles"
    REMOTE_ACCESS_SETTINGS = "/ipsec-vpn/remote-access/settings"
    SITE_TO_SITE_CONNECTIONS_IPV4 = "/ipsec-vpn/site-to-site/connections/ipv4"
    SITE_TO_SITE_CONNECTIONS_POLICY_BASED_IPV4 = "/ipsec-vpn/site-to-site/connections/policy-based/ipv4"
    SITE_TO_SITE_CONNECTIONS_ROUTE_BASED_IPV4 = "/ipsec-vpn/site-to-site/connections/route-based/ipv4"
    SITE_TO_SITE_FAILOVER_GROUPS = "/ipsec-vpn/site-to-site/failover-groups"
    SITE_TO_SITE_LIVE_CONNECTIONS_IPV4 = "/ipsec-vpn/site-to-site/live-connections/ipv4"


class Logging(StrEnum):
    """Endpoints for the Logging domain."""

    LOG_ATTRIBUTES_COMPONENTS = "/logging/log-attributes/components"
    LOG_ATTRIBUTES_TYPES = "/logging/log-attributes/types"
    LOG_DESTINATIONS_CENTRAL_FIREWALL_REPORTING = "/logging/log-destinations/central-firewall-reporting"
    LOG_DESTINATIONS_LOG_VIEWER = "/logging/log-destinations/log-viewer"
    LOG_DESTINATIONS_SYSLOG_SERVERS = "/logging/log-destinations/syslog-servers"
    LOG_DESTINATIONS_SYSLOG_SERVERS_BY_ID_OR_NAME_LOGS = "/logging/log-destinations/syslog-servers/{idOrName}/logs"
    LOG_SETTINGS = "/logging/log-settings"


class MalwareProtection(StrEnum):
    """Endpoints for the MalwareProtection domain."""

    SETTINGS = "/malware-protection/settings"


class Monitoring(StrEnum):
    """Endpoints for the Monitoring domain."""

    NETFLOW_COLLECTORS = "/monitoring/netflow/collectors"
    SNMP_AGENT_CONFIGURATION = "/monitoring/snmp/agent-configuration"
    SNMP_COMMUNITIES = "/monitoring/snmp/communities"
    SNMP_USERS = "/monitoring/snmp/users"


class Nat(StrEnum):
    """Endpoints for the Nat domain."""

    RULES_IPV4 = "/nat/rules/ipv4"
    RULES_IPV6 = "/nat/rules/ipv6"


class Network(StrEnum):
    """Endpoints for the Network domain."""

    ADDRESSES_FQDN = "/network/addresses/fqdn"
    ADDRESSES_IPV4 = "/network/addresses/ipv4"
    ADDRESSES_IPV6 = "/network/addresses/ipv6"
    ADDRESSES_MAC = "/network/addresses/mac"
    ADDRESS_GROUPS_COUNTRY = "/network/address-groups/country"
    ADDRESS_GROUPS_FQDN = "/network/address-groups/fqdn"
    ADDRESS_GROUPS_IPV4 = "/network/address-groups/ipv4"
    ADDRESS_GROUPS_IPV6 = "/network/address-groups/ipv6"
    CELLULAR_WAN_CONNECT_MODEM = "/network/cellular-wan/connect-modem"
    CELLULAR_WAN_DISCONNECT_MODEM = "/network/cellular-wan/disconnect-modem"
    CELLULAR_WAN_MODEM_SETTINGS = "/network/cellular-wan/modem-settings"
    CELLULAR_WAN_MODEM_STATUS = "/network/cellular-wan/modem-status"
    CELLULAR_WAN_RECOMMENDED_MODEM_SETTINGS = "/network/cellular-wan/recommended-modem-settings"
    CELLULAR_WAN_RESET_MODEM = "/network/cellular-wan/reset-modem"
    CELLULAR_WAN_SETTINGS = "/network/cellular-wan/settings"
    DHCP_RELAYS_IPV4 = "/network/dhcp/relays/ipv4"
    DHCP_RELAYS_IPV6 = "/network/dhcp/relays/ipv6"
    DHCP_SERVER_SERVERS_IPV4 = "/network/dhcp/server/servers/ipv4"
    DHCP_SERVER_SERVERS_IPV6 = "/network/dhcp/server/servers/ipv6"
    DHCP_SERVER_SETTINGS_IPV4 = "/network/dhcp/server/settings/ipv4"
    DNS_HOST_ENTRIES = "/network/dns/host-entries"
    DNS_PROTECTION_STATUS = "/network/dns/protection/status"
    DNS_REQUEST_ROUTES = "/network/dns/request-routes"
    DNS_SETTINGS = "/network/dns/settings"
    INTERFACES_NETWORK_INTERFACES = "/network/interfaces/network-interfaces"
    MDNS_REFLECTOR = "/network/mdns-reflector"
    NEIGHBORS_SETTINGS = "/network/neighbors/settings"
    NEIGHBORS_STATIC_IPV4 = "/network/neighbors/static/ipv4"
    NEIGHBORS_STATIC_IPV6 = "/network/neighbors/static/ipv6"
    ROUTER_ADVERTISEMENTS = "/network/router-advertisements"
    SERVICES = "/network/services"
    SERVICE_GROUPS = "/network/service-groups"
    ZONES = "/network/zones"


class Notification(StrEnum):
    """Endpoints for the Notification domain."""

    NOTIFICATIONS = "/notification/notifications"


class Routing(StrEnum):
    """Endpoints for the Routing domain."""

    GATEWAYS_CUSTOM_IPV4 = "/routing/gateways/custom/ipv4"
    GATEWAYS_CUSTOM_IPV6 = "/routing/gateways/custom/ipv6"
    GATEWAYS_IPV4 = "/routing/gateways/ipv4"
    GATEWAYS_IPV6 = "/routing/gateways/ipv6"
    GATEWAYS_WAN_IPV4 = "/routing/gateways/wan/ipv4"
    GATEWAYS_WAN_IPV6 = "/routing/gateways/wan/ipv6"
    STATIC_MULTICAST_ROUTES_IPV4 = "/routing/static-multicast-routes/ipv4"
    STATIC_MULTICAST_SETTINGS = "/routing/static-multicast-settings"
    STATIC_UNICAST_ROUTES_IPV4 = "/routing/static-unicast-routes/ipv4"
    STATIC_UNICAST_ROUTES_IPV6 = "/routing/static-unicast-routes/ipv6"


class SdWan(StrEnum):
    """Endpoints for the SdWan domain."""

    ROUTES_IPV4 = "/sd-wan/routes/ipv4"
    ROUTES_IPV6 = "/sd-wan/routes/ipv6"


class SophosCentral(StrEnum):
    """Endpoints for the SophosCentral domain."""

    DEREGISTER = "/sophos-central/deregister"
    REGISTER = "/sophos-central/register"
    SETTINGS = "/sophos-central/settings"
    STATUS = "/sophos-central/status"


class SpoofProtection(StrEnum):
    """Endpoints for the SpoofProtection domain."""

    SETTINGS = "/spoof-protection/settings"
    TRUSTED_MACS = "/spoof-protection/trusted-macs"
    TRUSTED_MACS_IMPORT = "/spoof-protection/trusted-macs/import"


class SslVpn(StrEnum):
    """Endpoints for the SslVpn domain."""

    CLIENTLESS_BOOKMARKS = "/ssl-vpn/clientless/bookmarks"
    CLIENTLESS_BOOKMARK_GROUPS = "/ssl-vpn/clientless/bookmark-groups"
    CLIENTLESS_POLICIES = "/ssl-vpn/clientless/policies"
    GLOBAL_SETTINGS = "/ssl-vpn/global-settings"
    REMOTE_ACCESS_POLICIES = "/ssl-vpn/remote-access/policies"


class System(StrEnum):
    """Endpoints for the System domain."""

    BACKUP_SETTINGS = "/system/backup/settings"
    HOTFIX_SETTINGS = "/system/hotfix/settings"
    PATTERN_UPDATES_SETTINGS = "/system/pattern-updates/settings"
    SECURITY_UPDATES = "/system/security-updates"


class TlsInspection(StrEnum):
    """Endpoints for the TlsInspection domain."""

    DECRYPTION_PROFILES = "/tls-inspection/decryption-profiles"
    RULES_IPV4 = "/tls-inspection/rules/ipv4"
    SETTINGS = "/tls-inspection/settings"


class TrafficShaping(StrEnum):
    """Endpoints for the TrafficShaping domain."""

    POLICIES = "/traffic-shaping/policies"
    SETTINGS = "/traffic-shaping/settings"


class Waf(StrEnum):
    """Endpoints for the Waf domain."""

    AUTHENTICATION_POLICIES = "/waf/authentication/policies"
    AUTHENTICATION_TEMPLATES = "/waf/authentication/templates"
    PROTECTION_POLICIES = "/waf/protection/policies"
    SERVERS = "/waf/servers"


class Web(StrEnum):
    """Endpoints for the Web domain."""

    CATEGORIES = "/web/categories"
    CONTENT_FILTERS = "/web/content-filters"
    EXCEPTIONS = "/web/exceptions"
    POLICIES = "/web/policies"
    SCAN_SETTINGS = "/web/scan-settings"
    URL_GROUPS = "/web/url-groups"
    USER_ACTIVITIES = "/web/user-activities"
    USER_NOTIFICATIONS = "/web/user-notifications"


class Wireless(StrEnum):
    """Endpoints for the Wireless domain."""

    HOTSPOT_HOTSPOTS = "/wireless/hotspot/hotspots"
    HOTSPOT_SETTINGS = "/wireless/hotspot/settings"
    HOTSPOT_VOUCHERS = "/wireless/hotspot/vouchers"


class ZeroDayProtection(StrEnum):
    """Endpoints for the ZeroDayProtection domain."""

    SETTINGS = "/zero-day-protection/settings"


__all__ = [
    "AclExceptionRules",
    "ActiveThreatResponse",
    "Administration",
    "Application",
    "Authentication",
    "Certificate",
    "DenialOfService",
    "Firewall",
    "FirewallHealthCheck",
    "IntrusionPrevention",
    "IpsecVpn",
    "Logging",
    "MalwareProtection",
    "Monitoring",
    "Nat",
    "Network",
    "Notification",
    "Routing",
    "SdWan",
    "SophosCentral",
    "SpoofProtection",
    "SslVpn",
    "System",
    "TlsInspection",
    "TrafficShaping",
    "Waf",
    "Web",
    "Wireless",
    "ZeroDayProtection",
]
