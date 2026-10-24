# CopilotKit
Source: https://docs.langchain.com/oss/python/langchain/frontend/integrations/copilotkit

Use CopilotKit with LangGraph, Deep Agents, and React with custom endpoints, the Python AG-UI bridge, and structured generative UI

[CopilotKit](https://www.copilotkit.ai/) provides a full React chat runtime and pairs especially well with LangGraph when you want the agent to return **structured UI payloads** instead of only plain text. In this pattern, your LangGraph deployment serves both the graph API and a custom CopilotKit endpoint, while the frontend parses assistant messages into dynamic React components.

On the server, the [copilotkit](https://pypi.org/project/copilotkit/) package provides [`CopilotKitMiddleware`](https://docs.copilotkit.ai) so a LangGraph graph, a LangChain agent, or a [Deep Agent](/oss/python/deepagents/overview) can speak the [Agent UI (AG-UI)](https://docs.ag-ui.com/) wire protocol, stream tool and message events to a chat UI, and read or write the shared **CopilotKit** slice of state, with helpers to mount a CopilotKit-compatible HTTP endpoint in front of your graph.

This approach is useful when you want:

* a ready-made chat runtime instead of wiring `stream.messages` yourself
* a custom server endpoint that can add provider-specific behavior next to your deployed graph
* structured generative UI rendered from a constrained component registry

[CopilotKit for LangGraph](https://docs.copilotkit.ai/langgraph) also documents [generative UI](https://docs.copilotkit.ai/langgraph/generative-ui), [human in the loop](https://docs.copilotkit.ai/langgraph/human-in-the-loop) (HITL), and [shared state](https://docs.copilotkit.ai/langgraph/shared-state) on top of the same middleware and clients.

<Info>
  For CopilotKit-specific APIs, UI patterns, and runtime configuration, see the
  [CopilotKit docs](https://docs.copilotkit.ai/langgraph). For a Deep Agent walkthrough, see
  [Deep Agents and CopilotKit](https://docs.copilotkit.ai/langgraph/deep-agents) in the CopilotKit docs.
</Info>

<ExampleEmbed />

## How it works

At a high level, CopilotKit sits between your React app and the LangGraph deployment. The frontend sends conversation state to a custom `/api/copilotkit` route mounted alongside the graph API, that route forwards the request to LangGraph, and the response comes back with both assistant messages and any structured UI payloads your component registry can render.

1. **Deploy the graph as usual** using LangSmith or using a LangGraph development server.
2. **Extend the deployment with an HTTP app** that mounts a CopilotKit route next to the graph API.
3. **Wrap the frontend in `CopilotKit`** and point it at that custom runtime URL.
4. **Register dynamic UI components** and parse assistant responses into those components at render time.

```mermaid theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
%%{
  init: {
    "fontFamily": "monospace",
    "flowchart": {
      "curve": "curve"
    }
  }
}%%
graph LR
  USER["User input"]
  UI["CopilotKit React app"]
  ENDPOINT["/api/copilotkit"]
  GRAPH["LangGraph deployment"]
  RENDER["Hashbrown UI kit"]

  USER --> UI
  UI --> ENDPOINT
  ENDPOINT --> GRAPH
  GRAPH --> ENDPOINT
  ENDPOINT --> UI
  UI --> RENDER
```

## What you get on the Python server

The [copilotkit](https://pypi.org/project/copilotkit/) and related packages bridge a LangGraph deployment and CopilotKit clients.

| Component                                                                                            | Role                                                                                                                                                                                                                                                                                                                                                                                    |
| ---------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `CopilotKitMiddleware`                                                                               | Merges CopilotKit and AG-UI state and requests into your agent, including frontend [tool calls](/oss/python/langchain/agents#tools) and context. Add it to the `middleware` list for [create\_agent](https://reference.langchain.com/python/langchain/agents/factory/create_agent) or [create\_deep\_agent](https://reference.langchain.com/python/deepagents/graph/create_deep_agent). |
| `CopilotKitState` (subclass)                                                                         | [Custom state](/oss/python/langchain/short-term-memory): extend `CopilotKitState` so the CopilotKit key is part of graph state.                                                                                                                                                                                                                                                         |
| `LangGraphAGUIAgent`                                                                                 | Bundles a compiled graph with a name and description for the runtime.                                                                                                                                                                                                                                                                                                                   |
| `add_langgraph_fastapi_endpoint` (from [ag-ui-langgraph](https://pypi.org/project/ag-ui-langgraph/)) | Wires a **FastAPI** app so CopilotKit can run your graph on the same [LangGraph](/oss/python/langgraph/overview) process. Use it when you add a [custom `http` app in `langgraph.json`](#extend-the-langgraph-deployment-with-a-custom-endpoint) instead of a separate HTTP server.                                                                                                     |

`CopilotKitMiddleware` is the same middleware for [create\_deep\_agent](https://reference.langchain.com/python/deepagents/graph/create_deep_agent) and for a graph from [create\_agent](https://reference.langchain.com/python/langchain/agents/factory/create_agent) when you add it to the `middleware` list. For a `create_agent` graph with `CopilotKitState` and a FastAPI bridge, follow the [Python `main.py` example](#extend-the-langgraph-deployment-with-a-custom-endpoint) below. Structured generative UI (for example `useAgentContext` and an `output_schema` from the client) needs extra middleware that maps Copilot state to a [structured output](/oss/python/langchain/agents#structured-output) strategy, as in the expandable `src/middleware.py` example in the same section.

Mounting `app` on the `http` key in `langgraph.json` follows the usual [LangGraph or LangSmith deployment](/oss/python/langgraph/deploy) so one process serves the graph and the same FastAPI app to the CopilotKit client.

## Installation

For the backend endpoint:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
uv add copilotkit ag-ui-langgraph fastapi uvicorn
```

The middleware package sits alongside the Deep Agents stack. Install it with your [chat model](/oss/python/integrations/chat) package (this example uses OpenAI):

<CodeGroup>
  ```python pip theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  pip install -U deepagents copilotkit langchain-openai
  ```

  ```python uv theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  uv add deepagents copilotkit langchain-openai
  ```
</CodeGroup>

For the frontend app:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
bun add @copilotkit/react-core @copilotkit/react-ui @hashbrownai/core @hashbrownai/react
```

## Use CopilotKit with a Deep Agent

Add `CopilotKitMiddleware` to the `middleware` list you pass to [create\_deep\_agent](https://reference.langchain.com/python/deepagents/graph/create_deep_agent). The middleware lets CopilotKit route frontend tool calls and align chat state with your graph. Keep any other [middleware you configure](/oss/python/deepagents/customization#middleware) in the same list.

The compiled graph is then ready to plug into a CopilotKit- or AG-UI–aware process (for example, the [FastAPI pattern below](#extend-the-langgraph-deployment-with-a-custom-endpoint)) or a guide such as [Deep Agents and CopilotKit](https://docs.copilotkit.ai/langgraph/deep-agents) in the CopilotKit documentation.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from deepagents import create_deep_agent
from copilotkit import CopilotKitMiddleware
from langgraph.checkpoint.memory import MemorySaver

def get_weather(location: str) -> str:
    """Return a simple weather string for a location."""
    return f"The weather in {location} is sunny."

agent = create_deep_agent(
    model="openai:gpt-5.5",
    tools=[get_weather],
    middleware=[CopilotKitMiddleware()],  # AG-UI, frontend tools, and context
    system_prompt="You are a helpful research assistant.",
    checkpointer=MemorySaver(),
)
```

## Extend the LangGraph deployment with a custom endpoint

The key idea is that the LangGraph deployment does not only serve graphs. It can also load an HTTP app, which lets you mount extra routes next to the deployment itself.

In `langgraph.json`, point `http.app` at your custom app entrypoint:

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "dependencies": ["."],
  "graphs": {
    "copilotkit_shadify": "./main.py:agent"
  },
  "http": {
    "app": "./main.py:app"
  }
}
```

In Python, create a `FastAPI` app and expose the LangGraph agent through CopilotKit's AG-UI bridge:

```python main.py theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from typing import Any, TypedDict

from ag_ui_langgraph import add_langgraph_fastapi_endpoint
from copilotkit import CopilotKitMiddleware, CopilotKitState, LangGraphAGUIAgent
from fastapi import FastAPI
from langchain.agents import create_agent

from src.middleware import apply_structured_output_schema, normalize_context

class AgentState(CopilotKitState):
    pass

class AgentContext(TypedDict, total=False):
    output_schema: dict[str, Any]

agent = create_agent(
    model="openai:gpt-5.5",
    middleware=[
        normalize_context,
        CopilotKitMiddleware(),
        apply_structured_output_schema,
    ],
    context_schema=AgentContext,
    state_schema=AgentState,
    system_prompt=(
        "You are a helpful UI assistant. Build visual responses using the "
        "available components."
    ),
)

app = FastAPI()

add_langgraph_fastapi_endpoint(
    app=app,
    agent=LangGraphAGUIAgent(
        name="copilotkit_shadify",
        description="A UI assistant that returns structured component payloads.",
        graph=agent,
    ),
    path="/",
)
```

This custom app is the important extension point: it mounts a CopilotKit-aware runtime without replacing the underlying LangGraph deployment.

In Python, the equivalent work happens in middleware: normalize the CopilotKit context and forward the `output_schema` from `useAgentContext(...)` into the model's structured output configuration.

```python expandable src/middleware.py theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import json
from collections.abc import Mapping

from langchain.agents.middleware import before_agent, wrap_model_call
from langchain.agents.structured_output import ProviderStrategy

@wrap_model_call
async def apply_structured_output_schema(request, handler):
    schema = None
    runtime = getattr(request, "runtime", None)
    runtime_context = getattr(runtime, "context", None)

    if isinstance(runtime_context, Mapping):
        schema = runtime_context.get("output_schema")

    if schema is None and isinstance(getattr(request, "state", None), dict):
        copilot_context = request.state.get("copilotkit", {}).get("context")
        if isinstance(copilot_context, list):
            for item in copilot_context:
                if isinstance(item, dict) and item.get("description") == "output_schema":
                    schema = item.get("value")
                    break

    if isinstance(schema, str):
        try:
            schema = json.loads(schema)
        except json.JSONDecodeError:
            schema = None

    if isinstance(schema, dict):
        request = request.override(
            response_format=ProviderStrategy(schema=schema, strict=True),
        )

    return await handler(request)

@before_agent
def normalize_context(state, runtime):
    copilotkit_state = state.get("copilotkit", {})
    context = copilotkit_state.get("context")

    if isinstance(context, list):
        normalized = [
            item.model_dump() if hasattr(item, "model_dump") else item
            for item in context
        ]
        return {"copilotkit": {**copilotkit_state, "context": normalized}}

    return None
```

The result is a clean separation of concerns:

* LangGraph still owns graph execution and persistence
* CopilotKit owns the chat-facing runtime contract
* your custom endpoint glues them together inside one deployment

Point your CopilotKit `runtimeUrl` at the route the FastAPI (or other) app exposes, not only the raw graph REST surface, when you use the [CopilotKit](https://docs.copilotkit.ai) runtime adapter.

Follow the CopilotKit documentation for [LangGraphHttpAgent](https://docs.copilotkit.ai/langgraph) or `LangGraphAgent` in the Node **CopilotRuntime**; the **Python** graph and middleware still define tool behavior and agent logic.
:::

## Structure the frontend app

On the frontend, wrap your app in `CopilotKit` and point it at the custom runtime URL:

```tsx theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { CopilotKit } from "@copilotkit/react-core";
import { CopilotChat, useAgentContext } from "@copilotkit/react-core/v2";
import { s } from "@hashbrownai/core";

import { useChatKit } from "@/components/chat/chat-kit";
import { chatTheme } from "@/lib/chat-theme";

export function App() {
  return (
    <CopilotKit runtimeUrl={import.meta.env.VITE_RUNTIME_URL ?? "/api/copilotkit"}>
      <Page />
    </CopilotKit>
  );
}

function Page() {
  const chatKit = useChatKit();

  useAgentContext({
    description: "output_schema",
    value: s.toJsonSchema(chatKit.schema),
  });

  return <CopilotChat {...chatTheme} />;
}
```

There are two important pieces here:

* `runtimeUrl="/api/copilotkit"` sends the chat to your custom backend route rather than directly to the raw LangGraph API
* `useAgentContext(...)` sends the UI schema to the agent so the model knows what structured output format it should produce

## Register the dynamic components

The component registry lives in `useChatKit()`. This is where you define the set of components the agent is allowed to emit, such as cards, rows, columns, charts, code blocks, and buttons.

```tsx theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { s } from "@hashbrownai/core";
import { exposeComponent, exposeMarkdown, useUiKit } from "@hashbrownai/react";

import { Button } from "@/components/ui/button";
import { Card } from "@/components/ui/card";
import { CodeBlock } from "@/components/ui/code-block";
import { Row, Column } from "@/components/ui/layout";
import { SimpleChart } from "@/components/ui/simple-chart";

export function useChatKit() {
  return useUiKit({
    components: [
      exposeMarkdown(),
      exposeComponent(Card, {
        name: "card",
        description: "Card to wrap generative UI content.",
        children: "any",
      }),
      exposeComponent(Row, {
        name: "row",
        props: {
          gap: s.string("Tailwind gap size") as never,
        },
        children: "any",
      }),
      exposeComponent(Column, {
        name: "column",
        children: "any",
      }),
      exposeComponent(SimpleChart, {
        name: "chart",
        props: {
          labels: s.array("Category labels", s.string("A label")),
          values: s.array("Numeric values", s.number("A value")),
        },
        children: false,
      }),
      exposeComponent(CodeBlock, {
        name: "code_block",
        props: {
          code: s.streaming.string("The code to display"),
          language: s.string("Programming language") as never,
        },
        children: false,
      }),
      exposeComponent(Button, {
        name: "button",
        children: "text",
      }),
    ],
  });
}
```

This registry becomes the contract between the agent and the UI. The model is not generating arbitrary JSX. It is generating structured data that must validate against the components and props you exposed.

## Render assistant messages as dynamic UI

Once the assistant response arrives, the custom message renderer decides how to display it. In this example:

* assistant messages are parsed as structured JSON against the UI kit schema
* valid structured output is rendered as real React components
* user messages are rendered as ordinary chat bubbles

```tsx theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import type { AssistantMessage } from "@ag-ui/core";
import type { RenderMessageProps } from "@copilotkit/react-ui";
import { useJsonParser } from "@hashbrownai/react";
import { memo } from "react";

import { useChatKit } from "@/components/chat/chat-kit";
import { Squircle } from "@/components/squircle";

const AssistantMessageRenderer = memo(function AssistantMessageRenderer({
  message,
}: {
  message: AssistantMessage;
}) {
  const kit = useChatKit();
  const { value } = useJsonParser(message.content ?? "", kit.schema);

  if (!value) return null;

  return (
    <div className="group/msg mt-2 flex w-full justify-start">
      <div className="magic-text-output w-full px-1 py-1">{kit.render(value)}</div>
    </div>
  );
});

export function CustomMessageRenderer({ message }: RenderMessageProps) {
  if (message.role === "assistant") {
    return <AssistantMessageRenderer message={message} />;
  }

  return (
    <div className="flex w-full justify-end">
      <Squircle className="w-full max-w-[64ch] px-4 py-3">
        <pre>{typeof message.content === "string" ? message.content : JSON.stringify(message.content, null, 2)}</pre>
      </Squircle>
    </div>
  );
}
```

This renderer pattern is what makes the integration feel native:

* CopilotKit handles chat state and transport
* the custom renderer decides how assistant payloads become UI
* [Hashbrown](https://hashbrown.dev/) turns validated structured data into concrete React elements

## Resources

* [Deep Agents and CopilotKit](https://docs.copilotkit.ai/langgraph/deep-agents) in the CopilotKit documentation — end-to-end Next.js, dev server, and **Deep Agent** path
* [CopilotKit: LangGraph features](https://docs.copilotkit.ai/langgraph) — generative UI, HITL, shared state
* [LangGraph deployment](/oss/python/langgraph/deploy) — production and dev server

## Best practices

* **Keep the custom endpoint thin:** use it to adapt CopilotKit to your graph deployment, not to duplicate business logic already inside the graph
* **Send the schema explicitly:** `useAgentContext` should describe the UI contract every time the page mounts
* **Register a constrained component set:** expose only the components and props you actually want the model to use
* **Treat rendering as a parsing step:** parse assistant content against your schema before rendering it
* **Keep user messages plain:** only assistant messages need the structured renderer; user messages can stay normal chat bubbles

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langchain/frontend/integrations/copilotkit.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# OpenUI
Source: https://docs.langchain.com/oss/python/langchain/frontend/integrations/openui

Generate complete, interactive dashboards and reports using the OpenUI component library and openui-lang

[OpenUI](https://github.com/thesysdev/openui) is a generative UI library that lets a language model produce complete, interactive UIs in a declarative format called **openui-lang**. Instead of returning a chat message, the agent returns a component tree with cards, charts, tables, tabs, and forms that the `Renderer` turns into a real React UI.

This integration is well-suited for data-rich outputs like reports, dashboards, and data explorers, where the model is both the data analyst and the UI designer.

<ExampleEmbed />

## How it works

1. **Generate the system prompt:** call `openuiLibrary.prompt()` once at startup; it produces a complete openui-lang reference that the model uses to write valid component trees
2. **Inject on first message:** send the system prompt as the opening system message when a new conversation starts
3. **Model writes openui-lang:** the model responds with a program like `root = Stack([header, kpis, chart])` instead of prose
4. **Render with `Renderer`:** pass the text to OpenUI's `Renderer` and the component library; it parses and renders the tree

```mermaid theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
%%{
  init: {
    "fontFamily": "monospace",
    "flowchart": {
      "curve": "curve"
    }
  }
}%%
graph LR
  PROMPT["openuiLibrary.prompt()"]
  AGENT["createAgent()"]
  STREAM["useStream()"]
  RENDERER["Renderer"]

  PROMPT --"system message"--> AGENT
  AGENT --"openui-lang text"--> STREAM
  STREAM --"ai message content"--> RENDERER
```

## Installation

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
npm install @langchain/react @openuidev/react-ui @openuidev/react-headless @openuidev/react-lang
```

<Tip>
  OpenUI requires React 19+ and [`zustand`](https://www.npmjs.com/package/zustand). The frontend code is React-only; the LangGraph agent backend can be written in TypeScript or Python.
</Tip>

## Import the component styles

Import OpenUI's bundled styles in your CSS entry point or directly in your root component:

```css theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
@import "@openuidev/react-ui/components.css";
@import "@openuidev/react-ui/styles/index.css";
```

## Generate the system prompt

OpenUI ships a `openuiLibrary.prompt()` function that generates the complete openui-lang reference, with all component signatures, syntax rules, streaming tips, and examples. Call it once at module load time:

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { openuiLibrary, openuiPromptOptions } from "@openuidev/react-ui/genui-lib";

// Generate the full openui-lang system prompt. Call this once at startup,
// not inside a component, to avoid recomputing it on every render.
const SYSTEM_PROMPT = openuiLibrary.prompt({
  ...openuiPromptOptions,
  preamble:
    "You are a report generator. When asked for a report, produce a detailed, " +
    "data-rich report using openui-lang: executive summary, KPI cards, charts, " +
    "tables, and multiple sections. Your ENTIRE response must be raw openui-lang " +
    "— no code fences, no markdown, no prose.",
});
```

The `preamble` overrides the default persona. Add `additionalRules` to inject task-specific constraints:

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const SYSTEM_PROMPT = openuiLibrary.prompt({
  ...openuiPromptOptions,
  preamble: "You are a report generator...",
  additionalRules: [
    ...(openuiPromptOptions.additionalRules ?? []),
    "Always end the report with 3–4 follow-up query buttons using " +
    "Button({ type: 'continue_conversation' }, 'secondary') inside a " +
    "Card([CardHeader('Explore Further'), Buttons([...])], 'sunk').",
  ],
});
```

## Inject the system prompt via useStream

Send the system prompt as the first message of every new thread. Check `stream.messages.length === 0` to detect a fresh thread and prepend a `system` message:

```tsx theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { useCallback } from "react";
import { useStream } from "@langchain/react";

const SYSTEM_PROMPT = openuiLibrary.prompt({ ... });

export function App() {
  const stream = useStream({
    apiUrl: import.meta.env.VITE_LANGGRAPH_API_URL ?? "/api/langgraph",
    assistantId: "openui",
  });

  const handleSubmit = useCallback(
    (text: string) => {
      // Inject the system prompt only on the first message of a new thread.
      // Subsequent messages already have it in their persisted history.
      const isNewThread = stream.messages.length === 0;
      stream.submit({
        messages: [
          ...(isNewThread
            ? [{ type: "system", content: SYSTEM_PROMPT }]
            : []),
          { type: "human", content: text },
        ],
      });
    },
    [stream],
  );

  // ...
}
```

## Render with the Renderer

Pass the AI message's text content directly to `Renderer` along with `openuiLibrary`:

```tsx theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { Renderer } from "@openuidev/react-lang";
import { openuiLibrary } from "@openuidev/react-ui/genui-lib";
import { AIMessage } from "langchain";

function MessageList({ messages, isLoading }) {
  const lastAiIdx = messages.reduce(
    (acc, msg, i) => (AIMessage.isInstance(msg) ? i : acc),
    -1,
  );

  return messages.map((msg, i) => {
    if (AIMessage.isInstance(msg)) {
      const text = msg.text;
      return (
        <Renderer
          key={msg.id ?? i}
          response={text}
          library={openuiLibrary}
          isStreaming={isLoading && i === lastAiIdx}
        />
      );
    }
    // ... human message bubble
  });
}
```

Pass `isStreaming={true}` during the active stream so the Renderer handles unresolved references gracefully as definitions arrive.

## The openui-lang format

The model writes a program rather than a JSON spec. Every statement is an assignment; `root` is the entry point. The official prompt teaches the model this format, including hoisting — writing `root` first so the UI shell appears immediately:

```
root = Stack([header, execSummary, kpis, marketSection])

header    = CardHeader("State of AI in 2025", "Comprehensive Analysis")
execSummary = MarkDownRenderer("## Executive Summary\n\nThe AI market reached...")

kpi1 = Card([CardHeader("$826B", "Global Market"), TextContent("42% YoY", "small")], "sunk")
kpi2 = Card([CardHeader("78%",   "Adoption"),       TextContent("Fortune 500",  "small")], "sunk")
kpis = Stack([kpi1, kpi2], "row", "m", "stretch", "start", true)

col1 = Col("Segment", "string")
col2 = Col("Revenue ($B)", "number")
tbl  = Table([col1, col2], [["Generative AI", 286], ["ML Infra", 198]])
s1   = Series("Revenue", [286, 198, 147])
ch1  = BarChart(["Gen AI", "ML Infra", "Vision"], [s1])
marketSection = Card([CardHeader("Market Breakdown"), tbl, ch1])
```

With hoisting enabled (recommended), the `root` line is written first so the page structure appears immediately and each section fills in as the model defines it.

## Progressive rendering utilities

Wiring [`useStream`](https://reference.langchain.com/javascript/langchain-react/index/useStream) to `Renderer` directly causes results in re-rendering on every streaming token and produces hundreds of no-op re-parses per response. This causes chart components to crash when their data hasn't arrived yet. The utilities below solve these problems:

| Problem                      | Solution                                                                                                             |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| **Partial string literals**  | `truncateAtOpenString` / `closeOrTruncateOpenString` — drop or close incomplete strings before parsing               |
| **Mid-token churn**          | `useStableText` — gate Renderer updates on complete statement boundaries (`name = Expr(…)`) rather than every token  |
| **Chart null-data crashes**  | `chartDataRefsResolved` — verify a chart's `Series` and label arrays are defined before including it in the snapshot |
| **No `root` yet / fallback** | `buildProgressiveRoot` — synthesise a `root = Stack([…])` from top-level variables when the model hasn't written one |
| **Snake\_case identifiers**  | `sanitizeIdentifiers` — the parser only accepts camelCase; convert any `snake_case` names the model emits            |

Copy the full block into your project and pass `stable` to `<Renderer>`:

````tsx expandable theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import {
  useCallback,
  useEffect,
  useMemo,
  useRef,
  useState,
} from "react";
import {
  type ActionEvent,
  BuiltinActionType,
  Renderer,
} from "@openuidev/react-lang";
import { openuiLibrary } from "@openuidev/react-ui/genui-lib";

/** Strip any markdown code fence the model may have emitted. */
function stripCodeFence(text: string): string {
  return text
    .replace(/^```[a-z]*\r?\n?/i, "")
    .replace(/\n?```\s*$/i, "")
    .trim();
}

/**
 * The openui-lang parser only accepts camelCase identifiers.
 * Convert any snake_case variable names the model emits; string content is untouched.
 */
function sanitizeIdentifiers(text: string): string {
  const toCamel = (s: string) =>
    s.replace(/_([a-zA-Z0-9])/g, (_, c: string) => c.toUpperCase());

  const snakeVars: string[] = [];
  for (const m of text.matchAll(/^([a-zA-Z][a-zA-Z0-9]*(?:_[a-zA-Z0-9]+)+)\s*=/gm)) {
    if (!snakeVars.includes(m[1])) snakeVars.push(m[1]);
  }
  if (snakeVars.length === 0) return text;

  let result = "";
  let inStr = false;
  let i = 0;
  while (i < text.length) {
    if (text[i] === "\\" && inStr) { result += text[i] + (text[i + 1] ?? ""); i += 2; continue; }
    if (text[i] === '"') { inStr = !inStr; result += text[i++]; continue; }
    if (!inStr) {
      let replaced = false;
      for (const v of snakeVars) {
        if (text.startsWith(v, i) && !/[a-zA-Z0-9_]/.test(text[i + v.length] ?? "")) {
          result += toCamel(v); i += v.length; replaced = true; break;
        }
      }
      if (!replaced) result += text[i++];
    } else {
      result += text[i++];
    }
  }
  return result;
}

/**
 * Walk the text tracking open strings. If the text ends mid-string, truncate to
 * the last safe newline — this prevents a partial string literal from consuming
 * any `root = Stack(…)` line we synthesise later.
 */
function truncateAtOpenString(text: string): string {
  let inStr = false;
  let lastSafeNewline = 0;
  for (let i = 0; i < text.length; i++) {
    const ch = text[i];
    if (ch === "\\" && inStr) { i++; continue; }
    if (ch === '"') { inStr = !inStr; continue; }
    if (ch === "\n" && !inStr) lastSafeNewline = i;
  }
  return inStr ? text.slice(0, lastSafeNewline) : text;
}

/**
 * Like truncateAtOpenString, but synthesises a closing `")` when the partial
 * line is a TextContent statement. This lets text render token-by-token while
 * all other partial-string lines are still truncated.
 */
function closeOrTruncateOpenString(text: string): string {
  let inStr = false;
  let lastSafeNewline = 0;
  for (let i = 0; i < text.length; i++) {
    const ch = text[i];
    if (ch === "\\" && inStr) { i++; continue; }
    if (ch === '"') { inStr = !inStr; continue; }
    if (ch === "\n" && !inStr) lastSafeNewline = i;
  }
  if (!inStr) return text;

  const safeText = lastSafeNewline > 0 ? text.slice(0, lastSafeNewline) : "";
  const partialLine = text.slice(lastSafeNewline > 0 ? lastSafeNewline + 1 : 0);

  if (/^[a-zA-Z][a-zA-Z0-9]*\s*=\s*TextContent\(/.test(partialLine)) {
    return (lastSafeNewline > 0 ? safeText + "\n" : "") + partialLine + '")';
  }
  return safeText;
}

/** Count lines that form a complete assignment ending with `)` or `]`. */
function countCompleteStatements(text: string): number {
  let count = 0;
  for (const line of text.split("\n")) {
    const t = line.trimEnd();
    if ((t.endsWith(")") || t.endsWith("]")) && /^[a-zA-Z]/.test(t)) count++;
  }
  return count;
}

const CHART_TYPES = new Set([
  "BarChart", "LineChart", "AreaChart", "RadarChart",
  "HorizontalBarChart", "PieChart", "RadialChart",
  "SingleStackedBarChart", "ScatterChart",
]);

const OPENUI_KEYWORDS = new Set([
  "true", "false", "null", "grouped", "stacked", "linear", "natural", "step",
  "pie", "donut", "string", "number", "action", "row", "column", "card", "sunk",
  "clear", "info", "warning", "error", "success", "neutral", "danger", "start",
  "end", "center", "between", "around", "evenly", "stretch", "baseline",
  "small", "default", "large", "none", "xs", "s", "m", "l", "xl",
  "horizontal", "vertical",
]);

/**
 * Chart components (recharts) crash with `.map() on null` when their labels or
 * series props are unresolved. Before committing a stable snapshot, verify that
 * every chart in the text has all its data variables already defined.
 */
function chartDataRefsResolved(text: string): boolean {
  const lines = text.split("\n");
  const complete = new Set<string>();
  for (const line of lines) {
    const t = line.trimEnd();
    const m = t.match(/^([a-zA-Z][a-zA-Z0-9]*)\s*=/);
    if (m && (t.endsWith(")") || t.endsWith("]"))) complete.add(m[1]);
  }
  for (const line of lines) {
    const t = line.trimEnd();
    const m = t.match(/^([a-zA-Z][a-zA-Z0-9]*)\s*=\s*([A-Z][a-zA-Z0-9]*)\(/);
    if (!m || !CHART_TYPES.has(m[2]) || !t.endsWith(")")) continue;
    const rhs = t.slice(t.indexOf("=") + 1).replace(/"(?:[^"\\]|\\.)*"/g, '""');
    for (const [, name] of rhs.matchAll(/\b([a-zA-Z][a-zA-Z0-9]*)\b/g)) {
      if (/^[a-z]/.test(name) && !OPENUI_KEYWORDS.has(name) && !complete.has(name))
        return false;
    }
  }
  return true;
}

/**
 * If the model hasn't written a `root = Stack(…)` yet, synthesise one from the
 * top-level variables (those defined but not referenced inside any other expression).
 * This enables progressive rendering even when the model writes root last.
 */
function buildProgressiveRoot(text: string): string {
  if (!text) return text;
  const safe = truncateAtOpenString(text);
  if (/^root\s*=/m.test(safe)) return safe;

  const defs: string[] = [];
  const seen = new Set<string>();
  for (const m of safe.matchAll(/^([a-zA-Z_][a-zA-Z0-9_]*)\s*=/gm)) {
    if (!seen.has(m[1])) { defs.push(m[1]); seen.add(m[1]); }
  }
  if (defs.length === 0) return safe;

  const referenced = new Set<string>();
  for (const line of safe.split("\n")) {
    const thisVar = line.match(/^([a-zA-Z_][a-zA-Z0-9_]*)\s*=/)?.[1];
    const stripped = line.replace(/"(?:[^"\\]|\\.)*"/g, '""');
    for (const v of defs) {
      if (v !== thisVar && new RegExp(`\\b${v}\\b`).test(stripped)) referenced.add(v);
    }
  }

  const topLevel = defs.filter((v) => !referenced.has(v));
  const rootVars = topLevel.length > 0 ? topLevel : defs;
  return `${safe.trimEnd()}\nroot = Stack([${rootVars.join(", ")}], "column", "l")`;
}

/**
 * Gate Renderer updates to moments when at least one new *complete* statement
 * has arrived. This eliminates hundreds of no-op re-parses during streaming.
 *
 * Special case: TextContent lines update token-by-token (via closeOrTruncate)
 * so text renders progressively without waiting for the full line to complete.
 */
function useStableText(raw: string, isStreaming: boolean): string {
  const [stable, setStable] = useState<string>("");
  const lastCount = useRef(0);

  useEffect(() => {
    const safe = truncateAtOpenString(raw);         // strict — for counting only
    const enhanced = closeOrTruncateOpenString(raw); // display — closes partial TextContent

    if (!isStreaming) { setStable(enhanced); return; }

    const count = countCompleteStatements(safe);
    const newComplete = count > lastCount.current && chartDataRefsResolved(safe);
    const partialTextContent = enhanced !== safe;

    if (newComplete || partialTextContent) {
      if (newComplete) lastCount.current = count;
      setStable(enhanced);
    }
  }, [raw, isStreaming]);

  return stable;
}

function AIMessageView({
  raw,
  isStreaming,
  onSubmit,
}: {
  raw: string;
  isStreaming: boolean;
  onSubmit: (text: string) => void;
}) {
  const stable = useStableText(raw, isStreaming);
  const processed = useMemo(() => buildProgressiveRoot(stable), [stable]);

  const handleAction = useCallback(
    (event: ActionEvent) => {
      if (event.type === BuiltinActionType.ContinueConversation) {
        onSubmit(event.humanFriendlyMessage);
      }
    },
    [onSubmit],
  );

  if (!processed) return null;

  return (
    <Renderer
      response={processed}
      library={openuiLibrary}
      isStreaming={isStreaming}
      onAction={handleAction}
    />
  );
}

export function MessageList({ messages, isLoading, onSubmit }) {
  const lastAiIdx = messages.reduce(
    (acc, msg, i) => (msg.getType() === "ai" ? i : acc),
    -1,
  );

  return messages.map((msg, i) => {
    if (msg.getType() === "human") {
      return (
        <div key={msg.id ?? i} className="flex justify-end">
          <div className="user-bubble">
            {msg.text}
          </div>
        </div>
      );
    }

    if (msg.getType() === "ai") {
      const raw = sanitizeIdentifiers(
        stripCodeFence(msg.text),
      );
      if (!raw) return null;
      return (
        <div key={msg.id ?? i}>
          <AIMessageView
            raw={raw}
            isStreaming={isLoading && i === lastAiIdx}
            onSubmit={onSubmit}
          />
        </div>
      );
    }

    return null;
  });
}
````

## Follow-up queries

OpenUI's `Button` component supports a `continue_conversation` action type. When the user clicks a follow-up button, `Renderer` fires `onAction` and the `AIMessageView` above submits the button's label as the next user message, exactly the same code path as typing in the input.

Add an "Explore Further" section to every report via `additionalRules` in the system prompt:

```
followUp1 = Button("Compare AI leaders 2024 vs 2025", { type: "continue_conversation" }, "secondary")
followUp2 = Button("Global AI investment breakdown",  { type: "continue_conversation" }, "secondary")
followUpBtns = Buttons([followUp1, followUp2], "row")
followUpCard  = Card([CardHeader("Explore Further"), followUpBtns], "sunk")
root = Stack([..., followUpCard])
```

## Best practices

* **Generate the system prompt at module load:** not inside a React component; the prompt is several kilobytes and should be computed once
* **Inject the system prompt only on fresh threads:** check `stream.messages.length === 0` and skip injection on subsequent turns to avoid duplicating the prompt in the thread history
* **Use hoisting order:** write `root = Stack([...])` first; the UI shell appears immediately and sections fill in progressively as the model defines each one
* **Gate on complete statements:** avoid re-rendering the Renderer on every token; update only when a full statement (`name = ComponentCall(...)`) has arrived
* **Verify chart data before rendering:** chart components need their `Series` and label arrays defined before they're included in the stable snapshot
* **Keep camelCase variable names:** the openui-lang parser only accepts camelCase identifiers; reinforce this in the system prompt's `additionalRules`

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langchain/frontend/integrations/openui.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Overview
Source: https://docs.langchain.com/oss/python/langchain/frontend/integrations/overview

Connect useStream to any React UI component library or generative UI framework

[`useStream`](https://reference.langchain.com/javascript/langchain-react/index/useStream) is UI-agnostic. It returns plain reactive state with messages, tool calls, loading flags, values, and thread metadata that you wire to any visual layer you choose. These pages show how different libraries integrate with LangChain frontends, each with a different philosophy for building AI chat and generative UI.

## Integrations

<CardGroup>
  <Card title="CopilotKit" icon="package" href="/oss/python/langchain/frontend/integrations/copilotkit">
    Full AI chat runtime with structured generative UI support. Add a custom CopilotKit endpoint to your LangGraph deployment, then render dynamic component trees in React.
  </Card>

  <Card title="AI Elements" icon="package" href="/oss/python/langchain/frontend/integrations/ai-elements">
    Composable shadcn/ui-based components for AI chat. Drop in `Conversation`, `Message`, `Tool`, and `Reasoning` and wire them directly to `stream.messages`.
  </Card>

  <Card title="assistant-ui" icon="package" href="/oss/python/langchain/frontend/integrations/assistant-ui">
    Headless React framework with a full runtime layer. Bridge `useStream` to `AssistantRuntimeProvider` via the `useExternalStoreRuntime` adapter.
  </Card>

  <Card title="OpenUI" icon="package" href="/oss/python/langchain/frontend/integrations/openui">
    Generative UI library that lets the agent produce complete, interactive dashboards in a declarative component DSL. Purpose-built for data-rich, report-style UIs.
  </Card>
</CardGroup>

## Choosing a library

Each library fits a slightly different integration model. The choice depends on what kind of UI you're building:

|                   | CopilotKit                                                     | AI Elements                          | assistant-ui                          | OpenUI                                              |
| ----------------- | -------------------------------------------------------------- | ------------------------------------ | ------------------------------------- | --------------------------------------------------- |
| **Best for**      | Full chat runtime plus structured generative UI                | Chat with rich message types         | Full-featured chat with minimal setup | Generated dashboards and reports                    |
| **UI style**      | CopilotKit chat shell + custom message renderers               | Composable shadcn/ui components      | Headless slots + default theme        | Prebuilt component library with declarative DSL     |
| **Customisation** | Custom backend endpoint, agent context, and renderers          | Edit source files directly           | Override component slots              | Theme via CSS custom properties                     |
| **Streaming UX**  | Runtime-managed chat stream with structured assistant payloads | Component-level progressive render   | Built-in thread management            | Hoisting — shell appears immediately, data fills in |
| **Tool calls**    | Via CopilotKit runtime and custom renderers                    | `Tool` / `ToolHeader` / `ToolOutput` | Custom via message slots              | Inline in the generated UI                          |
| **Agent format**  | Structured assistant responses plus optional Markdown          | Any `stream.messages`                | Any `stream.messages`                 | Agent outputs openui-lang text                      |

All four work well with LangChain agents, and the latter three also connect directly to [`useStream`](https://reference.langchain.com/javascript/langchain-react/index/useStream). CopilotKit is especially useful when you want a richer runtime layer and a dedicated endpoint that can sit alongside a [LangGraph](/oss/python/langgraph/overview) deployment.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langchain/frontend/integrations/overview.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
