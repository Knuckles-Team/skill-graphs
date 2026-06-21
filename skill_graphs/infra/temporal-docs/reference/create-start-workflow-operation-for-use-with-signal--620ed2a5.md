# Create start-workflow operation for use with signal-with-start
start_workflow_operation = Temporalio::Client::WithStartWorkflowOperation.new(
  MyWorkflow, 'my-workflow-input',
  id: 'my-workflow-id', task_queue: 'my-workflow-task-queue'
)
