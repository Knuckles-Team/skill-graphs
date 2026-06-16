# export LANGSMITH_API_KEY="your-api-key"
```

### Installation

The LangChain AzureChatOpenAI integration lives in the `@langchain/openai` package:

<CodeGroup>
  ```bash npm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  npm install @langchain/openai @langchain/core
  ```

  ```bash yarn theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  yarn add @langchain/openai @langchain/core
  ```

  ```bash pnpm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  pnpm add @langchain/openai @langchain/core
  ```
</CodeGroup>

## Instantiation

Now we can instantiate our model object and generate chat completions:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { AzureChatOpenAI } from "@langchain/openai"

const llm = new AzureChatOpenAI({
    model: "gpt-5.5",
    temperature: 0,
    maxTokens: undefined,
    maxRetries: 2,
    azureOpenAIApiKey: process.env.AZURE_OPENAI_API_KEY, // In Node.js defaults to process.env.AZURE_OPENAI_API_KEY
    azureOpenAIApiInstanceName: process.env.AZURE_OPENAI_API_INSTANCE_NAME, // In Node.js defaults to process.env.AZURE_OPENAI_API_INSTANCE_NAME
    azureOpenAIApiDeploymentName: process.env.AZURE_OPENAI_API_DEPLOYMENT_NAME, // In Node.js defaults to process.env.AZURE_OPENAI_API_DEPLOYMENT_NAME
    azureOpenAIApiVersion: process.env.AZURE_OPENAI_API_VERSION, // In Node.js defaults to process.env.AZURE_OPENAI_API_VERSION
})
```

## Invocation

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const aiMsg = await llm.invoke([
    [
        "system",
        "You are a helpful assistant that translates English to French. Translate the user sentence.",
    ],
    ["human", "I love programming."],
])
aiMsg
```

```text theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
AIMessage {
  "id": "chatcmpl-9qrWKByvVrzWMxSn8joRZAklHoB32",
  "content": "J'adore la programmation.",
  "additional_kwargs": {},
  "response_metadata": {
    "tokenUsage": {
      "completionTokens": 8,
      "promptTokens": 31,
      "totalTokens": 39
    },
    "finish_reason": "stop"
  },
  "tool_calls": [],
  "invalid_tool_calls": [],
  "usage_metadata": {
    "input_tokens": 31,
    "output_tokens": 8,
    "total_tokens": 39
  }
}
```

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
console.log(aiMsg.content)
```

```text theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
J'adore la programmation.
```

## Using Azure Managed identity

If you're using Azure Managed Identity, you can configure the credentials like this:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import {
  DefaultAzureCredential,
  getBearerTokenProvider,
} from "@azure/identity";
import { AzureChatOpenAI } from "@langchain/openai";

const credentials = new DefaultAzureCredential();
const azureADTokenProvider = getBearerTokenProvider(
  credentials,
  "https://cognitiveservices.azure.com/.default"
);

const llmWithManagedIdentity = new AzureChatOpenAI({
  azureADTokenProvider,
  azureOpenAIApiInstanceName: "<your_instance_name>",
  azureOpenAIApiDeploymentName: "<your_deployment_name>",
  azureOpenAIApiVersion: "<api_version>",
});
```

## Using a different domain

If your instance is hosted under a domain other than the default `openai.azure.com`, you'll need to use the alternate `AZURE_OPENAI_BASE_PATH` environment variable.
For example, here's how you would connect to the domain `https://westeurope.api.microsoft.com/openai/deployments/{DEPLOYMENT_NAME}`:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { AzureChatOpenAI } from "@langchain/openai";

const llmWithDifferentDomain = new AzureChatOpenAI({
  temperature: 0.9,
  azureOpenAIApiKey: "<your_key>", // In Node.js defaults to process.env.AZURE_OPENAI_API_KEY
  azureOpenAIApiDeploymentName: "<your_deployment_name>", // In Node.js defaults to process.env.AZURE_OPENAI_API_DEPLOYMENT_NAME
  azureOpenAIApiVersion: "<api_version>", // In Node.js defaults to process.env.AZURE_OPENAI_API_VERSION
  azureOpenAIBasePath:
    "https://westeurope.api.microsoft.com/openai/deployments", // In Node.js defaults to process.env.AZURE_OPENAI_BASE_PATH
});

```

## Custom headers

You can specify custom headers by passing in a `configuration` field:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { AzureChatOpenAI } from "@langchain/openai";

const llmWithCustomHeaders = new AzureChatOpenAI({
  azureOpenAIApiKey: process.env.AZURE_OPENAI_API_KEY, // In Node.js defaults to process.env.AZURE_OPENAI_API_KEY
  azureOpenAIApiInstanceName: process.env.AZURE_OPENAI_API_INSTANCE_NAME, // In Node.js defaults to process.env.AZURE_OPENAI_API_INSTANCE_NAME
  azureOpenAIApiDeploymentName: process.env.AZURE_OPENAI_API_DEPLOYMENT_NAME, // In Node.js defaults to process.env.AZURE_OPENAI_API_DEPLOYMENT_NAME
  azureOpenAIApiVersion: process.env.AZURE_OPENAI_API_VERSION, // In Node.js defaults to process.env.AZURE_OPENAI_API_VERSION
  configuration: {
    defaultHeaders: {
      "x-custom-header": `SOME_VALUE`,
    },
  },
});

await llmWithCustomHeaders.invoke("Hi there!");
```

The `configuration` field also accepts other `ClientOptions` parameters accepted by the official SDK.

**Note:** The specific header `api-key` currently cannot be overridden in this manner and will pass through the value from `azureOpenAIApiKey`.

## Migration from Azure OpenAI SDK

If you are using the deprecated Azure OpenAI SDK with the `@langchain/azure-openai` package, you can update your code to use the new Azure integration following these steps:

1. Install the new `@langchain/openai` package and remove the previous `@langchain/azure-openai` package:

<CodeGroup>
  ```bash npm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  npm install @langchain/openai
  ```

  ```bash yarn theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  yarn add @langchain/openai
  ```

  ```bash pnpm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  pnpm add @langchain/openai
  ```
</CodeGroup>

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
npm uninstall @langchain/azure-openai
```

2. Update your imports to use the new [`AzureChatOpenAI`](https://reference.langchain.com/javascript/langchain-openai/AzureChatOpenAI) class from the `@langchain/openai` package:

   ```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
   import { AzureChatOpenAI } from "@langchain/openai";
   ```

3. Update your code to use the new [`AzureChatOpenAI`](https://reference.langchain.com/javascript/langchain-openai/AzureChatOpenAI) class and pass the required parameters:

   ```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
   const model = new AzureChatOpenAI({
     azureOpenAIApiKey: "<your_key>",
     azureOpenAIApiInstanceName: "<your_instance_name>",
     azureOpenAIApiDeploymentName: "<your_deployment_name>",
     azureOpenAIApiVersion: "<api_version>",
   });
   ```

   Notice that the constructor now requires the `azureOpenAIApiInstanceName` parameter instead of the `azureOpenAIEndpoint` parameter, and adds the `azureOpenAIApiVersion` parameter to specify the API version.

   * If you were using Azure Managed Identity, you now need to use the `azureADTokenProvider` parameter to the constructor instead of `credentials`, see the [Azure Managed Identity](#using-azure-managed-identity) section for more details.

   * If you were using environment variables, you now have to set the `AZURE_OPENAI_API_INSTANCE_NAME` environment variable instead of `AZURE_OPENAI_API_ENDPOINT`, and add the `AZURE_OPENAI_API_VERSION` environment variable to specify the API version.

***

## API reference

For detailed documentation of all `AzureChatOpenAI` features and configurations head to the [API reference](https://reference.langchain.com/javascript/langchain-openai/AzureChatOpenAI).

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/javascript/integrations/chat/azure.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# ChatBedrockConverse integration
Source: https://docs.langchain.com/oss/javascript/integrations/chat/bedrock_converse

Integrate with the ChatBedrockConverse chat model using LangChain JavaScript.

[Amazon Bedrock Converse](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html) is a fully managed service that makes Foundation Models (FMs) from leading AI startups and Amazon available via an API. You can choose from a wide range of FMs to find the model that is best suited for your use case. It provides a unified conversational interface for Bedrock models.

This will help you getting started with `ChatBedrockConverse` [chat models](/oss/javascript/langchain/models). For detailed documentation of all `ChatBedrockConverse` features and configurations head to the [API reference](https://reference.langchain.com/javascript/langchain-aws/ChatBedrockConverse).

## Overview

### Integration details

| Class                                                                                                 | Package                                              | Serializable | [PY support](https://python.langchain.com/docs/integrations/chat/bedrock/#beta-bedrock-converse-api) |                                            Downloads                                           |                                           Version                                           |
| :---------------------------------------------------------------------------------------------------- | :--------------------------------------------------- | :----------: | :--------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------: |
| [`ChatBedrockConverse`](https://reference.langchain.com/javascript/langchain-aws/ChatBedrockConverse) | [`@langchain/aws`](https://npmjs.com/@langchain/aws) |       ✅      |                                                   ✅                                                  | ![NPM - Downloads](https://img.shields.io/npm/dm/@langchain/aws?style=flat-square\&label=%20&) | ![NPM - Version](https://img.shields.io/npm/v/@langchain/aws?style=flat-square\&label=%20&) |

### Model features

See the links in the table headers below for guides on how to use specific features.

| [Tool calling](/oss/javascript/langchain/tools) | [Structured output](/oss/javascript/langchain/structured-output) | [Image input](/oss/javascript/langchain/messages#multimodal) | Audio input | Video input | [Token-level streaming](/oss/javascript/langchain/streaming/) | [Token usage](/oss/javascript/langchain/models#token-usage) | [Logprobs](/oss/javascript/langchain/models#log-probabilities) |
| :---------------------------------------------: | :--------------------------------------------------------------: | :----------------------------------------------------------: | :---------: | :---------: | :-----------------------------------------------------------: | :---------------------------------------------------------: | :------------------------------------------------------------: |
|                        ✅                        |                                 ✅                                |                               ✅                              |      ❌      |      ❌      |                               ✅                               |                              ✅                              |                                ❌                               |

## Setup

To access Bedrock models you'll need to create an AWS account, set up the Bedrock API service, get an access key ID and secret key, and install the `@langchain/aws` integration package.

### Credentials

Head to the [AWS docs](https://docs.aws.amazon.com/bedrock/latest/userguide/getting-started.html) to sign up for AWS and setup your credentials. You'll also need to turn on model access for your account, which you can do by [following these instructions](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html).

Set your Bedrock credentials in the environment:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
export BEDROCK_AWS_REGION="us-east-1"
export BEDROCK_AWS_ACCESS_KEY_ID="your-access-key-id"
export BEDROCK_AWS_SECRET_ACCESS_KEY="your-secret-access-key"
```

Alternatively, set `AWS_BEARER_TOKEN_BEDROCK` for API key authentication. See the [AWS Bedrock API key docs](https://docs.aws.amazon.com/bedrock/latest/userguide/api-keys.html).

If you want to get automated tracing of your model calls you can also set your [LangSmith](/langsmith/observability) API key by uncommenting below:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}

# export LANGSMITH_TRACING="true"

# export LANGSMITH_API_KEY="your-api-key"
```

### Installation

The LangChain `ChatBedrockConverse` integration lives in the `@langchain/aws` package:

<CodeGroup>
  ```bash npm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  npm install @langchain/aws @langchain/core
  ```

  ```bash yarn theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  yarn add @langchain/aws @langchain/core
  ```

  ```bash pnpm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  pnpm add @langchain/aws @langchain/core
  ```
</CodeGroup>

## Instantiation

Now we can instantiate our model object and generate chat completions.

There are a few different ways to authenticate with AWS - the below examples rely on an access key, secret access key and region set in your environment variables:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { ChatBedrockConverse } from "@langchain/aws";

const llm = new ChatBedrockConverse({
  model: "anthropic.claude-3-5-sonnet-20240620-v1:0",
  region: process.env.BEDROCK_AWS_REGION,
  credentials: {
    accessKeyId: process.env.BEDROCK_AWS_ACCESS_KEY_ID!,
    secretAccessKey: process.env.BEDROCK_AWS_SECRET_ACCESS_KEY!,
  },
});
```

## Invocation

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const aiMsg = await llm.invoke([
  [
    "system",
    "You are a helpful assistant that translates English to French. Translate the user sentence.",
  ],
  ["human", "I love programming."],
])
aiMsg
```

```text theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
AIMessage {
  "id": "f5dc5791-224e-4fe5-ba2e-4cc51d9e7795",
  "content": "J'adore la programmation.",
  "additional_kwargs": {},
  "response_metadata": {
    "$metadata": {
      "httpStatusCode": 200,
      "requestId": "f5dc5791-224e-4fe5-ba2e-4cc51d9e7795",
      "attempts": 1,
      "totalRetryDelay": 0
    },
    "metrics": {
      "latencyMs": 584
    },
    "stopReason": "end_turn",
    "usage": {
      "inputTokens": 29,
      "outputTokens": 11,
      "totalTokens": 40
    }
  },
  "tool_calls": [],
  "invalid_tool_calls": [],
  "usage_metadata": {
    "input_tokens": 29,
    "output_tokens": 11,
    "total_tokens": 40
  }
}
```

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
console.log(aiMsg.content)
```

```text theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
J'adore la programmation.
```

## Tool calling

Tool calling with Bedrock models works in a similar way to [other models](/oss/javascript/langchain/tools), but note that not all Bedrock models support tool calling. Please refer to the [AWS model documentation](https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html) for more information.

***

## API reference

For detailed documentation of all `ChatBedrockConverse` features and configurations head to the [API reference](https://reference.langchain.com/javascript/langchain-aws/ChatBedrockConverse).

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/javascript/integrations/chat/bedrock_converse.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# ChatGoogle integration
Source: https://docs.langchain.com/oss/javascript/integrations/chat/google

Integrate with the ChatGoogle chat model using LangChain JavaScript.

This library supports access to a variety of Google's models, including the Gemini
family of models and their Nano Banana image generation model. You can access these
models through either Google's [Google AI](https://ai.google.dev/) API (sometimes also
called the Generative AI API or the AI Studio API) or through the Google Cloud Platform
[Vertex AI](https://cloud.google.com/vertex-ai) service.

This will help you getting started with `ChatGoogle` [chat models](/oss/javascript/langchain/models).
For detailed documentation of all `ChatGoogle` features and configurations head to the
[API reference](https://reference.langchain.com/javascript/langchain-google/index/ChatGoogle).

<Tip>
  `@langchain/google` is the recommended package for all new Google Gemini integrations.
  It replaces the older [`@langchain/google-genai`](/oss/javascript/integrations/chat/google_generative_ai)
  and [`@langchain/google-vertexai`](/oss/javascript/integrations/chat/google_vertex_ai) packages.
  See [legacy packages](/oss/javascript/integrations/providers/google#legacy-packages) for migration details.
</Tip>

## Overview

### Integration details

| Class                                                                                        | Package                                                                | Serializable | PY support |                                             Downloads                                             |                                             Version                                            |
| :------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------- | :----------: | :--------: | :-----------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------: |
| [`ChatGoogle`](https://reference.langchain.com/javascript/langchain-google/index/ChatGoogle) | [`@langchain/google`](https://www.npmjs.com/package/@langchain/google) |       ✅      |      ✅     | ![NPM - Downloads](https://img.shields.io/npm/dm/@langchain/google?style=flat-square\&label=%20&) | ![NPM - Version](https://img.shields.io/npm/v/@langchain/google?style=flat-square\&label=%20&) |

### Model features

See the links in the table headers below for guides on how to use specific features.

| [Tool calling](/oss/javascript/langchain/tools) | [Structured output](/oss/javascript/langchain/structured-output) | [Image input](/oss/javascript/langchain/messages#multimodal) | Audio input | Video input | [Token-level streaming](/oss/javascript/langchain/streaming/) | [Token usage](/oss/javascript/langchain/models#token-usage) | [Logprobs](/oss/javascript/langchain/models#log-probabilities) |
| :---------------------------------------------: | :--------------------------------------------------------------: | :----------------------------------------------------------: | :---------: | :---------: | :-----------------------------------------------------------: | :---------------------------------------------------------: | :------------------------------------------------------------: |
|                        ✅                        |                                 ✅                                |                               ✅                              |      ✅      |      ✅      |                               ✅                               |                              ✅                              |                                ✅                               |

Note that while logprobs are supported, Gemini has fairly restricted usage of them.

## Setup

### Credentials through AI Studio (API Key)

To use the model through Google AI Studio (sometimes called the Generative AI
API), you will need an API key. You can obtain one from the
[Google AI Studio](https://aistudio.google.com/app/apikey).

Once you have your API key, you can set it as an environment variable:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
export GOOGLE_API_KEY="your-api-key"
```

Or you can pass it directly to the model constructor:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { ChatGoogle } from "@langchain/google";

const llm = new ChatGoogle({
  apiKey: "your-api-key",
  model: "gemini-2.5-flash",
});
```

### Credentials through Vertex AI Express Mode (API Key)

Vertex AI also supports [Express Mode](https://cloud.google.com/vertex-ai/docs/start/introduction-unified-platform#express-mode),
which allows you to use an API key for authentication. You can obtain a Vertex AI
API key from the [Google Cloud Console](https://console.cloud.google.com/vertex-ai/studio/api-key).

Once you have your API key, you can set it as an environment variable:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
export GOOGLE_API_KEY="your-api-key"
```

When using [Vertex AI Express Mode](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/start/express-mode/overview), you will also need to specify the platform
type as `gcp` when instantiating the model.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const llm = new ChatGoogle({
  model: "gemini-2.5-flash",
  platformType: "gcp",
  // apiKey: "...", // Optional if GOOGLE_API_KEY is set
});
```

### Credentials through Vertex AI (OAuth Application Default Credentials / ADC)

For production environments on Google Cloud, it is recommended to use
[Application Default Credentials (ADC)](https://cloud.google.com/docs/authentication/provide-credentials-adc).
This is supported in Node.js environments.

If you are running on a local machine, you can set up ADC by installing the
[Google Cloud SDK](https://cloud.google.com/sdk) and running:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
gcloud auth application-default login
```

Alternatively, you can set the `GOOGLE_APPLICATION_CREDENTIALS` environment
variable to the path of your service account key file:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/service-account-key.json"
```

### Credentials through Vertex AI (OAuth saved credentials)

If you are running in a web environment or want to provide credentials directly,
you can use the `GOOGLE_CLOUD_CREDENTIALS` environment variable. This should
contain the **content** of your service account key file (not the path).

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
export GOOGLE_CLOUD_CREDENTIALS='{"type":"service_account","project_id":"your-project-id",...}'
```

You can also provide these credentials directly in your code using the
`credentials` parameter.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const llm = new ChatGoogle({
  model: "gemini-2.5-flash",
  platformType: "gcp",
  credentials: {
    type: "service_account",
    project_id: "your-project-id",
    private_key_id: "your-private-key-id",
    private_key: "your-private-key",
    client_email: "your-service-account-email",
    client_id: "your-client-id",
    auth_uri: "https://accounts.google.com/o/oauth2/auth",
    token_uri: "https://oauth2.googleapis.com/token",
    auth_provider_x509_cert_url: "https://www.googleapis.com/oauth2/v1/certs",
    client_x509_cert_url: "your-cert-url",
  }
});
```

### Tracing

If you want to get automated tracing of your model calls you can also set
your [LangSmith](/langsmith/observability) API key by uncommenting below:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}

# export LANGSMITH_TRACING="true"

# export LANGSMITH_API_KEY="your-api-key"
```

### Installation

The LangChain `ChatGoogle` integration lives in the `@langchain/google` package:

<CodeGroup>
  ```bash npm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  npm install @langchain/google @langchain/core
  ```

  ```bash yarn theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  yarn add @langchain/google @langchain/core
  ```

  ```bash pnpm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  pnpm add @langchain/google @langchain/core
  ```
</CodeGroup>

## Instantiation

The import path differs depending on whether you are running in a Node.js environment or a Web/Edge environment.

<CodeGroup>
  ```typescript Node.js theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { ChatGoogle } from "@langchain/google/node";
  ```

  ```typescript Web/Edge theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { ChatGoogle } from "@langchain/google";
  ```
</CodeGroup>

The model will automatically determine whether to use the Google AI API or Vertex AI based on your configuration:

* If you provide an `apiKey` (or set `GOOGLE_API_KEY`), it defaults to Google AI.
* If you provide `credentials` (or set `GOOGLE_APPLICATION_CREDENTIALS` / `GOOGLE_CLOUD_CREDENTIALS` in Node), it defaults to Vertex AI.

### Google AI (AI Studio)

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const llm = new ChatGoogle({
  model: "gemini-2.5-flash",
  maxRetries: 2,
  // apiKey: "...", // Optional if GOOGLE_API_KEY is set
});
```

### Vertex AI

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const llm = new ChatGoogle({
  model: "gemini-2.5-flash",
  // credentials: { ... }, // Optional if using ADC or GOOGLE_CLOUD_CREDENTIALS
});
```

### Vertex AI Express Mode

To use Vertex AI with an API key (Express Mode), you must explicitly set the `platformType`.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const llm = new ChatGoogle({
  model: "gemini-2.5-flash",
  platformType: "gcp",
  // apiKey: "...", // Optional if GOOGLE_API_KEY is set
});
```

### Model Configuration Best Practices

While `ChatGoogle` supports standard model parameters like `temperature`, `topP`, and `topK`,
best practice with Gemini models is to leave these at their default values. The models
are highly tuned around these defaults.

If you want to control the "randomness" or "creativity" of the model, it is recommended
to use specific instructions in your prompt or system prompt (e.g., "Be creative",
"Give a concise factual answer") rather than adjusting the temperature.

## Invocation

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { HumanMessage, SystemMessage } from "@langchain/core/messages";

const aiMsg = await llm.invoke([
  new SystemMessage(
    "You are a helpful assistant that translates English to French. Translate the user sentence."
  ),
  new HumanMessage("I love programming."),
]);
```

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
console.log(aiMsg.text);
```

```text theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
J'adore programmer.
```

## Response Metadata

The `AIMessage` response contains metadata about the generation, including
token usage and log probabilities.

### Token Usage

The `usage_metadata` property allows you to inspect token counts.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const res = await llm.invoke("Hello, how are you?");

console.log(res.usage_metadata);
```

```text theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{ input_tokens: 6, output_tokens: 7, total_tokens: 13 }
```

### Logprobs

If you enable `logprobs` in the model configuration, they will be available in
the `response_metadata`.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const llmWithLogprobs = new ChatGoogle({
  model: "gemini-2.5-flash",
  logprobs: 2, // Number of top candidates to return
});

const resWithLogprobs = await llmWithLogprobs.invoke("Hello");

console.log(resWithLogprobs.response_metadata.logprobs_result);
```

## Safety settings

By default, current versions of Gemini have safety settings turned off.

If you want to enable safety settings for various categories, you can use
the `safetySettings` attribute of the model.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { ChatGoogle } from "@langchain/google";

const llm = new ChatGoogle({
  model: "gemini-2.5-flash",
  safetySettings: [
    {
      category: "HARM_CATEGORY_HARASSMENT",
      threshold: "BLOCK_LOW_AND_ABOVE",
    },
  ],
});
```

## Structured output

You can use the `withStructuredOutput` method to get structured JSON output from the model.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { ChatGoogle } from "@langchain/google";
import { z } from "zod";

const llm = new ChatGoogle("gemini-2.5-flash");

const schema = z.object({
  people: z.array(z.object({
    name: z.string().describe("The name of the person"),
    age: z.number().describe("The age of the person"),
  })),
});

const structuredLlm = llm.withStructuredOutput(schema);

const res = await structuredLlm.invoke("John is 25 and Jane is 30.");
console.log(res);
```

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "people": [
    { "name": "John", "age": 25 },
    { "name": "Jane", "age": 30 }
  ]
}
```

## Tool calling

`ChatGoogle` supports standard LangChain [tool calling](/oss/javascript/langchain/tools) as
well as Gemini-specific "Specialty Tools" (like Code Execution and Grounding).

### Standard Tools

You can use standard LangChain tools defined with Zod schemas.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { ChatGoogle } from "@langchain/google";
import { tool } from "@langchain/core/tools";
import { z } from "zod";

const weatherTool = tool((input) => {
  return "It is sunny and 75 degrees.";
}, {
  name: "get_weather",
  description: "Get the weather for a location",
  schema: z.object({
    location: z.string(),
  }),
});

const llm = new ChatGoogle("gemini-2.5-flash")
  .bindTools([weatherTool]);

const res = await llm.invoke("What is the weather in SF?");
console.log(res.tool_calls);
```

### Specialty Tools

Gemini offers several built-in tools for code execution and grounding.

<Warning>
  You cannot mix these "Specialty Tools" (Code Execution, Google Search, etc.)
  with standard LangChain tools (like the weather tool above) in the same request.
</Warning>

#### Code execution

Gemini models support code execution, which allows the model to generate and run
Python code to solve complex problems.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { ChatGoogle } from "@langchain/google";

const llm = new ChatGoogle("gemini-2.5-flash")
  .bindTools([
    {
      codeExecution: {},
    },
  ]);

const res = await llm.invoke("Calculate the 100th Fibonacci number.");
console.log(res.contentBlocks);
```

#### Grounding with Google Search

You can use the `googleSearch` tool to ground responses with Google Search.
This is useful for questions about current events or specific facts.

<Note>
  The `googleSearchRetrieval` tool is maintained for backwards compatibility, but `googleSearch` is preferred.
</Note>

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { ChatGoogle } from "@langchain/google";

const llm = new ChatGoogle("gemini-2.5-flash")
  .bindTools([
    {
      googleSearch: {},
    },
  ]);

const res = await llm.invoke("Who won the latest World Series?");
console.log(res.text);
```

#### Grounding with URL Retrieval

You can also ground responses using a specific URL.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { ChatGoogle } from "@langchain/google";

const llm = new ChatGoogle("gemini-2.5-flash")
  .bindTools([
    {
      urlContext: {},
    },
  ]);

const prompt = "Summarize this page: https://js.langchain.com/";
const res = await llm.invoke(prompt);
console.log(res.text);
```

#### Grounding with a data store

If you are using Vertex AI (`platformType: "gcp"`), you can ground responses using
a Vertex AI Search data store.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { ChatGoogle } from "@langchain/google";

const projectId = "YOUR_PROJECT_ID";
const datastoreId = "YOUR_DATASTORE_ID";

const searchRetrievalToolWithDataset = {
  retrieval: {
    vertexAiSearch: {
      datastore: `projects/${projectId}/locations/global/collections/default_collection/dataStores/${datastoreId}`,
    },
    disableAttribution: false,
  },
};

const llm = new ChatGoogle({
  model: "gemini-2.5-pro",
  platformType: "gcp",
}).bindTools([searchRetrievalToolWithDataset]);

const res = await llm.invoke(
  "What is the score of Argentina vs Bolivia football game?"
);
console.log(res.text);
```

## Context caching

By default, Gemini models do implicit context caching. If the start of the
history that you send to Gemini exactly matches context that Gemini has in
its cache, it will reduce the token cost for that request.

You can also explicitly pass some content to the model once, cache the input
tokens, and then refer to the cached tokens for subsequent requests to reduce cost
and latency. Creating this explicit cache is not supported by LangChain, but
if you have created the cache, you can reference it in your invocation.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { ChatGoogle } from "@langchain/google";

const llm = new ChatGoogle("gemini-2.5-pro");

// Pass the cache name to the model
const res = await llm.invoke("Summarize this document", {
  cachedContent: "projects/123/locations/us-central1/cachedContents/456",
});
```

## Multimodal Requests

The `ChatGoogle` model supports multimodal requests, allowing you to send images,
audio, and video along with text. You can use the `contentBlocks` field in your
messages to provide these inputs in a structured way.

### Images

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { ChatGoogle } from "@langchain/google";
import { HumanMessage } from "@langchain/core/messages";
import * as fs from "fs";

const llm = new ChatGoogle("gemini-2.5-flash");

const image = fs.readFileSync("./hotdog.jpg").toString("base64");

const res = await llm.invoke([
  new HumanMessage({
    contentBlocks: [
      {
        type: "text",
        text: "What is in this image?",
      },
      {
        type: "image",
        mimeType: "image/jpeg",
        data: image,
      },
    ],
  }),
]);

console.log(res.text);
```

### Audio

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const audio = fs.readFileSync("./speech.wav").toString("base64");

const res = await llm.invoke([
  new HumanMessage({
    contentBlocks: [
      {
        type: "text",
        text: "Summarize this audio.",
      },
      {
        type: "audio",
        mimeType: "audio/wav",
        data: audio,
      },
    ],
  }),
]);

console.log(res.text);
```

### Video

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const video = fs.readFileSync("./movie.mp4").toString("base64");

const res = await llm.invoke([
  new HumanMessage({
    contentBlocks: [
      {
        type: "text",
        text: "Describe the video.",
      },
      {
        type: "video",
        mimeType: "video/mp4",
        data: video,
      },
    ],
  }),
]);

console.log(res.text);
```

## Reasoning / Thinking

Google's Gemini 2.5 and Gemini 3 models support "thinking" or "reasoning" steps.
These models may perform reasoning even if you don't explicitly configure it,
but the library will only return the reasoning summaries (thought blocks) if you
explicitly set a value for how much to reason/think.

This library offers compatibility between models, allowing you to use unified parameters:

* `maxReasoningTokens` (or `thinkingBudget`): Specifies the maximum number of tokens to use for reasoning.
  * `0`: Turns off reasoning (if supported).
  * `-1`: Uses the model's default.
  * `> 0`: Sets the specific token budget.

* `reasoningEffort` (or `thinkingLevel`): Sets the relative effort.
  * Values: `"minimal"`, `"low"`, `"medium"`, `"high"`.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { ChatGoogle } from "@langchain/google";

const llm = new ChatGoogle({
  model: "gemini-3.1-pro-preview",
  reasoningEffort: "high",
});

const res = await llm.invoke("What is the square root of 144?");

// The reasoning steps are available in the contentBlocks
const reasoningBlocks = res.contentBlocks.filter((block) => block.type === "reasoning");
reasoningBlocks.forEach((block) => {
  if (block.type === "reasoning") {
    console.log("Thought:", block.reasoning);
  }
});

console.log("Answer:", res.text);
```

<Note>
  Thought blocks also include a `reasoningContentBlock` field. This contains the `ContentBlock` based on
  the underlying part sent by Gemini. While this is typically a text block, for multimodal models like
  Nano Banana Pro, it could be an image or other media block.
</Note>

## Image Generation with Nano Banana and Nano Banana Pro

To generate images, you need to use a model that supports it (such as
`gemini-2.5-flash-image`) and configure the `responseModalities` to
include "IMAGE".

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { ChatGoogle } from "@langchain/google";
import * as fs from "fs";

const llm = new ChatGoogle({
  model: "gemini-2.5-flash-image",
  responseModalities: ["IMAGE", "TEXT"],
});

const res = await llm.invoke(
  "I would like to see a drawing of a house with the sun shining overhead. Drawn in crayon."
);

// Generated images are returned in the contentBlocks of the message
for (const [index, block] of res.contentBlocks.entries()) {
  if (block.type === "file" && block.data) {
    const base64Data = block.data;
    // Determine the correct file extension from the MIME type
    const mimeType = (block.mimeType || "image/png").split(";")[0];
    const extension = mimeType.split("/")[1] || "png";
    const filename = `generated_image_${index}.${extension}`;

    // Save the image to a file
    fs.writeFileSync(filename, Buffer.from(base64Data, "base64"));
    console.log(`[Saved image to ${filename}]`);
  } else if (block.type === "text") {
    console.log(block.text);
  }
}
```

## Speech Generation (TTS)

Some Gemini models support generating speech (audio output). To enable this,
configure the `responseModalities` to include "AUDIO" and provide a
`speechConfig`.

The `speechConfig` can be a
[full Gemini speech configuration object](https://ai.google.dev/api/generate-content#SpeechConfig),
but for most cases you just need to provide a string with a prebuilt
[voice name](https://ai.google.dev/gemini-api/docs/speech-generation#voices).

Many models return audio in raw PCM format (`audio/L16`), which requires a
WAV header to be playable by most media players.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { ChatGoogle } from "@langchain/google";
import * as fs from "fs";

const llm = new ChatGoogle({
  model: "gemini-2.5-flash-preview-tts",
  responseModalities: ["AUDIO", "TEXT"],
  speechConfig: "Zubenelgenubi", // Prebuilt voice name
});

const res = await llm.invoke("Say cheerfully: Have a wonderful day!");

// Function to add a WAV header to raw PCM data
function addWavHeader(pcmData: Buffer, sampleRate = 24000) {
  const header = Buffer.alloc(44);
  header.write("RIFF", 0);
  header.writeUInt32LE(36 + pcmData.length, 4);
  header.write("WAVE", 8);
  header.write("fmt ", 12);
  header.writeUInt32LE(16, 16);
  header.writeUInt16LE(1, 20); // PCM
  header.writeUInt16LE(1, 22); // Mono
  header.writeUInt32LE(sampleRate, 24);
  header.writeUInt32LE(sampleRate * 2, 28); // Byte rate (16-bit mono)
  header.writeUInt16LE(2, 32); // Block align
  header.writeUInt16LE(16, 34); // Bits per sample
  header.write("data", 36);
  header.writeUInt32LE(pcmData.length, 40);
  return Buffer.concat([header, pcmData]);
}

// Generated audio is returned in the contentBlocks
for (const [index, block] of res.contentBlocks.entries()) {
  if (block.type === "file" && block.data) {
    let audioBuffer = Buffer.from(block.data, "base64");
    let filename = `generated_audio_${index}.wav`;

    if (block.mimeType?.startsWith("audio/L16")) {
      audioBuffer = addWavHeader(audioBuffer);
    } else if (block.mimeType) {
      // Ignore parameters in the mimeType, such as "; rate=24000"
      const mimeType = block.mimeType.split(";")[0];
      const extension = mimeType.split("/")[1] || "wav";
      filename = `generated_audio_${index}.${extension}`;
    }

    // Save the audio to a file
    fs.writeFileSync(filename, audioBuffer);
    console.log(`[Saved audio to ${filename}]`);
  } else if (block.type === "text") {
    console.log(block.text);
  }
}
```

### Multi-speaker TTS

You can also configure multiple speakers for a single request. This is useful to have
Gemini read a script. The simplified `speechConfig` for this requires you to assign
a `speaker` to each pre-defined `name` representing the voice, and then use that
speaker in the script.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const multiSpeakerLlm = new ChatGoogle({
  model: "gemini-2.5-flash-preview-tts",
  responseModalities: ["AUDIO"],
  speechConfig: [
    { speaker: "Joe", name: "Kore" },
    { speaker: "Jane", name: "Puck" },
  ],
});

const res = await multiSpeakerLlm.invoke(`
  Joe: How's it going today, Jane?
  Jane: Not too bad, how about you?
`);
```

## API Reference

For detailed documentation of all `ChatGoogle` features and configurations head to the
[API reference](https://reference.langchain.com/javascript/langchain-google/index/ChatGoogle).

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/javascript/integrations/chat/google.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
