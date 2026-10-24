# Chat model integrations
Source: https://docs.langchain.com/oss/javascript/integrations/chat/index

Integrate with chat models using LangChain JavaScript.

[Chat models](/oss/javascript/langchain/models) are language models that use a sequence of [messages](/oss/javascript/langchain/messages) as inputs and return messages as outputs <Tooltip>(as opposed to plaintext)</Tooltip>.

## Install and use

<Tip>
  See [this section for general instructions on installing LangChain packages](/oss/javascript/langchain/install).
</Tip>

<AccordionGroup>
  <Accordion title="OpenAI">
    Install:

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

    Add environment variables:

    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    OPENAI_API_KEY=your-api-key
    ```

    Instantiate the model:

    ```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    import { ChatOpenAI } from "@langchain/openai";

    const model = new ChatOpenAI({ model: "gpt-5.4-mini" });
    ```

    ```javascript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    await model.invoke("Hello, world!")
    ```
  </Accordion>

  <Accordion title="Anthropic">
    Install:

    <CodeGroup>
      ```bash npm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      npm i @langchain/anthropic @langchain/core
      ```

      ```bash yarn theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      yarn add @langchain/anthropic @langchain/core
      ```

      ```bash pnpm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      pnpm add @langchain/anthropic @langchain/core
      ```
    </CodeGroup>

    Add environment variables:

    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    ANTHROPIC_API_KEY=your-api-key
    ```

    Instantiate the model:

    ```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    import { ChatAnthropic } from "@langchain/anthropic";

    const model = new ChatAnthropic({
    model: "claude-3-sonnet-20240620",
    temperature: 0
    });
    ```

    ```javascript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    await model.invoke("Hello, world!")
    ```
  </Accordion>

  <Accordion title="Google Gemini">
    Install:

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

    Add environment variables:

    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    GOOGLE_API_KEY=your-api-key
    ```

    Instantiate the model:

    ```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    import { ChatGoogle } from "@langchain/google";

    const model = new ChatGoogle("gemini-2.5-flash");
    ```

    ```javascript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    await model.invoke("Hello, world!")
    ```
  </Accordion>

  <Accordion title="MistralAI">
    Install:

    <CodeGroup>
      ```bash npm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      npm install @langchain/mistralai @langchain/core
      ```

      ```bash yarn theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      yarn add @langchain/mistralai @langchain/core
      ```

      ```bash pnpm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      pnpm add @langchain/mistralai @langchain/core
      ```
    </CodeGroup>

    Add environment variables:

    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    MISTRAL_API_KEY=your-api-key
    ```

    Instantiate the model:

    ```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    import { ChatMistralAI } from "@langchain/mistralai";

    const model = new ChatMistralAI({
    model: "mistral-large-latest",
    temperature: 0
    });
    ```

    ```javascript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    await model.invoke("Hello, world!")
    ```
  </Accordion>

  <Accordion title="Groq">
    Install:

    <CodeGroup>
      ```bash npm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      npm install @langchain/groq @langchain/core
      ```

      ```bash yarn theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      yarn add @langchain/groq @langchain/core
      ```

      ```bash pnpm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      pnpm add @langchain/groq @langchain/core
      ```
    </CodeGroup>

    Add environment variables:

    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    GROQ_API_KEY=your-api-key
    ```

    Instantiate the model:

    ```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    import { ChatGroq } from "@langchain/groq";

    const model = new ChatGroq({
    model: "llama-3.3-70b-versatile",
    temperature: 0
    });
    ```

    ```javascript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    await model.invoke("Hello, world!")
    ```
  </Accordion>
</AccordionGroup>

## Featured models

<Info>
  **While these LangChain classes support the indicated advanced feature**, you may need to refer to provider-specific documentation to learn which hosted models or backends support the feature.
</Info>

| Model                                                                                | Stream | [Tool Calling](/oss/javascript/langchain/tools/) | [`withStructuredOutput()`](/oss/javascript/langchain/models#structured-output) | [`Multimodal`](/oss/javascript/langchain/messages#multimodal) |
| ------------------------------------------------------------------------------------ | ------ | ------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------- |
| [`ChatOpenAI`](/oss/javascript/integrations/chat/openai/)                            | ✅      | ✅                                                | ✅                                                                              | ✅                                                             |
| [`ChatAnthropic`](/oss/javascript/integrations/chat/anthropic/)                      | ✅      | ✅                                                | ✅                                                                              | ✅                                                             |
| [`ChatGoogle`](/oss/javascript/integrations/chat/google/)                            | ✅      | ✅                                                | ✅                                                                              | ✅                                                             |
| [`ChatBedrockConverse`](/oss/javascript/integrations/chat/bedrock_converse/)         | ✅      | ✅                                                | ✅                                                                              | ✅                                                             |
| [`ChatCloudflareWorkersAI`](/oss/javascript/integrations/chat/cloudflare_workersai/) | ✅      | ❌                                                | ❌                                                                              | ❌                                                             |
| [`ChatCohere`](/oss/javascript/integrations/chat/cohere/)                            | ✅      | ✅                                                | ✅                                                                              | ✅                                                             |
| [`ChatFireworks`](/oss/javascript/integrations/chat/fireworks/)                      | ✅      | ✅                                                | ✅                                                                              | ✅                                                             |
| [`ChatGroq`](/oss/javascript/integrations/chat/groq/)                                | ✅      | ✅                                                | ✅                                                                              | ✅                                                             |
| [`ChatMistralAI`](/oss/javascript/integrations/chat/mistral/)                        | ✅      | ✅                                                | ✅                                                                              | ✅                                                             |
| [`ChatOllama`](/oss/javascript/integrations/chat/ollama/)                            | ✅      | ✅                                                | ✅                                                                              | ✅                                                             |
| [`ChatPerplexity`](/oss/javascript/integrations/chat/perplexity/)                    | ✅      | ❌                                                | ✅                                                                              | ❌                                                             |
| [`ChatTogetherAI`](/oss/javascript/integrations/chat/togetherai/)                    | ✅      | ✅                                                | ✅                                                                              | ✅                                                             |
| [`ChatXAI`](/oss/javascript/integrations/chat/xai/)                                  | ✅      | ✅                                                | ✅                                                                              | ❌                                                             |

See the [full list of chat model integrations](#all-chat-models) below for more options.

## Routers & proxies

Routers and proxies give you access to models from multiple providers through a single API and credential. They can simplify billing, let you switch between models without changing integrations, and offer features like automatic fallbacks.

| Provider                             | Integration                                                      | Description                                                             |
| ------------------------------------ | ---------------------------------------------------------------- | ----------------------------------------------------------------------- |
| [OpenRouter](https://openrouter.ai/) | [`ChatOpenRouter`](/oss/javascript/integrations/chat/openrouter) | Unified access to models from OpenAI, Anthropic, Google, Meta, and more |

## Chat Completions API

Certain model providers offer endpoints that are compatible with OpenAI's (legacy) [Chat Completions API](https://platform.openai.com/docs/guides/completions). In such case, you can use [`ChatOpenAI`](/oss/javascript/integrations/chat/openai) with a custom `base_url` to connect to these endpoints. Note that features built on top of the Chat Completions API may not be fully supported by `ChatOpenAI`; in such cases, consider using a provider-specific class if available.

## All chat models

<Columns>
  <Card title="Anthropic" icon="link" href="/oss/javascript/integrations/chat/anthropic" />

  <Card title="Azure OpenAI" icon="link" href="/oss/javascript/integrations/chat/azure" />

  <Card title="Baidu Qianfan" icon="link" href="/oss/javascript/integrations/chat/baidu_qianfan" />

  <Card title="Amazon Bedrock Converse" icon="link" href="/oss/javascript/integrations/chat/bedrock_converse" />

  <Card title="Cerebras" icon="link" href="/oss/javascript/integrations/chat/cerebras" />

  <Card title="Cloudflare Workers AI" icon="link" href="/oss/javascript/integrations/chat/cloudflare_workersai" />

  <Card title="Cohere" icon="link" href="/oss/javascript/integrations/chat/cohere" />

  <Card title="DeepSeek" icon="link" href="/oss/javascript/integrations/chat/deepseek" />

  <Card title="Fake LLM" icon="link" href="/oss/javascript/integrations/chat/fake" />

  <Card title="Google Gemini" icon="link" href="/oss/javascript/integrations/chat/google" />

  <Card title="Groq" icon="link" href="/oss/javascript/integrations/chat/groq" />

  <Card title="MistralAI" icon="link" href="/oss/javascript/integrations/chat/mistral" />

  <Card title="Ollama" icon="link" href="/oss/javascript/integrations/chat/ollama" />

  <Card title="OpenAI" icon="link" href="/oss/javascript/integrations/chat/openai" />

  <Card title="Perplexity" icon="link" href="/oss/javascript/integrations/chat/perplexity" />

  <Card title="xAI" icon="link" href="/oss/javascript/integrations/chat/xai" />

  <Card title="Fireworks" icon="link" href="/oss/javascript/integrations/chat/fireworks" />

  <Card title="IBM watsonx.ai" icon="link" href="/oss/javascript/integrations/chat/ibm" />

  <Card title="Together" icon="link" href="/oss/javascript/integrations/chat/togetherai" />
</Columns>

<Info>
  If you'd like to contribute an integration, see [Contributing integrations](/oss/javascript/contributing#add-a-new-integration).
</Info>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/javascript/integrations/chat/index.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# ChatOpenAI integration
Source: https://docs.langchain.com/oss/javascript/integrations/chat/openai

Integrate with the ChatOpenAI chat model using LangChain JavaScript.

[OpenAI](https://en.wikipedia.org/wiki/OpenAI) is an artificial intelligence (AI) research laboratory.

This guide will help you getting started with OpenAI [chat models](/oss/javascript/langchain/models). For detailed documentation of all `ChatOpenAI` features and configurations head to the [API reference](https://reference.langchain.com/javascript/langchain-openai/ChatOpenAI).

<Note>
  **Chat Completions API compatibility**

  `ChatOpenAI` is fully compatible with OpenAI's (legacy) [Chat Completions API](https://platform.openai.com/docs/guides/completions). If you are looking to connect to other model providers that support the Chat Completions API, you can do so – see [instructions](/oss/javascript/integrations/chat#chat-completions-api).
</Note>

<Info>
  **OpenAI models hosted on Azure**

  Note that certain OpenAI models can also be accessed via the [Microsoft Azure platform](https://azure.microsoft.com/en-us/products/ai-foundry/models/openai/).
</Info>

## Overview

### Integration details

| Class                                                                                  | Package                                                                | Serializable | [PY support](https://python.langchain.com/docs/integrations/chat/openai) |                                             Downloads                                             |                                             Version                                            |
| :------------------------------------------------------------------------------------- | :--------------------------------------------------------------------- | :----------: | :----------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------: |
| [`ChatOpenAI`](https://reference.langchain.com/javascript/langchain-openai/ChatOpenAI) | [`@langchain/openai`](https://www.npmjs.com/package/@langchain/openai) |       ✅      |                                     ✅                                    | ![NPM - Downloads](https://img.shields.io/npm/dm/@langchain/openai?style=flat-square\&label=%20&) | ![NPM - Version](https://img.shields.io/npm/v/@langchain/openai?style=flat-square\&label=%20&) |

### Model features

See the links in the table headers below for guides on how to use specific features.

| [Tool calling](/oss/javascript/langchain/tools) | [Structured output](/oss/javascript/langchain/structured-output) | [Image input](/oss/javascript/langchain/messages#multimodal) | Audio input | Video input | [Token-level streaming](/oss/javascript/langchain/streaming/) | [Token usage](/oss/javascript/langchain/models#token-usage) | [Logprobs](/oss/javascript/langchain/models#log-probabilities) |
| :---------------------------------------------: | :--------------------------------------------------------------: | :----------------------------------------------------------: | :---------: | :---------: | :-----------------------------------------------------------: | :---------------------------------------------------------: | :------------------------------------------------------------: |
|                        ✅                        |                                 ✅                                |                               ✅                              |      ❌      |      ❌      |                               ✅                               |                              ✅                              |                                ✅                               |

## Setup

To access OpenAI chat models you'll need to create an OpenAI account, get an API key, and install the `@langchain/openai` integration package.

### Credentials

Head to [OpenAI's website](https://platform.openai.com/) to sign up for OpenAI and generate an API key. Once you've done this set the `OPENAI_API_KEY` environment variable:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
export OPENAI_API_KEY="your-api-key"
```

If you want to get automated tracing of your model calls you can also set your [LangSmith](/langsmith/observability) API key by uncommenting below:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}

# export LANGSMITH_TRACING="true"
