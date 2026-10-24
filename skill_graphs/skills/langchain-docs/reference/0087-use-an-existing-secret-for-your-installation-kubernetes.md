# Use an existing secret for your installation (Kubernetes)
Source: https://docs.langchain.com/langsmith/self-host-using-an-existing-secret

By default, LangSmith will provision several Kubernetes secrets to store sensitive information such as license keys, salts, and other configuration parameters. However, you may want to use an existing secret that you have already created in your Kubernetes cluster (or provisioned via some sort of secrets operator). This can be useful if you want to manage sensitive information in a centralized way or if you have specific security requirements.

By default we will provision the following secrets corresponding to different components of LangSmith:

* `langsmith-secrets`: This secret contains the license key and some other basic configuration parameters. To get started, use the [secrets template](https://github.com/langchain-ai/helm/blob/main/charts/langsmith/templates/secrets.yaml).
* `langsmith-redis`: This secret contains the Redis connection string (or node URIs if using Redis cluster) and password. To get started, use the [Redis secrets template](https://github.com/langchain-ai/helm/blob/main/charts/langsmith/templates/redis/secrets.yaml).
* `langsmith-postgres`: This secret contains the Postgres connection string and password. To get started, use the [Postgres secrets template](https://github.com/langchain-ai/helm/blob/main/charts/langsmith/templates/postgres/secrets.yaml).
* `langsmith-clickhouse`: This secret contains the ClickHouse connection string and password. To get started, use the [ClickHouse secrets template](https://github.com/langchain-ai/helm/blob/main/charts/langsmith/templates/clickhouse/secrets.yaml).

## Requirements

* An existing Kubernetes cluster
* A way to create Kubernetes secrets in your cluster. This can be done using `kubectl`, a Helm chart, or a secrets operator like [Sealed Secrets](https://github.com/bitnami-labs/sealed-secrets)

## Parameters

You will need to create your own Kubernetes secrets that adhere to the structure of the secrets provisioned by the LangSmith Helm Chart.

<Warning>
  The secrets must have the same structure as the ones provisioned by the LangSmith Helm Chart (refer to the links above to see the specific secrets). If you miss any of the required keys, your LangSmith instance may not work correctly.
</Warning>

An example secret may look like this:

<Warning>
  Set `api_key_salt` once and do not change it. This value is used to hash all API keys at rest. Rotating it will permanently invalidate every existing API key in your organization, requiring all users to regenerate their keys.
</Warning>

```yaml theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
apiVersion: v1
kind: Secret
metadata:
  name: langsmith-secrets
  namespace: langsmith
stringData:
  oauth_client_id: foo
  oauth_client_secret: foo
  oauth_issuer_url: foo
  langsmith_license_key: foo
  langgraph_cloud_license_key: foo
  api_key_salt: foo
  jwt_secret: foo
  initial_org_admin_password: foo
  blob_storage_access_key: foo
  blob_storage_access_key_secret: foo
  azure_storage_account_key: foo
  azure_storage_connection_string: foo
  agent_builder_encryption_key: foo
  insights_encryption_key: foo
  # Chat (formerly Polly)
  polly_encryption_key: foo
```

## Configuration

With these secrets provisioned, you can configure your LangSmith instance to use the secrets directly to avoid passing in secret values through plaintext. You can do this by modifying the `langsmith_config.yaml` file for your LangSmith Helm Chart installation.

```yaml theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
config:
  existingSecretName: "langsmith-secrets" # The name of the secret that contains the license key and other basic configuration parameters  # sanitizer:ignore
redis:
  external:
    enabled: true # Set to true to use an external Redis instance. This secret is only needed if you are using an external Redis instance
    existingSecretName: "langsmith-redis" # The name of the secret that contains the Redis connection string and password
postgres:
  external:
    enabled: true # Set to true to use an external Postgres instance. This secret is only needed if you are using an external Postgres instance
    existingSecretName: "langsmith-postgres" # The name of the secret that contains the Postgres connection string and password  # sanitizer:ignore
clickhouse:
  external:
    enabled: true # Set to true to use an external ClickHouse instance. This secret is only needed if you are using an external ClickHouse instance
    existingSecretName: "langsmith-clickhouse" # The name of the secret that contains the ClickHouse connection string and password  # sanitizer:ignore
```

Once configured, you will need to update your LangSmith installation. You can follow the [upgrade guide](/langsmith/self-host-upgrades). If everything is configured correctly, your LangSmith instance should now be accessible via the Ingress. You can run the following to check that your secrets are being used correctly:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
kubectl describe deployment langsmith-backend | grep -i <secret-name>
```

You should see something like this in the output:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
POSTGRES_DATABASE_URI:                    <set to the key 'connection_url' in secret <your-secret-name>  Optional: false
CLICKHOUSE_DB:                            <set to the key 'clickhouse_db' in secret <your-secret-name>   Optional: false
```

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/self-host-using-an-existing-secret.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Self-hosted LangSmith
Source: https://docs.langchain.com/langsmith/self-hosted

<Note>
  **Important**<br />
  Self-hosted LangSmith is an add-on to the Enterprise plan designed for our largest, most security-conscious customers. For more details, refer to [Pricing](https://www.langchain.com/pricing). [Contact our sales team](https://www.langchain.com/contact-sales) if you want to get a license key to trial LangSmith in your environment.
</Note>

Host an instance of LangSmith in your own infrastructure for [observability](/langsmith/observability), [evaluation](/langsmith/evaluation), and [prompt engineering](/langsmith/prompt-engineering). You can optionally enable [LangSmith Deployment](/langsmith/deploy-self-hosted-full-platform) to deploy and manage agents through the LangSmith UI.

<Tip>
  **For step-by-step setup instructions for self-hosted LangSmith on AWS, GCP, or Azure**, refer to our cloud architecture guides: [AWS](/langsmith/aws-self-hosted), [GCP](/langsmith/gcp-self-hosted), or [Azure](/langsmith/azure-self-hosted).
</Tip>

<Note>
  Before installing or upgrading, review the [minimum versions for self-hosting dependencies](/langsmith/self-host-dependency-versions).
</Note>

<a />

## What's included

A self-hosted LangSmith instance includes:

**Services:**

* LangSmith frontend UI
* LangSmith backend API
* LangSmith Platform backend
* LangSmith Playground
* LangSmith queue
* LangSmith ACE (Arbitrary Code Execution) backend

**Storage services:**

* ClickHouse (traces and feedback data)
* PostgreSQL (operational data)
* Redis (queuing and caching)
* Blob storage (optional, but recommended for production)

<img alt="LangSmith architecture showing services and datastores" />

<img alt="LangSmith architecture showing services and datastores" />

To access the LangSmith UI and send API requests, you will need to expose the [LangSmith frontend](#services) service. Depending on your installation method, this can be a load balancer or a port exposed on the host machine.

### Services

| Service                                                    | Description                                                                                                                                                                                                                                                                                                                                              |
| ---------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <a /> **LangSmith frontend**                               | The frontend uses Nginx to serve the LangSmith UI and route API requests to the other servers. This serves as the entrypoint for the application and is the only component that must be exposed to users.                                                                                                                                                |
| <a /> **LangSmith backend**                                | The backend is the main entrypoint for CRUD API requests and handles the majority of the business logic for the application. This includes handling requests from the frontend and SDK, preparing traces for ingestion, and supporting the hub API.                                                                                                      |
| <a /> **LangSmith queue**                                  | The queue handles incoming traces and feedback to ensure that they are ingested and persisted into the traces and feedback datastore asynchronously, handling checks for data integrity and ensuring successful insert into the datastore, handling retries in situations such as database errors or the temporary inability to connect to the database. |
| <a /> **LangSmith platform backend**                       | The platform backend is another critical service that primarily handles authentication, run ingestion, and other high-volume tasks.                                                                                                                                                                                                                      |
| <a /> **LangSmith Playground**                             | The Playground is a service that handles forwarding requests to various LLM APIs to support the Playground feature. This can also be used to connect to your own custom model servers.                                                                                                                                                                   |
| <a /> **LangSmith ACE (Arbitrary Code Execution) backend** | The ACE backend is a service that handles executing arbitrary code in a secure environment. This is used to support running custom code within LangSmith.                                                                                                                                                                                                |

### Storage services

<Note>
  LangSmith will bundle all storage services by default. You can configure it to use external versions of all storage services. In a production setting, we **strongly recommend using external storage services**.
</Note>

| Service                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <a /> **ClickHouse**     | [ClickHouse](https://clickhouse.com/docs/en/intro) is a high-performance, column-oriented SQL database management system (DBMS) for online analytical processing (OLAP).<br /><br />LangSmith uses ClickHouse as the primary data store for traces and feedback (high-volume data).<br /><br />💡 [Connect to external ClickHouse](/langsmith/self-host-external-clickhouse)                                                                                                                                                                                                  |
| <a /> **PostgreSQL**     | [PostgreSQL](https://www.postgresql.org/about/) is a powerful, open source object-relational database system that uses and extends the SQL language combined with many features that safely store and scale the most complicated data workloads.<br /><br />LangSmith uses PostgreSQL as the primary data store for transactional workloads and operational data (almost everything besides traces and feedback).<br /><br />💡 [Connect to external PostgreSQL](/langsmith/self-host-external-postgres) - AWS RDS, GCP Cloud SQL, Azure Database                             |
| <a /> **Redis / Valkey** | [Redis](https://github.com/redis/redis) is a powerful in-memory key-value database that persists on disk. By holding data in memory, Redis offers high performance for operations like caching.<br /><br />LangSmith uses Redis to back queuing and caching operations. [Valkey](https://valkey.io/) is also officially supported as a drop-in replacement for Redis.<br /><br />💡 [Connect to external Redis or Valkey](/langsmith/self-host-external-redis) - AWS ElastiCache, GCP Memorystore, Azure Cache                                                                |
| <a /> **Blob storage**   | LangSmith supports several blob storage providers, including [AWS S3](https://aws.amazon.com/s3/), [Azure Blob Storage](https://azure.microsoft.com/en-us/services/storage/blobs/), and [Google Cloud Storage](https://cloud.google.com/storage).<br /><br />LangSmith uses blob storage to store large files, such as trace artifacts, feedback attachments, and other large data objects. Blob storage is optional, but highly recommended for production deployments.<br /><br />💡 [Enable blob storage](/langsmith/self-host-blob-storage) - AWS S3, GCP GCS, Azure Blob |

To install, follow the [Kubernetes setup guide](/langsmith/kubernetes).

## Next steps

* **[Enable LangSmith Deployment](/langsmith/deploy-self-hosted-full-platform)**: add a [control plane](/langsmith/control-plane) and [data plane](/langsmith/data-plane) to deploy and manage agents through the LangSmith UI.
* **[Deploy standalone Agent Servers](/langsmith/deploy-standalone-server)**: deploy Agent Servers directly without enabling LangSmith Deployment.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/self-hosted.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
