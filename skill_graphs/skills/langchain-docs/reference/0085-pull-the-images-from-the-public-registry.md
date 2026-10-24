# Pull the images from the public registry
docker pull langchain/langsmith-backend:latest
docker tag langchain/langsmith-backend:latest <your-registry>/langsmith-backend:latest
docker push <your-registry>/langsmith-backend:latest
```

You will need to repeat this for each image that you want to mirror.

## Configuration

Once the images are mirrored, you will need to configure your LangSmith installation to use the mirrored images. You can do this by modifying the `values.yaml` file for your LangSmith Helm Chart installation. Replace tag with the version you want to use, e.g. `0.10.66` for the latest version at the time of writing.

```yaml theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
images:
  imagePullSecrets: [] # Add your image pull secrets here if needed
  registry: "" # Set this to your registry URL if you mirrored all images to the same registry using our script. Then you can remove the repository prefix from the images below.
  aceBackendImage:
    repository: "(your-registry)/langchain/langsmith-ace-backend"
    pullPolicy: IfNotPresent
    tag: "0.10.66"
  backendImage:
    repository: "(your-registry)/langchain/langsmith-backend"
    pullPolicy: IfNotPresent
    tag: "0.10.66"
  frontendImage:
    repository: "(your-registry)/langchain/langsmith-frontend"
    pullPolicy: IfNotPresent
    tag: "0.10.66"
  hostBackendImage:
    repository: "(your-registry)/langchain/hosted-langserve-backend"
    pullPolicy: IfNotPresent
    tag: "0.10.66"
  operatorImage:
    repository: "(your-registry)/langchain/langgraph-operator"
    pullPolicy: IfNotPresent
    tag: "6cc83a8"
  platformBackendImage:
    repository: "(your-registry)/langchain/langsmith-go-backend"
    pullPolicy: IfNotPresent
    tag: "0.10.66"
  playgroundImage:
    repository: "(your-registry)/langchain/langsmith-playground"
    pullPolicy: IfNotPresent
    tag: "0.10.66"
  postgresImage:
    repository: "(your-registry)/postgres"
    pullPolicy: IfNotPresent
    tag: "14.7"
  redisImage:
    repository: "(your-registry)/redis"
    pullPolicy: IfNotPresent
    tag: "7"
  clickhouseImage:
    repository: "(your-registry)/clickhouse/clickhouse-server"
    pullPolicy: Always
    tag: "24.8"
```

## Additional images for Fleet and Insights

If you are using Fleet or Insights, the LangGraph operator dynamically creates Redis and PostgreSQL (pgvector) pods for each deployment. These pods use images defined in operator templates that require separate configuration.

You must mirror these additional images:

* `docker.io/redis:7`
* `docker.io/pgvector/pgvector:pg15`

Then override the operator templates in your `values.yaml` to use your mirrored images:

```yaml theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
operator:
  templates:
    redis: |
      apiVersion: apps/v1
      kind: Deployment
      metadata:
        name: ${service_name}
        namespace: ${namespace}
      spec:
        replicas: 1
        selector:
          matchLabels:
            app: ${service_name}
        template:
          metadata:
            labels:
              app: ${service_name}
          spec:
            enableServiceLinks: false
            containers:
            - name: redis
              image: (your-registry)/redis:7
              ports:
              - containerPort: 6379
                name: redis
              livenessProbe:
                exec:
                  command:
                  - redis-cli
                  - ping
                initialDelaySeconds: 30
                periodSeconds: 10
              readinessProbe:
                tcpSocket:
                  port: 6379
                initialDelaySeconds: 10
                periodSeconds: 5
    db: |
      apiVersion: apps/v1
      kind: StatefulSet
      metadata:
        name: ${service_name}
      spec:
        serviceName: ${service_name}
        selector:
          matchLabels:
            app: ${service_name}
        persistentVolumeClaimRetentionPolicy:
          whenDeleted: Delete
          whenScaled: Retain
        template:
          metadata:
            labels:
              app: ${service_name}
          spec:
            containers:
            - name: postgres
              image: (your-registry)/pgvector/pgvector:pg15
              ports:
              - containerPort: 5432
              command: ["docker-entrypoint.sh"]
              args:
                - postgres
                - -c
                - max_connections=${max_connections}
              env:
              - name: PGDATA
                value: /var/lib/postgresql/data/pgdata
              volumeMounts:
              - name: postgres-data
                mountPath: /var/lib/postgresql/data
            enableServiceLinks: false
        volumeClaimTemplates:
        - metadata:
            name: postgres-data
          spec:
            accessModes: ["ReadWriteOnce"]
            resources:
              requests:
                storage: "${storage_gi}Gi"
```

Replace `(your-registry)` with your registry URL. The template variables (`${service_name}`, `${namespace}`, `${max_connections}`, `${storage_gi}`) are replaced by the operator at runtime and must be kept as-is.

Once configured, you will need to update your LangSmith installation. You can follow our upgrade guide here: [Upgrading LangSmith](/langsmith/self-host-upgrades). If your upgrade is successful, your LangSmith instance should now be using the mirrored images from your Docker registry.

## Verifying image signatures

<Note>
  Image signatures are available **starting with v15** (LangSmith app version `0.15.x` and later). Earlier releases on the `v14-stable` and older channels are not signed and cannot be verified with the steps below.
</Note>

Stable-channel LangSmith images on `docker.io/langchain/*` are signed at release time using keyless [Sigstore/Cosign](https://docs.sigstore.dev/cosign/overview/) from the release workflow. The signing identity is bound to a specific GitHub Actions workflow, run, and commit, so the signature attests not just that the image is authentic but that it was produced by the stable-branch release pipeline running in `langchain-ai/langchainplus`. You can verify a signature before pulling or mirroring an image, and again after mirroring to confirm the digest you mirrored matches what we signed.

Install `cosign` ([installation guide](https://docs.sigstore.dev/cosign/system_config/installation/)), then verify any tag:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
cosign verify \
  --certificate-oidc-issuer https://token.actions.githubusercontent.com \
  --certificate-identity-regexp 'https://github\.com/langchain-ai/langchainplus/\.github/workflows/release_self_hosted_on_version_bump\.yaml@refs/heads/v[0-9]+-stable' \
  docker.io/langchain/langsmith-backend:<tag>
```

A successful verification confirms:

* The cosign claims on the signature are valid.
* The certificate chains to the Sigstore root and is logged in the [Rekor](https://docs.sigstore.dev/rekor/overview/) transparency log.
* The signing certificate was issued to the stable-branch release workflow via GitHub Actions OIDC.

The same command works against any of the released images by substituting the repository (`langsmith-frontend`, `langsmith-go-backend`, `agent-builder-deep-agent`, `langsmith-clio`, `langsmith-polly`, `agent-builder-tool-server`, `agent-builder-trigger-server`, `hosted-langserve-backend`, `langsmith-playground`, `langsmith-ace-backend`, plus their `*-fips` variants).

### Pinning to a specific release

For stricter verification — for example, pinning to a single stable branch or a specific commit — drop the regex and supply the exact certificate identity. Each signature's certificate also carries the workflow run ID and commit SHA as Subject Alternative Name extensions, so you can constrain to a specific release:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
cosign verify \
  --certificate-oidc-issuer https://token.actions.githubusercontent.com \
  --certificate-identity 'https://github.com/langchain-ai/langchainplus/.github/workflows/release_self_hosted_on_version_bump.yaml@refs/heads/v15-stable' \
  docker.io/langchain/langsmith-backend:0.15.9
```

To inspect the certificate's claims (workflow run, commit, runner), download the attestation and decode the embedded certificate:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
cosign download attestation docker.io/langchain/langsmith-backend:<tag>
```

### Verifying SBOM attestations

Released images also carry signed SPDX software bill of materials (SBOM) attestations, one per architecture in the image index. The attestations are attached to the per-architecture child digests rather than to the multi-architecture tag, so `cosign verify-attestation` against a bare tag reports `no matching attestations`. Resolve the child digests first, then verify each one.

List the per-architecture digests for a tag:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
docker buildx imagetools inspect --raw docker.io/langchain/langsmith-backend:<tag> \
  | jq -r '.manifests[] | select(.platform.os == "linux") | .digest + "  " + .platform.architecture'
```

Verify the SBOM attestation on one of those digests:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
cosign verify-attestation \
  --type spdxjson \
  --certificate-oidc-issuer https://token.actions.githubusercontent.com \
  --certificate-identity-regexp 'https://github\.com/langchain-ai/langchainplus/\.github/workflows/release_self_hosted_on_version_bump\.yaml@refs/heads/v[0-9]+-stable' \
  docker.io/langchain/langsmith-backend@<digest>
```

A successful verification gives the same guarantees as the image signature: the attestation was produced by the stable-branch release workflow, and its claims are logged in the [Rekor](https://docs.sigstore.dev/rekor/overview/) transparency log.

To extract the SPDX document itself, decode the verified attestation payload:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
cosign verify-attestation \
  --type spdxjson \
  --certificate-oidc-issuer https://token.actions.githubusercontent.com \
  --certificate-identity-regexp 'https://github\.com/langchain-ai/langchainplus/\.github/workflows/release_self_hosted_on_version_bump\.yaml@refs/heads/v[0-9]+-stable' \
  docker.io/langchain/langsmith-backend@<digest> \
  | jq -r '.payload' | base64 -d | jq '.predicate'
```

The decoded predicate is a standard SPDX 2.3 document listing every package in that image.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/self-host-mirroring-images.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# View trace counts across your organization
Source: https://docs.langchain.com/langsmith/self-host-organization-charts

<Note>
  This feature is available on Helm chart versions 0.9.5 and later.
</Note>

LangSmith automatically generates and syncs organization usage charts for self-hosted installations.

These charts are available under `Settings > Usage and billing > Usage graph`:

* Usage by Workspace: this counts traces (root runs) by workspace
* Organization Usage: this counts all traces (root runs) for the organization

The charts are refreshed to include any new workspaces every 5 minutes. Note that the charts are not editable.

## Programmatically fetch trace counts

You can retrieve trace counts programmatically using two different methods:

### Method 1: Use the LangSmith REST API

If your self-hosted installation uses an online key, you can use the [LangSmith REST API](/langsmith/smith-api/orgs/get-org-usage) to fetch organization usage data.

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
curl -X GET "https://your-langsmith-instance.com/api/v1/orgs/current/billing/usage" \
  -H "Accept: application/json" \
  -H "X-API-Key: your-api-key" \
  -G \
  -d "starting_on=2025-09-01T00:00:00Z" \
  -d "ending_before=2025-10-01T00:00:00Z" \
  -d "on_current_plan=true"
```

### Method 2: Use PostgreSQL support queries

For installations using offline keys or when you need more detailed export capabilities, you can run support queries directly against the PostgreSQL database. All available scripts are in the [support queries repository](https://github.com/langchain-ai/helm/tree/main/charts/langsmith/scripts/support_queries/postgres).

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
sh run_support_query_pg.sh "postgres://postgres:postgres@localhost:5432/postgres" \
  --input support_queries/pg_get_trace_counts_daily.sql \
  --output trace_counts.csv
```

For more detailed information about running support queries, see the [Run support queries against PostgreSQL](/langsmith/script-running-pg-support-queries) guide.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/self-host-organization-charts.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Use environment variables for model providers
Source: https://docs.langchain.com/langsmith/self-host-playground-environment-settings

<Note>
  This feature is only available on Helm chart versions 0.10.27 (application version 0.10.74) and later.
</Note>

Many model providers support setting credentials and other configuration options through environment variables. This is useful for self-hosted deployments where you want to avoid hardcoding sensitive information in your code or configuration files. In LangSmith, most model interactions are done through the `playground` service, which allows you to configure many of those environment variables directly on the pod itself. This can be useful to avoid having to set credentials in the UI.

## Requirements

* A self-hosted LangSmith instance with the `playground` service running.
* The provider you want to configure must support environment variables for configuration. Check the provider's Chat Model [documentation](https://docs.langchain.com/oss/python/integrations/providers/overview) for more information.
* The secrets/roles you may want to attach to the `playground` service.
  * Note that for [IRSA](https://docs.aws.amazon.com/eks/latest/userguide/iam-roles-for-service-accounts.html) you may need to grant the `langsmith-playground` service account the necessary permissions to access the secrets or roles in your cloud provider.

## Configuration

With the parameters from above, you can configure your LangSmith instance to use environment variables for model providers. You can do this by modifying the `langsmith_config.yaml` file for your LangSmith Helm Chart installation or the `docker-compose.yaml` file for your Docker installation.

<CodeGroup>
  ```yaml Helm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  playground:
    deployment:
      extraEnv:
        - name: OPENAI_BASE_URL
          value: https://<my_proxy_url>
        - name: OPENAI_API_KEY
          valueFrom:
            secretKeyRef:
              name: <your_secret_name>
              key: api_key
    serviceAccount: # Can be useful if you want to use IRSA or workload identity
      annotations:
        eks.amazonaws.com/role-arn: <your_role_arn>
  ```

  ```yaml Docker theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  # In your docker-compose.yaml file
  langchain-playground:
    environment:
      .. # Other environment variables
      - OPENAI_BASE_URL=https://<my_proxy_url>
      - OPENAI_API_KEY=<your_key> # This will be set in the .env file
  ```
</CodeGroup>

## VertexAI configuration

You can configure VertexAI credentials for the playground service using either environment variables with secrets or workload identity (GCP Workload Identity for GKE or AWS IRSA for EKS).

### Using secrets

Configure VertexAI credentials using Kubernetes secrets:

<CodeGroup>
  ```yaml Helm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  playground:
    deployment:
      extraEnv:
        # Playground-specific secret (recommended)
        - name: GOOGLE_VERTEX_AI_WEB_CREDENTIALS
          valueFrom:
            secretKeyRef:
              name: gcp-vertexai-secret
              key: credentials_json  # Your full service account JSON as string
        # Standard fallback option
        - name: GOOGLE_APPLICATION_CREDENTIALS
          value: /secrets/gcp-key.json
        # Optional: Set project/location if not in model config
        - name: GOOGLE_CLOUD_PROJECT
          value: "your-gcp-project-id"
        - name: VERTEXAI_PROJECT_ID
          value: "your-gcp-project-id"
        - name: VERTEXAI_LOCATION
          value: "us-central1"
      extraVolumeMounts:
        - name: gcp-secret-volume
          mountPath: /secrets
          readOnly: true
      extraVolumes:
        - name: gcp-secret-volume
          secret:
            secretName: gcp-key-json  # JSON file secret
            defaultMode: 0444
  ```

  ```yaml Docker theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  # In your docker-compose.yaml file
  langchain-playground:
    environment:
      .. # Other environment variables
      - GOOGLE_VERTEX_AI_WEB_CREDENTIALS=<your_service_account_json>  # Full JSON as string
      # Or use file path
      - GOOGLE_APPLICATION_CREDENTIALS=/secrets/gcp-key.json
      - GOOGLE_CLOUD_PROJECT=your-gcp-project-id
      - VERTEXAI_PROJECT_ID=your-gcp-project-id
      - VERTEXAI_LOCATION=us-central1
    volumes:
      - ./gcp-key.json:/secrets/gcp-key.json:ro
  ```
</CodeGroup>

### Using workload identity

You can configure the playground service account to use workload identity to assume a GCP service account role without storing credentials. This is the recommended approach for GKE clusters.

#### GCP Workload Identity (GKE)

For GKE clusters, use GCP Workload Identity:

<CodeGroup>
  ```yaml Helm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  playground:
    deployment:
      extraEnv:
        # Optional: Set project/location if not in model config
        - name: GOOGLE_CLOUD_PROJECT
          value: "your-gcp-project-id"
        - name: VERTEXAI_PROJECT_ID
          value: "your-gcp-project-id"
        - name: VERTEXAI_LOCATION
          value: "us-central1"
      # No credentials needed - pod assumes GCP SA role via annotation
    serviceAccount:
      create: true  # Enable if not exists
      annotations:
        iam.gke.io/gcp-service-account: "vertexai-sa@your-gcp-project.iam.gserviceaccount.com"
  ```
</CodeGroup>

<Note>
  When using GCP Workload Identity, ensure the GCP service account has the required VertexAI permissions (e.g., `roles/aiplatform.user`).
</Note>

#### AWS IRSA (EKS)

For EKS clusters, you can use AWS IRSA to assume a GCP service account role:

<CodeGroup>
  ```yaml Helm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  playground:
    deployment:
      extraEnv:
        # Optional: Set project/location if not in model config
        - name: GOOGLE_CLOUD_PROJECT
          value: "your-gcp-project-id"
        - name: VERTEXAI_PROJECT_ID
          value: "your-gcp-project-id"
        - name: VERTEXAI_LOCATION
          value: "us-central1"
      # No credentials needed - pod assumes GCP SA role via AWS IAM role
    serviceAccount:
      create: true  # Enable if not exists
      annotations:
        eks.amazonaws.com/role-arn: arn:aws:iam::<account>:role/LangSmith-VertexAI-Role
  ```
</CodeGroup>

<Note>
  When using AWS IRSA, ensure your AWS IAM role has the necessary permissions to assume the GCP service account role, and that the GCP service account has the required VertexAI permissions.
</Note>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/self-host-playground-environment-settings.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Configure LangSmith for scale
Source: https://docs.langchain.com/langsmith/self-host-scale

<Warning>
  The scaling guidance and example configurations on this page apply to **LangSmith version v0.13.0 or higher**.
</Warning>

A self-hosted LangSmith instance can handle a large number of traces and users. The default configuration for the self-hosted deployment can handle substantial load, and you can configure your deployment to be able to achieve higher scale. This page describes scaling considerations and provides some examples to help configure your self-hosted instance.

For example configurations, refer to [Example LangSmith configurations for scale](#example-langsmith-configurations-for-scale).

## Summary

The table below provides an overview comparing different LangSmith configurations for various load patterns (reads / writes):

|                                                             | **[Low / low](#low-reads-low-writes)**               | **[Low / high](#low-reads-high-writes)**             | **[High / low](#high-reads-low-writes)**             | [Medium / medium](#medium-reads-medium-writes)       | [High / high](#high-reads-high-writes)               |
| :---------------------------------------------------------- | :--------------------------------------------------- | :--------------------------------------------------- | :--------------------------------------------------- | :--------------------------------------------------- | :--------------------------------------------------- |
| <Tooltip>Concurrent frontend users</Tooltip>                | 5                                                    | 5                                                    | 50                                                   | 20                                                   | 50                                                   |
| <Tooltip>Traces submitted per second</Tooltip>              | 10                                                   | 1000                                                 | 10                                                   | 100                                                  | 1000                                                 |
| **Frontend replicas**<br />(500m CPU, 1Gi per replica)      | 1 (default)                                          | 4                                                    | 2                                                    | 2                                                    | 4                                                    |
| **Platform backend replicas**<br />(1 CPU, 2Gi per replica) | 3 (default)                                          | 20                                                   | 3 (default)                                          | 3 (default)                                          | 20                                                   |
| **Ingest queue replicas**<br />(1 CPU, 2Gi per replica)     | 3 (default)                                          | 24                                                   | 3 (default)                                          | 6                                                    | 24                                                   |
| **Backend replicas**<br />(1 CPU, 2Gi per replica)          | 2 (default)                                          | 5                                                    | 40                                                   | 16                                                   | 50                                                   |
| **Redis resources**                                         | 8 Gi (default)                                       | 26 Gi external                                       | 8 Gi (default)                                       | 13Gi external                                        | 26 Gi external                                       |
| **ClickHouse resources**                                    | 4 CPU<br />16 Gi (default)                           | 10 CPU<br />32Gi memory                              | 8 CPU<br />16 Gi per replica                         | 16 CPU<br />24Gi memory                              | 14 CPU<br />24 Gi per replica                        |
| **ClickHouse setup**                                        | Single instance                                      | Single instance                                      | 3-node <Tooltip>replicated cluster</Tooltip>         | Single instance                                      | 3-node <Tooltip>replicated cluster</Tooltip>         |
| <Tooltip>Postgres resources</Tooltip>                       | 2 CPU<br />8 GB memory<br />10 GB storage (external) | 2 CPU<br />8 GB memory<br />10 GB storage (external) | 2 CPU<br />8 GB memory<br />10 GB storage (external) | 2 CPU<br />8 GB memory<br />10 GB storage (external) | 2 CPU<br />8 GB memory<br />10 GB storage (external) |
| **Blob storage**                                            | Disabled                                             | Enabled                                              | Enabled                                              | Enabled                                              | Enabled                                              |

Below we go into more details about the read and write paths as well as provide a `values.yaml` snippet for you to start with for your self-hosted LangSmith instance.

## Trace ingestion (write path)

Common usage that put load on the write path:

* Ingesting traces via the Python or JavaScript LangSmith SDK
* Ingesting traces via the `@traceable` wrapper
* Submitting traces via the `/runs/multipart` endpoint

Services that play a large role in trace ingestion:

* Platform backend service: Receives initial request to ingest traces and places traces on a Redis queue
* Redis cache: Used to queue traces that need to be persisted
* Ingest queue service: Persists traces for querying
* ClickHouse: Persistent storage used for traces

When scaling up the write path (trace ingestion), it is helpful to monitor the four services/resources listed above. Here are some typical changes that can help increase performance of trace ingestion:

* Give ClickHouse more resources (CPU and memory) if it is approaching resource limits.
* Increase the number of platform-backend pods if ingest requests are taking long to respond.
* Increase ingest queue service pod replicas if traces are not being processed from Redis fast enough.
* Use a larger Redis cache if you notice that the current Redis instance is reaching resource limits. This could also be a reason why ingest requests take a long time.

## Trace querying (read path)

Common usage that puts load on the read path:

* Users on the frontend looking at tracing projects or individual traces
* Scripts used to query for trace info
* Hitting either the `/runs/query` or `/runs/<run-id>` api endpoints

Services that play a large role in querying traces:

* Backend service: Receives the request and submits a query to ClickHouse to then respond to the request
* ClickHouse: Persistent storage for traces. This is the main database that is queried when requesting trace info.

When scaling up the read path (trace querying), it is helpful to monitor the two services/resources listed above. Here are some typical changes that can help improve performance of trace querying:

* Increase the number of backend service pods. This would be most impactful if backend service pods are reaching 1 core CPU usage.
* Give ClickHouse more resources (CPU or Memory). ClickHouse can be very resource intensive, but it should lead to better performance.
* Move to a [replicated ClickHouse cluster](/langsmith/self-host-external-clickhouse#ha-replicated-clickhouse-cluster). Adding replicas of ClickHouse helps with read performance, but we recommend staying below 5 replicas (start with 3).

For more precise guidance on how this translates to helm chart values, refer to the examples the following [section](#example-langsmith-configurations-for-scale). If you are unsure why your LangSmith instance cannot handle a certain load pattern, contact the LangChain team.

## KEDA autoscaling for LangSmith queues

<Note>
  Available in LangSmith v0.13.0 and later.
</Note>

We highly recommend installing [KEDA](https://keda.sh/) (Kubernetes Event-driven Autoscaling) on your cluster. KEDA enables the `queue` and `ingest-queue` services to scale automatically based on their queue backlog size, as well as CPU and memory. This results in more efficient resource utilization and better handling of traffic spikes.

### Install KEDA

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
helm repo add kedacore https://kedacore.github.io/charts
helm install keda kedacore/keda --namespace keda --create-namespace
```

### Configure KEDA autoscaling

Once KEDA is installed, you can enable KEDA-based autoscaling for the `queue` and `ingest-queue` services in your `values.yaml`:

```yaml theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
queue:
  autoscaling:
    keda:
      enabled: true

ingestQueue:
  autoscaling:
    keda:
      enabled: true
```

With KEDA enabled, the queue services will automatically scale up when their backlog grows and scale down when their backlog is processed. This is especially useful for handling variable trace ingestion loads without over-provisioning resources.

<Note>
  You can also enable KEDA for other services (`backend`, `platformBackend`, etc) but they will still only scale with CPU and memory.
</Note>

## Example LangSmith configurations for scale

Below we provide some example LangSmith configurations based on expected read and write loads.

For read load (trace querying):

* Low means roughly 5 users looking at traces at a time (about 10 requests per second)
* Medium means roughly 20 users looking at traces at a time (about 40 requests per second)
* High means roughly 50 users looking at traces at a time (about 100 requests per second)

For write load (trace ingestion):

* Low means up to 10 traces submitted per second
* Medium means up to 100 traces submitted per second
* High means up to 1000 traces submitted per second

<Note>
  The exact optimal configuration depends on your usage and trace payloads. Use the examples below in combination with the information above and your specific usage to update your LangSmith configuration as you see fit. If you have any questions, please reach out to the LangChain team.
</Note>

### Low reads, low writes <a name="low-reads-low-writes" />

The default LangSmith configuration will handle this load. No custom resource configuration is needed here.

### Low reads, high writes <a name="low-reads-high-writes" />

You have a very high scale of trace ingestions, but single digit number of users on the frontend querying traces at any one time.

For this, we recommend a configuration like this:

```yaml theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
config:
  blobStorage:
    # Please also set the other keys to connect to your blob storage. See configuration section.
    enabled: true
  settings:
    redisRunsExpirySeconds: "3600"

# ttl:

#   enabled: true

#   ttl_period_seconds:

#     longlived: "7776000"  # 90 days (default is 400 days)

#     shortlived: "604800"  # 7 days (default is 14 days)

frontend:
  deployment:
    replicas: 4 # OR enable autoscaling below

# autoscaling:

#   hpa:

#     enabled: true

#     minReplicas: 2

#     maxReplicas: 4

platformBackend:
  deployment:
    replicas: 20 # OR enable autoscaling below

# autoscaling:

#   hpa:

#     enabled: true

#     minReplicas: 8

#     maxReplicas: 20

ingestQueue:
  deployment:
    replicas: 24 # OR enable KEDA autoscaling below

# autoscaling:

#   keda:

#     enabled: true

#     minReplicaCount: 8

#     maxReplicaCount: 24

backend:
  deployment:
    replicas: 5 # OR enable autoscaling below

# autoscaling:

#   hpa:

#     enabled: true

#     minReplicas: 3

#     maxReplicas: 5

## Ensure your Redis cache is at least 26 GB for high write scale
redis:
  external:
    enabled: true
    existingSecretName: langsmith-redis-secret # Set the connection url for your external Redis instance (26+ GB)

clickhouse:
  statefulSet:
    persistence:
      # This may depend on your configured TTL (see config section).
      # We recommend 600Gi for every shortlived TTL day if operating at this scale constantly.
      size: 4200Gi # This assumes 7 days TTL and operating a this scale constantly.
    resources:
      requests:
        cpu: "10"
        memory: "32Gi"
      limits:
        cpu: "16"
        memory: "48Gi"

commonEnv:
  - name: "CLICKHOUSE_ASYNC_INSERT_WAIT_PCT_FLOAT"
    value: "0"
```

### High reads, low writes <a name="high-reads-low-writes" />

You have a relatively low scale of trace ingestions, but many frontend users querying traces and/or have scripts that hit the `/runs/query` or `/runs/<run-id>` endpoints frequently.

**For this, we strongly recommend setting up a replicated ClickHouse cluster to enable high read scale at low latency.** See our [external ClickHouse doc](/langsmith/self-host-external-clickhouse#ha-replicated-clickhouse-cluster) for more guidance on how to setup a replicated ClickHouse cluster. For this load pattern, we recommend using a 3 node replicated setup, where each replica in the cluster should have resource requests of 8+ cores and 16+ GB memory, and resource limit of 12 cores and 32 GB memory.

For this, we recommend a configuration like this:

```yaml theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
config:
  blobStorage:
    # Please also set the other keys to connect to your blob storage. See configuration section.
    enabled: true

frontend:
  deployment:
    replicas: 2

ingestQueue:
  deployment:
    replicas: 3 # OR enable KEDA autoscaling below

# autoscaling:

#   keda:

#     enabled: true

#     minReplicaCount: 2

#     maxReplicaCount: 3

backend:
  deployment:
    replicas: 40 # OR enable autoscaling below

# autoscaling:

#   hpa:

#     enabled: true

#     minReplicas: 16

#     maxReplicas: 40

# We strongly recommend setting up a replicated clickhouse cluster for this load.

# Update these values as needed to connect to your replicated clickhouse cluster.
clickhouse:
  external:
    # If using a 3 node replicated setup, each replica in the cluster should have resource requests of 8+ cores and 16+ GB memory, and resource limit of 12 cores and 32 GB memory.
    enabled: true
    host: langsmith-ch-clickhouse-replicated.default.svc.cluster.local
    port: "8123"
    nativePort: "9000"
    user: "default"
    password: "password"
    database: "default"
    cluster: "replicated"
```

### Medium reads, medium writes <a name="medium-reads-medium-writes" />

This is a good all around configuration that should be able to handle most usage patterns of LangSmith. In internal testing, this configuration allowed us to scale to 100 traces ingested per second and 40 read requests per second.

For this, we recommend a configuration like this:

```yaml theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
config:
  blobStorage:
    # Please also set the other keys to connect to your blob storage. See configuration section.
    enabled: true
  settings:
    redisRunsExpirySeconds: "3600"

frontend:
  deployment:
    replicas: 2

ingestQueue:
  deployment:
    replicas: 6 # OR enable KEDA autoscaling below

# autoscaling:

#   keda:

#     enabled: true

#     minReplicaCount: 3

#     maxReplicaCount: 6

backend:
  deployment:
    replicas: 16 # OR enable autoscaling below

# autoscaling:

#   hpa:

#     enabled: true

#     minReplicas: 8

#     maxReplicas: 16

redis:
  statefulSet:
    resources:
      requests:
        memory: 13Gi
      limits:
        memory: 13Gi

  # -- For external redis instead use something like below --
  # external:
  #   enabled: true
  #   connectionUrl: "<URL>" OR existingSecretName: "<SECRET-NAME>"

clickhouse:
  statefulSet:
    persistence:
      # This may depend on your configured TTL.
      # We recommend 60Gi for every shortlived TTL day if operating at this scale constantly.
      size: 420Gi # This assumes 7 days TTL and operating a this scale constantly.
    resources:
      requests:
        cpu: "16"
        memory: "24Gi"
      limits:
        cpu: "28"
        memory: "40Gi"

commonEnv:
  - name: "CLICKHOUSE_ASYNC_INSERT_WAIT_PCT_FLOAT"
    value: "0"
```

<Warning>
  If you still notice slow reads with the above configuration, we recommend moving to a [replicated Clickhouse cluster setup](/langsmith/self-host-external-clickhouse#ha-replicated-clickhouse-cluster)
</Warning>

### High reads, high writes <a name="high-reads-high-writes" />

You have a very high rate of trace ingestion (approaching 1000 traces submitted per second) and also have many users querying traces on the frontend (over 50 users) and/or scripts that are consistently making requests to `/runs/query` or `/runs/<run-id>` endpoints.

**For this, we very strongly recommend setting up a replicated ClickHouse cluster to prevent degraded read performance at high write scale.** See our [external ClickHouse doc](/langsmith/self-host-external-clickhouse#ha-replicated-clickhouse-cluster) for more guidance on how to set up a replicated ClickHouse cluster. For this load pattern, we recommend using a 3 node replicated setup, where each replica in the cluster should have resource requests of 14+ cores and 24+ GB memory, and resource limit of 20 cores and 48 GB memory. We also recommend that each node/instance of ClickHouse has 600 Gi of volume storage for each day of TTL that you enable (as per the configuration below).

Overall, we recommend a configuration like this:

```yaml theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
config:
  blobStorage:
    # Please also set the other keys to connect to your blob storage. See configuration section.
    enabled: true
  settings:
    redisRunsExpirySeconds: "3600"

# ttl:

#   enabled: true

#   ttl_period_seconds:

#     longlived: "7776000"  # 90 days (default is 400 days)

#     shortlived: "604800"  # 7 days (default is 14 days)

frontend:
  deployment:
    replicas: 4 # OR enable autoscaling below

# autoscaling:

#   hpa:

#     enabled: true

#     minReplicas: 2

#     maxReplicas: 4

platformBackend:
  deployment:
    replicas: 20 # OR enable autoscaling below

# autoscaling:

#   hpa:

#     enabled: true

#     minReplicas: 8

#     maxReplicas: 20

ingestQueue:
  deployment:
    replicas: 24 # OR enable KEDA autoscaling below

# autoscaling:

#   keda:

#     enabled: true

#     minReplicaCount: 8

#     maxReplicaCount: 24

backend:
  deployment:
    replicas: 50 # OR enable autoscaling below

# autoscaling:

#   hpa:

#     enabled: true

#     minReplicas: 20

#     maxReplicas: 50

## Ensure your Redis cache is at least 26 GB for high write scale
redis:
  external:
    enabled: true
    existingSecretName: langsmith-redis-secret # Set the connection url for your external Redis instance (26+ GB)

# We strongly recommend setting up a replicated clickhouse cluster for this load.

# Update these values as needed to connect to your replicated clickhouse cluster.
clickhouse:
  external:
    # If using a 3 node replicated setup, each replica in the cluster should have resource requests of 14+ cores and 24+ GB memory, and resource limit of 20 cores and 48 GB memory.
    enabled: true
    host: langsmith-ch-clickhouse-replicated.default.svc.cluster.local
    port: "8123"
    nativePort: "9000"
    user: "default"
    password: "password"
    database: "default"
    cluster: "replicated"

commonEnv:
  - name: "CLICKHOUSE_ASYNC_INSERT_WAIT_PCT_FLOAT"
    value: "0"
```

<Note>
  Ensure that the Kubernetes cluster is configured with sufficient resources to scale to the recommended size. After deployment, all of the pods in the Kubernetes cluster should be in a `Running` state. Pods stuck in `Pending` may indicate that you are reaching node pool limits or need larger nodes.

  Also, ensure that any ingress controller deployed on the cluster is able to handle the desired load to prevent bottlenecks.
</Note>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/self-host-scale.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
