              "result": { "payloads": ["...serialized result..."] }
            }
          }
        ]
      }
    }
  ]
}
```

The outer `items` array can contain multiple Workflow Executions per file.
Only the key fields are shown above. Actual events include additional fields like `version`, `taskId`, and `workerVersion`.

## Prerequisites {/* #prerequisites */}

To use Workflow History Export, you must have:

1. A cloud account in the cloud provider where your Namespace is hosted.
2. An object storage bucket available to receive the exported History.

## Configure Workflow History Export {/* #configure */}

### AWS

[AWS S3 Export Configuration](/cloud/export/aws-export-s3)

### GCP

[GCP GCS Export Configuration](/cloud/export/gcp-export-gcs)

## Verify export setup {/* #verify */}

From the Export configuration page, select **Verify**.
This validates that Temporal can successfully write a test file to your object storage.

If everything is configured correctly, you will see a `Success` status indicating Temporal has written to the object store.

## Monitor export progress {/* #monitor */}

After Export has been configured, you can check that it's still working in several ways:

1. **Object Storage**:

   - File Delivery: After the initial hour of setting up, inspect your object storage.
     You should see the exported Event History files.
   - Directory Structure: Your exported files will adhere to the following naming convention and path:

   ```bash
   //[bucket-name]/temporal-workflow-history/export/[Namespace]/[Year]/[Month]/[Day]/[Hour]/[Minute]/
   ```
The exported file name will include a randomly generated ID. The time recorded in the directory structure
is the time the export uploads to object storage, not the Workflow completion time.

2. **Temporal Cloud Web UI**:

   - Export UI:

      - Last Successful Export: This displays the timestamp of the most recent successful export.
      - Last Status Check: This reflects the timestamp of the latest internal Workflow healthcheck.

   - Usage Dashboard:
      - Actions from the Export Job are included in the [Usage Dashboard](/cloud/actions-usage).

3. **Email**:
   - Emails are sent to `Namespace Administrator`, `Account Owner`, and `Global Administrator` roles when a Workflow History Export job fails due to a user related error (such as Object Store permissions issue).

:::note

An export configuration that fails for 7 consecutive days is automatically disabled.

:::

## Working with exported files

Use the proto schema defined [here](https://github.com/temporalio/api/blob/main/temporal/api/export/v1/message.proto) to deserialize exported files.

### Using exported files in analytics

It can be useful to convert protos to another format to perform analytics on the data. To convert protos to parquet, follow
[the example Python Workflow](https://github.com/temporalio/samples-python/tree/main/cloud_export_to_parquet). Note that this example Workflow:
* Transforms the nested proto structure into a flat, tabular format.
* Each row in the table represents a single history event from a Workflow. To preserve their relationship post-conversion, the `workflowID` and `runID` is included in every row.
* If you have enabled the codec server, the payload field is encrypted. This field may contain characters that are not recognized when loaded into a database so the payload field is excluded in this example.

## Export and High Availability Namespaces {/* #export-ha */}

### Export Region Persistence

When Export is configured for a [High Availability](/cloud/high-availability) Namespace, the export is tied to the specific region where it was initially set up. The export configuration does not automatically failover with the Namespace.

- If Export is configured in Region A, it will continue to export from Region A's storage even after a Namespace failover to Region B
- Exports always read from and write to the same region where they were originally configured
- The export process is independent of Namespace failover events
- Export does not fail over automatically because we prioritize data completeness and consistency over real-time availability for exports. HA data replication has inherent latency, which could result in incomplete or inconsistent exports during a failover.

### Failover Scenarios

**Namespace Failover with Healthy Primary Region**: When a Namespace fails over to a secondary region but the primary region remains healthy (including its blob storage), the export job continues to operate from the primary region. It does not automatically switch to export data from the secondary region.

**Primary Region Outage**: If the primary region (where Export was configured) experiences a complete outage including S3/GCS storage: Exports will be unavailable until the primary region recovers. Once the primary region recovers, export will resume and include any Workflow histories that occurred during the outage. There may be delays in export processing, but the complete dataset will eventually be available. It does not automatically switch to export data from the secondary region.

---

## Exporting Workflow Event History to GCS

## Prerequisites {/* #prerequisites */}

Before configuring the Export sink, complete the following steps in Google Cloud.

1. Create a GCS bucket and take note of its bucket name, for example, "test-export"

- Enable customer-managed encryption keys (CMEK) if you need additional security for your GCS bucket.
- Currently, only single region buckets are supported (choose "Region" option when creating the bucket in GCS, not "Multi-region" or "Same-region")
- The region of the bucket must be the same as the region of your Temporal Cloud Namespace.

2. Record the GCP Project ID that owns the bucket.
3. Create a service account in the same project that grants Temporal permission to write to your GCS bucket.
4. Follow the instructions in the Temporal Cloud UI. There are two ways to set up this service account:
   - Manual Setup:
     - Input the service account ID, GCP project ID and GCS bucket name.
     - Follow the instructions, manually set up a new service account.
   - Automated Setup:
     - Use the [Terraform template](https://github.com/temporalio/terraform-modules/tree/main/modules/export-sa) to create the service account.

## Configure Workflow History Export

There are multiple ways to configure export: through the [Temporal Cloud UI](#using-temporal-cloud-ui), [`tcld`](#using-tcld), or [`terraform`](#using-terraform).

:::note Why does Temporal Cloud provision multiple service accounts for Export?

Temporal Cloud creates multiple intermediary service accounts for export operations primarily for security purposes. The system randomly selects from these accounts when writing to your storage sink, which provides several benefits:

- **Security isolation**: If one service account is compromised or needs to be decommissioned, other accounts remain available
- **Load distribution**: Prevents exclusively using a single account, reducing security risk
- **Warm standby**: Keeps multiple accounts active to avoid potential throttling when switching between accounts
- **Reliability**: Provides resilience against cloud provider account-level issues that could affect a single service account

This approach prioritizes security and availability, ensuring robust export operations even if individual service accounts encounter issues.
:::

### Using Temporal Cloud UI

The following steps guide you through setting up Workflow History Export using the Temporal Cloud UI.

![](/img/cloud/gcp/export-sink-ui-gcp.png)

1. In the Cloud UI, navigate to the Namespaces section. Confirm that the Export feature is visible and properly displayed.
2. Configure the Export sink for a Namespace:
   1. Choose GCS as the sink type.
   2. Provide the following information:
      1. Name
      2. Service account ID
      3. GCP Project ID
      4. GCS bucket name
3. After inputting the necessary values, click on **Verify**.
   You should be able to write to the sink successfully.
   If not, please fix any errors or reach out to support for help.
   - If you just created the GCS bucket and granted permission for your service account, it may take some time for the permission to propagate. You may need to wait up to 5 minutes before clicking the **Verify** button to verify the connection.
4. Clicking **Create** will complete the Export sink setup.
5. The page will auto-refresh and you should see the status “Enabled” on the Export screen.
   You are now ready to export Workflow histories.
6. You can toggle the enable button if you want to stop export and resume in the future.
   **Note**: when you re-enable the feature, it will start from the current point in time, and not from the time when you disabled export.
7. You can also delete export by clicking **Delete**.

:::tip

Don't forget to click Create at the end of your setup to confirm your export.

:::

### Using tcld

To access export-related commands in tcld, please follow these steps:

1. [Download the latest version of tcld](https://docs.temporal.io/cloud/tcld/#install-tcld).
2. Make sure your tcld version is v0.35.0 or above.
3. Run the command: `tcld n export gcs`:
   ```bash
   NAME:
      tcld namespace export gcs - Manage GCS export sink

   USAGE:
      tcld namespace export gcs command [command options] [arguments...]

   COMMANDS:
      create, c    Create export sink
      update, u    Update export sink
      validate, v  Validate export sink
      get, g       Get export sink
      delete, d    Delete export sink
      list, l      List export sinks
      help, h      Shows a list of commands or help for one command

   OPTIONS:
      --help, -h  show help
   ```

4. Run the `tcld n export gcs create` command and provide the following information:
   - `--namespace`: The Namespace to configure export for.
   - `--sink-name`: The name of the export sink.
   - `--service-account-email`: The service account that has access to the sink.
   - `--gcs-bucket`: The name of the GCP GCS bucket.

   For example:

   ```bash
   tcld n export gcs create -n test.ns --sink-name test-sink --service-account-email test-sink@test-export-sink.iam.gserviceaccount.com --gcs-bucket test-export-validation
   ```
5. Check the status of this command by either viewing the Namespace Export status in the Temporal Cloud UI or using the following command and looking for the state of "Active":

```bash
tcld n export gcs g -n test.ns --sink-name test-sink
{
	"name": "test.ns",
	"resourceVersion": "b954de0c-c6ae-4dcc-90bd-3918b52c3f28",
	"state": "Active",
	"spec": {
		"name": "test-sink",
		"enabled": true,
		"destinationType": "Gcs",
		"s3Sink": null,
		"gcsSink": {
			"saId": "test-sink",
			"bucketName": "test-export-validation",
			"gcpProjectId": "test-export-sink",
		}
	},
	"health": "Ok",
	"errorMessage": "",
	"latestDataExportTime": "0001-01-01T00:00:00Z",
	"lastHealthCheckTime": "2024-01-23T06:40:02Z"
}
```

### Using `terraform`

See the [Terraform export support](https://registry.terraform.io/providers/temporalio/temporalcloud/latest/docs/resources/namespace_export_sink) for setup instructions.

### Next Steps

- [Verify export setup](/cloud/export#verify)
- [Monitor export progress](/cloud/export#monitor)
- [Work with exported files](/cloud/export#working-with-exported-files)

---

## Manage API keys

Temporal Cloud API keys offer industry-standard identity-based authentication for Temporal users and
[Service Accounts](/cloud/service-accounts). This document introduces Temporal Cloud's API key features:

- [API key overview](#overview)
- [API key best practices](#best-practices)
- [Global Administrator and Account Owner API key management](#manage-api-keys)
- [User API key management](#user-api-keys)
- [Manage API keys for Service Accounts](#serviceaccount-api-keys)
- [API keys for Namespace authentication](#namespace-authentication)
- [Use API keys to authenticate](#using-apikeys)
- [Troubleshoot your API key use](#troubleshooting)
- [API keys: Frequently Asked Questions](#faqs)

## API key overview {/* #overview */}

Each Temporal Cloud API key is a unique identity linked to role-based access control (RBAC) settings to ensure secure
and appropriate access.

The authentication process follows this pathway:

<CaptionedImage
  src="/img/cloud/apikeys/apikeyrbac.png"
  title="API key (authentication) → Identity (user or Service Account) → RBAC (authorization)"
/>

## API key best practices {/* #best-practices */}

- **Keep it secret; keep it safe**: Treat your API key like a password. Do not expose it in client-side code, public
  repositories, or other easily accessible locations.
- **Rotate keys regularly**: Change your API keys periodically to reduce risks from potential leaks.
- **Design your code for key updates**: Use key management practices that retrieve your API keys without hard-coding
  them into your apps. This lets you restart your Workers to refresh your rotated keys without recompiling your code.
- **Monitor API key usage**: Check usage metrics and logs regularly. Revoke the key immediately if you detect any
  unexpected or unauthorized activity.
- **Use a Key Management System (KMS)**: Employ a Key Management System to minimize the risk of key leaks.

For guidance on which identities should own API keys, when to use Namespace-scoped Service Accounts, and how to align
API keys with your Namespace topology, see [Managing Temporal Cloud access control](/best-practices/cloud-access-control).

### API key use cases

API keys are used for the following scenarios:

- _**Cloud operations automation**_: API keys work with Temporal Cloud operational tools, including
  [`tcld`](/cloud/tcld), [Cloud Ops APIs](/ops), and
  [the Terraform provider](/cloud/terraform-provider). Use them to manage your Temporal Cloud
  account, Namespaces, certificates, and user identities.
- _**Namespace authentication**_: API keys serve as an authentication mechanism for executing and managing Workflows via
  the SDK and Temporal CLI, offering an alternative to mTLS-based authentication.

### API key supported tooling

Use API keys to authenticate with:

- [The Temporal CLI](/cli)
- [Temporal SDKs](/develop)
- [`tcld`](/cloud/tcld/index.mdx)
- [The Cloud Operations API](/cloud/operation-api.mdx)
- [Temporalʼs Terraform provider](/cloud/terraform-provider)

### API key permissions

API keys support both users and Service Accounts. Here are the differences in their permissions:

- Any user can create, delete, and update their _own_ API key using the Cloud UI or `tcld`.
- Only Global Administrators and Account Owners can create, delete, and update access to API keys for all types of
  Service Accounts.
- Namespace Admins can create, delete, and update access to API keys for the Namespace-scoped Service Accounts they
  administer.

### API key prerequisites

Check these setup details before using API keys:

- The Global Administrator or Account Owner may need to [enable API keys access](#manage-api-keys) for your Temporal
  Account.
- Have access to the [Temporal Cloud UI](https://cloud.temporal.io/) or Temporal Cloud CLI
  ([tcld](https://docs.temporal.io/cloud/tcld/)) to create an API key.

## Global Administrator and Account Owner API key management {/* #manage-api-keys */}

Global Administrators and Account Owners can monitor, manage, disable, and delete API keys for any user or Service
Account within their account. To manage your account’s API keys:

1. [Log in](https://cloud.temporal.io/) to the Temporal Cloud UI.
1. Go to [Settings → API Keys](https://cloud.temporal.io/settings/api-keys)

Administrators can disable the creation of new API keys using the **Disable Create API Keys** button on the **API Keys**
Settings page. Existing API keys can still be used to authenticate into Temporal Cloud normally until they are either
disabled, deleted, or expired.

To disable or delete an individual API key use the vertical ellipsis menu in the API key table row.

To find an API key, you can filter by API key state and identity type (Global Administrators and Account Owners only).

:::caution DISABLED API KEYS

Deleting or disabling a key removes its ability to authenticate into Temporal Cloud. If you delete or disable an API key
being used by Workers to run a Workflow, those Workers will be unable to connect to Temporal until a new API key secret
is created and configured.

:::

## User API key management {/* #user-api-keys */}

Manage your personal API keys with the Temporal Cloud UI or `tcld`. These sections show you how to generate, manage, and
remove API keys for a user.

### Generate an API key

Create API keys using one of the following methods:

:::caution

- Once generated, copy and securely save the API key. It will be displayed only once for security purposes.

:::

#### Generate API keys with the Temporal Cloud UI

[Log in](https://cloud.temporal.io/) to the Temporal Cloud UI and navigate to your
[Profile Page → API Keys](https://cloud.temporal.io/profile/api-keys). Then select **Create API key** and provide the
following information:

- **API key name**: A short, identifiable name for the key
- **API key description**: A longer description of the key's use
- **Expiration date**: The end date for the API key

Finish by selecting **Generate API Key**.

#### Generate API keys with tcld

To generate an API key, log into your account and issue the following command:

```command
tcld login
tcld apikey create \
    --name <api-key-name> \
    --description "<api-key-description>" \
    --duration <api-key-duration>
```

Duration specifies the time until the API key expires, for example: "30d", "4d12h", etc.

### Enable or Disable an API key

You can enable or disable API keys. When disabled, an API key cannot authenticate with Temporal Cloud.

#### Manage API key state with the Temporal Cloud UI

Follow these steps:

1. [Log in](https://cloud.temporal.io/) to the Temporal Cloud UI.
1. Go to your [Profile Page → API Keys](https://cloud.temporal.io/profile/api-keys).
1. Select the vertical ellipsis menu in the API key table row.
1. Choose **Enable** or **Disable**.

#### Manage API Key State with tcld

To manage an API key, log into your account and use one of the following commands to enable or disable it:

```command
tcld login
tcld apikey disable --id <api-key-id>
tcld apikey enable --id <api-key-id>
```

### Delete an API key

Deleting an API key stops it from authenticating with Temporal Cloud.

:::caution

Deleting an API key used by Workers to run a Workflow will cause it to fail unless you rotate the key with a new one.
This can affect long-running Workflows that outlast the API key's lifetime.

:::

#### Delete API keys with the Temporal Cloud UI

Follow these steps to remove API keys:

1. [Log in](https://cloud.temporal.io/) to the Temporal Cloud UI.
1. Navigate to your [Profile Page → API Keys](https://cloud.temporal.io/profile/api-keys).
1. Select the vertical ellipsis menu in the API key table row.
1. Choose **Delete**.

#### Delete API keys with tcld

To delete an API key, log into your account and issue the following:

```command
tcld login
tcld apikey delete --id <api-key-id>
```

### Rotate an API key

Temporal API keys automatically expire based on the specified expiration time. Follow these steps to rotate API keys:

1. Create a new key. You may reuse key names if that helps.
1. Ensure that both the original key and new key function properly before moving to the next step.
1. Switch clients to load the new key and start using it.
1. Delete the old key after it is no longer in use.

For a broader machine-identity rotation strategy across API keys and Service Accounts, see
[Managing Temporal Cloud access control](/best-practices/cloud-access-control).

## Manage API keys for Service Accounts {/* #serviceaccount-api-keys */}

Global Administrators and Account Owners can manage and generate API keys for _all_ Service Accounts in their account.
Namespace Admins can manage and generate API keys for the Namespace-scoped Service Accounts they administer.

This is different for non-admin users, who manage and generate their own API keys.

### Generate an API Key for a Service Account

Create API keys for Service Accounts using one of the following methods:

:::caution

- Once generated, copy and securely save the API key. It will be displayed only once for security purposes.

:::

#### Generate API Keys with the Temporal Cloud UI

[Log in](https://cloud.temporal.io/) to the Temporal Cloud UI. Global Administrators or Account Owners can go to
[Settings → API Keys](https://cloud.temporal.io/settings/api-keys). Namespace Admins can go to
[Profile Page → API Keys](https://cloud.temporal.io/profile/api-keys). Select **Create API Key**, then choose **Service
Account** from the "Create an API key for" dropdown. In the "Mapped to identity" input box, select a Service Account and
provide the following information:

- **API key name**: A short, identifiable name for the key
- **API key description**: A longer description of the key's use
- **Expiration date**: The end date for the API key

Finish by selecting **Generate API Key**.

#### Generate API keys with tcld

To create an API key for a Service Account, use `tcld apikey create` with the `--service-account-id` flag:

```
tcld apikey create \
    --name <api-key-name> \
    --description "<api-key-description>" \
    --duration <api-key-duration> \
    --service-account-id <service-account-id>
```

### Enable or Disable an API key

Global Administrators and Account Owners can manage API key access for any user in their account using the Temporal
Cloud UI or `tcld`.

#### Manage keys with Temporal Cloud UI

Follow these steps:

1. [Log in](https://cloud.temporal.io/) to the Temporal Cloud UI.
1. Global Administrators or Account Owners can go to [Settings → API Keys](https://cloud.temporal.io/settings/api-keys).
   Namespace Admins can go to [Profile Page → API Keys](https://cloud.temporal.io/profile/api-keys).
1. Find the API key. Use the vertical ellipsis menu in the table row and select the Disable/Enable option to perform the
   action. There may be a delay after changing the status. Once successful, the updated API key status will be shown in
   the row.

#### Manage keys with tcld

Use the `tcld apikey disable` or `tcld apikey enable` command to disable or enable an API key:

```
tcld login
tcld apikey disable --id <api-key-id>
tcld apikey enable --id <api-key-id>
```

This command is the same for users and Service Accounts.

### Delete an API key for a Service Account

Global Administrators and Account Owners can delete API keys for any user or Service Account in their account using the
Temporal Cloud UI or `tcld`. Deleting a key removes its ability to authenticate with Temporal Cloud. If you delete an
API key used by a Worker to run a Workflow, that Worker will fail to connect to Temporal server unless you rotate the
API key with a new one.

#### Delete a Service Account API key with Temporal Cloud UI

Follow these steps:

1. Go to [Settings → API Keys](https://cloud.temporal.io/settings/api-keys).
1. Locate the API key. Use the vertical ellipsis menu in the table row and select the Delete option. There may be a
   delay after deleting the API key.
1. Once successful, the updated API key status will be reflected in the row.

#### Delete a Service Account API key with tcld

Use the `tcld apikey delete` command to delete an API key. The process for deleting an API key is the same for a user or
Service Account.

```
tcld login
tcld apikey delete --id <api-key-id>
```

### Rotate a Service Account API key

Temporal API keys automatically expire based on the specified expiration time. Follow these steps to rotate API keys:

1. Create a new key. You may reuse key names if that helps.
1. Ensure that both the original key and new key function properly before moving to the next step.
1. Switch clients to load the new key and start using it.
1. Delete the old key after it is no longer in use.

:::tip

Service Accounts can rotate their own API keys irrespective of their configured permissions. To use this feature, have
your Service Account create a new API key using the [Cloud Ops APIs](/ops) or [`tcld`](/cloud/tcld) before the current
one expires. Service Accounts cannot delete their own API keys without the requisite permissions, which helps keep
Workflow access secure.

:::

## API keys for Namespace authentication {/* #namespace-authentication */}

Create a Namespace with API key authentication as an alternative to mTLS-based authentication by selecting "Allow API
key authentication" during setup.

Use the gRPC Namespace endpoint: `<namespace>.<account>.tmprl.cloud:7233`. This is the recommended endpoint for all
Namespaces. For Namespaces with [High Availability](/cloud/high-availability), the Namespace endpoint automatically
directs traffic to the active region, so Workers and Clients don't need to change endpoints during a failover.

See [accessing Namespaces](/cloud/namespaces#access-namespaces) for more information on endpoint options.

## Use API keys to authenticate {/* #using-apikeys */}

Authenticate with Temporal Cloud using API keys with the following clients:

- [Temporal CLI](/cli)
- [SDKs](/develop)
- [Temporal Cloud CLI `tcld`](/cloud/tcld/index.mdx)
- [The Cloud Operations API](/cloud/operation-api.mdx)
- [Temporal’s Terraform Provider](/cloud/terraform-provider)

### Temporal CLI

To use your API key with the Temporal CLI, either pass it with the `--api-key` flag or set an environment variable in
