# Bad - different result on every replay

value = random.randint(1, 100)
```

#### Current time

Use [`workflow.now()`](https://python.temporal.io/temporalio.workflow.html#now) instead of `datetime.now()` or `time.time()`. The SDK returns the time of the last Workflow Task, which is consistent across replays:

```python
current_time = workflow.now()
```

#### Detecting replay (advanced)

Use [`workflow.unsafe.is_replaying`](https://python.temporal.io/temporalio.workflow.html#is_replaying) to guard code that should only run on the first execution, such as emitting metrics or sending external notifications from an [Interceptor](/develop/python/workers/interceptors).
:::caution

Never use this to affect Workflow business logic — branching on replay status breaks determinism.

:::

```python
if not workflow.unsafe.is_replaying():
    emit_metric("workflow_started", 1)
```

If your goal is to always take action when something new is happening, check that `workflow.unsafe.is_replaying_history_events()` is false instead. This will be false during read-only operations like queries and update validators.  This is what the SDK's built-in logger and tracing interceptors use internally.

---

## Cancellation - Python SDK

You can interrupt a Workflow Execution in one of the following ways:

- [Cancel](#cancellation): Canceling a Workflow provides a graceful way to stop Workflow Execution.
- [Terminate](#termination): Terminating a Workflow forcefully stops Workflow Execution.

Terminating a Workflow forcefully stops Workflow Execution. This action resembles killing a process.

- The system records a `WorkflowExecutionTerminated` event in the Event History.
- The termination forcefully and immediately stops the Workflow Execution.
- The Workflow code gets no chance to handle termination.
- A Workflow Task doesn't get scheduled.

In most cases, canceling is preferable because it allows the Workflow to finish gracefully. Terminate only if the
Workflow is stuck and cannot be canceled normally.

## Cancel a Workflow Execution {/* #cancellation */}

Canceling a Workflow provides a graceful way to stop Workflow Execution. This action resembles sending a `SIGTERM` to a
process.

- The system records a `WorkflowExecutionCancelRequested` event in the Event History.
- A Workflow Task gets scheduled to process the cancelation.
- The Workflow code can handle the cancelation and execute any cleanup logic.
- The system doesn't forcefully stop the Workflow.

To cancel a Workflow Execution in Python, use the
[cancel()](https://python.temporal.io/temporalio.client.WorkflowHandle.html#cancel) function on the Workflow handle.

```python
await client.get_workflow_handle("your_workflow_id").cancel()
```

### Cancel an Activity from a Workflow {/* #cancel-activity */}

Canceling an Activity from within a Workflow requires that the Activity Execution sends Heartbeats and sets a Heartbeat
Timeout. If the Heartbeat is not invoked, the Activity cannot receive a cancellation request. When any non-immediate
Activity is executed, the Activity Execution should send Heartbeats and set a
[Heartbeat Timeout](/encyclopedia/detecting-activity-failures#heartbeat-timeout) to ensure that the server knows it is
still working.

When an Activity is canceled, an error is raised in the Activity at the next available opportunity. If cleanup logic
needs to be performed, it can be done in a `finally` clause or inside a caught cancel error. However, for the Activity
to appear canceled the exception needs to be re-raised.

:::note

Unlike regular Activities, [Local Activities](/local-activity) can be canceled if they don't send Heartbeats. Local
Activities are handled locally, and all the information needed to handle the cancellation logic is available in the same
Worker process.

:::

To cancel an Activity from a Workflow Execution, call the
[cancel()](https://docs.python.org/3/library/asyncio-task.html#asyncio.Task.cancel) method on the Activity handle that
is returned from [start_activity()](https://python.temporal.io/temporalio.workflow.html#start_activity).

```python
@activity.defn
async def cancellable_activity(input: ComposeArgsInput) -> NoReturn:
    try:
        while True:
            print("Heartbeating cancel activity")
            await asyncio.sleep(0.5)
            activity.heartbeat("some details")
    except asyncio.CancelledError:
        print("Activity cancelled")
        raise

@activity.defn
async def run_activity(input: ComposeArgsInput):
    print("Executing activity")
    return input.arg1 + input.arg2

@workflow.defn
 class GreetingWorkflow:
     @workflow.run
     async def run(self, input: ComposeArgsInput) -> None:
        activity_handle = workflow.start_activity(
            cancellable_activity,
            ComposeArgsInput(input.arg1, input.arg2),
            start_to_close_timeout=timedelta(minutes=5),
            heartbeat_timeout=timedelta(seconds=30),
        )

        await asyncio.sleep(3)
        activity_handle.cancel()
```

:::note

The Activity handle is a Python task. By calling `cancel()`, you're essentially requesting the task to be canceled.

:::

## Terminate a Workflow Execution {/* #termination */}

Terminating a Workflow forcefully stops Workflow Execution. This action resembles killing a process.

- The system records a `WorkflowExecutionTerminated` event in the Event History.
- The termination forcefully and immediately stops the Workflow Execution.
- The Workflow code gets no chance to handle termination.
- A Workflow Task doesn't get scheduled.

To terminate a Workflow Execution in Python, use the
[terminate()](https://python.temporal.io/temporalio.client.WorkflowHandle.html#terminate) function on the Workflow
handle.

```python
await client.get_workflow_handle("your_workflow_id").terminate()
```

## Reset a Workflow Execution {/* #reset */}

Resetting a Workflow Execution terminates the current Workflow Execution and starts a new Workflow Execution from a
point you specify in its Event History. Use reset when a Workflow is blocked due to a non-deterministic error or other
issues that prevent it from completing.

When you reset a Workflow, the Event History up to the reset point is copied to the new Workflow Execution, and the
Workflow resumes from that point with the current code. Reset only works if you've fixed the underlying issue, such as
removing non-deterministic code. Any progress made after the reset point will be discarded. Provide a reason when
resetting, as it will be recorded in the Event History.

<Tabs>

<TabItem value="web-ui" label="Web UI">

1. Navigate to the Workflow Execution details page,
2. Click the **Reset** button in the top right dropdown menu,
3. Select the Event ID to reset to,
4. Provide a reason for the reset,
5. Confirm the reset.

The Web UI shows available reset points and creates a link to the new Workflow Execution after the reset completes.

</TabItem>

<TabItem value="cli" label="Temporal CLI">

Use the `temporal workflow reset` command to reset a Workflow Execution:

```bash
temporal workflow reset \
    --workflow-id <workflow-id> \
    --event-id <event-id> \
    --reason "Reason for reset"
```

For example:

```bash
temporal workflow reset \
    --workflow-id my-background-check \
    --event-id 4 \
    --reason "Fixed non-deterministic code"
```

By default, the command resets the latest Workflow Execution in the `default` Namespace. Use `--run-id` to reset a
specific run. Use `--namespace` to specify a different Namespace:

```bash
temporal workflow reset \
    --workflow-id my-background-check \
    --event-id 4 \
    --reason "Fixed non-deterministic code" \
    --namespace my-namespace \
    --tls-cert-path /path/to/cert.pem \
    --tls-key-path /path/to/key.pem
```

Monitor the new Workflow Execution after resetting to ensure it completes successfully.

</TabItem>

</Tabs>

---

## Child Workflows - Python SDK

This page shows how to do the following:

- [Start a Child Workflow Execution](#child-workflows)
- [Set a Parent Close Policy](#parent-close-policy)

## Start a Child Workflow Execution {/* #child-workflows */}

**How to start a Child Workflow Execution using the Temporal Python SDK.**

A [Child Workflow Execution](/child-workflows) is a Workflow Execution that is scheduled from within another Workflow using a Child Workflow API.

When using a Child Workflow API, Child Workflow related Events ([StartChildWorkflowExecutionInitiated](/references/events#startchildworkflowexecutioninitiated), [ChildWorkflowExecutionStarted](/references/events#childworkflowexecutionstarted), [ChildWorkflowExecutionCompleted](/references/events#childworkflowexecutioncompleted), etc...) are logged in the Workflow Execution Event History.

The [ChildWorkflowExecutionStarted](/references/events#childworkflowexecutionstarted) Event must be logged to the Event History before the Parent Workflow completes to ensure the Child Workflow has started.
In Python, awaiting `start_child_workflow()` or `execute_child_workflow()` internally waits for this Event before returning, so the Child Workflow is guaranteed to have started once the call resolves.
If you start a Child Workflow from a non-main coroutine (for example, a Signal or Update handler), make sure the Parent Workflow doesn't complete before that call resolves.

To spawn a Child Workflow Execution in Python, use the [`execute_child_workflow()`](https://python.temporal.io/temporalio.workflow.html#execute_child_workflow) function which starts the Child Workflow and waits for completion or
use the [`start_child_workflow()`](https://python.temporal.io/temporalio.workflow.html#start_child_workflow) function to start a Child Workflow and return its handle.
This is useful if you want to do something after it has only started, or to get the Workflow/Run ID, or to be able to signal it while running.

:::note

`execute_child_workflow()` is a helper function for `start_child_workflow()` plus `await handle`.

:::

    View the source code
  {' '}
  in the context of the rest of the application code.

```python
