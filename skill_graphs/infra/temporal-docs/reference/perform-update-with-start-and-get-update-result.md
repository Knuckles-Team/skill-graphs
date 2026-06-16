# Perform update-with-start and get update result
update_result = client.execute_with_start_workflow(
  MyWorkflow.my_update, 'update-input', start_workflow_operation:
)
