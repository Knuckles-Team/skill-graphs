# Connect to an external Redis or Valkey database
Source: https://docs.langchain.com/langsmith/self-host-external-redis

LangSmith uses Redis to back our queuing/caching operations. By default, LangSmith Self-Hosted will use an internal Redis instance. However, you can configure LangSmith to use an external Redis instance. By configuring an external Redis instance, you can more easily manage backups, scaling, and other operational tasks for your Redis instance.

[Valkey](https://valkey.io/) is also officially supported as a drop-in replacement for Redis. Anywhere this page refers to Redis, you can use a compatible Valkey instance. See [Requirements](#requirements) for supported versions.

<Warning>
  Each LangSmith installation must use its own dedicated Redis instance. Redis cannot be shared across separate LangSmith installations (for example, between an existing and new cluster during a migration). Sharing it across installations causes deployment tasks to be routed to the wrong cluster.
</Warning>

<Tip>
  **If you're using a managed Redis service**, we recommend:

  * [Amazon ElastiCache](https://aws.amazon.com/elasticache/redis/) (AWS)
  * [Google Cloud Memorystore](https://cloud.google.com/memorystore) (GCP)
  * [Azure Cache for Redis](https://azure.microsoft.com/en-us/services/cache/) (Azure)

  For cloud-specific IAM/Workload Identity authentication, refer to the [IAM authentication section](#iam-authentication).
</Tip>

## Requirements

* A provisioned Redis or [Valkey](https://valkey.io/) instance that your LangSmith instance will have network access to. We recommend using a managed service like:

  * [Amazon ElastiCache](https://aws.amazon.com/elasticache/redis/) (Redis or Valkey)
  * [Google Cloud Memorystore](https://cloud.google.com/memorystore) (Redis or Valkey)
  * [Azure Cache for Redis](https://azure.microsoft.com/en-us/services/cache/)

* **Supported versions:** Redis >= 5, or Valkey 8. Valkey is treated as a drop-in replacement for Redis throughout this guide.

* We support both Standalone and Redis Cluster (including Valkey Cluster). See the appropriate sections for deployment instructions.

* We support no authentication, password, and [IAM/Workload Identity](#iam-authentication) authentication.

* By default, we recommend an instance with at least 2 vCPUs and 8GB of memory. However, the actual requirements will depend on your tracing workload. We recommend monitoring your Redis instance and scaling up as needed.

## Standalone Redis

### Connection string

You will need to assemble the connection string for your Redis instance. This connection string should include the following information:

* Host
* Database
* Port
* URL params

This will take the form of:

```
"redis://host:port/db?<url_params>"
```

An example connection string might look like:

```
"redis://langsmith-redis:6379/0"
```

Note: If your Standalone Redis requires authentication or TLS, include these directly in the connection URL:

* Use `rediss://` when TLS is enabled on your Redis server.
* Provide the password in the connection string.

For example:

```text theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
rediss://langsmith-redis:6380/0?password=foo
```

For IAM authentication, use the identity as the username (no password):

```text theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
rediss://<iam-identity>@host:6380
```

### Configuration

With your connection string in hand, you can configure your LangSmith instance to use an external Redis instance. You can do this by modifying the `values` file for your LangSmith Helm Chart installation or the `.env` file for your Docker installation.

<CodeGroup>
  ```yaml Helm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  redis:
    external:
      enabled: true
      connectionUrl: "Your connection url"
  ```

  ```bash Docker theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  # In your .env file
  REDIS_DATABASE_URI="Your connection url"
  ```
</CodeGroup>

You can also store the connection URL in an existing Kubernetes Secret and reference it in your Helm values.

<CodeGroup>
  ```yaml Helm (using an existing Secret) theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  redis:
    external:
      enabled: true
      # Name of an existing Secret that contains the connection URL
      existingSecretName: "my-redis-secret"
      # Key in the Secret that stores the connection URL (default shown)
      connectionUrlSecretKey: "connection_url"
  ```

  ```yaml Kubernetes Secret theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  apiVersion: v1
  kind: Secret
  metadata:
    name: my-redis-secret
  type: Opaque
  stringData:
    # Full connection URL, e.g., using TLS with password
    connection_url: "rediss://langsmith-redis:6380/0?password=foo"
  ```
</CodeGroup>

Once configured, you should be able to reinstall your LangSmith instance. If everything is configured correctly, your LangSmith instance should now be using your external Redis instance.

## Redis cluster

As of LangSmith helm version **0.12.25**, we officially support **Redis Cluster**.

### Host names

When using Redis Cluster, provide a list of node hostnames and ports. Each node URI must be in the form:

```text theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
redis://hostname:port
```

For example:

```text theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
redis://redis-node-0:6379
redis://redis-node-1:6379
redis://redis-node-2:6379
```

Do not include a password in these URIs, and do not use `rediss` here. For Redis Cluster:

* Provide the password separately via `redis.external.cluster.password` or through a Secret using `passwordSecretKey`.
* TLS is enabled by default for Redis Cluster (`redis.external.cluster.tlsEnabled: true`). Set `tlsEnabled: false` if your cluster does not use TLS.

### Configuration

When connecting to an external Redis Cluster, configure the Helm values under `redis.external.cluster`. You can either:

* Provide node URIs and (optionally) a password directly in `values.yaml`.
* Or reference an existing Kubernetes `Secret` containing node URIs and password.

<CodeGroup>
  ```yaml Helm (inline values) theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  redis:
    external:
      enabled: true
      cluster:
        enabled: true
        # List of cluster node URIs. Format: redis://host:port
        nodeUris:
          - "redis://redis-node-0:6379"
          - "redis://redis-node-1:6379"
          - "redis://redis-node-2:6379"
        # Optional. If your cluster requires auth, set a password or use a Secret (recommended).
        password: "your_redis_password"
        # TLS is enabled by default. Set to false if your cluster does not use TLS.
        tlsEnabled: true
  ```

  ```yaml Helm (using an existing Secret) theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  redis:
    external:
      enabled: true
      # Name of an existing Secret that contains cluster connection details
      existingSecretName: "my-redis-cluster-secret"  # sanitizer:ignore
      cluster:
        enabled: true
        # Keys in the Secret. Defaults shown here; override if your Secret uses different keys.
        nodeUrisSecretKey: "redis_cluster_node_uris"  # sanitizer:ignore
        passwordSecretKey: "redis_cluster_password"  # sanitizer:ignore
        tlsEnabled: true
  ```
</CodeGroup>

If using an existing Secret, it should contain:

<CodeGroup>
  ```yaml Kubernetes Secret theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  apiVersion: v1
  kind: Secret
  metadata:
    name: my-redis-cluster-secret
  type: Opaque
  stringData:
    # JSON array of node URIs (as a string)
    redis_cluster_node_uris: '["redis://redis-node-0:6379","redis://redis-node-1:6379","redis://redis-node-2:6379"]'
    # Optional if your cluster requires a password
    redis_cluster_password: "your_redis_password"
  ```
</CodeGroup>

## Azure managed Redis

[Azure Managed Redis](https://azure.microsoft.com/en-us/products/managed-redis) supports two clustering policies that affect how LangSmith connects to it. Choose the configuration below based on the clustering policy of your instance.

### OSS Cluster

LangSmith connects to OSS clustering policy instances using Redis Cluster mode.

As of LangSmith helm chart version **0.13.33**, `ssl_check_hostname=false` is supported as a node URI parameter. In our testing, the OSS clustering policy requires disabling SSL hostname verification. Azure's proxy resolves connections to internal node IPs that are not present in the certificate's SAN, causing hostname verification to fail.

```yaml theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
redis:
  external:
    enabled: true
    cluster:
      enabled: true
      nodeUris:
        - "redis://<node_url>:10000?ssl_check_hostname=false"
      tlsEnabled: true
```

### EnterpriseCluster

As of LangSmith helm chart version **0.13.33**, LangSmith supports Azure Managed Redis with the EnterpriseCluster policy. This policy exposes a single endpoint that handles sharding internally. LangSmith must connect to it as a standalone (single-instance) client, but it does not support cluster unsafe operations such as MULTI/EXEC. Set `redis.external.clusterSafeMode: true` to disable unsafe cluster operations.

```yaml theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
redis:
  external:
    enabled: true
    connectionUrl: "rediss://<azure-redis-host>:6380"
    # Required for EnterpriseCluster: use a single-instance client and disable unsafe cluster operations
    clusterSafeMode: true
```

For Microsoft Entra (IAM) authentication with EnterpriseCluster, see the [Azure tab in IAM authentication](#azure-cache-for-redis) and include `clusterSafeMode: true` in your Helm values.

## TLS with Redis

Use this section to configure TLS for Redis connections. For mounting internal/public CAs so LangSmith trusts your Redis server certificate, see [Configure custom TLS certificates](/langsmith/self-host-custom-tls-certificates#mount-internal-cas-for-tls).

### Server TLS (one-way)

To validate the Redis server certificate:

* Provide a CA bundle using `config.customCa.secretName` and `config.customCa.secretKey`.
* For Standalone Redis, use `rediss://` in the connection URL.
* For Redis Cluster, `redis.external.cluster.tlsEnabled` defaults to `true`. Ensure it is not set to `false`.

<Warning>
  Mount a custom CA only when your Redis server uses an internal or private CA. Publicly trusted CAs do not require this configuration.
</Warning>

<CodeGroup>
  ```yaml Helm (Standalone - server TLS) theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  config:
    customCa:
      secretName: "langsmith-custom-ca"  # Secret containing your CA bundle  # sanitizer:ignore
      secretKey: "ca.crt"    # Key in the Secret with the CA bundle
  redis:
    external:
      enabled: true
      # Use rediss:// and include password if required by your server
      connectionUrl: "rediss://host:6380/0?password=<PASSWORD>"
  ```

  ```yaml Helm (Cluster - server TLS) theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  config:
    customCa:
      secretName: "langsmith-custom-ca"  # Secret containing your CA bundle  # sanitizer:ignore
      secretKey: "ca.crt"    # Key in the Secret with the CA bundle
  redis:
    external:
      enabled: true
      cluster:
        enabled: true
        tlsEnabled: true
        nodeUris:
          - "redis://redis-node-0:6379"
          - "redis://redis-node-1:6379"
          - "redis://redis-node-2:6379"
        password: "<PASSWORD>"
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

As of LangSmith helm chart version **0.12.29**, we support mTLS for Redis clients. For server-side authentication in mTLS, use the [Server TLS steps](#server-tls-one-way) (custom CA) in addition to the following client certificate configuration.

If your Redis server requires client certificate authentication:

* Provide a Secret with your client certificate and key.
* Reference it via `redis.external.clientCert.secretName` and specify the keys with `certSecretKey` and `keySecretKey`.
* For Standalone Redis, keep using `rediss://` in the connection URL.
* For Redis Cluster, `redis.external.cluster.tlsEnabled` defaults to `true`. Ensure it is not set to `false`.

<CodeGroup>
  ```yaml Helm (client Auth) theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  redis:
    external:
      enabled: true
      clientCert:
        secretName: "redis-mtls-secret"  # sanitizer:ignore
        certSecretKey: "tls.crt"
        keySecretKey: "tls.key"
      # Standalone example:
      # connectionUrl: "rediss://host:6380/0?password=<PASSWORD>"
      # Or, for Cluster:
      cluster:
        enabled: true
        tlsEnabled: true
        nodeUris:
          - "redis://redis-node-0:6379"
          - "redis://redis-node-1:6379"
          - "redis://redis-node-2:6379"
        password: "<PASSWORD>"
  ```

  ```yaml Kubernetes Secret (client cert/key) theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  apiVersion: v1
  kind: Secret
  metadata:
    name: redis-mtls-secret
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

If you need more granular control, add the `fsGroup` to each pod's security context individually. See the [mtls configuration example](https://github.com/langchain-ai/helm/blob/main/charts/langsmith/examples/mtls_config.yaml) for a complete reference.

## IAM authentication

As of LangSmith helm chart version **0.12.34**, we support IAM authentication for Redis. This allows you to use cloud provider workload identity instead of static passwords.

<Note>
  IAM authentication is supported for both standalone Redis and Redis Cluster configurations. However, not all cloud providers support IAM authentication for all Redis offerings. Check your cloud provider's documentation to verify IAM support for your specific Redis setup (e.g., GCP only supports IAM for Memorystore Cluster, not standalone Memorystore).
</Note>

<Tabs>
  <Tab title="AWS">
    <a />

    ### ElastiCache for Redis IAM authentication

    ElastiCache for Redis supports [IAM authentication](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/auth-iam.html), which allows you to authenticate using AWS IAM credentials instead of Redis AUTH passwords.

    #### Prerequisites

    1. **Configure workload identity** in your Kubernetes cluster using [AWS IRSA](https://docs.aws.amazon.com/eks/latest/userguide/iam-roles-for-service-accounts.html) or [EKS Pod Identity](https://docs.aws.amazon.com/eks/latest/userguide/pod-identities.html)
    2. **Enable IAM authentication** on your ElastiCache instance and grant access to your workload identity

    #### Configuration

    **Standalone Redis:**

    ```yaml theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    redis:
      external:
        enabled: true
        existingSecretName: "redis-secret"
        iamAuthProvider: "aws"
    ```

    ```yaml theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    apiVersion: v1
    kind: Secret
    metadata:
      name: redis-secret
    type: Opaque
    stringData:
      # IAM connection URL - identity as username, no password
      connection_url: "rediss://<iam-identity>@<elasticache-host>:6380"
    ```

    **Redis Cluster:**

    ```yaml theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    redis:
      external:
        enabled: true
        existingSecretName: "redis-cluster-secret"  # sanitizer:ignore
        iamAuthProvider: "aws"
        cluster:
          enabled: true
          nodeUrisSecretKey: "redis_cluster_node_uris"  # sanitizer:ignore
          tlsEnabled: true
    ```

    #### Required annotations

    You must apply the ServiceAccount annotations required by AWS IRSA to all LangSmith components that connect to Redis:

    **Deployments:** `backend`, `queue`, `platformBackend`, `hostBackend`, `ingestQueue`

    Example configuration:

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

    ### Memorystore for Redis IAM authentication

    Memorystore for Redis supports [IAM authentication](https://docs.cloud.google.com/memorystore/docs/cluster/about-iam-auth) for **Cluster instances only** (not standalone Memorystore). This allows you to authenticate using GCP service accounts.

    <Note>
      IAM authentication is only available for Memorystore Cluster, not standalone Memorystore instances.
    </Note>

    #### Prerequisites

    1. **Configure workload identity** in your Kubernetes cluster using [GCP Workload Identity](https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity)
    2. **Enable IAM authentication** on your Memorystore Cluster and grant access to your workload identity

    #### Configuration

    **Memorystore Cluster with IAM:**

    ```yaml theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    redis:
      external:
        enabled: true
        existingSecretName: "redis-cluster-secret"  # sanitizer:ignore
        iamAuthProvider: "gcp"
        cluster:
          enabled: true
          nodeUrisSecretKey: "redis_cluster_node_uris"  # sanitizer:ignore
          tlsEnabled: true
    ```

    ```yaml theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    apiVersion: v1
    kind: Secret
    metadata:
      name: redis-cluster-secret
    type: Opaque
    stringData:
      redis_cluster_node_uris: '["redis://node-0:6379","redis://node-1:6379","redis://node-2:6379"]'
    ```

    #### Required annotations

    You must apply the ServiceAccount annotations required by GCP Workload Identity to all LangSmith components that connect to Redis:

    **Deployments:** `backend`, `queue`, `platformBackend`, `hostBackend`, `ingestQueue`

    Example configuration:

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

    ### Azure Cache for Redis with Microsoft Entra authentication

    Azure Cache for Redis supports [Microsoft Entra authentication](https://learn.microsoft.com/en-us/azure/azure-cache-for-redis/cache-azure-active-directory-for-authentication), which allows you to authenticate using Azure managed identities.

    #### Prerequisites

    1. **Configure workload identity** in your Kubernetes cluster using [Azure Workload Identity](https://learn.microsoft.com/en-us/azure/aks/workload-identity-overview)
    2. **Enable Microsoft Entra authentication** on your Azure Cache for Redis and grant access to your workload identity

    #### Configuration

    **Standalone Redis:**

    ```yaml theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    redis:
      external:
        enabled: true
        existingSecretName: "redis-secret"
        iamAuthProvider: "azure"
        # Include if using EnterpriseCluster policy. See the Azure managed Redis section for details.
        # clusterSafeMode: true
    ```

    ```yaml theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    apiVersion: v1
    kind: Secret
    metadata:
      name: redis-secret
    type: Opaque
    stringData:
      # IAM connection URL - managed identity as username, no password
      connection_url: "rediss://<managed-identity>@<azure-redis-host>:6380"
    ```

    **Redis Cluster:**

    ```yaml theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    redis:
      external:
        enabled: true
        existingSecretName: "redis-cluster-secret"  # sanitizer:ignore
        iamAuthProvider: "azure"
        cluster:
          enabled: true
          nodeUrisSecretKey: "redis_cluster_node_uris"  # sanitizer:ignore
          tlsEnabled: true
    ```

    #### Required annotations

    You must apply the ServiceAccount annotations and pod labels required by Azure Workload Identity to all LangSmith components that connect to Redis:

    **Deployments:** `backend`, `queue`, `platformBackend`, `hostBackend`, `ingestQueue`

    Example configuration:

    ```yaml theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    backend:
      serviceAccount:
        annotations:
          azure.workload.identity/client-id: "<managed-identity-client-id>"
      deployment:
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
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/self-host-external-redis.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# FIPS-compliant images
Source: https://docs.langchain.com/langsmith/self-host-fips

Run self-hosted LangSmith installation on FIPS 140 compliant container images

<Note>
  FIPS and airgapped LangSmith deployments require a conversation with your LangChain account executive before rollout. Reach out to scope licensing, supported configurations, and upgrade paths before you change your installation.
</Note>

As of v15, every LangChain-authored LangSmith image has a `-fips` counterpart that runs in FIPS 140 mode. Use these images when your self-hosted deployment needs FIPS compliance, for example in federal agencies, defense contractors, and regulated industries.

## How the images are built

The `-fips` variants are built on top of [Chainguard FIPS container images](https://edu.chainguard.dev/chainguard/fips/fips-images/), which ship NIST-validated cryptographic modules (OpenSSL FIPS provider, Bouncy Castle FIPS, or BoringCrypto depending on the base). For the list of modules and their CMVP certificates, refer to [Chainguard's FIPS commitment](https://edu.chainguard.dev/chainguard/fips/fips-images/).

Every LangChain-authored image has a `-fips` counterpart published at the same tag as the non-FIPS version:

| Non-FIPS image                       | FIPS image                                |
| ------------------------------------ | ----------------------------------------- |
| `langchain/langsmith-ace-backend`    | `langchain/langsmith-ace-backend-fips`    |
| `langchain/langsmith-backend`        | `langchain/langsmith-backend-fips`        |
| `langchain/langsmith-frontend`       | `langchain/langsmith-frontend-fips`       |
| `langchain/langsmith-go-backend`     | `langchain/langsmith-go-backend-fips`     |
| `langchain/langsmith-playground`     | `langchain/langsmith-playground-fips`     |
| `langchain/hosted-langserve-backend` | `langchain/hosted-langserve-backend-fips` |
| `langchain/langgraph-operator`       | `langchain/langgraph-operator-fips`       |

PostgreSQL, Redis, and ClickHouse are not published as FIPS variants by LangChain. If your deployment requires FIPS for these components, bring your own FIPS-mode service and connect via [external Postgres](/langsmith/self-host-external-postgres), [external Redis](/langsmith/self-host-external-redis), or [external ClickHouse](/langsmith/self-host-external-clickhouse).

## Use FIPS images

Update `values.yaml` in your LangSmith Helm installation to point each LangChain image repository at its `-fips` counterpart, keeping your existing tag. Replace `0.15.0` with the [LangSmith version](/langsmith/self-hosted-changelog) you want to deploy:

```yaml theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
images:
  aceBackendImage:
    repository: "langchain/langsmith-ace-backend-fips"
    pullPolicy: IfNotPresent
    tag: "0.15.0"
  backendImage:
    repository: "langchain/langsmith-backend-fips"
    pullPolicy: IfNotPresent
    tag: "0.15.0"
  frontendImage:
    repository: "langchain/langsmith-frontend-fips"
    pullPolicy: IfNotPresent
    tag: "0.15.0"
  hostBackendImage:
    repository: "langchain/hosted-langserve-backend-fips"
    pullPolicy: IfNotPresent
    tag: "0.15.0"
  operatorImage:
    repository: "langchain/langgraph-operator-fips"
    pullPolicy: IfNotPresent
    tag: "0.15.0"
  platformBackendImage:
    repository: "langchain/langsmith-go-backend-fips"
    pullPolicy: IfNotPresent
    tag: "0.15.0"
  playgroundImage:
    repository: "langchain/langsmith-playground-fips"
    pullPolicy: IfNotPresent
    tag: "0.15.0"
```

Apply the change and upgrade following the [Upgrading LangSmith](/langsmith/self-host-upgrades) guide.

## Verify FIPS mode

Chainguard ships the `openssl-fips-test` tool inside every FIPS image. Running it against a pod prints the FIPS self-tests, the active FIPS provider version, and a link to the applicable CMVP certificate.

Check a running pod:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
kubectl exec <pod-name> -- openssl-fips-test
```

Expected output (abridged):

```text theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
Checking OpenSSL lifecycle assurance.
	✓ Self-test KAT_Integrity HMAC ... passed.
	✓ Self-test Module_Integrity HMAC ... passed.
	...
	✓ 29 out of 29 self-tests passed.
	✓ Check FIPS cryptographic module is available... passed.
	✓ Check FIPS approved only mode (EVP_default_properties_is_fips_enabled)... passed.
Public OpenSSL API (libssl.so & libcrypto.so):
	name:      OpenSSL 3.6.0 1 Oct 2025
	version:   3.6.0
FIPS cryptographic module provider details (fips.so):
	name:      OpenSSL FIPS Provider
	version:   3.1.2
Locate applicable CMVP certificate(s) at: CMVP #4985
```

You can also verify an image outside Kubernetes:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
docker run --rm --entrypoint openssl-fips-test langchain/langsmith-go-backend-fips:0.15.0
```

For more detail on interpreting the output, see [Chainguard's FIPS verification guide](https://edu.chainguard.dev/chainguard/fips/verify-fips/).

## Mirror for airgapped deployments

The `-fips` naming convention applies identically when mirroring images to a private registry. Follow the [image mirroring guide](/langsmith/self-host-mirroring-images) and substitute each repository with its `-fips` counterpart. Airgapped rollouts, with or without FIPS, require scoping with your LangChain account executive before you begin.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/self-host-fips.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Create an Ingress for installations (Kubernetes)
Source: https://docs.langchain.com/langsmith/self-host-ingress

By default, LangSmith will provision a LoadBalancer service for the `langsmith-frontend`. Depending on your cloud provider, this may result in a public IP address being assigned to the service. If you would like to use a custom domain or have more control over the routing of traffic to your LangSmith installation, you can configure an Ingress, Gateway API, or Istio Gateway.

## Requirements

* An existing Kubernetes cluster
* One of the following installed in your Kubernetes cluster:
  * An Ingress Controller (for standard Ingress)
  * Gateway API CRDs and a Gateway resource (for Gateway API)
  * Istio (for Istio Gateway)

## Parameters

You may need to provide certain parameters to your LangSmith installation to configure the Ingress. Additionally, we will want to convert the `langsmith-frontend` service to a ClusterIP service.

* *Hostname (optional)*: The hostname that you would like to use for your LangSmith installation. E.g `"langsmith.example.com"`. If you leave this empty, the ingress will serve all traffic to the LangSmith installation.

* *BasePath (optional)*: If you would like to serve LangSmith under a URL basePath, you can specify it here. For example, adding `"langsmith"` will serve the application at `"example.hostname.com/langsmith"`. This will apply to UI paths as well as API endpoints.

* *IngressClassName (optional)*: The name of the Ingress class that you would like to use. If not set, the default Ingress class will be used.

* *Annotations (optional)*: Additional annotations to add to the Ingress. Certain providers like AWS may use annotations to control things like TLS termination.

  For example, you can add the following annotations using the AWS ALB Ingress Controller to attach an ACM certificate to the Ingress:

  ```yaml theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  annotations:
    alb.ingress.kubernetes.io/certificate-arn: "<your-certificate-arn>"
  ```

* *Labels (optional)*: Additional labels to add to the Ingress.

* *TLS (optional)*: If you would like to serve LangSmith over HTTPS, you can add TLS configuration here (many Ingress controllers may have other ways of controlling TLS so this is often not needed). This should be an array of TLS configurations. Each TLS configuration should have the following fields:

  * hosts: An array of hosts that the certificate should be valid for. E.g \["langsmith.example.com"]

  * secretName: The name of the Kubernetes secret that contains the certificate and private key. This secret should have the following keys:

    * tls.crt: The certificate
    * tls.key: The private key

  * For more information, see [creating a TLS secret](https://kubernetes.io/do/langsmith/observability-concepts/services-networking/ingress/#tls).

## Configuration

You can configure your LangSmith instance to use one of three routing options: standard Ingress, Gateway API, or Istio Gateway. Choose the option that best fits your infrastructure.

### Option 1: Standard ingress

With these parameters in hand, you can configure your LangSmith instance to use an Ingress. You can do this by modifying the `config.yaml` file for your LangSmith Helm Chart installation.

```yaml theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
config:
  hostname: "" # Main domain for LangSmith
  basePath: "" # If you want to serve langsmith under a URL base path (e.g., /langsmith)
ingress:
  enabled: true
  hostname: "" # Deprecated: Use config.hostname instead after v0.12.0
  subdomain: "" # Deprecated: Use config.hostname instead after v0.12.0
  ingressClassName: "" # If not set, the default ingress class will be used
  annotations: {} # Add annotations here if needed
  labels: {} # Add labels here if needed
  tls: [] # Add TLS configuration here if needed
frontend:
  service:
    type: ClusterIP
```

Once configured, you will need to update your LangSmith installation. If everything is configured correctly, your LangSmith instance should now be accessible via the Ingress. You can run the following to check the status of your Ingress:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
kubectl get ingress
```

You should see something like this in the output:

```
NAME                         CLASS   HOSTS    ADDRESS          PORTS     AGE
langsmith-ingress            nginx   <host>   35.227.243.203   80, 443   95d
```

<Warning>
  If you do not have automated DNS setup, you will need to add the IP address to your DNS provider manually.
</Warning>

### Option 2: Gateway API

<Note>
  Gateway API support is available as of LangSmith v0.12.0
</Note>

If your cluster uses the [Kubernetes Gateway API](https://gateway-api.sigs.k8s.io/), you can configure LangSmith to provision HTTPRoute resources. This will create an HTTPRoute for LangSmith and an HTTPRoute for each [agent deployment](/langsmith/deployment).

#### Parameters

* *name (required)*: The name of the Gateway resource to reference
* *namespace (required)*: The namespace where the Gateway resource is located
* *hostname (optional)*: The hostname that you would like to use for your LangSmith installation. E.g `"langsmith.example.com"`
* *basePath (optional)*: If you would like to serve LangSmith under a base path, you can specify it here. E.g "example.com/langsmith"
* *sectionName (optional)*: The name of a specific listener section in the Gateway to use
* *annotations (optional)*: Additional annotations to add to the HTTPRoute resources
* *labels (optional)*: Additional labels to add to the HTTPRoute resources

#### Configuration

```yaml theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
config:
  hostname: "" # Main domain for LangSmith
  basePath: "" # If you want to serve langsmith under a base path. E.g "example.com/langsmith"
gateway:
  enabled: true
  name: "my-gateway" # Name of your Gateway resource
  namespace: "gateway-system" # Namespace of your Gateway resource
  sectionName: "" # Optional: specific listener section name
  annotations: {} # Add annotations here if needed
  labels: {} # Add labels here if needed
frontend:
  service:
    type: ClusterIP
```

Once configured, you can check the status of your HTTPRoutes:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
kubectl get httproute
```

### Option 3: Istio Gateway

<Note>
  Istio Gateway support is available as of LangSmith v0.12.0
</Note>

If your cluster uses [Istio](https://istio.io/), you can configure LangSmith to provision VirtualService resources. This will create a VirtualService for LangSmith and a VirtualService for each [agent deployment](/langsmith/deployment).

#### Parameters

* *name (optional)*: The name of the Istio Gateway resource to reference. Defaults to `"istio-gateway"`
* *namespace (optional)*: The namespace where the Istio Gateway resource is located. Defaults to `"istio-system"`
* *hostname (optional)*: The hostname that you would like to use for your LangSmith installation. E.g `"langsmith.example.com"`
* *basePath (optional)*: If you would like to serve LangSmith under a base path, you can specify it here. E.g "example.com/langsmith"
* *annotations (optional)*: Additional annotations to add to the VirtualService resources
* *labels (optional)*: Additional labels to add to the VirtualService resources

#### Configuration

```yaml theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
config:
  hostname: "" # Main domain for LangSmith
  basePath: "" # If you want to serve langsmith on a separate basePath. E.g "example.com/langsmith"
istioGateway:
  enabled: true
  name: "istio-gateway" # Name of your Istio Gateway resource
  namespace: "istio-system" # Namespace of your Istio Gateway resource
  annotations: {} # Add annotations here if needed
  labels: {} # Add labels here if needed
frontend:
  service:
    type: ClusterIP
```

Once configured, you can check the status of your VirtualServices:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
kubectl get virtualservice
```

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/self-host-ingress.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Mirror images for your LangSmith installation
Source: https://docs.langchain.com/langsmith/self-host-mirroring-images

By default, LangSmith will pull images from our public Docker registry. However, if you are running LangSmith in an environment that does not have internet access, or if you would like to use a private Docker registry, you can mirror the images to your own registry and then configure your LangSmith installation to use those images.

## Requirements

* Authenticated access to a Docker registry that your Kubernetes cluster/machine has access to.
* Docker installed on your local machine or a machine that has access to the Docker registry.
* A Kubernetes cluster where you can run LangSmith.

## Mirroring the images

For your convenience, we have provided a script that will mirror the images for you. You can find the script in the [LangSmith Helm Chart repository](https://github.com/langchain-ai/helm/blob/main/charts/langsmith/scripts/mirror_langsmith_images.sh)

To use the script, you will need to run the script with the following command specifying your registry and platform:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
bash mirror_images.sh <your-registry> [<platform>]
```

Where `<your-registry>` is the URL of your Docker registry (e.g. `myregistry.com`) and `<platform>` is the platform you are using (e.g. `linux/amd64`, `linux/arm64`, etc.). If you do not specify a platform, it will default to `linux/amd64`.

For example, if your registry is `myregistry.com`, your platform is `linux/arm64`, and you want to use the latest version of the images, you would run:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
bash mirror_langsmith_images.sh --registry myregistry --platform linux/arm64 --version 0.10.66
```

Note that this script will assume that you have Docker installed and that you are authenticated to your registry. It will also push the images to the specified registry with the same repository/tag as the original images.

Alternatively, you can pull, mirror, and push the images manually. The images that you will need to mirror are found in the `values.yaml` file of the LangSmith Helm Chart. These can be found here: [LangSmith Helm Chart values.yaml](https://github.com/langchain-ai/helm/blob/main/charts/langsmith/values.yaml#L14)

Here is an example of how to mirror the images using Docker:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
