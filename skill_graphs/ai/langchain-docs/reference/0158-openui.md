# OpenUI
Source: https://docs.langchain.com/oss/javascript/langchain/frontend/integrations/openui

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
Source: https://docs.langchain.com/oss/javascript/langchain/frontend/integrations/overview

Connect useStream to any React UI component library or generative UI framework

[`useStream`](https://reference.langchain.com/javascript/langchain-react/index/useStream) is UI-agnostic. It returns plain reactive state with messages, tool calls, loading flags, values, and thread metadata that you wire to any visual layer you choose. These pages show how different libraries integrate with LangChain frontends, each with a different philosophy for building AI chat and generative UI.

## Integrations

<CardGroup>
  <Card title="CopilotKit" icon="package" href="/oss/javascript/langchain/frontend/integrations/copilotkit">
    Full AI chat runtime with structured generative UI support. Add a custom CopilotKit endpoint to your LangGraph deployment, then render dynamic component trees in React.
  </Card>

  <Card title="AI Elements" icon="package" href="/oss/javascript/langchain/frontend/integrations/ai-elements">
    Composable shadcn/ui-based components for AI chat. Drop in `Conversation`, `Message`, `Tool`, and `Reasoning` and wire them directly to `stream.messages`.
  </Card>

  <Card title="assistant-ui" icon="package" href="/oss/javascript/langchain/frontend/integrations/assistant-ui">
    Headless React framework with a full runtime layer. Bridge `useStream` to `AssistantRuntimeProvider` via the `useExternalStoreRuntime` adapter.
  </Card>

  <Card title="OpenUI" icon="package" href="/oss/javascript/langchain/frontend/integrations/openui">
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

All four work well with LangChain agents, and the latter three also connect directly to [`useStream`](https://reference.langchain.com/javascript/langchain-react/index/useStream). CopilotKit is especially useful when you want a richer runtime layer and a dedicated endpoint that can sit alongside a [LangGraph](/oss/javascript/langgraph/overview) deployment.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langchain/frontend/integrations/overview.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Join & rejoin streams
Source: https://docs.langchain.com/oss/javascript/langchain/frontend/join-rejoin

Disconnect from and reconnect to running agent streams

Join and rejoin lets you disconnect from a running agent stream without stopping the agent, then reconnect to it later. The agent continues executing server-side while the client is away, and you pick up the stream exactly where you left off.

<PatternEmbed />

<Note>
  This feature requires the [LangGraph Agent Server](../langgraph/local-server). Run your agent locally with `langgraph dev` or [deploy it to LangSmith](/langsmith/deployment) to use this pattern.
</Note>

## Why join & rejoin?

Traditional streaming APIs tightly couple the client and server: if the client disconnects, the stream is lost. Join and rejoin breaks this coupling, enabling several important patterns:

* **Network interruptions**: mobile users moving between cell towers or Wi-Fi networks can seamlessly resume
* **Page navigation**: users navigating away from a chat page and returning later without losing progress
* **Mobile backgrounding**: apps suspended by the OS can rejoin the stream when foregrounded
* **Long-running tasks**: agents performing multi-minute operations (research, code generation, data analysis) where users don't need to keep the page open
* **Multi-device handoff**: start a conversation on your phone, rejoin on your desktop

## Core concepts

The join/rejoin pattern involves three key mechanisms:

| Method / Option                  | Purpose                                                                |
| -------------------------------- | ---------------------------------------------------------------------- |
| `threadId`                       | Bind the stream to the LangGraph thread you want to observe            |
| `onThreadId`                     | Persist newly-created thread IDs so a remount can reconnect            |
| `stream.disconnect()`            | Leave the stream client-side while the agent keeps running server-side |
| Remount with the same `threadId` | Reattach to in-flight work for that thread                             |

<Note>
  **Join/rejoin uses `stream.disconnect()`, not `stream.stop()`.** By default, `stream.stop()` **cancels the active run**: it disconnects the client *and* cancels the run on the server. For join/rejoin, call `stream.disconnect()` (alias for `stop({ cancel: false })`) so the agent continues processing while you are away.

  To cancel execution explicitly from app code, use `stream.stop()` or [`client.runs.cancel`](https://reference.langchain.com/javascript/langchain-langgraph-sdk/client/RunsClient/cancel).
</Note>

## Setting up `useStream`

The key setup step is persisting `threadId`. When the component remounts with
the same thread ID, the stream attaches to the thread's current state and any
in-flight run.

<Info>
  The code examples use `useStream<typeof myAgent>` for type-safe stream state. See Type inference for [Python](/oss/python/langchain/frontend/overview#type-inference) or [JavaScript](/oss/javascript/langchain/frontend/overview#type-inference) backends.
</Info>

<CodeGroup>
  ```tsx React theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { useStream } from "@langchain/react";
  import { useCallback, useState } from "react";

  function Chat() {
    const [connected, setConnected] = useState(true);
    const [mountKey, setMountKey] = useState(0);
    const [threadId, setThreadId] = useState<string | null>(
      () => sessionStorage.getItem("activeThreadId"),
    );

    const stream = useStream<typeof myAgent>({
      apiUrl: "http://localhost:2024",
      assistantId: "join_rejoin",
      threadId,
      onThreadId(id) {
        setThreadId(id);
        if (id) sessionStorage.setItem("activeThreadId", id);
      },
    });

    const disconnect = useCallback(() => {
      void stream.disconnect();
      setConnected(false);
    }, [stream]);

    const rejoin = useCallback(() => {
      setMountKey((key) => key + 1);
      setConnected(true);
    }, []);

    return (
      <div key={mountKey}>
        <ConnectionStatus connected={connected} />
        <MessageList messages={stream.messages} />
        <ChatControls
          stream={stream}
          threadId={threadId}
          connected={connected}
          onDisconnect={disconnect}
          onRejoin={rejoin}
        />
      </div>
    );
  }
  ```

  ```vue Vue theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  <script setup lang="ts">
  import { useStream } from "@langchain/vue";
  import { ref } from "vue";

  const connected = ref(true);
  const mountKey = ref(0);
  const threadId = ref<string | null>(sessionStorage.getItem("activeThreadId"));

  const stream = useStream<typeof myAgent>({
    apiUrl: "http://localhost:2024",
    assistantId: "join_rejoin",
    threadId,
    onThreadId(id) {
      threadId.value = id;
      if (id) sessionStorage.setItem("activeThreadId", id);
    },
  });

  function disconnect() {
    void stream.disconnect();
    connected.value = false;
  }

  function rejoin() {
    mountKey.value += 1;
    connected.value = true;
  }
  </script>

  <template>
    <div :key="mountKey">
      <ConnectionStatus :connected="connected" />
      <MessageList :messages="stream.messages" />
      <ChatControls
        :stream="stream"
        :threadId="threadId"
        :connected="connected"
        @disconnect="disconnect"
        @rejoin="rejoin"
      />
    </div>
  </template>
  ```

  ```svelte Svelte theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  <script lang="ts">
    import { useStream } from "@langchain/svelte";

    let connected = $state(true);
    let mountKey = $state(0);
    let threadId = $state<string | null>(sessionStorage.getItem("activeThreadId"));

    const stream = useStream<typeof myAgent>({
      apiUrl: "http://localhost:2024",
      assistantId: "join_rejoin",
      threadId: () => threadId,
      onThreadId(id) {
        threadId = id;
        if (id) sessionStorage.setItem("activeThreadId", id);
      },
    });

    function disconnect() {
      void stream.disconnect();
      connected = false;
    }

    function rejoin() {
      mountKey += 1;
      connected = true;
    }
  </script>

  <div key={mountKey}>
    <ConnectionStatus {connected} />
    <MessageList messages={stream.messages} />
    <ChatControls
      {threadId}
      {connected}
      onDisconnect={disconnect}
      onRejoin={rejoin}
    />
  </div>
  ```

  ```ts Angular theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { Component, signal } from "@angular/core";
  import { injectStream } from "@langchain/angular";

  @Component({
    selector: "app-chat",
    template: `
      <connection-status [connected]="connected()" />
      <message-list [messages]="stream.messages()" />
      <chat-controls
        [stream]="stream"
        [threadId]="threadId()"
        [connected]="connected()"
        (disconnect)="disconnect()"
        (rejoin)="rejoin()"
      />
    `,
  })
  export class ChatComponent {
    threadId = signal<string | null>(sessionStorage.getItem("activeThreadId"));
    connected = signal(true);
    mountKey = signal(0);

    stream = injectStream<typeof myAgent>({
      apiUrl: "http://localhost:2024",
      assistantId: "join_rejoin",
      threadId: this.threadId,
      onThreadId: (id) => {
        this.threadId.set(id);
        if (id) sessionStorage.setItem("activeThreadId", id);
      },
    });

    disconnect() {
      void this.stream.disconnect();
      this.connected.set(false);
    }

    rejoin() {
      this.mountKey.update((key) => key + 1);
      this.connected.set(true);
    }
  }
  ```
</CodeGroup>

## Submitting messages

Submit messages normally. The thread ID binding is what allows a later remount
to reconnect to the same conversation:

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
stream.submit({ messages: [{ type: "human", content: text }] });
```

## Disconnecting from a stream

Call `stream.disconnect()` to leave the stream without cancelling the run. The agent continues processing server-side.

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
await stream.disconnect();
// equivalent to: await stream.stop({ cancel: false })
```

Do **not** use `stream.stop()` here — by default it cancels the run on the server.

After calling `disconnect()`:

* `stream.isLoading` becomes `false`
* Your own `connected` flag should also become `false`
* The message list retains all messages received up to the disconnect point
* The agent continues running on the server
* No new messages are received until you rejoin

## Rejoining a stream

Remount the stream consumer with the saved thread ID to reconnect. In React, the
demo bumps a `mountKey`; in other frameworks, use the equivalent remount or
conditional-render pattern:

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
setMountKey((key) => key + 1);
setConnected(true);
```

After rejoining:

* `connected` becomes `true`
* Any messages generated while disconnected are delivered
* New streaming messages resume in real-time
* If the agent is still running, `stream.isLoading` becomes `true`; if it has
  already finished, you receive the final state immediately

## Best practices

* **Use `disconnect()` for join/rejoin, `stop()` to cancel**: navigating away or backgrounding the app should call `stream.disconnect()`. A user-facing "Stop" or "Cancel" button should call `stream.stop()` (or [`client.runs.cancel`](https://reference.langchain.com/javascript/langchain-langgraph-sdk/client/RunsClient/cancel)).
* **Always save the thread ID**: without it, rejoining is impossible. Use both component state and persistent storage for resilience.
* **Show clear connection state**: users should always know whether they are receiving live updates or viewing a snapshot.
* **Auto-rejoin on visibility change**: use the Page Visibility API to automatically rejoin when the user returns to the tab.
* **Set reasonable timeouts**: if a rejoin attempt takes too long, fall back to fetching the thread history instead.
* **Clean up stale threads**: remove persisted thread IDs when the user starts over or the backend reports that the thread is unavailable.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langchain/frontend/join-rejoin.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Markdown messages
Source: https://docs.langchain.com/oss/javascript/langchain/frontend/markdown-messages

Render LLM responses as rich, formatted markdown with proper streaming support

LLMs naturally produce markdown-formatted text, including headings, lists, code blocks,
tables, and inline formatting. Rendering this content as plain text wastes the
structure the model is providing. This pattern shows you how to parse and render
markdown in real time as it streams from the agent, across all major frontend
frameworks.

<PatternEmbed />

## How markdown rendering works

The rendering pipeline has three steps:

1. **Receive:** [`useStream`](https://reference.langchain.com/javascript/langchain-react/index/useStream) accumulates the streamed text into `msg.text` on
   each AI message, updating reactively as new tokens arrive.
2. **Parse:** A markdown parser converts the raw text to HTML (or a React
   element tree). This runs on every update but is fast enough for chat-length
   content (\< 5ms for a 5 KB message).
3. **Render:** The parsed output is rendered into the DOM. React uses virtual
   DOM diffing; Vue and Svelte use `v-html` / `{@html}` with sanitized HTML.

## Setting up `useStream`

The markdown pattern uses a simple chat agent with no special configuration.
Wire up [`useStream`](https://reference.langchain.com/javascript/langchain-react/index/useStream) with your agent URL and assistant ID.

<Info>
  The code examples use `useStream<typeof myAgent>` for type-safe stream state. See Type inference for [Python](/oss/python/langchain/frontend/overview#type-inference) or [JavaScript](/oss/javascript/langchain/frontend/overview#type-inference) backends.
</Info>

<CodeGroup>
  ```tsx React theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { useStream } from "@langchain/react";
  import { AIMessage, HumanMessage } from "langchain";

  const AGENT_URL = "http://localhost:2024";

  export function Chat() {
    const stream = useStream<typeof myAgent>({
      apiUrl: AGENT_URL,
      assistantId: "simple_agent",
    });

    return (
      <div>
        {stream.messages.map((msg) => {
          if (AIMessage.isInstance(msg)) {
            return <Markdown key={msg.id}>{msg.text}</Markdown>;
          }
          if (HumanMessage.isInstance(msg)) {
            return <p key={msg.id}>{msg.text}</p>;
          }
        })}
      </div>
    );
  }
  ```

  ```vue Vue theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  <script setup lang="ts">
  import { useStream } from "@langchain/vue";
  import { AIMessage, HumanMessage } from "langchain";

  const AGENT_URL = "http://localhost:2024";

  const stream = useStream<typeof myAgent>({
    apiUrl: AGENT_URL,
    assistantId: "simple_agent",
  });
  </script>

  <template>
    <div>
      <template v-for="msg in stream.messages.value" :key="msg.id">
        <Markdown v-if="AIMessage.isInstance(msg)">{{ msg.text }}</Markdown>
        <p v-else-if="HumanMessage.isInstance(msg)">{{ msg.text }}</p>
      </template>
    </div>
  </template>
  ```

  ```svelte Svelte theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  <script lang="ts">
    import { useStream } from "@langchain/svelte";
    import { AIMessage, HumanMessage } from "langchain";

    const AGENT_URL = "http://localhost:2024";

    const stream = useStream<typeof myAgent>({
      apiUrl: AGENT_URL,
      assistantId: "simple_agent",
    });
  </script>

  <div>
    {#each stream.messages as msg (msg.id)}
      {#if AIMessage.isInstance(msg)}
        <Markdown content={msg.text} />
      {:else if HumanMessage.isInstance(msg)}
        <p>{msg.text}</p>
      {/if}
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
        <app-markdown [content]="msg.text" />
      }
    `,
  })
  export class ChatComponent {
    stream = injectStream<typeof myAgent>({
      apiUrl: AGENT_URL,
      assistantId: "simple_agent",
    });
  }
  ```
</CodeGroup>

## Choosing a markdown library

Each framework has a natural choice for markdown rendering:

| Framework | Library                         | Output                           | Why                                                                |
| --------- | ------------------------------- | -------------------------------- | ------------------------------------------------------------------ |
| React     | `react-markdown` + `remark-gfm` | React elements                   | Component-based, virtual DOM diffing, no `dangerouslySetInnerHTML` |
| Vue       | `marked` + `dompurify`          | Sanitized HTML via `v-html`      | Lightweight, fast, GFM built-in                                    |
| Svelte    | `marked` + `dompurify`          | Sanitized HTML via `{@html}`     | Same as Vue, consistent API                                        |
| Angular   | `marked` + `dompurify`          | Sanitized HTML via `[innerHTML]` | Same as Vue/Svelte                                                 |

<Tip>
  React's `react-markdown` converts markdown directly to React elements, so it
  doesn't need HTML sanitization. There's no `dangerouslySetInnerHTML` involved.
  For Vue, Svelte, and Angular, always sanitize the parsed HTML with `dompurify`
  before rendering.
</Tip>

## Building the Markdown component

<CodeGroup>
  ```tsx React theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import ReactMarkdown from "react-markdown";
  import remarkGfm from "remark-gfm";

  export function Markdown({ children }: { children: string }) {
    return (
      <div className="markdown-content">
        <ReactMarkdown remarkPlugins={[remarkGfm]}>
          {children}
        </ReactMarkdown>
      </div>
    );
  }
  ```

  ```vue Vue theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  <script setup lang="ts">
  import { computed, useSlots } from "vue";
  import { marked } from "marked";
  import DOMPurify from "dompurify";

  marked.setOptions({ gfm: true, breaks: true });

  const slots = useSlots();

  const html = computed(() => {
    const slot = slots.default?.();
    const text = slot
      ?.map((vnode) =>
        typeof vnode.children === "string" ? vnode.children : ""
      )
      .join("") ?? "";
    if (!text) return "";
    return DOMPurify.sanitize(marked.parse(text) as string);
  });
  </script>

  <template>
    <div class="markdown-content" v-html="html" />
  </template>
  ```

  ```svelte Svelte theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  <script lang="ts">
    import { marked } from "marked";
    import DOMPurify from "dompurify";

    let { content }: { content: string } = $props();

    marked.setOptions({ gfm: true, breaks: true });

    let html = $derived.by(() => {
      if (!content) return "";
      return DOMPurify.sanitize(marked.parse(content) as string);
    });
  </script>

  <div class="markdown-content">
    {@html html}
  </div>
  ```

  ```ts Angular theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { Component, Input, computed, signal } from "@angular/core";
  import { marked } from "marked";
  import DOMPurify from "dompurify";

  marked.setOptions({ gfm: true, breaks: true });

  @Component({
    selector: "app-markdown",
    template: `<div class="markdown-content" [innerHTML]="html()"></div>`,
  })
  export class MarkdownComponent {
    @Input() set content(value: string) {
      this._content.set(value);
    }

    private _content = signal("");

    html = computed(() => {
      const text = this._content();
      if (!text) return "";
      return DOMPurify.sanitize(marked.parse(text) as string);
    });
  }
  ```
</CodeGroup>

## Sanitizing HTML output

When rendering parsed markdown as raw HTML (`v-html`, `{@html}`, `[innerHTML]`),
you must sanitize the output to prevent cross-site scripting (XSS). LLM
responses may contain arbitrary text, including markup that a markdown parser
could turn into executable HTML.

Use `dompurify` to strip dangerous elements:

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import DOMPurify from "dompurify";

const safeHtml = DOMPurify.sanitize(rawHtml);
```

DOMPurify removes `<script>` tags, `onclick` attributes, `javascript:` URLs,
and other XSS vectors while preserving safe markdown output like headings,
lists, code blocks, tables, and links.

<Note>
  React's `react-markdown` does not need `dompurify` because it produces React
  elements directly, no raw HTML injection is involved.
</Note>

## Streaming considerations

`useStream` updates `msg.text` reactively as each token arrives. The markdown
component re-parses on every update. For typical chat messages, this is
performant:

* `marked` parses at \~1 MB/s. A 5 KB message takes \< 5ms
* `react-markdown` + remark pipeline is similarly fast for chat-length content
* The browser's layout engine handles the DOM update efficiently

For very long responses (> 50 KB), consider these optimizations:

* **Throttle renders:** use `requestAnimationFrame` to batch updates at 60fps
  instead of re-rendering on every token
* **Incremental parsing:** parse only new content and append to a rendered
  buffer (advanced, typically not needed for chat UIs)

<Info>
  For most chat applications, the simple approach of re-parsing the full message
  on each token is sufficient. Only optimize if you observe janky scrolling or
  dropped frames with very long messages.
</Info>

## Best practices

* **Always sanitize:** when using `v-html`, `{@html}`, or `[innerHTML]`,
  always run the parsed output through `dompurify`. Never trust raw HTML from a
  markdown parser fed with LLM output.
* **Enable GFM:** GitHub Flavored Markdown adds tables, strikethrough, task
  lists, and autolinks. These features are commonly used by LLMs.
* **Handle empty content:** check for empty strings before parsing to avoid
  rendering empty containers.
* **Use `breaks: true`:** enable line break conversion so single newlines in
  LLM output render as `<br>` rather than being ignored. LLMs often use single
  newlines for visual separation.
* **Style for chat context:** use compact margins and sizes appropriate for
  chat bubbles, not full-width article layouts.
* **Test with rich content:** verify rendering with headings, nested lists,
  code blocks with long lines, wide tables, and blockquotes to catch overflow
  or layout issues.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langchain/frontend/markdown-messages.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
