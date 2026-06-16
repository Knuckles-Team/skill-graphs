# Instrument CrewAI and OpenAI
CrewAIInstrumentor().instrument(tracer_provider=tracer_provider)
OpenAIInstrumentor().instrument(tracer_provider=tracer_provider)
```

### 3. Create and run your CrewAI application

Once configured, your CrewAI application will automatically send traces to LangSmith:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from crewai import Agent, Crew, Task
from crewai.llm import LLM
from langsmith.integrations.otel import OtelSpanProcessor
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.instrumentation.crewai import CrewAIInstrumentor
from opentelemetry.instrumentation.openai import OpenAIInstrumentor

# Configure OpenTelemetry
current_provider = trace.get_tracer_provider()
if isinstance(current_provider, TracerProvider):
    tracer_provider = current_provider
else:
    tracer_provider = TracerProvider()
    trace.set_tracer_provider(tracer_provider)

tracer_provider.add_span_processor(OtelSpanProcessor())

# Instrument CrewAI and OpenAI
CrewAIInstrumentor().instrument(tracer_provider=tracer_provider)
OpenAIInstrumentor().instrument(tracer_provider=tracer_provider)

# Define your agent
llm = LLM(model="gpt-4o-mini")

coder = Agent(
    role="Software developer",
    goal="Write clear, concise code on demand",
    backstory="An expert coder with a keen eye for software trends.",
    verbose=True,
    llm=llm,
)

# Define your task
task = Task(
    description="Write a Python function that checks if a number is prime.",
    expected_output="A clear and concise Python function with documentation.",
    agent=coder,
)

# Create and run the crew
crew = Crew(
    agents=[coder],
    tasks=[task],
    verbose=True,
)

def run_crew():
    result = crew.kickoff()
    return result

if __name__ == "__main__":
    output = run_crew()
    print(output)
```

## Advanced usage

### Custom metadata and tags

You can add custom metadata to your traces by setting span attributes:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from opentelemetry import trace

tracer = trace.get_tracer(__name__)

def run_crew_with_metadata():
    with tracer.start_as_current_span("crewai_workflow") as span:
        span.set_attribute("langsmith.metadata.crew_type", "code_generation")
        span.set_attribute("langsmith.metadata.agent_count", "1")
        span.set_attribute("langsmith.span.tags", "crewai,code-generation")

        result = crew.kickoff()
        return result
```

### Combining with other instrumentors

You can combine CrewAI instrumentation with other OpenTelemetry instrumentors:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from opentelemetry.instrumentation.crewai import CrewAIInstrumentor
from opentelemetry.instrumentation.openai import OpenAIInstrumentor

# Initialize multiple instrumentors
CrewAIInstrumentor().instrument(tracer_provider=tracer_provider)
OpenAIInstrumentor().instrument(tracer_provider=tracer_provider)
```

## Resources

* [CrewAI documentation](https://docs.crewai.com/)
* [LangSmith OpenTelemetry guide](/langsmith/trace-with-opentelemetry)

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/trace-with-crewai.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Trace Google ADK applications
Source: https://docs.langchain.com/langsmith/trace-with-google-adk

This guide shows you how to trace [Google Agent Development Kit (ADK)](https://github.com/google/adk-python) agents in LangSmith. You'll configure automatic tracing for your ADK applications to capture agent invocations, tool calls, and LLM interactions.

## Installation

Install the required packages using your preferred package manager:

<CodeGroup>
  ```bash uv theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  uv add langsmith[google-adk]
  ```

  ```bash pip theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  pip install langsmith[google-adk]
  ```
</CodeGroup>

## Setup

Set your [API keys](/langsmith/create-account-api-key):

<CodeGroup>
  ```bash shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  export LANGSMITH_TRACING=true
  export LANGSMITH_ENDPOINT=https://api.smith.langchain.com
  export LANGSMITH_API_KEY=<your_langsmith_api_key>
  export LANGSMITH_PROJECT=<your_langsmith_project>

  export GOOGLE_API_KEY=<your_google_api_key>
  ```

  ```dotenv .env theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  LANGSMITH_TRACING=true
  LANGSMITH_ENDPOINT=https://api.smith.langchain.com
  LANGSMITH_API_KEY=<your_langsmith_api_key>
  LANGSMITH_PROJECT=<your_langsmith_project>

  GOOGLE_API_KEY=<your_google_api_key>
  ```
</CodeGroup>

To create a Google API key, refer to [Google AI Studio](https://aistudio.google.com/api-keys).

## Configure tracing

To trace ADK agents, use `configure_google_adk()` from the LangSmith SDK. Call this function once at the start of your application before creating any ADK agents:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langsmith.integrations.google_adk import configure_google_adk

configure_google_adk(
    project_name="my-adk-project",  # Optional: defaults to LANGSMITH_PROJECT env var
)
```

The function accepts the following optional parameters:

* `project_name`: LangSmith project to send traces to. Defaults to the `LANGSMITH_PROJECT` environment variable.
* `name`: Name for the root trace. Defaults to `"google_adk.session"`.
* `metadata`: Dictionary of key-value pairs for additional context.
* `tags`: List of strings to categorize traces.

## Example

This example creates a weather agent with a tool, then runs it with tracing enabled:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import asyncio

from dotenv import load_dotenv  # Optional
from google.adk.agents import Agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
from langsmith.integrations.google_adk import configure_google_adk

load_dotenv()  # Optional

async def main():
    # Configure LangSmith tracing
    configure_google_adk()

    # Define a tool
    def get_weather(city: str) -> dict:
        """Get weather for a city."""
        return {"city": city, "temperature": "72°F", "conditions": "Sunny"}

    # Create the agent
    agent = Agent(
        name="weather_agent",
        model="gemini-2.0-flash",
        description="Provides weather information.",
        instruction="Use the get_weather tool to answer weather questions.",
        tools=[get_weather],
    )

    # Set up session and runner
    session_service = InMemorySessionService()
    session = await session_service.create_session(
        app_name="weather_app",
        user_id="user_123",
        session_id="session_456",
    )

    runner = Runner(
        agent=agent,
        app_name="weather_app",
        session_service=session_service,
    )

    # Run the agent
    async for event in runner.run_async(
        user_id="user_123",
        session_id=session.id,
        new_message=types.Content(
            role="user",
            parts=[types.Part(text="What's the weather in San Francisco?")],
        ),
    ):
        if event.is_final_response():
            print(event.content.parts[0].text)

if __name__ == "__main__":
    asyncio.run(main())
```

## View traces in LangSmith

After running your application, you can view traces in the [LangSmith UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-trace-with-google-adk) that include:

* **Agent invocations**: Complete flows through your ADK agents
* **Tool calls**: Individual function calls made by agents
* **LLM interactions**: Requests and responses from Gemini models
* **Multi-agent workflows**: Traces from sequential and parallel agent compositions

## Custom metadata and tags

Add metadata and tags when configuring tracing to categorize and filter traces:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langsmith.integrations.google_adk import configure_google_adk

configure_google_adk(
    project_name="production-agents",
    metadata={
        "environment": "production",
        "team": "ml-platform",
    },
    tags=["adk", "weather", "v2"],
)
```

## Multi-agent workflows

The integration automatically traces multi-agent workflows including sequential and parallel agent compositions:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import asyncio

from dotenv import load_dotenv  # Optional
from google.adk.agents import Agent, SequentialAgent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
from langsmith.integrations.google_adk import configure_google_adk

load_dotenv()  # Optional

async def main():
    # Configure LangSmith tracing
    # Traces go to LANGSMITH_PROJECT env var by default.
    # Pass project_name="my-project" to override.
    configure_google_adk()

    # Create sub-agents
    translator = Agent(
        name="translator",
        model="gemini-2.0-flash",
        description="Translates text to English.",
    )

    summarizer = Agent(
        name="summarizer",
        model="gemini-2.0-flash",
        description="Summarizes text concisely.",
    )

    # Create a sequential agent that runs sub-agents in order
    pipeline = SequentialAgent(
        name="translate_and_summarize",
        sub_agents=[translator, summarizer],
        description="Translates text then summarizes it.",
    )

    # Set up and run
    session_service = InMemorySessionService()
    session = await session_service.create_session(
        app_name="pipeline_app",
        user_id="user_123",
        session_id="session_456",
    )

    runner = Runner(
        agent=pipeline,
        app_name="pipeline_app",
        session_service=session_service,
    )

    events = runner.run_async(
        user_id="user_123",
        session_id=session.id,
        new_message=types.Content(
            role="user",
            parts=[types.Part(text="Quelle est la plus haute tour de Paris?")],
        ),
    )

    async for event in events:
        if event.is_final_response():
            print(event.content.parts[0].text)

if __name__ == "__main__":
    asyncio.run(main())
```

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/trace-with-google-adk.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Trace Google Gemini applications
Source: https://docs.langchain.com/langsmith/trace-with-google-gemini

This guide shows you how to trace and log [Google's Gemini](https://ai.google.dev/gemini-api/docs) models in LangSmith. You'll instrument Gemini calls using the latest [`google-genai` SDK](https://googleapis.github.io/python-genai/) (Python) or [`@google/genai` SDK](https://googleapis.github.io/js-genai/release_docs/index.html) (JavaScript), wrap the Gemini client for tracing, and try examples including basic prompts, metadata tagging, and multi-turn conversations.

<Note>
  The LangSmith Gemini wrappers are in **beta**. The API may change in future releases.
</Note>

## Installation

Install the required packages using your preferred package manager:

<CodeGroup>
  ```bash pip theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  pip install langsmith google-genai
  ```

  ```bash npm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  npm install langsmith@latest @google/genai
  ```
</CodeGroup>

## Setup

Set your [API keys](/langsmith/create-account-api-key) and project name:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
export LANGSMITH_API_KEY=<your_langsmith_api_key>
export LANGSMITH_PROJECT=<your_project_name>
export LANGSMITH_TRACING=true
export GOOGLE_API_KEY=<your_google_api_key>
```

To create a Google API key, refer to [Google AI Studio](https://aistudio.google.com/apikey).

## Configure tracing

To trace Gemini API calls, use LangSmith's [`wrap_gemini`](https://reference.langchain.com/python/langsmith/wrappers/_gemini/wrap_gemini) (Python) or [`wrapGemini`](https://reference.langchain.com/javascript/functions/langsmith.wrappers_gemini.wrapGemini.html) (JavaScript) wrapper function. This wrapper intercepts calls to the Gemini client and automatically logs them as traces in LangSmith. The wrapper preserves all of the original client's functionality while adding observability:

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from google import genai
  from langsmith import wrappers

  def main():
      # genai.Client() reads GOOGLE_API_KEY / GEMINI_API_KEY from the environment
      gemini_client = genai.Client()

      # Wrap the Gemini client to enable LangSmith tracing
      client = wrappers.wrap_gemini(
          gemini_client,
          tracing_extra={
              "tags": ["gemini", "python"],
              "metadata": {
                  "integration": "google-genai",
              },
          },
      )

      # Make a traced Gemini call
      response = client.models.generate_content(
          model="gemini-2.5-flash",
          contents="Explain quantum computing in simple terms.",
      )

      print(response.text)

  if __name__ == "__main__":
      main()
  ```

  ```javascript JavaScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { GoogleGenAI } from "@google/genai";
  import { wrapGemini } from "langsmith/wrappers/gemini";

  const GEMINI_API_KEY = process.env.GEMINI_API_KEY;

  // Initialize the Gemini client
  const geminiClient = new GoogleGenAI({ apiKey: GEMINI_API_KEY });

  // Wrap the client to enable LangSmith tracing
  // Configuration is applied to ALL calls made with this wrapped client
  const client = wrapGemini(geminiClient, {
    tags: ["gemini", "javascript"],
    metadata: {
      integration: "google-genai",
    },
  });

  // Make a traced call - tracing happens automatically
  const response = await client.models.generateContent({
    model: "gemini-2.5-flash",
    contents: "Explain quantum computing in simple terms.",
  });

  console.log(response.text);
  ```
</CodeGroup>

<Tabs>
  <Tab title="Python" icon="brand-python">
    You can customize tracing by passing [`tracing_extra`](https://reference.langchain.com/python/langsmith/wrappers/_gemini/wrap_gemini) when calling `wrap_gemini()`. This parameter applies to all subsequent requests you make with that wrapped client, which allows you to attach tags and metadata for filtering and organizing traces in the [LangSmith UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-trace-with-google-gemini). The `tracing_extra` parameter accepts:

    * `tags`: A list of strings to categorize traces (for example, `["production", "gemini"]`).
    * `metadata`: A dictionary of key-value pairs for additional context (for example, `{"team": "ml-research", "integration": "google-genai"}`).
    * `client`: An optional custom LangSmith client instance.

    These settings apply consistently across all traces from the wrapped client, so that you can include environment-level tags or team metadata that should remain constant throughout your application.
  </Tab>

  <Tab title="JavaScript" icon="brand-javascript">
    You can customize tracing by passing configuration options to [`wrapGemini`](https://reference.langchain.com/javascript/functions/langsmith.wrappers_gemini.wrapGemini.html). These options apply to all subsequent requests you make with that wrapped client, which allows you to attach tags and metadata for filtering and organizing traces in the [LangSmith UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-trace-with-google-gemini). The configuration accepts:

    * `tags`: An array of strings to categorize traces (for example, `["production", "gemini"]`).
    * `metadata`: An object with key-value pairs for additional context (for example, `{ team: "ml-research", integration: "google-genai" }`).
    * `client`: An optional custom LangSmith client instance.

    These settings apply consistently across all traces from the wrapped client, so that you can include environment-level tags or team metadata that should remain constant throughout your application.
  </Tab>
</Tabs>

## View traces in LangSmith

After running your application, you can view traces in the [LangSmith UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-trace-with-google-gemini) that include:

* **Model requests**: Complete prompts sent to Gemini models
* **Model responses**: Generated text and structured outputs
* **Function calls**: Tool invocations and results when using function calling
* **Chat sessions**: Multi-turn conversation context
* **Performance metrics**: Latency and token usage information

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/trace-with-google-gemini.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Trace Instructor applications
Source: https://docs.langchain.com/langsmith/trace-with-instructor

LangSmith provides a convenient integration with [Instructor](https://python.useinstructor.com/), a popular open-source library for generating structured output with LLMs.

In order to use, you first need to set your LangSmith API key.

```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
export LANGSMITH_API_KEY=<your-api-key>

# For LangSmith API keys linked to multiple workspaces, set the LANGSMITH_WORKSPACE_ID environment variable to specify which workspace to use.
export LANGSMITH_WORKSPACE_ID=<your-workspace-id>
```

Next, you will need to install the LangSmith SDK:

<CodeGroup>
  ```bash pip theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  pip install -U langsmith
  ```

  ```bash uv theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  uv add langsmith
  ```
</CodeGroup>

Wrap your OpenAI client with `langsmith.wrappers.wrap_openai`

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from openai import OpenAI
from langsmith import wrappers

client = wrappers.wrap_openai(OpenAI())
```

After this, you can patch the wrapped OpenAI client using `instructor`:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import instructor

client = instructor.patch(client)
```

Now, you can use `instructor` as you normally would, but now everything is logged to LangSmith!

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from pydantic import BaseModel

class UserDetail(BaseModel):
    name: str
    age: int

user = client.chat.completions.create(
    model="gpt-5.4-mini",
    response_model=UserDetail,
    messages=[
        {"role": "user", "content": "Extract Jason is 25 years old"},
    ]
)
```

Oftentimes, you use `instructor` inside of other functions.
You can get nested traces by using this wrapped client and decorating those functions with `@traceable`.
Please see [Custom instrumentation](/langsmith/annotate-code) for more information on how to annotate your code for tracing with the `@traceable` decorator.

```python {highlight={2}} theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}

# You can customize the run name with the `name` keyword argument
@traceable(name="Extract User Details")
def my_function(text: str) -> UserDetail:
    return client.chat.completions.create(
        model="gpt-5.4-mini",
        response_model=UserDetail,
        messages=[
            {"role": "user", "content": f"Extract {text}"},
        ]
    )

my_function("Jason is 25 years old")
```

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/trace-with-instructor.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Trace LangChain applications (Python and JS/TS)
Source: https://docs.langchain.com/langsmith/trace-with-langchain

LangSmith integrates seamlessly with LangChain (Python and JavaScript), the popular open-source framework for building LLM applications.

## Installation

Install the following for Python or JS (the code snippets use the OpenAI integration).

For a full list of packages available, see the [LangChain docs](/oss/python/integrations/providers/overview).

<CodeGroup>
  ```bash pip theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  pip install langchain_openai
  ```

  ```bash yarn theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  yarn add @langchain/openai @langchain/core
  ```

  ```bash npm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  npm install @langchain/openai @langchain/core
  ```

  ```bash pnpm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  pnpm add @langchain/openai @langchain/core
  ```
</CodeGroup>

## Quick start

### 1. Configure your environment

```bash wrap theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
export LANGSMITH_TRACING=true
export LANGSMITH_API_KEY=<your-api-key>

# This example uses OpenAI, but you can use any LLM provider of choice
export OPENAI_API_KEY=<your-openai-api-key>

# For LangSmith API keys linked to multiple workspaces, set the LANGSMITH_WORKSPACE_ID environment variable to specify which workspace to use.
export LANGSMITH_WORKSPACE_ID=<your-workspace-id>
```

<Note>
  If your account is in a region other than US (the default), also set `LANGSMITH_ENDPOINT` to the API URL for your region. Without this, your API key won't be recognized and requests will fail to authenticate.

  <table>
    <thead>
      <tr>
        <th>Region</th>
      </tr>
    </thead>

    <tbody>
      <tr>
        <td>GCP US</td>
      </tr>

      <tr>
        <td>GCP EU</td>
      </tr>

      <tr>
        <td>GCP APAC</td>
      </tr>

      <tr>
        <td>AWS US</td>
      </tr>
    </tbody>
  </table>

  For example, EU accounts: `export LANGSMITH_ENDPOINT="https://eu.api.smith.langchain.com"`.
</Note>

<Info>
  If you are using LangChain.js with LangSmith and are not in a serverless environment, we also recommend setting the following explicitly to reduce latency:

  `export LANGCHAIN_CALLBACKS_BACKGROUND=true`

  If you are in a serverless environment, we recommend setting the reverse to allow tracing to finish before your function ends:

  `export LANGCHAIN_CALLBACKS_BACKGROUND=false`
</Info>

### 2. Log a trace

No extra code is needed to log a trace to LangSmith. Just run your LangChain code as you normally would.

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langchain_openai import ChatOpenAI
  from langchain_core.prompts import ChatPromptTemplate
  from langchain_core.output_parsers import StrOutputParser

  prompt = ChatPromptTemplate.from_messages([
      ("system", "You are a helpful assistant. Please respond to the user's request only based on the given context."),
      ("user", "Question: {question}\nContext: {context}")
  ])

  model = ChatOpenAI(model="gpt-5.4-mini")
  output_parser = StrOutputParser()
  chain = prompt | model | output_parser

  question = "Can you summarize this morning's meetings?"
  context = "During this morning's meeting, we solved all world conflict."

  chain.invoke({"question": question, "context": context})
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { ChatOpenAI } from "@langchain/openai";
  import { ChatPromptTemplate } from "@langchain/core/prompts";
  import { StringOutputParser } from "@langchain/core/output_parsers";

  const prompt = ChatPromptTemplate.fromMessages([
    ["system", "You are a helpful assistant. Please respond to the user's request only based on the given context."],
    ["user", "Question: {question}\nContext: {context}"],
  ]);

  const model = new ChatOpenAI({ modelName: "gpt-5.4-mini" });
  const outputParser = new StringOutputParser();
  const chain = prompt.pipe(model).pipe(outputParser);

  const question = "Can you summarize this morning's meetings?"
  const context = "During this morning's meeting, we solved all world conflict."

  await chain.invoke({ question: question, context: context });
  ```
</CodeGroup>

### 3. View your trace

By default, the trace will be logged to the project with the name `default`. You can view an example of a trace logged using the above code [publicly in LangSmith](https://smith.langchain.com/public/e6a46eb2-d785-4804-a1e3-23f167a04300/r).

## Trace selectively

The [previous section](#quick-start) showed how to trace all invocations of a LangChain runnables within your applications by setting a single environment variable. While this is a convenient way to get started, you may want to trace only specific invocations or parts of your application.

There are two ways to do this in Python: by manually passing in a `LangChainTracer` instance as a [callback](https://reference.langchain.com/python/langchain_core/callbacks/), or by using the [`tracing_context` context manager](https://reference.langchain.com/python/langsmith/observability/sdk/run_helpers/#langsmith.run_helpers.tracing_context).

In JS/TS, you can pass a [`LangChainTracer`](https://reference.langchain.com/javascript/classes/_langchain_core.tracers_tracer_langchain.LangChainTracer.html) instance as a callback.

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  # You can opt-in to specific invocations..
  import langsmith as ls

  with ls.tracing_context(enabled=True):
      chain.invoke({"question": "Am I using a callback?", "context": "I'm using a callback"})

  # This will NOT be traced (assuming LANGSMITH_TRACING is not set)
  chain.invoke({"question": "Am I being traced?", "context": "I'm not being traced"})

  # This would not be traced, even if LANGSMITH_TRACING=true
  with ls.tracing_context(enabled=False):
      chain.invoke({"question": "Am I being traced?", "context": "I'm not being traced"})
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  // You can configure a LangChainTracer instance to trace a specific invocation.
  import { LangChainTracer } from "@langchain/core/tracers/tracer_langchain";

  const tracer = new LangChainTracer();
  await chain.invoke(
    {
      question: "Am I using a callback?",
      context: "I'm using a callback"
    },
    { callbacks: [tracer] }
  );
  ```
</CodeGroup>

## Log to a specific project

### Statically

As mentioned in the [tracing conceptual guide](/langsmith/observability-concepts) LangSmith uses the concept of a Project to group traces. If left unspecified, the tracer project is set to default. You can set the `LANGSMITH_PROJECT` environment variable to configure a custom project name for an entire application run. This should be done before executing your application.

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
export LANGSMITH_PROJECT=my-project
```

<Warning>
  The `LANGSMITH_PROJECT` flag is only supported in JS SDK versions >= 0.2.16, use `LANGCHAIN_PROJECT` instead if you are using an older version.
</Warning>

### Dynamically

This largely builds off of the [previous section](#trace-selectively) and allows you to set the project name for a specific `LangChainTracer` instance or as parameters to the `tracing_context` context manager in Python.

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  # You can set the project name using the project_name parameter.
  import langsmith as ls

  with ls.tracing_context(project_name="My Project", enabled=True):
      chain.invoke({"question": "Am I using a context manager?", "context": "I'm using a context manager"})
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  // You can set the project name for a specific tracer instance:
  import { LangChainTracer } from "@langchain/core/tracers/tracer_langchain";

  const tracer = new LangChainTracer({ projectName: "My Project" });
  await chain.invoke(
    {
      question: "Am I using a callback?",
      context: "I'm using a callback"
    },
    { callbacks: [tracer] }
  );
  ```
</CodeGroup>

## Add metadata and tags to traces

You can annotate your traces with arbitrary metadata and tags by providing them in the [`RunnableConfig`](https://reference.langchain.com/python/langchain_core/runnables/?h=runnablecon#langchain_core.runnables.RunnableConfig). This is useful for associating additional information with a trace, such as the environment in which it was executed, or the user who initiated it. For information on how to query traces and runs by metadata and tags, see [Query traces (SDK)](/langsmith/export-traces)

<Note>
  When you attach metadata or tags to a runnable (either through the [`RunnableConfig`](https://reference.langchain.com/python/langchain-core/runnables/config/RunnableConfig) or at runtime with invocation params), they are inherited by all child runnables of that runnable.
</Note>

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langchain_openai import ChatOpenAI
  from langchain_core.prompts import ChatPromptTemplate
  from langchain_core.output_parsers import StrOutputParser

  prompt = ChatPromptTemplate.from_messages([
      ("system", "You are a helpful AI."),
      ("user", "{input}")
  ])

  # The tag "model-tag" and metadata {"model-key": "model-value"} will be attached to the ChatOpenAI run only
  chat_model = ChatOpenAI().with_config({"tags": ["model-tag"], "metadata": {"model-key": "model-value"}})
  output_parser = StrOutputParser()

  # Tags and metadata can be configured with RunnableConfig
  chain = (prompt | chat_model | output_parser).with_config({"tags": ["config-tag"], "metadata": {"config-key": "config-value"}})

  # Tags and metadata can also be passed at runtime
  chain.invoke({"input": "What is the meaning of life?"}, {"tags": ["invoke-tag"], "metadata": {"invoke-key": "invoke-value"}})
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { ChatOpenAI } from "@langchain/openai";
  import { ChatPromptTemplate } from "@langchain/core/prompts";
  import { StringOutputParser } from "@langchain/core/output_parsers";

  const prompt = ChatPromptTemplate.fromMessages([
      ["system", "You are a helpful AI."],
      ["user", "{input}"]
  ])

  // The tag "model-tag" and metadata {"model-key": "model-value"} will be attached to the ChatOpenAI run only
  const model = new ChatOpenAI().withConfig({ tags: ["model-tag"], metadata: { "model-key": "model-value" } });
  const outputParser = new StringOutputParser();

  // Tags and metadata can be configured with RunnableConfig
  const chain = (prompt.pipe(model).pipe(outputParser)).withConfig({"tags": ["config-tag"], "metadata": {"config-key": "top-level-value"}});

  // Tags and metadata can also be passed at runtime
  await chain.invoke({input: "What is the meaning of life?"}, {tags: ["invoke-tag"], metadata: {"invoke-key": "invoke-value"}})
  ```
</CodeGroup>

## Customize run name

You can customize the name of a given run when invoking or streaming your LangChain code by providing it in the [Config](https://reference.langchain.com/python/langchain_core/runnables/?h=runnablecon#langchain_core.runnables.RunnableConfig). This name is used to identify the run in LangSmith and can be used to filter and group runs. The name is also used as the title of the run in the LangSmith UI. This can be done by setting a `run_name` in the [`RunnableConfig`](https://reference.langchain.com/python/langchain-core/runnables/config/RunnableConfig) object at construction or by passing a `run_name` in the invocation parameters in JS/TS.

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  # When tracing within LangChain, run names default to the class name of the traced object (e.g., 'ChatOpenAI').
  configured_chain = chain.with_config({"run_name": "MyCustomChain"})
  configured_chain.invoke({"input": "What is the meaning of life?"})

  # You can also configure the run name at invocation time, like below
  chain.invoke({"input": "What is the meaning of life?"}, {"run_name": "MyCustomChain"})
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  // When tracing within LangChain, run names default to the class name of the traced object (e.g., 'ChatOpenAI').
  const configuredChain = chain.withConfig({ runName: "MyCustomChain" });
  await configuredChain.invoke({ input: "What is the meaning of life?" });

  // You can also configure the run name at invocation time, like below
  await chain.invoke({ input: "What is the meaning of life?" }, {runName: "MyCustomChain"})
  ```
</CodeGroup>

<Note>
  The `run_name` parameter only changes the name of the runnable you invoke (e.g., a chain, function). It does not rename the nested run automatically created when you invoke an LLM object like [`ChatOpenAI`](https://reference.langchain.com/python/langchain-openai/chat_models/base/ChatOpenAI) (`gpt-5.4-mini`). In the example, the enclosing run will appear in LangSmith as `MyCustomChain`, while the nested LLM run still shows the model’s default name.

  To give the LLM run a more meaningful name, you can either:

  * Wrap the model in another runnable and assign a `run_name` to that step.
  * Use a tracing decorator or helper (e.g., `@traceable` in Python, or `traceable` from `langsmith` in JS/TS) to create a custom run around the model call.
</Note>

## Override model name in traces

When tracing LangChain model calls, LangSmith automatically captures the model identifier used in the API call. However, you may want to display a different, more descriptive name in traces for organizational purposes or to distinguish between different model configurations. You can do this by passing the `ls_model_name` [metadata parameter](/langsmith/ls-metadata-parameters#ls_model_name) when constructing or configuring your LangChain model.

This is particularly useful when:

* Working with self-hosted or local models where the model ID might not be descriptive.
* Using the same model with different configurations and wanting to distinguish them in traces.
* Creating aliases for models to make traces more readable for your team.
* Standardizing model names across different deployment environments.

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langchain_openai import ChatOpenAI
  from langchain_ollama import ChatOllama

  # Override model name for a local model
  llm = ChatOllama(
      model="llama2:13b-chat",  # Actual model ID
      metadata={"ls_model_name": "llama2-13b-production"}  # Name shown in LangSmith
  )

  # Or with OpenAI to distinguish configurations
  llm_creative = ChatOpenAI(
      model="gpt-5.5",
      temperature=0.9,
      metadata={"ls_model_name": "gpt-5.4-creative"}
  )

  llm_factual = ChatOpenAI(
      model="gpt-5.5",
      temperature=0.1,
      metadata={"ls_model_name": "gpt-5.4-factual"}
  )

  # The metadata is inherited when the model is used in a chain
  result = llm.invoke("What is the meaning of life?")
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { ChatOpenAI } from "@langchain/openai";
  import { ChatOllama } from "@langchain/ollama";

  // Override model name for a local model
  const llm = new ChatOllama({
    model: "llama2:13b-chat",  // Actual model ID
    metadata: { ls_model_name: "llama2-13b-production" }  // Name shown in LangSmith
  });

  // Or with OpenAI to distinguish configurations
  const llmCreative = new ChatOpenAI({
    modelName: "gpt-5.5",
    temperature: 0.9,
    metadata: { ls_model_name: "gpt-5.4-creative" }
  });

  const llmFactual = new ChatOpenAI({
    modelName: "gpt-5.5",
    temperature: 0.1,
    metadata: { ls_model_name: "gpt-5.4-factual" }
  });

  // The metadata is inherited when the model is used in a chain
  const result = await llm.invoke("What is the meaning of life?");
  ```
</CodeGroup>

When you pass `ls_model_name` in the model's metadata, this name will appear in the LangSmith UI for all traces involving that model instance. This works for any LangChain chat model or LLM and is inherited by all runs that use the model, including when it's part of a chain.

<Note>
  The `ls_model_name` metadata parameter is also used for [cost tracking](/langsmith/cost-tracking). When combined with the `ls_provider` parameter, LangSmith can automatically calculate costs for custom or self-hosted models. For more information about all available metadata parameters, see the [metadata parameters reference](/langsmith/ls-metadata-parameters).
</Note>

## Customize run ID

You can customize the ID of a given run when invoking or streaming your LangChain code by providing it in the [Config](https://reference.langchain.com/python/langchain_core/runnables/?h=runnablecon#langchain_core.runnables.RunnableConfig). This ID is used to uniquely identify the run in LangSmith and can be used to query specific runs. The ID can be useful for linking runs across different systems or for implementing custom tracking logic. This can be done by setting a `run_id` in the [`RunnableConfig`](https://reference.langchain.com/python/langchain-core/runnables/config/RunnableConfig) object at construction or by passing a `run_id` in the invocation parameters.

<Note>
  This feature is not currently supported directly for LLM objects.
</Note>

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import uuid

  my_uuid = uuid.uuid4()

  # You can configure the run ID at invocation time:
  chain.invoke({"input": "What is the meaning of life?"}, {"run_id": my_uuid})
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  const myUuid = crypto.randomUUID();

  // You can configure the run ID at invocation time, like below
  await chain.invoke({ input: "What is the meaning of life?" }, { runId: myUuid });
  ```
</CodeGroup>

Note that if you do this at the **root** of a trace (i.e., the top-level run, that run ID will be used as the `trace_id`).

## Access run (span) ID for LangChain invocations

When you invoke a LangChain object, you can manually specify the run ID of the invocation. This run ID can be used to query the run in LangSmith.

In JS/TS, you can use a `RunCollectorCallbackHandler` instance to access the run ID.

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import uuid

  from langchain_openai import ChatOpenAI
  from langchain_core.prompts import ChatPromptTemplate
  from langchain_core.output_parsers import StrOutputParser

  prompt = ChatPromptTemplate.from_messages([
      ("system", "You are a helpful assistant. Please respond to the user's request only based on the given context."),
      ("user", "Question: {question}\n\nContext: {context}")
  ])
  model = ChatOpenAI(model="gpt-5.4-mini")
  output_parser = StrOutputParser()

  chain = prompt | model | output_parser

  question = "Can you summarize this morning's meetings?"
  context = "During this morning's meeting, we solved all world conflict."
  my_uuid = uuid.uuid4()
  result = chain.invoke({"question": question, "context": context}, {"run_id": my_uuid})
  print(my_uuid)
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { ChatOpenAI } from "@langchain/openai";
  import { ChatPromptTemplate } from "@langchain/core/prompts";
  import { StringOutputParser } from "@langchain/core/output_parsers";
  import { RunCollectorCallbackHandler } from "@langchain/core/tracers/run_collector";

  const prompt = ChatPromptTemplate.fromMessages([
    ["system", "You are a helpful assistant. Please respond to the user's request only based on the given context."],
    ["user", "Question: {question}\n\nContext: {context}"],
  ]);
  const model = new ChatOpenAI({ modelName: "gpt-5.4-mini" });
  const outputParser = new StringOutputParser();

  const chain = prompt.pipe(model).pipe(outputParser);
  const runCollector = new RunCollectorCallbackHandler();

  const question = "Can you summarize this morning's meetings?"
  const context = "During this morning's meeting, we solved all world conflict."
  await chain.invoke(
      { question: question, context: context },
      { callbacks: [runCollector] }
  );
  const runId = runCollector.tracedRuns[0].id;
  console.log(runId);
  ```
</CodeGroup>

## Ensure all traces are submitted before exiting

In LangChain Python, LangSmith's tracing is done in a background thread to avoid obstructing your production application. This means that your process may end before all traces are successfully posted to LangSmith. This is especially prevalent in a serverless environment, where your VM may be terminated immediately once your chain or agent completes.

You can make callbacks synchronous by setting the `LANGCHAIN_CALLBACKS_BACKGROUND` environment variable to `"false"`.

For both languages, LangChain exposes methods to wait for traces to be submitted before exiting your application. Below is an example:

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langchain_openai import ChatOpenAI
  from langchain_core.tracers.langchain import wait_for_all_tracers

  llm = ChatOpenAI()

  try:
    llm.invoke("Hello, World!")
  finally:
    wait_for_all_tracers()
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { awaitAllCallbacks } from "@langchain/core/callbacks/promises";

  try {
      const llm = new ChatOpenAI();
      const response = await llm.invoke("Hello, World!");
  } catch (e) {
      // handle error
  } finally {
      await awaitAllCallbacks();
  }
  ```
</CodeGroup>

## Trace without setting environment variables

As mentioned in other guides, the following environment variables allow you to configure tracing enabled, the api endpoint, the api key, and the tracing project:

* `LANGSMITH_TRACING`
* `LANGSMITH_API_KEY`
* `LANGSMITH_ENDPOINT`
* `LANGSMITH_PROJECT`

However, in some environments, it is not possible to set environment variables. In these cases, you can set the tracing configuration programmatically.

This largely builds off of the [previous section](#trace-selectively).

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import langsmith as ls

  # You can create a client instance with an api key and api url
  client = ls.Client(
      api_key="YOUR_API_KEY",  # This can be retrieved from a secrets manager
      api_url="https://api.smith.langchain.com",  # Self-hosted, GCP EU (`eu.api...`), GCP APAC (`apac.api...`), or AWS US (`aws.api...`) as needed
  )

  # You can pass the client and project_name to the tracing_context
  with ls.tracing_context(client=client, project_name="test-no-env", enabled=True):
      chain.invoke({"question": "Am I using a callback?", "context": "I'm using a callback"})
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { LangChainTracer } from "@langchain/core/tracers/tracer_langchain";
  import { Client } from "langsmith";

  // You can create a client instance with an api key and api url
  const client = new Client(
      {
          apiKey: "YOUR_API_KEY",
          apiUrl: "https://api.smith.langchain.com", // Self-hosted, GCP EU (`eu.api...`), GCP APAC (`apac.api...`), or AWS US (`aws.api...`) as needed
      }
  );

  // You can pass the client and project_name to the LangChainTracer instance
  const tracer = new LangChainTracer({client, projectName: "test-no-env"});
  await chain.invoke(
    {
      question: "Am I using a callback?",
      context: "I'm using a callback",
    },
    { callbacks: [tracer] }
  );
  ```
</CodeGroup>

## Distributed tracing with LangChain (Python)

LangSmith supports distributed tracing with LangChain Python. This allows you to link runs (spans) across different services and applications. The principles are similar to the [distributed tracing guide](/langsmith/distributed-tracing) for the LangSmith SDK.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import langsmith
from langchain_core.runnables import chain
from langsmith.run_helpers import get_current_run_tree

# -- This code should be in a separate file or service --
@chain
def child_chain(inputs):
    return inputs["test"] + 1

def child_wrapper(x, headers):
    with langsmith.tracing_context(parent=headers):
        child_chain.invoke({"test": x})

# -- This code should be in a separate file or service --
@chain
def parent_chain(inputs):
    rt = get_current_run_tree()
    headers = rt.to_headers()
    # ... make a request to another service with the headers
    # The headers should be passed to the other service, eventually to the child_wrapper function

parent_chain.invoke({"test": 1})
```

## Interoperability between LangChain (Python) and LangSmith SDK

If you are using LangChain for part of your application and the LangSmith SDK (see [Custom instrumentation](/langsmith/annotate-code)) for other parts, you can still trace the entire application seamlessly.

LangChain objects will be traced when invoked within a `traceable` function and be bound as a child run of the `traceable` function.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langsmith import traceable

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Please respond to the user's request only based on the given context."),
    ("user", "Question: {question}\nContext: {context}")
])

model = ChatOpenAI(model="gpt-5.4-mini")
output_parser = StrOutputParser()
chain = prompt | model | output_parser
