# ❌ Bad: Too many tools
email_agent = {
    "name": "email-sender",
    "tools": [send_email, web_search, database_query, file_upload],  # Unfocused
}
```

### Choose models by task

Different models excel at different tasks:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
subagents = [
    {
        "name": "contract-reviewer",
        "description": "Reviews legal documents and contracts",
        "system_prompt": "You are an expert legal reviewer...",
        "tools": [read_document, analyze_contract],
        "model": "google_genai:gemini-3.5-flash",  # Large context for long documents
    },
    {
        "name": "financial-analyst",
        "description": "Analyzes financial data and market trends",
        "system_prompt": "You are an expert financial analyst...",
        "tools": [get_stock_price, analyze_fundamentals],
        "model": "openai:gpt-5.5",  # Better for numerical analysis
    },
]
```

### Return concise results

Instruct subagents to return summaries, not raw data:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
data_analyst = {
    "system_prompt": """Analyze the data and return:
    1. Key insights (3-5 bullet points)
    2. Overall confidence score
    3. Recommended next actions

    Do NOT include:
    - Raw data
    - Intermediate calculations
    - Detailed tool outputs

    Keep response under 300 words."""
}
```

## Common patterns

### Multiple specialized subagents

Create specialized subagents for different domains:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from deepagents import create_deep_agent

subagents = [
    {
        "name": "data-collector",
        "description": "Gathers raw data from various sources",
        "system_prompt": "Collect comprehensive data on the topic",
        "tools": [web_search, api_call, database_query],
    },
    {
        "name": "data-analyzer",
        "description": "Analyzes collected data for insights",
        "system_prompt": "Analyze data and extract key insights",
        "tools": [statistical_analysis],
    },
    {
        "name": "report-writer",
        "description": "Writes polished reports from analysis",
        "system_prompt": "Create professional reports from insights",
        "tools": [format_document],
    },
]

agent = create_deep_agent(
    model="google_genai:gemini-3.5-flash",
    system_prompt="You coordinate data analysis and reporting. Use subagents for specialized tasks.",
    subagents=subagents
)
```

**Workflow:**

1. Main agent creates high-level plan
2. Delegates data collection to data-collector
3. Passes results to data-analyzer
4. Sends insights to report-writer
5. Compiles final output

Each subagent works with clean context focused only on its task.

## Context management

When you invoke a parent agent with [runtime context](/oss/python/langchain/runtime), that context automatically propagates to all subagents. Each subagent run receives the same runtime context you passed on the parent `invoke` / `ainvoke` call.

This means tools running inside any subagent can access the same context values you provided to the parent:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from dataclasses import dataclass

from deepagents import create_deep_agent
from langchain.messages import HumanMessage
from langchain.tools import tool, ToolRuntime

@dataclass
class Context:
    user_id: str
    session_id: str

@tool
def get_user_data(query: str, runtime: ToolRuntime[Context]) -> str:
    """Fetch data for the current user."""
    user_id = runtime.context.user_id
    return f"Data for user {user_id}: {query}"

research_subagent = {
    "name": "researcher",
    "description": "Conducts research for the current user",
    "system_prompt": "You are a research assistant.",
    "tools": [get_user_data],
}

agent = create_deep_agent(
    model="google_genai:gemini-3.5-flash",
    subagents=[research_subagent],
    context_schema=Context,
)

# Context flows to the researcher subagent and its tools automatically
result = await agent.invoke(
    {"messages": [HumanMessage("Look up my recent activity")]},
    context=Context(user_id="user-123", session_id="abc"),
)
```

### Per-subagent context

All subagents receive the same parent context. To pass configuration that is specific to a particular subagent, use **namespaced keys** (prefix keys with the subagent name, for example `researcher:max_depth`) in a flat `context` mapping, **or** model those settings as separate fields on your context type:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from dataclasses import dataclass

from langchain.messages import HumanMessage
from langchain.tools import tool, ToolRuntime

@dataclass
class Context:
    user_id: str
    researcher_max_depth: int | None = None
    fact_checker_strict_mode: bool | None = None

result = await agent.invoke(
    {"messages": [HumanMessage("Research this and verify the claims")]},
    context=Context(
        user_id="user-123",
        researcher_max_depth=3,
        fact_checker_strict_mode=True,
    ),
)

@tool
def verify_claim(claim: str, runtime: ToolRuntime[Context]) -> str:
    """Verify a factual claim."""
    strict_mode = runtime.context.fact_checker_strict_mode or False
    if strict_mode:
        return strict_verification(claim)
    return basic_verification(claim)
```

### Identifying which subagent called a tool

When the same tool is shared between the parent and multiple subagents, you can use the `lc_agent_name` metadata (the same value used in [streaming](#streaming)) to determine which agent initiated the call:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain.tools import tool, ToolRuntime

@tool
def shared_lookup(query: str, runtime: ToolRuntime) -> str:
    """Look up information."""
    agent_name = runtime.config.get("metadata", {}).get("lc_agent_name")
    if agent_name == "fact-checker":
        return strict_lookup(query)
    return general_lookup(query)
```

You can combine both patterns—read agent-specific settings from `runtime.context` and read `lc_agent_name` from `runtime.config` metadata when branching tool behavior.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain.tools import tool, ToolRuntime

@tool
def flexible_search(query: str, runtime: ToolRuntime[Context]) -> str:
    """Search with agent-specific settings."""
    agent_name = runtime.config.get("metadata", {}).get("lc_agent_name", "unknown")
    ctx = runtime.context
    if agent_name == "researcher":
        max_results = ctx.researcher_max_depth or 5
    else:
        max_results = 5
    include_raw = False

    return perform_search(query, max_results=max_results, include_raw=include_raw)
```

## Troubleshooting

### Subagent not being called

**Problem**: Main agent tries to do work itself instead of delegating.

**Solutions**:

1. **Make descriptions more specific:**

   ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
   # ✅ Good
   {"name": "research-specialist", "description": "Conducts in-depth research on specific topics using web search. Use when you need detailed information that requires multiple searches."}

   # ❌ Bad
   {"name": "helper", "description": "helps with stuff"}
   ```

2. **Instruct main agent to delegate:**

   ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
   agent = create_deep_agent(
       model="google_genai:gemini-3.5-flash",
       system_prompt="""...your instructions...

       IMPORTANT: For complex tasks, delegate to your subagents using the task() tool.
       This keeps your context clean and improves results.""",
       subagents=[...]
   )
   ```

### Context still getting bloated

**Problem**: Context fills up despite using subagents.

**Solutions**:

1. **Instruct subagent to return concise results:**

   ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
   system_prompt="""...

   IMPORTANT: Return only the essential summary.
   Do NOT include raw data, intermediate search results, or detailed tool outputs.
   Your response should be under 500 words."""
   ```

2. **Use filesystem for large data:**

   ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
   system_prompt="""When you gather large amounts of data:
   1. Save raw data to /data/raw_results.txt
   2. Process and analyze the data
   3. Return only the analysis summary

   This keeps context clean."""
   ```

### Wrong subagent being selected

**Problem**: Main agent calls inappropriate subagent for the task.

**Solution**: Differentiate subagents clearly in descriptions:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
subagents = [
    {
        "name": "quick-researcher",
        "description": "For simple, quick research questions that need 1-2 searches. Use when you need basic facts or definitions.",
    },
    {
        "name": "deep-researcher",
        "description": "For complex, in-depth research requiring multiple searches, synthesis, and analysis. Use for comprehensive reports.",
    }
]
```

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/deepagents/subagents.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Tools
Source: https://docs.langchain.com/oss/python/deepagents/tools

Connect Deep Agents to custom functions, APIs, databases, and any MCP server

Deep Agents can call any tool you define, any [LangChain tool](https://python.langchain.com/docs/concepts/tools/), and tools from any [MCP server](#mcp-tools).
Pass them to `create_deep_agent` via the `tools=` parameter alongside the [built-in harness tools](/oss/python/deepagents/harness#execution-environment) for planning, file management, and subagent spawning.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from deepagents import create_deep_agent

agent = create_deep_agent(
    model="anthropic:claude-sonnet-4-6",
    tools=[search, fetch_url, run_query],
)
```

## Custom tools

Pass any callable — plain functions, LangChain `@tool`-decorated functions, or tool dicts — directly to `tools=`.
Deep Agents infers the tool schema from the function signature and docstring, so you don't need to define a separate schema in most cases.

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

For full details on defining and using LangChain tools (tool dicts, `StructuredTool`, return types, error handling, and more), see [Tools](/oss/python/langchain/tools).

## MCP tools

<Note>
  Deep Agents fully support [Model Context Protocol (MCP)](/oss/python/langchain/mcp) — the open standard for connecting agents to external services. Load tools from any MCP server and pass them directly to `create_deep_agent`.
</Note>

MCP is an open protocol that lets agents connect to a growing ecosystem of servers — databases, APIs, file systems, browsers, and more — through a standard interface. Instead of writing custom integration code for each service, you point Deep Agents at an MCP server and it gets all the tools that server exposes.

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

For detailed configuration options — including stdio servers, OAuth authentication, tool filtering, and stateful sessions — see the full [MCP guide](/oss/python/langchain/mcp).

## Built-in harness tools

In addition to the tools you provide, every Deep Agent comes with a built-in set of tools from the harness:

| Tool          | Description                                                 |
| ------------- | ----------------------------------------------------------- |
| `ls`          | List files in a directory                                   |
| `read_file`   | Read file contents (with pagination and multimodal support) |
| `write_file`  | Create new files                                            |
| `edit_file`   | Perform exact string replacements in files                  |
| `glob`        | Find files matching a glob pattern                          |
| `grep`        | Search file contents                                        |
| `execute`     | Run shell commands (sandbox backends only)                  |
| `task`        | Spawn a subagent to handle a delegated task                 |
| `write_todos` | Manage a structured todo list                               |

For a full breakdown of what each built-in tool does, see [Harness capabilities](/oss/python/deepagents/harness#execution-environment).

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/deepagents/tools.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Chat model integrations
Source: https://docs.langchain.com/oss/python/integrations/chat/index

Integrate with chat models using LangChain Python.

[Chat models](/oss/python/langchain/models) are language models that use a sequence of [messages](/oss/python/langchain/messages) as inputs and return messages as outputs <Tooltip>(as opposed to traditional, plaintext LLMs)</Tooltip>.

## Featured models

<Info>
  **While these LangChain classes support the indicated advanced feature**, you may need to refer to provider-specific documentation to learn which hosted models or backends support the feature.
</Info>

| Model                                                                          | [Tool calling](/oss/python/langchain/tools) | [Structured output](/oss/python/langchain/structured-output/) | [Multimodal](/oss/python/langchain/messages#multimodal) |
| ------------------------------------------------------------------------------ | ------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------- |
| [`ChatOpenAI`](/oss/python/integrations/chat/openai)                           | ✅                                           | ✅                                                             | ✅                                                       |
| [`ChatAnthropic`](/oss/python/integrations/chat/anthropic)                     | ✅                                           | ✅                                                             | ✅                                                       |
| [`ChatVertexAI`](/oss/python/integrations/chat/google_vertex_ai) (deprecated)  | ✅                                           | ✅                                                             | ✅                                                       |
| [`ChatGoogleGenerativeAI`](/oss/python/integrations/chat/google_generative_ai) | ✅                                           | ✅                                                             | ✅                                                       |
| [`AzureChatOpenAI`](/oss/python/integrations/chat/azure_chat_openai)           | ✅                                           | ✅                                                             | ✅                                                       |
| [`ChatGroq`](/oss/python/integrations/chat/groq)                               | ✅                                           | ✅                                                             | ❌                                                       |
| [`ChatAmazonNova`](/oss/python/integrations/chat/amazon_nova)                  | ✅                                           | ❌                                                             | ✅                                                       |
| [`ChatHuggingFace`](/oss/python/integrations/chat/huggingface)                 | ✅                                           | ✅                                                             | ❌                                                       |
| [`ChatOllama`](/oss/python/integrations/chat/ollama)                           | ✅                                           | ✅                                                             | ❌                                                       |
| [`ChatXAI`](/oss/python/integrations/chat/xai)                                 | ✅                                           | ✅                                                             | ❌                                                       |
| [`ChatNVIDIA`](/oss/python/integrations/chat/nvidia_ai_endpoints)              | ✅                                           | ✅                                                             | ✅                                                       |
| [`ChatCohere`](/oss/python/integrations/chat/cohere)                           | ✅                                           | ✅                                                             | ❌                                                       |
| [`ChatMistralAI`](/oss/python/integrations/chat/mistralai)                     | ✅                                           | ✅                                                             | ❌                                                       |
| [`ChatTogether`](/oss/python/integrations/chat/together)                       | ✅                                           | ✅                                                             | ❌                                                       |
| [`ChatDeepSeek`](/oss/python/integrations/chat/deepseek)                       | ✅                                           | ✅                                                             | ❌                                                       |
| [`ChatDatabricks`](/oss/python/integrations/chat/databricks)                   | ✅                                           | ✅                                                             | ❌                                                       |
| [`ChatOpenRouter`](/oss/python/integrations/chat/openrouter)                   | ✅                                           | ✅                                                             | ✅                                                       |
| [`ChatLiteLLM`](/oss/python/integrations/chat/litellm)                         | ✅                                           | ✅                                                             | ✅                                                       |

See the [full list of chat model integrations](#all-chat-models) below for more options.

## Routers & proxies

Routers and proxies give you access to models from multiple providers through a single API and credential. They can simplify billing, let you switch between models without changing integrations, and offer features like automatic fallbacks.

| Provider                             | Integration                                                  | Description                                                                                       |
| ------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------------------------------------------- |
| [OpenRouter](https://openrouter.ai/) | [`ChatOpenRouter`](/oss/python/integrations/chat/openrouter) | Unified access to models from OpenAI, Anthropic, Google, Meta, and more                           |
| [LiteLLM](https://www.litellm.ai/)   | [`ChatLiteLLMRouter`](/oss/python/integrations/chat/litellm) | Unified interface for OpenAI, Anthropic, Azure, Hugging Face, and more with routing and fallbacks |

## Chat Completions API

Certain model providers offer endpoints that are compatible with OpenAI's [Chat Completions API](https://platform.openai.com/docs/api-reference/chat). In such cases, you can use [`ChatOpenAI`](/oss/python/integrations/chat/openai) with a custom `base_url` to connect to these endpoints for basic chat functionality.

<Warning>
  `ChatOpenAI` targets [official OpenAI API specifications](https://github.com/openai/openai-openapi) only. Non-standard response fields from third-party providers (e.g., `reasoning_content`, `reasoning`, `reasoning_details`) **are not extracted or preserved**. Use a provider-specific package when you need access to non-standard features.

  For instance, OpenRouter has a dedicated LangChain integration. See the [`ChatOpenRouter` guide](/oss/python/integrations/chat/openrouter) for setup and usage.
</Warning>

## All chat models

<Columns>
  <Card title="Abso" icon="link" href="/oss/python/integrations/chat/abso" />

  <Card title="AI21 Labs" icon="link" href="/oss/python/integrations/chat/ai21" />

  <Card title="AI/ML API" icon="link" href="/oss/python/integrations/chat/aimlapi" />

  <Card title="Amazon Nova" icon="link" href="/oss/python/integrations/chat/amazon_nova" />

  <Card title="Anthropic" icon="link" href="/oss/python/integrations/chat/anthropic" />

  <Card title="AzureAIOpenAIApiChatModel" icon="link" href="/oss/python/integrations/chat/azure_ai" />

  <Card title="Azure OpenAI" icon="link" href="/oss/python/integrations/chat/azure_chat_openai" />

  <Card title="Baseten" icon="link" href="/oss/python/integrations/chat/baseten" />

  <Card title="Cerebras" icon="link" href="/oss/python/integrations/chat/cerebras" />

  <Card title="CloudflareWorkersAI" icon="link" href="/oss/python/integrations/chat/cloudflare_workersai" />

  <Card title="Cohere" icon="link" href="/oss/python/integrations/chat/cohere" />

  <Card title="ContextualAI" icon="link" href="/oss/python/integrations/chat/contextual" />

  <Card title="Crusoe" icon="link" href="/oss/python/integrations/chat/crusoe" />

  <Card title="Databricks" icon="link" href="/oss/python/integrations/chat/databricks" />

  <Card title="DeepSeek" icon="link" href="/oss/python/integrations/chat/deepseek" />

  <Card title="Featherless AI" icon="link" href="/oss/python/integrations/chat/featherless_ai" />

  <Card title="Google Gemini" icon="link" href="/oss/python/integrations/chat/google_generative_ai" />

  <Card title="Google Cloud Vertex AI" icon="link" href="/oss/python/integrations/chat/google_vertex_ai" />

  <Card title="Google Anthropic on Vertex AI" icon="link" href="/oss/python/integrations/chat/google_anthropic_vertex" />

  <Card title="DigitalOcean Gradient" icon="link" href="/oss/python/integrations/chat/gradientai" />

  <Card title="GreenNode" icon="link" href="/oss/python/integrations/chat/greennode" />

  <Card title="Groq" icon="link" href="/oss/python/integrations/chat/groq" />

  <Card title="ChatHuggingFace" icon="link" href="/oss/python/integrations/chat/huggingface" />

  <Card title="IBM watsonx.ai" icon="link" href="/oss/python/integrations/chat/ibm_watsonx" />

  <Card title="Kinetica" icon="link" href="/oss/python/integrations/chat/kinetica" />

  <Card title="LiteLLM" icon="link" href="/oss/python/integrations/chat/litellm" />

  <Card title="MistralAI" icon="link" href="/oss/python/integrations/chat/mistralai" />

  <Card title="ModelScope" icon="link" href="/oss/python/integrations/chat/modelscope_chat_endpoint" />

  <Card title="Naver" icon="link" href="/oss/python/integrations/chat/naver" />

  <Card title="Nebius" icon="link" href="/oss/python/integrations/chat/nebius" />

  <Card title="Netmind" icon="link" href="/oss/python/integrations/chat/netmind" />

  <Card title="NVIDIA AI Endpoints" icon="link" href="/oss/python/integrations/chat/nvidia_ai_endpoints" />

  <Card title="OCIGenAI" icon="link" href="/oss/python/integrations/chat/oci_generative_ai" />

  <Card title="OCI Data Science" icon="link" href="/oss/python/integrations/chat/oci_data_science" />

  <Card title="Ollama" icon="link" href="/oss/python/integrations/chat/ollama" />

  <Card title="OpenAI" icon="link" href="/oss/python/integrations/chat/openai" />

  <Card title="OpenRouter" icon="link" href="/oss/python/integrations/chat/openrouter" />

  <Card title="Parallel" icon="link" href="/oss/python/integrations/chat/parallel" />

  <Card title="Pipeshift" icon="link" href="/oss/python/integrations/chat/pipeshift" />

  <Card title="ChatPredictionGuard" icon="link" href="/oss/python/integrations/chat/predictionguard" />

  <Card title="Qwen QwQ" icon="link" href="/oss/python/integrations/chat/qwq" />

  <Card title="Qwen" icon="link" href="/oss/python/integrations/chat/qwen" />

  <Card title="RunPod Chat Model" icon="link" href="/oss/python/integrations/chat/runpod" />

  <Card title="SambaNova" icon="link" href="/oss/python/integrations/chat/sambanova" />

  <Card title="ChatSeekrFlow" icon="link" href="/oss/python/integrations/chat/seekrflow" />

  <Card title="Together" icon="link" href="/oss/python/integrations/chat/together" />

  <Card title="Upstage" icon="link" href="/oss/python/integrations/chat/upstage" />

  <Card title="vLLM Chat" icon="link" href="/oss/python/integrations/chat/vllm" />

  <Card title="ChatWriter" icon="link" href="/oss/python/integrations/chat/writer" />

  <Card title="xAI" icon="link" href="/oss/python/integrations/chat/xai" />

  <Card title="Xinference" icon="link" href="/oss/python/integrations/chat/xinference" />
</Columns>

<Info>
  If you'd like to contribute an integration, see [Contributing integrations](/oss/python/contributing#add-a-new-integration).
</Info>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/chat/index.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Checkpointer integrations
Source: https://docs.langchain.com/oss/python/integrations/checkpointers/index

Integrate with checkpointer backends for LangGraph persistence.

Checkpointers enable [persistence](/oss/python/langgraph/persistence) in LangGraph, allowing agents to save and resume state across interactions.

To implement your own checkpointer for a custom storage backend, see [Build a custom checkpointer](/oss/python/langgraph/checkpointers#build-a-custom-checkpointer).

| Backend                                                                                          | Package                                                                                      | Source                                                                                                                          |
| ------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| [In-memory](https://reference.langchain.com/python/langgraph.checkpoint/memory/InMemorySaver)    | [`langgraph-checkpoint`](https://pypi.org/project/langgraph-checkpoint/)                     | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph/tree/main/libs/checkpoint)                                   |
| [SQLite](https://reference.langchain.com/python/langgraph.checkpoint.sqlite/SqliteSaver)         | [`langgraph-checkpoint-sqlite`](https://pypi.org/project/langgraph-checkpoint-sqlite/)       | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph/tree/main/libs/checkpoint-sqlite)                            |
| [PostgreSQL](https://reference.langchain.com/python/langgraph.checkpoint.postgres/PostgresSaver) | [`langgraph-checkpoint-postgres`](https://pypi.org/project/langgraph-checkpoint-postgres/)   | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph/tree/main/libs/checkpoint-postgres)                          |
| AWS (DynamoDB, Bedrock, Valkey)                                                                  | [`langgraph-checkpoint-aws`](https://pypi.org/project/langgraph-checkpoint-aws/)             | [langchain-ai/langchain-aws](https://github.com/langchain-ai/langchain-aws/tree/main/libs/langgraph-checkpoint-aws)             |
| MongoDB                                                                                          | [`langgraph-checkpoint-mongodb`](https://pypi.org/project/langgraph-checkpoint-mongodb/)     | [langchain-ai/langchain-mongodb](https://github.com/langchain-ai/langchain-mongodb/tree/main/libs/langgraph-checkpoint-mongodb) |
| Azure Cosmos DB NoSQL                                                                            | [`langchain-azure-cosmosdb`](https://pypi.org/project/langchain-azure-cosmosdb/)             | [langchain-ai/langchain-azure](https://github.com/langchain-ai/langchain-azure/tree/main/libs/azure-cosmosdb)                   |
| Redis                                                                                            | [`langgraph-checkpoint-redis`](https://pypi.org/project/langgraph-checkpoint-redis/)         | [redis-developer/langgraph-redis](https://github.com/redis-developer/langgraph-redis)                                           |
| [Cockroach DB](/oss/python/integrations/providers/cockroachdb#langgraph-checkpointer)            | [`langchain-cockroachdb`](https://pypi.org/project/langchain-cockroachdb/)                   | [cockroachdb/langchain-cockroachdb](https://github.com/cockroachdb/langchain-cockroachdb)                                       |
| [Aerospike](/oss/python/integrations/providers/aerospike#langgraph-checkpointer)                 | [`langgraph-checkpoint-aerospike`](https://pypi.org/project/langgraph-checkpoint-aerospike/) | [aerospike-community/aerospike-langgraph](https://github.com/aerospike-community/aerospike-langgraph)                           |

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/checkpointers/index.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Document loader integrations
Source: https://docs.langchain.com/oss/python/integrations/document_loaders/index

Integrate with document loaders using LangChain Python.

Document loaders provide a **standard interface** for reading data from different sources (such as Slack, Notion, or Google Drive) into LangChain’s [Document](https://reference.langchain.com/python/langchain-core/documents/base/Document) format.
This ensures that data can be handled consistently regardless of the source.

All document loaders implement the [`BaseLoader`](https://reference.langchain.com/python/langchain-core/document_loaders/base/BaseLoader) interface.

<Warning>
  Community document loaders are user-contributed and unverified. LangChain does not review or endorse these integrations; use them at your own risk.
</Warning>

## Interface

Each document loader may define its own parameters, but they share a common API:

* `load()` – Loads all documents at once.
* `lazy_load()` – Streams documents lazily, useful for large datasets.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain_docling.loader import DoclingLoader

FILE_PATH = "https://arxiv.org/pdf/2408.09869"

loader = DoclingLoader(file_path=FILE_PATH)

# Load all documents
documents = loader.load()
