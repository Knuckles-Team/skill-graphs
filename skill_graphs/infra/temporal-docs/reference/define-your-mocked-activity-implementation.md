# Define your mocked Activity implementation
@activity.defn(name="compose_greeting")
async def compose_greeting_mocked(input: ComposeGreetingInput) -> str:
    return f"{input.greeting}, {input.name} from mocked activity!"

async def test_mock_activity(client: Client):
    task_queue_name = str(uuid.uuid4())
    # Provide the mocked Activity implementation to the Worker
    async with Worker(
        client,
        task_queue=task_queue_name,
        workflows=[GreetingWorkflow],
        activities=[compose_greeting_mocked],
    ):
        # Execute your Workflow as usual
        assert "Hello, World from mocked activity!" == await client.execute_workflow(
            GreetingWorkflow.run,
            "World",
            id=str(uuid.uuid4()),
            task_queue=task_queue_name,
        )
```

The mocked Activity implementation should have the same signature as the real implementation (including the input and output types) and the same name.
When the Workflow invokes the Activity, it invokes the mocked implementation instead of the real one, allowing you to test your Workflow isolated.

### How to skip time {/* #skip-time */}

Some long-running Workflows can persist for months or even years.
Implementing the test framework allows your Workflow code to skip time and complete your tests in seconds rather than the Workflow's specified amount.

For example, if you have a Workflow sleep for a day, or have an Activity failure with a long retry interval, you don't need to wait the entire length of the sleep period to test whether the sleep function works.
Instead, test the logic that happens after the sleep by skipping forward in time and complete your tests in a timely manner.

The test framework included in most SDKs is an in-memory implementation of Temporal Server that supports skipping time.
Time is a global property of an instance of `TestWorkflowEnvironment`: skipping time (either automatically or manually) applies to all currently running tests.
If you need different time behaviors for different tests, run your tests in a series or with separate instances of the test server.
For example, you could run all tests with automatic time skipping in parallel, and then all tests with manual time skipping in series, and then all tests without time skipping in parallel.

#### Skip time automatically {/* #automatic-method */}

You can skip time automatically in the SDK of your choice.
Start a test server process that skips time as needed.
For example, in the time-skipping mode, Timers, which include sleeps and conditional timeouts, are fast-forwarded except when Activities are running.

Use the [`start_time_skipping()`](https://python.temporal.io/temporalio.testing.WorkflowEnvironment.html#start_time_skipping) method to start a test server process and skip time automatically.

Use the [`start_local()`](https://python.temporal.io/temporalio.testing.WorkflowEnvironment.html#start_local) method for a full local Temporal Server.

Use the [`from_client()`](https://python.temporal.io/temporalio.testing.WorkflowEnvironment.html#from_client) method for an existing Temporal Server.

#### Skip time manually {/* #manual-method */}

Skip time manually in the SDK of your choice.

To implement time skipping, use the [`start_time_skipping()`](https://python.temporal.io/temporalio.testing.WorkflowEnvironment.html#start_time_skipping) static method.

```python
from temporalio.testing import WorkflowEnvironment

async def test_manual_time_skipping():
    async with await WorkflowEnvironment.start_time_skipping() as env:
        # Your code here
        # You can use the env.sleep(seconds) method to manually advance time
        await env.sleep(3) # This will advance time by 3 seconds
        # Your code here
```

### Assert in Workflow {/* #assert-in-workflow */}

The `assert` statement is a convenient way to insert debugging assertions into the Workflow context.

The `assert` method is available in Python and TypeScript.

For information about assert statements in Python, see [`assert`](https://docs.python.org/3/reference/simple_stmts.html#the-assert-statement) in the Python Language Reference.

## How to Replay a Workflow Execution {/* #replay */}

Replay recreates the exact state of a Workflow Execution.
You can replay a Workflow from the beginning of its Event History.

Replay succeeds only if the [Workflow Definition](/workflow-definition) is compatible with the provided history from a deterministic point of view.

When you test changes to your Workflow Definitions, we recommend doing the following as part of your CI checks:

1. Determine which Workflow Types or Task Queues (or both) will be targeted by the Worker code under test.
2. Download the Event Histories of a representative set of recent open and closed Workflows from each Task Queue, either programmatically using the SDK client or via the Temporal CLI.
3. Run the Event Histories through replay.
4. Fail CI if any error is encountered during replay.

The following are examples of fetching and replaying Event Histories:

To replay Workflow Executions, use the [`replay_workflows`](https://python.temporal.io/temporalio.worker.Replayer.html#replay_workflows) or [`replay_workflow`](https://python.temporal.io/temporalio.worker.Replayer.html#replay_workflow) methods, passing one or more Event Histories as arguments.

In the following example (which, as of server v1.18, requires Advanced Visibility to be enabled), Event Histories are downloaded from the server and then replayed.
If any replay fails, the code raises an exception.

```python
workflows = client.list_workflows(f"TaskQueue=foo and StartTime > '2022-01-01T12:00:00'")
histories = workflows.map_histories()
replayer = Replayer(
    workflows=[MyWorkflowA, MyWorkflowB, MyWorkflowC]
)
await replayer.replay_workflows(histories)
```

In the next example, a single history is loaded from a JSON string:

```python
replayer = Replayer(workflows=[YourWorkflow])
await replayer.replay_workflow(WorkflowHistory.from_json(history_json_str))
```

In both examples, if Event History is non-deterministic, an error is thrown.
You can choose to wait until all histories have been replayed with `replay_workflows` by setting the `fail_fast` option to `false`.

:::note

If the Event History is exported by [Temporal Web UI](/web-ui) or through [Temporal CLI](/cli), you can pass the JSON file history object as a JSON string or as a Python dictionary through the `json.load()` function, which takes a file object and returns the JSON object.

:::tip
When fetching event histories directly from the server or exporting them, be aware that the data can be protobuf-encoded (`bytes`). The `Replayer`, however, often works with decoded histories (like a `dict`).

If you encounter `TypeError` exceptions related to `dict` vs. `bytes` mismatches during replay, ensure your event history is properly decoded before passing it to the Replayer.
:::

---

## Client - Python SDK

![Python SDK Banner](/img/assets/banner-python-temporal.png)

## Temporal Client

- [Temporal Client](/develop/python/client/temporal-client)

---

## Temporal Client - Python SDK

A [Temporal Client](/encyclopedia/temporal-sdks#temporal-client) enables you to communicate with the Temporal Service.
Communication with a Temporal Service lets you perform actions such as starting Workflow Executions, sending Signals and
Queries to Workflow Executions, getting Workflow results, and more.

This page shows you how to do the following using the Python SDK with the Temporal Client:

- [Connect to a local development Temporal Service](#connect-to-development-service)
- [Connect to Temporal Cloud](#connect-to-temporal-cloud)
- [Start a Workflow Execution](#start-workflow-execution)
- [Get Workflow results](#get-workflow-results)

A Temporal Client cannot be initialized and used inside a Workflow. However, it is acceptable and common to use a
Temporal Client inside an Activity to communicate with a Temporal Service.

## Connect to development Temporal Service {/* #connect-to-development-service */}

Use [`Client.connect`](https://python.temporal.io/temporalio.client.Client.html#connect) to create a client. Connection
options include the Temporal Server address, Namespace, and (optionally) TLS configuration. You can provide these
options directly in code, load them from **environment variables**, or a **TOML configuration file** using the
[`envconfig`](https://python.temporal.io/temporalio.envconfig.html) helpers. We recommend environment variables or a
configuration file for secure, repeatable configuration.

When you’re running a Temporal Service locally (such as with the
[Temporal CLI dev server](https://docs.temporal.io/cli/command-reference/server#start-dev)), the required options are minimal. If you
don't specify a host/port, most connections default to `127.0.0.1:7233` and the `default` Namespace.

<Tabs groupId="connect-options" defaultValue="config-file" >

<TabItem value="config-file" label="Configuration File">

You can use a TOML configuration file to set connection options for the Temporal Client. The configuration file lets you
configure multiple profiles, each with its own set of connection options. You can then specify which profile to use when
creating the Temporal Client. You can use the environment variable `TEMPORAL_CONFIG_FILE` to specify the location of the
TOML file or provide the path to the file directly in code. If you don't provide the configuration file path, the SDK
looks for it at the path `~/.config/temporalio/temporal.toml` or the equivalent on your OS. Refer to
[Environment Configuration](/develop/environment-configuration#configuration-methods) for more details about
configuration files and profiles.

:::info

The connection options set in configuration files have lower precedence than environment variables. This means that if
you set the same option in both the configuration file and as an environment variable, the environment variable value
overrides the option set in the configuration file.

:::

For example, the following TOML configuration file defines two profiles: `default` and `prod`. Each profile has its own
set of connection options.

```toml title="config.toml"
