# Create a worker with the client, activities, and workflows
worker = Temporalio::Worker.new(
  client:,
  task_queue: 'my-task-queue',
  workflows: [MyWorkflow],
  # This provides the activity instance which means it is reused for each attempt, but
  # just the class can be provided to instantiate for each attempt
  activities: [MyActivity.new]
)
