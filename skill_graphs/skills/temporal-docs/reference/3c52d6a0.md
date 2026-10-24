# Quickstart

Configure your local development environment to get started developing with Temporal.

<SetupSteps>
<SetupStep code={
  <>
    <CodeSnippet language="bash">
    go version
    </CodeSnippet>
    <CodeSnippet language="bash">
    go version go1.18.1 darwin/amd64
    </CodeSnippet>
  </>
}>

## Install Go

Make sure you have Go installed. These tutorials were produced using Go 1.18. Check your version of Go with the
following command:

This will return your installed Go version.

</SetupStep>

<SetupStep code={
<>
<CodeSnippet language="bash">
mkdir goproject
</CodeSnippet>
<CodeSnippet language="bash">
cd goproject
</CodeSnippet>
<CodeSnippet language="bash">
go mod init my-org/greeting
</CodeSnippet>
<CodeSnippet language="bash">
go get go.temporal.io/sdk
</CodeSnippet>
<CodeSnippet language="bash">
go get go.temporal.io/sdk/client
</CodeSnippet>
<CodeSnippet language="bash">
go mod tidy
</CodeSnippet>
</>
}>

## Install the Temporal Go SDK

If you are creating a new project using the Temporal Go SDK, you can start by creating a new directory.

Next, switch to the new directory.

Then, initialize a Go project in that directory.

Finally, install the Temporal SDK with `go get`.

</SetupStep>

<SetupStep code={
<>
<Tabs>
<TabItem value="macos" label="macOS" default>

        Install the Temporal CLI using Homebrew:
        <CodeSnippet language="bash">
        brew install temporal
        </CodeSnippet>
      </TabItem>

      <TabItem value="windows" label="Windows">
        Download the Temporal CLI archive for your architecture:

          Windows amd64
          Windows arm64

        Extract it and add <code>temporal.exe</code> to your PATH.
      </TabItem>

      <TabItem value="linux" label="Linux">
        Download the Temporal CLI for your architecture:

          Linux amd64
          Linux arm64

        Extract the archive and move the <code>temporal</code> binary into your PATH, for example:
        <CodeSnippet language="bash">
        sudo mv temporal /usr/local/bin
        </CodeSnippet>
      </TabItem>
    </Tabs>

</>
}>

## Install Temporal CLI and start the development server

The fastest way to get a development version of the Temporal Service running on your local machine is to use
[Temporal CLI](https://docs.temporal.io/cli).

Choose your operating system to install Temporal CLI:

</SetupStep>

<SetupStep code={
<>

After installing, open a new Terminal window and start the development server:
<CodeSnippet language="bash">temporal server start-dev</CodeSnippet>

Change the Web UI port
The Temporal Web UI may be on a different port in some examples or tutorials. To change the port for the Web UI, use the <code>--ui-port</code> option when starting the server:
<CodeSnippet language="bash">
temporal server start-dev --ui-port 8080
</CodeSnippet>
The Temporal Web UI will now be available at http://localhost:8080.

</>
}>

## Start the development server

Once you've installed Temporal CLI and added it to your PATH, open a new Terminal window and run the following command.

This command starts a local Temporal Service. It starts the Web UI, creates the default Namespace, and uses an in-memory
database.

The Temporal Service will be available on localhost:7233. The Temporal Web UI will be available at
http://localhost:8233.

Leave the local Temporal Service running as you work through tutorials and other projects. You can stop the Temporal
Service at any time by pressing CTRL+C.

Once you have everything installed, you're ready to build apps with Temporal on your local machine.

</SetupStep>
</SetupSteps>

## Run Hello World: Test Your Installation

Now let's verify your setup is working by creating and running a complete Temporal application with both a Workflow and
Activity.

This test will confirm that:

- The Temporal Go SDK is properly installed
- Your local Temporal Service is running
- You can successfully create and execute Workflows and Activities
- The communication between components is functioning correctly

### 1. Create the Activity

An Activity is a normal function or method that executes a single, well-defined action (either short- or long-running)
that is typically prone to failure. Examples include any action that interacts with the outside world, such as sending
emails, making network requests, writing to a database, or calling an API. If an Activity fails, Temporal automatically
retries it based on your configuration.

Create an Activity file (activity.go):

```go
package greeting

	"context"
	"fmt"
)

func Greet(ctx context.Context, name string) (string, error) {
	return fmt.Sprintf("Hello %s", name), nil
}
```

### 2. Create the Workflow

Workflows orchestrate Activities and contain the application logic. Temporal Workflows are resilient. They can run—and
keep running—for years, even if the underlying infrastructure fails. If the application itself crashes, Temporal will
automatically recreate its pre-failure state so it can continue right where it left off.

Create a Workflow file (workflow.go):

```go
package greeting

	"time"

	"go.temporal.io/sdk/workflow"
)

func SayHelloWorkflow(ctx workflow.Context, name string) (string, error) {
	ao := workflow.ActivityOptions{
		StartToCloseTimeout: time.Second * 10,
	}
	ctx = workflow.WithActivityOptions(ctx, ao)

	var result string
	err := workflow.ExecuteActivity(ctx, Greet, name).Get(ctx, &result)
	if err != nil {
		return "", err
	}

	return result, nil
}

```

### 3. Create and Run the Worker

With your Activity and Workflow defined, you need a Worker to execute them. A Worker polls a Task Queue, that you
configure it to poll, looking for work to do. Once the Worker dequeues a Workflow or Activity task from the Task Queue,
it then executes that task.

Workers are a crucial part of your Temporal application as they're what actually execute the tasks defined in your
Workflows and Activities. For more information on Workers, see
[Understanding Temporal](/evaluate/understanding-temporal#workers) and a [deep dive into Workers](/workers).

Create a Worker file (worker/main.go):

```go
package main

	"log"

	"my-org/greeting"

	"go.temporal.io/sdk/client"
	"go.temporal.io/sdk/worker"
)

func main() {
	c, err := client.Dial(client.Options{})
	if err != nil {
		log.Fatalln("Unable to create client", err)
	}
	defer c.Close()

	w := worker.New(c, "my-task-queue", worker.Options{})

	w.RegisterWorkflow(greeting.SayHelloWorkflow)
	w.RegisterActivity(greeting.Greet)

	err = w.Run(worker.InterruptCh())
	if err != nil {
		log.Fatalln("Unable to start worker", err)
	}
}
```

Run the Worker:

```bash
go run worker/main.go
```

### 4. Execute the Workflow

Now that your Worker is running, it's time to start a Workflow Execution.

Create a separate file called start/main.go:

```go
package main

	"context"
	"log"
	"os"

	greeting "my-org/greeting"

	"go.temporal.io/sdk/client"
)

func main() {
	c, err := client.Dial(client.Options{})
	if err != nil {
		log.Fatalln("Unable to create client", err)
	}
	defer c.Close()

	options := client.StartWorkflowOptions{
		ID:        "greeting-workflow",
		TaskQueue: "my-task-queue",
	}

	we, err := c.ExecuteWorkflow(context.Background(), options, greeting.SayHelloWorkflow, os.Args[1])
	if err != nil {
		log.Fatalln("Unable to execute workflow", err)
	}
	log.Println("Started workflow", "WorkflowID", we.GetID(), "RunID", we.GetRunID())

	var result string
	err = we.Get(context.Background(), &result)
	if err != nil {
		log.Fatalln("Unable get workflow result", err)
	}
	log.Println("Workflow result:", result)
}
```

Then run:

```bash
go run start/main.go Temporal
```

### Verify Success

If everything is working correctly, you should see:

- Worker processing the workflow and activity
- Output: `Workflow result: Hello Temporal`
- Workflow Execution details in the [Temporal Web UI](http://localhost:8233)

<CallToAction href="https://learn.temporal.io/getting_started/go/first_program_in_go/">
  Run your first Temporal Application
  Create a basic Workflow and run it with the Temporal Go SDK
</CallToAction>

<CallToAction href="https://learn.temporal.io/courses/">
  Take a Temporal 101 course
  Learn Temporal concepts and build your first application with a guided course
</CallToAction>

---

## Worker Versioning (Legacy) - Go SDK

## How to use Worker Versioning in Go (Deprecated) {/* #worker-versioning */}

:::caution

This section is for a deprecated Worker Versioning API. Please redirect your attention to [Worker Versioning](/production-deployment/worker-deployments/worker-versioning).

See the [Pre-release README](https://github.com/temporalio/temporal/blob/main/docs/worker-versioning.md) for more information.

:::

A Build ID corresponds to a deployment. If you don't already have one, we recommend a hash of the code--such as a Git SHA--combined with a human-readable timestamp.
To use Worker Versioning, you need to pass a Build ID to your Go Worker and opt in to Worker Versioning.

### Assign a Build ID to your Worker and opt in to Worker Versioning

You should understand assignment rules before completing this step.
See the [Worker Versioning Pre-release README](https://github.com/temporalio/temporal/blob/main/docs/worker-versioning.md) for more information.

To enable Worker Versioning for your Worker, assign the Build ID--perhaps from an environment variable--and turn it on.

```go
// ...
workerOptions := worker.Options{
   BuildID: buildID,
   UseBuildIDForVersioning: true,
// ...
}
w := worker.New(c, "your_task_queue_name", workerOptions)
// ...
```

:::warning

Importantly, when you start this Worker, it won't receive any tasks until you set up assignment rules.

:::

### Specify versions for Activities, Child Workflows, and Continue-as-New Workflows

By default, Activities, Child Workflows, and Continue-as-New Workflows are run on the build of the Workflow that created them if they are also configured to run on the same Task Queue.
When configured to run on a separate Task Queue, they will default to using the current assignment rules.

If you want to override this behavior, you can specify your intent via the `VersioningIntent` field on the appropriate options struct.

For example, if you want an Activity to use the latest assignment rules rather than inheriting from its parent:

```go
// ...
ao := workflow.ActivityOptions{
    VersioningIntent: VersioningIntentUseAssignmentRules,
    // ...other options
}
activityCtx := workflow.WithActivityOptions(ctx, ao)
var yourActivityResult YourActivityResultType
err := workflow.ExecuteActivity(ctx, YourActivityDefinition, yourActivityParam).Get(ctx, &yourActivityResult)
// ...
```

#### Specifying versions for Continue-As-New

When using the Continue-As-New feature, use the `WithWorkflowVersioningIntent` context modifier:

```go
ctx = workflow.WithWorkflowVersioningIntent(ctx, temporal.VersioningIntentUseAssignmentRules)
err := workflow.NewContinueAsNewError(ctx, "WorkflowName")
```

### Tell the Task Queue about your Worker's Build ID (Deprecated)

:::caution

This section is for a deprecated Worker Versioning API. Please redirect your attention to [Worker Versioning](/production-deployment/worker-deployments/worker-versioning).

:::

Now you can use the SDK (or the Temporal CLI) to tell the Task Queue about your Worker's Build ID.
You might want to do this as part of your CI deployment process.

```go
// ...
err := client.UpdateWorkerBuildIdCompatibility(ctx, &client.UpdateWorkerBuildIdCompatibilityOptions{
   TaskQueue: "your_task_queue_name",
   Operation: &client.BuildIDOpAddNewIDInNewDefaultSet{
      BuildID: "deadbeef",
   },
})
```

This code adds the `deadbeef` Build ID to the Task Queue as the sole version in a new version set, which becomes the default for the queue.
New Workflows execute on Workers with this Build ID, and existing ones will continue to process by appropriately compatible Workers.

If, instead, you want to add the Build ID to an existing compatible set, you can do this:

```go
// ...
err := client.UpdateWorkerBuildIdCompatibility(ctx, &client.UpdateWorkerBuildIdCompatibilityOptions{
   TaskQueue: "your_task_queue_name",
   Operation: &client.BuildIDOpAddNewCompatibleVersion{
      BuildID:                   "deadbeef",
      ExistingCompatibleBuildId: "some-existing-build-id",
   },
})
```

This code adds `deadbeef` to the existing compatible set containing `some-existing-build-id` and marks it as the new default Build ID for that set.

You can also promote an existing Build ID in a set to be the default for that set:

```go
// ...
err := client.UpdateWorkerBuildIdCompatibility(ctx, &client.UpdateWorkerBuildIdCompatibilityOptions{
   TaskQueue: "your_task_queue_name",
   Operation: &client.BuildIDPromoteIDWithinSet{
      BuildID: "some-existing-build-id",
   },
})
```

---

## Workers - Go SDK

![Go SDK Banner](/img/assets/banner-go-temporal.png)

## Workers

- [Run a Worker](/develop/go/workers/run-worker-process)
- [Sessions](/develop/go/workers/sessions)
- [Serverless Workers](/develop/go/workers/serverless-workers)

---

## Run a Worker - Go SDK

This page covers long-lived Workers that you host and run as persistent processes.
For Workers that run on serverless compute like AWS Lambda, see [Serverless Workers](/develop/go/workers/serverless-workers).

## Create and run a Worker {/* #develop-worker */}

Create a [`Worker`](https://pkg.go.dev/go.temporal.io/sdk/worker#Worker) by calling [`worker.New()`](https://pkg.go.dev/go.temporal.io/sdk/worker#New) and passing:

1. A Temporal Client.
2. The name of the Task Queue to poll.
3. A [`worker.Options`](https://pkg.go.dev/go.temporal.io/sdk/internal#WorkerOptions) struct (can be empty for defaults).

Register your Workflow and Activity types, then call `Run()` to start polling. The Worker process is a long-running process that blocks while polling for tasks.
Run it in a separate terminal from your starter code or other application logic.

```go
package main

    "log"

    "go.temporal.io/sdk/client"
    "go.temporal.io/sdk/worker"
)

func main() {
    c, err := client.Dial(client.Options{})
    if err != nil {
        log.Fatalln("Unable to create client", err)
    }
    defer c.Close()

    w := worker.New(c, "my-task-queue", worker.Options{})
    w.RegisterWorkflow(MyWorkflow)
    w.RegisterActivity(MyActivity)

    err = w.Run(worker.InterruptCh())
    if err != nil {
        log.Fatalln("Unable to start Worker", err)
    }
}
```

`Run()` accepts an interrupt channel so the Worker shuts down on `SIGINT` or `SIGTERM`.
You can also call `Start()` and `Stop()` separately for more control over the lifecycle.

:::tip

If you have [`gow`](https://github.com/mitranim/gow) installed, the Worker automatically reloads when you update the file:

```bash
go install github.com/mitranim/gow@latest
gow run worker/main.go
```

:::

## Connect to Temporal Cloud {/* #connect-to-temporal-cloud */}

To run a Worker against Temporal Cloud, configure the client connection with your Namespace address and authentication credentials.
See [Connect to Temporal Cloud](/develop/go/client/temporal-client#connect-to-temporal-cloud) for setup instructions.

## Register Workflows and Activities {/* #register-types */}

All Workers listening to the same Task Queue must be registered to handle the same Workflow Types and Activity Types.
If a Worker polls a Task for a type it does not know about, the Task fails. The Workflow Execution itself does not fail.

Use `RegisterWorkflow()` and `RegisterActivity()` to register types.
To register an Activity struct with multiple methods, pass the struct. The Worker gets access to all exported methods.

```go
w.RegisterWorkflow(WorkflowA)
w.RegisterWorkflow(WorkflowB)
w.RegisterActivity(&MyActivities{})
```

To customize the registered name or other options, use `RegisterWorkflowWithOptions()` or `RegisterActivityWithOptions()`.
See [`workflow.RegisterOptions`](https://pkg.go.dev/go.temporal.io/sdk/workflow#RegisterOptions) and [`activity.RegisterOptions`](https://pkg.go.dev/go.temporal.io/sdk/activity#RegisterOptions).

## Worker options {/* #worker-options */}

Pass a [`worker.Options`](https://pkg.go.dev/go.temporal.io/sdk/internal#WorkerOptions) struct to `worker.New()` to configure concurrency limits, pollers, timeouts, and other Worker behavior.
An empty struct uses defaults that work for most cases.

For the full list of options and their defaults, see the [Go SDK reference](https://pkg.go.dev/go.temporal.io/sdk@v1.42.0/internal#WorkerOptions).

---

## Serverless Workers on AWS Lambda - Go SDK

<ReleaseNoteHeader featureName="serverlessWorkers">
    To request access during Pre-release, create a [support ticket](/cloud/support#support-ticket) or contact your account team.
    APIs are experimental and may be subject to backwards-incompatible changes.
    [Sign up for updates](https://temporal.io/pages/serverless-workers-updates) to be notified when Serverless Workers reach Public Preview.
</ReleaseNoteHeader>

The `lambdaworker` package lets you run a Temporal Serverless Worker on AWS Lambda.
Deploy your Worker code as a Lambda function, and Temporal Cloud invokes it when Tasks arrive.
Each invocation starts a Worker, polls for Tasks, then gracefully shuts down before a configurable invocation deadline.
You register Workflows and Activities the same way you would with a standard Worker.

For a full end-to-end deployment guide covering AWS IAM setup, compute configuration, and verification, see [Deploy a Serverless Worker](/production-deployment/worker-deployments/serverless-workers).

## Create and run a Worker in Lambda {/* #create-and-run */}

Use the `RunWorker` function to start a Lambda-based Worker.
Pass a `WorkerDeploymentVersion` and a callback that registers your Workflows and Activities.

<!--SNIPSTART go-lambda-worker {"selectedLines": ["1-6", "8-18", "22-30"]}-->
[lambda-worker/worker/main.go](https://github.com/temporalio/samples-go/blob/main/lambda-worker/worker/main.go)
```go
package main

	greeting "github.com/temporalio/samples-go/lambda-worker/greeting"

	lambdaworker "go.temporal.io/sdk/contrib/aws/lambdaworker"
// ...
	"go.temporal.io/sdk/worker"
	"go.temporal.io/sdk/workflow"
)

func main() {
	lambdaworker.RunWorker(worker.WorkerDeploymentVersion{
		DeploymentName: "my-app",
		BuildID:        "build-1",
	}, func(opts *lambdaworker.Options) error {
		opts.TaskQueue = "serverless-task-queue-1"

// ...

		opts.RegisterWorkflowWithOptions(greeting.SampleWorkflow, workflow.RegisterOptions{
			VersioningBehavior: workflow.VersioningBehaviorPinned,
		})
		opts.RegisterActivity(greeting.HelloActivity)

		return nil
	})
}
```
<!--SNIPEND-->

The `WorkerDeploymentVersion` is required.
Worker Deployment Versioning is always enabled for Serverless Workers.
Each Workflow must have a [versioning behavior](/worker-versioning#versioning-behaviors), either `AutoUpgrade` or `Pinned`.
Set it per-Workflow at registration time, or set a worker-level default with `DefaultVersioningBehavior` in `DeploymentOptions`.

The `Options` callback gives you access to the same registration methods you use with a traditional Worker: `RegisterWorkflow`, `RegisterWorkflowWithOptions`, `RegisterActivity`, `RegisterActivityWithOptions`, and `RegisterNexusService`.

## Configure the Temporal connection {/* #configure-connection */}

The `lambdaworker` package automatically loads Temporal client configuration from a TOML config file and environment variables. Refer to [Environment Configuration](/develop/environment-configuration) for more details.

The config file is resolved in order:

1. `TEMPORAL_CONFIG_FILE` environment variable, if set.
2. `temporal.toml` in `$LAMBDA_TASK_ROOT` (typically `/var/task`).
3. `temporal.toml` in the current working directory.

The file is optional. If absent, only environment variables are used.

Encrypt sensitive values like TLS keys or API keys. Refer to [AWS documentation](https://docs.aws.amazon.com/lambda/latest/dg/configuration-envvars-encryption.html) for options.

## Adjust Worker defaults for Lambda {/* #lambda-tuned-defaults */}

The `lambdaworker` package applies conservative defaults suited to short-lived Lambda invocations.
These differ from standard Worker defaults to avoid overcommitting resources in a constrained environment.
Except for `ShutdownDeadlineBuffer`, these are the same [`worker.Options`](https://pkg.go.dev/go.temporal.io/sdk@v1.42.0/internal#WorkerOptions) available to any Temporal Worker, just with lower values for Lambda's constrained environment.

| Setting | Lambda default |
|---|---|
| `MaxConcurrentActivityExecutionSize` | 2 |
| `MaxConcurrentWorkflowTaskExecutionSize` | 10 |
| `MaxConcurrentLocalActivityExecutionSize` | 2 |
| `MaxConcurrentNexusTaskExecutionSize` | 5 |
| `MaxConcurrentActivityTaskPollers` | 1 |
| `MaxConcurrentWorkflowTaskPollers` | 2 |
| `MaxConcurrentNexusTaskPollers` | 1 |
| `WorkerStopTimeout` | 5 seconds |
| `DisableEagerActivities` | Always true |
| Sticky cache size | 100 |
| `ShutdownDeadlineBuffer` | 7 seconds |

`DisableEagerActivities` is always true and cannot be overridden.
Eager Activities require a persistent connection, which Lambda invocations don't maintain.

`ShutdownDeadlineBuffer` is specific to the `lambdaworker` package.
It controls how much time before the Lambda deadline the Worker begins its graceful shutdown.
The default is `WorkerStopTimeout` + 2 seconds.

If your Worker handles long-running Activities, increase `WorkerStopTimeout`, `ShutdownDeadlineBuffer`, and the Lambda invocation deadline (`--timeout`) together.
For guidance on how these values relate, see [Tuning for long-running Activities](/serverless-workers#tuning-for-long-running-activities).

## Add observability with OpenTelemetry {/* #add-observability */}

The `lambdaworker/otel` sub-package provides OpenTelemetry integration with defaults configured for the [AWS Distro for OpenTelemetry (ADOT)](https://aws-otel.github.io/docs/getting-started/lambda) Lambda layer.
With this enabled, the Worker emits SDK metrics and distributed traces for Workflow and Activity executions.
The ADOT Lambda layer collects this telemetry and can forward traces to AWS X-Ray and metrics to Amazon CloudWatch.

The underlying metrics and traces are the same ones the Go SDK emits in any environment.
For general observability concepts and the full list of available metrics, see [Observability - Go SDK](/develop/go/platform/observability) and the [SDK metrics reference](/references/sdk-metrics).

<!--SNIPSTART go-lambda-worker-->
[lambda-worker/worker/main.go](https://github.com/temporalio/samples-go/blob/main/lambda-worker/worker/main.go)
```go
package main

	greeting "github.com/temporalio/samples-go/lambda-worker/greeting"

	lambdaworker "go.temporal.io/sdk/contrib/aws/lambdaworker"
	otel "go.temporal.io/sdk/contrib/aws/lambdaworker/otel"
	"go.temporal.io/sdk/worker"
	"go.temporal.io/sdk/workflow"
)

func main() {
	lambdaworker.RunWorker(worker.WorkerDeploymentVersion{
		DeploymentName: "my-app",
		BuildID:        "build-1",
	}, func(opts *lambdaworker.Options) error {
		opts.TaskQueue = "serverless-task-queue-1"

		if err := otel.ApplyDefaults(opts, &opts.ClientOptions, otel.Options{}); err != nil {
			return err
		}

		opts.RegisterWorkflowWithOptions(greeting.SampleWorkflow, workflow.RegisterOptions{
			VersioningBehavior: workflow.VersioningBehaviorPinned,
		})
		opts.RegisterActivity(greeting.HelloActivity)

		return nil
	})
}
```
<!--SNIPEND-->

`ApplyDefaults` configures both metrics and tracing.
By default, telemetry is sent to `localhost:4317`, which is the ADOT Lambda layer's default collector endpoint.

To collect this telemetry, attach the [ADOT Collector layer](https://aws-otel.github.io/docs/getting-started/lambda) to your Lambda function.
The layer runs a collector sidecar that receives telemetry on `localhost:4317` and forwards traces to X-Ray and metrics to CloudWatch.
Go does not need a language-specific ADOT layer because the OTel SDK is compiled into the binary.

The default Collector configuration does not route OpenTelemetry Protocol (OTLP) data to the traces pipeline.
You must provide a custom Collector configuration that wires the OTLP receiver to both the traces and metrics pipelines.
Bundle the following `otel-collector-config.yaml` in your Lambda deployment package:

<!--SNIPSTART go-lambda-worker-otel-collector-config-->
[lambda-worker/otel-collector-config.yaml](https://github.com/temporalio/samples-go/blob/main/lambda-worker/otel-collector-config.yaml)
```yaml
receivers:
    otlp:
        protocols:
            grpc:
                endpoint: "localhost:4317"
            http:
                endpoint: "localhost:4318"

exporters:
    debug:
    awsxray:
        region: us-west-2
    awsemf:
        # AWS EMF exporter for metrics
        # These are example configurations
        namespace: TemporalWorkerMetrics
        log_group_name: /aws/lambda/<your-function-name>
        region: us-west-2
        dimension_rollup_option: NoDimensionRollup
        resource_to_telemetry_conversion:
            enabled: true

service:
    pipelines:
        traces:
            receivers: [otlp]
            exporters: [awsxray, debug]
        metrics:
            receivers: [otlp]
            exporters: [awsemf]
    telemetry:
        logs:
            level: debug
        metrics:
            address: localhost:8888
```
<!--SNIPEND-->

Set the following environment variable on the Lambda function to point the Collector at the bundled config:

- `OPENTELEMETRY_COLLECTOR_CONFIG_URI=/var/task/otel-collector-config.yaml`
