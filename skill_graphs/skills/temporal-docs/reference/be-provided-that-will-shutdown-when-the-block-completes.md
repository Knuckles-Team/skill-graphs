# be provided that will shutdown when the block completes
worker.run(shutdown_signals: ['SIGINT'])
```

To run multiple workers, `Temporalio::Worker.run_all` may be used instead.

All Workers listening to the same Task Queue name must be registered to handle the exact same Workflows Types and Activity Types.

If a Worker polls a Task for a Workflow Type or Activity Type it does not know about, it fails that Task.
However, the failure of the Task does not cause the associated Workflow Execution to fail.

---

## Workflow basics - Ruby SDK

## Develop a Workflow {/* #develop-workflow */}

Workflows are the fundamental unit of a Temporal Application, and it all starts with the development of a [Workflow Definition](/workflow-definition).

In the Temporal Ruby SDK programming model, Workflows are defined as classes.

Have the Workflow class extend `Temporalio::Workflow::Definition` to define a Workflow.

The entrypoint is the `execute` method.

```ruby
class MyWorkflow < Temporalio::Workflow::Definition
  def execute(name)
    Temporalio::Workflow.execute_activity(
      MyActivity,
      { greeting: 'Hello', name: },
      start_to_close_timeout: 100
    )
  end
end
```

Temporal Workflows may have any number of custom parameters.
However, we strongly recommend that hashes or objects are used as parameters, so that the object's individual fields may be altered without breaking the signature of the Workflow.

### Workflow Logic Requirements {/* #workflow-logic-requirements */}

Temporal Workflows [must be deterministic](https://docs.temporal.io/workflows#deterministic-constraints), which includes
Ruby workflows. This means there are several things workflows cannot do such as:

- Perform IO (network, disk, stdio, etc)
- Access/alter external mutable state
- Do any threading
- Do anything using the system clock (e.g. `Time.Now`)
- Make any random calls
- Make any not-guaranteed-deterministic calls

To prevent illegal workflow calls, a call tracer is put on the workflow thread that raises an exception if any illegal
calls are made.
Which calls are illegal is configurable in the worker options.

### Customize Workflow Type {/* #workflow-type */}

Workflows have a Type that are referred to as the Workflow name.

The following examples demonstrate how to set a custom name for your Workflow Type.

You can customize the Workflow name with a custom name in a `workflow_name` class method call on the class.
The Workflow name defaults to the unqualified class name.

```ruby
class MyWorkflow < Temporalio::Workflow::Definition
  # Customize the name
  workflow_name :MyDifferentWorkflowName

  def execute(name)
    Temporalio::Workflow.execute_activity(
      MyActivity,
      { greeting: 'Hello', name: },
      start_to_close_timeout: 100
    )
  end
end
```

---

## Cancellation - Ruby SDK

This page shows how to interrupt a Workflow Execution.

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

## Cancellation {/* #cancellation */}

To give a Workflow and its Activities the ability to be cancelled, do the following:

- Handle a Cancellation request within a Workflow.
- Set Activity Heartbeat Timeouts.
- Listen for and handle a Cancellation request within an Activity.
- Send a Cancellation request from a Temporal Client.

## Handle Cancellation in Workflow {/* #handle-cancellation-in-workflow */}

Workflow Definitions can be written to respond to cancellation requests. It is common for an Activity to be run on
Cancellation to perform cleanup.

Cancellation Requests on Workflows cancel the `Temporalio::Workflow.cancellation` which is a `Temporalio::Cancellation`
that effectively serves as a cancellation token. This is the cancellation that is implicitly used for all calls within
the workflow as well (e.g. Timers, Activities, etc) and therefore cancellation is propagated to them to be handled and
bubble out.

```ruby
class MyWorkflow < Temporalio::Workflow::Definition
  def execute
    # Whether this workflow waits on the activity to handle the cancellation or not is
    # dependent upon the cancellation_type parameter. We leave the default here which
    # sends the cancellation but does not wait on it to be handled.
    Temporalio::Workflow.execute_activity(MyActivity, start_to_close_timeout: 100)
  rescue Temporalio::Error => e
    # For this sample, we only want to execute cleanup when it's a cancellation
    raise unless Temporalio::Error.canceled?(e)

    # Call a cleanup activity. We have to do this with a new/detached cancellation
    # because the default workflow-level one is already canceled at this point.
    Temporalio::Workflow.execute_activity(
      MyCleanupActivity,
      start_to_close_timeout: 100,
      cancellation: Temporalio::Cancellation.new
    )

    # Re-raise the original exception
    raise
  end
end
```

## Handle Cancellation in an Activity {/* #handle-cancellation-in-an-activity */}

Ensure that the Activity is [Heartbeating](/develop/ruby/activities/timeouts#activity-heartbeats) to receive the
Cancellation request and stop execution. Also make sure that the
[Heartbeat Timeout](/develop/ruby/activities/timeouts#heartbeat-timeout) is set on the Activity Options when calling from
the Workflow. An Activity Cancellation Request raises a `Temporalio::Error::CanceledError` in the Activity.

```ruby
class MyActivity < Temporalio::Activity::Definition
  def execute
    # This is a naive loop simulating work, but similar heartbeat/cancellation logic
    # applies to other scenarios as well
    loop do
      # Send heartbeat
      Temporalio::Activity::Context.current.heartbeat
      # Sleep before heartbeating again
      sleep(3)
    end
  rescue Temporalio::Error::CanceledError
    raise 'Canceled!'
  end
end
```

## Request Cancellation {/* #request-cancellation */}

Use `cancel` on the `WorkflowHandle` to cancel a Workflow Execution.

```ruby
