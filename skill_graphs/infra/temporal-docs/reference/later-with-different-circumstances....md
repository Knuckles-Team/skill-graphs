# Later, with different circumstances...
await workflow.execute_activity(
    process_order,
    order,
    start_to_close_timeout=timedelta(seconds=10),
    retry_policy=slow_retry,
)
```

### Don't use Workflow Retry Policies

Unlike Activities, Workflows don't retry by default, and you usually shouldn't add a Retry Policy.
Workflows are deterministic and not designed for failure-prone operations.
A Workflow failure typically indicates a code bug or bad input data—retrying the entire Workflow repeats the same logic without fixing the underlying issue.

If you need retry logic for specific Workflow operations, implement it in your Workflow code rather than using a Workflow Retry Policy.

## Mark specific errors as non-retryable {/* #mark-errors-as-non-retryable */}

**How to mark specific errors as non-retryable using the Temporal Python SDK**

Some failures are permanent and won't resolve through retries.
Mark these as non-retryable to fail fast instead of waiting for timeouts.

Set the `non_retryable` flag when raising an `ApplicationError`:

```python
from temporalio import activity
from temporalio.exceptions import ApplicationError

@activity.defn
async def process_payment(card_number: str, amount: float):
    if not is_valid_card_format(card_number):
        # Invalid format will never become valid through retries
        raise ApplicationError(
            f"Invalid credit card format: {card_number}",
            type="InvalidCardFormat",
            non_retryable=True,
        )

    if amount <= 0:
        # Invalid amount won't be fixed by retrying
        raise ApplicationError(
            f"Amount must be positive: {amount}",
            type="InvalidAmount",
            non_retryable=True,
        )

    # Process payment...
```

An `ApplicationError` with `non_retryable=True` will never retry, regardless of the Retry Policy.

Use non-retryable errors for:
- Invalid input data that prevents the Activity from proceeding
- Business rule violations
- Authorization failures

**Use this sparingly.**
In most cases, it's better to let the Retry Policy handle when to stop retrying based on time or attempts.

## Specify non-retryable error types {/* #specify-non-retryable-error-types */}

**How to specify non-retryable error types in Retry Policies using the Temporal Python SDK**

Sometimes you want the Workflow (caller) to decide which error types shouldn't retry, rather than the Activity (implementer).

List error types that shouldn't retry in your Retry Policy:

```python
from temporalio import workflow
from temporalio.common import RetryPolicy
from datetime import timedelta

@workflow.defn
class CheckoutWorkflow:
    @workflow.run
    async def run(self, payment_details):
        retry_policy = RetryPolicy(
            non_retryable_error_types=[
                "InvalidCardFormat",
                "InsufficientFunds",
                "AccountClosed",
            ]
        )

        try:
            result = await workflow.execute_activity(
                process_payment,
                payment_details,
                start_to_close_timeout=timedelta(seconds=30),
                retry_policy=retry_policy,
            )
            return result
        except ActivityError as e:
            workflow.logger.error(f"Payment failed: {e.cause}")
            # Handle the non-retryable error...
```

When an Activity raises an `ApplicationError`, Temporal checks if its `type` is in `non_retryable_error_types`.
If it matches, the Activity fails immediately without retries.

### When to use each approach

**`non_retryable=True` in the Activity**: Use when the Activity implementer knows the error is permanently unrecoverable.
This enforces the constraint for all callers.

**`non_retryable_error_types` in the Retry Policy**: Use when the caller wants to decide which errors are unrecoverable based on their business logic.
This lets different Workflows make different decisions about the same Activity.

## Implement rollback logic with the Saga pattern {/* #implement-saga-pattern */}

**How to implement the Saga pattern using the Temporal Python SDK**

The Saga pattern coordinates a sequence of operations where each operation has a compensating action to undo its effects.
If any operation fails, execute compensating actions in reverse order to roll back previous operations.

Use this for multi-step processes like:
- E-commerce checkout (payment, inventory, shipping)
- Distributed transactions across services
- Multi-stage data updates

```python
from temporalio import workflow
from temporalio.exceptions import ActivityError
from datetime import timedelta

@workflow.defn
class OrderWorkflow:
    @workflow.run
    async def run(self, order):
        compensations = []

        try:
            # Reserve inventory
            compensations.append({
                "activity": revert_inventory,
                "input": order
            })
            await workflow.execute_activity(
                reserve_inventory,
                order,
                start_to_close_timeout=timedelta(seconds=10),
            )

            # Charge payment
            compensations.append({
                "activity": refund_payment,
                "input": order
            })
            payment_id = await workflow.execute_activity(
                charge_payment,
                order,
                start_to_close_timeout=timedelta(seconds=10),
            )

            # Create shipment
            compensations.append({
                "activity": cancel_shipment,
                "input": payment_id
            })
            shipment_id = await workflow.execute_activity(
                create_shipment,
                order,
                start_to_close_timeout=timedelta(seconds=10),
            )

            return {"payment_id": payment_id, "shipment_id": shipment_id}

        except ActivityError as e:
            workflow.logger.error(f"Order failed: {e.cause}, rolling back...")

            # Execute compensations in reverse order
            for compensation in reversed(compensations):
                try:
                    await workflow.execute_activity(
                        compensation["activity"],
                        compensation["input"],
                        start_to_close_timeout=timedelta(seconds=10),
                    )
                except ActivityError as comp_err:
                    # Log compensation failure but continue with others
                    workflow.logger.error(f"Compensation failed: {comp_err.cause}")

            # Re-raise the original error
            raise ApplicationError(
                f"Order failed: {e.cause}",
                type="OrderFailed"
            )
```

Key points:
- Add compensating actions to a list **before** executing each Activity
- Use `reversed(compensations)` to undo operations in the correct order
- Handle compensation failures gracefully (they might fail too)
- Temporal manages all state and retry logic, making Saga implementation straightforward

## Understand Temporal's failure types {/* #understand-failure-types */}

Temporal uses specialized exception types to represent different failure scenarios.
All exceptions inherit from [`TemporalError`](https://python.temporal.io/temporalio.exceptions.TemporalError.html).

**Do not extend `TemporalError` or its children.**
Use the provided exception types to ensure:
- Consistent behavior across process and language boundaries
- Compatibility with the Temporal Service
- Proper serialization via Protocol Buffers

### Common failure types

**`ApplicationError`**: Raised by your code to indicate application-specific failures.
This is the only Temporal exception you should raise manually.
When you raise an `ApplicationError`, you can optionally provide a `type` string and mark it as `non_retryable`.

**`ActivityError`**: Wraps exceptions raised from Activities.
The `cause` field contains the original error (`ApplicationError`, `TimeoutError`, `CancelledError`, etc.).
Catch this in Workflows to handle Activity failures.

**`TimeoutError`**: Occurs when an Activity or Workflow exceeds its configured timeout.

**`CancelledError`**: Results from cancellation of a Workflow, Activity, or Timer.
You can catch and ignore this to continue execution despite cancellation.

**`TerminatedError`**: Occurs when a Workflow Execution is forcefully terminated.

**`ChildWorkflowError`**: Raised when a Child Workflow Execution fails.

**`WorkflowAlreadyStartedError`**: Raised when attempting to start a Workflow with an ID that's already running.

**`ServerError`**: Used for exceptions from the Temporal Service itself (like database failures).

### Workflow Task vs Workflow Execution failures

**Workflow Task failures** occur when Workflow code raises a non-Temporal exception (like `ValueError`, `TypeError`, or non-determinism errors).
These retry automatically, letting you fix bugs and redeploy without losing Workflow state.

**Workflow Execution failures** occur when Workflow code raises a Temporal exception like `ApplicationError`.
These put the Workflow in "Failed" state with no automatic retries.

Example of a permanent failure that should fail the Workflow:

```python
if distance.kilometers > MAX_DELIVERY_DISTANCE:
    # Retrying won't change the distance - this is permanent
    raise ApplicationError(
        "Customer lives outside service area",
        type="OutsideServiceArea"
    )
```

### Protecting sensitive information

The default Failure Converter copies exception messages and stack traces as plain text visible in the Web UI.
If your exceptions might contain sensitive information, configure a custom Failure Converter to encrypt this data.
See the [Securing Application Data course](https://learn.temporal.io/courses/appdatasec/) for details.

---

## Best Practices - Python SDK

![Python SDK Banner](/img/assets/banner-python-temporal.png)

## Best practices

- [Error handling](/develop/python/best-practices/error-handling)
- [Testing](/develop/python/best-practices/testing-suite)
- [Python SDK sandbox](/develop/python/best-practices/python-sdk-sandbox)
- [Debugging](/develop/python/best-practices/debugging)
- [Data handling](/develop/python/data-handling)
- [Sync vs async](/develop/python/best-practices/python-sdk-sync-vs-async)

---

## Temporal Python SDK sandbox environment

The Temporal Python SDK enables you to run Workflow code in a sandbox environment to help prevent non-determinism errors in your application.
The Temporal Workflow Sandbox for Python is not completely isolated, and some libraries can internally mutate state, which can result in breaking determinism.

## Benefits

Temporal's Python SDK uses a sandbox environment for Workflow runs to make developing Workflow code safer.

If a Workflow Execution performs a non-deterministic event, an exception is thrown, which results in failing the Task Worker.
The Workflow will not progress until the code is fixed.

The Temporal Python sandbox offers a mechanism to _pass through modules_ from outside the sandbox. By default, this includes all standard library modules and Temporal modules. For performance and behavior reasons, users should pass through all models, Activities, Nexus services, or other modules that are in separate files whose calls will be deterministic. For more information, see [Passthrough modules](#passthrough-modules).

## How it works

The Sandbox environment consists of two main components.

- [Global state isolation](#global-state-isolation)
- [Restrictions](#restrictions)

### Global state isolation

The first component of the Sandbox is a global state isolation.
Global state isolation uses `exec` to compile and evaluate statements.

Upon the start of a Workflow, the file in which the Workflow is defined is imported into a newly created sandbox.

If a module is imported by the file, a known set, which includes all of Python's standard library, is _passed through_ from outside the sandbox.

These modules are expected to be free of side effects and have their non-deterministic aspects restricted.

For a full list of modules imported, see [Customize the Sandbox](#customize-the-sandbox).

### Restrictions

Restrictions prevent known non-deterministic library calls.
This is achieved by using proxy objects on modules wrapped around the custom importer set in the sandbox.

Restrictions apply at both the Workflow import level and the Workflow run time.

A default set of restrictions that prevents most dangerous standard library calls.

## Skip Workflow Sandboxing

The following techniques aren't recommended, but they allow you to avoid, skip, or break through the sandbox environment.

Skipping Workflow Sandboxing results in a lack of determinism checks. Using the Workflow Sandboxing environment helps prevent non-determinism errors but doesn't completely negate the risk.

### Skip Sandboxing for a block of code

To skip a sandbox environment for a specific block of code in a Workflow, use [`sandbox_unrestricted()`](https://python.temporal.io/temporalio.workflow.unsafe.html#sandbox_unrestricted). The Workflow will run without sandbox restrictions.

```python
with temporalio.workflow.unsafe.sandbox_unrestricted():
    # Your code
```

### Skip Sandboxing for an entire Workflow

To skip a sandbox environment for a Workflow, set the `sandboxed` argument in the [`@workflow.defn`](https://python.temporal.io/temporalio.workflow.html#defn) decorator to false.
The entire Workflow will run without sandbox restrictions.

```python
@workflow.defn(sandboxed=False)
```

### Skip Sandboxing for a Worker

To skip a sandbox environment for a Worker, set the `workflow_runner` keyword argument of the `Worker` init to [`UnsandboxedWorkflowRunner()`](https://python.temporal.io/temporalio.worker.UnsandboxedWorkflowRunner.html).

## Customize the sandbox

When creating the Worker, the `workflow_runner` defaults to [`SandboxedWorkflowRunner()`](https://python.temporal.io/temporalio.worker.workflow_sandbox.SandboxedWorkflowRunner.html).
The `SandboxedWorkflowRunner` init accepts a `restrictions` keyword argument that defines a set of restrictions to apply to this sandbox.

The [`SandboxRestrictions`](https://python.temporal.io/temporalio.worker.workflow_sandbox.SandboxRestrictions.html) dataclass is immutable and contains four fields that can be customized, but only three have notable values.

- [`passthrough_modules`](https://python.temporal.io/temporalio.worker.workflow_sandbox.SandboxRestrictions.html#passthrough_modules)
- [`invalid_modules_members`](https://python.temporal.io/temporalio.worker.workflow_sandbox.SandboxRestrictions.html#invalid_module_members)
- [`import_notification_policy`](https://python.temporal.io/temporalio.worker.workflow_sandbox.SandboxRestrictions.html#import_notificaton_policy)

### Passthrough modules

By default, the sandbox completely reloads non-standard-library and non-Temporal modules for every Workflow run. Passing through a module means that the module will not be reloaded every time the Workflow runs. Instead, the module will be imported from outside the sandbox and used directly in the Workflow. This can improve performance because importing a module can be a time-consuming process, and passing through a module can avoid this overhead.

:::note
It is important to note that you should only import _known-side-effect-free_ third-party modules: meaning they don't have any unintended consequences when imported and used multiple times. This is because passing through a module means that it will be used multiple times in a Workflow without being reloaded, so any side effects it has won't be repeated. For this reason, it's recommended to only pass through modules that are known to be deterministic, meaning they will always produce the same output given the same input.
:::

One way to pass through a module is at import time in the Workflow file using the [`imports_passed_through`](https://python.temporal.io/temporalio.workflow.unsafe.html#imports_passed_through) context manager.

```python
