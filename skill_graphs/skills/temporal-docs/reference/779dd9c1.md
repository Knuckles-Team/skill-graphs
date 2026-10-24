- **Provisioned mode**: You reserve capacity by adding Temporal Resource Units (TRUs), giving you guaranteed headroom for traffic spikes.

See [Capacity Modes](/cloud/capacity-modes) for complete details on TRUs, available increments, and how to manage capacity via UI, CLI, or API.

### Choosing the Right Approach

Use Provisioned capacity when the on-demand model can't respond quickly enough:

| Scenario | Pattern | Recommendation |
|----------|---------|----------------|
| **Planned spikes** | Promotions, holiday traffic, product launches | Pre-provision TRUs before the event starts |
| **Unplanned spikes** | Sudden traffic surges, viral events | React instantly via UI/CLI/API when you see throttling |
| **Load testing** | Validating new services at scale | Provision TRUs for the test, deprovision after |
| **Batch jobs** | Scheduled high-throughput jobs | Automate TRU scaling via API around job schedules |
| **Migrations** | Onboarding a new workload faster than on-demand adjusts | Bridge with TRUs for approximately 7 days while the on-demand envelope catches up |

:::note
When switching back to on-demand mode, your APS limit resets to the running average from the last 7 days.
Plan for this if your workload is sensitive to the transition.
:::

### Cost Optimization Tips

See [Capacity Modes Pricing](/cloud/pricing#capacity-modes-pricing) for billing details. To minimize costs:

- Provision only when you need extra capacity
- Deprovision promptly after spikes end
- For predictable patterns, automate scaling to minimize time in provisioned mode

### Automation Best Practices

Since you understand your workload patterns better than any auto-scaling system, consider building your own TRU automation:

- **Use the [Cloud Ops API](/ops), [Terraform Provider](/cloud/terraform-provider), or [tcld CLI](/cloud/tcld)** to programmatically scale capacity based on your application's signals
- **Set utilization thresholds**: For example, scale up when hitting 70-80% of your limit, scale down after sustained low usage
- **Schedule capacity changes**: Use [Temporal Schedules](/schedule) or Workflows to increase TRUs before known events
- **React to leading indicators**: If your application has upstream signals (incoming order queue depth, marketing campaign start), use those to trigger capacity changes proactively

## Knowing if You're Hitting APS Limits

In addition to understanding the patterns that can affect APS limits on a Temporal Namespace, it's also important to know if you're approaching (or exceeding) these limits.
Temporal Cloud provides several metrics that, if tracked, will tell you if you're being rate limited due to APS.
See the documentation on [detecting resource exhaustion](/cloud/service-health#rps-aps-rate-limits) for an explanation of those metrics as well as a sample Grafana dashboard that shows how they could be viewed.

### Monitoring for TRU Decisions

If you're considering Provisioned capacity, set up monitoring to understand your usage patterns:

- **Use [OpenMetrics](/cloud/metrics/openmetrics)**: For real-time visibility into APS consumption, integrate Temporal Cloud metrics with your observability stack
- **Track APS usage vs. limits**: Monitor `temporal_cloud_v0_resource_exhausted_errors` to detect throttling events
- **Set alerts at 70-80% utilization**: This gives you time to provision TRUs before hitting limits
- **Analyze historical patterns**: Understanding your traffic patterns helps you decide between reactive TRU provisioning and proactive automation

## Key Takeaways

Let's recap the main reasons customers hit APS limits and how to address them:

| Reason for Hitting APS Limits | How to Address It |
|-------------------------------|-------------------|
| Bursty Traffic                | Implement application-level queuing or rate limiting to smooth spike, stagger start times for scheduled batch operations. |
| Cascading Workflows and Fan-Out Patterns | Evaluate if Child Workflows are necessary (consider activities or another Namespace), limit fan-out size by processing work in batches within a Child Workflow, consider flattening deeply nested hierarchies. |
| Human-in-the-Loop Processes at Scale | Design long-running Workflows to minimize sustained APS load from interaction (by avoiding polling where UIs constantly Query state and using Signals only for key human inputs). |
| Many small activities         | Consider if you can combine multiple external calls within a single Activity. If processing a large amount of data, process it in chunks. |
| Multiple use cases in one Namespace | Plan for a set of Namespaces (one per environment) per use case. |
| Planned traffic spikes        | Pre-provision TRUs before the event, then deprovision after. |
| Unpredictable spikes requiring instant response | Switch to Provisioned mode for self-service capacity scaling via UI, CLI, or API. |
| Load testing at scale         | Provision TRUs for the test duration, deprovision when complete. |
| New workload onboarding       | Bridge with TRUs while the on-demand envelope adjusts (approximately 7 days). |

## General guidance

When designing Temporal Workflows with an eye toward APS limits, ask yourself the following questions:
- How many actions will a single execution of this Workflow consume?
- How many Workflows will typically be running at the same time?
- What happens to APS consumption when the number of Actions * number of active Workflows scales to 100x current volume?
- Are there natural opportunities to combine operations: combine activities, or process chunks of data together?
- Am I polling when I could be using Signals?
- Does this Workflow need to run continuously, or can it be event-driven?

A few hours spent optimizing Workflow design can save you from capacity crunches, emergency limit increases, and potentially significant cost increases down the road.

---

## Namespace best practices

:::info Applies to both open source and Temporal Cloud
This page covers namespace best practices that apply to **both** open source Temporal and Temporal Cloud.
Platform-specific guidance is clearly labeled throughout.

For reference documentation, see:
- [Namespace concepts](/namespaces)
- [Managing Namespaces (open source)](/self-hosted-guide/namespaces)
- [Namespaces (Temporal Cloud)](/cloud/namespaces)
:::

A [Namespace](/namespaces) is a unit of isolation within the Temporal Platform.
It ensures that Workflow Executions, Task Queues, and resources are logically separated, preventing conflicts and enabling safe multi-tenant usage.

Use this page to decide how many Namespaces you need and where to draw boundaries between environments, services,
domains, and tenants. For Cloud-specific namespace mechanics such as creation, tagging, and gRPC endpoints, see
[Namespaces (Temporal Cloud)](/cloud/namespaces).

Related guidance:
- [Managing Temporal Cloud access control](/best-practices/cloud-access-control)
- [Multi-tenant application patterns](/production-deployment/multi-tenant-patterns)
- [Managing Actions per Second (APS) limits in Temporal Cloud](/best-practices/managing-aps-limits)

## Naming Conventions

### Use lowercase and hyphens

Use lowercase letters and hyphens (`-`) as separators in Namespace names.

- **Temporal Cloud**: Namespace names are case-insensitive, so `MyNamespace` and `mynamespace` refer to the same Namespace.
- **Open source**: Namespace names are case-sensitive, so `MyNamespace` and `mynamespace` are different Namespaces.

To avoid confusion across environments, always use lowercase.

**Example**: `payment-checkout-prd`

### Follow a consistent naming pattern

Use a pattern like `<use-case>-<domain>-<environment>` to name Namespaces:

| Component | Max Length | Examples |
|-----------|------------|----------|
| Use case | 10 chars | `payments`, `fulfill`, `orders` |
| Domain | 10 chars | `checkout`, `notify`, `inventory` |
| Environment | 3 chars | `dev`, `stg`, `prd` |

**Examples**: `payments-checkout-dev`, `fulfill-notify-prd`, `orders-inventory-stg`

**Why this pattern?**
- Simple and easy to understand
- Clearly separates environments
- Groups related services under domains
- Allows platform teams to implement chargeback to application teams
- Namespace-level limits are isolated between different services and environments

:::tip Temporal Cloud
Cloud Namespace names are limited to [39 characters](/cloud/namespaces#temporal-cloud-namespace-name).
If you need to include region, use short codes (e.g., `aps1`, `use1`).
:::

## Organizational Patterns

### Choose your Namespace boundary intentionally

Start with the smallest number of Namespaces that gives you clear ownership and safe isolation.
In Temporal Cloud, a Namespace boundary affects:

- [APS limits](/cloud/limits#actions-per-second) and rate limiting
- access control and credential scope
- blast radius for misconfigured or overloaded Workers
- observability boundaries for dashboards and alerts
- operational overhead for provisioning, tagging, and lifecycle management

Use the following decision table as a starting point:

| If you need... | Prefer... | Why |
|---|---|---|
| Basic environment isolation for a single application or use case | Namespace per use case and environment | This is the simplest pattern and works well for most initial deployments |
| Separate operational ownership for services within the same use case | Namespace per use case, service, and environment | This isolates credentials, limits, and operational changes per service |
| Stronger boundaries across teams, domains, or business capabilities | Namespace per use case, domain, and environment | This reduces blast radius and lets teams own their own Namespace contracts |
| Tenant-specific credentials, rate limits, or compliance boundaries | Namespace per tenant | Use this only for a small number of high-value tenants because of the operational overhead |

As a default, start with one Namespace per use case and environment. Split later when APS pressure, security
requirements, ownership boundaries, or troubleshooting needs justify the extra operational cost.

### Pattern 1: Namespace per use case and environment

For simple configurations without multiple services or team boundaries.

**Naming convention**: `<use-case>-<environment>`

**Example**: `payments-prd`, `orders-dev`

Choose this pattern when:

- one team owns the use case
- environments need clean separation
- workload volume and criticality do not yet require further isolation

### Pattern 2: Namespace per use case, service, and environment

When multiple services that are part of the same use case communicate externally to Temporal via API (HTTP/gRPC).

**Naming convention**: `<use-case>-<service>-<environment>`

**Example**: `payments-gateway-prd`, `payments-processor-prd`

Choose this pattern when:

- services need separate credentials or access policies
- one service can exhaust APS or operational limits independently of the others
- teams want separate ownership of deployment, alerting, or on-call boundaries

### Pattern 3: Namespace per use case, domain, and environment

When multiple services need to communicate with each other, use [Temporal Nexus](/nexus) to connect Workflows across Namespace boundaries.
This provides better security, fault isolation, and modularity than sharing a Namespace.

**Naming convention**: `<use-case>-<domain>-<environment>`

**Example**: `payments-checkout-prd`, `payments-refunds-prd`

Choose this pattern when:

- multiple teams or domains need independent release cadence and ownership
- failures in one domain should not affect the others
- you want a stronger permission boundary between capabilities
- you plan to expose cross-Namespace contracts through Nexus

For systems without Nexus, services can communicate via [Signals](/sending-messages#sending-signals) or [Child Workflows](/child-workflows) within the same Namespace.

:::note Workflow ID uniqueness
When multiple teams share a Namespace, prefix each Workflow ID with a service-specific string to ensure uniqueness.
Task Queue names must also be unique within the Namespace.
:::

### Pattern 4: Namespace per tenant

Use a separate [Namespace](/namespaces) per tenant only when each tenant needs a true isolation boundary.

This is usually appropriate only for a small number of high-value tenants that require:

- dedicated credentials and access control
- tenant-specific rate limits or capacity decisions
- strict compliance or data-isolation boundaries
- independent debugging, alerting, and operational ownership

For most SaaS use cases, a shared Namespace with per-tenant [Task Queues](/task-queue) is simpler and more scalable.
See [Multi-tenant application patterns](/production-deployment/multi-tenant-patterns) for those designs.

### What should cause you to split a Namespace later?

Revisit your topology when one or more of the following becomes true:

- one workload is consuming enough APS that it regularly threatens others in the same Namespace
- one team needs tighter access controls or dedicated credentials
- production troubleshooting requires clearer dashboards, alerts, or ownership boundaries
- one application or domain is business-critical enough that its blast radius must be reduced
- a tenant or regulated workload needs stronger separation than Task Queue isolation can provide

Splitting a Namespace increases safety, but it also adds overhead for provisioning, tagging, credentials, and cross-Namespace coordination.
Use [Nexus](/nexus) where possible instead of sharing Temporal primitives across team or domain boundaries.

## Production Safeguards

### Use an Authorizer (open source only) {/* #authorizer */}

Use a custom [Authorizer](/self-hosted-guide/security#authorizer-plugin) on your Frontend Service to set restrictions on who can create, update, or deprecate Namespaces.

If an Authorizer is not set, Temporal uses the `nopAuthority` authorizer that unconditionally allows all API calls.

On Temporal Cloud, [role-based access controls](/cloud/manage-access/roles-and-permissions#namespace-level-permissions) provide namespace-level authorization without custom configuration.

### Enable deletion protection (Temporal Cloud only) {/* #deletion-protection */}

[Enable deletion protection](/cloud/namespaces#delete-protection) for production Namespaces to prevent accidental deletion.

### Enable High Availability (Temporal Cloud only) {/* #high-availability */}

For business-critical use cases with strict uptime requirements, enable [High Availability features](/cloud/high-availability) for a [99.99% contractual SLA](/cloud/high-availability#high-availability-features).

### Use Infrastructure as Code (Temporal Cloud only) {/* #terraform */}

Use the [Temporal Cloud Terraform provider](/cloud/terraform-provider) to manage Namespaces.
If Terraform isn't suitable, scripting against the [Cloud Ops API](/ops) or [tcld](/cloud/tcld) is a good alternative.

This provides:
- Documentation of each Namespace's purpose and owners
- Prevention of infrastructure drift
- Version-controlled configuration changes

Use `prevent_destroy = true` in your Terraform configuration to prevent accidental Namespace deletion via Terraform.
This is separate from [Temporal Cloud deletion protection](/cloud/namespaces#delete-protection), which prevents deletion through any interface.

**Reference**: [Example Terraform configuration](https://github.com/kawofong/temporal-terraform)

## Tagging (Temporal Cloud only) {/* #tagging */}

[Tags](/cloud/namespaces#tag-a-namespace) are key-value metadata pairs that help organize, track, and manage Namespaces.

Tags complement your naming convention by adding metadata that doesn't fit in the Namespace name.
While the name captures use case, domain, and environment, tags can capture additional dimensions like team ownership, data sensitivity, or business criticality.

### Recommended tag categories

| Tag Key | Purpose | Examples |
|---------|---------|----------|
| `environment` | Deployment stage | `dev`, `staging`, `production` |
| `team` | Owning team | `platform`, `payments`, `identity` |
| `division` | Business unit | `engineering`, `finance`, `ops` |
| `criticality` | Business importance | `high`, `medium`, `low` |
| `data-sensitivity` | Data classification | `pii`, `pci`, `public` |
| `latency-sensitivity` | Performance tier | `realtime`, `batch`, `async` |

For tag structure, limits, and management instructions, see [How to tag a Namespace](/cloud/namespaces#tag-a-namespace).

## SDK Client Configuration

Set Namespaces in your SDK Client to isolate your Workflow Executions.
If you do not set a Namespace, all Workflow Executions started using the Client will be associated with the `default` Namespace.

You must register a Namespace before setting it in your Client.

For configuration details, see:
- [Namespace concepts](/namespaces)
- [Namespaces (Temporal Cloud)](/cloud/namespaces#access-namespaces)

---

## Pre-production testing

This guide collects practical, experience-driven testing practices for teams running Temporal applications.
The goal is not just to verify that things fail and recover, but to build confidence that *recovery*, *correctness*, *consistency*, and *operability* hold under real-world conditions.

The scenarios below assume familiarity with Temporal concepts such as [Namespaces](/namespaces), [Workers](/workers), [Task Queues](/task-queue), [History shards](/temporal-service/temporal-server#history-shard), [Timers](/workflow-execution/timers-delays), and [Workflow replay](/workflow-execution#replay).
Start with [Understanding Temporal](/evaluate/understanding-temporal#durable-execution) if you need background.

Before starting any load testing in Temporal Cloud, we recommend connecting with your Temporal Account team and our Developer Success Engineering team.

## Guiding principles

Before diving into specific experiments, keep these principles in mind:

- **Failure is normal**: Temporal is designed to survive failure and issues, but *your application logic* must be too.
- **Partial failure is often harder to deal with than total failure**: Systems that are "mostly working" expose the most flaws.
- **Recovery paths deserve as much testing as steady state**: Analyze recovering application behavior as much as you analyze failing behavior.
- **Build observability before you break things**: Ensure metrics, logs, and visibility tools are in place before injecting failures.
- **Testing is a continual process**: Testing is never finished. Testing is a practice.

## Worker testing

**Relevant best practices**: [Worker deployment and performance](/best-practices/worker), appropriate timeouts, managing Worker shutdown, idempotency

- [Worker shutdown](/encyclopedia/workers/worker-shutdown)

### Kill all Workers, then restart them

**What to test**

Abruptly terminate all Workers processing a Task Queue, then restart them.

**Why it matters**

- Validates at-least-once execution semantics.
- Ensures Activities are idempotent and Workflows replay cleanly.
- Validates Task timeouts and retries and that Workers can finish business processes.

**How to run this**

Depending on execution environment:

- **Kubernetes**: Set pod count to zero:
  ```bash
  kubectl scale deployment <deployment-name> --replicas=0 -n <namespace>
  kubectl scale deployment <deployment-name> --replicas=3 -n <namespace>
  ```
- **Azure App Service**:
  ```bash
  az webapp restart --name <app-name> --resource-group <resource-group>
  ```

**Things to watch**

- Duplicate/improper Activity results
- Workflow failures
- Workflow backlog growth and drain time

### Frequent Worker restart

**What to test**

Periodically restart a fixed or random percentage (e.g. 20-30%) of your Worker fleet every few minutes.

**Why it matters**

- Mimics failure modes where Workers restart due to high CPU utilization and out-of-memory errors from compute-intensive logic in Activities.
- Ensures Temporal invalidates specific Sticky Task Queues and reschedules the task to the associated non-Sticky Task Queue.

**How to run this**

- **Kubernetes**: Build a script using `kubectl` to randomly delete pods in a loop.
- **Chaos Mesh**: [Simulate pod faults](https://chaos-mesh.org/docs/simulate-pod-chaos-on-kubernetes/).
- **App Services**: Scale down and up again.

**Things to watch**

- Replay latency
- Drop in Workflow and Activity completion
- Duplicate/improper Activity results
- Workflow failures
- Workflow backlog growth and drain time

## Load testing

### Pre-load test setup: expectations for success

1. Have SDK metrics accessible (not just the Cloud metrics)
2. Understand and predict what you should see from these metrics:
   - Rate limiting (`temporal_cloud_v1_resource_exhausted_error_count`)
   - Workflow failures (`temporal_cloud_v1_workflow_failed_count`)
   - Workflow execution time (`workflow_endtoend_latency`)
   - High Cloud latency (`temporal_cloud_v1_service_latency_p95`)
   - [Worker metrics](/develop/worker-performance) (`workflow_task_schedule_to_start_latency` and `activity_schedule_to_start_latency`)
3. Determine throughput requirements ahead of time. Work with your account team to match that to the Namespace capacity to avoid rate limiting. Capacity increases are done via Temporal support and can be requested for a load test (short-term).
4. Automate how you run the load test so you can start and stop it at will. How will you clear Workflow Executions that are just temporary?
5. What does "success" look like for this test? Be specific with metrics and numbers stated in business terms.

### Validate downstream load capacity

**Relevant best practices**: Idempotent Activities, bounded retries, appropriate timeouts and retry policies, understand behavior when limits are reached

**What to test**

- Schedule a large number of Actions and Requests by starting many Workflows
- Increase the number until you start overloading downstream systems

**Why it matters**

Validates behavior of Temporal application and application dependencies under high load.

**How to run this**

Start Workflows at a rate to surpass throughput limits. Example: [temporal-ratelimit-tester-go](https://github.com/joshmsmith/temporal-ratelimit-tester-go)

**Things to watch**

- Downstream service error rates (HTTP 5xx, database errors)
- Increased downstream service latency and saturation metrics
- Activity failure rates, specifically classifying between retryable and non-retryable errors
- Activity retry and backoff behavior against the overloaded system
- Workflow backlog growth and drain time
- Correctness and consistency of data (ensuring Activity idempotency holds under duress)
- Worker CPU/memory utilization

### Validate rate limiting behavior

**Relevant best practices**: [Manage Namespace capacity limits](/best-practices/managing-aps-limits), understand behavior when limits are reached

**What to test**

- Schedule a large number of Actions and Requests by starting many Workflows
- Increase the number until you get rate limited (trigger metric [`temporal_cloud_v0_resource_exhausted_error_count`](/cloud/metrics/reference#temporal_cloud_v0_resource_exhausted_error_count))

**Why it matters**

Validates behavior of Cloud service under high load: "In Temporal Cloud, the effect of rate limiting is increased latency, not lost work. Workers might take longer to complete Workflows."

**How to run this**

1. (Optional) Decrease a test Namespace's rate limits to make it easier to hit limits
2. Calculate current APS at current throughput (in production)
3. Calculate Workflow throughput needed to surpass limits
4. Start Workflows at a rate to surpass throughput limits using [temporal-ratelimit-tester-go](https://github.com/joshmsmith/temporal-ratelimit-tester-go)

**Things to watch**

- Worker behavior when rate limited
- Client behavior when rate limited
- Temporal request and long_request failure rates
- Workflow success rates
- Workflow latency rates

## Failover and availability

**Relevant best practices**: Use [High Availability features](/cloud/high-availability) for critical workloads.

- [High Availability monitoring](/cloud/high-availability/monitoring)

### Test region failover

**What to test**

Trigger a [High Availability](/cloud/high-availability) failover event for a Namespace.

**Why it matters**

- Real outages are messy and rarely isolated.
- Ensures your operational playbooks and automation are resilient.
- Validates Worker and Namespace failover behavior.

**How to run this**

Execute a manual failover per the [manual failovers documentation](/cloud/high-availability/failovers/manage#trigger-failover).

**Things to watch**

- Namespace availability
- Client and Worker connectivity to failover region
- Workflow Task reassignments
- Human-in-the-loop recovery steps

## Dependency and downstream testing

### Break the things your Workflows call

**What to test**

Intentionally break or degrade downstream dependencies used by Activities:

- Make databases read-only or unavailable
- Inject high latency or error rates into external APIs
- Throttle or pause message queues and event streams

**Why it matters**

- Temporal guarantees Workflow durability, not dependency availability.
- Validates that Activities are retryable, idempotent, and correctly timeout-bounded.
- Ensures Workflows make forward progress instead of livelocking on broken dependencies.

**Things to watch**

- Activity retry and backoff behavior
- Heartbeat effectiveness for long-running Activities
- Database connection exhaustion and retry storms
