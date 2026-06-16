- API timeouts vs Activity timeouts
- Whether failures propagate as Signals, compensations, or Workflow-level errors

**Anti-patterns this reveals**

- Non-idempotent Activities
- Infinite retries without circuit breaking
- Using Workflow logic to "wait out" broken dependencies

## Deployment and code-level testing

### Deploy a Workflow change with versioning

**Relevant best practices**: Implement a versioning strategy.

- [Workflow Versioning Strategies - Developer Corner](https://community.temporal.io/t/workflow-versioning-strategies/6911)
- [Worker Versioning](/production-deployment/worker-deployments/worker-versioning)
- [Replay Testing](/evaluate/development-production-features/testing-suite)

**What to test**

- Deploy Workflow code that would introduce non-deterministic errors (NDEs) but use a versioning strategy to deploy successfully
- Validate Workflow success and clear the backlog of tasks

**Why it matters**

- Unplanned NDEs can be a painful surprise
- Tests versioning strategy and patching discipline to build production confidence

**Things to watch**

- Workflow Task failure reasons
- Effectiveness of versioning and patching patterns

### Deploy a version that causes NDEs, then recover

**Relevant best practices**: Implement a versioning strategy.

- [Workflow Versioning Strategies - Developer Corner](https://community.temporal.io/t/workflow-versioning-strategies/6911)
- [Worker Versioning](/production-deployment/worker-deployments/worker-versioning)
- [Replay Testing](/evaluate/development-production-features/testing-suite)

**What to test**

- Deploy Workflow code that introduces non-deterministic errors (NDEs)
- Attempt rollback to a known-good version, or apply versioning strategies to apply the new changes successfully
- Clear or recover the backlog of tasks

**Why it matters**

- Unplanned NDEs can be a painful surprise
- Tests versioning strategy, patching discipline, and recovery tooling

**Things to watch**

- Workflow Task failure reasons
- Backlog growth and drain time
- Effectiveness of versioning and patching patterns

## Network-level testing

The scenarios below are most relevant if your infrastructure introduces network boundaries (such as firewalls, VPNs, or network policies) between Workers and the Temporal service, or if you need to verify application behavior during prolonged disconnections.

**Relevant best practices**: Idempotent Activities, bounded retries, appropriate timeouts

- [Activity timeouts](https://temporal.io/blog/activity-timeouts)
- [Idempotency and durable execution](https://temporal.io/blog/idempotency-and-durable-execution)

### Remove network connectivity to a Namespace

**What to test**

Temporarily block all network access between Workers and the Temporal service for a Namespace.

**Why it matters**

- Validates Worker retry behavior, Sticky Task Queue behavior, Worker recovery performance, backoff policies, and Workflow replay determinism under prolonged disconnection.
- Ensures no assumptions are made about "always-on" connectivity.

**Temporal failure modes exercised**

- Workflow Task timeouts vs retries
- Activity retry semantics
- Replay correctness after long gaps

**How to run this**

- **Kubernetes**: Apply a NetworkPolicy that denies egress from Worker pods to the Temporal APIs.
- **[ToxiProxy](https://github.com/Shopify/toxiproxy)**: Proves your application doesn't have single points of failure.
- **Chaos Mesh / Litmus**: NetworkChaos with full packet drop.
- **Local testing**: Block ports with iptables or firewall rules.

**Things to watch**

- Workflow failures (replay, timeout)
- Workflow Task retries
- Activity failures, classifications (retryable vs non-retryable)
- Worker CPU usage during reconnect storms

## Observability checklist

Before (and during) testing, ensure visibility into:

- Workflow Task and Activity failure rates
- Throughput limits and usage
- Workflow and Activity end-to-end latencies
- Task latency and backlog depth
- Event History size and event counts
- Worker CPU, memory, and restart counts
- gRPC error codes
- Retry behavior

## Game day runbook

Use this checklist when running tests during a scheduled game day or real incident simulation.

### Before you start

- Make sure people know you're testing and what scenarios you're trying
  - Let the teams that support the APIs you're calling know you're testing
  - Reach out to the Temporal Cloud Support and Account teams to coordinate
- Dashboards for SDK and Cloud metrics
  - Task latency, backlog depth, Workflow failures, Activity failures
- Alerts muted or routed appropriately
- Known-good deployment artifact available
- Rollback and scale controls verified

### During testing

- Introduce *one variable at a time*
- Record start/stop times of each experiment
- Capture screenshots or logs of unexpected behavior
- Track backlog growth and drain rate

### Recovery validation

- Workflows resume without manual intervention
- No permanent Workflow Task failures (unless intentional)
- Activity retries behave as expected
- Backlogs drain in predictable time

### After action review

- Identify unclear alerts or missing metrics/alerts
- Update retry, timeout, or versioning policies
- Document surprises and operational debt

## Summary

Pre-production testing with Temporal is about more than proving durability - it's about proving *operability under stress*.
You want to go through the exercise and know what to do before you go to production and have to do it for real.

If your system survives:

- Connectivity issues
- Repeated failovers
- Greater than expected load
- Mass Worker churn

...then you can have confidence it's ready for many kinds of production chaos.

---

## Worker deployment and performance

This document outlines best practices for deploying and optimizing Workers to ensure high performance, reliability, and
scalability. It covers deployment strategies, scaling techniques, tuning recommendations, and monitoring approaches to
help you get the most out of your Temporal Workers.

We also provide a reference application, the Order Management System (OMS), that demonstrates the deployment best
practices in action. You can find the OMS codebase on
[GitHub](https://github.com/temporalio/reference-app-orders-go/tree/main/docs).

## Quick checklist

Designing a comprehensive Worker deployment strategy to optimize production performance involves many considerations. We
provide a quick checklist to help you get started. Before deploying Workers to production, ensure you address the
following. Follow the links to the relevant sections for more details.

- **[Configure each Worker appropriately](#actively-tune-worker-options-instead-of-relying-on-defaults)**: Actively tune
  Worker options based on your code, language runtime limits, and system resource constraints. Don't rely on defaults,
  which are designed for ease in development and testing, but not optimal for production environments.
- **[Deploy enough Workers](#interpret-metrics-as-a-whole)**: Monitor performance metrics and scale Workers to meet your
  workload requirements.
- **[Separate Task Queues logically](#separate-task-queues-logically)**: Size and split work across Task types
  (Activities and Workflows) and Task Queues based on workload characteristics.
- **[Version Workers for safe deployments](#use-worker-versioning-to-safely-deploy-new-workflow-code)**: Ensure you can
  deploy new Workflow code without breaking running Executions.
- **Run benchmarks**: Test your configuration under realistic load to confirm limits and settings are appropriate for
  your environment.

## Deployment and lifecycle management

Well-designed Worker deployment ensures resilience, observability, and maintainability. A Worker should be treated as a
long-running service that can be deployed, upgraded, and scaled in a controlled way.

### Package and configure Workers for flexibility

Workers should be artifacts produced by a CI/CD pipeline. Inject all required parameters for connecting to Temporal
Cloud or a self-hosted Temporal Service at runtime via environment variables, configuration files, or command-line
parameters. This allows for more granularity, easier testability, easier upgrades, scalability, and isolation of
Workers.

In the order management reference app, Workers are packaged as Docker images with configuration provided via environment
variables and mounted configuration files. The following Dockerfile uses a multi-stage build to create a minimal,
production-ready Worker image:

{/* SNIPSTART oms-dockerfile-worker */}
[Dockerfile](https://github.com/temporalio/reference-app-orders-go/blob/main/Dockerfile)
```Dockerfile
FROM golang:1.24.1 AS oms-builder

WORKDIR /usr/src/oms

COPY go.mod go.sum ./
RUN --mount=type=cache,target=/go/pkg/mod \
    --mount=type=cache,target=/root/.cache/go-build \
    go mod download

COPY app ./app
COPY cmd ./cmd

RUN --mount=type=cache,target=/go/pkg/mod \
    --mount=type=cache,target=/root/.cache/go-build \
    CGO_ENABLED=0 go build -v -o /usr/local/bin/oms ./cmd/oms

FROM busybox AS oms-worker
```
{/* SNIPEND oms-dockerfile-worker */}

This Dockerfile uses a multi-stage build pattern with two stages:

1. `oms-builder` stage: compiles the Worker binary.

   1. Copies dependency files and downloads dependencies using BuildKit cache mounts to speed up subsequent builds.
   2. Copies the application code and builds a statically linked binary that doesn't require external libraries at
      runtime.

2. `oms-worker` stage: creates a minimal final image.

   1. Copies only the compiled binary from the `oms-builder` stage.
   2. Sets the entrypoint to run the Worker process.

The entrypoint `oms worker` starts the Worker process, which reads configuration from environment variables at runtime.
For example, the
[Billing Worker deployment in Kubernetes](https://github.com/temporalio/reference-app-orders-go/blob/main/deployments/k8s/billing-worker-deployment.yaml)
uses environment variables to configure the Worker:

{/* SNIPSTART oms-billing-worker-deployment {"selectedLines": ["20-35"]} */}
[deployments/k8s/billing-worker-deployment.yaml](https://github.com/temporalio/reference-app-orders-go/blob/main/deployments/k8s/billing-worker-deployment.yaml)
```yaml
