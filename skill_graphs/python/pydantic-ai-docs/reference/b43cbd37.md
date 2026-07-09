
```

Create a Starlette app that serves a web chat UI for this agent.
This method returns a pre-configured Starlette application that provides a web-based chat interface for interacting with the agent. By default, the UI is fetched from a CDN and cached on first use.
The returned Starlette application can be mounted into a FastAPI app or run directly with any ASGI server (uvicorn, hypercorn, etc.).
Note that the `deps` and `model_settings` will be the same for each request. To provide different `deps` for each request use the lower-level adapters directly.
Parameters:
Name | Type | Description | Default
---|---|---|---
`models` |  `ModelsParam` |  Additional models to make available in the UI. Can be: - A sequence of model names/instances (e.g., `['openai:gpt-5', 'anthropic:claude-sonnet-4-6']`) - A dict mapping display labels to model names/instances (e.g., `{'GPT 5': 'openai:gpt-5', 'Claude': 'anthropic:claude-sonnet-4-6'}`) The agent's model is always included. Builtin tool support is automatically determined from each model's profile. |  `None`
`builtin_tools` |  `AbstractBuiltinTool[](https://ai.pydantic.dev/api/builtin_tools/#pydantic_ai.builtin_tools.AbstractBuiltinTool "AbstractBuiltinTool



      dataclass
   \(pydantic_ai.builtin_tools.AbstractBuiltinTool\)")] | None` |  Additional builtin tools to make available in the UI. The agent's configured builtin tools are always included. Tool labels in the UI are derived from the tool's `label` property. |  `None`
`deps` |  `AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)")` |  Optional dependencies to use for all requests. |  `None`
`model_settings` |  `ModelSettings[](https://ai.pydantic.dev/api/settings/#pydantic_ai.settings.ModelSettings "ModelSettings \(pydantic_ai.settings.ModelSettings\)") | None` |  Optional settings to use for all model requests. |  `None`
`instructions` |  |  Optional extra instructions to pass to each agent run. |  `None`
`html_source` |  |  Path or URL for the chat UI HTML. Can be: - None (default): Fetches from CDN and caches locally - A Path instance: Reads from the local file - A URL string (http:// or https://): Fetches from the URL - A file path string: Reads from the local file |  `None`
Returns:
Type | Description
---|---
`Starlette` |  A configured Starlette application ready to be served (e.g., with uvicorn)
Example
```
from pydantic_ai import Agent
from pydantic_ai.builtin_tools import WebSearchTool

agent = Agent('openai:gpt-5', builtin_tools=[WebSearchTool()])
