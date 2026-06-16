# Multi-agent
Source: https://docs.langchain.com/oss/javascript/langchain/multi-agent/index

Multi-agent systems coordinate specialized components to tackle complex workflows. However, not every complex task requires this approach—a single agent with the right (sometimes dynamic) tools and prompt can often achieve similar results.

<Tip>
  For built-in multi-agent support, use [Deep Agents](/oss/javascript/deepagents/overview): a higher-level harness built on LangChain that ships with [subagents](/oss/javascript/deepagents/subagents), [skills](/oss/javascript/deepagents/skills), planning, a virtual filesystem, and context management.
</Tip>

## Why multi-agent?

When developers say they need "multi-agent," they're usually looking for one or more of these capabilities:

* <Icon icon="brain" /> **Context management**: Provide specialized knowledge without overwhelming the model's context window. If context were infinite and latency zero, you could dump all knowledge into a single prompt—but since it's not, you need patterns to selectively surface relevant information.
* <Icon icon="users" /> **Distributed development**: Allow different teams to develop and maintain capabilities independently, composing them into a larger system with clear boundaries.
* <Icon icon="git-branch" /> **Parallelization**: Spawn specialized workers for subtasks and execute them concurrently for faster results.

Multi-agent patterns are particularly valuable when a single agent has too many [tools](/oss/javascript/langchain/tools) and makes poor decisions about which to use, when tasks require specialized knowledge with extensive context (long prompts and domain-specific tools), or when you need to enforce sequential constraints that unlock capabilities only after certain conditions are met.

<Tip>
  At the center of multi-agent design is **[context engineering](/oss/javascript/langchain/context-engineering)**—deciding what information each agent sees. The quality of your system depends on ensuring each agent has access to the right data for its task.
</Tip>

## Patterns

Here are the main patterns for building multi-agent systems, each suited to different use cases:

| Pattern                                                                      | How it works                                                                                                                                                                                        |
| ---------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [**Subagents**](/oss/javascript/langchain/multi-agent/subagents)             | A main agent coordinates subagents as tools. All routing passes through the main agent, which decides when and how to invoke each subagent.                                                         |
| [**Handoffs**](/oss/javascript/langchain/multi-agent/handoffs)               | Behavior changes dynamically based on state. Tool calls update a state variable that triggers routing or configuration changes, switching agents or adjusting the current agent's tools and prompt. |
| [**Skills**](/oss/javascript/langchain/multi-agent/skills)                   | Specialized prompts and knowledge loaded on-demand. A single agent stays in control while loading context from skills as needed.                                                                    |
| [**Router**](/oss/javascript/langchain/multi-agent/router)                   | A routing step classifies input and directs it to one or more specialized agents. Results are synthesized into a combined response.                                                                 |
| [**Custom workflow**](/oss/javascript/langchain/multi-agent/custom-workflow) | Build bespoke execution flows with [LangGraph](/oss/javascript/langgraph/overview), mixing deterministic logic and agentic behavior. Embed other patterns as nodes in your workflow.                |

### Choosing a pattern

Use this table to match your requirements to the right pattern:

<div>
  | Pattern                                                          | Distributed development | Parallelization | Multi-hop | Direct user interaction |
  | ---------------------------------------------------------------- | :---------------------: | :-------------: | :-------: | :---------------------: |
  | [**Subagents**](/oss/javascript/langchain/multi-agent/subagents) |          ⭐⭐⭐⭐⭐          |      ⭐⭐⭐⭐⭐      |   ⭐⭐⭐⭐⭐   |            ⭐            |
  | [**Handoffs**](/oss/javascript/langchain/multi-agent/handoffs)   |            -            |        -        |   ⭐⭐⭐⭐⭐   |          ⭐⭐⭐⭐⭐          |
  | [**Skills**](/oss/javascript/langchain/multi-agent/skills)       |          ⭐⭐⭐⭐⭐          |       ⭐⭐⭐       |   ⭐⭐⭐⭐⭐   |          ⭐⭐⭐⭐⭐          |
  | [**Router**](/oss/javascript/langchain/multi-agent/router)       |           ⭐⭐⭐           |      ⭐⭐⭐⭐⭐      |     -     |           ⭐⭐⭐           |
</div>

* **Distributed development**: Can different teams maintain components independently?
* **Parallelization**: Can multiple agents execute concurrently?
* **Multi-hop**: Does the pattern support calling multiple subagents in series?
* **Direct user interaction**: Can subagents converse directly with the user?

<Tip>
  You can mix patterns! For example, a **subagents** architecture can invoke tools that invoke custom workflows or router agents. Subagents can even use the **skills** pattern to load context on-demand. The possibilities are endless!
</Tip>

### Visual overview

<Tabs>
  <Tab title="Subagents">
    A main agent coordinates subagents as tools. All routing passes through the main agent.

    <Frame>
      <img alt="Subagents pattern: main agent coordinates subagents as tools" />
    </Frame>
  </Tab>

  <Tab title="Handoffs">
    Agents transfer control to each other via tool calls. Each agent can hand off to others or respond directly to the user.

    <Frame>
      <img alt="Handoffs pattern: agents transfer control via tool calls" />
    </Frame>
  </Tab>

  <Tab title="Skills">
    A single agent loads specialized prompts and knowledge on-demand while staying in control.

    <Frame>
      <img alt="Skills pattern: single agent loads specialized context on-demand" />
    </Frame>
  </Tab>

  <Tab title="Router">
    A routing step classifies input and directs it to specialized agents. Results are synthesized.

    <Frame>
      <img alt="Router pattern: routing step classifies input to specialized agents" />
    </Frame>
  </Tab>
</Tabs>

<Tip>
  Trace the full coordination flow across agents with [LangSmith](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=oss-langchain-multi-agent-index). Follow the [tracing quickstart](/langsmith/trace-with-langchain) to get set up.

  We recommend you also set up [LangSmith Engine](/langsmith/engine) which monitors your traces, detects issues, and proposes fixes.
</Tip>

## Performance comparison

Different patterns have different performance characteristics. Understanding these tradeoffs helps you choose the right pattern for your latency and cost requirements.

**Key metrics:**

* **Model calls**: Number of LLM invocations. More calls = higher latency (especially if sequential) and higher per-request API costs.
* **Tokens processed**: Total [context window](/oss/javascript/langchain/context-engineering) usage across all calls. More tokens = higher processing costs and potential context limits.

### One-shot request

> **User:** "Buy coffee"

A specialized coffee agent/skill can call a `buy_coffee` tool.

| Pattern                                                          | Model calls | Best fit |
| ---------------------------------------------------------------- | :---------: | :------: |
| [**Subagents**](/oss/javascript/langchain/multi-agent/subagents) |      4      |          |
| [**Handoffs**](/oss/javascript/langchain/multi-agent/handoffs)   |      3      |     ✅    |
| [**Skills**](/oss/javascript/langchain/multi-agent/skills)       |      3      |     ✅    |
| [**Router**](/oss/javascript/langchain/multi-agent/router)       |      3      |     ✅    |

<Tabs>
  <Tab title="Subagents">
    **4 model calls:**

    <Frame>
      <img alt="Subagents one-shot: 4 model calls for buy coffee request" />
    </Frame>
  </Tab>

  <Tab title="Handoffs">
    **3 model calls:**

    <Frame>
      <img alt="Handoffs one-shot: 3 model calls for buy coffee request" />
    </Frame>
  </Tab>

  <Tab title="Skills">
    **3 model calls:**

    <Frame>
      <img alt="Skills one-shot: 3 model calls for buy coffee request" />
    </Frame>
  </Tab>

  <Tab title="Router">
    **3 model calls:**

    <Frame>
      <img alt="Router one-shot: 3 model calls for buy coffee request" />
    </Frame>
  </Tab>
</Tabs>

**Key insight:** Handoffs, Skills, and Router are most efficient for single tasks (3 calls each). Subagents adds one extra call because results flow back through the main agent—this overhead provides centralized control.

### Repeat request

> **Turn 1:** "Buy coffee"
> **Turn 2:** "Buy coffee again"

The user repeats the same request in the same conversation.

<div>
  | Pattern                                                          | Turn 2 calls | Total (both turns) | Best fit |
  | ---------------------------------------------------------------- | :----------: | :----------------: | :------: |
  | [**Subagents**](/oss/javascript/langchain/multi-agent/subagents) |       4      |          8         |          |
  | [**Handoffs**](/oss/javascript/langchain/multi-agent/handoffs)   |       2      |          5         |     ✅    |
  | [**Skills**](/oss/javascript/langchain/multi-agent/skills)       |       2      |          5         |     ✅    |
  | [**Router**](/oss/javascript/langchain/multi-agent/router)       |       3      |          6         |          |
</div>

<Tabs>
  <Tab title="Subagents">
    **4 calls again → 8 total**

    * Subagents are **stateless by design**—each invocation follows the same flow
    * The main agent maintains conversation context, but subagents start fresh each time
    * This provides strong context isolation but repeats the full flow
  </Tab>

  <Tab title="Handoffs">
    **2 calls → 5 total**

    * The coffee agent is **still active** from turn 1 (state persists)
    * No handoff needed—agent directly calls `buy_coffee` tool (call 1)
    * Agent responds to user (call 2)
    * **Saves 1 call by skipping the handoff**
  </Tab>

  <Tab title="Skills">
    **2 calls → 5 total**

    * The skill context is **already loaded** in conversation history
    * No need to reload—agent directly calls `buy_coffee` tool (call 1)
    * Agent responds to user (call 2)
    * **Saves 1 call by reusing loaded skill**
  </Tab>

  <Tab title="Router">
    **3 calls again → 6 total**

    * Routers are **stateless**—each request requires an LLM routing call
    * Turn 2: Router LLM call (1) → Milk agent calls buy\_coffee (2) → Milk agent responds (3)
    * Can be optimized by wrapping as a tool in a stateful agent
  </Tab>
</Tabs>

**Key insight:** Stateful patterns (Handoffs, Skills) save 40-50% of calls on repeat requests. Subagents maintain consistent cost per request—this stateless design provides strong context isolation but at the cost of repeated model calls.

### Multi-domain

> **User:** "Compare Python, JavaScript, and Rust for web development"

Each language agent/skill contains \~2000 tokens of documentation. All patterns can make parallel tool calls.

| Pattern                                                          | Model calls | Total tokens | Best fit |
| ---------------------------------------------------------------- | :---------: | :----------: | :------: |
| [**Subagents**](/oss/javascript/langchain/multi-agent/subagents) |      5      |     \~9K     |     ✅    |
| [**Handoffs**](/oss/javascript/langchain/multi-agent/handoffs)   |      7+     |    \~14K+    |          |
| [**Skills**](/oss/javascript/langchain/multi-agent/skills)       |      3      |     \~15K    |          |
| [**Router**](/oss/javascript/langchain/multi-agent/router)       |      5      |     \~9K     |     ✅    |

<Tabs>
  <Tab title="Subagents">
    **5 calls, \~9K tokens**

    <Frame>
      <img alt="Subagents multi-domain: 5 calls with parallel execution" />
    </Frame>

    Each subagent works in **isolation** with only its relevant context. Total: **9K tokens**.
  </Tab>

  <Tab title="Handoffs">
    **7+ calls, \~14K+ tokens**

    <Frame>
      <img alt="Handoffs multi-domain: 7+ sequential calls" />
    </Frame>

    Handoffs executes **sequentially**—can't research all three languages in parallel. Growing conversation history adds overhead. Total: **\~14K+ tokens**.
  </Tab>

  <Tab title="Skills">
    **3 calls, \~15K tokens**

    <Frame>
      <img alt="Skills multi-domain: 3 calls with accumulated context" />
    </Frame>

    After loading, **every subsequent call processes all 6K tokens of skill documentation**. Subagents processes 67% fewer tokens overall due to context isolation. Total: **15K tokens**.
  </Tab>

  <Tab title="Router">
    **5 calls, \~9K tokens**

    <Frame>
      <img alt="Router multi-domain: 5 calls with parallel execution" />
    </Frame>

    Router uses an **LLM for routing**, then invokes agents in parallel. Similar to Subagents but with explicit routing step. Total: **9K tokens**.
  </Tab>
</Tabs>

**Key insight:** For multi-domain tasks, patterns with parallel execution (Subagents, Router) are most efficient. Skills has fewer calls but high token usage due to context accumulation. Handoffs is inefficient here—it must execute sequentially and can't leverage parallel tool calling for consulting multiple domains simultaneously.

### Summary

Here's how patterns compare across all three scenarios:

<div>
  | Pattern                                                          | One-shot | Repeat request |      Multi-domain     |
  | ---------------------------------------------------------------- | :------: | :------------: | :-------------------: |
  | [**Subagents**](/oss/javascript/langchain/multi-agent/subagents) |  4 calls |  8 calls (4+4) |   5 calls, 9K tokens  |
  | [**Handoffs**](/oss/javascript/langchain/multi-agent/handoffs)   |  3 calls |  5 calls (3+2) | 7+ calls, 14K+ tokens |
  | [**Skills**](/oss/javascript/langchain/multi-agent/skills)       |  3 calls |  5 calls (3+2) |  3 calls, 15K tokens  |
  | [**Router**](/oss/javascript/langchain/multi-agent/router)       |  3 calls |  6 calls (3+3) |   5 calls, 9K tokens  |
</div>

**Choosing a pattern:**

<div>
  | Optimize for          | [Subagents](/oss/javascript/langchain/multi-agent/subagents) | [Handoffs](/oss/javascript/langchain/multi-agent/handoffs) | [Skills](/oss/javascript/langchain/multi-agent/skills) | [Router](/oss/javascript/langchain/multi-agent/router) |
  | --------------------- | :----------------------------------------------------------: | :--------------------------------------------------------: | :----------------------------------------------------: | :----------------------------------------------------: |
  | Single requests       |                                                              |                              ✅                             |                            ✅                           |                            ✅                           |
  | Repeat requests       |                                                              |                              ✅                             |                            ✅                           |                                                        |
  | Parallel execution    |                               ✅                              |                                                            |                                                        |                            ✅                           |
  | Large-context domains |                               ✅                              |                                                            |                                                        |                            ✅                           |
  | Simple, focused tasks |                                                              |                                                            |                            ✅                           |                                                        |
</div>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langchain/multi-agent/index.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Router
Source: https://docs.langchain.com/oss/javascript/langchain/multi-agent/router

In the **router** architecture, a routing step classifies input and directs it to specialized [agents](/oss/javascript/langchain/agents). This is useful when you have distinct **verticals** (separate knowledge domains that each require their own agent).

```mermaid theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
graph LR
    A([Query]) --> B[Router]
    B --> C[Agent A]
    B --> D[Agent B]
    B --> E[Agent C]
    C --> F[Synthesize]
    D --> F
    E --> F
    F --> G([Combined answer])

    classDef trigger fill:#F6FFDB,stroke:#6E8900,stroke-width:2px,color:#2E3900
    classDef process fill:#E5F4FF,stroke:#006DDD,stroke-width:2px,color:#030710

    class A,G trigger
    class B,C,D,E,F process
```

## Key characteristics

* Router decomposes the query
* Zero or more specialized agents are invoked in parallel
* Results are synthesized into a coherent response

## When to use

Use the router pattern when you have distinct verticals (separate knowledge domains that each require their own agent), need to query multiple sources in parallel, and want to synthesize results into a combined response.

## Basic implementation

The router classifies the query and directs it to the appropriate agent(s). Use [`Command`](/oss/javascript/langgraph/graph-api#command) for single-agent routing or [`Send`](/oss/javascript/langgraph/graph-api#send) for parallel fan-out to multiple agents.

<Tabs>
  <Tab title="Single agent">
    Use `Command` to route to a single specialized agent:

    ```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    import { z } from "zod";
    import { Command } from "@langchain/langgraph";

    const ClassificationResult = z.object({
      query: z.string(),
      agent: z.string(),
    });

    function classifyQuery(query: string): z.infer<typeof ClassificationResult> {
      // Use LLM to classify query and determine the appropriate agent
      // Classification logic here
      ...
    }

    function routeQuery(state: z.infer<typeof ClassificationResult>) {
      const classification = classifyQuery(state.query);

      // Route to the selected agent
      return new Command({ goto: classification.agent });
    }
    ```
  </Tab>

  <Tab title="Multiple agents (parallel)">
    Use `Send` to fan out to multiple specialized agents in parallel:

    ```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    import { z } from "zod";
    import { Command } from "@langchain/langgraph";

    const ClassificationResult = z.object({
      query: z.string(),
      agent: z.string(),
    });

    function classifyQuery(query: string): z.infer<typeof ClassificationResult>[] {
      // Use LLM to classify query and determine the appropriate agent
      // Classification logic here
      ...
    }

    function routeQuery(state: typeof State.State) {
      const classifications = classifyQuery(state.query);

      // Fan out to selected agents in parallel
      return classifications.map(
        (c) => new Send(c.agent, { query: c.query })
      );
    }
    ```
  </Tab>
</Tabs>

For a complete implementation, see the tutorial below.

<Card title="Tutorial: Build a multi-source knowledge base with routing" icon="book" href="/oss/javascript/langchain/multi-agent/router-knowledge-base">
  Build a router that queries GitHub, Notion, and Slack in parallel, then synthesizes results into a coherent answer. Covers state definition, specialized agents, parallel execution with `Send`, and result synthesis.
</Card>

## Stateless vs. stateful

Two approaches:

* [**Stateless routers**](#stateless) address each request independently
* [**Stateful routers**](#stateful) maintain conversation history across requests

## Stateless

Each request is routed independently—no memory between calls. For multi-turn conversations, see [Stateful routers](#stateful).

<Tip>
  **Router vs. Subagents**: Both patterns can dispatch work to multiple agents, but they differ in how routing decisions are made:

  * **Router**: A dedicated routing step (often a single LLM call or rule-based logic) that classifies the input and dispatches to agents. The router itself typically doesn't maintain conversation history or perform multi-turn orchestration—it's a preprocessing step.
  * **Subagents**: An main supervisor agent dynamically decides which [subagents](/oss/javascript/langchain/multi-agent/subagents) to call as part of an ongoing conversation. The main agent maintains context, can call multiple subagents across turns, and orchestrates complex multi-step workflows.

  Use a **router** when you have clear input categories and want deterministic or lightweight classification. Use a **supervisor** when you need flexible, conversation-aware orchestration where the LLM decides what to do next based on evolving context.
</Tip>

## Stateful

For multi-turn conversations, you need to maintain context across invocations.

### Tool wrapper

The simplest approach: wrap the stateless router as a tool that a conversational agent can call. The conversational agent handles memory and context; the router stays stateless. This avoids the complexity of managing conversation history across multiple parallel agents.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const searchDocs = tool(
  async ({ query }) => {
    const result = await workflow.invoke({ query }); // [!code highlight]
    return result.finalAnswer;
  },
  {
    name: "search_docs",
    description: "Search across multiple documentation sources",
    schema: z.object({
      query: z.string().describe("The search query"),
    }),
  }
);

// Conversational agent uses the router as a tool
const conversationalAgent = createAgent({
  model,
  tools: [searchDocs],
  systemPrompt: "You are a helpful assistant. Use search_docs to answer questions.",
});
```

### Full persistence

If you need the router itself to maintain state, use [persistence](/oss/javascript/langchain/short-term-memory) to store message history. When routing to an agent, fetch previous messages from state and selectively include them in the agent's context—this is a lever for [context engineering](/oss/javascript/langchain/context-engineering).

<Warning>
  **Stateful routers require custom history management.** If the router switches between agents across turns, conversations may not feel fluid to end users when agents have different tones or prompts. With parallel invocation, you'll need to maintain history at the router level (inputs and synthesized outputs) and leverage this history in routing logic. Consider the [handoffs pattern](/oss/javascript/langchain/multi-agent/handoffs) or [subagents pattern](/oss/javascript/langchain/multi-agent/subagents) instead—both provide clearer semantics for multi-turn conversations.
</Warning>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langchain/multi-agent/router.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
