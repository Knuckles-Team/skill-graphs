
Specifies whether to send a JWT access token as ‘authorization' header in requests with the Codec Server.

## `TEMPORAL_CODEC_INCLUDE_CREDENTIALS`

Specifies whether to include credentials along with requests to the Codec Server.

## `TEMPORAL_FORWARD_HEADERS`

Forward-specified HTTP headers to direct from HTTP API requests to the Temporal gRPC backend. This is a comma-delimited
list of the HTTP headers to be forwarded.

## `TEMPORAL_HIDE_LOGS`

If enabled, does not print logs from the Temporal Service.

---

## Temporal Web UI

The Temporal Web UI provides users with Workflow Execution state and metadata for debugging purposes. It ships with
every [Temporal CLI](/cli) release and is available with [Temporal Cloud](/cloud).

You can configure the Temporal Web UI to work in your own environment. See the
[UI configuration reference](/references/web-ui-configuration).

Web UI open source repos:

- [temporalio/ui](https://github.com/temporalio/ui)
- [temporalio/ui-server](https://github.com/temporalio/ui-server)

## Namespaces

All Namespaces in your self-hosted Temporal Service or Temporal Cloud account are listed under **Namespaces** in the
left section of the window. You can also switch Namespaces from the Workflows view by selecting from the Namespace
switcher at the top right corner of the window. After you select a Namespace, the Web UI shows the Recent Workflows page
for that Namespace. In Temporal Cloud, users can access only the Namespaces that they have been granted access to. For
details, see [Namespace-level permissions](/cloud/manage-access/roles-and-permissions#namespace-level-permissions).

## Workflows

The main Workflows page displays a table of all Workflow Executions within the retention period.

Users can list Workflow Executions by any of the following:

- [Status](/workflow-execution#workflow-execution-status)
- [Workflow ID](/workflow-execution/workflowid-runid#workflow-id)
- [Workflow Type](/workflow-definition#workflow-type)
- Start time
- End time
- Any other Default or Custom [Search Attribute](/search-attribute) that uses [List Filter](/list-filter)

For start time and end time, users can set their preferred date and time format as one of the following:

- UTC
- Local
- Relative

Select a Workflow Execution to view the Workflow Execution's History, Workers, Relationships, pending Activities and
Nexus Operations, Queries, and Metadata.

### Saved Views {/* #saved-views */}

Saved Views let you save and reuse your frequently used visibility queries in the Temporal Web UI. Instead of recreating
complex filters every time, you can save them once and apply them with a single click.

Saved Views are stored locally in your browser and are available to you whenever you use the Temporal Web UI in this
browser. Each user will have their own private collection.

#### Apply a Saved View

By default, The Workflows page has several default Saved Views. You can also create your own Saved Views.

Click the name of a Saved View in the list to display the corresponding Workflows that match the query.

The Workflow List page will refresh with the results of the Saved View.

#### Create a Saved View

You can create a new Saved View from the Workflows page.

1. Create a Saved View by using the filter UI to build your criteria, or you can use the raw query editor to write
   custom query strings.
1. Your new view will appear in the Custom Views list as New View. Click the Save as New button to bring up the Save as
   View window. Name your Saved View. Names must be unique to each user and can contain a max of 255 characters.
1. Click Save. Your new view will appear in the Custom Views list

You can create up to 20 Saved Views. When you reach this limit, you'll need to delete some Saved Views before you can
save new ones.

#### Make Temporary Changes to a Saved View query

You can modify a Saved View temporarily without changing the saved criteria.

1. Select the Saved View you want to change.
1. Adjust the UI filters as needed.
1. The Workflows page will refresh with the results of the new query, without changing the Saved View.
1. If you want to keep your temporary changes, you can:
   - Click Save, which will replace the original Saved View with your modifications.
   - Click Edit, modify the name, and click Save, which will replace the original Saved View with your modifications and
     change the name.
   - Click Edit, modify the name, and click Create New, which will create a new Saved View with your new settings and a
     new name.

#### Rename a Saved View Query

You can rename an existing Saved View from the Workflows page.

1. Select the Saved View you want to change.
1. Click Edit.
1. In the Edit View dialog box, enter a new name for the Saved View.
1. Click Save to apply your changes and rename the existing Saved View, or click Create Copy to create a new Saved View
   with the new name.

#### Deleting Saved Views

You can delete a Saved View from the Workflows page, because it is no longer useful, or to create room for new Saved
Views.

1. Select the Saved View you want to delete. You can only delete queries you’ve created; you cannot delete the system
   defaults.
1. Click “Edit” and then "Delete this Saved View".

:::note Deleting Saved Views is permanent

Deleted queries cannot be recovered, so make sure you won't need them again. If you accidentally delete a Saved List,
you will need to recreate it.

:::

#### Share a Saved View

You can share a Saved View as a URL.

1. Select the Saved View you want to share.
1. Click the “Share” button to copy the URL for this Saved View to the clipboard. You can also copy the URL directly
   from the browser.

:::note Saved Views and time

Saved Views that use relative times will be shared with absolute time.

:::

## Task Failures View {/* #task-failures-view */}

The Task Failures view is a pre-defined Saved View that displays Workflows that have a Workflow Task failure.
These Workflows are still running, but one of their Tasks has failed or timed out.

The details of the Task Failures view displays the Workflow's ID, the Run ID, and the Workflow type.
Clicking on any of the links in the details opens the Workflow page for that Workflow.
On this page, you will find more information about the Task that failed and remaining pending tasks.
You can also cancel the Workflow by clicking the Request Cancellation button on this page.

Our system monitors Workflow task execution patterns in real-time. When a Workflow experiences five consecutive task failures or timeouts, it gets automatically flagged. The moment the Workflow recovers with a successful task, the flag clears. This smart threshold filters out minor glitches while surfacing Workflows with genuine problems.

### Activating Task Failures View {/* #activate-task-failures-view */}

This is enabled by default for Temporal Cloud users. If you're self-hosting Temporal, you'll need to update the `system.numConsecutiveWorkflowTaskProblemsToTriggerSearchAttribute` [dynamic config](/references/dynamic-configuration).

Here's an example of how to make the config update for the dev server:

```command
temporal server start-dev \
 --dynamic-config-value system.numConsecutiveWorkflowTaskProblemsToTriggerSearchAttribute=5
```

`numConsecutiveWorkflowTaskProblemsToTriggerSearchAttribute` is the number of consecutive Workflow Task Failures required to trigger the `TemporalReportedProblems` search attribute. The default value is 5. If adding this search attribute causes strain on the visibility system, consider increasing this number.

To turn off the feature for a Namespace, set `numConsecutiveWorkflowTaskProblemsToTriggerSearchAttribute` to 0.

## History

A Workflow Execution History is a view of the [Events](/workflow-execution/event#event) and Event fields within the
Workflow Execution. Approximately [40 different Events](/references/events) can appear in a Workflow Execution's Event
History.

The top of the page lists the following execution metadata:

- Start Time, Close Time and Duration
- [Run Id](/workflow-execution/workflowid-runid#run-id)
- [Workflow Type](/workflow-definition#workflow-type)
- [Task Queue](/task-queue)
- Parent and Parent ID
- SDK
- [State Transitions](/workflow-execution#state-transition)
- [Billable Actions Count](/cloud/actions-usage#actions-in-workflows) (Temporal Cloud only)

The Input and Results section displays the function arguments and return values for debugging purposes. Results are not
available until the Workflow finishes.

The History tab has the following views:

- Timeline: A chronological or reverse-chronological order of events with a summary. Clicking into an Event displays all
  details for that Event.
- All: View all History Events.
- Compact: A logical grouping of Activities, Signals and Timers.
- JSON: The full JSON code for the workflow.

### Download Event History

The entire Workflow Execution Event History, in JSON format, can be downloaded from this section.

### Workflow Actions

Workflow Executions can request a Cancellation, send a Signal or Update, or Reset and Terminate directly from the UI.
Start a new Workflow Execution with pre-filled values with the Start Workflow Like This One button.

### Relationships

Displays the full hierarchy of a Workflow Execution with all parent and child nodes displayed in a tree.

### Workers

Displays the Workers currently polling on the Workflow Task Queue with a count. If no Workers are polling, an error
displays.

### Pending Activities

Displays a summary of recently active and/or pending Activity Executions. Clicking a pending Activity directs the user
to the Pending Activities tab to view details.

### Call Stack

The screen shows the captured result from the [\_\_stack_trace](/sending-messages#stack-trace-query) Query. The Query is
performed when the tab is selected. It works only if a Worker is running and available to return the call stack. The
call stack shows each location where Workflow code is waiting.

### Queries

Lists all Queries sent to the Workflow Execution.

### Metadata

Displays User Metadata including static Workflow Summary and Details and dynamic Current Details. Lists all Events with
User Metadata data to give you a human-readable log of what's happening in your Workflow.

## Schedules

On Temporal Cloud and self-hosted Temporal Service Web UI, the Schedules page lists all the [Schedules](/schedule)
created on the selected Namespace.

Click a Schedule to see details, such as configured frequency, start and end times, and recent and upcoming runs.

:::tip Setting Schedules with Strings

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

:::

To read more about Schedules, explore these links:

<RelatedReadContainer>
  <RelatedReadItem path="/develop/go/workflows/schedules" text="Schedules using the Go SDK" archetype="feature-guide" />
  <RelatedReadItem path="/develop/java/workflows/schedules" text="Schedules using the Java SDK" archetype="feature-guide" />
  <RelatedReadItem path="/develop/php/workflows/schedules" text="Schedules using the PHP SDK" archetype="feature-guide" />
  <RelatedReadItem path="/develop/python/workflows/schedules" text="Schedules using the Python SDK" archetype="feature-guide" />
  <RelatedReadItem
    path="/develop/typescript/workflows/schedules"
    text="Schedules using the TypeScript SDK"
    archetype="feature-guide"
  />
  <RelatedReadItem path="/develop/dotnet/workflows/schedules" text="Schedules using the .NET SDK" archetype="feature-guide" />
</RelatedReadContainer>

### Settings

On Temporal Cloud, **Settings** is visible only to Account Owner and Global Admin
[roles](/cloud/manage-access/roles-and-permissions#account-level-roles).

Click **Settings** to see and manage the list of users in your account and to set up integrations such as
[Observability](/cloud/metrics) and [Audit logging](/cloud/audit-logs).

On a self-hosted Temporal Service, manage your users, metrics, and logging in your
[server configuration](/references/configuration).

### Archive

On a self-hosted Temporal Service, Archive shows [Archived](/temporal-service/archival) data of your Workflow Executions
on the Namespace.

To see data in your self-hosted Temporal Service, you must have
[Archival set up and configured](/self-hosted-guide/archival).

For information and details on the Archive feature in Temporal Cloud, contact your Temporal representative.

### Codec Server

The Web UI can use a [Codec Server](/codec-server) with a custom Data Converter to decode inputs and return values. For
details, see [Securing your data](/production-deployment/data-encryption).

The UI supports a [Codec Server endpoint](/production-deployment/data-encryption#web-ui). For details on setting the
Codec Server endpoint, see [Codec Server setup](/production-deployment/data-encryption#codec-server-setup).

---

## Glossary

The following terms are used in [Temporal Platform](/temporal) documentation.

#### [Action](/cloud/pricing#action)

An Action is the fundamental pricing unit in Temporal Cloud. Temporal Actions are the building blocks for Workflow
Executions. When you execute a Temporal Workflow, its Actions create the ongoing state and progress of your Temporal
Application.

<!-- _Tags: [term](/tags/term), [pricing](/tags/pricing), [temporal-cloud](/tags/temporal-cloud), [explanation](/tags/explanation)_ -->

#### [Actions Per Second (APS)](/cloud/limits#actions-per-second)

APS, or Actions per second, is specific to Temporal Cloud. Each Temporal Cloud Namespace enforces a rate limit, which is
measured in Actions per second (APS). This is the number of Actions, such as starting or signaling a Workflow, that can
be performed per second within a specific Namespace.

<!-- _Tags: [term](/tags/term), [pricing](/tags/pricing), [temporal-cloud](/tags/temporal-cloud), [explanation](/tags/explanation)_ -->

#### [Activity](/activities)

In day-to-day conversation, the term "Activity" denotes an Activity Type, Activity Definition, or Activity Execution.

<!-- _Tags: [term](/tags/term), [explanation](/tags/explanation)_ -->

#### [Activity Definition](/activity-definition)

An Activity Definition is the code that defines the constraints of an Activity Task Execution.

<!-- _Tags: [term](/tags/term), [explanation](/tags/explanation)_ -->

#### [Activity Execution](/activity-execution)

An Activity Execution is the full chain of Activity Task Executions.

<!-- _Tags: [term](/tags/term), [explanation](/tags/explanation)_ -->

#### [Activity Heartbeat](/encyclopedia/detecting-activity-failures#activity-heartbeat)

An Activity Heartbeat is a ping from the Worker that is executing the Activity to the Temporal Service.

Each ping informs the Temporal Service that the Activity Execution is making progress and the Worker has not crashed.

<!-- _Tags: [term](/tags/term), [explanation](/tags/explanation)_ -->

#### [Activity Id](/activity-execution#activity-id)

A unique identifier for an Activity Execution.

<!-- _Tags: [term](/tags/term), [explanation](/tags/explanation)_ -->

#### [Activity Task](/tasks#activity-task)

An Activity Task contains the context needed to make an Activity Task Execution.

<!-- _Tags: [term](/tags/term), [explanation](/tags/explanation)_ -->

#### [Activity Task Execution](/tasks#activity-task-execution)

An Activity Task Execution occurs when a Worker uses the context provided from the Activity Task and executes the
Activity Definition.

<!-- _Tags: [term](/tags/term), [explanation](/tags/explanation)_ -->

#### [Activity Type](/activity-definition#activity-type)

An Activity Type is the mapping of a name to an Activity Definition.

<!-- _Tags: [term](/tags/term), [explanation](/tags/explanation)_ -->

#### [Archival](/temporal-service/archival)

Archival is a feature specific to a Self-hosted Temporal Service that automatically backs up Event Histories from
Temporal Service persistence to a custom blob store after the Closed Workflow Execution retention period is reached.

<!-- _Tags: [term](/tags/term), [explanation](/tags/explanation)_ -->

#### [Asynchronous Activity Completion](/activity-execution#asynchronous-activity-completion)

Asynchronous Activity Completion occurs when an external system provides the final result of a computation, started by
an Activity, to the Temporal System.

<!-- _Tags: [term](/tags/term), [explanation](/tags/explanation)_ -->

#### [Audit Logging](/cloud/audit-logs)

Audit Logging is a feature that provides forensic access information for accounts, users, and Namespaces.

<!-- _Tags: [term](/tags/term), [explanation](/tags/explanation), [temporal-cloud](/tags/temporal-cloud), [operations](/tags/operations)_ -->

#### [Authorizer Plugin](/self-hosted-guide/security#authorizer-plugin)

The `Authorizer` plugin contains a single `Authorize` method, which is invoked for each incoming API call. `Authorize`
receives information about the API call, along with the role and permission claims of the caller.

<!-- _Tags: [term](/tags/term)_ -->

#### [Availability Zone](/cloud/high-availability)

An availability zone is a part of the Temporal system where tasks or operations are handled and executed. This design
helps manage workloads and ensure tasks are completed. Temporal Cloud Namespaces are automatically distributed across
three availability zones, offering the 99.9% uptime outlined in our Cloud [SLA](/cloud/sla).

<!-- _Tags: [term](/tags/term), [explanation](/tags/explanation)_ -->

#### [Child Workflow](/child-workflows)

A Child Workflow Execution is a Workflow Execution that is spawned from within another Workflow.

<!-- _Tags: [term](/tags/term), [explanation](/tags/explanation), [child-workflow](/tags/child-workflow)_ -->

#### [Claim Mapper](/self-hosted-guide/security#claim-mapper)

The Claim Mapper component is a pluggable component that extracts Claims from JSON Web Tokens (JWTs).

<!-- _Tags: [term](/tags/term)_ -->

#### [Codec Server](/codec-server)

A Codec Server is an HTTP server that uses your custom Payload Codec to encode and decode your data remotely through
endpoints.

<!-- _Tags: [term](/tags/term)_ -->

#### [Command](/workflow-execution#command)

A Command is a requested action issued by a Worker to the Temporal Service after a Workflow Task Execution completes.

<!-- _Tags: [term](/tags/term), [explanation](/tags/explanation)_ -->

#### [Continue-As-New](/workflow-execution/continue-as-new)

Continue-As-New is the mechanism by which all relevant state is passed to a new Workflow Execution with a fresh Event
History.

<!-- _Tags: [term](/tags/term), [explanation](/tags/explanation), [continue-as-new](/tags/continue-as-new)_ -->

#### [Core SDK](https://temporal.io/blog/why-rust-powers-core-sdk)

The Core SDK is a shared common core library used by several Temporal SDKs. Written in Rust, the Core SDK provides
complex concurrency management and state machine logic among its standout features. Centralizing development enables the
Core SDK to support quick and reliable deployment of new features to existing SDKs, and to more easily add new SDK
languages to the Temporal ecosystem.

<!-- _Tags: [term](/tags/term), [explanation](/tags/explanation), [continue-as-new](/tags/continue-as-new)_ -->

#### [Custom Data Converter](/default-custom-data-converters#custom-data-converter)

A custom Data Converter extends the default Data Converter with custom logic for Payload conversion or Payload
encryption.

<!-- _Tags: [term](/tags/term), [explanation](/tags/explanation)_ -->

#### [Data Converter](/dataconversion)

A Data Converter is a Temporal SDK component that serializes and encodes data entering and exiting a Temporal Service.

<!-- _Tags: [term](/tags/term), [explanation](/tags/explanation)_ -->

#### [Default Data Converter](/default-custom-data-converters#default-data-converter)

The default Data Converter is used by the Temporal SDK to convert objects into bytes using a series of Payload
Converters.

<!-- _Tags: [term](/tags/term), [explanation](/tags/explanation)_ -->

#### [Delay Workflow Execution](/workflow-execution/timers-delays)

Start Delay determines the amount of time to wait before initiating a Workflow Execution. If the Workflow receives a
Signal-With-Start or Update-With-Start during the delay, it dispatches a Workflow Task and the remaining delay is
bypassed.

<!-- _Tags: [term](/tags/term), [explanation](/tags/explanation), [delay-workflow](/tags/delay-workflow)_ -->

#### [Dual Visibility](/dual-visibility)

Dual Visibility is a feature, specific to a Self-hosted Temporal Service, that lets you set a secondary Visibility store
in your Temporal Service to facilitate migrating your Visibility data from one database to another.

<!-- _Tags: [term](/tags/term), [explanation](/tags/explanation), [filtered-lists](/tags/filtered-lists), [visibility](/tags/visibility)_ -->

#### [Durable Execution](/temporal#durable-execution)

Durable Execution in the context of Temporal refers to the ability of a Workflow Execution to maintain its state and
progress even in the face of failures, crashes, or server outages.

<!-- _Tags: [temporal](/tags/temporal), [durable-execution](/tags/durable-execution), [term](/tags/term)_ -->

#### [Dynamic Handler](/dynamic-handler)

Dynamic Handlers are Workflows, Activities, Signals, or Queries that are unnamed and invoked when no other named handler
matches the call from the Server at runtime.

<!-- _Tags: [term](/tags/term), [explanation](/tags/explanation)_ -->

#### [Event](/workflow-execution/event#event)

Events are created by a Temporal Service in response to external occurrences and Commands generated by a Workflow
Execution.

<!-- _Tags: [term](/tags/term), [explanation](/tags/explanation)_ -->

#### [Event History](/workflow-execution/event#event-history)

An append-only log of Events that represents the full state a Workflow Execution.

<!-- _Tags: [term](/tags/term), [explanation](/tags/explanation)_ -->

#### [Failback](/cloud/high-availability)

After Temporal Cloud has resolved an outage or incident involving a failover, a failback process shifts Workflow
Execution processing back to the original region that was active before the incident.

#### [Failover](/cloud/high-availability)

A failover shifts Workflow Execution processing from an active Temporal Namespace region to a standby Temporal Namespace
region during outages or other incidents. Standby Namespace regions use replication to duplicate data and prevent data
loss during failover.

<!-- _Tags: [term](/tags/term), [explanation](/tags/explanation)_ -->

#### [Failure](/temporal#failure)

Temporal Failures are representations of various types of errors that occur in the system.

<!-- _Tags: [term](/tags/term), [explanation](/tags/explanation)_ -->

#### [Failure Converter](/failure-converter)

A Failure Converter converts error objects to proto Failures and back.

<!-- _Tags: [term](/tags/term), [explanation](/tags/explanation)_ -->

#### [Failures](/references/failures)

A Failure is Temporal's representation of various types of errors that occur in the system.

<!-- _Tags: [failure](/tags/failure), [explanation](/tags/explanation), [term](/tags/term)_ -->

#### [Frontend Service](/temporal-service/temporal-server#frontend-service)

The Frontend Service is a stateless gateway service that exposes a strongly typed Proto API. The Frontend Service is
responsible for rate limiting, authorizing, validating, and routing all inbound calls.

<!-- _Tags: [term](/tags/term)_ -->

#### [General Availability](/evaluate/development-production-features/release-stages#general-availability)

Learn more about the General Availability release stage

<!-- _Tags: [product-release-stages](/tags/product-release-stages), [term](/tags/term)_ -->

#### [Global Namespace](/global-namespace)

A Global Namespace is a Namespace that duplicates data from an active [Temporal Service](#temporal-cluster) to a standby
Service using the replication to keep both Namespaces in sync. Global Namespaces are designed to respond to service
issues like network congestion. When service to the primary Cluster is compromised, a [failover](#failover) transfers
control from the active to the standby cluster.

<!-- _Tags: [term](/tags/term), [explanation](/tags/explanation)_ -->

#### [Heartbeat Timeout](/encyclopedia/detecting-activity-failures#heartbeat-timeout)

A Heartbeat Timeout is the maximum time between Activity Heartbeats.

<!-- _Tags: [term](/tags/term), [explanation](/tags/explanation), [timeouts](/tags/timeouts)_ -->

#### [High Availability](/cloud/high-availability/)

High availability ensures that a system remains operational with minimal downtime. It achieves this with redundancy and
failover mechanisms that handle failures, so end-users remain unaware of incidents. Temporal Cloud guarantees this high
availability with its Service Level Agreements ([SLA](/cloud/sla))

<!-- _Tags: [term](/tags/term), [explanation](/tags/explanation), [timeouts](/tags/timeouts)_ -->

#### [High Availability features](/cloud/high-availability#high-availability-features)

High Availability features automatically synchronize your data between a primary Namespace and its replica, keeping them
