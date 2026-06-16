
- Ramping traffic gradually to a new Worker Deployment Version.
- Verifying a new Deployment Version with tests before sending production traffic to it.
- Instant rollback when you detect that a new Deployment Version is broken.
- Improved error rates when adopting it.

In addition, Worker Versioning introduces **Workflow Pinning**. For pinned Workflow Types, each execution runs entirely
on the Worker Deployment Version where it started. You need not worry about making breaking code changes to running,
pinned Workflows.

To use Workflow Pinning, we recommend using [rainbow deployments](#deployment-systems).

:::tip

Watch this Temporal Replay 2025 talk to learn more about Worker Versioning and see a demo.

  <iframe
    width="560"
    height="315"
    src="https://www.youtube.com/embed/rm4BlD9WXqc"
    title="YouTube video player"
    frameBorder="0"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    referrerPolicy="strict-origin-when-cross-origin"
    allowFullScreen
  ></iframe>

:::

:::note

Minimum versions:

- Go SDK version [v1.35.0](https://github.com/temporalio/sdk-go/releases/tag/v1.35.0)
- Python [v1.11](https://github.com/temporalio/sdk-python/releases/tag/1.11.0)
- Java [v1.29](https://github.com/temporalio/sdk-java/releases/tag/v1.29.0)
- Typescript [v1.12](https://github.com/temporalio/sdk-typescript/releases/tag/v1.12.0)
- .NET [v1.7.0](https://github.com/temporalio/sdk-dotnet/releases/tag/1.7.0)
- Ruby [v0.5.0](https://github.com/temporalio/sdk-ruby/releases/tag/v0.5.0)

Self-hosted users:

- Minimum Temporal CLI version [v1.4.1](https://github.com/temporalio/cli/releases/tag/v1.4.1)
- Minimum Temporal Server version: [v1.29.1](https://github.com/temporalio/temporal/releases/tag/v1.29.1)
- Minimum Temporal UI Version [v2.38.0](https://github.com/temporalio/ui/releases/tag/v2.38.0)

:::

## Getting Started with Worker Versioning {/* #definition */}

To get started with Worker Versioning, you should understand some concepts around versioning and deployments.

- A **Worker Deployment** is a deployment or service across multiple versions. In a rainbow deployment, more than two
  active Deployment Versions can run at once.
- A **Worker Deployment Version** is a version of a deployment or service. It can have multiple Workers polling on
  multiple Task Queues, but they all run the same build.
- A **Build ID**, in combination with a Worker Deployment name, identifies a single Worker Deployment Version.
- When a versioned worker polls on a task queue, that task queue becomes part of that Worker's version. That version's
  Worker Deployment controls how the task queue matches Workflow Tasks with Workers.
- Using **Workflow Pinning**, you can declare each Workflow type to have a **Versioning Behavior**, either Pinned or
  Auto-Upgrade.
  - A **Pinned** Workflow is guaranteed to complete on a single Worker Deployment Version.
  - An **Auto-Upgrade** Workflow will automatically move to a new code version as you roll it out, specifically its
    Target Worker Deployment Version (defined below). Therefore, Auto-Upgrade Workflows are not restricted to a single
    Deployment Version and need to be kept replay-safe manually, i.e. with
    [patching](/workflow-definition#workflow-versioning).
  - Both Pinned and Auto-Upgrade Workflows are guaranteed to start only on the Current or Ramping Version of their
    Worker Deployment.
  - Pinned Workflows are designed for use with rainbow deployments. See [Deployment Systems](#deployment-systems).
  - Pinned Workflows don't need to be patched, as they run on the same worker and build until they complete.
  - If you expect your Workflow to run longer than you want your Worker Deployment Versions to exist, you should mark
    your Workflow Type as Auto-Upgrade.
- Each Worker Deployment has a single [**Current Version**](/worker-versioning#versioning-definitions) which is where
  Workflows are routed to unless they were previously pinned on a different version.
- Each Worker Deployment can have a [**Ramping Version**](/worker-versioning#versioning-definitions) which is where a
  configurable percentage of Workflows are routed to unless they were previously pinned on a different version.
- For a given Workflow, its [**Target Worker Deployment Version**](/worker-versioning#versioning-definitions) is the
  version it will move to next.

## Setting up your deployment system {/* #deployment-systems */}

If you haven't already, you'll want to pick a container deployment solution for your Workers.

You also need to pick among three common deployment strategies:

- A **rolling deployment** strategy upgrades Workers in place with little control over how quickly they cut over and
  only a slow ability to roll Workers back. Rolling deploys have minimal footprint but tend to provide lower
  availability than the other strategies and are incompatible with Worker Versioning.
- A **blue-green deployment** strategy maintains two "colors," or Worker Deployment Versions simultaneously and can
  control how traffic is routed between them. This allows you to maximize your uptime with features like instant
  rollback and ramping. Worker Versioning enables the routing control that blue-green deployments need.
- A **rainbow deployment** strategy is like blue-green but with more colors, allowing Workflow Pinning. You can deploy
  new revisions of your Workflows freely while older versions drain. Using Worker Versioning, Temporal lets you know
  when all the Workflows of a given version are drained so that you can sunset it.

:::note

You also have the option to use the
[Temporal Worker Controller](/production-deployment/worker-deployments/kubernetes-controller) to automatically enable
rainbow deployments of your Workers if you're using Kubernetes.

:::

If you cannot yet support blue-green or rainbow style deployments, use [patching](/patching) as a fallback while you
work toward a versioned deployment model.

## Configuring a Worker for Versioning

You'll need to add a few additional configuration parameters to your Workers to toggle on Worker Versioning. There are
three new parameters, with different names depending on the language:

- `UseVersioning`: This enables the Versioning functionality for this Worker.
- A `Version` to identify the revision that this Worker will be allowed to execute. This is a combination of a
  deployment name and a build ID number.
- (Optional) The [Default Versioning Behavior](#definition). If unset, you'll be required to specify the behavior on
  each Workflow. Or you can default to Pinned or Auto-Upgrade.

Follow the example for your SDK below:

<SdkTabs>
<SdkTabs.Go>
```go
buildID:= mustGetEnv("MY_BUILD_ID")
w := worker.New(c, myTaskQueue, worker.Options{
  DeploymentOptions: worker.DeploymentOptions{
    UseVersioning: true,
    Version: worker.WorkerDeploymentVersion{
      DeploymentName: "llm_srv",
      BuildId:        buildID,
    },
    DefaultVersioningBehavior: workflow.VersioningBehaviorUnspecified,
  },
})
```
</SdkTabs.Go>
<SdkTabs.Java>
```java

WorkerOptions.newBuilder()
  .setDeploymentOptions(
      WorkerDeploymentOptions.newBuilder()
      .setVersion(new WorkerDeploymentVersion("llm_srv", "1.0"))
      .setUseVersioning(true)
      .setDefaultVersioningBehavior(VersioningBehavior.AUTO_UPGRADE)
      .build())
  .build();

```
</SdkTabs.Java>
<SdkTabs.Python>
```python
from temporalio.common import WorkerDeploymentVersion, VersioningBehavior
from temporalio.worker import Worker, WorkerDeploymentConfig

Worker(
    client,
    task_queue="mytaskqueue",
    workflows=workflows,
    activities=activities,
    deployment_config=WorkerDeploymentConfig(
        version=WorkerDeploymentVersion(
            deployment_name="llm_srv",
            build_id=my_env.build_id),
        use_worker_versioning=True,
        default_versioning_behavior=VersioningBehavior.UNSPECIFIED
    ),
)
```

</SdkTabs.Python>
<SdkTabs.TypeScript>

```ts
const myWorker = await Worker.create({
  workflowsPath: require.resolve('./workflows'),
  taskQueue,
  workerDeploymentOptions: {
    useWorkerVersioning: true,
    version: { buildId: '1.0', deploymentName: 'llm_srv' },
  },
  connection: nativeConnection,
});
```

</SdkTabs.TypeScript>
<SdkTabs.DotNet>

```csharp
var myWorker = new TemporalWorker(
    Client,
    new TemporalWorkerOptions(taskQueue)
    {DeploymentOptions = new(new("llm_srv", "1.0"), true)
      { DefaultVersioningBehavior = VersioningBehavior.Unspecified },
    }.AddWorkflow<MyWorkflow>());
```

</SdkTabs.DotNet>
<SdkTabs.Ruby>

```ruby
worker = Temporalio::Worker.new(
  client: client,
  task_queue: task_queue,
  workflows: [MyWorkflow],
  deployment_options: Temporalio::Worker::DeploymentOptions.new(
      version: Temporalio::WorkerDeploymentVersion.new(
          deployment_name: 'llm_srv',
          build_id: '1.0'
      ),
      use_worker_versioning: true,
      default_versioning_behavior: Temporalio::VersioningBehavior::UNSPECIFIED
  )
)
```

</SdkTabs.Ruby>
</SdkTabs>

## Choosing a Versioning Behavior {/* #choosing-behavior */}

The right versioning behavior depends on how long your Workflows run relative to your deployment frequency.

### Decision guide {/* #decision-guide */}

| Workflow Duration                        | Uses Continue-as-New? | Recommended Behavior                                     | Patching Required? |
| ---------------------------------------- | --------------------- | -------------------------------------------------------- | ------------------ |
| **Short** (completes before next deploy) | N/A                   | `PINNED`                                                 | Never              |
| **Medium** (spans multiple deploys)      | No                    | `AUTO_UPGRADE`                                           | Yes                |
| **Long** (weeks to years)                | Yes                   | `PINNED` + [upgrade on CaN](#upgrade-on-continue-as-new) | Never              |
| **Long** (weeks to years)                | No                    | `AUTO_UPGRADE` + patching                                | Yes                |

### Examples by Workflow type {/* #behavior-examples */}

| Workflow Type        | Duration     | Recommended Behavior       | Notes                               |
| -------------------- | ------------ | -------------------------- | ----------------------------------- |
| Order processing     | Minutes      | `PINNED`                   | Completes before next deploy        |
| Payment retry        | Hours        | `PINNED` or `AUTO_UPGRADE` | Depends on deploy frequency         |
| Subscription billing | Days         | `AUTO_UPGRADE`             | May span multiple deploys           |
| Customer entity      | Months-Years | `PINNED` + upgrade on CaN  | Uses Continue-as-New pattern        |
| AI agent / Chatbot   | Weeks        | `PINNED` + upgrade on CaN  | Long sleeps, uses CaN               |
| Compliance audit     | Months       | `AUTO_UPGRADE` + patching  | Cannot use CaN (needs full history) |

:::info Long-running Workflows with Continue-as-New

If your Workflow uses Continue-as-New to manage history size, you can upgrade to new Worker Deployment Versions at the
CaN boundary without patching. See [Upgrading on Continue-as-New](#upgrade-on-continue-as-new) below.

:::

### Default Versioning Behavior Considerations

If you are using blue-green deployments, you should default to Auto-Upgrade and should not use Workflow Pinning.
Otherwise, if your Worker and Workflows are new, we suggest not providing a `DefaultVersioningBehavior`.

In general, each Workflow Type should be annotated as Auto-Upgrade or Pinned. If all of your Workflows will be
short-running for the foreseeable future, you can default to Pinned.

Many users who are migrating to Worker Versioning will start by defaulting to Auto-Upgrade until they have had time to
annotate their Workflows. This default is the most similar to the legacy behavior. Once each Workflow Type is annotated,
you can remove the `DefaultVersioningBehavior`.

There is a possibility of a queue blocking limitation for new or Auto-Upgrade Workflows if there is a ramp, but one of
the Current or Ramping versions is down or doesn't have enough capacity. This leads to other versions not getting Tasks
or slowing down.

For example, you have a Current Version and a Ramping Version at 50%. If all of your Current Version Workers go down,
you would expect at least 50% of new Workflows to go to the Ramping Version. This won't happen because the Tasks for the
Current Version are blocking the queue.

:::note

Keep in mind that Child Workflows of a parent or previous Auto-Upgrade Workflow default to Auto-Upgrade behavior and not
Unspecified.

:::

You also want to make sure you understand how your Activities are going to work across different Worker Deployment
Versions. Refer to the [Worker Versioning Activity behavior docs](/worker-versioning#activity-behavior-across-versions)
for more details.

## Rolling out changes with the CLI

Next, deploy your Worker with the additional configuration parameters. Before making any Workflow revisions, you can use
the `temporal` CLI to check which of your Worker versions are currently polling:

You can view the Versions that are part of a Deployment with `temporal worker deployment describe`:

```bash
temporal worker deployment describe --name="$MY_DEPLOYMENT"
```

To activate a Deployment Version, use `temporal worker deployment set-current-version`, specifying the deployment name
and a Build ID:

```bash
temporal worker deployment set-current-version \
    --deployment-name "YourDeploymentName" \
    --build-id "YourBuildID"
```

To ramp a Deployment Version up to some percentage of your overall Worker fleet, use `set-ramping version`, with the
same parameters and a ramping percentage:

```bash
temporal worker deployment set-ramping-version \
    --deployment-name "YourDeploymentName" \
    --build-id "YourBuildID" \
    --percentage=5
```

You can verify that Workflows are cutting over to that version with `describe -w YourWorkflowID`:

```bash
temporal workflow describe -w YourWorkflowID
```

That returns the new Version that the workflow is running on:

```
Versioning Info:

  Behavior               AutoUpgrade
  Version                llm_srv.2.0
  OverrideBehavior       Unspecified
```

## Marking a Workflow Type as Pinned

You can mark a Workflow Type as pinned when you register it by adding an additional Pinned parameter. This will cause it
to remain on its original deployed version:

<SdkTabs>
<SdkTabs.Go>
```go
// w is the Worker configured as in the previous example
w.RegisterWorkflowWithOptions(HelloWorld, workflow.RegisterOptions{
	// or workflow.VersioningBehaviorAutoUpgrade
    VersioningBehavior: workflow.VersioningBehaviorPinned,
})
```
</SdkTabs.Go>
<SdkTabs.Java>
```java
@WorkflowInterface
public interface HelloWorld {
    @WorkflowMethod
    String hello();
}

public static class HelloWorldImpl implements HelloWorld {
    @Override
    @WorkflowVersioningBehavior(VersioningBehavior.PINNED)
    public String hello() {
        return "Hello, World!";
    }
}

```
</SdkTabs.Java>
<SdkTabs.Python>
```python
@workflow.defn(versioning_behavior=VersioningBehavior.PINNED)
class HelloWorld:
    @workflow.run
    async def run(self):
        return "hello world!"

```

</SdkTabs.Python>
<SdkTabs.TypeScript>

```ts
setWorkflowOptions({ versioningBehavior: 'PINNED' }, helloWorld);
export async function helloWorld(): Promise<string> {
  return 'hello world!';
}
```

</SdkTabs.TypeScript>
<SdkTabs.DotNet>

```csharp
[Workflow(VersioningBehavior = VersioningBehavior.Pinned)]
public class HelloWorld
{
    [WorkflowRun]
    public async Task<string> RunAsync()
    {
        return "hello world!";
    }
}
```

</SdkTabs.DotNet>
<SdkTabs.Ruby>

```ruby
class HelloWorld < Temporalio::Workflow::Definition
  workflow_versioning_behavior Temporalio::VersioningBehavior::PINNED

  def execute
    'hello world!'
  end
end
```

</SdkTabs.Ruby>
</SdkTabs>

## Moving a pinned Workflow

Sometimes you'll need to manually move a set of pinned Workflows off of a version that has a bug to a version with the
fix.

If you need to move a pinned Workflow to a new version, use `temporal workflow update-options`:

```bash
temporal workflow update-options \
    --workflow-id "$WORKFLOW_ID" \
    --versioning-override-behavior pinned \
    --versioning-override-deployment-name "$TARGET_DEPLOYMENT" \
    --versioning-override-build-id "$TARGET_BUILD_ID"
```

You can move several Workflows at once matching a `--query` parameter:

```bash
temporal workflow update-options \
  --query="TemporalWorkerDeploymentVersion=$TARGET_DEPLOYMENT:$BAD_BUILD_ID" \
  --versioning-override-behavior pinned \
  --versioning-override-deployment-name "$TARGET_DEPLOYMENT" \
  --versioning-override-build-id "$FIXED_BUILD_ID"
```

In this scenario, you may also need to use the other [Versioning APIs](/workflow-definition#workflow-versioning) to
patch your Workflow in the "fixed" build, so that your target Worker can handle the moved Workflows correctly. If you
made a [version-incompatible change](/workflow-definition#deterministic-constraints) to your Workflow, and you want to
roll back to an earlier version, it's not possible to patch it. Considering using
[Workflow Reset](/workflow-execution/event#reset) along with your move.

"Reset-with-Move" allows you to atomically Reset your Workflow and set a Versioning Override on the newly reset
Workflow, so when it resumes execution, all new Workflow Tasks will be executed on your new Worker.

```bash
temporal workflow reset with-workflow-update-options \
    --workflow-id "$WORKFLOW_ID" \
    --event-id "$EVENT_ID" \
    --reason "$REASON" \
    --versioning-override-behavior pinned \
    --versioning-override-deployment-name "$TARGET_DEPLOYMENT" \
    --versioning-override-build-id "$TARGET_BUILD_ID"
```

## Migrating a Workflow from Pinned to Auto-Upgrade

There may be times when you need to migrate your Workflow from Pinned to Auto-Upgrade because you configured your
Workflow Type with the wrong behavior or you've pinned a really long-running Workflow by mistake.

Pinned Workflows can block version drainage, especially when they run for a long time. You could move the Workflow to a
new build, but that would just push the problem to the next build.

In order to make this change, you need to change the versioning behavior for your Workflow from Pinned to Auto-Upgrade.
You can use `temporal workflow update-options` for this:

```bash
temporal workflow update-options \
    --workflow-id "$WORKFLOW_ID" \
    --versioning-override-behavior auto_upgrade
```

If you want to move all your Workflows of a certain type to this new configuration, you can do it with this command:

```bash
temporal workflow update-options \
    --query="WorkflowType='$WORKFLOW_TYPE'" \
    --versioning-override-behavior auto_upgrade
```

You can also filter on a certain build ID to limit the number of Workflows you apply it to:

```bash
temporal workflow update-options \
    --query="WorkflowType='$WORKFLOW_TYPE' AND TemporalWorkerDeploymentVersion='$TARGET_DEPLOYMENT:$OLD_VERSION'" \
    --versioning-override-behavior auto_upgrade
```

:::note

When you change the behavior to Auto-Upgrade, the Workflow will resume work on the Workflow's Target Version. So if the Workflow's Target Version is different from the earlier Pinned Version, you should make sure you [patch](/patching#patching) the Workflow code.

:::

## Upgrading on Continue-as-New {/* #upgrade-on-continue-as-new */}

Long-running Workflows that use [Continue-as-New](/workflow-execution/continue-as-new) can upgrade to newer Worker
Deployment Versions at Continue-as-New boundaries without requiring patching.

This pattern is ideal for:

- **Entity Workflows** that run for months or years
- **Batch processing** Workflows that checkpoint with Continue-as-New
- **AI agent Workflows** with long sleeps waiting for user input

:::note Public Preview

This feature is in Public Preview as an experimental SDK-level option.

:::

### How it works {/* #upgrade-on-can-how-it-works */}

By default, Pinned Workflows stay on their original Worker Deployment Version even when they Continue-as-New. With the
upgrade option enabled:

1. Each Workflow run remains pinned to its version (no patching needed during a run)
2. The Temporal Server tells the workflow when a new [Target Version](/worker-versioning#versioning-definitions) becomes available
3. When the Workflow performs Continue-as-New with the upgrade option, the new run starts on the [Target Version](/worker-versioning#versioning-definitions)

### Checking for new versions {/* #checking-for-new-versions */}

When a new Worker Deployment Version becomes Current or Ramping, active Workflows can detect this through
`target_worker_deployment_version_changed`:

<SdkTabs>
<SdkTabs.Go>

```go
func (w *Workflows) ContinueAsNewWithVersionUpgradeV1(
  ctx workflow.Context,
  attempt int,
) (string, error) {
  if attempt > 0 {
    return "v1.0", nil
  }

	// Check GetTargetWorkerDeploymentVersionChanged periodically.
	// GetTargetWorkerDeploymentVersionChanged is refreshed after each WFT completes.
  for {
	// Trigger a WFT when timer expires, thereby refreshing the GetTargetWorkerDeploymentVersionChanged flag.
	// Since this is just a test workflow, we aren't doing any real work. In a real workflow regularly
	// doing non-sleep workflow tasks, you would not need to artificially trigger a WFT to refresh the
	// GetTargetWorkerDeploymentVersionChanged flag. You could choose to check the field periodically, or you
	// might want to check before accepting updates, starting activities, or starting child workflows.
	err := workflow.Sleep(ctx, 10*time.Millisecond)
	if err != nil {
	  return "", err
	}
	info := workflow.GetInfo(ctx)
	if info.GetTargetWorkerDeploymentVersionChanged() {
	  return "", workflow.NewContinueAsNewErrorWithOptions(
		ctx,
		workflow.ContinueAsNewErrorOptions{
		  // Pass InitialVersioningBehavior=workflow.ContinueAsNewVersioningBehaviorAutoUpgrade
		  // to make the new run start with AutoUpgrade behavior and use the Target Version of
		  // its Worker Deployment.
		  InitialVersioningBehavior: workflow.ContinueAsNewVersioningBehaviorAutoUpgrade,
		},
		"ContinueAsNewWithVersionUpgrade",
		attempt+1,
	  )
	}
  }
}

func (w *Workflows) ContinueAsNewWithVersionUpgradeV2(
  ctx workflow.Context,
  attempt int,
) (string, error) {
  return "v2.0", nil
}
```

</SdkTabs.Go>
<SdkTabs.Java>

```java
public class ContinueAsNewWithVersionUpgradeImpl implements ContinueAsNewWithVersionUpgrade {
  @Override
  public String run(int attempt) {
    if (attempt > 0) {
      return "v1.0";
    }

    // isTargetWorkerDeploymentVersionChanged is refreshed after each Workflow Task completes.
    // In a Workflow that regularly does non-sleep Workflow Tasks you wouldn't need an artificial
    // timer; you could check the flag periodically, or before accepting Updates, starting
    // Activities, or starting child Workflows.
    while (true) {
      Workflow.sleep(Duration.ofMillis(10));
      if (Workflow.getInfo().isTargetWorkerDeploymentVersionChanged()) {
        // Set InitialVersioningBehavior to AUTO_UPGRADE so the new run starts with AutoUpgrade
        // behavior and uses the Target Version of its Worker Deployment.
        Workflow.continueAsNew(
            ContinueAsNewOptions.newBuilder()
                .setInitialVersioningBehavior(InitialVersioningBehavior.AUTO_UPGRADE)
                .build(),
            attempt + 1);
      }
    }
  }
}
```

</SdkTabs.Java>
<SdkTabs.Python>

```python
@workflow.defn
class ContinueAsNewWithVersionUpgrade:
    @workflow.run
    async def run(self, attempt: int) -> str:
        if attempt > 0:
            return "v1.0"

        # is_target_worker_deployment_version_changed() is refreshed after each Workflow Task
        # completes. In a Workflow that regularly does non-sleep Workflow Tasks you wouldn't need
        # an artificial timer; you could check the flag periodically, or before accepting Updates,
        # starting Activities, or starting child Workflows.
        while True:
            await workflow.sleep(timedelta(milliseconds=10))
            if workflow.info().is_target_worker_deployment_version_changed():
                # Set initial_versioning_behavior to AUTO_UPGRADE so the new run starts with
                # AutoUpgrade behavior and uses the Target Version of its Worker Deployment.
                workflow.continue_as_new(
                    attempt + 1,
                    initial_versioning_behavior=ContinueAsNewVersioningBehavior.AUTO_UPGRADE,
                )
```

</SdkTabs.Python>
<SdkTabs.TypeScript>

```ts

export async function continueAsNewWithVersionUpgrade(attempt: number): Promise<string> {
  if (attempt > 0) {
    return 'v1.0';
  }

  // targetWorkerDeploymentVersionChanged is refreshed after each Workflow Task completes.
  // In a Workflow that regularly does non-sleep Workflow Tasks you wouldn't need an artificial
  // timer; you could check the flag periodically, or before accepting Updates, starting
  // Activities, or starting child Workflows.
  for (;;) {
    await wf.sleep('10ms');
    if (wf.workflowInfo().targetWorkerDeploymentVersionChanged) {
      // Set initialVersioningBehavior to AUTO_UPGRADE so the new run starts with AutoUpgrade
      // behavior and uses the Target Version of its Worker Deployment.
