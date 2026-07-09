- [How to set a Cron Schedule using the PHP SDK](/develop/php/workflows/schedules#temporal-cron-jobs)
- [How to set a Cron Schedule using the Python SDK](/develop/python/workflows/schedules#temporal-cron-jobs)
- [How to set a Cron Schedule using the TypeScript SDK](/develop/typescript/workflows/schedules#temporal-cron-jobs)

<CaptionedImage
    src="/diagrams/temporal-cron-job.svg"
    title="Temporal Cron Job timeline" />

A Temporal Cron Job is similar to a classic unix cron job.
Just as a unix cron job accepts a command and a schedule on which to execute that command, a Cron Schedule can be provided with the call to spawn a Workflow Execution.
If a Cron Schedule is provided, the Temporal Server will spawn an execution for the associated Workflow Type per the schedule.

Each Workflow Execution within the series is considered a Run.

- Each Run receives the same input parameters as the initial Run.
- Each Run inherits the same Workflow Options as the initial Run.

The Temporal Server spawns the first Workflow Execution in the chain of Runs immediately.
However, it calculates and applies a backoff (`firstWorkflowTaskBackoff`) so that the first Workflow Task of the Workflow Execution does not get placed into a Task Queue until the scheduled time.
After each Run Completes, Fails, or reaches the [Workflow Run Timeout](/encyclopedia/detecting-workflow-failures#workflow-run-timeout), the same thing happens: the next run will be created immediately with a new `firstWorkflowTaskBackoff` that is calculated based on the current Server time and the defined Cron Schedule.

The Temporal Server spawns the next Run only after the current Run has Completed, Failed, or has reached the Workflow Run Timeout.
This means that, if a Retry Policy has also been provided, and a Run Fails or reaches the Workflow Run Timeout, the Run will first be retried per the Retry Policy until the Run Completes or the Retry Policy has been exhausted.
If the next Run, per the Cron Schedule, is due to spawn while the current Run is still Open (including retries), the Server automatically starts the new Run after the current Run completes successfully.
The start time for this new Run and the Cron definitions are used to calculate the `firstWorkflowTaskBackoff` that is applied to the new Run.

A [Workflow Execution Timeout](/encyclopedia/detecting-workflow-failures#workflow-execution-timeout) is used to limit how long a Workflow can be executing (have an Open status), including retries and any usage of Continue As New.
The Cron Schedule runs until the Workflow Execution Timeout is reached or you terminate the Workflow.

<CaptionedImage
    src="/diagrams/temporal-cron-job-failure-with-retry.svg"
    title="Temporal Cron Job Run Failure with a Retry Policy" />

## Cron Schedules {/* #cron-schedules */}

Cron Schedules are interpreted in UTC time by default.

The Cron Schedule is provided as a string and must follow one of two specifications:

**Classic specification**

This is what the "classic" specification looks like:

```
┌───────────── minute (0 - 59)
│ ┌───────────── hour (0 - 23)
│ │ ┌───────────── day of the month (1 - 31)
│ │ │ ┌───────────── month (1 - 12)
│ │ │ │ ┌───────────── day of the week (0 - 6) (Sunday to Saturday)
│ │ │ │ │
│ │ │ │ │
* * * * *
```

For example, `15 8 * * *` causes a Workflow Execution to spawn daily at 8:15 AM UTC.
Use the [crontab guru site](https://crontab.guru/) to test your cron expressions.

### `robfig` predefined schedules and intervals

You can also pass any of the [predefined schedules](https://pkg.go.dev/github.com/robfig/cron/v3#hdr-Predefined_schedules) or [intervals](https://pkg.go.dev/github.com/robfig/cron/v3#hdr-Intervals) described in the [`robfig/cron` documentation](https://pkg.go.dev/github.com/robfig/cron/v3).

```
| Schedules              | Description                                | Equivalent To |
| ---------------------- | ------------------------------------------ | ------------- |
| @yearly (or @annually) | Run once a year, midnight, Jan. 1st        | 0 0 1 1 *     |
| @monthly               | Run once a month, midnight, first of month | 0 0 1 * *     |
| @weekly                | Run once a week, midnight between Sat/Sun  | 0 0 * * 0     |
| @daily (or @midnight)  | Run once a day, midnight                   | 0 0 * * *     |
| @hourly                | Run once an hour, beginning of hour        | 0 * * * *     |
```

For example, "@weekly" causes a Workflow Execution to spawn once a week at midnight between Saturday and Sunday.

Intervals just take a string that can be accepted by [time.ParseDuration](http://golang.org/pkg/time/#ParseDuration).

```
@every <duration>
```

## Time zones {/* #cron-job-time-zones */}

_This feature only applies in Temporal 1.15 and up_

You can change the time zone that a Cron Schedule is interpreted in by prefixing the specification with `CRON_TZ=America/New_York` (or your [desired time zone from tz](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)). `CRON_TZ=America/New_York 15 8 * * *` therefore spawns a Workflow Execution every day at 8:15 AM New York time, subject to caveats listed below.

Consider that using time zones in production introduces a surprising amount of complexity and failure modes!
**If at all possible, we recommend specifying Cron Schedules in UTC (the default)**.

If you need to use time zones, here are a few edge cases to keep in mind:

- **Beware Daylight Saving Time:** If a Temporal Cron Job is scheduled around the time when daylight saving time (DST) begins or ends (for example, `30 2 * * *`), **it might run zero, one, or two times in a day**! The Cron library that we use does not do any special handling of DST transitions. Avoid schedules that include times that fall within DST transition periods.
  - For example, in the US, DST begins at 2 AM. When you "fall back," the clock goes `1:59 … 1:00 … 1:01 … 1:59 … 2:00 … 2:01 AM` and any Cron jobs that fall in that 1 AM hour are fired again. The inverse happens when clocks "spring forward" for DST, and Cron jobs that fall in the 2 AM hour are skipped.
  - In other time zones like Chile and Iran, DST "spring forward" is at midnight. 11:59 PM is followed by 1 AM, which means `00:00:00` never happens.
- **Self Hosting note:** If you manage your own Temporal Service, you are responsible for ensuring that it has access to current `tzdata` files. The official Docker images are built with [tzdata](https://docs.w3cub.com/go/time/tzdata/index) installed (provided by Alpine Linux), but ultimately you should be aware of how tzdata is deployed and updated in your infrastructure.
- **Updating Temporal:** If you use the official Docker images, note that an upgrade of the Temporal Service may include an update to the tzdata files, which may change the meaning of your Cron Schedule. You should be aware of upcoming changes to the definitions of the time zones you use, particularly around daylight saving time start/end dates.
- **Absolute Time Fixed at Start:** The absolute start time of the next Run is computed and stored in the database when the previous Run completes, and is not recomputed. This means that if you have a Cron Schedule that runs very infrequently, and the definition of the time zone changes between one Run and the next, the Run might happen at the wrong time. For example, `CRON_TZ=America/Los_Angeles 0 12 11 11 *` means "noon in Los Angeles on November 11" (normally not in DST). If at some point the government makes any changes (for example, move the end of DST one week later, or stay on permanent DST year-round), the meaning of that specification changes. In that first year, the Run happens at the wrong time, because it was computed using the older definition.

## How to stop a Temporal Cron Job {/* #stop-cron-schedules */}

A Temporal Cron Job does not stop spawning Runs until it has been Terminated or until the [Workflow Execution Timeout](/encyclopedia/detecting-workflow-failures#workflow-execution-timeout) is reached.

A Cancellation Request affects only the current Run.

Use the Workflow Id in any requests to Cancel or Terminate.

---

## Dynamic handler

This page discusses [Dynamic Handler](#dynamic-handler).

## What is a Dynamic Handler? {/* #dynamic-handler */}

Temporal supports Dynamic Workflows, Activities, Signals, and Queries.

:::note

Currently, the Temporal SDKs that support Dynamic Handlers are:

- [Java](/develop/java/workflows/message-passing#dynamic-handler)
- [Python](/develop/python/workflows/message-passing#dynamic-handler)
- [.NET](/develop/dotnet/workflows/message-passing#dynamic-handler)
- [Go](/develop/go/workflows/dynamic-workflow)
- [Ruby](/develop/ruby/workflows/message-passing#dynamic-handler)

:::

These are unnamed handlers that are invoked if no other statically defined handler with the given name exists.

Dynamic Handlers provide flexibility to handle cases where the names of Workflows, Activities, Signals, or Queries aren't known at run time.

:::caution

Dynamic Handlers should be used judiciously as a fallback mechanism rather than the primary approach.
Overusing them can lead to maintainability and debugging issues down the line.

Instead, Workflows, Activities, Signals, and Queries should be defined statically whenever possible, with clear names that indicate their purpose.
Use static definitions as the primary way of structuring your Workflows.

Reserve Dynamic Handlers for cases where the handler names are not known at compile time and need to be looked up dynamically at runtime.
They are meant to handle edge cases and act as a catch-all, not as the main way of invoking logic.

:::

---

## Patching

This page discusses [Patching](#patching).

## What is Patching? {/* #patching */}

A Patch defines a logical branch in a Workflow for a specific change, similar to a feature flag.
It applies a code change to new Workflow Executions while avoiding disruptive changes to in-progress Workflow Executions.
When you want to make substantive code changes that may affect existing Workflow executions, create a patch.

### Detailed Description of the `patched()` Function

This applies to the `patched()` function in the Python, .NET, and Ruby SDKs.

#### Behavior When Not Replaying

If the execution is not replaying, when it encounters a call to `patched()`, it first checks the event history.

- If the patch ID is not in the event history, the execution adds a marker to the event history, upserts a search attribute, and returns `true`. This happens in the first block of the patch ID.
- If the patch ID is in the event history, the execution doesn't modify the history, and returns `true`.
  This happens in a patch ID's subsequent blocks, because the event history was updated in the first block.

There is a caveat to this behavior, which we will cover below.

#### Behavior When Replaying With Marker Before-Or-At Current Location

If the execution is replaying and has a call to `patched()`, and if the event history has a marker from a call to `patched()` in the same place (which means it will match the original event history), then it writes a marker to the replay event history and returns `true`.

This is similar to the behavior of the non-replay case, and also happens in a given patch ID's first block.

If the code has a call to `patched()`, and the event history has a marker with that Patch ID earlier in the history, it will return `true` and will not modify the replay event history.

This is also similar to the behavior of the non-replay case, and also happens in a given patch ID's subsequent blocks.

#### Behavior When Replaying With Marker After Current Location

If the Event History's Marker Event is after the current execution point, that means the new patch is too early.
The execution will encounter the new patch before the original.
The execution will attempt to write the marker to the replay event history, but it will throw a non-deterministic exception because the replay and original event histories don't match.

#### Behavior When Replaying With No Marker For that Patch ID

During a Replay, if there is no marker for a given patch ID, the execution will return `false` and will not add a marker to the event history. In addition, all future calls to `patched()` with that ID will return `false` -- even after it is done replaying and is running new code.

The [preceding section](#behavior-when-not-replaying) states that if the execution is not replaying, the `patched()` function will always return `true`.
If the marker doesn't exist, it will be added, and if the marker already exists, it won't be re-added.

However, this behavior doesn't occur if there was already a call to `patched()` with that ID in the replay code, but not in the event history.
In this situation, the function won't return `true`.

#### A Summary of the Two Potentially Unexpected Behaviors

Recapping the potentially unexpected behaviors that may occur during a Replay:

If the execution hits a call to `patched()`, but that patch ID isn't _at or before that point_ in the event history, you may not realize that the event history _after_ the current execution location matters.
This behavior occurs because:

- If that patch ID exists later, you get a non-determinism error
- If the patch doesn't exist later, you don't get a non-determinism error, and the call returns `false`

If the execution hits a call to `patched()` with an ID that doesn't exist in the history, then not only will it return `false` in that occurence, but it will also return `false` if the execution surpasses the Replay threshold and is running new code.

#### Implications of the Behaviors

If you deploy new code while Workflows are executing, any Workflows that were in the middle of executing will Replay up to the point they were at when the Worker was shut down.
When they do this Replay, they will not follow the `patched()` branches in the code.
For the rest of the execution after they have replayed to the point before the deployment and worker restart, they will either:

- Use new code if there was no call to `patched()` in the replay code
- If there was a call to `patched()` in the replay code, they will
  run the non-patched code during and after replay

This might sound odd, but it's actually exactly what's needed because that means that if the future patched code depends on earlier patched code, then it won't use the new code -- it will use the old code instead.

But if there's new code in the future, and there was no code earlier in the body that required the new patch, then it can switch over to the new code, which it will do.

Note that this behavior means that the Workflow _does not always run the newest code_.
It only does that if not replaying or if replay is surpassed and there hasn't been a call to `patched()` (with that ID) throughout the replay.

#### Recommendations

Based on this behavior and the implications, when patching in new code, always put the newest code at the top of an if-patched-block.

```python
if patched('v3'):
    # This is the newest version of the code.
    # put this at the top, so when it is running
    # a fresh execution and not replaying,
    # this patched statement will return true
    # and it will run the new code.
    pass
elif patched('v2'):
    pass
else:
    pass
```

The following sample shows how `patched()` will behave in a conditional block that's arranged differently.
In this case, the code's conditional block doesn't have the newest code at the top.
Because `patched()` will return `True` when not Replaying (except with the preceding caveats), this snippet will run the `v2` branch instead of `v3` in new executions.

```python
if patched('v2'):
    # This is bad because when doing a new execution (i.e. not replaying),
    # patched statements evaluate to True (and put a marker
    # in the event history), which means that new executions
    # will use v2, and miss v3 below
    pass
elif patched('v3'):
    pass
else:
  pass
```

---

## Schedule

This page discusses [Schedule](#schedule).

## What is a Schedule? {/* #schedule */}

A Schedule contains instructions for starting a [Workflow Execution](/workflow-execution) at specific times.
Schedules provide a more flexible and user-friendly approach than [Temporal Cron Jobs](/cron-job).

- [How to enable Schedules](#limitations)
- [How to operate Schedules using the Temporal CLI](/cli/command-reference/schedule)

A Schedule has an identity and is independent of a Workflow Execution.
This differs from a Temporal Cron Job, which relies on a cron schedule as a property of the Workflow Execution.

:::info

For triggering a Workflow Execution at a specific one-time future point rather than on a recurring schedule, the [Start Delay](/workflow-execution/timers-delays#delay-workflow-execution) option should be used instead of a Schedule.

:::

### Action

The Action of a Schedule is where the Workflow Execution properties are established, such as Workflow Type, Task Queue, parameters, and timeouts.

Workflow Executions started by a Schedule have the following additional properties:

- The Action's timestamp is appended to the Workflow Id.
- The `TemporalScheduledStartTime` [Search Attribute](/search-attribute) is added to the Workflow Execution.
  The value is the Action's timestamp.
- The `TemporalScheduledById` Search Attribute is added to the Workflow Execution.
  The value is the Schedule Id.

### Spec

The Schedule Spec defines when the Action should be taken.
Unless many Schedules have Actions scheduled at the same time, Actions should generally start within 1 second of the specified time.
There are two kinds of Schedule Spec:

- A simple interval, like "every 30 minutes" (aligned to start at the Unix epoch, and optionally including a phase offset).
- A calendar-based expression, similar to the "cron expressions" supported by lots of software, including the older Temporal Cron feature.

These two kinds have multiple representations, depending on the interface or SDK you're using, but they all support the same features.

In the Temporal CLI, for example, an interval is specified as a string like `45m` to mean every 45 minutes, or `6h/5h` to mean every 6 hours but at the start of the fifth hour within each period.

In the Temporal CLI, a calendar expression can be specified as either a traditional cron string with five (or six or seven) positional fields, or as JSON with named fields:

```json
{
  "year": "2022",
  "month": "Jan,Apr,Jul,Oct",
  "dayOfMonth": "1,15",
  "hour": "11-14"
}
```

The following calendar JSON fields are available:

- `year`
- `month`
- `dayOfMonth`
- `dayOfWeek`
- `hour`
- `minute`
- `second`
- `comment`

Each field can contain a comma-separated list of ranges (or the `*` wildcard), and each range can include a slash followed by a skip value.
The `hour`, `minute`, and `second` fields default to `0` while the others default to `*`, so you can describe many useful specs with only a few fields.

For `month`, names of months may be used instead of integers (case-insensitive, abbreviations permitted).
For `dayOfWeek`, day-of-week names may be used.

The `comment` field is optional and can be used to include a free-form description of the intent of the calendar spec, useful for complicated specs.

No matter which form you supply, calendar and interval specs are converted to canonical representations.
What you see when you "describe" or "list" a Schedule might not look exactly like what you entered, but it has the same meaning.

#### Phase offset

By default, intervals align to the Unix epoch (January 1, 1970 at midnight UTC), so without a phase offset, a 7-day interval would fire every Thursday at whatever time midnight UTC equates to in your local time, which may not be convenient for your use case.

Use a phase offset when you need your recurring Schedule to fire at a specific, human-meaningful time like every 10 days at 5pm UTC on a particular date, rather than accepting the arbitrary time the epoch alignment produces.

There is an `offset` parameter you can set so an `interval` spec fires exactly at a pre-determined date and time. Here's an example of how you can calculate the `offset` and apply it to your Schedules.

Timestamps are measured with UNIX time. That means 7 days is 604,800 seconds (7 * 24 * 60 * 60), 5 days is 432,000 (5 * 24 * 60 * 60), etc. The Schedule fires when the following condition is true:

```
((currentTimestampUTC - phase offset) % interval) == 0
```

So using an interval of 7 days and a phase offset of 0, that means the Schedule fires on `December 28th 2023, at midnight UTC`:

```
((1703721600 - 0) % 604800) = 0
```

For an interval of 5 days and a phase offset of 0, the Schedule fires on `December 29th 2023`

```
((1703808000 - 0) % 432000) = 0
```

You can calculate the phase offset you need for any interval. Take the UNIX timestamp of any date and time you want your Schedule to execute, then calculate the following:

```
phase offset = referenceTimestampUTC % interval
```

For example, if you want a Schedule that will fire every 10 days, including Jun 19th 2024 at 5pm UTC, you need to calculate the UNIX timestamp:

```
UNIX Timestamp of 2024-06-19T17:00:00 UTC = 1718816400
```

Then you need to calculate the number of seconds for your interval:

```
Interval of 10 days = (10 * 24 * 60 * 60) = 864000
```

Finally, you can calculate the phase offset you need:

```
phase offset = 1718816400 % 864000 = 320400
```

So you will set your Schedule interval to `864000s` (10 days) and phase to `320400s` and you get exactly every 10 days at 5pm UTC.

#### Other Spec features

**Multiple intervals/calendar expressions:** A Spec can have combinations of multiple intervals and/or calendar expressions to define a specific Schedule.

**Time bounds:** Provide an absolute start or end time (or both) with a Spec to ensure that no actions are taken before the start time or after the end time.

**Exclusions:** A Spec can contain exclusions in the form of zero or more calendar expressions.
This can be used to express scheduling like "each Monday at noon except for holidays".
You'll have to provide your own set of exclusions and include it in each schedule; there are no pre-defined sets.
(This feature isn't currently exposed in the Temporal CLI or the Temporal Web UI.)

**Jitter:** If given, a random offset between zero and the maximum jitter is added to each Action time (but bounded by the time until the next scheduled Action).

**Time zones:** By default, calendar-based expressions are interpreted in UTC.
Temporal recommends using UTC to avoid various surprising properties of time zones.
If you don't want to use UTC, you can provide the name of a time zone.
The time zone definition is loaded on the Temporal Server Worker Service from either disk or the fallback embedded in the binary.

For more operational control, embed the contents of the time zone database file in the Schedule Spec itself.
(Note: this isn't currently exposed in the Temporal CLI or the web UI.)

### Pause

A Schedule can be Paused.
When a Schedule is Paused, the Spec has no effect.
However, you can still force manual actions by using the [temporal schedule trigger](/cli/command-reference/schedule#trigger) command.

To assist communication among developers and operators, a “notes” field can be updated on pause or resume to store an explanation for the current state.

### Backfill

A Schedule can be Backfilled.
When a Schedule is Backfilled, all the Actions that would have been taken over a specified time period are taken now (in parallel if the `AllowAll` [Overlap Policy](#overlap-policy) is used; sequentially if `BufferAll` is used).
You might use this to fill in runs from a time period when the Schedule was paused due to an external condition that's now resolved, or a period before the Schedule was created.

### Limit number of Actions

A Schedule can be limited to a certain number of scheduled Actions (that is, not trigger immediately).
After that it will act as if it were paused.

### Policies

A Schedule supports a set of Policies that enable customizing behavior.

#### Overlap Policy

The Overlap Policy controls what happens when it is time to start a Workflow Execution but a previously started Workflow Execution is still running.
The following options are available:

- `Skip`: **Default**.
  Nothing happens; the Workflow Execution is not started.
- `BufferOne`: Starts the Workflow Execution as soon as the current one completes.
  The buffer is limited to one.
  If another Workflow Execution is supposed to start, but one is already in the buffer, only the one in the buffer eventually starts.
- `BufferAll`: Allows an unlimited number of Workflows to buffer.
  They are started sequentially.
- `CancelOther`: Cancels the running Workflow Execution, and then starts the new one after the old one completes cancellation.
- `TerminateOther`: Terminates the running Workflow Execution and starts the new one immediately.
- `AllowAll` Starts any number of concurrent Workflow Executions.
  With this policy (and only this policy), more than one Workflow Execution, started by the Schedule, can run simultaneously.

#### Catchup Window

The Temporal Service might be down or unavailable at the time when a Schedule should take an Action.
When it comes back up, the Catchup Window controls which missed Actions should be taken at that point.
