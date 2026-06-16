# my_worker_file.py

from temporalio.worker import Worker
from temporalio.worker.workflow_sandbox import (
  SandboxedWorkflowRunner,
  SandboxMatcher,
  SandboxRestrictions,
)

my_restrictions = dataclasses.replace(
    SandboxRestrictions.default,
    invalid_module_members=SandboxRestrictions.invalid_module_members_default | SandboxMatcher(
      children={"datetime": SandboxMatcher(use={"date"})},
    ),
)
my_worker = Worker(..., workflow_runner=SandboxedWorkflowRunner(restrictions=my_restrictions))
```

### Import Notification Policy

The sandbox's import notification policy specifies how the sandbox behaves when it imports modules in a way that may be unintentional. It covers two common scenarios: dynamic imports and enforcing module passthrough. Each can be controlled independently.

A dynamic import occurs when a module is imported after the Workflow is loaded into the sandbox. These imports are often invisible and, if they don't do anything restricted by the sandbox, cause memory overhead. By default the [`WARN_ON_DYNAMIC_IMPORT`](https://python.temporal.io/temporalio.workflow.SandboxImportNotificationPolicy.html#WARN_ON_DYNAMIC_IMPORT) policy setting is enabled and a warning will be emitted when a module that is not in the [passthrough modules](#passthrough-modules) list is dynamically imported.

The other notable policy settings apply when a module is imported into the sandbox that was not passed through. These settings are disabled by default and must be explicitly turned on.
The [`WARN_ON_UNINTENTIONAL_PASSTHROUGH`](https://python.temporal.io/temporalio.workflow.SandboxImportNotificationPolicy.html#WARN_ON_UNINTENTIONAL_PASSTHROUGH) setting emits a warning when a module not included in the [passthrough modules](#passthrough-modules) list is imported.

Similarly, the [`RAISE_ON_UNINTENTIONAL_PASSTHROUGH`](https://python.temporal.io/temporalio.workflow.SandboxImportNotificationPolicy.html#RAISE_ON_UNINTENTIONAL_PASSTHROUGH) setting will raise an error when a non-passed-through module is imported.

The import notification policy can be set for specific imports by using [`sandbox_import_notification_policy`](https://python.temporal.io/temporalio.workflow.unsafe.html#sandbox_import_notification_policy) context manager.

```python
