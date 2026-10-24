# Managed Deep Agents SDKs
Source: https://docs.langchain.com/langsmith/managed-deep-agents-sdk

Use the Python, TypeScript, and React SDKs for Managed Deep Agents.

Build, run, and stream Managed Deep Agents from Python, TypeScript, and React. The SDKs wrap the `/v1/deepagents` API for creating agents, managing threads, streaming runs, registering MCP servers, and building React UIs.

For concepts, see the [Managed Deep Agents overview](/langsmith/managed-deep-agents-overview). For an end-to-end walkthrough, follow the [quickstart](/langsmith/managed-deep-agents-quickstart).

<Note>
  The SDK packages are in **public beta**. Method signatures and payload fields can change during the beta.

  Managed Deep Agents is in **private preview**, available on [LangSmith Cloud](/langsmith/cloud) in the US region only. [Join the waitlist](https://www.langchain.com/langsmith-managed-deep-agents-waitlist) to request access.
</Note>

## Install

<CodeGroup>
  ```bash Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  uv add managed-deepagents

  # or with pip
  pip install managed-deepagents
  ```

  ```bash TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  npm install @langchain/managed-deepagents
  ```

  ```bash React theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  npm install @langchain/managed-deepagents @langchain/react
  ```
</CodeGroup>

Requirements:

* Python 3.10 or newer for `managed-deepagents`.
* Node.js 20 or newer for `@langchain/managed-deepagents`.
* Managed Deep Agents [private preview access](https://www.langchain.com/langsmith-managed-deep-agents-waitlist).
* A [LangSmith API key](/langsmith/create-account-api-key) for a workspace with private preview access.

## Configure a client

Set your API key:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
export LANGSMITH_API_KEY="<LANGSMITH_API_KEY>"
```

Both SDKs default to `https://api.smith.langchain.com/v1/deepagents`. To use a compatible endpoint, set `LANGSMITH_ENDPOINT` or pass the API URL directly:

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from managed_deepagents import Client

  client = Client(
      api_key="<LANGSMITH_API_KEY>",
      api_url="https://api.smith.langchain.com/v1/deepagents",
  )
  ```

  ```ts TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { Client } from "@langchain/managed-deepagents";

  const client = new Client({
    apiKey: process.env.LANGSMITH_API_KEY,
    apiUrl: "https://api.smith.langchain.com/v1/deepagents",
  });
  ```
</CodeGroup>

## Create an agent

Requests to create an agent can use the same top-level `model` and `backend` fields as the [Managed Deep Agents CLI](/langsmith/managed-deep-agents-cli). Pass `model` as an object with an `id` of `{provider}:{model_id}`. See [supported providers and models](/oss/python/langchain/models#supported-providers-and-models).

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from managed_deepagents import Client

  with Client() as client:
      agent = client.agents.create(
          name="research-assistant",
          description="Research assistant that can search the web and summarize sources.",
          model={"id": "openai:gpt-5.5"},
          backend={"type": "state"},
          instructions=(
              "You are a careful research assistant. Search for sources, "
              "keep notes, and return concise answers with citations."
          ),
      )

  print(f"Agent ID: {agent['id']}")
  ```

  ```ts TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { Client } from "@langchain/managed-deepagents";

  const client = new Client({
    apiKey: process.env.LANGSMITH_API_KEY,
  });

  const agent = await client.agents.create({
    name: "research-assistant",
    description: "Research assistant that can search the web and summarize sources.",
    model: { id: "openai:gpt-5.5" },
    backend: { type: "state" },
    instructions:
      "You are a careful research assistant. Search for sources, keep notes, and return concise answers with citations.",
  });

  console.log(`Agent ID: ${agent.id}`);
  ```
</CodeGroup>

Python methods return dict-like responses, so use `agent["id"]`. TypeScript methods return typed objects, so use `agent.id`.

## Run and stream

Create a thread before running the agent. [Threads](/langsmith/use-threads#understand-threads) preserve conversation and execution state, so you can resume or inspect a run later. Use the `id` returned when you created the agent.

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from managed_deepagents import Client

  agent_id = "<agent_id>"

  with Client() as client:
      thread = client.threads.create(
          agent_id=agent_id,
          options={
              "test_run": False,
              "skip_memory_write_protection": False,
          },
      )

      for event in client.threads.stream(
          thread["id"],
          agent_id=agent_id,
          messages=[
              {
                  "role": "user",
                  "content": "Research recent approaches to agent memory and summarize the main trade-offs.",
              }
          ],
          stream_mode=["values", "updates", "messages-tuple"],
          stream_subgraphs=True,
      ):
          print(event.event, event.data)
  ```

  ```ts TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { Client } from "@langchain/managed-deepagents";

  const agentId = "<agent_id>";
  const client = new Client({
    apiKey: process.env.LANGSMITH_API_KEY,
  });

  const thread = await client.threads.create({
    agent_id: agentId,
    options: {
      test_run: false,
      skip_memory_write_protection: false,
    },
  });

  const langGraphClient = client.getLangGraphClient({ agentId });
  const stream = langGraphClient.runs.stream(thread.id, agentId, {
    input: {
      messages: [
        {
          role: "user",
          content:
            "Research recent approaches to agent memory and summarize the main trade-offs.",
        },
      ],
    },
    streamMode: ["values", "updates", "messages-tuple"],
    streamSubgraphs: true,
  });

  for await (const event of stream) {
    console.log(event.event, event.data);
  }
  ```
</CodeGroup>

The `options` object is optional, and both fields default to `false`. Set `test_run` to `true` to mark the thread as a test run that is filtered out of usage and analytics. By default, `skip_memory_write_protection` lets the runtime raise a human-in-the-loop interrupt before the agent writes to long-term memory, so you can approve or reject the write. Set it to `true` to let memory writes proceed immediately, which is useful for headless runs where no human is available to approve the write.

In Python, stream directly with `client.threads.stream(...)`. In TypeScript, get a LangGraph client with `client.getLangGraphClient(...)` and stream with `runs.stream(...)`, which accepts the message list under `input`. Each event exposes an `event` type and a `data` payload. The types you receive depend on `stream_mode`. For the stream modes and event types, see [Stream a run from a thread](/langsmith/managed-deep-agents-invoke#stream-a-run-from-a-thread).

## Use React `useStream`

The TypeScript SDK includes a LangGraph client adapter for `@langchain/react`. Use `getLangGraphClient()` so `useStream` manages thread lifecycle, run submission, and state updates, while the Managed Deep Agents SDK supplies the correct routes, auth headers, and payload format.

<Warning>
  Do not ship your LangSmith API key to the browser. In production React apps, route requests through your backend with a custom `fetch` instead of passing `apiKey` directly.
</Warning>

```tsx theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { Client } from "@langchain/managed-deepagents";
import { useStream } from "@langchain/react";

const agentId = "<agent_id>";

const managedDeepAgents = new Client({
  // In browser apps, prefer passing a custom fetch that calls your backend.
  apiKey: process.env.LANGSMITH_API_KEY,
});

const client = managedDeepAgents.getLangGraphClient({ agentId });

export function ManagedDeepAgentStream() {
  const stream = useStream({
    client,
    assistantId: agentId,
    fetchStateHistory: false,
  });

  return (
    <section>
      <button
        type="button"
        disabled={stream.isLoading}
        onClick={() => {
          void stream.submit({
            messages: [
              { role: "user", content: "Write a short status update." },
            ],
          });
        }}
      >
        Run agent
      </button>

      {stream.messages.map((message, index) => (
        <p key={message.id ?? index}>{String(message.content)}</p>
      ))}

      <p>State keys: {Object.keys(stream.values).join(", ")}</p>
    </section>
  );
}
```

## Resources

The SDK clients expose these resource groups:

| Resource         | Python                 | TypeScript            |
| ---------------- | ---------------------- | --------------------- |
| Agents           | `client.agents`        | `client.agents`       |
| Threads and runs | `client.threads`       | `client.threads`      |
| MCP servers      | `client.mcp_servers`   | `client.mcpServers`   |
| Auth sessions    | `client.auth_sessions` | `client.authSessions` |

Python methods use `snake_case`, such as `create_and_run` and `resolve_interrupt`. TypeScript methods use `camelCase`, such as `createAndRun` and `resolveInterrupt`.

The SDKs can register MCP servers, complete auth sessions, and discover a registered server's tool schemas with `client.mcp_servers.list_tools(...)` in Python or `client.mcpServers.listTools(...)` in TypeScript. Pass the selected tool entries to `client.agents.create(...)` or `client.agents.update(...)`.

## Handle errors

Requests raise typed errors that include the HTTP status, an error code, and response detail.

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from managed_deepagents import Client, ManagedDeepAgentsAPIError

  with Client() as client:
      try:
          client.agents.get("missing-agent")
      except ManagedDeepAgentsAPIError as error:
          print(error.status_code, error.code, error.detail)
  ```

  ```ts TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { Client, ManagedDeepAgentsAPIError } from "@langchain/managed-deepagents";

  const client = new Client({
    apiKey: process.env.LANGSMITH_API_KEY,
  });

  try {
    await client.agents.get("missing-agent");
  } catch (error) {
    if (error instanceof ManagedDeepAgentsAPIError) {
      console.log(error.status, error.code, error.detail);
    }
  }
  ```
</CodeGroup>

For endpoint-level request and response schemas, see the [Managed Deep Agents API reference](/langsmith/managed-deep-agents-api-overview).

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/managed-deep-agents-sdk.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Configure prompt settings
Source: https://docs.langchain.com/langsmith/managing-model-configurations

The [Playground](/langsmith/prompt-engineering-concepts#playground) enables you to control various settings for your prompts. The **Prompt Settings** window contains:

* [Model configuration](#model-configurations)
* [Tool settings](#tool-settings)
* [Prompt formatting](#prompt-formatting)

To access **Prompt Settings**:

1. Navigate to the **Playground** in the left sidebar.
2. Under the **Prompts** heading select the gear <Icon icon="settings" /> icon next to the model name, which will launch the **Prompt Settings** window.

   <div>
     <img alt="Model Configuration window in the LangSmith UI, settings for Provider, Model, Temperature, Max Output Tokens, Top P, Presence Penalty, Frequency Penalty, Reasoning Effort, etc." />

     <img alt="Model Configuration window in the LangSmith UI, settings for Provider, Model, Temperature, Max Output Tokens, Top P, Presence Penalty, Frequency Penalty, Reasoning Effort, etc." />
   </div>

## Model configurations

[Model configurations](/langsmith/model-configurations) define the parameters your prompt runs against. Configurations are shared across your workspace—any configuration saved here is available in other LangSmith features and visible to admins in **Settings** > **Model configurations**. For details on specific settings, refer to your model provider’s documentation (for example, [Anthropic](https://platform.claude.com/docs/en/api/messages) or [OpenAI](https://platform.openai.com/docs/api-reference/responses/create)).

### Create saved configurations

1. In the **Model Configurations** tab, adjust the model configuration as needed—you can select a [saved configuration to edit](#edit-configurations).
2. Click the **Save As** button in the top bar.
3. Enter a name and optional description for your configuration and confirm.
4. Now that you've saved the configuration, anyone in your organization's [workspace](/langsmith/administration-overview#workspaces) can access it. All saved configurations are available in the **Model Configuration** dropdown.
5. Once you have created a saved configuration, you can set it as your default, so any new prompt you create will automatically use this configuration. To set a configuration as your default, click the **Set as default** <Icon icon="pinned" /> icon next to the model name in the dropdown.

### Edit configurations

1. To rename a saved configuration, or update the description, select the configuration name or description and make the necessary changes.
2. Update the current configuration's parameters as needed and click the **Save** button at the top.

### Delete configurations

1. Select the configuration you want to remove.
2. Click the trash <Icon icon="trash" /> icon to delete it.

### Extra parameters

The **Extra Parameters** field allows you to pass additional model parameters that aren't directly supported in the LangSmith interface. This is particularly useful in two scenarios:

1. When model providers release new parameters that haven't yet been integrated into the LangSmith interface. You can specify these parameters in JSON format to use them right away. For example:

   ```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
   {
       "reasoning_effort": "medium"
   }
   ```

2. When troubleshooting parameter-related errors in the Playground, such as:

   ```
   TypeError: AsyncCompletions.create() got an unexpected keyword argument 'max_concurrency'
   ```

   If you receive an error about unnecessary parameters (which is more common when using [LangChain JS](/oss/python/langchain/overview) for run tracing), you can use this field to remove the extra parameters.

## Tool settings

[*Tools*](/langsmith/prompt-engineering-concepts#tools) enable your LLM to perform tasks like searching the web, looking up information, and so on. In the **Tools Settings** tab, you can manage the ways your LLM uses and accesses the tools you have defined in your prompt, including:

* **Parallel Tool Calls**: Calling multiple tools in parallel when appropriate. This allows the model to gather information from different sources simultaneously. (Dependent on model support for parallel execution.)
* **Tool Choice**: Select the tools that the model can access. For more details, refer to [Use tools in a prompt](/langsmith/use-tools).

<Callout icon="tool">
  To manage which tools are available in your workspace, including enabling, disabling, and editing tools across prompts, refer to [Manage tools with the registry](/langsmith/use-tools#manage-tools-with-the-registry).
</Callout>

## Prompt formatting

The **Prompt Format** tab allows you to specify:

* The **Prompt type**. For details on chat and completion prompts, refer to [Prompt engineering](/langsmith/prompt-engineering-concepts#prompt-types) concepts.
* The **Template format**. For details on prompt templating and using variables, refer to [F-string vs. mustache](/langsmith/prompt-engineering-concepts#f-string-vs-mustache).

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/managing-model-configurations.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Prevent logging of sensitive data in traces
Source: https://docs.langchain.com/langsmith/mask-inputs-outputs

When working with LangSmith traces, you may need to prevent sensitive information from being logged to maintain privacy and comply with security requirements. LangSmith provides multiple approaches to protect your data before it's sent to the backend:

* [Completely hide inputs and outputs](#hide-inputs-and-outputs) using environment variables or [Client](https://reference.langchain.com/python/langsmith/client/Client) configuration.
* [Hide metadata](#hide-metadata) to remove or transform run metadata.
* [Apply rule-based masking](#rule-based-masking-of-inputs-and-outputs) with regex patterns or anonymization libraries to selectively redact sensitive information.
* [Process inputs and outputs for individual functions](#processing-inputs-and-outputs-for-a-single-function) with function-level customization.
* [Use third-party anonymizers](#examples) like Microsoft Presidio and Amazon Comprehend for advanced PII detection.
* [Batch process run operations](#batch-processing-for-high-throughput-masking) to apply expensive masking logic across multiple runs at once, reducing per-run overhead. LangSmith processes runs in a background thread, which does not block your application.
* [Redact inputs and outputs per request](/langsmith/conditional-tracing#conditionally-redact-inputs-and-outputs) using `tracing_context` to mask data only for specific invocations (for example, based on tenant or feature flag) while leaving other traces untouched.

<Note>
  If your compliance or privacy requirements mandate that certain operations should never be traced at all (for example, clients with zero-retention policies), consider using [conditional tracing](/langsmith/conditional-tracing) to disable tracing selectively for specific requests instead of masking data.
</Note>

## Hide inputs and outputs

If you want to completely hide the inputs and outputs of your traces, you can set the following environment variables when running your application:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
LANGSMITH_HIDE_INPUTS=true
LANGSMITH_HIDE_OUTPUTS=true
```

This works for both the LangSmith SDK (Python and TypeScript) and LangChain.

You can also customize and override this behavior for a given [Client](https://reference.langchain.com/python/langsmith/client/Client) instance. This can be done by setting the `hide_inputs` and `hide_outputs` parameters on the [Client](https://reference.langchain.com/python/langsmith/client/Client) object (`hideInputs` and `hideOutputs` in TypeScript).

The following example returns an empty object for both `hide_inputs` and `hide_outputs`, but you can customize this to your needs:

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import openai
  from langsmith import Client
  from langsmith.wrappers import wrap_openai

  openai_client = wrap_openai(openai.Client())
  langsmith_client = Client(
      hide_inputs=lambda inputs: {}, hide_outputs=lambda outputs: {}
  )

  # The trace produced will have its metadata present, but the inputs will be hidden
  openai_client.chat.completions.create(
      model="gpt-5.4-mini",
      messages=[
          {"role": "system", "content": "You are a helpful assistant."},
          {"role": "user", "content": "Hello!"},
      ],
      langsmith_extra={"client": langsmith_client},
  )

  # The trace produced will not have hidden inputs and outputs
  openai_client.chat.completions.create(
      model="gpt-5.4-mini",
      messages=[
          {"role": "system", "content": "You are a helpful assistant."},
          {"role": "user", "content": "Hello!"},
      ],
  )
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import OpenAI from "openai";
  import { Client } from "langsmith";
  import { wrapOpenAI } from "langsmith/wrappers";

  const langsmithClient = new Client({
      hideInputs: (inputs) => ({}),
      hideOutputs: (outputs) => ({}),
  });

  // The trace produced will have its metadata present, but the inputs will be hidden
  const filteredOAIClient = wrapOpenAI(new OpenAI(), {
      client: langsmithClient,
  });
  await filteredOAIClient.chat.completions.create({
      model: "gpt-5.4-mini",
      messages: [
          { role: "system", content: "You are a helpful assistant." },
          { role: "user", content: "Hello!" },
      ],
  });

  const openaiClient = wrapOpenAI(new OpenAI());
  // The trace produced will not have hidden inputs and outputs
  await openaiClient.chat.completions.create({
      model: "gpt-5.4-mini",
      messages: [
          { role: "system", content: "You are a helpful assistant." },
          { role: "user", content: "Hello!" },
      ],
  });
  ```
</CodeGroup>

## Hide metadata

The `hide_metadata` parameter allows you to control whether run metadata is hidden or transformed when tracing with the LangSmith Python SDK. Metadata is passed with the `extra` parameter when creating runs (e.g., `extra={"metadata": {...}}`). `hide_metadata` is useful for removing sensitive information, complying with privacy requirements, or reducing the amount of data sent to LangSmith. You can configure metadata hiding in two ways:

* Using the SDK:

  ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langsmith import Client

  client = Client(hide_metadata=True)
  ```

* Using environment variables:

  ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  export LANGSMITH_HIDE_METADATA=true
  ```

The `hide_metadata` parameter accepts three types of values:

* `True`: Completely removes all metadata (sends an empty dictionary).
* `False` or `None`: Preserves metadata as-is (default behavior).
* `Callable`: A custom function that transforms the metadata dictionary.

When set, this parameter affects the `metadata` field in the `extra` parameter for all runs created or updated by the [Client](https://reference.langchain.com/python/langsmith/client/Client), including runs created through the `@traceable` decorator or LangChain integrations.

### Hide all metadata

Set `hide_metadata=True` to remove all metadata completely from runs sent to LangSmith:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langsmith import Client

# Hide all metadata completely
client = Client(hide_metadata=True)

# Now when you create runs, metadata will be empty
client.create_run(
    "my_run",
    inputs={"question": "What is 2+2?"},
    run_type="llm",
    extra={"metadata": {"user_id": "123", "session": "abc"}}
)

# The metadata sent to LangSmith will be {} instead of the provided metadata
```

### Custom transformation

Use a callable function to selectively filter, redact, or modify metadata before it's sent to LangSmith:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}

# Remove sensitive keys
def hide_sensitive_metadata(metadata: dict) -> dict:
    return {k: v for k, v in metadata.items() if not k.startswith("_private")}

client = Client(hide_metadata=hide_sensitive_metadata)

# Redact specific values
def redact_emails(metadata: dict) -> dict:
    import re
    result = {}
    for k, v in metadata.items():
        if isinstance(v, str) and "@" in v:
            result[k] = "[REDACTED_EMAIL]"
        else:
            result[k] = v
    return result

client = Client(hide_metadata=redact_emails)

# Add transformation marker
def add_marker(metadata: dict) -> dict:
    return {**metadata, "transformed": True}

client = Client(hide_metadata=add_marker)
```

## Rule-based masking of inputs and outputs

<Info>
  This feature is available in the following LangSmith SDK versions:

  * Python: 0.1.81 and above
  * TypeScript: 0.1.33 and above
</Info>

To mask specific data in inputs and outputs, you can use the `create_anonymizer` / `createAnonymizer` function and pass the newly created anonymizer when instantiating the [Client](https://reference.langchain.com/python/langsmith/client/Client). The anonymizer can be either constructed from a list of regex patterns and the replacement values or from a function that accepts and returns a string value.

The anonymizer will be skipped for inputs if `LANGSMITH_HIDE_INPUTS = true`. Same applies for outputs if `LANGSMITH_HIDE_OUTPUTS = true`.

However, if inputs or outputs are to be sent to [Client](https://reference.langchain.com/python/langsmith/client/Client), the `anonymizer` method will take precedence over functions found in `hide_inputs` and `hide_outputs`. By default, the `create_anonymizer` will only look at maximum of 10 nesting levels deep, which can be configured via the `max_depth` parameter.

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langsmith.anonymizer import create_anonymizer
  from langsmith import Client, traceable
  import re

  # create anonymizer from list of regex patterns and replacement values
  anonymizer = create_anonymizer([
      { "pattern": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+.[a-zA-Z]{2,}", "replace": "<email-address>" },
      { "pattern": r"[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}", "replace": "<UUID>" }
  ])

  # or create anonymizer from a function
  email_pattern = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+.[a-zA-Z]{2,}")
  uuid_pattern = re.compile(r"[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}")
  anonymizer = create_anonymizer(
      lambda text: email_pattern.sub("<email-address>", uuid_pattern.sub("<UUID>", text))
  )

  client = Client(anonymizer=anonymizer)

  @traceable(client=client)
  def main(inputs: dict) -> dict:
      ...
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { createAnonymizer } from "langsmith/anonymizer"
  import { traceable } from "langsmith/traceable"
  import { Client } from "langsmith"

  // create anonymizer from list of regex patterns and replacement values
  const anonymizer = createAnonymizer([
      { pattern: /[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+.[a-zA-Z]{2,}/g, replace: "<email>" },
      { pattern: /[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}/g, replace: "<uuid>" }
  ])

  // or create anonymizer from a function
  const anonymizer = createAnonymizer((value) => value.replace("...", "<value>"))

  const client = new Client({ anonymizer })

  const main = traceable(async (inputs: any) => {
      // ...
  }, { client })
  ```
</CodeGroup>

Please note, that using the anonymizer might incur a performance hit with complex regular expressions or large payloads, as the anonymizer serializes the payload to JSON before processing.

<Note>
  Improving the performance of `anonymizer` API is on our roadmap! If you are encountering performance issues, please contact support via [support.langchain.com](https://support.langchain.com).
</Note>

<img alt="Hide inputs outputs" />

Older versions of LangSmith SDKs can use the `hide_inputs` and `hide_outputs` parameters to achieve the same effect. You can also use these parameters to process the inputs and outputs more efficiently.

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import re
  from langsmith import Client, traceable

  # Define the regex patterns for email addresses and UUIDs
  EMAIL_REGEX = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+.[a-zA-Z]{2,}"
  UUID_REGEX = r"[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}"

  def replace_sensitive_data(data, depth=10):
      if depth == 0:
          return data
      if isinstance(data, dict):
          return {k: replace_sensitive_data(v, depth-1) for k, v in data.items()}
      elif isinstance(data, list):
          return [replace_sensitive_data(item, depth-1) for item in data]
      elif isinstance(data, str):
          data = re.sub(EMAIL_REGEX, "<email-address>", data)
          data = re.sub(UUID_REGEX, "<UUID>", data)
          return data
      else:
          return data

  client = Client(
      hide_inputs=lambda inputs: replace_sensitive_data(inputs),
      hide_outputs=lambda outputs: replace_sensitive_data(outputs)
  )

  inputs = {"role": "user", "content": "Hello! My email is user@example.com and my ID is 123e4567-e89b-12d3-a456-426614174000."}
  outputs = {"role": "assistant", "content": "Hi! I've noted your email as user@example.com and your ID as 123e4567-e89b-12d3-a456-426614174000."}

  @traceable(client=client)
  def child(inputs: dict) -> dict:
      return outputs

  @traceable(client=client)
  def parent(inputs: dict) -> dict:
      child_outputs = child(inputs)
      return child_outputs

  parent(inputs)
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { Client } from "langsmith";
  import { traceable } from "langsmith/traceable";

  // Define the regex patterns for email addresses and UUIDs
  const EMAIL_REGEX = /[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+.[a-zA-Z]{2,}/g;
  const UUID_REGEX = /[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}/g;

  function replaceSensitiveData(data: any, depth: number = 10): any {
      if (depth === 0) return data;
      if (typeof data === "object" && !Array.isArray(data)) {
          const result: Record<string, any> = {};
          for (const [key, value] of Object.entries(data)) {
              result[key] = replaceSensitiveData(value, depth - 1);
          }
          return result;
      } else if (Array.isArray(data)) {
          return data.map(item => replaceSensitiveData(item, depth - 1));
      } else if (typeof data === "string") {
          return data.replace(EMAIL_REGEX, "<email-address>").replace(UUID_REGEX, "<UUID>");
      } else {
          return data;
      }
  }

  const langsmithClient = new Client({
      hideInputs: (inputs) => replaceSensitiveData(inputs),
      hideOutputs: (outputs) => replaceSensitiveData(outputs)
  });

  const inputs = {
      role: "user",
      content: "Hello! My email is user@example.com and my ID is 123e4567-e89b-12d3-a456-426614174000."
  };
  const outputs = {
      role: "assistant",
      content: "Hi! I've noted your email as <email-address> and your ID as <UUID>."
  };

  const child = traceable(async (inputs: any) => {
      return outputs;
  }, { name: "child", client: langsmithClient });

  const parent = traceable(async (inputs: any) => {
      const childOutputs = await child(inputs);
      return childOutputs;
  }, { name: "parent", client: langsmithClient });

  await parent(inputs);
  ```
</CodeGroup>

## Processing inputs and outputs for a single function

<Info>
  The `process_outputs` parameter is available in LangSmith SDK version 0.1.98 and above for Python.
</Info>

In addition to [Client](https://reference.langchain.com/python/langsmith/client/Client)-level input and output processing, LangSmith provides function-level processing through the `process_inputs` and `process_outputs` parameters of the `@traceable` decorator.

These parameters accept functions that allow you to transform the inputs and outputs of a specific function before they are logged to LangSmith. This is useful for reducing payload size, removing sensitive information, or customizing how an object should be serialized and represented in LangSmith for a particular function.

Here's an example of how to use `process_inputs` and `process_outputs`:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langsmith import traceable

def process_inputs(inputs: dict) -> dict:
    # inputs is a dictionary where keys are argument names and values are the provided arguments
    # Return a new dictionary with processed inputs
    return {
        "processed_key": inputs.get("my_cool_key", "default"),
        "length": len(inputs.get("my_cool_key", ""))
    }

def process_outputs(output: Any) -> dict:
    # output is the direct return value of the function
    # Transform the output into a dictionary
    # In this case, "output" will be an integer
    return {"processed_output": str(output)}

@traceable(process_inputs=process_inputs, process_outputs=process_outputs)
def my_function(my_cool_key: str) -> int:
    # Function implementation
    return len(my_cool_key)

result = my_function("example")
```

In this example, `process_inputs` creates a new dictionary with processed input data, and `process_outputs` transforms the output into a specific format before logging to LangSmith.

<Warning>
  It's recommended to avoid mutating the source objects in the processor functions. Instead, create and return new objects with the processed data.
</Warning>

For asynchronous functions, the usage is similar:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
@traceable(process_inputs=process_inputs, process_outputs=process_outputs)
async def async_function(key: str) -> int:
    # Async implementation
    return len(key)
```

These function-level processors take precedence over [Client](https://reference.langchain.com/python/langsmith/client/Client)-level processors (`hide_inputs` and `hide_outputs`) when both are defined.

## Examples

You can combine rule-based masking with various anonymizers to scrub sensitive information from inputs and outputs. The following examples will cover working with regex, Microsoft Presidio, and Amazon Comprehend.

### Regex

<Info>
  The implementation below is not exhaustive and may miss some formats or edge cases. Test any implementation thoroughly before using it in production.
</Info>

You can use regex to mask inputs and outputs before they are sent to LangSmith. The implementation below masks email addresses, phone numbers, full names, credit card numbers, and SSNs.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import re
import openai
from langsmith import Client
from langsmith.wrappers import wrap_openai

# Define regex patterns for various PII
SSN_PATTERN = re.compile(r'\b\d{3}-\d{2}-\d{4}\b')
CREDIT_CARD_PATTERN = re.compile(r'\b(?:\d[ -]*?){13,16}\b')
EMAIL_PATTERN = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b')
PHONE_PATTERN = re.compile(r'\b(?:\+?1[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b')
FULL_NAME_PATTERN = re.compile(r'\b([A-Z][a-z]*\s[A-Z][a-z]*)\b')

def regex_anonymize(text):
    """
    Anonymize sensitive information in the text using regex patterns.
    Args:
        text (str): The input text to be anonymized.
    Returns:
        str: The anonymized text.
    """
    # Replace sensitive information with placeholders
    text = SSN_PATTERN.sub('[REDACTED SSN]', text)
    text = CREDIT_CARD_PATTERN.sub('[REDACTED CREDIT CARD]', text)
    text = EMAIL_PATTERN.sub('[REDACTED EMAIL]', text)
    text = PHONE_PATTERN.sub('[REDACTED PHONE]', text)
    text = FULL_NAME_PATTERN.sub('[REDACTED NAME]', text)
    return text

def recursive_anonymize(data, depth=10):
    """
    Recursively traverse the data structure and anonymize sensitive information.
    Args:
        data (any): The input data to be anonymized.
        depth (int): The current recursion depth to prevent excessive recursion.
    Returns:
        any: The anonymized data.
    """
    if depth == 0:
        return data
    if isinstance(data, dict):
        anonymized_dict = {}
        for k, v in data.items():
            anonymized_value = recursive_anonymize(v, depth - 1)
            anonymized_dict[k] = anonymized_value
        return anonymized_dict
    elif isinstance(data, list):
        anonymized_list = []
        for item in data:
            anonymized_item = recursive_anonymize(item, depth - 1)
            anonymized_list.append(anonymized_item)
        return anonymized_list
    elif isinstance(data, str):
        anonymized_data = regex_anonymize(data)
        return anonymized_data
    else:
        return data

openai_client = wrap_openai(openai.Client())

# Initialize the LangSmith @[Client] with the anonymization functions
langsmith_client = Client(
    hide_inputs=recursive_anonymize, hide_outputs=recursive_anonymize
)

# The trace produced will have its metadata present, but the inputs and outputs will be anonymized
response_with_anonymization = openai_client.chat.completions.create(
    model="gpt-5.4-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "My name is John Doe, my SSN is 123-45-6789, my credit card number is 4111 1111 1111 1111, my email is john.doe@example.com, and my phone number is (123) 456-7890."},
    ],
    langsmith_extra={"client": langsmith_client},
)

# The trace produced will not have anonymized inputs and outputs
response_without_anonymization = openai_client.chat.completions.create(
    model="gpt-5.4-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "My name is John Doe, my SSN is 123-45-6789, my credit card number is 4111 1111 1111 1111, my email is john.doe@example.com, and my phone number is (123) 456-7890."},
    ],
)
```

The anonymized run will look like this in LangSmith: <img alt="Anonymized run" />

The non-anonymized run will look like this in LangSmith: <img alt="Non-anonymized run" />

### Microsoft Presidio

<Info>
  The implementation below provides a general example of how to anonymize sensitive information in messages exchanged between a user and an LLM. It is not exhaustive and does not account for all cases. Test any implementation thoroughly before using it in production.
</Info>

Microsoft Presidio is a data protection and de-identification SDK. The implementation below uses Presidio to anonymize inputs and outputs before they are sent to LangSmith. For up to date information, please refer to Presidio's [official documentation](https://microsoft.github.io/presidio/).

To use Presidio and its spaCy model, install the following:

<CodeGroup>
  ```bash pip theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  pip install presidio-analyzer
  pip install presidio-anonymizer
  python -m spacy download en_core_web_lg
  ```

  ```bash uv theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  uv add presidio-analyzer
  uv add presidio-anonymizer
  python -m spacy download en_core_web_lg
  ```
</CodeGroup>

Also, install OpenAI:

<CodeGroup>
  ```bash pip theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  pip install openai
  ```

  ```bash uv theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  uv add openai
  ```
</CodeGroup>

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import openai
from langsmith import Client
from langsmith.wrappers import wrap_openai
from presidio_anonymizer import AnonymizerEngine
from presidio_analyzer import AnalyzerEngine

anonymizer = AnonymizerEngine()
analyzer = AnalyzerEngine()

def presidio_anonymize(data):
    """
    Anonymize sensitive information sent by the user or returned by the model.
    Args:
        data (any): The data to be anonymized.
    Returns:
        any: The anonymized data.
    """
    message_list = (
        data.get('messages') or [data.get('choices', [{}])[0].get('message')]
    )
    if not message_list or not all(isinstance(msg, dict) and msg for msg in message_list):
        return data

    for message in message_list:
        content = message.get('content', '')
        if not content.strip():
            print("Empty content detected. Skipping anonymization.")
            continue

        results = analyzer.analyze(
            text=content,
            entities=["PERSON", "PHONE_NUMBER", "EMAIL_ADDRESS", "US_SSN"],
            language='en'
        )
        anonymized_result = anonymizer.anonymize(
            text=content,
            analyzer_results=results
        )
        message['content'] = anonymized_result.text

    return data

openai_client = wrap_openai(openai.Client())

# initialize the langsmith @[Client] with the anonymization functions
langsmith_client = Client(
  hide_inputs=presidio_anonymize, hide_outputs=presidio_anonymize
)

# The trace produced will have its metadata present, but the inputs and outputs will be anonymized
response_with_anonymization = openai_client.chat.completions.create(
  model="gpt-5.4-mini",
  messages=[
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": "My name is Slim Shady, call me at 313-666-7440 or email me at real.slim.shady@gmail.com"},
  ],
  langsmith_extra={"client": langsmith_client},
)

# The trace produced will not have anonymized inputs and outputs
response_without_anonymization = openai_client.chat.completions.create(
  model="gpt-5.4-mini",
  messages=[
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": "My name is Slim Shady, call me at 313-666-7440 or email me at real.slim.shady@gmail.com"},
  ],
)
```

The anonymized run will look like this in LangSmith: <img alt="Anonymized run" />

The non-anonymized run will look like this in LangSmith: <img alt="Non-anonymized run" />

### Amazon Comprehend

<Info>
  The implementation below provides a general example of how to anonymize sensitive information in messages exchanged between a user and an LLM. It is not exhaustive and does not account for all cases. Test any implementation thoroughly before using it in production.
</Info>

Comprehend is a natural language processing service that can detect personally identifiable information. The implementation below uses Comprehend to anonymize inputs and outputs before they are sent to LangSmith. For up to date information, please refer to Comprehend's [official documentation](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_DetectPiiEntities.html).

To use Comprehend, install [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html):

<CodeGroup>
  ```bash pip theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  pip install boto3
  ```

  ```bash uv theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  uv add boto3
  ```
</CodeGroup>

Also, install OpenAI:

<CodeGroup>
  ```bash pip theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  pip install openai
  ```

  ```bash uv theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  uv add openai
  ```
</CodeGroup>

You will need to set up credentials in AWS and authenticate using the AWS CLI. Follow the [AWS Comprehend setup instructions](https://docs.aws.amazon.com/comprehend/latest/dg/setting-up.html).

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import openai
import boto3
from langsmith import Client
from langsmith.wrappers import wrap_openai

comprehend = boto3.client('comprehend', region_name='us-east-1')

def redact_pii_entities(text, entities):
    """
    Redact PII entities in the text based on the detected entities.
    Args:
        text (str): The original text containing PII.
        entities (list): A list of detected PII entities.
    Returns:
        str: The text with PII entities redacted.
    """
    sorted_entities = sorted(entities, key=lambda x: x['BeginOffset'], reverse=True)
    redacted_text = text
    for entity in sorted_entities:
        begin = entity['BeginOffset']
        end = entity['EndOffset']
        entity_type = entity['Type']
        # Define the redaction placeholder based on entity type
        placeholder = f"[{entity_type}]"
        # Replace the PII in the text with the placeholder
        redacted_text = redacted_text[:begin] + placeholder + redacted_text[end:]
    return redacted_text

def detect_pii(text):
    """
    Detect PII entities in the given text using AWS Comprehend.
    Args:
        text (str): The text to analyze.
    Returns:
        list: A list of detected PII entities.
    """
    try:
        response = comprehend.detect_pii_entities(
            Text=text,
            LanguageCode='en',
        )
        entities = response.get('Entities', [])
        return entities
    except Exception as e:
        print(f"Error detecting PII: {e}")
        return []

def comprehend_anonymize(data):
    """
    Anonymize sensitive information sent by the user or returned by the model.
    Args:
        data (any): The input data to be anonymized.
    Returns:
        any: The anonymized data.
    """
    message_list = (
        data.get('messages') or [data.get('choices', [{}])[0].get('message')]
    )
    if not message_list or not all(isinstance(msg, dict) and msg for msg in message_list):
        return data

    for message in message_list:
        content = message.get('content', '')
        if not content.strip():
            print("Empty content detected. Skipping anonymization.")
            continue

        entities = detect_pii(content)
        if entities:
            anonymized_text = redact_pii_entities(content, entities)
            message['content'] = anonymized_text
        else:
            print("No PII detected. Content remains unchanged.")

    return data

openai_client = wrap_openai(openai.Client())

# initialize the langsmith @[Client] with the anonymization functions
langsmith_client = Client(
  hide_inputs=comprehend_anonymize, hide_outputs=comprehend_anonymize
)

# The trace produced will have its metadata present, but the inputs and outputs will be anonymized
response_with_anonymization = openai_client.chat.completions.create(
  model="gpt-5.4-mini",
  messages=[
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": "My name is Slim Shady, call me at 313-666-7440 or email me at real.slim.shady@gmail.com"},
  ],
  langsmith_extra={"client": langsmith_client},
)
