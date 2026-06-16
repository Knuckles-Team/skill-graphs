# Wait for first act result or sleep fut
act_result = Temporalio::Workflow::Future.any_of(sleep_fut, *act_futs).wait
