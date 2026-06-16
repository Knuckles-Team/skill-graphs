# my_worker_file.py

from temporalio.worker import Worker
from temporalio.worker.workflow_sandbox import SandboxedWorkflowRunner, SandboxRestrictions

my_worker = Worker(
  ...,
  workflow_runner=SandboxedWorkflowRunner(
    restrictions=SandboxRestrictions.default.with_import_notification_policy(
      workflow.SandboxImportNotificationPolicy.WARN_ON_DYNAMIC_IMPORT | workflow.SandboxImportNotificationPolicy.WARN_ON_UNINTENTIONAL_PASSTHROUGH
    )
  )
)
```

The [`sandbox_import_notification_policy`](https://python.temporal.io/temporalio.workflow.unsafe.html#sandbox_import_notification_policy) context manager will always be respected if used in combination with the restrictions customization.

For more information on the Python sandbox, see the following resources.

- [Python SDK README](https://github.com/temporalio/sdk-python)
- [Python API docs](https://python.temporal.io/index.html)

---

## Temporal Python SDK synchronous vs. asynchronous Activity implementations

The Temporal Python SDK supports multiple ways of implementing an Activity:

- Asynchronously using [`asyncio`](https://docs.python.org/3/library/asyncio.html)
- Synchronously multithreaded using [`concurrent.futures.ThreadPoolExecutor`](https://docs.python.org/3/library/concurrent.futures.html#threadpoolexecutor)
- Synchronously multiprocess using [`concurrent.futures.ProcessPoolExecutor`](https://docs.python.org/3/library/concurrent.futures.html#processpoolexecutor) and [`multiprocessing.managers.SyncManager`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.managers.SyncManager)

It is important to implement your Activities using the correct method, otherwise
your application may fail in sporadic and unexpected ways. Which one you should
use depends on your use case. This section provides guidance to help you choose
the best approach.

## The Python Asynchronous Event Loop and Blocking Calls

First, let's look at how async event loops work in Python. The Python async
event loop runs in a thread and executes all tasks in its thread. When any
task is running in the event loop, the loop is blocked and no other tasks can be
running at the same time within that event loop. Whenever a task executes an
`await` expression, the task is suspended, and the event loop begins or resumes
execution of another task.

This means that the event loop can only pass the flow of control when the `await`
keyword is executed. If a program makes a blocking call, such as one that reads
from a file, makes a synchronous request to a network service, waits for user input,
or anything else that blocks the execution, the entire event loop must wait until
that execution has completed.

Blocking the async event loop in Python would turn your asynchronous program
into a synchronous program that executes serially, defeating the entire purpose
of using `asyncio`. This can also lead to potential deadlock, and unpredictable behavior
that causes tasks to be unable to execute. Debugging these issues can be difficult
and time consuming, as locating the source of the blocking call might not always
be immediately evident.

Due to this, Python developers must be extra careful to not make blocking calls
from within an asynchronous Activity, or use an async safe library to perform
these actions.

For example, making an HTTP call with the popular `requests` library within an
asynchronous Activity would lead to blocking your event loop. If you want to make
an HTTP call from within an asynchronous Activity, you should use an async-safe HTTP library
such as `aiohttp` or `httpx`. Otherwise, use a synchronous Activity.

## Python SDK Worker Execution Architecture

Python workers have the following components for executing code:

- Your event loop, which runs Tasks from async Activities **plus the rest of the Temporal Worker, such as communicating with the server**.
- An executor for executing Activity Tasks from synchronous Activities. A thread pool executor is recommended.
- A thread pool executor for executing Workflow Tasks.

> See Also: [docs for](https://python.temporal.io/temporalio.worker.Worker.html#__init__) `worker.__init__()`

### Activities

- Async Activities and the temporal worker SDK code both run the default asyncio event loop or whatever event loop you give the Worker.
- Synchronous Activities run in the `activity_executor`.

### Workflows

Since Workflow Tasks have the following three properties, they're run in threads.

- are CPU bound
- need to be timed out for deadlock detection
- need to not block other Workflow Tasks

The `workflow_task_executor` is the thread pool these Tasks are run on.
The fact that Workflow Tasks run in a thread pool can be confusing at first because Workflow Definitions are `async`.
The key differentiator is that the `async` in Workflow Definitions isn't referring to the standard event loop -- it's referring to the Workflow's own event loop.
Each Workflow gets its own “Workflow event loop,” which is deterministic, and described in [the Python SDK blog](https://temporal.io/blog/durable-distributed-asyncio-event-loop#temporal-workflows-are-asyncio-event-loops).
The Workflow event loop doesn't constantly loop -- it just gets cycled through during a Workflow Task to make as much progress as possible on all of its futures.
When it can no longer make progress on any of its futures, then the Workflow Task is complete.

### Number of CPU cores

The only ways to use more than one core in a python Worker (considering Python's GIL) are:

- Run more than one Worker Process.
- Run the synchronous Activities in a process pool executor, but a thread pool executor is recommended.

### A Worker infrastructure option: Separate Activity and Workflow Workers

To reduce the risk of event loops or executors getting blocked,
some users choose to deploy separate Workers for Workflow Tasks and Activity Tasks.

## Activity Definition

**By default, Activities should be synchronous rather than asynchronous**.
You should only make an Activity asynchronous if you are
certain that it doesn't block the event loop.

This is because if you have blocking code in an `async def` function,
it blocks your event loop and the rest of Temporal, which can cause bugs that are
hard to diagnose, including freezing your worker and blocking Workflow progress
(because Temporal can't tell the server that Workflow Tasks are completing).
The reason synchronous Activities help is because they
run in the `activity_executor` ([docs for](https://python.temporal.io/temporalio.worker.Worker.html#__init__) `worker.__init__()`)
rather than in the global event loop,
which helps because:

- There's no risk of accidentally blocking the global event loop.
- If you have multiple
  Activity Tasks running in a thread pool rather than an event loop, one bad
  Activity Task can't slow down the others; this is because the OS scheduler preemptively
  switches between threads, which the event loop coordinator doesn't do.

> See Also:
> ["Types of Activities" section of Python SDK README](https://github.com/temporalio/sdk-python#types-of-activities)

## How to implement Synchronous Activities

The following code is a synchronous Activity Definition.
It takes a name (`str`) as input and returns a
customized greeting (`str`) as output.

It makes a call to a microservice, and when making this call,
you'll notice that it uses the `requests` library. This is safe to do in
synchronous Activities.

```python

from temporalio import activity

class TranslateActivities:

    @activity.defn
    def greet_in_spanish(self, name: str) -> str:
        greeting = self.call_service("get-spanish-greeting", name)
        return greeting

    # Utility method for making calls to the microservices
    def call_service(self, stem: str, name: str) -> str:
        base = f"http://localhost:9999/{stem}"
        url = f"{base}?name={urllib.parse.quote(name)}"

        response = requests.get(url)
        return response.text
```

The preceding example doesn't share a session across the Activity, so
`__init__` was removed. While `requests` does have the ability to create sessions,
it's currently unknown if they're thread safe. Due to no longer having or needing
`__init__`, the case could be made here to not implement the Activities as a class,
but just as decorated functions as shown here:

```python
@activity.defn
def greet_in_spanish(name: str) -> str:
    greeting = call_service("get-spanish-greeting", name)
    return greeting
