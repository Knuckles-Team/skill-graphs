# Start 3 activities in background
fut1 = Temporalio::Workflow::Future.new do
  Temporalio::Workflow.execute_activity(MyActivity1, schedule_to_close_timeout: 300)
end
fut2 = Temporalio::Workflow::Future.new do
  Temporalio::Workflow.execute_activity(MyActivity2, schedule_to_close_timeout: 300)
end
fut3 = Temporalio::Workflow::Future.new do
  Temporalio::Workflow.execute_activity(MyActivity3, schedule_to_close_timeout: 300)
end
