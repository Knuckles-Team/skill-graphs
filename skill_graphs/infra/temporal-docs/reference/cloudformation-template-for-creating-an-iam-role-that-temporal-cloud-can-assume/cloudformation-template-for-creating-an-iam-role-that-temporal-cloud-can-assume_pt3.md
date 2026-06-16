      return await wf.makeContinueAsNewFunc<typeof continueAsNewWithVersionUpgrade>({
        initialVersioningBehavior: InitialVersioningBehavior.AUTO_UPGRADE,
      })(attempt + 1);
    }
  }
}
```

</SdkTabs.TypeScript>
<SdkTabs.DotNet>

```csharp
[Workflow]
public class ContinueAsNewWithVersionUpgrade
{
    [WorkflowRun]
    public async Task<string> RunAsync(int attempt)
    {
        if (attempt > 0)
        {
            return "v1.0";
        }

        // TargetWorkerDeploymentVersionChanged is refreshed after each Workflow Task completes.
        // In a Workflow that regularly does non-sleep Workflow Tasks you wouldn't need an
        // artificial timer; you could check the flag periodically, or before accepting Updates,
        // starting Activities, or starting child Workflows.
        while (true)
        {
            await Workflow.DelayAsync(TimeSpan.FromMilliseconds(10));
            if (Workflow.TargetWorkerDeploymentVersionChanged)
            {
                // Set InitialVersioningBehavior to AutoUpgrade so the new run starts with
                // AutoUpgrade behavior and uses the Target Version of its Worker Deployment.
                throw Workflow.CreateContinueAsNewException(
                    (ContinueAsNewWithVersionUpgrade wf) => wf.RunAsync(attempt + 1),
                    new ContinueAsNewOptions
                    {
                        InitialVersioningBehavior = InitialVersioningBehavior.AutoUpgrade,
                    });
            }
        }
    }
}
```

</SdkTabs.DotNet>
<SdkTabs.Ruby>

```ruby
class ContinueAsNewWithVersionUpgrade < Temporalio::Workflow::Definition
  workflow_versioning_behavior Temporalio::VersioningBehavior::PINNED

  def execute(attempt)
    return 'v1.0' if attempt.positive?

    # target_worker_deployment_version_changed? is refreshed after each Workflow Task completes.
    # In a Workflow that regularly does non-sleep Workflow Tasks you wouldn't need an artificial
    # timer; you could check the flag periodically, or before accepting Updates, starting
    # Activities, or starting child Workflows.
    loop do
      Temporalio::Workflow.sleep(0.01)
      next unless Temporalio::Workflow.target_worker_deployment_version_changed?

      # Set initial_versioning_behavior to AUTO_UPGRADE so the new run starts with AutoUpgrade
      # behavior and uses the Target Version of its Worker Deployment.
      raise Temporalio::Workflow::ContinueAsNewError.new(
        attempt + 1,
        initial_versioning_behavior: Temporalio::ContinueAsNewVersioningBehavior::AUTO_UPGRADE
      )
    end
  end
end
```

</SdkTabs.Ruby>
</SdkTabs>

### Limitations {/* #upgrade-on-can-limitations */}

:::caution Current Limitations

- **Lazy moving only:** Workflows must execute a step to receive the target-version-changed information. Sleeping
  Workflows won't proactively get it. If you have idle Workflows that you want to wake up so they can check the
  target-version-changed flag, you can send them a Signal.
- **Interface compatibility:** When continuing as new to a different version, ensure your Workflow input provided by the
  previous version's workflow definition is compatible with the new version's workflow definition. If incompatible, the
  new run may fail on its first Workflow Task.

:::

## Sunsetting an old Deployment Version

A Worker Deployment Version moves through the following states:

1. **Inactive**: The version exists because a Worker with that version has polled the server. If this version never
   becomes Active, it will never be Draining or Drained.
2. **Active**: The version is either Current or Ramping, so it is accepting new Workflows and existing Auto-Upgrade
   Workflows.
3. **Draining**: The version stopped being Current or Ramping, and it has open pinned Workflows running on it. It is
   possible to be Draining and have no open pinned Workflows for a short time, since the drainage status is updated
   periodically.
4. **Drained**: The version was draining and now all the pinned Workflows that were running on it are closed.

You can see these statuses when you describe a Worker Deployment in the `WorkerDeploymentVersionStatus` of each
`VersionSummary`, or by describing the version directly. When a version is Draining or Drained, that is displayed in a
value called `DrainageStatus`. Periodically, the Temporal Service will refresh this status by counting any open pinned
Workflows using that version.

On each refresh, `DrainageInfo.last_checked_time` is updated. Eventually, `DrainageInfo` will report that the version is
fully drained. At this point, no Workflows are still running on that version and no more will be automatically routed to
it, so you can consider shutting down the running Workers.

You can monitor this by checking `WorkerDeploymentInfo.VersionSummaries` or with
`temporal worker deployment describe-version`:

```bash
temporal worker deployment describe-version \
    --deployment-name "YourDeploymentName" \
    --build-id "YourBuildID"
```

```
Worker Deployment Version:
  Version                  llm_srv.1.0
  CreateTime               5 hours ago
  RoutingChangedTime       32 seconds ago
  RampPercentage           0
  DrainageStatus           draining
  DrainageLastChangedTime  31 seconds ago
  DrainageLastCheckedTime  31 seconds ago

Task Queues:
     Name        Type
  hello-world  activity
  hello-world  workflow
```

If you have implemented [Queries](/sending-messages#sending-queries) on closed pinned Workflows, you may need to keep
some Workers running to handle them.

### Adding a pre-deployment test

Before deploying a new Workflow revision, you can test it with synthetic traffic.

To do this, use pinning in your tests, following the examples below

<SdkTabs>
<SdkTabs.Go>
```go
workflowOptions := client.StartWorkflowOptions{
	ID:        "MyWorkflowId",
	TaskQueue: "MyTaskQueue",
	VersioningOverride: &client.PinnedVersioningOverride{
        Version: worker.WorkerDeploymentVersion{
            DeploymentName: "DeployName",
            BuildId:        "1.0",
        },
    },
}
// c is an initialized Client
we, err := c.ExecuteWorkflow(context.Background(), workflowOptions, HelloWorld, "Hello")
```
</SdkTabs.Go>
<SdkTabs.Java>
```java
MyWorkflow handle = client.newWorkflowStub(
    MyWorkflow.class,
    WorkflowOptions.newBuilder()
        .setWorkflowId("MyWorkflowId")
        .setTaskQueue("MyTaskQueue")
        .setVersioningOverride(new VersioningOverride.PinnedVersioningOverride(
            new WorkerDeploymentVersion("DeployName", "1.0")))
        .build()
);
WorkflowExecution we = WorkflowClient.start(handle::execute, "Hello");
```
</SdkTabs.Java>
<SdkTabs.Python>
```python
handle = client.start_workflow(
    MyWorkflow.run,
    "Hello",
    id="MyWorkflowId",
    task_queue="MyTaskQueue",
    versioning_override=PinnedVersioningOverride(
        WorkerDeploymentVersion("DeployName", "1.0")
    ),
)
```
</SdkTabs.Python>
<SdkTabs.TypeScript>
```ts
const handle = await client.workflow.start('helloWorld', {
  taskQueue: 'MyTaskQueue',
  workflowId: 'MyWorkflowId',
  versioningOverride: {
    pinnedTo: { buildId: '1.0', deploymentName: 'deploy-name' },
  },
});
```
</SdkTabs.TypeScript>
<SdkTabs.DotNet>
```csharp
var workerV1 = new WorkerDeploymentVersion("deploy-name", "1.0");
var handle = await Client.StartWorkflowAsync(
    (HelloWorld wf) => wf.RunAsync(),
      	new(id: "MyWorkflowId", taskQueue: "MyTaskQueue")
      	{
           VersioningOverride = new VersioningOverride.Pinned(workerV1),
        }
);
```
</SdkTabs.DotNet>
<SdkTabs.Ruby>
```ruby
worker_v1 = Temporalio::WorkerDeploymentVersion.new(
  deployment_name: 'deploy-name',
  build_id: '1.0'
)
handle = env.client.start_workflow(
  HelloWorld,
  id: 'MyWorkflowId',
  task_queue: 'MyTaskQueue',
  versioning_override: Temporalio::VersioningOverride.pinned(worker_v1)
)
```
</SdkTabs.Ruby>
</SdkTabs>

## Garbage collection

Worker Deployments are never garbage collected, but _Worker Deployment Versions_ (often referred to as Versions, Worker
Versions, Deployment Versions) are.

Versions are deleted to keep the total number of versions in one Worker Deployment less than or equal to
[`matching.maxVersionsInDeployment`](https://github.com/temporalio/temporal/blob/a3a53266c002ae33b630a41977274f8b5b587031/common/dynamicconfig/constants.go#L1317-L1321),
which is currently set to 100 in Temporal Cloud, but that's a conservative number and it could be increased if needed.

For example, when you deploy your 101st Worker Version in a Worker Deployment, the server looks at the oldest drained
version in the Worker deployment. If it has had no pollers in the last 5 minutes, the server deletes it. If that version
still has pollers, the server will try the next oldest version. If none of the 100 versions are eligible for deletion
(ie. none of them are drained with no pollers), then no version will be deleted and the poll from the 101st version
would fail.

At that point, to successfully deploy your 101st version, you would need to increase `matching.maxVersionsInDeployment`
or stop polling from one of the old drained versions to make it eligible for clean up.

If you want to re-deploy a previously deleted version, start polling with a Worker that has the same build ID and
Deployment Name as the deleted version and the server will recreate it.

This covers the complete lifecycle of working with Worker Versioning. We are continuing to improve this feature, and we
welcome any feedback or feature requests using the sidebar link!

---

## Quickstarts

Choose your language to get started locally. If you're using Temporal Cloud, check out [Get started with Temporal Cloud](/cloud/get-started).

<QuickstartCards
  items={[
    { href: "/develop/go/set-up-your-local-go", title: "Go", description: "Install the Go SDK and run a Hello World Workflow in Go." },
    { href: "/develop/java/set-up-your-local-java", title: "Java", description: "Install the Java SDK and run a Hello World Workflow in Java." },
    { href: "/develop/php/set-up-your-local-php", title: "PHP", description: "Install the PHP SDK and run a Hello World Workflow in PHP." },
    { href: "/develop/python/set-up-your-local-python", title: "Python", description: "Install the Python SDK and run a Hello World Workflow in Python." },
    { href: "/develop/ruby/set-up-local-ruby", title: "Ruby", description: "Install the Ruby SDK and run a Hello World Workflow in Ruby." },
    { href: "/develop/typescript/set-up-your-local-typescript", title: "TypeScript", description: "Install the TypeScript SDK and run a Hello World Workflow in TypeScript." },
    { href: "/develop/dotnet/set-up-your-local-dotnet", title: ".NET", description: "Install the .NET SDK and run a Hello World Workflow in C#." },
    { href: "/develop/rust/quickstart", title: "Rust", description: "Install the Rust SDK and run a Hello World Workflow in Rust." },
  ]}
/>

---

## API reference

Complete API documentation for all Temporal SDKs and server APIs.

## SDK API References

<PatternCards items={[
  {
    href: "https://pkg.go.dev/go.temporal.io/sdk",
    title: "Go SDK API",
    description: "Complete Go SDK API documentation on pkg.go.dev with all packages, types, and methods.",
    external: true,
  },
  {
    href: "https://www.javadoc.io/doc/io.temporal/temporal-sdk/latest/index.html",
    title: "Java SDK API",
    description: "Complete Java SDK API documentation on javadoc.io with all classes, interfaces, and annotations.",
    external: true,
  },
  {
    href: "https://php.temporal.io/namespaces/temporal.html",
    title: "PHP SDK API",
    description: "Complete PHP SDK API documentation with all namespaces, classes, and interfaces.",
    external: true,
  },
  {
    href: "https://python.temporal.io/",
    title: "Python SDK API",
    description: "Complete Python SDK API documentation with all modules, classes, and functions.",
    external: true,
  },
  {
    href: "https://ruby.temporal.io/",
    title: "Ruby SDK API",
    description: "Complete Ruby SDK API documentation with all modules, classes, and methods.",
    external: true,
  },
  {
    href: "https://typescript.temporal.io",
    title: "TypeScript SDK API",
    description: "Complete TypeScript SDK API documentation with all interfaces, types, and namespaces.",
    external: true,
  },
  {
    href: "https://dotnet.temporal.io/api/",
    title: ".NET SDK API",
    description: "Complete .NET SDK API documentation with all namespaces, classes, and methods.",
    external: true,
  },
]} />

## Server API References

<PatternCards items={[
  {
    href: "/self-hosted-guide/server-frontend-api-reference",
    title: "Server Frontend API",
    description: "gRPC API reference used by Client and Worker SDKs to communicate with Temporal Server.",
  },
]} />

## Need Help?

For questions about specific APIs, use the **Ask AI** button in the top navigation for instant answers, connect our [Model Context Protocol server](/with-ai) to AI tools for real-time documentation access, or visit our [Community Forum](https://community.temporal.io/) and [Slack](https://temporal.io/slack) for community support.

---

## Environment configuration(References)

The following table details all available settings, their corresponding environment variables, and their TOML file
paths. For more information on using environment variables and configuration files to set up your Temporal Client, refer
to the [Environment Configuration](/develop/environment-configuration).

| Setting                   | Environment Variable                     | TOML Path                                      | Description                                                                                                                                                                                                                 |
| :------------------------ | :--------------------------------------- | :--------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Configuration File Path   | `TEMPORAL_CONFIG_FILE`                   | **NA**                                         | Path to the TOML configuration file                                                                                                                                                                                         |
| Server Address            | `TEMPORAL_ADDRESS`                       | `profile.<name>.address`                       | The host and port of the Temporal Frontend service (e.g., "localhost:7233").                                                                                                                                                |
| Namespace                 | `TEMPORAL_NAMESPACE`                     | `profile.<name>.namespace`                     | The Temporal Namespace to connect to.                                                                                                                                                                                       |
| API Key                   | `TEMPORAL_API_KEY`                       | `profile.<name>.api_key`                       | An API key for authentication. If present, TLS is enabled by default.                                                                                                                                                       |
| Enable/Disable TLS        | `TEMPORAL_TLS`                           | `profile.<name>.tls.disabled`                  | Set to "true" to enable TLS, "false" to disable. In TOML, disabled = true turns TLS off.                                                                                                                                    |
| Client Certificate        | `TEMPORAL_TLS_CLIENT_CERT_DATA`          | `profile.<name>.tls.client_cert_data`          | The raw PEM data containing the client's public TLS certificate. Alternatively, you can use `TEMPORAL_TLS_CLIENT_CERT_PATH` to provide a path to the certificate or the TOML `profile.<name>.tls.client_cert_path`.         |
| Client Certificate Path   | `TEMPORAL_TLS_CLIENT_CERT_PATH`          | `profile.<name>.tls.client_cert_path`          | A filesystem path to the client's public TLS certificate. Alternatively, you can provide the raw PEM data using `TEMPORAL_TLS_CLIENT_CERT_DATA` or the TOML `profile.<name>.tls.client_cert_data`.                          |
| Client Key                | `TEMPORAL_TLS_CLIENT_KEY_DATA`           | `profile.<name>.tls.client_key_data`           | The raw PEM data containing the client's private TLS key. Alternatively, you can use `TEMPORAL_TLS_CLIENT_KEY_PATH` to provide a path to the key or the TOML `profile.<name>.tls.client_key_path`.                          |
| Client Key Path           | `TEMPORAL_TLS_CLIENT_KEY_PATH`           | `profile.<name>.tls.client_key_path`           | A filesystem path to the client's private TLS key. Alternatively, you can provide the raw PEM data using `TEMPORAL_TLS_CLIENT_KEY_DATA` or the TOML `profile.<name>.tls.client_key_data`.                                   |
| Server CA Cert            | `TEMPORAL_TLS_SERVER_CA_CERT_DATA`       | `profile.<name>.tls.server_ca_cert_data`       | The raw PEM data for the Certificate Authority certificate used to verify the server. Alternatively, you can use `TEMPORAL_TLS_SERVER_CA_CERT_PATH` to provide a path or the TOML `profile.<name>.tls.server_ca_cert_path`. |
| Server CA Cert Path       | `TEMPORAL_TLS_SERVER_CA_CERT_PATH`       | `profile.<name>.tls.server_ca_cert_path`       | A filesystem path to the Certificate Authority certificate. Alternatively, you can provide the raw PEM data using `TEMPORAL_TLS_SERVER_CA_CERT_DATA` or the TOML `profile.<name>.tls.server_ca_cert_data`.                  |
| TLS Server Name           | `TEMPORAL_TLS_SERVER_NAME`               | `profile.<name>.tls.server_name`               | Overrides the server name used for Server Name Indication (SNI) in the TLS handshake.                                                                                                                                       |
| Disable Host Verification | `TEMPORAL_TLS_DISABLE_HOST_VERIFICATION` | `profile.<name>.tls.disable_host_verification` | A boolean to disable server hostname verification. Use with caution. Not supported by all SDKs.                                                                                                                             |
| Codec Endpoint            | `TEMPORAL_CODEC_ENDPOINT`                | `profile.<name>.codec.endpoint`                | The endpoint for a remote Data Converter. This is not supported by all SDKs. SDKs that support this configuration don't apply it by default. Intended mostly for CLI use.                                                   |
| Codec Auth                | `TEMPORAL_CODEC_AUTH`                    | `profile.<name>.codec.auth`                    | The authorization header value for the remote data converter.                                                                                                                                                               |
| gRPC Metadata             | `TEMPORAL_GRPC_META_*`                   | `profile.<name>.grpc_meta`                     | Sets gRPC headers. The part after `_META_` becomes the header key (e.g., `_SOME_KEY` -> `some-key`).                                                                                                                        |

---

## OSS Temporal Service metrics reference

:::info OSS Temporal Service metrics

The information on this page is relevant to open source [Temporal Service deployments](/temporal-service).

See [Cloud metrics](/cloud/metrics/) for metrics emitted by [Temporal Cloud](/cloud/overview).

See [SDK metrics](/references/sdk-metrics) for metrics emitted by the [SDKs](/encyclopedia/temporal-sdks).

:::

A Temporal Service emits a range of metrics to help operators get visibility into the Temporal Service's performance and to set up alerts.

All metrics emitted by the Temporal Service are listed in [metric_defs.go](https://github.com/temporalio/temporal/blob/main/common/metrics/metric_defs.go).

For details on setting up metrics in your Temporal Service configuration, see the [Temporal Service configuration reference](/references/configuration#global).

The [dashboards repository](https://github.com/temporalio/dashboards) contains community-driven Grafana dashboard templates that can be used as a starting point for monitoring the Temporal Service and SDK metrics.
You can use these templates as references to build your own dashboards.
For any metrics that are missing in the dashboards, use [metric_defs.go](https://github.com/temporalio/temporal/blob/main/common/metrics/metric_defs.go) as a reference.

Note that, apart from these metrics emitted by the Temporal Service, you should also monitor infrastructure-specific metrics like CPU, memory, and network for all hosts that are running Temporal Service services.

## Common metrics

Temporal emits metrics for each gRPC service request.
These metrics are emitted with `type`, `operation`, and `namespace` tags, which provide visibility into Service usage and show the request rates across Services, Namespaces, and Operations.

- Use the `operation` tag in your query to get request rates, error rates, or latencies per operation.
- Use the `service_name` tag with the [service role tag values](https://github.com/temporalio/temporal/blob/bba148cf1e1642fd39fa0174423b183d5fc62d95/common/metrics/defs.go#L108) to get details for the specific service.

All common tags that you can add in your query are defined in the [metric_defs.go](https://github.com/temporalio/temporal/blob/main/common/metrics/metric_defs.go) file.

For example, to see service requests by operation on the Frontend Service, use the following:

`sum by (operation) (rate(service_requests{service_name="frontend"}[2m]))`

Note: All metrics queries in this topic are [Prometheus queries](https://prometheus.io/docs/prometheus/latest/querying/basics/).

The following list describes some metrics you can get started with.

### `service_requests`

Shows service requests received per Task Queue.
Example: Service requests by operation
`sum(rate(service_requests{operation=\"AddWorkflowTask\"}[2m]))`

### `service_latency`

Shows latencies for all Client request operations.
Usually these are the starting point to investigate which operation is experiencing high-latency issues.
Example: P95 service latency by operation for the Frontend Service
`histogram_quantile(0.95, sum(rate(service_latency_bucket{service_name="frontend"}[5m])) by (operation, le))`

### `service_error_with_type`

(Available only in v1.17.0+) Identifies errors encountered by the service.
Example: Service errors by type for the Frontend Service
`sum(rate(service_error_with_type{service_name="frontend"}[5m])) by (error_type)`

### `client_errors`

An indicator for connection issues between different Server roles.
Example: Client errors
`sum(rate(client_errors{service_name="frontend",service_role="history"}[5m]))`

In addition to these, you can define some service-specific metrics to get performance details for each service.
Start with the following list, and use [metric_defs.go](https://github.com/temporalio/temporal/blob/main/common/metrics/metric_defs.go) to define additional metrics as required.

## Matching Service metrics

### `poll_success`

Shows for Tasks that are successfully matched to a poller.
Example: `sum(rate(poll_success{}[5m]))`

### `poll_timeouts`

Shows when no Tasks are available for the poller within the poll timeout.
Example: `sum(rate(poll_timeouts{}[5m]))`

### `asyncmatch_latency`

Measures the time from creation to delivery for async matched Tasks.
The larger this latency, the longer Tasks are sitting in the queue waiting for your Workers to pick them up.
Example: `histogram_quantile(0.95, sum(rate(asyncmatch_latency_bucket{service_name="matching"}[5m])) by (operation, le))`

### `no_poller_tasks`

Emitted whenever a task is added to a task queue that has no poller, and is a counter metric.
This is usually an indicator that either the Worker or the starter programs are using the wrong Task Queue.

## History Service metrics

A History Task is an internal Task in Temporal that is created as part of a transaction to update Workflow state and is processed by the Temporal History service.
It is critical to ensure that the History Task processing system is healthy.
The following key metrics can be used to monitor the History Service health:

### `task_requests`

Emitted on every Task process request.
Example: `sum(rate(task_requests{operation=~"TransferActive.*"}[1m]))`

### `task_errors`

Emitted on every Task process error.
Example: `sum(rate(task_errors{operation=~"TransferActive.*"}[1m]))`

### `task_attempt`

Number of attempts on each Task Execution.
A Task is retried forever, and each retry increases the attempt count.
Example: `histogram_quantile(0.95, sum(rate(task_attempt_bucket{operation=~"TransferActive.*"}[1m])) by (operation, le))`

### `task_latency_processing`

Shows the processing latency per attempt.
Example: `histogram_quantile(0.95, sum(rate(task_latency_processing_bucket{operation=~"TransferActive.*",service_name="history"}[1m])) by (operation, le))`

### `task_latency`

