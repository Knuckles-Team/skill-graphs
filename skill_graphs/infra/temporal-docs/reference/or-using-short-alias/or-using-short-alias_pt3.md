```

Signals can also be used to change variable values.

```bash
tctl workflow signal --workflow_id "HelloSignal" --name "updateGreeting" --input \"Hi\"
```

The output would change from the first Signal received.

```text
13:57:44.258 [workflow-method] INFO  c.t.s.javaquickstart.GettingStarted - 1: Hello World!
13:58:22.352 [workflow-method] INFO  c.t.s.javaquickstart.GettingStarted - 2: Hi World!
```

When a Signal is sent, an await condition is made to block any Signals that contain the same input value.
However, changing the greeting in our example unblocks it:

```bash
tctl workflow signal --workflow_id "HelloSignal" --name "updateGreeting" --input \"Welcome\"
```

Worker output:

```text
13:57:44.258 [workflow-method] INFO  c.t.s.javaquickstart.GettingStarted - 1: Hello World!
13:58:22.352 [workflow-method] INFO  c.t.s.javaquickstart.GettingStarted - 2: Hi World!
13:59:29.097 [workflow-method] INFO  c.t.s.javaquickstart.GettingStarted - 3: Welcome World!
```

Sending Signals does not require a running Worker.

```bash
tctl workflow signal --workflow_id "HelloSignal" --name "updateGreeting" --input \"Welcome\"
```

CLI output:

```text
Signal workflow succeeded.
```

The Signal request is queued inside the Temporal Server until the Worker is restarted.
If the given Signal contains the same input as before, the queued Signal will be ignored.

Complete the Workflow by sending a Signal with a "Bye" greeting:

```bash
tctl workflow signal --workflow_id "HelloSignal" --name "updateGreeting" --input \"Bye\"
```

Check that the Workflow Execution has been completed.

```bash
tctl workflow showid HelloSignal
```

Signals are written as follows:

```bash
tctl workflow signal --workflow_id <id> <modifiers>
```

or

```bash
tctl workflow signal --query <query> <modifiers>
```

The following modifiers control the behavior of the command.
Make sure to include required modifiers in all command executions.

### --workflow_id

Specify a [Workflow Id](/workflow-execution/workflowid-runid#workflow-id). **This modifier is required.**

Alias: `-w`

**Example**

```bash
tctl workflow signal --workflow_id <id>
```

### --run_id

Specify a [Run Id](/workflow-execution/workflowid-runid#run-id).

Alias: `-r`

**Example**

```bash
tctl workflow signal --run_id <id>
```

### --name

Specify the name of a [Signal](/sending-messages#sending-signals).

**Example**

```bash
tctl workflow signal --query <query> --name <name>
```

### --input

Pass input for the [Signal](/sending-messages#sending-signals).
Input must be in JSON format.

Alias: `-i`

**Example**

```bash
tctl workflow signal --query <query> --input <json>
```

### --input_file

Pass input for the [Signal](/sending-messages#sending-signals) from a JSON file.

**Example**

```bash
tctl workflow signal --query <query> --input_file <filename>
```

## stack

The `tctl workflow stack` command queries [Workflow Execution](/workflow-execution) with `__stack_trace` as the query type.

This command can be used to locate errors and blocks in a [Workflow Definition](/workflow-definition).

`tctl workflow stack <modifiers>`

The following modifiers control the behavior of the command.

### --workflow_id

**This is a required modifier.**

Specify a [Workflow Id](/workflow-execution/workflowid-runid#workflow-id).

Alias: `-w`

**Example**

```bash
tctl workflow stack --workflow_id <id>
```

### --run_id

Specify a [Run Id](/workflow-execution/workflowid-runid#run-id).

Alias: `-r`

**Example**

```bash
tctl workflow stack --run_id <id>
```

### --input

Pass input for the query.
Input must be in JSON format.
For multiple JSON objects, concatenate them and use spaces as separators.

Alias: `-i`

**Example**

```bash
tctl workflow stack --input <json>
```

### --input_file

Pass input for the query from a JSON file.
For multiple JSON objects, concatenate them and use spaces or newline characters as separators.
Input from the command line overwrites input from the file.

**Example**

```bash
tctl workflow stack --input_file <filename>
```

### --query_reject_condition

Reject queries based on Workflow state.
Valid values are `not_open` and `not_completed_cleanly`.

**Example**

```bash
tctl workflow stack --query_reject_condition <value>
```

## start

The `tctl workflow start` command starts a new [Workflow Execution](/workflow-execution).
Unlike `run`, this command returns the Workflow Id and Run Id immediately after starting the Workflow.

`tctl workflow start <modifiers>`

The following modifiers control the behavior of the command.
Always include required modifiers when executing this command.

### --taskqueue

Specify a [Task Queue](/task-queue).

Alias: `--t`

**Example**

```bash
tctl workflow start --taskqueue <name>
```

### --workflow_id

**This is a required modifier.**

Specify a [Workflow Id](/workflow-execution/workflowid-runid#workflow-id).

Alias: `-w`

**Example**

```bash
tctl workflow start --workflow_id <id>
```

If a Workflow is started without providing an Id, the Client generates one in the form of a UUID.
Temporal recommends using a business id rather than the client-generated UUID.

**Example**

```bash
tctl workflow start  --workflow_id "HelloTemporal1" --taskqueue HelloWorldTaskQueue --workflow_type HelloWorld --execution_timeout 3600 --input \"Temporal\"
```

### --workflow_type

Specify the name of a [Workflow Type](/workflow-definition#workflow-type).

**Example**

```bash
tctl workflow start --workflow_type <name>
```

### --execution_timeout

Specify the [Start-To-Close Timeout](/encyclopedia/detecting-activity-failures#start-to-close-timeout) of the [Workflow Execution](/workflow-execution) in seconds.
The default value is 0.

**Example**

```bash
tctl workflow start --execution_timeout <seconds>
```

### --workflow_task_timeout

Specify the [Start-To-Close Timeout](/encyclopedia/detecting-activity-failures#start-to-close-timeout) of the [Workflow Task](/tasks#workflow-task) in seconds.
The default value is 10.

**Example**

```bash
tctl workflow start --workflow_task_timeout <seconds>
```

### --cron

Specify a [Cron Schedule](/cron-job#cron-schedules).

**Example**

```bash
tctl workflow start --cron <string>
```

### --workflowidreusepolicy

Specify a [Workflow Id Reuse Policy](/workflow-execution/workflowid-runid#workflow-id-reuse-policy).
Configure if the same [Workflow Id](/workflow-execution/workflowid-runid#workflow-id)is allowed for use in new [Workflow Execution](/workflow-execution).

There are three allowed values:

- [AllowDuplicateFailedOnly](/workflow-execution/workflowid-runid#workflow-id-reuse-policy)
- [AllowDuplicate](/workflow-execution/workflowid-runid#workflow-id-reuse-policy)
- [RejectDuplicate](/workflow-execution/workflowid-runid#workflow-id-reuse-policy)

**Examples**

```bash
tctl workflow start --workflowidreusepolicy AllowDuplicate
tctl workflow start --workflowidreusepolicy AllowDuplicateFailedOnly
tctl workflow start --workflowidreusepolicy RejectDuplicate
```

:::note

Multiple Workflows with the same Id cannot be run at the same time

:::

### --input

Pass input for the Workflow.
Input must be in JSON format.
For multiple JSON objects, pass each in a separate `--input` option.
Use `null` for null values.

Alias: `-i`

**Example**

```bash
tctl workflow start --input <json>
```

### --input_file

Pass input for the Workflow from a JSON file.
For multiple JSON objects, concatenate them and use spaces or newline characters as separators.
Input from the command line overwrites input from the file.

**Example**

```bash
tctl workflow start --input_file <filename>
```

### --memo_key

Pass a key for a memo.
For multiple keys, concatenate them and use spaces as separators.

**Example**

```bash
tctl workflow start --memo_key <key>
```

### --memo

Pass information for a [memo](/workflow-execution#memo) from a JSON file.

Memos are immutable key/value pairs that can be attached to a workflow run when starting the workflow.
Memos are visible when listing workflows.

For multiple memos, concatenate them and use spaces as separators.
The order must match the order of keys in `--memo_key`.

**Example**

```bash
tctl workflow start \
  -tq your-task-queue \
  -wt your-workflow \
  -et 60 \
  -i '"temporal"' \
  -memo_key '<key values>' \
  -memo '<value>'
```

### --memo_file

Pass information for a memo from a JSON file.
For multiple JSON objects, concatenate them and use spaces or newline characters as separators.
The order must match the order of keys in `--memo_key`.

**Example**

```bash
tctl workflow start --memo_file <filename>
```

### --search_attr_key

Specify a [Search Attribute](/search-attribute) name.
For multiple names, concatenate them and use pipes (`|`) as separators.

To list valid Search Attributes, use the `tctl cluster get-search-attributes` command.

**Example**

```bash
tctl workflow start --search_attr_key <key>
```

### --search_attr_value

Specify a [Search Attribute](/search-attribute) value.
For multiple values, concatenate them and use pipes (`|`) as separators.
If a value is an array, use JSON format, such as `["a","b"]`, `[1,2]`, `["true","false"]`, or `["2022-06-07T17:16:34-08:00","2022-06-07T18:16:34-08:00"]`.

To list valid Search Attributes and value types, use the `tctl cluster get-search-attributes` command.

**Example**

```bash
tctl workflow start --search_attr_value <value>
```

## terminate

The `tctl workflow terminate` command terminates a [Workflow Execution](/workflow-execution).

Terminating a running Workflow Execution records a `WorkflowExecutionTerminated` event as the closing event in the History.
No more [Workflow Task](/tasks#workflow-task) will be scheduled.

See also [`tctl workflow cancel`](#cancel).

`tctl workflow terminate --query <modifiers>`

The following modifiers control the behavior of the command.

### --workflow_id

_Required modifier_

Specify a [Workflow Id](/workflow-execution/workflowid-runid#workflow-id).

Alias: `-w`

**Example**

```bash
tctl workflow terminate --workflow_id <id>
```

### --run_id

Specify a [Run Id](/workflow-execution/workflowid-runid#run-id).

If `run_id` is not specified, `tctl` terminates the last Workflow Execution for the specified `workflow_id`.

Alias: `-r`

**Example**

```bash
tctl workflow terminate --run_id <id>
```

### --reason

Specify a reason for terminating the [Workflow Execution](/workflow-execution).

**Example**

```bash
tctl workflow terminate --workflow_id --reason <string>
```

---

## Troubleshoot payload and gRPC message size limit errors

Temporal enforces size limits on the data that passes between the Temporal Client, Workers, and the Temporal Service.
There are two distinct limits, each producing different error messages and behaviors, and they require different
solutions:

- [Payload size limit](#payload-size-limit)
- [gRPC message size limit](#grpc-message-size-limit)

## Payload size limit

The Temporal Service enforces a size limit on individual payloads. This limit is 2 MB on Temporal Cloud, but is
configurable on self-hosted deployments with a default of 2 MB. A [payload](/dataconversion#payload) represents the
serialized binary data for the input and output of Workflows and Activities.

### Error messages

The error message depends on which operation carried the oversized payload and which SDK version is in use. Examples
include:

- `WORKFLOW_TASK_FAILED_CAUSE_PAYLOADS_TOO_LARGE`
- `[TMPRL1103] Attempted to upload payloads with size that exceeded the error limit.`
- `BadScheduleActivityAttributes: ScheduleActivityTaskCommandAttributes.Input exceeds size limit`
- `Complete result exceeds size limit`
- `CompleteWorkflowExecutionCommandAttributes.Result exceeds size limit`
- `WORKFLOW_TASK_FAILED_CAUSE_BAD_UPDATE_WORKFLOW_EXECUTION_MESSAGE`

### Error behavior {/* #payload-error-behavior */}

The behavior when a payload exceeds the size limit depends on the SDK version.

**Python SDK 1.23.0+:** The SDK fails the Workflow Task with cause `WORKFLOW_TASK_FAILED_CAUSE_PAYLOADS_TOO_LARGE`. The
Workflow is not terminated and remains open, so you can deploy a fix and allow the Workflow to continue.

**All other SDK versions:** The behavior depends on whether the oversized payload is an input or a result:

- **Inputs (Workflow input, Activity input):** The Temporal Service rejects the command and terminates the Workflow.
  You'll need to resolve the issue and restart the Workflow.
- **Activity result:** The Temporal Service rejects the Activity completion and the Activity fails with an error.
- **Workflow result:** The Workflow gets stuck in a retry loop. The server rejects the `CompleteWorkflowExecution`
  command, and replay produces the same oversized result.

### How to resolve

1. Offload large payloads to an object store to reduce the risk of exceeding payload size limits:
  1. Pass references to the stored payloads within the Workflow instead of the actual data.
  1. Retrieve the payloads from the object store when needed during execution.

  This is called the
  [claim check pattern](https://dataengineering.wiki/Concepts/Software+Engineering/Claim+Check+Pattern). The claim
  check pattern is built into the SDKs as [External Storage](/external-storage), or you can implement your own claim
  check pattern by using a custom [Payload Codec](/payload-codec)

  This is the most reliable way to avoid hitting payload size limits. Consider implementing the claim check pattern for
  Workflows and Activities that have the potential to receive or return large payloads, even if they are currently
  within the limit.

  <ReleaseNoteHeader type="publicPreview">
    APIs and configuration may change before General Availability. Join the
   [#large-payloads Slack channel](https://temporalio.slack.com/archives/C09VA2DE15Y) to provide feedback or ask for
   help.
  </ReleaseNoteHeader>

1. Use compression with a [custom Payload Codec](/payload-codec) for large payloads. This may address the immediate
   issue, but if payload sizes continue to grow, the problem can arise again.

## gRPC message size limit

All communication between the Temporal Client, Workers, and the Temporal Service uses gRPC, which enforces a 4 MB limit
on each request. This limit applies to the full request, including all payload data and command metadata. For example,
when a Workflow schedules multiple Activities in a single Workflow Task, the Worker sends one request containing all
those commands to schedule the Activities and their inputs.

A Workflow can hit this limit even when every individual payload is under 2 MB. Scheduling several Activities with
moderate-sized inputs, or hundreds of Activities with tiny inputs in the same Workflow Task can push the combined
request past 4 MB. Activity results are also subject to this limit.

### Error messages

The error message depends on which operation carried the oversized gRPC message and which SDK version is in use.

- `WORKFLOW_TASK_FAILED_CAUSE_GRPC_MESSAGE_TOO_LARGE`
- `ScheduleToCloseTimeout` (Activities only, see [error behavior](#grpc-error-behavior) below)

### Error behavior {/* #grpc-error-behavior */}

The behavior when a gRPC message exceeds the size limit depends on the SDK version.

**Python SDK 1.23.0+:** The SDK fails the Workflow Task with cause `WORKFLOW_TASK_FAILED_CAUSE_PAYLOADS_TOO_LARGE`. The
Workflow is not terminated and remains open, so you can deploy a fix and allow the Workflow to continue. For Activities,
the Activity fails with an explicit error instead of timing out silently.

**All other SDK versions:** The behavior depends on where the oversized message originates:

- **Workflow Tasks:** The Workflow gets stuck in a retry loop that isn't visible in the Event History. This happens
  because when the Worker completes a Workflow Task, it sends all the commands the Workflow produced (such as Activity
  schedules and their inputs) back to the Temporal Service. If the combined size exceeds 4 MB, the SDK catches the gRPC
  error and sends a failed Workflow Task response with cause `WORKFLOW_TASK_FAILED_CAUSE_GRPC_MESSAGE_TOO_LARGE`. Replay
  produces the same oversized request every time, so the Workflow never makes progress.

- **Activity Tasks:** The Activity gets stuck in a retry loop or exits with a `ScheduleToCloseTimeout`. The Activity
  executes successfully, but the Worker can't deliver the oversized result over gRPC. The server never receives the
  completion, so it retries the Activity. Each retry completes successfully but fails to deliver the result. The
  Activity retries until the `ScheduleToCloseTimeout` expires. If no `ScheduleToCloseTimeout` is set, the Activity
  retries indefinitely until the Workflow is manually terminated. The `ResourceExhausted` gRPC error only appears in
  Worker logs.

### How to resolve

1. Break larger batches of commands into smaller batch sizes:
   - Workflow-level batching:
     1. Modify the Workflow to process Activities or Child Workflows in smaller batches.
     2. Iterate through each batch, waiting for completion before moving to the next.
   - [Workflow Task](/tasks#workflow-task)-level batching:
     1. Execute Activities in smaller batches within a single Workflow Task.
     2. Introduce brief pauses or sleeps between batches.
2. If the request is large because of payload sizes rather than the number of commands, refer to the
   [Payload size limit](#payload-size-limit) section for solutions.

---

## Troubleshoot the deadline-exceeded error

All requests made to the [Temporal Service](/temporal-service) by the Client or Worker are [gRPC requests](https://grpc.io/docs/what-is-grpc/core-concepts/#deadlines).
Sometimes, when these frontend requests can't be completed, you'll see this particular error message: `Context: deadline exceeded`.
Network interruptions, timeouts, server overload, and Query errors are some of the causes of this error.

The following sections discuss the nature of this error and how to troubleshoot it.

### Check system clocks

Timing skew can cause the system clock on a Worker to drift behind the system clock of the Temporal Service.
If the difference between the two clocks exceeds an Activity's Start-To-Close Timeout, an `Activity complete after timeout` error occurs.

If you receive an `Activity complete after timeout` error alongside `Context: deadline exceeded`, check the clocks on the Temporal Service's system and the system of the Worker sending that error.
If the Worker's clock doesn't match the Temporal Service, synchronize all clocks to an NTP server.

### Check Frontend Service logs

:::note

Cloud users cannot access some of the logs needed to diagnose the source of the error.

If you're using Temporal Cloud, create a [support ticket](/cloud/support#support-ticket) with as much information as possible, including the Namespace Name and the Workflow Ids of some Workflow Executions in which the issue occurs.

:::

[Frontend Service](/temporal-service/temporal-server#frontend-service) logs can show which parts of the Temporal Service aren't working.
For the error to appear, a service pod or container must be up and running.

OSS users can verify that the Frontend Service is connected and running by using the Temporal CLI.

```
temporal operator cluster health --address 127.0.0.1:7233
```

Use [`grpc-health-probe`](https://github.com/grpc-ecosystem/grpc-health-probe) to check the Frontend Service, [Matching Service](/temporal-service/temporal-server#matching-service), and [History Service](/temporal-service/temporal-server#history-service).

```
./grpc-health-probe -addr=frontendAddress:frontendPort -service=temporal.api.workflowservice.v1.WorkflowService

./grpc-health-probe -addr=matchingAddress:matchingPort -service=temporal.api.workflowservice.v1.MatchingService

./grpc-health-probe -addr=historyAddress:historyPort -service=temporal.api.workflowservice.v1.HistoryService
```

Logs can also be used to find failed Client [Query](/sending-messages#sending-queries) requests.

### Check your Temporal Service metrics

Temporal Service metrics can be used to detect issues (such as `resource exhausted`) that impact Temporal Service health.
A `resource exhausted` error can cause your client request to fail, which prompts the `deadline exceeded` error.

Use the following query to check for errors in `RpsLimit`, `ConcurrentLimit` and `SystemOverloaded` on your metrics dashboard.

```
sum(rate(service_errors_resource_exhausted{}[1m])) by (resource_exhausted_cause)
```

Look for high latencies, short timeouts, and other abnormal [Temporal Service metrics](/references/cluster-metrics).
If the metrics come from a specific service (such as History Service), check the service's health and performance.

### Check Workflow logic

Check your [Client and Worker configuration](/references/configuration) files for missing or invalid target values, such as the following:

- Server names
- Network or host addresses
- Certificates

Invalid targets also cause `connection refused` errors alongside `deadline exceeded`.
Check that the Client connects after updating your files.

### Advanced troubleshooting

In addition to the steps listed in the previous sections, check the areas mentioned in each of the following scenarios.

### After enabling mTLS

Check the health of the Temporal Service with `temporal operator cluster health`.

```
temporal operator cluster health --address [SERVER_ADDRESS]
```

Add any missing [environment variables](/references/web-ui-environment-variables) to the configuration files, and correct any incorrect values.
Server names and certificates must match between Frontend and internode.

### After restarting the Temporal Service

You might not be giving the Temporal Service enough time to respond and reconnect.
Restart the Server, wait, and then check all services for connectivity and further errors.

If the error persists, review your Workflow Execution History and server logs for more specific causes before continuing to troubleshoot.

### When executing or scheduling Workflows

One or more services might be unable to connect to the [Frontend Service](/temporal-service/temporal-server#frontend-service).
The Workflow might be unable to complete requests within the given connection time.

Increase the value of `frontend.keepAliveMaxConnectionAge` so that requests can be finished before the connection terminates.

:::note

If you increase `frontend.keepAliveMaxConnectionAge` values, consider monitoring your server performance for load.

:::

---

Still unable to resolve your issue?

- If you use Temporal Cloud, create a [support ticket](/cloud/support#support-ticket).
- If you use our open source software or Temporal Cloud, check for similar questions and possible solutions in our [community forum](https://community.temporal.io) or [community Slack](https://temporal.io/slack).

---

## Error handling and troubleshooting

Even the most reliable systems can encounter issues.
Our troubleshooting guides are designed to help you quickly identify and resolve potential errors, ensuring your Temporal applications run smoothly and efficiently.

- [Troubleshoot the BlobSizeLimitError](/troubleshooting/blob-size-limit-error): The `BlobSizeLimitError` happens when the size of a blob (payloads including Workflow context and each Workflow and Activity argument and return value) is too large.
  The maximum payload for a single request is 2 MB, and the maximum size for any Event History transaction is 4 MB.
- [Troubleshoot the Deadline-Exceeded Error](/troubleshooting/deadline-exceeded-error):
  The "Context: deadline exceeded" error occurs when requests to the Temporal Service by the Client or Worker cannot be completed.
  This can be due to network issues, timeouts, server overload, or Query errors.
- [Troubleshoot the Failed Reaching Server Error](/troubleshooting/last-connection-error): The message "Failed reaching server: last connection error" often happens due to an expired TLS certificate or during the Server startup process when Client requests reach the Server before roles are fully initialized.
- [Troubleshoot missed Schedule Actions](/troubleshooting/schedule-missed-actions): When a Schedule does not fire at its expected time, alert on the missed catchup window metric, then narrow down to the affected Schedule with `ListSchedules` and `DescribeSchedule`.
- [Troubleshoot Serverless Workers](/troubleshooting/serverless-workers): Diagnose issues with Serverless Workers on AWS Lambda by tracing the invocation flow from Task Queue to Worker execution.

---

## Troubleshoot the failed reaching server error

The message `Failed reaching server: last connection error` can often result from an expired TLS certificate or during the Server startup process, in which the Client requests reach the Server before the roles are fully initialized.

This troubleshooting guide shows you how to do the following:

- Verify the certification expiration date
- Renew the certification
- Update the server configuration

### Verify TLS certification expiration date

The first step in troubleshooting this error is to verify the expiration date of the TLS certification.
Then you can renew the certification and update the server configuration.

Choose one of the following methods to verify the expiration date of the TLS certification:

**Verify the expiration date of the TLS certification**

List the expiration date with the following command:

```command
tcld namespace accepted-client-ca list \
    --namespace <namespace_id>.<account_id> | \
    jq -r '.[0].notAfter'
```

If the returned date is in the past, the certificate has expired.
