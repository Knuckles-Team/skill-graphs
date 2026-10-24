# - Email: foo@langchain.dev
```

### Stream writer

Stream real-time updates from tools during execution. This is useful for providing progress feedback to users during long-running operations.

Use `runtime.stream_writer` to emit custom updates:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain.tools import tool, ToolRuntime

@tool
def get_weather(city: str, runtime: ToolRuntime) -> str:
    """Get weather for a given city."""
    writer = runtime.stream_writer

    # Stream custom updates as the tool executes
    writer(f"Looking up data for city: {city}")
    writer(f"Acquired data for city: {city}")

    return f"It's always sunny in {city}!"
```

<Note>
  If you use `runtime.stream_writer` inside your tool, the tool must be invoked within a LangGraph execution context. See [Streaming](/oss/python/langchain/streaming) for more details.
</Note>

### Execution info

Access thread ID, run ID, and retry state from within a tool via `runtime.execution_info`:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain.tools import tool, ToolRuntime

@tool
def log_execution_context(runtime: ToolRuntime) -> str:
    """Log execution identity information."""
    info = runtime.execution_info
    print(f"Thread: {info.thread_id}, Run: {info.run_id}")  # [!code highlight]
    print(f"Attempt: {info.node_attempt}")
    return "done"
```

<Note>
  Requires `deepagents>=0.5.0` (or `langgraph>=1.1.5`).
</Note>

### Server info

When your tool runs on LangGraph Server, access the assistant ID, graph ID, and authenticated user via `runtime.server_info`:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain.tools import tool, ToolRuntime

@tool
def get_assistant_scoped_data(runtime: ToolRuntime) -> str:
    """Fetch data scoped to the current assistant."""
    server = runtime.server_info
    if server is not None:
        print(f"Assistant: {server.assistant_id}, Graph: {server.graph_id}")  # [!code highlight]
        if server.user is not None:
            print(f"User: {server.user.identity}")  # [!code highlight]
    return "done"
```

`server_info` is `None` when the tool is not running on LangGraph Server (e.g., during local development or testing).

<Note>
  Requires `deepagents>=0.5.0` (or `langgraph>=1.1.5`).
</Note>

<Accordion title="Migrate from older injection patterns">
  Older examples used `InjectedState`, `InjectedStore`, `get_runtime()`, or `InjectedToolCallId`. Use [`ToolRuntime`](https://reference.langchain.com/python/langchain/tools/#langchain.tools.ToolRuntime) instead for one explicit interface to state, context, store, and execution metadata.

  #### Previous pattern

  ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langchain.tools import tool, InjectedState

  @tool
  def summarize(state: InjectedState) -> str:
      """Summarize the conversation."""
      messages = state["messages"]
      return f"Conversation length: {len(messages)} messages."
  ```

  #### Recommended pattern

  ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langchain.tools import tool, ToolRuntime

  @tool
  def summarize(runtime: ToolRuntime) -> str:
      """Summarize the conversation."""
      messages = runtime.state["messages"]
      return f"Conversation length: {len(messages)} messages."
  ```

  For agent-level migrations (for example `create_react_agent` and custom state), see the [LangChain v1 migration guide](/oss/python/migrate/langchain-v1).
</Accordion>

## Tool execution

In LangChain, tools are used by agents (for example via [`create_agent`](https://reference.langchain.com/python/langchain/agents/factory/create_agent)) and tool error handling is configured through [middleware](/oss/python/langchain/middleware).

For LangGraph workflows, tool execution is handled by [`ToolNode`](https://reference.langchain.com/python/langgraph/agents/#langgraph.prebuilt.tool_node.ToolNode). See [ToolNode](/oss/python/langgraph/workflows-agents#toolnode).

### Tool return values

You can choose different return values for your tools:

* Return a `string` for human-readable results.
* Return an `object` for structured results the model should parse.
* Return a `Command` with optional message when you need to write to state.

#### Return a string

Return a string when the tool should provide plain text for the model to read and use in its next response.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain.tools import tool

@tool
def get_weather(city: str) -> str:
    """Get weather for a city."""
    return f"It is currently sunny in {city}."
```

Behavior:

* The return value is converted to a `ToolMessage`.
* The model sees that text and decides what to do next.
* No agent state fields are changed unless the model or another tool does so later.

Use this when the result is naturally human-readable text.

#### Return an object

Return an object (for example, a `dict`) when your tool produces structured data that the model should inspect.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain.tools import tool

@tool
def get_weather_data(city: str) -> dict:
    """Get structured weather data for a city."""
    return {
        "city": city,
        "temperature_c": 22,
        "conditions": "sunny",
    }
```

Behavior:

* The object is serialized and sent back as tool output.
* The model can read specific fields and reason over them.
* Like string returns, this does not directly update graph state.

Use this when downstream reasoning benefits from explicit fields instead of free-form text.

#### Return a Command

Return a [`Command`](https://reference.langchain.com/python/langgraph/types/Command) when the tool needs to update graph state (for example, setting user preferences or app state).
You can return a `Command` with or without including a `ToolMessage`.
If the model needs to see that the tool succeeded (for example, to confirm a preference change), include a `ToolMessage` in the update, using `runtime.tool_call_id` for the `tool_call_id` parameter.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain.messages import ToolMessage
from langchain.tools import ToolRuntime, tool
from langgraph.types import Command

@tool
def set_language(language: str, runtime: ToolRuntime) -> Command:
    """Set the preferred response language."""
    return Command(
        update={
            "preferred_language": language,
            "messages": [
                ToolMessage(
                    content=f"Language set to {language}.",
                    tool_call_id=runtime.tool_call_id,
                )
            ],
        }
    )
```

Behavior:

* The command updates state using `update`.
* Updated state is available to subsequent steps in the same run.
* Use reducers for fields that may be updated by parallel tool calls.

Use this when the tool is not just returning data, but also mutating agent state.

#### Return directly from a tool

Set return direct on a tool to short-circuit the agent loop: the agent returns the tool's output to the caller immediately, without sending it back through the model for further processing.

<CodeGroup>
  ```python Google theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langchain.agents import create_agent
  from langchain.tools import tool
  from langchain_openai import ChatOpenAI

  @tool(return_direct=True)
  def fetch_order_status(order_id: str) -> str:
      """Fetch the current status of a customer order."""
      # In production, query your order management system here
      return f"Order {order_id} is shipped and will arrive in 2 days."

  agent = create_agent(
      ChatOpenAI(model="google_genai:gemini-3.5-flash"),
      tools=[fetch_order_status],
  )

  result = agent.invoke({
      "messages": [{"role": "user", "content": "What is the status of order #12345?"}]
  })
  # The agent returns the tool output directly without another LLM call:
  # "Order 12345 is shipped and will arrive in 2 days."
  ```

  ```python OpenAI theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langchain.agents import create_agent
  from langchain.tools import tool
  from langchain_openai import ChatOpenAI

  @tool(return_direct=True)
  def fetch_order_status(order_id: str) -> str:
      """Fetch the current status of a customer order."""
      # In production, query your order management system here
      return f"Order {order_id} is shipped and will arrive in 2 days."

  agent = create_agent(
      ChatOpenAI(model="openai:gpt-5.5"),
      tools=[fetch_order_status],
  )

  result = agent.invoke({
      "messages": [{"role": "user", "content": "What is the status of order #12345?"}]
  })
  # The agent returns the tool output directly without another LLM call:
  # "Order 12345 is shipped and will arrive in 2 days."
  ```

  ```python Anthropic theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langchain.agents import create_agent
  from langchain.tools import tool
  from langchain_openai import ChatOpenAI

  @tool(return_direct=True)
  def fetch_order_status(order_id: str) -> str:
      """Fetch the current status of a customer order."""
      # In production, query your order management system here
      return f"Order {order_id} is shipped and will arrive in 2 days."

  agent = create_agent(
      ChatOpenAI(model="anthropic:claude-sonnet-4-6"),
      tools=[fetch_order_status],
  )

  result = agent.invoke({
      "messages": [{"role": "user", "content": "What is the status of order #12345?"}]
  })
  # The agent returns the tool output directly without another LLM call:
  # "Order 12345 is shipped and will arrive in 2 days."
  ```

  ```python OpenRouter theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langchain.agents import create_agent
  from langchain.tools import tool
  from langchain_openai import ChatOpenAI

  @tool(return_direct=True)
  def fetch_order_status(order_id: str) -> str:
      """Fetch the current status of a customer order."""
      # In production, query your order management system here
      return f"Order {order_id} is shipped and will arrive in 2 days."

  agent = create_agent(
      ChatOpenAI(model="openrouter:anthropic/claude-sonnet-4-6"),
      tools=[fetch_order_status],
  )

  result = agent.invoke({
      "messages": [{"role": "user", "content": "What is the status of order #12345?"}]
  })
  # The agent returns the tool output directly without another LLM call:
  # "Order 12345 is shipped and will arrive in 2 days."
  ```

  ```python Fireworks theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langchain.agents import create_agent
  from langchain.tools import tool
  from langchain_openai import ChatOpenAI

  @tool(return_direct=True)
  def fetch_order_status(order_id: str) -> str:
      """Fetch the current status of a customer order."""
      # In production, query your order management system here
      return f"Order {order_id} is shipped and will arrive in 2 days."

  agent = create_agent(
      ChatOpenAI(model="fireworks:accounts/fireworks/models/qwen3p5-397b-a17b"),
      tools=[fetch_order_status],
  )

  result = agent.invoke({
      "messages": [{"role": "user", "content": "What is the status of order #12345?"}]
  })
  # The agent returns the tool output directly without another LLM call:
  # "Order 12345 is shipped and will arrive in 2 days."
  ```

  ```python Baseten theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langchain.agents import create_agent
  from langchain.tools import tool
  from langchain_openai import ChatOpenAI

  @tool(return_direct=True)
  def fetch_order_status(order_id: str) -> str:
      """Fetch the current status of a customer order."""
      # In production, query your order management system here
      return f"Order {order_id} is shipped and will arrive in 2 days."

  agent = create_agent(
      ChatOpenAI(model="baseten:zai-org/GLM-5"),
      tools=[fetch_order_status],
  )

  result = agent.invoke({
      "messages": [{"role": "user", "content": "What is the status of order #12345?"}]
  })
  # The agent returns the tool output directly without another LLM call:
  # "Order 12345 is shipped and will arrive in 2 days."
  ```

  ```python Ollama theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langchain.agents import create_agent
  from langchain.tools import tool
  from langchain_openai import ChatOpenAI

  @tool(return_direct=True)
  def fetch_order_status(order_id: str) -> str:
      """Fetch the current status of a customer order."""
      # In production, query your order management system here
      return f"Order {order_id} is shipped and will arrive in 2 days."

  agent = create_agent(
      ChatOpenAI(model="ollama:devstral-2"),
      tools=[fetch_order_status],
  )

  result = agent.invoke({
      "messages": [{"role": "user", "content": "What is the status of order #12345?"}]
  })
  # The agent returns the tool output directly without another LLM call:
  # "Order 12345 is shipped and will arrive in 2 days."
  ```
</CodeGroup>

Behavior:

* The tool executes normally and its output is wrapped in a `ToolMessage`.
* The agent stops looping and returns the tool's output as the final response, bypassing any additional model call.
* If the model calls multiple tools in a single turn, `return_direct` takes effect only when **all** called tools have `return_direct=True`.

Use this when:

* The tool's output is the complete, user-ready answer (for example, a lookup that returns a ready-to-display result).
* You want to avoid an extra model call when no additional reasoning is needed.
* You need deterministic, unmodified output — the model cannot rephrase, summarize, or act on the tool result.

<Warning>
  Because the model does not process the tool's output, `return_direct=True` is not suitable for tools whose results require further reasoning, summarization, or chaining with other tool calls.
</Warning>

### Error handling

Handle tool errors using LangChain agent [middleware](/oss/python/langchain/middleware) to retry failed tool calls or return custom error messages:

<CodeGroup>
  ```python Google theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from collections.abc import Callable

  from langchain.agents import create_agent
  from langchain.agents.middleware import wrap_tool_call
  from langchain.messages import ToolMessage
  from langchain.tools.tool_node import ToolCallRequest

  @wrap_tool_call
  def handle_tool_errors(
      request: ToolCallRequest,
      handler: Callable[[ToolCallRequest], ToolMessage],
  ) -> ToolMessage:
      """Convert tool exceptions into ToolMessages the model can handle."""
      try:
          return handler(request)
      except Exception as e:
          return ToolMessage(
              content=f"Tool error: Please check your input and try again. ({e})",
              tool_call_id=request.tool_call["id"],
          )

  agent = create_agent(
      model="google_genai:gemini-3.5-flash",
      tools=[],
      middleware=[handle_tool_errors],
  )
  ```

  ```python OpenAI theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from collections.abc import Callable

  from langchain.agents import create_agent
  from langchain.agents.middleware import wrap_tool_call
  from langchain.messages import ToolMessage
  from langchain.tools.tool_node import ToolCallRequest

  @wrap_tool_call
  def handle_tool_errors(
      request: ToolCallRequest,
      handler: Callable[[ToolCallRequest], ToolMessage],
  ) -> ToolMessage:
      """Convert tool exceptions into ToolMessages the model can handle."""
      try:
          return handler(request)
      except Exception as e:
          return ToolMessage(
              content=f"Tool error: Please check your input and try again. ({e})",
              tool_call_id=request.tool_call["id"],
          )

  agent = create_agent(
      model="openai:gpt-5.5",
      tools=[],
      middleware=[handle_tool_errors],
  )
  ```

  ```python Anthropic theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from collections.abc import Callable

  from langchain.agents import create_agent
  from langchain.agents.middleware import wrap_tool_call
  from langchain.messages import ToolMessage
  from langchain.tools.tool_node import ToolCallRequest

  @wrap_tool_call
  def handle_tool_errors(
      request: ToolCallRequest,
      handler: Callable[[ToolCallRequest], ToolMessage],
  ) -> ToolMessage:
      """Convert tool exceptions into ToolMessages the model can handle."""
      try:
          return handler(request)
      except Exception as e:
          return ToolMessage(
              content=f"Tool error: Please check your input and try again. ({e})",
              tool_call_id=request.tool_call["id"],
          )

  agent = create_agent(
      model="anthropic:claude-sonnet-4-6",
      tools=[],
      middleware=[handle_tool_errors],
  )
  ```

  ```python OpenRouter theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from collections.abc import Callable

  from langchain.agents import create_agent
  from langchain.agents.middleware import wrap_tool_call
  from langchain.messages import ToolMessage
  from langchain.tools.tool_node import ToolCallRequest

  @wrap_tool_call
  def handle_tool_errors(
      request: ToolCallRequest,
      handler: Callable[[ToolCallRequest], ToolMessage],
  ) -> ToolMessage:
      """Convert tool exceptions into ToolMessages the model can handle."""
      try:
          return handler(request)
      except Exception as e:
          return ToolMessage(
              content=f"Tool error: Please check your input and try again. ({e})",
              tool_call_id=request.tool_call["id"],
          )

  agent = create_agent(
      model="openrouter:anthropic/claude-sonnet-4-6",
      tools=[],
      middleware=[handle_tool_errors],
  )
  ```

  ```python Fireworks theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from collections.abc import Callable

  from langchain.agents import create_agent
  from langchain.agents.middleware import wrap_tool_call
  from langchain.messages import ToolMessage
  from langchain.tools.tool_node import ToolCallRequest

  @wrap_tool_call
  def handle_tool_errors(
      request: ToolCallRequest,
      handler: Callable[[ToolCallRequest], ToolMessage],
  ) -> ToolMessage:
      """Convert tool exceptions into ToolMessages the model can handle."""
      try:
          return handler(request)
      except Exception as e:
          return ToolMessage(
              content=f"Tool error: Please check your input and try again. ({e})",
              tool_call_id=request.tool_call["id"],
          )

  agent = create_agent(
      model="fireworks:accounts/fireworks/models/qwen3p5-397b-a17b",
      tools=[],
      middleware=[handle_tool_errors],
  )
  ```

  ```python Baseten theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from collections.abc import Callable

  from langchain.agents import create_agent
  from langchain.agents.middleware import wrap_tool_call
  from langchain.messages import ToolMessage
  from langchain.tools.tool_node import ToolCallRequest

  @wrap_tool_call
  def handle_tool_errors(
      request: ToolCallRequest,
      handler: Callable[[ToolCallRequest], ToolMessage],
  ) -> ToolMessage:
      """Convert tool exceptions into ToolMessages the model can handle."""
      try:
          return handler(request)
      except Exception as e:
          return ToolMessage(
              content=f"Tool error: Please check your input and try again. ({e})",
              tool_call_id=request.tool_call["id"],
          )

  agent = create_agent(
      model="baseten:zai-org/GLM-5",
      tools=[],
      middleware=[handle_tool_errors],
  )
  ```

  ```python Ollama theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from collections.abc import Callable

  from langchain.agents import create_agent
  from langchain.agents.middleware import wrap_tool_call
  from langchain.messages import ToolMessage
  from langchain.tools.tool_node import ToolCallRequest

  @wrap_tool_call
  def handle_tool_errors(
      request: ToolCallRequest,
      handler: Callable[[ToolCallRequest], ToolMessage],
  ) -> ToolMessage:
      """Convert tool exceptions into ToolMessages the model can handle."""
      try:
          return handler(request)
      except Exception as e:
          return ToolMessage(
              content=f"Tool error: Please check your input and try again. ({e})",
              tool_call_id=request.tool_call["id"],
          )

  agent = create_agent(
      model="ollama:devstral-2",
      tools=[],
      middleware=[handle_tool_errors],
  )
  ```
</CodeGroup>

### State injection

Tools access graph state through [`ToolRuntime`](https://reference.langchain.com/python/langchain/tools/#langchain.tools.ToolRuntime). See [Access context](#access-context) for state, context, store, and streaming APIs.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain.tools import tool, ToolRuntime

@tool
def get_message_count(runtime: ToolRuntime) -> str:
    """Get the number of messages in the conversation."""
    messages = runtime.state["messages"]
    return f"There are {len(messages)} messages."
```

For more details on accessing state, context, and long-term memory from tools, see [Access context](#access-context).

## Dynamic tool selection

With dynamic tools, the set of tools available to the agent is modified at runtime rather than defined all upfront. Not every tool is appropriate for every situation. Too many tools may overwhelm the model (overload context) and increase errors; too few limit capabilities. Dynamic tool selection enables adapting the available toolset based on authentication state, user permissions, feature flags, or conversation stage.

There are two approaches depending on whether tools are known ahead of time:

<Tabs>
  <Tab title="Filtering pre-registered tools">
    When all possible tools are known at agent creation time, you can pre-register them and dynamically filter which ones are exposed to the model based on state, permissions, or context.

    <Tabs>
      <Tab title="State">
        Enable advanced tools only after certain conversation milestones:

        ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
        from langchain.agents import create_agent
        from langchain.agents.middleware import wrap_model_call, ModelRequest, ModelResponse
        from typing import Callable

        @wrap_model_call
        def state_based_tools(
            request: ModelRequest,
            handler: Callable[[ModelRequest], ModelResponse]
        ) -> ModelResponse:
            """Filter tools based on conversation State."""
            # Read from State: check if user has authenticated
            state = request.state
            is_authenticated = state.get("authenticated", False)
            message_count = len(state["messages"])

            # Only enable sensitive tools after authentication
            if not is_authenticated:
                tools = [t for t in request.tools if t.name.startswith("public_")]
                request = request.override(tools=tools)
            elif message_count < 5:
                # Limit tools early in conversation
                tools = [t for t in request.tools if t.name != "advanced_search"]
                request = request.override(tools=tools)

            return handler(request)

        agent = create_agent(
            model="gpt-5.5",
            tools=[public_search, private_search, advanced_search],
            middleware=[state_based_tools]
        )
        ```
      </Tab>

      <Tab title="Store">
        Filter tools based on user preferences or feature flags in Store:

        ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
        from dataclasses import dataclass
        from langchain.agents import create_agent
        from langchain.agents.middleware import wrap_model_call, ModelRequest, ModelResponse
        from typing import Callable
        from langgraph.store.memory import InMemoryStore

        @dataclass
        class Context:
            user_id: str

        @wrap_model_call
        def store_based_tools(
            request: ModelRequest,
            handler: Callable[[ModelRequest], ModelResponse]
        ) -> ModelResponse:
            """Filter tools based on Store preferences."""
            user_id = request.runtime.context.user_id

            # Read from Store: get user's enabled features
            store = request.runtime.store
            feature_flags = store.get(("features",), user_id)

            if feature_flags:
                enabled_features = feature_flags.value.get("enabled_tools", [])
                # Only include tools that are enabled for this user
                tools = [t for t in request.tools if t.name in enabled_features]
                request = request.override(tools=tools)

            return handler(request)

        agent = create_agent(
            model="gpt-5.5",
            tools=[search_tool, analysis_tool, export_tool],
            middleware=[store_based_tools],
            context_schema=Context,
            store=InMemoryStore()
        )
        ```
      </Tab>

      <Tab title="Runtime Context">
        Filter tools based on user permissions from Runtime Context:

        ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
        from dataclasses import dataclass
        from langchain.agents import create_agent
        from langchain.agents.middleware import wrap_model_call, ModelRequest, ModelResponse
        from typing import Callable

        @dataclass
        class Context:
            user_role: str

        @wrap_model_call
        def context_based_tools(
            request: ModelRequest,
            handler: Callable[[ModelRequest], ModelResponse]
        ) -> ModelResponse:
            """Filter tools based on Runtime Context permissions."""
            # Read from Runtime Context: get user role
            if request.runtime is None or request.runtime.context is None:
                # If no context provided, default to viewer (most restrictive)
                user_role = "viewer"
            else:
                user_role = request.runtime.context.user_role

            if user_role == "admin":
                # Admins get all tools
                pass
            elif user_role == "editor":
                # Editors can't delete
                tools = [t for t in request.tools if t.name != "delete_data"]
                request = request.override(tools=tools)
            else:
                # Viewers get read-only tools
                tools = [t for t in request.tools if t.name.startswith("read_")]
                request = request.override(tools=tools)

            return handler(request)

        agent = create_agent(
            model="gpt-5.5",
            tools=[read_data, write_data, delete_data],
            middleware=[context_based_tools],
            context_schema=Context
        )
        ```
      </Tab>
    </Tabs>

    This approach is best when:

    * All possible tools are known at compile/startup time
    * You want to filter based on permissions, feature flags, or conversation state
    * Tools are static but their availability is dynamic

    See [Dynamically selecting tools](/oss/python/langchain/middleware/custom#dynamically-selecting-tools) for more examples.
  </Tab>

  <Tab title="Runtime tool registration">
    When tools are discovered or created at runtime (e.g., loaded from an MCP server, generated based on user data, or fetched from a remote registry), you need to both register the tools and handle their execution dynamically.

    This requires two middleware hooks:

    1. `wrap_model_call` - Add the dynamic tools to the request
    2. `wrap_tool_call` - Handle execution of the dynamically added tools

    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    from langchain.tools import tool
    from langchain.agents import create_agent
    from langchain.agents.middleware import AgentMiddleware, ModelRequest, ToolCallRequest

    # A tool that will be added dynamically at runtime
    @tool
    def calculate_tip(bill_amount: float, tip_percentage: float = 20.0) -> str:
        """Calculate the tip amount for a bill."""
        tip = bill_amount * (tip_percentage / 100)
        return f"Tip: ${tip:.2f}, Total: ${bill_amount + tip:.2f}"

    class DynamicToolMiddleware(AgentMiddleware):
        """Middleware that registers and handles dynamic tools."""

        def wrap_model_call(self, request: ModelRequest, handler):
            # Add dynamic tool to the request
            # This could be loaded from an MCP server, database, etc.
            updated = request.override(tools=[*request.tools, calculate_tip])
            return handler(updated)

        def wrap_tool_call(self, request: ToolCallRequest, handler):
            # Handle execution of the dynamic tool
            if request.tool_call["name"] == "calculate_tip":
                return handler(request.override(tool=calculate_tip))
            return handler(request)

    agent = create_agent(
        model="gpt-4o",
        tools=[get_weather],  # Only static tools registered here
        middleware=[DynamicToolMiddleware()],
    )

    # The agent can now use both get_weather AND calculate_tip
    result = agent.invoke({
        "messages": [{"role": "user", "content": "Calculate a 20% tip on $85"}]
    })
    ```

    This approach is best when:

    * Tools are discovered at runtime (e.g., from an MCP server)
    * Tools are generated dynamically based on user data or configuration
    * You're integrating with external tool registries

    <Note>
      The `wrap_tool_call` hook is required for runtime-registered tools because the agent needs to know how to execute tools that weren't in the original tool list. Without it, the agent won't know how to invoke the dynamically added tool.
    </Note>
  </Tab>
</Tabs>

## Headless tools

Some tools should run **where your user's app runs** (typically the browser), not inside the process. **Headless tools** are tool definitions, which include the name, description, and argument schema, that you register on the **server** with your agent. The **implementation** is registered only on the **client** and executed after a short interrupt/resume handshake.

This is different from ordinary tools whose function body runs on the server, and from [server-side tool use](#server-side-tool-use) where the model provider executes built-in tools remotely.

### When to use headless tools

Use them when the work depends on the **environment, device, or UI** that only exists on the client. For example:

* **Browser APIs:** Geolocation, IndexedDB, Clipboard, Canvas 2D, file pickers, Battery API, etc.
* **Privacy and locality:** Data stays on the device (for example, local “memory” in IndexedDB).
* **Latency:** No extra server round trip for purely local operations.
* **Structured, safe effects:** Prefer many small, typed tools (for example one tool per canvas primitive) instead of sending arbitrary code to `eval`.

### How the pattern works

In both runtimes, the model sees a normal tool it can call, but the actual execution happens outside the server process.

1. **Define** a headless tool with `tool(name=..., description=..., args_schema=...)` from `langchain.tools`. A headless tool is schema-only, with no in-process implementation.
2. **Register** that tool with `create_agent` or your LangGraph graph so the model can call it normally.
3. **Handle** the interrupt payload when the tool is invoked. Instead of running locally, the graph pauses with a payload shaped like `{"type": "tool", "tool_call": {"id", "name", "args"}}`.
4. **Resume** the graph after your app, another service, or a human step performs the action. For browser-based flows, you can mirror the schema in the frontend and attach `.implement(...)` there.

<Info>
  If you call `tool(...)` in Python with only `name`, `description`, and `args_schema`, LangChain returns a `HeadlessTool`. There is no `.implement()` API on the Python side.
</Info>

When the model issues a tool call for one of these tools, the run **interrupts** instead of executing the tool locally. Your app can inspect the payload, perform the action in the right environment (for example a browser, another service, or a human review step), then **resume** the graph with the tool result. When you use the supported JS SDK hooks, they can detect headless-tool interrupts, run the matching client implementation, and submit the resume command for you.

Use the optional **`onTool`** callback to observe lifecycle events (`start`, `success`, `error`) for UI feedback such as spinners or toasts.

<Card title="Headless tools frontend pattern" href="/oss/python/langchain/frontend/headless-tools" icon="device-desktop">
  See an end-to-end example of schema-only tools executed in the client with `useStream`.
</Card>

## Prebuilt tools

LangChain provides a large collection of prebuilt tools and toolkits for common tasks like web search, code interpretation, database access, and more. These ready-to-use tools can be directly integrated into your agents without writing custom code.

See the [tools and toolkits](/oss/python/integrations/tools) integration page for a complete list of available tools organized by category.

## Server-side tool use

Some chat models feature built-in tools that are executed server-side by the model provider. These include capabilities like web search and code interpreters that don't require you to define or host the tool logic.

Refer to the individual [chat model integration pages](/oss/python/integrations/providers) and the [tool calling documentation](/oss/python/langchain/models#server-side-tool-use) for details on enabling and using these built-in tools.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langchain/tools.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Agent Chat UI
Source: https://docs.langchain.com/oss/python/langchain/ui

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

Agent Chat UI can connect to both [local](/oss/python/langchain/studio) and [deployed agents](/oss/python/langchain/deploy).

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
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langchain/ui.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
