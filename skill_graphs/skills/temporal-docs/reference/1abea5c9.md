
- Cluster A comes with initial version: 1
- Cluster B comes with initial version: 2
- Shared version increment: 10

T = 0: adding event with event ID == 1 & version == 1

View in both Cluster A & B

```
| -------- | --------------- | --------------- | ------- |
| Events   | Version History |
| -------- | --------------- | --------------- | ------- |
| Event ID | Event Version   | Event ID        | Version |
| -------- | -------------   | --------------- | ------- |
| 1        | 1               | 1               | 1       |
| -------- | -------------   | --------------- | ------- |
```

T = 1: adding event with event ID == 2 & version == 1

View in both Cluster A & B

```
| -------- | --------------- | --------------- | ------- |
| Events   | Version History |
| -------- | --------------- | --------------- | ------- |
| Event ID | Event Version   | Event ID        | Version |
| -------- | -------------   | --------------- | ------- |
| 1        | 1               | 2               | 1       |
| 2        | 1               |                 |         |
| -------- | -------------   | --------------- | ------- |
```

T = 2: adding event with event ID == 3 & version == 1

View in both Cluster A & B

```
| -------- | --------------- | --------------- | ------- |
| Events   | Version History |
| -------- | --------------- | --------------- | ------- |
| Event ID | Event Version   | Event ID        | Version |
| -------- | -------------   | --------------- | ------- |
| 1        | 1               | 3               | 1       |
| 2        | 1               |                 |         |
| 3        | 1               |                 |         |
| -------- | -------------   | --------------- | ------- |
```

T = 3: Namespace failover triggered, Namespace version is now 2
adding event with event ID == 4 & version == 2

View in both Cluster A & B

```
| -------- | --------------- | --------------- | ------- |
| Events   | Version History |
| -------- | --------------- | --------------- | ------- |
| Event ID | Event Version   | Event ID        | Version |
| -------- | -------------   | --------------- | ------- |
| 1        | 1               | 3               | 1       |
| 2        | 1               | 4               | 2       |
| 3        | 1               |                 |         |
| 4        | 2               |                 |         |
| -------- | -------------   | --------------- | ------- |
```

T = 4: adding event with event ID == 5 & version == 2

View in both Cluster A & B

```
| -------- | --------------- | --------------- | ------- |
| Events   | Version History |
| -------- | --------------- | --------------- | ------- |
| Event ID | Event Version   | Event ID        | Version |
| -------- | -------------   | --------------- | ------- |
| 1        | 1               | 3               | 1       |
| 2        | 1               | 5               | 2       |
| 3        | 1               |                 |         |
| 4        | 2               |                 |         |
| 5        | 2               |                 |         |
| -------- | -------------   | --------------- | ------- |
```

</details>

Since Temporal is AP, during failover (change of active Temporal Service Namespace), there can exist cases where more than one Cluster can modify a Workflow Execution, causing divergence of Workflow Execution History. Below shows how the version history will look like under such conditions.

<details>
    <summary>
      Version history example (with data conflict)
    </summary>

Below, shows version history of the same Workflow Execution in 2 different Clusters.

- Cluster A comes with initial version: 1
- Cluster B comes with initial version: 2
- Cluster C comes with initial version: 3
- Shared version increment: 10

T = 0:

View in both Cluster B & C

```
| -------- | --------------- | --------------- | ------- |
| Events   | Version History |
| -------- | --------------- | --------------- | ------- |
| Event ID | Event Version   | Event ID        | Version |
| -------- | -------------   | --------------- | ------- |
| 1        | 1               | 2               | 1       |
| 2        | 1               | 3               | 2       |
| 3        | 2               |                 |         |
| -------- | -------------   | --------------- | ------- |
```

T = 1: adding event with event ID == 4 & version == 2 in Cluster B

```
| -------- | --------------- | --------------- | ------- |
| Events   | Version History |
| -------- | --------------- | --------------- | ------- |
| Event ID | Event Version   | Event ID        | Version |
| -------- | -------------   | --------------- | ------- |
| 1        | 1               | 2               | 1       |
| 2        | 1               | 4               | 2       |
| 3        | 2               |                 |         |
| 4        | 2               |                 |         |
| -------- | -------------   | --------------- | ------- |
```

T = 1: namespace failover to Cluster C, adding event with event ID == 4 & version == 3 in Cluster C

```
| -------- | --------------- | --------------- | ------- |
| Events   | Version History |
| -------- | --------------- | --------------- | ------- |
| Event ID | Event Version   | Event ID        | Version |
| -------- | -------------   | --------------- | ------- |
| 1        | 1               | 2               | 1       |
| 2        | 1               | 3               | 2       |
| 3        | 2               | 4               | 3       |
| 4        | 3               |                 |         |
| -------- | -------------   | --------------- | ------- |
```

T = 2: replication task from Cluster C arrives in Cluster B

Note: below are a tree structures

```
| ------------- | ------------- |
| Events        |
| ------------- | ------------- |
| Event ID      | Event Version |
| ------------- | ------------- |
| 1             | 1             |
| 2             | 1             |
| 3             | 2             |
| --------      | ------------- |
|               |
|               |
| --------      | ------------- |  | -------- | ------------- |
| Event ID      | Event Version |  | Event ID | Event Version |
| --------      | ------------- |  | -------- | ------------- |
| 4             | 2             |  | 4        | 3             |
| --------      | ------------- |  | -------- | ------------- |

| --------------- | ------------------- |
| Version History |
| --------------- | ------------------- |
| Event ID        | Version             |
| --------------- | -------             |
| 2               | 1                   |
| 3               | 2                   |
| --------------- | ------------------- |
|                 |
|                 |
| --------------- | -------             |  | --------------- | ------- |
| Event ID        | Version             |  | Event ID        | Version |
| --------------- | -------             |  | --------------- | ------- |
| 4               | 2                   |  | 4               | 3       |
| --------------- | -------             |  | --------------- | ------- |
```

T = 2: replication task from Cluster B arrives in Cluster C, same as above

</details>

## Conflict resolution

When a Workflow Execution History diverges, proper conflict resolution is applied.

In Multi-cluster Replication, Workflow Execution History Events are modeled as a tree, as shown in the second example in [Version History](#version-history).

Workflow Execution Histories that diverge will have more than one history branch.
Among all history branches, the history branch with the highest version is considered the `current branch` and the Workflow Execution's mutable state is a summary of the current branch.
Whenever there is a switch between Workflow Execution History branches, a complete rebuild of the Workflow Execution's mutable state will occur.

Temporal Multi-Cluster Replication relies on asynchronous replication of Events across Clusters, so in the case of a failover it is possible to have an Activity Task dispatched again to the newly active Cluster due to a replication task lag.
This also means that whenever a Workflow Execution is updated after a failover by the new Cluster, any previous replication tasks for that Execution cannot be applied.
This results in loss of some progress made by the Workflow Execution in the previous active Cluster.
During such conflict resolution, Temporal re-injects any external Events like Signals in the new Event History before discarding replication tasks.
Even though some progress could roll back during failovers, Temporal provides the guarantee that Workflow Executions won't get stuck and will continue to make forward progress.

Activity Execution completions are not forwarded across Clusters.
Any outstanding Activities will eventually time out based on the configuration.
Your application should have retry logic in place so that the Activity gets retried and dispatched again to a Worker after the failover to the new Cluster.
Handling this is similar to handling an Activity Task timeout caused by a Worker restarting.

## Zombie Workflows

There is an existing contract that for any Namespace and Workflow Id combination, there can be at most one run (Namespace + Workflow Id + Run Id) open / executing.

Multi-cluster Replication aims to keep the Workflow Execution History as up-to-date as possible among all participating Clusters.

Due to the nature of Multi-cluster Replication (for example, Workflow Execution History events are replicated asynchronously) different Runs (same Namespace and Workflow Id) can arrive at the target Cluster at different times, sometimes out of order, as shown below:

```
+-----------+        +----------------+        +-----------+
| Cluster A |        | Network Layer  |        | Cluster B |
+-----------+        +----------------+        +-----------+
      |                       |                        |
      | Run 1 Replication     |                        |
      |---------------------> |                        |
      |                       |                        |
      | Run 2 Replication     |                        |
      |---------------------> |                        |
      |                       |                        |
      |                       | Run 2 Replication      |
      |                       |--------------------->  |
      |                       |                        |
      |                       | Run 1 Replication      |
      |                       |--------------------->  |
      |                       |                        |
```

Because Run 2 appears in Cluster B first, Run 1 cannot be replicated as "runnable" due to the rule `at most one Run open` (see above), thus the "zombie" Workflow Execution state is introduced.
A "zombie" state is one in which a Workflow Execution which cannot be actively mutated by a Cluster (assuming the corresponding Namespace is active in this Cluster). A zombie Workflow Execution can only be changed by a replication Task.

Run 1 will be replicated similar to Run 2, except when Run 1's execution will become a "zombie" before Run 1 reaches completion.

## Workflow Task processing

In the context of Multi-cluster Replication, a Workflow Execution's mutable state is an entity which tracks all pending tasks.
Prior to the introduction of Multi-cluster Replication, Workflow Execution History entries (events) are from a single branch, and the Temporal Server will only append new entries (events) to the Workflow Execution History.

After the introduction of Multi-cluster Replication, it is possible that a Workflow Execution can have multiple Workflow Execution History branches.
Tasks generated according to one history branch may become invalidated by switching history branches during conflict resolution.

Example:

T = 0: task A is generated according to Event Id: 4, version: 2

```
| -------- | ------------- |
| Events   |
| -------- | ------------- |
| Event ID | Event Version |
| -------- | ------------- |
| 1        | 1             |
| 2        | 1             |
| 3        | 2             |
| -------- | ------------- |
|          |
|          |
| -------- | ------------- |
| Event ID | Event Version |
| -------- | ------------- |
| 4        | 2             | <-- task A belongs to this event |
| -------- | ------------- |
```

T = 1: conflict resolution happens, Workflow Execution's mutable state is rebuilt and history Event Id: 4, version: 3 is written down to persistence

```
| --------- | ------------- |
| Events    |
| --------- | ------------- |
| Event ID  | Event Version |
| --------  | ------------- |
| 1         | 1             |
| 2         | 1             |
| 3         | 2             |
| --------  | ------------- |
|           |
| --------- | ------------- |
|           |
| --------  | ------------- |                                  | -------- | ------------- |
| Event ID  | Event Version |                                  | Event ID | Event Version |
| --------  | ------------- |                                  | -------- | ------------- |
| 4         | 2             | <-- task A belongs to this event | 4        | 3             | <-- current branch / mutable state
| --------  | ------------- |                                  | -------- | ------------- |
```

T = 2: task A is loaded.

At this time, due to the rebuild of a Workflow Execution's mutable state (conflict resolution), Task A is no longer relevant (Task A's corresponding Event belongs to non-current branch).
Task processing logic will verify both the Event Id and version of the Task against a corresponding Workflow Execution's mutable state, then discard task A.

---

## Persistence

This page discusses the following:

- [Persistence](#persistence)
- [Dependency Versions](#dependency-versions)

## What is Persistence? {/* #persistence */}

The Temporal Persistence store is a database used by the [Temporal Server](/temporal-service/temporal-server) to persist events generated and processed in your Temporal Service and SDK.

A Temporal Service's only required dependency for basic operation is the Persistence database.
Multiple types of databases are supported.

<Components.CaptionedImage
src="/diagrams/temporal-database.svg"
title="Persistence"
/>

The database stores the following types of data:

- Tasks: Tasks to be dispatched.
- State of Workflow Executions:
  - Execution table: A capture of the mutable state of Workflow Executions.
  - History table: An append-only log of Workflow Execution History Events.
- Namespace metadata: Metadata of each Namespace in the Temporal Service.
- [Visibility](/temporal-service/visibility) data: Enables operations like "show all running Workflow Executions".
  For production environments, we recommend using Elasticsearch as your Visibility store.

An Elasticsearch database must be configured in a self-hosted Temporal Service to enable [advanced Visibility](/visibility#advanced-visibility) on Temporal Server versions 1.19.1 and earlier.

With Temporal Server version 1.20 and later, advanced Visibility features are available on SQL databases like MySQL (version 8.0.17 and later), PostgreSQL (version 12 and later), SQLite (v3.31.0 and later), and Elasticsearch.

### Dependency versions

Temporal tests compatibility by spanning the minimum and maximum stable major versions for each supported database.
The following versions are used in our test pipelines and actively tested before we release any version of Temporal:

- **Cassandra v3.11 and v4.0**
- **PostgreSQL 13.18, 14.15, 15.10 and 16.6**
- **MySQL v5.7 and v8.0** (specifically 8.0.19+ due to a bug)

You can verify supported databases in the [Temporal Server release notes](https://github.com/temporalio/temporal/releases).

- Because Temporal Server primarily relies on core database functionality, we do not expect compatibility to break often.
  {/* Temporal has no opinions on database upgrade paths; as long as you can upgrade your database according to each project's specifications, Temporal should work with any version within supported ranges. */}
- We do not run tests with vendors like Vitess and CockroachDB.
- Temporal also supports SQLite v3.x persistence, but this is meant only for development and testing, not production usage.

---

## Temporal Server

This page discusses the following:

- [Frontend Service](#frontend-service)
- [History Service](#history-service)
- [History Shard](#history-shard)
- [Matching Service](#matching-service)
- [Worker Service](#worker-service)
- [Retention Period](#retention-period)

## What is the Temporal Server? {/* #temporal-server */}

The Temporal Server consists of four independently scalable services:

- Frontend gateway: for rate limiting, routing, authorizing.
- History subsystem: maintains data (mutable state, queues, and timers).
- Matching subsystem: hosts Task Queues for dispatching.
- Worker Service: for internal background Workflows.

For example, a real-life production deployment can have 5 Frontend, 15 History, 17 Matching, and 3 Worker Services per Temporal Service.

The Temporal Server services can run independently or be grouped together into shared processes on one or more physical or virtual machines.
For live (production) environments, we recommend that each service runs independently, because each one has different scaling requirements and troubleshooting becomes easier.
The History, Matching, and Worker Services can scale horizontally within a Temporal Service.
The Frontend Service scales differently than the others because it has no sharding or partitioning; it is just stateless.

Each service is aware of the others, including scaled instances, through a membership protocol via [Ringpop](https://github.com/temporalio/ringpop-go).

### Versions and support

:::tip

We release new versions of the Temporal SDKs and Temporal Server software independently of one another.
That said, All SDK versions support all server versions.

To take advantage of bug fixes, performance improvements, and new features, please upgrade both SDK and servers to the latest versions on a regular cadence.

:::

All Temporal Server releases abide by the [Semantic Versioning Specification](https://semver.org/).

We support upgrade paths from every version beginning with Temporal v1.7.0.
For details on upgrading your Temporal Service, see [Upgrade Server](/self-hosted-guide/upgrade-server#upgrade-server).

We provide maintenance support for previously published minor and major versions by continuing to release critical bug fixes related to security, the prevention of data loss, and reliability, whenever they are found.

We aim to publish incremental upgrade guides for each minor and major version, which include specifics about dependency upgrades that we have tested for (such as Cassandra 3.0 -> 3.11).

We offer maintenance support of the last three **minor** versions after a release and do not plan to "backport" patches beyond that.

We offer maintenance support of **major** versions for at least 12 months after a GA release, and we provide at least 6 months' notice before EOL/deprecating support.

**Dependencies**

Temporal offers official support for, and is tested against, dependencies with the exact versions described in the `go.mod` file of the corresponding release tag.
(For example, [v1.5.1](https://github.com/temporalio/temporal/tree/v1.5.1) dependencies are documented in [the go.mod for v1.5.1](https://github.com/temporalio/temporal/blob/v1.5.1/go.mod).)

## What is a Frontend Service? {/* #frontend-service */}

The Frontend Service is a stateless gateway service that exposes a strongly typed [Proto API](https://github.com/temporalio/api/blob/main/temporal/api/workflowservice/v1/service.proto).
The Frontend Service is responsible for rate limiting, authorizing, validating, and routing all inbound calls.

<CaptionedImage
    src="/diagrams/temporal-frontend-service.svg"
    title="Frontend Service"
/>

Types of inbound calls include the following:

- [Namespace](/namespaces) CRUD
- External events
- Worker polls
- [Visibility](/temporal-service/visibility) requests
- [Temporal CLI](/cli) (the Temporal CLI) operations
- Calls from a remote Temporal Service related to [Multi-Cluster Replication](/temporal-service/multi-cluster-replication)

Every inbound request related to a Workflow Execution must have a Workflow Id, which is hashed for routing purposes.
The Frontend Service has access to the hash rings that maintain service membership information, including how many nodes (instances of each service) are in the Temporal Service.

Inbound call rate limiting is applied per host and per namespace.

The Frontend Service talks to the Matching Service, History Service, Worker Service, the database, and Elasticsearch (if in use).

- It uses the grpcPort 7233 to host the service handler.
- It uses port 6933 for membership-related communication.

Ports are configurable in the Temporal Service configuration.

## What is a History Service? {/* #history-service */}

The History Service is responsible for persisting Workflow Execution state to the Event History.
When the Workflow Execution is able to progress, the History Service adds a Task with the Workflow's updated history to the Task Queue.
From there, a Worker can poll for work, receive this updated history, and resume execution.

<CaptionedImage
    src="/diagrams/temporal-history-service.svg"
    title="Block diagram of how the History Service relates to the other services of the Temporal Server and to the Temporal Service"
/>

The total number of History Service processes can be between 1 and the total number of [History Shards](#history-shard).
An individual History Service can support many History Shards.
Temporal recommends starting at a ratio of 1 History Service process for every 500 History Shards.

Although the total number of History Shards remains static for the life of the Temporal Service, the number of History Service processes can change.

The History Service talks to the Matching Service and the database.

- It uses grpcPort 7234 to host the service handler.
- It uses port 6934 for membership-related communication.

Ports are configurable in the Temporal Service configuration.

### What is a History Shard? {/* #history-shard */}

A History Shard is an important unit within a Temporal Service by which concurrent Workflow Execution throughput can be scaled.

Each History Shard maps to a single persistence partition.
A History Shard assumes that only one concurrent operation can be within a partition at a time.
In essence, the number of History Shards represents the number of concurrent database operations that can occur for a Temporal Service.
This means that the number of History Shards in a Temporal Service plays a significant role in the performance of your Temporal Application.

Before integrating a database, the total number of History Shards for the Temporal Service must be chosen and set in the Temporal Service's configuration (see [persistence](/references/configuration#persistence)).
After the Shard count is configured and the database integrated, the total number of History Shards for the Temporal Service cannot be changed.

In theory, a Temporal Service can operate with an unlimited number of History Shards, but each History Shard adds compute overhead to the Temporal Service.
The Temporal Service has operated successfully using anywhere from 1 to 128K History Shards, with each Shard responsible for tens of thousands of Workflow Executions.
One Shard is useful only in small scale setups designed for testing, while 128k Shards is useful only in very large scale production environments.
The correct number of History Shards for any given Temporal Service depends entirely on the Temporal Application that it is supporting and the type of database.

A History Shard is represented as a hashed integer.
Each Workflow Execution is automatically assigned to a History Shard.
The assignment algorithm hashes Workflow Execution metadata such as Workflow Id and Namespace and uses that value to match a History Shard.

Each History Shard maintains the Workflow Execution Event History, Workflow Execution mutable state, and the following internal Task Queues:

- Internal Transfer Task Queue: Transfers internal tasks to the Matching Service.
  Whenever a new Workflow Task needs to be scheduled, the History Service's Transfer Task Queue Processor transactionally dispatches it to the Matching Service.
- Internal Timer Task Queue: Durably persists Timers.
- Internal Replicator Task Queue: Asynchronously replicates Workflow Executions from active Clusters to other passive Clusters.
  (Relies on the experimental Multi-Cluster feature.)
- Internal Visibility Task Queue: Pushes data to the [Advanced Visibility](/visibility#advanced-visibility) index.

## What is a Matching Service? {/* #matching-service */}

The Matching Service is responsible for hosting user-facing [Task Queues](/task-queue) for Task dispatching.

<CaptionedImage
    src="/diagrams/temporal-matching-service.svg"
    title="Matching Service"
/>

It is responsible for matching Workers to Tasks and routing new Tasks to the appropriate queue.
This service can scale internally by having multiple instances.

It talks to the Frontend Service, History Service, and the database.

- It uses grpcPort 7235 to host the service handler.
- It uses port 6935 for membership related communication.

Ports are configurable in the Temporal Service configuration.

## What is a Worker Service? {/* #worker-service */}
