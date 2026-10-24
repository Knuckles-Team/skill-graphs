# Start a timer
sleep_fut = Temporalio::Workflow::Future.new { Temporalio::Workflow.sleep(30) }
