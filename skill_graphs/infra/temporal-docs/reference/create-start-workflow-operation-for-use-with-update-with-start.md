# Create start-workflow operation for use with update-with-start
start_workflow_operation = Temporalio::Client::WithStartWorkflowOperation.new(
  MyWorkflow, 'my-workflow-input',
  id: 'my-workflow-id', task_queue: 'my-workflow-task-queue',
  id_conflict_policy: Temporalio::WorkflowIDConflictPolicy::USE_EXISTING
)
