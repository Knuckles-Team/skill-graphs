# my_worker_file.py

from temporalio.worker import Worker
from temporalio.worker.workflow_sandbox import SandboxedWorkflowRunner, SandboxRestrictions

my_worker = Worker(
  ...,
  workflow_runner=SandboxedWorkflowRunner(
    restrictions=SandboxRestrictions.default.with_passthrough_modules("pydantic")
  )
)
```

In both of these cases, now the `pydantic` module will be passed through from outside the sandbox instead of being reloaded for every Workflow run.

### Invalid module members

`invalid_module_members` includes modules that cannot be accessed.

Checks are compared against the fully qualified path to the item.

For example, to remove a restriction on `datetime.date.today()`, see the following example.

```python
