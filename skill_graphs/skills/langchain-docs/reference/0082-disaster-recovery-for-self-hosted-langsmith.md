# Disaster recovery for self-hosted LangSmith
Source: https://docs.langchain.com/langsmith/self-host-disaster-recovery

This page describes how to plan, configure, and operate disaster recovery (DR) for self-hosted LangSmith Observability and Evaluation. It covers what data must be protected, where it lives, how to back it up, and how to recover the platform after a regional or zonal failure.

<Note>
  **Shared responsibility.** For self-hosted deployments you are responsible for backups, replication, restore testing, and recovery procedures for every component, including LangSmith pods and all backing data stores. LangChain is responsible only for the LangSmith software itself. For the equivalent SaaS responsibilities, see the [Shared responsibility model](/langsmith/shared-responsibility-model).
</Note>

<Tip>
  For details on the architectural primitives (stateless services, queue heartbeats, exactly-once semantics) that this page assumes, refer to [Scalability and resilience](/langsmith/scalability-and-resilience).
</Tip>

## What you are recovering

Self-hosted LangSmith is composed of stateless services backed by four state stores. Recovery planning is almost entirely about the state stores. You can recreate the stateless services at any time by reapplying the Helm chart.

| Layer                            | Components                                                                                                                                                            | State         | Recovery action                                       |
| -------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- | ----------------------------------------------------- |
| LangSmith services               | `langsmith-frontend`, `langsmith-backend`, `langsmith-platform-backend`, `langsmith-queue`, `langsmith-ingest-queue`, `langsmith-playground`, `langsmith-ace-backend` | Stateless     | Reinstall the Helm chart                              |
| PostgreSQL                       | Operational data: orgs, workspaces, users, API keys, datasets, prompts, projects, deployments metadata                                                                | **Durable**   | Restore from backup or replica                        |
| ClickHouse                       | Traces and feedback (high volume analytical data)                                                                                                                     | **Durable**   | Restore from backup or replica                        |
| Blob storage (S3/GCS/Azure Blob) | Run inputs, outputs, errors, manifests, extras, events, attachments (when enabled)                                                                                    | **Durable**   | Restore from versioned bucket or replica              |
| Redis (or Valkey)                | Ephemeral queue state, pub/sub, cache, run heartbeats                                                                                                                 | Ephemeral     | Reprovision; no restore required                      |
| Kubernetes objects               | Helm values, `Secret`s, TLS material, IRSA / Workload Identity bindings                                                                                               | Configuration | Re-apply from source control or back up cluster state |

<Warning>
  All durable data stores must be protected together. Postgres, ClickHouse, and blob storage are the three stores that hold durable data; Redis is ephemeral and does not need to be backed up. Restoring Postgres without ClickHouse and blob storage (or vice versa) produces an inconsistent installation. References from Postgres to runs in ClickHouse and to objects in blob storage break across the divergence point. Always take coordinated backups, or use point-in-time recovery (PITR) targets that are close together across stores.
</Warning>

## Plan your RPO and RTO

Before designing your DR architecture, define two targets:

* **Recovery Point Objective (RPO):** the maximum amount of data loss your organization can tolerate, measured in time. With managed Postgres PITR, RPO is typically less than 5 minutes. With nightly snapshots only, RPO can be up to 24 hours.
* **Recovery Time Objective (RTO):** the maximum time you can take to restore service after a failure. A warm cross-region replica can deliver RTO in minutes; a cold restore from snapshot can take hours, especially for large ClickHouse datasets.

The following deployment patterns assume one of three target profiles:

| Profile         | Typical RPO      | Typical RTO            | Approach                                                                                                                                                                                                                                                     |
| --------------- | ---------------- | ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Snapshot-only   | 6 to 24 hours    | Hours                  | Daily managed backups of each store. Lowest cost, longest restore.                                                                                                                                                                                           |
| Multi-AZ HA     | Seconds          | Minutes (zone failure) | Synchronous standby in another AZ for Postgres and ClickHouse, Multi-AZ Redis, zone-redundant blob storage. Standard production posture.                                                                                                                     |
| Cross-region DR | Minutes to hours | Hours                  | Backups of Postgres, ClickHouse, and blob storage copied to a second region, restored on demand. Optionally a Postgres cross-region replica for a tighter Postgres RPO. Highest cost, slower recovery than Multi-AZ, but protects against a regional outage. |

## Postgres

LangSmith uses PostgreSQL as the primary store for operational and transactional data. **All communication with Postgres uses retries for retry-able errors**, so a brief outage during failover usually does not surface as user-visible errors. A prolonged outage will render the LangSmith API unavailable.

### Use a managed service

We strongly recommend running Postgres on a managed service in production. Managed services provide built-in automated backups, PITR, and HA failover. For setup, refer to [Connect external Postgres](/langsmith/self-host-external-postgres).

<Tabs>
  <Tab title="AWS">
    Run [Amazon RDS for PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_GettingStarted.CreatingConnecting.PostgreSQL.html) or [Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Overview.html) in Multi-AZ mode.

    * **Backups:** Enable [automated backups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.html) with a retention window that matches your compliance posture (7 to 35 days is typical).
    * **PITR:** Automated backups include PITR within the retention window.
    * **HA:** Multi-AZ deployments maintain a synchronous standby in a second availability zone with automatic failover.
    * **Cross-region DR:** For Aurora, configure an [Aurora Global Database](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database.html). For RDS, use [cross-region read replicas](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.XRgn.html) or copy automated snapshots to a secondary region.
    * **Encryption:** Enable storage encryption with a customer-managed [KMS](https://aws.amazon.com/kms/) key.
  </Tab>

  <Tab title="GCP">
    Run [Cloud SQL for PostgreSQL](https://cloud.google.com/sql/docs/postgres) with [high availability](https://cloud.google.com/sql/docs/postgres/high-availability) enabled.

    * **Backups:** Enable [automated backups](https://cloud.google.com/sql/docs/postgres/backup-recovery/backups) with PITR.
    * **HA:** Regional instances replicate synchronously to a standby in a second zone.
    * **Cross-region DR:** Configure [cross-region read replicas](https://cloud.google.com/sql/docs/postgres/replication/cross-region-replicas) and promote them on regional failure.
    * **Encryption:** Use [Cloud KMS customer-managed encryption keys](https://docs.cloud.google.com/sql/docs/postgres/cmek).
  </Tab>

  <Tab title="Azure">
    Run [Azure Database for PostgreSQL Flexible Server](https://learn.microsoft.com/en-us/azure/postgresql/flexible-server/overview) with zone-redundant HA.

    * **Backups:** Enable [automatic backups](https://learn.microsoft.com/en-us/azure/postgresql/flexible-server/concepts-backup-restore) with geo-redundant backup storage.
    * **HA:** Zone-redundant HA maintains a synchronous standby in a different availability zone.
    * **Cross-region DR:** Use [read replicas](https://learn.microsoft.com/en-us/azure/postgresql/flexible-server/concepts-read-replicas) in a secondary region for promotion on regional failure.
  </Tab>
</Tabs>

### In-cluster Postgres

If you must run Postgres in-cluster from the bundled chart, you are responsible for backing up the underlying PersistentVolume. Snapshot the PVC on a regular cadence using your CSI driver's snapshot class, and copy snapshots to object storage or a different region. **This path is not recommended for production.**

## ClickHouse

ClickHouse holds the high-volume trace and feedback data and is typically the largest data store in a LangSmith deployment. Backups and replication need to be planned for cost and restore-time impact.

### Managed ClickHouse

The fastest path to a resilient ClickHouse is a managed option. See [Connect external ClickHouse](/langsmith/self-host-external-clickhouse).

* **[LangSmith Managed ClickHouse](/langsmith/langsmith-managed-clickhouse):** LangChain operates the ClickHouse cluster, including backups and replication. VPC peering connects it to your LangSmith installation.
* **[ClickHouse Cloud](https://clickhouse.cloud/):** Provides built-in backups, replication, and HA. Available on AWS, GCP, and Azure marketplaces.

### Self-managed replicated cluster

If you self-manage ClickHouse for compliance or air-gap reasons, use a replicated cluster. A single-node ClickHouse instance cannot meet a meaningful RPO.

* Configure a multi-node ClickHouse cluster with replication via [Keeper or ZooKeeper](https://clickhouse.com/docs/architecture/replication).
* Set the `cluster` value in the LangSmith chart so migrations create `Replicated` table engines from the start. **Clustered setups must be configured against a fresh schema**, you cannot convert a standalone instance to clustered later.
* Spread replicas across availability zones.
* Schedule [`BACKUP TABLE` or `BACKUP DATABASE`](https://clickhouse.com/docs/operations/backup) to object storage on a frequency matching your RPO. The community [`clickhouse-backup`](https://github.com/Altinity/clickhouse-backup) tool is also a popular option for scheduled, incremental backups with built-in S3, GCS, and Azure Blob support.
* For cross-region DR, copy the backup bucket to a secondary region. Cross-region ClickHouse replication is not generally supported in self-managed deployments and is not offered by ClickHouse Cloud either, so plan for a backup/restore failover model rather than a hot replica.

For an example replicated configuration, see the [replicated ClickHouse example](https://github.com/langchain-ai/helm/blob/main/charts/langsmith/examples/replicated-clickhouse/README.md) in the Helm repo.

<Warning>
  Restoring ClickHouse can take significantly longer than restoring Postgres at the same data volume because trace tables are large. Account for this when setting your RTO. Validate restore time on a representative dataset during DR drills.
</Warning>

## Blob storage

If you have enabled [blob storage](/langsmith/self-host-blob-storage) (recommended for production), your run inputs, outputs, errors, manifests, extras, events, and attachments live in S3, GCS, or Azure Blob Storage. Cloud blob services are durable by design, but you should still configure protection against accidental deletion and regional outages.

<Tabs>
  <Tab title="AWS">
    * Enable [S3 Versioning](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html) to protect against accidental deletes and overwrites.
    * Enable [MFA Delete](https://docs.aws.amazon.com/AmazonS3/latest/userguide/MultiFactorAuthenticationDelete.html) for high-security buckets.
    * For cross-region DR, configure [Cross-Region Replication (CRR)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html) to a bucket in your DR region.
    * Use [S3 Object Lock](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html) for write-once-read-many (WORM) retention.
    * Encrypt with [SSE-KMS](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingKMSEncryption.html). LangSmith supports passing a specific KMS key ARN, see [KMS encryption header support](/langsmith/self-host-blob-storage#kms-encryption-header-support).
  </Tab>

  <Tab title="GCP">
    * Enable [Object Versioning](https://cloud.google.com/storage/docs/object-versioning) on the bucket.
    * Use [dual-region or multi-region buckets](https://cloud.google.com/storage/docs/locations) for geo-redundancy.
    * For cross-region DR, use [Storage Transfer Service](https://cloud.google.com/storage-transfer-service) or [Object Lifecycle Management](https://cloud.google.com/storage/docs/lifecycle) with replication policies.
    * Encrypt with [Customer-Managed Encryption Keys (CMEK)](https://cloud.google.com/storage/docs/encryption/customer-managed-keys).
  </Tab>

  <Tab title="Azure">
    * Choose a [redundancy tier](https://learn.microsoft.com/en-us/azure/storage/common/storage-redundancy) that matches your DR objectives. Use **RA-GRS** or **RA-GZRS** for cross-region read access during a primary region outage.
    * Enable [soft delete and blob versioning](https://learn.microsoft.com/en-us/azure/storage/blobs/soft-delete-blob-overview).
    * Encrypt with a [customer-managed key in Key Vault](https://learn.microsoft.com/en-us/azure/storage/common/customer-managed-keys-overview).
  </Tab>
</Tabs>

<Warning>
  **Keep TTL lifecycle rules in your DR bucket.** If you copy data to a DR bucket, replicate the lifecycle rules for `ttl_s/`, `ttl_l/`, and any custom `ttl_XXd/` prefixes too. Missing rules in the DR bucket will cause data to be retained indefinitely after failover. See [TTL configuration](/langsmith/self-host-blob-storage#ttl-configuration).
</Warning>

## Redis

Redis stores ephemeral metadata, queue state, and cross-instance pub/sub. **No durable data is stored in Redis, so you do not need to back it up.** Communication with Redis is retried for retry-able errors. The recovery design is to make Redis highly available within the active region and to reprovision it from scratch in the DR region.

* Use the managed service for your cloud: [Amazon ElastiCache](https://aws.amazon.com/elasticache/redis/), [Google Cloud Memorystore](https://cloud.google.com/memorystore), or [Azure Cache for Redis](https://azure.microsoft.com/en-us/products/cache).
* Enable Multi-AZ failover.
* For cross-region DR, provision a fresh Redis instance in the DR region during failover; do **not** reuse an active region's Redis URI in the new cluster.

<Warning>
  Each LangSmith installation must use its own dedicated Redis instance. **Do not share a Redis instance across two installations**, including a primary and a DR replica that may both be active at any point. Sharing Redis causes deployment tasks to be routed to the wrong cluster. See [Connect external Redis](/langsmith/self-host-external-redis).
</Warning>

## Kubernetes configuration and secrets

The Helm chart values, Kubernetes `Secret`s, and identity bindings are as important as your data backups. A complete restore requires both.

* **Helm values:** Store `values.yaml` in source control. Track per-environment overrides separately.
* **Image versions:** Pin the LangSmith chart version and image tags so a recovery installs the same software version. See [Self-host upgrades](/langsmith/self-host-upgrades) and [Dependency versions](/langsmith/self-host-dependency-versions).
* **Secrets:** LangSmith reads database, blob, and licensing credentials from Kubernetes `Secret`s. Mirror these to your DR cluster's secret manager ([AWS Secrets Manager](https://aws.amazon.com/secrets-manager/), [GCP Secret Manager](https://cloud.google.com/secret-manager), or [Azure Key Vault](https://azure.microsoft.com/en-us/products/key-vault/)). See [Use an existing secret](/langsmith/self-host-using-an-existing-secret).
* **TLS material:** If you terminate TLS at the LangSmith ingress, back up the certificate and key, or reissue from your private CA in the DR region. See [Custom TLS certificates](/langsmith/self-host-custom-tls-certificates).
* **IRSA / Workload Identity bindings:** Recreate IAM roles and service-account bindings in the DR region; service account ARNs and annotations are region-scoped.
* **License key:** Keep the LangSmith license key alongside other recovery secrets.

## Reference deployment patterns

### Single region with Multi-AZ HA (recommended baseline)

This is the minimum production posture and protects against zonal failures. It does not protect against a regional outage.

* Kubernetes node pools across at least two availability zones.
* Postgres in Multi-AZ HA mode (RDS Multi-AZ, Cloud SQL HA, or Flexible Server zone-redundant).
* ClickHouse as a managed service, or a 3-node replicated cluster spread across AZs.
* Redis with Multi-AZ failover enabled.
* Blob storage with versioning enabled and a redundancy tier of at least zone-redundant.
* Daily snapshots of every data store retained for at least 7 days.

### Cross-region active/passive DR

This protects against a regional outage. It is significantly more expensive but is the right pattern for tier-1 deployments.

* A second Kubernetes cluster in the DR region with the LangSmith Helm chart installed but scaled to a low replica count (warm) or zero (cold).
* Postgres cross-region replica (RDS or Aurora cross-region replica, Cloud SQL cross-region replica, Azure Flexible Server cross-region replica). Promote on failover.
* ClickHouse Cloud or LangSmith Managed ClickHouse with a region failover plan, **or** ClickHouse backups copied to the DR region and restored into a fresh self-managed cluster on failover. Cross-region ClickHouse replication is not generally supported (ClickHouse Cloud does not offer it either), so plan for backup/restore rather than a hot DR replica.
* Blob storage replicated to a DR bucket with versioning and matching lifecycle rules.
* Redis provisioned fresh in the DR region during failover.
* DNS managed by [Route 53](https://aws.amazon.com/route53/), [Cloud DNS](https://cloud.google.com/dns), or [Azure DNS](https://azure.microsoft.com/en-us/products/dns/) with health checks and failover policies pointing at the LangSmith frontend ingress in each region.

<Note>
  LangSmith is a single-write platform. A cross-region deployment should be **active/passive**, not active/active. Writing to both regions concurrently against the same logical installation is not supported and will produce data inconsistency.
</Note>

## Recovery procedures

### Restore after a zonal failure

In a single-region Multi-AZ deployment, zonal failures are handled automatically by your cloud provider:

1. Managed Postgres fails over to its standby in another AZ. LangSmith pods reconnect via the cluster endpoint after retry.
2. Managed Redis fails over similarly. LangSmith retries reconnect automatically.
3. Kubernetes reschedules LangSmith pods on healthy nodes in remaining AZs. Verify that node pools and Horizontal Pod Autoscaler limits allow this headroom.
4. Verify ingest by submitting a test trace from the SDK and confirming it appears in the UI.

### Restore after a regional failure

This is the cross-region failover runbook. Adapt to your specific infrastructure.

<Steps>
  <Step title="Declare failover">
    Confirm the primary region is unavailable. Communicate to stakeholders that you are failing over and what the expected RTO is.
  </Step>

  <Step title="Promote data stores">
    Promote the Postgres cross-region replica to primary in the DR region. For ClickHouse Cloud or LangSmith Managed ClickHouse, initiate the documented region failover. For self-managed ClickHouse, restore the latest backup into the DR cluster (this is typically the longest step).
  </Step>

  <Step title="Repoint blob storage">
    Update the LangSmith Helm `config.blobStorage.bucketName` and `apiURL` to point at the DR bucket. Confirm the bucket has the same TTL lifecycle rules. See [Blob storage configuration](/langsmith/self-host-blob-storage#configuration).
  </Step>

  <Step title="Provision Redis">
    Create a fresh managed Redis instance in the DR region. Update the LangSmith Helm `redis.external` values to point at it. **Do not import dumps from the primary Redis**; provision empty.
  </Step>

  <Step title="Scale the DR cluster">
    If running warm/cold, scale the LangSmith deployments to their production replica counts. Apply any pending Helm value updates from source control.
  </Step>

  <Step title="Run smoke tests">
    Submit a test trace, verify it lands in ClickHouse and (if blob storage is enabled) in the DR bucket. Open the UI and confirm traces, datasets, and projects load. Validate authentication. See [Diagnostics](/langsmith/diagnostics-self-hosted).
  </Step>

  <Step title="Cut DNS over">
    Update DNS to route traffic to the DR ingress. Communicate the cutover to stakeholders.
  </Step>

  <Step title="Plan failback">
    Once the primary region is healthy, plan a controlled failback. This is typically scheduled into a maintenance window and involves rebuilding the primary as the new DR replica before swapping again.
  </Step>
</Steps>

### Restore from snapshot

If you have lost the primary data store entirely and need to restore from snapshot:

<Steps>
  <Step title="Stop ingestion">
    Scale `langsmith-queue` and `langsmith-ingest-queue` to zero so no new traces are written while you restore.
  </Step>

  <Step title="Restore Postgres">
    Restore the Postgres backup to a new instance or perform PITR to the latest pre-incident timestamp. Update the LangSmith Helm `postgres.external` connection details to point to the restored instance.
  </Step>

  <Step title="Restore ClickHouse">
    Restore the most recent ClickHouse backup that aligns in time with the Postgres restore point. Restore time scales with data size.
  </Step>

  <Step title="Restore blob storage">
    If you lost blob data (rare), restore versioned objects from S3/GCS/Azure or copy from a replicated DR bucket.
  </Step>

  <Step title="Resume ingestion">
    Scale `langsmith-queue` and `langsmith-ingest-queue` back to production replica counts. Submit a smoke-test trace and verify it lands.
  </Step>
</Steps>

<Warning>
  Always restore Postgres, ClickHouse, and blob storage to the closest possible coordinated point in time. Restoring Postgres to a more recent point than ClickHouse can produce dangling project references and missing traces in the UI.
</Warning>

## Testing your DR plan

A backup is only as good as the last successful restore. Schedule the following exercises:

* **Quarterly:** Restore Postgres and ClickHouse snapshots into a non-production environment and run the [diagnostics tooling](/langsmith/diagnostics-self-hosted) and a smoke trace test. Measure actual restore time and confirm it is within RTO.
* **Twice yearly:** Perform a full cross-region failover drill against a staging installation. Promote the replica, repoint blob storage, scale the DR cluster, run smoke tests, and roll back.
* **On every chart upgrade:** Verify that the upgrade path does not invalidate your DR plan (for example, schema migrations applied only to the primary will need to replicate to the DR replica). See [Self-host upgrades](/langsmith/self-host-upgrades).

## Related pages

* [Scalability and resilience](/langsmith/scalability-and-resilience)
* [Shared responsibility model](/langsmith/shared-responsibility-model)
* [Connect external Postgres](/langsmith/self-host-external-postgres)
* [Connect external ClickHouse](/langsmith/self-host-external-clickhouse)
* [Connect external Redis](/langsmith/self-host-external-redis)
* [Enable blob storage](/langsmith/self-host-blob-storage)
* [Self-host upgrades](/langsmith/self-host-upgrades)
* [Use an existing secret](/langsmith/self-host-using-an-existing-secret)
* [Diagnostics for self-hosted](/langsmith/diagnostics-self-hosted)
* [AWS self-hosted reference architecture](/langsmith/aws-self-hosted)
* [GCP self-hosted reference architecture](/langsmith/gcp-self-hosted)
* [Azure self-hosted reference architecture](/langsmith/azure-self-hosted)

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/self-host-disaster-recovery.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Egress for billing and operational telemetry
Source: https://docs.langchain.com/langsmith/self-host-egress

<Info>
  This page only applies to customers who are not running in offline (air-gapped) mode and assumes you are using a self-hosted LangSmith instance serving version 0.9.0 or later.
</Info>

Self-hosted LangSmith instances store all information locally and never send sensitive information outside of your network. However, unless you are running in offline mode, LangSmith requires egress to `https://beacon.langchain.com` for the following:

* **Billing telemetry** — License verification and subscription/usage reporting (required)
* **Operational telemetry** — Logs, metrics, and traces for support diagnostics (optional, can be disabled)
* **Usage telemetry** — Anonymized usage snapshots for product insights (optional, can be disabled)

<Warning>
  **Egress to `https://beacon.langchain.com` is required.** Refer to the [allowlisting IP section](/langsmith/cloud#allowlisting-ip-addresses) for static IP addresses, if needed.
</Warning>

## Billing telemetry

Billing telemetry is **required** for self-hosted LangSmith instances that are not running in offline mode. This includes license verification and subscription/usage reporting.

<Info>
  Billing telemetry **cannot be disabled**. If you need to run without any egress, contact your account team about an offline (air-gapped) license.
</Info>

### What it does

* **License verification**: Validates your LangSmith license key at startup and periodically thereafter.
* **Subscription/usage reporting**: Reports platform usage metrics for billing purposes according to the entitlements in your order.

### What we collect

* License key validation requests
* Aggregated usage counts (number of traces, seats allocated, seats in use)
* Organization and workspace identifiers

### Example payloads

#### License verification

**Endpoint:** `POST beacon.langchain.com/v1/beacon/verify`

**Request:**

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "license": "<YOUR_LICENSE_KEY>"
}
```

**Response:**

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "token": "Valid JWT" //Short-lived JWT token to avoid repeated license checks
}
```

#### Subscription/usage reporting

**Endpoint:** `POST beacon.langchain.com/v1/beacon/ingest-traces`

**Request:**

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "license": "<YOUR_LICENSE_KEY>",
  "trace_transactions": [
    {
      "id": "af28dfea-5358-463d-a2dc-37df1da72498",
      "tenant_id": "3a1c2b6f-4430-4b92-8a5b-79b8b567bbc1",
      "session_id": "b26ae531-cdb3-42a5-8bcf-05355199fe27",
      "trace_count": 5,
      "start_insertion_time": "2025-01-06T10:00:00Z",
      "end_insertion_time": "2025-01-06T11:00:00Z",
      "start_interval_time": "2025-01-06T09:00:00Z",
      "end_interval_time": "2025-01-06T10:00:00Z",
      "status": "completed",
      "num_failed_send_attempts": 0,
      "transaction_type": "type1",
      "organization_id": "c5b5f53a-4716-4326-8967-d4f7f7799735"
    }
  ]
}
```

**Response:**

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "inserted_count": 1 //Number of transactions successfully ingested
}
```

## Operational telemetry

As of version **0.11**, LangSmith deployments send operational telemetry by default. This telemetry helps the LangChain team provide proactive support and faster troubleshooting for self-hosted instances.

<Info>
  Operational telemetry is **separate from** billing telemetry. You can disable operational telemetry while billing telemetry remains active.
</Info>

### What it does

* Enables proactive support and faster troubleshooting of self-hosted instances
* Assists with performance tuning
* Helps prioritize improvements based on real-world usage patterns

### What we collect

* **Request metadata**: Anonymized request counts, sizes, and durations
* **Database metrics**: Query durations, error rates, and performance counters
* **Operational traces**: Timing and error information for high-latency or failed requests (these are **not** customer traces — they are traces about the functioning of the LangSmith instance itself)
* **Log messages**: Warning and error log messages only

<Info>
  We do not collect actual payload contents, database records, or any data that can identify your end users or customers. All telemetry data is associated with an organization and deployment, but never identified with individual users. We **do not collect PII** (personally identifiable information) in any form.
</Info>

### How to disable

You can disable operational telemetry by setting the following values in your `langsmith_config.yaml` file:

```yaml theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
config:
  telemetry:
    logs: false
    metrics: false
    traces: false
```

You can also disable individual telemetry types by setting only specific values to `false`.

<Warning>
  Disabling operational telemetry stops exporting the logs, metrics, and traces described in this section. It does **not** disable billing telemetry (license verification and subscription/usage reporting).
</Warning>

### Example payloads

#### Operational metrics

**Endpoint:** `POST beacon.langchain.com/v1/beacon/v1/metrics`

**Request:**

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "resourceMetrics": [
    {
      "resource": {
        "attributes": [
          {
            "key": "resource.name",
            "value": { "stringValue": "langsmith-metrics" }
          },
          {
            "key": "env",
            "value": { "stringValue": "ls_self_hosted" }
          }
        ]
      },
      "scopeMetrics": [
        {
          "scope": {
            "name": "langsmith.metrics",
            "version": "0.1.0"
          },
          "metrics": [
            {
              "name": "langsmith_http_requests_latency",
              "unit": "seconds",
              "description": "Request latency of LangSmith services",
              "gauge": {
                "dataPoints": [
                  {
                    "asDouble": 12.34,
                    "startTimeUnixNano": 1678886400000000000,
                    "timeUnixNano": 1678886400000000000,
                    "attributes": [
                      {
                        "key": "endpoint",
                        "value": { "stringValue": "/sessions" }
                      },
                      { "key": "method", "value": { "stringValue": "GET" } },
                      {
                        "key": "service_name",
                        "value": { "stringValue": "langsmith_backend" }
                      }
                    ]
                  }
                ]
              }
            },
            {
              "name": "langsmith_http_requests_failed",
              "unit": "1",
              "description": "Counter of failed requests for LangSmith services",
              "sum": {
                "dataPoints": [
                  {
                    "asInt": 456,
                    "startTimeUnixNano": 1678886400000000000,
                    "timeUnixNano": 1678886400000000000,
                    "attributes": [
                      {
                        "key": "endpoint",
                        "value": { "stringValue": "/info" }
                      },
                      { "key": "method", "value": { "stringValue": "POST" } },
                      {
                        "key": "service_name",
                        "value": { "stringValue": "langsmith_platform_backend" }
                      }
                    ],
                    "aggregationTemporality": 2,
                    "isMonotonic": true
                  }
                ]
              }
            }
          ]
        }
      ]
    }
  ]
}
```

#### Operational traces

**Endpoint:** `POST beacon.langchain.com/v1/beacon/v1/traces`

**Request:**

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "resourceSpans": [
    {
      "resource": {
        "attributes": [
          {
            "key": "env",
            "value": {
              "stringValue": "ls_self_hosted"
            }
          },
          {
            "key": "service.name",
            "value": {
              "stringValue": "langsmith_backend"
            }
          }
        ]
      },
      "scopeSpans": [
        {
          "scope": {},
          "spans": [
            {
              "traceId": "71699b6fe85982c7c8995ea3d9c95df2",
              "spanId": "3c191d03fa8be0",
              "parentSpanId": "",
              "name": "receive_request",
              "startTimeUnixNano": "1581452772000000321",
              "endTimeUnixNano": "1581452773000000789",
              "droppedAttributesCount": 1,
              "events": [
                {
                  "timeUnixNano": "1581452773000000123",
                  "name": "parse_request",
                  "attributes": [
                    {
                      "key": "request_size",
                      "value": {
                        "stringValue": "100"
                      }
                    }
                  ],
                  "droppedAttributesCount": 2
                },
                {
                  "timeUnixNano": "1581452773000000123",
                  "name": "event",
                  "droppedAttributesCount": 2
                }
              ],
              "droppedEventsCount": 1,
              "status": {
                "message": "status-cancelled",
                "code": 2
              }
            },
            {
              "traceId": "71699b6fe85982c7c8995ea3d9c95df2",
              "spanId": "0932ksdka12345",
              "parentSpanId": "3c191d03fa8be0",
              "name": "process_request",
              "startTimeUnixNano": "1581452772000000321",
              "endTimeUnixNano": "1581452773000000789",
              "links": [],
              "droppedLinksCount": 3,
              "status": {}
            }
          ]
        }
      ]
    }
  ]
}
```

#### Operational log messages

We only export error log messages from self-hosted LangSmith instances. This allows the LangChain team to troubleshoot application errors without requiring back-and-forth communication with your team.

**Endpoint:** `POST beacon.langchain.com/v1/beacon/v1/logs`

**Request:**

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "resourceLogs": [
    {
      "resource": {
        "attributes": [
          {
            "key": "service.name",
            "value": {
              "stringValue": "langsmith_backend"
            }
          }
        ]
      },
      "scopeLogs": [
        {
          "scope": {},
          "logRecords": [
            {
              "timeUnixNano": "1581452773000009875",
              "severityNumber": 13,
              "severityText": "Warning",
              "body": {
                "stringValue": "Database connection pool approaching capacity"
              },
              "attributes": [
                {
                  "key": "component",
                  "value": {
                    "stringValue": "langsmith_backend"
                  }
                },
                {
                  "key": "pool_size",
                  "value": {
                    "intValue": "95"
                  }
                }
              ],
              "droppedAttributesCount": 0,
              "traceId": "08040201000000000000000000000000",
              "spanId": "0102040800000000"
            },
            {
              "timeUnixNano": "1581452773000000789",
              "severityNumber": 17,
              "severityText": "Error",
              "body": {
                "stringValue": "Failed to process trace batch"
              },
              "attributes": [
                {
                  "key": "component",
                  "value": {
                    "stringValue": "langsmith_queue_worker"
                  }
                },
                {
                  "key": "error_type",
                  "value": {
                    "stringValue": "timeout"
                  }
                }
              ],
              "droppedAttributesCount": 0,
              "traceId": "",
              "spanId": ""
            }
          ]
        }
      ]
    }
  ]
}
```

## Usage telemetry

Usage telemetry collects anonymized snapshots of your LangSmith instance's usage metrics. This data helps LangChain understand platform adoption patterns and inform product development decisions.

<Info>
  Usage telemetry is **enabled by default** and can be disabled. Unlike billing telemetry, you have full control over whether these snapshots are sent to LangChain.
</Info>

### What it does

* Captures aggregated usage metrics at regular intervals
* Provides insight into feature adoption and platform growth
* Helps LangChain prioritize improvements and new features based on real-world usage

### What we collect

* **Platform metrics**: Counts of workspaces, projects, experiments, datasets, evaluators, and other platform resources
* **Feature usage**: Counts of run rules, annotation queues, prompts, and prompt-related activity
* **Users**: Total number of registered users and count of active PATs (Personal Access Tokens) in the last 30 days
* **Timestamps**: Time range for the snapshot (from/to timestamps in UTC)

<Info>
  All metrics are **aggregated counts only**. No individual resource data, identifiers, or usage patterns are collected. We do not collect any information that could identify your end users or customers.
</Info>

### Example payloads

**Endpoint:** `POST /v1/beacon/usage-snapshot`

**Request:**

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "license_key": "<YOUR_LICENSE_KEY>",
  "from_timestamp": "2026-03-25T02:00:00+00:00",
  "to_timestamp": "2026-03-26T02:00:00+00:00",
  "measures": {
    "workspaces": 12,
    "users": 63,
    "projects": 87,
    "experiments": 34,
    "datasets": 15,
    "evaluators": 8,
    "run_rules": 5,
    "annotation_queues": 3,
    "prompts": 22,
    "prompt_commits": 156,
    "prompt_pulls": 1043,
    "active_pats_30d": 47
  }
}
```

### How to disable

You can disable usage telemetry by setting the following environment variable in your deployment configuration:

```yaml theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
PHONE_HOME_USAGE_REPORTING_ENABLED: false
```

Add this to the `commonEnv` section of your Helm configuration to permanently disable usage telemetry reporting.

<Warning>
  Disabling usage telemetry does **not** affect billing or operational telemetry. License verification and subscription/usage reporting will continue to function normally.
</Warning>

## Our commitment

LangChain will not store any sensitive information in billing or operational telemetry. Any data collected will not be shared with a third party. Log messages are filtered to only include error severity levels, and we do not capture log messages that could contain sensitive application data. If you have any concerns about the data being sent, disable telemetry and/or reach out to your account team.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/self-host-egress.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Configure environment variables in the Helm chart
Source: https://docs.langchain.com/langsmith/self-host-environment-variables

How to use commonEnv and extraEnv to configure environment variables across LangSmith services in the Helm chart.

The LangSmith Helm chart provides two ways to inject environment variables into services: `commonEnv` and `extraEnv`. Understanding the difference between them helps you configure your deployment correctly and avoid runtime errors.

## commonEnv

`commonEnv` is a top-level field in `values.yaml` that applies to **all deployments and statefulsets except the `playground` and `aceBackend` services**, which are sandboxed and do not receive `commonEnv` values.

Use `commonEnv` when a variable must be available to most services simultaneously, such as custom CA certificate paths, proxy settings, or feature flags that affect the entire platform.

```yaml theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
commonEnv:
  - name: MY_ENV_VAR
    value: "my-value"
```

### Services that receive commonEnv

The following services receive `commonEnv`:

* `backend`
* `platformBackend`
* `queue`
* `ingestQueue`
* `frontend`
* `hostBackend`

### Services that do not receive commonEnv

The following services are sandboxed and do **not** receive `commonEnv`:

* `playground`
* `aceBackend`

To set environment variables on these services, use their `extraEnv` directly:

```yaml theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
playground:
  deployment:
    extraEnv:
      - name: MY_ENV_VAR
        value: "my-value"

aceBackend:
  deployment:
    extraEnv:
      - name: MY_ENV_VAR
        value: "my-value"
```

## extraEnv

`extraEnv` is a per-service field that adds environment variables to a specific service only. Each service that supports `extraEnv` exposes it under `<service>.deployment.extraEnv`.

Use `extraEnv` when a variable applies to one service only, or when you need to set a variable on `playground` or `aceBackend` that `commonEnv` does not reach.

```yaml theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
backend:
  deployment:
    extraEnv:
      - name: MY_BACKEND_VAR
        value: "backend-value"
```

## No duplicate variable names

The chart uses a `detectDuplicates` helper to validate environment variable names for each service. If the same variable name appears more than once in the combined list of variables for a service (including those added from `commonEnv`, `extraEnv`, and chart-managed variables), Helm fails during template rendering with an error like:

```
Duplicate keys detected: [MY_ENV_VAR]
```

To resolve this, remove the duplicate from either `commonEnv` or the service's `extraEnv` so each variable name appears exactly once per service.

<Warning>
  Chart-managed variables (set internally by the Helm chart) count toward duplicate detection. Do not add a variable name to `commonEnv` or `extraEnv` if the chart already manages that variable. Review the [chart values file](https://github.com/langchain-ai/helm/blob/main/charts/langsmith/values.yaml) to see which variables the chart sets by default.
</Warning>

## Example: set a variable on most services but override it on one

To use a common value for most services while overriding it for a specific service, set it in `commonEnv` and add the override to that service's `extraEnv`. Because `playground` and `aceBackend` do not receive `commonEnv`, you must always set variables for those services through their own `extraEnv`.

```yaml theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}

# Apply to all services that receive commonEnv
commonEnv:
  - name: SSRF_ALLOW_K8S_INTERNAL
    value: "true"

# playground does not receive commonEnv — set it directly
playground:
  deployment:
    extraEnv:
      - name: SSRF_ALLOW_K8S_INTERNAL
        value: "true"
      - name: SSRF_ALLOW_PRIVATE_IPS_PLAYGROUND
        value: "true"
```

## Common feature flags

### Reduce batched-run persistence logging

By default, LangSmith logs a success message for every batch of runs it persists via the Go-based ingest queue. On deployments that process a high volume of traces, this can produce excessive log noise.

`FF_PERSIST_BATCHED_RUNS_SUCCESS_LOGGING` defaults to `true` and is injected into all services via `commonEnv` when `ingestQueue.enabled` is `true` (the default). To disable these success log messages, override it in `commonEnv`:

```yaml theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
commonEnv:
  - name: FF_PERSIST_BATCHED_RUNS_SUCCESS_LOGGING
    value: "false"
```

<Note>
  Setting this flag to `false` suppresses per-batch success messages only. Errors are still logged.
</Note>

## Related pages

* [Configure LangSmith for scale](/langsmith/self-host-scale)
* [Playground environment settings](/langsmith/self-host-playground-environment-settings)
* [LangSmith Helm chart values.yaml](https://github.com/langchain-ai/helm/blob/main/charts/langsmith/values.yaml)

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/self-host-environment-variables.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
