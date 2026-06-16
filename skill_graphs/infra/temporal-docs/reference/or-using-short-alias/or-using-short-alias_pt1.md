# OR using short alias
tctl --ns your-namespace n re
```

The following modifiers control the behavior of the command.

### --active_cluster

Specify the name of the active [Temporal Cluster](/temporal-service) when registering a [Namespace](/namespaces).
This value changes for Global Namespaces when a failover occurs.

**Example**

```bash
tctl namespace register --active_cluster <name>
```

### --clusters

Specify a list of [Temporal Clusters](/temporal-service) when registering a [Namespace](/namespaces).

The list contains the names of Clusters (separated by spaces) to which the Namespace can fail over.
Make sure to include to the currently active Cluster.
This is a read-only setting and cannot be changed.

This modifier is valid only when the `--global_namespace` modifier is set to true.

**Example**

```bash
tctl namespace register --clusters <names>
```

### --description

Specify a description when registering a [Namespace](/namespaces).

**Example**

```bash
tctl namespace register --description <value>
```

### --global_namespace

Specifies whether a [Namespace](/namespaces) is a [Global Namespace](/global-namespace).
When enabled, it controls the creation of replication tasks on updates allowing the state to be replicated across Clusters.
This is a read-only setting and cannot be changed.

**Example**

```bash
tctl namespace register --global_namespace <boolean>
```

### --history_archival_state

Set the state of [Archival](/temporal-service/archival).
Valid values are `disabled` and `enabled`.

**Example**

```bash
tctl namespace register --history_archival_state <value>
```

### --history_uri

Specify the URI for [Archival](/temporal-service/archival).
The URI cannot be changed after Archival is first enabled.

**Example**

```bash
tctl namespace register --history_uri <uri>
```

### --namespace_data

Specify data for a [Namespace](/namespaces) in the form of key-value pairs (such as `k1:v1,k2:v2,k3:v3`).

**Example**

```bash
tctl namespace register --namespace_data <data>
```

### --owner_email

Specify the email address of the [Namespace](/namespaces) owner.

**Example**

```bash
tctl namespace register --owner_email <value>
```

### --retention

Set the [Retention Period](/temporal-service/temporal-server#retention-period) for the [Namespace](/namespaces).

The Retention Period applies to Closed [Workflow Executions](/workflow-execution).

**Example**

```bash
tctl namespace register --retention <value>
```

### --visibility_archival_state

Set the visibility state for [Archival](/temporal-service/archival).
Valid values are `disabled` and `enabled`.

**Example**

```bash
tctl namespace register --visibility_archival_state <value>
```

### --visibility_uri

Specify the visibility URI for [Archival](/temporal-service/archival).
The URI cannot be changed after Archival is first enabled.

**Example**

```bash
tctl namespace register --visibility_uri <uri>
```

## update

The `tctl namespace update` command updates a [Namespace](/namespaces).

`tctl namespace update`

The following modifiers control the behavior of the command.

### --active_cluster

Specify the name of the active [Temporal Cluster](/temporal-service) when updating a [Namespace](/namespaces).

**Example**

```bash
tctl namespace update --active_cluster <name>
```

### --add_bad_binary

Add a binary checksum to use when resetting a [Workflow Execution](/workflow-execution).
Temporal will not dispatch any [Commands](/workflow-execution#command) to the given binary.

See also [`--remove_bad_binary`](#--remove_bad_binary).

**Example**

```bash
tctl namespace update --add_bad_binary <value>
```

### --clusters

Specify a list of [Temporal Clusters](/temporal-service) when updating a [Namespace](/namespaces).

The list contains the names of Clusters (separated by spaces) to which the Namespace can fail over.

This modifier is valid only when the `--global_namespace` modifier is set to true.

**Example**

```bash
tctl namespace update --clusters <names>
```

### --description

Specify a description when updating a [Namespace](/namespaces).

**Example**

```bash
tctl namespace update --description <value>
```

### --history_archival_state

Set the state of [Archival](/temporal-service/archival).
Valid values are `disabled` and `enabled`.

**Example**

```bash
tctl namespace update --history_archival_state <value>
```

### --history_uri

Specify the URI for [Archival](/temporal-service/archival).
The URI cannot be changed after Archival is first enabled.

**Example**

```bash
tctl namespace update --history_uri <uri>
```

### --namespace_data

Specify data for a [Namespace](/namespaces) in the form of key-value pairs (such as `k1:v1,k2:v2,k3:v3`).

**Example**

```bash
tctl namespace update --namespace_data <data>
```

### --owner_email

Specify the email address of the [Namespace](/namespaces) owner.

**Example**

```bash
tctl namespace update --owner_email <value>
```

### --reason

Specify a reason for updating a [Namespace](/namespaces).

**Example**

```bash
tctl namespace update --reason <value>
```

### --remove_bad_binary

Remove a binary checksum.

See also [`--add_bad_binary`](#--add_bad_binary).

**Example**

```bash
tctl namespace update --remove_bad_binary <value>
```

### --retention

Specify the number of days to retain [Workflow Executions](/workflow-execution).

**Example**

```bash
tctl namespace update --retention <value>
```

### --visibility_archival_state

Set the visibility state for [Archival](/temporal-service/archival).
Valid values are `disabled` and `enabled`.

**Example**

```bash
tctl namespace update --visibility_archival_state <value>
```

### --visibility_uri

Specify the visibility URI for [Archival](/temporal-service/archival).
The URI cannot be changed after Archival is first enabled.

**Example**

```bash
tctl namespace update --visibility_uri <uri>
```

---

## tctl 1.17 schedule command reference

:::info tctl is deprecated

The tctl command line utility has been deprecated and is no longer actively supported.
We recommend transitioning to [Temporal CLI](/cli) for continued use and access to new features.

Thank you for being a valued part of the Temporal community.

:::

A [Schedule](/schedule) is an experimental feature available in `tctl 1.17` and `tctl next`.

- [Backfill a Schedule using tctl](#backfill)
- [Create a Schedule using tctl](#create)
- [Delete a Schedule using tctl](#delete)
- [Describe a Schedule using tctl](#describe)
- [List Schedules using tctl](#list)
- [Toggle Pause on Schedule using tctl](#toggle)
- [Trigger an Action on a Schedule using tctl](#trigger)
- [Update a Schedule using tctl](#update)

## backfill

Backfilling a Schedule means having it do now what it would have done over a specified time range (generally in the past, although it won't prevent you from giving a time range in the future).
You might use this to fill in runs from a time period when the Schedule was paused due to an external condition that's now resolved, or a period before the Schedule was created.

```shell
tctl schedule backfill --sid 'your-schedule-id' \
  --overlap-policy 'BufferAll'                \
  --start-time '2022-05-01T00:00:00Z'         \
  --end-time   '2022-05-31T23:59:59Z'
```

Note that, similar to [tctl schedule trigger](#trigger) immediately, you probably want to override the Overlap Policy.
Specifying `AllowAll` runs all the backfilled Workflows at once; `BufferAll` runs them sequentially.
The other policies don't make much sense in this context.

## create

With tctl, create a Schedule like this:

```shell
$ tctl config set version next   # ensure you're using the new tctl
$ tctl schedule create \
    --schedule-id 'your-schedule-id' \
    --interval '5h/15m' \
    --calendar '{"dayOfWeek":"Fri","hour":"11","minute":"3"}' \
    --overlap-policy 'BufferAll' \
    --workflow-id 'your-workflow-id' \
    --task-queue 'your-task-queue' \
    --workflow-type 'YourWorkflowType'
```

This Schedule takes action every 5 hours at 15 minutes past the hour and also at 11:03 on Fridays.
It starts a Workflow `YourWorkflowType` on Task Queue `your-task-queue`, giving it a Workflow Id like `your-workflow-id-2022-06-17T11:03:00Z`.
Workflows do not run in parallel.
If they would otherwise overlap, they are buffered to run sequentially.

You can also use traditional cron strings, including all features that are supported by `CronSchedule` today, such as `@weekly` and other shorthands, `@every`, and `CRON_TZ`.

```shell
$ tctl schedule create \
    --schedule-id 'your-schedule-id' \
    --cron '3 11 * * Fri' \
    --workflow-id 'your-workflow-id' \
    --task-queue 'your-task-queue' \
    --workflow-type 'YourWorkflowType'
```

<!-- ADDING TO DEPRECATED SECTION FOR INBOUND LINKS AND OLDER DEPLOYMENTS -->

Temporal Workflow Schedule Cron strings follow this format:

```
┌───────────── minute (0 - 59)
│ ┌───────────── hour (0 - 23)
│ │ ┌───────────── day of the month (1 - 31)
│ │ │ ┌───────────── month (1 - 12)
│ │ │ │ ┌───────────── day of the week (0 - 6) (Sunday to Saturday)
│ │ │ │ │
* * * * *
```

Any combination of `--calendar`, `--interval`, and `--cron` is supported and Actions will happen at any of the specified times.
If you use both `--time-zone` and also `CRON_TZ`, they must agree.

See `tctl schedule create --help` for the full set of available options.

## delete

A Schedule can be deleted.

Deleting a Schedule **does not** affect any Workflows started by the Schedule.
Workflow Executions started by Schedules can be cancelled or terminated using the same methods as any others.
However, Workflow Executions started by a Schedule can be identified by the Search Attributes added to them and can be targeted by a [batch](/tctl-v1/batch/) command for termination.

```shell
$ tctl schedule delete --schedule-id 'your-schedule-id'
```

## describe

Display the current Schedule configuration as well as extra information about past, current, and future Runs.

```shell
tctl schedule describe --schedule-id 'your-schedule-id'
```

Because the Schedule Spec is converted to canonical representations, the output might not be in the same form as it was input.

## list

```shell
tctl schedule list
```

Because the Schedule Spec is converted to canonical representations, the output might not be in the same form as it was input.

## toggle

```shell
$ tctl schedule toggle --schedule-id 'your-schedule-id' --pause --reason "paused because the database is down"
$ tctl schedule toggle --schedule-id 'your-schedule-id' --unpause --reason "the database is back up"
```

## trigger

Starting a Workflow Run immediately with a Schedule, regardless of its configured Spec, is a common use case.

```shell
$ tctl schedule trigger --schedule-id 'your-schedule-id'
```

Note that the action that it takes is subject to the Overlap Policy of the Schedule by default: if the overlap policy is `Skip` and a Workflow is already running, the triggered Action to start the next Workflow Run is skipped!
Likewise, if the overlap policy is `BufferAll`, the triggered run is buffered behind one or more runs.

If you really want it to run right now, you can override the overlap policy for this request:

```shell
$ tctl schedule trigger --schedule-id 'your-schedule-id' --overlap-policy 'AllowAll'
```

## update

Any part of the Schedule configuration can be updated at any time.

`tctl schedule update` takes the same options as `tctl schedule create` and replaces the entire configuration of the schedule with what's provided.

This means if you want to change just one value, you have to provide everything else again.

---

## tctl v1.17 taskqueue command reference

:::info tctl is deprecated

The tctl command line utility has been deprecated and is no longer actively supported.
We recommend transitioning to [Temporal CLI](/cli) for continued use and access to new features.

Thank you for being a valued part of the Temporal community.

:::

The `tctl taskqueue` command enables [Task Queue](/task-queue) operations.

Alias: `t`

- [tctl taskqueue describe](#describe)
- [tctl taskqueue list-partition](#list-partition)

## describe

The `tctl taskqueue describe` command describes the poller information of a [Task Queue](/task-queue).

`tctl taskqueue describe <modifiers> <value>`

The following modifiers control the behavior of the command.

### --taskqueue

_Required modifier_

Specify a [Task Queue](/task-queue).

Alias: `--t`

**Example**

```bash
tctl taskqueue describe --taskqueue <value>
```

### --taskqueuetype

Specify the type of a [Task Queue](/task-queue).
The type can be `workflow` or `activity`.
The default is `workflow`.

**Example**

```bash
tctl taskqueue describe --taskqueue <value> --taskqueuetype <type>
```

## list-partition

The `tctl taskqueue list-partition` command lists the partitions of a [Task Queue](/task-queue) and the hostname for the partitions.

`tctl taskqueue list-partition --taskqueue <value>`

The following modifier controls the behavior of the command.

### --taskqueue

_Required modifier_

Specify a [Task Queue](/task-queue) description.

Alias: `--t`

**Example**

```bash
tctl taskqueue list-partition --taskqueue <value>
```

---

## tctl v1.17 workflow command reference

:::info tctl is deprecated

The tctl command line utility has been deprecated and is no longer actively supported.
We recommend transitioning to [Temporal CLI](/cli) for continued use and access to new features.

Thank you for being a valued part of the Temporal community.

:::

The `tctl workflow` commands enable [Workflow Execution](/workflow-execution) operations.

- [tctl workflow cancel](#cancel)
- [tctl workflow count](#count)
- [tctl workflow describe](#describe)
- [tctl workflow describeid](#describeid)
- [tctl workflow list](#list)
- [tctl workflow listall](#listall)
- [tctl workflow listarchived](#listarchived)
- [tctl workflow observe](#observe)
- [tctl workflow observeid](#observeid)
- [tctl workflow query](#query)
- [tctl workflow reset](#reset)
- [tctl workflow reset-batch](#reset-batch)
- [tctl workflow run](#run)
- [tctl workflow scan](#scan)
- [tctl workflow show](#show)
- [tctl workflow showid](#showid)
- [tctl workflow signal](#signal)
- [tctl workflow stack](#stack)
- [tctl workflow start](#start)
- [tctl workflow terminate](#terminate)

## cancel

The `tctl workflow cancel --query` command cancels a [Workflow Execution](/workflow-execution).

Canceling a running Workflow Execution records a `WorkflowExecutionCancelRequested` event in the History.
A new [Workflow Task](/tasks#workflow-task) will be scheduled.
After cancellation, the Workflow Execution can perform cleanup work.

See also [`tctl workflow terminate --query`](#terminate).

`tctl workflow cancel --query <query> <modifiers>`

The following modifiers control the behavior of the command.

### --workflow_id

Specify a [Workflow Id](/workflow-execution/workflowid-runid#workflow-id).

Alias: `-w`

**Example**

```bash
tctl workflow cancel --workflow_id <id>
```

### --run_id

Specify a [Run Id](/workflow-execution/workflowid-runid#run-id).

Alias: `-r`

**Example**

```bash
tctl workflow cancel --run_id <id>
```

## count

The `tctl workflow count` command counts [Workflow Executions](/workflow-execution).
This command requires Elasticsearch to be enabled.

`tctl workflow count <modifiers>`

The following modifier controls the behavior of the command.

### --query

_Required modifier_

Specify an SQL-like query of [Search Attributes](/search-attribute).

Alias: `-q`

**Example**

To count all open [Workflow Executions](/workflow-execution):

```bash
tctl workflow count --query 'ExecutionStatus="Running"'
```

## describe

The `tctl workflow describe` command shows information about a [Workflow Execution](/workflow-execution).
This information can be used to locate a failed Workflow Execution, for example.

To find a Workflow with a given Run Id, refer to [`tctl workflow describeid`](#describeid).

`tctl workflow describe <modifiers>`

The following modifiers control the behavior of the command.
Always include required modifiers when executing this command.

### --workflow_id

**This is a required modifier.**

Specify a [Workflow Id](/workflow-execution/workflowid-runid#workflow-id).

Alias: `-w`

**Example**

```bash
tctl workflow describe --workflow_id <id>
```

### --run_id

Specify a [Run Id](/workflow-execution/workflowid-runid#run-id).
If a Run Id is not provided, the command will show the latest Workflow Execution of that Workflow Id.

Alias: `-r`

**Example**

```bash
tctl workflow describe --run_id <id>
```

### --print_raw

Print properties exactly as they are stored.

**Example**

```bash
tctl workflow describe --print_raw
```

### --reset_points_only

Show only events that are eligible for reset.
If successful, the command returns the Run Id of all deployments, and the times at which the Events were created.

**Example**

```bash
tctl workflow describe --reset_points_only
```

## describeid

The `tctl workflow describeid` command shows information about a [Workflow Execution](/workflow-execution) for the specified [Workflow Id](/workflow-execution/workflowid-runid#workflow-id)and optional [Run Id](/workflow-execution/workflowid-runid#run-id).

`tctl workflow describeid <workflow_id> <run_id> <modifiers>`

This command is a shortcut for `tctl workflow describe --workflow_id <workflowid> --run_id <runid>`.

The following modifiers control the behavior of the command.

### --print_raw

Print properties exactly as they are stored.

**Example**

```bash
tctl workflow describeid <workflow_id> <id> --print_raw
```

### --reset_points_only

Show only events that are eligible for reset.

**Example**

```bash
tctl workflow describeid <workflow_id> --reset_points_only
```

## list

The `tctl workflow list` command lists open or closed [Workflow Executions](/workflow-execution).

By default, this command lists a maximum of 10 closed Workflow Executions.

- To set the size of a page, use the `--pagesize` option.
- To list multiple pages, use the `--more` option.
- To list open Workflow Executions, use the `--open` option.

See also [`tctl workflow listall`](#listall), [`tctl workflow listarchived`](#listarchived), and [`tctl workflow scan`](#scan).

`tctl workflow list <modifiers>`

The following modifiers control the behavior of the command.

### --print_raw_time

Print the raw timestamp.

**Example**

```bash
tctl workflow list --print_raw_time
```

### --print_datetime

Print the timestamp.

**Example**

```bash
tctl workflow list --print_datetime
```

### --print_memo

Print a memo.

**Example**

```bash
tctl workflow list --print_memo
```

### --print_search_attr

Print the [Search Attributes](/search-attribute).

**Example**

```bash
tctl workflow list --print_search_attr
```

### --print_full

Print the full message without table formatting.

**Example**

```bash
tctl workflow list --print_full
```

### --print_json

Print the raw JSON objects.

**Example**

```bash
tctl workflow list --print_json
```

### --open

List open [Workflow Executions](/workflow-execution).
(By default, the `tctl workflow list` command lists closed Workflow Executions.)

**Example**

```bash
tctl workflow list --open
```

### --earliest_time

Specify the earliest start time to list.
Supported format are as follows:

- `<year>-<month>-<day>T<hour>:<minute>:<second><+|-><offsethours>:<offsetminutes>`
- Raw Unix Epoch time (the number of milliseconds since 0000 UTC on January 1, 1970).
- `<n><duration`, where `<n>` is a value between 0 and 1000000, and `<duration>` is one of the following:
  - `second` or `s`
  - `minute` or `m`
  - `hour` or `h`
  - `day` or `d`
  - `week` or `w`
  - `month` or `M`
  - `year` or `y`

**Examples**

To specify 3:04:05 PM India Standard Time on January 2, 2022:

```bash
tctl workflow list --earliest-time '2022-01-02T15:04:05+05:30'
```

To specify 15 minutes before the current time:

```bash
tctl workflow list --earliest-time '15minute'
```

### --latest_time

Specify the latest start time to list.
Supported formats are as follows:

- `<year>-<month>-<day>T<hour>:<minute>:<second><+|-><offsethours>:<offsetminutes>`
- Raw Unix Epoch time (the number of milliseconds since 0000 UTC on January 1, 1970).
- `<n><duration`, where `<n>` is a value between 0 and 1000000, and `<duration>` is one of the following:
  - `second` or `s`
  - `minute` or `m`
  - `hour` or `h`
  - `day` or `d`
  - `week` or `w`
  - `month` or `M`
  - `year` or `y`

**Examples**

To specify 11:02:17 PM Pacific Daylight Time on April 13, 2022:

```bash
tctl workflow list --latest_time '2022-04-13T23:02:17-07:00'
```

To specify 10s before the current time:

```bash
tctl workflow list --latest_time '10second'
```

### --workflow_id

Specify a [Workflow Id](/workflow-execution/workflowid-runid#workflow-id).

Alias: `-w`

**Example**

```bash
tctl workflow list --workflow_id <id>
```

### --workflow_type

Specify the name of a [Workflow Type](/workflow-definition#workflow-type).

**Example**

```bash
tctl workflow list --workflow_type <name>
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
tctl workflow list --status <value>
```

### --query

**How to list and filter Workflow Executions with a [List Filter](/list-filter) using tctl.**

The `--query` flag is supported only when [Advanced Visibility](/visibility#advanced-visibility) is configured with the Cluster.

Using the `--query` option causes tctl to ignore all other filter options, including `open`, `earliest_time`, `latest_time`, `workflow_id`, and `workflow_type`.

Alias: `-q`

**Example**

```bashbash
tctl workflow list --query "WorkflowId=<your-workflow-id>"
```

More examples:

```bashbash
tctl workflow list \
  --query "WorkflowType='main.SampleParentWorkflow' AND ExecutionStatus='Running'"
```

```bashbash
tctl workflow list \
  --query '(CustomKeywordField = "keyword1" and CustomIntField >= 5) or CustomKeywordField = "keyword2"' \
  --print_search_attr
```

```bashbash
tctl workflow list \
  --query 'CustomKeywordField in ("keyword2", "keyword1") and CustomIntField >= 5 and CloseTime between "2018-06-07T16:16:36-08:00" and "2019-06-07T16:46:34-08:00" order by CustomDatetimeField desc' \
  --print_search_attr
```

```bashbash
tctl workflow list \
  --query 'WorkflowType = "main.Workflow" and (WorkflowId = "1645a588-4772-4dab-b276-5f9db108b3a8" or RunId = "be66519b-5f09-40cd-b2e8-20e4106244dc")'
```

```bashbash
tctl workflow list \
  --query 'WorkflowType = "main.Workflow" StartTime > "2019-06-07T16:46:34-08:00" and ExecutionStatus = "Running"'
```

### --more

List more than one page.
(By default, the `tctl workflow list` command lists one page of results.)

**Example**

```bash
tctl workflow list --more
```

### --pagesize

Specify the maximum number of [Workflow Executions](/workflow-execution) to list on a page.
(By default, the `tctl workflow list` command lists 10 Workflow Executions per page.)

**Example**

```bash
tctl workflow list --pagesize <value>
```

## listall

The `tctl workflow listall` command lists all open or closed [Workflow Executions](/workflow-execution).

By default, this command lists all closed Workflow Executions.
To list open Workflow Executions, use the `--open` option.

See also [`tctl workflow list`](#list), [`tctl workflow listarchived`](#listarchived), and [`tctl workflow scan`](#scan).

`tctl workflow listall <modifiers>`

The following modifiers control the behavior of the command.

###`--print_raw_time

Print the raw timestamp.

**Example**

```bash
tctl workflow listall --print_raw_time
```

### --print_datetime

Print the timestamp.

**Example**

```bash
tctl workflow listall --print_datetime
```

### --print_memo

Print a memo.

**Example**

```bash
tctl workflow listall --print_memo
```

### --print_search_attr

Print the [Search Attributes](/search-attribute).

**Example**

```bash
tctl workflow listall --print_search_attr
```

### `--print_full`

Print the full message without table formatting.

**Example**

```bash
tctl workflow listall --print_full
```

### --print_json

Print the raw JSON objects.

**Example**

```bash
tctl workflow listall --print_json
```

### --open

List open [Workflow Executions](/workflow-execution).
(By default, the `tctl workflow listall` command lists closed Workflow Executions.)

**Example**

```bash
tctl workflow listall --open
```

### --earliest_time

Specify the earliest start time to list. Supported format are as follows:

- `<year>-<month>-<day>T<hour>:<minute>:<second><+|-><offsethours>:<offsetminutes>`
- Raw Unix Epoch time (the number of milliseconds since 0000 UTC on January 1, 1970).
- `<n><duration`, where `<n>` is a value between 0 and 1000000, and `<duration>` is one of the following:
  - `second` or `s`
  - `minute` or `m`
  - `hour` or `h`
  - `day` or `d`
  - `week` or `w`
  - `month` or `M`
  - `year` or `y`

**Examples**

To specify 3:04:05 PM India Standard Time on January 2, 2022:

```bash
tctl workflow listall --earliest-time '2022-01-02T15:04:05+05:30'
```

To specify 15 minutes before the current time:

```bash
tctl workflow listall --earliest-time '15minute'
```

### --latest_time

Specify the latest start time to list. Supported formats are as follows:

- `<year>-<month>-<day>T<hour>:<minute>:<second><+|-><offsethours>:<offsetminutes>`
