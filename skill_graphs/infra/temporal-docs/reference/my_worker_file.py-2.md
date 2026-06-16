# my_worker_file.py

from temporalio.worker import Worker
from temporalio.worker.workflow_sandbox import SandboxedWorkflowRunner, SandboxRestrictions

my_restrictions = dataclasses.replace(
    SandboxRestrictions.default,
    invalid_module_members=SandboxRestrictions.invalid_module_members_default.with_child_unrestricted(
      "datetime", "date", "today",
    ),
)
my_worker = Worker(..., workflow_runner=SandboxedWorkflowRunner(restrictions=my_restrictions))
```

Restrictions can also be added by piping (`|`) together [`SandboxMatcher`](https://python.temporal.io/temporalio.worker.workflow_sandbox.SandboxMatcher.html) instances.

The following example restricts the `datetime.date` class from being used.

```python
