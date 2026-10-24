# Capture token for later completion
captured_token = activity.info().task_token
activity.raise_complete_async()
```

To update an Activity outside the Activity, use the [get_async_activity_handle()](https://python.temporal.io/temporalio.client.Client.html#get_async_activity_handle) method to get the handle of the Activity.

```python
handle = my_client.get_async_activity_handle(task_token=captured_token)
```

Then, on that handle, you can call the results of the Activity, `heartbeat`, `complete`, `fail`, or `report_cancellation` method to update the Activity.

```python
await handle.complete("Completion value.")
```

---

## Activity basics - Python SDK

## Develop a basic Activity {/* #develop-activities */}

**How to develop a basic Activity using the Temporal Python SDK.**

One of the primary things that Workflows do is orchestrate the execution of Activities. An Activity is a normal function
or method execution that's intended to execute a single, well-defined action (either short or long-running), such as
querying a database, calling a third-party API, or transcoding a media file. An Activity can interact with the world outside
the Temporal Platform or use a Temporal Client to interact with a Temporal Service. For the Workflow to be able to
execute the Activity, we must define the [Activity Definition](/activity-definition).

You can develop an Activity Definition by using the `@activity.defn` decorator. Register the function as an Activity
with a custom name through a decorator argument, for example `@activity.defn(name="your_activity")`.

:::note

The Temporal Python SDK supports multiple ways of implementing an Activity:

- Asynchronously using [`asyncio`](https://docs.python.org/3/library/asyncio.html)
- Synchronously multithreaded using
  [`concurrent.futures.ThreadPoolExecutor`](https://docs.python.org/3/library/concurrent.futures.html#threadpoolexecutor)
- Synchronously multiprocess using
  [`concurrent.futures.ProcessPoolExecutor`](https://docs.python.org/3/library/concurrent.futures.html#processpoolexecutor)
  and
  [`multiprocessing.managers.SyncManager`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.managers.SyncManager)

Blocking the async event loop in Python would turn your asynchronous program into a synchronous program that executes
serially, defeating the entire purpose of using `asyncio`. This can also lead to potential deadlock, and unpredictable
behavior that causes tasks to be unable to execute. Debugging these issues can be difficult and time consuming, as
locating the source of the blocking call might not always be immediately obvious.

Due to this, consider not making blocking calls from within an asynchronous Activity, or use an async safe library to
perform these actions. If you must use a blocking library, consider using a synchronous Activity instead.

:::

    View the source code
  {' '}
  in the context of the rest of the application code.

```python
from temporalio import activity
