# Start 5 activities
act_futs = 5.times.map do |i|
  Temporalio::Workflow::Future.new do
    Temporalio::Workflow.execute_activity(MyActivity, "my-arg-#{i}", schedule_to_close_timeout: 300)
  end
end
