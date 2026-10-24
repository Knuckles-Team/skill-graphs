# Define the structure for email classification
class EmailClassification(TypedDict):
    intent: Literal["question", "bug", "billing", "feature", "complex"]
    urgency: Literal["low", "medium", "high", "critical"]
    topic: str
    summary: str

class EmailAgentState(TypedDict):
    # Raw email data
    email_content: str
    sender_email: str
    email_id: str

    # Classification result
    classification: EmailClassification | None

    # Raw search/API results
    search_results: list[str] | None  # List of raw document chunks
    customer_history: dict | None  # Raw customer data from CRM

    # Generated content
    draft_response: str | None
    messages: list[str] | None
```

Notice that the state contains only raw data—no prompt templates, no formatted strings, no instructions. The classification output is stored as a single dictionary, straight from the LLM.

## Step 4: Build your nodes

Now we implement each step as a function. A node in LangGraph is just a Python function that takes the current state and returns updates to it.

### Handle errors appropriately

Different errors need different handling strategies:

| Error Type                                                      | Who Fixes It            | Strategy                           | When to Use                                               |
| --------------------------------------------------------------- | ----------------------- | ---------------------------------- | --------------------------------------------------------- |
| Transient errors (network issues, rate limits)                  | System (automatic)      | Retry policy                       | Temporary failures that usually resolve on retry          |
| LLM-recoverable errors (tool failures, parsing issues)          | LLM                     | Store error in state and loop back | LLM can see the error and adjust its approach             |
| User-fixable errors (missing information, unclear instructions) | Human                   | Pause with `interrupt()`           | Need user input to proceed                                |
| Recoverable failure after retries                               | Developer (declarative) | `error_handler`                    | Run a compensation/recovery branch after retry exhaustion |
| Unexpected errors                                               | Developer               | Let them bubble up                 | Unknown issues that need debugging                        |

<Tabs>
  <Tab title="Transient errors" icon="rotate">
    Add a retry policy to automatically retry network issues and rate limits.

    Combine with `timeout=` to cap each attempt. See [Fault tolerance](/oss/python/langgraph/fault-tolerance) for the full lifecycle.

    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    from langgraph.types import RetryPolicy

    workflow.add_node(
        "search_documentation",
        search_documentation,
        retry_policy=RetryPolicy(max_attempts=3, initial_interval=1.0)
    )
    ```
  </Tab>

  <Tab title="LLM-recoverable" icon="brain">
    Store the error in state and loop back so the LLM can see what went wrong and try again:

    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    from langgraph.types import Command

    def execute_tool(state: State) -> Command[Literal["agent", "execute_tool"]]:
        try:
            result = run_tool(state['tool_call'])
            return Command(update={"tool_result": result}, goto="agent")
        except ToolError as e:
            # Let the LLM see what went wrong and try again
            return Command(
                update={"tool_result": f"Tool error: {str(e)}"},
                goto="agent"
            )
    ```
  </Tab>

  <Tab title="User-fixable" icon="user">
    Pause and collect information from the user when needed (like account IDs, order numbers, or clarifications):

    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    from langgraph.types import Command

    def lookup_customer_history(state: State) -> Command[Literal["draft_response"]]:
        if not state.get('customer_id'):
            user_input = interrupt({
                "message": "Customer ID needed",
                "request": "Please provide the customer's account ID to look up their subscription history"
            })
            return Command(
                update={"customer_id": user_input['customer_id']},
                goto="lookup_customer_history"
            )
        # Now proceed with the lookup
        customer_data = fetch_customer_history(state['customer_id'])
        return Command(update={"customer_history": customer_data}, goto="draft_response")
    ```
  </Tab>

  <Tab title="Unexpected" icon="alert-triangle">
    Let them bubble up for debugging. Don't catch what you can't handle:

    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    def send_reply(state: EmailAgentState):
        try:
            email_service.send(state["draft_response"])
        except Exception:
            raise  # Surface unexpected errors
    ```
  </Tab>

  <Tab title="Saga / compensation" icon="arrows-exchange">
    After retries are exhausted, run a recovery function that updates state and routes to a compensation branch.

    See [Fault tolerance](/oss/python/langgraph/fault-tolerance#error-handling) for the full pattern.

    <Note>
      `error_handler` requires `langgraph>=1.2`.
    </Note>

    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    from langgraph.errors import NodeError
    from langgraph.types import Command, RetryPolicy

    def payment_error_handler(state: State, error: NodeError) -> Command:
        return Command(
            update={"status": f"compensated: {error.error}"},
            goto="finalize",
        )

    workflow.add_node(
        "charge_payment",
        charge_payment,
        retry_policy=RetryPolicy(max_attempts=3, retry_on=ConnectionError),
        error_handler=payment_error_handler,
    )
    ```
  </Tab>
</Tabs>

### Implementing our email agent nodes

We'll implement each node as a simple function. Remember: nodes take state, do work, and return updates.

<AccordionGroup>
  <Accordion title="Read and classify nodes" icon="brain">
    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    from typing import Literal
    from langgraph.graph import StateGraph, START, END
    from langgraph.types import interrupt, Command, RetryPolicy
    from langchain_openai import ChatOpenAI
    from langchain.messages import HumanMessage

    llm = ChatOpenAI(model="gpt-5-nano")

    def read_email(state: EmailAgentState) -> dict:
        """Extract and parse email content"""
        # In production, this would connect to your email service
        return {
            "messages": [HumanMessage(content=f"Processing email: {state['email_content']}")]
        }

    def classify_intent(state: EmailAgentState) -> Command[Literal["search_documentation", "human_review", "draft_response", "bug_tracking"]]:
        """Use LLM to classify email intent and urgency, then route accordingly"""

        # Create structured LLM that returns EmailClassification dict
        structured_llm = llm.with_structured_output(EmailClassification)

        # Format the prompt on-demand, not stored in state
        classification_prompt = f"""
        Analyze this customer email and classify it:

        Email: {state['email_content']}
        From: {state['sender_email']}

        Provide classification including intent, urgency, topic, and summary.
        """

        # Get structured response directly as dict
        classification = structured_llm.invoke(classification_prompt)

        # Determine next node based on classification
        if classification['intent'] == 'billing' or classification['urgency'] == 'critical':
            goto = "human_review"
        elif classification['intent'] in ['question', 'feature']:
            goto = "search_documentation"
        elif classification['intent'] == 'bug':
            goto = "bug_tracking"
        else:
            goto = "draft_response"

        # Store classification as a single dict in state
        return Command(
            update={"classification": classification},
            goto=goto
        )
    ```
  </Accordion>

  <Accordion title="Search and tracking nodes" icon="database">
    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    def search_documentation(state: EmailAgentState) -> Command[Literal["draft_response"]]:
        """Search knowledge base for relevant information"""

        # Build search query from classification
        classification = state.get('classification', {})
        query = f"{classification.get('intent', '')} {classification.get('topic', '')}"

        try:
            # Implement your search logic here
            # Store raw search results, not formatted text
            search_results = [
                "Reset password via Settings > Security > Change Password",
                "Password must be at least 12 characters",
                "Include uppercase, lowercase, numbers, and symbols"
            ]
        except SearchAPIError as e:
            # For recoverable search errors, store error and continue
            search_results = [f"Search temporarily unavailable: {str(e)}"]

        return Command(
            update={"search_results": search_results},  # Store raw results or error
            goto="draft_response"
        )

    def bug_tracking(state: EmailAgentState) -> Command[Literal["draft_response"]]:
        """Create or update bug tracking ticket"""

        # Create ticket in your bug tracking system
        ticket_id = "BUG-12345"  # Would be created via API

        return Command(
            update={
                "search_results": [f"Bug ticket {ticket_id} created"],
                "current_step": "bug_tracked"
            },
            goto="draft_response"
        )
    ```
  </Accordion>

  <Accordion title="Response nodes" icon="edit">
    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    def draft_response(state: EmailAgentState) -> Command[Literal["human_review", "send_reply"]]:
        """Generate response using context and route based on quality"""

        classification = state.get('classification', {})

        # Format context from raw state data on-demand
        context_sections = []

        if state.get('search_results'):
            # Format search results for the prompt
            formatted_docs = "\n".join([f"- {doc}" for doc in state['search_results']])
            context_sections.append(f"Relevant documentation:\n{formatted_docs}")

        if state.get('customer_history'):
            # Format customer data for the prompt
            context_sections.append(f"Customer tier: {state['customer_history'].get('tier', 'standard')}")

        # Build the prompt with formatted context
        draft_prompt = f"""
        Draft a response to this customer email:
        {state['email_content']}

        Email intent: {classification.get('intent', 'unknown')}
        Urgency level: {classification.get('urgency', 'medium')}

        {chr(10).join(context_sections)}

        Guidelines:
        - Be professional and helpful
        - Address their specific concern
        - Use the provided documentation when relevant
        """

        response = llm.invoke(draft_prompt)

        # Determine if human review needed based on urgency and intent
        needs_review = (
            classification.get('urgency') in ['high', 'critical'] or
            classification.get('intent') == 'complex'
        )

        # Route to appropriate next node
        goto = "human_review" if needs_review else "send_reply"

        return Command(
            update={"draft_response": response.content},  # Store only the raw response
            goto=goto
        )

    def human_review(state: EmailAgentState) -> Command[Literal["send_reply", END]]:
        """Pause for human review using interrupt and route based on decision"""

        classification = state.get('classification', {})

        # interrupt() must come first - any code before it will re-run on resume
        human_decision = interrupt({
            "email_id": state.get('email_id',''),
            "original_email": state.get('email_content',''),
            "draft_response": state.get('draft_response',''),
            "urgency": classification.get('urgency'),
            "intent": classification.get('intent'),
            "action": "Please review and approve/edit this response"
        })

        # Now process the human's decision
        if human_decision.get("approved"):
            return Command(
                update={"draft_response": human_decision.get("edited_response", state.get('draft_response',''))},
                goto="send_reply"
            )
        else:
            # Rejection means human will handle directly
            return Command(update={}, goto=END)

    def send_reply(state: EmailAgentState) -> dict:
        """Send the email response"""
        # Integrate with email service
        print(f"Sending reply: {state['draft_response'][:100]}...")
        return {}
    ```
  </Accordion>
</AccordionGroup>

## Step 5: Wire it together

Now we connect our nodes into a working graph. Since our nodes handle their own routing decisions, we only need a few essential edges.

To enable [human-in-the-loop](/oss/python/langgraph/interrupts) with `interrupt()`, we need to compile with a [checkpointer](/oss/python/langgraph/persistence) to save state between runs:

<Accordion title="Graph compilation code" icon="sitemap">
  ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langgraph.checkpoint.memory import MemorySaver
  from langgraph.types import RetryPolicy

  # Create the graph
  workflow = StateGraph(EmailAgentState)

  # Add nodes with appropriate error handling
  workflow.add_node("read_email", read_email)
  workflow.add_node("classify_intent", classify_intent)

  # Add retry policy for nodes that might have transient failures
  workflow.add_node(
      "search_documentation",
      search_documentation,
      retry_policy=RetryPolicy(max_attempts=3)
  )
  workflow.add_node("bug_tracking", bug_tracking)
  workflow.add_node("draft_response", draft_response)
  workflow.add_node("human_review", human_review)
  workflow.add_node("send_reply", send_reply)

  # Add only the essential edges
  workflow.add_edge(START, "read_email")
  workflow.add_edge("read_email", "classify_intent")
  workflow.add_edge("send_reply", END)

  # Compile with checkpointer for persistence, in case run graph with Local_Server --> Please compile without checkpointer
  memory = MemorySaver()
  app = workflow.compile(checkpointer=memory)
  ```
</Accordion>

The graph structure is minimal because routing happens inside nodes through [`Command`](https://reference.langchain.com/python/langgraph/types/Command) objects. Each node declares where it can go using type hints like `Command[Literal["node1", "node2"]]`, making the flow explicit and traceable.

### Try out your agent

Let's run our agent with an urgent billing issue that needs human review:

<Accordion title="Testing the agent" icon="flask">
  ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from typing import TypedDict

  from langgraph.checkpoint.memory import InMemorySaver
  from langgraph.graph import END, START, StateGraph
  from langgraph.types import Command, interrupt

  class EmailState(TypedDict):
      email_content: str
      response_text: str | None

  def human_review_node(state: EmailState):
      interrupt(
          {
              "approved": False,
              "edited_response": state.get("response_text") or "",
          }
      )
      return {"response_text": "placeholder"}

  app = (
      StateGraph(EmailState)
      .add_node("human_review", human_review_node)
      .add_edge(START, "human_review")
      .add_edge("human_review", END)
      .compile(checkpointer=InMemorySaver())
  )

  initial_state = {
      "email_content": "I was charged twice for my subscription! This is urgent!",
      "response_text": "Draft response",
  }

  # Run with a thread_id for persistence
  config = {"configurable": {"thread_id": "customer_123"}}
  stream = app.stream_events(initial_state, config, version="v3")
  _ = stream.output  # drive the stream to completion
  # The graph will pause at human_review
  print(f"human review interrupt:{stream.interrupts}")

  human_response = Command(
      resume={
          "approved": True,
          "edited_response": "We sincerely apologize for the double charge. I've initiated an immediate refund...",
      }
  )

  # Resume execution
  resumed = app.stream_events(human_response, config, version="v3")
  final_state = resumed.output
  print("Email sent successfully!")
  ```
</Accordion>

The graph pauses when it hits `interrupt()`, saves everything to the checkpointer, and waits. It can resume days later, picking up exactly where it left off. The `thread_id` ensures all state for this conversation is preserved together.

## Summary and next steps

### Key Insights

Building this email agent has shown us the LangGraph way of thinking:

<CardGroup>
  <Card title="Break into discrete steps" icon="sitemap" href="#step-1-map-out-your-workflow-as-discrete-steps">
    Each node does one thing well. This decomposition enables streaming progress updates, durable execution that can pause and resume, and clear debugging since you can inspect state between steps.
  </Card>

  <Card title="State is shared memory" icon="database" href="#step-3-design-your-state">
    Store raw data, not formatted text. This lets different nodes use the same information in different ways.
  </Card>

  <Card title="Nodes are functions" icon="code" href="#step-4-build-your-nodes">
    They take state, do work, and return updates. When they need to make routing decisions, they specify both the state updates and the next destination.
  </Card>

  <Card title="Errors are part of the flow" icon="alert-triangle" href="#handle-errors-appropriately">
    Transient failures get retries, LLM-recoverable errors loop back with context, user-fixable problems pause for input, and unexpected errors bubble up for debugging.
  </Card>

  <Card title="Human input is first-class" icon="user" href="/oss/python/langgraph/interrupts">
    The `interrupt()` function pauses execution indefinitely, saves all state, and resumes exactly where it left off when you provide input. When combined with other operations in a node, it must come first.
  </Card>

  <Card title="Graph structure emerges naturally" icon="sitemap" href="#step-5-wire-it-together">
    You define the essential connections, and your nodes handle their own routing logic. This keeps control flow explicit and traceable - you can always understand what your agent will do next by looking at the current node.
  </Card>
</CardGroup>

### Advanced considerations

<Accordion title="Node granularity trade-offs" icon="adjustments">
  <Info>
    This section explores the trade-offs in node granularity design. Most applications can skip this and use the patterns shown above.
  </Info>

  You might wonder: why not combine `Read Email` and `Classify Intent` into one node?

  Or why separate Doc Search from Draft Reply?

  The answer involves trade-offs between resilience and observability.

  **The resilience consideration:** LangGraph's [persistence layer](/oss/python/langgraph/persistence) creates checkpoints at node boundaries. When a workflow resumes after an interruption or failure, it starts from the beginning of the node where execution stopped. Smaller nodes mean more frequent checkpoints, which means less work to repeat if something goes wrong. If you combine multiple operations into one large node, a failure near the end means re-executing everything from the start of that node.

  Why we chose this breakdown for the email agent:

  * **Isolation of external services:** Doc Search and Bug Track are separate nodes because they call external APIs. If the search service is slow or fails, we want to isolate that from the LLM calls. We can add retry policies to these specific nodes without affecting others.

  * **Intermediate visibility:** Having `Classify Intent` as its own node lets us inspect what the LLM decided before taking action. This is valuable for debugging and monitoring—you can see exactly when and why the agent routes to human review.

  * **Different failure modes:** LLM calls, database lookups, and email sending have different retry strategies. Separate nodes let you configure these independently.

  * **Reusability and testing:** Smaller nodes are easier to test in isolation and reuse in other workflows.

  A different valid approach: You could combine `Read Email` and `Classify Intent` into a single node. You'd lose the ability to inspect the raw email before classification and would repeat both operations on any failure in that node. For most applications, the observability and debugging benefits of separate nodes are worth the trade-off.

  Application-level concerns: The caching discussion in Step 2 (whether to cache search results) is an application-level decision, not a LangGraph framework feature. You implement caching within your node functions based on your specific requirements—LangGraph doesn't prescribe this.

  Performance considerations: More nodes doesn't mean slower execution. LangGraph writes checkpoints in the background by default ([async durability mode](/oss/python/langgraph/checkpointers#durability-modes)), so your graph continues running without waiting for checkpoints to complete. This means you get frequent checkpoints with minimal performance impact. You can adjust this behavior if needed—use `"exit"` mode to checkpoint only at completion, or `"sync"` mode to block execution until each checkpoint is written.
</Accordion>

### Where to go from here

This was an introduction to thinking about building agents with LangGraph. You can extend this foundation with:

<CardGroup>
  <Card title="Human-in-the-loop patterns" icon="user-check" href="/oss/python/langgraph/interrupts">
    Learn how to add tool approval before execution, batch approval, and other patterns
  </Card>

  <Card title="Subgraphs" icon="hierarchy" href="/oss/python/langgraph/use-subgraphs">
    Create subgraphs for complex multi-step operations
  </Card>

  <Card title="Streaming" icon="broadcast" href="/oss/python/langgraph/streaming">
    Add streaming to show real-time progress to users
  </Card>

  <Card title="Observability" icon="chart-line" href="/oss/python/langgraph/observability">
    Add observability with LangSmith for debugging and monitoring
  </Card>

  <Card title="Tool Integration" icon="tool" href="/oss/python/langchain/tools">
    Integrate more tools for web search, database queries, and API calls
  </Card>

  <Card title="Retry Logic" icon="rotate" href="/oss/python/langgraph/use-graph-api#add-retry-policies">
    Implement retry logic with exponential backoff for failed operations
  </Card>
</CardGroup>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langgraph/thinking-in-langgraph.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Agent Chat UI
Source: https://docs.langchain.com/oss/python/langgraph/ui

[Agent Chat UI](https://github.com/langchain-ai/agent-chat-ui) is a Next.js application that provides a conversational interface for interacting with any LangChain agent. It supports real-time chat, tool visualization, and advanced features like time-travel debugging and state forking. Agent Chat UI works seamlessly with agents created using [`create_agent`](https://reference.langchain.com/python/langchain/agents/factory/create_agent) and provides interactive experiences for your agents with minimal setup, whether you're running locally or in a deployed context (such as [LangSmith](/langsmith/observability)).

Agent Chat UI is open source and can be adapted to your application needs.

<Frame>
  <iframe title="Agent Chat UI" />
</Frame>

<Tip>
  You can use generative UI in the Agent Chat UI. For more information, see [Implement generative user interfaces with LangGraph](/langsmith/generative-ui-react).
</Tip>

### Quick start

The fastest way to get started is using the hosted version:

1. **Visit [Agent Chat UI](https://agentchat.vercel.app)**
2. **Connect your agent** by entering your deployment URL or local server address
3. **Start chatting** - the UI will automatically detect and render tool calls and interrupts

### Local development

For customization or local development, you can run Agent Chat UI locally:

<CodeGroup>
  ```bash Use npx theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  # Create a new Agent Chat UI project
  npx create-agent-chat-app --project-name my-chat-ui
  cd my-chat-ui

  # Install dependencies and start
  pnpm install
  pnpm dev
  ```

  ```bash Clone repository theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  # Clone the repository
  git clone https://github.com/langchain-ai/agent-chat-ui.git
  cd agent-chat-ui

  # Install dependencies and start
  pnpm install
  pnpm dev
  ```
</CodeGroup>

### Connect to your agent

Agent Chat UI can connect to both [local](/oss/python/langgraph/studio#set-up-local-agent-server) and [deployed agents](/oss/python/langgraph/deploy).

After starting Agent Chat UI, you'll need to configure it to connect to your agent:

1. **Graph ID**: Enter your graph name (find this under `graphs` in your `langgraph.json` file)
2. **Deployment URL**: Your Agent server's endpoint (e.g., `http://localhost:2024` for local development, or your deployed agent's URL)
3. **LangSmith API key (optional)**: Add your LangSmith API key (not required if you're using a local Agent server)

Once configured, Agent Chat UI will automatically fetch and display any interrupted threads from your agent.

<Tip>
  Agent Chat UI has out-of-the-box support for rendering tool calls and tool result messages. To customize what messages are shown, see [Hiding Messages in the Chat](https://github.com/langchain-ai/agent-chat-ui?tab=readme-ov-file#hiding-messages-in-the-chat).
</Tip>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langgraph/ui.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Use the functional API
Source: https://docs.langchain.com/oss/python/langgraph/use-functional-api

The [**Functional API**](/oss/python/langgraph/functional-api) allows you to add LangGraph's key features ([persistence](/oss/python/langgraph/persistence), [memory](/oss/python/langgraph/add-memory), [human-in-the-loop](/oss/python/langgraph/interrupts), and [streaming](/oss/python/langgraph/streaming)) to your applications with minimal changes to your existing code.

<Tip>
  For conceptual information on the functional API, see [Functional API](/oss/python/langgraph/functional-api).
</Tip>

## Creating a simple workflow

When defining an `entrypoint`, input is restricted to the first argument of the function. To pass multiple inputs, you can use a dictionary.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
@entrypoint(checkpointer=checkpointer)
def my_workflow(inputs: dict) -> int:
    value = inputs["value"]
    another_value = inputs["another_value"]
    ...

my_workflow.invoke({"value": 1, "another_value": 2})
```

<Accordion title="Extended example: simple workflow">
  ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langchain_core.utils.uuid import uuid7
  from langgraph.func import entrypoint, task
  from langgraph.checkpoint.memory import InMemorySaver

  # Task that checks if a number is even
  @task
  def is_even(number: int) -> bool:
      return number % 2 == 0

  # Task that formats a message
  @task
  def format_message(is_even: bool) -> str:
      return "The number is even." if is_even else "The number is odd."

  # Create a checkpointer for persistence
  checkpointer = InMemorySaver()

  @entrypoint(checkpointer=checkpointer)
  def workflow(inputs: dict) -> str:
      """Simple workflow to classify a number."""
      even = is_even(inputs["number"]).result()
      return format_message(even).result()

  # Run the workflow with a unique thread ID
  config = {"configurable": {"thread_id": str(uuid7())}}
  result = workflow.invoke({"number": 7}, config=config)
  print(result)
  ```
</Accordion>

<Accordion title="Extended example: Compose an essay with an LLM">
  This example demonstrates how to use the `@task` and `@entrypoint` decorators
  syntactically. Given that a checkpointer is provided, the workflow results will
  be persisted in the checkpointer.

  ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import uuid
  from langchain.chat_models import init_chat_model
  from langgraph.func import entrypoint, task
  from langgraph.checkpoint.memory import InMemorySaver

  model = init_chat_model('gpt-3.5-turbo')

  # Task: generate essay using an LLM
  @task
  def compose_essay(topic: str) -> str:
      """Generate an essay about the given topic."""
      return model.invoke([
          {"role": "system", "content": "You are a helpful assistant that writes essays."},
          {"role": "user", "content": f"Write an essay about {topic}."}
      ]).content

  # Create a checkpointer for persistence
  checkpointer = InMemorySaver()

  @entrypoint(checkpointer=checkpointer)
  def workflow(topic: str) -> str:
      """Simple workflow that generates an essay with an LLM."""
      return compose_essay(topic).result()

  # Execute the workflow
  config = {"configurable": {"thread_id": str(uuid7())}}
  result = workflow.invoke("the history of flight", config=config)
  print(result)
  ```
</Accordion>

## Parallel execution

Tasks can be executed in parallel by invoking them concurrently and waiting for the results. This is useful for improving performance in IO bound tasks (e.g., calling APIs for LLMs).

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
@task
def add_one(number: int) -> int:
    return number + 1

@entrypoint(checkpointer=checkpointer)
def graph(numbers: list[int]) -> list[str]:
    futures = [add_one(i) for i in numbers]
    return [f.result() for f in futures]
```

<Accordion title="Extended example: parallel LLM calls">
  This example demonstrates how to run multiple LLM calls in parallel using `@task`. Each call generates a paragraph on a different topic, and results are joined into a single text output.

  ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import uuid
  from langchain.chat_models import init_chat_model
  from langgraph.func import entrypoint, task
  from langgraph.checkpoint.memory import InMemorySaver

  # Initialize the LLM model
  model = init_chat_model("gpt-3.5-turbo")

  # Task that generates a paragraph about a given topic
  @task
  def generate_paragraph(topic: str) -> str:
      response = model.invoke([
          {"role": "system", "content": "You are a helpful assistant that writes educational paragraphs."},
          {"role": "user", "content": f"Write a paragraph about {topic}."}
      ])
      return response.content

  # Create a checkpointer for persistence
  checkpointer = InMemorySaver()

  @entrypoint(checkpointer=checkpointer)
  def workflow(topics: list[str]) -> str:
      """Generates multiple paragraphs in parallel and combines them."""
      futures = [generate_paragraph(topic) for topic in topics]
      paragraphs = [f.result() for f in futures]
      return "\n\n".join(paragraphs)

  # Run the workflow
  config = {"configurable": {"thread_id": str(uuid7())}}
  result = workflow.invoke(["quantum computing", "climate change", "history of aviation"], config=config)
  print(result)
  ```

  This example uses LangGraph's concurrency model to improve execution time, especially when tasks involve I/O like LLM completions.
</Accordion>

## Calling graphs

The **Functional API** and the [**Graph API**](/oss/python/langgraph/graph-api) can be used together in the same application as they share the same underlying runtime.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langgraph.func import entrypoint
from langgraph.graph import StateGraph

builder = StateGraph()
...
some_graph = builder.compile()

@entrypoint()
def some_workflow(some_input: dict) -> int:
    # Call a graph defined using the graph API
    result_1 = some_graph.invoke(...)
    # Call another graph defined using the graph API
    result_2 = another_graph.invoke(...)
    return {
        "result_1": result_1,
        "result_2": result_2
    }
```

<Accordion title="Extended example: calling a simple graph from the functional API">
  ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import uuid
  from typing import TypedDict
  from langgraph.func import entrypoint
  from langgraph.checkpoint.memory import InMemorySaver
  from langgraph.graph import StateGraph

  # Define the shared state type
  class State(TypedDict):
      foo: int

  # Define a simple transformation node
  def double(state: State) -> State:
      return {"foo": state["foo"] * 2}

  # Build the graph using the Graph API
  builder = StateGraph(State)
  builder.add_node("double", double)
  builder.set_entry_point("double")
  graph = builder.compile()

  # Define the functional API workflow
  checkpointer = InMemorySaver()

  @entrypoint(checkpointer=checkpointer)
  def workflow(x: int) -> dict:
      result = graph.invoke({"foo": x})
      return {"bar": result["foo"]}

  # Execute the workflow
  config = {"configurable": {"thread_id": str(uuid7())}}
  print(workflow.invoke(5, config=config))  # Output: {'bar': 10}
  ```
</Accordion>

## Call other entrypoints

You can call other **entrypoints** from within an **entrypoint** or a **task**.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
@entrypoint() # Will automatically use the checkpointer from the parent entrypoint
def some_other_workflow(inputs: dict) -> int:
    return inputs["value"]

@entrypoint(checkpointer=checkpointer)
def my_workflow(inputs: dict) -> int:
    value = some_other_workflow.invoke({"value": 1})
    return value
```

<Accordion title="Extended example: calling another entrypoint">
  ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import uuid
  from langgraph.func import entrypoint
  from langgraph.checkpoint.memory import InMemorySaver

  # Initialize a checkpointer
  checkpointer = InMemorySaver()

  # A reusable sub-workflow that multiplies a number
  @entrypoint()
  def multiply(inputs: dict) -> int:
      return inputs["a"] * inputs["b"]

  # Main workflow that invokes the sub-workflow
  @entrypoint(checkpointer=checkpointer)
  def main(inputs: dict) -> dict:
      result = multiply.invoke({"a": inputs["x"], "b": inputs["y"]})
      return {"product": result}

  # Execute the main workflow
  config = {"configurable": {"thread_id": str(uuid7())}}
  print(main.invoke({"x": 6, "y": 7}, config=config))  # Output: {'product': 42}
  ```
</Accordion>

## Streaming

The **Functional API** uses the same streaming mechanism as the **Graph API**. Please
read the [**streaming guide**](/oss/python/langgraph/streaming) section for more details.

Example of using the streaming API to stream both updates and custom data.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langgraph.func import entrypoint
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.config import get_stream_writer   # [!code highlight]

checkpointer = InMemorySaver()

@entrypoint(checkpointer=checkpointer)
def main(inputs: dict) -> int:
    writer = get_stream_writer()   # [!code highlight]
    writer("Started processing")   # [!code highlight]
    result = inputs["x"] * 2
    writer(f"Result is {result}")   # [!code highlight]
    return result

config = {"configurable": {"thread_id": "abc"}}

for mode, chunk in main.stream(   # [!code highlight]
    {"x": 5},
    stream_mode=["custom", "updates"],   # [!code highlight]
    config=config
):
    print(f"{mode}: {chunk}")
```

1. Import [`get_stream_writer`](https://reference.langchain.com/python/langgraph/config/get_stream_writer) from `langgraph.config`.
2. Obtain a stream writer instance within the entrypoint.
3. Emit custom data before computation begins.
4. Emit another custom message after computing the result.
5. Use `.stream()` to process streamed output.
6. Specify which streaming modes to use.

```pycon theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
('updates', {'add_one': 2})
('updates', {'add_two': 3})
('custom', 'hello')
('custom', 'world')
('updates', {'main': 5})
```

<Warning>
  **Async with Python \< 3.11**
  If using Python \< 3.11 and writing async code, using [`get_stream_writer`](https://reference.langchain.com/python/langgraph/config/get_stream_writer) will not work. Instead please
  use the `StreamWriter` class directly. See [Async with Python \< 3.11](/oss/python/langgraph/streaming#async) for more details.

  ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langgraph.types import StreamWriter

  @entrypoint(checkpointer=checkpointer)
  async def main(inputs: dict, writer: StreamWriter) -> int:  # [!code highlight]
  ...
  ```
</Warning>

## Retry policy

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.func import entrypoint, task
from langgraph.types import RetryPolicy

# This variable is just used for demonstration purposes to simulate a network failure.

# It's not something you will have in your actual code.
attempts = 0

# Let's configure the RetryPolicy to retry on ValueError.

# The default RetryPolicy is optimized for retrying specific network errors.
retry_policy = RetryPolicy(retry_on=ValueError)

@task(retry_policy=retry_policy)
def get_info():
    global attempts
    attempts += 1

    if attempts < 2:
        raise ValueError('Failure')
    return "OK"

checkpointer = InMemorySaver()

@entrypoint(checkpointer=checkpointer)
def main(inputs, writer):
    return get_info().result()

config = {
    "configurable": {
        "thread_id": "1"
    }
}

main.invoke({'any_input': 'foobar'}, config=config)
```

```pycon theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
'OK'
```

## Set task and entrypoint timeouts

Use the `timeout` parameter with `@task` or `@entrypoint` to limit how long a single async attempt can run. Provide the timeout in seconds or as a `datetime.timedelta`.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import asyncio

from langgraph.errors import NodeTimeoutError
from langgraph.func import entrypoint, task
from langgraph.types import RetryPolicy

@task(
    timeout=1.0,
    retry_policy=RetryPolicy(retry_on=NodeTimeoutError),
)
async def call_api(url: str) -> str:
    await asyncio.sleep(2)
    return f"result from {url}"

@entrypoint(timeout=5.0)
async def workflow(inputs: dict) -> str:
    return await call_api(inputs["url"])

try:
    await workflow.ainvoke({"url": "https://example.com"})
except NodeTimeoutError:
    print("Task timed out")
```

Timeouts are supported only for async tasks and entrypoints. If you set `timeout` on a sync function, LangGraph raises an error when the task or entrypoint is declared.

When a task or entrypoint exceeds its timeout, LangGraph raises `NodeTimeoutError`, which subclasses Python's built-in `TimeoutError`. If a retry policy retries `TimeoutError` or `NodeTimeoutError`, the timed-out attempt is retried. The timeout applies to each attempt independently, so the timer resets for every retry.

## Caching tasks

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import time
from langgraph.cache.memory import InMemoryCache
from langgraph.func import entrypoint, task
from langgraph.types import CachePolicy

@task(cache_policy=CachePolicy(ttl=120))    # [!code highlight]
def slow_add(x: int) -> int:
    time.sleep(1)
    return x * 2

@entrypoint(cache=InMemoryCache())
def main(inputs: dict) -> dict[str, int]:
    result1 = slow_add(inputs["x"]).result()
    result2 = slow_add(inputs["x"]).result()
    return {"result1": result1, "result2": result2}

for chunk in main.stream({"x": 5}, stream_mode="updates"):
    print(chunk)

#> {'slow_add': 10}
#> {'slow_add': 10, '__metadata__': {'cached': True}}
#> {'main': {'result1': 10, 'result2': 10}}
```

1. `ttl` is specified in seconds. The cache will be invalidated after this time.

## Resuming after an error

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import time
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.func import entrypoint, task
from langgraph.types import StreamWriter

# This variable is just used for demonstration purposes to simulate a network failure.

# It's not something you will have in your actual code.
attempts = 0

@task()
def get_info():
    """
    Simulates a task that fails once before succeeding.
    Raises an exception on the first attempt, then returns "OK" on subsequent tries.
    """
    global attempts
    attempts += 1

    if attempts < 2:
        raise ValueError("Failure")  # Simulate a failure on the first attempt
    return "OK"

# Initialize an in-memory checkpointer for persistence
checkpointer = InMemorySaver()

@task
def slow_task():
    """
    Simulates a slow-running task by introducing a 1-second delay.
    """
    time.sleep(1)
    return "Ran slow task."

@entrypoint(checkpointer=checkpointer)
def main(inputs, writer: StreamWriter):
    """
    Main workflow function that runs the slow_task and get_info tasks sequentially.

    Parameters:
    - inputs: Dictionary containing workflow input values.
    - writer: StreamWriter for streaming custom data.

    The workflow first executes `slow_task` and then attempts to execute `get_info`,
    which will fail on the first invocation.
    """
    slow_task_result = slow_task().result()  # Blocking call to slow_task
    get_info().result()  # Exception will be raised here on the first attempt
    return slow_task_result

# Workflow execution configuration with a unique thread identifier
config = {
    "configurable": {
        "thread_id": "1"  # Unique identifier to track workflow execution
    }
}

# This invocation will take ~1 second due to the slow_task execution
try:
    # First invocation will raise an exception due to the `get_info` task failing
    main.invoke({'any_input': 'foobar'}, config=config)
except ValueError:
    pass  # Handle the failure gracefully
```

When we resume execution, we won't need to re-run the `slow_task` as its result is already saved in the checkpoint.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
main.invoke(None, config=config)
```

```pycon theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
'Ran slow task.'
```

## Human-in-the-loop

The functional API supports [human-in-the-loop](/oss/python/langgraph/interrupts) workflows using the [`interrupt`](https://reference.langchain.com/python/langgraph/types/interrupt) function and the `Command` primitive.

### Basic human-in-the-loop workflow

We will create three [tasks](/oss/python/langgraph/functional-api#task):

1. Append `"bar"`.
2. Pause for human input. When resuming, append human input.
3. Append `"qux"`.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langgraph.func import entrypoint, task
from langgraph.types import Command, interrupt

@task
def step_1(input_query):
    """Append bar."""
    return f"{input_query} bar"

@task
def human_feedback(input_query):
    """Append user input."""
    feedback = interrupt(f"Please provide feedback: {input_query}")
    return f"{input_query} {feedback}"

@task
def step_3(input_query):
    """Append qux."""
    return f"{input_query} qux"
```

We can now compose these tasks in an [entrypoint](/oss/python/langgraph/functional-api#entrypoint):

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langgraph.checkpoint.memory import InMemorySaver

checkpointer = InMemorySaver()

@entrypoint(checkpointer=checkpointer)
def graph(input_query):
    result_1 = step_1(input_query).result()
    result_2 = human_feedback(result_1).result()
    result_3 = step_3(result_2).result()

    return result_3
```

[interrupt()](/oss/python/langgraph/interrupts#pause-using-interrupt) is called inside a task, enabling a human to review and edit the output of the previous task. The results of prior tasks-- in this case `step_1`-- are persisted, so that they are not run again following the [`interrupt`](https://reference.langchain.com/python/langgraph/types/interrupt).

Let's send in a query string:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
config = {"configurable": {"thread_id": "1"}}

for event in graph.stream("foo", config):
    print(event)
    print("\n")
```

Note that we've paused with an [`interrupt`](https://reference.langchain.com/python/langgraph/types/interrupt) after `step_1`. The interrupt provides instructions to resume the run. To resume, we issue a [`Command`](/oss/python/langgraph/interrupts#resuming-interrupts) containing the data expected by the `human_feedback` task.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
