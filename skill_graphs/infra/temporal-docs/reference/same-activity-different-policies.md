# Same Activity, different policies
await workflow.execute_activity(
    process_order,
    order,
    start_to_close_timeout=timedelta(seconds=10),
    retry_policy=fast_retry,
)
