# Functional API overview
Source: https://docs.langchain.com/oss/python/langgraph/functional-api

The **Functional API** allows you to add LangGraph's key features ([persistence](/oss/python/langgraph/persistence), [memory](/oss/python/langgraph/add-memory), [human-in-the-loop](/oss/python/langgraph/interrupts), and [streaming](/oss/python/langgraph/streaming)) to your applications with minimal changes to your existing code.

It is designed to integrate these features into existing code that may use standard language primitives for branching and control flow, such as `if` statements, `for` loops, and function calls. Unlike many data orchestration frameworks that require restructuring code into an explicit pipeline or DAG, the Functional API allows you to incorporate these capabilities without enforcing a rigid execution model.

The Functional API uses two key building blocks:

* **`@entrypoint`**: Marks a function as the starting point of a workflow, encapsulating logic and managing execution flow, including handling long-running tasks and interrupts.
* **[`@task`](https://reference.langchain.com/python/langgraph/func/task)**: Represents a discrete unit of work, such as an API call or data processing step, that can be executed asynchronously within an entrypoint. Tasks return a future-like object that can be awaited or resolved synchronously.

This provides a minimal abstraction for building workflows with state management and streaming.

<Tip>
  For information on how to use the functional API, see [Use Functional API](/oss/python/langgraph/use-functional-api).
</Tip>

## Functional API vs. Graph API

For users who prefer a more declarative approach, LangGraph's [Graph API](/oss/python/langgraph/graph-api) allows you to define workflows using a Graph paradigm. Both APIs share the same underlying runtime, so you can use them together in the same application.

Here are some key differences:

* **Control flow**: The Functional API does not require thinking about graph structure. You can use standard Python constructs to define workflows. This will usually trim the amount of code you need to write.
* **Short-term memory**: The **GraphAPI** requires declaring a [**State**](/oss/python/langgraph/graph-api#state) and may require defining [**reducers**](/oss/python/langgraph/graph-api#reducers) to manage updates to the graph state. `@entrypoint` and `@tasks` do not require explicit state management as their state is scoped to the function and is not shared across functions.
* **Checkpointing**: Both APIs generate and use checkpoints. In the **Graph API** a new checkpoint is generated after every [superstep](/oss/python/langgraph/graph-api). In the **Functional API**, when tasks are executed, their results are saved to an existing checkpoint associated with the given entrypoint instead of creating a new checkpoint.
* **Visualization**: The Graph API makes it easy to visualize the workflow as a graph which can be useful for debugging, understanding the workflow, and sharing with others. The Functional API does not support visualization as the graph is dynamically generated during runtime.

## Example

Below we demonstrate a simple application that writes an essay and [interrupts](/oss/python/langgraph/interrupts) to request human review.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.func import entrypoint, task
from langgraph.types import interrupt

@task
def write_essay(topic: str) -> str:
    """Write an essay about the given topic."""
    time.sleep(1) # A placeholder for a long-running task.
    return f"An essay about topic: {topic}"

@entrypoint(checkpointer=InMemorySaver())
def workflow(topic: str) -> dict:
    """A simple workflow that writes an essay and asks for a review."""
    essay = write_essay("cat").result()
    is_approved = interrupt({
        # Any json-serializable payload provided to interrupt as argument.
        # It will be surfaced on the client side as an Interrupt when streaming data
        # from the workflow.
        "essay": essay, # The essay we want reviewed.
        # We can add any additional information that we need.
        # For example, introduce a key called "action" with some instructions.
        "action": "Please approve/reject the essay",
    })

    return {
        "essay": essay, # The essay that was generated
        "is_approved": is_approved, # Response from HIL
    }
```

<Accordion title="Detailed Explanation">
  This workflow will write an essay about the topic "cat" and then pause to get a review from a human. The workflow can be interrupted for an indefinite amount of time until a review is provided.

  When the workflow is resumed, it executes from the very start, but because the result of the `writeEssay` task was already saved, the task result will be loaded from the checkpoint instead of being recomputed.

  ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import time
  from langchain_core.utils.uuid import uuid7
  from langgraph.func import entrypoint, task
  from langgraph.types import interrupt
  from langgraph.checkpoint.memory import InMemorySaver

  @task
  def write_essay(topic: str) -> str:
      """Write an essay about the given topic."""
      time.sleep(1)  # This is a placeholder for a long-running task.
      return f"An essay about topic: {topic}"

  @entrypoint(checkpointer=InMemorySaver())
  def workflow(topic: str) -> dict:
      """A simple workflow that writes an essay and asks for a review."""
      essay = write_essay("cat").result()
      is_approved = interrupt(
          {
              # Any json-serializable payload provided to interrupt as argument.
              # It will be surfaced on the client side as an Interrupt when streaming data
              # from the workflow.
              "essay": essay,  # The essay we want reviewed.
              # We can add any additional information that we need.
              # For example, introduce a key called "action" with some instructions.
              "action": "Please approve/reject the essay",
          }
      )
      return {
          "essay": essay,  # The essay that was generated
          "is_approved": is_approved,  # Response from HIL
      }

  thread_id = str(uuid7())
  config = {"configurable": {"thread_id": thread_id}}
  for item in workflow.stream("cat", config):
      print(item)
  # > {'write_essay': 'An essay about topic: cat'}
  # > {
  # >     '__interrupt__': (
  # >        Interrupt(
  # >            value={
  # >                'essay': 'An essay about topic: cat',
  # >                'action': 'Please approve/reject the essay'
  # >            },
  # >            id='b9b2b9d788f482663ced6dc755c9e981'
  # >        ),
  # >    )
  # > }
  ```

  An essay has been written and is ready for review. Once the review is provided, we can resume the workflow:

  ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langgraph.types import Command

  # Get review from a user (e.g., via a UI)
  # In this case, we're using a bool, but this can be any json-serializable value.
  human_review = True

  for item in workflow.stream(Command(resume=human_review), config):
      print(item)
  ```

  ```pycon theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  {'workflow': {'essay': 'An essay about topic: cat', 'is_approved': False}}
  ```

  The workflow has been completed and the review has been added to the essay.
</Accordion>

## Entrypoint

The [`@entrypoint`](https://reference.langchain.com/python/langgraph/func/entrypoint) decorator can be used to create a workflow from a function. It encapsulates workflow logic and manages execution flow, including handling *long-running tasks* and [interrupts](/oss/python/langgraph/interrupts).

### Definition

An **entrypoint** is defined by decorating a function with the `@entrypoint` decorator.

The function **must accept a single positional argument**, which serves as the workflow input. If you need to pass multiple pieces of data, use a dictionary as the input type for the first argument.

Decorating a function with an `entrypoint` produces a [`Pregel`](https://reference.langchain.com/python/langgraph/pregel/#langgraph.pregel.Pregel.stream) instance which helps to manage the execution of the workflow (e.g., handles streaming, resumption, and checkpointing).

You will usually want to pass a **checkpointer** to the `@entrypoint` decorator to enable persistence and use features like **human-in-the-loop**.

<Tabs>
  <Tab title="Sync">
    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    from langgraph.func import entrypoint

    @entrypoint(checkpointer=checkpointer)
    def my_workflow(some_input: dict) -> int:
        # some logic that may involve long-running tasks like API calls,
        # and may be interrupted for human-in-the-loop.
        ...
        return result
    ```
  </Tab>

  <Tab title="Async">
    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    from langgraph.func import entrypoint

    @entrypoint(checkpointer=checkpointer)
    async def my_workflow(some_input: dict) -> int:
        # some logic that may involve long-running tasks like API calls,
        # and may be interrupted for human-in-the-loop
        ...
        return result
    ```
  </Tab>
</Tabs>

<Warning>
  **Serialization**
  The **inputs** and **outputs** of entrypoints must be JSON-serializable to support checkpointing. Please see the [serialization](#serialization) section for more details.
</Warning>

### Injectable parameters

When declaring an `entrypoint`, you can request access to additional parameters that will be injected automatically at runtime. These parameters include:

| Parameter    | Description                                                                                                                                                                 |
| ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **previous** | Access the state associated with the previous `checkpoint` for the given thread. See [short-term-memory](#short-term-memory).                                               |
| **store**    | An instance of \[BaseStore]\[langgraph.store.base.BaseStore]. Useful for [long-term memory](/oss/python/langgraph/use-functional-api#long-term-memory).                     |
| **writer**   | Use to access the StreamWriter when working with Async Python \< 3.11. See [streaming with functional API for details](/oss/python/langgraph/use-functional-api#streaming). |
| **config**   | For accessing run time configuration. See [RunnableConfig](https://python.langchain.com/docs/concepts/runnables/#runnableconfig) for information.                           |

<Warning>
  Declare the parameters with the appropriate name and type annotation.
</Warning>

<Accordion title="Requesting Injectable Parameters">
  ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langchain_core.runnables import RunnableConfig
  from langgraph.func import entrypoint
  from langgraph.store.base import BaseStore
  from langgraph.store.memory import InMemoryStore
  from langgraph.checkpoint.memory import InMemorySaver
  from langgraph.types import StreamWriter

  in_memory_checkpointer = InMemorySaver(...)
  in_memory_store = InMemoryStore(...)  # An instance of InMemoryStore for long-term memory

  @entrypoint(
      checkpointer=in_memory_checkpointer,  # Specify the checkpointer
      store=in_memory_store  # Specify the store
  )
  def my_workflow(
      some_input: dict,  # The input (e.g., passed via `invoke`)
      *,
      previous: Any = None, # For short-term memory
      store: BaseStore,  # For long-term memory
      writer: StreamWriter,  # For streaming custom data
      config: RunnableConfig  # For accessing the configuration passed to the entrypoint
  ) -> ...:
  ```
</Accordion>

### Executing

Using the [`@entrypoint`](#entrypoint) yields a [`Pregel`](https://reference.langchain.com/python/langgraph/pregel/#langgraph.pregel.Pregel.stream) object that can be executed using the `invoke`, `ainvoke`, `stream`, and `astream` methods.

<Tabs>
  <Tab title="Invoke">
    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    config = {
        "configurable": {
            "thread_id": "some_thread_id"
        }
    }
    my_workflow.invoke(some_input, config)  # Wait for the result synchronously
    ```
  </Tab>

  <Tab title="Async Invoke">
    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    config = {
        "configurable": {
            "thread_id": "some_thread_id"
        }
    }
    await my_workflow.ainvoke(some_input, config)  # Await result asynchronously
    ```
  </Tab>

  <Tab title="Stream">
    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    config = {
        "configurable": {
            "thread_id": "some_thread_id"
        }
    }

    for chunk in my_workflow.stream(some_input, config):
        print(chunk)
    ```
  </Tab>

  <Tab title="Async Stream">
    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    config = {
        "configurable": {
            "thread_id": "some_thread_id"
        }
    }

    async for chunk in my_workflow.astream(some_input, config):
        print(chunk)
    ```
  </Tab>
</Tabs>

### Resuming

Resuming an execution after an [interrupt](https://reference.langchain.com/python/langgraph/types/interrupt) can be done by passing a **resume** value to the [`Command`](https://reference.langchain.com/python/langgraph/types/Command) primitive.

<Tabs>
  <Tab title="Invoke">
    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    from langgraph.types import Command

    config = {
        "configurable": {
            "thread_id": "some_thread_id"
        }
    }

    my_workflow.invoke(Command(resume=some_resume_value), config)
    ```
  </Tab>

  <Tab title="Async Invoke">
    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    from langgraph.types import Command

    config = {
        "configurable": {
            "thread_id": "some_thread_id"
        }
    }

    await my_workflow.ainvoke(Command(resume=some_resume_value), config)
    ```
  </Tab>

  <Tab title="Stream">
    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    from langgraph.types import Command

    config = {
        "configurable": {
            "thread_id": "some_thread_id"
        }
    }

    for chunk in my_workflow.stream(Command(resume=some_resume_value), config):
        print(chunk)
    ```
  </Tab>

  <Tab title="Async Stream">
    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    from langgraph.types import Command

    config = {
        "configurable": {
            "thread_id": "some_thread_id"
        }
    }

    async for chunk in my_workflow.astream(Command(resume=some_resume_value), config):
        print(chunk)
    ```
  </Tab>
</Tabs>

**Resuming after an error**

To resume after an error, run the `entrypoint` with a `None` and the same **thread id** (config).

This assumes that the underlying **error** has been resolved and execution can proceed successfully.

<Tabs>
  <Tab title="Invoke">
    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}

    config = {
        "configurable": {
            "thread_id": "some_thread_id"
        }
    }

    my_workflow.invoke(None, config)
    ```
  </Tab>

  <Tab title="Async Invoke">
    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}

    config = {
        "configurable": {
            "thread_id": "some_thread_id"
        }
    }

    await my_workflow.ainvoke(None, config)
    ```
  </Tab>

  <Tab title="Stream">
    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}

    config = {
        "configurable": {
            "thread_id": "some_thread_id"
        }
    }

    for chunk in my_workflow.stream(None, config):
        print(chunk)
    ```
  </Tab>

  <Tab title="Async Stream">
    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}

    config = {
        "configurable": {
            "thread_id": "some_thread_id"
        }
    }

    async for chunk in my_workflow.astream(None, config):
        print(chunk)
    ```
  </Tab>
</Tabs>

### Short-term memory

When an `entrypoint` is defined with a `checkpointer`, it stores information between successive invocations on the same **thread id** in [checkpoints](/oss/python/langgraph/checkpointers#checkpoints).

This allows accessing the state from the previous invocation using the `previous` parameter.

By default, the `previous` parameter is the return value of the previous invocation.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
@entrypoint(checkpointer=checkpointer)
def my_workflow(number: int, *, previous: Any = None) -> int:
    previous = previous or 0
    return number + previous

config = {
    "configurable": {
        "thread_id": "some_thread_id"
    }
}

my_workflow.invoke(1, config)  # 1 (previous was None)
my_workflow.invoke(2, config)  # 3 (previous was 1 from the previous invocation)
```

#### `entrypoint.final`

[`entrypoint.final`](https://reference.langchain.com/python/langgraph/func/entrypoint/final) is a special primitive that can be returned from an entrypoint and allows **decoupling** the value that is **saved in the checkpoint** from the **return value of the entrypoint**.

The first value is the return value of the entrypoint, and the second value is the value that will be saved in the checkpoint. The type annotation is `entrypoint.final[return_type, save_type]`.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
@entrypoint(checkpointer=checkpointer)
def my_workflow(number: int, *, previous: Any = None) -> entrypoint.final[int, int]:
    previous = previous or 0
    # This will return the previous value to the caller, saving
    # 2 * number to the checkpoint, which will be used in the next invocation
    # for the `previous` parameter.
    return entrypoint.final(value=previous, save=2 * number)

config = {
    "configurable": {
        "thread_id": "1"
    }
}

my_workflow.invoke(3, config)  # 0 (previous was None)
my_workflow.invoke(1, config)  # 6 (previous was 3 * 2 from the previous invocation)
```

## Task

A **task** represents a discrete unit of work, such as an API call or data processing step. It has two key characteristics:

* **Asynchronous Execution**: Tasks are designed to be executed asynchronously, allowing multiple operations to run concurrently without blocking.
* **Checkpointing**: Task results are saved to a checkpoint, enabling resumption of the workflow from the last saved state. (See [persistence](/oss/python/langgraph/persistence) for more details).

### Definition

Tasks are defined using the `@task` decorator, which wraps a regular Python function.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langgraph.func import task

@task()
def slow_computation(input_value):
    # Simulate a long-running operation
    ...
    return result
```

<Warning>
  **Serialization**
  The **outputs** of tasks must be JSON-serializable to support checkpointing.
</Warning>

### Execution

**Tasks** can only be called from within an **entrypoint**, another **task**, or a [state graph node](/oss/python/langgraph/graph-api#nodes).

Tasks *cannot* be called directly from the main application code.

When you call a **task**, it returns *immediately* with a future object. A future is a placeholder for a result that will be available later.

To obtain the result of a **task**, you can either wait for it synchronously (using `result()`) or await it asynchronously (using `await`).

<Tabs>
  <Tab title="Synchronous Invocation">
    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    @entrypoint(checkpointer=checkpointer)
    def my_workflow(some_input: int) -> int:
        future = slow_computation(some_input)
        return future.result()  # Wait for the result synchronously
    ```
  </Tab>

  <Tab title="Asynchronous Invocation">
    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    @entrypoint(checkpointer=checkpointer)
    async def my_workflow(some_input: int) -> int:
        return await slow_computation(some_input)  # Await result asynchronously
    ```
  </Tab>
</Tabs>

## When to use a task

**Tasks** are useful in the following scenarios:

* **Checkpointing**: When you need to save the result of a long-running operation to a checkpoint, so you don't need to recompute it when resuming the workflow.
* **Human-in-the-loop**: If you're building a workflow that requires human intervention, you MUST use **tasks** to encapsulate any randomness (e.g., API calls) to ensure that the workflow can be resumed correctly. See the [determinism](#determinism) section for more details.
* **Parallel Execution**: For I/O-bound tasks, **tasks** enable parallel execution, allowing multiple operations to run concurrently without blocking (e.g., calling multiple APIs).
* **Observability**: Wrapping operations in **tasks** provides a way to track the progress of the workflow and monitor the execution of individual operations using [LangSmith](/langsmith/observability).
* **Retryable Work**: When work needs to be retried to handle failures or inconsistencies, **tasks** provide a way to encapsulate and manage the retry logic.

## Serialization

There are two key aspects to serialization in LangGraph:

1. `entrypoint` inputs and outputs must be JSON-serializable.
2. `task` outputs must be JSON-serializable.

These requirements are necessary for enabling checkpointing and workflow resumption. Use python primitives like dictionaries, lists, strings, numbers, and booleans to ensure that your inputs and outputs are serializable.

Serialization ensures that workflow state, such as task results and intermediate values, can be reliably saved and restored. This is critical for enabling human-in-the-loop interactions, fault tolerance, and parallel execution.

Providing non-serializable inputs or outputs will result in a runtime error when a workflow is configured with a checkpointer.

## Determinism

When you resume a workflow run, the code does **NOT** resume from the **same line of code** where execution stopped. Execution returns to a checkpoint boundary, and the workflow **replays** forward until it reaches the pause again.

For the Functional API, replay starts at the beginning of the **entrypoint** while LangGraph restores completed [**task**](/oss/python/langgraph/functional-api#task) and [**subgraph**](/oss/python/langgraph/use-subgraphs) results from the checkpointer instead of recomputing them. That preserves the recorded order of steps across pauses, including for long-running or non-deterministic **task** outputs.

To use features like **human-in-the-loop**, you must place non-deterministic work (for example, random values) and side effects (for example, file writes or API calls) in [**tasks**](/oss/python/langgraph/functional-api#task).

Different runs of a workflow can produce different results, but resuming a **specific** thread should replay the same persisted **task** and **subgraph** results.

To ensure that your workflow is deterministic and can be consistently replayed, follow these guidelines:

* **Avoid repeating work**: In an **entrypoint**, if you chain several side effects (for example, logging, file writes, or network calls), give each its own **task** so resume restores their outputs from the checkpointer instead of running them again.
* **Encapsulate non-deterministic operations**: Keep values that can change between attempts (for example, random numbers or wall-clock reads) inside **tasks**, so replay lines up with what was checkpointed.
* **Use idempotent operations**: For partial task failures and retries, see [Idempotency](#idempotency).

## Idempotency

Idempotency ensures that running the same operation multiple times produces the same result. This helps prevent duplicate API calls and redundant processing if a step is rerun due to a failure. Always place API calls inside **tasks** functions for checkpointing, and design them to be idempotent in case of re-execution.
This is particularly important for operations that result in data writes.
When a workflow resumes, LangGraph replays completed **task** results from the checkpoint. A **task** that started but did not finish may run again on that resume, so design side effects to be idempotent. Use idempotency keys or verify existing results to avoid unintended duplication.

## Common pitfalls

### Handling side effects

Encapsulate side effects (e.g., writing to a file, sending an email) in tasks to ensure they are not executed multiple times when resuming a workflow.

<Tabs>
  <Tab title="Incorrect">
    In this example, a side effect (writing to a file) is directly included in the workflow, so it will be executed a second time when resuming the workflow.

    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    @entrypoint(checkpointer=checkpointer)
    def my_workflow(inputs: dict) -> int:
        # This code will be executed a second time when resuming the workflow.
        # Which is likely not what you want.
        with open("output.txt", "w") as f:  # [!code highlight]
            f.write("Side effect executed")  # [!code highlight]
        value = interrupt("question")
        return value
    ```
  </Tab>

  <Tab title="Correct">
    In this example, the side effect is encapsulated in a task, ensuring consistent execution upon resumption.

    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    from langgraph.func import task

    @task  # [!code highlight]
    def write_to_file():  # [!code highlight]
        with open("output.txt", "w") as f:
            f.write("Side effect executed")

    @entrypoint(checkpointer=checkpointer)
    def my_workflow(inputs: dict) -> int:
        # The side effect is now encapsulated in a task.
        write_to_file().result()
        value = interrupt("question")
        return value
    ```
  </Tab>
</Tabs>

### Non-deterministic control flow

Operations that might give different results each time (like getting current time or random numbers) should be encapsulated in tasks to ensure that on resume, the same result is returned.

* In a task: Get random number (5) → interrupt → resume → (returns 5 again) → ...
* Not in a task: Get random number (5) → interrupt → resume → get new random number (7) → ...

This is especially important when using **human-in-the-loop** workflows with multiple interrupt calls. LangGraph keeps a list of resume values for each task/entrypoint. When an interrupt is encountered, it's matched with the corresponding resume value. This matching is strictly **index-based**, so the order of the resume values should match the order of the interrupts.

If order of execution is not maintained when resuming, one [`interrupt`](https://reference.langchain.com/python/langgraph/types/interrupt) call may be matched with the wrong `resume` value, leading to incorrect results.

Please read the section on [determinism](#determinism) for more details.

<Tabs>
  <Tab title="Incorrect">
    In this example, the workflow uses the current time to determine which task to execute. This is non-deterministic because the result of the workflow depends on the time at which it is executed.

    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    from langgraph.func import entrypoint

    @entrypoint(checkpointer=checkpointer)
    def my_workflow(inputs: dict) -> int:
        t0 = inputs["t0"]
        t1 = time.time()  # [!code highlight]

        delta_t = t1 - t0

        if delta_t > 1:
            result = slow_task(1).result()
            value = interrupt("question")
        else:
            result = slow_task(2).result()
            value = interrupt("question")

        return {
            "result": result,
            "value": value
        }
    ```
  </Tab>

  <Tab title="Correct">
    In this example, the workflow uses the input `t0` to determine which task to execute. This is deterministic because the result of the workflow depends only on the input.

    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    import time

    from langgraph.func import task

    @task  # [!code highlight]
    def get_time() -> float:  # [!code highlight]
        return time.time()

    @entrypoint(checkpointer=checkpointer)
    def my_workflow(inputs: dict) -> int:
        t0 = inputs["t0"]
        t1 = get_time().result()  # [!code highlight]

        delta_t = t1 - t0

        if delta_t > 1:
            result = slow_task(1).result()
            value = interrupt("question")
        else:
            result = slow_task(2).result()
            value = interrupt("question")

        return {
            "result": result,
            "value": value
        }
    ```
  </Tab>
</Tabs>

## Learn more

* [How to use the Functional API](/oss/python/langgraph/use-functional-api)
* [Graph API conceptual overview](/oss/python/langgraph/graph-api)
* [Choosing between Graph API and Functional API](/oss/python/langgraph/choosing-apis)

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langgraph/functional-api.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Graph API overview
Source: https://docs.langchain.com/oss/python/langgraph/graph-api

## Graphs

At its core, LangGraph models agent workflows as graphs. You define the behavior of your agents using three key components:

1. [`State`](#state): A shared data structure that represents the current snapshot of your application. It can be any data type, but is typically defined using a shared state schema.

2. [`Nodes`](#nodes): Functions that encode the logic of your agents. They receive the current state as input, perform some computation or side-effect, and return an updated state.

3. [`Edges`](#edges): Functions that determine which `Node` to execute next based on the current state. They can be conditional branches or fixed transitions.

By composing `Nodes` and `Edges`, you can create complex, looping workflows that evolve the state over time. The real power, though, comes from how LangGraph manages that state.

To emphasize: `Nodes` and `Edges` are nothing more than functions—they can contain an LLM or just good ol' code.

In short: *nodes do the work, edges tell what to do next*.

LangGraph's underlying graph algorithm uses [message passing](https://en.wikipedia.org/wiki/Message_passing) to define a general program. When a Node completes its operation, it sends messages along one or more edges to other node(s). These recipient nodes then execute their functions, pass the resulting messages to the next set of nodes, and the process continues. Inspired by Google's [Pregel](https://research.google/pubs/pregel-a-system-for-large-scale-graph-processing/) system, the program proceeds in discrete "super-steps."

A super-step can be considered a single iteration over the graph nodes. Nodes that run in parallel are part of the same super-step, while nodes that run sequentially belong to separate super-steps. At the start of graph execution, all nodes begin in an `inactive` state. A node becomes `active` when it receives a new message (state) on any of its incoming edges (or "channels"). The active node then runs its function and responds with updates. At the end of each super-step, nodes with no incoming messages vote to `halt` by marking themselves as `inactive`. The graph execution terminates when all nodes are `inactive` and no messages are in transit.

### StateGraph

The [`StateGraph`](https://reference.langchain.com/python/langgraph/graph/state/StateGraph) class is the main graph class to use. This is parameterized by a user defined `State` object.

### Compiling your graph

To build your graph, you first define the [state](#state), you then add [nodes](#nodes) and [edges](#edges), and then you compile it. What exactly is compiling your graph and why is it needed?

Compiling is a pretty simple step. It provides a few basic checks on the structure of your graph (no orphaned nodes, etc). It is also where you can specify runtime args like [checkpointers](/oss/python/langgraph/persistence) and breakpoints. You compile your graph by just calling the `.compile` method:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
graph = graph_builder.compile(...)
```

<Warning>
  You **MUST** compile your graph before you can use it.
</Warning>

## State

The first thing you do when you define a graph is define the `State` of the graph. The `State` consists of the [schema of the graph](#schema) as well as [`reducer` functions](#reducers) which specify how to apply updates to the state. The schema of the `State` will be the input schema to all `Nodes` and `Edges` in the graph, and can be either a `TypedDict` or a `Pydantic` model. All `Nodes` will emit updates to the `State` which are then applied using the specified `reducer` function.

### Schema

The main documented way to specify the schema of a graph is by using a [`TypedDict`](https://docs.python.org/3/library/typing.html#typing.TypedDict). If you want to provide default values in your state, use a [`dataclass`](https://docs.python.org/3/library/dataclasses.html). We also support using a Pydantic [`BaseModel`](/oss/python/langgraph/use-graph-api#use-pydantic-models-for-graph-state) as your graph state if you want recursive data validation (though note that Pydantic is less performant than a `TypedDict` or `dataclass`).

By default, the graph will have the same input and output schemas. If you want to change this, you can also specify explicit input and output schemas directly. This is useful when you have a lot of keys, and some are explicitly for input and others for output. See the [guide](/oss/python/langgraph/use-graph-api#define-input-and-output-schemas) for more information.

<Info>
  The higher-level [`create_agent`](/oss/python/langchain/agents) factory in `langchain` does not support Pydantic state schemas.
</Info>

#### Multiple schemas

Typically, all graph nodes communicate with a single schema. This means that they will read and write to the same state channels. But, there are cases where we want more control over this:

* Internal nodes can pass information that is not required in the graph's input / output.
* We may also want to use different input / output schemas for the graph. The output might, for example, only contain a single relevant output key.

It is possible to have nodes write to private state channels inside the graph for internal node communication. We can simply define a private schema, `PrivateState`.

It is also possible to define explicit input and output schemas for a graph. In these cases, we define an "internal" schema that contains *all* keys relevant to graph operations. But, we also define `input` and `output` schemas that are sub-sets of the "internal" schema to constrain the input and output of the graph. See [Define input and output schemas](/oss/python/langgraph/use-graph-api#define-input-and-output-schemas) for more detail.

Let's look at an example:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
class InputState(TypedDict):
    user_input: str

class OutputState(TypedDict):
    graph_output: str

class OverallState(TypedDict):
    foo: str
    user_input: str
    graph_output: str

class PrivateState(TypedDict):
    bar: str

def node_1(state: InputState) -> OverallState:
    # Write to OverallState
    return {"foo": state["user_input"] + " name"}

def node_2(state: OverallState) -> PrivateState:
    # Read from OverallState, write to PrivateState
    return {"bar": state["foo"] + " is"}

def node_3(state: PrivateState) -> OutputState:
    # Read from PrivateState, write to OutputState
    return {"graph_output": state["bar"] + " Lance"}

builder = StateGraph(OverallState,input_schema=InputState,output_schema=OutputState)
builder.add_node("node_1", node_1)
builder.add_node("node_2", node_2)
builder.add_node("node_3", node_3)
builder.add_edge(START, "node_1")
builder.add_edge("node_1", "node_2")
builder.add_edge("node_2", "node_3")
builder.add_edge("node_3", END)

graph = builder.compile()
graph.invoke({"user_input":"My"})

# {'graph_output': 'My name is Lance'}
```

There are two subtle and important points to note here:

1. We pass `state: InputState` as the input schema to `node_1`. But, we write out to `foo`, a channel in `OverallState`. How can we write out to a state channel that is not included in the input schema? This is because a node *can write to any state channel in the graph state.* The graph state is the union of the state channels defined at initialization, which includes `OverallState` and the filters `InputState` and `OutputState`.

2. We initialize the graph with:

   ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
   StateGraph(
       OverallState,
       input_schema=InputState,
       output_schema=OutputState
   )
   ```

   How can we write to `PrivateState` in `node_2`? How does the graph gain access to this schema if it was not passed in the `StateGraph` initialization?

   We can do this because `_nodes` can also declare additional state `channels_` as long as the state schema definition exists. In this case, the `PrivateState` schema is defined, so we can add `bar` as a new state channel in the graph and write to it.

<Warning>
  **Private channels are not redacted when streaming.**

  Input, output, and private schemas constrain what each node *reads* (its input schema) and what `invoke` *returns* (the output schema). They do **not** hide channels from `stream`.

  When you stream with `stream_mode="values"`, the graph emits **all** of its state channels by default, including private ones, because values streaming defaults to the full set of state channels rather than the output schema. This is why a private channel like `bar` is hidden by `invoke` but visible while streaming:

  ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  for chunk in graph.stream({"user_input": "My"}, stream_mode="values"):
      print(chunk)
  # {'user_input': 'My'}
  # {'user_input': 'My', 'foo': 'My name'}
  # {'user_input': 'My', 'foo': 'My name', 'bar': 'My name is'}        # <-- private channel
  # {'user_input': 'My', 'foo': 'My name', 'bar': 'My name is', 'graph_output': 'My name is Lance'}
  ```

  To restrict the streamed values to a specific set of channels (e.g. only the output schema), pass `output_keys`:

  ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  for chunk in graph.stream(
      {"user_input": "My"},
      stream_mode="values",
      output_keys=["graph_output"],  # [!code highlight]
  ):
      print(chunk)
  # {'graph_output': 'My name is Lance'}
  ```

  If you only need the channels a node actually produced each step (rather than the full accumulated state), use `stream_mode="updates"` instead.
</Warning>

### Reducers

Reducers are key to understanding how updates from nodes are applied to the `State`. Each key in the `State` has its own independent reducer function. If no reducer function is explicitly specified then it is assumed that all updates to that key should override it. There are a few different types of reducers, starting with the default type of reducer:

#### Default reducer

These two examples show how to use the default reducer:

```python Example A theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from typing_extensions import TypedDict

class State(TypedDict):
    foo: int
    bar: list[str]
```

In this example, no reducer functions are specified for any key. Let's assume the input to the graph is:

`{"foo": 1, "bar": ["hi"]}`. Let's then assume the first `Node` returns `{"foo": 2}`. This is treated as an update to the state. Notice that the `Node` does not need to return the whole `State` schema - just an update. After applying this update, the `State` would then be `{"foo": 2, "bar": ["hi"]}`. If the second node returns `{"bar": ["bye"]}` then the `State` would then be `{"foo": 2, "bar": ["bye"]}`

```python Example B theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from typing import Annotated
from typing_extensions import TypedDict
from operator import add

class State(TypedDict):
    foo: int
    bar: Annotated[list[str], add]
```

In this example, we've used the `Annotated` type to specify a reducer function (`operator.add`) for the second key (`bar`). Note that the first key remains unchanged. Let's assume the input to the graph is `{"foo": 1, "bar": ["hi"]}`. Let's then assume the first `Node` returns `{"foo": 2}`. This is treated as an update to the state. Notice that the `Node` does not need to return the whole `State` schema - just an update. After applying this update, the `State` would then be `{"foo": 2, "bar": ["hi"]}`. If the second node returns `{"bar": ["bye"]}` then the `State` would then be `{"foo": 2, "bar": ["hi", "bye"]}`. Notice here that the `bar` key is updated by adding the two lists together.

#### Overwrite

<Tip>
  In some cases, you may want to bypass a reducer and directly overwrite a state value. LangGraph provides the [`Overwrite`](https://reference.langchain.com/python/langgraph/types/) type for this purpose. [Learn how to use `Overwrite` here](/oss/python/langgraph/use-graph-api#bypass-reducers-with-overwrite).
</Tip>

### Working with messages in graph state

#### Why use messages?

Most modern LLM providers have a chat model interface that accepts a list of messages as input. LangChain's [chat model interface](/oss/python/langchain/models) in particular accepts a list of message objects as inputs. These messages come in a variety of forms such as [`HumanMessage`](https://reference.langchain.com/python/langchain-core/messages/human/HumanMessage) (user input) or [`AIMessage`](https://reference.langchain.com/python/langchain-core/messages/ai/AIMessage) (LLM response).

To read more about what message objects are, please refer to the [Messages conceptual guide](/oss/python/langchain/messages).

#### Using messages in your graph

In many cases, it is helpful to store prior conversation history as a list of messages in your graph state. To do so, we can add a key (channel) to the graph state that stores a list of `Message` objects and annotate it with a reducer function (see `messages` key in the example below). The reducer function is vital to telling the graph how to update the list of `Message` objects in the state with each state update (for example, when a node sends an update). If you don't specify a reducer, every state update will overwrite the list of messages with the most recently provided value. If you wanted to simply append messages to the existing list, you could use `operator.add` as a reducer.

However, you might also want to manually update messages in your graph state (e.g. human-in-the-loop). If you were to use `operator.add`, the manual state updates you send to the graph would be appended to the existing list of messages, instead of updating existing messages. To avoid that, you need a reducer that can keep track of message IDs and overwrite existing messages, if updated. To achieve this, you can use the prebuilt [`add_messages`](https://reference.langchain.com/python/langgraph/graph/message/add_messages) function. For brand new messages, it will simply append to existing list, but it will also handle the updates for existing messages correctly.

#### Serialization

In addition to keeping track of message IDs, the [`add_messages`](https://reference.langchain.com/python/langgraph/graph/message/add_messages) function will also try to deserialize messages into LangChain `Message` objects whenever a state update is received on the `messages` channel.

For more information, see [LangChain serialization/deserialization](https://python.langchain.com/docs/how_to/serialization/). This allows sending graph inputs / state updates in the following format:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}

# this is supported
{"messages": [HumanMessage(content="message")]}
