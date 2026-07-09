- Raw Unix Epoch time (the number of milliseconds since 0000 UTC on January 1, 1970).
- `<n><duration`, where `<n>` is a value between 0 and 1000000, and `<duration>` is one of the following:
  - `second` or `s`
  - `minute` or `m`
  - `hour` or `h`
  - `day` or `d`
  - `week` or `w`
  - `month` or `M`
  - `year` or `y`

Alias: `--lt`

**Examples**

To specify 11:02:17 PM Pacific Daylight Time on April 13, 2022:

```bash
tctl workflow listall --latest-time '2022-04-13T23:02:17-07:00'
```

To specify 10 seconds before the current time:

```bash
tctl workflow listall --latest-time '10second'
```

### --workflow_id

Specify a [Workflow Id](/workflow-execution/workflowid-runid#workflow-id).

Alias: `-w`

**Example**

```bash
tctl workflow listall --workflow_id <id>
```

### --workflow_type

Specify the name of a [Workflow Type](/workflow-definition#workflow-type).

**Example**

```bash
tctl workflow listall --workflow_type <name>
```

### --status

Specify the status of a [Workflow Execution](/workflow-execution).
Supported values are as follows:

- `completed`
- `failed`
- `canceled`
- `terminated`
- `continuedasnew`
- `timedout`

**Example**

```bash
tctl workflow listall --status <value>
```

### --query

Specify an SQL-like query of [Search Attributes](/search-attribute).

Using the `--query` option causes tctl to ignore all other filter options, including `open`, `earliest_time`, `latest_time`, `workflow_id`, and `workflow_type`.

Alias: `-q`

**Example**

```bash
tctl workflow listall --query <value>
```

## listarchived

The `tctl workflow listarchived` command lists archived [Workflow Executions](/workflow-execution).

By default, this command lists a maximum of 100 Workflow Executions.

- To set the size of a page, use the `--pagesize` option.
- To list all pages, use the `--all` option.

See also [`tctl workflow list`](#list), [`tctl workflow listall`](#listall), and [`tctl workflow scan`](#scan).

`tctl workflow listarchived <modifiers>`

The following modifiers control the behavior of the command.

### --print_raw_time

Print the raw timestamp.

**Example**

```bash
tctl workflow listarchived --print_raw_time
```

### --print_datetime

Print the timestamp.

**Example**

```bash
tctl workflow listarchived --print_datetime
```

### --print_memo

Print a memo.

**Example**

```bash
tctl workflow listarchived --print_memo
```

### --print_search_attr

Print the [Search Attributes](/search-attribute).

**Example**

```bash
tctl workflow listarchived --print_search_attr
```

### --print_full

Print the full message without table formatting.

**Example**

```bash
tctl workflow listarchived --print_full
```

### --print_json

Print the raw JSON objects.

**Example**

```bash
tctl workflow listarchived --print_json
```

### --query

Specify an SQL-like query of [Search Attributes](/search-attribute).

Consult the documentation of the visibility archiver that is used by your [Namespace](/namespaces) for detailed instructions.

Alias: `-q`

**Example**

```bash
tctl workflow listarchived --query <value>
```

### --pagesize

Specify the maximum number of [Workflow Executions](/workflow-execution) to list on a page.
(By default, the `tctl workflow listarchived` command lists 100 Workflow Executions per page.)

**Example**

```bash
tctl workflow listarchived --pagesize <value>
```

### --all

List all pages.

**Example**

```bash
tctl workflow listarchived --all
```

## observe

The `tctl workflow observe` command shows the progress of the [Event History](/workflow-execution/event#event-history) of a [Workflow Execution](/workflow-execution).

See also [`tctl workflow observeid`](#observeid).

`tctl workflow observe <modifiers>`

Alias: `o`

The following modifiers control the behavior of the command.

### --workflow_id

Specify a [Workflow Id](/workflow-execution/workflowid-runid#workflow-id).

Alias: `-w`

**Example**

```bash
tctl workflow observe --workflow_id <id>
```

### --run_id

Specify a [Run Id](/workflow-execution/workflowid-runid#run-id).

Alias: `-r`

**Example**

```bash
tctl workflow observe --run_id <id>
```

### --show_detail

Show event details.

**Example**

```bash
tctl workflow observe --show_detail
```

### --max_field_length

Specify the maximum length for each attribute field.
The default value is 0.

**Example**

```bash
tctl workflow observe --max_field_length <length>
```

## observeid

The `tctl workflow observeid` command shows the progress of the [Event History](/workflow-execution/event#event-history) of a [Workflow Execution](/workflow-execution) for the specified [Workflow Id](/workflow-execution/workflowid-runid#workflow-id)and optional [Run Id](/workflow-execution/workflowid-runid#run-id).

`tctl workflow observeid <workflow_id> [<run_id>] <modifiers>`

This command is a shortcut for `tctl workflow observe --workflow_id <workflowid> [--run_id <runid>]`.

The following modifiers control the behavior of the command.

### --show_detail

Show event details.

**Example**

```bash
tctl workflow observeid --show_detail
```

### --max_field_length

Specify the maximum length for each attribute field.
The default value is 0.

**Example**

```bash
tctl workflow observeid --max_field_length <length>
```

## query

Alias: `q`

The `tctl workflow query` command sends a [Query](/sending-messages#sending-queries) to a [Workflow Execution](/workflow-execution).

Queries can be used to retrieve all or part of the Workflow state with given parameters.

```bash
$ tctl workflow query --workflow_id "HelloQuery" --query_type "getCount"
Query result as JSON:
3
```

Queries can also be used on completed Workflows.
Let's complete a Workflow by updating its greeting, and then query the now-finished Workflow.

```bash
$ tctl workflow signal --workflow_id "HelloQuery" --name "updateGreeting" --input \"Bye\"
Signal workflow succeeded.
$ tctl workflow query --workflow_id "HelloQuery" --query_type "getCount"
Query result as JSON:
4
```

Queries are written as follows:

`tctl workflow query --workflow_id [modifiers]`

The following modifiers control the behavior of the command.
Always include required modifiers when executing this command.

### --workflow_id

Specify a [Workflow Id](/workflow-execution/workflowid-runid#workflow-id). **This modifier is required.**

Alias: `-w`

**Example**

```bash
tctl workflow query --workflow_id <id>
```

### --run_id

Specify a [Run Id](/workflow-execution/workflowid-runid#run-id).

Alias: `-r`

**Example**

```bash
tctl workflow query --run_id <id>
```

### --query_type

Specify the type of Query to run.

**Example**

```bash
tctl workflow query --query_type <value>
```

### --input

Pass input for the Query.
Input must be in JSON format.
For multiple JSON objects, concatenate them and use spaces as separators.

Alias: `-i`

**Example**

```bash
tctl workflow query --input <json>
```

### --input_file

Pass input for the Query from a JSON file.
For multiple JSON objects, concatenate them and use spaces or newline characters as separators.
Input from the command line overwrites input from the file.

**Example**

```bash
tctl workflow query --input_file <filename>
```

### --query_reject_condition

Reject Queries based on Workflow state.
Valid values are `not_open` and `not_completed_cleanly`.

**Example**

```bash
tctl workflow query --query_reject_condition <value>
```

## reset

The `tctl workflow reset` command resets a [Workflow Execution](/workflow-execution) by either [`eventId`](#--event_id)or [`resetType`](#--reset_type).

Resetting a Workflow allows the process to be resumed from a certain point without losing your parameters or Event History.

To run multiple Reset operations at once, see [`tctl workflow reset-batch`](#reset-batch).

`tctl workflow reset <modifiers>`

The following modifiers control the behavior of the command.

### --workflow_id

Specify a [Workflow Id](/workflow-execution/workflowid-runid#workflow-id).

Alias: `-w`

**Example**

```bash
tctl workflow reset --workflow_id <id>
```

### --run_id

Specify a [Run Id](/workflow-execution/workflowid-runid#run-id).

Alias: `-r`

**Example**

```bash
tctl workflow reset --run_id <id>
```

### --event_id

Specify the `eventId` of any event after `WorkflowTaskStarted` to which you want to reset.
Valid values are `WorkflowTaskCompleted`, `WorkflowTaskFailed`, and `WorkflowTaskTimeout`.

**Example**

```bash
tctl workflow reset --event_id <id>
```

### --reason

Specify a reason for resetting the [Workflow Execution](/workflow-execution).

**Example**

```bash
tctl workflow reset --reason <string>
```

### --reset_type

Specify the event type to which you want to reset.

| Value                | Description                                                 |
| -------------------- | ----------------------------------------------------------- |
| `FirstWorkflowTask`  | Reset to the beginning of the Event History.                |
| `LastWorkflowTask`   | Reset to the end of the Event History.                      |
| `LastContinuedAsNew` | Reset to the end of the Event History for the previous Run. |
| `BadBinary`          | Reset to the point where a bad binary was used.             |

**Example**

```bash
tctl workflow reset --reset_type <value>
```

### --reset_reapply_type

Specify the types of events to reapply after the reset point.
Valid values are `All`, `Signal`, and `None`. The default is `All`.

**Example**

```bash
tctl workflow reset --reset_reapply_type <value>
```

### --reset_bad_binary_checksum

Specify the binary checksum when using `--reset_type BadBinary`.

**Example**

```bash
tctl workflow reset --reset_bad_binary_checksum <value>
```

## reset-batch

The `tctl workflow reset-batch` command resets a batch of [Workflow Executions](/workflow-execution) by [`resetType`](#--reset_type).

Resetting a Workflow allows the process to be resumed from a certain point without losing your parameters or Event History.

To reset individual Workflows, see [`tctl workflow reset`](#reset).

`tctl workflow reset-batch <modifiers>`

The following modifiers control the behavior of the command.

### --input_file

Provide an input file that specifies [Workflow Execution](/workflow-execution) to reset.

Each line contains one [Workflow Id](/workflow-execution/workflowid-runid#workflow-id)as the base Run and, optionally, a [Run Id](/workflow-execution/workflowid-runid#run-id).
If a Run Id is not specified, the current Run Id is used.

**Example**

```bash
tctl workflow reset-batch --input_file <filename>
```

### --query

Specify an SQL-like query of [Search Attributes](/search-attribute) describing the [Workflow Executions](/workflow-execution) to reset.

Alias: `-q`

**Example**

```bash
tctl workflow reset-batch --query <value>
```

### --exclude_file

Provide an input file that specifies [Workflow Executions](/workflow-execution) to exclude from resetting.

Each line contains one [Workflow Id](/workflow-execution/workflowid-runid#workflow-id).

**Example**

```bash
tctl workflow reset-batch --exclude_file <filename>
```

### --input_separator

Specify the separator for the input file.
The default is a tab (`\t`).

**Example**

```bash
tctl workflow reset-batch --input_separator <string>
```

### --reason

Specify a reason for resetting the [Workflow Executions](/workflow-execution).

**Example**

```bash
tctl workflow reset-batch --reason <string>
```

### --input_parallism

Specify the number of goroutines to run in parallel.
Each goroutine processes one line for every second.
The default is 1.

**Example**

```bash
tctl workflow reset-batch --input_parallism <value>
```

### --skip_current_open

Indicate that a [Workflow Execution](/workflow-execution) should be skipped if the current Run is open for the same [Workflow Id](/workflow-execution/workflowid-runid#workflow-id)as the base Run.

**Example**

```bash
tctl workflow reset-batch --skip_current_open
```

### --skip_base_is_not_current

Indicate that a [Workflow Execution](/workflow-execution) should be skipped if the base Run is not the current Run.

**Example**

```bash
tctl workflow reset-batch --skip_base_is_not_current
```

### --only_non_deterministic

Indicate that a [Workflow Execution](/workflow-execution) should be reset only if its last event is `WorkflowTaskFailed` with a nondeterminism error.

**Example**

```bash
tctl workflow reset-batch --only_non_deterministic
```

### --dry_run

Simulate use of the `tctl workflow reset-batch` command without resetting any [Workflow Executions](/workflow-execution).
Output is logged to `stdout`.

**Example**

```bash
tctl workflow reset-batch --dry_run
```

### --reset_type

Specify the event type to which you want to reset.

| Value                | Description                                                 |
| -------------------- | ----------------------------------------------------------- |
| `FirstWorkflowTask`  | Reset to the beginning of the Event History.                |
| `LastWorkflowTask`   | Reset to the end of the Event History.                      |
| `LastContinuedAsNew` | Reset to the end of the Event History for the previous Run. |
| `BadBinary`          | Reset to the point where a bad binary was used.             |

**Example**

```bash
tctl workflow reset-batch --reset_type <value>
```

### --reset_bad_binary_checksum

Specify the binary checksum when using `--reset_type BadBinary`.

**Example**

```bash
tctl workflow reset-batch --reset_bad_binary_checksum <value>
```

## run

The `tctl workflow run` command starts a new [Workflow Execution](/workflow-execution) and can show the progress of a Workflow Execution.
The command is entered in the following format:

`tctl workflow run <modifiers>`

To run a Workflow, the user must specify the following:

- Task queue name (`--taskqueue`)
- Workflow Type (`--workflow_type`)

```bash
tctl workflow run --taskqueue your-task-queue-name --workflow_type YourWorkflowDefinitionName
```

Single quotes (`''`) are used to wrap input as JSON.
This command doesn't finish until the Workflow completes.

The following modifiers control the behavior of the command.

### --taskqueue

Specify a [Task Queue](/task-queue).

Alias: `--t`

**Example**

```bash
tctl workflow run --taskqueue <name>
```

### --workflow_id

Specify a [Workflow Id](/workflow-execution/workflowid-runid#workflow-id).

Alias: `-w`

**Example**

```bash
tctl workflow run --workflow_id <id>
```

### --workflow_type

Specify the name of a [Workflow Type](/workflow-definition#workflow-type).

**Example**

```bash
tctl workflow run --workflow_type <name>
```

### --execution_timeout

Specify the [Start-To-Close Timeout](/encyclopedia/detecting-activity-failures#start-to-close-timeout) of the [Workflow Execution](/workflow-execution) in seconds.
The default value is 0.

**Example**

```bash
tctl workflow run --execution_timeout <seconds>
```

### --workflow_task_timeout

Specify the [Start-To-Close Timeout](/encyclopedia/detecting-activity-failures#start-to-close-timeout) of the [Workflow Task](/tasks#workflow-task) in seconds.
The default value is 10.

**Example**

```bash
tctl workflow run --workflow_task_timeout <seconds>
```

### --cron

Specify a [Cron Schedule](/cron-job#cron-schedules).

**Example**

```bash
tctl workflow run --cron <string>
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
tctl workflow run --workflowidreusepolicy AllowDuplicate
tctl workflow run --workflowidreusepolicy AllowDuplicateFailedOnly
tctl workflow run --workflowidreusepolicy RejectDuplicate
```

### --input

Pass input for the Workflow.
Input must be in JSON format.
For multiple JSON objects, pass each in a separate `--input` option. Use `null` for null values.

Alias: `-i`

**Example**

```bash
tctl workflow run --input <json>
```

### --input_file

Pass input for the Workflow from a JSON file.
For multiple JSON objects, concatenate them and use spaces or newline characters as separators.
Input from the command line overwrites input from the file.

**Example**

```bash
tctl workflow run --input_file <filename>
```

### --memo_key

Pass a key for a memo.
For multiple keys, concatenate them and use spaces as separators.

**Example**

```bash
tctl workflow run --memo_key <key>
```

### --memo

Pass a memo.
A memo is information in JSON format that can be shown when the Workflow is listed.
For multiple memos, concatenate them and use spaces as separators.
The order must match the order of keys in `--memo_key`.

**Example**

```bash
tctl workflow run --memo <json>
```

### --memo_file

Pass information for a memo from a JSON file.
For multiple JSON objects, concatenate them and use spaces or newline characters as separators.
The order must match the order of keys in `--memo_key`.

**Example**

```bash
tctl workflow run --memo_file <filename>
```

### --search_attr_key

Specify a [Search Attribute](/search-attribute) key.
For multiple keys, concatenate them and use pipes (`|`) as separators.

To list valid keys, use the `tctl cluster get-search-attributes` command.

**Example**

```bash
tctl workflow run --search_attr_key <key>
```

### --search_attr_value

Specify a [Search Attribute](/search-attribute) value.
For multiple values, concatenate them and use pipes (`|`) as separators.
If a value is an array, use JSON format, such as `["a","b"]`, `[1,2]`, `["true","false"]`, or `["2022-06-07T17:16:34-08:00","2022-06-07T18:16:34-08:00"]`.

To list valid keys and value types, use the `tctl cluster get-search-attributes` command.

**Example**

```bash
tctl workflow run --search_attr_value <value>
```

### --show_detail

Get event details.

**Example**

```bash
tctl workflow run --show_detail
```

### --max_field_length

Specify the maximum length for each attribute field.
The default value is 0.

**Example**

```bash
tctl workflow run --max_field_length <length>
```

## scan

The `tctl workflow scan` command lists [Workflow Executions](/workflow-execution).
It is faster than the `tctl workflow listall` command, but the results are not sorted.

By default, this command lists a maximum of 2000 Workflow Executions.
To set the size of a page, use the `--pagesize` option.

See also [`tctl workflow list`](#list), [`tctl workflow listall`](#listall), and [`tctl workflow listarchived`](#listarchived).

`tctl workflow scan <modifiers>`

The following modifiers control the behavior of the command.

### --print_raw_time

Print the raw timestamp.

**Example**

```bash
tctl workflow scan --print_raw_time
```

### --print_datetime

Print the timestamp.

**Example**

```bash
tctl workflow scan --print_datetime
```

### --print_memo

Print a memo.

**Example**

```bash
tctl workflow scan --print_memo
```

### --print_search_attr

Print the [Search Attributes](/search-attribute).

**Example**

```bash
tctl workflow scan --print_search_attr
```

### --print_full

Print the full message without table formatting.

**Example**

```bash
tctl workflow scan --print_full
```

### --print_json

Print the raw JSON objects.

**Example**

```bash
tctl workflow scan --print_json
```

### --pagesize

Specify the maximum number of [Workflow Execution](/workflow-execution) to list on a page.
(By default, the `tctl workflow scan` command lists 2000 Workflow Executions per page.)

**Example**

```bash
tctl workflow scan --pagesize <value>
```

### --query

Specify an SQL-like query of [Search Attributes](/search-attribute).

Alias: `-q`

**Example**

```bash
tctl workflow scan --query <value>
```

## show

The `tctl workflow show` command shows the [Event History](/workflow-execution/event#event-history) for the specified [Workflow Execution](/workflow-execution).

`tctl workflow show <modifiers>`

See also [`tctl workflow showid`](#showid).

The following modifiers control the behavior of the command.

### --workflow_id

Show the History of a [Workflow Execution](/workflow-execution) by specifying a [Workflow Id](/workflow-execution/workflowid-runid#workflow-id).

Alias: `-w`

**Example**

```bash
tctl workflow show --workflow_id <id>
```

### --run_id

Show the History of a [Workflow Execution](/workflow-execution) by specifying a [Run Id](/workflow-execution/workflowid-runid#run-id).

Alias: `-r`

**Example**

```bash
tctl workflow show --run_id <id>
```

### --print_datetime

Print the timestamp.

**Example**

```bash
tctl workflow show --print_datetime
```

### --print_raw_time

Print the raw timestamp.

**Example**

```bash
tctl workflow show --print_raw_time
```

### --output_filename

Serialize an event to a file.

**Example**

```bash
tctl workflow show --output_filename <filename>
```

### --print_full

Print full event details.

**Example**

```bash
tctl workflow show --print_full
```

### --print_event_version

Print the event version.

**Example**

```bash
tctl workflow show --print_event_version
```

### --event_id

Print the details of a specified event.
The default value is 0.

**Example**

```bash
tctl workflow show --event_id <id>
```

### --max_field_length

Specify the maximum length for each attribute field.
The default value is 500.

**Example**

```bash
tctl workflow show --max_field_length <length>
```

### --reset_points_only

Show only events that are eligible for reset.

**Example**

```bash
tctl workflow show --reset_points_only
```

## showid

The `tctl workflow showid` command shows the Workflow Execution Event History for the specified [Workflow Id](/workflow-execution/workflowid-runid#workflow-id)and optional [Run Id](/workflow-execution/workflowid-runid#run-id).

`tctl workflow showid <workflow_id> [<run_id>] <modifiers>`

This command is a shortcut for `tctl workflow show --workflow_id <workflowid> [--run_id <runid>]`.

Example:

```bashbash
tctl workflow showid <workflow_id>
```

Example output:

```bashtext
1  WorkflowExecutionStarted    {WorkflowType:{Name:HelloWorld}, ParentInitiatedEventId:0,
                                TaskQueue:{Name:HelloWorldTaskQueue, Kind:Normal},
                                Input:[Temporal], WorkflowExecutionTimeout:1h0m0s,
                                WorkflowRunTimeout:1h0m0s, WorkflowTaskTimeout:10s,
                                Initiator:Unspecified, LastCompletionResult:[],
                                OriginalExecutionRunId:f0c04163-833f-490b-99a9-ee48b6199213,
                                Identity:tctl@z0mb1e,
                                FirstExecutionRunId:f0c04163-833f-490b-99a9-ee48b6199213,
                                Attempt:1, WorkflowExecutionExpirationTime:2020-10-13
                                21:41:06.349 +0000 UTC, FirstWorkflowTaskBackoff:0s}
2  WorkflowTaskScheduled       {TaskQueue:{Name:HelloWorldTaskQueue,
                                Kind:Normal},
                                StartToCloseTimeout:10s, Attempt:1}
3  WorkflowTaskStarted         {ScheduledEventId:2, Identity:15079@z0mb1e,
                                RequestId:731f7b41-5ae4-42e4-9695-ecd857d571f1}
4  WorkflowTaskCompleted       {ScheduledEventId:2,
                                StartedEventId:3,
                                Identity:15079@z0mb1e}
5  WorkflowExecutionCompleted  {Result:[],
                                WorkflowTaskCompletedEventId:4}
```

The following modifiers control the behavior of the command.

### --print_datetime

Print the timestamp.

**Example**

```bash
tctl workflow showid <workflow_id> --print_datetime
```

### --print_raw_time

Print the raw timestamp.

**Example**

```bash
tctl workflow showid <workflow_id> --print_raw_time
```

### --output_filename

Serialize an event to a file.

**Example**

```bash
tctl workflow showid <workflow_id> --output_filename <filename>
```

### --print_full

Print full event details.

**Example**

```bash
tctl workflow showid <workflow_id> --print_full
```

### --print_event_version

Print the event version.

**Example**

```bash
tctl workflow showid <workflow_id> --print_event_version
```

### --event_id

Print the details of a specified event.
The default value is 0.

**Example**

```bash
tctl workflow showid <workflow_id> --event_id <id>
```

### --max_field_length

Specify the maximum length for each attribute field.
The default value is 500.

**Example**

```bash
tctl workflow showid <workflow_id> --max_field_length <length>
```

### --reset_points_only

Show only events that are eligible for reset.

**Example**

```bash
tctl workflow showid <workflow_id> --reset_points_only
```

## signal

The `tctl workflow signal` command [Signals](/sending-messages#sending-signals) a [Workflow Execution](/workflow-execution).

Workflows listen for Signals by their Signal name, and can be made to listen to one or more Signal names.
Workflows can also listen for SQL queries.

The Workflow below listens for instances of "HelloSignal":

```bash
tctl workflow start  --workflow_id "HelloSignal" --taskqueue HelloWorldTaskQueue --workflow_type HelloWorld --execution_timeout 3600 --input \"World\"
```

The Worker would return this output upon receiving the Signal:

```text
13:57:44.258 [workflow-method] INFO  c.t.s.javaquickstart.GettingStarted - 1: Hello World!
