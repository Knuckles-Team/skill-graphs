# Long-term memory
Source: https://docs.langchain.com/oss/python/langchain/long-term-memory

Add long-term memory to LangChain agents to store and recall data across conversations and sessions

Long-term memory lets your agent store and recall information across different conversations and sessions.
Unlike [short-term memory](/oss/python/langchain/short-term-memory), which is scoped to a single thread, long-term memory persists across threads and can be recalled at any time.

Long-term memory is built on [LangGraph stores](/oss/python/langgraph/stores), which save data as JSON documents organized by namespace and key.

## Usage

To add long-term memory to an agent, create a store and pass it to [`create_agent`](https://reference.langchain.com/python/langchain/agents/factory/create_agent):

<Tabs>
  <Tab title="InMemoryStore">
    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    from langchain.agents import create_agent
    from langchain_core.runnables import Runnable
    from langgraph.store.memory import InMemoryStore

    # InMemoryStore saves data to an in-memory dictionary. Use a DB-backed store in production use.
    store = InMemoryStore()

    agent: Runnable = create_agent(
        "claude-sonnet-4-6",
        tools=[],
        store=store,
    )
    ```
  </Tab>

  <Tab title="PostgreSQL">
    ```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    pip install langgraph-checkpoint-postgres
    ```

    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    from langchain.agents import create_agent
    from langchain_core.runnables import Runnable
    from langgraph.store.postgres import PostgresStore  # type: ignore[import-not-found]

    DB_URI = "postgresql://postgres:postgres@localhost:5432/postgres?sslmode=disable"

    with PostgresStore.from_conn_string(DB_URI) as store:
        store.setup()
        agent: Runnable = create_agent(
            "claude-sonnet-4-6",
            tools=[],
            store=store,
        )
    ```
  </Tab>
</Tabs>

Tools can then read from and write to the store using the `runtime.store` parameter. See [Read long-term memory in tools](#read-long-term-memory-in-tools) and [Write long-term memory from tools](#write-long-term-memory-from-tools) for examples.

<Tip>
  For a deeper dive into memory types (semantic, episodic, procedural) and strategies for writing memories, see the [Memory conceptual guide](/oss/python/concepts/memory#long-term-memory).
</Tip>

## Memory storage

LangGraph stores long-term memories as JSON documents in a [store](/oss/python/langgraph/stores).

Each memory is organized under a custom `namespace` (similar to a folder) and a distinct `key` (like a file name). Namespaces often include user or org IDs or other labels that makes it easier to organize information.

This structure enables hierarchical organization of memories. Cross-namespace searching is then supported through content filters.

<Tabs>
  <Tab title="InMemoryStore">
    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    from collections.abc import Sequence

    from langgraph.store.base import IndexConfig
    from langgraph.store.memory import InMemoryStore

    def embed(texts: Sequence[str]) -> list[list[float]]:
        # Replace with an actual embedding function or LangChain embeddings object
        return [[1.0, 2.0] for _ in texts]

    # InMemoryStore saves data to an in-memory dictionary. Use a DB-backed store in production use.
    store = InMemoryStore(index=IndexConfig(embed=embed, dims=2))
    user_id = "my-user"
    application_context = "chitchat"
    namespace = (user_id, application_context)
    store.put(
        namespace,
        "a-memory",
        {
            "rules": [
                "User likes short, direct language",
                "User only speaks English & python",
            ],
            "my-key": "my-value",
        },
    )
    # get the "memory" by ID
    item = store.get(namespace, "a-memory")
    # search for "memories" within this namespace, filtering on content equivalence, sorted by vector similarity
    items = store.search(
        namespace, filter={"my-key": "my-value"}, query="language preferences"
    )
    ```
  </Tab>

  <Tab title="PostgreSQL">
    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    from collections.abc import Sequence

    from langgraph.store.base import IndexConfig
    from langgraph.store.postgres import PostgresStore  # type: ignore[import-not-found]

    def embed(texts: Sequence[str]) -> list[list[float]]:
        # Replace with an actual embedding function or LangChain embeddings object
        return [[1.0, 2.0] for _ in texts]

    DB_URI = "postgresql://postgres:postgres@localhost:5432/postgres?sslmode=disable"

    with PostgresStore.from_conn_string(
        DB_URI,
        index=IndexConfig(embed=embed, dims=2),  # type: ignore[arg-type]
    ) as store:
        store.setup()
        user_id = "my-user"
        application_context = "chitchat"
        namespace = (user_id, application_context)
        store.put(
            namespace,
            "a-memory",
            {
                "rules": [
                    "User likes short, direct language",
                    "User only speaks English & python",
                ],
                "my-key": "my-value",
            },
        )
        item = store.get(namespace, "a-memory")
        items = store.search(
            namespace, filter={"my-key": "my-value"}, query="language preferences"
        )
    ```
  </Tab>
</Tabs>

For more information about the memory store, see the [Persistence](/oss/python/langgraph/stores) guide.

## Read long-term memory in tools

<Tabs>
  <Tab title="InMemoryStore">
    <CodeGroup>
      ```python Google theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      from dataclasses import dataclass

      from langchain.agents import create_agent
      from langchain.tools import ToolRuntime, tool
      from langchain_core.runnables import Runnable
      from langgraph.store.memory import InMemoryStore

      @dataclass
      class Context:
          user_id: str

      # InMemoryStore saves data to an in-memory dictionary. Use a DB-backed store in production.
      store = InMemoryStore()

      # Write sample data to the store using the put method
      store.put(
          (
              "users",
          ),  # Namespace to group related data together (users namespace for user data)
          "user_123",  # Key within the namespace (user ID as key)
          {
              "name": "John Smith",
              "language": "English",
          },  # Data to store for the given user
      )

      @tool
      def get_user_info(runtime: ToolRuntime[Context]) -> str:
          """Look up user info."""
          # Access the store - same as that provided to `create_agent`
          assert runtime.store is not None
          user_id = runtime.context.user_id
          # Retrieve data from store - returns StoreValue object with value and metadata
          user_info = runtime.store.get(("users",), user_id)
          return str(user_info.value) if user_info else "Unknown user"

      agent: Runnable = create_agent(
          model="google_genai:gemini-3.5-flash",
          tools=[get_user_info],
          # Pass store to agent - enables agent to access store when running tools
          store=store,
          context_schema=Context,
      )

      # Run the agent
      agent.invoke(
          {"messages": [{"role": "user", "content": "look up user information"}]},
          context=Context(user_id="user_123"),
      )
      ```

      ```python OpenAI theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      from dataclasses import dataclass

      from langchain.agents import create_agent
      from langchain.tools import ToolRuntime, tool
      from langchain_core.runnables import Runnable
      from langgraph.store.memory import InMemoryStore

      @dataclass
      class Context:
          user_id: str

      # InMemoryStore saves data to an in-memory dictionary. Use a DB-backed store in production.
      store = InMemoryStore()

      # Write sample data to the store using the put method
      store.put(
          (
              "users",
          ),  # Namespace to group related data together (users namespace for user data)
          "user_123",  # Key within the namespace (user ID as key)
          {
              "name": "John Smith",
              "language": "English",
          },  # Data to store for the given user
      )

      @tool
      def get_user_info(runtime: ToolRuntime[Context]) -> str:
          """Look up user info."""
          # Access the store - same as that provided to `create_agent`
          assert runtime.store is not None
          user_id = runtime.context.user_id
          # Retrieve data from store - returns StoreValue object with value and metadata
          user_info = runtime.store.get(("users",), user_id)
          return str(user_info.value) if user_info else "Unknown user"

      agent: Runnable = create_agent(
          model="openai:gpt-5.5",
          tools=[get_user_info],
          # Pass store to agent - enables agent to access store when running tools
          store=store,
          context_schema=Context,
      )

      # Run the agent
      agent.invoke(
          {"messages": [{"role": "user", "content": "look up user information"}]},
          context=Context(user_id="user_123"),
      )
      ```

      ```python Anthropic theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      from dataclasses import dataclass

      from langchain.agents import create_agent
      from langchain.tools import ToolRuntime, tool
      from langchain_core.runnables import Runnable
      from langgraph.store.memory import InMemoryStore

      @dataclass
      class Context:
          user_id: str

      # InMemoryStore saves data to an in-memory dictionary. Use a DB-backed store in production.
      store = InMemoryStore()

      # Write sample data to the store using the put method
      store.put(
          (
              "users",
          ),  # Namespace to group related data together (users namespace for user data)
          "user_123",  # Key within the namespace (user ID as key)
          {
              "name": "John Smith",
              "language": "English",
          },  # Data to store for the given user
      )

      @tool
      def get_user_info(runtime: ToolRuntime[Context]) -> str:
          """Look up user info."""
          # Access the store - same as that provided to `create_agent`
          assert runtime.store is not None
          user_id = runtime.context.user_id
          # Retrieve data from store - returns StoreValue object with value and metadata
          user_info = runtime.store.get(("users",), user_id)
          return str(user_info.value) if user_info else "Unknown user"

      agent: Runnable = create_agent(
          model="anthropic:claude-sonnet-4-6",
          tools=[get_user_info],
          # Pass store to agent - enables agent to access store when running tools
          store=store,
          context_schema=Context,
      )

      # Run the agent
      agent.invoke(
          {"messages": [{"role": "user", "content": "look up user information"}]},
          context=Context(user_id="user_123"),
      )
      ```

      ```python OpenRouter theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      from dataclasses import dataclass

      from langchain.agents import create_agent
      from langchain.tools import ToolRuntime, tool
      from langchain_core.runnables import Runnable
      from langgraph.store.memory import InMemoryStore

      @dataclass
      class Context:
          user_id: str

      # InMemoryStore saves data to an in-memory dictionary. Use a DB-backed store in production.
      store = InMemoryStore()

      # Write sample data to the store using the put method
      store.put(
          (
              "users",
          ),  # Namespace to group related data together (users namespace for user data)
          "user_123",  # Key within the namespace (user ID as key)
          {
              "name": "John Smith",
              "language": "English",
          },  # Data to store for the given user
      )

      @tool
      def get_user_info(runtime: ToolRuntime[Context]) -> str:
          """Look up user info."""
          # Access the store - same as that provided to `create_agent`
          assert runtime.store is not None
          user_id = runtime.context.user_id
          # Retrieve data from store - returns StoreValue object with value and metadata
          user_info = runtime.store.get(("users",), user_id)
          return str(user_info.value) if user_info else "Unknown user"

      agent: Runnable = create_agent(
          model="openrouter:anthropic/claude-sonnet-4-6",
          tools=[get_user_info],
          # Pass store to agent - enables agent to access store when running tools
          store=store,
          context_schema=Context,
      )

      # Run the agent
      agent.invoke(
          {"messages": [{"role": "user", "content": "look up user information"}]},
          context=Context(user_id="user_123"),
      )
      ```

      ```python Fireworks theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      from dataclasses import dataclass

      from langchain.agents import create_agent
      from langchain.tools import ToolRuntime, tool
      from langchain_core.runnables import Runnable
      from langgraph.store.memory import InMemoryStore

      @dataclass
      class Context:
          user_id: str

      # InMemoryStore saves data to an in-memory dictionary. Use a DB-backed store in production.
      store = InMemoryStore()

      # Write sample data to the store using the put method
      store.put(
          (
              "users",
          ),  # Namespace to group related data together (users namespace for user data)
          "user_123",  # Key within the namespace (user ID as key)
          {
              "name": "John Smith",
              "language": "English",
          },  # Data to store for the given user
      )

      @tool
      def get_user_info(runtime: ToolRuntime[Context]) -> str:
          """Look up user info."""
          # Access the store - same as that provided to `create_agent`
          assert runtime.store is not None
          user_id = runtime.context.user_id
          # Retrieve data from store - returns StoreValue object with value and metadata
          user_info = runtime.store.get(("users",), user_id)
          return str(user_info.value) if user_info else "Unknown user"

      agent: Runnable = create_agent(
          model="fireworks:accounts/fireworks/models/qwen3p5-397b-a17b",
          tools=[get_user_info],
          # Pass store to agent - enables agent to access store when running tools
          store=store,
          context_schema=Context,
      )

      # Run the agent
      agent.invoke(
          {"messages": [{"role": "user", "content": "look up user information"}]},
          context=Context(user_id="user_123"),
      )
      ```

      ```python Baseten theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      from dataclasses import dataclass

      from langchain.agents import create_agent
      from langchain.tools import ToolRuntime, tool
      from langchain_core.runnables import Runnable
      from langgraph.store.memory import InMemoryStore

      @dataclass
      class Context:
          user_id: str

      # InMemoryStore saves data to an in-memory dictionary. Use a DB-backed store in production.
      store = InMemoryStore()

      # Write sample data to the store using the put method
      store.put(
          (
              "users",
          ),  # Namespace to group related data together (users namespace for user data)
          "user_123",  # Key within the namespace (user ID as key)
          {
              "name": "John Smith",
              "language": "English",
          },  # Data to store for the given user
      )

      @tool
      def get_user_info(runtime: ToolRuntime[Context]) -> str:
          """Look up user info."""
          # Access the store - same as that provided to `create_agent`
          assert runtime.store is not None
          user_id = runtime.context.user_id
          # Retrieve data from store - returns StoreValue object with value and metadata
          user_info = runtime.store.get(("users",), user_id)
          return str(user_info.value) if user_info else "Unknown user"

      agent: Runnable = create_agent(
          model="baseten:zai-org/GLM-5",
          tools=[get_user_info],
          # Pass store to agent - enables agent to access store when running tools
          store=store,
          context_schema=Context,
      )

      # Run the agent
      agent.invoke(
          {"messages": [{"role": "user", "content": "look up user information"}]},
          context=Context(user_id="user_123"),
      )
      ```

      ```python Ollama theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      from dataclasses import dataclass

      from langchain.agents import create_agent
      from langchain.tools import ToolRuntime, tool
      from langchain_core.runnables import Runnable
      from langgraph.store.memory import InMemoryStore

      @dataclass
      class Context:
          user_id: str

      # InMemoryStore saves data to an in-memory dictionary. Use a DB-backed store in production.
      store = InMemoryStore()

      # Write sample data to the store using the put method
      store.put(
          (
              "users",
          ),  # Namespace to group related data together (users namespace for user data)
          "user_123",  # Key within the namespace (user ID as key)
          {
              "name": "John Smith",
              "language": "English",
          },  # Data to store for the given user
      )

      @tool
      def get_user_info(runtime: ToolRuntime[Context]) -> str:
          """Look up user info."""
          # Access the store - same as that provided to `create_agent`
          assert runtime.store is not None
          user_id = runtime.context.user_id
          # Retrieve data from store - returns StoreValue object with value and metadata
          user_info = runtime.store.get(("users",), user_id)
          return str(user_info.value) if user_info else "Unknown user"

      agent: Runnable = create_agent(
          model="ollama:devstral-2",
          tools=[get_user_info],
          # Pass store to agent - enables agent to access store when running tools
          store=store,
          context_schema=Context,
      )

      # Run the agent
      agent.invoke(
          {"messages": [{"role": "user", "content": "look up user information"}]},
          context=Context(user_id="user_123"),
      )
      ```
    </CodeGroup>
  </Tab>

  <Tab title="PostgreSQL">
    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    from dataclasses import dataclass

    from langchain.agents import create_agent
    from langchain.tools import ToolRuntime, tool
    from langchain_core.runnables import Runnable
    from langgraph.store.postgres import PostgresStore  # type: ignore[import-not-found]

    @dataclass
    class Context:
        user_id: str

    DB_URI = "postgresql://postgres:postgres@localhost:5432/postgres?sslmode=disable"

    with PostgresStore.from_conn_string(DB_URI) as store:
        store.setup()
        store.put(("users",), "user_123", {"name": "John Smith", "language": "English"})

        @tool
        def get_user_info(runtime: ToolRuntime[Context]) -> str:
            """Look up user info."""
            assert runtime.store is not None
            user_info = runtime.store.get(("users",), runtime.context.user_id)
            return str(user_info.value) if user_info else "Unknown user"

        agent: Runnable = create_agent(
            "claude-sonnet-4-6",
            tools=[get_user_info],
            store=store,
            context_schema=Context,
        )

        result = agent.invoke(
            {"messages": [{"role": "user", "content": "look up user information"}]},
            context=Context(user_id="user_123"),
        )
    ```
  </Tab>
</Tabs>

<a />

## Write long-term memory from tools

<Tabs>
  <Tab title="InMemoryStore">
    <CodeGroup>
      ```python Google theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      from dataclasses import dataclass

      from langchain.agents import create_agent
      from langchain.tools import ToolRuntime, tool
      from langchain_core.runnables import Runnable
      from langgraph.store.memory import InMemoryStore
      from typing_extensions import TypedDict

      # InMemoryStore saves data to an in-memory dictionary. Use a DB-backed store in production.
      store = InMemoryStore()

      @dataclass
      class Context:
          user_id: str

      # TypedDict defines the structure of user information for the LLM
      class UserInfo(TypedDict):
          name: str

      # Tool that allows agent to update user information (useful for chat applications)
      @tool
      def save_user_info(user_info: UserInfo, runtime: ToolRuntime[Context]) -> str:
          """Save user info."""
          # Access the store - same as that provided to `create_agent`
          assert runtime.store is not None
          store = runtime.store
          user_id = runtime.context.user_id
          # Store data in the store (namespace, key, data)
          store.put(("users",), user_id, dict(user_info))
          return "Successfully saved user info."

      agent: Runnable = create_agent(
          model="google_genai:gemini-3.5-flash",
          tools=[save_user_info],
          store=store,
          context_schema=Context,
      )

      # Run the agent
      agent.invoke(
          {"messages": [{"role": "user", "content": "My name is John Smith"}]},
          # user_id passed in context to identify whose information is being updated
          context=Context(user_id="user_123"),
      )

      # You can access the store directly to get the value
      item = store.get(("users",), "user_123")
      ```

      ```python OpenAI theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      from dataclasses import dataclass

      from langchain.agents import create_agent
      from langchain.tools import ToolRuntime, tool
      from langchain_core.runnables import Runnable
      from langgraph.store.memory import InMemoryStore
      from typing_extensions import TypedDict

      # InMemoryStore saves data to an in-memory dictionary. Use a DB-backed store in production.
      store = InMemoryStore()

      @dataclass
      class Context:
          user_id: str

      # TypedDict defines the structure of user information for the LLM
      class UserInfo(TypedDict):
          name: str

      # Tool that allows agent to update user information (useful for chat applications)
      @tool
      def save_user_info(user_info: UserInfo, runtime: ToolRuntime[Context]) -> str:
          """Save user info."""
          # Access the store - same as that provided to `create_agent`
          assert runtime.store is not None
          store = runtime.store
          user_id = runtime.context.user_id
          # Store data in the store (namespace, key, data)
          store.put(("users",), user_id, dict(user_info))
          return "Successfully saved user info."

      agent: Runnable = create_agent(
          model="openai:gpt-5.5",
          tools=[save_user_info],
          store=store,
          context_schema=Context,
      )

      # Run the agent
      agent.invoke(
          {"messages": [{"role": "user", "content": "My name is John Smith"}]},
          # user_id passed in context to identify whose information is being updated
          context=Context(user_id="user_123"),
      )

      # You can access the store directly to get the value
      item = store.get(("users",), "user_123")
      ```

      ```python Anthropic theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      from dataclasses import dataclass

      from langchain.agents import create_agent
      from langchain.tools import ToolRuntime, tool
      from langchain_core.runnables import Runnable
      from langgraph.store.memory import InMemoryStore
      from typing_extensions import TypedDict

      # InMemoryStore saves data to an in-memory dictionary. Use a DB-backed store in production.
      store = InMemoryStore()

      @dataclass
      class Context:
          user_id: str

      # TypedDict defines the structure of user information for the LLM
      class UserInfo(TypedDict):
          name: str

      # Tool that allows agent to update user information (useful for chat applications)
      @tool
      def save_user_info(user_info: UserInfo, runtime: ToolRuntime[Context]) -> str:
          """Save user info."""
          # Access the store - same as that provided to `create_agent`
          assert runtime.store is not None
          store = runtime.store
          user_id = runtime.context.user_id
          # Store data in the store (namespace, key, data)
          store.put(("users",), user_id, dict(user_info))
          return "Successfully saved user info."

      agent: Runnable = create_agent(
          model="anthropic:claude-sonnet-4-6",
          tools=[save_user_info],
          store=store,
          context_schema=Context,
      )

      # Run the agent
      agent.invoke(
          {"messages": [{"role": "user", "content": "My name is John Smith"}]},
          # user_id passed in context to identify whose information is being updated
          context=Context(user_id="user_123"),
      )

      # You can access the store directly to get the value
      item = store.get(("users",), "user_123")
      ```

      ```python OpenRouter theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      from dataclasses import dataclass

      from langchain.agents import create_agent
      from langchain.tools import ToolRuntime, tool
      from langchain_core.runnables import Runnable
      from langgraph.store.memory import InMemoryStore
      from typing_extensions import TypedDict

      # InMemoryStore saves data to an in-memory dictionary. Use a DB-backed store in production.
      store = InMemoryStore()

      @dataclass
      class Context:
          user_id: str

      # TypedDict defines the structure of user information for the LLM
      class UserInfo(TypedDict):
          name: str

      # Tool that allows agent to update user information (useful for chat applications)
      @tool
      def save_user_info(user_info: UserInfo, runtime: ToolRuntime[Context]) -> str:
          """Save user info."""
          # Access the store - same as that provided to `create_agent`
          assert runtime.store is not None
          store = runtime.store
          user_id = runtime.context.user_id
          # Store data in the store (namespace, key, data)
          store.put(("users",), user_id, dict(user_info))
          return "Successfully saved user info."

      agent: Runnable = create_agent(
          model="openrouter:anthropic/claude-sonnet-4-6",
          tools=[save_user_info],
          store=store,
          context_schema=Context,
      )

      # Run the agent
      agent.invoke(
          {"messages": [{"role": "user", "content": "My name is John Smith"}]},
          # user_id passed in context to identify whose information is being updated
          context=Context(user_id="user_123"),
      )

      # You can access the store directly to get the value
      item = store.get(("users",), "user_123")
      ```

      ```python Fireworks theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      from dataclasses import dataclass

      from langchain.agents import create_agent
      from langchain.tools import ToolRuntime, tool
      from langchain_core.runnables import Runnable
      from langgraph.store.memory import InMemoryStore
      from typing_extensions import TypedDict

      # InMemoryStore saves data to an in-memory dictionary. Use a DB-backed store in production.
      store = InMemoryStore()

      @dataclass
      class Context:
          user_id: str

      # TypedDict defines the structure of user information for the LLM
      class UserInfo(TypedDict):
          name: str

      # Tool that allows agent to update user information (useful for chat applications)
      @tool
      def save_user_info(user_info: UserInfo, runtime: ToolRuntime[Context]) -> str:
          """Save user info."""
          # Access the store - same as that provided to `create_agent`
          assert runtime.store is not None
          store = runtime.store
          user_id = runtime.context.user_id
          # Store data in the store (namespace, key, data)
          store.put(("users",), user_id, dict(user_info))
          return "Successfully saved user info."

      agent: Runnable = create_agent(
          model="fireworks:accounts/fireworks/models/qwen3p5-397b-a17b",
          tools=[save_user_info],
          store=store,
          context_schema=Context,
      )

      # Run the agent
      agent.invoke(
          {"messages": [{"role": "user", "content": "My name is John Smith"}]},
          # user_id passed in context to identify whose information is being updated
          context=Context(user_id="user_123"),
      )

      # You can access the store directly to get the value
      item = store.get(("users",), "user_123")
      ```

      ```python Baseten theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      from dataclasses import dataclass

      from langchain.agents import create_agent
      from langchain.tools import ToolRuntime, tool
      from langchain_core.runnables import Runnable
      from langgraph.store.memory import InMemoryStore
      from typing_extensions import TypedDict

      # InMemoryStore saves data to an in-memory dictionary. Use a DB-backed store in production.
      store = InMemoryStore()

      @dataclass
      class Context:
          user_id: str

      # TypedDict defines the structure of user information for the LLM
      class UserInfo(TypedDict):
          name: str

      # Tool that allows agent to update user information (useful for chat applications)
      @tool
      def save_user_info(user_info: UserInfo, runtime: ToolRuntime[Context]) -> str:
          """Save user info."""
          # Access the store - same as that provided to `create_agent`
          assert runtime.store is not None
          store = runtime.store
          user_id = runtime.context.user_id
          # Store data in the store (namespace, key, data)
          store.put(("users",), user_id, dict(user_info))
          return "Successfully saved user info."

      agent: Runnable = create_agent(
          model="baseten:zai-org/GLM-5",
          tools=[save_user_info],
          store=store,
          context_schema=Context,
      )

      # Run the agent
      agent.invoke(
          {"messages": [{"role": "user", "content": "My name is John Smith"}]},
          # user_id passed in context to identify whose information is being updated
          context=Context(user_id="user_123"),
      )

      # You can access the store directly to get the value
      item = store.get(("users",), "user_123")
      ```

      ```python Ollama theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      from dataclasses import dataclass

      from langchain.agents import create_agent
      from langchain.tools import ToolRuntime, tool
      from langchain_core.runnables import Runnable
      from langgraph.store.memory import InMemoryStore
      from typing_extensions import TypedDict

      # InMemoryStore saves data to an in-memory dictionary. Use a DB-backed store in production.
      store = InMemoryStore()

      @dataclass
      class Context:
          user_id: str

      # TypedDict defines the structure of user information for the LLM
      class UserInfo(TypedDict):
          name: str

      # Tool that allows agent to update user information (useful for chat applications)
      @tool
      def save_user_info(user_info: UserInfo, runtime: ToolRuntime[Context]) -> str:
          """Save user info."""
          # Access the store - same as that provided to `create_agent`
          assert runtime.store is not None
          store = runtime.store
          user_id = runtime.context.user_id
          # Store data in the store (namespace, key, data)
          store.put(("users",), user_id, dict(user_info))
          return "Successfully saved user info."

      agent: Runnable = create_agent(
          model="ollama:devstral-2",
          tools=[save_user_info],
          store=store,
          context_schema=Context,
      )

      # Run the agent
      agent.invoke(
          {"messages": [{"role": "user", "content": "My name is John Smith"}]},
          # user_id passed in context to identify whose information is being updated
          context=Context(user_id="user_123"),
      )

      # You can access the store directly to get the value
      item = store.get(("users",), "user_123")
      ```
    </CodeGroup>
  </Tab>

  <Tab title="PostgreSQL">
    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    from dataclasses import dataclass

    from langchain.agents import create_agent
    from langchain.tools import ToolRuntime, tool
    from langchain_core.runnables import Runnable
    from langgraph.store.postgres import PostgresStore  # type: ignore[import-not-found]
    from typing_extensions import TypedDict

    @dataclass
    class Context:
        user_id: str

    class UserInfo(TypedDict):
        name: str

    @tool
    def save_user_info(user_info: UserInfo, runtime: ToolRuntime[Context]) -> str:
        """Save user info."""
        assert runtime.store is not None
        runtime.store.put(("users",), runtime.context.user_id, dict(user_info))
        return "Successfully saved user info."

    DB_URI = "postgresql://postgres:postgres@localhost:5432/postgres?sslmode=disable"

    with PostgresStore.from_conn_string(DB_URI) as store:
        store.setup()
        agent: Runnable = create_agent(
            "claude-sonnet-4-6",
            tools=[save_user_info],
            store=store,
            context_schema=Context,
        )

        agent.invoke(
            {"messages": [{"role": "user", "content": "My name is John Smith"}]},
            context=Context(user_id="user_123"),
        )
    ```
  </Tab>
</Tabs>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langchain/long-term-memory.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Model Context Protocol (MCP)
Source: https://docs.langchain.com/oss/python/langchain/mcp

[Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction) is an open protocol that standardizes how applications provide tools and context to LLMs. LangChain agents can use tools defined on MCP servers using the [`langchain-mcp-adapters`](https://github.com/langchain-ai/langchain-mcp-adapters) library.

## Quickstart

Install the `langchain-mcp-adapters` library:

<CodeGroup>
  ```bash pip theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  pip install langchain-mcp-adapters
  ```

  ```bash uv theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  uv add langchain-mcp-adapters
  ```
</CodeGroup>

`langchain-mcp-adapters` enables agents to use tools defined across one or more MCP servers.

<Note>
  `MultiServerMCPClient` is **stateless by default**. Each tool invocation creates a fresh MCP `ClientSession`, executes the tool, and then cleans up. See the [stateful sessions](#stateful-sessions) section for more details.
</Note>

```python Accessing multiple MCP servers icon="server" theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient  # [!code highlight]
from langchain.agents import create_agent

async def main():
    client = MultiServerMCPClient(  # [!code highlight]
        {
            "math": {
                "transport": "stdio",  # Local subprocess communication
                "command": "python",
                # Absolute path to your math_server.py file
                "args": ["/path/to/math_server.py"],
            },
            "weather": {
                "transport": "http",  # HTTP-based remote server
                # Ensure you start your weather server on port 8000
                "url": "http://localhost:8000/mcp",
            }
        }
    )

    tools = await client.get_tools()  # [!code highlight]
    agent = create_agent(
        "claude-sonnet-4-6",
        tools  # [!code highlight]
    )
    math_response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "what's (3 + 5) x 12?"}]}
    )
    weather_response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "what is the weather in nyc?"}]}
    )
    print(math_response)
    print(weather_response)

if __name__ == "__main__":
    asyncio.run(main())
```

<Tip>
  Trace MCP tool calls alongside your agent's reasoning steps with [LangSmith](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=oss-langchain-mcp). Follow the [tracing quickstart](/langsmith/trace-with-langchain) to get set up.
</Tip>

## Custom servers

To create a custom MCP server, use the [FastMCP](https://gofastmcp.com/getting-started/welcome) library:

<CodeGroup>
  ```bash pip theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  pip install fastmcp
  ```

  ```bash uv theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  uv add fastmcp
  ```
</CodeGroup>

To test your agent with MCP tool servers, use the following examples:

<CodeGroup>
  ```python title="Math server (stdio transport)" icon="device-floppy" theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from fastmcp import FastMCP

  mcp = FastMCP("Math")

  @mcp.tool()
  def add(a: int, b: int) -> int:
      """Add two numbers"""
      return a + b

  @mcp.tool()
  def multiply(a: int, b: int) -> int:
      """Multiply two numbers"""
      return a * b

  if __name__ == "__main__":
      mcp.run(transport="stdio")
  ```

  ```python title="Weather server (streamable HTTP transport)" icon="wifi" theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from fastmcp import FastMCP

  mcp = FastMCP("Weather")

  @mcp.tool()
  async def get_weather(location: str) -> str:
      """Get weather for location."""
      return "It's always sunny in New York"

  if __name__ == "__main__":
      mcp.run(transport="streamable-http")
  ```
</CodeGroup>

## Transports

MCP supports different transport mechanisms for client-server communication.

### HTTP

The `http` transport (also referred to as `streamable-http`) uses HTTP requests for client-server communication. See the [MCP HTTP transport specification](https://modelcontextprotocol.io/specification/2025-03-26/basic/transports#streamable-http) for more details.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
client = MultiServerMCPClient(
    {
        "weather": {
            "transport": "http",
            "url": "http://localhost:8000/mcp",
        }
    }
)
```

#### Passing headers

When connecting to MCP servers over HTTP, you can include custom headers (e.g., for authentication or tracing) using the `headers` field in the connection configuration. This is supported for `sse` (deprecated by MCP spec) and `streamable_http` transports.

```python Passing headers with MultiServerMCPClient theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent

client = MultiServerMCPClient(
    {
        "weather": {
            "transport": "http",
            "url": "http://localhost:8000/mcp",
            "headers": {  # [!code highlight]
                "Authorization": "Bearer YOUR_TOKEN",  # [!code highlight]
                "X-Custom-Header": "custom-value"  # [!code highlight]
            },  # [!code highlight]
        }
    }
)
tools = await client.get_tools()
agent = create_agent("openai:gpt-5.5", tools)
response = await agent.ainvoke({"messages": "what is the weather in nyc?"})
```

#### Authentication

The `langchain-mcp-adapters` library uses the official [MCP SDK](https://github.com/modelcontextprotocol/python-sdk) under the hood, which allows you to provide a custom authentication mechanism by implementing the `httpx.Auth` interface.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain_mcp_adapters.client import MultiServerMCPClient

client = MultiServerMCPClient(
    {
        "weather": {
            "transport": "http",
            "url": "http://localhost:8000/mcp",
            "auth": auth, # [!code highlight]
        }
    }
)
```

* [Example custom auth implementation](https://github.com/modelcontextprotocol/python-sdk/blob/main/examples/clients/simple-auth-client/mcp_simple_auth_client/main.py)
* [Built-in OAuth flow](https://github.com/modelcontextprotocol/python-sdk/blob/main/src/mcp/client/auth/oauth2.py#L216)

### stdio

Client launches server as a subprocess and communicates via standard input/output. Best for local tools and simple setups.

<Note>
  Unlike HTTP transports, `stdio` connections are inherently **stateful**: the subprocess persists for the lifetime of the client connection. However, when using `MultiServerMCPClient` without explicit session management, each tool call still creates a new session. See [stateful sessions](#stateful-sessions) for managing persistent connections.
</Note>

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
client = MultiServerMCPClient(
    {
        "math": {
            "transport": "stdio",
            "command": "python",
            "args": ["/path/to/math_server.py"],
        }
    }
)
```

## Stateful sessions

By default, `MultiServerMCPClient` is **stateless**: each tool invocation creates a fresh MCP session, executes the tool, and then cleans up.

If you need to control the [lifecycle](https://modelcontextprotocol.io/specification/2025-03-26/basic/lifecycle) of an MCP session (for example, when working with a stateful server that maintains context across tool calls), you can create a persistent `ClientSession` using `client.session()`.

```python Using MCP ClientSession for stateful tool usage theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_mcp_adapters.tools import load_mcp_tools
from langchain.agents import create_agent

client = MultiServerMCPClient({...})

# Create a session explicitly
async with client.session("server_name") as session:  # [!code highlight]
    # Pass the session to load tools, resources, or prompts
    tools = await load_mcp_tools(session)  # [!code highlight]
    agent = create_agent(
        "google_genai:gemini-3.5-flash",
        tools
    )
```

## Core features

### Tools

[Tools](https://modelcontextprotocol.io/docs/concepts/tools) allow MCP servers to expose executable functions that LLMs can invoke to perform actions—such as querying databases, calling APIs, or interacting with external systems. LangChain converts MCP tools into LangChain [tools](/oss/python/langchain/tools), making them directly usable in any LangChain agent or workflow.

#### Loading tools

Use `client.get_tools()` to retrieve tools from MCP servers and pass them to your agent:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent

client = MultiServerMCPClient({...})
tools = await client.get_tools()  # [!code highlight]
agent = create_agent("claude-sonnet-4-6", tools)
```

By default, when an MCP tool fails, the error is passed back to the model as a tool message with `status="error"` instead of raising an exception. This lets the agent read the error and try again. To raise an exception instead, set `handle_tool_errors=False` on `MultiServerMCPClient` or `load_mcp_tools`.

This applies only to tool execution errors (`CallToolResult(isError=True)`). Transport, session, and content-conversion failures always raise.

<Note>
  Returning MCP tool errors as failed tool messages requires `langchain-mcp-adapters>=0.3.0`. Earlier versions raise a `ToolException`.
</Note>

#### Structured content

MCP tools can return [structured content](https://modelcontextprotocol.io/specification/2025-03-26/server/tools#structured-content) alongside the human-readable text response. This is useful when a tool needs to return machine-parseable data (like JSON) in addition to text that gets shown to the model.

When an MCP tool returns `structuredContent`, the adapter wraps it in an [`MCPToolArtifact`](https://reference.langchain.com/python/langchain_mcp_adapters/#langchain_mcp_adapters.tools.MCPToolArtifact) and returns it as the tool's artifact. You can access this using the `artifact` field on the `ToolMessage`. You can also use [interceptors](#tool-interceptors) to process or transform structured content automatically.

**Extracting structured content from artifact**

After invoking your agent, you can access the structured content from tool messages in the response:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent
from langchain.messages import ToolMessage

client = MultiServerMCPClient({...})
tools = await client.get_tools()
agent = create_agent("claude-sonnet-4-6", tools)

result = await agent.ainvoke(
    {"messages": [{"role": "user", "content": "Get data from the server"}]}
)
