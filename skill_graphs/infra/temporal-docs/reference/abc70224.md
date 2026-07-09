
**In the Activity (implementer decides):** Set the `non_retryable` flag when throwing an
[Application Failure](/encyclopedia/application-failures#failure-representation). This enforces the constraint for all
callers. Use this when the Activity implementer knows that the error can never be resolved through retries.

**In the Retry Policy (caller decides):** Add the error type to the Retry Policy's list of
[non-retryable error types](/encyclopedia/retry-policies#non-retryable-errors). This lets different Workflows make
different decisions about the same Activity. Use this when the decision depends on the caller's business logic.

### Preserve retryability when wrapping errors

When an Activity returns an error, the SDK checks the **outermost** error type to determine retryability. If you catch a
non-retryable Application Failure and re-throw it wrapped in a generic language error, the `non_retryable` flag is lost
and the Activity will be retried.

To add context to an error while preserving its retry behavior, wrap it in another Application Failure with the same
`non_retryable` flag. Do not wrap Application Failures in generic language errors.

For a detailed explanation of how the SDK-to-server chain works, see
[The outermost error type determines retryability](/encyclopedia/application-failures#outermost-error-type).

### Use non-retryable errors sparingly

In most cases, let the Retry Policy handle retry limits through [timeouts](/encyclopedia/detecting-activity-failures)
and maximum attempts. Reserve `non_retryable` for cases where retrying is guaranteed to be futile.

For SDK-specific syntax and code examples, see the error handling guide for your language:

- [Python](/develop/python/best-practices/error-handling)
- [Go](/develop/go/best-practices/error-handling)
- [.NET](/develop/dotnet/best-practices/error-handling)
- [Ruby](/develop/ruby/best-practices/error-handling)

## Design Activities for idempotence {/* #idempotence */}

Activities may execute more than once due to retries, so design them to be
[idempotent](/activity-definition#idempotency): producing the same result whether executed once or multiple times.

This is especially important because of an edge case in distributed systems. A Worker can execute an Activity, complete
it, and then crash before reporting the result to the Temporal Service. The Activity is retried even though it
completed, because the Service has no record of the completion.

Use idempotency keys to prevent duplicate operations. Combine the Workflow Run ID and Activity ID for a value that is
consistent across retries but unique across Workflow Executions.

## Implement compensation with the Saga pattern {/* #saga-pattern */}

When a multi-step process fails partway through, previous steps may need to be undone. The
[Saga pattern](/evaluate/use-cases-design-patterns#saga) coordinates a sequence of operations where each step has a
compensating action that reverses its effects. If any step fails, the compensating actions for previously completed
steps execute in reverse order.

For SDK-specific implementations with working code examples, see:

- [Python Saga pattern](/develop/python/best-practices/error-handling#implement-saga-pattern)

---

## Best practices

These guides outline foundational principles and best practices for using Temporal Cloud. It exists to provide a
**validated, opinionated** framework that helps teams that either do not have an enablement plan for or want to evaluate
and refine their use of Temporal.

## Overview

Without clearly defined Temporal standards, organizations often struggle with inconsistent Workflow implementations,
fragmented best practices, and misaligned development approaches. This documentation framework helps developers
establish robust Temporal standards by providing:

- **Proven foundation principles** that have been validated across diverse use cases
- **Standardized implementation patterns** for teams to adopt consistently across projects
- **Confidence in alignment** with Temporal's architectural principles and recommended practices

By following this guidance, developers can define comprehensive Temporal standards that ensure their workflow
orchestration implementations are maintainable, scalable, and aligned with platform best practices from the start.

## Target audience

This section is intended for:

- Developers responsible for building a Temporal Cloud practice within their organization.
- Anyone building tutorials, courses, onboarding paths, or documentation
- Partners or vendors creating Temporal-related learning materials

## Available guides

- **[Managing a Namespace](./managing-namespace.mdx)** Best practices for configuring, managing, and optimizing Temporal
  Namespaces.

- **[Managing Temporal Cloud Access Control](./cloud-access-control.mdx)** Guidelines for implementing proper access
  control and user management in Temporal Cloud.

- **[Security Controls for Temporal Cloud](./security-controls.mdx)** Comprehensive security practices for protecting
  your Temporal Cloud deployment.

- **[Worker Deployment and Performance](./worker.mdx)** Best practices for deploying and optimizing Temporal Workers for
  performance and reliability.

- **[Cost Optimization](./cost-optimization.mdx)** Strategies for optimizing costs associated with workloads running on
  Temporal Cloud while maintaining Workflow reliability and observability.

- **[Pre-Production Testing](./pre-production-testing.mdx)** Experience-driven testing practices covering failure
  injection, load testing, and operational validation.

- **[Knowledge Hub](./knowledge-hub.mdx)** Best practices for building and maintaining an internal Temporal knowledge hub
  that accelerates developer onboarding, reduces platform team support load, and establishes consistent standards.

---

## Knowledge Hub

As organizations scale their Temporal adoption, the use cases become more complex, and it can be difficult to locate all the relevant information you need.
Tribal knowledge gets siloed within teams, leading to inconsistent patterns for Workflow design, error handling, and testing.
This fragmentation leads to an increased burden on support, as well as slower onboarding for new developers.
You may also inadvertently introduce security vulnerabilities or compliance gaps.
To prevent these issues, you can establish an internal Temporal knowledge hub to address common issues that arise when multiple teams
adopt Temporal independently.

This guide covers what belongs in a knowledge hub, how to communicate it, and how to keep it useful over time.
To bootstrap your knowledge hub, use the
[Temporal Platform Hub](https://go.temporal.io/platform-hub) template as a starting point.

## What belongs in your knowledge hub

Although Temporal itself has [thorough documentation](https://docs.temporal.io/), not all of it applies to your organization or your teams' use cases.
The knowledge hub distills the documentation into just the specific information your teams need.
One way to organize the content is according to where developers are in their journey.
The following sample outline shows what sections to include.

### Evaluate

The Evaluation section helps developers understand what Temporal is and whether it fits their problem.
Goals for this section are to increase knowledge hub traffic and decrease the support question rate.
Include the following items in this section:

- **Temporal overview** explains what Temporal is, why your organization chose it, and the business value metrics
  that justify adoption.
- **Decision framework** provides qualifying questions, good and bad use cases, and alternative recommendations so
  developers can determine whether Temporal fits their problem.

### Build

The Build section is aimed at developers who are just getting started with Temporal.
The goal of this section is to give developers a single path from zero to a running Workflow.
Include the following items in this section:

- **Getting started** walks developers through a 30-minute quickstart covering environment setup, a starter template,
  and running a first Workflow locally and on Temporal Cloud. Use an existing Temporal [quickstart](/quickstarts), or build one from your own use case.
- **Learning paths** provides self-paced courses from foundational to advanced topics, tailored by persona, and links
  to [Temporal's free training](https://learn.temporal.io/).

### Ship

The Ship section provides the architecture standards and guardrails developers need to go from a local prototype to a production
deployment.
The goal for this section is to provide reference material developers need to reduce their time to production.
Include the following items in this section:

- **Architecture and standards** documents Namespace conventions, connectivity requirements, and Worker deployment
  standards that every team follows.
- **Cost guidance** explains billable Actions, storage tiers, and cost-saving tips so developers build cost-efficient
  Workflows.
- **Shared responsibility** defines an ownership matrix between Platform and Application teams across IAM,
  infrastructure, development, deployment, observability, and operations.
- **Design patterns** curates Workflow patterns with descriptions and code sample links that developers can adopt
  directly.

### Operate

The Operate section gives developers the tools to self-serve during incidents and find answers without escalating to the Platform team.
The goal of this section is to decrease the number of questions to support.
Include the following items in this section:

- **Troubleshooting and escalation** covers observability tools, runbooks for common issues, escalation paths, SLAs,
  and example alert definitions.
- **Support and FAQs** documents your support tier, ticket submission process, Temporal account contacts, expert-led
  session types, and frequently asked questions.

## Measuring success of your knowledge hub

After you've created your knowledge hub, establish metrics to measure its effectiveness for your organization.
The following table shows example indicators that organizations use to measure the impact of their knowledge hub,
along with realistic before-and-after targets:

| Metric | Before Knowledge Hub | Target | What it tells you |
| :--- | :--- | :--- | :--- |
| **Time to first Workflow** | Days to weeks (developers piece together scattered resources) | Under 30 minutes (developers follow a single getting started guide) | Measures onboarding friction. A short time to first Workflow signals that your getting started guide is effective. |
| **Time to Workflow in production** | Weeks to months (blocked by unclear Namespace provisioning and deployment processes) | Under 2 weeks (developers follow documented self-service provisioning) | Measures the gap between development and delivering value. Long times point to missing documentation and automation opportunities. |
| **Support question rate** | 20-30+ questions per week to the Platform team via Slack | Fewer than 5 per week | Measures self-service resolution. A declining trend shows that developers are finding answers in the knowledge hub instead of asking the Platform team. |
| **Knowledge Hub traffic** | N/A (no centralized resource exists) | Steady or growing page views per month | Identifies which content developers rely on and where gaps remain. Declining traffic on a page may indicate it is outdated; high traffic with high bounce rates may indicate the page is not answering the question. |

These metrics create a feedback loop: measure, identify gaps, improve content, and measure again.

## What doesn't belong in your knowledge hub

A knowledge hub is not a mirror of [Temporal's official documentation](https://docs.temporal.io/).
Avoid duplicating SDK API references, concept explanations, or release notes that Temporal already maintains.
When that content changes, your copy becomes a source of confusion rather than clarity.
Instead, link to the official docs and reserve your knowledge hub for organization-specific decisions, conventions,
and operational procedures that Temporal's public documentation does not cover.

## How to maintain and communicate your knowledge hub

Having a thorough, complete knowledge hub isn't useful if the information becomes stale, or if developers don't know it exists.

### Assign ownership

Designate a Platform team or developer experience team as the owner.
This team is responsible for initial content creation, ongoing maintenance, and reviewing contributions from
application teams.

### Make it discoverable

A knowledge hub that developers can not find is the same as not having one.

- Register a short URL (for example, `go/temporal`) that redirects to the knowledge hub.
- Pin the link in your Temporal-related communication channels (Slack, Microsoft Teams).
- When answering questions in Slack, respond with a link to the relevant knowledge hub page instead of re-explaining
  inline.
  This builds the habit of checking the hub first.

### Review metrics regularly

Track the metrics from [Measuring success of your knowledge hub](#measuring-success-of-your-knowledge-hub) on a regular cadence to identify what is
working and where gaps remain.

Capture every question that reaches the Platform team through Slack or tickets as a candidate for new content.

Solicit contributions from application teams through a lightweight process such as a pull request template.

### Keep content current

- **Review on a cadence**: Review each page at least quarterly.
  Assign a review owner and date to each page so staleness is visible.
- **Tie updates to events**: Update the knowledge hub whenever your organization changes its Temporal architecture,
  updates its deployment tooling, or modifies its shared responsibility model.
- **Prune aggressively**: Remove or archive content that no longer applies.
  Outdated documentation is worse than no documentation because developers follow it and get unexpected results.

## Get started

Start with the [Temporal Platform Hub template](https://go.temporal.io/platform-hub) as your foundation.

---

## Managing Actions per Second (APS) limits in Temporal Cloud

If you're running Workflows on Temporal Cloud, you've probably noticed that each Namespace comes with an Actions Per Second (APS) limit.
But what exactly does that mean, and why does it matter?

In Temporal, an "action" is any operation that modifies Workflow state or interacts with the Temporal service.
Your Namespace's APS limit controls how many of these operations can happen per second across all Workflows within that Namespace.
When the APS limit is reached, Temporal begins to throttle requests.
Depending on the business priority of the Workflow, this may be fine or it may have significant impact.

The difficulty is that APS consumption isn't always intuitive.
A single Workflow Execution generates multiple actions from the moment it starts, and use cases that fit nicely within APS limits at small scale can exhaust those limits as they grow.
Many customers are surprised to find they're hitting APS constraints well before they expected to based on their Workflow count alone.

This guide will help you understand why customers hit APS limits, how to design Workflows that use actions efficiently, and what to do when you're approaching capacity.
When design changes aren't enough, Temporal Cloud offers [Provisioned Capacity Mode](#provisioned-capacity-and-trus) that let you reserve additional capacity using Temporal Resource Units (TRUs) for spiky or unpredictable workloads.

Whether you're just getting started with Temporal Cloud or optimizing an existing deployment, managing APS effectively is key to building scalable, reliable applications.

## Understanding Actions in Temporal

Before we dive into why customers hit APS limits, let's talk about what actions are.

### What Counts as an Action?

In Temporal, actions are the fundamental operations that drive your Workflows forward.
Here's an overview of what counts, with [the full list in our documentation](/cloud/actions).

- Workflows: Starting, completing, resetting. Also starting Child Workflows, as well as Schedules and Timers
- Activities: Starting, retrying, Heartbeating
- Signals, Updates, and Queries

Actions that count toward an APS limit are, with a few exemptions, the same as actions that are billable.
The key insight here is that nearly everything that happens in Temporal--state changes, decision points, interactions--is counted as an action.

### The Action Multiplier Effect

What this means is that when you start a single Workflow, you're not performing just one action as it relates to APS because a Workflow isn’t a single atomic operation, it’s a series of events that Temporal orchestrates.
Each Activity at the start of the Workflow is an Action, so there can be a burst of Activities at the start of a Workflow.
Additionally, there are often business reasons to start multiple Workflows at the same time.

These can all contribute to the multiplier effect.

### The Effect of Rate Limiting

In Temporal Cloud, the effect of rate limiting is increased latency, not lost work.
Workers [might take longer](/cloud/service-availability#throughput) to complete Workflows.

## Common Reasons Customers Hit APS Limits

Now that you understand how actions are defined and how they count toward APS limits, let's look at the patterns that most commonly push customers into APS constraints.

### Bursty Traffic

Most businesses don't operate at constant velocity—they have rhythms, cycles, and spikes.
These patterns can create APS challenges because Temporal Cloud enforces limits at the per-second level.

Common bursty patterns include:

- Calendar-driven spikes: Month-end financial close processes, quarterly reporting Workflows, payroll that runs on the 1st and 15th, scheduled batch jobs that kick off at midnight. These create predictable but intense load concentrations.
- Event-driven surges: Product launches, marketing campaigns, flash sales, breaking news, or seasonal events like Black Friday.
- Recovery scenarios: When a downstream dependency fails and then recovers, you often get a thundering herd effect—hundreds or thousands of Workflows that were waiting all suddenly resume execution simultaneously, creating an artificial spike in APS consumption.
- Geographic/business hours concentration: Global applications often see load follow the sun, with peak activity during business hours in each region. If your business concentrates in specific markets, you'll see daily peaks rather than even 24/7 distribution.
- Retry Storms: when a large number of Workflows get stuck on an Activity, and that Activity is failing, if retry delay is very short, this can cause a spike in Actions.
- Timer Storms: a large number of Workflows all set a Timer for the exact same time--triggering a spike as those Timers fire and then Activities run, causing a lot of actions all at the same time.

These types of processes can result in your Namespace averaging 200 APS over a day, but spiking to 800 APS or more during your peak hour/day/event/etc.

#### How to Mitigate

You can’t change the patterns of how customers interact with your systems, but there are some adjustments you can make to your Workflows to make traffic patterns more consistent, especially for use cases where immediate response isn’t necessary.

These adjustments include:
- Implement application-level queuing or rate limiting to smooth out predictable spikes.
- For scheduled batch operations, stagger start times rather than triggering everything at once--implement jitter in your high-volume [Schedules](/schedule#spec).
- Implement jitter when starting Workflows, such as with [Start Delay](/workflow-execution/timers-delays#delay-workflow-execution).
- Accept rate limiting
- [Provisioned Capacity](/cloud/capacity-modes#provisioned-capacity)

### Cascading Workflows and Fan-Out Patterns

Decomposing complex processes into parent and Child Workflows (or with Nexus) is a common and often appropriate pattern, but the APS costs multiply dramatically with depth and fan-out.

Consider an order fulfillment Workflow that spawns Child Workflows for payment processing, inventory management, shipping, and customer notifications.
Each Child Workflow goes through its full action lifecycle (start, tasks, activities, completion), and all of those actions count toward the APS limits on your Namespace.

This pattern appears frequently in:
- Batch processing: A parent workflow processes a file with 1,000 records, spawning a Child Workflow for each record. Batch processing is also often bursty whenever the batch begins.
- Map-reduce patterns: Data processing Workflows that fan out to process partitions in parallel, then aggregate results.

This challenge additionally compounds when you have multiple levels of nesting--parent Workflows that create children, which create their own children.

#### How to Mitigate

- Evaluate whether Child Workflows are necessary--other options include Activities or Workflows in another Namespace (via Nexus)
- When you do use Child Workflows, limit fan-out size--design a Child Workflow to process its work in batches rather than one Child per work item. [This sample application](https://github.com/temporalio/samples-java/tree/main/core/src/main/java/io/temporal/samples/batch/slidingwindow) shows more detail.
- Consider flattening deeply nested hierarchies into shallower structures.

### Human-in-the-Loop Processes at Scale

Workflows that incorporate human decision-making--approvals, reviews, manual data entry, quality checks--tend to be long-running and interaction-intensive, which creates sustained APS load.

These Workflows can involve Queries from UIs to display current state and pending tasks.

At small scale, this is manageable. But when you're running thousands of them at the same time--like a content moderation queue with pending reviews, or a loan approval system processing applications, or a support ticket system managing thousands of open cases--the cumulative APS load from all of those long-running Workflows adds up.

#### How to Mitigate

- Avoid polling patterns where UIs constantly query Workflow state. Instead, push state changes to a database that UIs can read.

### Real-Time SLAs and Deadline Management

Businesses with strict service level agreements often implement active monitoring and escalation in their Workflows.
This is generally accomplished by setting Timers every [x] minutes to determine if an SLA deadline is approaching, allowing the Workflow to trigger escalations or alerts.

Each of these Timers/monitoring actions affect APS.
When you have thousands of in-flight Workflows all actively monitoring their own SLAs, the background load becomes significant.
You're consuming substantial APS capacity even when Workflows aren't doing their primary work.

#### How to Mitigate

- Use longer monitoring intervals where possible. For example, check SLAs every 30 minutes rather than every 1 minute.
- Where possible, consolidate Timers. Rather than 10 Timers that check 10 tasks, have 1 Timer and then check those 10 tasks.
- Where possible, have an external system signal your Workflow rather than using short-lived Timers to poll.
- For retries, use exponential backoff with reasonable initial intervals.

## Additional Design Patterns
There are some design patterns that can lead to high APS that are consistent across many different types of business use cases.

### Many Small Activities

Consider two approaches to processing 1,000 records:

- Approach A: Create a Workflow that spawns 1,000 separate activities, one per record.
- Approach B: Create a Workflow that spawns 10 activities, each processing 100 records in a batch.

Approach B will clearly result in less APS.
This is a simple example, but this pattern shows up everywhere: processing individual transactions versus batches, sending individual notifications versus bulk operations, or making separate API calls versus batch endpoints.
Each separate Activity adds Action overhead.

#### How to Mitigate

- Consider if you can combine multiple external calls within a single Activity.
- If processing a large amount of data, process it in chunks.
- See [How Many Activities should I use in my Temporal Workflow?](https://temporal.io/blog/how-many-activities-should-i-use-in-my-temporal-workflow) for more information.

### Multiple Use Cases in One Namespace
Often when starting with Temporal, the first use case is implemented in a single Namespace, generally one per logical environment.
When the second Temporal use case is implemented, it runs in the same Namespace, the same for the third, fourth, etc.

An APS limit is set per Namespace, so multiple use cases with multiple traffic patterns in the same Namespace can exhaust this limit quickly.

#### How to Mitigate

Plan for a set of Namespaces (one per environment) per use case. This gives each use case its own APS envelope and
reduces the blast radius when one workload spikes or misbehaves.

If you are deciding whether to split by use case, service, or domain, see
[Managing a Namespace](/best-practices/managing-namespace) for a topology decision framework.

## Provisioned Capacity and TRUs

The strategies above help you design Workflows that use actions efficiently.
But sometimes you need more capacity than the on-demand model provides, especially for spiky or unpredictable workloads.

Temporal Cloud offers two [Capacity Modes](/cloud/capacity-modes):

- **On-Demand mode** (default): Your Namespace automatically scales based on your trailing 7-day usage. This works well for steady, predictable workloads.
