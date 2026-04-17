[Skip to main content](https://docs.langchain.com/oss/python/langchain/quickstart#content-area)
[Docs by LangChain home page![light logo](https://mintcdn.com/langchain-5e9cc07a/nQm-sjd_MByLhgeW/images/brand/langchain-docs-dark-blue.png?fit=max&auto=format&n=nQm-sjd_MByLhgeW&q=85&s=5babf1a1962208fd7eed942fa2432ecb)![dark logo](https://mintcdn.com/langchain-5e9cc07a/nQm-sjd_MByLhgeW/images/brand/langchain-docs-light-blue.png?fit=max&auto=format&n=nQm-sjd_MByLhgeW&q=85&s=0bcd2a1f2599ed228bcedf0f535b45b1)](https://docs.langchain.com/)![https://mintlify.s3.us-west-1.amazonaws.com/langchain-5e9cc07a/images/brand/langchain-icon.png](https://mintlify.s3.us-west-1.amazonaws.com/langchain-5e9cc07a/images/brand/langchain-icon.png)Open source
Search...
Ctrl K
  * [](https://chat.langchain.com/)
  * [Try LangSmith](https://smith.langchain.com/)
  * [Try LangSmith](https://smith.langchain.com/)


Search...
Navigation
Get started
Quickstart
[Deep Agents](https://docs.langchain.com/oss/python/deepagents/overview)[LangChain](https://docs.langchain.com/oss/python/langchain/overview)[LangGraph](https://docs.langchain.com/oss/python/langgraph/overview)[Integrations](https://docs.langchain.com/oss/python/integrations/providers/overview)[Learn](https://docs.langchain.com/oss/python/learn)[Reference](https://docs.langchain.com/oss/python/reference/overview)[Contribute](https://docs.langchain.com/oss/python/contributing/overview)
Python
  * [Overview](https://docs.langchain.com/oss/python/langchain/overview)


##### Get started
  * [Install](https://docs.langchain.com/oss/python/langchain/install)
  * [Quickstart](https://docs.langchain.com/oss/python/langchain/quickstart)
  * [Changelog](https://docs.langchain.com/oss/python/releases/changelog)
  * [Philosophy](https://docs.langchain.com/oss/python/langchain/philosophy)


##### Core components
  * [Agents](https://docs.langchain.com/oss/python/langchain/agents)
  * [Models](https://docs.langchain.com/oss/python/langchain/models)
  * [Messages](https://docs.langchain.com/oss/python/langchain/messages)
  * [Tools](https://docs.langchain.com/oss/python/langchain/tools)
  * [Short-term memory](https://docs.langchain.com/oss/python/langchain/short-term-memory)
  * Streaming
  * [Structured output](https://docs.langchain.com/oss/python/langchain/structured-output)


##### Middleware
  * [Overview](https://docs.langchain.com/oss/python/langchain/middleware/overview)
  * [Prebuilt middleware](https://docs.langchain.com/oss/python/langchain/middleware/built-in)
  * [Custom middleware](https://docs.langchain.com/oss/python/langchain/middleware/custom)


##### Advanced usage
  * [Guardrails](https://docs.langchain.com/oss/python/langchain/guardrails)
  * [Runtime](https://docs.langchain.com/oss/python/langchain/runtime)
  * [Context engineering](https://docs.langchain.com/oss/python/langchain/context-engineering)
  * [Model Context Protocol (MCP)](https://docs.langchain.com/oss/python/langchain/mcp)
  * [Human-in-the-loop](https://docs.langchain.com/oss/python/langchain/human-in-the-loop)
  * Multi-agent
  * [Retrieval](https://docs.langchain.com/oss/python/langchain/retrieval)
  * [Long-term memory](https://docs.langchain.com/oss/python/langchain/long-term-memory)


##### Agent development
  * [LangSmith Studio](https://docs.langchain.com/oss/python/langchain/studio)
  * [Test](https://docs.langchain.com/oss/python/langchain/test)
  * [Agent Chat UI](https://docs.langchain.com/oss/python/langchain/ui)


##### Deploy with LangSmith
  * [Deployment](https://docs.langchain.com/oss/python/langchain/deploy)
  * [Observability](https://docs.langchain.com/oss/python/langchain/observability)


On this page
  * [Requirements](https://docs.langchain.com/oss/python/langchain/quickstart#requirements)
  * [Build a basic agent](https://docs.langchain.com/oss/python/langchain/quickstart#build-a-basic-agent)
  * [Build a real-world agent](https://docs.langchain.com/oss/python/langchain/quickstart#build-a-real-world-agent)


[Get started](https://docs.langchain.com/oss/python/langchain/install)
# Quickstart
Copy page
Copy page
This quickstart takes you from a simple setup to a fully functional AI agent in just a few minutes.
**LangChain Docs MCP server** If you’re using an AI coding assistant or IDE (e.g. Claude Code or Cursor), you should install the [LangChain Docs MCP server](https://docs.langchain.com/use-these-docs) to get the most out of it. This ensures your agent has access to up-to-date LangChain documentation and examples.
##
[​](https://docs.langchain.com/oss/python/langchain/quickstart#requirements)
Requirements
For these examples, you will need to:
  * [Install](https://docs.langchain.com/oss/python/langchain/install) the LangChain package
  * Set up a
  * Set the `ANTHROPIC_API_KEY` environment variable in your terminal

Although these examples use Claude, you can use [any supported model](https://docs.langchain.com/oss/python/integrations/providers/overview) by changing the model name in the code and setting up the appropriate API key.
##
[​](https://docs.langchain.com/oss/python/langchain/quickstart#build-a-basic-agent)
Build a basic agent
Start by creating a simple agent that can answer questions and call tools. The agent will use Claude Sonnet 4.5 as its language model, a basic weather function as a tool, and a simple prompt to guide its behavior.
Copy
```
from langchain.agents import create_agent

def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

agent = create_agent(
    model="claude-sonnet-4-6",
    tools=[get_weather],
    system_prompt="You are a helpful assistant",
)

# Run the agent
agent.invoke(
    {"messages": [{"role": "user", "content": "what is the weather in sf"}]}
)

```

To learn how to trace your agent with LangSmith, see the [LangSmith documentation](https://docs.langchain.com/langsmith/trace-with-langchain).
##
[​](https://docs.langchain.com/oss/python/langchain/quickstart#build-a-real-world-agent)
Build a real-world agent
Next, build a practical weather forecasting agent that demonstrates key production concepts:
  1. **Detailed system prompts** for better agent behavior
  2. **Create tools** that integrate with external data
  3. **Model configuration** for consistent responses
  4. **Structured output** for predictable results
  5. **Conversational memory** for chat-like interactions
  6. **Create and run the agent** to test the fully functional agent

Let’s walk through each step:
1
[](https://docs.langchain.com/oss/python/langchain/quickstart)
Define the system prompt
The system prompt defines your agent’s role and behavior. Keep it specific and actionable:
Copy
```
SYSTEM_PROMPT = """You are an expert weather forecaster, who speaks in puns.

You have access to two tools:

- get_weather_for_location: use this to get the weather for a specific location
- get_user_location: use this to get the user's location

If a user asks you for the weather, make sure you know the location. If you can tell from the question that they mean wherever they are, use the get_user_location tool to find their location."""

```

2
[](https://docs.langchain.com/oss/python/langchain/quickstart)
Create tools
[Tools](https://docs.langchain.com/oss/python/langchain/tools) let a model interact with external systems by calling functions you define. Tools can depend on [runtime context](https://docs.langchain.com/oss/python/langchain/runtime) and also interact with [agent memory](https://docs.langchain.com/oss/python/langchain/short-term-memory).Notice below how the `get_user_location` tool uses runtime context:
Copy
```
from dataclasses import dataclass
from langchain.tools import tool, ToolRuntime

@tool
def get_weather_for_location(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

@dataclass
class Context:
    """Custom runtime context schema."""
    user_id: str

@tool
def get_user_location(runtime: ToolRuntime[Context]) -> str:
    """Retrieve user information based on user ID."""
    user_id = runtime.context.user_id
    return "Florida" if user_id == "1" else "SF"

```

Tools should be well-documented: their name, description, and argument names become part of the model’s prompt. LangChain’s [`@tool` decorator](https://reference.langchain.com/python/langchain-core/tools/convert/tool) adds metadata and enables runtime injection with the `ToolRuntime` parameter.
3
[](https://docs.langchain.com/oss/python/langchain/quickstart)
Configure your model
Set up your [language model](https://docs.langchain.com/oss/python/langchain/models) with the right parameters for your use case:
Copy
```
from langchain.chat_models import init_chat_model

model = init_chat_model(
    "claude-sonnet-4-6",
    temperature=0.5,
    timeout=10,
    max_tokens=1000
)

```

Depending on the model and provider chosen, initialization parameters may vary; refer to their reference pages for details.
4
[](https://docs.langchain.com/oss/python/langchain/quickstart)
Define response format
Optionally, define a structured response format if you need the agent responses to match a specific schema.
Copy
```
from dataclasses import dataclass

# We use a dataclass here, but Pydantic models are also supported.
@dataclass
class ResponseFormat:
    """Response schema for the agent."""
    # A punny response (always required)
    punny_response: str
    # Any interesting information about the weather if available
    weather_conditions: str | None = None

```

5
[](https://docs.langchain.com/oss/python/langchain/quickstart)
Add memory
Add [memory](https://docs.langchain.com/oss/python/langchain/short-term-memory) to your agent to maintain state across interactions. This allows the agent to remember previous conversations and context.
Copy
```
from langgraph.checkpoint.memory import InMemorySaver

checkpointer = InMemorySaver()

```

In production, use a persistent checkpointer that saves message history to a database. See [Add and manage memory](https://docs.langchain.com/oss/python/langgraph/add-memory#manage-short-term-memory) for more details.
6
[](https://docs.langchain.com/oss/python/langchain/quickstart)
Create and run the agent
Now assemble your agent with all the components and run it!
Copy
```
from langchain.agents.structured_output import ToolStrategy

agent = create_agent(
    model=model,
    system_prompt=SYSTEM_PROMPT,
    tools=[get_user_location, get_weather_for_location],
    context_schema=Context,
    response_format=ToolStrategy(ResponseFormat),
    checkpointer=checkpointer
)

# `thread_id` is a unique identifier for a given conversation.
config = {"configurable": {"thread_id": "1"}}

response = agent.invoke(
    {"messages": [{"role": "user", "content": "what is the weather outside?"}]},
    config=config,
    context=Context(user_id="1")
)

print(response['structured_response'])
# ResponseFormat(
#     punny_response="Florida is still having a 'sun-derful' day! The sunshine is playing 'ray-dio' hits all day long! I'd say it's the perfect weather for some 'solar-bration'! If you were hoping for rain, I'm afraid that idea is all 'washed up' - the forecast remains 'clear-ly' brilliant!",
#     weather_conditions="It's always sunny in Florida!"
# )


# Note that we can continue the conversation using the same `thread_id`.
response = agent.invoke(
    {"messages": [{"role": "user", "content": "thank you!"}]},
    config=config,
    context=Context(user_id="1")
)

print(response['structured_response'])
# ResponseFormat(
#     punny_response="You're 'thund-erfully' welcome! It's always a 'breeze' to help you stay 'current' with the weather. I'm just 'cloud'-ing around waiting to 'shower' you with more forecasts whenever you need them. Have a 'sun-sational' day in the Florida sunshine!",
#     weather_conditions=None
# )

```

Show Full example code
Copy
```
from dataclasses import dataclass

from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from langchain.tools import tool, ToolRuntime
from langgraph.checkpoint.memory import InMemorySaver
from langchain.agents.structured_output import ToolStrategy


# Define system prompt
SYSTEM_PROMPT = """You are an expert weather forecaster, who speaks in puns.

You have access to two tools:

- get_weather_for_location: use this to get the weather for a specific location
- get_user_location: use this to get the user's location

If a user asks you for the weather, make sure you know the location. If you can tell from the question that they mean wherever they are, use the get_user_location tool to find their location."""

# Define context schema
@dataclass
class Context:
    """Custom runtime context schema."""
    user_id: str

# Define tools
@tool
def get_weather_for_location(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

@tool
def get_user_location(runtime: ToolRuntime[Context]) -> str:
    """Retrieve user information based on user ID."""
    user_id = runtime.context.user_id
    return "Florida" if user_id == "1" else "SF"

# Configure model
model = init_chat_model(
    "claude-sonnet-4-6",
    temperature=0
)

# Define response format
@dataclass
class ResponseFormat:
    """Response schema for the agent."""
    # A punny response (always required)
    punny_response: str
    # Any interesting information about the weather if available
    weather_conditions: str | None = None

# Set up memory
checkpointer = InMemorySaver()

# Create agent
agent = create_agent(
    model=model,
    system_prompt=SYSTEM_PROMPT,
    tools=[get_user_location, get_weather_for_location],
    context_schema=Context,
    response_format=ToolStrategy(ResponseFormat),
    checkpointer=checkpointer
)

# Run agent
# `thread_id` is a unique identifier for a given conversation.
config = {"configurable": {"thread_id": "1"}}

response = agent.invoke(
    {"messages": [{"role": "user", "content": "what is the weather outside?"}]},
    config=config,
    context=Context(user_id="1")
)

print(response['structured_response'])
# ResponseFormat(
#     punny_response="Florida is still having a 'sun-derful' day! The sunshine is playing 'ray-dio' hits all day long! I'd say it's the perfect weather for some 'solar-bration'! If you were hoping for rain, I'm afraid that idea is all 'washed up' - the forecast remains 'clear-ly' brilliant!",
#     weather_conditions="It's always sunny in Florida!"
# )


# Note that we can continue the conversation using the same `thread_id`.
response = agent.invoke(
    {"messages": [{"role": "user", "content": "thank you!"}]},
    config=config,
    context=Context(user_id="1")
)

print(response['structured_response'])
# ResponseFormat(
#     punny_response="You're 'thund-erfully' welcome! It's always a 'breeze' to help you stay 'current' with the weather. I'm just 'cloud'-ing around waiting to 'shower' you with more forecasts whenever you need them. Have a 'sun-sational' day in the Florida sunshine!",
#     weather_conditions=None
# )

```

To learn how to trace your agent with LangSmith, see the [LangSmith documentation](https://docs.langchain.com/langsmith/trace-with-langchain).
Congratulations! You now have an AI agent that can:
  * **Understand context** and remember conversations
  * **Use multiple tools** intelligently
  * **Provide structured responses** in a consistent format
  * **Handle user-specific information** through context
  * **Maintain conversation state** across interactions


* * *
[Connect these docs](https://docs.langchain.com/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
Was this page helpful?
YesNo
[ Install LangChain Previous ](https://docs.langchain.com/oss/python/langchain/install)[ Changelog Next ](https://docs.langchain.com/oss/python/langchain/changelog-py)
Ctrl+I
[Docs by LangChain home page![light logo](https://mintcdn.com/langchain-5e9cc07a/nQm-sjd_MByLhgeW/images/brand/langchain-docs-dark-blue.png?fit=max&auto=format&n=nQm-sjd_MByLhgeW&q=85&s=5babf1a1962208fd7eed942fa2432ecb)![dark logo](https://mintcdn.com/langchain-5e9cc07a/nQm-sjd_MByLhgeW/images/brand/langchain-docs-light-blue.png?fit=max&auto=format&n=nQm-sjd_MByLhgeW&q=85&s=0bcd2a1f2599ed228bcedf0f535b45b1)](https://docs.langchain.com/)
Resources
[Forum](https://forum.langchain.com/)[Changelog](https://changelog.langchain.com/)[LangChain Academy](https://academy.langchain.com/)[Trust Center](https://trust.langchain.com/)
Company
[Home](https://langchain.com/)[About](https://langchain.com/about)[Careers](https://langchain.com/careers)[Blog](https://blog.langchain.com/)
