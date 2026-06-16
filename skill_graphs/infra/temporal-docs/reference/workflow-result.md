# workflow result
workflow_result = start_workflow_operation.workflow_handle.result
```

## Message handler patterns {/* #message-handler-patterns */}

This section covers common write operations, such as Signal and Update handlers.
It doesn't apply to pure read operations, like Queries or Update Validators.

:::tip

For additional information, see [Inject work into the main Workflow](/handling-messages#injecting-work-into-main-workflow) and [Ensuring your messages are processed exactly once](/handling-messages#exactly-once-message-processing).

:::

### Add async handlers {/* #async-handlers */}

Signal and Update handlers can be asynchronous as well as blocking.
Using asynchronous calls allows you to wait for Activities, Child Workflows, Durable Timers, wait conditions, etc.
This expands the possibilities for what can be done by a handler but it also means that handler executions and your main Workflow method are all running concurrently, with switching occurring between them at await calls.

It's essential to understand the things that could go wrong in order to use asynchronous handlers safely.
See [Workflow message passing](/encyclopedia/workflow-message-passing) for guidance on safe usage of async Signal and Update handlers, and the [Controlling handler concurrency](#control-handler-concurrency) and [Waiting for message handlers to finish](#wait-for-message-handlers) sections below.

The following code is an Activity that simulates a network call to a remote service:

```ruby
class CallGreetingService < Temporalio::Activity::Definition
  def execute(to_language)
    # Simulate a network call
    sleep(0.2)
    # This intentionally returns nil on not found
    CallGreetingService.greetings[to_language.to_sym]
  end

  def self.greetings
    @greetings ||= {
      arabic: 'مرحبا بالعالم',
      chinese: '你好，世界',
      english: 'Hello, world',
      french: 'Bonjour, monde',
      hindi: 'नमस्ते दुनिया',
      portuguese: 'Olá mundo',
      spanish: 'Hola mundo'
    }
  end
end
```

The following code is a Workflow Update for asynchronous use of the preceding Activity:

```ruby
class GreetingWorkflow < Temporalio::Workflow::Definition
  # ...

  workflow_update
  def apply_language_with_lookup(new_language)
    # Call an activity if it's not there.
    unless @greetings.include?(new_language.to_sym)
      # We use a mutex so that, if this handler is executed multiple times, each execution
      # can schedule the activity only when the previously scheduled activity has
      # completed. This ensures that multiple calls to apply_language_with_lookup are
      # processed in order.
      @apply_language_mutex ||= Mutex.new
      @apply_language_mutex.synchronize do
        greeting = Temporalio::Workflow.execute_activity(
          CallGreetingService, new_language, start_to_close_timeout: 10
        )
        # The requested language might not be supported by the remote service. If so, we
        # raise ApplicationError, which will fail the update. The
        # WorkflowExecutionUpdateAccepted event will still be added to history. (Update
        # validators can be used to reject updates before any event is written to history,
        # but they cannot be async, and so we cannot use an update validator for this
        # purpose.)
        raise Temporalio::Error::ApplicationError, "Greeting service does not support #{new_language}" unless greeting

        @greetings[new_language.to_sym] = greeting
      end
    end
    set_language(new_language)
  end
end
```

After updating the code for asynchronous calls, your Update handler can schedule an Activity and await the result.
Although an async Signal handler can initiate similar network tasks, using an Update handler allows the Client to receive a result or error once the Activity completes.
This lets your Client track the progress of asynchronous work performed by the Update's Activities, Child Workflows, etc.

### Use wait conditions {/* #block-with-wait */}

Sometimes, async Signal or Update handlers need to meet certain conditions before they should continue.
Using a wait condition with [`wait_condition`](https://ruby.temporal.io/Temporalio/Workflow.html#wait_condition-class_method) sets a function that prevents the code from proceeding until the condition is truthy.
This is an important feature that helps you control your handler logic.

Here are two important use cases for `wait_condition`:

- Waiting in a handler until it is appropriate to continue.
- Waiting in the main Workflow until all active handlers have finished.

The condition state you're waiting for can be updated by and reflect any part of the Workflow code.
This includes the main Workflow method, other handlers, or child coroutines spawned by the main Workflow method, and so forth.

#### In handlers {/* #wait-in-handlers */}

Sometimes, async Signal or Update handlers need to meet certain conditions before they should continue.
Using a wait condition with [`wait_condition`](https://ruby.temporal.io/Temporalio/Workflow.html#wait_condition-class_method) sets a function that prevents the code from proceeding until the condition is truthy.
This is an important feature that helps you control your handler logic.

Consider a `ready_for_update_to_execute` method that runs before your Update handler executes.
The `wait_condition` call waits until your condition is met:

```ruby
workflow_update
def my_update(my_update_input)
  Temporalio::Workflow.wait_condition { ready_for_update_to_execute(my_update_input) }
  # ...
end
```

Remember: Handlers can execute before the main Workflow method starts.

#### Before finishing the Workflow {/* #wait-for-message-handlers */}

Workflow wait conditions can ensure your handler completes before a Workflow finishes.
When your Workflow uses async Signal or Update handlers, your main Workflow method can return or continue-as-new while a handler is still waiting on an async task, such as an Activity result.
The Workflow completing may interrupt the handler before it finishes crucial work and cause Client errors when trying retrieve Update results.
Use `Temporalio::Workflow.all_handlers_finished?` to address this problem and allow your Workflow to end smoothly:

```ruby
class MyWorkflow < Temporalio::Workflow::Definition
  def execute
    # ...

    Temporalio::Workflow.wait_condition { Temporalio::Workflow.all_handlers_finished? }
    'workflow-result'
  end
end
```

By default, your Worker will log a warning when you allow a Workflow Execution to finish with unfinished handler executions.
You can silence these warnings on a per-handler basis by passing the `unfinished_policy` argument to the [`workflow_signal`](https://ruby.temporal.io/Temporalio/Workflow/Definition.html#workflow_signal-class_method) / [`workflow_update`](https://ruby.temporal.io/Temporalio/Workflow/Definition.html#workflow_update-class_method) class methods:

```ruby
workflow_update unfinished_policy: Temporalio::Workflow::HandlerUnfinishedPolicy::ABANDON
def my_update
  # ...
```

See [Finishing handlers before the Workflow completes](/handling-messages#finishing-message-handlers) for more information.

### Use workflow_init to access input early

The `workflow_init` class method above `initialize` gives it access to [Workflow input](/handling-messages#workflow-initializers).
When you use the `workflow_init` on your constructor, you give the constructor the same Workflow parameters as your `execute` method.
The SDK will then ensure that your constructor receives the Workflow input arguments that the [Client sent](/develop/ruby/client/temporal-client#start-workflow).
The Workflow input arguments are also passed to your `execute` method -- that always happens, whether or not you use the `workflow_init` class method above `initialize`.

Here's an example.
The constructor and `execute` must have the same parameters with the same types:

```ruby
class WorkflowInitWorkflow < Temporalio::Workflow::Definition
  workflow_init
  def initialize(input)
    @name_with_title = "Sir #{input['name']}"
  end

  def execute(input)
    Temporalio::Workflow.wait_condition { @title_has_been_checked }
    "Hello, #{@name_with_title}"
  end

  workflow_update
  def check_title_validity
    # The handler is now guaranteed to see some workflow input since it was
    # processed by the constructor
    valid = Temporalio::Workflow.execute_activity(
      CheckTitleValidityActivity,
      @name_with_title,
      start_to_close_timeout: 100
    )
    @title_has_been_checked = true
    valid
  end
end
```

### Use locks to prevent concurrent handler execution {/* #control-handler-concurrency */}

Concurrent processes can interact in unpredictable ways.
Incorrectly written [concurrent message-passing](/handling-messages#message-handler-concurrency) code may not work correctly when multiple handler instances run simultaneously.
Here's an example of a pathological case:

```ruby
class MyWorkflow < Temporalio::Workflow::Definition
  # ...

  workflow_signal
  def bad_handler
    data = Temporalio::Workflow.execute_activity(
      FetchDataActivity,
      start_to_close_timeout: 100
    )
    @x = data['x']
    # 🐛🐛 Bug!! If multiple instances of this handler are executing concurrently, then
    # there may be times when the Workflow has @x from one Activity execution and @y
    # from another.
    Temporalio::Workflow.sleep(1)
    @y = data['y']
  end
end
```

Coordinating access with `Mutex`, a mutual exclusion lock, corrects this code.
Locking makes sure that only one handler instance can execute a specific section of code at any given time:

```ruby
class MyWorkflow < Temporalio::Workflow::Definition
  # ...

  workflow_signal
  def safe_handler
    @mutex ||= Mutex.new
    @mutex.synchronize do
      data = Temporalio::Workflow.execute_activity(
        FetchDataActivity,
        start_to_close_timeout: 100
      )
      @x = data['x']
      # 🐛🐛 Bug!! If multiple instances of this handler are executing concurrently, then
      # there may be times when the Workflow has @x from one Activity execution and @y
      # from another.
      Temporalio::Workflow.sleep(1)
      @y = data['y']
    end
  end
end
```

For additional concurrency options, `wait_condition` can be used to do more advanced things such as using an integer
attribute + `wait_condition` as a semaphore.

## Troubleshooting {/* #message-handler-troubleshooting */}

When sending a Signal, Update, or Query to a Workflow, your Client might encounter the following errors:

- **The Client can't contact the server**:
  You'll receive a [`Temporalio::Error::RPCError`](https://ruby.temporal.io/Temporalio/Error/RPCError.html) exception whose `code` is an `UNAVAILABLE` constant defined in [`Code`](https://ruby.temporal.io/Temporalio/Error/RPCError/Code.html) (after some retries).

- **The Workflow does not exist**:
  You'll receive a [`Temporalio::Error::RPCError`](https://ruby.temporal.io/Temporalio/Error/RPCError.html) exception whose `code` is a `NOT_FOUND` constant defined in [`Code`](https://ruby.temporal.io/Temporalio/Error/RPCError/Code.html).

See [Exceptions in message handlers](/handling-messages#exceptions) for a non–Ruby-specific discussion of this topic.

### Signal issues {/* #signal-problems */}

When using Signal, the only exception that will result from your requests during its execution is `RPCError`.
All handlers may experience additional exceptions during the initial (pre-Worker) part of a handler request lifecycle.

For Queries and Updates, the Client waits for a response from the Worker.
If an issue occurs during the handler Execution by the Worker, the Client may receive an exception.

### Update issues {/* #update-problems */}

When working with Updates, you may encounter these errors:

- **No Workflow Workers are polling the Task Queue**:
  Your request will be retried by the SDK Client indefinitely.
  Use a `Cancellation` in your [RPC options](https://ruby.temporal.io/Temporalio/Client/RPCOptions.html) to cancel the Update.
  This raises a [WorkflowUpdateRPCTimeoutOrCanceledError](https://ruby.temporal.io/Temporalio/Error/WorkflowUpdateRPCTimeoutOrCanceledError.html) exception.

- **Update failed**: You'll receive a [`WorkflowUpdateFailedError`](https://ruby.temporal.io/Temporalio/Error/WorkflowUpdateFailedError.html) exception.
  There are two ways this can happen:

  - The Update was rejected by an Update validator defined in the Workflow alongside the Update handler.

  - The Update failed after having been accepted.

  Update failures are like [Workflow failures](/references/failures).
  Issues that cause a Workflow failure in the main method also cause Update failures in the Update handler.
  These might include:

      - A failed Child Workflow
      - A failed Activity (if the Activity retries have been set to a finite number)
      - The Workflow author raising `ApplicationError`
      - Any error listed in `workflow_failure_exception_types` on the Worker or [`workflow_failure_exception_type`](https://ruby.temporal.io/Temporalio/Workflow/Definition.html#workflow_failure_exception_type-class_method) on the Workflow (empty by default)

- **The handler caused the Workflow Task to fail**:
  A [Workflow Task Failure](/references/failures) causes the server to retry Workflow Tasks indefinitely. What happens to your Update request depends on its stage:
  - If the request hasn't been accepted by the server, you receive a `FAILED_PRECONDITION` [`Temporalio::Error::RPCError`](https://ruby.temporal.io/Temporalio/Error/RPCError.html) exception.
  - If the request has been accepted, it is durable.
    Once the Workflow is healthy again after a code deploy, use an [`WorkflowUpdateHandle`](https://ruby.temporal.io/Temporalio/Client/WorkflowUpdateHandle.html) to fetch the Update result.

- **The Workflow finished while the Update handler execution was in progress**:
  You'll receive a [`Temporalio::Error::RPCError`](https://ruby.temporal.io/Temporalio/Error/RPCError.html) "workflow execution already completed".

  This will happen if the Workflow finished while the Update handler execution was in progress, for example because

  - The Workflow was canceled or failed.

  - The Workflow completed normally or continued-as-new and the Workflow author did not [wait for handlers to be finished](/handling-messages#finishing-message-handlers).

### Query issues {/* #query-problems */}

When working with Queries, you may encounter these errors:

- **There is no Workflow Worker polling the Task Queue**:
  You'll receive a [`Temporalio::Error::RPCError`](https://ruby.temporal.io/Temporalio/Error/RPCError.html) exception whose `code` is a `FAILED_PRECONDITION` constant defined in [`Code`](https://ruby.temporal.io/Temporalio/Error/RPCError/Code.html).

- **Query failed**:
  You'll receive a [`WorkflowQueryFailedError`](https://ruby.temporal.io/Temporalio/Error/WorkflowQueryFailedError.html) exception if something goes wrong during a Query.
  Any exception in a Query handler will trigger this error.
  This differs from Signal and Update requests, where exceptions can lead to Workflow Task Failure instead.

- **The handler caused the Workflow Task to fail.**
  This would happen, for example, if the Query handler blocks the thread for too long without yielding.

## Dynamic handlers {/* #dynamic-handler */}

Temporal supports Dynamic Queries, Signals, Updates, Workflows, and Activities.
These are unnamed handlers that are invoked if no other statically defined handler with the given name exists.

Dynamic Handlers provide flexibility to handle cases where the names of Queries, Signals, Updates, Workflows, or Activities, aren't known at run time.

:::caution

Dynamic Handlers should be used judiciously as a fallback mechanism rather than the primary approach.
Overusing them can lead to maintainability and debugging issues down the line.

Instead, Signals, Queries, Workflows, or Activities should be defined statically whenever possible, with clear names that indicate their purpose.
Use static definitions as the primary way of structuring your Workflows.

Reserve Dynamic Handlers for cases where the handler names are not known at compile time and need to be looked up dynamically at runtime.
They are meant to handle edge cases and act as a catch-all, not as the main way of invoking logic.

:::

### Dynamic Query {/* #set-a-dynamic-query */}

A Dynamic Query in Temporal is a Query method that is invoked dynamically at runtime if no other Query with the same name is registered.
A Query can be made dynamic by setting `dynamic` to `true` on the `workflow_query` class method.
Only one Dynamic Query can be present on a Workflow.

The Query Handler parameters must accept a string name as the first parameter. Often users set `raw_args` to `true` and set the second parameter as `*args` which will be an array of `Temporalio::Converters::RawValue`.
The [Temporalio::Workflow.payload_converter](https://ruby.temporal.io/Temporalio/Workflow.html#payload_converter-class_method) property is used to convert the raw value instances to proper types.

```ruby
workflow_query dynamic: true, raw_args: true
def dynamic_query(query_name, *args)
  first_param = Temporalio::Workflow.payload_converter.from_payload(
    args.first || raise 'Missing first parameter'
  )
  "Got parameter #{first_param} for query #{query_name}"
end
```

### Dynamic Signal {/* #set-a-dynamic-signal */}

A Dynamic Signal in Temporal is a Signal that is invoked dynamically at runtime if no other Signal with the same input is registered.
A Signal can be made dynamic by setting `dynamic` to `true` on the `workflow_signal` class method.
Only one Dynamic Signal can be present on a Workflow.

The Signal Handler parameters must accept a string name as the first parameter. Often users set `raw_args` to `true` and set the second parameter as `*args` which will be an array of `Temporalio::Converters::RawValue`.
The [Temporalio::Workflow.payload_converter](https://ruby.temporal.io/Temporalio/Workflow.html#payload_converter-class_method) property is used to convert the raw value instances to proper types.

```ruby
workflow_signal dynamic: true, raw_args: true
def dynamic_signal(signal_name, *args)
  first_param = Temporalio::Workflow.payload_converter.from_payload(
    args.first || raise 'Missing first parameter'
  )
  @pending_things << "Got parameter #{first_param} for signal #{signal_name}"
end
```

### Dynamic Update {/* #set-a-dynamic-update */}

A Dynamic Update in Temporal is an Update that is invoked dynamically at runtime if no other Update with the same input is registered.
An Update can be made dynamic by setting `dynamic` to `true` on the `workflow_update` class method.
Only one Dynamic Update can be present on a Workflow.

The Update Handler parameters must accept a string name as the first parameter. Often users set `raw_args` to `true` and set the second parameter as `*args` which will be an array of `Temporalio::Converters::RawValue`.
The [Temporalio::Workflow.payload_converter](https://ruby.temporal.io/Temporalio/Workflow.html#payload_converter-class_method) property is used to convert the raw value instances to proper types.

```ruby
workflow_update dynamic: true, raw_args: true
def dynamic_update(update_name, *args)
  first_param = Temporalio::Workflow.payload_converter.from_payload(
    args.first || raise 'Missing first parameter'
  )
  @pending_things << "Got parameter #{first_param} for update #{update_name}"
end
```

---

## Schedules - Ruby SDK

This page shows how to do the following:

- [Schedule a Workflow](#schedule-a-workflow)
  - [Create a Scheduled Workflow](#create-a-workflow)
  - [Backfill a Scheduled Workflow](#backfill-a-scheduled-workflow)
  - [Delete a Scheduled Workflow](#delete-a-scheduled-workflow)
  - [Describe a Scheduled Workflow](#describe-a-scheduled-workflow)
  - [List a Scheduled Workflow](#list-a-scheduled-workflow)
  - [Pause a Scheduled Workflow](#pause-a-scheduled-workflow)
  - [Trigger a Scheduled Workflow](#trigger-a-scheduled-workflow)
  - [Update a Scheduled Workflow](#update-a-scheduled-workflow)
- [Use Start Delay](#start-delay)

## Schedule a Workflow {/* #schedule-a-workflow */}

Scheduling Workflows is a crucial aspect of automation.
By scheduling a Workflow, you can automate repetitive tasks, reduce manual intervention, and ensure timely execution.

Use the following actions to manage Scheduled Workflows.

### Create a Scheduled Workflow {/* #create-a-workflow */}

The create action enables you to create a new Schedule. When you create a new Schedule, a unique Schedule ID is generated, which you can use to reference the Schedule in other Schedule commands.

To create a Scheduled Workflow Execution in Ruby, use the [create_schedule](https://ruby.temporal.io/Temporalio/Client.html#create_schedule-instance_method)
method on the Client.
Then pass the Schedule ID and the Schedule object to the method to create a Scheduled Workflow Execution.
Set the Schedule's `action` member to an instance of `Temporalio::Client::Schedule::Action::StartWorkflow` to schedule a Workflow Execution.

```ruby
handle = my_client.create_schedule(
  'my_schedule_id',
  Temporalio::Client::Schedule.new(
    action: Temporalio::Client::Schedule::Action::StartWorkflow.new(
      MyWorkflow, 'some-input',
      id: 'my-workflow-id', task_queue: 'my-task-queue'
    ),
    spec: Temporalio::Client::Schedule::Spec.new(
      intervals: [
        Temporalio::Client::Schedule::Spec::Interval.new(
          every: 5 * 24 * 60 * 60.0, # 5 days
        )
      ]
    )
  )
)
```

:::tip Schedule Auto-Deletion

Once a Schedule has completed creating all its Workflow Executions, the Temporal Service deletes it since it won’t fire again.
The Temporal Service doesn't guarantee when this removal will happen.

:::

### Backfill a Scheduled Workflow {/* #backfill-a-scheduled-workflow */}

The backfill action executes Actions ahead of their specified time range. This command is useful when you need to execute a missed or delayed Action, or when you want to test the Workflow before its scheduled time.

To backfill a Scheduled Workflow Execution in Ruby, use the [backfill](https://ruby.temporal.io/Temporalio/Client/ScheduleHandle.html#backfill-instance_method)
method on the Schedule Handle.

```ruby
handle = my_client.schedule_handle('my-schedule-id')
now = Time.now(in: 'UTC')
handle.backfill(
  Temporalio::Client::Schedule::Backfill.new(
    start_at: now - (4 * 60),
    end_at: now - (2 * 60),
    overlap: Temporalio::Client::Schedule::OverlapPolicy::ALLOW_ALL
  )
)
```

### Delete a Scheduled Workflow {/* #delete-a-scheduled-workflow */}

The delete action enables you to delete a Schedule. When you delete a Schedule, it does not affect any Workflows that were started by the Schedule.

To delete a Scheduled Workflow Execution in Ruby, use the [delete](https://ruby.temporal.io/Temporalio/Client/ScheduleHandle.html#delete-instance_method) method on the Schedule Handle.

```ruby
handle = my_client.schedule_handle('my-schedule-id')
handle.delete
```

### Describe a Scheduled Workflow {/* #describe-a-scheduled-workflow */}

The describe action shows the current Schedule configuration, including information about past, current, and future Workflow Runs. This command is helpful when you want to get a detailed view of the Schedule and its associated Workflow Runs.

To describe a Scheduled Workflow Execution in Ruby, use the [describe](https://ruby.temporal.io/Temporalio/Client/ScheduleHandle.html#describe-instance_method) method on the Schedule Handle.

```ruby
handle = my_client.schedule_handle('my-schedule-id')
desc = handle.describe
puts "Schedule info: #{desc.info}"
```

### List a Scheduled Workflow {/* #list-a-scheduled-workflow */}

The list action lists all the available Schedules. This command is useful when you want to view a list of all the Schedules and their respective Schedule IDs.

To list all schedules, use the [list_schedules](https://ruby.temporal.io/Temporalio/Client.html#list_schedules-instance_method) asynchronous method on the Client.
This returns an enumerator/enumerable.
If a schedule is added or deleted, it may not be available in the list immediately.

```ruby
my_client.list_schedules.each do |sched|
  puts "Schedule info: #{sched}"
end
```

### Pause a Scheduled Workflow {/* #pause-a-scheduled-workflow */}

The pause action enables you to pause and unpause a Schedule. When you pause a Schedule, all the future Workflow Runs associated with the Schedule are temporarily stopped. This command is useful when you want to temporarily halt a Workflow due to maintenance or any other reason.

To pause a Scheduled Workflow Execution in Ruby, use the [pause](https://ruby.temporal.io/Temporalio/Client/ScheduleHandle.html#pause-instance_method) method on the Schedule Handle.
You can pass a note to the `pause` method to provide a reason for pausing the schedule.

```ruby
handle = my_client.schedule_handle('my-schedule-id')
handle.pause(note: 'Pausing the schedule for now')
```

### Trigger a Scheduled Workflow {/* #trigger-a-scheduled-workflow */}

The trigger action triggers an immediate action with a given Schedule. By default, this action is subject to the Overlap Policy of the Schedule. This command is helpful when you want to execute a Workflow outside of its scheduled time.

To trigger a Scheduled Workflow Execution in Ruby, use the [trigger](https://ruby.temporal.io/Temporalio/Client/ScheduleHandle.html#trigger-instance_method) method on the Schedule Handle.

```ruby
handle = my_client.schedule_handle('my-schedule-id')
handle.trigger
```

### Update a Scheduled Workflow {/* #update-a-scheduled-workflow */}

The update action enables you to update an existing Schedule. This command is useful when you need to modify the Schedule's configuration, such as changing the start time, end time, or interval.

To update a Scheduled Workflow Execution in Ruby, use the [update](https://ruby.temporal.io/Temporalio/Client/ScheduleHandle.html#update-instance_method) method on the Schedule Handle.
This method accepts a block which itself accepts an update input object and is expected to return an update with a new
schedule to update, or `nil` to not update.

```ruby
handle = my_client.schedule_handle('my-schedule-id')
handle.update do |input|
  # Return a new schedule with the action updated
  Temporalio::Client::Schedule::Update.new(
    schedule: input.description.schedule.with(
      # Update the action
      action: Temporalio::Client::Schedule::Action::StartWorkflow.new(
        MyNewWorkflow, 'some-new-input',
        id: 'my-workflow-id', task_queue: 'my-task-queue'
      )
    )
  )
end
```

## Use Start Delay {/* #start-delay */}

Use the `start_delay` to schedule a Workflow Execution at a specific one-time future point rather than on a recurring schedule.

Use the `start_delay` parameter on either the `start_workflow` or `execute_workflow` methods in the Client.

```ruby
handle = my_client.start_workflow(
  MyWorkflow, 'some-input',
  id: 'my-workflow-id', task_queue: 'my-task-queue',
  start_delay: 3 * 60 * 60 # 3 hours
)
```

---

## Workflow Timeouts - Ruby SDK

## Workflow timeouts {/* #workflow-timeouts */}

Each Workflow timeout controls the maximum duration of a different aspect of a Workflow Execution.

- **[Workflow Execution Timeout](/encyclopedia/detecting-workflow-failures#workflow-execution-timeout)**: Limits how long the full Workflow Execution can run.
- **[Workflow Run Timeout](/encyclopedia/detecting-workflow-failures#workflow-run-timeout)**: Limits the duration of an individual run of a Workflow Execution.
- **[Workflow Task Timeout](/encyclopedia/detecting-workflow-failures#workflow-task-timeout)**: Limits the time allowed for a Worker to process a Workflow Task.

Set these values as keyword parameter options when starting a Workflow.

```ruby
result = my_client.execute_workflow(
  MyWorkflow, 'some-input',
  id: 'my-workflow-id', task_queue: 'my-task-queue',
  execution_timeout: 5 * 60
)
```

### Workflow retries {/* #workflow-retries */}

A Retry Policy can work in cooperation with the timeouts to provide fine controls to optimize the execution experience.

Use a [Retry Policy](/encyclopedia/retry-policies) to automatically retry Workflow Executions on failure.

Workflow Executions do not retry by default, and Retry Policies should be used with Workflow Executions only in certain situations.

The `retry_policy` can be set when calling `start_workflow` or `execute_workflow`.

```ruby
result = my_client.execute_workflow(
  MyWorkflow, 'some-input',
  id: 'my-workflow-id', task_queue: 'my-task-queue',
  retry_policy: Temporalio::RetryPolicy.new(max_interval: 10)
)
```

---

## Timers - Ruby SDK

This page describes how to set a Durable Timer using the Temporal Ruby SDK.

A [Durable Timer](/workflow-execution/timers-delays) is used to pause the execution of a Workflow for a specified
duration. A Workflow can sleep for days or even months. Timers are persisted, so even if your Worker or Temporal Service
is down when the time period completes, as soon as your Worker and Temporal Service are back up, the Durable Timer call
will resolve and your code will continue executing.

Sleeping is a resource-light operation: it does not tie up the process, and you can run millions of Timers off a single
Worker.

To add a Timer in a Workflow, use `Temporalio::Workflow.sleep`. _Technically_ `Kernel#sleep` works, but the workflow
form allows one to set a summary to view in the UI.

```ruby
