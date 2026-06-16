# Create a replayer
replayer = Temporalio::Worker::WorkflowReplayer.new(workflows: [MyWorkflow])
