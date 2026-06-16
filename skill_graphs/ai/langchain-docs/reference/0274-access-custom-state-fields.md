# Access custom state fields
@tool
def get_user_preference(
    pref_name: str,
    runtime: ToolRuntime
) -> str:
    """Get a user preference value."""
    preferences = runtime.state.get("user_preferences", {})
    return preferences.get(pref_name, "Not set")
```

<Warning>
  The `runtime` parameter is hidden from the model. For the example above, the model only sees `pref_name` in the tool schema.
</Warning>

#### Update state

Use [`Command`](https://reference.langchain.com/python/langgraph/types/Command) to update the agent's state. This is useful for tools that need to update custom state fields.
Include a `ToolMessage` in the update so the model can see the result of the tool call:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain.agents import AgentState
from langchain.messages import ToolMessage
from langchain.tools import ToolRuntime, tool
from langgraph.types import Command

class CustomState(AgentState):
    user_name: str

@tool
def set_user_name(new_name: str, runtime: ToolRuntime[None, CustomState]) -> Command:
    """Set the user's name in the conversation state."""
    return Command(
        update={
            "user_name": new_name,
            "messages": [
                ToolMessage(
                    content=f"User name set to {new_name}.",
                    tool_call_id=runtime.tool_call_id,
                )
            ],
        }
    )
```

<Tip>
  When tools update state variables, consider defining a [reducer](/oss/python/langgraph/graph-api#reducers) for those fields. Since LLMs can call multiple tools in parallel, a reducer determines how to resolve conflicts when the same state field is updated by concurrent tool calls.
</Tip>

### Context

Context provides immutable configuration data that is passed at invocation time. Use it for user IDs, session details, or application-specific settings that shouldn't change during a conversation.

<Note>
  While `thread_id` (passed via `config={"configurable": {"thread_id": ...}}`) scopes the *conversation*: message history and checkpoints, `context` carries *per-run* data your tools and middleware read at invocation time. In production you typically pass both together: a stable `thread_id` per conversation, and a `context` object on every invoke.
</Note>

Access context through `runtime.context`. Pass it alongside a `thread_id` so the conversation is persisted across turns:

<CodeGroup>
  ```python Google theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from dataclasses import dataclass

  from langchain.agents import create_agent
  from langchain.tools import tool, ToolRuntime
  from langchain_core.utils.uuid import uuid7
  from langchain_openai import ChatOpenAI

  USER_DATABASE = {
      "user123": {
          "name": "Alice Johnson",
          "account_type": "Premium",
          "balance": 5000,
          "email": "alice@example.com",
      },
      "user456": {
          "name": "Bob Smith",
          "account_type": "Standard",
          "balance": 1200,
          "email": "bob@example.com",
      },
  }

  @dataclass
  class UserContext:
      user_id: str

  @tool
  def get_account_info(runtime: ToolRuntime[UserContext]) -> str:
      """Get the current user's account information."""
      user_id = runtime.context.user_id

      if user_id in USER_DATABASE:
          user = USER_DATABASE[user_id]
          return (
              f"Account holder: {user['name']}\n"
              f"Type: {user['account_type']}\n"
              f"Balance: ${user['balance']}"
          )
      return "User not found"

  model = ChatOpenAI(model="google_genai:gemini-3.5-flash")
  agent = create_agent(
      model,
      tools=[get_account_info],
      context_schema=UserContext,
      system_prompt="You are a financial assistant.",
  )

  result = agent.invoke(
      {"messages": [{"role": "user", "content": "What's my current balance?"}]},
      config={"configurable": {"thread_id": str(uuid7())}},
      context=UserContext(user_id="user123"),
  )
  ```

  ```python OpenAI theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from dataclasses import dataclass

  from langchain.agents import create_agent
  from langchain.tools import tool, ToolRuntime
  from langchain_core.utils.uuid import uuid7
  from langchain_openai import ChatOpenAI

  USER_DATABASE = {
      "user123": {
          "name": "Alice Johnson",
          "account_type": "Premium",
          "balance": 5000,
          "email": "alice@example.com",
      },
      "user456": {
          "name": "Bob Smith",
          "account_type": "Standard",
          "balance": 1200,
          "email": "bob@example.com",
      },
  }

  @dataclass
  class UserContext:
      user_id: str

  @tool
  def get_account_info(runtime: ToolRuntime[UserContext]) -> str:
      """Get the current user's account information."""
      user_id = runtime.context.user_id

      if user_id in USER_DATABASE:
          user = USER_DATABASE[user_id]
          return (
              f"Account holder: {user['name']}\n"
              f"Type: {user['account_type']}\n"
              f"Balance: ${user['balance']}"
          )
      return "User not found"

  model = ChatOpenAI(model="openai:gpt-5.5")
  agent = create_agent(
      model,
      tools=[get_account_info],
      context_schema=UserContext,
      system_prompt="You are a financial assistant.",
  )

  result = agent.invoke(
      {"messages": [{"role": "user", "content": "What's my current balance?"}]},
      config={"configurable": {"thread_id": str(uuid7())}},
      context=UserContext(user_id="user123"),
  )
  ```

  ```python Anthropic theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from dataclasses import dataclass

  from langchain.agents import create_agent
  from langchain.tools import tool, ToolRuntime
  from langchain_core.utils.uuid import uuid7
  from langchain_openai import ChatOpenAI

  USER_DATABASE = {
      "user123": {
          "name": "Alice Johnson",
          "account_type": "Premium",
          "balance": 5000,
          "email": "alice@example.com",
      },
      "user456": {
          "name": "Bob Smith",
          "account_type": "Standard",
          "balance": 1200,
          "email": "bob@example.com",
      },
  }

  @dataclass
  class UserContext:
      user_id: str

  @tool
  def get_account_info(runtime: ToolRuntime[UserContext]) -> str:
      """Get the current user's account information."""
      user_id = runtime.context.user_id

      if user_id in USER_DATABASE:
          user = USER_DATABASE[user_id]
          return (
              f"Account holder: {user['name']}\n"
              f"Type: {user['account_type']}\n"
              f"Balance: ${user['balance']}"
          )
      return "User not found"

  model = ChatOpenAI(model="anthropic:claude-sonnet-4-6")
  agent = create_agent(
      model,
      tools=[get_account_info],
      context_schema=UserContext,
      system_prompt="You are a financial assistant.",
  )

  result = agent.invoke(
      {"messages": [{"role": "user", "content": "What's my current balance?"}]},
      config={"configurable": {"thread_id": str(uuid7())}},
      context=UserContext(user_id="user123"),
  )
  ```

  ```python OpenRouter theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from dataclasses import dataclass

  from langchain.agents import create_agent
  from langchain.tools import tool, ToolRuntime
  from langchain_core.utils.uuid import uuid7
  from langchain_openai import ChatOpenAI

  USER_DATABASE = {
      "user123": {
          "name": "Alice Johnson",
          "account_type": "Premium",
          "balance": 5000,
          "email": "alice@example.com",
      },
      "user456": {
          "name": "Bob Smith",
          "account_type": "Standard",
          "balance": 1200,
          "email": "bob@example.com",
      },
  }

  @dataclass
  class UserContext:
      user_id: str

  @tool
  def get_account_info(runtime: ToolRuntime[UserContext]) -> str:
      """Get the current user's account information."""
      user_id = runtime.context.user_id

      if user_id in USER_DATABASE:
          user = USER_DATABASE[user_id]
          return (
              f"Account holder: {user['name']}\n"
              f"Type: {user['account_type']}\n"
              f"Balance: ${user['balance']}"
          )
      return "User not found"

  model = ChatOpenAI(model="openrouter:anthropic/claude-sonnet-4-6")
  agent = create_agent(
      model,
      tools=[get_account_info],
      context_schema=UserContext,
      system_prompt="You are a financial assistant.",
  )

  result = agent.invoke(
      {"messages": [{"role": "user", "content": "What's my current balance?"}]},
      config={"configurable": {"thread_id": str(uuid7())}},
      context=UserContext(user_id="user123"),
  )
  ```

  ```python Fireworks theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from dataclasses import dataclass

  from langchain.agents import create_agent
  from langchain.tools import tool, ToolRuntime
  from langchain_core.utils.uuid import uuid7
  from langchain_openai import ChatOpenAI

  USER_DATABASE = {
      "user123": {
          "name": "Alice Johnson",
          "account_type": "Premium",
          "balance": 5000,
          "email": "alice@example.com",
      },
      "user456": {
          "name": "Bob Smith",
          "account_type": "Standard",
          "balance": 1200,
          "email": "bob@example.com",
      },
  }

  @dataclass
  class UserContext:
      user_id: str

  @tool
  def get_account_info(runtime: ToolRuntime[UserContext]) -> str:
      """Get the current user's account information."""
      user_id = runtime.context.user_id

      if user_id in USER_DATABASE:
          user = USER_DATABASE[user_id]
          return (
              f"Account holder: {user['name']}\n"
              f"Type: {user['account_type']}\n"
              f"Balance: ${user['balance']}"
          )
      return "User not found"

  model = ChatOpenAI(model="fireworks:accounts/fireworks/models/qwen3p5-397b-a17b")
  agent = create_agent(
      model,
      tools=[get_account_info],
      context_schema=UserContext,
      system_prompt="You are a financial assistant.",
  )

  result = agent.invoke(
      {"messages": [{"role": "user", "content": "What's my current balance?"}]},
      config={"configurable": {"thread_id": str(uuid7())}},
      context=UserContext(user_id="user123"),
  )
  ```

  ```python Baseten theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from dataclasses import dataclass

  from langchain.agents import create_agent
  from langchain.tools import tool, ToolRuntime
  from langchain_core.utils.uuid import uuid7
  from langchain_openai import ChatOpenAI

  USER_DATABASE = {
      "user123": {
          "name": "Alice Johnson",
          "account_type": "Premium",
          "balance": 5000,
          "email": "alice@example.com",
      },
      "user456": {
          "name": "Bob Smith",
          "account_type": "Standard",
          "balance": 1200,
          "email": "bob@example.com",
      },
  }

  @dataclass
  class UserContext:
      user_id: str

  @tool
  def get_account_info(runtime: ToolRuntime[UserContext]) -> str:
      """Get the current user's account information."""
      user_id = runtime.context.user_id

      if user_id in USER_DATABASE:
          user = USER_DATABASE[user_id]
          return (
              f"Account holder: {user['name']}\n"
              f"Type: {user['account_type']}\n"
              f"Balance: ${user['balance']}"
          )
      return "User not found"

  model = ChatOpenAI(model="baseten:zai-org/GLM-5")
  agent = create_agent(
      model,
      tools=[get_account_info],
      context_schema=UserContext,
      system_prompt="You are a financial assistant.",
  )

  result = agent.invoke(
      {"messages": [{"role": "user", "content": "What's my current balance?"}]},
      config={"configurable": {"thread_id": str(uuid7())}},
      context=UserContext(user_id="user123"),
  )
  ```

  ```python Ollama theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from dataclasses import dataclass

  from langchain.agents import create_agent
  from langchain.tools import tool, ToolRuntime
  from langchain_core.utils.uuid import uuid7
  from langchain_openai import ChatOpenAI

  USER_DATABASE = {
      "user123": {
          "name": "Alice Johnson",
          "account_type": "Premium",
          "balance": 5000,
          "email": "alice@example.com",
      },
      "user456": {
          "name": "Bob Smith",
          "account_type": "Standard",
          "balance": 1200,
          "email": "bob@example.com",
      },
  }

  @dataclass
  class UserContext:
      user_id: str

  @tool
  def get_account_info(runtime: ToolRuntime[UserContext]) -> str:
      """Get the current user's account information."""
      user_id = runtime.context.user_id

      if user_id in USER_DATABASE:
          user = USER_DATABASE[user_id]
          return (
              f"Account holder: {user['name']}\n"
              f"Type: {user['account_type']}\n"
              f"Balance: ${user['balance']}"
          )
      return "User not found"

  model = ChatOpenAI(model="ollama:devstral-2")
  agent = create_agent(
      model,
      tools=[get_account_info],
      context_schema=UserContext,
      system_prompt="You are a financial assistant.",
  )

  result = agent.invoke(
      {"messages": [{"role": "user", "content": "What's my current balance?"}]},
      config={"configurable": {"thread_id": str(uuid7())}},
      context=UserContext(user_id="user123"),
  )
  ```
</CodeGroup>

### Long-term memory (Store)

The [`BaseStore`](https://reference.langchain.com/python/langchain-core/stores/BaseStore) provides persistent storage that survives across conversations. Unlike state (short-term memory), data saved to the store remains available in future sessions.

Access the store through `runtime.store`. The store uses a namespace/key pattern to organize data:

<Tip>
  For production deployments, use a persistent store implementation like [`PostgresStore`](https://reference.langchain.com/python/langgraph/store/#langgraph.store.postgres.PostgresStore) instead of `InMemoryStore`. See the [memory documentation](/oss/python/langgraph/add-memory) for setup details.
</Tip>

```python expandable theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from typing import Any
from langgraph.store.memory import InMemoryStore
from langchain.agents import create_agent
from langchain.tools import tool, ToolRuntime
from langchain_openai import ChatOpenAI

# Access memory
@tool
def get_user_info(user_id: str, runtime: ToolRuntime) -> str:
    """Look up user info."""
    store = runtime.store
    user_info = store.get(("users",), user_id)
    return str(user_info.value) if user_info else "Unknown user"

# Update memory
@tool
def save_user_info(user_id: str, user_info: dict[str, Any], runtime: ToolRuntime) -> str:
    """Save user info."""
    store = runtime.store
    store.put(("users",), user_id, user_info)
    return "Successfully saved user info."

model = ChatOpenAI(model="gpt-5.5")

store = InMemoryStore()
agent = create_agent(
    model,
    tools=[get_user_info, save_user_info],
    store=store
)

# First session: save user info
agent.invoke({
    "messages": [{"role": "user", "content": "Save the following user: userid: abc123, name: Foo, age: 25, email: foo@langchain.dev"}]
})

# Second session: get user info
agent.invoke({
    "messages": [{"role": "user", "content": "Get user info for user with id 'abc123'"}]
})

# Here is the user info for user with ID "abc123":

# - Name: Foo

# - Age: 25
