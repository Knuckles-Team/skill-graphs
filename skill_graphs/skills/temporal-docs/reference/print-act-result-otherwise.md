# Print act result otherwise
Temporalio::Workflow.logger.info("Act result: #{act_result}")
```

There are several other details not covered here about futures, such as how exceptions are handled, how to use a setter
proc instead of a block, etc. See the [API documentation](https://ruby.temporal.io/Temporalio/Workflow/Future.html) for details.

---

## Workflows - Ruby SDK

![Ruby SDK Banner](/img/assets/banner-ruby-temporal.png)

## Workflows

- [Workflow basics](/develop/ruby/workflows/basics)
- [Child Workflows](/develop/ruby/workflows/child-workflows)
- [Continue-As-New](/develop/ruby/workflows/continue-as-new)
- [Cancellation](/develop/ruby/workflows/cancellation)
- [Timeouts](/develop/ruby/workflows/timeouts)
- [Message passing](/develop/ruby/workflows/message-passing)
- [Schedules](/develop/ruby/workflows/schedules)
- [Timers](/develop/ruby/workflows/timers)
- [Futures](/develop/ruby/workflows/futures)
- [Dynamic Workflow](/develop/ruby/workflows/dynamic-workflow)
- [Versioning](/develop/ruby/workflows/versioning)

---

## Message passing - Ruby SDK

A Workflow can act like a stateful service that receives messages: Queries, Signals, and Updates.
These messages interact with the Workflow via handler methods defined in the Workflow code.
Clients use messages to read Workflow state or change its behavior.

See [Workflow message passing](/encyclopedia/workflow-message-passing) for a general overview.

## Write message handlers {/* #writing-message-handlers */}

:::info
The code that follows is part of a [working solution](https://github.com/temporalio/samples-ruby/tree/main/message_passing_simple).
:::

Follow these guidelines when writing your message handlers:

- Message handlers are defined as methods on the Workflow class, decorated by calling one of three class methods before defining the handler method: `workflow_query`, `workflow_signal`, and `workflow_update`.
- These also implicitly create class-methods with the same name as the instance methods for use by callers.
- The parameters and return values of handlers and the main Workflow function must be [serializable](/dataconversion).
- Prefer single hash/object input parameter to multiple input parameters.
  Hash/object parameters allow you to add fields without changing the calling signature.

### Query handlers {/* #queries */}

A [Query](/sending-messages#sending-queries) is a synchronous operation that retrieves state from a Workflow Execution.
Define as a method:

```ruby
class GreetingWorkflow < Temporalio::Workflow::Definition
  # ...

  workflow_query
  def languages(input)
    # A query handler returns a value: it can inspect but must not mutate the Workflow state.
    if input['include_unsupported']
      CallGreetingService.greetings.keys.sort
    else
      @greetings.keys.sort
    end
  end

  # ...
end
```

Or as an attribute reader:

```ruby
class GreetingWorkflow < Temporalio::Workflow::Definition
  # This is the equivalent of:
  #    workflow_query
  #    def language
  #      @language
  #    end
  workflow_query_attr_reader :language

  # ...
end
```

- The `workflow_query` class method can accept arguments.
  See the API reference docs: [`workflow_query`](https://ruby.temporal.io/Temporalio/Workflow/Definition.html#workflow_query-class_method).
- A Query handler must not modify Workflow state.
- You can't perform async blocking operations such as executing an Activity in a Query handler.

### Signal handlers {/* #signals */}

A [Signal](/sending-messages#sending-signals) is an asynchronous message sent to a running Workflow Execution to change its state and control its flow:

```ruby
class GreetingWorkflow < Temporalio::Workflow::Definition
  # ...

  workflow_signal
  def approve(input)
    # A signal handler mutates the workflow state but cannot return a value.
    @approved_for_release = true
    @approver_name = input['name']
  end

  # ...
end
```

- The `workflow_signal` class method can accept arguments.
  Refer to the API docs: [`workflow_signal`](https://ruby.temporal.io/Temporalio/Workflow/Definition.html#workflow_signal-class_method).

- The handler should not return a value.
  The response is sent immediately from the server, without waiting for the Workflow to process the Signal.

- Signal (and Update) handlers can be asynchronous and blocking.
  This allows you to use Activities, Child Workflows, durable Timers, wait conditions, and more.
  See [Async handlers](#async-handlers) and [Workflow message passing](/encyclopedia/workflow-message-passing) for guidelines on safely using async Signal and Update handlers.

### Update handlers and validators {/* #updates */}

An [Update](/sending-messages#sending-updates) is a trackable synchronous request sent to a running Workflow Execution.
It can change the Workflow state, control its flow, and return a result.
The sender must wait until the Worker accepts or rejects the Update.
The sender may wait further to receive a returned value or an exception if something goes wrong:

```ruby
class GreetingWorkflow < Temporalio::Workflow::Definition
  # ...

  workflow_update
  def set_language(new_language) # rubocop:disable Naming/AccessorMethodName
    # An update handler can mutate the workflow state and return a value.
    prev = @language.to_sym
    @language = new_language.to_sym
    prev
  end

  workflow_update_validator(:set_language)
  def validate_set_language(new_language)
    # In an update validator you raise any exception to reject the update.
    raise "#{new_language} is not supported" unless @greetings.include?(new_language.to_sym)
  end

  # ...
end
```

- The `workflow_update` class method can take arguments as described in the API reference docs for [`workflow_update`](https://ruby.temporal.io/Temporalio/Workflow/Definition.html#workflow_update-class_method).

- About validators:
  - Use validators to reject an Update before it is written to History.
    Validators are always optional.
    If you don't need to reject Updates, you can skip them.
  - Define an Update validator with the [`workflow_update_validator`](https://ruby.temporal.io/Temporalio/Workflow/Definition.html#workflow_update-class_method) class method invoked before defining the method.
    The first parameter when declaring the validator is the name of the Update handler method.
    The validator must accept the same argument types as the handler and should not return a value.

- Accepting and rejecting Updates with validators:
  - To reject an Update, raise an exception of any type in the validator.
  - Without a validator, Updates are always accepted.
- Validators and Event History:
  - The `WorkflowExecutionUpdateAccepted` event is written into the History whether the acceptance was automatic or programmatic.
  - When a Validator raises an error, the Update is rejected, the Update is not run, and `WorkflowExecutionUpdateAccepted` _won't_ be added to the Event History.
    The caller receives an "Update failed" error.

- Use [`current_update_info`](https://ruby.temporal.io/Temporalio/Workflow.html#current_update_info-class_method) to obtain information about the current Update.
  This includes the Update ID, which can be useful for deduplication when using Continue-As-New: see [Ensuring your messages are processed exactly once](/handling-messages#exactly-once-message-processing).
- Update (and Signal) handlers can be asynchronous and blocking.
  This allows you to use Activities, Child Workflows, durable Timers, wait conditions, and more.
  See [Async handlers](#async-handlers) and [Workflow message passing](/encyclopedia/workflow-message-passing) for guidelines on safely using async Update and Signal handlers.

## Send messages {/* #send-messages */}

To send Queries, Signals, or Updates you call methods on a [`WorkflowHandle`](https://ruby.temporal.io/Temporalio/Client/WorkflowHandle.html) instance.
To obtain the Workflow handle, you can:

- Use [`Client#start_workflow`](https://ruby.temporal.io/Temporalio/Client.html#start_workflow-instance_method) to start a Workflow and return its handle.
- Use the [`Client#workflow_handle`](https://ruby.temporal.io/Temporalio/Client.html#workflow_handle-instance_method) method to retrieve a Workflow handle by its Workflow Id.

For example:

```ruby
client = Temporalio::Client.connect('localhost:7233', 'default')
handle = client.start_workflow(
  MessagePassingSimple::GreetingWorkflow,
  id: 'message-passing-simple-sample-workflow-id',
  task_queue: 'message-passing-simple-sample'
)
```

To check the argument types required when sending messages -- and the return type for Queries and Updates -- refer to the corresponding handler method in the Workflow Definition.

:::warning Using Continue-as-New and Updates

- Temporal _does not_ support Continue-as-New functionality within Update handlers.
- Complete all handlers _before_ using Continue-as-New.
- Use Continue-as-New from your main Workflow Definition method, just as you would complete or fail a Workflow Execution.

:::

### Send a Query {/* #send-query */}

Call a Query method with [`WorkflowHandle#query`](https://ruby.temporal.io/Temporalio/Client/WorkflowHandle.html#query-instance_method):

```ruby
supported_languages = handle.query(MessagePassingSimple::GreetingWorkflow.languages, { include_unsupported: false })
```

- Sending a Query doesn’t add events to a Workflow's Event History.

- You can send Queries to closed Workflow Executions within a Namespace's Workflow retention period.
  This includes Workflows that have completed, failed, or timed out.
  Querying terminated Workflows is not safe and, therefore, not supported.

- A Worker must be online and polling the Task Queue to process a Query.

### Send a Signal {/* #send-signal */}

You can send a Signal to a Workflow Execution from a Temporal Client or from another Workflow Execution.
However, you can only send Signals to Workflow Executions that haven’t closed.

#### From a Client {/* #send-signal-from-client */}

Use [`WorkflowHandle#signal`](https://ruby.temporal.io/Temporalio/Client/WorkflowHandle.html#signal-instance_method) from Client code to send a Signal:

```ruby
handle.signal(MessagePassingSimple::GreetingWorkflow.approve, { name: 'John Q. Approver' })
```

- The call returns when the server accepts the Signal; it does _not_ wait for the Signal to be delivered to the Workflow Execution.

- The [WorkflowExecutionSignaled](/references/events#workflowexecutionsignaled) Event appears in the Workflow's Event History.

#### From a Workflow {/* #send-signal-from-workflow */}

A Workflow can send a Signal to another Workflow, known as an _External Signal_.
In this case you need to obtain a Workflow handle for the external Workflow.
Use `Temporalio::Workflow.external_workflow_handle`, passing a running Workflow Id, to retrieve a Workflow handle:

```ruby
class WorkflowB < Temporalio::Workflow::Definition
  def execute
    handle = Temporalio::Workflow.external_workflow_handle('workflow-a-id')
    handle.signal(WorkflowA.some_signal, 'some signal arg')
  end
end
```

When an External Signal is sent:

- A [SignalExternalWorkflowExecutionInitiated](/references/events#signalexternalworkflowexecutioninitiated) Event appears in the sender's Event History.
- A [WorkflowExecutionSignaled](/references/events#workflowexecutionsignaled) Event appears in the recipient's Event History.

#### Signal-With-Start {/* #signal-with-start */}

Signal-With-Start allows a Client to send a Signal to a Workflow Execution, starting the Execution if it is not already running.
If there's a Workflow running with the given Workflow Id, it will be signaled.
If there isn't, a new Workflow will be started and immediately signaled.

To use Signal-With-Start, call `signal_with_start_workflow` with a `WithStartWorkflowOperation`:

```ruby
client = Temporalio::Client.connect('localhost:7233', 'default')
