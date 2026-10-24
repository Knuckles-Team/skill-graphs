# Pass context at invocation time
graph.invoke(
    {"messages": [{"role": "user", "content": "hi"}]},
    {"configurable": {"thread_id": "1"}},
    context=Context(user_id="1"),  # [!code highlight]
)
```

### Use in production

In production, use a store backed by a database:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langgraph.store.postgres import PostgresStore

DB_URI = "postgresql://postgres:postgres@localhost:5432/postgres?sslmode=disable"
with PostgresStore.from_conn_string(DB_URI) as store:  # [!code highlight]
    builder = StateGraph(...)
    graph = builder.compile(store=store)  # [!code highlight]
```

<Accordion title="Example: using Postgres store">
  ```
  pip install -U "psycopg[binary,pool]" langgraph langgraph-checkpoint-postgres
  ```

  <Tip>
    You need to call `store.setup()` the first time you're using Postgres store
  </Tip>

  <Tabs>
    <Tab title="Async">
      ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      from dataclasses import dataclass
      from langchain.chat_models import init_chat_model
      from langgraph.graph import StateGraph, MessagesState, START
      from langgraph.checkpoint.postgres.aio import AsyncPostgresSaver
      from langgraph.store.postgres.aio import AsyncPostgresStore  # [!code highlight]
      from langgraph.runtime import Runtime  # [!code highlight]
      import uuid

      model = init_chat_model(model="claude-haiku-4-5-20251001")

      @dataclass
      class Context:
          user_id: str

      async def call_model(  # [!code highlight]
          state: MessagesState,
          runtime: Runtime[Context],  # [!code highlight]
      ):
          user_id = runtime.context.user_id  # [!code highlight]
          namespace = ("memories", user_id)
          memories = await runtime.store.asearch(namespace, query=str(state["messages"][-1].content))  # [!code highlight]
          info = "\n".join([d.value["data"] for d in memories])
          system_msg = f"You are a helpful assistant talking to the user. User info: {info}"

          # Store new memories if the user asks the model to remember
          last_message = state["messages"][-1]
          if "remember" in last_message.content.lower():
              memory = "User name is Bob"
              await runtime.store.aput(namespace, str(uuid.uuid4()), {"data": memory})  # [!code highlight]

          response = await model.ainvoke(
              [{"role": "system", "content": system_msg}] + state["messages"]
          )
          return {"messages": response}

      DB_URI = "postgresql://postgres:postgres@localhost:5432/postgres?sslmode=disable"

      async with (
          AsyncPostgresStore.from_conn_string(DB_URI) as store,  # [!code highlight]
          AsyncPostgresSaver.from_conn_string(DB_URI) as checkpointer,
      ):
          # await store.setup()
          # await checkpointer.setup()

          builder = StateGraph(MessagesState, context_schema=Context)  # [!code highlight]
          builder.add_node(call_model)
          builder.add_edge(START, "call_model")

          graph = builder.compile(
              checkpointer=checkpointer,
              store=store,  # [!code highlight]
          )

          config = {"configurable": {"thread_id": "1"}}
          async for chunk in graph.astream(
              {"messages": [{"role": "user", "content": "Hi! Remember: my name is Bob"}]},
              config,
              stream_mode="values",
              context=Context(user_id="1"),  # [!code highlight]
          ):
              chunk["messages"][-1].pretty_print()

          config = {"configurable": {"thread_id": "2"}}
          async for chunk in graph.astream(
              {"messages": [{"role": "user", "content": "what is my name?"}]},
              config,
              stream_mode="values",
              context=Context(user_id="1"),  # [!code highlight]
          ):
              chunk["messages"][-1].pretty_print()
      ```
    </Tab>

    <Tab title="Sync">
      ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      from dataclasses import dataclass
      from langchain.chat_models import init_chat_model
      from langgraph.graph import StateGraph, MessagesState, START
      from langgraph.checkpoint.postgres import PostgresSaver
      from langgraph.store.postgres import PostgresStore  # [!code highlight]
      from langgraph.runtime import Runtime  # [!code highlight]
      import uuid

      model = init_chat_model(model="claude-haiku-4-5-20251001")

      @dataclass
      class Context:
          user_id: str

      def call_model(  # [!code highlight]
          state: MessagesState,
          runtime: Runtime[Context],  # [!code highlight]
      ):
          user_id = runtime.context.user_id  # [!code highlight]
          namespace = ("memories", user_id)
          memories = runtime.store.search(namespace, query=str(state["messages"][-1].content))  # [!code highlight]
          info = "\n".join([d.value["data"] for d in memories])
          system_msg = f"You are a helpful assistant talking to the user. User info: {info}"

          # Store new memories if the user asks the model to remember
          last_message = state["messages"][-1]
          if "remember" in last_message.content.lower():
              memory = "User name is Bob"
              runtime.store.put(namespace, str(uuid.uuid4()), {"data": memory})  # [!code highlight]

          response = model.invoke(
              [{"role": "system", "content": system_msg}] + state["messages"]
          )
          return {"messages": response}

      DB_URI = "postgresql://postgres:postgres@localhost:5432/postgres?sslmode=disable"

      with (
          PostgresStore.from_conn_string(DB_URI) as store,  # [!code highlight]
          PostgresSaver.from_conn_string(DB_URI) as checkpointer,
      ):
          # store.setup()
          # checkpointer.setup()

          builder = StateGraph(MessagesState, context_schema=Context)  # [!code highlight]
          builder.add_node(call_model)
          builder.add_edge(START, "call_model")

          graph = builder.compile(
              checkpointer=checkpointer,
              store=store,  # [!code highlight]
          )

          config = {"configurable": {"thread_id": "1"}}
          for chunk in graph.stream(
              {"messages": [{"role": "user", "content": "Hi! Remember: my name is Bob"}]},
              config,
              stream_mode="values",
              context=Context(user_id="1"),  # [!code highlight]
          ):
              chunk["messages"][-1].pretty_print()

          config = {"configurable": {"thread_id": "2"}}
          for chunk in graph.stream(
              {"messages": [{"role": "user", "content": "what is my name?"}]},
              config,
              stream_mode="values",
              context=Context(user_id="1"),  # [!code highlight]
          ):
              chunk["messages"][-1].pretty_print()
      ```
    </Tab>
  </Tabs>
</Accordion>

<Accordion title="Example: using MongoDB store" />

<Accordion title="Example: using Redis store">
  ```
  pip install -U langgraph langgraph-checkpoint-redis
  ```

  <Tip>
    You need to call `store.setup()` the first time you're using [Redis store](https://pypi.org/project/langgraph-checkpoint-redis/).
  </Tip>

  <Tabs>
    <Tab title="Async">
      ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      from dataclasses import dataclass
      from langchain.chat_models import init_chat_model
      from langgraph.graph import StateGraph, MessagesState, START
      from langgraph.checkpoint.redis.aio import AsyncRedisSaver
      from langgraph.store.redis.aio import AsyncRedisStore  # [!code highlight]
      from langgraph.runtime import Runtime  # [!code highlight]
      import uuid

      model = init_chat_model(model="claude-haiku-4-5-20251001")

      @dataclass
      class Context:
          user_id: str

      async def call_model(  # [!code highlight]
          state: MessagesState,
          runtime: Runtime[Context],  # [!code highlight]
      ):
          user_id = runtime.context.user_id  # [!code highlight]
          namespace = ("memories", user_id)
          memories = await runtime.store.asearch(namespace, query=str(state["messages"][-1].content))  # [!code highlight]
          info = "\n".join([d.value["data"] for d in memories])
          system_msg = f"You are a helpful assistant talking to the user. User info: {info}"

          # Store new memories if the user asks the model to remember
          last_message = state["messages"][-1]
          if "remember" in last_message.content.lower():
              memory = "User name is Bob"
              await runtime.store.aput(namespace, str(uuid.uuid4()), {"data": memory})  # [!code highlight]

          response = await model.ainvoke(
              [{"role": "system", "content": system_msg}] + state["messages"]
          )
          return {"messages": response}

      DB_URI = "redis://localhost:6379"

      async with (
          AsyncRedisStore.from_conn_string(DB_URI) as store,  # [!code highlight]
          AsyncRedisSaver.from_conn_string(DB_URI) as checkpointer,
      ):
          # await store.setup()
          # await checkpointer.asetup()

          builder = StateGraph(MessagesState, context_schema=Context)  # [!code highlight]
          builder.add_node(call_model)
          builder.add_edge(START, "call_model")

          graph = builder.compile(
              checkpointer=checkpointer,
              store=store,  # [!code highlight]
          )

          config = {"configurable": {"thread_id": "1"}}
          async for chunk in graph.astream(
              {"messages": [{"role": "user", "content": "Hi! Remember: my name is Bob"}]},
              config,
              stream_mode="values",
              context=Context(user_id="1"),  # [!code highlight]
          ):
              chunk["messages"][-1].pretty_print()

          config = {"configurable": {"thread_id": "2"}}
          async for chunk in graph.astream(
              {"messages": [{"role": "user", "content": "what is my name?"}]},
              config,
              stream_mode="values",
              context=Context(user_id="1"),  # [!code highlight]
          ):
              chunk["messages"][-1].pretty_print()
      ```
    </Tab>

    <Tab title="Sync">
      ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      from dataclasses import dataclass
      from langchain.chat_models import init_chat_model
      from langgraph.graph import StateGraph, MessagesState, START
      from langgraph.checkpoint.redis import RedisSaver
      from langgraph.store.redis import RedisStore  # [!code highlight]
      from langgraph.runtime import Runtime  # [!code highlight]
      import uuid

      model = init_chat_model(model="claude-haiku-4-5-20251001")

      @dataclass
      class Context:
          user_id: str

      def call_model(  # [!code highlight]
          state: MessagesState,
          runtime: Runtime[Context],  # [!code highlight]
      ):
          user_id = runtime.context.user_id  # [!code highlight]
          namespace = ("memories", user_id)
          memories = runtime.store.search(namespace, query=str(state["messages"][-1].content))  # [!code highlight]
          info = "\n".join([d.value["data"] for d in memories])
          system_msg = f"You are a helpful assistant talking to the user. User info: {info}"

          # Store new memories if the user asks the model to remember
          last_message = state["messages"][-1]
          if "remember" in last_message.content.lower():
              memory = "User name is Bob"
              runtime.store.put(namespace, str(uuid.uuid4()), {"data": memory})  # [!code highlight]

          response = model.invoke(
              [{"role": "system", "content": system_msg}] + state["messages"]
          )
          return {"messages": response}

      DB_URI = "redis://localhost:6379"

      with (
          RedisStore.from_conn_string(DB_URI) as store,  # [!code highlight]
          RedisSaver.from_conn_string(DB_URI) as checkpointer,
      ):
          store.setup()
          checkpointer.setup()

          builder = StateGraph(MessagesState, context_schema=Context)  # [!code highlight]
          builder.add_node(call_model)
          builder.add_edge(START, "call_model")

          graph = builder.compile(
              checkpointer=checkpointer,
              store=store,  # [!code highlight]
          )

          config = {"configurable": {"thread_id": "1"}}
          for chunk in graph.stream(
              {"messages": [{"role": "user", "content": "Hi! Remember: my name is Bob"}]},
              config,
              stream_mode="values",
              context=Context(user_id="1"),  # [!code highlight]
          ):
              chunk["messages"][-1].pretty_print()

          config = {"configurable": {"thread_id": "2"}}
          for chunk in graph.stream(
              {"messages": [{"role": "user", "content": "what is my name?"}]},
              config,
              stream_mode="values",
              context=Context(user_id="1"),  # [!code highlight]
          ):
              chunk["messages"][-1].pretty_print()
      ```
    </Tab>
  </Tabs>
</Accordion>

<Accordion title="Example: using Oracle store">
  ```
  pip install -U langgraph langgraph-oracledb langchain-openai
  ```

  <Note>
    **Setup**
    To use the [Oracle store](https://pypi.org/project/langgraph-oracledb/), you will need an Oracle AI Database instance — the vector index used for semantic `search` requires [Oracle AI Vector Search](https://docs.oracle.com/en/database/oracle/oracle-database/23/vecse/).
  </Note>

  <Tip>
    You need to call `store.setup()` and `checkpointer.setup()` the first time you're using the Oracle store and checkpointer.
  </Tip>

  <Tabs>
    <Tab title="Sync">
      ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import uuid

      from langchain.chat_models import init_chat_model
      from langchain.embeddings import init_embeddings
      from langchain_core.runnables import RunnableConfig
      from langgraph.graph import StateGraph, MessagesState, START
      from langgraph.store.base import BaseStore
      from langgraph_oracledb.checkpoint.oracle import OracleSaver
      from langgraph_oracledb.store.oracle import OracleStore  # [!code highlight]

      model = init_chat_model(model="claude-haiku-4-5-20251001")
      embeddings = init_embeddings("openai:text-embedding-3-small")

      DB_URI = "user/password@localhost:1521/FREEPDB1"

      with (
          OracleStore.from_conn_string(  # [!code highlight]
              DB_URI,
              index={"embed": embeddings, "dims": 1536},  # [!code highlight]
          ) as store,
          OracleSaver.from_conn_string(DB_URI) as checkpointer,
      ):
          store.setup()
          checkpointer.setup()

          def call_model(
              state: MessagesState,
              config: RunnableConfig,
              *,
              store: BaseStore,  # [!code highlight]
          ):
              user_id = config["configurable"]["user_id"]
              namespace = ("memories", user_id)
              memories = store.search(namespace, query=str(state["messages"][-1].content))  # [!code highlight]
              info = "\n".join([d.value["data"] for d in memories])
              system_msg = f"You are a helpful assistant talking to the user. User info: {info}"

              # Store new memories if the user asks the model to remember
              last_message = state["messages"][-1]
              if "remember" in last_message.content.lower():
                  memory = "User name is Bob"
                  store.put(namespace, str(uuid.uuid4()), {"data": memory})  # [!code highlight]

              response = model.invoke(
                  [{"role": "system", "content": system_msg}] + state["messages"]
              )
              return {"messages": response}

          builder = StateGraph(MessagesState)
          builder.add_node(call_model)
          builder.add_edge(START, "call_model")

          graph = builder.compile(
              checkpointer=checkpointer,
              store=store,  # [!code highlight]
          )

          config = {
              "configurable": {
                  "thread_id": "1",  # [!code highlight]
                  "user_id": "1",  # [!code highlight]
              }
          }
          for chunk in graph.stream(
              {"messages": [{"role": "user", "content": "Hi! Remember: my name is Bob"}]},
              config,  # [!code highlight]
              stream_mode="values",
          ):
              chunk["messages"][-1].pretty_print()

          config = {
              "configurable": {
                  "thread_id": "2",  # [!code highlight]
                  "user_id": "1",
              }
          }

          for chunk in graph.stream(
              {"messages": [{"role": "user", "content": "what is my name?"}]},
              config,  # [!code highlight]
              stream_mode="values",
          ):
              chunk["messages"][-1].pretty_print()
      ```
    </Tab>

    <Tab title="Async">
      ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import uuid

      from langchain.chat_models import init_chat_model
      from langchain.embeddings import init_embeddings
      from langchain_core.runnables import RunnableConfig
      from langgraph.graph import StateGraph, MessagesState, START
      from langgraph.store.base import BaseStore
      from langgraph_oracledb.checkpoint.oracle import AsyncOracleSaver
      from langgraph_oracledb.store.oracle import AsyncOracleStore  # [!code highlight]

      model = init_chat_model(model="claude-haiku-4-5-20251001")
      embeddings = init_embeddings("openai:text-embedding-3-small")

      DB_URI = "user/password@localhost:1521/FREEPDB1"

      async with (
          AsyncOracleStore.from_conn_string(  # [!code highlight]
              DB_URI,
              index={"embed": embeddings, "dims": 1536},  # [!code highlight]
          ) as store,
          AsyncOracleSaver.from_conn_string(DB_URI) as checkpointer,
      ):
          await store.setup()
          await checkpointer.setup()

          async def call_model(
              state: MessagesState,
              config: RunnableConfig,
              *,
              store: BaseStore,  # [!code highlight]
          ):
              user_id = config["configurable"]["user_id"]
              namespace = ("memories", user_id)
              memories = await store.asearch(namespace, query=str(state["messages"][-1].content))  # [!code highlight]
              info = "\n".join([d.value["data"] for d in memories])
              system_msg = f"You are a helpful assistant talking to the user. User info: {info}"

              # Store new memories if the user asks the model to remember
              last_message = state["messages"][-1]
              if "remember" in last_message.content.lower():
                  memory = "User name is Bob"
                  await store.aput(namespace, str(uuid.uuid4()), {"data": memory})  # [!code highlight]

              response = await model.ainvoke(
                  [{"role": "system", "content": system_msg}] + state["messages"]
              )
              return {"messages": response}

          builder = StateGraph(MessagesState)
          builder.add_node(call_model)
          builder.add_edge(START, "call_model")

          graph = builder.compile(
              checkpointer=checkpointer,
              store=store,  # [!code highlight]
          )

          config = {
              "configurable": {
                  "thread_id": "1",  # [!code highlight]
                  "user_id": "1",  # [!code highlight]
              }
          }
          async for chunk in graph.astream(
              {"messages": [{"role": "user", "content": "Hi! Remember: my name is Bob"}]},
              config,  # [!code highlight]
              stream_mode="values",
          ):
              chunk["messages"][-1].pretty_print()

          config = {
              "configurable": {
                  "thread_id": "2",  # [!code highlight]
                  "user_id": "1",
              }
          }

          async for chunk in graph.astream(
              {"messages": [{"role": "user", "content": "what is my name?"}]},
              config,  # [!code highlight]
              stream_mode="values",
          ):
              chunk["messages"][-1].pretty_print()
      ```
    </Tab>
  </Tabs>
</Accordion>

### Use semantic search

Enable semantic search in your graph's memory store to let graph agents search for items in the store by semantic similarity.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain.embeddings import init_embeddings
from langgraph.store.memory import InMemoryStore
