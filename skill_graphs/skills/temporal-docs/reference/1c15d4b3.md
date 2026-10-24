
There is a direct relationship between the sticky cache size and Worker memory consumption.
As the cache size increases, so does the memory usage of the Worker.

The maximum size of the sticky cache can be configured. For example, the default in the Go SDK is 10,000 Workflows.

A larger sticky cache can improve performance by reducing the need to replay Workflow histories.
However, it also increases memory usage, which can lead to issues if not properly managed.

Monitor this metric alongside Worker memory usage.
A sudden increase in `sticky_cache_size` can correlate with increased memory consumption and potential performance issues.

If memory consumption is too high, you can reduce the maximum sticky cache size.
Conversely, if you have available memory and want to improve performance, you might increase it.

### `temporal_sticky_cache_hit_total` and `temporal_sticky_cache_miss_total`

The [`temporal_sticky_cache_hit_total`](https://docs.temporal.io/references/sdk-metrics#sticky_cache_hit) metric is a counter that measures the total number of times a Workflow Task found a cached Workflow Execution to run against, and
the opposite is [`temporal_sticky_cache_miss_total`](https://docs.temporal.io/references/sdk-metrics#sticky_cache_miss), which is a counter that measures the total number of times a Workflow Task did not find a cached Workflow Execution to run against.

Sticky Execution is a feature where a Worker caches a Workflow Execution and creates a dedicated Task Queue to listen on.
This improves performance because the Temporal Service only sends new events to the Worker instead of entire Event Histories, and the Workflow doesn't have to Replay.

A “hit” means the Worker finds the Workflow in its cache when processing a Workflow Task, allowing immediate processing without fetching the full Event History from the server and Replaying.
A "miss" means the Worker didn't find the Workflow in its cache, and it must fetch the Event History and Replay.

Monitoring these two metrics and comparing them can help you understand how your sticky cache is being used.
A high rate of cache hits with a low rate of cache misses indicates that your Workflows are being scheduled efficiently, with minimal need for fetching Event Histories and Replaying.

### `temporal_sticky_cache_total_forced_eviction_total`

The [`temporal_sticky_cache_total_forced_eviction_total`](https://docs.temporal.io/references/sdk-metrics#sticky_cache_hit) metric is a counter that measures the total number of Workflow Executions that have been forcibly evicted from the sticky cache.

Sticky Execution is a feature where a Worker caches a Workflow Execution and creates a dedicated Task Queue to listen on.
This improves performance because the Temporal Service only sends new events to the Worker instead of entire Event Histories, and the Workflow doesn't have to Replay.

A "forced eviction" in this context means that a Workflow Execution was removed from the cache before it completed, typically because the cache was full and needed to make room for other Workflow Executions.
This means that if the Worker needs to process more Tasks for the evicted Workflow Execution, it will have to fetch the entire Event History from the Temporal Service and Replay.

Monitoring the `temporal_sticky_cache_total_forced_eviction_total` metric can help you understand how often your Workflows are being evicted from the cache.
A high rate of forced evictions could indicate that your cache size is too small for your workload, and you may need to increase the `WorkflowCacheSize` setting if your Worker resources can accommodate it.

---

## Troubleshoot missed Schedule Actions

When a [Schedule](/schedule) does not start a Workflow Execution at its expected time, the Action was either skipped intentionally (paused, overlap policy, end time reached) or the Temporal Service could not take the Action within the [Catchup Window](/schedule#catchup-window). This guide covers the second case.

## Alert on missed catchup window

The Temporal Service emits a counter each time it skips a scheduled Action because it could not run it within the configured Catchup Window. Alert on any non-zero value.

### Temporal Cloud

Alert on [`temporal_cloud_v1_schedule_missed_catchup_window_count`](/cloud/metrics/openmetrics/metrics-reference#temporal_cloud_v1_schedule_missed_catchup_window_count) grouped by `temporal_namespace`.

Example PromQL:

```
sum by (temporal_namespace) (
  increase(temporal_cloud_v1_schedule_missed_catchup_window_count[5m])
) > 0
```

### Self-hosted

Alert on [`schedule_missed_catchup_window`](/references/cluster-metrics#schedule_missed_catchup_window) grouped by `namespace`.

Example PromQL:

```
sum by (namespace) (
  increase(schedule_missed_catchup_window[5m])
) > 0
```

The metric is scoped to the Namespace, not to individual Schedules. A non-zero value tells you that at least one Schedule in the Namespace missed an Action, but not which one.

## Investigate which Schedule missed an Action

Once the alert fires, narrow your search down to the affected Schedule in two steps.

### 1. List Schedules in the Namespace

Enumerate the Schedules in the alerting Namespace:

```
temporal schedule list --namespace <your-namespace>
```

[`ListSchedules`](/cli/command-reference/schedule#list) returns Schedule Ids and summary information. It does not return per-Schedule miss counters, so use it only to produce the set of Schedule Ids to inspect.

### 2. Describe each Schedule

For each Schedule Id returned, run:

```
temporal schedule describe \
  --schedule-id <your-schedule-id> \
  --namespace <your-namespace>
```

[`DescribeSchedule`](/cli/command-reference/schedule#describe) returns full Schedule state, including the `info` block with cumulative counters. The relevant fields:

| Field | Meaning |
|-------|---------|
| `missedCatchupWindow` | Actions skipped because they could not run within the Catchup Window. Non-zero here identifies the Schedule responsible for the alert. |
| `overlapSkipped` | Actions skipped because the previous run was still in progress and the Overlap Policy is `Skip`. |
| `bufferDropped` | Buffered Actions dropped because the buffer was full under `BufferOne` or `BufferAll`. |
| `bufferSize` | Current depth of the Action buffer. |
| `recentActions` | Most recent Action times and results. |
| `runningWorkflows` | Workflow Executions currently running for this Schedule. |

Scripting the fan-out against the JSON output (`temporal schedule describe -o json`) is usually faster than inspecting each Schedule interactively.

## Interpret the result

Once you have identified the Schedule with a non-zero `missedCatchupWindow`, use the rest of the `DescribeSchedule` output to determine impact and root cause.

### Assess impact

- Compare `recentActions` to the Schedule's Spec to determine how many Actions were skipped and over what time period.
- If the Schedule uses the `Skip` Overlap Policy and the preceding run was long-running, the miss may reflect that run exceeding the Catchup Window, not a Service outage.
- For business-critical Schedules, [Backfill](/schedule#backfill) the skipped interval once the underlying cause is resolved.

### Common root causes

- **Service or Namespace outage longer than the Catchup Window.** The default Catchup Window is one year, so a miss typically means the Schedule is configured with a tighter window (minimum ten seconds) and the outage exceeded it.
- **Namespace rate limiting.** If scheduled starts are throttled, Actions can queue past the Catchup Window. Cross-check [`temporal_cloud_v1_schedule_rate_limited_count`](/cloud/metrics/openmetrics/metrics-reference#temporal_cloud_v1_schedule_rate_limited_count) (Cloud) or [`schedule_rate_limited`](/references/cluster-metrics#schedule_rate_limited) (self-hosted) in the same time range.
- **Buffer overruns under `BufferAll`.** Long-running Workflow Executions under `BufferAll` can push buffered Actions past the Catchup Window. Cross-check [`temporal_cloud_v1_schedule_buffer_overruns_count`](/cloud/metrics/openmetrics/metrics-reference#temporal_cloud_v1_schedule_buffer_overruns_count) (Cloud) or [`schedule_buffer_overruns`](/references/cluster-metrics#schedule_buffer_overruns) (self-hosted) and examine `bufferSize`.

### Remediate

- Widen the Catchup Window if the current value is tighter than your Service's worst-case unavailability. The trade-off is that more late Actions will fire during recovery.
- Revisit the Overlap Policy if runs routinely exceed the Spec interval. `BufferAll` and `Skip` have different failure modes under sustained delay.
- Increase Namespace throughput limits if rate limiting is the contributing factor.
- [Backfill](/schedule#backfill) the missed interval if the skipped Actions need to run.

## Related reading

- [Schedule concept](/schedule)
- [Catchup Window](/schedule#catchup-window)
- [Temporal CLI schedule reference](/cli/command-reference/schedule)
- [Temporal Cloud OpenMetrics metrics reference](/cloud/metrics/openmetrics/metrics-reference)
- [Self-hosted cluster metrics reference](/references/cluster-metrics)

---

## Troubleshoot Serverless Workers

<ReleaseNoteHeader featureName="serverlessWorkers">
  To request access during Pre-release, create a [support ticket](/cloud/support#support-ticket) or contact your account team.
  APIs are experimental and may be subject to backwards-incompatible changes.
  [Sign up for updates](https://temporal.io/pages/serverless-workers-updates) to be notified when Serverless Workers reach Public Preview.
</ReleaseNoteHeader>

This page walks through the Serverless Worker invocation flow and helps you identify where a failure is occurring.

When a Serverless Worker invocation works correctly, the following sequence happens:

1. You deploy the Worker function on Lambda.
2. You configure a [Worker Deployment Version](/worker-versioning#deployment-versions) with a compute provider. This starts a [Worker Controller Instance (WCI)](/serverless-workers#how-invocation-works) Workflow and a validation invocation of the Lambda function.
3. The Lambda polls the Temporal Service successfully, binding the [Task Queue](/task-queue) configured on the Worker to the Worker Deployment Version.
4. The WCI continuously monitors the associated Task Queue on a schedule. The [Matching Service](/temporal-service/temporal-server#matching-service) also notifies the WCI Workflow of sync match failures immediately as they happen.
5. A Task arrives on the Task Queue and the WCI detects the backlog.
6. The WCI invokes the Lambda function.
7. The Lambda function starts, the Worker connects to Temporal and polls the Task Queue.
8. The Worker processes Tasks and shuts down gracefully.

Start by determining whether the Lambda function is being invoked at all, then narrow down from there.

## Is the Lambda function being invoked? {/* #is-lambda-invoked */}

Check the Lambda function's CloudWatch metrics or invocation logs.

In the AWS Console, go to **Lambda > Functions > your function > Monitor**. Look for recent invocations in the
**Invocations** graph. You can also check **CloudWatch > Log groups > /aws/lambda/your-function-name** for execution
logs.

If there are no invocations, continue to [Lambda is not being invoked](#lambda-not-invoked).

If the Lambda is being invoked but Workflows are not progressing, skip to
[Lambda is invoked but Tasks are not completing](#lambda-invoked-not-completing).

## Lambda is not being invoked {/* #lambda-not-invoked */}

Work through the following checks in order.

### Validate the connection to Lambda {/* #validate-connection */}

Start by verifying that Temporal can reach the Lambda function. Go to **Workers > Deployments > select your
deployment**, open the **Actions** menu on the version, and click **Validate Connection**. A successful validation
confirms that the Worker Deployment Version has a compute provider configured, that Temporal can assume the invocation
role, and that the Lambda function can be invoked.

If validation fails, verify that the Lambda function ARN and invocation role ARN in the Worker Deployment Version
configuration are correct. Verify the invocation role was created using the
[CloudFormation template](/production-deployment/worker-deployments/serverless-workers/aws-lambda#configure-iam)
and that the External ID matches the value in the Worker Deployment Version configuration.

If the Worker Deployment Version does not have a compute provider configured, no
[Worker Controller Instance (WCI)](/serverless-workers#how-invocation-works) Workflow exists and the Lambda is never
automatically invoked. A common cause is manually invoking the Lambda function before creating the Worker Deployment
Version in the UI or CLI. When the Lambda runs, the Worker connects to Temporal and polls the Task Queue. That polling
registers the Worker Deployment Version and binds the Task Queue on the server, but the version has no compute provider.
To fix the issue, create or update the Worker Deployment Version with the compute provider flags as described in the
[deploy guide](/production-deployment/worker-deployments/serverless-workers/aws-lambda#create-worker-deployment-version).

### Check that the version is set as current {/* #check-version-current */}

The Worker Deployment Version must be set as the current version for new Tasks to route to it. If you created the
version through the CLI, you need to
[set it as current](/production-deployment/worker-deployments/serverless-workers/aws-lambda#set-current-version).

You can verify the current version with `temporal worker deployment describe`.

### Check that the WCI is detecting Tasks {/* #check-wci-detecting-tasks */}

If the connection validates successfully but the Lambda is still not being invoked, the
[Worker Controller Instance (WCI)](/serverless-workers#worker-controller-instance) may not be detecting Tasks on the
Task Queue.

Check which Task Queues are bound to the Worker Deployment Version and whether there is a backlog:

```bash
temporal worker deployment describe-version \
  --namespace <NAMESPACE> \
  --deployment-name <DEPLOYMENT_NAME> \
  --build-id <BUILD_ID> \
  --report-task-queue-stats
```

If no Task Queues are listed, the binding has not been established. The server binds a Task Queue to a Worker Deployment
Version when a Worker with that deployment version successfully connects and polls the Task Queue.

A common cause is a failed first invocation. When you create a Worker Deployment Version, the WCI invokes the Lambda to
validate the configuration. If that first invocation fails (for example, due to missing environment variables, incorrect
TLS configuration, or missing dependencies), the Worker never connects to Temporal and never polls. Without a successful
poll, the Task Queue binding is never created.

To diagnose a failed first invocation, invoke the Lambda function manually from the AWS Console. The console displays
the execution result and any errors directly, making it easier to identify configuration issues than searching through
CloudWatch logs. Once the Lambda runs successfully and the Worker connects to Temporal, the Task Queue binding is
established.

## Lambda is invoked but Tasks are not completing {/* #lambda-invoked-not-completing */}

If CloudWatch shows Lambda invocations but Workflows are not progressing, the problem is in the Worker's execution
within the Lambda function.

### Check Lambda execution logs {/* #check-execution-logs */}

Check CloudWatch logs for errors during Worker startup. In the AWS Console, go to **CloudWatch > Log groups >
/aws/lambda/your-function-name** and look for recent error messages.

Common errors include:

- **Connection failures**: The Worker cannot reach the Temporal Service. Check that the `TEMPORAL_ADDRESS` and
  `TEMPORAL_API_KEY` environment variables (or `temporal.toml` config file) are correctly set on the Lambda function.
  For self-hosted deployments, verify
  [network reachability](/production-deployment/worker-deployments/serverless-workers/self-hosted-setup#ensure-network-reachability).
- **TLS errors**: The TLS certificate or key is missing, expired, or does not match the Namespace.
- **Authentication errors**: The API key is invalid or does not have access to the Namespace.

### Check for Lambda timeout {/* #check-lambda-timeout */}

If the Lambda function reaches its configured timeout before the Worker finishes processing, AWS terminates the
invocation.

The Worker begins graceful shutdown before the Lambda deadline. If Activities take longer than the available execution
window, the Activities are abandoned mid-execution and retried on the next invocation.

For long-running Activities, increase the Lambda timeout and the Worker's shutdown buffer together. See
[Tuning for long-running Activities](/serverless-workers#tuning-for-long-running-activities) for guidance on how these
values relate.

### Check that the deployment name and build ID match {/* #check-deployment-match */}

If CloudWatch shows rapid, repeated invocations with no Workflow progress, the deployment name or build ID in the Worker
code may not match the Worker Deployment Version configuration.

The deployment name and build ID in your Lambda function code must exactly match the values you used when creating the
Worker Deployment Version. Compare the values in your code against the WCI Workflow ID
(`temporal-sys-worker-controller-instance:<deployment-name>:<build-id>`) and the output of
`temporal worker deployment describe`.

A mismatch causes an invocation loop: the WCI invokes the Lambda, the Worker starts and polls with a different
deployment version than the WCI expects, the Task is not processed, and the WCI invokes the Lambda again.

To fix the loop, update the deployment name and build ID in the Worker code to match the Worker Deployment Version, then
redeploy the Lambda function.

---

## Develop with AI

Give your AI coding agent Temporal expertise with Skills and real-time documentation access with the Temporal Knowledge Base MCP
Server.

## Skills

Skills give AI agents domain-specific Temporal expertise. They work with Claude Code, Codex, Cursor, and any agent that
supports [Skills](https://agentskills.io).

### Temporal Developer Skill

The [Temporal Developer Skill](https://github.com/temporalio/skill-temporal-developer) gives your AI coding agent
expert-level knowledge of Temporal's programming model — workflow determinism rules, activity patterns, retry policies,
error handling, testing strategies, worker configuration, versioning, and common gotchas.

<Tabs groupId="skill-install" queryString>
<TabItem value="claude-code" label="Claude Code Plugin">

1. Add the Temporal skills marketplace to Claude Code:

   ```bash
   /plugin marketplace add temporalio/claude-temporal-plugin
   ```

2. Install the Temporal Developer Skill:

   ```bash
   /plugin install temporal@temporal-marketplace
   ```

</TabItem>
<TabItem value="cursor" label="Cursor">

Install the Temporal plugin from the [Cursor Marketplace](https://cursor.com/marketplace/temporal), or run the following
command in Cursor's agent chat:

```
/add-plugin temporal
```

</TabItem>
<TabItem value="codex" label="Codex">

Install from the Codex app or CLI:

- **Codex app:** Open the plugins menu, search for **temporal**, then click **+** (or **Add to Codex**).
- **Codex CLI:** Run `/plugin`, search for **temporal**, and mark it for installation.

</TabItem>
<TabItem value="npx" label="npx">

This works with Claude Code, Codex, Cline, and other agents.

Install the skill using the `skills` CLI:

```bash
npx skills add https://github.com/temporalio/skill-temporal-developer
```

</TabItem>
<TabItem value="manual" label="Manual">

Clone the skill repository into your Claude skills directory. Change the target directory if you are using agents other
than Claude:

```bash
git clone https://github.com/temporalio/skill-temporal-developer.git ~/.claude/skills/temporal-developer
```

</TabItem>
</Tabs>

Restart your coding agent after installing.

### Temporal Cloud Skill

The [Temporal Cloud Skill](https://github.com/temporalio/skill-temporal-cloud) helps your AI coding agent troubleshoot
Temporal Cloud connectivity, authentication, and configuration issues.

<Tabs groupId="skill-install" queryString>
<TabItem value="npx" label="npx">

This works with Claude Code, Codex, Cline, and other agents.

Install the skill using the `skills` CLI:

```bash
npx skills add https://github.com/temporalio/skill-temporal-cloud
```

</TabItem>
<TabItem value="manual" label="Manual">

Clone the skill repository into your Claude skills directory. Change the target directory if you are using agents other
than Claude:

```bash
git clone https://github.com/temporalio/skill-temporal-cloud.git ~/.claude/skills/temporal-cloud
```

</TabItem>
</Tabs>

Restart your coding agent after installing.

## Temporal Knowledge Base  MCP Server

Connect Temporal expertise directly to your AI assistant for accurate, up-to-date answers about Temporal. The
Temporal knowledge base MCP server gives AI tools real-time access to best practices compiled from our documentation, educational materials, community forum responses, and slack channels, so responses draw from current expertise
rather than training data.

:::info Authentication required

The Temporal Knowledge Base MCP Server is publicly available, but requires a one-time login with a Google or GitHub account to enforce rate limits and prevent abuse.
Only an opaque user ID is used for rate limiting. Your name, email, repositories, and other personal data are not accessed or collected.

:::

### Claude Code

Add the Temporal knowledge base MCP server globally so it's available in all your projects:

1. Register the MCP server with Claude Code:

   ```bash
   claude mcp add --scope user --transport http temporal-docs https://temporal.mcp.kapa.ai
   ```

2. Restart Claude Code and run `/mcp` to authenticate with your Google account.

To add the server to a specific project only, omit the `--scope user` flag. This stores the configuration in the
project's `.mcp.json` file:

```bash
claude mcp add --transport http temporal-docs https://temporal.mcp.kapa.ai
```

### Claude Desktop

1. Open Claude Desktop settings
2. Navigate to **Settings > Connectors**
3. Add a new MCP server with the URL: `https://temporal.mcp.kapa.ai`

### Other MCP-compatible tools

The Temporal Knowledge Base MCP Server URL is:

```
https://temporal.mcp.kapa.ai
```

The server requires authentication through MCP OAuth.
Not all MCP clients support this protocol.
If your client supports MCP OAuth, it will open a browser window to verify with Google or GitHub on first connection.
If your client does not support MCP OAuth, you may need to use a stdio proxy that handles the OAuth flow and passes credentials to the remote server.
Check your client's documentation for details on connecting to OAuth-protected MCP servers.
