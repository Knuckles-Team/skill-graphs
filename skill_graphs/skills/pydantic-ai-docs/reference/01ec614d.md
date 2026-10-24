# Built-in Tools
Built-in tools are native tools provided by LLM providers that can be used to enhance your agent's capabilities. Unlike [common tools](https://ai.pydantic.dev/common-tools/), which are custom implementations that Pydantic AI executes, built-in tools are executed directly by the model provider.
## Overview
Pydantic AI supports the following built-in tools:
  * **[`WebSearchTool`](https://ai.pydantic.dev/api/builtin_tools/#pydantic_ai.builtin_tools.WebSearchTool "WebSearchTool



      dataclass
  ")**: Allows agents to search the web
  * **[`CodeExecutionTool`](https://ai.pydantic.dev/api/builtin_tools/#pydantic_ai.builtin_tools.CodeExecutionTool "CodeExecutionTool



      dataclass
  ")**: Enables agents to execute code in a secure environment
  * **[`ImageGenerationTool`](https://ai.pydantic.dev/api/builtin_tools/#pydantic_ai.builtin_tools.ImageGenerationTool "ImageGenerationTool



      dataclass
  ")**: Enables agents to generate images
  * **[`WebFetchTool`](https://ai.pydantic.dev/api/builtin_tools/#pydantic_ai.builtin_tools.WebFetchTool "WebFetchTool



      dataclass
  ")**: Enables agents to fetch web pages
  * **[`MemoryTool`](https://ai.pydantic.dev/api/builtin_tools/#pydantic_ai.builtin_tools.MemoryTool "MemoryTool



      dataclass
  ")**: Enables agents to use memory
  * **[`MCPServerTool`](https://ai.pydantic.dev/api/builtin_tools/#pydantic_ai.builtin_tools.MCPServerTool "MCPServerTool



      dataclass
  ")**: Enables agents to use remote MCP servers with communication handled by the model provider
  * **[`FileSearchTool`](https://ai.pydantic.dev/api/builtin_tools/#pydantic_ai.builtin_tools.FileSearchTool "FileSearchTool



      dataclass
  ")**: Enables agents to search through uploaded files using vector search (RAG)


These tools are passed to the agent via the `builtin_tools` parameter and are executed by the model provider's infrastructure.
Provider Support
Not all model providers support built-in tools. If you use a built-in tool with an unsupported provider, Pydantic AI will raise a [`UserError`](https://ai.pydantic.dev/api/exceptions/#pydantic_ai.exceptions.UserError "UserError") when you try to run the agent.
If a provider supports a built-in tool that is not currently supported by Pydantic AI, please file an issue.
## Dynamic Configuration
Sometimes you need to configure a built-in tool dynamically based on the [run context](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext "RunContext



      dataclass
  ") (e.g., user dependencies), or conditionally omit it. You can achieve this by passing a function to `builtin_tools` that takes [`RunContext`](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext "RunContext



      dataclass
  ") as an argument and returns an [`AbstractBuiltinTool`](https://ai.pydantic.dev/api/builtin_tools/#pydantic_ai.builtin_tools.AbstractBuiltinTool "AbstractBuiltinTool



      dataclass
  ") or `None`.
This is particularly useful for tools like [`WebSearchTool`](https://ai.pydantic.dev/api/builtin_tools/#pydantic_ai.builtin_tools.WebSearchTool "WebSearchTool



      dataclass
  ") where you might want to set the user's location based on the current request, or disable the tool if the user provides no location.
[With Pydantic AI Gateway](https://ai.pydantic.dev/builtin-tools/#__tabbed_1_1)[Directly to Provider API](https://ai.pydantic.dev/builtin-tools/#__tabbed_1_2)
[Learn about Gateway](https://ai.pydantic.dev/gateway) dynamic_builtin_tool.py```
from pydantic_ai import Agent, RunContext, WebSearchTool


async def prepared_web_search(ctx: RunContext[dict]) -> WebSearchTool | None:
    if not ctx.deps.get('location'):
        return None

    return WebSearchTool(
        user_location={'city': ctx.deps['location']},
    )

agent = Agent(
    'gateway/openai-responses:gpt-5.2',
    builtin_tools=[prepared_web_search],
    deps_type=dict,
)
