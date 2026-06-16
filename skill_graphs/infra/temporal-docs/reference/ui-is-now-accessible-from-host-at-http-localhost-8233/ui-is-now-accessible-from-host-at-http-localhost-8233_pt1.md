# UI is now accessible from host at http://localhost:8233/
```

::::

</TabItem>

</Tabs>

## Install the Temporal Cloud extension

If you are using Temporal Cloud, install the Temporal Cloud extension for the Temporal CLI. You can install the
extension using the following command:

:::tip Support, stability, and dependency info

The Temporal Cloud extension is in [Pre-release](/evaluate/development-production-features/release-stages#pre-release).
APIs and configuration may change before the stable release.

:::

```bash
brew install temporalio/prerelease/temporal-cloud
```

## Run a local development server

The CLI includes a local Temporal development service for fast feedback while building your application.

Start the server:

```bash
temporal server start-dev
```

This command automatically starts the Web UI, creates the `default` [Namespace](/namespaces), and uses an in-memory
SQLite database.

The Temporal Server will be available on `localhost:7233` and the Temporal Web UI will be available at
[`http://localhost:8233`](http://localhost:8233/).

Persist state locally by specifying a database file:

```shell
temporal server start-dev --db-filename temporal.db
```

### Development server configuration

#### Namespace registration

Namespaces are pre-registered at startup for immediate use. Customize pre-registered Namespaces with the following
command:

```shell
temporal server start-dev --namespace foo --namespace bar
```

Register Namespaces with `namespace create`:

```shell
temporal operator namespace create --namespace foo
```

#### Enable or turn off the Temporal Web UI

By default, the Temporal Web UI is enabled when running the development server using the Temporal CLI. To turn off the
UI, use the `--headless` modifier:

```shell
temporal server start-dev --headless
```

#### Dynamic configuration

Advanced Temporal CLI configuration requires a dynamic configuration file.

To set values on the command line, use `--dynamic-config-value KEY=JSON_VALUE`. For example, enable the Search Attribute
cache:

```bash
temporal server start-dev --dynamic-config-value system.forceSearchAttributesCacheRefreshOnRead=false
```

This setting makes created Search Attributes immediately available.

## Configure the CLI

### Environment variables

The following table describes the environment variables you can set for the Temporal CLI.

{/* This is an automatically generated file and the TEMPORAL_API_KEY correction will disappear on the next push. */}

| Variable                                 | Definition                                                                | Client Option                   |
| ---------------------------------------- | ------------------------------------------------------------------------- | ------------------------------- |
| `TEMPORAL_ADDRESS`                       | Host and port (formatted as host:port) for the Temporal Frontend Service. | --address                       |
| `TEMPORAL_CODEC_AUTH`                    | Authorization header for requests to Codec Server.                        | --codec-auth                    |
| `TEMPORAL_CODEC_ENDPOINT`                | Endpoint for remote Codec Server.                                         | --codec-endpoint                |
| `TEMPORAL_NAMESPACE`                     | Namespace in Temporal Workflow. Default: "default".                       | --namespace                     |
| `TEMPORAL_TLS_CA`                        | Path to server CA certificate.                                            | --tls-ca-path                   |
| `TEMPORAL_TLS_CERT`                      | Path to x509 certificate.                                                 | --tls-cert-path                 |
| `TEMPORAL_TLS_DISABLE_HOST_VERIFICATION` | Turns off TLS host name verification. Default: false.                     | --tls-disable-host-verification |
| `TEMPORAL_TLS_KEY`                       | Path to private certificate key.                                          | --tls-key-path                  |
| `TEMPORAL_TLS_SERVER_NAME`               | Override for target TLS server name.                                      | --tls-server-name               |
| `TEMPORAL_API_KEY`                       | API key used for authentication.                                          | --api-key                       |

{/* This is an automatically generated file and this caution will disappear on the next push. */}
{/* issue: https://github.com/temporalio/cli/issues/776 */}

### Create and modify configuration files

The Temporal CLI lets you create and modify TOML configuration files to store your environment variables and other
settings. Refer to [Environment Configuration](../develop/environment-configuration#cli-integration) for more
information.

### Configure proxy support

The Temporal CLI provides support for users who are operating behind a proxy. This feature ensures seamless
communication even in network-restricted environments.

#### Setting up proxy support

If you are behind a proxy, you'll need to instruct the Temporal CLI to route its requests via that proxy. You can
achieve this by setting the `HTTPS_PROXY` environment variable.

```command
export HTTPS_PROXY=<host>:<port>
```

Replace `<host>` with the proxy's hostname or IP address, and `<port>` with the proxy's port number.

Once set, you can run the Temporal CLI commands as you normally would.

::::note

Temporal CLI uses the gRPC library which natively supports HTTP CONNECT proxies. The gRPC library checks for the
`HTTPS_PROXY` (and its case-insensitive variants) environment variable to determine if it should route requests through
a proxy.

::::

In addition to `HTTPS_PROXY`, gRPC also respects the `NO_PROXY` environment variable. This can be useful if there are
specific addresses or domains you wish to exclude from proxying.

For more information, see [Proxy](https://github.com/grpc/grpc-go/blob/master/Documentation/proxy.md) in the gRPC
documentation.

## Enable auto-completion

Enable auto-completion using the following commands.

### zsh auto-completion

1. Add the following line to your `~/.zshrc` startup script:

   ```sh
   eval "$(temporal completion zsh)"
   ```

2. Re-launch your shell or run:

   ```sh
   source ~/.zshrc
   ```

### Bash auto-completion

1. Install [bash-completion](https://github.com/scop/bash-completion#installation) and add the software to your
   `~/.bashrc`.

2. Add the following line to your `~/.bashrc` startup script:

   ```sh
   eval "$(temporal completion bash)"
   ```

3. Re-launch your shell or run:

   ```sh
   source ~/.bashrc
   ```

::::note

If auto-completion fails with the error: `bash: _get_comp_words_by_ref: command not found`, you did not successfully
install [bash-completion](https://github.com/scop/bash-completion#installation). This package must be loaded into your
shell for `temporal` auto-completion to work.

::::

### Fish auto-completion

1. Create the Fish custom completions directory if it does not already exist:

   ```fish
   mkdir -p ~/.config/fish/completions
   ```

2. Configure the completions to load when needed. Note: the filename must be `temporal.fish` or the completions will not
   be found:

   ```fish
   echo 'eval "$(temporal completion fish)"' >~/.config/fish/completions/temporal.fish
   ```

3. Re-launch your shell or run:

   ```fish
   source ~/.config/fish/completions/temporal.fish
   ```

## Getting CLI help

From the command line:

```
temporal <command> <subcommand> --help
```

For example:

- `temporal --help`
- `temporal workflow --help`
- `temporal workflow delete --help`

For a full list of commands, see the [Temporal CLI command reference](/cli#command-reference).

---

## Audit Logs - AWS Kinesis

## Configure Audit Logs using AWS Kinesis {/* #configure-audit-log */}

To set up Audit Logs, you must have an Amazon Web Services (AWS) account and set up Kinesis Data Streams.

1. If you don't have an AWS account, follow the instructions from AWS in [Create and activate an AWS account](https://aws.amazon.com/premiumsupport/knowledge-center/create-and-activate-aws-account/).
2. To set up Kinesis Data Streams, open the [AWS Management Console](https://aws.amazon.com/console/), search for Kinesis, and start the setup process.

You can use [this AWS CloudFormation template](https://temporal-auditlogs-config.s3.us-west-2.amazonaws.com/cloudformation/iam-role-for-temporal-audit-logs.yaml) to create an IAM role with access to a Kinesis stream you have in your account.

Be aware that Kinesis has a rate limit of 1,000 messages per second and quotas for both the number of records written and the size of the records.
For more information, see [Why is my Kinesis data stream throttling?](https://aws.amazon.com/premiumsupport/knowledge-center/kinesis-data-stream-throttling/)

### Create an Audit Log sink

1. In the Temporal Cloud UI, select **Settings**.
1. On the **Settings** page, select **Audit Logs**.
1. In the **Audit Log Integration** card, select **Setup**.
1. On the **Audit Log Integration** page, choose your **Access method** (either **Auto** or **Manual**).
   - **Auto:** Configure the AWS CloudFormation stack in your AWS account from the Cloud UI.
   - **Manual:** Use a generated AWS CloudFormation template to set up Kinesis manually.
1. In **Kinesis ARN**, paste the Kinesis ARN from your AWS account.
1. In **Role name**, provide a name for a new IAM Role.
1. In **Select an AWS region**, select the appropriate region for your Kinesis stream.

If you chose the **Auto** access method, continue with the following steps:

1. Select **Save and launch stack**.
1. In **Stack name** in the AWS CloudFormation console, specify a name for the stack.
1. In the lower-right corner of the page, select **Create stack**.

If you chose the **Manual** access method, continue with the following steps:

1. Select **Save and download template**.
1. Open the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/).
1. Select **Create Stack**.
1. On the **Create stack** page, select **Template is ready** and **Update a template file**.
1. Select **Choose file** and specify the template you generated in step 1.
1. Select **Next** on this page and on the next two pages.
1. On the **Review** page, select **Create stack**.

To ensure that Audit Logs can flow into the Kinesis stream, you can use the **Verify** button to confirm it is set up correctly. This validates that Temporal can successfully write to your stream.
If everything is configured correctly, you will see a `Success` status indicating Temporal has written to the kinesis stream.

## Consume an Audit Log {/* #consume-an-audit-log */}

**How to consume an Audit Log**

After you create an Audit Log sink, wait for the logs to flow into the Kinesis stream.
You will see the first logs within 10 minutes after you configure the sink.

:::note

You must configure and implement your own consumer of the Kinesis stream.
For an example, see [Example of consuming an Audit Log](#example-of-consuming-an-audit-log).

:::

### Example of consuming an Audit Log

The following Go code is an example of consuming Audit Logs from a Kinesis stream and delivering them to an S3 bucket.

```go
func main() {
   fmt.Println("print audit log from S3")
   cfg, err := config.LoadDefaultConfig(context.TODO(),
      config.WithSharedConfigProfile("your_profile"),
   )
   if err != nil {
      fmt.Println(err)
   }
   s3Client := s3.NewFromConfig(cfg)
   response, err := s3Client.GetObject(
      context.Background(),
      &s3.GetObjectInput{
         Bucket: aws.String("your_bucket_name"),
         Key:    aws.String("your_s3_file_path")})
   if err != nil {
      fmt.Println(err)
   }
   defer response.Body.Close()

   content, err := io.ReadAll(response.Body)

   fmt.Println(string(content))
}
```

The preceding code also prints the logs in the terminal.
The following is a sample result.

```json
{
  "emit_time": "2023-11-14T07:56:55Z",
  "level": "LOG_LEVEL_INFO",
  "caller_ip_address": "10.1.2.3, 10.4.5.6",
  "user_email": "user1@example.com",
  "operation": "DeleteUser",
  "details": {
    "target_users": ["d7dca96f-adcc-417d-aafc-e8f5d2ba9fe1"],
    "search_attribute_update": {}
  },
  "status": "OK",
  "category": "LOG_CATEGORY_ADMIN",
  "log_id": "0mc69c0323b871293ce231dd1c7fb639",
  "request_id": "445297d3-43a7-4793-8a04-1b1dd1999640",
  "principal": {
    "id": "988cb80b-d6be-4bb5-9c87-d09f93f58ed3",
    "type": "user",
    "name": "user1@example.com"
  }
}
```

---

## Audit Logs - GCP Pub/Sub

## Manual Setup Prerequisites

:::note

These steps are only required for manual setup.
If you use Terraform for your deployment, you don't need to complete these prerequisites.

:::

Before configuring the manual Audit Log sink, complete the following steps in Google Cloud:

1. Create a Pub/Sub topic and make a note of its topic name, such as `test-auditlog`.
1. Set up a service account in the same project in Google Cloud and follow the instructions in the
   Temporal Cloud UI to configure the permissions for that service account.

## Create an Audit Log sink

1. In the Temporal Cloud UI, select **Settings**.
1. On the **Settings** page, select **Audit Logs**.
1. In the **Audit Logs Integration** card, select **Setup**.
1. On the **Audit Log Integration** page, select **Pub/Sub**.
1. In the **service account email** field, enter the email of the service account you created in the prerequisites.
1. In the **Topic name** field, enter the topic name of the Pub/Sub topic you created in the prerequisites.
1. There are two ways to configure the service account to write to the Pub/Sub sink: select **Manual** to configure the account manually, or **Deploy with Terraform** to use Terraform.
   If you use Terraform, you don't need to complete the prerequisite steps above.
1. Follow the instructions in the Temporal Cloud UI for the method you chose.
1. To ensure that audit logs can reach your Pub/Sub topic, you can use the **Verify** button to confirm it is set up correctly. This validates that Temporal can successfully write to your topic.
If everything is configured correctly, you will see a `Success` status indicating Temporal has written to the Pub/Sub topic.
1. Click **Create** to configure the audit log.
   Audit Logs will begin to show up in Pub/Sub within 10 minutes

![Temporal Cloud UI Setup for Audit Logs with GCP Pub/Sub](/img/cloud/gcp/audit-logging-pub-sub-gcp.png)

:::info MORE INFORMATION

For more details, refer to [Audit Logs with Temporal Cloud](https://docs.temporal.io/cloud/audit-logs).

:::

---

## Audit Logs

Audit Logs is a feature of [Temporal Cloud](/cloud/overview) that provides forensic access information for a variety of operations in the Temporal Cloud Control Plane.

Audit Logs answers "who, when, and what" questions about Temporal Cloud resources.
These answers can help you evaluate the security of your organization, and they can provide information that you need to satisfy audit and compliance requirements.

You need the Account Owner or Global Administrator role to view Audit Logs via UI, use the API, or to configure an Audit Log Integration with [AWS Kinesis](/cloud/audit-logs-aws) or [GCP Pub/Sub](/cloud/audit-logs-gcp).

:::info

Audit Logs do NOT capture data plane events, like Workflow Start, Workflow Terminate, Schedule Create, etc.
Instead, explore the [Export](/cloud/export) feature, which does let you send closed Workflow Histories to external storage.

:::

## Which events are supported by Audit Logs? {/* #supported-events */}

- Account
  - `ChangeAccountPlanType`: Change Account Plan Type
  - `UpdateAccountAPI`: Configure Audit Logs, Configure Observability Endpoint
- API Keys
  - `CreateAPIKey`: Create API Key
  - `DeleteAPIKey`: Delete API Key
  - `UpdateAPIKey`: Update API Key
- Connectivity Rules
  - `CreateConnectivityRule`: Create Connectivity Rule
  - `DeleteConnectivityRule`: Delete Connectivity Rule
- Namespace
  - `CreateNamespaceAPI`: Create Namespace
  - `DeleteNamespaceAPI`: Delete Namespace
  - `FailoverNamespacesAPI`: Failover (for High Availability Namespaces)
  - `RenameCustomSearchAttributeAPI`: Rename Custom Search Attribute
  - `UpdateNamespaceAPI`: Includes retention period changes, replica edits, authentication method updates, custom search attribute updates, and connectivity rule bindings
- Namespace Export
  - `CreateNamespaceExportSink`: Create Namespace Export Sink
  - `DeleteNamespaceExportSink`: Delete Namespace Export Sink
  - `UpdateNamespaceExportSink`: Update Namespace Export Sink
  - `ValidateNamespaceExportSink`: Validate Namespace Export Sink
- Nexus Endpoint
  - `CreateNexusEndpoint`: Create Nexus Endpoint
  - `DeleteNexusEndpoint`: Delete Nexus Endpoint
  - `UpdateNexusEndpoint`: Update Nexus Endpoint
- Service Accounts
  - `CreateServiceAccount`: Create Service Account
  - `CreateServiceAccountAPIKey`: Create Service Account API Key
  - `DeleteServiceAccount`: Delete Service Account
  - `UpdateServiceAccount`: Update Service Account
- User
  - `CreateUserAPI`: Create Users
  - `DeleteUserAPI`: Delete Users
  - `InviteUsersAPI`: Invite Users
  - `SetUserNamespaceAccessAPI`: Set User Namespace Access
  - `UpdateIdentityNamespacePermissionsAPI`: Update Identity Namespace Permissions
  - `UpdateUserAPI`: Update User Account-level Roles
  - `UpdateUserNamespacePermissionsAPI`: Update User Namespace Permissions
- User Groups
  - `CreateUserGroup`: Create User Group
  - `DeleteUserGroup`: Delete User Group
  - `SetUserGroupNamespaceAccess`: Set User Group Namespace Access
  - `UpdateUserGroup`: Update User Group

### Audit Log format

:::info DEPRECATION NOTICE

The `request_id` field is deprecated and is planned for removal on or after November 1 2026. Use `async_operation_id` instead.

:::

Audit Logs use the following JSON format:

```json
{
  "operation":          // Operation that was performed
  "principal":          // Information about who initiated the operation
  "raw_details":        // Details about the request
  "x_forwarded_for":    // The IP address(es) making the call
  "emit_time":          // Time the operation was recorded
  "log_id":             // Unique ID of the log entry
  "async_operation_id": // Optional async operation id set by the user when sending a request
  "request_id":         // DEPRECATED, use async_operation_id
  "status":             // Status, such as OK or ERROR
  "version":            // Version of the log entry
}
```

:::note

The [`X-Forwarded-For`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Forwarded-For) format is a comma-separated list of IP addresses which should be evaluated from the last to the first, until meeting the first untrusted IP address of the list. This allows for instance to consider proxies in the path.

Temporal provides the caller IP address in that format to allow customers to identify a caller IP address even if one (or more proxies) are in the network path to reach Temporal Cloud.

:::

### Example of an Audit Log

```json
[
  {
    "operation": "UserLogin",
    "status": "OK",
    "version": 2,
    "logId": "edb3aa3e-78c4-48fc-9c7e-2078c6989775",
    "xForwardedFor": "10.1.2.3",
    "asyncOperationId": "",
    "emitTime": {
      "$typeName": "google.protobuf.Timestamp",
      "seconds": 1759436617,
      "nanos": 48000000
    },
    "principal": {
      "type": "user",
      "id": "",
      "name": "user@email.com",
      "apiKeyId": ""
    }
  },
  {
    "operation": "UserLogin",
    "status": "OK",
    "version": 2,
    "logId": "5fe6a81e-8d3c-4f4d-88a5-52db864c9ea5",
    "xForwardedFor": "10.1.2.3",
    "asyncOperationId": "",
    "emitTime": {
      "seconds": 1759178573,
      "nanos": 671000000
    },
    "principal": {
      "type": "user",
      "id": "",
      "name": "user@email.com",
      "apiKeyId": ""
    }
  }
]
```

## How to configure an Audit Log Integration {/* #configure-audit-logs */}

Audit Logs can be configured in AWS Kinesis or GCP Pub/Sub.

- [AWS Kinesis Instructions](/cloud/audit-logs-aws)
- [GCP Pub/Sub Instructions](/cloud/audit-logs-gcp)

## How to troubleshoot Audit Log sink {/* #troubleshoot-audit-logs */}

The Audit Logs page of the Temporal Cloud UI provides the current status of an Audit Log Integration.

- If an error is detected, a summary of the error appears below the page title.
- If the Audit Log Integration is functioning normally, an **On** badge appears next to the page heading.

After an Admin Operation is performed, users can see Audit Log messages flow through the stream.

Upon successful configuration of the Audit Log sink and set up of a stream, you will receive events within the hour of setup.
Temporal is able to retain Audit Log information for up to 30 days.
To retrieve logs up to the past 30 days, you will need to file a request.

If you experience an issue with an Audit Log sink, we can provide the missing audit information.
Open a support ticket to request assistance.

## How to delete an Audit Log sink {/* #delete-an-audit-log-sink */}

To delete an Audit Log sink, follow these steps:

1. In the Temporal Cloud UI, select **Settings**.
1. On the **Settings** page, select **Audit Logs**.
1. In the **Audit Logs Integration** card, select **Edit**.
1. At the bottom of the **Audit Logs Integration** page, choose **Delete**.

After you confirm the deletion, the Audit Log Sink is removed from your account and logs stop flowing to your stream.

## View an Audit Log {/* #view-an-audit-log */}

An Audit Log can be viewed in the Temporal Cloud UI.
1. In the Temporal Cloud UI, select **Settings**.
1. On the **Settings** page, select **Audit Logs**.

Up to 1000 events can be downloaded from the Audit Log UI to a local file.

## Access an Audit Log via API {/* #audit-log-api */}

An Audit Log can be accessed using the [Temporal Cloud Ops API](/ops). Use the API to access
an Audit Log if you wish to make dashboards for viewing an Audit Log outside of Temporal Cloud.
If your goal is to export an Audit Log, it is better to use an Audit Log sink and capture each
entry as it is generated.

Audit Logs are accessible for the past 30 days using the API.

The API allows:
- StartTimeInclusive: Filter for UTC time >= (defaults to 30 days ago) - optional
- EndTimeExclusive: Filter for UTC time < (defaults to current time) - optional
- PageSize: Cannot exceed 1000. Defaults to 100. - optional
- PageToken: The page token if this is continuing from another response - optional

---

## Exporting Workflow Event History to AWS S3

## Prerequisites

Before configuring the Export Sink, ensure you have the following:

- An AWS S3 bucket.
   - The S3 bucket must reside in the same region as your Namespace.
- (Optional) An IAM role that has write permission to the above S3 bucket.
   - You can follow the automation in the UI to create the IAM role. Please pre-create the role if setting up Export via terraform/tcld.
- (Optional) A KMS ARN associated with the S3 bucket.

## Configure Workflow History export

There are multiple ways to configure export: through the [Temporal Cloud UI](#using-temporal-cloud-ui), [`tcld`](#using-tcld), or [`terraform`](#using-terraform).

### Using Temporal Cloud UI

You can use the Temporal Cloud UI to configure the Workflow History Export.

The Temporal Cloud UI provides two ways for configuring Workflow History Export:

- [Automated setup](#automated-setup) (recommended): The Cloud UI launches the AWS CloudFormation Console to create a stack with write permission to the S3 bucket.
- [Manual setup](#manual-setup): The Cloud UI provides a CloudFormation template for users to manually configure a CloudFormation stack.

:::info Why does Temporal Cloud provision multiple internal IAM roles to trust for Export?

Temporal Cloud creates multiple intermediary IAM roles for export operations for security purposes.
The system randomly selects from these roles when writing to your storage sink, which provides several benefits:

- **Security isolation**: If one IAM role is compromised or needs to be decommissioned, other IAM roles remain available
- **Load distribution**: Avoids relying on a single IAM role, reducing security risk
- **Warm standby**: Keeps multiple IAM roles active to avoid potential throttling when switching between IAM roles
- **Reliability**: Provides resilience against cloud provider account-level issues that could affect a single IAM role

This approach prioritizes security and availability, ensuring robust export operations even if individual IAM roles encounter issues.
:::

The following steps guide you through setting up Workflow History Export using the Temporal Cloud UI.

![](/img/cloud/gcp/export-sink-ui.png)

:::tip

Don't forget to click **Create** at the end of your setup to confirm your export.

:::

#### Automated setup

You can use the automated setup to create a CloudFormation stack with write permission to your S3 bucket.
Make sure to verify the export setup before you save the configuration.

1. Open the Temporal Cloud UI and navigate to the Namespace you want to configure.
2. Select **Configure** from the **Export** card.
3. Provide the following information to configure the export sink and then select **Create and launch stack**:
   - Name: A name for the export sink.
   - AWS S3 Bucket Name: The name of the configured AWS S3 bucket to send Closed Workflow Histories to.
   - AWS Account ID: The AWS account ID.
   - Role Name: The name of the AWS IAM role to use for the CloudFormation stack that has write permission to the S3 bucket.
   - KMS ARN: (optional) The ARN of the AWS KMS key to use for encryption of the exported Event History.
