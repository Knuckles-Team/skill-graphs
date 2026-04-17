[Skip to main content](https://docs.langchain.com/oss/python/langchain/overview#content-area)
[Docs by LangChain home page![light logo](https://mintcdn.com/langchain-5e9cc07a/nQm-sjd_MByLhgeW/images/brand/langchain-docs-dark-blue.png?fit=max&auto=format&n=nQm-sjd_MByLhgeW&q=85&s=5babf1a1962208fd7eed942fa2432ecb)![dark logo](https://mintcdn.com/langchain-5e9cc07a/nQm-sjd_MByLhgeW/images/brand/langchain-docs-light-blue.png?fit=max&auto=format&n=nQm-sjd_MByLhgeW&q=85&s=0bcd2a1f2599ed228bcedf0f535b45b1)](https://docs.langchain.com/)![https://mintlify.s3.us-west-1.amazonaws.com/langchain-5e9cc07a/images/brand/langchain-icon.png](https://mintlify.s3.us-west-1.amazonaws.com/langchain-5e9cc07a/images/brand/langchain-icon.png)Open source
Search...
Ctrl K
  * [](https://chat.langchain.com/)
  * [Try LangSmith](https://smith.langchain.com/)
  * [Try LangSmith](https://smith.langchain.com/)


Search...
Navigation
LangChain overview
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
  * [ Create an agent](https://docs.langchain.com/oss/python/langchain/overview#create-an-agent)
  * [ Core benefits](https://docs.langchain.com/oss/python/langchain/overview#core-benefits)


# LangChain overview
Copy page
LangChain is an open source framework with a pre-built agent architecture and integrations for any model or tool — so you can build agents that adapt as fast as the ecosystem evolves
Copy page
LangChain is the easy way to start building completely custom agents and applications powered by LLMs. With under 10 lines of code, you can connect to OpenAI, Anthropic, Google, and [more](https://docs.langchain.com/oss/python/integrations/providers/overview). LangChain provides a pre-built agent architecture and model integrations to help you get started quickly and seamlessly incorporate LLMs into your agents and applications.
**LangChain vs. LangGraph vs. Deep Agents** If you are looking to build an agent, we recommend you start with [Deep Agents](https://docs.langchain.com/oss/python/deepagents/overview) which comes “batteries-included”, with modern features like automatic compression of long conversations, a virtual filesystem, and subagent-spawning for managing and isolating context.Deep Agents are implementations of LangChain [agents](https://docs.langchain.com/oss/python/langchain/agents). If you don’t need these capabilities or would like to customize your own for your agents and autonomous applications, start with LangChain.Use [LangGraph](https://docs.langchain.com/oss/python/langgraph/overview), our low-level agent orchestration framework and runtime, when you have more advanced needs that require a combination of deterministic and agentic workflows and heavy customization.
LangChain [agents](https://docs.langchain.com/oss/python/langchain/agents) are built on top of LangGraph in order to provide durable execution, streaming, human-in-the-loop, persistence, and more. You do not need to know LangGraph for basic LangChain agent usage. We recommend you use LangChain if you want to quickly build agents and autonomous applications.
##
[​](https://docs.langchain.com/oss/python/langchain/overview#create-an-agent)
Copy
```
# pip install -qU langchain "langchain[anthropic]"
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

See the [Installation instructions](https://docs.langchain.com/oss/python/langchain/install) and [Quickstart guide](https://docs.langchain.com/oss/python/langchain/quickstart) to get started building your own agents and applications with LangChain.
Use [LangSmith](https://docs.langchain.com/langsmith/home) to trace requests, debug agent behavior, and evaluate outputs. Set `LANGSMITH_TRACING=true` and your API key to get started.
##
[​](https://docs.langchain.com/oss/python/langchain/overview#core-benefits)
## [Standard model interface Different providers have unique APIs for interacting with models, including the format of responses. LangChain standardizes how you interact with models so that you can seamlessly swap providers and avoid lock-in. Learn more ](https://docs.langchain.com/oss/python/langchain/models)## [Easy to use, highly flexible agent LangChain’s agent abstraction is designed to be easy to get started with, letting you build a simple agent in under 10 lines of code. But it also provides enough flexibility to allow you to do all the context engineering your heart desires. Learn more ](https://docs.langchain.com/oss/python/langchain/agents)[ ![https://mintcdn.com/langchain-5e9cc07a/nQm-sjd_MByLhgeW/images/brand/langgraph-icon.png?fit=max&auto=format&n=nQm-sjd_MByLhgeW&q=85&s=b997e1a7487d507a36556eedbfd99f81](https://mintcdn.com/langchain-5e9cc07a/nQm-sjd_MByLhgeW/images/brand/langgraph-icon.png?fit=max&auto=format&n=nQm-sjd_MByLhgeW&q=85&s=b997e1a7487d507a36556eedbfd99f81) Built on top of LangGraph LangChain’s agents are built on top of LangGraph. This allows us to take advantage of LangGraph’s durable execution, human-in-the-loop support, persistence, and more. Learn more ](https://docs.langchain.com/oss/python/langgraph/overview)[ ![https://mintcdn.com/langchain-5e9cc07a/nQm-sjd_MByLhgeW/images/brand/observability-icon-dark.png?fit=max&auto=format&n=nQm-sjd_MByLhgeW&q=85&s=ccbc183bca2a5e4ca78d30149e3836cc](https://mintcdn.com/langchain-5e9cc07a/nQm-sjd_MByLhgeW/images/brand/observability-icon-dark.png?fit=max&auto=format&n=nQm-sjd_MByLhgeW&q=85&s=ccbc183bca2a5e4ca78d30149e3836cc) Debug with LangSmith Gain deep visibility into complex agent behavior with visualization tools that trace execution paths, capture state transitions, and provide detailed runtime metrics. Learn more ](https://docs.langchain.com/langsmith/observability)
* * *
[Connect these docs](https://docs.langchain.com/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
Was this page helpful?
YesNo
[ Install LangChain Next ](https://docs.langchain.com/oss/python/langchain/install)
Ctrl+I
[Docs by LangChain home page![light logo](https://mintcdn.com/langchain-5e9cc07a/nQm-sjd_MByLhgeW/images/brand/langchain-docs-dark-blue.png?fit=max&auto=format&n=nQm-sjd_MByLhgeW&q=85&s=5babf1a1962208fd7eed942fa2432ecb)![dark logo](https://mintcdn.com/langchain-5e9cc07a/nQm-sjd_MByLhgeW/images/brand/langchain-docs-light-blue.png?fit=max&auto=format&n=nQm-sjd_MByLhgeW&q=85&s=0bcd2a1f2599ed228bcedf0f535b45b1)](https://docs.langchain.com/)
Resources
[Forum](https://forum.langchain.com/)[Changelog](https://changelog.langchain.com/)[LangChain Academy](https://academy.langchain.com/)[Trust Center](https://trust.langchain.com/)
Company
[Home](https://langchain.com/)[About](https://langchain.com/about)[Careers](https://langchain.com/careers)[Blog](https://blog.langchain.com/)
