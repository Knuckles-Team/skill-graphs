# Utility method for making calls to the microservices
def call_service(stem: str, name: str) -> str:
    base = f"http://localhost:9999/{stem}"
    url = f"{base}?name={urllib.parse.quote(name)}"

    response = requests.get(url)
    return response.text
```

Whether to implement Activities as class methods or functions is a design
choice left up to the developer when cross-activity state isn't needed. Both are
equally valid implementations.

### How to run Synchronous Activities on a Worker

When running synchronous Activities, the Worker
needs to have an `activity_executor`. Temporal
recommends using a `ThreadPoolExecutor` as shown here:

```python
with ThreadPoolExecutor(max_workers=42) as executor:
    worker = Worker(
        # ...
        activity_executor=executor,
        # ...
    )
```

## How to Implement Asynchronous Activities

The following code is an implementation of the preceding Activity, but as an
asynchronous Activity Definition.

It makes
a call to a microservice, accessed through HTTP, to request this
greeting in Spanish. This Activity uses the `aiohttp` library to make an async
safe HTTP request. Using the `requests` library here would have resulted in
blocking code within the async event loop, which will block the entire async
event loop. For more in-depth information about this issue, refer to the
[Python asyncio documentation](https://docs.python.org/3/library/asyncio-dev.html#running-blocking-code).

The following code also implements the Activity Definition as a class, rather than a
function. The `aiohttp` library requires an established `Session` to perform the
HTTP request. It would be inefficient to establish a `Session` every time an
Activity is invoked, so instead this code accepts a `Session` object as an instance
parameter and makes it available to the methods. This approach will also be
beneficial when the execution is over and the `Session` needs to be closed.

In this example, the Activity supplies the name in the URL and retrieves
the greeting from the body of the response.

```python

from temporalio import activity

class TranslateActivities:
    def __init__(self, session: aiohttp.ClientSession):
        self.session = session

    @activity.defn
    async def greet_in_spanish(self, name: str) -> str:
        greeting = await self.call_service("get-spanish-greeting", name)
        return greeting

    # Utility method for making calls to the microservices
    async def call_service(self, stem: str, name: str) -> str:
        base = f"http://localhost:9999/{stem}"
        url = f"{base}?name={urllib.parse.quote(name)}"

        async with self.session.get(url) as response:
            translation = await response.text()

            if response.status >= 400:
                raise ApplicationError(
                    f"HTTP Error {response.status}: {translation}",
                    # We want to have Temporal automatically retry 5xx but not 4xx
                    non_retryable=response.status < 500,
                )

            return translation
```

### How to run synchronous code from an asynchronous activity

If your Activity is asynchronous and you don't want to change it to synchronous,
but you need to run blocking code inside it,
then you can use python utility functions to run synchronous code
in an asynchronous function:

- [`loop.run_in_executor()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.run_in_executor), which is also mentioned in the ["running blocking code" section of the "developing with asyncio" guide](https://docs.python.org/3/library/asyncio-dev.html#running-blocking-code)
- [`asyncio.to_thread()`](https://docs.python.org/3/library/asyncio-task.html#running-in-threads)

## When Should You Use Async Activities

Asynchronous Activities have many advantages, such as potential speed up of execution.
However, as discussed above, making unsafe calls within the async event loop
can cause sporadic and difficult to diagnose bugs. For this reason, we recommend
using asynchronous Activities _only_ when you are certain that your Activities
are async safe and don't make blocking calls.

If you experience bugs that you think may be a result of an unsafe call being made in an asynchronous Activity, convert it to a synchronous Activity and see if the issue resolves.

---

## Testing - Python SDK

The Testing section of the Temporal Application development guide describes the frameworks that facilitate Workflow and integration testing.

In the context of Temporal, you can create these types of automated tests:

- **End-to-end:** Running a Temporal Server and Worker with all its Workflows and Activities; starting and interacting with Workflows from a Client.
- **Integration:** Anything between end-to-end and unit testing.
  - Running Activities with mocked Context and other SDK imports (and usually network requests).
  - Running Workers with mock Activities, and using a Client to start Workflows.
  - Running Workflows with mocked SDK imports.
- **Unit:** Running a piece of Workflow or Activity code (a function or method) and mocking any code it calls.

We generally recommend writing the majority of your tests as integration tests.

Because the test server supports skipping time, use the test server for both end-to-end and integration tests with Workers.

## Test frameworks {/* #test-frameworks */}

Some SDKs have support or examples for popular test frameworks, runners, or libraries.

One recommended framework for testing in Python for the Temporal SDK is [pytest](https://docs.pytest.org/), which can help with fixtures to stand up and tear down test environments, provide useful test discovery, and make it easy to write parameterized tests.

## Testing Activities {/* #test-activities */}

An Activity can be tested with a mock Activity environment, which provides a way to mock the Activity context, listen to Heartbeats, and cancel the Activity.
This behavior allows you to test the Activity in isolation by calling it directly, without needing to create a Worker to run the Activity.

### Run an Activity {/* #run-an-activity */}

If an Activity references its context, you need to mock that context when testing in isolation.

To run an Activity in a test, use the [`ActivityEnvironment`](https://python.temporal.io/temporalio.testing.ActivityEnvironment.html) class.

This class allows you to run any callable inside an Activity context.
Use it to test the behavior of your code under various conditions.

### Listen to Heartbeats {/* #listen-to-heartbeats */}

When an Activity sends a Heartbeat, be sure that you can see the Heartbeats in your test code so that you can verify them.

To test a Heartbeat in an Activity, use the [`on_heartbeat()`](https://python.temporal.io/temporalio.testing.ActivityEnvironment.html#on_heartbeat) property of the [`ActivityEnvironment`](https://python.temporal.io/temporalio.testing.ActivityEnvironment.html) class.
This property sets a custom function that is called every time the `activity.heartbeat()` function is called within the Activity.

```python
@activity.defn
async def activity_with_heartbeats(param: str):
    activity.heartbeat(f"param: {param}")
    activity.heartbeat("second heartbeat")

env = ActivityEnvironment()
heartbeats = []
