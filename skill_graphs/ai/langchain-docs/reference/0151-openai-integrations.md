# OpenAI integrations
Source: https://docs.langchain.com/oss/javascript/integrations/providers/openai

Integrate with OpenAI using LangChain JavaScript.

LangChain integrates with OpenAI and Azure OpenAI through the `@langchain/openai` package.

> [OpenAI](https://en.wikipedia.org/wiki/OpenAI) is American artificial intelligence (AI) research laboratory
> consisting of the non-profit `OpenAI Incorporated`
> and its for-profit subsidiary corporation `OpenAI Limited Partnership`.
> OpenAI conducts AI research with the declared intention of promoting and developing a friendly AI.
> OpenAI systems run on an `Azure`-based supercomputing platform from `Microsoft`.

> The [OpenAI API](https://platform.openai.com/docs/models) is powered by a diverse set of models with different capabilities and price points.
>
> [ChatGPT](https://chat.openai.com) is the Artificial Intelligence (AI) chatbot developed by `OpenAI`.

## Installation and setup

* Get an OpenAI api key and set it as an environment variable (`OPENAI_API_KEY`)

## Chat model

See a [usage example](/oss/javascript/integrations/chat/openai).

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { ChatOpenAI } from "@langchain/openai";
```

## LLM

See a [usage example](/oss/javascript/integrations/llms/openai).

<Tip>
  See [this section for general instructions on installing LangChain packages](/oss/javascript/langchain/install).
</Tip>

```bash npm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
npm install @langchain/openai @langchain/core
```

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { OpenAI } from "@langchain/openai";
```

## Text embedding model

See a [usage example](/oss/javascript/integrations/embeddings/openai)

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { OpenAIEmbeddings } from "@langchain/openai";
```

## Chain

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { OpenAIModerationChain } from "@langchain/classic/chains";
```

## Middleware

Middleware specifically designed for OpenAI models. Learn more about [middleware](/oss/javascript/langchain/middleware/overview).

| Middleware                                | Description                                               |
| ----------------------------------------- | --------------------------------------------------------- |
| [Content moderation](#content-moderation) | Moderate agent traffic using OpenAI's moderation endpoint |

### Content moderation

Moderate agent traffic (user input, model output, and tool results) using OpenAI's moderation endpoint to detect and handle unsafe content. Content moderation is useful for the following:

* Applications requiring content safety and compliance
* Filtering harmful, hateful, or inappropriate content
* Customer-facing agents that need safety guardrails
* Meeting platform moderation requirements

<Info>
  Learn more about [OpenAI's moderation models](https://platform.openai.com/docs/guides/moderation) and categories.
</Info>

**API reference:** [`openAIModerationMiddleware`](https://reference.langchain.com/javascript/langchain/index/openAIModerationMiddleware)

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { createAgent, openAIModerationMiddleware } from "langchain";

const agent = createAgent({
  model: "openai:gpt-5.5",
  tools: [searchTool, databaseTool],
  middleware: [
    openAIModerationMiddleware({
      model: "openai:gpt-5.5",
      moderationModel: "omni-moderation-latest",
      checkInput: true,
      checkOutput: true,
      exitBehavior: "end",
    }),
  ],
});
```

<Accordion title="Configuration options">
  <ParamField type="string | BaseChatModel">
    OpenAI model to use for moderation. Can be either a model name string (e.g., `"openai:gpt-5.5"`) or a `BaseChatModel` instance. The middleware will use this model's client to access the moderation endpoint.
  </ParamField>

  <ParamField type="ModerationModel">
    OpenAI moderation model to use. Options: `'omni-moderation-latest'`, `'omni-moderation-2024-09-26'`, `'text-moderation-latest'`, `'text-moderation-stable'`
  </ParamField>

  <ParamField type="boolean">
    Whether to check user input messages before the model is called
  </ParamField>

  <ParamField type="boolean">
    Whether to check model output messages after the model is called
  </ParamField>

  <ParamField type="boolean">
    Whether to check tool result messages before the model is called
  </ParamField>

  <ParamField type="'error' | 'end' | 'replace'">
    How to handle violations when content is flagged. Options:

    * `'end'` - End agent execution immediately with a violation message
    * `'error'` - Throw `OpenAIModerationError` exception
    * `'replace'` - Replace the flagged content with the violation message and continue
  </ParamField>

  <ParamField type="string | undefined">
    Custom template for violation messages. Supports template variables:

    * `{categories}` - Comma-separated list of flagged categories
    * `{category_scores}` - JSON string of category scores
    * `{original_content}` - The original flagged content

    Default: `"I'm sorry, but I can't comply with that request. It was flagged for {categories}."`
  </ParamField>
</Accordion>

<Accordion title="Full example">
  The middleware integrates OpenAI's moderation endpoint to check content at different stages:

  **Moderation stages:**

  * `checkInput` - User messages before model call
  * `checkOutput` - AI messages after model call
  * `checkToolResults` - Tool outputs before model call

  **Exit behaviors:**

  * `'end'` (default) - Stop execution with violation message
  * `'error'` - Throw exception for application handling
  * `'replace'` - Replace flagged content and continue

  ```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { createAgent, openAIModerationMiddleware } from "langchain";

  // Basic moderation
  const agent = createAgent({
    model: "openai:gpt-5.5",
    tools: [searchTool, customerDataTool],
    middleware: [
      openAIModerationMiddleware({
        model: "openai:gpt-5.5",
        moderationModel: "omni-moderation-latest",
        checkInput: true,
        checkOutput: true,
      }),
    ],
  });

  // Strict moderation with custom message
  const agentStrict = createAgent({
    model: "openai:gpt-5.5",
    tools: [searchTool, customerDataTool],
    middleware: [
      openAIModerationMiddleware({
        model: "openai:gpt-5.5",
        moderationModel: "omni-moderation-latest",
        checkInput: true,
        checkOutput: true,
        checkToolResults: true,
        exitBehavior: "error",
        violationMessage:
          "Content policy violation detected: {categories}. " +
          "Please rephrase your request.",
      }),
    ],
  });

  // Moderation with replacement behavior
  const agentReplace = createAgent({
    model: "openai:gpt-5.5",
    tools: [searchTool],
    middleware: [
      openAIModerationMiddleware({
        model: "openai:gpt-5.5",
        checkInput: true,
        exitBehavior: "replace",
        violationMessage: "[Content removed due to safety policies]",
      }),
    ],
  });
  ```
</Accordion>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/javascript/integrations/providers/openai.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# LangChain JavaScript integrations
Source: https://docs.langchain.com/oss/javascript/integrations/providers/overview

Integrate with providers using LangChain JavaScript/TypeScript.

LangChain integrates with a wide variety of chat & embedding models, tools & toolkits, document loaders, vector stores, and more.

A **provider** is a third-party service or platform that LangChain integrates with to access AI capabilities like chat models, embeddings, and vector stores. These providers have standalone `langchain-provider` packages for improved versioning, dependency management, and testing.

## Popular providers

| Provider                                                                         | Package                                                                                | Downloads                                                             | Latest                                                         |
| :------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------- | :-------------------------------------------------------------------- | :------------------------------------------------------------- |
| [Anthropic](/oss/javascript/integrations/providers/anthropic)                    | [`@langchain/anthropic`](https://www.npmjs.com/package/@langchain/anthropic)           | ![Downloads](https://img.shields.io/npm/dm/@langchain/anthropic)      | ![NPM](https://img.shields.io/npm/v/@langchain/anthropic)      |
| [Azure CosmosDB](/oss/javascript/integrations/vectorstores/azure_cosmosdb_nosql) | [`@langchain/azure-cosmosdb`](https://www.npmjs.com/package/@langchain/azure-cosmosdb) | ![Downloads](https://img.shields.io/npm/dm/@langchain/azure-cosmosdb) | ![NPM](https://img.shields.io/npm/v/@langchain/azure-cosmosdb) |
| [Cerebras](/oss/javascript/integrations/chat/cerebras)                           | [`@langchain/cerebras`](https://www.npmjs.com/package/@langchain/cerebras)             | ![Downloads](https://img.shields.io/npm/dm/@langchain/cerebras)       | ![NPM](https://img.shields.io/npm/v/@langchain/cerebras)       |
| Cloudflare                                                                       | [`@langchain/cloudflare`](https://www.npmjs.com/package/@langchain/cloudflare)         | ![Downloads](https://img.shields.io/npm/dm/@langchain/cloudflare)     | ![NPM](https://img.shields.io/npm/v/@langchain/cloudflare)     |
| [Cohere](/oss/javascript/integrations/chat/cohere)                               | [`@langchain/cohere`](https://www.npmjs.com/package/@langchain/cohere)                 | ![Downloads](https://img.shields.io/npm/dm/@langchain/cohere)         | ![NPM](https://img.shields.io/npm/v/@langchain/cohere)         |
| [Exa](/oss/javascript/integrations/retrievers/exa)                               | [`@langchain/exa`](https://www.npmjs.com/package/@langchain/exa)                       | ![Downloads](https://img.shields.io/npm/dm/@langchain/exa)            | ![NPM](https://img.shields.io/npm/v/@langchain/exa)            |
| [Google](/oss/javascript/integrations/providers/google)                          | [`@langchain/google`](https://www.npmjs.com/package/@langchain/google)                 | ![Downloads](https://img.shields.io/npm/dm/@langchain/google)         | ![NPM](https://img.shields.io/npm/v/@langchain/google)         |
| [Groq](/oss/javascript/integrations/chat/groq)                                   | [`@langchain/groq`](https://www.npmjs.com/package/@langchain/groq)                     | ![Downloads](https://img.shields.io/npm/dm/@langchain/groq)           | ![NPM](https://img.shields.io/npm/v/@langchain/groq)           |
| [MistralAI](/oss/javascript/integrations/chat/mistral)                           | [`@langchain/mistralai`](https://www.npmjs.com/package/@langchain/mistralai)           | ![Downloads](https://img.shields.io/npm/dm/@langchain/mistralai)      | ![NPM](https://img.shields.io/npm/v/@langchain/mistralai)      |
| [MongoDB](/oss/javascript/integrations/vectorstores/mongodb_atlas)               | [`@langchain/mongodb`](https://www.npmjs.com/package/@langchain/mongodb)               | ![Downloads](https://img.shields.io/npm/dm/@langchain/mongodb)        | ![NPM](https://img.shields.io/npm/v/@langchain/mongodb)        |
| [Neo4j](/oss/javascript/integrations/vectorstores/neo4jvector)                   | [`@langchain/neo4j`](https://www.npmjs.com/package/@langchain/neo4j)                   | ![Downloads](https://img.shields.io/npm/dm/@langchain/neo4j)          | ![NPM](https://img.shields.io/npm/v/@langchain/neo4j)          |
| [Nomic](/oss/javascript/integrations/embeddings/nomic)                           | [`@langchain/nomic`](https://www.npmjs.com/package/@langchain/nomic)                   | ![Downloads](https://img.shields.io/npm/dm/@langchain/nomic)          | ![NPM](https://img.shields.io/npm/v/@langchain/nomic)          |
| [Ollama](/oss/javascript/integrations/chat/ollama)                               | [`@langchain/ollama`](https://www.npmjs.com/package/@langchain/ollama)                 | ![Downloads](https://img.shields.io/npm/dm/@langchain/ollama)         | ![NPM](https://img.shields.io/npm/v/@langchain/ollama)         |
| [OpenAI](/oss/javascript/integrations/providers/openai)                          | [`@langchain/openai`](https://www.npmjs.com/package/@langchain/openai)                 | ![Downloads](https://img.shields.io/npm/dm/@langchain/openai)         | ![NPM](https://img.shields.io/npm/v/@langchain/openai)         |
| [OpenRouter](/oss/javascript/integrations/chat/openrouter)                       | [`@langchain/openrouter`](https://www.npmjs.com/package/@langchain/openrouter)         | ![Downloads](https://img.shields.io/npm/dm/@langchain/openrouter)     | ![NPM](https://img.shields.io/npm/v/@langchain/openrouter)     |
| [Perplexity](/oss/javascript/integrations/providers/perplexity)                  | [`@langchain/perplexity`](https://www.npmjs.com/package/@langchain/perplexity)         | ![Downloads](https://img.shields.io/npm/dm/@langchain/perplexity)     | ![NPM](https://img.shields.io/npm/v/@langchain/perplexity)     |
| [PGVector](/oss/javascript/integrations/vectorstores/pgvector)                   | [`@langchain/pgvector`](https://www.npmjs.com/package/@langchain/pgvector)             | ![Downloads](https://img.shields.io/npm/dm/@langchain/pgvector)       | ![NPM](https://img.shields.io/npm/v/@langchain/pgvector)       |
| [Pinecone](/oss/javascript/integrations/vectorstores/pinecone)                   | [`@langchain/pinecone`](https://www.npmjs.com/package/@langchain/pinecone)             | ![Downloads](https://img.shields.io/npm/dm/@langchain/pinecone)       | ![NPM](https://img.shields.io/npm/v/@langchain/pinecone)       |
| [Qdrant](/oss/javascript/integrations/vectorstores/qdrant)                       | [`@langchain/qdrant`](https://www.npmjs.com/package/@langchain/qdrant)                 | ![Downloads](https://img.shields.io/npm/dm/@langchain/qdrant)         | ![NPM](https://img.shields.io/npm/v/@langchain/qdrant)         |
| [Redis](/oss/javascript/integrations/vectorstores/redis)                         | [`@langchain/redis`](https://www.npmjs.com/package/@langchain/redis)                   | ![Downloads](https://img.shields.io/npm/dm/@langchain/redis)          | ![NPM](https://img.shields.io/npm/v/@langchain/redis)          |
| [Tavily](/oss/javascript/integrations/providers/tavily)                          | [`@langchain/tavily`](https://www.npmjs.com/package/@langchain/tavily)                 | ![Downloads](https://img.shields.io/npm/dm/@langchain/tavily)         | ![NPM](https://img.shields.io/npm/v/@langchain/tavily)         |
| [Together AI](/oss/javascript/integrations/chat/togetherai)                      | [`@langchain/together-ai`](https://www.npmjs.com/package/@langchain/together-ai)       | ![Downloads](https://img.shields.io/npm/dm/@langchain/together-ai)    | ![NPM](https://img.shields.io/npm/v/@langchain/together-ai)    |
| [turbopuffer](/oss/javascript/integrations/vectorstores/turbopuffer)             | [`@langchain/turbopuffer`](https://www.npmjs.com/package/@langchain/turbopuffer)       | ![Downloads](https://img.shields.io/npm/dm/@langchain/turbopuffer)    | ![NPM](https://img.shields.io/npm/v/@langchain/turbopuffer)    |
| [Weaviate](/oss/javascript/integrations/vectorstores/weaviate)                   | [`@langchain/weaviate`](https://www.npmjs.com/package/@langchain/weaviate)             | ![Downloads](https://img.shields.io/npm/dm/@langchain/weaviate)       | ![NPM](https://img.shields.io/npm/v/@langchain/weaviate)       |
| [xAI](/oss/javascript/integrations/chat/xai)                                     | [`@langchain/xai`](https://www.npmjs.com/package/@langchain/xai)                       | ![Downloads](https://img.shields.io/npm/dm/@langchain/xai)            | ![NPM](https://img.shields.io/npm/v/@langchain/xai)            |
| [You.com](/oss/javascript/integrations/providers/youdotcom)                      | [`@youdotcom-oss/langchain`](https://www.npmjs.com/package/@youdotcom-oss/langchain)   | ![Downloads](https://img.shields.io/npm/dm/@youdotcom-oss/langchain)  | ![NPM](https://img.shields.io/npm/v/@youdotcom-oss/langchain)  |

## All providers

See [all providers](/oss/javascript/integrations/providers/all_providers) or search for a provider using the search field.

<Info>
  If you'd like to contribute an integration, see [Contributing integrations](/oss/javascript/contributing#add-a-new-integration).
</Info>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/javascript/integrations/providers/overview.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Retriever integrations
Source: https://docs.langchain.com/oss/javascript/integrations/retrievers/index

Integrate with retrievers using LangChain JavaScript.

A [retriever](/oss/javascript/langchain/retrieval) is an interface that returns documents given an unstructured query.
It is more general than a vector store.
A retriever does not need to be able to store documents, only to return (or retrieve) them.

Retrievers accept a string query as input and return a list of `Document` objects.

For specifics on how to use retrievers, see the [relevant how-to guides here](/oss/javascript/langchain/retrieval).

Note that all [vector stores](/oss/javascript/integrations/vectorstores) can be [cast to retrievers](/oss/javascript/langchain/retrieval).
Refer to the vector store [integration docs](/oss/javascript/integrations/vectorstores/) for available vector store retrievers.

## All retrievers

<Columns>
  <Card title="Alchemyst AI Retriever" icon="link" href="/oss/javascript/integrations/retrievers/alchemystai-retriever" />

  <Card title="Knowledge Bases for Amazon Bedrock" icon="link" href="/oss/javascript/integrations/retrievers/bedrock-knowledge-bases" />

  <Card title="Exa" icon="link" href="/oss/javascript/integrations/retrievers/exa" />

  <Card title="HyDE Retriever" icon="link" href="/oss/javascript/integrations/retrievers/hyde" />

  <Card title="Amazon Kendra Retriever" icon="link" href="/oss/javascript/integrations/retrievers/kendra-retriever" />

  <Card title="Time-Weighted Retriever" icon="link" href="/oss/javascript/integrations/retrievers/time-weighted-retriever" />
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
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/javascript/integrations/retrievers/index.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Sandbox integrations
Source: https://docs.langchain.com/oss/javascript/integrations/sandboxes/index

Integrate with sandbox providers using LangChain JavaScript.

Sandboxes provide isolated execution environments for running agent-generated code safely. Learn more about [sandboxes](/oss/javascript/deepagents/sandboxes).

<div>
  <a href="/oss/javascript/integrations/providers/modal">
    <img alt="" />

    <img alt="" />

    <span>Modal</span>
  </a>

  <a href="/oss/javascript/integrations/providers/daytona">
    <img alt="" />

    <img alt="" />

    <span>Daytona</span>
  </a>

  <a href="/oss/javascript/integrations/providers/deno">
    <img alt="" />

    <img alt="" />

    <span>Deno</span>
  </a>

  <a href="/langsmith/sandboxes">
    <img alt="" />

    <span>LangSmith</span>
  </a>
</div>

If you'd like to contribute a sandbox, see [Implement a sandbox integration](/oss/javascript/contributing/implement-langchain#sandboxes).

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/javascript/integrations/sandboxes/index.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Text splitter integrations
Source: https://docs.langchain.com/oss/javascript/integrations/splitters/index

Integrate with text splitters using LangChain.

<CodeGroup>
  ```bash npm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  npm install @langchain/textsplitters @langchain/core
  # Requires Node.js 20+
  ```

  ```bash pnpm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  pnpm add @langchain/textsplitters @langchain/core
  # Requires Node.js 20+
  ```

  ```bash yarn theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  yarn add @langchain/textsplitters @langchain/core
  # Requires Node.js 20+
  ```

  ```bash bun theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  bun add @langchain/textsplitters @langchain/core
  # Requires Node.js 20+
  ```
</CodeGroup>

**Text splitters** break large docs into smaller chunks that will be retrievable individually and fit within model context window limit.

There are several strategies for splitting documents, each with its own advantages.

<Tip>
  For most use cases, start with the [`RecursiveCharacterTextSplitter`](/oss/javascript/integrations/splitters/recursive_text_splitter). It provides a solid balance between keeping context intact and managing chunk size. This default strategy works well out of the box, and you should only consider adjusting it if you need to fine-tune performance for your specific application.
</Tip>

## Text structure-based

Text is naturally organized into hierarchical units such as paragraphs, sentences, and words. We can leverage this inherent structure to inform our splitting strategy, creating split that maintain natural language flow, maintain semantic coherence within split, and adapts to varying levels of text granularity. LangChain's `RecursiveCharacterTextSplitter` implements this concept:

* The [`RecursiveCharacterTextSplitter`](/oss/javascript/integrations/splitters/recursive_text_splitter) attempts to keep larger units (e.g., paragraphs) intact.
* If a unit exceeds the chunk size, it moves to the next level (e.g., sentences).
* This process continues down to the word level if necessary.

Example usage:

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { RecursiveCharacterTextSplitter } from "@langchain/textsplitters";

const splitter = new RecursiveCharacterTextSplitter({ chunkSize: 100, chunkOverlap: 0 })
const texts = splitter.splitText(document)
```

**Available text splitters**:

* [Recursively split text](/oss/javascript/integrations/splitters/recursive_text_splitter)

## Length-based

An intuitive strategy is to split documents based on their length. This simple yet effective approach ensures that each chunk doesn't exceed a specified size limit. Key benefits of length-based splitting:

* Straightforward implementation
* Consistent chunk sizes
* Easily adaptable to different model requirements

Types of length-based splitting:

* Token-based: Splits text based on the number of tokens, which is useful when working with language models.
* Character-based: Splits text based on the number of characters, which can be more consistent across different types of text.

Example implementation using LangChain's `CharacterTextSplitter` with token-based splitting:

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { TokenTextSplitter } from "@langchain/textsplitters";

const splitter = new TokenTextSplitter({ encodingName: "cl100k_base", chunkSize: 100, chunkOverlap: 0 })
const texts = splitter.splitText(document)
```

**Available text splitters**:

* [Split by tokens](/oss/javascript/integrations/splitters/split_by_token)
* [Split by characters](/oss/javascript/integrations/splitters/character_text_splitter)

## Document structure-based

Some documents have an inherent structure, such as HTML, Markdown, or JSON files. In these cases, it's beneficial to split the document based on its structure, as it often naturally groups semantically related text. Key benefits of structure-based splitting:

* Preserves the logical organization of the document
* Maintains context within each chunk
* Can be more effective for downstream tasks like retrieval or summarization

**Available text splitters**:

* [Split code](/oss/javascript/integrations/splitters/code_splitter)

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/integrations/splitters/index.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Store integrations
Source: https://docs.langchain.com/oss/javascript/integrations/stores/index

Integrate with stores using LangChain JavaScript.

## Overview

LangChain provides a key-value store interface for storing and retrieving data by key. The key-value store interface in LangChain is primarily used for caching [embeddings](/oss/javascript/integrations/embeddings).

## Interface

All [`BaseStores`](https://reference.langchain.com/javascript/langchain-core/stores/BaseStore) are **generic** and support the following interface, where `K` represents the key type and `V` represents the value type:

* `mget(keys: K[]): Promise<(V | undefined)[]>`: get the values for multiple keys, returning `undefined` if a key does not exist
* `mset(keyValuePairs: [K, V][]): Promise<void>`: set the values for multiple keys
* `mdelete(keys: K[]): Promise<void>`: delete multiple keys
* `yieldKeys(prefix?: string): AsyncGenerator<K | string>`: asynchronously yield all keys in the store, optionally filtering by a prefix

The generic nature of the interface allows you to use different types for keys and values. For example, `BaseStore<string, BaseMessage>` would store messages with string keys, while `BaseStore<string, number[]>` would store arrays of numbers.

<Note>
  Base stores are designed to work with **multiple** key-value pairs at once for efficiency. This saves on network round-trips and may allow for more efficient batch operations in the underlying store.
</Note>

## Built-in stores for local development

<Columns>
  <Card title="InMemoryStore" icon="link" href="/oss/javascript/integrations/stores/in_memory" />

  <Card title="LocalFileStore" icon="link" href="/oss/javascript/integrations/stores/file_system" />
</Columns>

## Custom stores

You can also implement your own custom store by extending the [`BaseStore`](https://reference.langchain.com/javascript/langchain-core/stores/BaseStore) class. See the [store interface documentation](https://reference.langchain.com/javascript/langchain-core/stores/BaseStore) for more details.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/javascript/integrations/stores/index.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
