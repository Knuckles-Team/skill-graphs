# my_workflow_file.py

from temporalio import workflow

with workflow.unsafe.sandbox_import_notification_policy(
    workflow.SandboxImportNotificationPolicy.SILENT
):

@workflow.defn
class MyWorkflow:
     # ...
```

This can also be done at worker creation time by customizing the runner's restrictions.

```python
