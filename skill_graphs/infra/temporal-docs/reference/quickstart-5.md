# Quickstart

Configure your local development environment to get started developing with Temporal.

<SetupSteps>
<SetupStep code={
  <>
    <CodeSnippet language="bash">
    python3 -V
    </CodeSnippet>
    <CodeSnippet language="bash">
    python 3.13.3
    </CodeSnippet>
  </>
}>
## Install Python

Make sure you have Python installed. Check your version of Python with the following command.

</SetupStep>

<SetupStep code={
<>
<CodeSnippet language="bash">
mkdir temporal-project
</CodeSnippet>
<CodeSnippet language="bash">
cd temporal-project
</CodeSnippet>
<CodeSnippet language="bash">
python3 -m venv env
</CodeSnippet>
<CodeSnippet language="bash">
source env/bin/activate
</CodeSnippet>
<CodeSnippet language="bash">
pip install temporalio
</CodeSnippet>
</>
}>

## Install the Temporal Python SDK

You should install the Temporal Python SDK in your project using a virtual environment. Create a directory for your
Temporal project, switch to the new directory, create a Python virtual environment, activate it, and then install the
Temporal SDK.

Next, you'll configure a local Temporal Service for development.

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

## Install Temporal CLI

The fastest way to get a development version of the Temporal Service running on your local machine is to use
[Temporal CLI](https://docs.temporal.io/cli).

Choose your operating system to install Temporal CLI.

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

- The Temporal Python SDK is properly installed
- Your local Temporal Service is running
- You can successfully create and execute Workflows and Activities
- The communication between components is functioning correctly

### 1. Create the Activity

Create an Activity file (activities.py):

```python
from temporalio import activity

@activity.defn
async def greet(name: str) -> str:
    return f"Hello {name}"
```

An Activity is a normal function or method that executes a single, well-defined action (either short or long running),
which often involve interacting with the outside world, such as sending emails, making network requests, writing to a
database, or calling an API, which are prone to failure. If an Activity fails, Temporal automatically retries it based
on your configuration.

### 2. Create the Workflow

Create a Workflow file (workflows.py):

```python
from datetime import timedelta
from temporalio import workflow

with workflow.unsafe.imports_passed_through():
    from activities import greet

@workflow.defn
class SayHelloWorkflow:
    @workflow.run
    async def run(self, name: str) -> str:
        return await workflow.execute_activity(
            greet,
            name,
            schedule_to_close_timeout=timedelta(seconds=10),
        )
```

Workflows orchestrate Activities and contain the application logic. Temporal Workflows are resilient. They can run and
keep running for years, even if the underlying infrastructure fails. If the application itself crashes, Temporal will
automatically recreate its pre-failure state so it can continue right where it left off.

### 3. Create the Worker

Create a Worker file (worker.py):

```python

from temporalio.client import Client
from temporalio.worker import Worker
from temporalio import workflow

with workflow.unsafe.imports_passed_through():
    from workflows import SayHelloWorkflow
    from activities import greet

async def main():
    client = await Client.connect("localhost:7233")
    worker = Worker(
        client,
        task_queue="my-task-queue",
        workflows=[SayHelloWorkflow],
        activities=[greet],
    )
    print("Worker started.")
    await worker.run()

if __name__ == "__main__":
    asyncio.run(main())
```

Run the Worker by opening up a new terminal:

```bash
source env/bin/activate
python3 worker.py
```

Keep this terminal running - you should see "Worker started" displayed.

With your Activity and Workflow defined, you need a Worker to execute them. A Worker polls a Task Queue, that you
configure it to poll, looking for work to do. Once the Worker dequeues the Workflow or Activity task from the Task
Queue, it then executes that task.

Workers are a crucial part of your Temporal application as they're what actually execute the tasks defined in your
Workflows and Activities. For more information on Workers, see
[Understanding Temporal](/evaluate/understanding-temporal#workers) and a [deep dive into Workers](/workers).

### 4. Execute the Workflow

Now that your Worker is running, it's time to start a Workflow Execution.

This final step will validate that everything is working correctly with your file labeled `starter.py`.

Create a separate file called `starter.py`:

```python

from temporalio.client import Client

async def main():
    client = await Client.connect("localhost:7233")
    result = await client.execute_workflow(
        "SayHelloWorkflow",
        "Temporal",
        id=f"say-hello-workflow-{uuid.uuid4()}",
        task_queue="my-task-queue",
    )
    print("Workflow result:", result)

if __name__ == "__main__":
    asyncio.run(main())
```

While the Worker is still running, run the following command in a new terminal:

```bash
source env/bin/activate
python3 starter.py
```

### Verify Success

If everything is working correctly, you should see:

- Worker processing the Workflow and Activity
- Output: `Workflow result: Hello Temporal`
- Workflow Execution details in the [Temporal Web UI](http://localhost:8233)

<CallToAction href="https://learn.temporal.io/getting_started/python/first_program_in_python/">
  Run your first Temporal Application
  Create a basic Workflow and run it with the Temporal Python SDK
</CallToAction>

<CallToAction href="https://learn.temporal.io/courses/">
  Take a Temporal 101 course
  Learn Temporal concepts and build your first application with a guided course
</CallToAction>

---

## Workers - Python SDK

![Python SDK Banner](/img/assets/banner-python-temporal.png)

## Workers

- [Worker processes](/develop/python/workers/run-worker-process)
- [Interceptors](/develop/python/workers/interceptors)

---

## Interceptors - Python SDK

Interceptors are SDK hooks that let you intercept inbound and outbound Temporal calls. You use them to add common
behavior across many calls, such as tracing and context propagation.
This is similar to using middleware in web frameworks such as
[Django](https://docs.djangoproject.com/en/5.2/topics/http/middleware/),
[Starlette](https://www.starlette.io/middleware/), and
[Flask](https://flask.palletsprojects.com/en/stable/lifecycle/#middleware).

There are two types of interceptors--inbound and outbound.

* Outbound interceptors wrap network calls, running before they reach the network and after they return.
* Inbound interceptors run after the network hop, wrapping application code and running before it starts and after it returns.

Concretely, there are five categories of inbound and outbound calls that you can modify in this way:

| | [Outbound Client](https://python.temporal.io/temporalio.client.OutboundInterceptor.html) | [Inbound Workflow](https://python.temporal.io/temporalio.worker.WorkflowInboundInterceptor.html) | [Outbound Workflow](https://python.temporal.io/temporalio.worker.WorkflowOutboundInterceptor.html) | [Inbound Activity](https://python.temporal.io/temporalio.worker.ActivityInboundInterceptor.html) | [Outbound Activity](https://python.temporal.io/temporalio.worker.ActivityOutboundInterceptor.html) |
| --- | --- | --- | --- | --- | --- |
| **Description** | Wraps calls from your application to the Temporal Client to start a Workflow or send [Messages](/encyclopedia/workflow-message-passing/) to it | Wraps calls arriving into a [Workflow Execution](/workflow-execution), such as executing the Workflow, handling [Messages](/encyclopedia/workflow-message-passing/) | Wraps calls a [Workflow](/workflow-definition) makes to the SDK, such as scheduling [Activities](/activities), starting [Child Workflows](/child-workflows), and invoking [Nexus Operations](/nexus) | Wraps calls arriving into an [Activity Execution](/activity-execution) | Wraps calls an [Activity](/activities) makes to the SDK, such as sending [Heartbeats](/encyclopedia/detecting-activity-failures#activity-heartbeat) and reading Activity info |
| **Runs on** | Client | Worker (Workflow sandbox) | Worker (Workflow sandbox) | Worker (Activity context) | Worker (Activity context) |
| **Example methods** | `start_workflow()`, `signal_workflow()`, `list_workflows()` | `execute_workflow()`, `handle_query()`, `handle_signal()`, `handle_update_handler()` | `start_activity()`, `start_child_workflow()`, `signal_child_workflow()`, `start_nexus_operation()` | `execute_activity()` | `info()`, `heartbeat()` |

These are not exhaustive lists; refer to the linked API docs for each category.

:::warning Workflow interceptors and replay

Workflow inbound and outbound interceptor methods also execute during [replay](/develop/python/best-practices/testing-suite#replay). Use replay-safe APIs for logging, randomness, and time in these interceptors.
See [Develop Workflow logic](/develop/python/workflows/basics#workflow-logic-requirements) for details.

If you want to write generic code shared by all inbound Workflow call handlers but want to skip read-only operations, check `workflow.unsafe.is_read_only()`.

Activity and Client interceptors are not affected by replay.

:::

## Register an Interceptor {/* #register */}

Registering an interceptor means supplying an interceptor instance to the SDK so Temporal can invoke it when matching
Client or Worker calls occur. Once registered, the interceptor runs as part of the call path and can observe or modify
request and response data.

### Register on the Client

Pass interceptors in the `interceptors` argument of `Client.connect()`. Client interceptors modify outbound calls such
as starting and signaling Workflows.

```python
client = await Client.connect(
    "localhost:7233",
    interceptors=[TracingInterceptor()],
)
```

The `interceptors` list can contain multiple interceptors.
In this case they form a chain: a method implemented on an interceptor instance in the list can perform side effects, and modify the data, before passing it on to the corresponding method on the next interceptor in the list.

### Register via a Plugin

If you're building a reusable library or want to bundle interceptors with other primitives, you can register them through a [Plugin](/develop/plugins-guide#interceptors).

### Register on the Worker only

If your interceptor doesn't affect the Client, you can pass interceptors in the `interceptors` argument of `Worker()`.
Worker interceptors modify inbound and outbound Workflow and Activity calls.

```python
worker = Worker(
    client,
    task_queue="my-task-queue",
    interceptors=[SomeWorkerInterceptor()],
    # ...
)
```

:::note

If your interceptor class inherits from both `client.Interceptor` and `worker.Interceptor`, pass it to
`Client.connect()` rather than the `Worker()` constructor. The Worker will use interceptors from its underlying Client
automatically.

:::

## How to implement Interceptors in Python

Interceptors run as a chain.  Each interceptor wraps the entire inner call: your code runs before the call, invokes `next` to execute the rest of the chain, and then runs after the call completes. This means you can inspect or modify both the `input` and the result, handle errors, and perform side effects at either stage.

### Implementing Client call Interceptors

To modify outbound Client calls, define a class inheriting from
[`client.Interceptor`](https://python.temporal.io/temporalio.client.Interceptor.html), and implement the method
`intercept_client()` to return an instance of
[`OutboundInterceptor`](https://python.temporal.io/temporalio.client.OutboundInterceptor.html) that implements the
subset of outbound Client calls that you wish to modify.

This example implements an Interceptor on outbound Client calls that sets a certain key in the outbound `headers` field.
A User ID is context-propagated by being sent in a header field with outbound requests:

```python
class ContextPropagationInterceptor(
    temporalio.client.Interceptor, temporalio.worker.Interceptor
):
    def __init__(
        self,
        payload_converter: temporalio.converter.PayloadConverter = temporalio.converter.default().payload_converter,
    ) -> None:
        self._payload_converter = payload_converter

    def intercept_client(
        self, next: temporalio.client.OutboundInterceptor
    ) -> temporalio.client.OutboundInterceptor:
        return _ContextPropagationClientOutboundInterceptor(
            next, self._payload_converter
        )

def set_header_from_context(
    input: _InputWithHeaders, payload_converter: temporalio.converter.PayloadConverter
) -> None:
    user_id_val = user_id.get()
    if user_id_val:
        input.headers = {
            **input.headers,
            HEADER_KEY: payload_converter.to_payload(user_id_val),
        }

class _ContextPropagationClientOutboundInterceptor(
    temporalio.client.OutboundInterceptor
):
    def __init__(
        self,
        next: temporalio.client.OutboundInterceptor,
        payload_converter: temporalio.converter.PayloadConverter,
    ) -> None:
        super().__init__(next)
        self._payload_converter = payload_converter

    async def start_workflow(
        self, input: temporalio.client.StartWorkflowInput
    ) -> temporalio.client.WorkflowHandle[Any, Any]:
        set_header_from_context(input, self._payload_converter)
        return await super().start_workflow(input)
```

It often happens that your Worker and Client interceptors will share code because they implement closely related logic.
In the Python SDK, you will typically want to create an interceptor class that inherits from _both_ `client.Interceptor`
and `worker.Interceptor` as above, since their method sets do not overlap.

You can then [register](#register) this interceptor in your client/starter code.

Your interceptor classes need not implement every method; the default implementation is always to pass the data on to the next method in the interceptor chain.
During execution, when the SDK encounters an Inbound Activity call, it will look to the first Interceptor instance, get hold of the appropriate intercepted method, and call it.
The intercepted method will perform its function then call the same method on the next Interceptor in the chain.
At the end of the chain the SDK will call the "real" SDK method.

### Implementing Worker call Interceptors

To modify inbound and outbound Workflow and Activity calls, define a class inheriting from `worker.Interceptor`. This is
an interface with two methods named `intercept_activity` and `workflow_interceptor_class`, which you can use to
configure interceptions of Activity and Workflow calls, respectively. `intercept_activity` returns an
`ActivityInboundInterceptor`.

This example demonstrates using an interceptor to measure [Schedule-To-Start](/encyclopedia/detecting-activity-failures#schedule-to-start-timeout) and Schedule-To-Close latency.
Notice how the interceptor wraps the call: it records Schedule-To-Start before `execute_activity`, then records Schedule-To-Close after it completes:

```python
from datetime import datetime, timezone
from temporalio import activity
from temporalio.worker import (
    ActivityInboundInterceptor,
    ExecuteActivityInput,
    Interceptor,
    Worker,
)

class SimpleWorkerInterceptor(Interceptor):
    def intercept_activity(
        self, next: ActivityInboundInterceptor
    ) -> ActivityInboundInterceptor:
        return ActivityMetricsInterceptor(next)

class ActivityMetricsInterceptor(ActivityInboundInterceptor):
    async def execute_activity(self, input: ExecuteActivityInput):
        info = activity.info()
        meter = activity.metric_meter()
        attrs = {"workflow_type": info.workflow_type}

        # Before the activity executes: record Schedule-To-Start
        schedule_to_start = info.started_time - info.current_attempt_scheduled_time
        meter.create_histogram_timedelta(
            "custom_activity_schedule_to_start_latency",
            description="Time between activity scheduling and start",
            unit="duration",
        ).record(schedule_to_start, attrs)

        # Execute the activity
        result = await self.next.execute_activity(input)

        # After the activity completes: record Schedule-To-Close
        elapsed = datetime.now(timezone.utc) - info.current_attempt_scheduled_time
        meter.create_histogram_timedelta(
            "custom_activity_schedule_to_close_latency",
            description="Time between activity scheduling and completion",
            unit="duration",
        ).record(elapsed, attrs)

        return result

client = await Client.connect(
    "localhost:7233",
)
worker = Worker(
    client,
    interceptors=[SimpleWorkerInterceptor()],
    # ...
)
```

The `workflow_interceptor_class` returns a `WorkflowInboundInterceptor` that works similarly to
`ActivityInboundInterceptor`.

---

## Worker processes - Python SDK

## Run a Worker Process {/* #run-a-dev-worker */}

**How to run a Worker Process using the Temporal Python SDK.**

The [Worker Process](/workers#worker-process) is where Workflow Functions and Activity Functions are executed.

- Each [Worker Entity](/workers#worker-entity) in the Worker Process must register the exact Workflow Types and Activity
  Types it may execute.
- Each Worker Entity must also associate itself with exactly one [Task Queue](/task-queue).
- Each Worker Entity polling the same Task Queue must be registered with the same Workflow Types and Activity Types.

A [Worker Entity](/workers#worker-entity) is the component within a Worker Process that listens to a specific Task
Queue.

Although multiple Worker Entities can be in a single Worker Process, a single Worker Entity Worker Process may be
perfectly sufficient. For more information, see the [Worker tuning guide](/develop/worker-performance).

A Worker Entity contains a Workflow Worker and/or an Activity Worker, which makes progress on Workflow Executions and
Activity Executions, respectively.

To develop a Worker, use the `Worker()` constructor and add your Client, Task Queue, Workflows, and Activities as
arguments. The following code example creates a Worker that polls for tasks from the Task Queue and executes the
Workflow. When a Worker is created, it accepts a list of Workflows in the workflows parameter, a list of Activities in
the activities parameter, or both.

    View the source code
  {' '}
  in the context of the rest of the application code.

```python
from temporalio.client import Client
from temporalio.worker import Worker
