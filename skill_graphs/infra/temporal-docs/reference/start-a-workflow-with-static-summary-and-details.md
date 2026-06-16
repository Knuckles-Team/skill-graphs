# Start a Workflow with static summary and details
handle = await client.start_workflow(
    YourWorkflow.run,
    "workflow input",
    id="your-workflow-id",
    task_queue="your-task-queue",
    static_summary="Order processing for customer #12345",
    static_details="Processing premium order with expedited shipping"
)
```

`static_summary` is a single-line description that appears in the Workflow list view, limited to 200 bytes.
`static_details` can be multi-line and provides more comprehensive information that appears in the Workflow details view, with a larger limit of 20K bytes.

The input format is standard Markdown excluding images, HTML, and scripts.

You can also use the `execute_workflow` method with the same parameters:

```python
result = await client.execute_workflow(
    YourWorkflow.run,
    "workflow input",
    id="your-workflow-id",
    task_queue="your-task-queue",
    static_summary="Order processing for customer #12345",
    static_details="Processing premium order with expedited shipping"
)
```

### Inside the Workflow

Within a Workflow, you can get and set the _current Workflow details_.
Unlike static summary/details set at Workflow start, this value can be updated throughout the life of the Workflow.
Current Workflow details also takes Markdown format (excluding images, HTML, and scripts) and can span multiple lines.

```python
@workflow.defn
class YourWorkflow:
    @workflow.run
    async def run(self, input: str) -> str:
        # Get the current details
        current_details = workflow.get_current_details()
        print(f"Current details: {current_details}")

        # Set/update the current details
        workflow.set_current_details("Updated workflow details with new status")

        return "Workflow completed"
```

### Adding Summary to Activities and Timers

You can attach a metadata parameter `summary` to Activities when starting them from within a Workflow:

```python
@workflow.defn
class YourWorkflow:
    @workflow.run
    async def run(self, input: str) -> str:
        # Start an activity with a summary
        result = await workflow.execute_activity(
            your_activity,
            input,
            start_to_close_timeout=timedelta(seconds=10),
            summary="Processing user data"
        )
        return result
```

Similarly, you can attach a `summary` to Timers within a Workflow:

```python
@workflow.defn
class YourWorkflow:
    @workflow.run
    async def run(self, input: str) -> str:
        # Create a timer with a summary
        await workflow.sleep(timedelta(minutes=5), summary="Waiting for payment confirmation")
        return "Timer completed"
```
The input format for `summary` is a string, and limited to 200 bytes.

## Viewing Summary and Details in the UI

Once you've added summaries and details to your Workflows, Activities, and Timers, you can view this enriched information in the Temporal Web UI.
Navigate to your Workflow's details page to see the metadata displayed in two key locations:

### Workflow Overview Section

At the top of the Workflow details page, you'll find the Workflow-level metadata:

- **Summary & Details** - Displays the static summary and static details set when starting the Workflow
- **Current Details** - Displays the dynamic details that can be updated during Workflow execution

All Workflow details support standard Markdown formatting (excluding images, HTML, and scripts), allowing you to create rich, structured information displays.

### Event History

Individual events in the Workflow's Event History display their associated summaries when available.

Workflow, Activity and Timer summaries appear in purple text next to their corresponding events, providing immediate context without requiring you to expand the Event details.
When you do expand an Event, the summary is also prominently displayed in the detailed view.

---

## Client - Python SDK(Platform)

![Python SDK Banner](/img/assets/banner-python-temporal.png)

## Platform

- [Observability](/develop/python/platform/observability)
- [Enriching the UI](/develop/python/platform/enriching-ui)

---

## Observability - Python SDK

The observability section of the Temporal Developer's guide covers the many ways to view the current state of your [Temporal Application](/temporal#temporal-application)—that is, ways to view which [Workflow Executions](/workflow-execution) are tracked by the [Temporal Platform](/temporal#temporal-platform) and the state of any specified Workflow Execution, either currently or at points of an execution.

This section covers features related to viewing the state of the application, including:

- [Emit metrics](#metrics)
- [Set up tracing](#tracing)
- [Log from a Workflow](#logging)
- [Visibility APIs](#visibility)

## Emit metrics {/* #metrics */}

**How to emit metrics**

Each Temporal SDK is capable of emitting an optional set of metrics from either the Client or the Worker process.
For a complete list of metrics capable of being emitted, see the [SDK metrics reference](/references/sdk-metrics).

- For an overview of Prometheus and Grafana integration, refer to the [Monitoring](/self-hosted-guide/monitoring) guide.
- For a list of metrics, see the [SDK metrics reference](/references/sdk-metrics).
- For an end-to-end example that exposes metrics with the Python SDK, refer to the [samples-python](https://github.com/temporalio/samples-python/tree/main/prometheus) repo.

Metrics in Python are configured globally; therefore, you should set a Prometheus endpoint before any other Temporal code.

The following example exposes a Prometheus endpoint on port `9000`.

```python
from temporalio.runtime import Runtime, TelemetryConfig, PrometheusConfig
