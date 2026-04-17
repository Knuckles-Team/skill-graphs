[Skip to main content](https://docs.temporal.io/production-deployment/multi-tenant-patterns#__docusaurus_skipToContent_fallback)
[![Temporal logo](https://docs.temporal.io/img/assets/temporal-logo-dark.svg)](https://temporal.io)[Home](https://docs.temporal.io/)[Courses](https://learn.temporal.io/getting_started/)[SDKs](https://docs.temporal.io/develop)[AI Cookbook](https://docs.temporal.io/ai-cookbook)[Code Exchange](https://temporal.io/code-exchange)[Temporal Cloud](https://docs.temporal.io/cloud)
Ask AI
Search
  * [Home](https://docs.temporal.io/)
  * [Quickstarts](https://docs.temporal.io/quickstarts)
  * [Evaluate](https://docs.temporal.io/evaluate/)
  * [Develop](https://docs.temporal.io/develop/)
  * [Temporal Cloud](https://docs.temporal.io/cloud)
  * [Deploy to production](https://docs.temporal.io/production-deployment)
  * [CLI (temporal)](https://docs.temporal.io/cli)
  * [References](https://docs.temporal.io/references/)
  * [Troubleshooting](https://docs.temporal.io/troubleshooting/)
  * [Best practices](https://docs.temporal.io/best-practices/)
    * [Worker deployment and performance](https://docs.temporal.io/best-practices/worker)
    * [Pre-Production Testing](https://docs.temporal.io/best-practices/pre-production-testing)
    * [Multi-tenant patterns](https://docs.temporal.io/production-deployment/multi-tenant-patterns)
    * [Namespace best practices](https://docs.temporal.io/best-practices/managing-namespace)
    * [Managing APS limits](https://docs.temporal.io/best-practices/managing-aps-limits)
    * [Managing Cloud access control](https://docs.temporal.io/best-practices/cloud-access-control)
    * [Security controls for Cloud](https://docs.temporal.io/best-practices/security-controls)
    * [Cost Optimization](https://docs.temporal.io/best-practices/cost-optimization)
    * [Knowledge Hub](https://docs.temporal.io/best-practices/knowledge-hub)
  * [Encyclopedia](https://docs.temporal.io/encyclopedia/)
  * [Glossary](https://docs.temporal.io/glossary)
  * [Use with AI](https://docs.temporal.io/with-ai)


  * [](https://docs.temporal.io/)
  * [Best practices](https://docs.temporal.io/best-practices/)
  * Multi-tenant patterns


On this page
# Multi-tenant application patterns
Many SaaS providers and large enterprise platform teams use a single Temporal [Namespace](https://docs.temporal.io/namespaces) with [per-tenant Task Queues](https://docs.temporal.io/production-deployment/multi-tenant-patterns#1-task-queues-per-tenant-recommended) to power their multi-tenant applications. This approach maximizes resource efficiency while maintaining logical separation between tenants.
This guide covers architectural patterns, design considerations, and practical examples for building multi-tenant applications with Temporal.
## Architectural principles[​](https://docs.temporal.io/production-deployment/multi-tenant-patterns#architectural-principles "Direct link to Architectural principles")
When designing a multi-tenant Temporal application, follow these principles:
  * **Define your tenant model** - Determine what constitutes a tenant in your business (customers, pricing tiers, teams, etc.)
  * **Prefer simplicity** - Start with the simplest pattern that meets your needs
  * **Understand Temporal limits** - Design within the constraints of your Temporal deployment
  * **Test at scale** - Performance testing must drive your capacity decisions
  * **Plan for growth** - Consider how you'll onboard new tenants and scale workers


## Architectural patterns[​](https://docs.temporal.io/production-deployment/multi-tenant-patterns#architectural-patterns "Direct link to Architectural patterns")
There are three main patterns for multi-tenant applications in Temporal, listed from most to least recommended:
### 1. Task queues per tenant (Recommended)[​](https://docs.temporal.io/production-deployment/multi-tenant-patterns#1-task-queues-per-tenant-recommended "Direct link to 1. Task queues per tenant \(Recommended\)")
**Use different[Task Queues](https://docs.temporal.io/task-queue) for each tenant's [Workflows](https://docs.temporal.io/workflows) and [Activities](https://docs.temporal.io/activities).**
This is the recommended pattern for most use cases. Each tenant gets dedicated Task Queue(s), with [Workers](https://docs.temporal.io/workers) polling multiple tenant Task Queues in a single process.
**Pros:**
  * Strong isolation between tenants
  * Efficient resource utilization
  * Flexible worker scaling
  * Easy to add new tenants
  * Can handle thousands of tenants per [Namespace](https://docs.temporal.io/namespaces)


**Cons:**
  * Requires worker configuration management
  * Potential for uneven resource distribution
  * Need to prevent "noisy neighbor" issues at the worker level


Related 📚
[Task Queue Isolation Pattern Details](https://docs.temporal.io/production-deployment/multi-tenant-patterns#task-queue-isolation-pattern)feature-guide
### 2. Shared Workflow Task Queues, separate Activity Task Queues[​](https://docs.temporal.io/production-deployment/multi-tenant-patterns#2-shared-workflow-task-queues-separate-activity-task-queues "Direct link to 2. Shared Workflow Task Queues, separate Activity Task Queues")
**Share[Workflow Task Queues](https://docs.temporal.io/task-queue) but use different [Activity Task Queues](https://docs.temporal.io/task-queue) per tenant.**
Use this pattern when [Workflows](https://docs.temporal.io/workflows) are lightweight but [Activities](https://docs.temporal.io/activities) have heavy resource requirements or external dependencies that need isolation.
**Pros:**
  * Easier worker management than full isolation
  * Activity-level tenant isolation
  * Good for compute-intensive Activities


**Cons:**
  * Less isolation than pattern #1
  * Workflow visibility is shared
  * More complex to reason about


### 3. Namespace per tenant[​](https://docs.temporal.io/production-deployment/multi-tenant-patterns#3-namespace-per-tenant "Direct link to 3. Namespace per tenant")
**Use a separate[Namespace](https://docs.temporal.io/namespaces) for each tenant.**
Only practical for a small number (< 50) of high-value tenants due to operational overhead.
**Pros:**
  * Complete isolation between tenants
  * Per-tenant rate limiting
  * Maximum security


**Cons:**
  * Higher operational overhead
  * Credential and connectivity management per [Namespace](https://docs.temporal.io/namespaces)
  * Requires more [Workers](https://docs.temporal.io/workers) (minimum 2 per Namespace for high availability)
  * Expensive at scale


Related 📚
[Namespace Isolation in Temporal Cloud](https://docs.temporal.io/evaluate/development-production-features/multi-tenancy#namespace-isolation)
## Task Queue isolation pattern[​](https://docs.temporal.io/production-deployment/multi-tenant-patterns#task-queue-isolation-pattern "Direct link to Task Queue isolation pattern")
This section details the recommended pattern for most multi-tenant applications.
### Worker design[​](https://docs.temporal.io/production-deployment/multi-tenant-patterns#worker-design "Direct link to Worker design")
When a [Worker](https://docs.temporal.io/workers) starts up:
  1. **Load tenant configuration** - Retrieve the list of tenants this Worker should handle (from config file, API, or database)
  2. **Create[Task Queues](https://docs.temporal.io/task-queue)** - For each tenant, generate a unique Task Queue name (e.g., `customer-{tenant-id}`)
  3. **Register[Workflows](https://docs.temporal.io/workflows) and [Activities](https://docs.temporal.io/activities)** - Register your Workflow and Activity implementations once, passing the tenant-specific Task Queue name
  4. **Poll multiple Task Queues** - A single Worker process polls all assigned tenant Task Queues


```
// Example: Go worker polling multiple tenant Task Queues
for _, tenant := range assignedTenants {
    taskQueue := fmt.Sprintf("customer-%s", tenant.ID)

    worker := worker.New(client, taskQueue, worker.Options{})
    worker.RegisterWorkflow(YourWorkflow)
    worker.RegisterActivity(YourActivity)
}

```

### Routing requests to Task Queues[​](https://docs.temporal.io/production-deployment/multi-tenant-patterns#routing-requests-to-task-queues "Direct link to Routing requests to Task Queues")
Your application needs to route [Workflow](https://docs.temporal.io/workflows) starts and other operations to the correct tenant [Task Queue](https://docs.temporal.io/task-queue):
```
// Example: Starting a Workflow for a specific tenant
taskQueue := fmt.Sprintf("customer-%s", tenantID)
workflowOptions := client.StartWorkflowOptions{
    ID:        workflowID,
    TaskQueue: taskQueue,
}

```

Consider creating an API or service that:
  * Maps tenant IDs to Task Queue names
  * Tracks which [Workers](https://docs.temporal.io/workers) are handling which tenants
  * Allows both your application and Workers to read the mappings of:
    1. Tenant IDs to Task Queues
    2. Workers to tenants


### Capacity planning[​](https://docs.temporal.io/production-deployment/multi-tenant-patterns#capacity-planning "Direct link to Capacity planning")
Key questions to answer through performance testing:
**[Namespace](https://docs.temporal.io/namespaces) capacity:**
  * How many concurrent [Task Queue](https://docs.temporal.io/task-queue) pollers can your Namespace support?
  * What are your [Actions Per Second (APS)](https://docs.temporal.io/cloud/limits#actions-per-second) limits?
  * What are your [Operations Per Second (OPS)](https://docs.temporal.io/references/operation-list) limits?


**[Worker](https://docs.temporal.io/workers) capacity:**
  * How many tenants can a single Worker process handle?
  * What are the CPU and memory requirements per tenant?
  * How many concurrent [Workflow](https://docs.temporal.io/workflows) executions per tenant?
  * How many concurrent [Activity](https://docs.temporal.io/activities) executions per tenant?


**SDK configuration to tune:**
  * `MaxConcurrentWorkflowTaskExecutionSize`
  * `MaxConcurrentActivityExecutionSize`
  * `MaxConcurrentWorkflowTaskPollers`
  * `MaxConcurrentActivityTaskPollers`
  * Worker replicas (in Kubernetes deployments)


### Provisioning new tenants[​](https://docs.temporal.io/production-deployment/multi-tenant-patterns#provisioning-new-tenants "Direct link to Provisioning new tenants")
Automate tenant onboarding with a Temporal [Workflow](https://docs.temporal.io/workflows):
  1. Create a tenant onboarding Workflow that:
     * Validates tenant information
     * Provisions infrastructure
     * Deploys/updates [Worker](https://docs.temporal.io/workers) configuration
     * Triggers Worker restarts or scaling
     * Verifies the tenant is operational
  2. Store tenant-to-Worker mappings in a database or configuration service
  3. Update Worker deployments to pick up new tenant assignments


## Practical example[​](https://docs.temporal.io/production-deployment/multi-tenant-patterns#practical-example "Direct link to Practical example")
**Scenario:** A SaaS company has 1,000 customers and expects to grow to 5,000 customers over 3 years. They have 2 [Workflows](https://docs.temporal.io/workflows) and ~25 [Activities](https://docs.temporal.io/activities) per Workflow. All customers are on the same tier (no segmentation yet).
### Assumptions[​](https://docs.temporal.io/production-deployment/multi-tenant-patterns#assumptions "Direct link to Assumptions")
Item | Value
---|---
Current customers | 1,000
Workflow Task Queues per customer | 1
Activity Task Queues per customer | 1
Max Task Queue pollers per Namespace | 5,000
SDK concurrent Workflow task pollers | 5
SDK concurrent Activity task pollers | 5
Max concurrent Workflow executions | 200
Max concurrent Activity executions | 200
### Capacity calculations[​](https://docs.temporal.io/production-deployment/multi-tenant-patterns#capacity-calculations "Direct link to Capacity calculations")
**[Task Queue](https://docs.temporal.io/task-queue) poller limits:**
  * Each [Worker](https://docs.temporal.io/workers) uses 10 pollers per tenant (5 Workflow + 5 Activity)
  * Maximum Workers in [Namespace](https://docs.temporal.io/namespaces): 5,000 pollers ÷ 10 = **500 Workers**


**Worker capacity:**
  * Each Worker can theoretically handle 200 [Workflows](https://docs.temporal.io/workflows) and 200 [Activities](https://docs.temporal.io/activities) concurrently
  * Conservative estimate: **250 tenants per Worker** (accounting for overhead)
  * For 1,000 customers: **4 Workers minimum** (plus replicas for HA)
  * For 5,000 customers: **20 Workers minimum** (plus replicas for HA)


**Namespace capacity:**
  * At 250 tenants per Worker, need 2 Workers per group of tenants (for HA)
  * Maximum tenants in Namespace: (500 Workers ÷ 2) × 250 = **62,500 tenants**


These are theoretical calculations based on SDK defaults. **Always perform load testing** to determine actual capacity for your specific workload. Monitor CPU, memory, and Temporal metrics during testing.
While testing, also pay attention to your [metrics capacity and cardinality](https://docs.temporal.io/cloud/metrics/openmetrics/api-reference#managing-high-cardinality).
### Worker assignment strategies[​](https://docs.temporal.io/production-deployment/multi-tenant-patterns#worker-assignment-strategies "Direct link to Worker assignment strategies")
**Option 1: Static configuration**
  * Each [Worker](https://docs.temporal.io/workers) reads a config file listing assigned tenant IDs
  * Simple to implement
  * Requires deployment to add tenants


**Option 2: Dynamic API**
  * Workers call an API on startup to get assigned tenants
  * Workers identified by static ID (1 to N)
  * API returns tenant list based on Worker ID
  * More flexible, no deployment needed for new tenants


## Best practices[​](https://docs.temporal.io/production-deployment/multi-tenant-patterns#best-practices "Direct link to Best practices")
### Monitoring[​](https://docs.temporal.io/production-deployment/multi-tenant-patterns#monitoring "Direct link to Monitoring")
Track these [metrics](https://docs.temporal.io/references/sdk-metrics) per tenant:
  * [Workflow completion](https://docs.temporal.io/cloud/metrics/openmetrics/metrics-reference#workflow-completion-metrics) rates
  * [Activity execution](https://docs.temporal.io/cloud/metrics/openmetrics/metrics-reference#task-queue-metrics) rates
  * [Task Queue backlog](https://docs.temporal.io/cloud/metrics/openmetrics/metrics-reference#task-queue-metrics)
  * [Worker resource utilization](https://docs.temporal.io/references/sdk-metrics#worker_task_slots_used)
  * [Workflow failure rates](https://docs.temporal.io/encyclopedia/detecting-workflow-failures)


### Handling noisy neighbors[​](https://docs.temporal.io/production-deployment/multi-tenant-patterns#handling-noisy-neighbors "Direct link to Handling noisy neighbors")
Even with [Task Queue](https://docs.temporal.io/task-queue) isolation, monitor for tenants that:
  * Generate excessive load
  * Have high failure rates
  * Cause [Worker](https://docs.temporal.io/workers) resource exhaustion


Strategies:
  * Implement per-tenant rate limiting in your application
  * Move problematic tenants to dedicated Workers
  * Use [Workflow](https://docs.temporal.io/workflows)/[Activity](https://docs.temporal.io/activities) timeouts aggressively


### Tenant lifecycle[​](https://docs.temporal.io/production-deployment/multi-tenant-patterns#tenant-lifecycle "Direct link to Tenant lifecycle")
Plan for:
  * **Onboarding** - Automated provisioning [Workflow](https://docs.temporal.io/workflows)
  * **Scaling** - When to add new [Workers](https://docs.temporal.io/workers) for growing tenants
  * **Offboarding** - Graceful tenant removal and data cleanup
  * **Rebalancing** - Redistributing tenants across Workers


### Search Attributes[​](https://docs.temporal.io/production-deployment/multi-tenant-patterns#search-attributes "Direct link to Search Attributes")
Use [Search Attributes](https://docs.temporal.io/search-attribute) to enable tenant-scoped queries:
```
// Add tenant ID as a Search Attribute
searchAttributes := map[string]interface{}{
    "TenantId": tenantID,
}

```

This allows filtering [Workflows](https://docs.temporal.io/workflows) by tenant in the UI and SDK:
```
TenantId = 'customer-123' AND ExecutionStatus = 'Running'

```

## Related resources[​](https://docs.temporal.io/production-deployment/multi-tenant-patterns#related-resources "Direct link to Related resources")
Related 📚
  * [Multi-tenancy Overview](https://docs.temporal.io/evaluate/development-production-features/multi-tenancy)feature-guide
  * [Temporal Cloud Limits](https://docs.temporal.io/cloud/limits)
  * [Visibility and Search Attributes](https://docs.temporal.io/visibility)feature-guide


**Tags:**
  * [Multitenancy](https://docs.temporal.io/tags/multitenancy)
  * [Best Practices](https://docs.temporal.io/tags/best-practices)


Help us make Temporal better. Contribute to our
[Previous Pre-Production Testing](https://docs.temporal.io/best-practices/pre-production-testing)[Next Namespace best practices](https://docs.temporal.io/best-practices/managing-namespace)
  * [Architectural principles](https://docs.temporal.io/production-deployment/multi-tenant-patterns#architectural-principles)
  * [Architectural patterns](https://docs.temporal.io/production-deployment/multi-tenant-patterns#architectural-patterns)
    * [1. Task queues per tenant (Recommended)](https://docs.temporal.io/production-deployment/multi-tenant-patterns#1-task-queues-per-tenant-recommended)
    * [2. Shared Workflow Task Queues, separate Activity Task Queues](https://docs.temporal.io/production-deployment/multi-tenant-patterns#2-shared-workflow-task-queues-separate-activity-task-queues)
    * [3. Namespace per tenant](https://docs.temporal.io/production-deployment/multi-tenant-patterns#3-namespace-per-tenant)
  * [Task Queue isolation pattern](https://docs.temporal.io/production-deployment/multi-tenant-patterns#task-queue-isolation-pattern)
    * [Worker design](https://docs.temporal.io/production-deployment/multi-tenant-patterns#worker-design)
    * [Routing requests to Task Queues](https://docs.temporal.io/production-deployment/multi-tenant-patterns#routing-requests-to-task-queues)
    * [Capacity planning](https://docs.temporal.io/production-deployment/multi-tenant-patterns#capacity-planning)
    * [Provisioning new tenants](https://docs.temporal.io/production-deployment/multi-tenant-patterns#provisioning-new-tenants)
  * [Practical example](https://docs.temporal.io/production-deployment/multi-tenant-patterns#practical-example)
    * [Assumptions](https://docs.temporal.io/production-deployment/multi-tenant-patterns#assumptions)
    * [Capacity calculations](https://docs.temporal.io/production-deployment/multi-tenant-patterns#capacity-calculations)
    * [Worker assignment strategies](https://docs.temporal.io/production-deployment/multi-tenant-patterns#worker-assignment-strategies)
  * [Best practices](https://docs.temporal.io/production-deployment/multi-tenant-patterns#best-practices)
    * [Monitoring](https://docs.temporal.io/production-deployment/multi-tenant-patterns#monitoring)
    * [Handling noisy neighbors](https://docs.temporal.io/production-deployment/multi-tenant-patterns#handling-noisy-neighbors)
    * [Tenant lifecycle](https://docs.temporal.io/production-deployment/multi-tenant-patterns#tenant-lifecycle)
    * [Search Attributes](https://docs.temporal.io/production-deployment/multi-tenant-patterns#search-attributes)
  * [Related resources](https://docs.temporal.io/production-deployment/multi-tenant-patterns#related-resources)


  * [Temporal Cloud](https://temporal.io/cloud)
  * [Meetups](https://temporal.io/community#events)
  * [Workshops](https://temporal.io/community#workshops)
  * [Support forum](https://community.temporal.io/)
  * [Ask an expert](https://pages.temporal.io/ask-an-expert)


  * [Learn Temporal](https://learn.temporal.io)
  * [Blog](https://temporal.io/blog)
  * [Use cases](https://temporal.io/use-cases)
  * [Newsletter signup](https://pages.temporal.io/newsletter-subscribe)


  * [Security](https://docs.temporal.io/security)
  * [Privacy policy](https://temporal.io/global-privacy-policy)
  * [Terms of service](https://docs.temporal.io/pdf/temporal-tos-2021-07-24.pdf)
  * [We're hiring](https://temporal.io/careers)


[![Temporal logo](https://docs.temporal.io/img/favicon.png)](https://temporal.io)
Copyright © 2026 Temporal Technologies Inc.
Feedback![](https://static.scarf.sh/a.png?x-pxid=6fb132d3-92f6-455f-bf17-eb3d6937bdea)
Recaptcha requires verification.
-
protected by **reCAPTCHA**
-
