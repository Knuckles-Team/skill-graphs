# Manage billing in your account
Source: https://docs.langchain.com/langsmith/billing

This page describes how to manage billing for your LangSmith organization:

* [Set up billing for your account](#set-up-billing-for-your-account): Complete the billing setup process for Developer and Plus plans, including special instructions for legacy accounts.
* [Track contract usage (Enterprise)](#track-contract-usage-enterprise): View prepaid contract consumption.
* [Update your information](#update-your-information-paid-plans-only): Modify invoice email addresses, business information, and tax IDs for your organization.
* [Enforce spend limits](#enforce-spend-limits): Learn how to manage your spend through usage limits and data retention.

## Set up billing for your account

<Note>
  Before using this guide, note the following:

  * If you are interested in the [Enterprise](https://www.langchain.com/pricing) plan, please [contact sales](https://www.langchain.com/contact-sales). This guide is only for our self-serve billing plans.
</Note>

To set up billing for your LangSmith organization, navigate to the [Billing and Usage](https://smith.langchain.com/settings/payments) page under **Settings**. Depending on your organization's settings, there are different setup guides:

* [Developer plan](#developer-plan%3A-set-up-billing-on-your-personal-organization)
* [Plus plan](#plus-plan%3A-set-up-billing-on-a-shared-organization)

### Developer plan: set up billing on your personal organization

Personal organizations are limited to 5,000 traces per month until a credit card is added. To add a card:

1. Click **Add card to remove trace limit**.
2. Add your credit card information.
3. Once complete, you will no longer be rate limited to 5,000 traces, and you will be charged for any excess traces at rates specified on the [pricing](https://www.langchain.com/pricing-langsmith) page.

### Plus plan: set up billing on a shared organization

Team organizations are given an initial 10,000 traces per month. Any excess traces will be charged at rates specified on the [pricing](https://www.langchain.com/pricing-langsmith) page.

<Note>
  New organizations that you manually create are required to be on the Plus Plan. If you see a message about needing to upgrade to Plus to use this organization, follow these steps.
</Note>

1. Click **Upgrade to Plus**.
2. Invite members to your organization, as desired.
3. Enter your credit card information. Then, enter business information, invoice email, and tax ID. If this organization belongs to a business, check the **This is a business** checkbox and enter the information accordingly. For more information, refer to the [Update your information section](#update-your-information-paid-plans-only).

## Track contract usage (Enterprise)

Contract burndown tracking is available for [**Enterprise plan**](/langsmith/pricing-plans) customers with prepaid commitments. You must have the [`organization:manage` permission](/langsmith/organization-workspace-operations) to access this feature.

For details on viewing your prepaid contract consumption, refer to [Contract burndown](/langsmith/view-usage#contract-burndown).

<Note>
  For more details on the Enterprise plan, [contact the sales team](https://www.langchain.com/contact-sales).
</Note>

## Update your information (Paid plans only)

To update business information for your LangSmith organization, head to the [Billing and Usage](https://smith.langchain.com/settings/payments) page under **Settings**.

### Invoice email

To update the email address for invoices, follow these steps:

1. Navigate to the **Plans and Billing** tab.
2. Locate the section beneath the payment method, where the current invoice email is displayed.
3. Enter the new email address for invoices in the provided field.
4. The new email address will be automatically saved.

You will receive all future invoices to the updated email address.

### Business information and tax ID

<Note>
  In certain jurisdictions, LangSmith is required to collect sales tax. If you are a business, providing your tax ID may qualify you for a sales tax exemption.
</Note>

To update your organization's business information, follow these steps:

1. Navigate to the **Plans and Billing** tab.
2. Below the invoice email section, you will find a checkbox labeled **Business**.
3. Check the **Business** checkbox if your organization belongs to a business.
4. A business information section will appear, allowing you to enter or update the following details:
   * Business Name
   * Address
   * Tax ID for applicable jurisdictions
5. A Tax ID field will appear for applicable jurisdictions after you select a country.
6. After entering the necessary information, click the **Save** button to save your changes.

This ensures that your business information is up-to-date and accurate for billing and tax purposes.

## Enforce spend limits

<Check>
  You may find it helpful to read the following pages, before continuing with this section on optimizing your tracing spend:

  * [Data Retention Conceptual Docs](/langsmith/usage-and-billing#data-retention)
  * [Usage Limiting Conceptual Docs](/langsmith/usage-and-billing#usage-limits)
</Check>

<Note>
  Some of the features mentioned in this guide are not currently available on Enterprise plan due to its custom nature of billing. If you are on the Enterprise plan and have questions about cost optimization, contact your sales rep or support via [support.langchain.com](https://support.langchain.com).
</Note>

### Understand your current usage

The first step of any optimization process is to understand current usage. For details on the usage graph, granular usage, invoices, and contract burndown, refer to [View usage](/langsmith/view-usage).

LangSmith measures usage per workspace, because workspaces often represent development environments or teams within an organization.

### Set limits on usage

<img alt="P2usagelimitsempty v2" />

#### Set spend limit for workspace

1. To set limits, navigate to **Settings** -> **Billing and Usage** -> **Usage limits**.
2. Input a spend limit for your selected workspace. LangSmith will determine an appropriate number of base and extended trace limits to match that spend. The trace limits include the free trace allocation that comes with your plan (see details on [pricing page](https://smith.langchain.com/settings/payments)).

<Note>
  For organizations with **multiple workspaces only**: For simplicity, LangSmith incorporates the free traces into the cost calculation of the **first workspace only**. In actuality, the free traces can be "consumed" by any workspace. Therefore, although workspace-level spend limits are approximate for multi-workspace organizations, the organization-level spend limit is absolute.
</Note>

#### Configure trace tier distribution

LangSmith has two trace tiers: base traces and extended traces. Base traces have the base retention and are short-lived (14 days), while extended traces have extended retention and are long-lived (400 days by default, [customizable for Enterprise customers](/langsmith/data-purging-compliance#customize-extended-retention-policy)). For more information, refer to the [data retention conceptual docs](/langsmith/usage-and-billing#data-retention).

Set the desired default trace tier by selecting an option below the **Default data retention** label. All traces will have this tier by default when they are registered. Note that because extended traces cost more than base traces, selecting **Extended** as your default data retention option will result in less overall traces allowed in the billing period. By default, updating this setting will only apply to future incoming traces. To apply to all existing traces in the workspace, select the checkbox.

If the default data retention is set to **Base** you can optionally use the slider to distribute trace limits across base and extended tracess. LangSmith automatically provides a suggestion for this distribution but you can tailor this to your needs. For example, if you are running lots of automations or other features that may upgrade a trace to extended, you may want to increase your extended trace limits. To see the complete list of features that may upgrade a trace, [see here](https://docs.langchain.com/langsmith/usage-and-billing#how-it-works:~:text=Data%20retention%20auto%2Dupgrades).

<Note>
  The extended data retention limit can cause features other than tracing to stop working once reached. If you plan to use this feature, read more about its [functionality and side effects](/langsmith/usage-and-billing#side-effects-of-extended-data-retention-traces-limit).
</Note>

### Other methods of managing traces

#### Customize extended retention period ([Enterprise](/langsmith/pricing-plans) only)

[Enterprise](/langsmith/pricing-plans) customers can customize the extended data retention period at the workspace level to meet compliance requirements. The default is 400 days, but this can be adjusted based on your organization's needs. For more information, refer to [Customize extended retention policy](/langsmith/data-purging-compliance#customize-extended-retention-policy).

#### Change project-level default retention

Data retention settings are adjustable per tracing project. At the project level, you choose between two tiers: base (14 days) or extended (400 days). To customize the extended duration beyond 400 days, use [workspace-level configuration](/langsmith/data-purging-compliance#customize-extended-retention-policy) (Enterprise only).

Navigate to **Projects** > ***Your project name*** > Select **Retention** and select the desired default retention. This will only affect retention (and pricing) for **traces going forward**.

<img alt="P1projectretention" />

#### Apply extended data retention to a percentage of traces

You may not want all traces to expire after 14 days. You can automatically extend the retention of traces that match some criteria by creating an [automation rule](/langsmith/rules). You might want to apply extended data retention to specific types of traces, such as:

* 10% of all traces: For general analysis or analyzing trends long term.
* Errored traces: To investigate and debug issues thoroughly.
* Traces with specific metadata: For long-term examination of particular features or user flows.

To configure this:

1. Navigate to **Projects** > ***Your project name*** > Select **+ New** > Select **New Automation**.
2. Name your rule and optionally apply filters or a sample rate. For more information on configuring filters, refer to [filtering techniques](/langsmith/filter-traces-in-application#filter-operators).

<Note>
  When an automation rule matches any [run](/langsmith/observability-concepts#runs) within a [trace](/langsmith/observability-concepts#traces), then all runs within the trace are upgraded to extended data retention (400 days by default, [customizable for Enterprise customers](/langsmith/data-purging-compliance#customize-extended-retention-policy)).
</Note>

For example, this is the expected configuration to keep 10% of all traces for extended data retention:

<img alt="P2sampletraces" />

If you want to keep a subset of traces for **longer than 400 days** for data collection purposes, you can create another run rule that sends some runs to a dataset of your choosing. A dataset allows you to store the trace inputs and outputs (e.g., as a key-value dataset), and will persist indefinitely, even after the trace gets deleted.

### LangSmith Deployment billing

In addition to traces, LangSmith charges for deployed agents via LangSmith Deployment (formerly LangGraph Platform).

* **Deployment Runs**: A one end-to-end invocation of a deployed LangGraph agent and is billed at \$0.005 each. Nodes and subgraphs within a single agent execution are not charged separately. Calls to other LangGraph agents are charged separately to the deployment hosting the called agent. When using human-in-the-loop with interrupts, resuming after an interrupt creates a separate Deployment Run.
* **Deployment Uptime**: You are also charged for the time your deployment's database is live and persisting state. See the [pricing page](https://www.langchain.com/pricing) for uptime costs by deployment type (Development vs Production).

For high-volume deployment usage, please [contact our sales team](https://www.langchain.com/contact-sales) to discuss custom pricing options.

### Summary

If you have questions about further managing your spend, please contact support via [support.langchain.com](https://support.langchain.com).

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/billing.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Automatically run evaluators on experiments
Source: https://docs.langchain.com/langsmith/bind-evaluator-to-dataset

LangSmith supports two ways to grade experiments created via the SDK:

* **Programmatically**, by specifying evaluators in your code (see [How to evaluate an LLM application](/langsmith/evaluate-llm-application) for details)
* By **binding evaluators to a dataset** in the UI. This will automatically run the evaluators on any new experiments created, in addition to any evaluators you've set up via the SDK. This is useful when you're iterating on your application (target function), and have a standard set of evaluators you want to run for all experiments.

## Configuring an evaluator on a dataset

1. In the [LangSmith UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-bind-evaluator-to-dataset), select a dataset.
2. Click the **Evaluators** tab.
3. Click **+ Evaluator** to open the **Add Evaluator** panel.
4. Choose one of the following:
   * **Create from scratch**: Build a new [LLM-as-a-Judge](/langsmith/llm-as-judge), [Code](/langsmith/online-evaluations-code), or [Composite](/langsmith/composite-evaluators-ui) evaluator, or select **From labeled data** to create an LLM-as-a-judge evaluator [aligned to human feedback](/langsmith/improve-judge-evaluator-feedback).
   * **Attach an existing evaluator**: Select an evaluator already in your workspace to reuse it.
   * **Create from a template**: Start from a ready-made evaluator.

<Note>
  When you configure an evaluator for a dataset, it will only affect the experiment runs that are created after the evaluator is configured. It will not affect the evaluation of experiment runs that were created before the evaluator was configured.
</Note>

## LLM-as-a-judge evaluators

The process for binding evaluators to a dataset is very similar to the process for configuring a LLM-as-a-judge evaluator in the Playground. View instructions for [configuring an LLM-as-a-judge evaluator in the Playground.](/langsmith/llm-as-judge?mode=ui)

## Custom code evaluators

The process for binding a code evaluators to a dataset is very similar to the process for configuring a code evaluator in online evaluation. View instruction for [configuring code evaluators](/langsmith/online-evaluations-code).

The only difference between configuring a code evaluator in online evaluation and binding a code evaluator to a dataset is that the custom code evaluator can reference outputs that are part of the dataset's `Example`.

For custom code evaluators bound to a dataset, the evaluator function takes in two arguments:

* A `Run` ([reference](/langsmith/run-data-format)). This represents the new run in your experiment. For example, if you ran an experiment via SDK, this would contain the input/output from your chain or model you are testing.
* An `Example` ([reference](/langsmith/example-data-format)). This represents the reference example in your dataset that the chain or model you are testing uses. The `inputs` to the Run and Example should be the same. If your Example has a reference `outputs`, then you can use this to compare to the run's output for scoring.

The code below shows an example of a simple evaluator function that checks that the outputs exactly equal the reference outputs.

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import numpy as np

  def perform_eval(run, example):
      # run is a Run object
      # example is an Example object
      output = run['outputs']['output']
      ref_output = example['outputs']['outputs']
      output_match = np.array_equal(output, ref_output)

      return { "exact_match": output_match }
  ```

  ```javascript JavaScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  function perform_eval(run, example) {
      // run is a Run object
      // example is an Example object
      const output = run.outputs.output;
      const refOutput = example.outputs.outputs;

      // Deep equality check for arrays/objects
      const outputMatch = JSON.stringify(output) === JSON.stringify(refOutput);

      return { "exact_match": outputMatch };
  }
  ```
</CodeGroup>

## Next steps

* Analyze your experiment results in the [experiments tab](/langsmith/analyze-an-experiment)
* Compare your experiment results in the [comparison view](/langsmith/compare-experiment-results)

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/bind-evaluator-to-dataset.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Use server-side caching
Source: https://docs.langchain.com/langsmith/caching

Cache values server-side in your agent deployment using stale-while-revalidate and key-value cache APIs.

[Agent Server](/langsmith/agent-server) includes a built-in cache you can use inside your deployed graphs. Call `swr` with a key and a loader function, and the server caches the result, revalidates stale entries in the background, and returns fresh data on every read.

All cache APIs are **server-side only** and require the LangGraph Agent Server runtime. Values must be JSON-serializable.

<Note>
  `swr` requires Agent Server runtime **v0.7.79** or later and is currently in **beta**.
  `cache_get` and `cache_set` require **v0.7.29** or later.
</Note>

## Quick start

Pass a key and an async loader function. `swr` returns the cached value if available, or calls your loader to fetch it:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langgraph_sdk.cache import swr

result = await swr("config:global", load_config)
config_data = result.value
```

On the first call, `swr` awaits `load_config()` and caches the result. On subsequent calls, it returns the cached value instantly and revalidates in the background.

## Configure freshness

Control how long cached values are considered fresh and when they expire:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from datetime import timedelta
from langgraph_sdk.cache import swr

result = await swr(
    "config:global",
    load_config,
    fresh_for=timedelta(minutes=5),
    max_age=timedelta(hours=1),
)
```

| Parameter   | Default             | Description                                                                                                         |
| ----------- | ------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `fresh_for` | `timedelta(0)`      | Duration to treat a cached value as fresh. During this window, `swr` returns the cached value with no revalidation. |
| `max_age`   | `timedelta(days=1)` | Maximum lifetime of a cached entry. After this, `swr` blocks on the loader before returning. Capped at 1 day.       |

### How revalidation works

| Cache state | Condition                    | Behavior                                                       |
| ----------- | ---------------------------- | -------------------------------------------------------------- |
| **Miss**    | Key not in cache             | Awaits `loader()`, stores result, returns it.                  |
| **Fresh**   | `age < fresh_for`            | Returns cached value, no revalidation.                         |
| **Stale**   | `fresh_for <= age < max_age` | Returns cached value immediately, triggers background refresh. |
| **Expired** | `age >= max_age`             | Awaits `loader()`, stores result, returns it.                  |

## Use with Pydantic models

Pass a `model` parameter to automatically serialize and deserialize Pydantic models:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from pydantic import BaseModel
from langgraph_sdk.cache import swr

class UserProfile(BaseModel):
    name: str
    email: str
    role: str

result = await swr(
    f"profile:{user_id}",
    lambda: fetch_profile(user_id),
    model=UserProfile,
)
profile: UserProfile = result.value  # deserialized automatically
```

`swr` calls `model_dump(mode="json")` before storing and `model.model_validate()` when reading back.

## Cache auth credentials

You can cache credential validation in a [custom auth handler](/langsmith/custom-auth) to avoid hitting your identity provider on every request:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from datetime import timedelta
from langgraph_sdk import Auth
from langgraph_sdk.cache import swr

auth = Auth()

@auth.authenticate
async def authenticate(headers: dict) -> Auth.types.MinimalUserDict:
    token = (headers.get(b"authorization") or b"").decode()
    if not token:
        raise Auth.exceptions.HTTPException(status_code=401, detail="Missing token")

    result = await swr(
        f"auth:token:{token}",
        lambda: validate_and_fetch_user(token),
        fresh_for=timedelta(minutes=5),
        max_age=timedelta(hours=1),
    )
    return result.value
```

With this setup, the server returns the cached user for 5 minutes without revalidation, then revalidates in the background for up to 1 hour. After 1 hour, the next request blocks until `validate_and_fetch_user` completes.

## Inspect cache status

`swr` returns an `SWRResult` object with the value and cache status:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
result = await swr("my-key", my_loader)

result.value   # the cached or freshly loaded value
result.status  # "miss" | "fresh" | "stale" | "expired"
```

Call `.mutate()` to update the cached value or force a revalidation:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
await result.mutate(new_value)  # update the cache with a new value
await result.mutate()           # force revalidation by calling the loader
```

## Low-level cache API

For simple get/set caching without revalidation, use `cache_get` and `cache_set` directly:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from datetime import timedelta
from langgraph_sdk.cache import cache_get, cache_set

value = await cache_get("my-key")

if value is None:
    value = await expensive_computation()
    await cache_set("my-key", value, ttl=timedelta(hours=1))
```

### `cache_get`

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
async def cache_get(key: str) -> Any | None
```

Return the deserialized value, or `None` if the key does not exist or has expired.

### `cache_set`

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
async def cache_set(key: str, value: Any, *, ttl: timedelta | None = None) -> None
```

| Parameter | Type                | Default  | Description                                                                   |
| --------- | ------------------- | -------- | ----------------------------------------------------------------------------- |
| `key`     | `str`               | required | The cache key                                                                 |
| `value`   | `Any`               | required | Value to cache. Must be JSON-serializable                                     |
| `ttl`     | `timedelta \| None` | `None`   | Time-to-live. The server caps this at 1 day. `None` or zero defaults to 1 day |

## Next steps

* [Add custom authentication](/langsmith/custom-auth) to your deployment.
* [Add custom lifespan events](/langsmith/custom-lifespan) to initialize resources at server startup.
* Learn about the [agent server architecture](/langsmith/agent-server).

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/caching.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# How to cancel a run
Source: https://docs.langchain.com/langsmith/cancel-run

Cancel a single run or multiple runs via the API, and choose between interrupt and rollback actions.

This guide covers how to cancel runs for your agent via the [LangSmith Deployment API](/langsmith/server-api-ref). You can cancel a single run by ID or cancel multiple runs by thread or status. Cancellation is useful for stopping long-running or stuck runs, or when a user abandons a request.

## Setup

Create a client and thread:

<Tabs>
  <Tab title="Python">
    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    from langgraph_sdk import get_client

    client = get_client(url=<DEPLOYMENT_URL>)
    assistant_id = "agent"
    thread = await client.threads.create()
    ```
  </Tab>

  <Tab title="Javascript">
    ```js theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    import { Client } from "@langchain/langgraph-sdk";

    const client = new Client({ apiUrl: <DEPLOYMENT_URL> });
    const assistantID = "agent";
    const thread = await client.threads.create();
    ```
  </Tab>

  <Tab title="CURL">
    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    curl --request POST \
      --url <DEPLOYMENT_URL>/threads \
      --header 'Content-Type: application/json' \
      --data '{}'
    ```
  </Tab>
</Tabs>

## Cancel a single run

The following examples create a run, cancel it with different options, and print the run to show what you get in each case. You can cancel runs in `pending` or `running` status. Trying to cancel a run that is not in `pending` or `running` status will result in an error.

### Cancel with interrupt (default)

**interrupt** stops the worker executing the run and marks the run as `interrupted`. Nothing is deleted:

* The run record remains (with status `interrupted`). You can fetch it, inspect inputs/outputs, and see the execution history.
* All checkpoints for that run remain stored. The thread state at the last completed step is preserved.
* You can later resume from a checkpoint (for example, with [time travel](/langsmith/human-in-the-loop-time-travel)) or inspect the partial state.

Use **interrupt** when you want to stop a run but keep it for debugging, auditing, or resuming from a checkpoint.

<Tabs>
  <Tab title="Python">
    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    run = await client.runs.create(
        thread["thread_id"],
        assistant_id,
        input={"messages": [{"role": "user", "content": "Long task"}]},
    )
    await client.runs.cancel(thread["thread_id"], run["run_id"])

    run_after = await client.runs.get(thread["thread_id"], run["run_id"], wait=True)
    print(run_after["status"])   # "interrupted"
    ```
  </Tab>

  <Tab title="Javascript">
    ```js theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    const run = await client.runs.create(
        thread["thread_id"],
        assistantID,
        { input: { messages: [{ role: "user", content: "Long task" }] } }
    );
    await client.runs.cancel(thread["thread_id"], run["run_id"], wait=true);

    const runAfter = await client.runs.get(thread["thread_id"], run["run_id"]);
    console.log(runAfter["status"]);   // "interrupted"
    ```
  </Tab>

  <Tab title="CURL">
    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    # Create a run (use the run_id and thread_id from the response)
    curl --request POST \
      --url <DEPLOYMENT_URL>/threads/<THREAD_ID>/runs \
      --header 'Content-Type: application/json' \
      --data '{"assistant_id": "agent", "input": {"messages": [{"role": "user", "content": "Summarize the docs"}]}}'

    # Cancel with default action (interrupt)
    curl --request POST \
      --url <DEPLOYMENT_URL>/threads/<THREAD_ID>/runs/<RUN_ID>/cancel?wait=true

    # Get the run to see status "interrupted" and that the run still exists
    curl --request GET \
      --url <DEPLOYMENT_URL>/threads/<THREAD_ID>/runs/<RUN_ID>
    ```
  </Tab>
</Tabs>

### Cancel with rollback

**rollback** stops the run and then removes it and its checkpoints from storage:

* The run record is deleted. The run no longer appears in run lists or history for that thread.
* All checkpoints created by that run are deleted. The thread’s state is reverted to what it was before the run started (as if the run had never been executed).
* You cannot resume or inspect the run after a rollback.

Use **rollback** when you want to fully discard a run and its effects (for example, after a user abandons a request and you do not need to keep partial work).

<Tabs>
  <Tab title="Python">
    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    run = await client.runs.create(
        thread["thread_id"],
        assistant_id,
        input={"messages": [{"role": "user", "content": "Long task"}]},
    )
    await client.runs.cancel(thread["thread_id"], run["run_id"], action="rollback", wait=True)

    # Throws an error because the run is deleted
    try:
        await client.runs.get(thread["thread_id"], run["run_id"])
    except Exception:
        print("Run was correctly deleted")
    ```
  </Tab>

  <Tab title="Javascript">
    ```js theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    const run = await client.runs.create(
        thread["thread_id"],
        assistantID,
        { input: { messages: [{ role: "user", content: "Long task" }] } }
    );
    await client.runs.cancel(thread["thread_id"], run["run_id"], wait=true, action="rollback");

    // Throws an error because the run is deleted
    try {
        await client.runs.get(thread["thread_id"], run["run_id"]);
    } catch (e) {
        console.log("Run was correctly deleted");
    }
    ```
  </Tab>

  <Tab title="CURL">
    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    # Create a run, then cancel with rollback
    curl --request POST \
      --url <DEPLOYMENT_URL>/threads/<THREAD_ID>/runs \
      --header 'Content-Type: application/json' \
      --data '{"assistant_id": "agent", "input": {"messages": [{"role": "user", "content": "Summarize the docs"}]}}'

    curl --request POST \
      --url "<DEPLOYMENT_URL>/threads/<THREAD_ID>/runs/<RUN_ID>/cancel?action=rollback"

    # Throws an error because the run is deleted
    curl --request GET \
      --url <DEPLOYMENT_URL>/threads/<THREAD_ID>/runs/<RUN_ID>
    ```
  </Tab>
</Tabs>

### Cancel with wait

By default, the cancel request returns after the cancellation is requested and the run is cancelled asynchronously. `wait=True` makes the cancel request block until the run has been fully cancelled. This is useful when you want to know the final state of the run after it has been cancelled (e.g., what checkpoints were created, what the final output was).

<Tabs>
  <Tab title="Python">
    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    run = await client.runs.create(
        thread["thread_id"],
        assistant_id,
        input={"messages": [{"role": "user", "content": "Long task"}]},
    )
    # Cancel the run asynchronously
    await client.runs.cancel(thread["thread_id"], run["run_id"])
    # Get the status of the run
    run_after = await client.runs.get(thread["thread_id"], run["run_id"])
    print(run_after["status"])  # "pending" or "running"

    # Wait for the run to be properly cancelled
    await client.runs.join(thread["thread_id"], run["run_id"])
    run_after = await client.runs.get(thread["thread_id"], run["run_id"])
    print(run_after["status"])  # "interrupted"
    ```
  </Tab>

  <Tab title="Javascript">
    ```js theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    const run = await client.runs.create(
        thread["thread_id"],
        assistantID,
        { input: { messages: [{ role: "user", content: "Long task" }] } }
    );
    // Cancel the run asynchronously
    await client.runs.cancel(thread["thread_id"], run["run_id"]);
    // Get the status of the run
    const runRunning = await client.runs.get(thread["thread_id"], run["run_id"])
    console.log(runRunning["status"])  // "pending" or "running"

    // Wait for the run to be properly cancelled
    await client.runs.join(thread["thread_id"], run["run_id"])
    const runInterrupted = await client.runs.get(thread["thread_id"], run["run_id"])
    console.log(runInterrupted["status"])  // "interrupted"
    ```
  </Tab>

  <Tab title="CURL">
    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    # Create a run
    curl --request POST \
      --url <DEPLOYMENT_URL>/threads/<THREAD_ID>/runs \
      --header 'Content-Type: application/json' \
      --data '{"assistant_id": "agent", "input": {"messages": [{"role": "user", "content": "Summarize the docs"}]}}'

    # Cancel the run asynchronously
    curl --request POST \
      --url "<DEPLOYMENT_URL>/threads/<THREAD_ID>/runs/<RUN_ID>/cancel"

    # Get the status of the run, should be "pending" or "running" until cancellation completes, then "interrupted"
    curl --request GET \
      --url <DEPLOYMENT_URL>/threads/<THREAD_ID>/runs/<RUN_ID>
    ```
  </Tab>
</Tabs>

## Cancel multiple runs

Use the bulk cancel endpoint to cancel multiple runs in one request. Both the interrupt and rollback actions are supported.

### Cancel by thread ID and run IDs

Cancel specific runs by passing their IDs.

<Tabs>
  <Tab title="Python">
    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    run1 = await client.runs.create(
        thread["thread_id"],
        assistant_id,
        input={"messages": [{"role": "user", "content": "First request"}]},
    )
    run2 = await client.runs.create(
        thread["thread_id"],
        assistant_id,
        input={"messages": [{"role": "user", "content": "Second request"}]},
        multitask_strategy="enqueue",
    )

    await client.runs.cancel_many(
        thread_id=thread["thread_id"],
        run_ids=[run1["run_id"], run2["run_id"]]
    )

    # Wait for the runs to be cancelled
    await client.runs.join(thread["thread_id"], run2["run_id"])
    runs_after = await client.runs.list(thread["thread_id"])
    for run in runs_after:
        if run["run_id"] in (run1["run_id"], run2["run_id"]):
            print(run["run_id"], run["status"])  # "interrupted"
    ```
  </Tab>

  <Tab title="Javascript">
    ```js theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    // Bulk delete by run IDs is not supported in the Javascript SDK
    ```
  </Tab>

  <Tab title="CURL">
    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    # Create two runs (capture run_id from each response)
    curl --request POST \
      --url <DEPLOYMENT_URL>/threads/<THREAD_ID>/runs \
      --header 'Content-Type: application/json' \
      --data '{"assistant_id": "agent", "input": {"messages": [{"role": "user", "content": "First request"}]}}'

    curl --request POST \
      --url <DEPLOYMENT_URL>/threads/<THREAD_ID>/runs \
      --header 'Content-Type: application/json' \
      --data '{"assistant_id": "agent", "input": {"messages": [{"role": "user", "content": "Second request"}]}}'

    # Cancel both by run IDs
    curl --request POST \
      --url "<DEPLOYMENT_URL>/runs/cancel?action=interrupt" \
      --header 'Content-Type: application/json' \
      --data '{"thread_id": "<THREAD_ID>", "run_ids": ["<RUN_ID_1>", "<RUN_ID_2>"]}'

    # List runs to confirm
    curl --request GET \
      --url <DEPLOYMENT_URL>/threads/<THREAD_ID>/runs
    ```
  </Tab>
</Tabs>

### Cancel by status

Cancel all runs that match a status across all threads in a deployment. Valid status options are `pending`, `running`, or `all`.

<Tabs>
  <Tab title="Python">
    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    run1 = await client.runs.create(
        thread["thread_id"],
        assistant_id,
        input={"messages": [{"role": "user", "content": "First request"}]},
    )
    thread2 = await client.threads.create()
    run2 = await client.runs.create(
        thread2["thread_id"],
        assistant_id,
        input={"messages": [{"role": "user", "content": "Second request"}]},
    )

    await client.runs.cancel_many(
        status="running",
    )

    # Wait for the runs to be cancelled
    await client.runs.join(thread2["thread_id"], run2["run_id"])
    run_after = await client.runs.get(thread["thread_id"], run1["run_id"])
    print(run_after["status"])  # running run is now "interrupted"
    run_after2 = await client.runs.get(thread2["thread_id"], run2["run_id"])
    print(run_after2["status"])  # runs are cancelled across all threads
    ```
  </Tab>

  <Tab title="Javascript">
    ```js theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    // Bulk delete by status is not supported in the Javascript SDK
    ```
  </Tab>

  <Tab title="CURL">
    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    # Create a run
    curl --request POST \
      --url <DEPLOYMENT_URL>/threads/<THREAD_ID>/runs \
      --header 'Content-Type: application/json' \
      --data '{"assistant_id": "agent", "input": {"messages": [{"role": "user", "content": "First request"}]}}'

    # Create a second thread
    curl --request POST \
      --url <DEPLOYMENT_URL>/threads \
      --header 'Content-Type: application/json' \
      --data '{}'

    # Create a run in the second thread
    curl --request POST \
      --url <DEPLOYMENT_URL>/threads/<THREAD_ID_2>/runs \
      --header 'Content-Type: application/json' \
      --data '{"assistant_id": "agent", "input": {"messages": [{"role": "user", "content": "Second request"}]}}'

    # Cancel all running runs
    curl --request POST \
      --url "<DEPLOYMENT_URL>/runs/cancel?action=interrupt" \
      --header 'Content-Type: application/json' \
      --data '{"status": "running"}'

    # Get the status of the runs to confirm
    curl --request GET \
      --url <DEPLOYMENT_URL>/threads/<THREAD_ID>/runs/<RUN_ID_1>
    curl --request GET \
      --url <DEPLOYMENT_URL>/threads/<THREAD_ID_2>/runs/<RUN_ID_2>
    ```
  </Tab>
</Tabs>

## Cancel on disconnect

When starting a run with streaming or when waiting on a run, you can set `on_disconnect="cancel"` so that the run is cancelled if the client disconnects. This avoids leaving runs in progress when a user closes the app or loses connection.

<Tabs>
  <Tab title="Python">
    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    # With runs.wait: run is cancelled if the client disconnects
    result = await client.runs.wait(
        thread["thread_id"],
        assistant_id,
        input={"messages": [{"role": "user", "content": "Long task"}]},
        on_disconnect="cancel",
    )

    # With runs.stream: run is cancelled if the client disconnects
    async for chunk in client.runs.stream(
        thread["thread_id"],
        assistant_id,
        input={"messages": [{"role": "user", "content": "Long task"}]},
        on_disconnect="cancel",
    ):
        print(chunk)

    # With runs.join: wait for an existing run; cancel if client disconnects
    run = await client.runs.create(
        thread["thread_id"],
        assistant_id,
        input={"messages": [{"role": "user", "content": "Long task"}]},
    )
    await client.runs.join(
        thread["thread_id"],
        run["run_id"],
        on_disconnect="cancel",
    )

    # With runs.join_stream: join an existing run and stream; cancel if client disconnects
    async for chunk in client.runs.join_stream(
        thread["thread_id"],
        run["run_id"],
        on_disconnect="cancel",
    ):
        print(chunk)
    ```
  </Tab>

  <Tab title="Javascript">
    ```js theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    // With runs.wait: run is cancelled if the client disconnects
    const result = await client.runs.wait(
        thread["thread_id"],
        assistantID,
        { input: { messages: [{ role: "user", content: "Long task" }] }, onDisconnect: "cancel" }
    );

    // With runs.stream: run is cancelled if the client disconnects
    const streamResponse = client.runs.stream(
        thread["thread_id"],
        assistantID,
        { input: { messages: [{ role: "user", content: "Long task" }] }, onDisconnect: "cancel" }
    );
    for await (const chunk of streamResponse) {
        console.log(chunk);
    }

    // With runs.join does not support cancel on disconnect in the Javascript SDK

    // With runs.joinStream: join an existing run and stream; cancel if client disconnects
    const joinStreamResponse = client.runs.joinStream(
        thread["thread_id"],
        run["run_id"],
        { cancelOnDisconnect: true }
    );
    for await (const chunk of joinStreamResponse) {
        console.log(chunk);
    }
    ```
  </Tab>

  <Tab title="CURL">
    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    # runs.wait: create run and wait for output; cancel if client disconnects
    curl --request POST \
      --url <DEPLOYMENT_URL>/threads/<THREAD_ID>/runs/wait \
      --header 'Content-Type: application/json' \
      --data '{"assistant_id": "agent", "input": {"messages": [{"role": "user", "content": "Long task"}]}, "on_disconnect": "cancel"}'

    # Create and stream a run; cancel if client disconnects
    curl --request POST \
      --url "<DEPLOYMENT_URL>/threads/<THREAD_ID>/runs/stream?on_disconnect=cancel" \
      --header 'Content-Type: application/json' \
      --data '{"assistant_id": "agent", "input": {"messages": [{"role": "user", "content": "Long task"}]}}'

    # runs.join: wait on an existing run; cancel if client disconnects
    curl --request GET \
      --url "<DEPLOYMENT_URL>/threads/<THREAD_ID>/runs/<RUN_ID>/join?cancel_on_disconnect=cancel"

    # runs.join_stream: join an existing run and stream; cancel if client disconnects
    curl --request GET \
      --url "<DEPLOYMENT_URL>/threads/<THREAD_ID>/runs/<RUN_ID>/stream?cancel_on_disconnect=cancel"
    ```
  </Tab>
</Tabs>

## Common scenarios

* **Human-in-the-loop and interrupts**: Agents can pause at [interrupts](/langsmith/add-human-in-the-loop) for human input. Cancelling a run stops execution; it is different from an interrupt, where the run is paused and can be resumed with new input.
* **Time travel**: After cancelling with action `interrupt`, the run and checkpoints are still available. You can [resume from a checkpoint](/langsmith/human-in-the-loop-time-travel) (time travel) to replay or branch execution.
* **Double-texting**: When a user sends new input while a run is in progress, the [multitask strategy](/langsmith/double-texting) (enqueue, reject, interrupt, rollback) determines whether the existing run is interrupted or rolled back and how the new run is handled. To cancel runs explicitly from your application, use the cancel API described on this page.
* **Studio**: In [Studio](/langsmith/use-studio), use the **Cancel** button in the run UI to cancel the current run.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/cancel-run.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
