# Agent will call go_back_to_warranty and restart the warranty verification step
```

## Complete example

Here's everything together in a runnable script:

<Expandable title="Complete code">
  ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  """
  Customer Support State Machine Example

  This example demonstrates the state machine pattern.
  A single agent dynamically changes its behavior based on the current_step state,
  creating a state machine for sequential information collection.
  """

  from langchain_core.utils.uuid import uuid7

  from langgraph.checkpoint.memory import InMemorySaver
  from langgraph.types import Command
  from typing import Callable, Literal
  from typing_extensions import NotRequired

  from langchain.agents import AgentState, create_agent
  from langchain.agents.middleware import wrap_model_call, ModelRequest, ModelResponse, SummarizationMiddleware
  from langchain.chat_models import init_chat_model
  from langchain.messages import HumanMessage, ToolMessage
  from langchain.tools import tool, ToolRuntime

  model = init_chat_model("google_genai:gemini-3.5-flash")

  # Define the possible workflow steps
  SupportStep = Literal["warranty_collector", "issue_classifier", "resolution_specialist"]

  class SupportState(AgentState):
      """State for customer support workflow."""

      current_step: NotRequired[SupportStep]
      warranty_status: NotRequired[Literal["in_warranty", "out_of_warranty"]]
      issue_type: NotRequired[Literal["hardware", "software"]]

  @tool
  def record_warranty_status(
      status: Literal["in_warranty", "out_of_warranty"],
      runtime: ToolRuntime[None, SupportState],
  ) -> Command:
      """Record the customer's warranty status and transition to issue classification."""
      return Command(
          update={
              "messages": [
                  ToolMessage(
                      content=f"Warranty status recorded as: {status}",
                      tool_call_id=runtime.tool_call_id,
                  )
              ],
              "warranty_status": status,
              "current_step": "issue_classifier",
          }
      )

  @tool
  def record_issue_type(
      issue_type: Literal["hardware", "software"],
      runtime: ToolRuntime[None, SupportState],
  ) -> Command:
      """Record the type of issue and transition to resolution specialist."""
      return Command(
          update={
              "messages": [
                  ToolMessage(
                      content=f"Issue type recorded as: {issue_type}",
                      tool_call_id=runtime.tool_call_id,
                  )
              ],
              "issue_type": issue_type,
              "current_step": "resolution_specialist",
          }
      )

  @tool
  def escalate_to_human(reason: str) -> str:
      """Escalate the case to a human support specialist."""
      # In a real system, this would create a ticket, notify staff, etc.
      return f"Escalating to human support. Reason: {reason}"

  @tool
  def provide_solution(solution: str) -> str:
      """Provide a solution to the customer's issue."""
      return f"Solution provided: {solution}"

  # Define prompts as constants
  WARRANTY_COLLECTOR_PROMPT = """You are a customer support agent helping with device issues.

  CURRENT STEP: Warranty verification

  At this step, you need to:
  1. Greet the customer warmly
  2. Ask if their device is under warranty
  3. Use record_warranty_status to record their response and move to the next step

  Be conversational and friendly. Don't ask multiple questions at once."""

  ISSUE_CLASSIFIER_PROMPT = """You are a customer support agent helping with device issues.

  CURRENT STEP: Issue classification
  CUSTOMER INFO: Warranty status is {warranty_status}

  At this step, you need to:
  1. Ask the customer to describe their issue
  2. Determine if it's a hardware issue (physical damage, broken parts) or software issue (app crashes, performance)
  3. Use record_issue_type to record the classification and move to the next step

  If unclear, ask clarifying questions before classifying."""

  RESOLUTION_SPECIALIST_PROMPT = """You are a customer support agent helping with device issues.

  CURRENT STEP: Resolution
  CUSTOMER INFO: Warranty status is {warranty_status}, issue type is {issue_type}

  At this step, you need to:
  1. For SOFTWARE issues: provide troubleshooting steps using provide_solution
  2. For HARDWARE issues:
     - If IN WARRANTY: explain warranty repair process using provide_solution
     - If OUT OF WARRANTY: escalate_to_human for paid repair options

  Be specific and helpful in your solutions."""

  # Step configuration: maps step name to (prompt, tools, required_state)
  STEP_CONFIG = {
      "warranty_collector": {
          "prompt": WARRANTY_COLLECTOR_PROMPT,
          "tools": [record_warranty_status],
          "requires": [],
      },
      "issue_classifier": {
          "prompt": ISSUE_CLASSIFIER_PROMPT,
          "tools": [record_issue_type],
          "requires": ["warranty_status"],
      },
      "resolution_specialist": {
          "prompt": RESOLUTION_SPECIALIST_PROMPT,
          "tools": [provide_solution, escalate_to_human],
          "requires": ["warranty_status", "issue_type"],
      },
  }

  @wrap_model_call
  def apply_step_config(
      request: ModelRequest,
      handler: Callable[[ModelRequest], ModelResponse],
  ) -> ModelResponse:
      """Configure agent behavior based on the current step."""
      # Get current step (defaults to warranty_collector for first interaction)
      current_step = request.state.get("current_step", "warranty_collector")

      # Look up step configuration
      step_config = STEP_CONFIG[current_step]

      # Validate required state exists
      for key in step_config["requires"]:
          if request.state.get(key) is None:
              raise ValueError(f"{key} must be set before reaching {current_step}")

      # Format prompt with state values
      system_prompt = step_config["prompt"].format(**request.state)

      # Inject system prompt and step-specific tools
      request = request.override(
          system_prompt=system_prompt,
          tools=step_config["tools"],
      )

      return handler(request)

  # Collect all tools from all step configurations
  all_tools = [
      record_warranty_status,
      record_issue_type,
      provide_solution,
      escalate_to_human,
  ]

  # Create the agent with step-based configuration and summarization
  agent = create_agent(
      model,
      tools=all_tools,
      state_schema=SupportState,
      middleware=[
          apply_step_config,
          SummarizationMiddleware(
              model="gpt-5.4-mini",
              trigger=("tokens", 4000),
              keep=("messages", 10)
          )
      ],
      checkpointer=InMemorySaver(),
  )

  # ============================================================================
  # Test the workflow
  # ============================================================================

  if __name__ == "__main__":
      thread_id = str(uuid7())
      config = {"configurable": {"thread_id": thread_id}}

      result = agent.invoke(
          {"messages": [HumanMessage("Hi, my phone screen is cracked")]},
          config
      )

      result = agent.invoke(
          {"messages": [HumanMessage("Yes, it's still under warranty")]},
          config
      )

      result = agent.invoke(
          {"messages": [HumanMessage("The screen is physically cracked from dropping it")]},
          config
      )

      result = agent.invoke(
          {"messages": [HumanMessage("What should I do?")]},
          config
      )
      for msg in result['messages']:
          msg.pretty_print()
  ```
</Expandable>

## Next steps

* Learn about the [subagents pattern](/oss/python/langchain/multi-agent/subagents-personal-assistant) for centralized orchestration
* Explore [middleware](/oss/python/langchain/middleware) for more dynamic behaviors
* Read the [multi-agent overview](/oss/python/langchain/multi-agent) to compare patterns
* Use [LangSmith](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=oss-langchain-multi-agent-handoffs-customer-support) to debug and monitor your multi-agent system

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langchain/multi-agent/handoffs-customer-support.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Multi-agent
Source: https://docs.langchain.com/oss/python/langchain/multi-agent/index

Multi-agent systems coordinate specialized components to tackle complex workflows. However, not every complex task requires this approach—a single agent with the right (sometimes dynamic) tools and prompt can often achieve similar results.

<Tip>
  For built-in multi-agent support, use [Deep Agents](/oss/python/deepagents/overview): a higher-level harness built on LangChain that ships with [subagents](/oss/python/deepagents/subagents), [skills](/oss/python/deepagents/skills), planning, a virtual filesystem, and context management.
</Tip>

## Why multi-agent?

When developers say they need "multi-agent," they're usually looking for one or more of these capabilities:

* <Icon icon="brain" /> **Context management**: Provide specialized knowledge without overwhelming the model's context window. If context were infinite and latency zero, you could dump all knowledge into a single prompt—but since it's not, you need patterns to selectively surface relevant information.
* <Icon icon="users" /> **Distributed development**: Allow different teams to develop and maintain capabilities independently, composing them into a larger system with clear boundaries.
* <Icon icon="git-branch" /> **Parallelization**: Spawn specialized workers for subtasks and execute them concurrently for faster results.

Multi-agent patterns are particularly valuable when a single agent has too many [tools](/oss/python/langchain/tools) and makes poor decisions about which to use, when tasks require specialized knowledge with extensive context (long prompts and domain-specific tools), or when you need to enforce sequential constraints that unlock capabilities only after certain conditions are met.

<Tip>
  At the center of multi-agent design is **[context engineering](/oss/python/langchain/context-engineering)**—deciding what information each agent sees. The quality of your system depends on ensuring each agent has access to the right data for its task.
</Tip>

## Patterns

Here are the main patterns for building multi-agent systems, each suited to different use cases:

| Pattern                                                                  | How it works                                                                                                                                                                                        |
| ------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [**Subagents**](/oss/python/langchain/multi-agent/subagents)             | A main agent coordinates subagents as tools. All routing passes through the main agent, which decides when and how to invoke each subagent.                                                         |
| [**Handoffs**](/oss/python/langchain/multi-agent/handoffs)               | Behavior changes dynamically based on state. Tool calls update a state variable that triggers routing or configuration changes, switching agents or adjusting the current agent's tools and prompt. |
| [**Skills**](/oss/python/langchain/multi-agent/skills)                   | Specialized prompts and knowledge loaded on-demand. A single agent stays in control while loading context from skills as needed.                                                                    |
| [**Router**](/oss/python/langchain/multi-agent/router)                   | A routing step classifies input and directs it to one or more specialized agents. Results are synthesized into a combined response.                                                                 |
| [**Custom workflow**](/oss/python/langchain/multi-agent/custom-workflow) | Build bespoke execution flows with [LangGraph](/oss/python/langgraph/overview), mixing deterministic logic and agentic behavior. Embed other patterns as nodes in your workflow.                    |

### Choosing a pattern

Use this table to match your requirements to the right pattern:

<div>
  | Pattern                                                      | Distributed development | Parallelization | Multi-hop | Direct user interaction |
  | ------------------------------------------------------------ | :---------------------: | :-------------: | :-------: | :---------------------: |
  | [**Subagents**](/oss/python/langchain/multi-agent/subagents) |          ⭐⭐⭐⭐⭐          |      ⭐⭐⭐⭐⭐      |   ⭐⭐⭐⭐⭐   |            ⭐            |
  | [**Handoffs**](/oss/python/langchain/multi-agent/handoffs)   |            -            |        -        |   ⭐⭐⭐⭐⭐   |          ⭐⭐⭐⭐⭐          |
  | [**Skills**](/oss/python/langchain/multi-agent/skills)       |          ⭐⭐⭐⭐⭐          |       ⭐⭐⭐       |   ⭐⭐⭐⭐⭐   |          ⭐⭐⭐⭐⭐          |
  | [**Router**](/oss/python/langchain/multi-agent/router)       |           ⭐⭐⭐           |      ⭐⭐⭐⭐⭐      |     -     |           ⭐⭐⭐           |
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
* **Tokens processed**: Total [context window](/oss/python/langchain/context-engineering) usage across all calls. More tokens = higher processing costs and potential context limits.

### One-shot request

> **User:** "Buy coffee"

A specialized coffee agent/skill can call a `buy_coffee` tool.

| Pattern                                                      | Model calls | Best fit |
| ------------------------------------------------------------ | :---------: | :------: |
| [**Subagents**](/oss/python/langchain/multi-agent/subagents) |      4      |          |
| [**Handoffs**](/oss/python/langchain/multi-agent/handoffs)   |      3      |     ✅    |
| [**Skills**](/oss/python/langchain/multi-agent/skills)       |      3      |     ✅    |
| [**Router**](/oss/python/langchain/multi-agent/router)       |      3      |     ✅    |

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
  | Pattern                                                      | Turn 2 calls | Total (both turns) | Best fit |
  | ------------------------------------------------------------ | :----------: | :----------------: | :------: |
  | [**Subagents**](/oss/python/langchain/multi-agent/subagents) |       4      |          8         |          |
  | [**Handoffs**](/oss/python/langchain/multi-agent/handoffs)   |       2      |          5         |     ✅    |
  | [**Skills**](/oss/python/langchain/multi-agent/skills)       |       2      |          5         |     ✅    |
  | [**Router**](/oss/python/langchain/multi-agent/router)       |       3      |          6         |          |
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

| Pattern                                                      | Model calls | Total tokens | Best fit |
| ------------------------------------------------------------ | :---------: | :----------: | :------: |
| [**Subagents**](/oss/python/langchain/multi-agent/subagents) |      5      |     \~9K     |     ✅    |
| [**Handoffs**](/oss/python/langchain/multi-agent/handoffs)   |      7+     |    \~14K+    |          |
| [**Skills**](/oss/python/langchain/multi-agent/skills)       |      3      |     \~15K    |          |
| [**Router**](/oss/python/langchain/multi-agent/router)       |      5      |     \~9K     |     ✅    |

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
  | Pattern                                                      | One-shot | Repeat request |      Multi-domain     |
  | ------------------------------------------------------------ | :------: | :------------: | :-------------------: |
  | [**Subagents**](/oss/python/langchain/multi-agent/subagents) |  4 calls |  8 calls (4+4) |   5 calls, 9K tokens  |
  | [**Handoffs**](/oss/python/langchain/multi-agent/handoffs)   |  3 calls |  5 calls (3+2) | 7+ calls, 14K+ tokens |
  | [**Skills**](/oss/python/langchain/multi-agent/skills)       |  3 calls |  5 calls (3+2) |  3 calls, 15K tokens  |
  | [**Router**](/oss/python/langchain/multi-agent/router)       |  3 calls |  6 calls (3+3) |   5 calls, 9K tokens  |
</div>

**Choosing a pattern:**

<div>
  | Optimize for          | [Subagents](/oss/python/langchain/multi-agent/subagents) | [Handoffs](/oss/python/langchain/multi-agent/handoffs) | [Skills](/oss/python/langchain/multi-agent/skills) | [Router](/oss/python/langchain/multi-agent/router) |
  | --------------------- | :------------------------------------------------------: | :----------------------------------------------------: | :------------------------------------------------: | :------------------------------------------------: |
  | Single requests       |                                                          |                            ✅                           |                          ✅                         |                          ✅                         |
  | Repeat requests       |                                                          |                            ✅                           |                          ✅                         |                                                    |
  | Parallel execution    |                             ✅                            |                                                        |                                                    |                          ✅                         |
  | Large-context domains |                             ✅                            |                                                        |                                                    |                          ✅                         |
  | Simple, focused tasks |                                                          |                                                        |                          ✅                         |                                                    |
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
Source: https://docs.langchain.com/oss/python/langchain/multi-agent/router

In the **router** architecture, a routing step classifies input and directs it to specialized [agents](/oss/python/langchain/agents). This is useful when you have distinct **verticals** (separate knowledge domains that each require their own agent).

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

The router classifies the query and directs it to the appropriate agent(s). Use [`Command`](/oss/python/langgraph/graph-api#command) for single-agent routing or [`Send`](/oss/python/langgraph/graph-api#send) for parallel fan-out to multiple agents.

<Tabs>
  <Tab title="Single agent">
    Use `Command` to route to a single specialized agent:

    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    from langgraph.types import Command

    def classify_query(query: str) -> str:
        """Use LLM to classify query and determine the appropriate agent."""
        # Classification logic here
        ...

    def route_query(state: State) -> Command:
        """Route to the appropriate agent based on query classification."""
        active_agent = classify_query(state["query"])

        # Route to the selected agent
        return Command(goto=active_agent)
    ```
  </Tab>

  <Tab title="Multiple agents (parallel)">
    Use `Send` to fan out to multiple specialized agents in parallel:

    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    from typing import TypedDict
    from langgraph.types import Send

    class ClassificationResult(TypedDict):
        query: str
        agent: str

    def classify_query(query: str) -> list[ClassificationResult]:
        """Use LLM to classify query and determine which agents to invoke."""
        # Classification logic here
        ...

    def route_query(state: State):
        """Route to relevant agents based on query classification."""
        classifications = classify_query(state["query"])

        # Fan out to selected agents in parallel
        return [
            Send(c["agent"], {"query": c["query"]})
            for c in classifications
        ]
    ```
  </Tab>
</Tabs>

For a complete implementation, see the tutorial below.

<Card title="Tutorial: Build a multi-source knowledge base with routing" icon="book" href="/oss/python/langchain/multi-agent/router-knowledge-base">
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
  * **Subagents**: An main supervisor agent dynamically decides which [subagents](/oss/python/langchain/multi-agent/subagents) to call as part of an ongoing conversation. The main agent maintains context, can call multiple subagents across turns, and orchestrates complex multi-step workflows.

  Use a **router** when you have clear input categories and want deterministic or lightweight classification. Use a **supervisor** when you need flexible, conversation-aware orchestration where the LLM decides what to do next based on evolving context.
</Tip>

## Stateful

For multi-turn conversations, you need to maintain context across invocations.

### Tool wrapper

The simplest approach: wrap the stateless router as a tool that a conversational agent can call. The conversational agent handles memory and context; the router stays stateless. This avoids the complexity of managing conversation history across multiple parallel agents.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
@tool
def search_docs(query: str) -> str:
    """Search across multiple documentation sources."""
    result = workflow.invoke({"query": query})  # [!code highlight]
    return result["final_answer"]

# Conversational agent uses the router as a tool
conversational_agent = create_agent(
    model,
    tools=[search_docs],
    prompt="You are a helpful assistant. Use search_docs to answer questions."
)
```

### Full persistence

If you need the router itself to maintain state, use [persistence](/oss/python/langchain/short-term-memory) to store message history. When routing to an agent, fetch previous messages from state and selectively include them in the agent's context—this is a lever for [context engineering](/oss/python/langchain/context-engineering).

<Warning>
  **Stateful routers require custom history management.** If the router switches between agents across turns, conversations may not feel fluid to end users when agents have different tones or prompts. With parallel invocation, you'll need to maintain history at the router level (inputs and synthesized outputs) and leverage this history in routing logic. Consider the [handoffs pattern](/oss/python/langchain/multi-agent/handoffs) or [subagents pattern](/oss/python/langchain/multi-agent/subagents) instead—both provide clearer semantics for multi-turn conversations.
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
