# Custom workflow
Source: https://docs.langchain.com/oss/javascript/langchain/multi-agent/custom-workflow

In the **custom workflow** architecture, you define your own bespoke execution flow using [LangGraph](/oss/javascript/langgraph/overview). You have complete control over the graph structure—including sequential steps, conditional branches, loops, and parallel execution.

```mermaid theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
graph LR
    A([Input]) --> B{{Conditional}}
    B -->|path_a| C[Deterministic step]
    B -->|path_b| D((Agentic step))
    C --> G([Output])
    D --> G([Output])

    classDef trigger fill:#F6FFDB,stroke:#6E8900,stroke-width:2px,color:#2E3900
    classDef process fill:#E5F4FF,stroke:#006DDD,stroke-width:2px,color:#030710
    classDef decision fill:#FDF3FF,stroke:#7E65AE,stroke-width:2px,color:#504B5F

    class A,G trigger
    class C,D process
    class B decision
```

## Key characteristics

* Complete control over graph structure
* Mix deterministic logic with agentic behavior
* Support for sequential steps, conditional branches, loops, and parallel execution
* Embed other patterns as nodes in your workflow

## When to use

Use custom workflows when standard patterns (subagents, skills, etc.) don't fit your requirements, you need to mix deterministic logic with agentic behavior, or your use case requires complex routing or multi-stage processing.

Each node in your workflow can be a simple function, an LLM call, or an entire [agent](/oss/javascript/langchain/agents) with [tools](/oss/javascript/langchain/tools). You can also compose other architectures within a custom workflow—for example, embedding a multi-agent system as a single node.

For a complete example of a custom workflow, see the tutorial below.

<Card title="Tutorial: Build a multi-source knowledge base with routing" icon="book" href="/oss/javascript/langchain/multi-agent/router-knowledge-base">
  The [router pattern](/oss/javascript/langchain/multi-agent/router) is an example of a custom workflow. This tutorial walks through building a router that queries GitHub, Notion, and Slack in parallel, then synthesizes results.

  >
</Card>

## Basic implementation

The core insight is that you can call a LangChain agent directly inside any LangGraph node, combining the flexibility of custom workflows with the convenience of prebuilt agents:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { z } from "zod";
import { createAgent } from "langchain";
import { StateGraph, START, END, StateSchema, MessagesValue } from "@langchain/langgraph";

const agent = createAgent({ model: "openai:gpt-4o", tools: [...] });

const AgentState = new StateSchema({
  messages: MessagesValue,
  query: z.string(),
});

const agentNode: GraphNode<typeof AgentState> = (state) => {
  // A LangGraph node that invokes a LangChain agent
  const result = await agent.invoke({
    messages: [{ role: "user", content: state.query }]
  });
  return { answer: result.messages.at(-1)?.content };
}

// Build a simple workflow
const workflow = new StateGraph(State)
  .addNode("agent", agentNode)
  .addEdge(START, "agent")
  .addEdge("agent", END)
  .compile();
```

## Example: RAG pipeline

A common use case is combining [retrieval](/oss/javascript/langchain/retrieval) with an agent. This example builds a WNBA stats assistant that retrieves from a knowledge base and can fetch live news.

<Accordion title="Custom RAG workflow">
  The workflow demonstrates three types of nodes:

  * **Model node** (Rewrite): Rewrites the user query for better retrieval using [structured output](/oss/javascript/langchain/structured-output).
  * **Deterministic node** (Retrieve): Performs vector similarity search — no LLM involved.
  * **Agent node** (Agent): Reasons over retrieved context and can fetch additional information via tools.

  ```mermaid theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  graph LR
      A([Query]) --> B{{Rewrite}}
      B --> C[(Retrieve)]
      C --> D((Agent))
      D --> E([Response])

      classDef trigger fill:#F6FFDB,stroke:#6E8900,stroke-width:2px,color:#2E3900
      classDef process fill:#E5F4FF,stroke:#006DDD,stroke-width:2px,color:#030710

      class A,E trigger
      class B,C,D process
  ```

  <Tip>
    You can use LangGraph state to pass information between workflow steps. This allows each part of your workflow to read and update structured fields, making it easy to share data and context across nodes.
  </Tip>

  ```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { StateGraph, Annotation, START, END } from "@langchain/langgraph";
  import { createAgent, tool } from "langchain";
  import { ChatOpenAI, OpenAIEmbeddings } from "@langchain/openai";
  import { MemoryVectorStore } from "@langchain/classic/vectorstores/memory";
  import * as z from "zod";

  const State = Annotation.Root({
    question: Annotation<string>(),
    rewrittenQuery: Annotation<string>(),
    documents: Annotation<string[]>(),
    answer: Annotation<string>(),
  });

  // WNBA knowledge base with rosters, game results, and player stats
  const embeddings = new OpenAIEmbeddings();
  const vectorStore = await MemoryVectorStore.fromTexts(
    [
      // Rosters
      "New York Liberty 2024 roster: Breanna Stewart, Sabrina Ionescu, Jonquel Jones, Courtney Vandersloot.",
      "Las Vegas Aces 2024 roster: A'ja Wilson, Kelsey Plum, Jackie Young, Chelsea Gray.",
      "Indiana Fever 2024 roster: Caitlin Clark, Aliyah Boston, Kelsey Mitchell, NaLyssa Smith.",
      // Game results
      "2024 WNBA Finals: New York Liberty defeated Minnesota Lynx 3-2 to win the championship.",
      "June 15, 2024: Indiana Fever 85, Chicago Sky 79. Caitlin Clark had 23 points and 8 assists.",
      "August 20, 2024: Las Vegas Aces 92, Phoenix Mercury 84. A'ja Wilson scored 35 points.",
      // Player stats
      "A'ja Wilson 2024 season stats: 26.9 PPG, 11.9 RPG, 2.6 BPG. Won MVP award.",
      "Caitlin Clark 2024 rookie stats: 19.2 PPG, 8.4 APG, 5.7 RPG. Won Rookie of the Year.",
      "Breanna Stewart 2024 stats: 20.4 PPG, 8.5 RPG, 3.5 APG.",
    ],
    [{}, {}, {}, {}, {}, {}, {}, {}, {}],
    embeddings
  );
  const retriever = vectorStore.asRetriever({ k: 5 });

  const getLatestNews = tool(
    async ({ query }) => {
      // Your news API here
      return "Latest: The WNBA announced expanded playoff format for 2025...";
    },
    {
      name: "get_latest_news",
      description: "Get the latest WNBA news and updates",
      schema: z.object({ query: z.string() }),
    }
  );

  const agent = createAgent({
    model: "openai:gpt-5.5",
    tools: [getLatestNews],
  });

  const model = new ChatOpenAI({ model: "gpt-5.5" });

  const RewrittenQuery = z.object({ query: z.string() });

  async function rewriteQuery(state: typeof State.State) {
    const systemPrompt = `Rewrite this query to retrieve relevant WNBA information.
  The knowledge base contains: team rosters, game results with scores, and player statistics (PPG, RPG, APG).
  Focus on specific player names, team names, or stat categories mentioned.`;
    const response = await model.withStructuredOutput(RewrittenQuery).invoke([
      { role: "system", content: systemPrompt },
      { role: "user", content: state.question },
    ]);
    return { rewrittenQuery: response.query };
  }

  async function retrieve(state: typeof State.State) {
    const docs = await retriever.invoke(state.rewrittenQuery);
    return { documents: docs.map((doc) => doc.pageContent) };
  }

  async function callAgent(state: typeof State.State) {
    const context = state.documents.join("\n\n");
    const prompt = `Context:\n${context}\n\nQuestion: ${state.question}`;
    const response = await agent.invoke({
      messages: [{ role: "user", content: prompt }],
    });
    return { answer: response.messages.at(-1)?.contentBlocks };
  }

  const workflow = new StateGraph(State)
    .addNode("rewrite", rewriteQuery)
    .addNode("retrieve", retrieve)
    .addNode("agent", callAgent)
    .addEdge(START, "rewrite")
    .addEdge("rewrite", "retrieve")
    .addEdge("retrieve", "agent")
    .addEdge("agent", END)
    .compile();

  const result = await workflow.invoke({
    question: "Who won the 2024 WNBA Championship?",
  });
  console.log(result.answer);
  ```
</Accordion>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langchain/multi-agent/custom-workflow.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Handoffs
Source: https://docs.langchain.com/oss/javascript/langchain/multi-agent/handoffs

In the **handoffs** architecture, behavior changes dynamically based on state. The core mechanism: [tools](/oss/javascript/langchain/tools) update a state variable (e.g., `current_step` or `active_agent`) that persists across turns, and the system reads this variable to adjust behavior—either applying different configuration (system prompt, tools) or routing to a different [agent](/oss/javascript/langchain/agents). This pattern supports both handoffs between distinct agents and dynamic configuration changes within a single agent.

<Tip>
  The term **handoffs** was coined by [OpenAI](https://openai.github.io/openai-agents-python/handoffs/) for using tool calls (e.g., `transfer_to_sales_agent`) to transfer control between agents or states.
</Tip>

```mermaid theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
sequenceDiagram
    participant User
    participant Agent
    participant Workflow State

    User->>Agent: "My phone is broken"
    Note over Agent,Workflow State: Step: Get warranty status<br/>Tools: record_warranty_status
    Agent-->>User: "Is your device under warranty?"

    User->>Agent: "Yes, it's still under warranty"
    Agent->>Workflow State: record_warranty_status("in_warranty")
    Note over Agent,Workflow State: Step: Classify issue<br/>Tools: record_issue_type
    Agent-->>User: "Can you describe the issue?"

    User->>Agent: "The screen is cracked"
    Agent->>Workflow State: record_issue_type("hardware")
    Note over Agent,Workflow State: Step: Provide resolution<br/>Tools: provide_solution, escalate_to_human
    Agent-->>User: "Here's the warranty repair process..."
```

## Key characteristics

* State-driven behavior: Behavior changes based on a state variable (e.g., `current_step` or `active_agent`)
* Tool-based transitions: Tools update the state variable to move between states
* Direct user interaction: Each state's configuration handles user messages directly
* Persistent state: State survives across conversation turns

## When to use

Use the handoffs pattern when you need to enforce sequential constraints (unlock capabilities only after preconditions are met), the agent needs to converse directly with the user across different states, or you're building multi-stage conversational flows. This pattern is particularly valuable for customer support scenarios where you need to collect information in a specific sequence—for example, collecting a warranty ID before processing a refund.

## Basic implementation

The core mechanism is a [tool](/oss/javascript/langchain/tools) that returns a [`Command`](/oss/javascript/langgraph/graph-api#command) to update state, triggering a transition to a new step or agent:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { tool, ToolMessage, type ToolRuntime } from "langchain";
import { Command } from "@langchain/langgraph";
import { z } from "zod";

const transferToSpecialist = tool(
  async (_, config: ToolRuntime<typeof StateSchema>) => {
    return new Command({
      update: {
        messages: [
          new ToolMessage({  // [!code highlight]
            content: "Transferred to specialist",
            tool_call_id: config.toolCallId  // [!code highlight]
          })
        ],
        currentStep: "specialist"  // Triggers behavior change
      }
    });
  },
  {
    name: "transfer_to_specialist",
    description: "Transfer to the specialist agent.",
    schema: z.object({})
  }
);
```

<Note>
  **Why include a `ToolMessage`?** When an LLM calls a tool, it expects a response. The `ToolMessage` with matching `tool_call_id` completes this request-response cycle—without it, the conversation history becomes malformed. This is required whenever your handoff tool updates messages.
</Note>

For a complete implementation, see the tutorial below.

<Card title="Tutorial: Build customer support with handoffs" icon="users" href="/oss/javascript/langchain/multi-agent/handoffs-customer-support">
  Learn how to build a customer support agent using the handoffs pattern, where a single agent transitions between different configurations.
</Card>

## Implementation approaches

There are two ways to implement handoffs: **[single agent with middleware](#single-agent-with-middleware)** (one agent with dynamic configuration) or **[multiple agent subgraphs](#multiple-agent-subgraphs)** (distinct agents as graph nodes).

### Single agent with middleware

A single agent changes its behavior based on state. Middleware intercepts each model call and dynamically adjusts the system prompt and available tools. Tools update the state variable to trigger transitions:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { tool, ToolMessage, type ToolRuntime } from "langchain";
import { Command } from "@langchain/langgraph";
import { z } from "zod";

const recordWarrantyStatus = tool(
  async ({ status }, config: ToolRuntime<typeof StateSchema>) => {
    return new Command({
      update: {
        messages: [
          new ToolMessage({
            content: `Warranty status recorded: ${status}`,
            tool_call_id: config.toolCallId,
          }),
        ],
        warrantyStatus: status,
        currentStep: "specialist", // Update state to trigger transition
      },
    });
  },
  {
    name: "record_warranty_status",
    description: "Record warranty status and transition to next step.",
    schema: z.object({
      status: z.string(),
    }),
  }
);
```

<Accordion title="Complete example: Customer support with middleware">
  ```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import {
    createAgent,
    createMiddleware,
    tool,
    ToolMessage,
    type ToolRuntime,
  } from "langchain";
  import { Command, MemorySaver, StateSchema } from "@langchain/langgraph";
  import { z } from "zod";

  // 1. Define state with current_step tracker
  const SupportState = new StateSchema({ // [!code highlight]
    currentStep: z.string().default("triage"), // [!code highlight]
    warrantyStatus: z.string().optional(),
  });

  // 2. Tools update currentStep via Command
  const recordWarrantyStatus = tool(
    async ({ status }, config: ToolRuntime<typeof SupportState.State>) => {
      return new Command({ // [!code highlight]
        update: { // [!code highlight]
          messages: [ // [!code highlight]
            new ToolMessage({
              content: `Warranty status recorded: ${status}`,
              tool_call_id: config.toolCallId,
            }),
          ],
          warrantyStatus: status,
          // Transition to next step
          currentStep: "specialist", // [!code highlight]
        },
      });
    },
    {
      name: "record_warranty_status",
      description: "Record warranty status and transition",
      schema: z.object({ status: z.string() }),
    }
  );

  // 3. Middleware applies dynamic configuration based on currentStep
  const applyStepConfig = createMiddleware({
    name: "applyStepConfig",
    stateSchema: SupportState, // [!code highlight]
    wrapModelCall: async (request, handler) => {
      const step = request.state.currentStep || "triage"; // [!code highlight]

      // Map steps to their configurations
      const configs = {
        triage: {
          prompt: "Collect warranty information...",
          tools: [recordWarrantyStatus],
        },
        specialist: {
          prompt: `Provide solutions based on warranty: ${request.state.warrantyStatus}`,
          tools: [provideSolution, escalate],
        },
      };

      const config = configs[step as keyof typeof configs];
      return handler({
        ...request,
        systemPrompt: config.prompt,
        tools: config.tools,
      });
    },
  });

  // 4. Create agent with middleware
  const agent = createAgent({
    model,
    tools: [recordWarrantyStatus, provideSolution, escalate],
    middleware: [applyStepConfig], // [!code highlight]
    checkpointer: new MemorySaver(), // Persist state across turns  // [!code highlight]
  });
  ```
</Accordion>

### Multiple agent subgraphs

Multiple distinct agents exist as separate nodes in a graph. Handoff tools navigate between agent nodes using `Command.PARENT` to specify which node to execute next.

<Warning>
  Subgraph handoffs require careful **[context engineering](/oss/javascript/langchain/context-engineering)**. Unlike single-agent middleware (where message history flows naturally), you must explicitly decide what messages pass between agents. Get this wrong and agents receive malformed conversation history or bloated context. See [Context engineering](#context-engineering) below.
</Warning>

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import {
  tool,
  ToolMessage,
  AIMessage,
  type ToolRuntime,
} from "langchain";
import { Command, StateSchema, MessagesValue } from "@langchain/langgraph";

const CustomState = new StateSchema({
  messages: MessagesValue,
});

const transferToSales = tool(
  async (_, runtime: ToolRuntime<typeof CustomState.State>) => {
    const lastAiMessage = runtime.state.messages // [!code highlight]
      .reverse() // [!code highlight]
      .find(AIMessage.isInstance); // [!code highlight]

    const transferMessage = new ToolMessage({ // [!code highlight]
      content: "Transferred to sales agent", // [!code highlight]
      tool_call_id: runtime.toolCallId, // [!code highlight]
    }); // [!code highlight]
    return new Command({
      goto: "sales_agent",
      update: {
        activeAgent: "sales_agent",
        messages: [lastAiMessage, transferMessage].filter(Boolean), // [!code highlight]
      },
      graph: Command.PARENT,
    });
  },
  {
    name: "transfer_to_sales",
    description: "Transfer to the sales agent.",
    schema: z.object({}),
  }
);
```

<Accordion title="Complete example: Sales and support with handoffs">
  This example shows a multi-agent system with separate sales and support agents. Each agent is a separate graph node, and handoff tools allow agents to transfer conversations to each other.

  ```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import {
    StateGraph,
    START,
    END,
    StateSchema,
    MessagesValue,
    Command,
    ConditionalEdgeRouter,
    GraphNode,
  } from "@langchain/langgraph";
  import { createAgent, AIMessage, ToolMessage } from "langchain";
  import { tool, ToolRuntime } from "@langchain/core/tools";
  import { z } from "zod/v4";

  // 1. Define state with active_agent tracker
  const MultiAgentState = new StateSchema({
    messages: MessagesValue,
    activeAgent: z.string().optional(),
  });

  // 2. Create handoff tools
  const transferToSales = tool(
    async (_, runtime: ToolRuntime<typeof MultiAgentState.State>) => {
      const lastAiMessage = [...runtime.state.messages] // [!code highlight]
        .reverse() // [!code highlight]
        .find(AIMessage.isInstance); // [!code highlight]
      const transferMessage = new ToolMessage({ // [!code highlight]
        content: "Transferred to sales agent from support agent", // [!code highlight]
        tool_call_id: runtime.toolCallId, // [!code highlight]
      }); // [!code highlight]
      return new Command({
        goto: "sales_agent",
        update: {
          activeAgent: "sales_agent",
          messages: [lastAiMessage, transferMessage].filter(Boolean), // [!code highlight]
        },
        graph: Command.PARENT,
      });
    },
    {
      name: "transfer_to_sales",
      description: "Transfer to the sales agent.",
      schema: z.object({}),
    }
  );

  const transferToSupport = tool(
    async (_, runtime: ToolRuntime<typeof MultiAgentState.State>) => {
      const lastAiMessage = [...runtime.state.messages] // [!code highlight]
        .reverse() // [!code highlight]
        .find(AIMessage.isInstance); // [!code highlight]
      const transferMessage = new ToolMessage({ // [!code highlight]
        content: "Transferred to support agent from sales agent", // [!code highlight]
        tool_call_id: runtime.toolCallId, // [!code highlight]
      }); // [!code highlight]
      return new Command({
        goto: "support_agent",
        update: {
          activeAgent: "support_agent",
          messages: [lastAiMessage, transferMessage].filter(Boolean), // [!code highlight]
        },
        graph: Command.PARENT,
      });
    },
    {
      name: "transfer_to_support",
      description: "Transfer to the support agent.",
      schema: z.object({}),
    }
  );

  // 3. Create agents with handoff tools
  const salesAgent = createAgent({
    model: "google_genai:gemini-3.5-flash",
    tools: [transferToSupport],
    systemPrompt:
      "You are a sales agent. Help with sales inquiries. If asked about technical issues or support, transfer to the support agent.",
  });

  const supportAgent = createAgent({
    model: "google_genai:gemini-3.5-flash",
    tools: [transferToSales],
    systemPrompt:
      "You are a support agent. Help with technical issues. If asked about pricing or purchasing, transfer to the sales agent.",
  });

  // 4. Create agent nodes that invoke the agents
  const callSalesAgent: GraphNode<typeof MultiAgentState.State> = async (state) => {
    const response = await salesAgent.invoke(state);
    return response;
  };

  const callSupportAgent: GraphNode<typeof MultiAgentState.State> = async (state) => {
    const response = await supportAgent.invoke(state);
    return response;
  };

  // 5. Create router that checks if we should end or continue
  const routeAfterAgent: ConditionalEdgeRouter<
    typeof MultiAgentState.State,
    "sales_agent" | "support_agent"
  > = (state) => {
    const messages = state.messages ?? [];

    // Check the last message - if it's an AIMessage without tool calls, we're done
    if (messages.length > 0) {
      const lastMsg = messages[messages.length - 1];
      if (lastMsg instanceof AIMessage && !lastMsg.tool_calls?.length) { // [!code highlight]
        return END; // [!code highlight]
      } // [!code highlight]
    }

    // Otherwise route to the active agent
    const active = state.activeAgent ?? "sales_agent";
    return active as "sales_agent" | "support_agent";
  };

  const routeInitial: ConditionalEdgeRouter<
    typeof MultiAgentState.State,
    "sales_agent" | "support_agent"
  > = (state) => {
    // Route to the active agent based on state, default to sales agent
    return (state.activeAgent ?? "sales_agent") as
      | "sales_agent"
      | "support_agent";
  };

  // 6. Build the graph
  const builder = new StateGraph(MultiAgentState)
    .addNode("sales_agent", callSalesAgent)
    .addNode("support_agent", callSupportAgent);
    // Start with conditional routing based on initial activeAgent
    .addConditionalEdges(START, routeInitial, [
      "sales_agent",
      "support_agent",
    ])
    // After each agent, check if we should end or route to another agent
    .addConditionalEdges("sales_agent", routeAfterAgent, [
      "sales_agent",
      "support_agent",
      END,
    ]);
    builder.addConditionalEdges("support_agent", routeAfterAgent, [
      "sales_agent",
      "support_agent",
      END,
    ]);

  const graph = builder.compile();
  const result = await graph.invoke({
    messages: [
      {
        role: "user",
        content: "Hi, I'm having trouble with my account login. Can you help?",
      },
    ],
  });

  for (const msg of result.messages) {
    console.log(msg.content);
  }
  ```
</Accordion>

<Tip>
  Use **single agent with middleware** for most handoffs use cases—it's simpler. Only use **multiple agent subgraphs** when you need bespoke agent implementations (e.g., a node that's itself a complex graph with reflection or retrieval steps).
</Tip>

#### Context engineering

With subgraph handoffs, you control exactly what messages flow between agents. This precision is essential for maintaining valid conversation history and avoiding context bloat that could confuse downstream agents. For more on this topic, see [context engineering](/oss/javascript/langchain/context-engineering).

**Handling context during handoffs**

When handing off between agents, you need to ensure the conversation history remains valid. LLMs expect tool calls to be paired with their responses, so when using `Command.PARENT` to hand off to another agent, you must include both:

1. **The `AIMessage` containing the tool call** (the message that triggered the handoff)
2. **A `ToolMessage` acknowledging the handoff** (the artificial response to that tool call)

Without this pairing, the receiving agent will see an incomplete conversation and may produce errors or unexpected behavior.

The example below assumes only the handoff tool was called (no parallel tool calls):

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const transferToSales = tool(
  async (_, runtime: ToolRuntime<typeof MultiAgentState.State>) => {
    // Get the AI message that triggered this handoff
    const lastAiMessage = runtime.state.messages.at(-1);

    // Create an artificial tool response to complete the pair
    const transferMessage = new ToolMessage({
      content: "Transferred to sales agent",
      tool_call_id: runtime.toolCallId,
    });

    return new Command({
      goto: "sales_agent",
      update: {
        activeAgent: "sales_agent",
        // Pass only these two messages, not the full subagent history
        messages: [lastAiMessage, transferMessage],
      },
      graph: Command.PARENT,
    });
  },
  {
    name: "transfer_to_sales",
    description: "Transfer to the sales agent.",
    schema: z.object({}),
  }
);
```

<Note>
  **Why not pass all subagent messages?** While you could include the full subagent conversation in the handoff, this often creates problems. The receiving agent may become confused by irrelevant internal reasoning, and token costs increase unnecessarily. By passing only the handoff pair, you keep the parent graph's context focused on high-level coordination. If the receiving agent needs additional context, consider summarizing the subagent's work in the ToolMessage content instead of passing raw message history.
</Note>

**Returning control to the user**

When returning control to the user (ending the agent's turn), ensure the final message is an `AIMessage`. This maintains valid conversation history and signals to the user interface that the agent has finished its work.

## Implementation considerations

As you design your multi-agent system, consider:

* **Context filtering strategy**: Will each agent receive full conversation history, filtered portions, or summaries? Different agents may need different context depending on their role.
* **Tool semantics**: Clarify whether handoff tools only update routing state or also perform side effects. For example, should `transfer_to_sales()` also create a support ticket, or should that be a separate action?
* **Token efficiency**: Balance context completeness against token costs. Summarization and selective context passing become more important as conversations grow longer.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langchain/multi-agent/handoffs.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
