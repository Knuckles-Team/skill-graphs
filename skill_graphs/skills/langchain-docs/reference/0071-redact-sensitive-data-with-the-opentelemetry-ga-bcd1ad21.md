# Redact sensitive data with the OpenTelemetry Gateway architecture
Source: https://docs.langchain.com/langsmith/otel-gateway-trace-redaction

Use an OpenTelemetry collector to redact sensitive data from traces before they land in LangSmith.

[LangChain](/langsmith/trace-with-langchain) and [LangGraph](/langsmith/trace-with-langgraph) applications support [OpenTelemetry-based tracing](/langsmith/trace-with-opentelemetry). Instead of sending traces directly to LangSmith, you can route them through an OpenTelemetry collector you control, apply redaction rules to strip sensitive fields, and forward the sanitized traces to LangSmith.

Traces flow from your application to the collector over OTLP/HTTP. The collector runs a transform processor that redacts sensitive span attributes, such as prompt inputs and model completions, before forwarding the sanitized spans to the LangSmith API.

```mermaid theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
flowchart TD
    A["Application<br/>(LangChain / LangGraph)"]

    subgraph collector[":4318"]
        B["Receiver<br/>OTLP/HTTP"]
        C["Transform Processor<br/>PII Redaction<br/>(email, phone, SSN, CC)"]
        D["OTLP/HTTP Exporter"]
        B --> C --> D
    end

    E["LangSmith API<br/>api.smith.langchain.com"]

    A -->|"OTLP/HTTP"| B
    D -->|"OTLP/HTTP"| E
```

## Prerequisites

Both of the following approaches require the following environment variables. Set `OTEL_EXPORTER_OTLP_ENDPOINT` to the address of your collector:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
LANGSMITH_OTEL_ENABLED="true"
LANGSMITH_TRACING="true"
LANGSMITH_OTEL_ONLY="true"
LANGSMITH_PROJECT="my-project"
OTEL_EXPORTER_OTLP_ENDPOINT="http://<my-otel-collector-endpoint>:4318"
```

For more on `LANGSMITH_PROJECT`, refer to [Log traces to a specific project](/langsmith/log-traces-to-project).

## Configure the collector

Both approaches also require an OpenTelemetry collector running as an intermediary between your application and LangSmith. The following configuration sets up an OTLP receiver on port `4318`, a transform processor that redacts the `gen_ai.prompt` and `gen_ai.completion` span attributes, and an exporter that forwards the sanitized traces to the LangSmith API:

```yaml theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
receivers:
  otlp:
    protocols:
      http:
        endpoint: 0.0.0.0:4318

processors:
  transform/redact:
    error_mode: ignore
    trace_statements:
      - context: span
        statements:
          - replace_pattern(attributes["gen_ai.completion"], "[\\s\\S]*", "[REDACTED]")
          - replace_pattern(attributes["gen_ai.prompt"], "[\\s\\S]*", "[REDACTED]")

exporters:
  otlphttp/langsmith:
    traces_endpoint: "https://api.smith.langchain.com/otel/v1/traces"
    headers:
      x-api-key: "${env:LANGSMITH_API_KEY}"
      Langsmith-Project: "${env:LANGSMITH_PROJECT}"

service:
  pipelines:
    traces:
      receivers: [otlp]
      processors: [transform/redact]
      exporters: [otlphttp/langsmith]
```

## Trace with LangChain or LangGraph

Use this approach if your application already uses [LangChain](/langsmith/trace-with-langchain) or [LangGraph](/langsmith/trace-with-langgraph). The tracing integration handles span creation automatically based on your environment variables, so no additional instrumentation code is required:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_openai import ChatOpenAI

@tool
def tell_joke(topic: str) -> str:
   llm = ChatOpenAI()
   response = llm.invoke(f"Tell me a short, funny joke about {topic}.")
   return response.content

agent = create_agent(
   model=ChatOpenAI(),
   tools=[tell_joke],
   system_prompt="When the user asks for jokes, use the tell_joke tool for each topic.",
)

topics = ["programming", "python", "kubernetes", "machine learning"]

result = agent.invoke(
   {"messages": [{"role": "user", "content": f"Tell me jokes about these topics: {', '.join(topics)}"}]}
)

print(result["messages"][-1].content)
```

## Trace with the OpenTelemetry SDK directly

Use this approach if you need programmatic control over the tracer provider and exporter. For example, to set per-request project names or configure custom headers at runtime. You configure the provider explicitly in code rather than relying on environment variables alone:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import os

from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor

project_name = os.environ["LANGSMITH_PROJECT"]
otlp_endpoint = os.environ["OTEL_EXPORTER_OTLP_ENDPOINT"]

provider = TracerProvider()
provider.add_span_processor(
   BatchSpanProcessor(
       OTLPSpanExporter(
           endpoint=otlp_endpoint+"/v1/traces",
           headers={"Langsmith-Project": project_name},
       )
   )
)
trace.set_tracer_provider(provider)

chain = ChatPromptTemplate.from_template("Tell me a joke about {topic}") | ChatOpenAI()

for topic in ["programming", "python", "databases", "kubernetes", "machine learning"]:
   print(f"Asking about {topic}...")
   result = chain.invoke({"topic": topic})
   print(f"  {result.content[:100]}\n")

provider.force_flush()
provider.shutdown()
```

<Note>
  If you prefer to redact sensitive data without routing through a collector, see [Prevent logging of sensitive data in traces](/langsmith/mask-inputs-outputs).
</Note>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/otel-gateway-trace-redaction.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Set up LangSmith
Source: https://docs.langchain.com/langsmith/platform-setup

This section covers how to host and manage LangSmith infrastructure for [observability](/langsmith/observability), [evaluation](/langsmith/evaluation), and [prompt engineering](/langsmith/prompt-engineering).

## Choose how to set up LangSmith

You can deploy LangSmith in one of two modes:

* [**Cloud**](/langsmith/cloud): fully managed by LangChain
* [**Self-hosted**](/langsmith/self-hosted): you manage the full stack within your infrastructure

<Callout>
  The self-hosted deployment option is available on the Enterprise plan. [Get a demo](https://www.langchain.com/contact-sales) to learn more.
</Callout>

<Columns>
  <Card title="Cloud" icon="cloud" href="/langsmith/cloud">
    Fully managed observability, evaluation, and prompt engineering.
  </Card>

  <Card title="Self-hosted" icon="server" href="/langsmith/self-hosted">
    **(Enterprise)** Full control with observability, evaluation, and prompt engineering in your infrastructure.
  </Card>
</Columns>

### Comparison

Refer to the following table for a comparison:

| Feature                                          | **Cloud**                           | **Self-Hosted**                           |
| ------------------------------------------------ | ----------------------------------- | ----------------------------------------- |
| **Infrastructure location**                      | LangChain's cloud                   | Your infrastructure                       |
| **Who manages updates**                          | LangChain                           | You                                       |
| **Can deploy agents?**                           | ✅ Yes                               | ✅ Yes (with LangSmith Deployment enabled) |
| **Observability data location**                  | LangChain cloud                     | Your infrastructure                       |
| **[Pricing](https://www.langchain.com/pricing)** | Plus tier                           | Enterprise                                |
| **Best for**                                     | Quick setup, managed infrastructure | Full control, data isolation              |

### Related

* [Plans and Pricing](https://www.langchain.com/pricing)
* [Observability](/langsmith/observability)

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/platform-setup.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Model providers
Source: https://docs.langchain.com/langsmith/playground-model-providers

The [Playground](/langsmith/prompt-engineering-concepts#playground) supports a wide range of model providers. You can select a provider, configure your preferred settings, and save these configurations to reuse across multiple prompts.

Use this page for a list of the available providers and their configuration options:

<div>
  <a href="#amazon-bedrock">
    <img alt="" />

    <img alt="" />

    <span>Amazon Bedrock</span>
  </a>

  <a href="#anthropic">
    <img alt="" />

    <img alt="" />

    <span>Anthropic</span>
  </a>

  <a href="#azure-openai">
    <img alt="" />

    <img alt="" />

    <span>Azure OpenAI</span>
  </a>

  <a href="#deepseek">
    <img alt="" />

    <img alt="" />

    <span>DeepSeek</span>
  </a>

  <a href="#fireworks">
    <img alt="" />

    <img alt="" />

    <span>Fireworks</span>
  </a>

  <a href="#google-gemini">
    <img alt="" />

    <img alt="" />

    <span>Google Gemini</span>
  </a>

  <a href="#google-vertex-ai">
    <img alt="" />

    <img alt="" />

    <span>Google Vertex AI</span>
  </a>

  <a href="#groq">
    <img alt="" />

    <img alt="" />

    <span>Groq</span>
  </a>

  <a href="#mistral-ai">
    <img alt="" />

    <img alt="" />

    <span>Mistral AI</span>
  </a>

  <a href="#openai">
    <img alt="" />

    <img alt="" />

    <span>OpenAI</span>
  </a>

  <a href="#openai-compatible-endpoint">
    <Icon icon="link" />

    <span>OpenAI compatible endpoint</span>
  </a>

  <a href="#xai">
    <img alt="" />

    <img alt="" />

    <span>XAI</span>
  </a>
</div>

For details on creating and managing model configurations, refer to the [Configure prompt settings](/langsmith/managing-model-configurations) page.

## Amazon Bedrock

Before you use this model, ensure you have [AWS credentials or IAM role](https://docs.aws.amazon.com/bedrock/latest/userguide/security-iam.html).

### Authentication

Amazon Bedrock supports two authentication methods. **IAM trusted entity is the recommended approach** because it avoids sharing long-lived AWS access keys with LangSmith.

#### IAM trusted entity (recommended)

<Note>
  **Not applicable for [self-hosted LangSmith](/langsmith/self-hosted).** Use Access Keys (or the Bedrock API Key) instead.
</Note>

With IAM trusted entity authentication, you create an IAM role in your AWS account and allow LangSmith to assume it. No access keys are stored in LangSmith. Instead, LangSmith uses [AWS STS](https://docs.aws.amazon.com/STS/latest/APIReference/welcome.html) to assume the role on each request.

To set this up:

1. Create an IAM role in your AWS account with permissions to invoke Bedrock models (e.g., `bedrock:InvokeModel`).
2. Add a trust policy that allows LangSmith's AWS account (`808407022534`) to assume the role, using your LangSmith workspace ID as the external ID:

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::808407022534:root"
      },
      "Action": "sts:AssumeRole",
      "Condition": {
        "StringEquals": {
          "sts:ExternalId": "<your-langsmith-workspace-id>"
        }
      }
    }
  ]
}
```

<Tip>
  You can find your workspace ID in your [LangSmith workspace settings](https://smith.langchain.com/settings).
</Tip>

3. In the LangSmith Playground, expand the **IAM Trusted Entity** section under the Bedrock provider and enter the ARN of the role you created.

For more details on trust policies, see the [AWS documentation](https://aws.amazon.com/blogs/security/how-to-use-trust-policies-with-iam-roles/).

#### Access keys

Alternatively, you can authenticate with AWS access keys (`AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`). Enter these in the Bedrock provider configuration in the Playground. This method is simpler to set up but less secure because it requires storing long-lived credentials.

### Available models

AWS Bedrock provides access to foundation models from multiple providers:

* **Anthropic:** Claude models.
* **Amazon:** Titan models.
* **Cohere:** Command models.
* **Meta:** Llama models.
* **Others:** Additional providers available based on region.

For the current list of available models, refer to the [AWS Bedrock documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/models-supported.html).

### Configuration parameters

Parameters depend on the underlying model provider:

#### For Anthropic models

Uses Anthropic configuration (see [Anthropic](#anthropic) section below).

#### For Amazon Titan

| Parameter       | Range     | Description             |
| --------------- | --------- | ----------------------- |
| **Temperature** | 0.0 - 1.0 | Response randomness     |
| **Max Tokens**  | 1+        | Maximum response length |
| **Top P**       | 0.0 - 1.0 | Nucleus sampling        |

#### AWS-specific settings

* **Region:** AWS region for model deployment.

### Tool calling

Depends on underlying model:

* **Anthropic models:** `auto`, `any`.
* **Cohere models:** `auto`.

## Anthropic

Before you use this model, ensure you have an [Anthropic API key](https://console.anthropic.com/settings/keys).

### Available models

Anthropic offers three tiers of models across their Claude generations:

* **Opus:** Highest intelligence and capability.
* **Sonnet:** Balanced performance and cost.
* **Haiku:** Fast and cost-effective.

Recent Claude models support extended thinking capabilities for showing reasoning processes.

For the current list of available models, refer to the [Anthropic documentation](https://docs.anthropic.com/claude/docs/models-overview).

### Configuration parameters

| Parameter             | Range     | Default  | Description                                        |
| --------------------- | --------- | -------- | -------------------------------------------------- |
| **Temperature**       | 0.0 - 1.0 | Optional | Randomness control (uncheck to use model default)  |
| **Max Output Tokens** | 1+        | 1024     | Maximum response length                            |
| **Top P**             | 0.0 - 1.0 | Optional | Nucleus sampling (uncheck for model default)       |
| **Top K**             | 1+        | Optional | Limits to top K tokens (uncheck for model default) |

<Note>
  Temperature, Top P, and Top K are optional. When unchecked, Claude uses its internal defaults.
</Note>

#### Extended Thinking

Available on supported Claude models. Enable the model to show reasoning before responding, similar to OpenAI's o-series.

| Parameter                    | Range  | Description                             |
| ---------------------------- | ------ | --------------------------------------- |
| **Enable Extended Thinking** | Toggle | Show/hide thinking process              |
| **Budget Tokens**            | 1+     | Max tokens for thinking (default: 1024) |

When enabled, responses include:

1. A "thinking" section with the model's reasoning.
2. The final response.

#### Advanced options

* **Base URL:** Override API endpoint for custom deployments.

### Tool calling

* **Supported Tool Choices:** `auto`, `any` (requires at least one tool).
* **Parallel Execution:** No (sequential only).

## Azure OpenAI

Before you use this model, ensure you have [Azure OpenAI credentials](https://learn.microsoft.com/en-us/azure/ai-services/openai/quickstart) (endpoint + API key).

### Available models

Azure OpenAI provides the same model families as OpenAI:

* **GPT series:** General-purpose chat models.
* **o-series:** Reasoning-focused models.
* **Legacy models:** GPT-3.5 and GPT-4 variants.

Model availability varies by Azure region and requires deployment before use.

For the current list of available models, refer to the [Azure OpenAI documentation](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/models).

### Configuration parameters

Azure OpenAI supports the same parameters as OpenAI:

#### Standard parameters

| Parameter             | Range      | Description                                                        |
| --------------------- | ---------- | ------------------------------------------------------------------ |
| **Temperature**       | 0.0 - 2.0  | Controls randomness. Lower = more focused, higher = more creative. |
| **Max Output Tokens** | 1+         | Maximum length of the response                                     |
| **Top P**             | 0.0 - 1.0  | Nucleus sampling threshold. Alternative to temperature.            |
| **Presence Penalty**  | -2.0 - 2.0 | Penalize new topics (positive) or encourage them (negative)        |
| **Frequency Penalty** | -2.0 - 2.0 | Penalize repetition (positive) or allow it (negative)              |
| **Seed**              | Integer    | For reproducible outputs                                           |

#### Advanced parameters

**Reasoning Effort:** Available on reasoning-optimized models (o-series and newer GPT models).

**Service Tier:** Available on newer models.

**Other parameters:**

* **JSON Mode:** Force valid JSON responses.
* **Parallel Tool Calls:** Execute multiple tools concurrently.

#### Azure-specific features

* **Deployment Management:** Models must be deployed before use.
* **Regional Availability:** Choose Azure regions for data residency.
* **Content Filtering:** Built-in content moderation and safety features.
* **Managed Identity:** Azure AD authentication support.
* **Private Endpoints:** VNet integration for secure access.

### Tool calling

* **Supported Tool Choices:** `auto`, `required`, `none`, or specific tool name.
* **Parallel Execution:** Yes.

## DeepSeek

Before you use this model, ensure you have a [DeepSeek API key](https://platform.deepseek.com/api_keys).

### Available models

DeepSeek offers general-purpose models, reasoning-optimized models (R-series), and coding-specialized models.

For the current list of available models, refer to [DeepSeek's documentation](https://platform.deepseek.com/api-docs/).

### Configuration parameters

| Parameter             | Range      | Description             |
| --------------------- | ---------- | ----------------------- |
| **Temperature**       | 0.0 - 2.0  | Response randomness     |
| **Max Tokens**        | 1+         | Maximum response length |
| **Top P**             | 0.0 - 1.0  | Nucleus sampling        |
| **Presence Penalty**  | -2.0 - 2.0 |                         |
| **Frequency Penalty** | -2.0 - 2.0 |                         |

## Fireworks

Before you use this model, ensure you have a [Fireworks API key](https://fireworks.ai/api-keys).

### Available models

Fireworks provides high-speed inference for popular open-source models and fine-tuned variants, including:

* **Llama:** Meta's Llama models in various sizes.
* **Mixtral:** Mistral's mixture-of-experts models.
* **Qwen:** Alibaba's multilingual models.
* **DeepSeek:** DeepSeek models.
* **Other open models:** Gemma, Phi, and more.

For the current list of available models, refer to [Fireworks' model documentation](https://docs.fireworks.ai/models).

### Configuration parameters

| Parameter       | Range     | Description             |
| --------------- | --------- | ----------------------- |
| **Temperature** | 0.0 - 2.0 | Response randomness     |
| **Max Tokens**  | 1+        | Maximum response length |
| **Top P**       | 0.0 - 1.0 | Nucleus sampling        |

### Tool calling

* **Supported Tool Choices:** `auto`, `required`, `none`.
* **Parallel Execution:** Yes.

## Google Gemini

Before you use this model, ensure you have a [Google AI API key](https://aistudio.google.com/app/apikey).

### Available models

Google offers Gemini models in multiple tiers (Ultra, Pro, Flash) optimized for different use cases.

For the current list of available models, refer to [Google's Gemini documentation](https://ai.google.dev/models/gemini).

### Configuration parameters

| Parameter             | Range     | Description             |
| --------------------- | --------- | ----------------------- |
| **Temperature**       | 0.0 - 2.0 | Response randomness     |
| **Max Output Tokens** | 1+        | Maximum response length |
| **Top P**             | 0.0 - 1.0 | Nucleus sampling        |
| **Top K**             | 1+        | Top-k sampling          |

### Tool calling

* **Supported Tool Choices:** `auto`, `any`, `none`.
* **Parallel Execution:** No.

## Google Vertex AI

Before you use this model, ensure you have [Google Cloud credentials](https://cloud.google.com/vertex-ai/docs/authentication).

### Available models

Google offers Gemini models in multiple tiers (Ultra, Pro, Flash) optimized for different use cases, plus other models available through Vertex AI.

For the current list of available models, refer to the [Vertex AI documentation](https://cloud.google.com/vertex-ai/docs/generative-ai/models).

### Configuration parameters

| Parameter             | Range     | Description             |
| --------------------- | --------- | ----------------------- |
| **Temperature**       | 0.0 - 2.0 | Response randomness     |
| **Max Output Tokens** | 1+        | Maximum response length |
| **Top P**             | 0.0 - 1.0 | Nucleus sampling        |
| **Top K**             | 1+        | Top-k sampling          |

#### Advanced options

* **Region Selection:** Deploy in specific Google Cloud regions.
* **Safety Settings:** Configure content filtering thresholds.

### Tool calling

* **Supported Tool Choices:** `auto`, `any`, `none`.
* **Parallel Execution:** No.

## Groq

Before you use this model, ensure you have a [Groq API key](https://console.groq.com/keys).

### Available models

Groq provides high-speed inference for popular open-source models including Llama, Mixtral, and Gemma variants.

For the current list of available models, refer to [Groq's model documentation](https://console.groq.com/docs/models).

### Configuration parameters

| Parameter       | Range     | Description             |
| --------------- | --------- | ----------------------- |
| **Temperature** | 0.0 - 2.0 | Response randomness     |
| **Max Tokens**  | 1+        | Maximum response length |

### Tool calling

* **Supported Tool Choices:** `auto`, `required`, `none`.
* **Parallel Execution:** Yes.

## Mistral AI

Before you use this model, ensure you have a [Mistral AI API key](https://console.mistral.ai/api-keys/).

### Available models

Mistral offers models in multiple tiers (Large, Medium, Small) optimized for different performance and cost requirements.

For the current list of available models, refer to [Mistral's documentation](https://docs.mistral.ai/platform/endpoints/).

### Configuration parameters

| Parameter       | Range     | Description             |
| --------------- | --------- | ----------------------- |
| **Temperature** | 0.0 - 1.0 | Response randomness     |
| **Max Tokens**  | 1+        | Maximum response length |
| **Top P**       | 0.0 - 1.0 | Nucleus sampling        |

### Tool calling

* **Supported Tool Choices:** `auto`, `any`, `none`.
* **Parallel Execution:** No.

## OpenAI

Before you use this model, ensure you have an [OpenAI API key](https://platform.openai.com/api-keys) or [Azure OpenAI credentials](https://learn.microsoft.com/en-us/azure/ai-services/openai/quickstart).

### Available models

OpenAI offers several model families with different capabilities and price points:

* **GPT series:** General-purpose chat models with various size/capability tiers.
* **o-series:** Reasoning-focused models optimized for complex problem-solving.
* **Legacy models:** Older GPT-3.5 and GPT-4 variants.

For the current list of available models, refer to the [OpenAI documentation](https://platform.openai.com/docs/models).

### Configuration parameters

Standard:

| Parameter             | Range      | Description                                                        |
| --------------------- | ---------- | ------------------------------------------------------------------ |
| **Temperature**       | 0.0 - 2.0  | Controls randomness. Lower = more focused, higher = more creative. |
| **Max Output Tokens** | 1+         | Maximum length of the response                                     |
| **Top P**             | 0.0 - 1.0  | Nucleus sampling threshold. Alternative to temperature.            |
| **Presence Penalty**  | -2.0 - 2.0 | Penalize new topics (positive) or encourage them (negative)        |
| **Frequency Penalty** | -2.0 - 2.0 | Penalize repetition (positive) or allow it (negative)              |
| **Seed**              | Integer    | For reproducible outputs                                           |

Advanced:

**Reasoning Effort**: Available on reasoning-optimized models (o-series and newer GPT models).

Controls reasoning depth before responding. Higher effort = better quality for complex tasks, longer latency.

| Value     | Description                                  |
| --------- | -------------------------------------------- |
| `none`    | Disables reasoning (standard chat behavior)  |
| `minimal` | Minimal reasoning                            |
| `low`     | Light reasoning                              |
| `medium`  | Moderate reasoning (default)                 |
| `high`    | Deep reasoning                               |
| `xhigh`   | Extra deep reasoning (if supported by model) |

<Note>
  When reasoning\_effort is active (not `none`), temperature, top\_p, and penalties are automatically disabled.
</Note>

**Service Tier**: Available on newer models.

Controls request priority and processing allocation.

| Value      | Description                                          |
| ---------- | ---------------------------------------------------- |
| `auto`     | System decides based on load (default)               |
| `default`  | Standard processing queue                            |
| `flex`     | Lower cost, variable latency (if supported by model) |
| `priority` | High-priority queue, lower latency, higher cost      |

**Other parameters:**

* **JSON Mode:** Force valid JSON responses.
* **Responses API:** Improved streaming (default: enabled).
* **Parallel Tool Calls:** Execute multiple tools concurrently.

### Tool calling

* **Supported Tool Choices:** `auto`, `required`, `none`, or specific tool name
* **Parallel Execution:** Yes

## OpenAI Compatible Endpoint

Authentication varies by endpoint (often API key or none).

### Configuration

**Required:**

* **Base URL:** Your endpoint URL (e.g., `https://your-endpoint.com/v1`).
* **Model Name:** Your model identifier.

Works with any framework or service that implements the OpenAI-compatible API format, including:

* Self-hosted open-source inference servers
* Model routing proxies
* Custom model endpoints

### Configuration parameters

All OpenAI-compatible parameters:

| Parameter             | Range      | Description             |
| --------------------- | ---------- | ----------------------- |
| **Temperature**       | 0.0 - 2.0  | Response randomness     |
| **Max Tokens**        | 1+         | Maximum response length |
| **Top P**             | 0.0 - 1.0  | Nucleus sampling        |
| **Frequency Penalty** | -2.0 - 2.0 | Reduce repetition       |
| **Presence Penalty**  | -2.0 - 2.0 | Encourage new topics    |

**Advanced:**

* **JSON Mode:** If endpoint supports it.
* **Streaming:** If endpoint supports it.
* **Function Calling:** If endpoint implements OpenAI format.

### Tool calling

* **Supported Tool Choices:** `auto`, `required`, `none` (if endpoint supports).
* **Parallel Execution:** Yes (if endpoint supports).

### Example endpoints

**Local Ollama:**

```
Base URL: http://localhost:11434/v1
Model: llama3.1
```

**vLLM Server:**

```
Base URL: https://your-server.com/v1
Model: mistral-7b-instruct
```

**LiteLLM Proxy:**

```
Base URL: https://litellm.example.com
Model: gpt-4 (routes to configured backend)
```

## XAI

Before you use this model, ensure you have an [xAI API key](https://console.x.ai/).

### Available models

xAI offers Grok models in multiple sizes for different use cases.

For the current list of available models, refer to [xAI's documentation](https://docs.x.ai/docs).

### Configuration parameters

Standard OpenAI-compatible parameters:

| Parameter             | Range     | Description                |
| --------------------- | --------- | -------------------------- |
| **Temperature**       | 0.0 - 2.0 | Response randomness        |
| **Max Tokens**        | 1+        | Maximum response length    |
| **Top P**             | 0.0 - 1.0 | Nucleus sampling           |
| **Presence Penalty**  | 0 - 2.0   | Hidden on reasoning models |
| **Frequency Penalty** | 0 - 2.0   | Hidden on reasoning models |

### Tool calling

* **Supported Tool Choices:** OpenAI-compatible.
* **Parallel Execution:** Yes (if supported).

## Common Configuration Across All Providers

### Extra Parameters

All providers support a **JSON editor for extra parameters** not exposed in the UI:

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "logprobs": true,
  "top_logprobs": 5,
  "custom_parameter": "value"
}
```

**Use cases:**

* Provider-specific beta features
* Advanced parameters not yet in UI
* Custom metadata for tracking

**Limitation:** Cannot override parameters already in the UI (e.g., can't set temperature here if it's set above)

### Rate Limiting

**Requests Per Second (RPS)** - Available for all providers when running over datasets:

* **Range:** 0 - 500 RPS
* **Purpose:** Respect API rate limits, control costs
* **Default:** Varies by provider

Set this when running experiments or evaluations to avoid hitting rate limits.

## Next steps

<CardGroup>
  <Card title="Configure prompt settings" icon="settings" href="/langsmith/managing-model-configurations">
    Learn how to create and manage model configurations in the Playground.
  </Card>

  <Card title="Create a prompt" icon="edit" href="/langsmith/create-a-prompt">
    Get started building prompts with your chosen model provider.
  </Card>
</CardGroup>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/playground-model-providers.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Collect feedback with presigned URLs
Source: https://docs.langchain.com/langsmith/presigned-feedback-tokens

Use presigned feedback tokens to collect user feedback from client-side applications without exposing your LangSmith API key.

Presigned feedback tokens let you collect [feedback](/langsmith/observability-concepts#feedback) from client-side applications (browsers, mobile apps, etc.) without exposing your [LangSmith API key](/langsmith/create-account-api-key). Each token generates a URL scoped to a specific [run](/langsmith/observability-concepts#runs) and feedback key. Clients submit feedback by calling that URL directly with no authentication required.

This is useful when:

* Your frontend collects thumbs up/down or star ratings from end users.
* You want to embed feedback links in emails, Slack messages, or other external channels.
* You need to decouple feedback collection from your backend.

<Note>
  If you are using [Agent Server](/langsmith/agent-server), presigned feedback URLs are generated automatically when you include `feedback_keys` in the run request. For that workflow, refer to [Collect user feedback for Agent Server runs](/langsmith/agent-server-feedback).
</Note>

## Create a presigned feedback token

Use [`create_presigned_feedback_token()`](https://reference.langchain.com/python/langsmith/client/Client/create_presigned_feedback_token) / [`createPresignedFeedbackToken`](https://reference.langchain.com/javascript/classes/langsmith.client.Client.html#createpresignedfeedbacktoken) to generate a token for a specific run and feedback key. The returned object includes a `url` that clients can call to submit feedback:

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langsmith import Client

  client = Client()

  run_id = "<run_id>"

  token = client.create_presigned_feedback_token(
      run_id,
      feedback_key="user_score",
  )

  print(token.url)
  # https://api.smith.langchain.com/api/v1/feedback/tokens/<token_id>
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { Client } from "langsmith";

  const client = new Client();

  const runId = "<run_id>";

  const token = await client.createPresignedFeedbackToken(runId, "user_score");

  console.log(token.url);
  // https://api.smith.langchain.com/api/v1/feedback/tokens/<token_id>
  ```
</CodeGroup>

### Set token expiration

Tokens expire after 3 hours by default. Pass `expiration` to customize this with either a `timedelta` (relative) or a `datetime` (absolute):

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import datetime
  from langsmith import Client

  client = Client()

  run_id = "<run_id>"

  token = client.create_presigned_feedback_token(
      run_id,
      feedback_key="user_score",
      expiration=datetime.timedelta(hours=24),
  )
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { Client } from "langsmith";

  const client = new Client();

  const runId = "<run_id>";

  const token = await client.createPresignedFeedbackToken(runId, "user_score", {
    expiration: { hours: 24 },
  });
  ```
</CodeGroup>

### Constrain feedback values

Pass `feedback_config` to restrict what values clients can submit. This is useful for enforcing a specific feedback schema (e.g., thumbs up/down, 1–5 stars, or categorical labels):

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langsmith import Client

  client = Client()

  run_id = "<run_id>"

  token = client.create_presigned_feedback_token(
      run_id,
      feedback_key="user_score",
      feedback_config={
          "type": "continuous",
          "min": 0,
          "max": 1,
      },
  )
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { Client } from "langsmith";

  const client = new Client();

  const runId = "<run_id>";

  const token = await client.createPresignedFeedbackToken(runId, "user_score", {
    feedbackConfig: {
      type: "continuous",
      min: 0,
      max: 1,
    },
  });
  ```
</CodeGroup>

### Create tokens in batch (Python only)

Use `create_presigned_feedback_tokens` (plural) to generate tokens for multiple feedback keys in a single call:

```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langsmith import Client

client = Client()

run_id = "<run_id>"

tokens = client.create_presigned_feedback_tokens(
    run_id,
    feedback_keys=["thumbs_up", "thumbs_down"],
)

for token in tokens:
    print(f"{token.id}: {token.url}")
```

## Submit feedback with a presigned URL

Once you have a presigned URL, your frontend code or email client submits feedback by sending a `POST` or `GET` request to it. The URL does not require an API key or authentication because the token provides the authorization.

### POST request

Use `POST` from your frontend when a user interacts with a feedback control (e.g., clicking a thumbs up button). `POST` supports `score`, `value`, `comment`, `correction`, and `metadata` fields.

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
curl --request POST \
  --url "https://api.smith.langchain.com/api/v1/feedback/tokens/<token_id>" \
  --header "Content-Type: application/json" \
  --data '{
    "score": 1,
    "comment": "This response was helpful!"
  }'
```

### GET request

Use `GET` when embedding a feedback link in an email or Slack message. The user's click triggers the request. `GET` supports `score`, `value`, `comment`, and `correction` as query parameters. `metadata` is not supported with `GET`.

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
curl --request GET \
  --url "https://api.smith.langchain.com/api/v1/feedback/tokens/<token_id>?score=1&comment=This%20response%20was%20helpful!"
```

### Submit feedback using the SDK

You can also submit feedback from a presigned token using the SDK, which is useful for server-side workflows where you received a token URL from another service.

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langsmith import Client

  client = Client()

  client.create_feedback_from_token(
      "<token_or_url>",
      score=1,
      comment="This response was helpful!",
  )
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  // Use a direct HTTP request to the presigned URL
  await fetch(tokenUrl, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      score: 1,
      comment: "This response was helpful!",
    }),
  });
  ```
</CodeGroup>

## List existing tokens

Retrieve all presigned feedback tokens for a run using `list_presigned_feedback_tokens` / `listPresignedFeedbackTokens`.

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langsmith import Client

  client = Client()

  run_id = "<run_id>"

  for token in client.list_presigned_feedback_tokens(run_id):
      print(f"ID: {token.id}, URL: {token.url}, Expires: {token.expires_at}")
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { Client } from "langsmith";

  const client = new Client();

  const runId = "<run_id>";

  for await (const token of client.listPresignedFeedbackTokens(runId)) {
    console.log(`URL: ${token.url}, Expires: ${token.expires_at}`);
  }
  ```
</CodeGroup>

## Related

* [Reference guide on feedback data format](/langsmith/feedback-data-format)
* [Log feedback using the SDK](/langsmith/attach-user-feedback)

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/presigned-feedback-tokens.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Pricing plans
Source: https://docs.langchain.com/langsmith/pricing-plans

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/pricing-plans.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
