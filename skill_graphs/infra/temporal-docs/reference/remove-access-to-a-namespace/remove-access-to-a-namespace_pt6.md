| `--fairness-key` | No | **string** Fairness key (max 64 bytes) for proportional task dispatch. Tasks with same key share capacity based on their weight. |
| `--fairness-weight` | No | **float** Weight [0.001-1000] for this fairness key. Keys are dispatched proportionally to their weights. |
| `--headers` | No | **string[]** Temporal workflow headers in 'KEY=VALUE' format. Keys must be identifiers, and values must be JSON values. May be passed multiple times to set multiple Temporal headers. Note: These are workflow headers, not gRPC headers. |
| `--id-conflict-policy` | No | **string-enum** Determines how to resolve a conflict when spawning a new Workflow Execution with a particular Workflow Id used by an existing Open Workflow Execution. Accepted values: Fail, UseExisting, TerminateExisting. |
| `--id-reuse-policy` | No | **string-enum** Re-use policy for the Workflow ID in new Workflow Executions. Accepted values: AllowDuplicate, AllowDuplicateFailedOnly, RejectDuplicate, TerminateIfRunning. |
| `--input`, `-i` | No | **string[]** Input value. Use JSON content or set --input-meta to override. Can't be combined with --input-file. Can be passed multiple times to pass multiple arguments. |
| `--input-base64` | No | **bool** Assume inputs are base64-encoded and attempt to decode them. |
| `--input-file` | No | **string[]** A path or paths for input file(s). Use JSON content or set --input-meta to override. Can't be combined with --input. Can be passed multiple times to pass multiple arguments. |
| `--input-meta` | No | **string[]** Input payload metadata as a `KEY=VALUE` pair. When the KEY is "encoding", this overrides the default ("json/plain"). Can be passed multiple times. Repeated metadata keys are applied to the corresponding inputs in the provided order. |
| `--memo` | No | **string[]** Memo using 'KEY="VALUE"' pairs. Use JSON values. |
| `--priority-key` | No | **int** Priority key (1-5, lower numbers = higher priority). Tasks in a queue should be processed in close-to-priority-order. Default is 3 when not specified. |
| `--run-timeout` | No | **duration** Fail a Workflow Run if it lasts longer than `DURATION`. |
| `--search-attribute` | No | **string[]** Search Attribute in `KEY=VALUE` format. Keys must be identifiers, and values must be JSON values. For example: `'YourKey={"your": "value"}'`. Can be passed multiple times. |
| `--start-delay` | No | **duration** Delay before starting the Workflow Execution. Can't be used with cron schedules. If the Workflow receives a signal or update prior to this time, the Workflow Execution starts immediately. |
| `--static-details` | No | **string** Static Workflow details for human consumption in UIs. Uses Temporal Markdown formatting, may be multiple lines. _(Experimental)_ |
| `--static-summary` | No | **string** Static Workflow summary for human consumption in UIs. Uses Temporal Markdown formatting, should be a single line. _(Experimental)_ |
| `--task-queue`, `-t` | Yes | **string** Workflow Task queue. |
| `--task-timeout` | No | **duration** Fail a Workflow Task if it lasts longer than `DURATION`. This is the Start-to-close timeout for a Workflow Task. |
| `--type` | Yes | **string** Workflow Type name. |
| `--workflow-id`, `-w` | No | **string** Workflow ID. If not supplied, the Service generates a unique ID. |

## execute-update-with-start

Send a message to a Workflow Execution to invoke an Update handler, and wait for
the update to complete. If the Workflow Execution is not running, then a new workflow
execution is started and the update is sent.

Experimental.

```
temporal workflow execute-update-with-start \
  --update-name YourUpdate \
  --update-input '{"update-key": "update-value"}' \
  --workflow-id YourWorkflowId \
  --type YourWorkflowType \
  --task-queue YourTaskQueue \
  --id-conflict-policy Fail \
  --input '{"wf-key": "wf-value"}'
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--cron` | No | **string** Cron schedule for the Workflow. |
| `--execution-timeout` | No | **duration** Fail a WorkflowExecution if it lasts longer than `DURATION`. This time-out includes retries and ContinueAsNew tasks. |
| `--fail-existing` | No | **bool** Fail if the Workflow already exists. |
| `--fairness-key` | No | **string** Fairness key (max 64 bytes) for proportional task dispatch. Tasks with same key share capacity based on their weight. |
| `--fairness-weight` | No | **float** Weight [0.001-1000] for this fairness key. Keys are dispatched proportionally to their weights. |
| `--headers` | No | **string[]** Temporal workflow headers in 'KEY=VALUE' format. Keys must be identifiers, and values must be JSON values. May be passed multiple times to set multiple Temporal headers. Note: These are workflow headers, not gRPC headers. |
| `--id-conflict-policy` | No | **string-enum** Determines how to resolve a conflict when spawning a new Workflow Execution with a particular Workflow Id used by an existing Open Workflow Execution. Accepted values: Fail, UseExisting, TerminateExisting. |
| `--id-reuse-policy` | No | **string-enum** Re-use policy for the Workflow ID in new Workflow Executions. Accepted values: AllowDuplicate, AllowDuplicateFailedOnly, RejectDuplicate, TerminateIfRunning. |
| `--input`, `-i` | No | **string[]** Input value. Use JSON content or set --input-meta to override. Can't be combined with --input-file. Can be passed multiple times to pass multiple arguments. |
| `--input-base64` | No | **bool** Assume inputs are base64-encoded and attempt to decode them. |
| `--input-file` | No | **string[]** A path or paths for input file(s). Use JSON content or set --input-meta to override. Can't be combined with --input. Can be passed multiple times to pass multiple arguments. |
| `--input-meta` | No | **string[]** Input payload metadata as a `KEY=VALUE` pair. When the KEY is "encoding", this overrides the default ("json/plain"). Can be passed multiple times. Repeated metadata keys are applied to the corresponding inputs in the provided order. |
| `--memo` | No | **string[]** Memo using 'KEY="VALUE"' pairs. Use JSON values. |
| `--priority-key` | No | **int** Priority key (1-5, lower numbers = higher priority). Tasks in a queue should be processed in close-to-priority-order. Default is 3 when not specified. |
| `--run-id`, `-r` | No | **string** Run ID. If unset, looks for an Update against the currently-running Workflow Execution. |
| `--run-timeout` | No | **duration** Fail a Workflow Run if it lasts longer than `DURATION`. |
| `--search-attribute` | No | **string[]** Search Attribute in `KEY=VALUE` format. Keys must be identifiers, and values must be JSON values. For example: `'YourKey={"your": "value"}'`. Can be passed multiple times. |
| `--start-delay` | No | **duration** Delay before starting the Workflow Execution. Can't be used with cron schedules. If the Workflow receives a signal or update prior to this time, the Workflow Execution starts immediately. |
| `--static-details` | No | **string** Static Workflow details for human consumption in UIs. Uses Temporal Markdown formatting, may be multiple lines. _(Experimental)_ |
| `--static-summary` | No | **string** Static Workflow summary for human consumption in UIs. Uses Temporal Markdown formatting, should be a single line. _(Experimental)_ |
| `--task-queue`, `-t` | Yes | **string** Workflow Task queue. |
| `--task-timeout` | No | **duration** Fail a Workflow Task if it lasts longer than `DURATION`. This is the Start-to-close timeout for a Workflow Task. |
| `--type` | Yes | **string** Workflow Type name. |
| `--update-first-execution-run-id` | No | **string** Parent Run ID. The update is sent to the last Workflow Execution in the chain started with this Run ID. |
| `--update-id` | No | **string** Update ID. If unset, defaults to a UUID. |
| `--update-input` | No | **string[]** Update input value. Use JSON content or set --update-input-meta to override. Can't be combined with --update-input-file. Can be passed multiple times to pass multiple arguments. |
| `--update-input-base64` | No | **bool** Assume update inputs are base64-encoded and attempt to decode them. |
| `--update-input-file` | No | **string[]** A path or paths for input file(s). Use JSON content or set --update-input-meta to override. Can't be combined with --update-input. Can be passed multiple times to pass multiple arguments. |
| `--update-input-meta` | No | **string[]** Input update payload metadata as a `KEY=VALUE` pair. When the KEY is "encoding", this overrides the default ("json/plain"). Can be passed multiple times. |
| `--update-name` | Yes | **string** Update name. |
| `--workflow-id`, `-w` | No | **string** Workflow ID. If not supplied, the Service generates a unique ID. |

## fix-history-json

Reserialize an Event History JSON file:

```
temporal workflow fix-history-json \
    --source /path/to/original.json \
    --target /path/to/reserialized.json
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--source`, `-s` | Yes | **string** Path to the original file. |
| `--target`, `-t` | No | **string** Path to the results file. When omitted, output is sent to stdout. |

## list

List Workflow Executions. The optional `--query` limits the output to
Workflows matching a Query:

```
temporal workflow list \
    --query YourQuery
```

Visit https://docs.temporal.io/visibility to read more about Search Attributes
and Query creation. See `temporal batch --help` for a quick reference.

View a list of archived Workflow Executions:

```
temporal workflow list \
    --archived
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--archived` | No | **bool** Limit output to archived Workflow Executions. _(Experimental)_ |
| `--limit` | No | **int** Maximum number of Workflow Executions to display. |
| `--page-size` | No | **int** Maximum number of Workflow Executions to fetch at a time from the server. |
| `--query`, `-q` | No | **string** Content for an SQL-like `QUERY` List Filter. |

## metadata

Issue a Query for and display user-set metadata like summary and
details for a specific Workflow Execution:

```
temporal workflow metadata \
    --workflow-id YourWorkflowId
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--headers` | No | **string[]** Temporal workflow headers in 'KEY=VALUE' format. Keys must be identifiers, and values must be JSON values. May be passed multiple times to set multiple Temporal headers. Note: These are workflow headers, not gRPC headers. |
| `--reject-condition` | No | **string-enum** Optional flag for rejecting Queries based on Workflow state. Accepted values: not_open, not_completed_cleanly. |
| `--run-id`, `-r` | No | **string** Run ID. |
| `--workflow-id`, `-w` | Yes | **string** Workflow ID. |

## pause

Pause a Workflow Execution.
Note: This is an experimental feature and may change in the future.

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--reason` | No | **string** Reason for pausing the Workflow Execution. Defaults to message with the current user's name. |
| `--run-id`, `-r` | No | **string** Run ID. |
| `--workflow-id`, `-w` | Yes | **string** Workflow ID. |

## query

Send a Query to a Workflow Execution by Workflow ID to retrieve its state.
This synchronous operation exposes the internal state of a running Workflow
Execution, which constantly changes. You can query both running and completed
Workflow Executions:

```
temporal workflow query \
    --workflow-id YourWorkflowId
    --type YourQueryType
    --input '{"YourInputKey": "YourInputValue"}'
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--headers` | No | **string[]** Temporal workflow headers in 'KEY=VALUE' format. Keys must be identifiers, and values must be JSON values. May be passed multiple times to set multiple Temporal headers. Note: These are workflow headers, not gRPC headers. |
| `--input`, `-i` | No | **string[]** Input value. Use JSON content or set --input-meta to override. Can't be combined with --input-file. Can be passed multiple times to pass multiple arguments. |
| `--input-base64` | No | **bool** Assume inputs are base64-encoded and attempt to decode them. |
| `--input-file` | No | **string[]** A path or paths for input file(s). Use JSON content or set --input-meta to override. Can't be combined with --input. Can be passed multiple times to pass multiple arguments. |
| `--input-meta` | No | **string[]** Input payload metadata as a `KEY=VALUE` pair. When the KEY is "encoding", this overrides the default ("json/plain"). Can be passed multiple times. Repeated metadata keys are applied to the corresponding inputs in the provided order. |
| `--name` | Yes | **string** Query Type/Name. |
| `--reject-condition` | No | **string-enum** Optional flag for rejecting Queries based on Workflow state. Accepted values: not_open, not_completed_cleanly. |
| `--run-id`, `-r` | No | **string** Run ID. |
| `--workflow-id`, `-w` | Yes | **string** Workflow ID. |

## reset

Reset a Workflow Execution so it can resume from a point in its Event History
without losing its progress up to that point:

```
temporal workflow reset \
    --workflow-id YourWorkflowId \
    --event-id YourLastEvent
```

Start from where the Workflow Execution last continued as new:

```
temporal workflow reset \
    --workflow-id YourWorkflowId \
    --type LastContinuedAsNew
```

For batch resets, limit your resets to FirstWorkflowTask, LastWorkflowTask, or
BuildId. Do not use Workflow IDs, run IDs, or event IDs with this command.

Visit https://docs.temporal.io/visibility to read more about Search
Attributes and Query creation.

### with-workflow-update-options

Run Workflow Update Options atomically after the Workflow is reset.
Workflows selected by the reset command are forwarded onto the subcommand.

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--versioning-override-behavior` | Yes | **string-enum** Override the versioning behavior of a Workflow. Accepted values: pinned, auto_upgrade. |
| `--versioning-override-build-id` | No | **string** When overriding to a `pinned` behavior, specifies the Build ID of the version to target. |
| `--versioning-override-deployment-name` | No | **string** When overriding to a `pinned` behavior, specifies the Deployment Name of the version to target. |

## result

Wait for and print the result of a Workflow Execution:

```
temporal workflow result \
    --workflow-id YourWorkflowId
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--run-id`, `-r` | No | **string** Run ID. |
| `--workflow-id`, `-w` | Yes | **string** Workflow ID. |

## show

Show a Workflow Execution's Event History.
When using JSON output (`--output json`), you may pass the results to an SDK
to perform a replay:

```
temporal workflow show \
    --workflow-id YourWorkflowId
    --output json
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--detailed` | No | **bool** Display events as detailed sections instead of table. Does not apply to JSON output. |
| `--follow`, `-f` | No | **bool** Follow the Workflow Execution progress in real time. Does not apply to JSON output. |
| `--reverse` | No | **bool** Fetch Event History newest-event-first. Cannot be combined with --follow. |
| `--run-id`, `-r` | No | **string** Run ID. |
| `--workflow-id`, `-w` | Yes | **string** Workflow ID. |

## signal

Send an asynchronous notification (Signal) to a running Workflow Execution by
its Workflow ID. The Signal is written to the History. When you include
`--input`, that data is available for the Workflow Execution to consume:

```
temporal workflow signal \
    --workflow-id YourWorkflowId \
    --name YourSignal \
    --input '{"YourInputKey": "YourInputValue"}'
```

Visit https://docs.temporal.io/visibility to read more about Search Attributes
and Query creation. See `temporal batch --help` for a quick reference.

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--headers` | No | **string[]** Temporal workflow headers in 'KEY=VALUE' format. Keys must be identifiers, and values must be JSON values. May be passed multiple times to set multiple Temporal headers. Note: These are workflow headers, not gRPC headers. |
| `--input`, `-i` | No | **string[]** Input value. Use JSON content or set --input-meta to override. Can't be combined with --input-file. Can be passed multiple times to pass multiple arguments. |
| `--input-base64` | No | **bool** Assume inputs are base64-encoded and attempt to decode them. |
| `--input-file` | No | **string[]** A path or paths for input file(s). Use JSON content or set --input-meta to override. Can't be combined with --input. Can be passed multiple times to pass multiple arguments. |
| `--input-meta` | No | **string[]** Input payload metadata as a `KEY=VALUE` pair. When the KEY is "encoding", this overrides the default ("json/plain"). Can be passed multiple times. Repeated metadata keys are applied to the corresponding inputs in the provided order. |
| `--name` | Yes | **string** Signal name. |
| `--query`, `-q` | No | **string** Content for an SQL-like `QUERY` List Filter. You must set either --workflow-id or --query. |
| `--reason` | No | **string** Reason for batch operation. Only use with --query. Defaults to user name. |
| `--rps` | No | **float** Limit batch's requests per second. Only allowed if query is present. |
| `--run-id`, `-r` | No | **string** Run ID. Only use with --workflow-id. Cannot use with --query. |
| `--workflow-id`, `-w` | No | **string** Workflow ID. You must set either --workflow-id or --query. |
| `--yes`, `-y` | No | **bool** Don't prompt to confirm signaling. Only allowed when --query is present. |

## signal-with-start

Send an asynchronous notification (Signal) to a Workflow Execution.
If the Workflow Execution is not running or is not found, it starts the
workflow then sends the signal.

```
temporal workflow signal-with-start \
  --signal-name YourSignal \
  --signal-input '{"some-key": "some-value"}' \
  --workflow-id YourWorkflowId \
  --type YourWorkflowType \
  --task-queue YourTaskQueue \
  --input '{"some-key": "some-value"}'
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--cron` | No | **string** Cron schedule for the Workflow. |
| `--execution-timeout` | No | **duration** Fail a WorkflowExecution if it lasts longer than `DURATION`. This time-out includes retries and ContinueAsNew tasks. |
| `--fail-existing` | No | **bool** Fail if the Workflow already exists. |
| `--fairness-key` | No | **string** Fairness key (max 64 bytes) for proportional task dispatch. Tasks with same key share capacity based on their weight. |
| `--fairness-weight` | No | **float** Weight [0.001-1000] for this fairness key. Keys are dispatched proportionally to their weights. |
| `--headers` | No | **string[]** Temporal workflow headers in 'KEY=VALUE' format. Keys must be identifiers, and values must be JSON values. May be passed multiple times to set multiple Temporal headers. Note: These are workflow headers, not gRPC headers. |
| `--id-conflict-policy` | No | **string-enum** Determines how to resolve a conflict when spawning a new Workflow Execution with a particular Workflow Id used by an existing Open Workflow Execution. Accepted values: Fail, UseExisting, TerminateExisting. |
| `--id-reuse-policy` | No | **string-enum** Re-use policy for the Workflow ID in new Workflow Executions. Accepted values: AllowDuplicate, AllowDuplicateFailedOnly, RejectDuplicate, TerminateIfRunning. |
| `--input`, `-i` | No | **string[]** Input value. Use JSON content or set --input-meta to override. Can't be combined with --input-file. Can be passed multiple times to pass multiple arguments. |
| `--input-base64` | No | **bool** Assume inputs are base64-encoded and attempt to decode them. |
| `--input-file` | No | **string[]** A path or paths for input file(s). Use JSON content or set --input-meta to override. Can't be combined with --input. Can be passed multiple times to pass multiple arguments. |
| `--input-meta` | No | **string[]** Input payload metadata as a `KEY=VALUE` pair. When the KEY is "encoding", this overrides the default ("json/plain"). Can be passed multiple times. Repeated metadata keys are applied to the corresponding inputs in the provided order. |
| `--memo` | No | **string[]** Memo using 'KEY="VALUE"' pairs. Use JSON values. |
| `--priority-key` | No | **int** Priority key (1-5, lower numbers = higher priority). Tasks in a queue should be processed in close-to-priority-order. Default is 3 when not specified. |
| `--run-timeout` | No | **duration** Fail a Workflow Run if it lasts longer than `DURATION`. |
| `--search-attribute` | No | **string[]** Search Attribute in `KEY=VALUE` format. Keys must be identifiers, and values must be JSON values. For example: `'YourKey={"your": "value"}'`. Can be passed multiple times. |
| `--signal-input` | No | **string[]** Signal input value. Use JSON content or set --signal-input-meta to override. Can't be combined with --signal-input-file. Can be passed multiple times to pass multiple arguments. |
| `--signal-input-base64` | No | **bool** Assume signal inputs are base64-encoded and attempt to decode them. |
| `--signal-input-file` | No | **string[]** A path or paths for input file(s). Use JSON content or set --signal-input-meta to override. Can't be combined with --signal-input. Can be passed multiple times to pass multiple arguments. |
| `--signal-input-meta` | No | **string[]** Input signal payload metadata as a `KEY=VALUE` pair. When the KEY is "encoding", this overrides the default ("json/plain"). Can be passed multiple times. |
| `--signal-name` | Yes | **string** Signal name. |
| `--start-delay` | No | **duration** Delay before starting the Workflow Execution. Can't be used with cron schedules. If the Workflow receives a signal or update prior to this time, the Workflow Execution starts immediately. |
| `--static-details` | No | **string** Static Workflow details for human consumption in UIs. Uses Temporal Markdown formatting, may be multiple lines. _(Experimental)_ |
| `--static-summary` | No | **string** Static Workflow summary for human consumption in UIs. Uses Temporal Markdown formatting, should be a single line. _(Experimental)_ |
| `--task-queue`, `-t` | Yes | **string** Workflow Task queue. |
| `--task-timeout` | No | **duration** Fail a Workflow Task if it lasts longer than `DURATION`. This is the Start-to-close timeout for a Workflow Task. |
| `--type` | Yes | **string** Workflow Type name. |
| `--workflow-id`, `-w` | No | **string** Workflow ID. If not supplied, the Service generates a unique ID. |

## stack

Perform a Query on a Workflow Execution using a `__stack_trace`-type Query.
Display a stack trace of the threads and routines currently in use by the
Workflow for troubleshooting:

```
temporal workflow stack \
    --workflow-id YourWorkflowId
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--reject-condition` | No | **string-enum** Optional flag to reject Queries based on Workflow state. Accepted values: not_open, not_completed_cleanly. |
| `--run-id`, `-r` | No | **string** Run ID. |
| `--workflow-id`, `-w` | Yes | **string** Workflow ID. |

## start

Start a new Workflow Execution. Returns the Workflow- and Run-IDs:

```
temporal workflow start \
    --workflow-id YourWorkflowId \
    --type YourWorkflow \
    --task-queue YourTaskQueue \
    --input '{"some-key": "some-value"}'
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.
