
#### Sample request/response

Consider the following sample request/response when creating and hosting a Codec Server with the following specifications:

- Scheme: `https`
- Host: `dev.mydomain.com/codec`
- Path: `/decode`

```json
HTTP/1.1 POST /decode
Host: https://dev.mydomain.com/codec
Content-Type: application/json
X-Namespace: myapp-dev.acctid123
Authorization: Bearer <token>

{"payloads":[{"metadata":{"encoding":"anNvbi9wcm90b2J1Zg==","messageType":"dGVtcG9yYWxfc2hvcC5vcmNoZXN0cmF0aW9ucy52MS5TdGFydFNob3BwaW5nQ2FydFJlcXVlc3Q="},"data":"eyJjYXJ0SWQiOiJleGFtcGxlLWNhcnQiLCJzaG9wcGVySWQiOiJ5b3VyLXNob3BwZXItaWQtZXhhbXBsZSIsImVtYWlsIjoieW91ci1lbWFpbEBkb21haW4uY29tIn0"}]}

200 OK
Content-Type: application/json

{
  "payloads": [{
    "metadata":{
      "encoding": "json/protobuf",
      "messageType": "temporal_shop.orchestrations.v1.StartShoppingCartRequest"
    },
    "data":{
      "cartId":"example-cart",
      "shopperId":"your-shopper-id-example",
      "email":"your-email@domain.com"
    }}]
}
```

You can also perform remote encoding on an `/encode` endpoint, which looks the same in reverse:

- Scheme: `https`
- Host: `dev.mydomain.com/codec`
- Path: `/encode`

```json
HTTP/1.1 POST /encode
Host: https://dev.mydomain.com/codec
Content-Type: application/json
X-Namespace: myapp-dev.acctid123
Authorization: Bearer <token>

{"payloads":[{"metadata":{"encoding":"json/protobuf","messageType":"temporal_shop.orchestrations.v1.StartShoppingCartRequest"},"data":{"cartId":"example-cart","shopperId":"your-shopper-id-example","email":"your-email@domain.com"}}]}

200 OK
Content-Type: application/json

{
  "payloads": [
    {
      "metadata": {
        "encoding": "anNvbi9wcm90b2J1Zg==",
        "messageType": "dGVtcG9yYWxfc2hvcC5vcmNoZXN0cmF0aW9ucy52MS5TdGFydFNob3BwaW5nQ2FydFJlcXVlc3Q="
      },
      "data": "eyJjYXJ0SWQiOiJleGFtcGxlLWNhcnQiLCJzaG9wcGVySWQiOiJ5b3VyLXNob3BwZXItaWQtZXhhbXBsZSIsImVtYWlsIjoieW91ci1lbWFpbEBkb21haW4uY29tIn0"
    }
  ]
}
```

### Set your Codec Server endpoints with Web UI and CLI

After you create your Codec Server and expose the requisite endpoints, set the endpoints in your Web UI and CLI.

#### Web UI

On Temporal Cloud and self-hosted Temporal Service, you can configure a Codec Server endpoint to be used for a Namespace in the Web UI.

<CaptionedImage
    src="/img/info/set-codec-endpoint-form.png"
    title="Codec Server endpoint Namespace setting"
/>

:::caution

If your Codec Server is on a private network, your browser may block Temporal Web UI from accessing it. On Chrome, your browser may prompt you to allow access to the Codec Server endpoint. Make sure to allow access to the Codec Server endpoint. Refer to the [Chrome for Developers blog: New permission prompt for Local Network Access](https://developer.chrome.com/blog/local-network-access/) for details on this permission prompt.

If your browser has blocked Temporal's access to your Codec Server, refer to [Chrome documentation](https://support.google.com/chrome/answer/114662) for details on how to change the site settings. In **Site settings**, look for the **Local network** setting and change it to **Allow** to only change this setting for Temporal without affecting other sites.

:::

To set a Codec Server endpoint on a Namespace, do the following.

1. In the Web UI, go to Namespaces, select the Namespace where you want to configure the Codec Server endpoint, and click **Edit**.
1. In the **Codec Server** section on the Namespace configuration page, enter your Codec Server endpoint and port number.
1. Optional: If your Codec Server is configured to [authenticate requests](#authorization) from Temporal Web UI, enable **Pass access token** to send a JWT access token with the HTTPS requests.
1. Optional: If your Codec Server is configured to [verify origins of requests](#cors), enable **Include cross-origin credentials**.

On Temporal Cloud, you must have [Namespace Admin privileges](/cloud/manage-access/roles-and-permissions#namespace-level-permissions) to add a Codec Server endpoint on the Namespace. Setting a Codec Server endpoint on a Cloud Namespace enables it for all users on the Namespace.

Setting a Codec Server endpoint on a self-hosted Temporal Service enables it for the entire Temporal Service. You can use a single Codec Server to handle different encoding and decoding routes for each namespace.

You can also override the global Codec Server setting at the browser level. This can be useful when developing, testing, or troubleshooting encoding functionality.

<CaptionedImage
    src="/img/info/data-encoder-button.png"
    title="Codec Server endpoint browser setting"
/>

To set a browser override for the Namespace-level endpoint, do the following.

1. Navigate to **Workflows** in your Namespace.
2. In the top-right corner, select **Configure Codec Server**.
3. Select whether you want to use the Namespace-level (or Temporal Service-level for self-hosted Temporal Service) or the browser-level Codec Endpoint setting as the default for your browser.
   In Temporal Cloud:
   - **Use Namespace-level settings, where available. Otherwise, use my browser setting.**
     Uses the Namespace-level Codec Server endpoint by default.
     If no endpoint is set on the Namespace, your browser setting is applied.
   - **Use my browser setting and ignore Namespace-level setting.**
     Applies your browser-level setting by default, overriding the Namespace-level Codec Server endpoint.
4. Enter your Codec Server endpoint and port number.
5. Optional: If your Codec Server is configured to [authenticate requests](#authorization) from Temporal Web UI, enable **Pass access token** to send a JWT access token with the HTTPS requests.
6. Optional: If your Codec Server is configured to [verify origins of requests](#cors), enable **Include cross-origin credentials**.

In a self-hosted Temporal Service with dedicated UI Server configuration, you can also set the codec endpoint in the UI server [configuration file](/references/web-ui-configuration#codec):

```yaml
codec:
    endpoint: {{ default .Env.TEMPORAL_CODEC_ENDPOINT "{namespace}"}}
```

#### CLI

You can configure a Codec Server endpoint with the Temporal CLI using the `--codec-endpoint` flag.

For example, if you are running your Codec Server on `http://localhost:8888`, you can use `env set` to set the endpoint globally:

```bash
temporal env set --codec-endpoint "http://localhost:8888"
```

If your Codec Server endpoint is not set globally, provide the `--codec-endpoint` option with each command.
For example, to see the decoded output of the Workflow Execution "yourWorkflow" in the Namespace "yourNamespace", run:

```bash
temporal --codec-endpoint "http://localhost:8888" --namespace "yourNamespace" workflow show --workflow-id "yourWorkflow"  --run-id "<yourRunId>" --output "table"
```

For details, see the [CLI reference](/cli/).

If your Codec Server requires authentication, the Temporal CLI will also accept a `--codec-auth` parameter to supply an
authorization header:

```shell
temporal workflow show \
   --workflow-id converters_workflowID \
   --codec-endpoint 'http://localhost:8081/{namespace}' \
   --codec-auth 'auth-header'
```

### Working with large payloads

If your payloads exceed the Temporal Service's size limits, use [External Storage](/external-storage) to offload large
payloads to an external store like Amazon S3. The Web UI displays a claim reference instead of the payload content for
externally stored payloads. When External Storage is configured on your Codec Server, the Codec Server can retrieve
and decode these payloads for viewing in the Web UI and CLI. See
[Codec Server with External Storage](/codec-server#external-storage) for details.

### Temporal Nexus

The Data Converter works the same for a Nexus Operation as it does for other payloads sent between a Worker and Temporal Cloud.
Both the caller and handler Workers must use compatible Data Converters to pass operation inputs and results between them.

See [Nexus Payload Encryption & Data Converter](/nexus/security#payload-encryption-data-converter) for details.

---

## Temporal Platform production deployments

To take your application to production, you'll need to deploy the following components:

- Your application code, including your Workflows, Activities, and Workers, on your infrastructure using your existing
  build, test and deploy tools.

- A production-ready Temporal Service to coordinate the execution of your Workflows and Activities.
  - You can use Temporal Cloud, a fully managed platform, or you can self-host the service.

:::tip Do you need a production Temporal Service?

If you're still developing and testing your application locally, you may not need a production Temporal Service. Use the
[Temporal CLI development server](/cli/command-reference/server#start-dev) — a single binary with no external dependencies:

`temporal server start-dev`

This starts a complete Temporal Service with Web UI on your local machine. We recommend this for local development
regardless of whether you plan to use Temporal Cloud or self-host in production. See the
[Temporal CLI server](/cli/command-reference/server) page for configuration options.

:::

## Use Temporal Cloud

You can let us handle the operations of running the Temporal Service, and focus on your application. Follow the
[Temporal Cloud guide](/cloud) to get started.

<CaptionedImage
  src="/diagrams/basic-platform-topology-cloud.svg"
  title="Connect your application instances to Temporal Cloud"
/>

## Run a Self-hosted Temporal Service

Alternatively, you can run your own production level Temporal Service to orchestrate your durable applications. Follow
the [Self-hosted guide](/self-hosted-guide) to get started.

<CaptionedImage
  src="/diagrams/basic-platform-topology-self-hosted.svg"
  title="Connect your application instances to your self-hosted Temporal Service"
/>

## Worker deployments

Whether you're hosting with Temporal Cloud or on your own, you have control over where to run and scale your Workers. We
provide guidance on [Worker Deployments](/production-deployment/worker-deployments).

---

## Multi-tenant application patterns

Many SaaS providers and large enterprise platform teams use a single Temporal [Namespace](/namespaces) with [per-tenant Task Queues](#1-task-queues-per-tenant-recommended) or [Task Queue Fairness](#2-single-task-queue-with-fairness) to power their multi-tenant applications. These approaches maximize resource efficiency while maintaining logical separation between tenants.

This guide covers architectural patterns, design considerations, and practical examples for building multi-tenant applications with Temporal.

For related guidance on where to draw Namespace boundaries and how to scope credentials and permissions, see
[Namespace best practices](/best-practices/managing-namespace) and
[Managing Temporal Cloud access control](/best-practices/cloud-access-control).

## Architectural principles

When designing a multi-tenant Temporal application, follow these principles:

- **Define your tenant model** - Determine what constitutes a tenant in your business (customers, pricing tiers, teams, etc.)
- **Prefer simplicity** - Start with the simplest pattern that meets your needs
- **Understand Temporal limits** - Design within the constraints of your Temporal deployment
- **Test at scale** - Performance testing must drive your capacity decisions
- **Plan for growth** - Consider how you'll onboard new tenants and scale workers

## Architectural patterns

There are four main patterns for multi-tenant applications in Temporal, listed from most to least recommended:

### 1. Task queues per tenant (Recommended)

**Use different [Task Queues](/task-queue) for each tenant's [Workflows](/workflows) and [Activities](/activities).**

This is the recommended pattern for most use cases. Each tenant gets dedicated Task Queue(s), with [Workers](/workers) polling multiple tenant Task Queues in a single process.

**Pros:**
- Strong isolation between tenants
- Efficient resource utilization
- Flexible worker scaling
- Easy to add new tenants
- Can handle thousands of tenants per [Namespace](/namespaces)

**Cons:**
- Requires worker configuration management
- Potential for uneven resource distribution
- Need to prevent "noisy neighbor" issues at the worker level

<RelatedReadContainer>
  <RelatedReadItem path="#task-queue-isolation-pattern" text="Task Queue Isolation Pattern Details" archetype="feature-guide" />
</RelatedReadContainer>

### 2. Single Task Queue with Fairness

**Use a single [Task Queue](/task-queue) with [Fairness keys](/develop/task-queue-priority-fairness#task-queue-fairness) to distribute work across tenants.**

This pattern uses [Task Queue Fairness](/develop/task-queue-priority-fairness#task-queue-fairness) to manage multi-tenant workloads within a single Task Queue. Each tenant is assigned a fairness key, and fairness weights control how much of the Task Queue's capacity each tenant receives.

You can also set per-fairness-key rate limits (requests per second) to cap individual tenant throughput, preventing any single tenant from consuming too much capacity.

**Pros:**
- Priority and Fairness keys and weights can be adjusted without redeployment
- Onboarding new tenants doesn't require spinning up additional [Workers](/workers)
- Simpler Worker topology than per-tenant Task Queues

**Cons:**
- Fairness is probabilistic and may be harder to debug than strict isolation
- The fairness weight applies at schedule time, not at dispatch time, so it only affects newly-scheduled Tasks
- When using [Worker Versioning](/worker-versioning), Fairness isn't guaranteed between versions

:::tip
This pattern works well when you have many tenants with different service tiers and want to manage them without the operational overhead of per-tenant Task Queues or Workers.
:::

<RelatedReadContainer>
  <RelatedReadItem path="/develop/task-queue-priority-fairness#task-queue-fairness" text="Task Queue Fairness Reference" archetype="feature-guide" />
</RelatedReadContainer>

### 3. Shared Workflow Task Queues, separate Activity Task Queues

**Share [Workflow Task Queues](/task-queue) but use different [Activity Task Queues](/task-queue) per tenant.**

Use this pattern when [Workflows](/workflows) are lightweight but [Activities](/activities) have heavy resource requirements or external dependencies that need isolation.

**Pros:**
- Easier worker management than full isolation
- Activity-level tenant isolation
- Good for compute-intensive Activities

**Cons:**
- Less isolation than pattern #1
- Workflow visibility is shared
- More complex to reason about

### 4. Namespace per tenant

**Use a separate [Namespace](/namespaces) for each tenant.**

Only practical for a smaller number of high-value tenants due to operational overhead. Most teams find this manageable for fewer than 50 tenants, though organizations with strong automation may scale higher. This pattern is not a good fit if you expect a very large number of tenants (10,000+).

**Pros:**
- Complete isolation between tenants — no noisy neighbor problem
- Each Namespace has its own [rate limits](/cloud/limits) that can be provisioned on demand per customer
- Each Namespace can be deployed across [multiple regions](/cloud/service-availability) globally
- Per-Namespace observability is available by default
- Maximum security boundary

**Cons:**
- Higher operational overhead
- Credential and connectivity management per [Namespace](/namespaces)
- Requires a new [Worker](/workers) pool deployment for each customer (minimum 2 per Namespace for high availability)
- Not cost-effective at scale

This pattern is usually chosen when tenant boundaries also need to be credential boundaries. For example, each tenant may
need its own service accounts, API keys, dashboards, or rate limits. If that is your primary driver, review
[Managing Temporal Cloud access control](/best-practices/cloud-access-control) together with
[Namespace best practices](/best-practices/managing-namespace) before committing to Namespace-per-tenant isolation.

<RelatedReadContainer>
  <RelatedReadItem path="/evaluate/development-production-features/multi-tenancy#namespace-isolation" text="Namespace Isolation in Temporal Cloud" archetype="cloud-guide" />
</RelatedReadContainer>

### Pattern comparison

| | Task Queues per tenant | Fairness-based | Shared Workflow / Separate Activity TQs | Namespace per tenant |
|---|---|---|---|---|
| **Isolation** | Task Queue level | Probabilistic (weighted) | Activity-level only | Complete |
| **Noisy neighbor protection** | Strong | Weight-based throttling | Activity-level | Full — separate rate limits |
| **Worker management** | Moderate — config per tenant | Simple — single Task Queue | Moderate | High — Worker pool per tenant |
| **Onboarding new tenants** | Config update and restart | Set fairness and priority values (no new Workers) | Config update and Worker restart | New Namespace and Worker pool |
| **Observability** | Per-Task Queue metrics | Per-Task Queue metrics | Mixed | Per-Namespace |
| **Rate limiting** | Shared across Task Queue | Per-key rate limits | Shared across Namespace | Independent per Namespace |
| **Scale ceiling** | Thousands of tenants | Thousands of tenants | Thousands of tenants | 10,000 (Namespace limit) |
| **Best for** | Most multi-tenant apps | Tiered SaaS with many tenants | Heavy Activity workloads | High-value, compliance-sensitive tenants |

## Task Queue isolation pattern

This section details the recommended pattern for most multi-tenant applications.

### Worker design

When a [Worker](/workers) starts up:

1. **Load tenant configuration** - Retrieve the list of tenants this Worker should handle (from config file, API, or database)
2. **Create [Task Queues](/task-queue)** - For each tenant, generate a unique Task Queue name (e.g., `customer-{tenant-id}`)
3. **Register [Workflows](/workflows) and [Activities](/activities)** - Register your Workflow and Activity implementations once, passing the tenant-specific Task Queue name
4. **Poll multiple Task Queues** - A single Worker process polls all assigned tenant Task Queues

```go
// Example: Go worker polling multiple tenant Task Queues
for _, tenant := range assignedTenants {
    taskQueue := fmt.Sprintf("customer-%s", tenant.ID)

    worker := worker.New(client, taskQueue, worker.Options{})
    worker.RegisterWorkflow(YourWorkflow)
    worker.RegisterActivity(YourActivity)
}
```

### Routing requests to Task Queues

Your application needs to route [Workflow](/workflows) starts and other operations to the correct tenant [Task Queue](/task-queue):

```go
// Example: Starting a Workflow for a specific tenant
taskQueue := fmt.Sprintf("customer-%s", tenantID)
workflowOptions := client.StartWorkflowOptions{
    ID:        workflowID,
    TaskQueue: taskQueue,
}
```

Consider creating an API or service that:
- Maps tenant IDs to Task Queue names
- Tracks which [Workers](/workers) are handling which tenants
- Allows both your application and Workers to read the mappings of:
    1. Tenant IDs to Task Queues
    1. Workers to tenants

### Capacity planning

Key questions to answer through performance testing:

**[Namespace](/namespaces) capacity:**
- How many concurrent [Task Queue](/task-queue) pollers can your Namespace support?
- What are your [Actions Per Second (APS)](/cloud/limits#actions-per-second) limits?
- What are your [Operations Per Second (OPS)](/references/operation-list) limits?

**[Worker](/workers) capacity:**
- How many tenants can a single Worker process handle?
- What are the CPU and memory requirements per tenant?
- How many concurrent [Workflow](/workflows) executions per tenant?
- How many concurrent [Activity](/activities) executions per tenant?

**SDK configuration to tune:**
- `MaxConcurrentWorkflowTaskExecutionSize`
- `MaxConcurrentActivityExecutionSize`
- `MaxConcurrentWorkflowTaskPollers`
- `MaxConcurrentActivityTaskPollers`
- Worker replicas (in Kubernetes deployments)

### Provisioning new tenants

Automate tenant onboarding with a Temporal [Workflow](/workflows):

1. Create a tenant onboarding Workflow that:
   - Validates tenant information
   - Provisions infrastructure
   - Deploys/updates [Worker](/workers) configuration
   - Triggers Worker restarts or scaling
   - Verifies the tenant is operational

2. Store tenant-to-Worker mappings in a database or configuration service

3. Update Worker deployments to pick up new tenant assignments

## Practical example

**Scenario:** A SaaS company has 1,000 customers and expects to grow to 5,000 customers over 3 years. They have 2 [Workflows](/workflows) and ~25 [Activities](/activities) per Workflow. All customers are on the same tier (no segmentation yet).

### Assumptions

| Item | Value |
|------|-------|
| Current customers | 1,000 |
| Workflow Task Queues per customer | 1 |
| Activity Task Queues per customer | 1 |
| Max Task Queue pollers per Namespace | 20,000 (per [Cloud limits](/cloud/limits)) |
| SDK concurrent Workflow task pollers | 5 |
| SDK concurrent Activity task pollers | 5 |
| Max concurrent Workflow executions | 200 |
| Max concurrent Activity executions | 200 |

### Capacity calculations

**[Task Queue](/task-queue) poller limits:**
- Each [Worker](/workers) uses 10 pollers per tenant (5 Workflow + 5 Activity)
- Maximum Workers in [Namespace](/namespaces): 20,000 pollers ÷ 10 = **2,000 Workers**

**Worker capacity:**
- Each Worker can theoretically handle 200 [Workflows](/workflows) and 200 [Activities](/activities) concurrently
- Conservative estimate: **250 tenants per Worker** (accounting for overhead)
- For 1,000 customers: **4 Workers minimum** (plus replicas for HA)
- For 5,000 customers: **20 Workers minimum** (plus replicas for HA)

**Namespace capacity:**
- At 250 tenants per Worker, need 2 Workers per group of tenants (for HA)
- Maximum tenants in Namespace: (2,000 Workers ÷ 2) × 250 = **250,000 tenants**

:::note
These are theoretical calculations based on SDK defaults. **Always perform load testing** to determine actual capacity for your specific workload. Monitor CPU, memory, and Temporal metrics during testing.

While testing, also pay attention to your [metrics capacity and cardinality](/cloud/metrics/openmetrics/api-reference#managing-high-cardinality).
:::

### Worker assignment strategies

**Option 1: Static configuration**
- Each [Worker](/workers) reads a config file listing assigned tenant IDs
- Simple to implement
- Requires deployment to add tenants

**Option 2: Dynamic API**
- Workers call an API on startup to get assigned tenants
- Workers identified by static ID (1 to N)
- API returns tenant list based on Worker ID
- More flexible, no deployment needed for new tenants

## Best practices

### How tenant isolation affects Namespace and access design

Your multi-tenant architecture also determines how much isolation you get from Namespaces and access controls:

- **Shared Namespace with per-tenant Task Queues**: Best for scale and operational simplicity, but tenant isolation is
  mostly enforced by your application and worker routing logic rather than by Temporal credentials.
- **Separate Namespaces for domains or services**: Useful when teams need separate credentials, dashboards, APS
  envelopes, or on-call boundaries.
- **Namespace per tenant**: Strongest isolation, but highest provisioning and credential-management overhead.

If tenants, teams, or regulated workloads need different credentials or RBAC boundaries, decide that together with your
Namespace topology. See [Namespace best practices](/best-practices/managing-namespace) and
[Managing Temporal Cloud access control](/best-practices/cloud-access-control).

### Monitoring

Track these [metrics](/references/sdk-metrics) per tenant:
- [Workflow completion](/cloud/metrics/openmetrics/metrics-reference#workflow-completion-metrics) rates
- [Activity execution](/cloud/metrics/openmetrics/metrics-reference#task-queue-metrics) rates
- [Task Queue backlog](/cloud/metrics/openmetrics/metrics-reference#task-queue-metrics)
- [Worker resource utilization](/references/sdk-metrics#worker_task_slots_used)
- [Workflow failure rates](/encyclopedia/detecting-workflow-failures)

### Handling noisy neighbors

Even with [Task Queue](/task-queue) isolation, monitor for tenants that:
- Generate excessive load
- Have high failure rates
- Cause [Worker](/workers) resource exhaustion

Strategies:
- Implement per-tenant rate limiting in your application
- Implement fairness keys and apply per-key rate limits
- Move problematic tenants to dedicated Workers
- Use [Workflow](/workflows)/[Activity](/activities) timeouts aggressively

### Tenant lifecycle

Plan for:
- **Onboarding** - Automated provisioning [Workflow](/workflows)
- **Scaling** - When to add new [Workers](/workers) for growing tenants
- **Offboarding** - Graceful tenant removal and data cleanup
- **Rebalancing** - Redistributing tenants across Workers

### Search Attributes

Use [Search Attributes](/search-attribute) to enable tenant-scoped queries:
```go
// Add tenant ID as a Search Attribute
searchAttributes := map[string]interface{}{
    "TenantId": tenantID,
}
```

This allows filtering [Workflows](/workflows) by tenant in the UI and SDK:
```sql
TenantId = 'customer-123' AND ExecutionStatus = 'Running'
```

## Related resources

<RelatedReadContainer>
  <RelatedReadItem path="/evaluate/development-production-features/multi-tenancy" text="Multi-tenancy Overview" archetype="feature-guide" />
