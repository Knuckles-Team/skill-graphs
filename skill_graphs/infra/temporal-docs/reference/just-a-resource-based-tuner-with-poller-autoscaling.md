# Just a resource based tuner, with poller autoscaling
tuner = WorkerTuner.create_resource_based(
    target_memory_usage=0.5,
    target_cpu_usage=0.5,
)
worker = Worker(
    client,
    task_queue="foo",
    tuner=tuner,
    workflow_task_poller_behavior=PollerBehaviorAutoscaling(),
    activity_task_poller_behavior=PollerBehaviorAutoscaling()
)
