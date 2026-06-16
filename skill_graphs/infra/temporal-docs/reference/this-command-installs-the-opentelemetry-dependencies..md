# This command installs the `opentelemetry` dependencies.
pip install temporalio[opentelemetry]
```

Then the [`temporalio.contrib.opentelemetry.TracingInterceptor`](https://python.temporal.io/temporalio.contrib.opentelemetry.TracingInterceptor.html) class can be set as an interceptor as an argument of [`Client.connect()`](https://python.temporal.io/temporalio.client.Client.html#connect).

When your Client is connected, spans are created for all Client calls, Activities, and Workflow invocations on the Worker.
Spans are created and serialized through the server to give one trace for a Workflow Execution.

## Log from a Workflow {/* #logging */}

Logging enables you to record critical information during code execution.
Loggers create an audit trail and capture information about your Workflow's operation.
An appropriate logging level depends on your specific needs.
During development or troubleshooting, you might use debug or even trace.
In production, you might use info or warn to avoid excessive log volume.

The logger supports the following logging levels:

| Level   | Use                                                                                                       |
| ------- | --------------------------------------------------------------------------------------------------------- |
| `TRACE` | The most detailed level of logging, used for very fine-grained information.                               |
| `DEBUG` | Detailed information, typically useful for debugging purposes.                                            |
| `INFO`  | General information about the application's operation.                                                    |
| `WARN`  | Indicates potentially harmful situations or minor issues that don't prevent the application from working. |
| `ERROR` | Indicates error conditions that might still allow the application to continue running.                    |

The Temporal SDK core normally uses `WARN` as its default logging level.

**How to log from a Workflow**

Send logs and errors to a logging service, so that when things go wrong, you can see what happened.

The SDK core uses `WARN` for its default logging level.

You can log from a Workflow using Python's standard library, by importing the logging module `logging`.

Set your logging configuration to a level you want to expose logs to.
The following example sets the logging information level to `INFO`.

```python
logging.basicConfig(level=logging.INFO)
```

Then in your Workflow, set your [`logger`](https://python.temporal.io/temporalio.workflow.html#logger) and level on the Workflow. The following example logs the Workflow.

    View the source code
  {' '}
  in the context of the rest of the application code.

```python
