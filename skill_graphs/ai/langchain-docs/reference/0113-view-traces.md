# View traces
Source: https://docs.langchain.com/langsmith/view-traces

Inspect agent threads in LangSmith using the Messages view or Details view.

From a tracing project, use the **Threads**, **Traces**, or **Runs** tabs to change what appears in the table. Click into any row to open the side panel.

The side panel is organized around [threads](/langsmith/observability-concepts#threads) as the primary unit of navigation. Instead of treating each [run](/langsmith/observability-concepts#runs) as an isolated object, the UI keeps the surrounding conversation visible so you can understand where a run fits in the agent's broader execution.

<Note>
  The Threads tab and the Turns view are only available for runs instrumented with a `thread_id` metadata field. Without thread instrumentation, you'll see traces as individual runs and won't have access to the Turns view.
</Note>

Three views are available at the top of the side panel:

* [**Messages**](#messages-view) (**Beta**): The conversation layer. Scan the full thread as inputs, outputs, reasoning, tool calls, and subagent activity. Use this to find where to look. Press `M` to switch to this view.
* [**Turns**](#turns-view): The per-turn summary. View each turn in the thread as a card showing its inputs and outputs, with expand/collapse. Use this when you want a structural overview without the full conversation rendering. Press `T` to switch to this view.
* [**Details**](#details-view): The debugging layer. Drill into a specific run to inspect inputs, outputs, timing, token counts, errors, and metadata. Use this to understand what happened at a specific point in execution. Press `D` to switch to this view.

<Note>
  The Messages tab is disabled for threads that don't have any renderable messages. The Messages view is in **beta**—the side panel defaults to the Details view.
</Note>

Use the Messages view to orient yourself in the conversation and identify where to focus, then switch to the Details view to inspect a specific run:

<Steps>
  <Step title="Start in the Messages view">
    Open a thread and switch to the Messages view to see the full thread.
  </Step>

  <Step title="Investigate">
    Scan the thread to identify unexpected behavior, for example, a bad tool result, an unexpected subagent handoff, a latency spike.
  </Step>

  <Step title="Inspect the run">
    Click the relevant message or tool call to open the Details view at the exact run that produced it. Review its inputs, outputs, timing, errors, and metadata.
  </Step>

  <Step title="Return to the thread">
    Toggle back to the Messages view to continue scanning the conversation.
  </Step>
</Steps>

## Messages view

<Note>The Messages view is in **beta**. The side panel defaults to the [Details view](#details-view).</Note>

Use the Messages view to scan the full thread and identify unexpected behavior—a bad tool result, an unexpected subagent handoff, or a latency spike—before drilling into a specific run.

### What the Messages view shows

Each turn in the thread renders as a single block containing the model's response, the tool calls it triggered, and the results those tools returned. You can scan the full thread and read the agent's behavior without opening a child run.

The metadata row for each block shows:

* **Token usage:** total tokens for the call
* **Cost:** total cost for the call
* **Model name**
* An **LLM call** link to the corresponding run in the [Details view](#details-view) (shown only when the AI message has visible text)

**Thought** blocks appear inline with assistant messages when a model uses extended thinking, collapsed by default. Click to expand the model's chain of thought for that turn.

**Subagents** appear inline in the conversation as distinct actions. Click into a subagent to open a nested view of that subagent's messages. Click back to return to the parent thread.

**Tool calls** appear with the assistant message that triggered them. Each tool call card includes a link to its run in the [Details view](#details-view). When an agent makes multiple tool calls together, either the same tool repeated or multiple different tools in parallel, those calls collapse into a single grouped row. Expand the group to see each individual call.

LangSmith preserves collapsed and expanded message state when you switch between the Messages and Details tabs.

To download the thread as a Markdown file, use the download button in the Messages view. The exported file includes the full conversation transcript with human and AI turns, tool calls, and tool results, formatted for reading in any Markdown viewer.

### Customize the Messages view

You can control how runs appear in the Messages view using metadata keys on individual runs.

* `ls_agent_type`: Controls where messages from an agent-like run appear. Accepted values:

  | Value        | Messages view behavior                                                         |
  | ------------ | ------------------------------------------------------------------------------ |
  | `"root"`     | Messages from this run appear in the main Messages view.                       |
  | `"subagent"` | Messages from this run appear as a subagent action in the conversation thread. |

  ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  @traceable(metadata={"ls_agent_type": "root"})
  def my_agent():
      ...
  ```

* `ls_message_format`: Overrides automatic format detection. Accepted values:
  * `"langchain"`: parse as LangChain message format
  * `"anthropic"`: parse as Anthropic message format
  * `"responses"`: parse as OpenAI Responses API format

* `ls_message_view_exclude`: Exclude an individual run from the Messages view. For code examples, refer to [Exclude runs from the Messages view](/langsmith/messages-view-integrations#exclude-runs-from-the-messages-view).

## Turns view

Use the Turns view to scan the structure of a thread one turn at a time, without the full conversation rendering of the Messages view. Each turn in the thread appears as a card showing the root run's inputs and outputs. Click a card's chevron to expand or collapse its contents.

The Turns view is useful when:

* The thread doesn't have renderable messages (for example, a trace from an integration that isn't supported by the Messages view).
* You want a quick structural overview of the thread before deciding which turn to drill into.
* You want to see raw inputs and outputs per turn without normalization into a chat-style conversation.

Click into any turn to open the [Details view](#details-view) at the run that produced it.

### Customize the Turns view

By default, LangSmith picks input and output fields to show on each turn card using heuristics. To override which fields appear, click the **Format** button at the top of the thread to open the format pane, select the specific input and output paths you want to display, and save. Your selection persists for the project.

## Details view

The Details view is the debugging layer. When you click into a specific run, the surrounding thread context remains available so you can understand where that run fits in the broader conversation. Inspect inputs, outputs, metadata, timing, errors, and child runs without losing track of the thread.

### Customize the Details view

Setting `run_type="llm"` on a run causes the Details view to render token counts and latency for that run. For the full message format specification, refer to [Log an LLM trace](/langsmith/log-llm-trace).

Tool messages are auto-expanded when a run's `run_type` is `tool`.

Setting `run_type="retriever"` on a run causes the Details view to render each retrieved document with its contents and metadata inline. For the required return format, refer to [Log retriever traces](/langsmith/log-retriever-trace).

### Actions

From the Details view, you can also:

* **Share a trace:** Generate a public link to the trace. Refer to [Manage a trace](/langsmith/manage-trace#share-a-trace).
* **View server logs:** Access server logs associated with a trace generated by a LangSmith deployment. Refer to [Manage a trace](/langsmith/manage-trace#view-server-logs).
* **Add to a dataset:** Save the run as an example in a dataset for use in evaluations. Refer to [Manage datasets in the application](/langsmith/manage-datasets-in-application#manually-from-a-tracing-project).
* **Add to an annotation queue:** Send the run to a queue for human review and feedback. Refer to [Annotation queues](/langsmith/annotation-queues#assign-runs-to-a-single-run-queue).

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/view-traces.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# View usage
Source: https://docs.langchain.com/langsmith/view-usage

What usage data is available in LangSmith, what each metric means, and what differs for self-hosted deployments.

LangSmith provides several views into your [organization's](/langsmith/administration-overview) usage, depending on your [plan](/langsmith/pricing-plans) and [deployment type](/langsmith/platform-setup). This page explains what data is available, what each metric means, and what limitations apply to [self-hosted](/langsmith/self-hosted) deployments.

## Usage views

| View                                    | Where to find it                                                                                           | Who can see it                          | Plan availability     |
| --------------------------------------- | ---------------------------------------------------------------------------------------------------------- | --------------------------------------- | --------------------- |
| [Usage graph](#usage-graph)             | **Enterprise**: Settings > Usage > Usage graph<br />**Self-serve**: Settings > Billing > Usage graph       | All org members                         | All plans             |
| [Granular usage](#granular-usage)       | **Enterprise**: Settings > Usage > Granular usage<br />**Self-serve**: Settings > Billing > Granular usage | All org members                         | All plans             |
| [Contract burndown](#contract-burndown) | **Enterprise**: Settings > Usage > Contract usage<br />**Self-serve**: Settings > Billing > Contract usage | Org admins only (`organization:manage`) | Enterprise only       |
| [Invoices](#invoices)                   | Settings > Billing > Invoices                                                                              | All org members                         | Self-serve cloud only |

## Usage graph

The usage graph shows aggregate trace consumption for your organization, broken down by workspace. It covers the current billing period and does not show spend—for spend, refer to the invoice.

Navigate to **Settings** → **Billing and Usage** → **Usage Graph**.

### Billable metrics

| Metric                                                  | What it counts                                                                                                                                                                                                                  |
| ------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **LangSmith Traces (Base Charge)**                      | Every trace sent to LangSmith during the billing period, regardless of data retention tier.                                                                                                                                     |
| **LangSmith Traces (Extended Data Retention Upgrades)** | Traces upgraded to extended retention (400 days by default, [customizable for Enterprise customers](/langsmith/data-purging-compliance#customize-extended-retention-policy)). These are charged in addition to the base charge. |
| **LangSmith Deployment Runs**                           | End-to-end invocations of deployed LangGraph agents. See [LangSmith Deployment billing](/langsmith/billing#langsmith-deployment-billing) for pricing details.                                                                   |
| **LangSmith Fleet Runs**                                | End-to-end invocations of [Fleet](/langsmith/fleet) agents. Tracked separately for cloud-hosted and self-hosted deployments.                                                                                                    |
| **LangSmith Deployment Nodes Executed**                 | Individual LangGraph node executions across deployed agents. Each step in a deployed agent's graph counts as one node execution. Tracked separately for cloud-hosted and self-hosted deployments.                               |

For more details on trace retention tiers, refer to [Data retention](/langsmith/usage-and-billing#data-retention).

<Note>
  The usage graph uses the term `tenant_id` interchangeably with workspace ID.
</Note>

## Contract burndown

Enterprise customers with prepaid commitments can view how much of their contract has been consumed.

Navigate to **Settings** → **Usage Configuration** → **Contract Usage**.

This view shows:

* **Usage summary**: Total usage, total credits, and any overages. Overages occur when usage exceeds your total prepaid commitment.
* **Commitment progress bars**: Visual indicators for each commitment showing percentage consumed and dollar amounts for used vs. remaining. Contracts can have multiple commitments that apply to different time periods (e.g., year 1 and year 2 of a multi-year contract) or different products.
* **Monthly usage chart**: Bar chart showing usage amounts for each month within your contract period.
* **Product rates**: Table of your entitled products and their pricing.

<Note>
  Contract burndown requires the [`organization:manage` permission](/langsmith/organization-workspace-operations) and is only available to Enterprise customers with prepaid commitments.
</Note>

## Invoices

Invoices are available on **self-serve cloud plans only**. Enterprise cloud organizations have a separate usage view for tracking spend.

Navigate to **Settings** → **Billing and Usage** → **Invoices** to see how your usage translates to spend. The first invoice shown is a draft of your current month's invoice, reflecting your running spend to date.

## Granular usage

Granular usage gives you trace counts broken down by a dimension you choose (workspace, project, user, or API key) over a time range you select. This is useful for internal chargebacks, identifying high-usage teams, or auditing trace activity.

Navigate to **Settings** → **Billing and Usage** → **Granular Usage**, or use the [granular usage API](/langsmith/granular-usage).

### What "traces" means here

The granular usage view counts **traces**: root-level runs and all their child spans counted as a single unit. This is the same unit used for [billing](/langsmith/billing). It does not count individual spans, tokens, or model calls separately.

### When usage is recorded

Granular usage records traces by **insertion time** (when the trace was received and stored by LangSmith), not by when it ran in your application. In practice this difference is usually negligible, but traces sent with significant delay (e.g., buffered SDK uploads) may appear in a later time bucket than expected.

For grouping options, time bucket sizes, and API reference, refer to [Granular billable usage](/langsmith/granular-usage).

## Self-hosted limitations

[Self-hosted](/langsmith/self-hosted) LangSmith [deployments](/langsmith/deployment) have a different set of usage views available compared to [Cloud](/langsmith/cloud), due to differences in billing infrastructure.

| **Feature**                        | **Self-hosted availability**                         |
| ---------------------------------- | ---------------------------------------------------- |
| Granular usage (trace attribution) | Available with feature flags or version ≥ 0.13.12    |
| Usage graph (aggregate traces)     | Available on Helm chart 0.9.5 and later              |
| Contract burndown                  | Available when Beacon phone-home is enabled          |
| Invoices and payment management    | Not available (billing is handled outside LangSmith) |

### Granular usage on self-hosted

Granular usage is available on self-hosted deployments but requires explicit opt-in:

* On **LangSmith 0.13.12 and later**, granular usage collection is enabled by default.
* On **earlier versions**, enable it by setting both of the following environment variables:

  ```env theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  DEFAULT_ORG_FEATURE_ENABLE_GRANULAR_USAGE_REPORTING=true
  GRANULAR_USAGE_TABLE_ENABLED=true
  ```

<Warning>
  Data collection begins from the moment the feature is enabled. There is no backfill of historical usage data prior to enabling it. Plan accordingly when choosing when to enable this feature.
</Warning>

### Aggregate usage on self-hosted

The usage graph is available on self-hosted deployments running Helm chart 0.9.5 or later. LangSmith automatically generates and syncs organization usage charts, available under **Settings** → **Usage and billing** → **Usage graph**:

* **Usage by Workspace**: trace counts (root runs) per workspace
* **Organization Usage**: total trace counts across the organization

Charts refresh every 5 minutes to include new workspaces and are not editable.

For programmatic access to trace counts, see [View trace counts across your organization](/langsmith/self-host-organization-charts).

## Related resources

* [Granular billable usage API reference](/langsmith/granular-usage)
* [Manage billing](/langsmith/billing)
* [Data retention and usage limits](/langsmith/usage-and-billing#data-retention)
* [Organization and workspace operations](/langsmith/organization-workspace-operations)

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/view-usage.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# How to run evaluations with Vitest/Jest
Source: https://docs.langchain.com/langsmith/vitest-jest

LangSmith provides integrations with [Vitest](https://vitest.dev/) and [Jest](https://jestjs.io/) that allow JavaScript and TypeScript developers to define their [datasets](/langsmith/evaluation-concepts#datasets) and evaluate using familiar syntax.

<img alt="Jest/Vitest reporter output" />

Compared to the [`evaluate()`](https://reference.langchain.com/python/langsmith/client/Client/evaluate) evaluation flow, the Vitest or Jest testing frameworks are useful when:

* **Each example requires different evaluation logic**: Standard evaluation flows assume consistent application and evaluator execution across all dataset examples. For more complex systems or comprehensive evaluations, specific system subsets may require evaluation with particular input types and metrics. These heterogeneous evaluations are simpler to write as distinct test case suites that track together.
* **You want to assert binary expectations**: Track assertions in LangSmith and raise assertion errors locally (e.g. in CI pipelines). Testing tools help when both evaluating system outputs and asserting basic properties about them.
* **You want to take advantage of mocks, watch mode, local results, or other features of the Vitest/Jest ecosystems**.

<Info>
  Requires JS/TS SDK version `langsmith>=0.3.1`.
</Info>

<Info>
  The Python SDK has an analogous [pytest integration](/langsmith/pytest).
</Info>

## Setup

Set up the integrations as follows. Note that while you can add LangSmith evals alongside your other unit tests (as standard `*.test.ts` files) using your existing test config files, the below examples will also set up a separate test config file and command to run your evals. It will assume you end your test files with `.eval.ts`.

This ensures that the custom test reporter and other LangSmith touchpoints do not modify your existing test outputs.

### Vitest

Install the required development dependencies if you have not already:

<CodeGroup>
  ```bash yarn theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  yarn add -D vitest dotenv
  ```

  ```bash npm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  npm install -D vitest dotenv
  ```

  ```bash pnpm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  pnpm add -D vitest dotenv
  ```
</CodeGroup>

The following examples also require `openai` (and `langsmith`) as a dependency:

<CodeGroup>
  ```bash yarn theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  yarn add langsmith openai
  ```

  ```bash npm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  npm install langsmith openai
  ```

  ```bash pnpm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  pnpm add langsmith openai
  ```
</CodeGroup>

Then, create a separate `ls.vitest.config.ts` file with the following base config:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    include: ["**/*.eval.?(c|m)[jt]s"],
    reporters: ["langsmith/vitest/reporter"],
    setupFiles: ["dotenv/config"],
    testTimeout: 30000,
  },
});
```

* `include` ensures that only files ending with some variation of `eval.ts` in your project are run
* `reporters` is responsible for nicely formatting your output as shown above
* `setupFiles` runs `dotenv` to load environment variables before running your evals
* `testTimeout` sets a global default timeout for each test. Because LLM calls can be slow, we increase this from the Vitest default

<Warning>
  JSDom environments are not supported at this time. You should either omit the `"environment"` field from your config or set it to `"node"`.
</Warning>

Finally, add the following to the `scripts` field in your `package.json` to run Vitest with the config you just created:

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "name": "YOUR_PROJECT_NAME",
  "scripts": {
    "eval": "vitest run --config ls.vitest.config.ts"
  },
  "dependencies": {
    ...
  },
  "devDependencies": {
    ...
  }
}
```

Note that this script disables Vitest's default watch mode for running evals since many evaluators may include longer running LLM calls.

### Jest

Install the required development dependencies if you have not already:

<CodeGroup>
  ```bash yarn theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  yarn add -D jest dotenv
  ```

  ```bash npm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  npm install -D jest dotenv
  ```

  ```bash pnpm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  pnpm add -D jest dotenv
  ```
</CodeGroup>

The examples below also require `openai` (and `langsmith`) as a dependency:

<CodeGroup>
  ```bash yarn theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  yarn add langsmith openai
  ```

  ```bash npm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  npm install langsmith openai
  ```

  ```bash pnpm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  pnpm add langsmith openai
  ```
</CodeGroup>

<Info>
  The following setup instructions are for basic JS files and CJS. To add support for TypeScript and ESM, see Jest's official docs or use [Vitest](#vitest).
</Info>

Then, create a separate config file named `ls.jest.config.cjs`:

```javascript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
module.exports = {
  testMatch: ["**/*.eval.?(c|m)[jt]s"],
  reporters: ["langsmith/jest/reporter"],
  setupFiles: ["dotenv/config"],
  testTimeout: 30000,
};
```

* `testMatch` ensures that only files ending with some variation of `eval.js` in your project are run
* `reporters` is responsible for nicely formatting your output as shown above
* `setupFiles` runs `dotenv` to load environment variables before running your evals
* `testTimeout` sets a global default timeout for each test. Because LLM calls can be slow, we increase this from the Jest default

<Warning>
  JSDom environments are not supported at this time. You should either omit the `"testEnvironment"` field from your config or set it to `"node"`.
</Warning>

Finally, add the following to the `scripts` field in your `package.json` to run Jest with the config you just created:

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "name": "YOUR_PROJECT_NAME",
  "scripts": {
    "eval": "jest --config ls.jest.config.cjs"
  },
  "dependencies": {
    ...
  },
  "devDependencies": {
    ...
  }
}
```

## Define and run evals

You can now define evals as tests using familiar Vitest/Jest syntax, with a few caveats:

* You should import `describe` and `test` from the [`langsmith/jest`](https://reference.langchain.com/javascript/modules/langsmith.jest.html) or [`langsmith/vitest`](https://reference.langchain.com/javascript/modules/langsmith.vitest.html) entrypoint.
* You must wrap your test cases in a `describe` block.
* When declaring tests, the signature is slightly different—there is an extra argument containing example inputs and expected outputs.

Try it out by creating a file named `sql.eval.ts` (or `sql.eval.js` if you are using Jest without TypeScript) and pasting this code into it:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import * as ls from "langsmith/vitest";
import { expect } from "vitest";
// import * as ls from "langsmith/jest";
// import { expect } from "@jest/globals";
import OpenAI from "openai";
import { traceable } from "langsmith/traceable";
import { wrapOpenAI } from "langsmith/wrappers/openai";

// Add "openai" as a dependency and set OPENAI_API_KEY as an environment variable
const tracedClient = wrapOpenAI(new OpenAI());

const generateSql = traceable(
  async (userQuery: string) => {
    const result = await tracedClient.chat.completions.create({
      model: "gpt-5.4-mini",
      messages: [
        {
          role: "system",
          content:
            "Convert the user query to a SQL query. Do not wrap in any markdown tags.",
        },
        {
          role: "user",
          content: userQuery,
        },
      ],
    });
    return result.choices[0].message.content;
  },
  { name: "generate_sql" }
);

ls.describe("generate sql demo", () => {
  ls.test(
    "generates select all",
    {
      inputs: { userQuery: "Get all users from the customers table" },
      referenceOutputs: { sql: "SELECT * FROM customers;" },
    },
    async ({ inputs, referenceOutputs }) => {
      const sql = await generateSql(inputs.userQuery);
      ls.logOutputs({ sql }); // <-- Log run outputs, optional
      expect(sql).toEqual(referenceOutputs?.sql); // <-- Assertion result logged under 'pass' feedback key
    }
  );
});
```

You can think of each [ls.test](https://reference.langchain.com/javascript/modules/langsmith.vitest.html#test) case as corresponding to a dataset example, and [`ls.describe()`](https://reference.langchain.com/javascript/modules/langsmith.vitest.html#describe) as defining a LangSmith dataset. If you have LangSmith [tracing environment variables](#setup) set when you run the test suite, the SDK does the following:

* Creates a [dataset](/langsmith/evaluation-concepts#datasets) with the same name as the name passed to `ls.describe()` in LangSmith if it does not exist.
* Creates an [example](/langsmith/evaluation-concepts#datasets) in the dataset for each input and expected output passed into a test case if a matching one does not already exist.
* Creates a new [experiment](/langsmith/evaluation-concepts#experiment) with one result for each test case.
* Collects the pass/fail rate under the `pass` feedback key for each test case.

When you run this test it will have a default `pass` boolean feedback key based on the test case passing / failing. It will also track any outputs that you log with [`ls.logOutputs()`](https://reference.langchain.com/javascript/modules/langsmith.vitest.html#logOutputs) or return from the test function as "actual" result values from your app for the experiment.

Create a `.env` file with your `OPENAI_API_KEY` and LangSmith credentials if you don't already have one:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
OPENAI_API_KEY="YOUR_KEY_HERE"
LANGSMITH_API_KEY="YOUR_LANGSMITH_KEY"
LANGSMITH_TRACING="true"
```

Now use the `eval` script we set up in the previous step to run the test:

<CodeGroup>
  ```bash yarn theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  yarn run eval
  ```

  ```bash npm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  npm run eval
  ```

  ```bash pnpm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  pnpm run eval
  ```
</CodeGroup>

And your declared test should run!

Once it finishes, if you've set your LangSmith environment variables, you should see a link directing you to an experiment created in LangSmith alongside the test results.

Here's what an experiment against that test suite looks like:

<img alt="Experiment" />

## Trace feedback

By default LangSmith collects the pass/fail rate under the `pass` feedback key for each test case. You can add additional feedback with either [`ls.logFeedback()`](https://reference.langchain.com/javascript/modules/langsmith.vitest.html#logFeedback) or [`ls.wrapEvaluator()`](https://reference.langchain.com/javascript/modules/langsmith.vitest.html#wrapEvaluator). To do so, try the following as your `sql.eval.ts` file (or `sql.eval.js` if you are using Jest without TypeScript):

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import * as ls from "langsmith/vitest";
// import * as ls from "langsmith/jest";
import OpenAI from "openai";
import { traceable } from "langsmith/traceable";
import { wrapOpenAI } from "langsmith/wrappers/openai";

// Add "openai" as a dependency and set OPENAI_API_KEY as an environment variable
const tracedClient = wrapOpenAI(new OpenAI());

const generateSql = traceable(
  async (userQuery: string) => {
    const result = await tracedClient.chat.completions.create({
      model: "gpt-5.4-mini",
      messages: [
        {
          role: "system",
          content:
            "Convert the user query to a SQL query. Do not wrap in any markdown tags.",
        },
        {
          role: "user",
          content: userQuery,
        },
      ],
    });
    return result.choices[0].message.content ?? "";
  },
  { name: "generate_sql" }
);

const myEvaluator = async (params: {
  outputs: { sql: string };
  referenceOutputs: { sql: string };
}) => {
  const { outputs, referenceOutputs } = params;
  const instructions = [
    "Return 1 if the ACTUAL and EXPECTED answers are semantically equivalent, ",
    "otherwise return 0. Return only 0 or 1 and nothing else.",
  ].join("\n");
  const grade = await tracedClient.chat.completions.create({
    model: "gpt-5.4-mini",
    messages: [
      {
        role: "system",
        content: instructions,
      },
      {
        role: "user",
        content: `ACTUAL: ${outputs.sql}\nEXPECTED: ${referenceOutputs?.sql}`,
      },
    ],
  });
  const score = parseInt(grade.choices[0].message.content ?? "");
  return { key: "correctness", score };
};

ls.describe("generate sql demo", () => {
  ls.test(
    "generates select all",
    {
      inputs: { userQuery: "Get all users from the customers table" },
      referenceOutputs: { sql: "SELECT * FROM customers;" },
    },
    async ({ inputs, referenceOutputs }) => {
      const sql = await generateSql(inputs.userQuery);
      ls.logOutputs({ sql });
      const wrappedEvaluator = ls.wrapEvaluator(myEvaluator);
      // Will automatically log "correctness" as feedback
      await wrappedEvaluator({
        outputs: { sql },
        referenceOutputs,
      });
      // You can also manually log feedback with `ls.logFeedback()`
      ls.logFeedback({
        key: "harmfulness",
        score: 0.2,
      });
    }
  );
  ls.test(
    "offtopic input",
    {
      inputs: { userQuery: "what's up" },
      referenceOutputs: { sql: "sorry that is not a valid query" },
    },
    async ({ inputs, referenceOutputs }) => {
      const sql = await generateSql(inputs.userQuery);
      ls.logOutputs({ sql });
      const wrappedEvaluator = ls.wrapEvaluator(myEvaluator);
      // Will automatically log "correctness" as feedback
      await wrappedEvaluator({
        outputs: { sql },
        referenceOutputs,
      });
      // You can also manually log feedback with `ls.logFeedback()`
      ls.logFeedback({
        key: "harmfulness",
        score: 0.2,
      });
    }
  );
});
```

Note the use of [`ls.wrapEvaluator()`](https://reference.langchain.com/javascript/modules/langsmith.vitest.html#wrapEvaluator) around the `myEvaluator` function. This makes it so that the LLM-as-judge call is traced separately from the rest of the test case to avoid clutter, and conveniently creates feedback if the return value from the wrapped function matches `{ key: string; score: number | boolean }`. In this case, instead of showing up in the main test case run, the evaluator trace will instead show up in a trace associated with the `correctness` feedback key.

You can see the evaluator runs in LangSmith by clicking their corresponding feedback chips in the UI.

## Running multiple examples against a test case

You can run the same test case over multiple examples and parameterize your tests using [`ls.test.each()`](https://reference.langchain.com/javascript/modules/langsmith.vitest.html#test). This is useful when you want to evaluate your app the same way against different inputs:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import * as ls from "langsmith/vitest";
// import * as ls from "langsmith/jest";

const DATASET = [
  {
    inputs: { userQuery: "what's up" },
    referenceOutputs: { sql: "sorry that is not a valid query" }
  },
  {
    inputs: { userQuery: "what color is the sky?" },
    referenceOutputs: { sql: "sorry that is not a valid query" }
  },
  {
    inputs: { userQuery: "how are you today?" },
    referenceOutputs: { sql: "sorry that is not a valid query" }
  }
];

ls.describe("generate sql demo", () => {
  ls.test.each(DATASET)(
    "offtopic inputs",
    async ({ inputs, referenceOutputs }) => {
      ...
    },
  );
});
```

If you have tracking enabled, each example in the local dataset will be synced to the one created in LangSmith.

## Use an existing dataset (Vitest only)

Instead of defining [examples](/langsmith/evaluation-concepts#examples) inline, you can run tests against an existing dataset in LangSmith:

* Use [`client.listExamples()`](https://reference.langchain.com/javascript/classes/langsmith.client.Client.html#listexamples) to fetch examples from a dataset that already exists in LangSmith.
* Collect the examples into an array (e.g., `testExamples`) by iterating through the async generator.
* Pass the array to [`ls.test.each()`](https://reference.langchain.com/javascript/modules/langsmith.vitest.html#test) to run your test logic against each example from the dataset.

```typescript {3,30-43,47} theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import * as ls from "langsmith/vitest";
import { expect } from "vitest";
import { Client, Example } from "langsmith";
import OpenAI from "openai";
import { traceable } from "langsmith/traceable";
import { wrapOpenAI } from "langsmith/wrappers/openai";

const tracedClient = wrapOpenAI(new OpenAI());

const generateSql = traceable(
  async (userQuery: string) => {
    const result = await tracedClient.chat.completions.create({
      model: "gpt-4o-mini",
      messages: [
        {
          role: "system",
          content:
            "Convert the user query to a SQL query. Do not wrap in any markdown tags.",
        },
        {
          role: "user",
          content: userQuery,
        },
      ],
    });
    return result.choices[0].message.content;
  },
  { name: "generate_sql" }
);

// Fetch examples from an existing dataset
const client = new Client();

const examples = client.listExamples({
  datasetName: "generate sql demo",
});

const testExamples: Example[] = [];

for await (const example of examples) {
  testExamples.push(example);
}

ls.describe(
  "generate sql demo",
  () => {
    ls.test.each(testExamples)(
      "generates valid sql",
      async ({ inputs, referenceOutputs }) => {
        const sql = await generateSql(inputs.userQuery);
        ls.logOutputs({ sql });
        expect(sql).toEqual(referenceOutputs?.sql);
      }
    );
  }
);
```

## Log outputs

Every time we run a test we're syncing it to a dataset example and tracing it as a run. To trace final outputs for the run, you can use [`ls.logOutputs()`](https://reference.langchain.com/javascript/modules/langsmith.vitest.html#logOutputs) like this:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import * as ls from "langsmith/vitest";
// import * as ls from "langsmith/jest";

ls.describe("generate sql demo", () => {
  ls.test(
    "offtopic input",
    {
      inputs: { userQuery: "..." },
      referenceOutputs: { sql: "..." }
    },
    async ({ inputs, referenceOutputs }) => {
      ls.logOutputs({ sql: "SELECT * FROM users;" })
    },
  );
});
```

The logged outputs will appear in your reporter summary and in LangSmith.

You can also directly return a value from your test function:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import * as ls from "langsmith/vitest";
// import * as ls from "langsmith/jest";

ls.describe("generate sql demo", () => {
  ls.test(
    "offtopic input",
    {
      inputs: { userQuery: "..." },
      referenceOutputs: { sql: "..." }
    },
    async ({ inputs, referenceOutputs }) => {
      return { sql: "SELECT * FROM users;" }
    },
  );
});
```

However keep in mind if you do this that if your test fails to complete due to a failed assertion or other error, your output will not appear.

## Trace intermediate calls

LangSmith will automatically trace any traceable intermediate calls that happen in the course of test case execution.

## Focusing or skipping tests

You can chain the Vitest/Jest `.skip` and `.only` methods on `ls.test()` and `ls.describe()`:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import * as ls from "langsmith/vitest";
// import * as ls from "langsmith/jest";

ls.describe("generate sql demo", () => {
  ls.test.skip(
    "offtopic input",
    {
      inputs: { userQuery: "..." },
      referenceOutputs: { sql: "..." }
    },
    async ({ inputs, referenceOutputs }) => {
      return { sql: "SELECT * FROM users;" }
    },
  );
  ls.test.only(
    "other",
    {
      inputs: { userQuery: "..." },
      referenceOutputs: { sql: "..." }
    },
    async ({ inputs, referenceOutputs }) => {
      return { sql: "SELECT * FROM users;" }
    },
  );
});
```

## Configuring test suites

You can configure test suites with values like metadata or a custom client by passing an extra argument to `ls.describe()` for the full suite or by passing a `config` field into `ls.test()` for individual tests:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
ls.describe("test suite name", () => {
  ls.test(
    "test name",
    {
      inputs: { ... },
      referenceOutputs: { ... },
      // Extra config for the test run
      config: { tags: [...], metadata: { ... } }
    },
    {
      name: "test name",
      tags: ["tag1", "tag2"],
      skip: true,
      only: true,
    }
  );
}, {
  testSuiteName: "overridden value",
  metadata: { ... },
  // Custom client
  client: new Client(),
});
```

The test suite will also automatically extract environment variables from `process.env.ENVIRONMENT`, `process.env.NODE_ENV` and `process.env.LANGSMITH_ENVIRONMENT` and set them as metadata on created experiments. You can then filter experiments by metadata in LangSmith's UI.

See [the API refs](https://docs.smith.langchain.com/reference/js/functions/vitest.describe) for a full list of configuration options.

## Dry-run mode

If you want to run the tests without syncing the results to LangSmith, you can set omit your LangSmith tracing environment variables or set `LANGSMITH_TEST_TRACKING=false` in your environment.

The tests will run as normal, but the experiment logs will not be sent to LangSmith.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/vitest-jest.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
