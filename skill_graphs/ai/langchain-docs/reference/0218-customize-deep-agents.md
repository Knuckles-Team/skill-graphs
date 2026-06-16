# Customize Deep Agents
Source: https://docs.langchain.com/oss/python/deepagents/customization

Learn how to customize Deep Agents with system prompts, tools, subagents, and more

Build the harness around your goal. `create_deep_agent` gives you a production-ready foundation: connect it to your data, shape its behavior, and add the capabilities your use case needs.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from deepagents import create_deep_agent

agent = create_deep_agent(
    model="anthropic:claude-sonnet-4-6",
    system_prompt="You are a helpful assistant.",
    tools=[search, fetch_url],
    memory=["./AGENTS.md"],
    skills=["./skills/"],
)
```

| Parameter                                                                         | What it does                                                                |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| [`model=`](#model)                                                                | Which model to use                                                          |
| [`system_prompt=`](#system-prompt)                                                | Custom instructions for the agent                                           |
| [`tools=`](#tools)                                                                | Domain tools the agent can call                                             |
| [`memory=`](#memory)                                                              | AGENTS.md files loaded at startup                                           |
| [`skills=`](#skills)                                                              | Skills directory for on-demand knowledge                                    |
| [`backend=`](#backends)                                                           | Filesystem backend (StateBackend by default)                                |
| [`permissions=`](/oss/python/deepagents/permissions)                              | Path-level access control for the filesystem                                |
| [`subagents=`](#subagents)                                                        | Custom subagents for delegated tasks                                        |
| [`middleware=`](#middleware)                                                      | Extra middleware appended to the [default stack](#default-stack-main-agent) |
| [`interrupt_on=`](#human-in-the-loop)                                             | Pause before tool calls for human approval                                  |
| [`response_format=`](#structured-output)                                          | Structured output schema                                                    |
| [`state_schema=`](/oss/python/deepagents/context-engineering#custom-state-schema) | Custom graph state schema                                                   |
| [profiles](#profiles)                                                             | Per-model defaults as a reusable bundle                                     |

<Accordion title="Full function signature">
  ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  create_deep_agent(
      model: str | BaseChatModel | None = None,
      tools: Sequence[BaseTool | Callable | dict[str, Any]] | None = None,
      *,
      system_prompt: str | SystemMessage | None = None,
      middleware: Sequence[AgentMiddleware] = (),
      subagents: Sequence[SubAgent | CompiledSubAgent | AsyncSubAgent] | None = None,
      skills: list[str] | None = None,
      memory: list[str] | None = None,
      permissions: list[FilesystemPermission] | None = None,
      backend: BackendProtocol | BackendFactory | None = None,
      interrupt_on: dict[str, bool | InterruptOnConfig] | None = None,
      response_format: ResponseFormat[ResponseT] | type[ResponseT] | dict[str, Any] | None = None,
      state_schema: type[DeepAgentState] | None = None,
      context_schema: type[ContextT] | None = None,
      checkpointer: Checkpointer | None = None,
      store: BaseStore | None = None,
      debug: bool = False,
      name: str | None = None,
      cache: BaseCache | None = None
  ) -> CompiledStateGraph[AgentState[ResponseT], ContextT, _InputAgentState, _OutputAgentState[ResponseT]]
  ```
</Accordion>

For the full parameter list, see the [`create_deep_agent`](https://reference.langchain.com/python/deepagents/graph/create_deep_agent) API reference. To compose a fully custom harness from scratch, see [Configure the harness](/oss/python/langchain/agents#configure-the-harness) or follow the step-by-step [Build a deep agent from scratch](/oss/python/langchain/deep-agent-from-scratch) guide.

<Tip>
  As you add tools, subagents, and backends, use [LangSmith](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=oss-deepagents-customization) to trace how each piece behaves together. Follow the [observability quickstart](/langsmith/observability-quickstart) to get set up, and see [Going to production](/oss/python/deepagents/going-to-production) for deployment on LangSmith.

  We recommend you also set up [LangSmith Engine](/langsmith/engine), which monitors your traces, detects issues, and proposes fixes.
</Tip>

## Model

Pass a `model` string in `provider:model` format, or an initialized model instance. See [supported models](/oss/python/deepagents/models#supported-models) for all providers and [suggested models](/oss/python/deepagents/models#suggested-models) for tested recommendations.

<Tip>
  Use the `provider:model` format (for example `openai:gpt-5.5`) to quickly switch between models.
</Tip>

<Tabs>
  <Tab title="OpenAI">
    👉 Read the [OpenAI chat model integration docs](/oss/python/integrations/chat/openai/)

    ```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    pip install -U "langchain[openai]"
    ```

    <CodeGroup>
      ```python default parameters theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import os
      from deepagents import create_deep_agent

      os.environ["OPENAI_API_KEY"] = "sk-..."

      agent = create_deep_agent(model="openai:gpt-5.5")
      # this calls init_chat_model for the specified model with default parameters
      # to use specific model parameters, use init_chat_model directly
      ```

      ```python init_chat_model theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import os
      from langchain.chat_models import init_chat_model
      from deepagents import create_deep_agent

      os.environ["OPENAI_API_KEY"] = "sk-..."

      model = init_chat_model(model="openai:gpt-5.5")
      agent = create_deep_agent(model=model)
      ```

      ```python Model Class theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import os
      from langchain_openai import ChatOpenAI
      from deepagents import create_deep_agent

      os.environ["OPENAI_API_KEY"] = "sk-..."

      model = ChatOpenAI(model="gpt-5.5")
      agent = create_deep_agent(model=model)
      ```
    </CodeGroup>
  </Tab>

  <Tab title="Anthropic">
    👉 Read the [Anthropic chat model integration docs](/oss/python/integrations/chat/anthropic/)

    ```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    pip install -U "langchain[anthropic]"
    ```

    <CodeGroup>
      ```python default parameters theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import os
      from deepagents import create_deep_agent

      os.environ["ANTHROPIC_API_KEY"] = "sk-..."

      agent = create_deep_agent(model="anthropic:claude-sonnet-4-6")
      # this calls init_chat_model for the specified model with default parameters
      # to use specific model parameters, use init_chat_model directly
      ```

      ```python init_chat_model theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import os
      from langchain.chat_models import init_chat_model
      from deepagents import create_deep_agent

      os.environ["ANTHROPIC_API_KEY"] = "sk-..."

      model = init_chat_model(model="claude-sonnet-4-6")
      agent = create_deep_agent(model=model)
      ```

      ```python Model Class theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import os
      from langchain_anthropic import ChatAnthropic
      from deepagents import create_deep_agent

      os.environ["ANTHROPIC_API_KEY"] = "sk-..."

      model = ChatAnthropic(model="claude-sonnet-4-6")
      agent = create_deep_agent(model=model)
      ```
    </CodeGroup>
  </Tab>

  <Tab title="Azure">
    👉 Read the [Azure chat model integration docs](/oss/python/integrations/chat/azure_chat_openai/)

    ```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    pip install -U "langchain[openai]"
    ```

    <CodeGroup>
      ```python default parameters theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import os
      from deepagents import create_deep_agent

      os.environ["AZURE_OPENAI_API_KEY"] = "..."
      os.environ["AZURE_OPENAI_ENDPOINT"] = "..."
      os.environ["OPENAI_API_VERSION"] = "2025-03-01-preview"

      agent = create_deep_agent(model="azure_openai:gpt-5.5")
      # this calls init_chat_model for the specified model with default parameters
      # to use specific model parameters, use init_chat_model directly
      ```

      ```python init_chat_model theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import os
      from langchain.chat_models import init_chat_model
      from deepagents import create_deep_agent

      os.environ["AZURE_OPENAI_API_KEY"] = "..."
      os.environ["AZURE_OPENAI_ENDPOINT"] = "..."
      os.environ["OPENAI_API_VERSION"] = "2025-03-01-preview"

      model = init_chat_model(
          model="azure_openai:gpt-5.5",
          azure_deployment=os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"],
      )
      agent = create_deep_agent(model=model)
      ```

      ```python Model Class theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import os
      from langchain_openai import AzureChatOpenAI
      from deepagents import create_deep_agent

      os.environ["AZURE_OPENAI_API_KEY"] = "..."
      os.environ["AZURE_OPENAI_ENDPOINT"] = "..."
      os.environ["OPENAI_API_VERSION"] = "2025-03-01-preview"

      model = AzureChatOpenAI(
          model="gpt-5.5",
          azure_deployment=os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"],
      )
      agent = create_deep_agent(model=model)
      ```
    </CodeGroup>
  </Tab>

  <Tab title="Google Gemini">
    👉 Read the [Google GenAI chat model integration docs](/oss/python/integrations/chat/google_generative_ai/)

    ```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    pip install -U "langchain[google-genai]"
    ```

    <CodeGroup>
      ```python default parameters theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import os
      from deepagents import create_deep_agent

      os.environ["GOOGLE_API_KEY"] = "..."

      agent = create_deep_agent(model="google_genai:gemini-3.5-flash")
      # this calls init_chat_model for the specified model with default parameters
      # to use specific model parameters, use init_chat_model directly
      ```

      ```python init_chat_model theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import os
      from langchain.chat_models import init_chat_model
      from deepagents import create_deep_agent

      os.environ["GOOGLE_API_KEY"] = "..."

      model = init_chat_model(model="google_genai:gemini-3.5-flash")
      agent = create_deep_agent(model=model)
      ```

      ```python Model Class theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import os
      from langchain_google_genai import ChatGoogleGenerativeAI
      from deepagents import create_deep_agent

      os.environ["GOOGLE_API_KEY"] = "..."

      model = ChatGoogleGenerativeAI(model="gemini-3.1-pro-preview")
      agent = create_deep_agent(model=model)
      ```
    </CodeGroup>
  </Tab>

  <Tab title="AWS Bedrock">
    👉 Read the [AWS Bedrock chat model integration docs](/oss/python/integrations/chat/bedrock/)

    ```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    pip install -U "langchain[aws]"
    ```

    <CodeGroup>
      ```python default parameters theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      from deepagents import create_deep_agent

      # Follow the steps here to configure your credentials:
      # https://docs.aws.amazon.com/bedrock/latest/userguide/getting-started.html

      agent = create_deep_agent(
          model="anthropic.claude-sonnet-4-6",
          model_provider="bedrock_converse",
      )
      # this calls init_chat_model for the specified model with default parameters
      # to use specific model parameters, use init_chat_model directly
      ```

      ```python init_chat_model theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      from langchain.chat_models import init_chat_model
      from deepagents import create_deep_agent

      # Follow the steps here to configure your credentials:
      # https://docs.aws.amazon.com/bedrock/latest/userguide/getting-started.html

      model = init_chat_model(
          model="anthropic.claude-sonnet-4-6",
          model_provider="bedrock_converse",
      )
      agent = create_deep_agent(model=model)
      ```

      ```python Model Class theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      from langchain_aws import ChatBedrock
      from deepagents import create_deep_agent

      # Follow the steps here to configure your credentials:
      # https://docs.aws.amazon.com/bedrock/latest/userguide/getting-started.html

      model = ChatBedrock(model="anthropic.claude-sonnet-4-6")
      agent = create_deep_agent(model=model)
      ```
    </CodeGroup>
  </Tab>

  <Tab title="HuggingFace">
    👉 Read the [HuggingFace chat model integration docs](/oss/python/integrations/chat/huggingface/)

    ```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    pip install -U "langchain[huggingface]"
    ```

    <CodeGroup>
      ```python default parameters theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import os
      from deepagents import create_deep_agent

      os.environ["HUGGINGFACEHUB_API_TOKEN"] = "hf_..."

      agent = create_deep_agent(
          model="microsoft/Phi-3-mini-4k-instruct",
          model_provider="huggingface",
          temperature=0.7,
          max_tokens=1024,
      )
      # this calls init_chat_model for the specified model with default parameters
      # to use specific model parameters, use init_chat_model directly
      ```

      ```python init_chat_model theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import os
      from langchain.chat_models import init_chat_model
      from deepagents import create_deep_agent

      os.environ["HUGGINGFACEHUB_API_TOKEN"] = "hf_..."

      model = init_chat_model(
          model="microsoft/Phi-3-mini-4k-instruct",
          model_provider="huggingface",
          temperature=0.7,
          max_tokens=1024,
      )
      agent = create_deep_agent(model=model)
      ```

      ```python Model Class theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import os
      from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
      from deepagents import create_deep_agent

      os.environ["HUGGINGFACEHUB_API_TOKEN"] = "hf_..."

      llm = HuggingFaceEndpoint(
          repo_id="microsoft/Phi-3-mini-4k-instruct",
          temperature=0.7,
          max_length=1024,
      )
      model = ChatHuggingFace(llm=llm)
      agent = create_deep_agent(model=model)
      ```
    </CodeGroup>
  </Tab>

  <Tab title="Other">
    Pass any [supported model string](/oss/python/deepagents/models#supported-models), or an initialized model instance:

    <CodeGroup>
      ```python model string theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      from deepagents import create_deep_agent

      agent = create_deep_agent(model="provider:model-name")
      ```

      ```python init_chat_model theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      from deepagents import create_deep_agent
      from langchain.chat_models import init_chat_model

      model = init_chat_model("provider:model-name")
      agent = create_deep_agent(model=model)
      ```

      ```python model class theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      from langchain_<provider> import Chat<Provider>
      from deepagents import create_deep_agent

      model = Chat<Provider>(model="model-name")
      agent = create_deep_agent(model=model)
      ```
    </CodeGroup>
  </Tab>
</Tabs>

<Tip>
  Chat models automatically retry transient API failures (with exponential backoff). For defaults, limits, and code samples for tuning `max_retries` / `timeout` live on the LangChain [Models](/oss/python/langchain/models#connection-resilience) page.
</Tip>

## Tools

In addition to [built-in tools](/oss/python/deepagents/overview#core-capabilities) for planning, file management, and subagent spawning, you can provide custom tools:

<CodeGroup>
  ```python Google theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import os
  from typing import Literal
  from tavily import TavilyClient
  from deepagents import create_deep_agent

  tavily_client = TavilyClient(api_key=os.environ["TAVILY_API_KEY"])

  def internet_search(
      query: str,
      max_results: int = 5,
      topic: Literal["general", "news", "finance"] = "general",
      include_raw_content: bool = False,
  ):
      """Run a web search"""
      return tavily_client.search(
          query,
          max_results=max_results,
          include_raw_content=include_raw_content,
          topic=topic,
      )

  agent = create_deep_agent(
      model="google_genai:gemini-3.5-flash",
      tools=[internet_search],
  )
  ```

  ```python OpenAI theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import os
  from typing import Literal
  from tavily import TavilyClient
  from deepagents import create_deep_agent

  tavily_client = TavilyClient(api_key=os.environ["TAVILY_API_KEY"])

  def internet_search(
      query: str,
      max_results: int = 5,
      topic: Literal["general", "news", "finance"] = "general",
      include_raw_content: bool = False,
  ):
      """Run a web search"""
      return tavily_client.search(
          query,
          max_results=max_results,
          include_raw_content=include_raw_content,
          topic=topic,
      )

  agent = create_deep_agent(
      model="openai:gpt-5.5",
      tools=[internet_search],
  )
  ```

  ```python Anthropic theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import os
  from typing import Literal
  from tavily import TavilyClient
  from deepagents import create_deep_agent

  tavily_client = TavilyClient(api_key=os.environ["TAVILY_API_KEY"])

  def internet_search(
      query: str,
      max_results: int = 5,
      topic: Literal["general", "news", "finance"] = "general",
      include_raw_content: bool = False,
  ):
      """Run a web search"""
      return tavily_client.search(
          query,
          max_results=max_results,
          include_raw_content=include_raw_content,
          topic=topic,
      )

  agent = create_deep_agent(
      model="anthropic:claude-sonnet-4-6",
      tools=[internet_search],
  )
  ```

  ```python OpenRouter theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import os
  from typing import Literal
  from tavily import TavilyClient
  from deepagents import create_deep_agent

  tavily_client = TavilyClient(api_key=os.environ["TAVILY_API_KEY"])

  def internet_search(
      query: str,
      max_results: int = 5,
      topic: Literal["general", "news", "finance"] = "general",
      include_raw_content: bool = False,
  ):
      """Run a web search"""
      return tavily_client.search(
          query,
          max_results=max_results,
          include_raw_content=include_raw_content,
          topic=topic,
      )

  agent = create_deep_agent(
      model="openrouter:anthropic/claude-sonnet-4-6",
      tools=[internet_search],
  )
  ```

  ```python Fireworks theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import os
  from typing import Literal
  from tavily import TavilyClient
  from deepagents import create_deep_agent

  tavily_client = TavilyClient(api_key=os.environ["TAVILY_API_KEY"])

  def internet_search(
      query: str,
      max_results: int = 5,
      topic: Literal["general", "news", "finance"] = "general",
      include_raw_content: bool = False,
  ):
      """Run a web search"""
      return tavily_client.search(
          query,
          max_results=max_results,
          include_raw_content=include_raw_content,
          topic=topic,
      )

  agent = create_deep_agent(
      model="fireworks:accounts/fireworks/models/qwen3p5-397b-a17b",
      tools=[internet_search],
  )
  ```

  ```python Baseten theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import os
  from typing import Literal
  from tavily import TavilyClient
  from deepagents import create_deep_agent

  tavily_client = TavilyClient(api_key=os.environ["TAVILY_API_KEY"])

  def internet_search(
      query: str,
      max_results: int = 5,
      topic: Literal["general", "news", "finance"] = "general",
      include_raw_content: bool = False,
  ):
      """Run a web search"""
      return tavily_client.search(
          query,
          max_results=max_results,
          include_raw_content=include_raw_content,
          topic=topic,
      )

  agent = create_deep_agent(
      model="baseten:zai-org/GLM-5",
      tools=[internet_search],
  )
  ```

  ```python Ollama theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import os
  from typing import Literal
  from tavily import TavilyClient
  from deepagents import create_deep_agent

  tavily_client = TavilyClient(api_key=os.environ["TAVILY_API_KEY"])

  def internet_search(
      query: str,
      max_results: int = 5,
      topic: Literal["general", "news", "finance"] = "general",
      include_raw_content: bool = False,
  ):
      """Run a web search"""
      return tavily_client.search(
          query,
          max_results=max_results,
          include_raw_content=include_raw_content,
          topic=topic,
      )

  agent = create_deep_agent(
      model="ollama:devstral-2",
      tools=[internet_search],
  )
  ```
</CodeGroup>

### MCP tools

<Tip>
  Deep Agents fully support [Model Context Protocol (MCP)](/oss/python/langchain/mcp) tools. You can load tools from any MCP server—databases, APIs, file systems, and more—and pass them directly to `create_deep_agent`.
</Tip>

Install `langchain-mcp-adapters` to connect to MCP servers:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
pip install langchain-mcp-adapters
```

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient
from deepagents import create_deep_agent

async def main():
    async with MultiServerMCPClient(
        {
            "my_server": {
                "transport": "http",
                "url": "http://localhost:8000/mcp",
            }
        }
    ) as client:
        tools = await client.get_tools()

        agent = create_deep_agent(
            model="openai:gpt-5.5",
            tools=tools,
        )

        result = await agent.ainvoke(
            {"messages": [{"role": "user", "content": "Use the MCP server to help me."}]},
            config={"configurable": {"thread_id": "1"}},
        )

asyncio.run(main())
```

For detailed configuration options including stdio servers, OAuth authentication, tool filtering, and stateful sessions, see the full [MCP guide](/oss/python/langchain/mcp).

## System prompt

Deep Agents come with a built-in system prompt. A deep agent's value comes from the orchestration layer the SDK provides on top of the model—planning, virtual-filesystem tools, and subagents—and the model needs to know those exist and when to reach for them. The built-in prompt teaches the agent how to use that scaffolding so you don't have to re-derive it for every project; tweak it through a [profile](/oss/python/deepagents/profiles#harness-profiles) or your own `system_prompt=` rather than copying it verbatim.

When middleware add special tools, like the filesystem tools, it appends them to the system prompt.

Each deep agent should also include a custom system prompt specific to its specific use case:

<CodeGroup>
  ```python Google theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from deepagents import create_deep_agent

  research_instructions = """\
  You are an expert researcher. Your job is to conduct \
  thorough research, and then write a polished report. \
  """

  agent = create_deep_agent(
      model="google_genai:gemini-3.5-flash",
      system_prompt=research_instructions,
  )
  ```

  ```python OpenAI theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from deepagents import create_deep_agent

  research_instructions = """\
  You are an expert researcher. Your job is to conduct \
  thorough research, and then write a polished report. \
  """

  agent = create_deep_agent(
      model="openai:gpt-5.5",
      system_prompt=research_instructions,
  )
  ```

  ```python Anthropic theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from deepagents import create_deep_agent

  research_instructions = """\
  You are an expert researcher. Your job is to conduct \
  thorough research, and then write a polished report. \
  """

  agent = create_deep_agent(
      model="anthropic:claude-sonnet-4-6",
      system_prompt=research_instructions,
  )
  ```

  ```python OpenRouter theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from deepagents import create_deep_agent

  research_instructions = """\
  You are an expert researcher. Your job is to conduct \
  thorough research, and then write a polished report. \
  """

  agent = create_deep_agent(
      model="openrouter:anthropic/claude-sonnet-4-6",
      system_prompt=research_instructions,
  )
  ```

  ```python Fireworks theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from deepagents import create_deep_agent

  research_instructions = """\
  You are an expert researcher. Your job is to conduct \
  thorough research, and then write a polished report. \
  """

  agent = create_deep_agent(
      model="fireworks:accounts/fireworks/models/qwen3p5-397b-a17b",
      system_prompt=research_instructions,
  )
  ```

  ```python Baseten theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from deepagents import create_deep_agent

  research_instructions = """\
  You are an expert researcher. Your job is to conduct \
  thorough research, and then write a polished report. \
  """

  agent = create_deep_agent(
      model="baseten:zai-org/GLM-5",
      system_prompt=research_instructions,
  )
  ```

  ```python Ollama theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from deepagents import create_deep_agent

  research_instructions = """\
  You are an expert researcher. Your job is to conduct \
  thorough research, and then write a polished report. \
  """

  agent = create_deep_agent(
      model="ollama:devstral-2",
      system_prompt=research_instructions,
  )
  ```
</CodeGroup>

### Prompt assembly

Deep Agents builds the system prompt from up to four named parts so that caller-supplied instructions, the SDK's built-in agent guidance, and any model-specific [profile](/oss/python/deepagents/profiles) overrides can coexist with predictable precedence. Without this layering, a profile suffix tuned for Claude (for example) could overwrite or be overwritten by your `system_prompt=` argument depending on call order; the named slots make the ordering explicit and stable.

In practice, most callers only encounter two slots: `USER` (your `system_prompt=`) and `BASE` (the SDK default). Selecting a model with a built-in profile—Anthropic or OpenAI today—adds a `SUFFIX`. The full four-part assembly is mainly relevant when you author a custom `HarnessProfile` or debug why a profile's text appears where it does.

The four named parts (each may be absent):

| Name     | Source                                                                                    | Notes                                                     |
| -------- | ----------------------------------------------------------------------------------------- | --------------------------------------------------------- |
| `USER`   | `system_prompt=` argument to `create_deep_agent`                                          | `str` or `SystemMessage`; omitted when unset.             |
| `BASE`   | The SDK default (`BASE_AGENT_PROMPT`)                                                     | Always present unless replaced by a profile's `CUSTOM`.   |
| `CUSTOM` | [`HarnessProfile.base_system_prompt`](/oss/python/deepagents/profiles#harness-profiles)   | Replaces `BASE` outright when a matching profile sets it. |
| `SUFFIX` | [`HarnessProfile.system_prompt_suffix`](/oss/python/deepagents/profiles#harness-profiles) | Appended last when a matching profile sets it.            |

The order is always **`USER` -> (`BASE` or `CUSTOM`) -> `SUFFIX`**, joined by blank lines (`\n\n`). Two invariants follow:

1. **`USER` is always at the front.** The caller's text precedes any SDK or profile content, so persona/instructions take precedence regardless of which model is selected.
2. **`SUFFIX` is always at the end.** Profile suffixes sit closest to the conversation history, where model-tuning guidance lands most reliably.

Assembled shapes (✓ = field is set, - = field is unset):

| `system_prompt=` | profile `base_system_prompt` (`CUSTOM`) | profile `system_prompt_suffix` (`SUFFIX`) | Final assembled system prompt |
| ---------------- | :-------------------------------------: | :---------------------------------------: | ----------------------------- |
| `None`           |                    -                    |                     -                     | `BASE`                        |
| `None`           |                    -                    |                     ✓                     | `BASE` + `SUFFIX`             |
| `None`           |                    ✓                    |                     -                     | `CUSTOM`                      |
| `None`           |                    ✓                    |                     ✓                     | `CUSTOM` + `SUFFIX`           |
| `str`            |                    -                    |                     -                     | `USER` + `BASE`               |
| `str`            |                    -                    |                     ✓                     | `USER` + `BASE` + `SUFFIX`    |
| `str`            |                    ✓                    |                     -                     | `USER` + `CUSTOM`             |
| `str`            |                    ✓                    |                     ✓                     | `USER` + `CUSTOM` + `SUFFIX`  |

Worked example—built-in profiles (Anthropic, OpenAI) ship only a `system_prompt_suffix`, so a typical call lands in the `str` + `-` + `✓` row:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
agent = create_deep_agent(
    model="anthropic:claude-sonnet-4-6",
    system_prompt="You are a customer-support agent for ACME Corp.",
)

# Final = USER + BASE + SUFFIX

#       = "You are a customer-support agent for ACME Corp."

#         + "\n\n"

#         + BASE_AGENT_PROMPT

#         + "\n\n"
