# Verify that the expected Heartbeats are received by the callback function.
assert heartbeats == ["param: test", "second heartbeat"]
```

## Testing Workflows {/* #test-workflows */}

### How to mock Activities {/* #mock-activities */}

Mock the Activity invocation when unit testing your Workflows.

When integration testing Workflows with a Worker, you can mock Activities by providing mock Activity implementations to the Worker.

Provide mock Activity implementations to the Worker.

```python

from temporalio.client import Client
from temporalio.worker import Worker
