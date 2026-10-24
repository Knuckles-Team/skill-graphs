# Tool calling
Source: https://docs.langchain.com/oss/python/langchain/frontend/tool-calling

Display agent tool calls with rich, type-safe UI cards

Agents can invoke external tools like weather APIs, calculators, web search,
database queries, and more. The results are in raw JSON. This pattern shows you
how to render
structured, type-safe UI cards for every tool call your agent makes, complete
with loading states and error handling.

<PatternEmbed />

## How tool calling works

When a LangGraph agent decides it needs external data, it emits one or more
**tool calls** as part of an AI message. Each tool call includes:

* **name**: the tool being invoked (e.g. `"get_weather"`, `"calculator"`)
* **args**: the structured arguments passed to the tool
* **id**: a unique identifier linking the call to its result

The agent runtime executes the tool, and the result comes back as a
`ToolMessage`. The [`useStream`](https://reference.langchain.com/javascript/langchain-react/index/useStream) hook unifies all of this into a single
`toolCalls` array you can render directly.

## Setting up `useStream`

The first step is wiring up [`useStream`](https://reference.langchain.com/javascript/langchain-react/index/useStream) to your agent backend. The hook returns
reactive state including a `toolCalls` array that updates in real time as the
agent streams.

<Info>
  The code examples use `useStream<typeof myAgent>` for type-safe stream state. See Type inference for [Python](/oss/python/langchain/frontend/overview#type-inference) or [JavaScript](/oss/javascript/langchain/frontend/overview#type-inference) backends.
</Info>

<CodeGroup>
  ```tsx React theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { useStream } from "@langchain/react";

  const AGENT_URL = "http://localhost:2024";

  export function Chat() {
    const stream = useStream<typeof myAgent>({
      apiUrl: AGENT_URL,
      assistantId: "tool_calling",
    });

    return (
      <div>
        {stream.messages.map((msg) => (
          <Message key={msg.id} message={msg} toolCalls={stream.toolCalls} />
        ))}
      </div>
    );
  }
  ```

  ```vue Vue theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  <script setup lang="ts">
  import { useStream } from "@langchain/vue";

  const AGENT_URL = "http://localhost:2024";

  const stream = useStream<typeof myAgent>({
    apiUrl: AGENT_URL,
    assistantId: "tool_calling",
  });
  </script>

  <template>
    <div>
      <Message
        v-for="msg in stream.messages.value"
        :key="msg.id"
        :message="msg"
        :tool-calls="stream.toolCalls.value"
      />
    </div>
  </template>
  ```

  ```svelte Svelte theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  <script lang="ts">
    import { useStream } from "@langchain/svelte";

    const AGENT_URL = "http://localhost:2024";

    const stream = useStream<typeof myAgent>({
      apiUrl: AGENT_URL,
      assistantId: "tool_calling",
    });
  </script>

  <div>
    {#each stream.messages as msg (msg.id)}
      <Message message={msg} toolCalls={stream.toolCalls} />
    {/each}
  </div>
  ```

  ```ts Angular theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { Component } from "@angular/core";
  import { injectStream } from "@langchain/angular";

  const AGENT_URL = "http://localhost:2024";

  @Component({
    selector: "app-chat",
    template: `
      @for (msg of stream.messages(); track msg.id) {
        <app-message [message]="msg" [toolCalls]="stream.toolCalls()" />
      }
    `,
  })
  export class ChatComponent {
    stream = injectStream<typeof myAgent>({
      apiUrl: AGENT_URL,
      assistantId: "tool_calling",
    });
  }
  ```
</CodeGroup>

## The AssembledToolCall type

Each entry in the `toolCalls` array is an `AssembledToolCall` object:

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
interface AssembledToolCall<
  TName extends string = string,
  TInput = unknown,
  TOutput = unknown,
> {
  name: TName;
  callId: string;
  id: string;
  namespace: string[];
  input: TInput;
  args: TInput;
  output: TOutput | null;
  status: "running" | "finished" | "error";
  error: string | undefined;
}
```

| Property    | Description                                                                    |
| ----------- | ------------------------------------------------------------------------------ |
| `name`      | The name of the tool (e.g. `"get_weather"`)                                    |
| `callId`    | Unique ID matching the AI message's `tool_calls` entry                         |
| `id`        | Alias for `callId`, matching message-level tool calls                          |
| `namespace` | Namespace where the tool call was emitted                                      |
| `input`     | Structured arguments the agent passed to the tool                              |
| `args`      | Alias for `input`, matching message-level tool calls                           |
| `output`    | Tool output after a successful call, or `null` while running or after an error |
| `status`    | Lifecycle state: `"running"`, `"finished"`, or `"error"`                       |
| `error`     | Error details when the tool call fails                                         |

## Filtering tool calls per message

An AI message may trigger multiple tool calls, and your chat may contain many AI
messages. To render the right tool cards under each message, filter by matching
`callId` against the message's `tool_calls` array:

```tsx theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
function Message({
  message,
  toolCalls,
}: {
  message: AIMessage;
  toolCalls: AssembledToolCall[];
}) {
  const messageToolCalls = toolCalls.filter((tc) =>
    message.tool_calls?.find((t) => t.id === tc.callId)
  );

  return (
    <div>
      <p>{message.text}</p>
      {messageToolCalls.map((tc) => (
        <ToolCard key={tc.callId} toolCall={tc} />
      ))}
    </div>
  );
}
```

## Building specialized tool cards

Rather than dumping raw JSON, build dedicated UI components for each tool. Use
`name` to select the right card:

```tsx theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
function ToolCard({ toolCall }: { toolCall: AssembledToolCall }) {
  if (toolCall.status === "running") {
    return <LoadingCard name={toolCall.name} />;
  }

  if (toolCall.status === "error") {
    return <ErrorCard name={toolCall.name} error={toolCall.error} />;
  }

  switch (toolCall.name) {
    case "get_weather":
      return <WeatherCard input={toolCall.input} output={toolCall.output} />;
    case "calculator":
      return (
        <CalculatorCard input={toolCall.input} output={toolCall.output} />
      );
    case "web_search":
      return <SearchCard input={toolCall.input} output={toolCall.output} />;
    default:
      return <GenericToolCard toolCall={toolCall} />;
  }
}
```

### Weather card example

```tsx theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
function WeatherCard({
  input,
  output,
}: {
  input: { location: string };
  output: { temperature: number; condition: string };
}) {
  return (
    <div className="rounded-lg border p-4">
      <div className="flex items-center gap-2">
        <CloudIcon />
        <h3 className="font-semibold">{input.location}</h3>
      </div>
      <div className="mt-2 text-3xl font-bold">{output.temperature}°F</div>
      <p className="text-muted-foreground">{output.condition}</p>
    </div>
  );
}
```

### Loading and error states

Always handle the pending and error states to give users clear feedback:

```tsx theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
function LoadingCard({ name }: { name: string }) {
  return (
    <div className="flex items-center gap-2 rounded-lg border p-4 animate-pulse">
      <Spinner />
      <span>Running {name}...</span>
    </div>
  );
}

function ErrorCard({ name, error }: { name: string; error?: unknown }) {
  return (
    <div className="rounded-lg border border-red-300 bg-red-50 p-4">
      <h3 className="font-semibold text-red-700">Error in {name}</h3>
      <p className="text-sm text-red-600">
        {String(error ?? "Tool execution failed")}
      </p>
    </div>
  );
}
```

## Type-safe tool arguments

If your tools are defined with structured schemas, you can use the
`ToolCallFromTool` utility type to get fully typed `args`:

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { tool } from "@langchain/core/tools";
import { z } from "zod";

const getWeather = tool(async ({ location }) => { /* ... */ }, {
  name: "get_weather",
  description: "Get the current weather for a location",
  schema: z.object({
    location: z.string().describe("City name"),
  }),
});

type WeatherToolCall = ToolCallFromTool<typeof getWeather>;
// WeatherToolCall.input and WeatherToolCall.args are now { location: string }
```

<Tip>
  Using `ToolCallFromTool` gives you compile-time safety. If the tool schema
  changes, your UI components will flag type errors immediately.
</Tip>

## Rendering tool calls inline with streaming text

Tool calls often arrive interleaved with streamed text. The [`useStream`](https://reference.langchain.com/javascript/langchain-react/index/useStream) hook
keeps `toolCalls` in sync with the stream, so pending cards appear as soon as
the agent emits the call, before the tool has finished executing.

This means users see:

1. The AI's text as it streams in
2. A loading card the moment a tool call is emitted
3. The card updates to show the result once the tool completes

<Note>
  Tool calls update in place. The same `callId` transitions from `"running"` to
  `"finished"` (or `"error"`), so your UI re-renders the same component
  with new state.
</Note>

## Handling multiple concurrent tool calls

Agents can invoke several tools in parallel. The `toolCalls` array will contain
multiple entries with `status: "running"` simultaneously. Each resolves
independently, so your UI should handle partial completion gracefully:

```tsx theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
function ToolCallList({ toolCalls }: { toolCalls: AssembledToolCall[] }) {
  const pending = toolCalls.filter((tc) => tc.status === "running");
  const completed = toolCalls.filter((tc) => tc.status === "finished");

  return (
    <div className="space-y-2">
      {completed.map((tc) => (
        <ToolCard key={tc.callId} toolCall={tc} />
      ))}
      {pending.map((tc) => (
        <LoadingCard key={tc.callId} name={tc.name} />
      ))}
    </div>
  );
}
```

## Best practices

Follow these guidelines when building tool call UIs:

* **Always handle all three states**: `running`, `finished`, and `error`.
  Users should never see a blank card.
* **Validate results safely**. Tool outputs are typed as `unknown` until you
  narrow them for a specific card.
* **Provide a generic fallback**. Not every tool needs a bespoke card. Render
  a collapsible JSON view for unknown tool names.
* **Show the tool name and args during loading**. Users want to know *what*
  the agent is doing, even before the result arrives.
* **Keep cards compact**. Tool cards sit inline with chat messages. Avoid
  overwhelming the conversation with oversized widgets.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langchain/frontend/tool-calling.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Get help
Source: https://docs.langchain.com/oss/python/langchain/get-help

Connect with the LangChain community, access learning resources, and get the support you need to build with confidence.

## Learning resources

Start your journey or deepen your knowledge with our comprehensive learning materials.

* **[Chat LangChain](https://chat.langchain.com/)**: Ask the docs anything about LangChain, powered by real-time docs
* **[API Reference](https://reference.langchain.com/python/)**: Complete documentation for all LangChain packages

## Community support

Get help from fellow developers and the LangChain team through our active community channels.

* **[Community Forum](https://forum.langchain.com/)**: Ask questions, share solutions, and discuss best practices
* **[Community Slack](https://www.langchain.com/join-community)**: Connect with other builders and get quick help

## Professional support

For enterprise needs and critical applications, access dedicated support channels.

* **[Support portal](https://support.langchain.com/)**: Submit tickets and track support requests
* **[LangSmith status](https://status.smith.langchain.com/)**: Real-time status of LangSmith services and APIs

## Contribute

Help us improve LangChain for everyone. Whether you're fixing bugs, adding features, or improving documentation, we welcome your contributions.

* **[Contributing Guide](/oss/python/contributing/overview)**: Everything you need to know about contributing to LangChain

## Stay connected

Follow us for the latest updates, announcements, and community highlights.

* **[X (Twitter)](https://x.com/langchain)**: Daily updates and community spotlights
* **[LinkedIn](https://www.linkedin.com/company/langchain/)**: Professional network and company updates

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langchain/get-help.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Guardrails
Source: https://docs.langchain.com/oss/python/langchain/guardrails

Implement safety checks and content filtering for your agents

Guardrails help you build safe, compliant AI applications by validating and filtering content at key points in your agent's execution. They can detect sensitive information, enforce content policies, validate outputs, and prevent unsafe behaviors before they cause problems.

Common use cases include:

* Preventing PII leakage
* Detecting and blocking prompt injection attacks
* Blocking inappropriate or harmful content
* Enforcing business rules and compliance requirements
* Validating output quality and accuracy

You can implement guardrails using [middleware](/oss/python/langchain/middleware) to intercept execution at strategic points - before the agent starts, after it completes, or around model and tool calls.

<div>
  <img alt="Middleware flow diagram" />
</div>

Guardrails can be implemented using two complementary approaches:

<CardGroup>
  <Card title="Deterministic guardrails" icon="list-check">
    Use rule-based logic like regex patterns, keyword matching, or explicit checks. Fast, predictable, and cost-effective, but may miss nuanced violations.
  </Card>

  <Card title="Model-based guardrails" icon="brain">
    Use LLMs or classifiers to evaluate content with semantic understanding. Catch subtle issues that rules miss, but are slower and more expensive.
  </Card>
</CardGroup>

LangChain provides both built-in guardrails (e.g., [PII detection](#pii-detection), [human-in-the-loop](#human-in-the-loop)) and a flexible middleware system for building custom guardrails using either approach.

## Built-in guardrails

### PII detection

LangChain provides built-in middleware for detecting and handling Personally Identifiable Information (PII) in conversations. This middleware can detect common PII types like emails, credit cards, IP addresses, and more.

PII detection middleware is helpful for cases such as health care and financial applications with compliance requirements, customer service agents that need to sanitize logs, and generally any application handling sensitive user data.

The PII middleware supports multiple strategies for handling detected PII:

| Strategy | Description                             | Example               |
| -------- | --------------------------------------- | --------------------- |
| `redact` | Replace with `[REDACTED_{PII_TYPE}]`    | `[REDACTED_EMAIL]`    |
| `mask`   | Partially obscure (e.g., last 4 digits) | `****-****-****-1234` |
| `hash`   | Replace with deterministic hash         | `a8f5f167...`         |
| `block`  | Raise exception when detected           | Error thrown          |

<Note>
  With `apply_to_output=True`, `PIIMiddleware` also redacts streamed wire output—text deltas, tool-call args, tool outputs, and state snapshots—via a registered stream transformer. Requires `langchain>=1.3.2`. See [Register transformers on middleware](/oss/python/langchain/event-streaming#register-transformers-on-middleware).
</Note>

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain.agents import create_agent
from langchain.agents.middleware import PIIMiddleware

agent = create_agent(
    model="gpt-5.5",
    tools=[customer_service_tool, email_tool],
    middleware=[
        # Redact emails in user input before sending to model
        PIIMiddleware(
            "email",
            strategy="redact",
            apply_to_input=True,
        ),
        # Mask credit cards in user input
        PIIMiddleware(
            "credit_card",
            strategy="mask",
            apply_to_input=True,
        ),
        # Block API keys - raise error if detected
        PIIMiddleware(
            "api_key",
            detector=r"sk-[a-zA-Z0-9]{32}",
            strategy="block",
            apply_to_input=True,
        ),
    ],
)

# When user provides PII, it will be handled according to the strategy
result = agent.invoke({
    "messages": [{"role": "user", "content": "My email is john.doe@example.com and card is 5105-1051-0510-5100"}]
})
```

<Accordion title="Built-in PII types and configuration">
  **Built-in PII types:**

  * `email` - Email addresses
  * `credit_card` - Credit card numbers (Luhn validated)
  * `ip` - IP addresses
  * `mac_address` - MAC addresses
  * `url` - URLs

  **Configuration options:**

  | Parameter               | Description                                                            | Default                |
  | ----------------------- | ---------------------------------------------------------------------- | ---------------------- |
  | `pii_type`              | Type of PII to detect (built-in or custom)                             | Required               |
  | `strategy`              | How to handle detected PII (`"block"`, `"redact"`, `"mask"`, `"hash"`) | `"redact"`             |
  | `detector`              | Custom detector function or regex pattern                              | `None` (uses built-in) |
  | `apply_to_input`        | Check user messages before model call                                  | `True`                 |
  | `apply_to_output`       | Check AI messages after model call                                     | `False`                |
  | `apply_to_tool_results` | Check tool result messages after execution                             | `False`                |
</Accordion>

See the [middleware documentation](/oss/python/langchain/middleware#pii-detection) for complete details on PII detection capabilities.

### Human-in-the-loop

LangChain provides built-in middleware for requiring human approval before executing sensitive operations. This is one of the most effective guardrails for high-stakes decisions.

Human-in-the-loop middleware is helpful for cases such as financial transactions and transfers, deleting or modifying production data, sending communications to external parties, and any operation with significant business impact.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain.agents import create_agent
from langchain.agents.middleware import HumanInTheLoopMiddleware
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.types import Command

agent = create_agent(
    model="gpt-5.5",
    tools=[search_tool, send_email_tool, delete_database_tool],
    middleware=[
        HumanInTheLoopMiddleware(
            interrupt_on={
                # Require approval for sensitive operations
                "send_email": True,
                "delete_database": True,
                # Auto-approve safe operations
                "search": False,
            }
        ),
    ],
    # Persist the state across interrupts
    checkpointer=InMemorySaver(),
)

# Human-in-the-loop requires a thread ID for persistence
config = {"configurable": {"thread_id": "some_id"}}

# Agent will pause and wait for approval before executing sensitive tools
result = agent.invoke(
    {"messages": [{"role": "user", "content": "Send an email to the team"}]},
    config=config
)

result = agent.invoke(
    Command(resume={"decisions": [{"type": "approve"}]}),
    config=config  # Same thread ID to resume the paused conversation
)
```

<Tip>
  See the [human-in-the-loop documentation](/oss/python/langchain/human-in-the-loop) for complete details on implementing approval workflows.
</Tip>

## Custom guardrails

For more sophisticated guardrails, you can create custom middleware that runs before or after the agent executes. This gives you full control over validation logic, content filtering, and safety checks.

### Before agent guardrails

Use "before agent" hooks to validate requests once at the start of each invocation. This is useful for session-level checks like authentication, rate limiting, or blocking inappropriate requests before any processing begins.

<CodeGroup>
  ```python title="Class syntax" theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from typing import Any

  from langchain.agents.middleware import AgentMiddleware, AgentState, hook_config
  from langgraph.runtime import Runtime

  class ContentFilterMiddleware(AgentMiddleware):
      """Deterministic guardrail: Block requests containing banned keywords."""

      def __init__(self, banned_keywords: list[str]):
          super().__init__()
          self.banned_keywords = [kw.lower() for kw in banned_keywords]

      @hook_config(can_jump_to=["end"])
      def before_agent(self, state: AgentState, runtime: Runtime) -> dict[str, Any] | None:
          # Get the first user message
          if not state["messages"]:
              return None

          first_message = state["messages"][0]
          if first_message.type != "human":
              return None

          content = first_message.content.lower()

          # Check for banned keywords
          for keyword in self.banned_keywords:
              if keyword in content:
                  # Block execution before any processing
                  return {
                      "messages": [{
                          "role": "assistant",
                          "content": "I cannot process requests containing inappropriate content. Please rephrase your request."
                      }],
                      "jump_to": "end"
                  }

          return None

  # Use the custom guardrail
  from langchain.agents import create_agent

  agent = create_agent(
      model="gpt-5.5",
      tools=[search_tool, calculator_tool],
      middleware=[
          ContentFilterMiddleware(
              banned_keywords=["hack", "exploit", "malware"]
          ),
      ],
  )

  # This request will be blocked before any processing
  result = agent.invoke({
      "messages": [{"role": "user", "content": "How do I hack into a database?"}]
  })
  ```

  ```python title="Decorator syntax" theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from typing import Any

  from langchain.agents.middleware import before_agent, AgentState, hook_config
  from langgraph.runtime import Runtime

  banned_keywords = ["hack", "exploit", "malware"]

  @before_agent(can_jump_to=["end"])
  def content_filter(state: AgentState, runtime: Runtime) -> dict[str, Any] | None:
      """Deterministic guardrail: Block requests containing banned keywords."""
      # Get the first user message
      if not state["messages"]:
          return None

      first_message = state["messages"][0]
      if first_message.type != "human":
          return None

      content = first_message.content.lower()

      # Check for banned keywords
      for keyword in banned_keywords:
          if keyword in content:
              # Block execution before any processing
              return {
                  "messages": [{
                      "role": "assistant",
                      "content": "I cannot process requests containing inappropriate content. Please rephrase your request."
                  }],
                  "jump_to": "end"
              }

      return None

  # Use the custom guardrail
  from langchain.agents import create_agent

  agent = create_agent(
      model="gpt-5.5",
      tools=[search_tool, calculator_tool],
      middleware=[content_filter],
  )

  # This request will be blocked before any processing
  result = agent.invoke({
      "messages": [{"role": "user", "content": "How do I hack into a database?"}]
  })
  ```
</CodeGroup>

### After agent guardrails

Use "after agent" hooks to validate final outputs once before returning to the user. This is useful for model-based safety checks, quality validation, or final compliance scans on the complete agent response.

<CodeGroup>
  ```python title="Class syntax" theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langchain.agents.middleware import AgentMiddleware, AgentState, hook_config
  from langgraph.runtime import Runtime
  from langchain.messages import AIMessage
  from langchain.chat_models import init_chat_model
  from typing import Any

  class SafetyGuardrailMiddleware(AgentMiddleware):
      """Model-based guardrail: Use an LLM to evaluate response safety."""

      def __init__(self):
          super().__init__()
          self.safety_model = init_chat_model("gpt-5.4-mini")

      @hook_config(can_jump_to=["end"])
      def after_agent(self, state: AgentState, runtime: Runtime) -> dict[str, Any] | None:
          # Get the final AI response
          if not state["messages"]:
              return None

          last_message = state["messages"][-1]
          if not isinstance(last_message, AIMessage):
              return None

          # Use a model to evaluate safety
          safety_prompt = f"""Evaluate if this response is safe and appropriate.
          Respond with only 'SAFE' or 'UNSAFE'.

          Response: {last_message.content}"""

          result = self.safety_model.invoke([{"role": "user", "content": safety_prompt}])

          if "UNSAFE" in result.content:
              last_message.content = "I cannot provide that response. Please rephrase your request."

          return None

  # Use the safety guardrail
  from langchain.agents import create_agent

  agent = create_agent(
      model="gpt-5.5",
      tools=[search_tool, calculator_tool],
      middleware=[SafetyGuardrailMiddleware()],
  )

  result = agent.invoke({
      "messages": [{"role": "user", "content": "How do I make explosives?"}]
  })
  ```

  ```python title="Decorator syntax" theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langchain.agents.middleware import after_agent, AgentState, hook_config
  from langgraph.runtime import Runtime
  from langchain.messages import AIMessage
  from langchain.chat_models import init_chat_model
  from typing import Any

  safety_model = init_chat_model("gpt-5.4-mini")

  @after_agent(can_jump_to=["end"])
  def safety_guardrail(state: AgentState, runtime: Runtime) -> dict[str, Any] | None:
      """Model-based guardrail: Use an LLM to evaluate response safety."""
      # Get the final AI response
      if not state["messages"]:
          return None

      last_message = state["messages"][-1]
      if not isinstance(last_message, AIMessage):
          return None

      # Use a model to evaluate safety
      safety_prompt = f"""Evaluate if this response is safe and appropriate.
      Respond with only 'SAFE' or 'UNSAFE'.

      Response: {last_message.content}"""

      result = safety_model.invoke([{"role": "user", "content": safety_prompt}])

      if "UNSAFE" in result.content:
          last_message.content = "I cannot provide that response. Please rephrase your request."

      return None

  # Use the safety guardrail
  from langchain.agents import create_agent

  agent = create_agent(
      model="gpt-5.5",
      tools=[search_tool, calculator_tool],
      middleware=[safety_guardrail],
  )

  result = agent.invoke({
      "messages": [{"role": "user", "content": "How do I make explosives?"}]
  })
  ```
</CodeGroup>

### Combine multiple guardrails

You can stack multiple guardrails by adding them to the middleware array. They execute in order, allowing you to build layered protection:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain.agents import create_agent
from langchain.agents.middleware import PIIMiddleware, HumanInTheLoopMiddleware

agent = create_agent(
    model="gpt-5.5",
    tools=[search_tool, send_email_tool],
    middleware=[
        # Layer 1: Deterministic input filter (before agent)
        ContentFilterMiddleware(banned_keywords=["hack", "exploit"]),

        # Layer 2: PII protection (before and after model)
        PIIMiddleware("email", strategy="redact", apply_to_input=True),
        PIIMiddleware("email", strategy="redact", apply_to_output=True),

        # Layer 3: Human approval for sensitive tools
        HumanInTheLoopMiddleware(interrupt_on={"send_email": True}),

        # Layer 4: Model-based safety check (after agent)
        SafetyGuardrailMiddleware(),
    ],
)
```

## Additional resources

* [Middleware documentation](/oss/python/langchain/middleware) - Complete guide to custom middleware
* [Middleware API reference](https://reference.langchain.com/python/langchain/middleware/) - Complete guide to custom middleware
* [Human-in-the-loop](/oss/python/langchain/human-in-the-loop) - Add human review for sensitive operations
* [Testing agents](/oss/python/langchain/test/) - Strategies for testing safety mechanisms

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langchain/guardrails.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Human-in-the-loop
Source: https://docs.langchain.com/oss/python/langchain/human-in-the-loop

The Human-in-the-Loop (HITL) [middleware](/oss/python/langchain/middleware/built-in#human-in-the-loop) lets you add human oversight to agent tool calls.
When a model proposes an action that might require review—for example, writing to a file or executing SQL—the middleware can pause execution and wait for a decision.

It does this by checking each tool call against a configurable policy. If intervention is needed, the middleware issues an [interrupt](https://reference.langchain.com/python/langgraph/types/interrupt) that halts execution. The graph state is saved using LangGraph's [persistence layer](/oss/python/langgraph/persistence), so execution can pause safely and resume later.

A human decision then determines what happens next: the action can be approved as-is (`approve`), modified before running (`edit`), rejected with feedback (`reject`), or responded to directly (`respond`) for "ask user" style tools.

## Interrupt decision types

The [middleware](/oss/python/langchain/middleware/built-in#human-in-the-loop) defines four built-in ways a human can respond to an interrupt:

| Decision Type | Description                                                               | Example Use Case                                 |
| ------------- | ------------------------------------------------------------------------- | ------------------------------------------------ |
| ✅ `approve`   | The action is approved as-is and executed without changes.                | Send an email draft exactly as written           |
| ✏️ `edit`     | The tool call is executed with modifications.                             | Change the recipient before sending an email     |
| ❌ `reject`    | The tool call is rejected, with an explanation added to the conversation. | Deny file deletion and explain why               |
| 💬 `respond`  | Tool execution is skipped; the human's message becomes the tool result.   | Answer an "ask\_user" prompt with a direct reply |

The available decision types for each tool depend on the policy you configure in `interrupt_on`.
When multiple tool calls are paused at the same time, each action requires a separate decision.
Decisions must be provided in the same order as the actions appear in the interrupt request.

Use `reject` when the human is denying the requested action. Use `respond` only when the human is acting as the tool, such as answering an `ask_user` prompt. Do not use `respond` to deny side-effecting tools, because its message is treated as a successful tool result.

<Tip>
  When **editing** tool arguments, make changes conservatively. Significant modifications to the original arguments may cause the model to re-evaluate its approach and potentially execute the tool multiple times or take unexpected actions.
</Tip>

## Configuring interrupts

To use HITL, add the [middleware](/oss/python/langchain/middleware/built-in#human-in-the-loop) to the agent's `middleware` list when creating the agent.

You configure it with a mapping of tool actions to the decision types that are allowed for each action. The middleware will interrupt execution when a tool call matches an action in the mapping.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain.agents import create_agent
from langchain.agents.middleware import HumanInTheLoopMiddleware # [!code highlight]
from langgraph.checkpoint.memory import InMemorySaver # [!code highlight]

agent = create_agent(
    model="gpt-5.5",
    tools=[write_file, execute_sql, read_data],
    middleware=[
        HumanInTheLoopMiddleware( # [!code highlight]
            interrupt_on={
                "write_file": True,  # All decisions (approve, edit, reject, respond) allowed
                "execute_sql": {"allowed_decisions": ["approve", "reject"]},  # No editing allowed
                "read_data": False, # Safe operation, no approval needed
            },
            # Prefix for interrupt messages - combined with tool name and args to form the full message
            # e.g., "Tool execution pending approval: execute_sql with query='DELETE FROM...'"
            # Individual tools can override this by specifying a "description" in their interrupt config
            description_prefix="Tool execution pending approval",
        ),
    ],
    # Human-in-the-loop requires checkpointing to handle interrupts.
    # In production, use a persistent checkpointer like AsyncPostgresSaver.
    checkpointer=InMemorySaver(),  # [!code highlight]
)
```

<Info>
  You must configure a checkpointer to persist the graph state across interrupts.
  In production, use a persistent checkpointer like [`AsyncPostgresSaver`](https://reference.langchain.com/python/langgraph/checkpoints/#langgraph.checkpoint.postgres.aio.AsyncPostgresSaver). For testing or prototyping, use [`InMemorySaver`](https://reference.langchain.com/python/langgraph/checkpoints/#langgraph.checkpoint.memory.InMemorySaver).

  When invoking the agent, pass a `config` that includes the **thread ID** to associate execution with a conversation thread.
  See the [LangGraph interrupts documentation](/oss/python/langgraph/interrupts) for details.
</Info>

<Accordion title="Configuration options">
  <ParamField type="dict">
    Mapping of tool names to approval configs. Values can be `True` (interrupt with default config), `False` (auto-approve), or an `InterruptOnConfig` object.
  </ParamField>

  <ParamField type="string">
    Prefix for action request descriptions
  </ParamField>

  **`InterruptOnConfig` options:**

  <ParamField type="list[string]">
    List of allowed decisions: `'approve'`, `'edit'`, `'reject'`, or `'respond'`
  </ParamField>

  <ParamField type="string | callable">
    Static string or callable function for custom description
  </ParamField>

  <ParamField type="callable">
    Optional predicate that receives a [ToolCallRequest](https://reference.langchain.com/python/langgraph.prebuilt/tool_node/ToolCallRequest) and returns `True` to interrupt or `False` to auto-approve. Use it to gate interrupts on a call's arguments. Requires `langchain>=1.3.3`.
  </ParamField>
</Accordion>

## Conditional interrupts

By default, every tool call listed in `interrupt_on` pauses for review. To pause only some calls, add a `when` predicate to a tool's `InterruptOnConfig`. The predicate receives a `ToolCallRequest` and returns `True` to interrupt or `False` to auto-approve, so you can gate on the tool's arguments.

<Note>
  Conditional interrupts require `langchain>=1.3.3`.
</Note>

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain.agents import create_agent
from langchain.agents.middleware import HumanInTheLoopMiddleware, ToolCallRequest
from langgraph.checkpoint.memory import InMemorySaver

def writes_outside_workspace(request: ToolCallRequest) -> bool:
    """Pause writes to paths outside the workspace directory."""
    path = request.tool_call["args"].get("path", "")
    return not path.startswith("/workspace/")

def is_write_query(request: ToolCallRequest) -> bool:
    """Pause SQL that isn't a read-only SELECT."""
    query = request.tool_call["args"].get("query", "")
    return not query.lstrip().upper().startswith("SELECT")

agent = create_agent(
    model="gpt-5.5",
    tools=[write_file, execute_sql, read_data],
    middleware=[
        HumanInTheLoopMiddleware(
            interrupt_on={
                "write_file": {
                    "allowed_decisions": ["approve", "edit", "reject"],
                    "when": writes_outside_workspace,
                },
                "execute_sql": {
                    "allowed_decisions": ["approve", "reject"],
                    "when": is_write_query,
                },
            },
        ),
    ],
    checkpointer=InMemorySaver(),
)
```

When the `when` predicate returns `False`, the call runs without interrupting. When it returns `True`, or when you omit `when`, the call pauses as usual. Calls that evaluate to `False` are never added to the interrupt batch, so a reviewer only sees the actions that need a decision.

## Responding to interrupts

When you invoke the agent, it runs until it either completes or an interrupt is raised. An interrupt is triggered when a tool call matches the policy you configured in `interrupt_on`. With `version="v2"`, the result is a `GraphOutput` with an `interrupts` attribute containing the actions that require review. You can then present those actions to a reviewer and resume execution once decisions are provided.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langgraph.types import Command

# Human-in-the-loop leverages LangGraph's persistence layer.

# You must provide a thread ID to associate the execution with a conversation thread,

# so the conversation can be paused and resumed (as is needed for human review).
config = {"configurable": {"thread_id": "some_id"}} # [!code highlight]

# Run the graph until the interrupt is hit.
result = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": "Delete old records from the database",
            }
        ]
    },
    config=config, # [!code highlight]
    version="v2", # [!code highlight]
)

# result is a GraphOutput with .value and .interrupts
print(result.interrupts)  # [!code highlight]

# > (

# >    Interrupt(

# >       value={

# >          'action_requests': [

# >             {

# >                'name': 'execute_sql',

# >                'arguments': {'query': 'DELETE FROM records WHERE created_at < NOW() - INTERVAL \'30 days\';'},

# >                'description': 'Tool execution pending approval\n\nTool: execute_sql\nArgs: {...}'

# >             }

# >          ],

# >          'review_configs': [

# >             {

# >                'action_name': 'execute_sql',

# >                'allowed_decisions': ['approve', 'reject']

# >             }

# >          ]

# >       }

# >    ),

# > )

# Resume with approval decision
agent.invoke(
    Command( # [!code highlight]
        resume={"decisions": [{"type": "approve"}]}  # or "reject" [!code highlight]
    ), # [!code highlight]
    config=config, # Same thread ID to resume the paused conversation
    version="v2",
)
```

### Decision types

<Tabs>
  <Tab title="✅ approve">
    Use `approve` to approve the tool call as-is and execute it without changes.

    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    agent.invoke(
        Command(
            # Decisions are provided as a list, one per action under review.
            # The order of decisions must match the order of actions
            # in the interrupt request.
            resume={
                "decisions": [
                    {
                        "type": "approve",
                    }
                ]
            }
        ),
        config=config,  # Same thread ID to resume the paused conversation
        version="v2",
    )
    ```
  </Tab>

  <Tab title="✏️ edit">
    Use `edit` to modify the tool call before execution.
    Provide the edited action with the new tool name and arguments.

    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    agent.invoke(
        Command(
            # Decisions are provided as a list, one per action under review.
            # The order of decisions must match the order of actions
            # in the interrupt request.
            resume={
                "decisions": [
                    {
                        "type": "edit",
                        # Edited action with tool name and args
                        "edited_action": {
                            # Tool name to call.
                            # Will usually be the same as the original action.
                            "name": "new_tool_name",
                            # Arguments to pass to the tool.
                            "args": {"key1": "new_value", "key2": "original_value"},
                        }
                    }
                ]
            }
        ),
        config=config,  # Same thread ID to resume the paused conversation
        version="v2",
    )
    ```

    <Tip>
      When **editing** tool arguments, make changes conservatively. Significant modifications to the original arguments may cause the model to re-evaluate its approach and potentially execute the tool multiple times or take unexpected actions.
    </Tip>
  </Tab>

  <Tab title="❌ reject">
    Use `reject` to deny the tool call and provide feedback instead of execution. The tool is not executed.

    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    agent.invoke(
        Command(
            # Decisions are provided as a list, one per action under review.
            # The order of decisions must match the order of actions
            # in the interrupt request.
            resume={
                "decisions": [
                    {
                        "type": "reject",
                        # Optional: explain why the action was rejected
                        # and whether the agent should retry a different approach.
                        "message": "User rejected this action. Do not retry this tool call.",
                    }
                ]
            }
        ),
        config=config,  # Same thread ID to resume the paused conversation
        version="v2",
    )
    ```

    The `message` is added to the conversation as feedback to help the agent understand why the action was rejected and what it should do instead. When you omit `message`, the middleware uses a default rejection message that tells the model the tool was not executed and not to retry the same tool call unless the user asks. For side-effecting tools, provide a domain-specific message that is explicit about whether the agent should abandon the action, ask a follow-up question, or try a safer alternative.
  </Tab>

  <Tab title="💬 respond">
    Use `respond` for "ask user" style tools where the tool's real implementation is the human's reply. The `message` content is returned directly as the tool result; the tool itself is not executed.

    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    agent.invoke(
        Command(
            # Decisions are provided as a list, one per action under review.
            # The order of decisions must match the order of actions
            # in the interrupt request.
            resume={
                "decisions": [
                    {
                        "type": "respond",
                        # The human's reply, returned directly as the tool result
                        "message": "Blue.",
                    }
                ]
            }
        ),
        config=config,  # Same thread ID to resume the paused conversation
        version="v2",
    )
    ```

    The `message` is returned to the agent as a successful `ToolMessage`. Use `respond` when the tool is intentionally a placeholder for human input, for example, an `ask_user` tool that prompts for clarification. Do not use `respond` to deny a proposed action, because it tells the model that the tool completed successfully.
  </Tab>
</Tabs>

***

### Multiple decisions

When multiple actions are under review, provide a decision for each action in the same order as they appear in the interrupt:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
    "decisions": [
        {"type": "approve"},
        {
            "type": "edit",
            "edited_action": {
                "name": "tool_name",
                "args": {"param": "new_value"}
            }
        },
        {
            "type": "reject",
            "message": "This action is not allowed"
        }
    ]
}
```

## Streaming with human-in-the-loop

You can use `stream()` instead of `invoke()` to get real-time updates while the agent runs and handles interrupts. Use `stream_mode=['updates', 'messages']` with `version="v2"` to stream both agent progress and LLM tokens in the unified v2 format.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langgraph.types import Command

config = {"configurable": {"thread_id": "some_id"}}
