# Execute workflow synchronously
result = client.execute_workflow(
  'YourWorkflow',
  'workflow input',
  id: 'your-workflow-id',
  task_queue: 'your-task-queue',
  static_summary: 'Order processing for customer #12345',
  static_details: 'Processing premium order with expedited shipping'
)
```

#### Inside the Workflow

Within a Workflow, you can get and set the _current workflow details_.
Unlike static summary/details set at Workflow start, this value can be updated throughout the life of the Workflow.
Current Workflow details also takes Markdown format (excluding images, HTML, and scripts) and can span multiple lines.

```ruby
require 'temporalio'

class YourWorkflow < Temporalio::Workflow::Definition
  def execute(input)
    # Get the current details
    current_details = Temporalio::Workflow.current_details
    Temporalio::Workflow.logger.info("Current details: #{current_details}")

    # Set/update the current details
    Temporalio::Workflow.current_details = 'Updated workflow details with new status'

    'Workflow completed'
  end
end
```

#### Adding Summary to Activities and Timers

You can attach a `summary:` to activities when starting them from within a Workflow:

```ruby
require 'temporalio'

class YourWorkflow < Temporalio::Workflow::Definition
  def execute(input)
    # Execute an activity with a summary
    result = Temporalio::Workflow.execute_activity(
      'YourActivity',
      input,
      start_to_close_timeout: 10,
      summary: 'Processing user data'
    )

    result
  end
end
```

Similarly, you can attach a `summary:` to timers within a Workflow:

```ruby
require 'temporalio'

class YourWorkflow < Temporalio::Workflow::Definition
  def execute(input)
    # Create a timer with a summary
    Temporalio::Workflow.sleep(300, summary: 'Waiting for payment confirmation')

    'Timer completed'
  end
end
```

The input format for `summary:` is a string, and limited to 200 bytes.

## Viewing Summary and Details in the UI

Once you've added summaries and details to your Workflows, Activities, and Timers, you can view this enriched information in the Temporal Web UI.
Navigate to your Workflow's details page to see the metadata displayed in two key locations:

### Workflow Overview Section

At the top of the workflow details page, you'll find the workflow-level metadata:

- **Summary & Details** - Displays the static summary and static details set when starting the workflow
- **Current Details** - Displays the dynamic details that can be updated during workflow execution

All Workflow details support standard Markdown formatting (excluding images, HTML, and scripts), allowing you to create rich, structured information displays.

### Event History

Individual events in the Workflow's Event History display their associated summaries when available:

Workflow, Activity and Timer summaries appear in purple text next to their corresponding Events, providing immediate context without requiring you to expand the event details. When you do expand an event, the summary is also prominently displayed in the detailed view.

---

## Client - Ruby SDK(Platform)

![Ruby SDK Banner](/img/assets/banner-ruby-temporal.png)

## Platform

- [Observability](/develop/ruby/platform/observability)
- [Enriching the UI](/develop/ruby/platform/enriching-ui)

---

## Observability - Ruby SDK

This page covers capabilities related to viewing the state of the application, including:

- [Metrics](#metrics)
- [Tracing](#tracing)
- [Logging](#logging)
- [Visibility](#visibility)

The observability guide covers the many ways to view the current state of your [Temporal Application](/temporal#temporal-application).
This includes viewing [Workflow Executions](/workflow-execution) tracked by the [Temporal Platform](/temporal#temporal-platform), as well as inspecting state at any point during execution.

## Emit metrics {/* #metrics */}

Each Temporal SDK can optionally emit metrics from either the Client or Worker process.
Metrics can be scraped by systems like Prometheus, and graphs can be created using tools like Grafana.

- For an overview of Prometheus and Grafana integration, refer to the [Monitoring](/self-hosted-guide/monitoring) guide.
- For a list of metrics, see the [SDK metrics reference](/references/sdk-metrics).

Metrics in Ruby are configured on the `metrics` argument of the `telemetry` argument when creating a global `Temporalio::Runtime`. That object should be created globally and should be used for all clients; therefore, you should configure this before any other Temporal code.

## Set a Prometheus endpoint

The following example exposes a Prometheus endpoint on port `9000`.

```ruby
Temporalio::Runtime.default = Temporalio::Runtime.new(
  telemetry: Temporalio::Runtime::TelemetryOptions.new(
    metrics: Temporalio::Runtime::MetricsOptions.new(
      prometheus: Temporalio::Runtime::PrometheusMetricsOptions.new(
        bind_address: '0.0.0.0:9000'
      )
    )
  )
)
```

### Custom metric handling

Instead of Prometheus or OpenTelemetry, an instance of `Temporalio::Runtime::MetricBuffer` can be provided as a `buffer` argument to the `MetricsOptions`.
`retrieve_updates` can then be periodically called on the buffer to get metric updates.

## Setup Tracing {/* #tracing */}

Tracing enables observability into the sequence of calls across your application, including Workflows and Activities.

OpenTelemetry tracing for clients, activities, and workflows can be enabled using the `Temporalio::Contrib::OpenTelemetry::TracingInterceptor`. Specifically, when creating a client, set the interceptor like so:

```ruby
require 'opentelemetry/api'
require 'opentelemetry/sdk'
require 'temporalio/client'
require 'temporalio/contrib/open_telemetry'
