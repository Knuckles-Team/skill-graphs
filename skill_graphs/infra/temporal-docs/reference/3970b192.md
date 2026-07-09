# Using mTLS certificates
temporal workflow list \
  --address <namespace>.<account>.tmprl.cloud:7233 \
  --namespace <namespace>.<account> \
  --tls-cert-path /path/to/client.pem \
  --tls-key-path /path/to/client.key
```

### Log out

To log out, run the `temporal cloud logout` command.

```bash
temporal cloud logout --profile prod
```

This will remove the OAuth token from the specified configuration profile. If you provided API keys or mTLS
certificates, they will remain in the profile.

## Cloud administration

The Temporal Cloud extension adds `temporal cloud` commands for managing your Temporal Cloud control plane resources in
your Temporal Cloud account, including Namespaces, Users, Service Accounts, API keys, and others. Any of the
authentication methods above grants access to these commands.

The extension enables you to do the following through the CLI:

- Create, configure, and delete Namespaces.
- Create and manage API keys for programmatic access.
- Invite users, assign roles, and manage user groups.
- Create and configure Nexus endpoints.
- View account information and manage connectivity rules.

For installation instructions, see
[Install the Temporal Cloud extension](/cli/setup-cli#install-the-temporal-cloud-extension). For the full list of
commands, see the [`cloud` command reference](/cli/command-reference/cloud).

## Next steps

- [CLI basics](/cli/common-operations) for common CLI commands.
- [Environment configuration](/develop/environment-configuration) for managing connection profiles across environments.
- [Cloud command reference](/cli/command-reference/cloud) for all `temporal cloud` commands.

---

## Temporal CLI activity command reference

{/* NOTE: This is an auto-generated file. Any edit to this file will be overwritten.
This file is generated from https://github.com/temporalio/cli/blob/main/internal/commandsgen/commands.yml via internal/cmd/gen-docs */}

This page provides a reference for the `temporal` CLI `activity` command. The flags applicable to each subcommand are presented in a table within the heading for the subcommand. Refer to [Global Flags](#global-flags) for flags that you can use with every subcommand.

## cancel

Request cancellation of a Standalone Activity.

```
temporal activity cancel \
    --activity-id YourActivityId
```

Requesting cancellation transitions the Activity's run state
to CancelRequested. If the Activity is heartbeating, a
cancellation error will be raised when the next heartbeat
response is received; if the Activity allows this error to
propagate, the Activity transitions to canceled status.

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--activity-id`, `-a` | Yes | **string** Activity ID. |
| `--reason` | No | **string** Reason for cancellation. |
| `--run-id`, `-r` | No | **string** Activity Run ID. If not set, targets the latest run. |

## complete

Complete an Activity, marking it as successfully finished. Specify the
Activity ID and include a JSON result for the returned value:

```
temporal activity complete \
    --activity-id YourActivityId \
    --workflow-id YourWorkflowId \
    --result '{"YourResultKey": "YourResultVal"}'
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--activity-id`, `-a` | Yes | **string** Activity ID. This may be the ID of an Activity invoked by a Workflow, or of a Standalone Activity. |
| `--result` | Yes | **string** Result `JSON` to return. |
| `--run-id`, `-r` | No | **string** Run ID. For workflow Activities (when --workflow-id is provided), this is the Workflow Run ID. For Standalone Activities, this is the Activity Run ID. |
| `--workflow-id`, `-w` | No | **string** Workflow ID. Required for workflow Activities. Omit for Standalone Activities. |

## count

Return a count of Standalone Activities. Use `--query` to filter
the activities to be counted.

```
temporal activity count \
    --query 'ActivityType="YourActivity"'
```

Visit https://docs.temporal.io/visibility to read more about
Search Attributes and queries.

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--query`, `-q` | No | **string** Query to filter Activity Executions to count. |

## describe

Display information about a Standalone Activity.

```
temporal activity describe \
    --activity-id YourActivityId
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--activity-id`, `-a` | Yes | **string** Activity ID. |
| `--raw` | No | **bool** Print properties without changing their format. |
| `--run-id`, `-r` | No | **string** Activity Run ID. If not set, targets the latest run. |

## execute

Start a new Standalone Activity and block until it completes.
The result is output to stdout.

```
temporal activity execute \
    --activity-id YourActivityId \
    --type YourActivity \
    --task-queue YourTaskQueue \
    --start-to-close-timeout 30s \
    --input '{"some-key": "some-value"}'
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--activity-id`, `-a` | Yes | **string** Activity ID. |
| `--fairness-key` | No | **string** Fairness key (max 64 bytes) for proportional task dispatch. |
| `--fairness-weight` | No | **float** Weight [0.001-1000] for this fairness key. |
| `--headers` | No | **string[]** Temporal activity headers in 'KEY=VALUE' format. Keys must be identifiers, and values must be JSON values. May be passed multiple times. |
| `--heartbeat-timeout` | No | **duration** Maximum time between successful Worker heartbeats. On expiry the current activity attempt fails. |
| `--id-conflict-policy` | No | **string-enum** Policy for handling activity start when an Activity with the same ID is currently running. Accepted values: Fail, UseExisting. |
| `--id-reuse-policy` | No | **string-enum** Policy for handling activity start when an Activity with the same ID exists and has completed. Accepted values: AllowDuplicate, AllowDuplicateFailedOnly, RejectDuplicate. |
| `--input`, `-i` | No | **string[]** Input value. Use JSON content or set --input-meta to override. Can't be combined with --input-file. Can be passed multiple times to pass multiple arguments. |
| `--input-base64` | No | **bool** Assume inputs are base64-encoded and attempt to decode them. |
| `--input-file` | No | **string[]** A path or paths for input file(s). Use JSON content or set --input-meta to override. Can't be combined with --input. Can be passed multiple times to pass multiple arguments. |
| `--input-meta` | No | **string[]** Input payload metadata as a `KEY=VALUE` pair. When the KEY is "encoding", this overrides the default ("json/plain"). Can be passed multiple times. Repeated metadata keys are applied to the corresponding inputs in the provided order. |
| `--priority-key` | No | **int** Priority key (1-5, lower = higher priority). Default is 3 when not specified. |
| `--retry-backoff-coefficient` | No | **float** Coefficient for calculating the next retry interval. Must be 1 or larger. |
| `--retry-initial-interval` | No | **duration** Interval of the first retry. If "retry-backoff-coefficient" is 1.0, it is used for all retries. |
| `--retry-maximum-attempts` | No | **int** Maximum number of attempts. Setting to 1 disables retries. Setting to 0 means unlimited attempts. |
| `--retry-maximum-interval` | No | **duration** Maximum interval between retries. |
| `--schedule-to-close-timeout` | No | **duration** Maximum time for the Activity Execution, including all retries. Either this or "start-to-close-timeout" is required. |
| `--schedule-to-start-timeout` | No | **duration** Maximum time an Activity task can stay in a task queue before a Worker picks it up. On expiry it results in a non-retryable failure and no further attempts are scheduled. |
| `--search-attribute` | No | **string[]** Search Attribute in `KEY=VALUE` format. Keys must be identifiers, and values must be JSON values. Can be passed multiple times. See https://docs.temporal.io/visibility. |
| `--start-to-close-timeout` | No | **duration** Maximum time for a single Activity attempt. On expiry a new attempt may be scheduled if permitted by the retry policy and schedule-to-close timeout. Either this or "schedule-to-close-timeout" is required. |
| `--static-details` | No | **string** Static Activity details for human consumption in UIs. Uses standard Markdown formatting excluding images, HTML, and script tags. _(Experimental)_ |
| `--static-summary` | No | **string** Static Activity summary for human consumption in UIs. Uses standard Markdown formatting excluding images, HTML, and script tags. _(Experimental)_ |
| `--task-queue`, `-t` | Yes | **string** Activity task queue. |
| `--type` | Yes | **string** Activity Type name. |

## fail

Fail an Activity, marking it as having encountered an error:

```
temporal activity fail \
    --activity-id YourActivityId \
    --workflow-id YourWorkflowId
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--activity-id`, `-a` | Yes | **string** Activity ID. This may be the ID of an Activity invoked by a Workflow, or of a Standalone Activity. |
| `--detail` | No | **string** Failure detail (JSON). Attached as the failure details payload. |
| `--reason` | No | **string** Failure reason. Attached as the failure message. |
| `--run-id`, `-r` | No | **string** Run ID. For workflow Activities (when --workflow-id is provided), this is the Workflow Run ID. For Standalone Activities, this is the Activity Run ID. |
| `--workflow-id`, `-w` | No | **string** Workflow ID. Required for workflow Activities. Omit for Standalone Activities. |

## list

List Standalone Activities. Use `--query` to filter results.

```
temporal activity list \
    --query 'ActivityType="YourActivity"'
```

Visit https://docs.temporal.io/visibility to read more about
Search Attributes and queries.

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--limit` | No | **int** Maximum number of Activity Executions to display. |
| `--page-size` | No | **int** Maximum number of Activity Executions to fetch at a time from the server. |
| `--query`, `-q` | No | **string** Query to filter the Activity Executions to list. |

## pause

Pause an Activity. Not supported for Standalone Activities.

If the Activity is not currently running (e.g. because it previously
failed), it will not be run again until it is unpaused.

However, if the Activity is currently running, it will run until the next
time it fails, completes, or times out, at which point the pause will kick in.

If the Activity is on its last retry attempt and fails, the failure will
be returned to the caller, just as if the Activity had not been paused.

Specify the Activity and Workflow IDs:

```
temporal activity pause \
    --activity-id YourActivityId \
    --workflow-id YourWorkflowId
```

To later unpause the activity, see [unpause](#unpause). You may also want to
[reset](#reset) the activity to unpause it while also starting it from the beginning.

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--activity-id`, `-a` | No | **string** The Activity ID to pause. Required. |
| `--identity` | No | **string** The identity of the user or client submitting this request. |
| `--reason` | No | **string** Reason for pausing the Activity. |
| `--run-id`, `-r` | No | **string** Run ID. |
| `--workflow-id`, `-w` | Yes | **string** Workflow ID. |

## reset

Reset an activity. Not supported for Standalone Activities.
This restarts the activity as if it were first being
scheduled. That is, it will reset both the number of attempts and the
activity timeout, as well as, optionally, the
[heartbeat details](#reset-heartbeats).

If the activity may be executing (i.e. it has not yet timed out), the
reset will take effect the next time it fails, heartbeats, or times out.
If is waiting for a retry (i.e. has failed or timed out), the reset
will apply immediately.

If the activity is already paused, it will be unpaused by default.
You can specify `keep_paused` to prevent this.

If the activity is paused and the `keep_paused` flag is not provided,
it will be unpaused. If the activity is paused and `keep_paused` flag
is provided - it will stay paused.

Either `--activity-id` (with `--workflow-id`) or `--query` must be specified.

### Resetting activities that heartbeat {/* #reset-heartbeats */}

Activities that heartbeat will receive a [Canceled failure](/references/failures#cancelled-failure)
the next time they heartbeat after a reset.

If, in your Activity, you need to do any cleanup when an Activity is
reset, handle this error and then re-throw it when you've cleaned up.

If the `reset_heartbeats` flag is set, the heartbeat details will also be cleared.

Specify the Activity and Workflow IDs:

```
temporal activity reset \
    --activity-id YourActivityId \
    --workflow-id YourWorkflowId
    --keep-paused
    --reset-heartbeats
```

Activities can be reset in bulk with a visibility query list filter:

```
temporal activity reset \
    --query 'WorkflowType="YourWorkflow"'
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--activity-id`, `-a` | No | **string** The Activity ID to reset. Mutually exclusive with `--query`. Requires `--workflow-id` to be specified. |
| `--headers` | No | **string[]** Temporal workflow headers in 'KEY=VALUE' format. Keys must be identifiers, and values must be JSON values. May be passed multiple times to set multiple Temporal headers. Note: These are workflow headers, not gRPC headers. |
| `--jitter` | No | **duration** The activity will reset at random a time within the specified duration. Can only be used with --query. |
| `--keep-paused` | No | **bool** If the activity was paused, it will stay paused. |
| `--query`, `-q` | No | **string** Content for an SQL-like `QUERY` List Filter. You must set either --workflow-id or --query. Note: Using --query for batch activity operations is an experimental feature and may change in the future. |
| `--reason` | No | **string** Reason for batch operation. Only use with --query. Defaults to user name. |
| `--reset-attempts` | No | **bool** Reset the activity attempts. |
| `--reset-heartbeats` | No | **bool** Reset the Activity's heartbeats. |
| `--restore-original-options` | No | **bool** Restore the original options of the activity. |
| `--rps` | No | **float** Limit batch's requests per second. Only allowed if query is present. |
| `--run-id`, `-r` | No | **string** Run ID. Only use with --workflow-id. Cannot use with --query. |
| `--workflow-id`, `-w` | No | **string** Workflow ID. You must set either --workflow-id or --query. |
| `--yes`, `-y` | No | **bool** Don't prompt to confirm signaling. Only allowed when --query is present. |

## result

Wait for a Standalone Activity to complete and output the
result.

```
temporal activity result \
    --activity-id YourActivityId
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--activity-id`, `-a` | Yes | **string** Activity ID. |
| `--run-id`, `-r` | No | **string** Activity Run ID. If not set, targets the latest run. |

## start

Start a new Standalone Activity. Outputs the Activity ID and
Run ID.

```
temporal activity start \
    --activity-id YourActivityId \
    --type YourActivity \
    --task-queue YourTaskQueue \
    --start-to-close-timeout 5m \
    --input '{"some-key": "some-value"}'
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--activity-id`, `-a` | Yes | **string** Activity ID. |
| `--fairness-key` | No | **string** Fairness key (max 64 bytes) for proportional task dispatch. |
| `--fairness-weight` | No | **float** Weight [0.001-1000] for this fairness key. |
| `--headers` | No | **string[]** Temporal activity headers in 'KEY=VALUE' format. Keys must be identifiers, and values must be JSON values. May be passed multiple times. |
| `--heartbeat-timeout` | No | **duration** Maximum time between successful Worker heartbeats. On expiry the current activity attempt fails. |
| `--id-conflict-policy` | No | **string-enum** Policy for handling activity start when an Activity with the same ID is currently running. Accepted values: Fail, UseExisting. |
| `--id-reuse-policy` | No | **string-enum** Policy for handling activity start when an Activity with the same ID exists and has completed. Accepted values: AllowDuplicate, AllowDuplicateFailedOnly, RejectDuplicate. |
| `--input`, `-i` | No | **string[]** Input value. Use JSON content or set --input-meta to override. Can't be combined with --input-file. Can be passed multiple times to pass multiple arguments. |
| `--input-base64` | No | **bool** Assume inputs are base64-encoded and attempt to decode them. |
| `--input-file` | No | **string[]** A path or paths for input file(s). Use JSON content or set --input-meta to override. Can't be combined with --input. Can be passed multiple times to pass multiple arguments. |
| `--input-meta` | No | **string[]** Input payload metadata as a `KEY=VALUE` pair. When the KEY is "encoding", this overrides the default ("json/plain"). Can be passed multiple times. Repeated metadata keys are applied to the corresponding inputs in the provided order. |
| `--priority-key` | No | **int** Priority key (1-5, lower = higher priority). Default is 3 when not specified. |
| `--retry-backoff-coefficient` | No | **float** Coefficient for calculating the next retry interval. Must be 1 or larger. |
| `--retry-initial-interval` | No | **duration** Interval of the first retry. If "retry-backoff-coefficient" is 1.0, it is used for all retries. |
| `--retry-maximum-attempts` | No | **int** Maximum number of attempts. Setting to 1 disables retries. Setting to 0 means unlimited attempts. |
| `--retry-maximum-interval` | No | **duration** Maximum interval between retries. |
| `--schedule-to-close-timeout` | No | **duration** Maximum time for the Activity Execution, including all retries. Either this or "start-to-close-timeout" is required. |
| `--schedule-to-start-timeout` | No | **duration** Maximum time an Activity task can stay in a task queue before a Worker picks it up. On expiry it results in a non-retryable failure and no further attempts are scheduled. |
| `--search-attribute` | No | **string[]** Search Attribute in `KEY=VALUE` format. Keys must be identifiers, and values must be JSON values. Can be passed multiple times. See https://docs.temporal.io/visibility. |
| `--start-to-close-timeout` | No | **duration** Maximum time for a single Activity attempt. On expiry a new attempt may be scheduled if permitted by the retry policy and schedule-to-close timeout. Either this or "schedule-to-close-timeout" is required. |
| `--static-details` | No | **string** Static Activity details for human consumption in UIs. Uses standard Markdown formatting excluding images, HTML, and script tags. _(Experimental)_ |
| `--static-summary` | No | **string** Static Activity summary for human consumption in UIs. Uses standard Markdown formatting excluding images, HTML, and script tags. _(Experimental)_ |
| `--task-queue`, `-t` | Yes | **string** Activity task queue. |
| `--type` | Yes | **string** Activity Type name. |

## terminate

Terminate a Standalone Activity.

```
temporal activity terminate \
    --activity-id YourActivityId \
    --reason YourReason
```

Activity code cannot see or respond to terminations.

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--activity-id`, `-a` | Yes | **string** Activity ID. |
| `--reason` | No | **string** Reason for termination. Defaults to a message with the current user's name. |
| `--run-id`, `-r` | No | **string** Activity Run ID. If not set, targets the latest run. |

## unpause

Re-schedule a previously-paused Activity for execution.
Not supported for Standalone Activities.

If the Activity is not running and is past its retry timeout, it will be
scheduled immediately. Otherwise, it will be scheduled after its retry
timeout expires.

Use `--reset-attempts` to reset the number of previous run attempts to
zero. For example, if an Activity is near the maximum number of attempts
N specified in its retry policy, `--reset-attempts` will allow the
Activity to be retried another N times after unpausing.

Use `--reset-heartbeat` to reset the Activity's heartbeats.

Either `--activity-id` (with `--workflow-id`) or `--query` must be specified.

Specify the Activity and Workflow IDs:

```
temporal activity unpause \
    --activity-id YourActivityId \
    --workflow-id YourWorkflowId
    --reset-attempts
    --reset-heartbeats
```

Activities can be unpaused in bulk via a visibility Query list filter:

```
temporal activity unpause \
    --query 'TemporalPauseInfo IS NOT NULL'
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--activity-id`, `-a` | No | **string** The Activity ID to unpause. Mutually exclusive with `--query`. Requires `--workflow-id` to be specified. |
| `--headers` | No | **string[]** Temporal workflow headers in 'KEY=VALUE' format. Keys must be identifiers, and values must be JSON values. May be passed multiple times to set multiple Temporal headers. Note: These are workflow headers, not gRPC headers. |
| `--jitter` | No | **duration** The activity will start at random a time within the specified duration. Can only be used with --query. |
| `--query`, `-q` | No | **string** Content for an SQL-like `QUERY` List Filter. You must set either --workflow-id or --query. Note: Using --query for batch activity operations is an experimental feature and may change in the future. |
| `--reason` | No | **string** Reason for batch operation. Only use with --query. Defaults to user name. |
| `--reset-attempts` | No | **bool** Reset the activity attempts. |
| `--reset-heartbeats` | No | **bool** Reset the Activity's heartbeats. |
| `--rps` | No | **float** Limit batch's requests per second. Only allowed if query is present. |
| `--run-id`, `-r` | No | **string** Run ID. Only use with --workflow-id. Cannot use with --query. |
| `--workflow-id`, `-w` | No | **string** Workflow ID. You must set either --workflow-id or --query. |
| `--yes`, `-y` | No | **bool** Don't prompt to confirm signaling. Only allowed when --query is present. |

## update-options

Update the options of a running Activity that were passed into it from
a Workflow. Updates are incremental, only changing the specified options.
Not supported for Standalone Activities.

For example:

```
temporal activity update-options \
    --activity-id YourActivityId \
    --workflow-id YourWorkflowId \
    --task-queue NewTaskQueueName \
    --schedule-to-close-timeout DURATION \
    --schedule-to-start-timeout DURATION \
    --start-to-close-timeout DURATION \
    --heartbeat-timeout DURATION \
    --retry-initial-interval DURATION \
    --retry-maximum-interval DURATION \
    --retry-backoff-coefficient NewBackoffCoefficient \
    --retry-maximum-attempts NewMaximumAttempts
```

You may follow this command with `temporal activity reset`, and the new values will apply after the reset.

Either `--activity-id` or `--query` must be specified.

Activity options can be updated in bulk with a visibility query list filter:

```
temporal activity update-options \
    --query 'WorkflowType="YourWorkflow"' \
    --task-queue NewTaskQueueName
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--activity-id`, `-a` | No | **string** The Activity ID to update options. Mutually exclusive with `--query`. Requires `--workflow-id` to be specified. |
