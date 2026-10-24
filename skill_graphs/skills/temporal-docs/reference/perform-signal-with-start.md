# Perform signal-with-start
handle = client.signal_with_start_workflow(
  MyWorkflow.my_signal, 'signal-input', start_workflow_operation:
)
```

### Send an Update {/* #send-update-from-client */}

An Update is a synchronous, blocking call that can change Workflow state, control its flow, and return a result.

A Client sending an Update must wait until the Server delivers the Update to a Worker.
Workers must be available and responsive.
If you need a response as soon as the Server receives the request, use a Signal instead.
You can't send Updates directly from one Workflow to another. If you need to send Updates across Workflows, like to Child Workflows, use an Activity.

- `WorkflowExecutionUpdateAccepted` is added to the Event History when the Worker confirms that the Update passed validation.
- `WorkflowExecutionUpdateCompleted` is added to the Event History when the Worker confirms that the Update has finished.

To send an Update to a Workflow Execution, you can:

- Call the Update method with `execute_update` from the Workflow handle and wait for the Update to complete.
  This code fetches an Update result:

  ```ruby
  prev_language = handle.execute_update(MessagePassingSimple::GreetingWorkflow.set_language, :chinese)
  ```

2. Use `start_update` to receive a handle as soon as the Update is accepted.
     It returns a `WorkflowUpdateHandle`

  - Use this `WorkflowUpdateHandle` later to fetch your results.
  - Asynchronous Update handlers normally perform long-running async Activities.
  - `start_update` only waits until the Worker has accepted or rejected the Update, not until all asynchronous operations are complete.

  For example:

  ```ruby
  # Start an update and then wait for it to complete
  update_handle = handle.start_update(
    MessagePassingSimple::GreetingWorkflow.apply_language_with_lookup,
    :arabic,
    wait_for_stage: Temporalio::Client::WorkflowUpdateWaitStage::ACCEPTED
  )
  prev_language = update_handle.result
  ```

  For more details, see the "Async handlers" section.

#### Update-With-Start {/* #update-with-start */}

:::tip Stability

In [Public Preview](/evaluate/development-production-features/release-stages#public-preview) in Temporal Cloud.

Minimum Temporal Server version [Temporal Server version 1.26](https://github.com/temporalio/temporal/releases/tag/v1.26.2)

:::

[Update-with-Start](/sending-messages#update-with-start) lets you [send an Update](/develop/ruby/workflows/message-passing#send-update-from-client) that checks whether an already-running Workflow with that ID exists:

- If the Workflow exists, the Update is processed.
- If the Workflow does not exist, a new Workflow Execution is started with the given ID, and the Update is processed before the main Workflow method starts to execute.

Use `execute_update_with_start_workflow` to start the Update and wait for the result in one go.

Alternatively, use `start_update_with_start_workflow` to start the Update and receive a `WorkflowUpdateHandle`, and then use `update_handle.result` to retrieve the result from the Update.

These calls return once the requested Update wait stage has been reached, or when the request times out.

- You will need to provide a `WithStartWorkflowOperation` to define the Workflow that will be started if necessary, and its arguments.
- You must specify an [id_conflict_policy](/workflow-execution/workflowid-runid#workflow-id-conflict-policy) when creating the `WithStartWorkflowOperation`.
  Note that a `WithStartWorkflowOperation` can only be used once.

Here's an example:

```ruby
client = Temporalio::Client.connect('localhost:7233', 'default')
