# Quickstart
Source: https://docs.langchain.com/oss/python/langgraph/quickstart

This quickstart demonstrates how to build a calculator agent using the LangGraph Graph API or the Functional API.

<Tip>
  **Using an AI coding assistant?**

  * Install the [LangChain Docs MCP server](/use-these-docs) to give your agent access to up-to-date LangChain documentation and examples.
  * Install [LangChain Skills](https://github.com/langchain-ai/langchain-skills) to improve your agent's performance on LangChain ecosystem tasks.
</Tip>

* [Use the Graph API](#use-the-graph-api) if you prefer to define your agent as a graph of nodes and edges.
* [Use the Functional API](#use-the-functional-api) if you prefer to define your agent as a single function.

For conceptual information, see [Graph API overview](/oss/python/langgraph/graph-api) and [Functional API overview](/oss/python/langgraph/functional-api).

<Info>
  For this example, you will need to set up a [Claude (Anthropic)](https://www.anthropic.com/) account and get an API key. Then, set the `ANTHROPIC_API_KEY` environment variable in your terminal.
</Info>

<Tabs>
  <Tab title="Use the Graph API">
    ## 1. Define tools and model

    In this example, we'll use the Claude Sonnet 4.5 model and define tools for addition, multiplication, and division.

    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    from langchain.tools import tool
    from langchain.chat_models import init_chat_model

    model = init_chat_model(
        "claude-sonnet-4-6",
        temperature=0
    )

    # Define tools
    @tool
    def multiply(a: int, b: int) -> int:
        """Multiply `a` and `b`.

        Args:
            a: First int
            b: Second int
        """
        return a * b

    @tool
    def add(a: int, b: int) -> int:
        """Adds `a` and `b`.

        Args:
            a: First int
            b: Second int
        """
        return a + b

    @tool
    def divide(a: int, b: int) -> float:
        """Divide `a` and `b`.

        Args:
            a: First int
            b: Second int
        """
        return a / b

    # Augment the LLM with tools
    tools = [add, multiply, divide]
    tools_by_name = {tool.name: tool for tool in tools}
    model_with_tools = model.bind_tools(tools)
    ```

    ## 2. Define state

    The graph's state is used to store the messages and the number of LLM calls.

    <Tip>
      State in LangGraph persists throughout the agent's execution.

      The `Annotated` type with `operator.add` ensures that new messages are appended to the existing list rather than replacing it.
    </Tip>

    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    from langchain.messages import AnyMessage
    from typing_extensions import TypedDict, Annotated
    import operator

    class MessagesState(TypedDict):
        messages: Annotated[list[AnyMessage], operator.add]
        llm_calls: int
    ```

    ## 3. Define model node

    The model node is used to call the LLM and decide whether to call a tool or not.

    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    from langchain.messages import SystemMessage

    def llm_call(state: dict):
        """LLM decides whether to call a tool or not"""

        return {
            "messages": [
                model_with_tools.invoke(
                    [
                        SystemMessage(
                            content="You are a helpful assistant tasked with performing arithmetic on a set of inputs."
                        )
                    ]
                    + state["messages"]
                )
            ],
            "llm_calls": state.get('llm_calls', 0) + 1
        }
    ```

    ## 4. Define tool node

    The tool node is used to call the tools and return the results.

    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    from langchain.messages import ToolMessage

    def tool_node(state: dict):
        """Performs the tool call"""

        result = []
        for tool_call in state["messages"][-1].tool_calls:
            tool = tools_by_name[tool_call["name"]]
            observation = tool.invoke(tool_call["args"])
            result.append(ToolMessage(content=observation, tool_call_id=tool_call["id"]))
        return {"messages": result}
    ```

    ## 5. Define end logic

    The conditional edge function is used to route to the tool node or end based upon whether the LLM made a tool call.

    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    from typing import Literal
    from langgraph.graph import StateGraph, START, END

    def should_continue(state: MessagesState) -> Literal["tool_node", END]:
        """Decide if we should continue the loop or stop based upon whether the LLM made a tool call"""

        messages = state["messages"]
        last_message = messages[-1]

        # If the LLM makes a tool call, then perform an action
        if last_message.tool_calls:
            return "tool_node"

        # Otherwise, we stop (reply to the user)
        return END
    ```

    ## 6. Build and compile the agent

    The agent is built using the [`StateGraph`](https://reference.langchain.com/python/langgraph/graph/state/StateGraph) class and compiled using the [`compile`](https://reference.langchain.com/python/langgraph/graph/state/StateGraph/compile) method.

    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    # Build workflow
    agent_builder = StateGraph(MessagesState)

    # Add nodes
    agent_builder.add_node("llm_call", llm_call)
    agent_builder.add_node("tool_node", tool_node)

    # Add edges to connect nodes
    agent_builder.add_edge(START, "llm_call")
    agent_builder.add_conditional_edges(
        "llm_call",
        should_continue,
        ["tool_node", END]
    )
    agent_builder.add_edge("tool_node", "llm_call")

    # Compile the agent
    agent = agent_builder.compile()

    # Show the agent
    from IPython.display import Image, display
    display(Image(agent.get_graph(xray=True).draw_mermaid_png()))

    # Invoke
    from langchain.messages import HumanMessage
    messages = [HumanMessage(content="Add 3 and 4.")]
    messages = agent.invoke({"messages": messages})
    for m in messages["messages"]:
        m.pretty_print()
    ```

    <Tip>
      Trace and debug your agent with [LangSmith](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=oss-langgraph-quickstart). Follow the [tracing quickstart](/langsmith/trace-with-langgraph) to get set up. When ready for production, see [Deploy](/langsmith/deployment) for hosting options.

      We recommend you also set up [LangSmith Engine](/langsmith/engine) which monitors your traces, detects issues, and proposes fixes.
    </Tip>

    Congratulations! You've built your first agent using the LangGraph Graph API.

    <Accordion title="Full code example">
      ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      # Step 1: Define tools and model

      from langchain.tools import tool
      from langchain.chat_models import init_chat_model

      model = init_chat_model(
          "claude-sonnet-4-6",
          temperature=0
      )

      # Define tools
      @tool
      def multiply(a: int, b: int) -> int:
          """Multiply `a` and `b`.

          Args:
              a: First int
              b: Second int
          """
          return a * b

      @tool
      def add(a: int, b: int) -> int:
          """Adds `a` and `b`.

          Args:
              a: First int
              b: Second int
          """
          return a + b

      @tool
      def divide(a: int, b: int) -> float:
          """Divide `a` and `b`.

          Args:
              a: First int
              b: Second int
          """
          return a / b

      # Augment the LLM with tools
      tools = [add, multiply, divide]
      tools_by_name = {tool.name: tool for tool in tools}
      model_with_tools = model.bind_tools(tools)

      # Step 2: Define state

      from langchain.messages import AnyMessage
      from typing_extensions import TypedDict, Annotated
      import operator

      class MessagesState(TypedDict):
          messages: Annotated[list[AnyMessage], operator.add]
          llm_calls: int

      # Step 3: Define model node
      from langchain.messages import SystemMessage

      def llm_call(state: MessagesState):
          """LLM decides whether to call a tool or not"""

          return {
              "messages": [
                  model_with_tools.invoke(
                      [
                          SystemMessage(
                              content="You are a helpful assistant tasked with performing arithmetic on a set of inputs."
                          )
                      ]
                      + state["messages"]
                  )
              ],
              "llm_calls": state.get('llm_calls', 0) + 1
          }

      # Step 4: Define tool node

      from langchain.messages import ToolMessage

      def tool_node(state: MessagesState):
          """Performs the tool call"""

          result = []
          for tool_call in state["messages"][-1].tool_calls:
              tool = tools_by_name[tool_call["name"]]
              observation = tool.invoke(tool_call["args"])
              result.append(ToolMessage(content=observation, tool_call_id=tool_call["id"]))
          return {"messages": result}

      # Step 5: Define logic to determine whether to end

      from typing import Literal
      from langgraph.graph import StateGraph, START, END

      # Conditional edge function to route to the tool node or end based upon whether the LLM made a tool call
      def should_continue(state: MessagesState) -> Literal["tool_node", END]:
          """Decide if we should continue the loop or stop based upon whether the LLM made a tool call"""

          messages = state["messages"]
          last_message = messages[-1]

          # If the LLM makes a tool call, then perform an action
          if last_message.tool_calls:
              return "tool_node"

          # Otherwise, we stop (reply to the user)
          return END

      # Step 6: Build agent

      # Build workflow
      agent_builder = StateGraph(MessagesState)

      # Add nodes
      agent_builder.add_node("llm_call", llm_call)
      agent_builder.add_node("tool_node", tool_node)

      # Add edges to connect nodes
      agent_builder.add_edge(START, "llm_call")
      agent_builder.add_conditional_edges(
          "llm_call",
          should_continue,
          ["tool_node", END]
      )
      agent_builder.add_edge("tool_node", "llm_call")

      # Compile the agent
      agent = agent_builder.compile()

      from IPython.display import Image, display
      # Show the agent
      display(Image(agent.get_graph(xray=True).draw_mermaid_png()))

      # Invoke
      from langchain.messages import HumanMessage
      messages = [HumanMessage(content="Add 3 and 4.")]
      messages = agent.invoke({"messages": messages})
      for m in messages["messages"]:
          m.pretty_print()

      ```
    </Accordion>
  </Tab>

  <Tab title="Use the Functional API">
    ## 1. Define tools and model

    In this example, we'll use the Claude Sonnet 4.5 model and define tools for addition, multiplication, and division.

    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    from langchain.tools import tool
    from langchain.chat_models import init_chat_model

    model = init_chat_model(
        "claude-sonnet-4-6",
        temperature=0
    )

    # Define tools
    @tool
    def multiply(a: int, b: int) -> int:
        """Multiply `a` and `b`.

        Args:
            a: First int
            b: Second int
        """
        return a * b

    @tool
    def add(a: int, b: int) -> int:
        """Adds `a` and `b`.

        Args:
            a: First int
            b: Second int
        """
        return a + b

    @tool
    def divide(a: int, b: int) -> float:
        """Divide `a` and `b`.

        Args:
            a: First int
            b: Second int
        """
        return a / b

    # Augment the LLM with tools
    tools = [add, multiply, divide]
    tools_by_name = {tool.name: tool for tool in tools}
    model_with_tools = model.bind_tools(tools)

    from langgraph.graph import add_messages
    from langchain.messages import (
        SystemMessage,
        HumanMessage,
        ToolCall,
    )
    from langchain_core.messages import BaseMessage
    from langgraph.func import entrypoint, task
    ```

    ## 2. Define model node

    The model node is used to call the LLM and decide whether to call a tool or not.

    <Tip>
      The [`@task`](https://reference.langchain.com/python/langgraph/func/task) decorator marks a function as a task that can be executed as part of the agent. Tasks can be called synchronously or asynchronously within your entrypoint function.
    </Tip>

    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    @task
    def call_llm(messages: list[BaseMessage]):
        """LLM decides whether to call a tool or not"""
        return model_with_tools.invoke(
            [
                SystemMessage(
                    content="You are a helpful assistant tasked with performing arithmetic on a set of inputs."
                )
            ]
            + messages
        )
    ```

    ## 3. Define tool node

    The tool node is used to call the tools and return the results.

    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    @task
    def call_tool(tool_call: ToolCall):
        """Performs the tool call"""
        tool = tools_by_name[tool_call["name"]]
        return tool.invoke(tool_call)

    ```

    ## 4. Define agent

    The agent is built using the [`@entrypoint`](https://reference.langchain.com/python/langgraph/func/entrypoint) function.

    <Note>
      In the Functional API, instead of defining nodes and edges explicitly, you write standard control flow logic (loops, conditionals) within a single function.
    </Note>

    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    @entrypoint()
    def agent(messages: list[BaseMessage]):
        model_response = call_llm(messages).result()

        while True:
            if not model_response.tool_calls:
                break

            # Execute tools
            tool_result_futures = [
                call_tool(tool_call) for tool_call in model_response.tool_calls
            ]
            tool_results = [fut.result() for fut in tool_result_futures]
            messages = add_messages(messages, [model_response, *tool_results])
            model_response = call_llm(messages).result()

        messages = add_messages(messages, model_response)
        return messages

    # Invoke
    messages = [HumanMessage(content="Add 3 and 4.")]
    for chunk in agent.stream(messages, stream_mode="updates"):
        print(chunk)
        print("\n")
    ```

    <Tip>
      Trace and debug your agent with [LangSmith](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=oss-langgraph-quickstart). Follow the [tracing quickstart](/langsmith/trace-with-langgraph) to get set up. When ready for production, see [Deploy](/langsmith/deployment) for hosting options.

      We recommend you also set up [LangSmith Engine](/langsmith/engine) which monitors your traces, detects issues, and proposes fixes.
    </Tip>

    Congratulations! You've built your first agent using the LangGraph Functional API.

    <Accordion title="Full code example" icon="code">
      ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      # Step 1: Define tools and model

      from langchain.tools import tool
      from langchain.chat_models import init_chat_model

      model = init_chat_model(
          "claude-sonnet-4-6",
          temperature=0
      )

      # Define tools
      @tool
      def multiply(a: int, b: int) -> int:
          """Multiply `a` and `b`.

          Args:
              a: First int
              b: Second int
          """
          return a * b

      @tool
      def add(a: int, b: int) -> int:
          """Adds `a` and `b`.

          Args:
              a: First int
              b: Second int
          """
          return a + b

      @tool
      def divide(a: int, b: int) -> float:
          """Divide `a` and `b`.

          Args:
              a: First int
              b: Second int
          """
          return a / b

      # Augment the LLM with tools
      tools = [add, multiply, divide]
      tools_by_name = {tool.name: tool for tool in tools}
      model_with_tools = model.bind_tools(tools)

      from langgraph.graph import add_messages
      from langchain.messages import (
          SystemMessage,
          HumanMessage,
          ToolCall,
      )
      from langchain_core.messages import BaseMessage
      from langgraph.func import entrypoint, task

      # Step 2: Define model node

      @task
      def call_llm(messages: list[BaseMessage]):
          """LLM decides whether to call a tool or not"""
          return model_with_tools.invoke(
              [
                  SystemMessage(
                      content="You are a helpful assistant tasked with performing arithmetic on a set of inputs."
                  )
              ]
              + messages
          )

      # Step 3: Define tool node

      @task
      def call_tool(tool_call: ToolCall):
          """Performs the tool call"""
          tool = tools_by_name[tool_call["name"]]
          return tool.invoke(tool_call)

      # Step 4: Define agent

      @entrypoint()
      def agent(messages: list[BaseMessage]):
          model_response = call_llm(messages).result()

          while True:
              if not model_response.tool_calls:
                  break

              # Execute tools
              tool_result_futures = [
                  call_tool(tool_call) for tool_call in model_response.tool_calls
              ]
              tool_results = [fut.result() for fut in tool_result_futures]
              messages = add_messages(messages, [model_response, *tool_results])
              model_response = call_llm(messages).result()

          messages = add_messages(messages, model_response)
          return messages

      # Invoke
      messages = [HumanMessage(content="Add 3 and 4.")]
      for chunk in agent.stream(messages, stream_mode="updates"):
          print(chunk)
          print("\n")
      ```
    </Accordion>
  </Tab>
</Tabs>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langgraph/quickstart.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Build a custom SQL agent
Source: https://docs.langchain.com/oss/python/langgraph/sql-agent

In this tutorial we will build a custom agent that can answer questions about a SQL database using LangGraph.

LangChain offers built-in [agent](/oss/python/langchain/agents) implementations, implemented using [LangGraph](/oss/python/langgraph/overview) primitives. If deeper customization is required, agents can be implemented directly in LangGraph. This guide demonstrates an example implementation of a SQL agent. For a practical introduction, see [building a SQL agent using higher-level LangChain abstractions](/oss/python/langchain/sql-agent).

<Warning>
  Building Q\&A systems of SQL databases requires executing model-generated SQL queries. There are inherent risks in doing this. Make sure that your database connection permissions are always scoped as narrowly as possible for your agent's needs. This will mitigate, though not eliminate, the risks of building a model-driven system.
</Warning>

The [prebuilt agent](/oss/python/langchain/sql-agent) lets us get started quickly, but we relied on the system prompt to constrain its behavior—for example, we instructed the agent to always start with the "list tables" tool, and to always run a query-checker tool before executing the query.

We can enforce a higher degree of control in LangGraph by customizing the agent. Here, we implement a simple ReAct-agent setup, with dedicated nodes for specific tool-calls. We will use the same \[state] as the prebuilt agent.

### Concepts

We will cover the following concepts:

* [Tools](/oss/python/langchain/tools) for reading from SQL databases
* The LangGraph [Graph API](/oss/python/langgraph/graph-api), including state, nodes, edges, and conditional edges.
* [Human-in-the-loop](/oss/python/langgraph/interrupts) processes

## Setup

### Installation

<CodeGroup>
  ```bash pip theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  pip install langchain langgraph
  ```
</CodeGroup>

### LangSmith

Set up [LangSmith](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=oss-langgraph-sql-agent) to inspect what is happening inside your chain or agent. Then set the following environment variables:

```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
export LANGSMITH_TRACING="true"
export LANGSMITH_API_KEY="..."
```

## 1. Select an LLM

Select a model that supports [tool-calling](/oss/python/integrations/providers/overview):

<Tabs>
  <Tab title="OpenAI">
    👉 Read the [OpenAI chat model integration docs](/oss/python/integrations/chat/openai/)

    ```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    pip install -U "langchain[openai]"
    ```

    <CodeGroup>
      ```python init_chat_model theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import os
      from langchain.chat_models import init_chat_model

      os.environ["OPENAI_API_KEY"] = "sk-..."

      model = init_chat_model("gpt-5.5")
      ```

      ```python Model Class theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import os
      from langchain_openai import ChatOpenAI

      os.environ["OPENAI_API_KEY"] = "sk-..."

      model = ChatOpenAI(model="gpt-5.5")
      ```
    </CodeGroup>
  </Tab>

  <Tab title="Anthropic">
    👉 Read the [Anthropic chat model integration docs](/oss/python/integrations/chat/anthropic/)

    ```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    pip install -U "langchain[anthropic]"
    ```

    <CodeGroup>
      ```python init_chat_model theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import os
      from langchain.chat_models import init_chat_model

      os.environ["ANTHROPIC_API_KEY"] = "sk-..."

      model = init_chat_model("claude-sonnet-4-6")
      ```

      ```python Model Class theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import os
      from langchain_anthropic import ChatAnthropic

      os.environ["ANTHROPIC_API_KEY"] = "sk-..."

      model = ChatAnthropic(model="claude-sonnet-4-6")
      ```
    </CodeGroup>
  </Tab>

  <Tab title="Azure">
    👉 Read the [Azure chat model integration docs](/oss/python/integrations/chat/azure_chat_openai/)

    ```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    pip install -U "langchain[openai]"
    ```

    <CodeGroup>
      ```python init_chat_model theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import os
      from langchain.chat_models import init_chat_model

      os.environ["AZURE_OPENAI_API_KEY"] = "..."
      os.environ["AZURE_OPENAI_ENDPOINT"] = "..."
      os.environ["OPENAI_API_VERSION"] = "2025-03-01-preview"

      model = init_chat_model(
          "azure_openai:gpt-5.5",
          azure_deployment=os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"],
      )
      ```

      ```python Model Class theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import os
      from langchain_openai import AzureChatOpenAI

      os.environ["AZURE_OPENAI_API_KEY"] = "..."
      os.environ["AZURE_OPENAI_ENDPOINT"] = "..."
      os.environ["OPENAI_API_VERSION"] = "2025-03-01-preview"

      model = AzureChatOpenAI(
          model="gpt-5.5",
          azure_deployment=os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"]
      )
      ```
    </CodeGroup>
  </Tab>

  <Tab title="Google Gemini">
    👉 Read the [Google GenAI chat model integration docs](/oss/python/integrations/chat/google_generative_ai/)

    ```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    pip install -U "langchain[google-genai]"
    ```

    <CodeGroup>
      ```python init_chat_model theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import os
      from langchain.chat_models import init_chat_model

      os.environ["GOOGLE_API_KEY"] = "..."

      model = init_chat_model("google_genai:gemini-2.5-flash-lite")
      ```

      ```python Model Class theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import os
      from langchain_google_genai import ChatGoogleGenerativeAI

      os.environ["GOOGLE_API_KEY"] = "..."

      model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")
      ```
    </CodeGroup>
  </Tab>

  <Tab title="AWS Bedrock">
    👉 Read the [AWS Bedrock chat model integration docs](/oss/python/integrations/chat/bedrock/)

    ```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    pip install -U "langchain[aws]"
    ```

    <CodeGroup>
      ```python init_chat_model theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      from langchain.chat_models import init_chat_model

      # Follow the steps here to configure your credentials:
      # https://docs.aws.amazon.com/bedrock/latest/userguide/getting-started.html

      model = init_chat_model(
          "anthropic.claude-3-5-sonnet-20240620-v1:0",
          model_provider="bedrock_converse",
      )
      ```

      ```python Model Class theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      from langchain_aws import ChatBedrock

      model = ChatBedrock(model="anthropic.claude-3-5-sonnet-20240620-v1:0")
      ```
    </CodeGroup>
  </Tab>

  <Tab title="HuggingFace">
    👉 Read the [HuggingFace chat model integration docs](/oss/python/integrations/chat/huggingface/)

    ```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    pip install -U "langchain[huggingface]"
    ```

    <CodeGroup>
      ```python init_chat_model theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import os
      from langchain.chat_models import init_chat_model

      os.environ["HUGGINGFACEHUB_API_TOKEN"] = "hf_..."

      model = init_chat_model(
          "microsoft/Phi-3-mini-4k-instruct",
          model_provider="huggingface",
          temperature=0.7,
          max_tokens=1024,
      )
      ```

      ```python Model Class theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import os
      from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

      os.environ["HUGGINGFACEHUB_API_TOKEN"] = "hf_..."

      llm = HuggingFaceEndpoint(
          repo_id="microsoft/Phi-3-mini-4k-instruct",
          temperature=0.7,
          max_length=1024,
      )
      model = ChatHuggingFace(llm=llm)
      ```
    </CodeGroup>
  </Tab>

  <Tab title="OpenRouter">
    👉 Read the [OpenRouter chat model integration docs](/oss/python/integrations/chat/openrouter/)

    ```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    pip install -U "langchain-openrouter"
    ```

    <CodeGroup>
      ```python init_chat_model theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import os
      from langchain.chat_models import init_chat_model

      os.environ["OPENROUTER_API_KEY"] = "sk-..."

      model = init_chat_model(
          "auto",
          model_provider="openrouter",
      )
      ```

      ```python Model Class theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import os
      from langchain_openrouter import ChatOpenRouter

      os.environ["OPENROUTER_API_KEY"] = "sk-..."

      model = ChatOpenRouter(model="auto")
      ```
    </CodeGroup>
  </Tab>
</Tabs>

The output shown in the examples below used OpenAI.

## 2. Configure the database

You will be creating a [SQLite database](https://www.sqlitetutorial.net/sqlite-sample-database/) for this tutorial. SQLite is a lightweight database that is easy to set up and use. We will be loading the `chinook` database, which is a sample database that represents a digital media store.

For convenience, we have hosted the database (`Chinook.db`) on a public GCS bucket.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import pathlib
import requests

url = "https://storage.googleapis.com/benchmarks-artifacts/chinook/Chinook.db"
local_path = pathlib.Path("Chinook.db")

if local_path.exists():
    print(f"{local_path} already exists, skipping download.")
else:
    response = requests.get(url, timeout=60)
    if response.status_code == 200:
        local_path.write_bytes(response.content)
        print(f"File downloaded and saved as {local_path}")
    else:
        print(f"Failed to download the file. Status code: {response.status_code}")
```

We will use Python's built-in `sqlite3` module to interact with the database:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import sqlite3

con = sqlite3.connect("Chinook.db")
cursor = con.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = [row[0] for row in cursor.fetchall() if not row[0].startswith("sqlite_")]

print("Dialect: sqlite")
print(f"Available tables: {tables}")

cursor.execute("SELECT * FROM Artist LIMIT 5;")
print(f"Sample output: {cursor.fetchall()}")
con.close()
```

```
Dialect: sqlite
Available tables: ['Album', 'Artist', 'Customer', 'Employee', 'Genre', 'Invoice', 'InvoiceLine', 'MediaType', 'Playlist', 'PlaylistTrack', 'Track']
Sample output: [(1, 'AC/DC'), (2, 'Accept'), (3, 'Aerosmith'), (4, 'Alanis Morissette'), (5, 'Alice In Chains')]
```

## 3. Add tools for database interactions

<Warning>
  The following database tools are minimal wrappers for demonstration purposes only. They are not intended to be secure or used in production. Use narrowly scoped database permissions and add application-specific validation before executing model-generated SQL.
</Warning>

We can implement database [tools](/oss/python/langchain/tools) as thin wrappers using the `@tool` decorator from `langchain.tools`:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import sqlite3
from langchain.tools import tool

# Below are minimal tools for demonstration purposes.

@tool
def sql_db_list_tables() -> str:
    """Input is an empty string, output is a comma-separated list of tables in the database."""
    con = sqlite3.connect("Chinook.db")
    try:
        cursor = con.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = [
            row[0]
            for row in cursor.fetchall()
            if not row[0].startswith("sqlite_")
        ]
        return ", ".join(tables)
    finally:
        con.close()

@tool
def sql_db_schema(table_names: str) -> str:
    """Input to this tool is a comma-separated list of tables, output is the schema and sample rows for those tables.
    Be sure that the tables actually exist by calling sql_db_list_tables first!
    Example Input: table1, table2, table3"""
    con = sqlite3.connect("Chinook.db")
    try:
        cursor = con.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        valid_tables = {
            row[0] for row in cursor.fetchall() if not row[0].startswith("sqlite_")
        }
        results = []
        for table in table_names.split(","):
            table = table.strip()
            if table not in valid_tables:
                results.append(
                    f"Error: table_names {{{table!r}}} not found in database"
                )
                continue
            cursor.execute(
                "SELECT sql FROM sqlite_master WHERE type='table' AND name=?;",
                (table,),
            )
            schema_row = cursor.fetchone()
            if schema_row:
                results.append(schema_row[0])
                try:
                    quoted_table = '"' + table.replace('"', '""') + '"'
                    cursor.execute(f"SELECT * FROM {quoted_table} LIMIT 3;")
                    rows = cursor.fetchall()
                    if rows:
                        col_names = [description[0] for description in cursor.description]
                        results.append(
                            f"/*\n3 rows from {table} table:\n"
                            + "\t".join(col_names)
                            + "\n"
                            + "\n".join(
                                "\t".join(str(x) for x in row) for row in rows
                            )
                            + "\n*/"
                        )
                except Exception as e:
                    results.append(f"Error fetching sample rows: {e}")
        return "\n\n".join(results)
    finally:
        con.close()

@tool
def sql_db_query(query: str) -> str:
    """Input to this tool is a detailed and correct SQL query, output is a result from the database.
    If the query is not correct, an error message will be returned.
    If an error is returned, rewrite the query, check the query, and try again.
    If you encounter an issue with Unknown column 'xxxx' in 'field list', use sql_db_schema to query the correct table fields."""
    con = sqlite3.connect("Chinook.db")
    try:
        cursor = con.cursor()
        cursor.execute(query)
        res = cursor.fetchall()
        return str(res)
    except Exception as e:
        return f"Error: {e}"
    finally:
        con.close()

tools = [sql_db_list_tables, sql_db_schema, sql_db_query]

for tool in tools:
    print(f"{tool.name}: {tool.description}\n")
```

```
sql_db_list_tables: Input is an empty string, output is a comma-separated list of tables in the database.

sql_db_schema: Input to this tool is a comma-separated list of tables, output is the schema and sample rows for those tables.
    Be sure that the tables actually exist by calling sql_db_list_tables first!
    Example Input: table1, table2, table3

sql_db_query: Input to this tool is a detailed and correct SQL query, output is a result from the database.
    If the query is not correct, an error message will be returned.
    If an error is returned, rewrite the query, check the query, and try again.
    If you encounter an issue with Unknown column 'xxxx' in 'field list', use sql_db_schema to query the correct table fields.
```

## 4. Define application steps

We construct dedicated nodes for the following steps:

* Listing DB tables
* Calling the "get schema" tool
* Generating a query
* Checking the query

Putting these steps in dedicated nodes lets us (1) force tool-calls when needed, and (2) customize the prompts associated with each step.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from typing import Literal

from langchain.messages import AIMessage
from langchain_core.runnables import RunnableConfig
from langgraph.graph import END, START, MessagesState, StateGraph
from langgraph.prebuilt import ToolNode

get_schema_tool = next(tool for tool in tools if tool.name == "sql_db_schema")
get_schema_node = ToolNode([get_schema_tool], name="get_schema")

run_query_tool = next(tool for tool in tools if tool.name == "sql_db_query")
run_query_node = ToolNode([run_query_tool], name="run_query")

# Example: create a predetermined tool call
def list_tables(state: MessagesState):
    tool_call = {
        "name": "sql_db_list_tables",
        "args": {},
        "id": "abc123",
        "type": "tool_call",
    }
    tool_call_message = AIMessage(content="", tool_calls=[tool_call])

    list_tables_tool = next(tool for tool in tools if tool.name == "sql_db_list_tables")
    tool_message = list_tables_tool.invoke(tool_call)
    response = AIMessage(f"Available tables: {tool_message.content}")

    return {"messages": [tool_call_message, tool_message, response]}

# Example: force a model to create a tool call
def call_get_schema(state: MessagesState):
    # Note that LangChain enforces that all models accept `tool_choice="any"`
    # as well as `tool_choice=<string name of tool>`.
    llm_with_tools = model.bind_tools([get_schema_tool], tool_choice="any")
    response = llm_with_tools.invoke(state["messages"])

    return {"messages": [response]}

generate_query_system_prompt = """
You are an agent designed to interact with a SQL database.
Given an input question, create a syntactically correct {dialect} query to run,
then look at the results of the query and return the answer. Unless the user
specifies a specific number of examples they wish to obtain, always limit your
query to at most {top_k} results.

You can order the results by a relevant column to return the most interesting
examples in the database. Never query for all the columns from a specific table,
only ask for the relevant columns given the question.

DO NOT make any DML statements (INSERT, UPDATE, DELETE, DROP etc.) to the database.
""".format(
    dialect="sqlite",
    top_k=5,
)

def generate_query(state: MessagesState):
    system_message = {
        "role": "system",
        "content": generate_query_system_prompt,
    }
    # We do not force a tool call here, to allow the model to
    # respond naturally when it obtains the solution.
    llm_with_tools = model.bind_tools([run_query_tool])
    response = llm_with_tools.invoke([system_message] + state["messages"])

    return {"messages": [response]}

check_query_system_prompt = """
You are a SQL expert with a strong attention to detail.
Double check the {dialect} query for common mistakes, including:
- Using NOT IN with NULL values
- Using UNION when UNION ALL should have been used
- Using BETWEEN for exclusive ranges
- Data type mismatch in predicates
- Properly quoting identifiers
- Using the correct number of arguments for functions
- Casting to the correct data type
- Using the proper columns for joins

If there are any of the above mistakes, rewrite the query. If there are no mistakes,
just reproduce the original query.

You will call the appropriate tool to execute the query after running this check.
""".format(dialect="sqlite")

def check_query(state: MessagesState):
    system_message = {
        "role": "system",
        "content": check_query_system_prompt,
    }

    # Generate an artificial user message to check
    tool_call = state["messages"][-1].tool_calls[0]
    user_message = {"role": "user", "content": tool_call["args"]["query"]}
    llm_with_tools = model.bind_tools([run_query_tool], tool_choice="any")
    response = llm_with_tools.invoke([system_message, user_message])
    response.id = state["messages"][-1].id

    return {"messages": [response]}
```

## 5. Implement the agent

We can now assemble these steps into a workflow using the [Graph API](/oss/python/langgraph/graph-api). We define a [conditional edge](/oss/python/langgraph/graph-api#conditional-edges) at the query generation step that will route to the query checker if a query is generated, or end if there are no tool calls present, such that the LLM has delivered a response to the query.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
def should_continue(state: MessagesState) -> Literal[END, "check_query"]:
    messages = state["messages"]
    last_message = messages[-1]
    if not last_message.tool_calls:
        return END
    else:
        return "check_query"

builder = StateGraph(MessagesState)
builder.add_node(list_tables)
builder.add_node(call_get_schema)
builder.add_node(get_schema_node, "get_schema")
builder.add_node(generate_query)
builder.add_node(check_query)
builder.add_node(run_query_node, "run_query")

builder.add_edge(START, "list_tables")
builder.add_edge("list_tables", "call_get_schema")
builder.add_edge("call_get_schema", "get_schema")
builder.add_edge("get_schema", "generate_query")
builder.add_conditional_edges(
    "generate_query",
    should_continue,
)
builder.add_edge("check_query", "run_query")
builder.add_edge("run_query", "generate_query")

agent = builder.compile()
```

We visualize the application below:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import pathlib

pathlib.Path("graph.png").write_bytes(agent.get_graph().draw_mermaid_png())
```

<img alt="SQL agent graph" />

We can now invoke the graph:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
question = "Which genre on average has the longest tracks?"

for step in agent.stream(
    {"messages": [{"role": "user", "content": question}]},
    stream_mode="values",
):
    step["messages"][-1].pretty_print()
```

```
================================ Human Message =================================

Which genre on average has the longest tracks?
================================== Ai Message ==================================

Available tables: Album, Artist, Customer, Employee, Genre, Invoice, InvoiceLine, MediaType, Playlist, PlaylistTrack, Track
================================== Ai Message ==================================
Tool Calls:
  sql_db_schema (call_yzje0tj7JK3TEzDx4QnRR3lL)
 Call ID: call_yzje0tj7JK3TEzDx4QnRR3lL
  Args:
    table_names: Genre, Track
================================= Tool Message =================================
Name: sql_db_schema

CREATE TABLE "Genre" (
	"GenreId" INTEGER NOT NULL,
	"Name" NVARCHAR(120),
	PRIMARY KEY ("GenreId")
)

/*
3 rows from Genre table:
GenreId	Name
1	Rock
2	Jazz
3	Metal
*/

CREATE TABLE "Track" (
	"TrackId" INTEGER NOT NULL,
	"Name" NVARCHAR(200) NOT NULL,
	"AlbumId" INTEGER,
	"MediaTypeId" INTEGER NOT NULL,
	"GenreId" INTEGER,
	"Composer" NVARCHAR(220),
	"Milliseconds" INTEGER NOT NULL,
	"Bytes" INTEGER,
	"UnitPrice" NUMERIC(10, 2) NOT NULL,
	PRIMARY KEY ("TrackId"),
	FOREIGN KEY("MediaTypeId") REFERENCES "MediaType" ("MediaTypeId"),
	FOREIGN KEY("GenreId") REFERENCES "Genre" ("GenreId"),
	FOREIGN KEY("AlbumId") REFERENCES "Album" ("AlbumId")
)

/*
3 rows from Track table:
TrackId	Name	AlbumId	MediaTypeId	GenreId	Composer	Milliseconds	Bytes	UnitPrice
1	For Those About To Rock (We Salute You)	1	1	1	Angus Young, Malcolm Young, Brian Johnson	343719	11170334	0.99
2	Balls to the Wall	2	2	1	U. Dirkschneider, W. Hoffmann, H. Frank, P. Baltes, S. Kaufmann, G. Hoffmann	342562	5510424	0.99
3	Fast As a Shark	3	2	1	F. Baltes, S. Kaufman, U. Dirkscneider & W. Hoffman	230619	3990994	0.99
*/
================================== Ai Message ==================================
Tool Calls:
  sql_db_query (call_cb9ApLfZLSq7CWg6jd0im90b)
 Call ID: call_cb9ApLfZLSq7CWg6jd0im90b
  Args:
    query: SELECT Genre.Name, AVG(Track.Milliseconds) AS AvgMilliseconds FROM Track JOIN Genre ON Track.GenreId = Genre.GenreId GROUP BY Genre.GenreId ORDER BY AvgMilliseconds DESC LIMIT 5;
================================== Ai Message ==================================
Tool Calls:
  sql_db_query (call_DMVALfnQ4kJsuF3Yl6jxbeAU)
 Call ID: call_DMVALfnQ4kJsuF3Yl6jxbeAU
  Args:
    query: SELECT Genre.Name, AVG(Track.Milliseconds) AS AvgMilliseconds FROM Track JOIN Genre ON Track.GenreId = Genre.GenreId GROUP BY Genre.GenreId ORDER BY AvgMilliseconds DESC LIMIT 5;
================================= Tool Message =================================
Name: sql_db_query

[('Sci Fi & Fantasy', 2911783.0384615385), ('Science Fiction', 2625549.076923077), ('Drama', 2575283.78125), ('TV Shows', 2145041.0215053763), ('Comedy', 1585263.705882353)]
================================== Ai Message ==================================

The genre with the longest tracks on average is "Sci Fi & Fantasy," with an average track length of approximately 2,911,783 milliseconds. Other genres with relatively long tracks include "Science Fiction," "Drama," "TV Shows," and "Comedy."
```

<Tip>
  See [LangSmith trace](https://smith.langchain.com/public/94b8c9ac-12f7-4692-8706-836a1f30f1ea/r) for the above run.
</Tip>

## 6. Implement human-in-the-loop review

It can be prudent to check the agent's SQL queries before they are executed for any unintended actions or inefficiencies.

Here we leverage LangGraph's [human-in-the-loop](/oss/python/langgraph/interrupts) features to pause the run before executing a SQL query and wait for human review. Using LangGraph's [persistence layer](/oss/python/langgraph/persistence), we can pause the run indefinitely (or at least as long as the persistence layer is alive).

Let's wrap the `sql_db_query` tool in a node that receives human input. We can implement this using the [interrupt](/oss/python/langgraph/interrupts) function. Below, we allow for input to approve the tool call, edit its arguments, or provide user feedback.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain.tools import tool
from langgraph.types import interrupt
from langchain_core.runnables import RunnableConfig

@tool(
    run_query_tool.name,
    description=run_query_tool.description,
    args_schema=run_query_tool.args_schema,
)
def run_query_tool_with_interrupt(config: RunnableConfig, **tool_input):
    request = {
        "action": run_query_tool.name,
        "args": tool_input,
        "description": "Please review the tool call",
    }
    response = interrupt([request])  # [!code highlight]
    # approve the tool call
    if response["type"] == "accept":
        tool_response = run_query_tool.invoke(tool_input, config)
    # update tool call args
    elif response["type"] == "edit":
        tool_input = response["args"]["args"]
        tool_response = run_query_tool.invoke(tool_input, config)
    # respond to the LLM with user feedback
    elif response["type"] == "response":
        user_feedback = response["args"]
        tool_response = user_feedback
    else:
        raise ValueError(f"Unsupported interrupt response type: {response['type']}")

    return tool_response
