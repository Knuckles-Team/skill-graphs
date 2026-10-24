
### Development pattern

By abstracting complexities and streamlining boilerplate code, developers can craft straightforward code that directly aligns with their business logic, enhancing code readability and bolstering developer productivity.

Consider a bank loan application.
Developers can design the business logic of a bank loan using the Temporal SDK.
The Workflow defines the overarching business logic, encompassing tasks such as validating applicant information, credit checks, loan approval, and applicant notifications, as Activities.

:::caution Do not copy and use code

The following is pseudocode. For tested samples see your language SDK's developer's guide.

:::

```
func LoanApplicationWorkflow {

    sdk.ExecuteActivity(CreditCheck)

    sdk.ExecuteActivity(AutomatedApproval)

    sdk.ExecuteActivity(NotifyApplicant)

    // ...
}
```

For instance, Temporal SDKs have built-in support for handling failures, timeouts, and retries.
In the event of an Activity failure, the SDK automatically initiates retries according to configurable policies established by the developer within the SDK. This streamlined process simplifies the integration of fault-tolerance mechanisms into applications.

:::caution Do not copy and use code

The following is pseudocode. For tested samples see your language SDK's developer's guide.

:::

```
func LoanApplicationWorkflow {

    options = {
        MaxAttempts: 3,
        StartToCloseTimeout: 30min,
        HeartbeatTimeout: 10min,
    }

    sdk.ExecuteActivity(CreditCheck, options)

    sdk.ExecuteActivity(AutomatedApproval)

    sdk.ExecuteActivity(NotifyApplicant)

    // ...
}
```

### Replays

Another quality of the SDKs lies in their ability to replay Workflow Executions, a complex operation that contributes significantly to the Platform's promised reliability.

<CaptionedImage
    src="/diagrams/replay-basic.svg"
    title="The SDKs Replay code execution to continue from the last step" />

We will delve into this idea more later, but for now, it signifies that the SDKs can automatically continue a process from the point of interruption, should a failure occur.
This capability stems from the SDK's ability to persist each step the program takes.

{/* - [Developing for Durable Execution using the Go SDK](/develop/go/durable-execution) */}

## Temporal SDKs major components {/* #major-components */}

**What are the major components of Temporal SDKs?**

Temporal SDKs offer developers the following:

- A Temporal Client to communicate with a Temporal Service
- APIs to develop application code (Workflows & Activities)
- APIs to configure and run Workers

<CaptionedImage
    src="/diagrams/temporal-sdk-components.svg"
    title="Temporal SDK components create a runtime across your environment and a Temporal Service" />

Let's break down each one.

### Temporal Client

A Temporal Client acts as the bridge for communication between your applications and the Temporal Service.
The Client performs key functions that facilitate the execution of, management of, and communication with Workflows.

The most common operations that a Temporal Client enables you to perform are the following:

- Get the result of Workflow Execution.
- List Workflow Executions.
- Query a Workflow Execution.
- Signal a Workflow Execution.
- Start a Workflow Execution.

The following code is an example using the Go SDK.
It showcases how to initialize a Temporal Client, create a connection to a local Temporal Service, and start a Workflow Execution:

:::caution Do not copy and use code

The following code is for example purposes only.
For tested code samples and best practices, use your preferred language SDK's developer's guide.

- [Go SDK Temporal Client feature guide](/develop/go/client/temporal-client)
- [Java SDK Temporal Client feature guide](/develop/java/client/temporal-client)
- [PHP SDK Temporal Client feature guide](/develop/php/client/temporal-client)
- [Python SDK Temporal Client feature guide](/develop/python/client)
- [TypeScript SDK Temporal Client feature guide](/develop/typescript/client)

:::

```go
package main

	"context"

	"go.temporal.io/sdk/client"
)

func main() {
	// Temporal Client setup code
	c, err := client.NewClient(client.Options{})
	if err != nil {
		log.Fatalln("Unable to create client", err)
	}
	defer c.Close()
	// Prepare Workflow option and parameters
	workflowOptions := client.StartWorkflowOptions{
		ID:        "loan-application-1",
		TaskQueue: "loan-application-task-queue",
	}
	applicantDetails := ApplicantDetails{
		// ...
	}
	// Start the Workflow
	workflowRun, err := c.ExecuteWorkflow(context.Background(), workflowOptions, "loan-application-workflow", applicantDetails)
	if err != nil {
		// ...
	}
	// ...
}
```

Developers can then use the Client as the main entry point for interacting with the application through Temporal.
Using that Client, developers may for example start or Signal Workflows, Query a Workflow's state, etc.
We can see in the example above how the developer has used `ExecuteWorkflow` API to start a Workflow.

### APIs to Develop Workflows

Workflows are defined as code: either a function or an object method, depending on the language.

For example, the following is a valid Temporal Workflow in Go:

:::caution Do not copy and use code

The following code is for example purposes only.
For tested code samples and best practices, use your preferred language SDK's developer's guide.

:::

```go
func LoanApplication(ctx context.Context) (error) {
    // ...
	return nil
}
```

The Workflow code uses Temporal SDK APIs to orchestrate the steps of the application.

:::caution Do not copy and use code

The following code is for example purposes only.
For tested code samples and best practices, use your preferred language SDK's developer's guide.

:::

```go
func LoanApplication(ctx workflow.Context, input *LoanApplicationWorkflowInput) (*LoanApplicationWorkflowResult, error) {
	// ...
	var result activities.CreditCheckResult
	f := workflow.ExecuteActivity(ctx, a.CreditCheck, CreditCheckInput(*input))
	err := f.Get(ctx, &result)
	// ...
	// Return the results
	return &loanApplicationResults, nil
}
```

A Workflow executes Activities (other functions that interact with external systems), handles and sends messages (Queries, Signals, Updates), and interacts with other Workflows.

This Workflow code, while executing, can be paused, resumed, and migrated across physical machines without losing state.

When a Workflow calls the API to execute an Activity, the Worker sends a [Command](https://docs.temporal.io/references/commands) back to the Temporal Service. The Temporal Service creates Activity Tasks in response which the same or a different Worker can then pick up and begin executing. In this way, the Worker and Temporal Service work together to incrementally execute Workflow code in a reliable way.
We discuss this more in detail in [The SDK and Temporal Service relationship](/encyclopedia/temporal-sdks#sdk-and-cluster-relationship) section.

The SDK APIs also enable developers to write code that more genuinely maps to their process. This is because without a specialized SDK, developers might have to write a lot of boilerplate code. This can lead to code that's hard to maintain, difficult to understand, or that doesn't directly correspond to the underlying business process.

For example, the bank loan application Workflow might actually look like this:

:::caution Do not copy and use code

The following code is for example purposes only.
For tested code samples and best practices, use your preferred language SDK's developer's guide.

:::

```go
// LoanApplicationWorkflow is the workflow definition.
func LoanApplicationWorkflow(ctx workflow.Context, applicantName string, loanAmount int) (string, error) {
	// Step 1: Notify the applicant that the application process has started
	err := workflow.ExecuteActivity(ctx, NotifyApplicantActivity, applicantName, "Application process started").Get(ctx, nil)
	if err != nil {
		return "", err
	}

	// Step 2: Perform a credit check
	var creditCheckResult string
	err = workflow.ExecuteActivity(ctx, LoanCreditCheckActivity, loanAmount).Get(ctx, &creditCheckResult)
	if err != nil {
		return "", err
	}

	// Step 3: Perform an automatic approval check
	var approvalCheckResult string
	err = workflow.ExecuteActivity(ctx, AutomaticApprovalCheckActivity, creditCheckResult).Get(ctx, &approvalCheckResult)
	if err != nil {
		return "", err
	}

	// Step 4: Notify the applicant of the decision
	var notificationResult string
	err = workflow.ExecuteActivity(ctx, NotifyApplicantActivity, applicantName, approvalCheckResult).Get(ctx, &notificationResult)
	if err != nil {
		return "", err
	}

	return notificationResult, nil
}
```

The level of abstraction that APIs offer enables the developer to focus on business logic without having to worry about the intricacies of distributed computing such as retries, or having to explicitly maintain a state machine and the intermediate state for each step of the process.

Additionally, the state of the Workflow is automatically persisted so if a failure does occur, it resumes right where it left off.

### APIs to create and manage Worker Processes

Workers are responsible for executing Workflow and Activity code (application code). The SDK provides APIs for configuring and starting Workers, enabling developers to control how the code is executed.
Workers are horizontally scalable, often run with systems like Kubernetes, and configured according to the application's needs.

Here is an example of how you could initialize a Worker using the Go SDK.

:::caution Do not copy and use code

The following code is for example purposes only.
For tested code samples and best practices, use your preferred language SDK's developer's guide.

:::

```go
func main() {
    // Create the client object just once per process
    c, err := client.NewClient(client.Options{})
    if err != nil {
        log.Fatalln("Unable to create Temporal client", err)
    }
    defer c.Close()

    // Create the Worker instance
    w := worker.New(c, "loan-application-task-queue", worker.Options{})

    // Register the workflow and activity with the worker
    w.RegisterWorkflow(LoanApplicationWorkflow)
    w.RegisterActivity(LoanCreditCheck)

    // Start listening to the Task Queue
    err = w.Run(worker.InterruptCh())
    if err != nil {
        log.Fatalln("Unable to start Worker", err)
    }
}
```

The Worker polls on the specified Task Queue, processing those Tasks, and reporting the results back to the Temporal Service. They execute both the Workflows and Activities, and the SDK ensures that they perform these tasks efficiently and reliably.

### APIs to customize Activity Execution behavior

Activities in Temporal are individual units of work that often represent non-deterministic parts of the code logic, such as querying a database or calling an external service. The SDK provides APIs to customize the behavior of an Activity Execution.

By default, if an Activity attempts to communicate with another system and encounters a transient failure like a network issue, Temporal ensures the Activity is tried again automatically.

However, Temporal enables developers to control a variety of timeouts, a Retry Policy, Heartbeat monitoring, and asynchronous completion.

The following code is an example of a custom set of Activity Execution options that affect the timeout and retry behavior of the execution, should the Activity encounter a failure.

:::caution Do not copy and use code

The following code is for example purposes only.
For tested code samples and best practices, use your preferred language SDK's developer's guide.

:::

```go
// LoanApplicationWorkflow is the Workflow Definition.
func LoanApplicationWorkflow(ctx workflow.Context, applicantName string, loanAmount int) (string, error) {
    // ...
    var creditCheckResult string
    // set a Retry Policy
    ao := workflow.ActivityOptions{
		ScheduleToCloseTimeout: time.Hour,
		HeartbeatTimeout:       time.Minute,
		RetryPolicy:            &temporal.RetryPolicy{
			InitialInterval:    time.Second,
			BackoffCoefficient: 2,
			MaximumInterval:    time.Minute,
			MaximumAttempts:    5,
		},
	}
    ctx = workflow.WithActivityOptions(ctx, ao)
    err = workflow.ExecuteActivity(ctx, LoanCreditCheckActivity, loanAmount).Get(ctx, &creditCheckResult)
    if err != nil {
        return "", err
    }
	// ...
    return notificationResult, nil
}

// LoanCreditCheckActivity is an Activity function that performs a credit check.
func LoanCreditCheckActivity(ctx context.Context, loanAmount int) (string, error) {
	// ... your logic here ...
	return "Credit check passed", nil
}
```

## The SDK and Temporal Service relationship {/* #sdk-and-cluster-relationship */}

**How do the Temporal SDKs work with the Temporal Service?**

The Temporal Service functions more as a choreographer than a conductor. Rather than directly assigning tasks to Workers, the Temporal Service arranges the Tasks into a Task Queue while Workers poll the Task Queue. Developers may create a fleet of Workers and tune them so that a Task is picked up as soon as it is available. If a Worker goes down, Tasks can wait until the next Worker is available.

A Workflow might request to execute an Activity, start a Timer, or start a Child Workflow, each of which translates into a Command, dispatched to the Temporal Service.
In addition to acting on these Commands, the Temporal Service documents that interaction by appending their corresponding Events into the Workflow Execution's Event History.

Take for instance the call to execute an Activity. When a Workflow invokes it, the Worker doesn't immediately execute that Activity code. Instead, it generates a ScheduleActivityTask Command, dispatching it to the Cluster. In response, the Cluster queues up a new Activity Task. Only when a Worker finds itself free, it collects the task and begins executing the Activity code.

The Temporal Service persists Workflow Execution Event History, so that if there is a failure, the SDK Worker is able to Replay the execution and resume where it left off.

This is where the deterministic constraints of the Workflow code comes into play, requiring the use of Activities to create side effects and interact with the outside world.

Let's look at an example Workflow with a single Activity.

```go
func LoanApplication(ctx workflow.Context, input *LoanApplicationWorkflowInput) (*LoanApplicationWorkflowResult, error) {

	ctx = workflow.WithActivityOptions(ctx, workflow.ActivityOptions{
		StartToCloseTimeout: time.Minute,
	})

	var result activities.NotifyApplicantActivityResult
	f := workflow.ExecuteActivity(ctx, a.NotifyApplicantActivity, NotifyApplicantActivityInput(*input))

	err := f.Get(ctx, &result)

	// Return the results
	return &l.LoanApplicationState, nil
}

type Activities struct {}

func (a *Activities) NotifyApplicantActivity(ctx context.Context, input *NotifyApplicantActivityInput) (*NotifyApplicantActivityResult, error) {
	var result NotifyApplicantActivityResult

	// Call the thirdparty API and handle the result

	return &result, err
}
```

The Activity above is performing a single call to an external API. Since the call can fail due to transient issues, we define it outside of the Workflow and provide it with retry options.

When you create a new Worker process, the Worker creates a long-lasting connection to the Temporal Service, polling a Task Queue for Tasks that are related to the code it is capable of executing.

<CaptionedImage
    src="/diagrams/how-sdk-works-1.svg"
    title="A Worker long polls for Tasks" />

Although the Worker is now running, unless a Workflow is explicitly started, the Task Queue doesn't have any Tasks on it and so, no code executes.
We can use a Temporal Client (available in Temporal SDKs and the Temporal CLI) to start a new Workflow.

<CaptionedImage
    src="/diagrams/how-sdk-works-2.svg"
    title="Start a Workflow using a Temporal Client" />

Starting a Workflow Execution creates a new Event, WorkflowExecutionStarted, and adds it to the Workflow Execution's Event History.

The Temporal Service then schedules a Workflow Task by adding it to the Task Queue.
When the Worker has capacity, it picks up this Task, and begin executing code.

Each step of the Task (e.g. Scheduled, Started, and Completed), gets recorded into the Event History.

- Scheduled means that the Temporal Service has added a Task to the Task Queue.
- Started means that the Worker has dequeued the Task.
- Completed means that the Worker finished executing the Task by responding to the Temporal Service.

When the call to invoke the Activity is evaluated, the Worker suspends executing the code and sends a Command to the Temporal Service to schedule an Activity Task.

<CaptionedImage
    src="/diagrams/how-sdk-works-3.svg"
    title="Worker suspends code execution and sends a Command to the Temporal Service" />

When the Worker process can perform more work, it picks up the Activity Task and begins executing the Activity code, which includes the call to the external API.

If the Activity fails, say the API goes down, Temporal will automatically retry the Activity with one second between intervals, as the configurations have defined, an infinite number of times until the Activity succeeds or is canceled.

In the case where the calls succeeds, and the code completes, the Worker tells the Temporal Service the Activity Task completed.

<CaptionedImage
    src="/diagrams/how-sdk-works-activity.svg"
    title="The Worker reports that the Activity Execution completed" />

Included is any data that was returned from the Activity (results of the API call), which is then persisted in the Workflow Execution Event History, and is now accessible to the Workflow code.

The Temporal Service creates a new Workflow Task which the Worker picks up.

<CaptionedImage
    src="/diagrams/how-sdk-works-1.svg"
    title="The Worker picks up the new Task" />

This is when the SDK Worker Replays the Workflow code, using the Event History as guidance on what to expect. If the Replay encounters an Event that doesn't match up with what is expected from the code, a [non-determinism](/references/errors#non-deterministic-error) error gets thrown.

If there is alignment, the Worker continues evaluating code.

Assuming the Activity Execution is successful, the Workflow now has the result of the Activity and the Worker is able to finish evaluating and executing the Workflow code, responding to the Temporal Service when complete.

The result of the Workflow can now be retrieved using a Temporal Client.

<CaptionedImage
    src="/diagrams/how-sdk-works-4.svg"
    title="The Temporal Client can now access the result of the Workflow" />

And that’s how a Temporal Worker and Temporal Service work together.

---

## Archival

This page discusses [Archival](#archival).

## What is Archival? {/* #archival */}

Use Archival to copy closed Workflow Execution [Event Histories](/workflow-execution/event#event-history) and Visibility records from Temporal Service persistence to blob storage.

- [How to create a custom Archiver](/self-hosted-guide/archival#custom-archiver)
- [How to set up Archival](/self-hosted-guide/archival#set-up-archival)

When a Workflow Execution closes, Temporal schedules close-processing tasks for both Visibility records and Event History archival.
Archival then runs asynchronously after a randomized delay.
By default, that delay is up to 5 minutes (`history.archivalProcessorArchiveDelay`), capped by the Namespace [Retention Period](/temporal-service/temporal-server#retention-period).

The closed execution still stays in Temporal persistence until retention cleanup runs.
For some time, the same closed execution can exist in both persistence and archival storage.
Archival enables Workflow Execution data to persist beyond retention without overwhelming the Temporal Service persistence store.

This feature is helpful for compliance and debugging.

Temporal's Archival feature is considered **experimental** and not subject to normal [versioning and support policy](/temporal-service/temporal-server#versions-and-support).

Archival is not supported when running Temporal through Docker.
It's disabled by default when installing the system manually and when deploying through [helm charts](https://github.com/temporalio/helm-charts/blob/main/charts/temporal/templates/server-configmap.yaml).
It can be enabled in the [config](https://github.com/temporalio/temporal/blob/main/config/development.yaml).

---

## Multi-Cluster Replication

This page discusses the following:

- [Multi-Cluster Replication](#multi-cluster-replication)
- [Namespace Versions](#namespace-versions)
- [Version History](#version-history)
- [Conflict Resolution](#conflict-resolution)
- [Zombie Workflows](#zombie-workflows)
- [Workflow Task Processing](#workflow-task-processing)

## What is Multi-Cluster Replication? {/* #multi-cluster-replication */}

Multi-Cluster Replication is a feature which asynchronously replicates Workflow Executions from active Clusters to other passive Clusters, for backup and state reconstruction.
When necessary, for higher availability, Cluster operators can failover to any of the backup Clusters.

Temporal's Multi-Cluster Replication feature is considered **experimental** and not subject to normal [versioning and support policy](/temporal-service/temporal-server#versions-and-support).

Temporal automatically forwards Start, Signal, and Query requests to the active Cluster.
This feature must be enabled through a Dynamic Config flag per [Global Namespace](/global-namespace).

When the feature is enabled, Tasks are sent to the Parent Task Queue partition that matches that Namespace, if it exists.

All Visibility APIs can be used against active and standby Clusters.
This enables [Temporal UI](https://docs.temporal.io/web-ui) to work seamlessly for Global Namespaces.
Applications making API calls directly to the Temporal Visibility API continue to work even if a Global Namespace is in standby mode.
However, they might see a lag due to replication delay when querying the Workflow Execution state from a standby Cluster.

## Namespace Versions

A _version_ is a concept in Multi-Cluster Replication that describes the chronological order of events per Namespace.

With Multi-Cluster Replication, all Namespace change events and Workflow Execution History events are replicated asynchronously for high throughput.
This means that data across clusters is **not** strongly consistent.
To guarantee that Namespace data and Workflow Execution data will achieve eventual consistency (especially when there is a data conflict during a failover), a **version** is introduced and attached to Namespaces.
All Workflow Execution History entries generated in a Namespace will also come with the version attached to that Namespace.

All participating Clusters are pre-configured with a unique initial version and a shared version increment:

- `initial version < shared version increment`

When performing failover for a Namespace from one Cluster to another Cluster, the version attached to the Namespace will be changed by the following rule:

- for all versions which follow `version % (shared version increment) == (active cluster's initial version)`, find the smallest version which has `version >= old version in namespace`

When there is a data conflict, a comparison will be made and Workflow Execution History entries with the highest version will be considered the source of truth.

When a cluster is trying to mutate a Workflow Execution History, the version will be checked.
A cluster can mutate a Workflow Execution History only if the following is true:

- The version in the Namespace belongs to this cluster, i.e.
  `(version in namespace) % (shared version increment) == (this cluster's initial version)`
- The version of this Workflow Execution History's last entry (event) is equal or less than the version in the Namespace, i.e.
  `(last event's version) <= (version in namespace)`

<details>
    <summary>
      Namespace version change example
    </summary>

Assuming the following scenario:

- Cluster A comes with initial version: 1
- Cluster B comes with initial version: 2
- Shared version increment: 10

T = 0: Namespace α is registered, with active Cluster set to Cluster A

```
namespace α's version is 1
all workflows events generated within this namespace, will come with version 1
```

T = 1: namespace β is registered, with active Cluster set to Cluster B

```
namespace β's version is 2
all workflows events generated within this namespace, will come with version 2
```

T = 2: Namespace α is updated to with active Cluster set to Cluster B

```
namespace α's version is 2
all workflows events generated within this namespace, will come with version 2
```

T = 3: Namespace β is updated to with active Cluster set to Cluster A

```
namespace β's version is 11
all workflows events generated within this namespace, will come with version 11
```

</details>

## Version history

Version history is a concept which provides a high level summary of version information in regards to Workflow Execution History.

Whenever there is a new Workflow Execution History entry generated, the version from Namespace will be attached.
The Workflow Execution's mutable state will keep track of all history entries (events) and the corresponding version.

<details>
    <summary>
        Version history example (without data conflict)
    </summary>
