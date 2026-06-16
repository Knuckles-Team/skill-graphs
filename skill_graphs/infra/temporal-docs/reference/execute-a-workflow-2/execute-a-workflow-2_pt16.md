  <RelatedReadItem path="/cloud/limits" text="Temporal Cloud Limits" archetype="cloud-guide" />
  <RelatedReadItem path="/visibility" text="Visibility and Search Attributes" archetype="feature-guide" />
</RelatedReadContainer>

---

## Self-hosted Archival setup

Use Archival to back up closed Workflow Execution [Event Histories](/workflow-execution/event#event-history) and
Visibility records from Temporal Service persistence to blob storage.

- [How to create a custom Archiver](#custom-archiver)
- [How to set up Archival](#set-up-archival)

When a Workflow Execution closes, Temporal schedules close-processing tasks for both Visibility records and Event
History Archival. Archival then runs asynchronously after a randomized delay. By default, that delay is up to 5 minutes
set by `history.archivalProcessorArchiveDelay`, and is capped by the Namespace
[Retention Period](/temporal-service/temporal-server#retention-period).

The closed execution still stays in Temporal persistence until retention cleanup runs. For some time, the same closed
execution can exist in both persistence and archival storage. Archival enables Workflow Execution data to persist beyond
retention without overwhelming the Temporal Service persistence store.

Use this to keep closed Workflow data available for compliance, audits, and debugging without keeping all closed data in
your primary persistence store.

:::info Experimental feature

Archival is an **experimental** feature and not subject to normal
[versioning and support policy](/temporal-service/temporal-server#versions-and-support).

:::

Archival is not supported when running Temporal through Docker. It's disabled by default when installing the system
manually and when deploying through
[helm charts](https://github.com/temporalio/helm-charts/blob/main/charts/temporal/templates/server-configmap.yaml). It
can be enabled in the server [configuration](https://github.com/temporalio/temporal/blob/main/config/development.yaml).

### Set up Archival {/* #set-up-archival */}

To set up [Archival](/temporal-service/archival), decide the following:

- **Which provider to use:** S3, Google Cloud, local file system, or custom.
- **Which URI to use:** URI scheme and path identify the provider and destination.
- **Which Namespace should use Archival:** Archival must be enabled at both the Temporal Service level and the Namespace
  level.

Take the following steps to set up Archival:

1. [Choose an Archival provider](#choose-an-archival-provider).
2. [Configure Archival options](#configure-archival-options).
3. [Create an Archiving Namespace](#create-an-archiving-namespace).

#### Choose an Archival provider {/* #choose-an-archival-provider */}

Temporal directly supports several providers:

- **Local file system**: The
  [filestore archiver](https://github.com/temporalio/temporal/tree/main/common/archiver/filestore) is used to archive
  data in the file system of whatever host the Temporal server is running on. In the case of
  [temporal helm-charts](https://github.com/temporalio/helm-charts), the archive data is stored in the `history` pod.
  APIs do not function with the filestore archive. This provider is used mainly for local installations and testing and
  should not be relied on for production environments.
- **Google Cloud**: The [gcloud archiver](https://github.com/temporalio/temporal/tree/main/common/archiver/gcloud) is
  used to connect and archive data with [Google Cloud](https://cloud.google.com/storage).
- **S3**: The [s3store archiver](https://github.com/temporalio/temporal/tree/main/common/archiver/s3store) is used to
  connect and archive data with [S3](https://aws.amazon.com/s3).
- **Custom**: If you want to use a provider that is not currently supported, you can
  [create your own archiver](#custom-archiver) to support it.

Save the provider URI so you can pass it when you create a Namespace with Archival enabled.

#### Configure Archival options {/* #configure-archival-options */}

Configure Archival in
[`config/development.yaml`](https://github.com/temporalio/temporal/blob/main/config/development.yaml#L93):

```yaml
