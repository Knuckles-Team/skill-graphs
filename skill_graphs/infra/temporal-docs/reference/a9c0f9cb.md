
```
cd caller
go run ./starter \
  -target-host localhost:7233 \
  -namespace my-caller-namespace
```

This will result in:

```
2024/10/04 19:57:40 Workflow result: Nexus Echo 👋
2024/10/04 19:57:40 Started workflow WorkflowID nexus_hello_caller_workflow_20240723195740 RunID c9789128-2fcd-4083-829d-95e43279f6d7
2024/10/04 19:57:40 Workflow result: ¡Hola! Nexus 👋
```

### Canceling a Nexus Operation {/* #canceling-a-nexus-operation */}

To cancel a Nexus Operation from within a Workflow, create a Go context using the `workflow.WithCancel` API.
This returns a new context and a function that, when called, cancels the context and any SDK method that was passed this context.
The future returned by `NexusClient.ExecuteOperation` is resolved when the operation finishes, whether it succeeds, fails, times out, or is canceled.

Only asynchronous operations can be canceled in Nexus, as cancelation is sent using an operation token.
The Workflow or other resources backing the operation may choose to ignore the cancelation request.
If ignored, the operation may enter a terminal state.

Once the caller Workflow completes, the caller's Nexus Machinery will not make any further attempts to cancel operations that are still running.
It's okay to leave operations running in some use cases.
To ensure cancelations are delivered, wait for all pending operations to finish before exiting the Workflow.

See the [Nexus cancelation sample](https://github.com/temporalio/samples-go/tree/main/nexus-cancelation) for reference.

## Make Nexus calls across Namespaces in Temporal Cloud {/* #nexus-calls-across-namespaces-temporal-cloud */}

This section assumes you are already familiar with [how to connect a Worker to Temporal Cloud](/develop/go/client/temporal-client#connect-to-temporal-cloud).
The same [source code](https://github.com/temporalio/samples-go/tree/main/nexus) is used in this section, but the `tcld` CLI will be used to create Namespaces and the Nexus Endpoint, and mTLS client certificates will be used to securely connect the caller and handler Workers to their respective Temporal Cloud Namespaces.

### Install the latest `tcld` CLI and generate certificates

To install the latest version of the `tcld` CLI, run the following command (on MacOS):

```
brew install temporalio/brew/tcld
```

If you don't already have certificates, you can generate them for mTLS Worker authentication using the command below:

```
tcld gen ca --org $YOUR_ORG_NAME --validity-period 1y --ca-cert ca.pem --ca-key ca.key
```

These certificates will be valid for one year.

### Create caller and handler Namespaces

Before deploying to Temporal Cloud, ensure that the appropriate Namespaces are created for both the caller and handler.
If you already have these Namespaces, you don't need to do this.

```
tcld login

tcld namespace create \
  --namespace <your-caller-namespace> \
  --cloud-provider aws \
  --region us-west-2 \
  --ca-certificate-file 'path/to/your/ca.pem' \
  --retention-days 1

tcld namespace create \
  --namespace <your-target-namespace> \
  --cloud-provider aws \
  --region us-west-2 \
  --ca-certificate-file 'path/to/your/ca.pem' \
  --retention-days 1
```

Alternatively, you can create Namespaces through the UI: [https://cloud.temporal.io/Namespaces](https://cloud.temporal.io/Namespaces).

### Create a Nexus Endpoint to route requests from caller to handler

To create a Nexus Endpoint you must have a Developer account role or higher, and have NamespaceAdmin permission on the `--target-namespace`.

```
tcld nexus endpoint create \
  --name <my-nexus-endpoint-name> \
  --target-task-queue my-handler-task-queue \
  --target-namespace <my-target-namespace.account> \
  --description-file description.md
```

Alternatively, you can create a Nexus Endpoint through the UI: [https://cloud.temporal.io/nexus](https://cloud.temporal.io/nexus).

### Run Workers Connected to Temporal Cloud with TLS certificates

Run the handler Worker:

```
cd handler

go run ./worker \
  -target-host <your-target-namespace.account>.tmprl.cloud:7233 \
  -namespace <your-target-namespace.account> \
  -client-cert 'path/to/your/ca.pem' \
  -client-key 'path/to/your/ca.key'
```

Run the caller Worker:

```
cd caller

go run ./worker \
  -target-host <your-caller-namespace.account>.tmprl.cloud:7233 \
  -namespace <your-caller-namespace.account> \
  -client-cert 'path/to/your/ca.pem' \
  -client-key 'path/to/your/ca.key'
```

### Start a caller Workflow

```
cd caller

go run ./starter \
  -target-host <your-caller-namespace.account>.tmprl.cloud:7233 \
  -namespace <your-caller-namespace.account> \
  -client-cert 'path/to/your/ca.pem' \
  -client-key 'path/to/your/ca.key'
```

This will result in:

```
2024/10/04 19:57:40 Workflow result: Nexus Echo 👋
2024/10/04 19:57:40 Workflow result: ¡Hola! Nexus 👋
```

### Run Workers Connected to Temporal Cloud with API keys

[View the source code](https://github.com/temporalio/samples-go/tree/main/nexus) in the context of the rest of the application code.

Run the handler Worker:

```
cd handler

go run ./worker \
  -target-host <region>.<cloud_provider>.api.temporal.io:7233 \
  -namespace <your-target-namespace.account> \
  -api-key <your-api-key>
```

Run the caller Worker:

```
cd caller

go run ./worker \
  -target-host <region>.<cloud_provider>.api.temporal.io:7233 \
  -namespace <your-caller-namespace.account> \
  -api-key <your-api-key>
```

### Start a caller Workflow

```
cd caller

go run ./starter \
  -target-host <region>.<cloud_provider>.api.temporal.io:7233 \
  -namespace <your-caller-namespace.account> \
  -api-key <your-api-key>
```

This will result in:

```
2024/10/04 19:57:40 Workflow result: Nexus Echo 👋
2024/10/04 19:57:40 Workflow result: ¡Hola! Nexus 👋
```

## Observability

### Web UI

A synchronous Nexus Operation will surface in the caller Workflow as follows, with just `NexusOperationScheduled` and `NexusOperationCompleted` events in the caller's Event history:

<CaptionedImage
    src="/img/cloud/nexus/go-sdk-observability-sync.png"
    title="Observability Sync"
/>

An asynchronous Nexus Operation will surface in the caller Workflow as follows, with `NexusOperationScheduled`, `NexusOperationStarted`, and `NexusOperationCompleted`, in the caller's Event history:

<CaptionedImage
    src="/img/cloud/nexus/go-sdk-observability-async.png"
    title="Observability Async"
/>

### Temporal CLI

Use the `workflow describe` command to show pending Nexus Operations in the caller Workflow and any attached callbacks on the handler Workflow:

```
temporal workflow describe -w <ID>
```

Nexus events are included in the caller's Event history:

```
temporal workflow show -w <ID>
```

For **asynchronous Nexus Operations** the following are reported in the caller's history:

- `NexusOperationScheduled`
- `NexusOperationStarted`
- `NexusOperationCompleted`

For **synchronous Nexus Operations** the following are reported in the caller's history:

- `NexusOperationScheduled`
- `NexusOperationCompleted`

:::note

`NexusOperationStarted` isn't reported in the caller's history for synchronous operations.

:::

## Learn more

- Read the high-level description of the [Temporal Nexus feature](/evaluate/nexus) and watch the [Nexus keynote and demo](https://youtu.be/qqc2vsv1mrU?feature=shared&t=2082).
- Learn how Nexus works in the [Nexus deep dive talk](https://www.youtube.com/watch?v=izR9dQ_eIe4) and [Encyclopedia](/nexus).
- Deploy Nexus Endpoints in production with [Temporal Cloud](/cloud/nexus).

---

## Nexus - Go SDK

![Go SDK Banner](/img/assets/banner-go-temporal.png)

## Temporal Nexus

- [Quickstart](/develop/go/nexus/quickstart)
- [Feature guide](/develop/go/nexus/feature-guide)

---

## Nexus Go Quickstart

[Temporal Nexus](/evaluate/nexus) connects Temporal Applications within and across Namespaces using a Nexus Endpoint, a Nexus Service contract, and Nexus Operations. Build a Nexus Service that wraps an existing Temporal Workflow, then invoke it from a caller Workflow.

:::info NEW TO NEXUS?

This page will help you get a working sample running in Go.
To evaluate whether Nexus fits your use case, see the [evaluation guide](/evaluate/nexus) and to learn more about Nexus features, click [here](/nexus).

:::

**Prerequisites:** Complete the [Go SDK Quickstart](/develop/go/set-up-your-local-go) first.
You should have `activity.go`, `workflow.go`, `worker/main.go`, and `start/main.go` from that guide.

## What you'll build

You have `SayHelloWorkflow` running in the `default` Namespace.
By the end of this guide:

1. A Nexus Service will expose `SayHelloWorkflow` as an Operation.
2. A second Namespace will contain a Workflow that calls that Operation.
3. The caller Workflow will get back `"Hello Temporal"` — the same result, but across Namespaces.

<SetupSteps>

<SetupStep code={
<>

<CodeSnippet language="go" title="service.go">
{`package greeting

const (
    HelloServiceName   = "my-hello-service"
    HelloOperationName = "say-hello"
)

type HelloInput struct {
    Name string
}`}
</CodeSnippet>

</>
}>

## 1. Define the Nexus Service

Create a file called `service.go` that defines the Nexus Service contract.

Creating a Nexus Service establishes the contract between your implementation and any callers.
It provides type safety when invoking Nexus Operations and ensures that Operation Handlers fulfill the contract.

`HelloServiceName` and `HelloOperationName` are string constants that uniquely identify the Service and Operation.
`HelloInput` defines the input type for the Operation.
`SayHelloWorkflow` returns `string`, so the Operation output type is also `string`.

</SetupStep>

<SetupStep code={
<>

<CodeSnippet language="go" title="nexus_handler.go">
{`package greeting

    "context"

    "github.com/nexus-rpc/sdk-go/nexus"
    "go.temporal.io/sdk/client"
    "go.temporal.io/sdk/temporalnexus"
    "go.temporal.io/sdk/workflow"
)

// HelloNexusWorkflow is the handler Workflow for the Nexus SayHello Operation.
// It bridges the Nexus HelloInput to SayHelloWorkflow's string parameter.
func HelloNexusWorkflow(ctx workflow.Context, input HelloInput) (string, error) {
    return SayHelloWorkflow(ctx, input.Name)
}

var HelloOperation = temporalnexus.NewWorkflowRunOperation(
    HelloOperationName,
    HelloNexusWorkflow,
    func(ctx context.Context, input HelloInput, options nexus.StartOperationOptions) (client.StartWorkflowOptions, error) {
        return client.StartWorkflowOptions{
            // RequestID is stable across retries, making it safe to use as a Workflow ID.
            ID: options.RequestID,
        }, nil
    },
)`}
</CodeSnippet>

</>
}>

## 2. Define the Nexus Operation handlers

Create a file called `nexus_handler.go` that implements the Nexus Operation handler.

Operation handlers contain the logic that runs when a caller invokes a Nexus Operation.

`HelloNexusWorkflow` acts as the handler Workflow.
It bridges the Nexus `HelloInput` to `SayHelloWorkflow`'s `string` parameter by extracting `input.Name`.

`temporalnexus.NewWorkflowRunOperation` creates an asynchronous Nexus Operation that starts `HelloNexusWorkflow` when invoked.
The Options function returns `client.StartWorkflowOptions`, including a stable Workflow ID derived from `options.RequestID`.

</SetupStep>

<SetupStep code={
<>

<CodeSnippet language="go" title="worker/main.go">
{`package main

    "log"

    "my-org/greeting"

    "github.com/nexus-rpc/sdk-go/nexus"
    "go.temporal.io/sdk/client"
    "go.temporal.io/sdk/worker"
)

func main() {
    // Empty Options defaults to the "default" Namespace.
    c, err := client.Dial(client.Options{})
    if err != nil {
        log.Fatalln("Unable to create client", err)
    }
    defer c.Close()

    w := worker.New(c, "my-task-queue", worker.Options{})
    w.RegisterWorkflow(greeting.SayHelloWorkflow)
    w.RegisterWorkflow(greeting.HelloNexusWorkflow)
    w.RegisterActivity(greeting.Greet)

    service := nexus.NewService(greeting.HelloServiceName)
    err = service.Register(greeting.HelloOperation)
    if err != nil {
        log.Fatalln("Unable to register operations", err)
    }
    w.RegisterNexusService(service)

    err = w.Run(worker.InterruptCh())
    if err != nil {
        log.Fatalln("Unable to start worker", err)
    }
}`}
</CodeSnippet>

</>
}>

## 3. Register the Nexus Service handler in a Worker

Update your existing `worker/main.go` to register the Nexus Service Handler.

This Worker runs in the `default` Namespace — the same Namespace where `SayHelloWorkflow` is already registered.

A Worker will only poll for and process incoming Nexus requests if the Nexus Service Handlers are registered.
This is the same Worker concept used for Workflows and Activities.

`nexus.NewService` creates a named Nexus Service.
`service.Register` adds the `HelloOperation` to the Service.
`w.RegisterNexusService` registers the Service with the Worker so it can receive Nexus Operation requests.
`HelloNexusWorkflow` must also be registered so the Worker can execute it as the handler Workflow.

</SetupStep>

<SetupStep code={
<>

<CodeSnippet language="go" title="caller_workflow.go">
{`package greeting

    "time"

    "go.temporal.io/sdk/workflow"
)

const (
    CallerTaskQueue = "my-caller-task-queue"
    NexusEndpoint   = "my-nexus-endpoint-name"
)

func CallerWorkflow(ctx workflow.Context, name string) (string, error) {
    c := workflow.NewNexusClient(NexusEndpoint, HelloServiceName)

    fut := c.ExecuteOperation(ctx, HelloOperationName, HelloInput{Name: name}, workflow.NexusOperationOptions{
        ScheduleToCloseTimeout: 10 * time.Second,
    })

    var result string
    if err := fut.Get(ctx, &result); err != nil {
        return "", err
    }
    return result, nil
}`}
</CodeSnippet>

</>
}>

## 4. Develop the caller Workflow

Create a file called `caller_workflow.go` that defines a Workflow which invokes the Nexus Operation.

The caller Workflow demonstrates the consumer side of Nexus.
Instead of importing handler code directly, the caller only depends on the Service contract.
This keeps the caller and handler decoupled so they can live in separate Namespaces, repositories, or even teams.

`workflow.NewNexusClient` creates a client bound to your Nexus Service and Endpoint.
`ExecuteOperation` starts the Operation and returns a future.
`fut.Get` blocks until the Operation completes and writes the result into `result`.

</SetupStep>

<SetupStep code={
<>

<CodeSnippet language="bash">
temporal operator namespace create --namespace my-caller-namespace
</CodeSnippet>

<CodeSnippet language="bash">
{`temporal operator nexus endpoint create \\
  --name my-nexus-endpoint-name \\
  --target-namespace default \\
  --target-task-queue my-task-queue`}
</CodeSnippet>

</>
}>

## 5. Create the caller Namespace and Nexus Endpoint

Before running the application, create a caller Namespace and a Nexus Endpoint to route requests from the caller to the handler.
The handler uses the `default` Namespace that was created when you started the dev server.

Namespaces provide isolation between the caller and handler sides.
The Nexus Endpoint acts as a routing layer that connects the caller Namespace to the handler's target Namespace and Task Queue.
The endpoint name must match the `NexusEndpoint` constant defined in `caller_workflow.go` from step 4.

Make sure your local Temporal dev server is running (`temporal server start-dev`).

</SetupStep>

<SetupStep code={
<>

<CodeSnippet language="go" title="caller/main.go">
{`package main

    "context"
    "log"

    "my-org/greeting"

    "go.temporal.io/sdk/client"
    "go.temporal.io/sdk/worker"
)

func main() {
    c, err := client.Dial(client.Options{
        Namespace: "my-caller-namespace",
    })
    if err != nil {
        log.Fatalln("Unable to create client", err)
    }
    defer c.Close()

    w := worker.New(c, greeting.CallerTaskQueue, worker.Options{})
    w.RegisterWorkflow(greeting.CallerWorkflow)

    if err := w.Start(); err != nil {
        log.Fatalln("Unable to start worker", err)
    }
    defer w.Stop()

    wr, err := c.ExecuteWorkflow(context.Background(), client.StartWorkflowOptions{
        ID:        "nexus-caller-workflow",
        TaskQueue: greeting.CallerTaskQueue,
    }, greeting.CallerWorkflow, "Temporal")
    if err != nil {
        log.Fatalln("Unable to execute workflow", err)
    }

    var result string
    if err := wr.Get(context.Background(), &result); err != nil {
        log.Fatalln("Unable to get workflow result", err)
    }
    log.Println("Workflow result:", result)
}`}
</CodeSnippet>

</>
}>

## 6. Run and Verify

Create `caller/main.go` to start the caller Worker and execute the Workflow.

This brings everything together: the caller Worker hosts `CallerWorkflow`, which uses the Nexus client to invoke `say-hello` on the handler side.
The full request flows from the caller Workflow, through the Nexus Endpoint, to the handler Worker running `HelloNexusWorkflow` (which calls `SayHelloWorkflow`), and back to the caller.

**Ensure the `nexus-rpc` dependency is synchronized:**

In a terminal, from within your project:

```bash
go mod tidy
```

**Run the application:**

1. Start the handler Worker in one terminal:

```bash
go run worker/main.go
```

2. Run the caller in another terminal:

```bash
go run caller/main.go
```

You should see:

```
Workflow result: Hello Temporal
```

Open the [Temporal Web UI](http://localhost:8233) and switch between Namespaces to see both Workflow Executions.
In `my-caller-namespace`, find the `CallerWorkflow` execution — you should see `NexusOperationScheduled`, `NexusOperationStarted`, and `NexusOperationCompleted` events in its history.
In `default`, find the `HelloNexusWorkflow` execution that was started by the Nexus Operation.

</SetupStep>
</SetupSteps>

## Next Steps

Now that you have a working Nexus Service, here are some resources to deepen your understanding:

- **[Go Nexus Feature Guide](/develop/go/nexus/feature-guide)**: Covers synchronous and asynchronous Operations, error handling, cancellation, and cross-Namespace calls.
- **[Nexus Operations](/nexus/operations)**: The full Operation lifecycle, including retries, timeouts, and execution semantics.
- **[Nexus Services](/nexus/services)**: Designing Service contracts and registering multiple Services per Worker.
- **[Nexus Patterns](/nexus/patterns)**: Comparing the collocated and router-queue deployment patterns.
- **[Error Handling in Nexus](/nexus/error-handling)**: Handling retryable and non-retryable errors across caller and handler boundaries.
- **[Execution Debugging](/nexus/execution-debugging)**: Bi-directional linking and OpenTelemetry tracing for debugging Nexus calls.
- **[Nexus Endpoints](/nexus/endpoints)**: Managing Endpoints and understanding how they route requests.
- **[Temporal Nexus on Temporal Cloud](/cloud/nexus)**: Deploying Nexus in a production Temporal Cloud environment with built-in access controls and multi-region connectivity.

---

## Enriching the user interface - Go SDK

Temporal supports adding context to Workflows and Events with metadata.
This helps users identify and understand Workflows and their operations.

## Adding Summary and Details to Workflows

### Starting a Workflow

When starting a Workflow, you can provide a static summary and details to help identify the Workflow in the UI:

```go

    "context"
    "go.temporal.io/sdk/client"
)

func main() {
    // Create the client
    c, err := client.Dial(client.Options{})
    if err != nil {
        // Handle error
    }
    defer c.Close()

    // Start workflow options with static summary and details
    workflowOptions := client.StartWorkflowOptions{
        ID:        "your-workflow-id",
        TaskQueue: "your-task-queue",
        StaticSummary: "Order processing for customer #12345",
        StaticDetails: "Processing premium order with expedited shipping",
    }

    // Start the workflow
    we, err := c.ExecuteWorkflow(context.Background(), workflowOptions, YourWorkflow, "workflow input")
    if err != nil {
        // Handle error
    }
}
```

`StaticSummary` is a single-line description that appears in the Workflow list view, limited to 200 bytes.
`StaticDetails` can be multi-line and provides more comprehensive information that appears in the Workflow details view, with a larger limit of 20K bytes.

The input format is standard Markdown excluding images, HTML, and scripts.

### Inside the Workflow

Within a Workflow, you can get and set the _current workflow details_.
Unlike static summary/details set at Workflow start, this value can be updated throughout the life of the Workflow.
Current Workflow details also takes Markdown format (excluding images, HTML, and scripts) and can span multiple lines.

```go

    "go.temporal.io/sdk/workflow"
)

func YourWorkflow(ctx workflow.Context, input string) (string, error) {
    // Get the current details
    currentDetails := workflow.GetCurrentDetails(ctx)
    workflow.GetLogger(ctx).Info("Current details", "details", currentDetails)

    // Set/update the current details
    workflow.SetCurrentDetails(ctx, "Updated workflow details with new status")

    return "Workflow completed", nil
}
```

### Adding Summary to Activities and Timers

You can attach a metadata parameter `Summary` to Activities when starting them from within a Workflow:

```go

    "time"
    "go.temporal.io/sdk/workflow"
)

func YourWorkflow(ctx workflow.Context, input string) (string, error) {
    // Activity options with summary
    ao := workflow.ActivityOptions{
        StartToCloseTimeout: 10 * time.Second,
        Summary: "Processing user data",
    }
    ctx = workflow.WithActivityOptions(ctx, ao)

    // Execute the activity
    var result string
    err := workflow.ExecuteActivity(ctx, YourActivity, input).Get(ctx, &result)
    if err != nil {
        return "", err
    }

    return result, nil
}
```

Similarly, you can attach a `Summary` to timers within a Workflow:

```go

    "time"
    "go.temporal.io/sdk/workflow"
)

func YourWorkflow(ctx workflow.Context, input string) (string, error) {
    // Create a timer with options including summary
    timerFuture := workflow.NewTimerWithOptions(ctx, 5*time.Minute, workflow.TimerOptions{
        Summary: "Waiting for payment confirmation",
    })

    // Wait for the timer
    err := timerFuture.Get(ctx, nil)
    if err != nil {
        return "", err
    }

    return "Timer completed", nil
}
```

The input format for `Summary` is a string, and limited to 200 bytes.

## Viewing Summary and Details in the UI

Once you've added summaries and details to your workflows, activities, and timers, you can view this enriched information in the Temporal Web UI.
Navigate to your Workflow's details page to see the metadata displayed in two key locations:

### Workflow Overview Section

At the top of the workflow details page, you'll find the workflow-level metadata:

- **Summary & Details** - Displays the static summary and static details set when starting the workflow
- **Current Details** - Displays the dynamic details that can be updated during workflow execution

All Workflow details support standard Markdown formatting (excluding images, HTML, and scripts), allowing you to create rich, structured information displays.

### Event History

Individual events in the Workflow's Event History display their associated summaries when available.

Workflow, Activity and Timer summaries appear in purple text next to their corresponding events, providing immediate context without requiring you to expand the event details.
When you do expand an event, the summary is also prominently displayed in the detailed view.

---

## Client - Go SDK(Platform)

![Go SDK Banner](/img/assets/banner-go-temporal.png)

## Platform

- [Observability](/develop/go/platform/observability)
- [Enriching the UI](/develop/go/platform/enriching-ui)

---

## Observability - Go SDK

This page covers the many ways to view the current state of your [Temporal Application](/temporal#temporal-application)—that is, ways to view which [Workflow Executions](/workflow-execution) are tracked by the [Temporal Platform](/temporal#temporal-platform) and the state of any specified Workflow Execution, either currently or at points of an execution.

This section covers features related to viewing the state of the application, including:

- [Metrics](#metrics)
- [Tracing](#tracing)
- [Logging](#logging)
- [Visibility](#visibility)

## How to emit metrics {/* #metrics */}

**How to emit application metrics using the Temporal Go SDK.**

Each Temporal SDK is capable of emitting an optional set of metrics from either the Client or the Worker process.
For a complete list of metrics capable of being emitted, see the [SDK metrics reference](/references/sdk-metrics).

- For an overview of Prometheus and Grafana integration, refer to the [Monitoring](/self-hosted-guide/monitoring) guide.
- For a list of metrics, see the [SDK metrics reference](/references/sdk-metrics).
- For an end-to-end example that exposes metrics with the Go SDK, refer to the [samples-go](https://github.com/temporalio/samples-go/tree/main/metrics) repo.

To emit metrics from the Temporal Client in Go, create a [metrics handler](https://pkg.go.dev/go.temporal.io/sdk/internal/common/metrics#Handler) from the [Client Options](https://pkg.go.dev/go.temporal.io/sdk@v1.15.0/internal#ClientOptions) and specify a listener address to be used by Prometheus.

```go
client.Options{
		MetricsHandler: sdktally.NewMetricsHandler(newPrometheusScope(prometheus.Configuration{
