# Terminate
handle.terminate
```

Workflow Executions can also be Terminated directly from the WebUI. In this case, a custom note can be logged from the
UI when that happens.

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

## Child Workflows - Ruby SDK

This page shows how to do the following:

- [Start a Child Workflow Execution](#child-workflows) using the Ruby SDK
- [Set a Parent Close Policy](#parent-close-policy) using the Ruby SDK

## Start a Child Workflow Execution {/* #child-workflows */}

A [Child Workflow Execution](/child-workflows) is a Workflow Execution that is scheduled from within another Workflow using a Child Workflow API.

When using a Child Workflow API, Child Workflow related Events ([StartChildWorkflowExecutionInitiated](/references/events#startchildworkflowexecutioninitiated), [ChildWorkflowExecutionStarted](/references/events#childworkflowexecutionstarted), [ChildWorkflowExecutionCompleted](/references/events#childworkflowexecutioncompleted), etc...) are logged in the Workflow Execution Event History.

The [ChildWorkflowExecutionStarted](/references/events#childworkflowexecutionstarted) Event must be logged to the Event History before the Parent Workflow completes to ensure the Child Workflow has started.
In Ruby, calling `start_child_workflow` or `execute_child_workflow` internally waits for this Event before returning, so the Child Workflow is guaranteed to have started once the call returns.

To spawn a Child Workflow Execution in Ruby, use the `execute_child_workflow` method which starts the Child Workflow and waits for completion or
use the `start_child_workflow` method to start a Child Workflow and return its handle.
This is useful if you want to do something after it has only started, or to get the Workflow/Run ID, or to be able to signal it while running.

:::note

`execute_child_workflow` is a helper method for `start_child_workflow(...).result`.

:::

```ruby
Temporalio::Workflow.execute_child_workflow(MyChildWorkflow, 'my-workflow-arg')
```

## Set a Parent Close Policy {/* #parent-close-policy */}

A [Parent Close Policy](/parent-close-policy) determines what happens to a Child Workflow Execution if its Parent changes to a Closed status (Completed, Failed, or Timed Out).

The default Parent Close Policy option is set to terminate the Child Workflow Execution.

Set the `parent_close_policy` parameter for `execute_child_workflow` or `start_child_workflow` to specify the behavior of the Child Workflow when the Parent Workflow closes.

```ruby
Temporalio::Workflow.execute_child_workflow(
  MyChildWorkflow,
  'my-workflow-arg',
  parent_close_policy: Temporalio::Workflow::ParentClosePolicy::ABANDON
)
```

---

## Continue-As-New - Ruby SDK

This page describes how to Continue-As-New using the Temporal Ruby SDK.

[Continue-As-New](/workflow-execution/continue-as-new) enables a Workflow Execution to close successfully and create a new Workflow Execution in a single atomic operation if the number of Events in the Event History is becoming too large.
The Workflow Execution spawned from the use of Continue-As-New has the same Workflow Id, a new Run Id, and a fresh Event History and is passed all the appropriate parameters.

:::caution

As a precautionary measure, the Workflow Execution's Event History is limited to [51,200 Events](https://github.com/temporalio/temporal/blob/e3496b1c51bfaaae8142b78e4032cc791de8a76f/service/history/configs/config.go#L382) or [50 MB](https://github.com/temporalio/temporal/blob/e3496b1c51bfaaae8142b78e4032cc791de8a76f/service/history/configs/config.go#L380) and will warn you after 10,240 Events or 10 MB.

:::

To prevent a Workflow Execution Event History from exceeding this limit and failing, use Continue-As-New to start a new Workflow Execution with a fresh Event History.

A very large Event History can adversely affect the performance of a Workflow Execution.
For example, in the case of a Workflow Worker failure, the full Event History must be pulled from the Temporal Service and given to another Worker via a Workflow Task.
If the Event history is very large, it may take some time to load it.

The Continue-As-New feature enables developers to complete the current Workflow Execution and start a new one atomically.

The new Workflow Execution has the same Workflow Id, but a different Run Id, and has its own Event History.

## Continue-As-New in Ruby {/* #continue-as-new */}

To Continue-As-New in Ruby, raise a `Temporalio::Workflow::ContinueAsNewError` from inside your Workflow, which will stop the Workflow immediately and Continue-As-New.

```ruby
raise Temporalio::Workflow::ContinueAsNewError.new('my-new-arg')
```

:::warning Using Continue-as-New and Updates

- Temporal _does not_ support Continue-as-New functionality within Update handlers.
- Complete all handlers _before_ using Continue-as-New.
- Use Continue-as-New from your main Workflow Definition method, just as you would complete or fail a Workflow Execution.

:::

---

## Dynamic Workflow - Ruby SDK

## Set a Dynamic Workflow {/* #set-a-dynamic-workflow */}

A Dynamic Workflow in Temporal is a Workflow that is invoked dynamically at runtime if no other Workflow with the same name is registered.
A Workflow can be made dynamic by invoking `workflow_dynamic` class method at the top of the definition.
You must register the Workflow with the Worker before it can be invoked.
Only one Dynamic Workflow can be present on a Worker.

Often, dynamic is used in conjunction with `workflow_raw_args` which does not convert arguments but instead passes them
through as a splatted array of `Temporalio::Converters::RawValue` instances.

```ruby
class MyDynamicWorkflow < Temporalio::Workflow::Definition
  # Make this the dynamic workflow and accept raw args
  workflow_dynamic
  workflow_raw_args

  def execute(*raw_args)
    # Require a single arg for our workflow
    raise Temporalio::Error::ApplicationError, 'One arg expected' unless raw_args.size == 1

    # Use payload converter to convert it
    name = Temporalio::Workflow.payload_converter.from_payload(raw_args.first.payload)
    Temporalio::Workflow.execute_activity(
      MyActivity,
      { greeting: 'Hello', name: },
      start_to_close_timeout: 100
    )
  end
end
```

---

## Workflow futures - Ruby SDK

## Workflow Futures {/* #workflow-futures */}

`Temporalio::Workflow::Future` can be used for running things in the background or concurrently.
Temporal provides Workflow-safe wrappers around some core language features in cases like these.
`Temporalio::Workflow::Future` is a safe wrapper around `Fiber.schedule` for running multiple Activities at once.
The Ruby SDK also provides `Workflow.wait_condition` for awaiting a result.

Futures are never used implicitly, but they work with all Workflow code and constructs.
For instance, to run 3 activities and wait for them all to complete, something like this can be written:

```ruby
