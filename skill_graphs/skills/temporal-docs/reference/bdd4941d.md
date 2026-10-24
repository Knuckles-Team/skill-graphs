- **Performance Optimization**: Identify bottlenecks and optimize your Workflow and Activity implementations.
- **Effective Debugging**: Quickly locate and diagnose issues in your Temporal applications.
- **Compliance and Auditing**: Maintain detailed records of all Workflow executions for compliance and auditing purposes.
- **Operational Insights**: Gain a deep understanding of your application's behavior and usage patterns.
- **Scalability Management**: Monitor and manage the scalability of your Temporal Service effectively.

Jump straight into the Temporal SDK feature guide.

<RelatedReadContainer>
    <RelatedReadItem path="/develop/go/platform/observability" text="Observability using the Go SDK" archetype="feature-guide" />
    <RelatedReadItem path="/develop/dotnet/platform/observability" text="Observability using the .NET SDK" archetype="feature-guide" />
    <RelatedReadItem path="/develop/java/platform/observability" text="Observability using the Java SDK" archetype="feature-guide" />
    <RelatedReadItem path="/develop/php/platform/observability" text="Observability using the PHP SDK" archetype="feature-guide" />
    <RelatedReadItem path="/develop/python/platform/observability" text="Observability using the Python SDK" archetype="feature-guide" />
    <RelatedReadItem path="/develop/typescript/platform/observability" text="Observability using the TypeScript SDK" archetype="feature-guide" />
    <RelatedReadItem path="/develop/ruby/platform/observability" text="Observability using the Ruby SDK" archetype="feature-guide" />
</RelatedReadContainer>

---

## Temporal product release stages guide

:::tip CHANGELOG
To stay up-to-date with the latest feature changes, visit the [changelog](https://temporal.io/change-log).
:::

This Product Release Stages Guide provides an understanding of how Temporal features are released. It describes and lists the criteria for each release stage, so that you can make informed decisions about the adoption of each new feature.

Product Release Guide Expectations:

|                                 | Pre-release                                                        | Public Preview                                                                              | General Availability                             |
| ------------------------------- | ------------------------------------------------------------------ | ------------------------------------------------------------------------------------------- | ------------------------------------------------ |
| **Features access**             | Self-hosted Temporal users: Everyone; Temporal Cloud: Invite only. | Everyone. Temporal Cloud may limit the number of users being onboarded to ensure stability. | Everyone.                                        |
| **Feature completeness**        | Limited functionality.                                             | Core functionality is complete.                                                             | Mature and feature complete.                     |
| **API stability**               | Experimental; API is subject to change.                            | API breaking changes are kept to a minimum.                                                 | API is stable.                                   |
| **Feature region Availability** | Limited regions.                                                   | Most regions.                                                                               | All [regions](/cloud/regions).                   |
| **Feature support**             | Community and engineering team.                                    | [Formal support](/cloud/support#support-ticket).                                            | [Formal support](/cloud/support#support-ticket). |
| **Feature recommended usage**   | Experimental.                                                      | Production use cases.                                                                       | Production usage.                                |
| **Feature Cloud pricing**       | No additional cost.                                                | Pricing changes are kept to a minimum.                                                      | Pricing is stable.                               |
| **Feature Interoperability**    | Limited.                                                           | Features are compatible with each other, unless otherwise stated.                           | Features are compatible with each other.         |

## Pre-release {/* #pre-release */}

**Access:** Most Pre-release features are released in the open source Temporal software and are publicly available.
However, some features which are explicit to hosting Temporal Services, such as [API Keys](/cloud/api-keys), may be specific to Temporal Cloud.

In Temporal Cloud, Pre-release features are invite-only: Temporal will work directly with a group of existing Temporal Cloud customers to be part of testing of each Pre-release feature.
These customers are invited to provide feedback to the Temporal team.

**Classification:** New features in Pre-release may not be fully mature and may have bugs.
Users acknowledge and agree that Pre-release features are provided on an “as-is” basis, and that they are provided without any indemnification, support, warranties, or representation of any kind.

**Feedback:** Feedback is highly encouraged and important for guiding Temporal feature development.
We encourage you to share your experience so that you can influence the future direction of Temporal.

**Availability:** Temporal may modify features before they become Generally Available, or may even decide to remove them.
This means there is no guarantee that a new feature will become Generally Available.
A Pre-release feature can be deprecated at any time.

Pre-release features may be disabled by default, and can be enabled via configuration.
Temporal Cloud customers can contact the Temporal account team or [Temporal Support Team](/cloud/support#support-ticket) to gain Pre-release access.

## Public Preview {/* #public-preview */}

**Access:** New features in Public preview are available to everyone.

**Classification:** Features in public preview may undergo further development and testing before they are made Generally Available.
These features are being refined and are recommended for production usage.

**Feedback:** Temporal users are invited to share feedback via the [Community Slack](http://t.mp/slack), by reaching out directly to the Temporal team at product@temporal.io, or by creating issues in the relevant [GitHub repository](https://github.com/temporalio).
Temporal also encourages Temporal Cloud users to submit feedback via [support ticket](/cloud/support#support-ticket).
This feedback will assist in guiding the improvements for General Availability.

**Availability:** New Features in Public Preview may evolve.
The APIs may undergo changes; however, Temporal's goal is to maintain backward compatibility.

## General Availability {/* #general-availability */}

**Access:** Features in General Availability are available to everyone.

**Classification:** The feature is now fully developed, tested, and available for use without further anticipated changes.

**Feedback:** Temporal users are invited to share feedback via the [Community Slack](http://t.mp/slack), by reaching out directly to the Temporal team at product@temporal.io, or by creating issues in the relevant [GitHub repository](https://github.com/temporalio).

**Availability:** Features in General Availability are released with stable APIs and recommended for production use with a committed SLA.

:::info Exceptions

There may be exceptions for different features, but this is the typical expectation.
Any variation will be documented.

:::

---

## Schedules - Temporal feature

Temporal Schedules is a feature that allows you to "schedule" Temporal Workflows at specified times or intervals, adjusting for peak use.

It offers a flexible way to automate and manage your Temporal Workflows, ensuring your business processes run smoothly and efficiently especially when handling time-sensitive tasks.

1. **Automate Repetitive Tasks:**
   Schedules automate repetitive tasks, reducing manual intervention and ensuring timely execution of business processes.
2. **Enhanced Workflow Control and Observability:**
   Gain complete control over your automation processes. With Schedules, you can create, backfill, delete, describe, list, pause, trigger, and update Workflow Executions.
3. **Flexible Timing:**
   Schedule Workflow Executions to run at regular intervals or specific future times, ensuring they execute precisely when needed.
4. **Reliable and Scalable:**
   Designed for reliability and scalability, Temporal Schedules handle the complexities of distributed systems while ensuring your Workflows run as intended, even during failures.
5. **Eliminate External Dependencies:**
   Schedules remove the need to integrate external scheduling systems.

Jump straight to a Temporal SDK feature guide.

<RelatedReadContainer>
    <RelatedReadItem path="/develop/go/workflows/schedules" text="Schedules using the Go SDK" archetype="feature-guide" />
    <RelatedReadItem path="/develop/java/workflows/schedules" text="Schedules using the Java SDK" archetype="feature-guide" />
    <RelatedReadItem path="/develop/php/workflows/schedules" text="Schedules using the PHP SDK" archetype="feature-guide" />
    <RelatedReadItem path="/develop/python/workflows/schedules" text="Schedules using the Python SDK" archetype="feature-guide" />
    <RelatedReadItem path="/develop/typescript/workflows/schedules" text="Schedules using the TypeScript SDK" archetype="feature-guide" />
    <RelatedReadItem path="/develop/dotnet/workflows/schedules" text="Schedules using the .NET SDK" archetype="feature-guide" />
    <RelatedReadItem path="/develop/ruby/workflows/schedules" text="Schedules using the Ruby SDK" archetype="feature-guide" />
</RelatedReadContainer>

---

## Serverless Workers Interactive Demo

<ReleaseNoteHeader type="prerelease">
  To request access during Pre-release, create a
  [support ticket](/cloud/support#support-ticket) or contact your account team. APIs are experimental and may be subject
  to backwards-incompatible changes. [Sign up for updates](https://temporal.io/pages/serverless-workers-updates) to be
  notified when Serverless Workers reach Public Preview.
</ReleaseNoteHeader>

Serverless Workers let you run Temporal Workers on serverless compute like AWS Lambda. There are no long-lived processes
to provision or scale. Temporal Cloud invokes your Worker when Tasks arrive, and the Worker shuts down when the work is
done.

Use the interactive demo below to explore how the configuration options affect the generated Worker code, deployment
script, and CLI commands. Click "Start Workflow" to simulate the end-to-end Serverless Worker invocation flow.

<ServerlessWorkerDemo />

---

## Next steps

- [Serverless Workers](/serverless-workers) for concepts, autoscaling, and lifecycle details.
- [Deploy a Serverless Worker](/production-deployment/worker-deployments/serverless-workers) for the full end-to-end
  deployment guide.

---

## Serverless Workers(Serverless-workers)

Serverless Workers let you run Temporal Workers on serverless compute platforms like AWS Lambda. There are no servers to
provision, no clusters to scale, and no idle compute to pay for. Temporal invokes the Worker when Tasks arrive, and the
Worker shuts down when the Tasks are done.

Serverless Workers use the same Temporal SDKs as traditional long-lived Workers. You register Workflows and Activities
the same way. The difference is in the lifecycle: instead of running a long-lived process, Temporal invokes the
Serverless Worker on demand when Tasks arrive. The Worker starts, polls for available Tasks, processes them, and exits
when the Task is done.

For a deeper look at how Serverless invocation works under the hood, see [Serverless Workers](/serverless-workers) in
the encyclopedia.

## Why use Serverless Workers?

Serverless Workers are a good fit for many workloads. They offer several advantages compared to long-lived Workers on
dedicated compute.

### Reduce operational overhead

Long-lived Workers require you to provision infrastructure, configure scaling policies, manage deployments, and monitor
host-level health. Serverless Workers reduce this burden by offloading invocation and scaling to Temporal and the
compute provider. You still deploy the function and configure the compute provider, but there is no always-on
infrastructure to manage and no autoscaling policies to tune.

Worker management is one of the most common sources of support questions for Temporal users. Serverless Workers offer a
prescriptive deployment path that reduces the operational surface area and lets you focus on writing Workflows instead
of managing infrastructure.

### Get started faster

Running a long-lived Worker requires choosing a hosting strategy, configuring compute resources, and setting up
deployment pipelines before you can execute your first Workflow in production.

With Serverless Workers, deploying a Worker is as simple as deploying a function. Package your Worker code, deploy it to
your serverless provider, and configure the connection to Temporal. There is no need to set up Kubernetes, manage
container orchestration, or design a scaling strategy.

### Scale automatically

Serverless compute providers handle scaling natively. When Task volume increases, the provider spins up additional
function instances. When traffic drops, instances scale down. When there is no work, there is no compute running.

This automatic scaling is especially useful for bursty, event-driven workloads where traffic patterns are unpredictable
or highly variable.

### Pay only for what you use

Long-lived Workers run continuously, whether or not there is work to process. Serverless Workers run only when Tasks are
available. For workloads with low or intermittent volume, this pay-per-invocation model can significantly reduce compute
costs.

## When to use Serverless Workers

Serverless Workers are a good fit when:

- **Workloads are bursty or event-driven.** Order processing, notifications, webhook handlers, and similar workloads
  that experience spiky traffic benefit from automatic scaling without over-provisioning.
- **Traffic is low or intermittent.** If Workers spend most of their time idle, Serverless Workers eliminate the cost of
  always-on compute.
- **You want a simpler getting-started path.** Deploying a function is simpler than setting up a container orchestration
  platform. Serverless Workers reduce the steps between writing Worker code and running your first Workflow.
- **Your organization has standardized on serverless.** Teams that already run services on Lambda, Cloud Run, or similar
  platforms can run Temporal Workers using the same deployment patterns and tooling.
- **You serve multiple tenants with infrequent workloads.** Platforms that run Workflows on behalf of many users or
  customers can avoid running dedicated Workers per tenant.

Serverless Workers may not be ideal when:

- **Activities are long-running and cannot be interrupted.** Some serverless platforms enforce execution time limits.
  For example, AWS Lambda has a 15-minute execution limit. Activities that run longer than the provider's timeout and
  cannot be broken into smaller steps need a different hosting strategy or a provider with longer limits (such as Cloud
  Run). Long-running Workflows are not affected because Workflows can span multiple invocations.
- **Workloads require sustained high throughput.** For consistently high-volume Task Queues, long-lived Workers on
  dedicated compute may be more cost-effective and performant.
- **You need persistent connections.** Some features require a persistent connection between the Worker and Temporal,
  which serverless invocations do not maintain.

## How Serverless Workers compare to long-lived Workers

|                | Long-lived Worker                                          | Serverless Worker                                                                                  |
| -------------- | ---------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| **Lifecycle**  | Long-lived process that runs continuously.                 | Invoked on demand. Starts and stops per invocation.                                                |
| **Scaling**    | You manage scaling (Kubernetes HPA, instance count, etc.). | Temporal invokes additional instances as needed, within the compute provider's concurrency limits. |
| **Connection** | Persistent connection to Temporal.                         | Fresh connection on each invocation.                                                               |

## Supported providers

| Provider   | Status    |
| ---------- | --------- |
| AWS Lambda | Available |

## Next steps

- [Interactive demo](/evaluate/serverless-workers/demo) to explore the configuration and invocation flow.
- [How Serverless Workers work](/serverless-workers) for a deeper look at the invocation lifecycle, compute providers,
  and architecture.
- [Deploy a Serverless Worker](/production-deployment/worker-deployments/serverless-workers) for the end-to-end
  deployment guide.
- [Serverless Workers - Go SDK](/develop/go/workers/serverless-workers/aws-lambda) for SDK-specific configuration and
  defaults.

---

## Temporal Nexus - Temporal feature

As Temporal adoption grows across teams, organizations partition their applications into isolated Namespaces for security and fault isolation.
Nexus bridges these boundaries, connecting Temporal applications across Namespaces, regions, and clouds with built-in durable execution, observability, and access control.
Each team retains ownership of their own Namespace while sharing capabilities through clean service contracts.
Watch the [Nexus overview](https://www.youtube.com/watch?v=tJ1OwSFokOg&t=117s) for a walkthrough.

## Before Nexus
Connecting Namespaces was possible, but painful. It required extensive configuration, added operational overhead, and often depended on additional infrastructure

- **Child Workflows** - Limited to the same Namespace. Cross-Namespace use leaks underlying implementation details, requiring callers to manage the target Namespace, Task Queue, and Workflow options.
- **Activity wrappers** - Require per-target mTLS clients, adding configuration and certificate management overhead. Often over-permissioned, lack built-in observability, and require error-prone boilerplate for async results.
- **Extra gateway infrastructure** - Not durable, difficult to debug across services, and adds another service to manage and patch.

Nexus replaces all of these with a clean service contract between caller and handler, reducing code, and providing first-class observability.

## Benefits

Connect Temporal Applications across teams, domains, regions, and clouds with:

- **Stronger security posture** - Built-in access controls for service contracts instead of broad Namespace access. Each team controls their own Namespace, Workers, and deployment lifecycle.
- **Higher reliability** - Durable, atomic handoffs eliminate lost requests. Faults are isolated so misbehaving Workers don't impact other teams.
- **Easier to build and maintain** - Less boilerplate code, custom retry and deduplication logic, and ongoing maintenance. Teams focus on business logic instead of infrastructure.
- **Scalable platform patterns** - Enables cross-team and cross-region orchestration without centralizing ownership.
- **Lower barriers to cross-team use cases** - Makes it easy to incrementally build and adopt shared services, with built-in discoverability.
- **Compliance and data isolation** - Isolated Namespaces support auditability, data residency requirements, and dedicated encryption and access controls for sensitive data (PCI, PII).

## What customers are using Nexus for

- **Duolingo** - Self-service infrastructure ([Case study](https://temporal.io/resources/case-studies/duolingo-temporal-nexus) | [Webinar](https://www.youtube.com/watch?v=tJ1OwSFokOg&t=524s))
- **Netflix** - Infrastructure orchestration ([Replay talk](https://www.youtube.com/watch?v=izR9dQ_eIe4&t=470s) | [Webinar](https://www.youtube.com/watch?v=At1FfqGQiu0&t=1295s))
- **Miro** - Cross-region data migration ([Replay talk](https://youtu.be/YLmFR-IAC3M?feature=shared&t=1488))

## Should I use Nexus?

Use the following decision tree to help determine if Nexus is right for your use case:

    <CaptionedImage
      src="/diagrams/nexusadoptionlight.svg"
      srcDark="/diagrams/nexusadoptiondark.svg"
      alt="Should I use Nexus? Decision tree"
    />

## Get started {/* #learn-more */}

Join the [#nexus](https://temporalio.slack.com/archives/C07LQN0JK9B) channel in [Temporal Slack](https://t.mp/slack) to connect with the Nexus community.

<RelatedReadContainer>
  <RelatedReadItem path="/nexus" text="Nexus concepts and architecture" archetype="encyclopedia" />
  <RelatedReadItem path="/develop/go/nexus" text="Go SDK - Nexus quick start" archetype="feature-guide" />
  <RelatedReadItem path="/develop/java/nexus" text="Java SDK - Nexus quick start" archetype="feature-guide" />
  <RelatedReadItem path="/develop/python/nexus" text="Python SDK - Nexus quick start" archetype="feature-guide" />
  <RelatedReadItem path="/develop/typescript/nexus" text="TypeScript SDK - Nexus quick start" archetype="feature-guide" />
  <RelatedReadItem path="/develop/dotnet/nexus" text=".NET SDK - Nexus quick start" archetype="feature-guide" />
  <RelatedReadItem path="/cloud/nexus" text="Temporal Cloud" archetype="feature-guide" />
  <RelatedReadItem path="/production-deployment/self-hosted-guide/nexus" text="Self-hosted deployment" archetype="feature-guide" />
</RelatedReadContainer>

---

## Temporal Testing Suite - Temporal feature

In the context of Temporal, you can create these types of automated tests:

1. End-to-end: Running a Temporal Server and Worker with all its Workflows and Activities; starting and interacting with Workflows from a Client.
2. Integration: Anything between end-to-end and unit testing.
   Running Activities with mocked Context and other SDK imports (and usually network requests).
   Running Workers with mock Activities, and using a Client to start Workflows.
   Running Workflows with mocked SDK imports.
3. Unit: Running a piece of Workflow or Activity code and mocking any code it calls.

Jump straight to a Temporal SDK feature guide.

<RelatedReadContainer>
    <RelatedReadItem path="/develop/go/best-practices/testing-suite" text="Testing using the Go SDK" archetype="feature-guide" />
    <RelatedReadItem path="/develop/java/best-practices/testing-suite" text="Testing using the Java SDK" archetype="feature-guide" />
    <RelatedReadItem path="/develop/php/best-practices/testing-suite" text="Testing using the PHP SDK" archetype="feature-guide" />
    <RelatedReadItem path="/develop/python/best-practices/testing-suite" text="Testing using the Python SDK" archetype="feature-guide" />
    <RelatedReadItem path="/develop/typescript/best-practices/testing-suite" text="Testing using the TypeScript SDK" archetype="feature-guide" />
    <RelatedReadItem path="/develop/dotnet/best-practices/testing-suite" text="Testing using the .NET SDK" archetype="feature-guide" />
    <RelatedReadItem path="/develop/ruby/best-practices/testing-suite" text="Testing using the Ruby SDK" archetype="feature-guide" />
</RelatedReadContainer>

---

## Child Workflows - Temporal feature

In Temporal, **Child Workflows** enable applications to achieve another level of composability when it comes to throughput.

The following example scenarios are a few reasons to use this feature:

- To create a separate service that can be invoked from multiple other services or applications.
- To partition a step into smaller chunks.
- To manage a dedicated resource and guarantee uniqueness.
- To execute logic periodically without overwhelming the parent business process.

See the SDK feature guides for implementation details:

<RelatedReadContainer>
  <RelatedReadItem path="/develop/go/workflows/child-workflows" text="Go SDK Child Workflow feature guide" archetype="feature-guide" />
  <RelatedReadItem path="/develop/java/workflows/child-workflows" text="Java SDK Child Workflow feature guide" archetype="feature-guide" />
  <RelatedReadItem path="/develop/php/workflows/child-workflows" text="PHP SDK Child Workflow feature guide" archetype="feature-guide" />
  <RelatedReadItem path="/develop/python/workflows/child-workflows" text="Python SDK Child Workflow feature guide" archetype="feature-guide" />
  <RelatedReadItem path="/develop/typescript/workflows/child-workflows" text="TypeScript SDK Child Workflow feature guide" archetype="feature-guide" />
  <RelatedReadItem path="/develop/dotnet/workflows/child-workflows" text=".NET SDK Child Workflow feature guide" archetype="feature-guide" />
  <RelatedReadItem path="/develop/ruby/workflows/child-workflows" text="Ruby SDK Child Workflow feature guide" archetype="feature-guide" />
  <RelatedReadItem path="/develop/rust/workflows/child-workflows" text="Rust SDK Child Workflow feature guide" archetype="feature-guide" />
</RelatedReadContainer>

For a deep dive into Child Workflows see the [Child Workflows Encyclopedia page](/child-workflows).
