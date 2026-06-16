# Create a worker with the client, activities, and workflows
worker = Temporalio::Worker.new(
  client:,
  task_queue: 'my-task-queue',
  workflows: [SayHelloWorkflow],
  # There are various forms an activity can take, see "Activities" section for details
  activities: [SayHelloActivity]
)
