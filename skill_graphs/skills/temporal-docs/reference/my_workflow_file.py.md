# my_workflow_file.py

from temporalio import workflow

with workflow.unsafe.imports_passed_through():

@workflow.defn
class MyWorkflow:
     # ...
```

Alternatively, this can be done at Worker creation time by customizing the runner's restrictions.

```python
