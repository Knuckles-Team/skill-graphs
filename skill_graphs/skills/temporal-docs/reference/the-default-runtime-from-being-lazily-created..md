# the default Runtime from being lazily created.
new_runtime = Runtime(telemetry=TelemetryConfig(metrics=PrometheusConfig(bind_address="0.0.0.0:9000")))
my_client = await Client.connect("my.temporal.host:7233", runtime=new_runtime)
```

## Set up tracing {/* #tracing */}

**How to set up tracing**

Tracing allows you to view the call graph of a Workflow along with its Activities and any Child Workflows.

Temporal Web's tracing capabilities mainly track Activity Execution within a Temporal context. If you need custom tracing specific for your use case, you should make use of context propagation to add tracing logic accordingly.

To configure tracing in Python, install the `opentelemetry` dependencies.

```bash
