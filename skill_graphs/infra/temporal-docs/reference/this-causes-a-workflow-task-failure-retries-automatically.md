# This causes a Workflow Task failure (retries automatically)
raise ValueError("Unexpected condition")
```

This is intentional.
Regular Python exceptions are treated as bugs that can be fixed with a code deployment, not business logic failures.
The Workflow Task retries indefinitely, letting you fix the bug and redeploy without losing Workflow state.

## Handle exceptions in Workflows {/* #handle-exceptions-in-workflows */}

**How to handle exceptions in Workflows using the Temporal Python SDK**

Use Python's `try/except` blocks to handle Activity failures in your Workflow:

```python
from temporalio import workflow
from temporalio.exceptions import ActivityError, ApplicationError
from datetime import timedelta

@workflow.defn
class MoneyTransferWorkflow:
    @workflow.run
    async def run(self, details):
        # Withdraw money
        try:
            withdraw_result = await workflow.execute_activity(
                withdraw,
                details,
                start_to_close_timeout=timedelta(seconds=10)
            )
        except ActivityError as e:
            raise ApplicationError(
                f"Withdrawal failed: {e.cause}",
                type="WithdrawalError"
            )

        # Deposit money
        try:
            deposit_result = await workflow.execute_activity(
                deposit,
                details,
                start_to_close_timeout=timedelta(seconds=10)
            )
        except ActivityError as e:
            # Deposit failed - attempt refund
            try:
                await workflow.execute_activity(
                    refund,
                    withdraw_result,
                    start_to_close_timeout=timedelta(seconds=10)
                )
                raise ApplicationError(
                    f"Deposit failed but money refunded to source account",
                    type="DepositError"
                )
            except ActivityError as refund_err:
                raise ApplicationError(
                    f"Deposit failed and refund also failed: {refund_err.cause}",
                    type="CriticalTransferError"
                )

        return f"Transfer complete: {withdraw_result}, {deposit_result}"
```

Common Temporal exceptions you can catch in Workflows:
- `ActivityError` - Activity failed after exhausting retries
- `ChildWorkflowError` - Child Workflow failed
- `CancelledError` - Workflow, Activity, or Timer was canceled
- `TimeoutError` - Operation exceeded timeout

If these exceptions propagate unhandled, the Workflow Execution fails (or enters "Canceled" state for `CancelledError`).

## Configure custom Retry Policies {/* #configure-custom-retry-policies */}

**How to configure custom Retry Policies using the Temporal Python SDK**

Activities have a default Retry Policy with unlimited attempts and exponential backoff.
Customize this to match your expected failure patterns.

```python
from temporalio import workflow
from temporalio.common import RetryPolicy
from datetime import timedelta

@workflow.defn
class OrderWorkflow:
    @workflow.run
    async def run(self, order):
        # Custom retry for rate-limited service
        retry_policy = RetryPolicy(
            initial_interval=timedelta(seconds=10),
            backoff_coefficient=3.0,
            maximum_interval=timedelta(minutes=5),
            maximum_attempts=20,
        )

        result = await workflow.execute_activity(
            call_external_service,
            order,
            start_to_close_timeout=timedelta(seconds=30),
            retry_policy=retry_policy,
        )
        return result
```

Retry Policy attributes:
- **`initial_interval`**: Delay before first retry (default: 1 second)
- **`backoff_coefficient`**: Multiplier for subsequent delays (default: 2.0)
- **`maximum_interval`**: Cap on retry delay (default: 100× initial interval)
- **`maximum_attempts`**: Maximum retry attempts (default: unlimited)
- **`non_retryable_error_types`**: Error types that shouldn't retry (default: empty)

### Match your Retry Policy to failure types

**For transient failures** (brief network issues): Use the defaults or a low `initial_interval` and `backoff_coefficient`.

**For intermittent failures** (rate limiting): Increase `initial_interval` and `backoff_coefficient` to space out retries and let the condition resolve.

**For cost-sensitive APIs**: Set `maximum_attempts` to limit retries (rare—usually prefer timeouts).

### Use different policies for different Activities

You can use different Retry Policies for different Activities, or even multiple policies for the same Activity:

```python
fast_retry = RetryPolicy(
    initial_interval=timedelta(seconds=1),
    backoff_coefficient=1.5,
)

slow_retry = RetryPolicy(
    initial_interval=timedelta(seconds=30),
    backoff_coefficient=3.0,
)
