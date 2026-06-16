# Custom model providers
Source: https://docs.langchain.com/langsmith/llm-gateway-custom-providers

Route requests through the LLM Gateway to any OpenAI-compatible endpoint, such as a self-hosted open-source model served through an inference server.

<Note>
  **Private beta:** The LLM Gateway is in private beta. Sign up for [the waitlist](https://www.langchain.com/langsmith-llm-gateway-waitlist) to get access.
</Note>

In addition to the [built-in providers](/langsmith/llm-gateway#supported-providers), the LLM Gateway can proxy requests to **any OpenAI-compatible endpoint**, such as a self-hosted open-source model served through an inference server (vLLM, Ollama, and similar).

## How it works

A custom provider is defined by an **OpenAI Compatible Endpoint** [model configuration](/langsmith/model-configurations) that you save under **Settings → Model configurations** in the [LangSmith UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-llm-gateway-custom-providers). The gateway uses the following options from the configuration:

* A **base URL**: the upstream endpoint the gateway forwards requests to.
* A **model name**: injected into each request so callers don't have to specify it.
* An **API key**: stored as a [workspace secret](/langsmith/llm-gateway-admin-setup#2-add-provider-secrets), never sent by the client.

You then address the saved configuration by name through the `https://gateway.smith.langchain.com/providers/{configName}` route. When a request comes in, the gateway looks up the configuration, resolves the secret, and proxies the call to the configured upstream URL.

<Note>
  `{configName}` is the configuration name from your workspace [model configuration](/langsmith/model-configurations). If the name contains characters that aren't URL-safe (such as `/` or spaces), URL-encode them in the path. For example, a configuration named `meta-llama/Llama-3.1-8B-Instruct` becomes `https://gateway.smith.langchain.com/providers/meta-llama%2FLlama-3.1-8B-Instruct/v1/chat/completions`.
</Note>

## 1. Create a custom provider configuration

1. Add the upstream endpoint's API key as a workspace secret under **Settings → Integrations → Provider Secrets**. Give it a descriptive name (for example, `MY_PROVIDER_API_KEY`).
2. Go to **Settings → Model configurations** and create a configuration with **OpenAI Compatible Endpoint** as the provider.
3. Set the **Base URL** to your upstream endpoint (for example, `https://my-inference-server.example.com/v1`) and the **Model Name** to the model identifier the endpoint expects.
4. Set the **API Key Name** to the secret you created.
5. Save the configuration with a **name**. This name is what you'll use in the gateway route.

<Note>
  Each configuration pins a single model, since the gateway overrides the request body's `model` with the configured value. To serve multiple models from the same endpoint, create one configuration per model (each with its own name and `/providers/{configName}` route).
</Note>

## 2. Make a call

Call the saved configuration by name. The route is `https://gateway.smith.langchain.com/providers/{configName}`, where `{configName}` is the configuration name you saved in **Settings → Model configurations** (`my-custom-endpoint` in the following examples).

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
curl https://gateway.smith.langchain.com/providers/my-custom-endpoint/v1/chat/completions \
    -H "Authorization: Bearer $LANGSMITH_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{"messages":[{"role":"user","content":"ping"}]}'
```

The gateway overrides the request body's `model` field with the model name from the saved configuration, so the value you pass from the client is ignored.

## Supported endpoints

Custom providers use the same allowlist as the built-in OpenAI provider: `POST /v1/chat/completions` (including streaming), `POST /v1/responses`, and the `GET /v1/models` listing endpoints. Any other path returns `501 Not Implemented`.

## Next steps

* [Quickstart](/langsmith/llm-gateway-quickstart): set the gateway base URL and API key environment variables.
* [Spend policies](/langsmith/llm-gateway-spend-policies): apply cost limits to custom providers.
* [PII and secrets redaction](/langsmith/llm-gateway-redaction): redact sensitive data before it reaches your endpoint.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/llm-gateway-custom-providers.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# PII and secrets redaction
Source: https://docs.langchain.com/langsmith/llm-gateway-redaction

Scan and redact PII and secrets from LLM requests before they reach providers.

<Note>
  **Private beta:** The LLM Gateway is in private beta. [Sign up for the waitlist](https://www.langchain.com/langsmith-llm-gateway-waitlist) to get access.
</Note>

When a PII or secrets redaction policy is active, the gateway scans outbound requests before they reach the LLM provider. If sensitive data is detected, it is redacted from the request. The agent continues to receive a response.

Redacted content is also redacted in the LangSmith trace, so sensitive data does not persist in your observability data either.

## PII detection

The gateway detects and redacts the following categories of personally identifiable information:

| Category                                            | Examples                         |
| --------------------------------------------------- | -------------------------------- |
| **Names**                                           | Person names in natural language |
| **Nationality, religion, or political affiliation** | Nationality                      |
| **Locations**                                       | Addresses, cities, countries     |

Detection uses Presidio for named entities (names, locations, and NRP) and pattern-based rules for structured identifiers.

## Secrets detection

The gateway detects and redacts API keys, tokens, and credentials across a wide range of providers and formats:

| Category                    | Patterns detected                                                   |
| --------------------------- | ------------------------------------------------------------------- |
| **Social Security Numbers** | US SSN patterns (for example, 123-45-6789)                          |
| **Phone numbers**           | US phone number patterns                                            |
| **LangSmith**               | Personal tokens, service keys                                       |
| **AWS**                     | Access tokens                                                       |
| **GitHub**                  | Personal access tokens, fine-grained PATs, OAuth tokens, app tokens |
| **GitLab**                  | Personal access tokens                                              |
| **AI providers**            | OpenAI API keys, Anthropic API keys                                 |
| **Cloud platforms**         | GCP API keys, Azure AD client secrets                               |
| **Collaboration tools**     | Slack bot/user/app tokens, Datadog access tokens                    |
| **Package registries**      | PyPI upload tokens, npm access tokens                               |
| **Cryptographic**           | Private keys                                                        |
| **Stripe**                  | Access tokens                                                       |

## Enable redaction policies

<Warning>
  Creating and managing policies requires `organization:manage` permission.
</Warning>

1. Go to **Settings → Gateway → LLM Gateway**.
2. Click **Create policy**.
3. Select **PII redaction** or **Secrets redaction** as the policy type.
4. Configure which categories to detect (or enable all).
5. Save.

Redaction policies apply to all requests that pass through the gateway in the scope where they're configured. They take effect immediately.

## How redacted content appears

When PII or a secret is detected, the content is replaced with a placeholder in both the request sent to the provider and the LangSmith trace. For example:

**Original request:**

```
Please process the refund for John Smith, SSN 123-45-6789.
```

**Upstream redaction:**

```
Please process the refund for [SAFE_TO_USE:PERSON_kbqdjxyz], SSN [SAFE_TO_USE:US_SSN_abqxlmwp]
```

Placeholders follow the format `[SAFE_TO_USE:<CATEGORY>_<suffix>]`:

* **SAFE\_TO\_USE:** fixed prefix marking the value as a redacted placeholder.
* **\<CATEGORY>:** the detected type. Examples: `PERSON`, `LOCATION`, `US_SSN`, `US_PHONE_NUMBER`, `OPENAI_API_KEY`, `GITHUB_PAT`, `LANGSMITH_PERSONAL_TOKEN`.
* **\<suffix>:** an 8-character random tag.

The trace in LangSmith shows the redacted version along with metadata indicating that redaction occurred and which categories were detected.

**Downstream de-redacted response:**

As the upstream provider is returning a response, the gateway will replace the redaction placeholders with caller's original values. For example, your agent may see this response:

```
Checking Confirming John Smith's SSN to be 123-45-6789.... Okay! I will process the full refund.
```

## What redaction covers

**What it covers:**

* Outbound request content (the message sent to the LLM provider) is scanned and redacted before it leaves the gateway.
* The redacted version is what appears in LangSmith traces.

**What it does not cover:**

* **Responses from the LLM provider:** if the model generates sensitive data in its response, that content is not redacted. Streaming response redaction is in progress.
* **Data already in your traces:** redaction only applies to requests flowing through the gateway. Traces written directly to the LangSmith API (bypassing the gateway) are not scanned.
* **Platform-level ingestion:** if your requirement is to prevent PII from ever entering LangSmith regardless of how it arrives (for example, data residency compliance), gateway redaction alone is not sufficient. That requires ingestion-level redaction, which is a separate capability.
* **Prompt scanning:** system prompts, developer prompts, and tool-call arguments are not scanned.
  **Scanner failures are fail-close**: if a PII or secrets scanner is unreachable, slow or errors, that stage blocks the request from proceeding.

This distinction matters. If your security model requires that sensitive data never reaches any system (not just the LLM provider) make sure you understand which surface the gateway covers and which surfaces require additional controls.

## Next steps

* [Spend policies](/langsmith/llm-gateway-spend-policies): add cost controls alongside data protection.
* [Traces, Engine, and access control](/langsmith/llm-gateway-access): see how redaction events appear in traces and surface in Engine.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/llm-gateway-redaction.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Spend policies
Source: https://docs.langchain.com/langsmith/llm-gateway-spend-policies

Set cost limits on LLM usage across your organization and prevent runaway spend before it reaches providers.

<Note>
  **Private beta:** The LLM Gateway is in private beta. [Sign up for the waitlist](https://www.langchain.com/langsmith-llm-gateway-waitlist) to get access.
</Note>

A spend policy defines a cost cap for a specific scope (organization, workspace, API key, or user) over a time window (monthly, weekly, daily, or hourly). The [LLM Gateway](/langsmith/llm-gateway) tracks spend in real time and blocks any request that would push spend past the cap, returning a `402` response:

```
API Error: 402 request blocked by gateway policies: R&D Spend Cap
```

The blocked request is traced to LangSmith with the policy violation recorded as metadata, so you can see exactly what was blocked and why.

## Policy dimensions

Spend policies are evaluated from broadest to most specific. All matching policies are checked, and if any one returns a block, the request is rejected. You can set a policy as a default (applying a blanket spend cap to all workspaces, users, or API keys) or as a granular policy (individual limits or limits on a group of entities).

| Scope            | What it caps                                                                    | Example                                                                           |
| ---------------- | ------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| **Organization** | Total spend across all workspaces in the org                                    | "The entire org cannot spend more than \$10,000/month on LLM calls"               |
| **Workspace**    | Total spend within a single workspace or group of workspaces                    | "The workspaces related to R\&D cannot spend more than \$2,000/month"             |
| **API key**      | Spend by a single API key or group of API keys (maps to a service or agent)     | "The customer support agent keys cannot spend more than \$500/month cumulatively" |
| **User**         | Spend by a single user or group of users (resolved from the API key's identity) | "No individual developer can spend more than \$50/day"                            |

### Conflict resolution

By default, LLM Gateway assesses the broadest scope first. If a granular policy applies, the most restrictive policy wins. Narrower scopes can only tighten limits, never loosen them. If an org-level policy caps spend at \$10,000/month and a workspace-level policy caps at \$15,000/month, the \$10,000 org cap still applies.

### Defaults vs. granular policies

Spend policies have two aspects:

1. **Sums across a dimension:** the total cap for that scope. Example: "This workspace's total spend cannot exceed \$5,000/month."
2. **Defaults for each member of a dimension:** a base limit that applies to every API key or user within a scope unless overridden. Example: "Each API key in this workspace gets a \$200/month default cap." Individual API keys can receive additional policies that raise their specific limit, but no policy can loosen a cap set at a broader scope.

## Time windows

| Window      | Resets                                  | Use case                                                                               |
| ----------- | --------------------------------------- | -------------------------------------------------------------------------------------- |
| **Monthly** | First of each month                     | Budget alignment, overall cost control                                                 |
| **Weekly**  | Midnight UTC on the Monday of each week | weekly budgeting                                                                       |
| **Daily**   | Midnight UTC                            | Prevent single-day cost spikes (for example, a coding agent in a retry loop overnight) |
| **Hourly**  | Top of each hour                        | Catch runaway agents quickly                                                           |

You can apply multiple time windows to the same scope. For example, a workspace can have both a \$5,000/month cap and a \$500/day cap. Both are enforced independently.

## Create a spend policy

<Warning>
  Creating and managing policies requires `organization:manage` permission. For the full permissions breakdown, refer to [Traces, Engine, and access control](/langsmith/llm-gateway-access).
</Warning>

1. Go to **Settings → Gateway → LLM Gateway**.
2. Click **Create policy**.
3. Select the scope (organization, workspace, API key, or user).
4. Set the time window (monthly, weekly, daily, or hourly).
5. Set the spend cap in USD.
6. Save.

Policies take effect immediately. The gateway evaluates them on every incoming request with sub-second enforcement latency.

## View spend

The spend visibility dashboard shows real-time cost rollups so you can understand where your LLM budget is going before you reach the limit.

From the gateway settings page, you can view how much each policy has spent against its cap.

## Integration with LangSmith Engine

When a spend policy blocks a request, the violation is recorded as metadata on the trace. These violations surface as issues in [LangSmith Engine](/langsmith/engine), where you can click through from the issue to the trace to understand what the agent was doing when it hit the limit.

This is useful for diagnosing whether a blocked request represents a genuine cost problem (a coding agent in a retry loop) or a policy that needs adjustment (a legitimate workload that grew beyond its cap).

## Next steps

* [PII and secrets redaction](/langsmith/llm-gateway-redaction): add data protection policies alongside cost controls.
* [Traces, Engine, and access control](/langsmith/llm-gateway-access): how policy events flow into observability and triage.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/llm-gateway-spend-policies.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# How to run an evaluation locally (Python only)
Source: https://docs.langchain.com/langsmith/local

Sometimes it is helpful to run an evaluation locally without uploading any results to LangSmith. For example, if you're quickly iterating on a prompt and want to smoke test it on a few examples, or if you're validating that your target and evaluator functions are defined correctly, you may not want to record these evaluations.

You can do this by using the LangSmith Python SDK and passing `upload_results=False` to `evaluate()` / `aevaluate()`.

This will run you application and evaluators exactly as it always does and return the same output, but nothing will be recorded to LangSmith. This includes not just the experiment results but also the application and evaluator traces.

<Note>
  If you want to upload results to LangSmith but also need to process them in your script (for quality gates, custom aggregations, etc.), refer to [Read experiment results locally](/langsmith/read-local-experiment-results).
</Note>

## Example

Let's take a look at an example:

Requires `langsmith>=0.2.0`. Example also uses `pandas`.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langsmith import Client

# 1. Create and/or select your dataset
ls_client = Client()
dataset = ls_client.clone_public_dataset(
    "https://smith.langchain.com/public/a63525f9-bdf2-4512-83e3-077dc9417f96/d"
)

# 2. Define an evaluator
def is_concise(outputs: dict, reference_outputs: dict) -> bool:
    return len(outputs["answer"]) < (3 * len(reference_outputs["answer"]))

# 3. Define the interface to your app
def chatbot(inputs: dict) -> dict:
    return {"answer": inputs["question"] + " is a good question. I don't know the answer."}

# 4. Run an evaluation
experiment = ls_client.evaluate(
    chatbot,
    data=dataset,
    evaluators=[is_concise],
    experiment_prefix="my-first-experiment",
    # 'upload_results' is the relevant arg.
    upload_results=False
)

# 5. Analyze results locally
results = list(experiment)

# Check if 'is_concise' returned False.
failed = [r for r in results if not r["evaluation_results"]["results"][0].score]

# Explore the failed inputs and outputs.
for r in failed:
    print(r["example"].inputs)
    print(r["run"].outputs)

# Explore the results as a Pandas DataFrame.

# Must have 'pandas' installed.
df = experiment.to_pandas()
df[["inputs.question", "outputs.answer", "reference.answer", "feedback.is_concise"]]
```

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{'question': 'What is the largest mammal?'}
{'answer': "What is the largest mammal? is a good question. I don't know the answer."}
{'question': 'What do mammals and birds have in common?'}
{'answer': "What do mammals and birds have in common? is a good question. I don't know the answer."}
```

|   | inputs.question                           | outputs.answer                                                                         | reference.answer           | feedback.is\_concise |
| - | ----------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------- | -------------------- |
| 0 | What is the largest mammal?               | What is the largest mammal? is a good question. I don't know the answer.               | The blue whale             | False                |
| 1 | What do mammals and birds have in common? | What do mammals and birds have in common? is a good question. I don't know the answer. | They are both warm-blooded | False                |

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/local.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Local development & testing
Source: https://docs.langchain.com/langsmith/local-dev-testing

Compare langgraph dev and langgraph up for local development and production-like testing of Agent Server applications.

This guide covers how to develop and test [Agent Server](/langsmith/agent-server) applications locally. The [LangGraph CLI](/langsmith/cli) provides two commands for local development, each optimized for different stages of your workflow:

* [`langgraph dev`](#langgraph-dev): A lightweight development server for rapid iteration.
* [`langgraph up`](#langgraph-up): A production-like testing environment for validation.

| Feature               | `langgraph dev`                                                             | `langgraph up`                                                                           |
| --------------------- | --------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| **Docker required**   | No                                                                          | Yes                                                                                      |
| **Installation**      | `pip install langgraph-cli[inmem]`                                          | `pip install langgraph-cli`                                                              |
| **Primary use case**  | Rapid development & testing                                                 | Production-like validation                                                               |
| **State persistence** | In-memory & pickled to local directory                                      | PostgreSQL                                                                               |
| **Hot reloading**     | Yes (default)                                                               | Optional (`--watch` flag)                                                                |
| **Default port**      | `2024`                                                                      | `8123`                                                                                   |
| **Resource usage**    | Lightweight                                                                 | Heavier (build and run separate docker containers for the server, PostgreSQL, and Redis) |
| **IDE Debugging**     | Built-in [DAP](https://microsoft.github.io/debug-adapter-protocol/) support | Regular container debugging                                                              |
| **Custom auth**       | Yes                                                                         | Yes (with license key)                                                                   |

<Tip>
  For full reference details, refer to the [LangGraph CLI reference](/langsmith/cli) page.
</Tip>

## Development

Here's the typical workflow when building applications:

```mermaid theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
flowchart LR
    A["Develop<br/><code>langgraph dev</code>"] --> B["Test Locally<br/><code>langgraph dev</code>"] --> C["Validate<br/><code>langgraph up</code>"] --> D["Deploy<br/>via UI or API"]

    style A fill:#E5F4FF,stroke:#006DDD,stroke-width:2px,color:#030710
    style B fill:#E5F4FF,stroke:#006DDD,stroke-width:2px,color:#030710
    style C fill:#FDF3FF,stroke:#7E65AE,stroke-width:2px,color:#504B5F
    style D fill:#F6FFDB,stroke:#6E8900,stroke-width:2px,color:#2E3900
```

| Stage                      | Tool                                        | Purpose                                            |
| -------------------------- | ------------------------------------------- | -------------------------------------------------- |
| **Develop & Test Locally** | [`langgraph dev`](/langsmith/cli#dev)       | Write and iterate on your graph with hot reloading |
| **Validate**               | [`langgraph up`](/langsmith/cli#up)         | Test production-like behavior with full stack      |
| **Deploy**                 | [`langgraph deploy`](/langsmith/cli#deploy) | Deploy to production with confidence               |

### Recommended workflow

1. **Daily development**: Use `langgraph dev` for rapid iteration.
2. **Periodic validation**: Test major changes with `langgraph up`.
3. **Pre-deployment check**: Run `langgraph up --recreate` for a fresh build.
4. **Deploy**: Push to production via the [LangSmith UI](/langsmith/deployment-quickstart) or [Control Plane API](/langsmith/api-ref-control-plane).

## `langgraph dev`

The [`langgraph dev`](/langsmith/cli#dev) command runs a lightweight server directly in your environment, designed for speed and convenience during active development. The key features include:

* **No Docker required**: Runs directly in your environment.
* **Hot reloading**: Automatically reloads when you change code.
* **Fast startup**: Ready in seconds.
* **Built-in [Debug Adapter Protocol](https://microsoft.github.io/debug-adapter-protocol/) support**: Attach your IDE debugger to the server for line-level breakpoints & debugging.
* **Local storage**: State persisted to local directory.

<Note>
  The `dev` server is tested with the same integration test suite as production to ensure its behavior is the same during development while using minimal resources.
</Note>

<Accordion title="Get started with langgraph dev">
  Before you begin, ensure you have:

  * An API key for [LangSmith](https://smith.langchain.com/settings) (free to sign up).
  * [uv](https://docs.astral.sh/uv/getting-started/installation/) for Python or [npx](https://docs.npmjs.com/cli/commands/npx) for TypeScript.

  <Steps>
    <Step title="Create a LangGraph app">
      Create a new app from the [`new-langgraph-project-python` template](https://github.com/langchain-ai/new-langgraph-project) or [`new-langgraph-project-js` template](https://github.com/langchain-ai/new-langgraphjs-project). This template demonstrates a single-node application you can extend with your own logic.

      <Tabs>
        <Tab title="Python server">
          ```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
          uvx --from langgraph-cli@latest langgraph new path/to/your/app --template new-langgraph-project-python
          ```
        </Tab>

        <Tab title="Node server">
          ```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
          npx @langchain/langgraph-cli new path/to/your/app --template new-langgraph-project-js
          ```
        </Tab>
      </Tabs>

      <Tip>
        **Additional templates**<br />
        If you use [`langgraph new`](/langsmith/cli) without specifying a template, you will be presented with an interactive menu that will allow you to choose from a list of available templates.
      </Tip>
    </Step>

    <Step title="Install dependencies">
      <Tabs>
        <Tab title="Python server">
          ```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
          cd path/to/your/app
          uv sync --dev -U
          ```
        </Tab>

        <Tab title="Node server">
          ```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
          cd path/to/your/app
          yarn install
          ```
        </Tab>
      </Tabs>
    </Step>

    <Step title="Launch Agent Server">
      <Tabs>
        <Tab title="Python server">
          ```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
          uv run langgraph dev
          ```
        </Tab>

        <Tab title="Node server">
          ```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
          npx @langchain/langgraph-cli dev
          ```
        </Tab>
      </Tabs>

      Sample output:

      ```
      >    Ready!
      >
      >    - API: [http://localhost:2024](http://localhost:2024/)
      >
      >    - Docs: http://localhost:2024/docs
      >
      >    - Studio Web UI: https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:2024
      ```
    </Step>

    <Step title="Test the API">
      <Tabs>
        <Tab title="Python SDK (async)">
          1. Install the LangGraph Python SDK:

          ```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
          pip install langgraph-sdk
          ```

          2. Send a message to the assistant (threadless run):

          ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
          from langgraph_sdk import get_client
          import asyncio

          client = get_client(url="http://localhost:2024")

          async def main():
              async for chunk in client.runs.stream(
                  None,  # Threadless run
                  "agent", # Name of assistant. Defined in langgraph.json.
                  input={
                  "messages": [{
                      "role": "human",
                      "content": "What is LangGraph?",
                      }],
                  },
              ):
                  print(f"Receiving new event of type: {chunk.event}...")
                  print(chunk.data)
                  print("\n\n")

          asyncio.run(main())
          ```
        </Tab>

        <Tab title="Python SDK (sync)">
          1. Install the LangGraph Python SDK:

          ```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
          pip install langgraph-sdk
          ```

          2. Send a message to the assistant (threadless run):

          ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
          from langgraph_sdk import get_sync_client

          client = get_sync_client(url="http://localhost:2024")

          for chunk in client.runs.stream(
              None,  # Threadless run
              "agent", # Name of assistant. Defined in langgraph.json.
              input={
                  "messages": [{
                      "role": "human",
                      "content": "What is LangGraph?",
                  }],
              },
              stream_mode="messages-tuple",
          ):
              print(f"Receiving new event of type: {chunk.event}...")
              print(chunk.data)
              print("\n\n")
          ```
        </Tab>

        <Tab title="Javascript SDK">
          1. Install the LangGraph JS SDK:

          ```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
          npm install @langchain/langgraph-sdk
          ```

          2. Send a message to the assistant (threadless run):

          ```js theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
          const { Client } = await import("@langchain/langgraph-sdk");

          // only set the apiUrl if you changed the default port when calling langgraph dev
          const client = new Client({ apiUrl: "http://localhost:2024"});

          const streamResponse = client.runs.stream(
              null, // Threadless run
              "agent", // Assistant ID
              {
                  input: {
                      "messages": [
                          { "role": "user", "content": "What is LangGraph?"}
                      ]
                  },
                  streamMode: "messages-tuple",
              }
          );

          for await (const chunk of streamResponse) {
              console.log(`Receiving new event of type: ${chunk.event}...`);
              console.log(JSON.stringify(chunk.data));
              console.log("\n\n");
          }
          ```
        </Tab>

        <Tab title="Rest API">
          ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
          curl -s --request POST \
              --url "http://localhost:2024/runs/stream" \
              --header 'Content-Type: application/json' \
              --data "{
                  \"assistant_id\": \"agent\",
                  \"input\": {
                      \"messages\": [
                          {
                              \"role\": \"human\",
                              \"content\": \"What is LangGraph?\"
                          }
                      ]
                  },
                  \"stream_mode\": \"messages-tuple\"
              }"
          ```
        </Tab>
      </Tabs>
    </Step>
  </Steps>
</Accordion>

### Use cases

Use `langgraph dev` as your primary development tool for:

* **Daily feature development**: Make changes to your code and the server automatically reloads. Test immediately without rebuilding containers—perfect for fast iteration cycles.

* **Quick prototyping and experiments**: Spin up a server in seconds to test ideas without Docker setup overhead.

* **Environments without Docker**: In CI/CD pipelines or lightweight VMs where Docker isn't available:
  ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  langgraph dev --no-browser
  ```

* **Debugger attachment**: Use `--debug-port` to attach your IDE debugger for step-through debugging during development.

## `langgraph up`

The [`langgraph up`](/langsmith/cli#up) command orchestrates a full Docker-based stack that mirrors production infrastructure, helping catch deployment issues before production. The key features include:

* **Verify build & dependencies**: Tests your build process and dependencies.
* **Isolated networking**: Realistic container networking.
* **Production validation**: Verifies deployment readiness.

<Accordion title="Get started with langgraph up">
  ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  # Ensure Docker is running
  docker ps

  # Start production-like stack
  langgraph up
  ```

  Your server starts at `http://localhost:8123` with full persistent storage.
</Accordion>

### Use cases

Use `langgraph up` for validation and production-readiness testing:

* **Pre-deployment validation**: Before deploying to production, you can run a final check with a fresh build to ensure your dependencies are all correctly specified.

  ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  langgraph up --recreate
  ```

  This catches issues related to dependency resolution in containers and any other build process problems.

* **Major feature validation**: After implementing significant changes, test with the full production stack periodically to ensure everything works in a containerized environment.

* **Docker troubleshooting**: When debugging container-specific issues, networking problems, or environment variable configurations that only appear in production.

## Pre-deployment checklist

Before deploying an application, verify the following with `langgraph up`:

* All [dependencies](/langsmith/setup-app-requirements-txt) install correctly in the container.
* Application starts without errors.
* Graph executes successfully.
* All [environment variables](/langsmith/env-var) work correctly.
* [Authentication/authorization](/langsmith/cli#adding-custom-authentication) works as expected.

## Dependencies configuration

Both `langgraph dev` and `langgraph up` read your application's [dependencies](/langsmith/application-structure#dependencies) from your [configuration files](/langsmith/application-structure#configuration-file), but they run in different environments:

* **`langgraph dev`** runs your code directly in your local environment (Python or Node.js) without Docker.
* **`langgraph up`** builds a Docker container and runs your code inside that isolated container.

Properly configuring your dependencies ensures both commands work correctly and that what you test locally matches what gets deployed to production.

### `langgraph.json` file

The `dependencies` field tells the [CLI](/langsmith/cli) **where** to find your application code. The `dependencies` field can point to:

* **A directory with package config** (containing `pyproject.toml`, `setup.py`, `requirements.txt`, or `package.json`)
* **A specific subdirectory**: `"dependencies": ["./my_agent"]`
* **A specific package**: `"dependencies": ["my-package==1.0.0"]` (Python) or `"dependencies": ["my-package@1.0.0"]` (JavaScript)

<Tabs>
  <Tab title="Python">
    ```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    {
      "dependencies": ["."],
      "graphs": {
        "my_agent": "./my_agent/agent.py:graph"
      },
      "env": "./.env"
    }
    ```
  </Tab>

  <Tab title="JavaScript">
    ```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    {
      "dependencies": ["."],
      "graphs": {
        "my_agent": "./my_agent/agent.js:graph"
      },
      "env": "./.env"
    }
    ```
  </Tab>
</Tabs>

### Package dependency files

These files define **what** packages your application needs:

<Tabs>
  <Tab title="Python">
    **pyproject.toml example:**

    ```toml theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    [project]
    name = "my-agent"
    version = "0.1.0"
    dependencies = [
        "langchain-openai",
        "langchain-anthropic",
        "langgraph",
    ]
    ```

    **requirements.txt example:**

    ```
    langchain-openai
    langchain-anthropic
    langgraph
    ```
  </Tab>

  <Tab title="JavaScript">
    **package.json example:**

    ```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    {
      "name": "my-agent",
      "version": "1.0.0",
      "dependencies": {
        "@langchain/openai": "^0.3.0",
        "@langchain/anthropic": "^0.3.0",
        "@langchain/langgraph": "^0.2.0"
      }
    }
    ```
  </Tab>
</Tabs>

### Dependency resolution process

When you run [`langgraph up`](/langsmith/cli#up), the CLI follows these steps to install your application's dependencies:

1. [`langgraph.json`](/langsmith/application-structure#configuration-file) tells the CLI **where** to look for your application code. The `dependencies: ["."]` field points to the current directory.
2. **Find package configuration**: The CLI looks in that directory for a package configuration file ([`pyproject.toml`](/langsmith/setup-pyproject), [`requirements.txt`](/langsmith/setup-app-requirements-txt), or [`package.json`](/langsmith/setup-javascript)).
3. **Read dependencies list**: The CLI reads the list of packages from the configuration file.
4. **Install packages**: The CLI installs all the packages using the appropriate package manager for your language (`uv` or `pip` for Python, `npm` for JavaScript).

This two-file approach separates concerns: `langgraph.json` handles application structure and location, while the package configuration file handles language-specific package dependencies.

For more information on the installer, refer to [CLI configuration file](/langsmith/cli#configuration-file).

### Troubleshooting

If you encounter issues with dependency installation, try switching to `pip`:

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "dependencies": ["."],
  "pip_installer": "pip"
}
```

Then rebuild:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
langgraph up --recreate
```

## Debug your local Docker setup

Production deployment might succeed even when `langgraph up` fails on your local machine. This happens because production uses managed infrastructure while `langgraph up` runs the full stack locally on your computer.

The following are common local environment issues that don't affect production.

### Docker configuration issues

`langgraph up` requires Docker locally:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}

# Check if Docker is running
docker ps
```

[Cloud deployments](/langsmith/cloud) don't use your local Docker.

**Solution**: Install Docker, or use `langgraph dev` for local testing.

### Port conflicts

`langgraph up` uses ports `8123`, `5432`, and `6379` that might be occupied:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}

# Check for conflicts
lsof -i :8123  # API server
lsof -i :5432  # PostgreSQL
lsof -i :6379  # Redis
```

**Solution**: Stop conflicting services or use the [`--port`](/langsmith/cli#dev) flag.

### Resource constraints

`langgraph up` requires more RAM and disk for:

* PostgreSQL container
* Redis container
* API server container

**Solution**: Free up resources or use `langgraph dev`.

### Network configuration

VPN connections, firewall rules, or corporate proxy settings can affect local Docker networking.

**Solution**: Test with `langgraph dev` or temporarily disable VPN/firewall to isolate the issue.

## Next steps

Now that you have a LangGraph app running locally, you're ready to deploy it:

**Choose a hosting option for LangSmith:**

* [**Cloud**](/langsmith/cloud): Fastest setup, fully managed (recommended).
* [**Self-hosted**](/langsmith/self-hosted): Full control in your infrastructure.

For more details, refer to the [Platform setup comparison](/langsmith/platform-setup).

**Then deploy your app:**

* [Deploy to Cloud quickstart](/langsmith/deployment-quickstart): Quick setup guide.
* [Full Cloud setup guide](/langsmith/deploy-to-cloud): Comprehensive deployment documentation.

**Explore features:**

* **[Studio](/langsmith/studio)**: Visualize, interact with, and debug your application with the Studio UI. Try the [Studio quickstart](/langsmith/quick-start-studio).
* **API References**: [LangSmith Deployment API](https://langchain-ai.github.io/langgraph/cloud/reference/api/api_ref/), [Python SDK](/langsmith/langgraph-python-sdk), [JS/TS SDK](/langsmith/langgraph-js-ts-sdk)

## Related resources

* [CLI Reference](/langsmith/cli): Detailed documentation for all CLI commands
* [Application Structure](/langsmith/application-structure): How to structure your LangGraph application
* [Troubleshooting](/langsmith/troubleshooting-studio): Common issues and solutions
* [Setting up with pyproject.toml](/langsmith/setup-pyproject): Configure Python dependencies
* [Setting up with requirements.txt](/langsmith/setup-app-requirements-txt): Alternative dependency configuration

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/local-dev-testing.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
