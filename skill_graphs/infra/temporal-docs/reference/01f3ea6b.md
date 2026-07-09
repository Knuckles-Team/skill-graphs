  <RelatedReadItem path="https://docs.temporal.io/cloud/api-keys" text="API Keys documentation" archetype="cloud-guide" />
  <RelatedReadItem path="https://docs.temporal.io/ops?_gl=1*1yf937l*_gcl_au*MTg1MTAxMTEwNC4xNzEzOTcxMjYw*_ga*MTgwODU1MzQyNi4xNzA3NzA4ODIz*_ga_R90Q9SJD3D*MTcyMTI0MTAyNy41MjIuMS4xNzIxMjQ5NTYxLjAuMC4w" text="Cloud Ops API documentation" archetype="cloud-guide" />
  <RelatedReadItem path="/cloud/tcld" text="Temporal Cloud CLI" archetype="cloud-guide" />
  <RelatedReadItem path="/cloud/terraform-provider" text="Terraform Provider for Cloud" archetype="cloud-guide" />
</RelatedReadContainer>

From centralizing cloud operations and automating certificate rotation to streamlining user management and onboarding new teams, Temporal's Cloud Automation features cover a wide range of use cases that enhance efficiency and security across your organization.

---

## Temporal's production deployment features

Transform your Temporal applications into production-ready systems by deploying your application code, Workflows, Activities, and Workers for operational use.
When your application is ready to start serving production traffic, we offer two Temporal Service options:

- **[Choose Temporal Cloud for your Temporal Service](/cloud)**
  Let us handle the Temporal Service operations so you can focus on your applications.
- **[Self-host a Temporal Service](/self-hosted-guide)**
  Deploy your own production level Temporal Service to orchestrate your durable applications.

| Feature                            | Temporal Cloud                                                            | Self-hosted                                      |
| ---------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------ |
| **Multi-tenant**                   | ✅ Up to 100 Namespaces                                                   | ✅ Unlimited Namespaces                          |
| **High availability and failover** | ✅ [Namespaces with High Availability features](/cloud/high-availability) | ✅ Global Namespaces & Multi-Cluster Replication |
| **Application state persistence**  | ✅ 30-90 day Retention                                                    | ✅ Unlimited                                     |
| **Long term state retention**      | ✅ Workflow History Export                                                | ✅ Archival                                      |
| **Community support**              | ✅ Slack, Forum                                                           | ✅ Slack, Forum                                  |
| **Paid support**                   | ✅ Prioritized responses                                                  | ✖️                                                |

---

## Core application - Temporal feature

**Workflows**, **Activities**, and **Workers** form the core parts of a Temporal Application.

**Workflows**: A Workflow defines the overall flow of the application.
You write it in your programming language of choice using the Temporal SDK.
Conceptually, a Workflow specifies a sequence of steps and orchestrates the execution of Activities.

**Activities**: An Activity is a method or function that encapsulates business logic prone to failure (e.g., calling a service that may go down).
The system can automatically retry these Activities upon some failures.
Activities perform a single, well-defined action, such as calling another service, transcoding a media file, or sending an email message.

**Workers**: A Worker executes your Workflow and Activity code.

**Follow one of our tutorials to [Get started](https://learn.temporal.io/getting_started/) learning how to develop Workflows and Activities and run them in Worker Processes.**

Or jump straight to a Temporal SDK feature guide:

<RelatedReadContainer>
  <RelatedReadItem path="/develop/go" text="Go SDK Core application feature guide" archetype="feature-guide" />
  <RelatedReadItem path="/develop/java" text="Java SDK guide" archetype="feature-guide" />
  <RelatedReadItem path="/develop/php" text="PHP SDK Core application feature guide" archetype="feature-guide" />
  <RelatedReadItem path="/develop/python" text="Python SDK Core application feature guide" archetype="feature-guide" />
  <RelatedReadItem path="/develop/typescript" text="TypeScript SDK Core application feature guide" archetype="feature-guide" />
  <RelatedReadItem path="/develop/dotnet" text=".NET SDK Core application feature guide" archetype="feature-guide" />
  <RelatedReadItem path="/develop/ruby" text="Ruby SDK Core application feature guide" archetype="feature-guide" />
</RelatedReadContainer>

For a deep dive into Temporal Workflows, Activities, and Workers, visit the following Temporal Encyclopedia pages or enroll in one of [our courses](https://learn.temporal.io/courses/).

- [Temporal Workflows](/workflows)
- [Temporal Activities](/activities)
- [Temporal Workers](/workers)

---

## Data encryption - Temporal feature

Data Converters in Temporal are SDK components that handle the serialization and encoding of data transmitted and received by a Temporal Client.
Workflow input and output need to be serialized and deserialized so they can be sent as JSON to the Temporal Service.

Temporal provides its own default Data Converter logic, which is not apparent to a user if payloads contain plain text or JSON data.
For enhanced security, you can implement your own encryption standards using a Codec Server.
Temporal's data encryption capabilities ensure the security and confidentiality of your Workflows and provides protection without compromising performance.

Jump straight to a Temporal SDK feature guide.

<RelatedReadContainer>
    <RelatedReadItem path="/develop/go/data-handling/data-encryption" text="Data Encryption using the Go SDK" archetype="feature-guide" />
    <RelatedReadItem path="/develop/java/best-practices/converters-and-encryption" text="Data Encryption using the Java SDK" archetype="feature-guide" />
    <RelatedReadItem path="/develop/python/data-handling/data-encryption" text="Data Encryption using the Python SDK" archetype="feature-guide" />
    <RelatedReadItem path="/develop/typescript/converters-and-encryption" text="Data Encryption using the TypeScript SDK" archetype="feature-guide" />
    <RelatedReadItem path="/develop/dotnet/best-practices/converters-and-encryption" text="Data Encryption using the .NET SDK" archetype="feature-guide" />
    <RelatedReadItem path="/develop/ruby/best-practices/converters-and-encryption" text="Data Encryption using the Ruby SDK" archetype="feature-guide" />
</RelatedReadContainer>

---

## Debugging - Temporal feature

Temporal offers powerful and efficient debugging capabilities for both development and production. These capabilities help developers inspect and troubleshoot Workflows and Activities with precision, ensuring that Workflows perform as expected.

By leveraging detailed event histories and intuitive tooling, you can trace the execution path of Workflows, identify issues, and understand the state of your application at any given point in time.

Jump straight to a Temporal SDK feature guide.

<RelatedReadContainer>
    <RelatedReadItem path="/develop/go/best-practices/debugging" text="Debugging using the Go SDK" archetype="feature-guide" />
    <RelatedReadItem path="/develop/java/best-practices/debugging" text="Debugging using the Java SDK" archetype="feature-guide" />
    <RelatedReadItem path="/develop/php/best-practices/debugging" text="Debugging using the PHP SDK" archetype="feature-guide" />
    <RelatedReadItem path="/develop/python/best-practices/debugging" text="Debugging using the Python SDK" archetype="feature-guide" />
    <RelatedReadItem path="/develop/typescript/best-practices/debugging" text="Debugging using the TypeScript SDK" archetype="feature-guide" />
    <RelatedReadItem path="/develop/dotnet/best-practices/debugging" text="Debugging using the .NET SDK" archetype="feature-guide" />
    <RelatedReadItem path="/develop/ruby/best-practices/debugging" text="Debugging using the Ruby SDK" archetype="feature-guide" />
</RelatedReadContainer>

---

## Failure detection - Temporal feature

In Temporal, timeouts detect application failures.
The system can then automatically mitigate these failures through retries.
Both major application function primitives, **Workflows** and **Activities**, have dedicated **timeout configurations** and can be configured with a **Retry Policy**.

**Follow one of our tutorials to [Get started](https://learn.temporal.io/getting_started/) exploring timeouts and Retry Policies.**

Or jump straight to a Temporal SDK feature guide.

<RelatedReadContainer>
    <RelatedReadItem path="/develop/go/workflows/timeouts" text="Set Workflow timeouts and Retry Policies using the Go SDK" archetype="feature-guide" />
    <RelatedReadItem path="/develop/java/workflows/timeouts" text="Set Workflow timeouts and Retry Policies using the Java SDK" archetype="feature-guide" />
    <RelatedReadItem path="/develop/php/workflows/timeouts" text="Set Workflow timeouts and Retry Policies using the PHP SDK" archetype="feature-guide" />
    <RelatedReadItem path="/develop/python/workflows/timeouts" text="Set Workflow timeouts and Retry Policies using the Python SDK" archetype="feature-guide" />
    <RelatedReadItem path="/develop/typescript/workflows/timeouts" text="Set Workflow timeouts and Retry Policies using the TypeScript SDK" archetype="feature-guide" />
    <RelatedReadItem path="/develop/dotnet/workflows/timeouts" text="Set Workflow timeouts and Retry Policies using the .NET SDK" archetype="feature-guide" />
    <RelatedReadItem path="/develop/ruby/workflows/timeouts" text="Set Workflow timeouts and Retry Policies using the Ruby SDK" archetype="feature-guide" />
</RelatedReadContainer>

<RelatedReadContainer>
  <RelatedReadItem path="/develop/go/activities/timeouts" text="Set Activity timeouts and Retry Policies using the Go SDK" archetype="feature-guide" />
  <RelatedReadItem path="/develop/java/activities/timeouts" text="Set Activity timeouts and Retry Policies using the Java SDK" archetype="feature-guide" />
  <RelatedReadItem path="/develop/php/activities/timeouts" text="Set Activity timeouts and Retry Policies using the PHP SDK" archetype="feature-guide" />
  <RelatedReadItem path="/develop/python/activities/timeouts" text="Set Activity timeouts and Retry Policies using the Python SDK" archetype="feature-guide" />
  <RelatedReadItem path="/develop/typescript/activities/timeouts" text="Set Activity timeouts and Retry Policies using the TypeScript SDK" archetype="feature-guide" />
  <RelatedReadItem path="/develop/dotnet/activities/timeouts" text="Set Activity timeouts and Retry Policies using the .NET SDK" archetype="feature-guide" />
  <RelatedReadItem path="/develop/ruby/activities/timeouts" text="Set Activity timeouts and Retry Policies using the Ruby SDK" archetype="feature-guide" />
</RelatedReadContainer>

For a deep dive into timeouts and Retry Policies visit the following Temporal Encyclopedia pages or enroll in one of [our courses](https://learn.temporal.io/courses/).

<RelatedReadContainer>
    <RelatedReadItem path="/encyclopedia/detecting-workflow-failures" text="Detecting Workflow failures" archetype="encyclopedia" />
    <RelatedReadItem path="/encyclopedia/detecting-activity-failures" text="Detecting Activity failures" archetype="encyclopedia" />
    <RelatedReadItem path="/encyclopedia/retry-policies" text="Retry Policies" archetype="encyclopedia" />
</RelatedReadContainer>

---

## Temporal development and production features

Through a Temporal SDK, Temporal provides a wide range of features that enable developers to build applications that serve a wide range of use cases.

- **[Core application primitives](/evaluate/development-production-features/core-application)**: Develop and run your application with Workflows, Activities, and Workers.
- **[Testing suite](/evaluate/development-production-features/testing-suite)**: Each Temporal SDK comes with a testing suite that enables developers to test their applications as they would any other.
- **[Scheduled Workflows](/evaluate/development-production-features/schedules)**: Start a business process at a specific time or on a given time interval.
- **[Interrupt a Workflow](/evaluate/development-production-features/interrupt-workflow)**: Cancel or terminate a business process (Workflow) that is already in progress and compensate for any steps already taken.
- **Runtime safeguards**: Prevent avoidable errors and issues from executing during runtime.
- **[Failure detection and mitigation](/evaluate/development-production-features/failure-detection)**: Detect failures with timeouts and configure automatic retries to mitigate them.
- **[Temporal Nexus](/evaluate/nexus)**: Connect Temporal Applications across (and within) isolated Namespaces for improved modularity, security, debugging, and fault isolation. Nexus supports cross-team, cross-domain, and multi-region use cases.
- **[Workflow message passing](/evaluate/development-production-features/workflow-message-passing)**: Build responsive applications that react to events at runtime and enable data retrieval from ongoing Workflows.
- **Versioning**: Support multiple versions of your business logic for long-running business processes.
- **[Observability](/evaluate/development-production-features/observability)**: List business processes, view their state, and set up dashboards with metrics.
- **[Debugging](/evaluate/development-production-features/debugging)**: Surface errors and step through code to find issues.
- **[Data encryption](/evaluate/development-production-features/data-encryption)**: Transform data and protect the privacy of the users of your application.
- **[Throughput composability](/evaluate/development-production-features/throughput-composability)**: Breakup business processes by data streams, team ownership, or other organization factors.
- **[Cloud Automation](/evaluate/development-production-features/cloud-automation)**: Simplify cloud management and boost security with Temporal's Cloud Automation.
- **[Low Latency](/evaluate/development-production-features/low-latency)**: Making your applications faster, more performant, and more efficient.
- **[Multi-tenancy](/evaluate/development-production-features/multi-tenancy)**: Enhances efficiency and cost-effectiveness.

For detailed information on Temporal feature release stages and criteria, see this [Product Release Stages Guide](/evaluate/development-production-features/release-stages).

---

## Interrupt a Workflow - Cancellation and Termination

Discover how Temporal enables you to gracefully handle Workflow interruptions through cancellations and terminations.
Understand how to stop a Workflow cleanly with cancellation, allowing for proper cleanup and state management.

For situations where a Workflow is stuck, termination provides an immediate solution, ensuring your applications remain
robust and responsive.

<RelatedReadContainer>
  <RelatedReadItem
    path="/develop/go/workflows/cancellation"
    text="Handling Cancellation and Termination using the Go SDK"
    archetype="feature-guide"
  />
  <RelatedReadItem
    path="/develop/java/workflows/cancellation"
    text="Handling Cancellation and Termination using the Java SDK"
    archetype="feature-guide"
  />
  <RelatedReadItem
    path="/develop/php/workflows/cancellation"
    text="Handling Cancellation and Termination using the PHP SDK"
    archetype="feature-guide"
  />
  <RelatedReadItem
    path="/develop/python/workflows/cancellation"
    text="Handling Cancellation and Termination using the Python SDK"
    archetype="feature-guide"
  />
  <RelatedReadItem
    path="/develop/typescript/workflows/cancellation"
    text="Handling Cancellation and Termination using the TypeScript SDK"
    archetype="feature-guide"
  />
  <RelatedReadItem
    path="/develop/dotnet/workflows/cancellation"
    text="Handling Cancellation and Termination using the .NET SDK"
    archetype="feature-guide"
  />
  <RelatedReadItem
    path="/develop/ruby/workflows/cancellation"
    text="Handling Cancellation and Termination using the Ruby SDK"
    archetype="feature-guide"
  />
</RelatedReadContainer>

---

## Job Queue

## What is a Job Queue?

A job is a single, discrete unit of work that runs asynchronously in the background such as sending an email, processing a webhook, syncing data, or executing a single function reliably.

A job queue is the system that manages these jobs: accepting work, dispatching it to workers, retrying on failure, and providing visibility into what's running and what failed.

**[Standalone Activities](/standalone-activity) are Temporal's job queue.**

They let you use Temporal Activities as background jobs, in addition to using the same Activities as steps inside a Workflow. You write an Activity once and can run it either as a background job or as part of a multi-step Workflow.

Under the hood, Standalone Activities use Temporal's [Task Queues](/task-queue) for dispatching work to Workers.

Temporal provides stronger guarantees, better visibility, and more control than traditional job queues - while remaining cost-effective for high-volume use cases and offering a clean upgrade path to multi-step workflow orchestration.

### Overview

Standalone Activities add the ability to execute any Temporal Activity as a top-level Activity Execution for durable job processing.

#### Unified programming model & worker deployment

- Write an Activity once and use it anywhere - with a unified Activity programming model
- Optional heartbeats support checkpointing for long-running jobs
- Deploy to an Activity Worker once, and invoke standalone or from within a Workflow

#### Execution lifecycle

- Jobs are submitted as Standalone Activity Executions
- Each job is durably persisted with Temporal reliability, so jobs are not lost
- Jobs are scheduled with priority, fairness, deduplication and no head-of-line blocking
- Workers poll task queues and execute Activities (you run your own Workers)
- Temporal ensures retries, timeouts, and exponential backoff policy is enforced

#### Observability & lifecycle controls

- Full job visibility (list, search) with detailed execution state, retry count, errors & results
- OpenMetrics support
- Lifecycle controls: cancel, pause, unpause, reset, terminate
- Manual completion for external integrations & on-call management

## Next steps

Learn more about [Standalone Activity concepts, features, and limitations](/standalone-activity), or jump to a language-specific quickstart:

- [Go SDK - Standalone Activities quickstart and code sample](/develop/go/activities/standalone-activities)
- [Python SDK - Standalone Activities quickstart and code sample](/develop/python/activities/standalone-activities)
- [.NET SDK - Standalone Activities quickstart and code sample](/develop/dotnet/activities/standalone-activities)
- [Java SDK - Standalone Activities quickstart and code sample](/develop/java/activities/standalone-activities)
- [TypeScript SDK - Standalone Activities quickstart and code sample](/develop/typescript/activities/standalone-activities)

---

## Low latency - Temporal feature

Temporal Cloud provides features that significantly reduce latency compared to self-hosted instances, making your applications faster, more performant, and more efficient.
In the world of modern applications, low latency is crucial for ensuring minimal delay in Workflow Executions.
This low-latency architecture ensures rapid Workflow Execution and responsiveness, critical for time-sensitive applications and high-performance systems.

Temporal Cloud's custom persistence layer incorporates three key components that contribute to low latency:

- **Better Sharding:** Distributes load across multiple databases, preventing bottlenecks.
  Enables independent resizing, improving scalability and handling high-traffic events without delay.
- **Write-Ahead Log (WAL):** Aggregates updates before writing to the database, reducing write latency.
  Stores writes in an append-only format, reducing latency and database size by batching updates before writing to the database.
- **Tiered Storage of Workflow Event History:** Offloads completed Workflow Event Histories, improving database efficiency.

Temporal Cloud provides lower latency, making it suitable for latency-sensitive, large-scale, or business-critical applications.

<RelatedReadContainer>
  <RelatedReadItem path="https://temporal.io/blog/exploring-temporal-cloud-automation-features" text="Exploring Temporal Cloud Automation Features" archetype="blog-post" />
  <RelatedReadItem path="https://temporal.io/blog/high-availability-and-disaster-recovery-with-temporal-cloud" text="High Availability and Disaster Recovery with Temporal Cloud" archetype="blog-post" />
  <RelatedReadItem path="https://temporal.io/blog/higher-throughput-and-lower-latency-temporal-clouds-custom-persistence-layer" text="Higher throughput and lower latency: Temporal Cloud’s custom persistence layer" archetype="blog-post" />
  <RelatedReadItem path="https://temporal.io/blog/how-to-migrate-your-self-hosted-service-to-temporal-cloud" text="How to Migrate Your Self-Hosted Service to Temporal Cloud" archetype="blog-post" />
  <RelatedReadItem path="https://temporal.io/blog/scaling-temporal-the-basics" text="Scaling your self-hosted instance" archetype="blog-post" />
  <RelatedReadItem path="https://temporal.io/blog/benchmarking-latency-temporal-cloud-vs-self-hosted-temporal" text="Benchmarking Latency: Temporal Cloud vs. Self-Hosted Temporal" archetype="blog-post" />
  <RelatedReadItem path="https://docs.temporal.io/cloud/service-availability#latency" text="Temporal Cloud’s Latency SLO" archetype="cloud-guide" />
  <RelatedReadItem path="https://www.youtube.com/watch?v=SQv9ot-jB6o&list=PLl9kRkvFJrlREHL7fiEKBWTp5QuFeYS2r&index=5" text="Replay Conference Talk: Custom Persistence Layer" archetype="replay-talk" />
</RelatedReadContainer>

---

## Multi-tenancy - Temporal feature

Multi-tenancy in Temporal operates at two levels:

## Namespace isolation

[Namespaces](/namespaces) are Temporal's unit of isolation, providing logical separation for multi-tenant deployments in both open source Temporal and Temporal Cloud.

### Open source Temporal

Namespaces in self-hosted Temporal provide:

- **Workflow ID uniqueness**: Temporal guarantees unique Workflow IDs within a Namespace. Different Namespaces can have Workflows with the same ID without conflict.
- **Resource isolation**: Traffic from one Namespace does not impact other Namespaces on the same Temporal Service.
- **Configuration boundaries**: Settings like [Retention Period](/temporal-service/temporal-server#retention-period) and [Archival](/temporal-service/archival) destination are configured per Namespace.
- **Access control**: Use a custom [Authorizer](/self-hosted-guide/security#authorization) on your Frontend Service to restrict who can access each Namespace.
- **Inter-namespace communication**: Use [Nexus](/evaluate/nexus) for controlled communication between Namespaces.

### Temporal Cloud

Temporal Cloud builds on these capabilities with additional isolation guarantees:

- **Independent authentication** via [API keys](/cloud/api-keys) or [mTLS certificates](/cloud/certificates)
- **Built-in [role-based access controls](/cloud/manage-access/roles-and-permissions#namespace-level-permissions)** without custom Authorizer configuration
- **Separate [rate limits](/cloud/limits#namespace-level)** to prevent noisy neighbor problems
- **[High availability replication](/cloud/high-availability)** across regions

<RelatedReadContainer>
  <RelatedReadItem path="/cloud/security#namespace-isolation" text="Namespace Isolation Details" archetype="cloud-guide" />
  <RelatedReadItem path="/cloud/pricing" text="Temporal Cloud Pricing" archetype="cloud-guide" />
</RelatedReadContainer>

## Application multi-tenancy

Many organizations use Temporal to power their own multi-tenant SaaS applications, isolating their customers' workloads using Task Queues, Search Attributes, and Worker design patterns.

See the [multi-tenant application patterns guide](/production-deployment/multi-tenant-patterns) for detailed recommendations on architecting multi-tenant applications with Temporal.

---

## Observability - Temporal feature

Temporal's observability feature helps you track the state of your Workflows in real-time, providing tools for detailed metrics, tracing, comprehensive logging, and visibility into your application state.

Monitor performance, trace Activity and Workflow Executions, debug, and filter Workflow Executions to gain deeper insights into your Workflows.

**Key Components of Temporal's Observability and Visibility**

- **Metrics**: Detailed performance metrics to track the health and efficiency of your Temporal Service and Workflows.
- **Tracing**: End-to-end tracing of Workflow and Activity Executions to understand the flow and timing of operations.
- **Logging**: Comprehensive logging capabilities for debugging and auditing purposes.
- **Search Attributes**: Custom attributes that can be used to enhance searchability and provide additional context to Workflow Executions.
- **Web UI**: A user-friendly interface for visualizing and interacting with your Workflows and Temporal Service state.

**Benefits of Temporal's Observability and Visibility Features**

- **Real-time Monitoring**: Track the state and progress of your Workflows as they execute.
