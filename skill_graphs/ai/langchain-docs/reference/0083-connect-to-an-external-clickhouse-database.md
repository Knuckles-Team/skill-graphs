# Connect to an external ClickHouse database
Source: https://docs.langchain.com/langsmith/self-host-external-clickhouse

ClickHouse is a high-performance, column-oriented database system. It allows for fast ingestion of data and is optimized for analytical queries.

LangSmith uses ClickHouse as the primary data store for traces and feedback. By default, self-hosted LangSmith will use an internal ClickHouse database that is bundled with the LangSmith instance. This is run as a stateful set in the same Kubernetes cluster as the LangSmith application or as a Docker container on the same host as the LangSmith application.

However, you can configure LangSmith to use an external ClickHouse database for easier management and scaling. By configuring an external ClickHouse database, you can manage backups, scaling, and other operational tasks for your database. While Clickhouse is not yet a native service in Azure, AWS, or Google Cloud, you can run LangSmith with an external ClickHouse database in the following ways:

* [LangSmith-managed ClickHouse](/langsmith/langsmith-managed-clickhouse)

* Provision a [ClickHouse Cloud](https://clickhouse.cloud/) either directly or through a cloud provider marketplace:

  * [Azure Marketplace](https://azuremarketplace.microsoft.com/en-us/marketplace/apps/clickhouse.clickhouse_cloud?tab=Overview)
  * [Google Cloud Marketplace](https://console.cloud.google.com/marketplace/product/clickhouse-public/clickhouse-cloud)
  * [AWS Marketplace](https://aws.amazon.com/marketplace/seller-profile?id=adb43736-8b95-4d49-8009-3693cbee8578)

* On a VM in your cloud provider

<Note>
  Using the first two options (LangSmith-managed ClickHouse or ClickHouse Cloud) will provision a Clickhouse service OUTSIDE of your VPC. However, both options support private endpoints, meaning that you can direct traffic to the ClickHouse service without exposing it to the public internet (eg via AWS PrivateLink, or GCP Private Service Connect).

  Additionally, sensitive information can be configured to be not stored in Clickhouse. Please contact support via [support.langchain.com](https://support.langchain.com) for more information.
</Note>

## Requirements

* A provisioned ClickHouse instance that your LangSmith application will have network access to (see above for options).
* A user with admin access to the ClickHouse database. This user will be used to create the necessary tables, indexes, and views.
* We support both standalone ClickHouse and externally managed clustered deployments. For clustered deployments, ensure all nodes are running the same version. Note that clustered setups are not supported with bundled ClickHouse installations.
* We only support ClickHouse versions >= 23.9. Use of ClickHouse versions >= 24.2 requires LangSmith v0.6 or later.

<Warning>
  Downgrading ClickHouse to an earlier version can cause data corruption of system tables and result in significant downtime. If you need assistance with a ClickHouse version change or are experiencing issues after an upgrade, contact support at [support.langchain.com](https://support.langchain.com) before attempting a downgrade.
</Warning>

* We rely on a few configuration parameters to be set on your ClickHouse instance. These are detailed below:

```xml theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
<profiles>
  <default>
      <async_insert>1</async_insert> # Turn on async insert
      <async_insert_max_data_size>25000000</async_insert_max_data_size> # Flush data to disk after 25MB. You may need to adjust this based on your workload.
      <wait_for_async_insert>0</wait_for_async_insert> # Disable waiting for async insert by default
      <parallel_view_processing>1</parallel_view_processing> # Enable parallel view processing
      <materialize_ttl_after_modify>0</materialize_ttl_after_modify> # Disable TTL materialization after modify
      <wait_for_async_insert_timeout>120</wait_for_async_insert_timeout> # Set the timeout for waiting for async insert
      <lightweight_deletes_sync>0</lightweight_deletes_sync> # Disable lightweight deletes sync
      <allow_materialized_view_with_bad_select>1</allow_materialized_view_with_bad_select> # Allow materialized views with legacy SELECT statements that cause CH to fail
  </default>
</profiles>
```

<Warning>
  Our system has been tuned to work with the above configuration parameters. Changing these parameters may result in unexpected behavior.
</Warning>

## HA replicated Clickhouse cluster

<Warning>
  By default, the setup process above will only work with a single node Clickhouse cluster.
</Warning>

If you would like to use a multi-node Clickhouse cluster for HA, we support this with additional required configuration. This setup can use a Clickhouse cluster with multiple nodes where data replicated via Zookeeper or Clickhouse Keeper. For more information on Clickhouse replication, see [Clickhouse Data Replication Docs](https://clickhouse.com/docs/architecture/replication).

In order to setup LangSmith with a replicated multi-node Clickhouse setup:

* You need to have a Clickhouse cluster that is setup with Keeper or Zookeeper for data replication and the appropriate settings. See [Clickhouse Replication Setup Docs](https://clickhouse.com/docs/architecture/replication).
* You need to set the cluster setting in the [LangSmith Configuration](#configuration) section, specifically the `cluster` settings to match your Clickhouse Cluster name. This will use the `Replicated` table engines when running the Clickhouse migrations.
* If in addition to HA, you would like to load balance among the Clickhouse nodes (to distribute reads or writes), we suggest using a load balancer or DNS load balancing to round robin among your Clickhouse servers.
* **Note**: You will need to enable your `cluster` setting before launching LangSmith for the first time and running the Clickhouse migrations. This is a requirement since the table engine will need to be created as a `Replicated` table engine vs the non replicated engine type.

When running migrations with `cluster` enabled, the migration will create the `Replicated` table engine flavor. This means that data will be replicated among the servers in the cluster. This is a master-master setup where any server can process reads, writes, or merges.

<Note>
  For an example setup of a replicated ClickHouse cluster, refer to the [replicated ClickHouse section](https://github.com/langchain-ai/helm/blob/main/charts/langsmith/examples/replicated-clickhouse/README.md) in the LangSmith Helm chart repo, under examples.
</Note>

## LangSmith-managed ClickHouse

* If using LangSmith-managed ClickHouse, you will need to set up a VPC peering connection between the LangSmith VPC and the ClickHouse VPC. Please contact support via [support.langchain.com](https://support.langchain.com) for more information.
* You will also need to set up Blob Storage. You can read more about Blob Storage in the [Blob Storage documentation](/langsmith/self-host-blob-storage).

<Note>
  ClickHouse installations managed by LangSmith use a SharedMerge engine, which automatically clusters them and separates compute from storage.
</Note>

For more information, refer to the [managed ClickHouse](/langsmith/langsmith-managed-clickhouse) page.

## Parameters

You will need to provide several parameters to your LangSmith installation to configure an external ClickHouse database. These parameters include:

* **Host**: The hostname or IP address of the ClickHouse database
* **HTTP Port**: The port that the ClickHouse database listens on for HTTP connections
* **Native Port**: The port that the ClickHouse database listens on for [native connections](https://clickhouse.com/docs/en/interfaces/tcp)
* **Database**: The name of the ClickHouse database that LangSmith should use
* **Username**: The username to use to connect to the ClickHouse database
* **Password**: The password to use to connect to the ClickHouse database
* **Cluster (Optional)**: The name of the ClickHouse cluster if using an external Clickhouse cluster. When set, LangSmith will run migrations on the cluster and replicate data across instances.

<Warning>
  Important considerations for clustered deployments:

  * Clustered setups must be configured on a fresh schema - existing standalone ClickHouse instances cannot be converted to clustered mode.

  * Clustering is only supported with externally managed ClickHouse deployments. It is not compatible with bundled ClickHouse installations as these do not include required ZooKeeper configurations.

  * When using a clustered deployment, LangSmith will automatically:

    * Run database migrations across all nodes in the cluster
    * Configure tables for data replication across the cluster

  Note that while data is replicated across nodes, LangSmith does not configure distributed tables or handle query routing - queries will be directed to the specified host. You will need to handle any load balancing or query distribution at the infrastructure level if desired.
</Warning>

## Configuration

With these parameters in hand, you can configure your LangSmith instance to use the provisioned ClickHouse database. You can do this by modifying the `config.yaml` file for your LangSmith Helm Chart installation or the `.env` file for your Docker installation.

<CodeGroup>
  ```yaml Helm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  clickhouse:
    external:
      enabled: true
      host: "host"
      port: "http port"
      nativePort: "native port"
      user: "default"
      password: "password"
      database: "default"
      tls: false
      cluster: "my_cluster_name"  # Optional: Set this if using an external Clickhouse cluster
  ```

  ```bash Docker theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  # In your .env file
  CLICKHOUSE_HOST=langchain-clickhouse # Change to your Clickhouse host if using external Clickhouse. Otherwise, leave it as is
  CLICKHOUSE_USER=default # Change to your Clickhouse user if needed
  CLICKHOUSE_DB=default # Change to your Clickhouse database if needed
  CLICKHOUSE_PORT=8123 # Change to your Clickhouse port if needed
  CLICKHOUSE_TLS=false # Change to true if you are using TLS to connect to Clickhouse. Otherwise, leave it as is
  CLICKHOUSE_PASSWORD=password # Change to your Clickhouse password if needed
  CLICKHOUSE_NATIVE_PORT=9000 # Change to your Clickhouse native port if needed
  CLICKHOUSE_CLUSTER=my_cluster_name # Optional: Set this if using an external Clickhouse cluster
  ```
</CodeGroup>

Once configured, you should be able to reinstall your LangSmith instance. If everything is configured correctly, your LangSmith instance should now be using your external ClickHouse database.

## TLS with ClickHouse

Use this section to configure TLS for ClickHouse connections. For mounting internal/public CAs so LangSmith trusts your ClickHouse server certificate, see [Configure custom TLS certificates](/langsmith/self-host-custom-tls-certificates#mount-internal-cas-for-tls).

### Server TLS (one-way)

To enable TLS for ClickHouse connections:

* Set `tls: true` in your configuration (or use `tlsSecretKey` with an external secret).
* Use the appropriate TLS ports (typically `8443` for HTTP and `9440` for native TCP connections).
* Provide a CA bundle using `config.customCa.secretName` and `config.customCa.secretKey` if using an internal CA.

<Warning>
  Mount a custom CA only when your ClickHouse server uses an internal or private CA. Publicly trusted CAs do not require this configuration.
</Warning>

<CodeGroup>
  ```yaml Helm (server TLS) theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  config:
    customCa:
      secretName: "langsmith-custom-ca"  # Secret containing your CA bundle  # sanitizer:ignore
      secretKey: "ca.crt"    # Key in the Secret with the CA bundle
  clickhouse:
    external:
      enabled: true
      host: "your-clickhouse-host.example.com"
      port: "8443"
      nativePort: "9440"
      user: "default"
      password: "password"
      database: "default"
      tls: true
  ```

  ```yaml Kubernetes Secret (CA bundle) theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  apiVersion: v1
  kind: Secret
  metadata:
    name: langsmith-custom-ca
  type: Opaque
  stringData:
    ca.crt: |
      -----BEGIN CERTIFICATE-----
      <ROOT_OR_INTERMEDIATE_CA_CERT_CHAIN>
      -----END CERTIFICATE-----
  ```
</CodeGroup>

### Mutual TLS with client auth (mTLS)

As of LangSmith helm chart version **0.12.29**, we support mTLS for ClickHouse clients. For server-side authentication in mTLS, use the [Server TLS steps](#server-tls-one-way) (custom CA) in addition to the following client certificate configuration.

If your ClickHouse server requires client certificate authentication:

* Provide a Secret with your client certificate and key.
* Reference it via `clickhouse.external.clientCert.secretName` and specify the keys with `certSecretKey` and `keySecretKey`.

<CodeGroup>
  ```yaml Helm (client auth) theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  clickhouse:
    external:
      enabled: true
      host: "your-clickhouse-host.example.com"
      port: "8443"
      nativePort: "9440"
      user: "default"
      password: "password"
      database: "default"
      tls: true
      clientCert:
        secretName: "clickhouse-client-cert"  # sanitizer:ignore
        certSecretKey: "tls.crt"
        keySecretKey: "tls.key"
  ```

  ```yaml Kubernetes Secret (client cert/key) theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  apiVersion: v1
  kind: Secret
  metadata:
    name: clickhouse-client-cert
  type: Opaque
  stringData:
    tls.crt: |
      -----BEGIN CERTIFICATE-----
      <CLIENT_CERT>
      -----END CERTIFICATE-----
    tls.key: |
      -----BEGIN PRIVATE KEY-----
      <CLIENT_KEY>
      -----END PRIVATE KEY-----
  ```
</CodeGroup>

#### Non-TLS native port for migrations

<Warning>
  When using mTLS with ClickHouse, you must **keep a non-TLS native (TCP) port** open for our migrations job, which runs on helm install and upgrade. The application itself will not communicate through this port, it is **only used by the migration job**.
</Warning>

By default, the migration job connects to port `9000` for migrations. If your ClickHouse instance uses a different non-TLS native port, you can configure it using the `CLICKHOUSE_MIGRATE_NATIVE_PORT` environment variable:

```yaml theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
backend:
  clickhouseMigrations:
    extraEnv:
      - name: CLICKHOUSE_MIGRATE_NATIVE_PORT
        value: "9000"  # Change to your non-TLS native port
```

#### Pod security context for certificate volumes

The certificate volumes mounted for mTLS are protected by file access restrictions. To ensure all LangSmith pods can read the certificate files, you must set `fsGroup: 1000` in the pod security context.

You can configure this in one of two ways:

**Option 1: Use `commonPodSecurityContext`**

Set the `fsGroup` at the top level to apply it to all pods:

```yaml theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
commonPodSecurityContext:
  fsGroup: 1000
```

**Option 2: Add to individual pod security contexts**

If you need more granular control, add the `fsGroup` to each pod's security context individually. See the [mTLS configuration example](https://github.com/langchain-ai/helm/blob/main/charts/langsmith/examples/mtls_config.yaml) for a complete reference.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/self-host-external-clickhouse.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Connect to an external PostgreSQL database
Source: https://docs.langchain.com/langsmith/self-host-external-postgres

LangSmith uses a PostgreSQL database as the primary data store for transactional workloads and operational data (almost everything besides runs). By default, LangSmith Self-Hosted will use an internal PostgreSQL database. However, you can configure LangSmith to use an external PostgreSQL database. By configuring an external PostgreSQL database, you can more easily manage backups, scaling, and other operational tasks for your database.

<Tip>
  **If you're using a managed PostgreSQL service**, we recommend:

  * [Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_GettingStarted.CreatingConnecting.PostgreSQL.html) (AWS)
  * [Google Cloud SQL](https://cloud.google.com/curated-resources/cloud-sql#section-1) (GCP)
  * [Azure Database for PostgreSQL](https://azure.microsoft.com/en-us/products/postgresql#features) (Azure)

  For cloud-specific IAM/Workload Identity authentication, refer to the [IAM authentication section](#iam-authentication).
</Tip>

## Requirements

* A provisioned PostgreSQL database that your LangSmith instance will have network access to. We recommend using a managed PostgreSQL service like:

  * [Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_GettingStarted.CreatingConnecting.PostgreSQL.html)
  * [Google Cloud SQL](https://cloud.google.com/curated-resources/cloud-sql#section-1)
  * [Azure Database for PostgreSQL](https://azure.microsoft.com/en-us/products/postgresql#features)

* Note: We only officially support PostgreSQL versions >= 14.

* We support password and [IAM/Workload Identity](#iam-authentication) authentication.

* A user with admin access to the PostgreSQL database. This user will be used to create the necessary tables, indexes, and schemas.

* This user will also need to have the ability to create extensions in the database. We use/will try to install the `btree_gin`, `btree_gist`, `pgcrypto`, `citext`, `ltree`, and `pg_trgm` extensions.

* If using a schema other than public, ensure that you do not have any other schemas with the extensions enabled, or you must include that in your search path.

* Support for pgbouncer and other connection poolers is community-based. Community members have reported that pgbouncer has worked with `pool_mode` = `session` and a suitable setting for `ignore_startup_parameters` (as of writing, `search_path` and `lock_timeout` need to be ignored). Care is needed to avoid polluting connection pools; some level of PostgreSQL expertise is advisable. LangChain Inc currently does not have roadmap plans for formal test coverage or commercial support of pgbouncer or amazon rds proxy or any other poolers, but the community is welcome to discuss and collaborate on support through GitHub issues.

* By default, we recommend an instance with **at least 2 vCPUs and 8GB of memory**. However, the actual requirements will depend on your workload and the number of users you have. We recommend monitoring your PostgreSQL instance and scaling up as needed.

## Connection string

You will need to provide a connection string to your PostgreSQL database. This connection string should include the following information:

* Host
* Port
* Database
* Username
* Password (Make sure to URL encode this if there are any special characters) - **Note:** When using IAM authentication, the password is not required in the connection string. More below.
* URL params

This will take the form of:

```
username:password@host:port/database?<url_params>
```

An example connection string might look like:

```
myuser:mypassword@myhost:5432/mydatabase?sslmode=disable
```

Without URL parameters, the connection string would look like:

```
myuser:mypassword@myhost:5432/mydatabase
```

For IAM authentication, omit the password and use the identity name as the username:

```
my-workload-identity@myhost:5432/mydatabase?sslmode=require
```

## Configuration

With your connection string in hand, you can configure your LangSmith instance to use an external PostgreSQL database. You can do this by modifying the `values` file for your LangSmith Helm Chart installation or the `.env` file for your Docker installation.

<CodeGroup>
  ```yaml Helm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  postgres:
    external:
      enabled: true
      connectionUrl: "Your connection url"
  ```

  ```bash Docker theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  # In your .env file
  POSTGRES_DATABASE_URI="Your connection url"
  ```
</CodeGroup>

Once configured, you should be able to reinstall your LangSmith instance. If everything is configured correctly, your LangSmith instance should now be using your external PostgreSQL database.

## TLS with PostgreSQL

Use this section to configure TLS for PostgreSQL connections. For mounting internal/public CAs so LangSmith trusts your PostgreSQL server certificate, see [Configure custom TLS certificates](/langsmith/self-host-custom-tls-certificates#mount-internal-cas-for-tls).

### Server TLS (one-way)

To validate the PostgreSQL server certificate:

* Provide a CA bundle using `config.customCa.secretName` and `config.customCa.secretKey`.
* Use `sslmode=require` or `sslmode=verify-full`, as well as `sslrootcert=system` to your connection URL.

<Warning>
  Mount a custom CA only when your PostgreSQL server uses an internal or private CA. Publicly trusted CAs do not require this configuration.
</Warning>

<CodeGroup>
  ```yaml Helm (server TLS) theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  config:
    customCa:
      secretName: "langsmith-custom-ca"  # Secret containing your CA bundle  # sanitizer:ignore
      secretKey: "ca.crt"    # Key in the Secret with the CA bundle
  postgres:
    external:
      enabled: true
      connectionUrl: "myuser:mypassword@myhost:5432/mydatabase?sslmode=verify-full&sslrootcert=system"
      customTls: true
  ```

  ```yaml Kubernetes Secret (CA bundle) theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  apiVersion: v1
  kind: Secret
  metadata:
    name: langsmith-custom-ca
  type: Opaque
  stringData:
    ca.crt: |
      -----BEGIN CERTIFICATE-----
      <ROOT_OR_INTERMEDIATE_CA_CERT_CHAIN>
      -----END CERTIFICATE-----
  ```
</CodeGroup>

### Mutual TLS with client auth (mTLS)

As of LangSmith helm chart version **0.12.29**, we support mTLS for PostgreSQL clients. For server-side authentication in mTLS, use the [Server TLS steps](#server-tls-one-way) (custom CA) in addition to the following client certificate configuration.

If your PostgreSQL server requires client certificate authentication:

* Provide a Secret with your client certificate and key.
* Reference it via `postgres.external.clientCert.secretName` and specify the keys with `certSecretKey` and `keySecretKey`.
* Use `sslmode=verify-full` and `sslrootcert=system` in your connection URL.

<CodeGroup>
  ```yaml Helm (client Auth) theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  postgres:
    external:
      enabled: true
      connectionUrl: "myuser:mypassword@myhost:5432/mydatabase?sslmode=verify-full&sslrootcert=system"
      customTls: true
      clientCert:
        secretName: "postgres-mtls-secret"  # sanitizer:ignore
        certSecretKey: "tls.crt"
        keySecretKey: "tls.key"
  ```

  ```yaml Kubernetes Secret (client cert/key) theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  apiVersion: v1
  kind: Secret
  metadata:
    name: postgres-mtls-secret
  type: Opaque
  stringData:
    tls.crt: |
      -----BEGIN CERTIFICATE-----
      <CLIENT_CERT>
      -----END CERTIFICATE-----
    tls.key: |
      -----BEGIN PRIVATE KEY-----
      <CLIENT_KEY>
      -----END PRIVATE KEY-----
  ```
</CodeGroup>

#### Pod security context for certificate volumes

The certificate volumes mounted for mTLS are protected by file access restrictions. To ensure all LangSmith pods can read the certificate files, you must set `fsGroup: 1000` in the pod security context.

You can configure this in one of two ways:

**Option 1: Use `commonPodSecurityContext`**

Set the `fsGroup` at the top level to apply it to all pods:

```yaml theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
commonPodSecurityContext:
  fsGroup: 1000
```

**Option 2: Add to individual pod security contexts**

If you need more granular control, add the `fsGroup` to each pod's security context individually. See the [mTLS configuration example](https://github.com/langchain-ai/helm/blob/main/charts/langsmith/examples/mtls_config.yaml) for a complete reference.

## IAM authentication

As of LangSmith helm chart version **0.12.34**, we support IAM authentication for PostgreSQL. This allows you to use cloud provider workload identity instead of static passwords.

<Warning>
  IAM authentication only handles connection authentication. You may still need to run SQL commands in your database to create the IAM user/role and grant it the necessary permissions and privileges to access the LangSmith schema.
</Warning>

<Tabs>
  <Tab title="AWS">
    <a />

    ### Amazon RDS IAM authentication

    Amazon RDS supports [IAM database authentication](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.IAMDBAuth.html), which allows you to authenticate to your PostgreSQL instance using AWS IAM credentials instead of database passwords.

    #### Prerequisites

    1. **Configure workload identity** in your Kubernetes cluster using [AWS IRSA](https://docs.aws.amazon.com/eks/latest/userguide/iam-roles-for-service-accounts.html) or [EKS Pod Identity](https://docs.aws.amazon.com/eks/latest/userguide/pod-identities.html)
    2. **Enable IAM authentication** on your RDS PostgreSQL instance and grant access to your workload identity

    #### Configuration

    <Warning>
      If you switch to a new IAM user after LangSmith has already run initial migrations, you may need to transfer ownership of existing tables to the new IAM user. Otherwise, migrations may fail due to insufficient privileges on tables owned by the previous user.
    </Warning>

    Set the `iamAuthProvider` to `"aws"` and provide an IAM-compatible connection string (without password):

    ```yaml theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    postgres:
      external:
        enabled: true
        existingSecretName: "postgres-secret"
        iamAuthProvider: "aws"
    ```

    ```yaml theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    apiVersion: v1
    kind: Secret
    metadata:
      name: postgres-secret
    type: Opaque
    stringData:
      # IAM connection URL - note no password, username is the IAM identity name
      connection_url: "<iam-identity-name>@<rds-host>:5432/<database>?sslmode=require"
    ```

    <Warning>
      IAM authentication requires TLS. You must include `sslmode=require` in your connection string.
    </Warning>

    #### Required annotations

    You must apply the ServiceAccount annotations required by AWS IRSA to all LangSmith components that connect to PostgreSQL:

    **Deployments:** `backend`, `queue`, `platformBackend`, `hostBackend`, `ingestQueue`

    **Jobs:** `migrations`, `authBootstrap`, `feedbackConfigMigration`, `feedbackDataMigration`, `e2eTest`

    <Note>
      All jobs listed above (except `e2eTest`) use the `backend` service account. The `e2eTest` job uses its own service account and requires separate annotation configuration.
    </Note>

    Example configuration for the backend service:

    ```yaml theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    backend:
      serviceAccount:
        annotations:
          eks.amazonaws.com/role-arn: "arn:aws:iam::<account-id>:role/<role-name>"

    queue:
      serviceAccount:
        annotations:
          eks.amazonaws.com/role-arn: "arn:aws:iam::<account-id>:role/<role-name>"

    platformBackend:
      serviceAccount:
        annotations:
          eks.amazonaws.com/role-arn: "arn:aws:iam::<account-id>:role/<role-name>"

    hostBackend:
      serviceAccount:
        annotations:
          eks.amazonaws.com/role-arn: "arn:aws:iam::<account-id>:role/<role-name>"

    ingestQueue:
      serviceAccount:
        annotations:
          eks.amazonaws.com/role-arn: "arn:aws:iam::<account-id>:role/<role-name>"
    ```

    See the [Helm values reference](https://github.com/langchain-ai/helm/blob/main/charts/langsmith/values.yaml) for the full list of configurable services.
  </Tab>

  <Tab title="GCP">
    <a />

    ### Cloud SQL IAM authentication

    Cloud SQL supports [IAM authentication](https://cloud.google.com/sql/docs/postgres/iam-authentication), which allows you to authenticate using GCP service accounts instead of database passwords.

    #### Prerequisites

    1. **Configure workload identity** in your Kubernetes cluster using [GCP Workload Identity](https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity)
    2. **Enable IAM authentication** on your Cloud SQL instance and grant access to your workload identity

    #### Configuration

    <Warning>
      If you switch to a new IAM user after LangSmith has already run initial migrations, you may need to transfer ownership of existing tables to the new IAM user. Otherwise, migrations may fail due to insufficient privileges on tables owned by the previous user.
    </Warning>

    Set the `iamAuthProvider` to `"gcp"` and provide an IAM-compatible connection string (without password):

    ```yaml theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    postgres:
      external:
        enabled: true
        existingSecretName: "postgres-secret"
        iamAuthProvider: "gcp"
    ```

    ```yaml theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    apiVersion: v1
    kind: Secret
    metadata:
      name: postgres-secret
    type: Opaque
    stringData:
      # IAM connection URL - note no password, username is the service account email
      connection_url: "<service-account>@<project>.iam@<cloud-sql-host>:5432/<database>?sslmode=require"
    ```

    <Warning>
      IAM authentication requires TLS. You must include `sslmode=require` in your connection string.
    </Warning>

    #### Required annotations

    You must apply the ServiceAccount annotations required by GCP Workload Identity to all LangSmith components that connect to PostgreSQL:

    **Deployments:** `backend`, `queue`, `platformBackend`, `hostBackend`, `ingestQueue`

    **Jobs:** `migrations`, `authBootstrap`, `feedbackConfigMigration`, `feedbackDataMigration`, `e2eTest`

    <Note>
      All jobs listed above (except `e2eTest`) use the `backend` service account. The `e2eTest` job uses its own service account and requires separate annotation configuration.
    </Note>

    Example configuration for the backend service:

    ```yaml theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    backend:
      serviceAccount:
        annotations:
          iam.gke.io/gcp-service-account: "<service-account>@<project>.iam.gserviceaccount.com"

    queue:
      serviceAccount:
        annotations:
          iam.gke.io/gcp-service-account: "<service-account>@<project>.iam.gserviceaccount.com"

    platformBackend:
      serviceAccount:
        annotations:
          iam.gke.io/gcp-service-account: "<service-account>@<project>.iam.gserviceaccount.com"

    hostBackend:
      serviceAccount:
        annotations:
          iam.gke.io/gcp-service-account: "<service-account>@<project>.iam.gserviceaccount.com"

    ingestQueue:
      serviceAccount:
        annotations:
          iam.gke.io/gcp-service-account: "<service-account>@<project>.iam.gserviceaccount.com"
    ```

    See the [Helm values reference](https://github.com/langchain-ai/helm/blob/main/charts/langsmith/values.yaml) for the full list of configurable services.
  </Tab>

  <Tab title="Azure">
    <a />

    ### Azure Database for PostgreSQL with Microsoft Entra authentication

    Azure Database for PostgreSQL supports [Microsoft Entra authentication](https://learn.microsoft.com/en-us/azure/postgresql/flexible-server/concepts-azure-ad-authentication), which allows you to authenticate using Azure managed identities instead of database passwords.

    #### Prerequisites

    1. **Configure workload identity** in your Kubernetes cluster using [Azure Workload Identity](https://learn.microsoft.com/en-us/azure/aks/workload-identity-overview)
    2. **Enable Microsoft Entra authentication** on your Azure Database for PostgreSQL instance and grant access to your workload identity

    #### Configuration

    <Warning>
      If you switch to a new IAM user after LangSmith has already run initial migrations, you may need to transfer ownership of existing tables to the new IAM user. Otherwise, migrations may fail due to insufficient privileges on tables owned by the previous user.
    </Warning>

    Set the `iamAuthProvider` to `"azure"` and provide an IAM-compatible connection string (without password):

    ```yaml theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    postgres:
      external:
        enabled: true
        existingSecretName: "postgres-secret"
        iamAuthProvider: "azure"
    ```

    ```yaml theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    apiVersion: v1
    kind: Secret
    metadata:
      name: postgres-secret
    type: Opaque
    stringData:
      # IAM connection URL - note no password, username is the managed identity name
      connection_url: "<managed-identity-name>@<azure-postgres-host>:5432/<database>?sslmode=require"
    ```

    <Warning>
      IAM authentication requires TLS. You must include `sslmode=require` in your connection string.
    </Warning>

    #### Required annotations

    You must apply the ServiceAccount annotations and pod labels required by Azure Workload Identity to all LangSmith components that connect to PostgreSQL:

    **Deployments:** `backend`, `queue`, `platformBackend`, `hostBackend`, `ingestQueue`

    **Jobs:** `migrations`, `authBootstrap`, `feedbackConfigMigration`, `feedbackDataMigration`, `e2eTest`

    <Note>
      All jobs listed above (except `e2eTest`) use the `backend` service account. For these jobs, you only need to configure pod labels (Azure requires `azure.workload.identity/use: "true"` on pods). The `e2eTest` job uses its own service account and requires separate annotation configuration.
    </Note>

    Example configuration for the backend service:

    ```yaml theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    backend:
      serviceAccount:
        annotations:
          azure.workload.identity/client-id: "<managed-identity-client-id>"
      deployment:
        labels:
          azure.workload.identity/use: "true"
      migrations:
        labels:
          azure.workload.identity/use: "true"

    queue:
      serviceAccount:
        annotations:
          azure.workload.identity/client-id: "<managed-identity-client-id>"
      deployment:
        labels:
          azure.workload.identity/use: "true"

    platformBackend:
      serviceAccount:
        annotations:
          azure.workload.identity/client-id: "<managed-identity-client-id>"
      deployment:
        labels:
          azure.workload.identity/use: "true"

    hostBackend:
      serviceAccount:
        annotations:
          azure.workload.identity/client-id: "<managed-identity-client-id>"
      deployment:
        labels:
          azure.workload.identity/use: "true"

    ingestQueue:
      serviceAccount:
        annotations:
          azure.workload.identity/client-id: "<managed-identity-client-id>"
      deployment:
        labels:
          azure.workload.identity/use: "true"
    ```

    See the [Helm values reference](https://github.com/langchain-ai/helm/blob/main/charts/langsmith/values.yaml) for the full list of configurable services.
  </Tab>
</Tabs>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/self-host-external-postgres.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
