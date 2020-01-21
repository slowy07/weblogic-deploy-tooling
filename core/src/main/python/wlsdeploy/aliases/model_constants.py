"""
Copyright (c) 2017, 2020, Oracle Corporation and/or its affiliates.  All rights reserved.
Licensed under the Universal Permissive License v 1.0 as shown at https://oss.oracle.com/licenses/upl.
"""

# lists may be represented in the model as comma-separated strings
MODEL_LIST_DELIMITER = ','
KSS_KEYSTORE_TYPE = 'kss'
KSS_KEYSTORE_FILE_INDICATOR = 'kss:'


# names of model elements, alphabetically

ACTIVE_DIRECTORY_AUTHENTICATOR = 'ActiveDirectoryAuthenticator'
ADJUDICATOR = 'Adjudicator'
ADMIN_CONSOLE = 'AdminConsole'
ADMIN_PASSWORD = 'AdminPassword'
ADMIN_SERVER_NAME = 'AdminServerName'
ADMIN_USERNAME = 'AdminUserName'
APP_DEPLOYMENTS = 'appDeployments'
APP_DIR = 'AppDir'
APPEND = 'append'
APPLICATION = 'Application'
RCU_DB_INFO = 'RCUDbInfo'
OPSS_SECRETS = 'OPSSSecrets'
RCU_PREFIX = 'rcu_prefix'
RCU_SCHEMA_PASSWORD = 'rcu_schema_password'
RCU_ADMIN_PASSWORD = 'rcu_admin_password'
RCU_DB_CONN = 'rcu_db_conn_string'
RCU_VARIABLES = 'rcu_variables'
USE_ATP = 'useATP'
ATP_TNS_ENTRY = 'tns.alias'
ATP_DEFAULT_TABLESPACE = 'atp.default.tablespace'
ATP_TEMPORARY_TABLESPACE = 'atp.temp.tablespace'
ATP_ADMIN_USER = 'atp.admin.user'
AUDITOR = 'Auditor'
AUTHENTICATION_PROVIDER = 'AuthenticationProvider'
AUTHORIZER = 'Authorizer'
CAPACITY = 'Capacity'
CERT_PATH_PROVIDER = 'CertPathProvider'
CERTIFICATE_REGISTRY = 'CertificateRegistry'
CLASSPATH = 'ClassPath'
CLIENT_PARAMS = 'ClientParams'
CLUSTER = 'Cluster'
CLUSTER_MESSAGING_MODE = 'ClusterMessagingMode'
COHERENCE_ACTIVE_DIRECTORY = 'ActiveDirectory'
COHERENCE_CACHE_CONFIG_FILE = 'CacheConfigurationFile'
COHERENCE_ADDRESS_PROVIDERS = 'CoherenceAddressProviders'
COHERENCE_ADDRESS_PROVIDER = 'CoherenceAddressProvider'
COHERENCE_CACHE = 'CoherenceCache'
COHERENCE_CACHE_CONFIG = 'CoherenceCacheConfig'
COHERENCE_CLUSTER_SYSTEM_RESOURCE = 'CoherenceClusterSystemResource'
COHERENCE_CLUSTER_PARAMS = 'CoherenceClusterParams'
COHERENCE_CUSTOM_CLUSTER_CONFIGURATION = 'CustomClusterConfigurationFileName'
COHERENCE_FEDERATION_PARAMS = 'CoherenceFederationParams'
COHERENCE_INIT_PARAM = 'CoherenceInitParam'
COHERENCE_LOGGING_PARAMS = 'CoherenceLoggingParams'
COHERENCE_PARTITION_CACHE_CONFIGS = 'CoherencePartitionCacheConfig'
COHERENCE_PERSISTENCE_PARAMS = 'CoherencePersistenceParams'
COHERENCE_RESOURCE = 'CoherenceResource'
COHERENCE_SERVICE = 'CoherenceService'
COHERENCE_SNAPSHOT_DIRECTORY = 'SnapshotDirectory'
COHERENCE_SOCKET_ADDRESS = 'CoherenceSocketAddress'
COHERENCE_TRASH_DIRECTORY = 'TrashDirectory'
COHERENCE_WELL_KNOWN_ADDRESSES = 'CoherenceClusterWellKnownAddresses'
COHERENCE_WELL_KNOWN_ADDRESS = 'CoherenceClusterWellKnownAddress'
CONFIGURATION_PROPERTY = 'ConfigurationProperty'
CONNECTION_FACTORY = 'ConnectionFactory'
CONTEXT_CASE = 'ContextCase'
CONTEXT_REQUEST_CLASS = 'ContextRequestClass'
CPU_UTILIZATION = 'CpuUtilization'
CREATE_TABLE_DDL_FILE = 'CreateTableDDLFile'
CREDENTIAL = 'Credential'
CREDENTIAL_ENCRYPTED = 'CredentialEncrypted'
CREDENTIAL_MAPPER = 'CredentialMapper'
CUSTOM_DBMS_AUTHENTICATOR = 'CustomDBMSAuthenticator'
DATA_SOURCE = 'DataSource'
DEFAULT_ADJUDICATOR = 'DefaultAdjudicator'
DEFAULT_ADMIN_SERVER_NAME = 'AdminServer'
DEFAULT_AUDITOR = 'DefaultAuditor'
DEFAULT_AUTHENTICATOR = 'DefaultAuthenticator'
DEFAULT_AUTHORIZER = 'DefaultAuthorizer'
DEFAULT_CREDENTIAL_MAPPER = 'DefaultCredentialMapper'
DEFAULT_DELIVERY_PARAMS = 'DefaultDeliveryParams'
DEFAULT_IDENTITY_ASSERTER = 'DefaultIdentityAsserter'
DEFAULT_ROLE_MAPPER = 'DefaultRoleMapper'
DEFAULT_WLS_DOMAIN_NAME = 'base_domain'
DELIVERY_FAILURE_PARAMS = 'DeliveryFailureParams'
DELIVERY_PARAMS_OVERRIDES = 'DeliveryParamsOverrides'
DESTINATION_KEY = 'DestinationKey'
DIRECTORY = 'Directory'
DISTRIBUTED_QUEUE = 'DistributedQueue'
DISTRIBUTED_QUEUE_MEMBER = 'DistributedQueueMember'
DISTRIBUTED_TOPIC = 'DistributedTopic'
DISTRIBUTED_TOPIC_MEMBER = 'DistributedTopicMember'
DOMAIN = 'Domain'
DOMAIN_NAME = 'Name'
DOMAIN_INFO = 'domainInfo'
DOMAIN_INFO_ALIAS = 'DomainInfo'
DOMAIN_LIBRARIES = 'domainLibraries'
DOMAIN_SCRIPTS = 'domainBin'
DYNAMIC_SERVERS = 'DynamicServers'
EMBEDDED_LDAP = 'EmbeddedLDAP'
ERROR_DESTINATION = 'ErrorDestination'
EXECUTE_QUEUE = 'ExecuteQueue'
EXPRESSION = 'Expression'
FAIR_SHARE_REQUEST_CLASS = 'FairShareRequestClass'
FILE_OPEN = 'FileOpen'
FILE_STORE = 'FileStore'
FLOW_CONTROL_PARAMS = 'FlowControlParams'
FOREIGN_CONNECTION_FACTORY = 'ForeignConnectionFactory'
FOREIGN_DESTINATION = 'ForeignDestination'
FOREIGN_JNDI_PROVIDER = 'ForeignJNDIProvider'
FOREIGN_JNDI_PROVIDER_OVERRIDE = 'ForeignJndiProviderOverride'
FOREIGN_JNDI_PROVIDER_LINK = 'ForeignJNDILink'
FOREIGN_SERVER = 'ForeignServer'
GROUP = 'Group'
GROUP_PARAMS = 'GroupParams'
GLOBAL_VARIABLE_SUBSTITUTION = 'VariableSubstitution'
HARVESTED_TYPE = 'HarvestedType'
HARVESTER = 'Harvester'
HEAP_DUMP_ACTION = 'HeapDumpAction'
HEAP_RETAINED = 'HeapRetained'
IMAGE_NOTIFICATION = 'ImageNotification'
INSTRUMENTATION = 'Instrumentation'
IPLANET_AUTHENTICATOR = 'IPlanetAuthenticator'
JDBC_CONNECTION_POOL_PARAMS = 'JDBCConnectionPoolParams'
JDBC_DATASOURCE_PARAMS = 'JDBCDataSourceParams'
JDBC_DRIVER_PARAMS = 'JDBCDriverParams'
JDBC_DRIVER_PARAMS_PROPERTIES = 'Properties'
JDBC_DRIVER_PARAMS_PROPERTY = 'Property'
JDBC_ORACLE_PARAMS = 'JDBCOracleParams'
JDBC_STORE = 'JDBCStore'
JDBC_SYSTEM_RESOURCE = 'JDBCSystemResource'
JDBC_SYSTEM_RESOURCE_OVERRIDE = 'JdbcSystemResourceOverride'
JDBC_RESOURCE = 'JdbcResource'
JMS_BRIDGE_DESTINATION = 'JMSBridgeDestination'
JMS_CONNECTION_CONSUMER = 'JmsConnectionConsumer'
JMS_NOTIFICATION = 'JMSNotification'
JMS_RESOURCE = 'JmsResource'
JMS_SERVER = 'JMSServer'
JMS_SESSION_POOL = 'JmsSessionPool'
JMS_SYSTEM_RESOURCE = 'JMSSystemResource'
JMS_SYSTEM_RESOURCE_OVERRIDE = 'JmsSystemResourceOverride'
JMX = 'JMX'
JMX_NOTIFICATION = 'JMXNotification'
JNDI_NAME = 'JNDIName'
JNDI_PROPERTY = 'JNDIProperty'
JTA = 'JTA'
JTA_PARTITION = 'JtaPartition'
JTA_MIGRATABLE_TARGET = 'JTAMigratableTarget'
KEY = 'Key'
KUBERNETES = 'kubernetes'
KUBERNETES_ALIAS = 'Kubernetes'
LDAP_AUTHENTICATOR = 'LDAPAuthenticator'
LDAP_X509_IDENTITY_ASSERTER = 'LDAPX509IdentityAsserter'
LIBRARY = 'Library'
LOAD_BALANCING_PARAMS = 'LoadBalancingParams'
LOG = 'Log'
LOG_FILTER = 'LogFilter'
LOG_ACTION = 'LogAction'
MACHINE = 'Machine'
MAIL_SESSION = 'MailSession'
MAIL_SESSION_OVERRIDE = 'MailSessionOverride'
MAIL_SESSION_PROPERTIES = 'Properties'
MAX_THREADS_CONSTRAINT = 'MaxThreadsConstraint'
MIGRATABLE_TARGET = 'MigratableTarget'
MIN_THREADS_CONSTRAINT = 'MinThreadsConstraint'
MESSAGE_LOGGING_PARAMS = 'MessageLoggingParams'
MESSAGING_BRIDGE = 'MessagingBridge'
MULTICAST = 'Multicast'
MULTICAST_ADDRESS = 'MulticastAddress'
MULTICAST_PORT = 'MulticastPort'
NEGOTIATE_IDENTITY_ASSERTER = 'NegotiateIdentityAsserter'
NETWORK_ACCESS_POINT = 'NetworkAccessPoint'
NM_PROPERTIES = 'NMProperties'
NM_TYPE = 'NMType'
NODE_MANAGER = 'NodeManager'
NODE_MANAGER_PW_ENCRYPTED = 'NodeManagerPasswordEncrypted'
NODE_MANAGER_USER_NAME = 'NodeManagerUsername'
NOVELL_AUTHENTICATOR = 'NovellAuthenticator'
ODL_CONFIGURATION = 'ODLConfiguration'
OPEN_LDAP_AUTHENTICATOR = 'OpenLDAPAuthenticator'
ORACLE_OID_AUTHENTICATOR = 'OracleInternetDirectoryAuthenticator'
ORACLE_OUD_AUTHENTICATOR = 'OracleUnifiedDirectoryAuthenticator'
ORACLE_OVD_AUTHENTICATOR = 'OracleVirtualDirectoryAuthenticator'
OVERLOAD_PROTECTION = 'OverloadProtection'
PARTITION = 'Partition'
PARTITION_SYSTEM_FILE = 'SystemFileSystem'
PARTITION_USER_FILE = 'UserFileSystem'
PARTITION_WORK_MANAGER = 'PartitionWorkManager'
PASSWORD_VALIDATOR = 'PasswordValidator'
PATH_SERVICE = 'PathService'
PASSWORD_ENCRYPTED = 'PasswordEncrypted'
PERSISTENT_STORE = 'PersistentStore'
PKI_CREDENTIAL_MAPPER = 'PKICredentialMapper'
PLAN_DIR = 'PlanDir'
PLAN_PATH = 'PlanPath'
PREPEND = 'prepend'
PROPERTIES = 'Properties'
PRODUCTION_MODE_ENABLED='ProductionModeEnabled'
QUEUE = 'Queue'
QUOTA = 'Quota'
REALM = 'Realm'
RECOVER_ONLY_ONCE = 'RecoverOnlyOnce'
REPLACE = 'replace'
RESOURCE_GROUP = 'ResourceGroup'
RESOURCE_GROUP_TEMPLATE = 'ResourceGroupTemplate'
RESOURCES = 'resources'
RESOURCE_MANAGEMENT = 'ResourceManagement'
RESOURCE_MANAGER = 'ResourceManager'
RESPONSE_TIME_REQUEST_CLASS = 'ResponseTimeRequestClass'
RESTFUL_MANAGEMENT_SERVICES = 'RestfulManagementServices'
REST_NOTIFICATION = 'RestNotification'
RO_SQL_AUTHENTICATOR = 'ReadOnlySQLAuthenticator'
ROLE_MAPPER = 'RoleMapper'
SAF_AGENT = 'SAFAgent'
SAF_ERROR_DESTINATION = 'SafErrorDestination'
SAF_ERROR_HANDLING = 'SAFErrorHandling'
SAF_IMPORTED_DESTINATION = 'SAFImportedDestinations'
SAF_LOGIN_CONTEXT = 'SAFLoginContext'
SAF_MESSAGE_LOG_FILE = 'JmssafMessageLogFile'
SAF_QUEUE = 'SAFQueue'
SAF_REMOTE_CONTEXT = 'SAFRemoteContext'
SAF_TOPIC = 'SAFTopic'
SAML_AUTHENTICATOR = 'SAMLAuthenticator'
SAML_CREDENTIAL_MAPPER_V2 = 'SAMLCredentialMapperV2'
SAML_IDENTITY_ASSERTER_V2 = 'SAML2IdentityAsserterV2'
SAML2_CREDENTIAL_MAPPER = 'SAML2CredentialMapper'
SAML2_IDENTITY_ASSERTER = 'SAML2IdentityAsserter'
SCRIPT_ACTION = 'ScriptAction'
SECURITY = 'Security'
SECURITY_CONFIGURATION = 'SecurityConfiguration'
SECURITY_PARAMS = 'SecurityParams'
SELF_TUNING = 'SelfTuning'
SERVER = 'Server'
SERVER_FAILURE_TRIGGER = 'ServerFailureTrigger'
SERVER_GROUP_TARGETING_LIMITS = 'ServerGroupTargetingLimits'
SERVER_POD = 'serverPod'
SERVER_START = 'ServerStart'
SERVER_START_MODE = 'ServerStartMode'
SERVER_TEMPLATE = 'ServerTemplate'
SHUTDOWN_CLASS = 'ShutdownClass'
SINGLETON_SERVICE = 'SingletonService'
SMTP_NOTIFICATION = 'SMTPNotification'
SNMP_NOTIFICATION = 'SNMPNotification'
SOURCE_DESTINATION = 'SourceDestination'
SQL_AUTHENTICATOR = 'SQLAuthenticator'
SSL = 'SSL'
STARTUP_CLASS = 'StartupClass'
STORE = 'Store'
SUB_DEPLOYMENT = 'SubDeployment'
SUB_DEPLOYMENT_NAME = 'SubDeploymentName'
SYSTEM_PASSWORD_VALIDATOR = 'SystemPasswordValidator'
TARGET = 'Target'
TARGET_DESTINATION = 'TargetDestination'
TEMPLATE = 'Template'
THREAD_DUMP_ACTION = 'ThreadDumpAction'
THRESHOLDS = 'Thresholds'
TOPIC = 'Topic'
TOPOLOGY = 'topology'
TRANSACTION_LOG_JDBC_STORE = 'TransactionLogJDBCStore'
TRANSACTION_PARAMS = 'TransactionParams'
TRIGGER = 'Trigger'
UNIFORM_DISTRIBUTED_QUEUE = 'UniformDistributedQueue'
UNIFORM_DISTRIBUTED_TOPIC = 'UniformDistributedTopic'
UNIX_MACHINE = 'UnixMachine'
UPDATE_MODE = 'UpdateMode'
USER = 'User'
VIRTUAL_TARGET = 'VirtualTarget'
VIRTUAL_USER_AUTHENTICATOR = 'VirtualUserAuthenticator'
WATCH = 'Watch'
WATCH_NOTIFICATION = 'WatchNotification'
WEBAPP_CONTAINER = 'WebAppContainer'
WEB_SERVER = 'WebServer'
WEB_SERVER_LOG = 'WebServerLog'
WEB_SERVICE = 'WebService'
WEB_SERVICE_BUFFERING = 'WebServiceBuffering'
WEB_SERVICE_LOGICAL_STORE = 'WebServiceLogicalStore'
WEB_SERVICE_PERSISTENCE = 'WebServicePersistence'
WEB_SERVICE_PHYSICAL_STORE = 'WebServicePhysicalStore'
WEB_SERVICE_REQUEST_BUFFERING_QUEUE = 'WebServiceRequestBufferingQueue'
WEB_SERVICE_RESPONSE_BUFFERING_QUEUE = 'WebServiceResponseBufferingQueue'
WEBLOGIC_CERT_PATH_PROVIDER = 'WebLogicCertPathProvider'
WORK_MANAGER = "WorkManager"
WLDF_INSTRUMENTATION_MONITOR = "WLDFInstrumentationMonitor"
WLDF_RESOURCE = "WLDFResource"
WLDF_SYSTEM_RESOURCE = "WLDFSystemResource"
WLS_ROLES = "WLSRoles"
WS_RELIABLE_DELIVERY_POLICY = 'WSReliableDeliveryPolicy'
XACML_AUTHORIZER = 'XACMLAuthorizer'
XACML_ROLE_MAPPER = 'XACMLRoleMapper'
XML_ENTITY_CACHE = 'XMLEntityCache'
XML_REGISTRY = 'XMLRegistry'

# names of attributes, alphabetically

ABSOLUTE_PLAN_PATH = 'AbsolutePlanPath'
ABSOLUTE_SOURCE_PATH = 'AbsoluteSourcePath'
ACTION = 'Action'
ACTIVE_TYPE = 'ActiveType'
ARGUMENTS = 'Arguments'
CONSTRAINED_CANDIDATE_SERVER = 'ConstrainedCandidateServer'
CUSTOM_IDENTITY_KEYSTORE_FILE = 'CustomIdentityKeyStoreFileName'
CUSTOM_TRUST_KEYSTORE_FILE = 'CustomTrustKeyStoreFileName'
DEPLOYMENT_ORDER = 'DeploymentOrder'
DESTINATION_SERVER = 'DestinationServer'
DRIVER_NAME = 'DriverName'
DRIVER_PARAMS_PROPERTY_VALUE = 'Value'
DRIVER_PARAMS_USER_PROPERTY = 'user'
DRIVER_PARAMS_TRUSTSTORE_PROPERTY = 'javax.net.ssl.trustStore'
DRIVER_PARAMS_kEYSTORE_PROPERTY = 'javax.net.ssl.keyStore'
DRIVER_PARAMS_TRUSTSTORETYPE_PROPERTY = 'javax.net.ssl.trustStoreType'
DRIVER_PARAMS_KEYSTORETYPE_PROPERTY = 'javax.net.ssl.keyStoreType'
DRIVER_PARAMS_TRUSTSTOREPWD_PROPERTY = 'javax.net.ssl.trustStorePassword'
DRIVER_PARAMS_KEYSTOREPWD_PROPERTY = 'javax.net.ssl.keyStorePassword'
DRIVER_PARAMS_NET_SERVER_DN_MATCH_PROPERTY = 'oracle.net.ssl_server_dn_match'
DRIVER_PARAMS_NET_SSL_VERSION = 'oracle.net.ssl_version'
DRIVER_PARAMS_NET_TNS_ADMIN = 'oracle.net.tns_admin'
DRIVER_PARAMS_NET_FAN_ENABLED = 'oracle.jdbc.fanEnabled'
DYNAMIC_CLUSTER_SIZE = 'DynamicClusterSize'
ENABLED = 'Enabled'
HARVESTED_ATTRIBUTE = 'HarvestedAttribute'
HARVESTED_INSTANCE = 'HarvestedInstance'
HOSTING_SERVER = 'HostingServer'
INSTALL_DIR = 'InstallDir'
LISTEN_ADDRESS = 'ListenAddress'
LISTEN_PORT = 'ListenPort'
MASKED_PASSWORD = '<Masked>'
MIME_MAPPING_FILE = 'MimeMappingFile'
NAME = 'Name'
NOTIFICATION = 'Notification'
PASSWORD = 'Password'
PATH_TO_SCRIPT = 'PathToScript'
PLAN_STAGE_MODE = 'PlanStageMode'
SECURITY_DD_MODEL = 'SecurityDDModel'
SET_OPTION_APP_DIR = 'AppDir'
SET_OPTION_DOMAIN_NAME = 'DomainName'
SET_OPTION_JAVA_HOME = 'JavaHome'
SET_OPTION_SERVER_START_MODE = 'ServerStartMode'
SOURCE_PATH = 'SourcePath'
TAGS = 'Tags'
TARGETS = 'Targets'
URL = 'URL'
USER_PREFERRED_SERVER = 'UserPreferredServer'

# Default Security Provider names and types
DEFAULT_ADJUDICATOR_NAME = 'DefaultAdjudicator'
DEFAULT_ADJUDICATOR_TYPE = DEFAULT_ADJUDICATOR
DEFAULT_AUDITOR_NAME = None
DEFAULT_AUDITOR_TYPE = DEFAULT_AUDITOR
DEFAULT_AUTHENTICATOR_NAME = 'DefaultAuthenticator'
DEFAULT_AUTHENTICATOR_TYPE = DEFAULT_AUTHENTICATOR
DEFAULT_IDENTITY_ASSERTER_NAME = 'DefaultIdentityAsserter'
DEFAULT_IDENTITY_ASSERTER_TYPE = DEFAULT_IDENTITY_ASSERTER
DEFAULT_AUTHORIZER_NAME = 'XACMLAuthorizer'
DEFAULT_AUTHORIZER_TYPE = XACML_AUTHORIZER
DEFAULT_CERT_PATH_PROVIDER_NAME = 'WebLogicCertPathProvider'
DEFAULT_CERT_PATH_PROVIDER_TYPE = WEBLOGIC_CERT_PATH_PROVIDER
DEFAULT_CREDENTIAL_MAPPER_NAME = 'DefaultCredentialMapper'
DEFAULT_CREDENTIAL_MAPPER_TYPE = DEFAULT_CREDENTIAL_MAPPER
DEFAULT_PASSWORD_VALIDATOR_NAME = 'SystemPasswordValidator'
DEFAULT_PASSWORD_VALIDATOR_TYPE = SYSTEM_PASSWORD_VALIDATOR
DEFAULT_ROLE_MAPPER_NAME = 'XACMLRoleMapper'
DEFAULT_ROLE_MAPPER_TYPE = XACML_ROLE_MAPPER

KNOWN_TOPLEVEL_MODEL_SECTIONS = [
    DOMAIN_INFO,
    TOPOLOGY,
    RESOURCES,
    APP_DEPLOYMENTS,
    KUBERNETES
]

# these domain attributes have special processing in create,
# and should be skipped in regular attribute processing.
CREATE_ONLY_DOMAIN_ATTRIBUTES = [
    DOMAIN_NAME,
    ADMIN_SERVER_NAME
]
