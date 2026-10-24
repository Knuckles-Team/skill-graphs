# Embedding model integrations
Source: https://docs.langchain.com/oss/javascript/integrations/embeddings/index

Integrate with embedding models using LangChain JavaScript.

## Overview

<Note>
  This overview covers **text-based embedding models**. LangChain does not currently support multimodal embeddings.
</Note>

Embedding models transform raw text—such as a sentence, paragraph, or tweet—into a fixed-length vector of numbers that captures its **semantic meaning**. These vectors allow machines to compare and search text based on meaning rather than exact words.

In practice, this means that texts with similar ideas are placed close together in the vector space. For example, instead of matching only the phrase *"machine learning"*, embeddings can surface documents that discuss related concepts even when different wording is used.

### How it works

1. **Vectorization** — The model encodes each input string as a high-dimensional vector.
2. **Similarity scoring** — Vectors are compared using mathematical metrics to measure how closely related the underlying texts are.

### Similarity metrics

Several metrics are commonly used to compare embeddings:

* **Cosine similarity** — measures the angle between two vectors.
* **Euclidean distance** — measures the straight-line distance between points.
* **Dot product** — measures how much one vector projects onto another.

## Interface

LangChain provides a standard interface for text embedding models (e.g., OpenAI, Cohere, Hugging Face) via the [Embeddings](https://reference.langchain.com/javascript/langchain-core/embeddings/Embeddings) interface.

Two main methods are available:

* `embedDocuments(documents: string[]) → number[][]`: Embeds a list of documents.
* `embedQuery(text: string) → number[]`: Embeds a single query.

<Note>
  The interface allows queries and documents to be embedded with different strategies, though most providers handle them the same way in practice.
</Note>

## Install and use

<AccordionGroup>
  <Accordion title="OpenAI">
    Install dependencies:

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
    import { OpenAIEmbeddings } from "@langchain/openai";

    const embeddings = new OpenAIEmbeddings({
      model: "text-embedding-3-large"
    });
    ```
  </Accordion>

  <Accordion title="Azure">
    Install dependencies

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
    AZURE_OPENAI_API_INSTANCE_NAME=<YOUR_INSTANCE_NAME>
    AZURE_OPENAI_API_KEY=<YOUR_KEY>
    AZURE_OPENAI_API_VERSION="2024-02-01"
    ```

    Instantiate the model:

    ```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    import { AzureOpenAIEmbeddings } from "@langchain/openai";

    const embeddings = new AzureOpenAIEmbeddings({
      azureOpenAIApiEmbeddingsDeploymentName: "text-embedding-ada-002"
    });
    ```
  </Accordion>

  <Accordion title="AWS">
    Install dependencies:

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

    Add environment variables:

    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    BEDROCK_AWS_REGION=your-region
    ```

    Instantiate the model:

    ```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    import { BedrockEmbeddings } from "@langchain/aws";

    const embeddings = new BedrockEmbeddings({
      model: "amazon.titan-embed-text-v1"
    });
    ```
  </Accordion>

  <Accordion title="Google Gemini">
    Install dependencies:

    <CodeGroup>
      ```bash npm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      npm install @langchain/google-genai @langchain/core
      ```

      ```bash yarn theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      yarn add @langchain/google-genai @langchain/core
      ```

      ```bash pnpm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      pnpm add @langchain/google-genai @langchain/core
      ```
    </CodeGroup>

    Add environment variables:

    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    GOOGLE_API_KEY=your-api-key
    ```

    Instantiate the model:

    ```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    import { GoogleGenerativeAIEmbeddings } from "@langchain/google-genai";

    const embeddings = new GoogleGenerativeAIEmbeddings({
      model: "text-embedding-004"
    });
    ```
  </Accordion>

  <Accordion title="Google Vertex">
    Install dependencies:

    <CodeGroup>
      ```bash npm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      npm install @langchain/google-vertexai @langchain/core
      ```

      ```bash yarn theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      yarn add @langchain/google-vertexai @langchain/core
      ```

      ```bash pnpm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      pnpm add @langchain/google-vertexai @langchain/core
      ```
    </CodeGroup>

    Add environment variables:

    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    GOOGLE_APPLICATION_CREDENTIALS=credentials.json
    ```

    Instantiate the model:

    ```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    import { VertexAIEmbeddings } from "@langchain/google-vertexai";

    const embeddings = new VertexAIEmbeddings({
      model: "gemini-embedding-001"
    });
    ```
  </Accordion>

  <Accordion title="MistralAI">
    Install dependencies:

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
    import { MistralAIEmbeddings } from "@langchain/mistralai";

    const embeddings = new MistralAIEmbeddings({
      model: "mistral-embed"
    });
    ```
  </Accordion>

  <Accordion title="Cohere">
    Install dependencies:

    <CodeGroup>
      ```bash npm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      npm install @langchain/cohere @langchain/core
      ```

      ```bash yarn theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      yarn add @langchain/cohere @langchain/core
      ```

      ```bash pnpm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      pnpm add @langchain/cohere @langchain/core
      ```
    </CodeGroup>

    Add environment variables:

    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    COHERE_API_KEY=your-api-key
    ```

    Instantiate the model:

    ```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    import { CohereEmbeddings } from "@langchain/cohere";

    const embeddings = new CohereEmbeddings({
      model: "embed-english-v3.0"
    });
    ```
  </Accordion>

  <Accordion title="Ollama">
    Install dependencies:

    <CodeGroup>
      ```bash npm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      npm install @langchain/ollama @langchain/core
      ```

      ```bash yarn theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      yarn add @langchain/ollama @langchain/core
      ```

      ```bash pnpm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      pnpm add @langchain/ollama @langchain/core
      ```
    </CodeGroup>

    Instantiate the model:

    ```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    import { OllamaEmbeddings } from "@langchain/ollama";

    const embeddings = new OllamaEmbeddings({
      model: "llama2",
      baseUrl: "http://localhost:11434", // Default value
    });
    ```
  </Accordion>
</AccordionGroup>

## Caching

Embeddings can be stored or temporarily cached to avoid needing to recompute them.

Caching embeddings can be done using a `CacheBackedEmbeddings`. This wrapper stores embeddings in a key-value store, where the text is hashed and the hash is used as the key in the cache.

The main supported way to initialize a `CacheBackedEmbeddings` is `fromBytesStore`. It takes the following parameters:

* **underlyingEmbeddings**: The embedder to use for embedding.
* **documentEmbeddingStore**: Any [`BaseStore`](/oss/javascript/integrations/stores/) for caching document embeddings.
* **options.namespace**: (optional, defaults to `""`) The namespace to use for the document cache. Helps avoid collisions (e.g., set it to the embedding model name).

<Important>
  - Always set the `namespace` parameter to avoid collisions when using different embedding models.
  - `CacheBackedEmbeddings` does not cache query embeddings by default. To enable this, specify a `query_embedding_store`.
</Important>

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { CacheBackedEmbeddings } from "@langchain/classic/embeddings/cache_backed";
import { InMemoryStore } from "@langchain/core/stores";

const underlyingEmbeddings = new OpenAIEmbeddings();

const inMemoryStore = new InMemoryStore();

const cacheBackedEmbeddings = CacheBackedEmbeddings.fromBytesStore(
  underlyingEmbeddings,
  inMemoryStore,
  {
    namespace: underlyingEmbeddings.model,
  }
);

// Example: caching a query embedding
const tic = Date.now();
const queryEmbedding = cacheBackedEmbeddings.embedQuery("Hello, world!");
console.log(`First call took: ${Date.now() - tic}ms`);

// Example: caching a document embedding
const tic = Date.now();
const documentEmbedding = cacheBackedEmbeddings.embedDocuments(["Hello, world!"]);
console.log(`Cached creation time: ${Date.now() - tic}ms`);
```

In production, you would typically use a more robust persistent store, such as a database or cloud storage. Please see [stores integrations](/oss/javascript/integrations/stores/) for options.

## All integrations

<Columns>
  <Card title="Azure OpenAI" icon="link" href="/oss/javascript/integrations/embeddings/azure_openai" />

  <Card title="Baidu Qianfan" icon="link" href="/oss/javascript/integrations/embeddings/baidu_qianfan" />

  <Card title="Amazon Bedrock" icon="link" href="/oss/javascript/integrations/embeddings/bedrock" />

  <Card title="Cloudflare Workers AI" icon="link" href="/oss/javascript/integrations/embeddings/cloudflare_ai" />

  <Card title="Cohere" icon="link" href="/oss/javascript/integrations/embeddings/cohere" />

  <Card title="Google Generative AI" icon="link" href="/oss/javascript/integrations/embeddings/google_generative_ai" />

  <Card title="Google Vertex AI" icon="link" href="/oss/javascript/integrations/embeddings/google_vertex_ai" />

  <Card title="MistralAI" icon="link" href="/oss/javascript/integrations/embeddings/mistralai" />

  <Card title="Mixedbread AI" icon="link" href="/oss/javascript/integrations/embeddings/mixedbread_ai" />

  <Card title="Nomic" icon="link" href="/oss/javascript/integrations/embeddings/nomic" />

  <Card title="Ollama" icon="link" href="/oss/javascript/integrations/embeddings/ollama" />

  <Card title="Oracle AI Database" icon="link" href="/oss/javascript/integrations/embeddings/oracleai" />

  <Card title="OpenAI" icon="link" href="/oss/javascript/integrations/embeddings/openai" />

  <Card title="Pinecone" icon="link" href="/oss/javascript/integrations/embeddings/pinecone" />

  <Card title="Fireworks" icon="link" href="/oss/javascript/integrations/embeddings/fireworks" />

  <Card title="IBM watsonx.ai" icon="link" href="/oss/javascript/integrations/embeddings/ibm" />

  <Card title="TogetherAI" icon="link" href="/oss/javascript/integrations/embeddings/togetherai" />
</Columns>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/javascript/integrations/embeddings/index.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# OpenAIEmbeddings integration
Source: https://docs.langchain.com/oss/javascript/integrations/embeddings/openai

Integrate with the OpenAIEmbeddings embedding model using LangChain JavaScript.

This will help you get started with OpenAIEmbeddings [embedding models](/oss/javascript/integrations/embeddings) using LangChain. For detailed documentation on `OpenAIEmbeddings` features and configuration options, please refer to the [API reference](https://reference.langchain.com/javascript/langchain-openai/OpenAIEmbeddings).

## Overview

### Integration details

| Class                                                                                              | Package                                                                | Local | [Py support](https://python.langchain.com/docs/integrations/embeddings/openai/) |                                             Downloads                                             |                                             Version                                            |
| :------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------- | :---: | :-----------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------: |
| [`OpenAIEmbeddings`](https://reference.langchain.com/javascript/langchain-openai/OpenAIEmbeddings) | [`@langchain/openai`](https://www.npmjs.com/package/@langchain/openai) |   ❌   |                                        ✅                                        | ![NPM - Downloads](https://img.shields.io/npm/dm/@langchain/openai?style=flat-square\&label=%20&) | ![NPM - Version](https://img.shields.io/npm/v/@langchain/openai?style=flat-square\&label=%20&) |

## Setup

To access OpenAIEmbeddings embedding models you'll need to create an OpenAI account, get an API key, and install the `@langchain/openai` integration package.

### Credentials

Head to [platform.openai.com](https://platform.openai.com) to sign up to OpenAI and generate an API key. Once you've done this set the `OPENAI_API_KEY` environment variable:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
export OPENAI_API_KEY="your-api-key"
```

If you want to get automated tracing of your model calls you can also set your [LangSmith](/langsmith/observability) API key by uncommenting below:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}

# export LANGSMITH_TRACING="true"

# export LANGSMITH_API_KEY="your-api-key"
```

### Installation

The LangChain OpenAIEmbeddings integration lives in the `@langchain/openai` package:

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

Now you can instantiate the embeddings model:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { OpenAIEmbeddings } from "@langchain/openai";

const embeddings = new OpenAIEmbeddings({
  apiKey: "YOUR-API-KEY", // In Node.js defaults to process.env.OPENAI_API_KEY
  batchSize: 512, // Default value if omitted is 512. Max is 2048
  model: "text-embedding-3-large",
});
```

If you're part of an organization, you can set `process.env.OPENAI_ORGANIZATION` to your OpenAI organization id, or pass it in as `organization` when
initializing the model.

## Indexing and retrieval

Embedding models are often used in retrieval-augmented generation (RAG) flows, both as part of indexing data as well as later retrieving it. For more detailed instructions, please see our RAG tutorials under the [**Learn** tab](/oss/javascript/learn/).

Below, see how to index and retrieve data using the `embeddings` object we initialized above. In this example, we will index and retrieve a sample document using the demo [`MemoryVectorStore`](/oss/javascript/integrations/vectorstores/memory).

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
// Create a vector store with a sample text
import { MemoryVectorStore } from "@langchain/classic/vectorstores/memory";

const text = "LangChain is the framework for building context-aware reasoning applications";

const vectorstore = await MemoryVectorStore.fromDocuments(
  [{ pageContent: text, metadata: {} }],
  embeddings,
);

// Use the vector store as a retriever that returns a single document
const retriever = vectorstore.asRetriever(1);

// Retrieve the most similar text
const retrievedDocuments = await retriever.invoke("What is LangChain?");

retrievedDocuments[0].pageContent;
```

```text theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
LangChain is the framework for building context-aware reasoning applications
```

## Direct usage

Under the hood, the vectorstore and retriever implementations are calling `embeddings.embedDocument(...)` and `embeddings.embedQuery(...)` to create embeddings for the text(s) used in `fromDocuments` and the retriever's `invoke` operations, respectively.

You can directly call these methods to get embeddings for your own use cases.

### Embed single texts

You can embed queries for search with `embedQuery`. This generates a vector representation specific to the query:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const singleVector = await embeddings.embedQuery(text);

console.log(singleVector.slice(0, 100));
```

```text theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
[
    -0.01927683,  0.0037708976,  -0.032942563,  0.0037671267,  0.008175306,
   -0.012511838,  -0.009713832,   0.021403614,  -0.015377721, 0.0018684798,
    0.020574018,   0.022399133,   -0.02322873,   -0.01524951,  -0.00504169,
   -0.007375876,   -0.03448109, 0.00015130726,   0.021388533, -0.012564631,
   -0.020031009,   0.027406884,  -0.039217334,    0.03036327,  0.030393435,
   -0.021750538,   0.032610722,  -0.021162277,  -0.025898525,  0.018869571,
    0.034179416,  -0.013371604,  0.0037652412,   -0.02146395, 0.0012641934,
   -0.055688616,    0.05104287,  0.0024982197,  -0.019095825, 0.0037369595,
  0.00088757504,   0.025189597,  -0.018779071,   0.024978427,  0.016833287,
  -0.0025868358,  -0.011727491, -0.0021154736,  -0.017738303, 0.0013839195,
  -0.0131151825,   -0.05405959,   0.029729757,  -0.003393808,  0.019774588,
    0.028885076,   0.004355387,   0.026094612,    0.06479911,  0.038040817,
    -0.03478276,  -0.012594799,  -0.024767255, -0.0031430433,  0.017874055,
   -0.015294761,   0.005709139,   0.025355516,   0.044798266,   0.02549127,
    -0.02524993, 0.00014553308,  -0.019427665,  -0.023545485,  0.008748483,
    0.019850006,  -0.028417485,  -0.001860938,   -0.02318348, -0.010799851,
     0.04793565, -0.0048983963,    0.02193154,  -0.026411368,  0.026426451,
   -0.012149832,   0.035355937,  -0.047814984,  -0.027165547, -0.008228099,
   -0.007737882,   0.023726488,  -0.046487626,  -0.007783133, -0.019638835,
     0.01793439,  -0.018024892,  0.0030336871,  -0.019578502, 0.0042837397
]
```

### Embed multiple texts

You can embed multiple texts for indexing with `embedDocuments`. The internals used for this method may (but do not have to) differ from embedding queries:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const text2 = "LangGraph is a library for building stateful, multi-actor applications with LLMs";

const vectors = await embeddings.embedDocuments([text, text2]);

console.log(vectors[0].slice(0, 100));
console.log(vectors[1].slice(0, 100));
```

```text theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
[
    -0.01927683,  0.0037708976,  -0.032942563,  0.0037671267,  0.008175306,
   -0.012511838,  -0.009713832,   0.021403614,  -0.015377721, 0.0018684798,
    0.020574018,   0.022399133,   -0.02322873,   -0.01524951,  -0.00504169,
   -0.007375876,   -0.03448109, 0.00015130726,   0.021388533, -0.012564631,
   -0.020031009,   0.027406884,  -0.039217334,    0.03036327,  0.030393435,
   -0.021750538,   0.032610722,  -0.021162277,  -0.025898525,  0.018869571,
    0.034179416,  -0.013371604,  0.0037652412,   -0.02146395, 0.0012641934,
   -0.055688616,    0.05104287,  0.0024982197,  -0.019095825, 0.0037369595,
  0.00088757504,   0.025189597,  -0.018779071,   0.024978427,  0.016833287,
  -0.0025868358,  -0.011727491, -0.0021154736,  -0.017738303, 0.0013839195,
  -0.0131151825,   -0.05405959,   0.029729757,  -0.003393808,  0.019774588,
    0.028885076,   0.004355387,   0.026094612,    0.06479911,  0.038040817,
    -0.03478276,  -0.012594799,  -0.024767255, -0.0031430433,  0.017874055,
   -0.015294761,   0.005709139,   0.025355516,   0.044798266,   0.02549127,
    -0.02524993, 0.00014553308,  -0.019427665,  -0.023545485,  0.008748483,
    0.019850006,  -0.028417485,  -0.001860938,   -0.02318348, -0.010799851,
     0.04793565, -0.0048983963,    0.02193154,  -0.026411368,  0.026426451,
   -0.012149832,   0.035355937,  -0.047814984,  -0.027165547, -0.008228099,
   -0.007737882,   0.023726488,  -0.046487626,  -0.007783133, -0.019638835,
     0.01793439,  -0.018024892,  0.0030336871,  -0.019578502, 0.0042837397
]
[
   -0.010181213,   0.023419594,   -0.04215527, -0.0015320902,  -0.023573855,
  -0.0091644935,  -0.014893179,   0.019016149,  -0.023475688,  0.0010219777,
    0.009255648,    0.03996757,   -0.04366983,   -0.01640774,  -0.020194141,
    0.019408813,  -0.027977299,  -0.022017224,   0.013539891,  -0.007769135,
    0.032647192,  -0.015089511,  -0.022900717,   0.023798235,   0.026084099,
   -0.024625633,   0.035003178,  -0.017978394,  -0.049615882,   0.013364594,
    0.031132633,   0.019142363,   0.023195215,  -0.038396914,   0.005584942,
   -0.031946007,   0.053682756, -0.0036356465,   0.011240003,  0.0056690844,
  -0.0062791156,   0.044146635,  -0.037387207,    0.01300699,   0.018946031,
   0.0050415234,   0.029618073,  -0.021750772,  -0.000649473, 0.00026951815,
   -0.014710871,  -0.029814405,    0.04204308,  -0.014710871,  0.0039616977,
   -0.021512369,   0.054608323,   0.021484323,    0.02790718,  -0.010573876,
   -0.023952495,  -0.035143413,  -0.048802506, -0.0075798146,   0.023279356,
   -0.022690361,  -0.016590048,  0.0060477243,   0.014100839,   0.005476258,
   -0.017221114, -0.0100059165,  -0.017922299,  -0.021989176,    0.01830094,
     0.05516927,   0.001033372,  0.0017310516,   -0.00960624,  -0.037864015,
    0.013063084,   0.006591143,  -0.010160177,  0.0011394264,    0.04953174,
    0.004806626,   0.029421741,  -0.037751824,   0.003618117,   0.007162609,
    0.027696826, -0.0021070621,  -0.024485396, -0.0042141243,   -0.02801937,
   -0.019605145,   0.016281527,  -0.035143413,    0.01640774,   0.042323552
]
```

## Specifying dimensions

With the `text-embedding-3` class of models, you can specify the size of the embeddings you want returned. For example by default `text-embedding-3-large` returns embeddings of dimension 3072:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { OpenAIEmbeddings } from "@langchain/openai";

const embeddingsDefaultDimensions = new OpenAIEmbeddings({
  model: "text-embedding-3-large",
});

const vectorsDefaultDimensions = await embeddingsDefaultDimensions.embedDocuments(["some text"]);
console.log(vectorsDefaultDimensions[0].length);
```

```text theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
3072
```

By passing in `dimensions: 1024` we can reduce the size of our embeddings to 1024:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { OpenAIEmbeddings } from "@langchain/openai";

const embeddings1024 = new OpenAIEmbeddings({
  model: "text-embedding-3-large",
  dimensions: 1024,
});

const vectors1024 = await embeddings1024.embedDocuments(["some text"]);
console.log(vectors1024[0].length);
```

```text theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
1024
```

## Custom URLs

You can customize the base URL the SDK sends requests to by passing a `configuration` parameter like this:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { OpenAIEmbeddings } from "@langchain/openai";

const model = new OpenAIEmbeddings({
  configuration: {
    baseURL: "https://your_custom_url.com",
  },
});
```

You can also pass other `ClientOptions` parameters accepted by the official SDK.

If you are hosting on Azure OpenAI, see the [dedicated page instead](/oss/javascript/integrations/embeddings/azure_openai).

***

## API reference

For detailed documentation of all `OpenAIEmbeddings` features and configurations head to the [API reference](https://reference.langchain.com/javascript/langchain-openai/OpenAIEmbeddings).

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/javascript/integrations/embeddings/openai.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Cache integrations
Source: https://docs.langchain.com/oss/javascript/integrations/llm_caching/index

Integrate with caches using LangChain JavaScript.

[Caching LLM calls](/oss/javascript/langchain/models#prompt-caching) can be useful for testing, cost savings, and speed.

Below are some integrations that allow you to cache results of individual LLM calls using different caches with different strategies.

<Columns>
  <Card title="Azure Cosmos DB NoSQL Semantic Cache" icon="link" href="/oss/javascript/integrations/llm_caching/azure_cosmosdb_nosql" />
</Columns>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/javascript/integrations/llm_caching/index.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# LLM integrations
Source: https://docs.langchain.com/oss/javascript/integrations/llms/index

Integrate with LLMs using LangChain JavaScript.

<Warning>
  **You are currently on a page documenting the use of text completion models. Many of the latest and most popular models are [chat completion models](/oss/javascript/langchain/models).**

  Unless you are specifically using more advanced prompting techniques, you are probably looking for [this page instead](/oss/javascript/integrations/chat/).
</Warning>

[LLMs](/oss/javascript/langchain/models) are language models that takes a string as input and return a string as output.

## All LLMs

<Columns>
  <Card title="Azure OpenAI" icon="link" href="/oss/javascript/integrations/llms/azure" />

  <Card title="Cloudflare Workers AI" icon="link" href="/oss/javascript/integrations/llms/cloudflare_workersai" />

  <Card title="Cohere" icon="link" href="/oss/javascript/integrations/llms/cohere" />

  <Card title="Google Vertex AI" icon="link" href="/oss/javascript/integrations/llms/google_vertex_ai" />

  <Card title="JigsawStack Prompt Engine" icon="link" href="/oss/javascript/integrations/llms/jigsawstack" />

  <Card title="MistralAI" icon="link" href="/oss/javascript/integrations/llms/mistral" />

  <Card title="Ollama" icon="link" href="/oss/javascript/integrations/llms/ollama" />

  <Card title="OpenAI" icon="link" href="/oss/javascript/integrations/llms/openai" />

  <Card title="Fireworks" icon="link" href="/oss/javascript/integrations/llms/fireworks" />

  <Card title="IBM watsonx.ai" icon="link" href="/oss/javascript/integrations/llms/ibm" />

  <Card title="Together AI" icon="link" href="/oss/javascript/integrations/llms/together" />
</Columns>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/javascript/integrations/llms/index.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Middleware integrations
Source: https://docs.langchain.com/oss/javascript/integrations/middleware/index

Integrate with middleware using LangChain JavaScript.

Browse available middleware for different providers or contribute your own to the ecosystem. Learn more about how middleware works in the [middleware overview](/oss/javascript/langchain/middleware/overview) and how to use middleware with Deep Agents in the [Deep Agents docs](/oss/javascript/deepagents/customization#middleware).

## Share your middleware

Middleware enables context engineering, harness customization, and runtime safety controls. It is a useful extension point in LangChain and we love highlighting what the community builds with it:

<CardGroup>
  <Card title="Add an official integration" icon="package" href="/oss/javascript/contributing/implement-langchain#middleware">
    Follow the contributing guide to build and publish a middleware package.
  </Card>

  <Card title="Share a community middleware" icon="users" href="https://github.com/langchain-ai/docs">
    Open a PR to the docs repo to add your middleware to the table below.
  </Card>
</CardGroup>

## Official integrations

| Provider                                                       | Middleware available |
| -------------------------------------------------------------- | -------------------- |
| [Anthropic](/oss/javascript/integrations/middleware/anthropic) | Prompt caching       |

## Community integrations

<Warning>
  Community middleware is user-contributed and unverified. LangChain does not review or endorse these integrations; use them at your own risk.
</Warning>

| Middleware                                                                            | Description                                                                                                                                              | Source                                                                                                  |
| ------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| [langchain-task-steering](https://github.com/edvinhallvaxhiu/langchain-task-steering) | Implicit state-machine middleware for ordered task pipelines with per-task tool scoping, dynamic prompt injection, and composable completion validation. | [`edvinhallvaxhiu/langchain-task-steering`](https://github.com/edvinhallvaxhiu/langchain-task-steering) |

Have a middleware to share? [Open a PR](https://github.com/langchain-ai/docs) to add it here.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/javascript/integrations/middleware/index.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
