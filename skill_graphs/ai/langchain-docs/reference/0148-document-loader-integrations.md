# Document loader integrations
Source: https://docs.langchain.com/oss/javascript/integrations/document_loaders/index

Integrate with document loaders using LangChain JavaScript.

Document loaders provide a **standard interface** for reading data from different sources (such as Slack, Notion, or Google Drive) into LangChain's [Document](https://reference.langchain.com/javascript/langchain-core/documents/Document) format.
This ensures that data can be handled consistently regardless of the source.

All document loaders implement the [BaseLoader](https://reference.langchain.com/javascript/classes/_langchain_core.document_loaders_base.BaseDocumentLoader.html) interface.

<Warning>
  Community document loaders are user-contributed and unverified. LangChain does not review or endorse these integrations; use them at your own risk.
</Warning>

## Interface

Each document loader may define its own parameters, but they share a common API:

* `load()`: Loads all documents at once.
* `loadAndSplit()`: Loads all documents at once and splits them into smaller documents.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { OracleDocLoader } from "@oracle/langchain-oracledb";

const loader = new OracleDocLoader(,
  ...  // <-- Integration specific parameters here
);
const data = await loader.load();
```

## By category

LangChain.js categorizes document loaders in two different ways:

* [File loaders](/oss/javascript/integrations/document_loaders/file_loaders/), which load data into LangChain formats from your local filesystem.
* [Web loaders](/oss/javascript/integrations/document_loaders/web_loaders/), which load data from remote sources.

### File loaders

<Info>
  If you'd like to contribute an integration, see [Contributing integrations](/oss/javascript/contributing#add-a-new-integration).
</Info>

#### Common file types

| Document Loader                                                                           | Description                                                 | Package/API |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------- | ----------- |
| [`DirectoryLoader`](/oss/javascript/integrations/document_loaders/file_loaders/directory) | Load all files from a directory with custom loader mappings | Package     |
| [JSON](/oss/javascript/integrations/document_loaders/file_loaders/json)                   | Load JSON files using JSON pointer to target specific keys  | Package     |
| [`JSONLines`](/oss/javascript/integrations/document_loaders/file_loaders/jsonlines)       | Load data from JSONLines/JSONL files                        | Package     |
| [`Text`](/oss/javascript/integrations/document_loaders/file_loaders/text)                 | Load plain text files                                       | Package     |

#### Specialized file loaders

| Document Loader                                                                            | Description                                                          | Package/API |
| ------------------------------------------------------------------------------------------ | -------------------------------------------------------------------- | ----------- |
| [`MultiFileLoader`](/oss/javascript/integrations/document_loaders/file_loaders/multi_file) | Load data from multiple individual file paths                        | Package     |
| [`OracleDocLoader`](/oss/javascript/integrations/document_loaders/file_loaders/oracleai)   | Ingest Oracle AI Vector Search tables or Oracle Text-supported files | Package     |

### Web loaders

#### Cloud providers

| Document Loader                                                                                                 | Description                                        | Web Support | Package/API |
| --------------------------------------------------------------------------------------------------------------- | -------------------------------------------------- | :---------: | ----------- |
| [Google Cloud SQL for PostgreSQL](/oss/javascript/integrations/document_loaders/web_loaders/google_cloudsql_pg) | Load documents from Cloud SQL PostgreSQL databases |      ✅      | Package     |

#### Audio & video

| Document Loader                                                              | Description                                                                    | Web Support | Package/API |
| ---------------------------------------------------------------------------- | ------------------------------------------------------------------------------ | :---------: | ----------- |
| [`Soniox`](/oss/javascript/integrations/document_loaders/web_loaders/soniox) | Transcribe multilingual audio files with optional translation using Soniox API |      ✅      | API         |

#### Other

| Document Loader                                                                    | Description                             | Web Support | Package/API |
| ---------------------------------------------------------------------------------- | --------------------------------------- | :---------: | ----------- |
| [`LangSmith`](/oss/javascript/integrations/document_loaders/web_loaders/langsmith) | Load datasets and traces from LangSmith |      ✅      | API         |

## All document loaders

<Columns>
  <Card title="DirectoryLoader" icon="link" href="/oss/javascript/integrations/document_loaders/file_loaders/directory" />

  <Card title="Google Cloud SQL for PostgreSQL" icon="link" href="/oss/javascript/integrations/document_loaders/web_loaders/google_cloudsql_pg" />

  <Card title="JSON" icon="link" href="/oss/javascript/integrations/document_loaders/file_loaders/json" />

  <Card title="JSONLines" icon="link" href="/oss/javascript/integrations/document_loaders/file_loaders/jsonlines" />

  <Card title="LangSmith" icon="link" href="/oss/javascript/integrations/document_loaders/web_loaders/langsmith" />

  <Card title="MultiFileLoader" icon="link" href="/oss/javascript/integrations/document_loaders/file_loaders/multi_file" />

  <Card title="OracleDocLoader" icon="link" href="/oss/javascript/integrations/document_loaders/file_loaders/oracleai" />

  <Card title="Soniox" icon="link" href="/oss/javascript/integrations/document_loaders/web_loaders/soniox" />

  <Card title="Text" icon="link" href="/oss/javascript/integrations/document_loaders/file_loaders/text" />
</Columns>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/javascript/integrations/document_loaders/index.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Document transformer integrations
Source: https://docs.langchain.com/oss/javascript/integrations/document_transformers/index

Integrate with document transformers using LangChain JavaScript.

<Columns>
  <Card title="OpenAI functions metadata tagger" icon="link" href="/oss/javascript/integrations/document_transformers/openai_metadata_tagger" />
</Columns>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/javascript/integrations/document_transformers/index.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# AzureOpenAIEmbeddings integration
Source: https://docs.langchain.com/oss/javascript/integrations/embeddings/azure_openai

Integrate with the AzureOpenAIEmbeddings embedding model using LangChain JavaScript.

[Azure OpenAI](https://azure.microsoft.com/products/ai-services/openai-service/) is a cloud service to help you quickly develop generative AI experiences with a diverse set of prebuilt and curated models from OpenAI, Meta and beyond.

LangChain.js supports integration with [Azure OpenAI](https://azure.microsoft.com/products/ai-services/openai-service/) using the new Azure integration in the [OpenAI SDK](https://github.com/openai/openai-node).

You can learn more about Azure OpenAI and its difference with the OpenAI API on [this page](https://learn.microsoft.com/azure/ai-services/openai/overview). If you don't have an Azure account, you can [create a free account](https://azure.microsoft.com/free/) to get started.

This will help you get started with AzureOpenAIEmbeddings [embedding models](/oss/javascript/integrations/embeddings) using LangChain. For detailed documentation on `AzureOpenAIEmbeddings` features and configuration options, please refer to the [API reference](https://reference.langchain.com/javascript/langchain-openai/AzureOpenAIEmbeddings).

<Info>
  **Previously, LangChain.js supported integration with Azure OpenAI using the dedicated [Azure OpenAI SDK](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/openai/openai). This SDK is now deprecated in favor of the new Azure integration in the OpenAI SDK, which allows to access the latest OpenAI models and features the same day they are released, and allows seamless transition between the OpenAI API and Azure OpenAI.**

  If you are using Azure OpenAI with the deprecated SDK, see the [migration guide](#migration-from-azure-openai-sdk) to update to the new API.
</Info>

## Overview

### Integration details

| Class                                                                                                        | Package                                                                | Local | [Py support](https://python.langchain.com/docs/integrations/embeddings/azure_openai/) |                                             Downloads                                             |                                             Version                                            |
| :----------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------- | :---: | :-----------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------: |
| [`AzureOpenAIEmbeddings`](https://reference.langchain.com/javascript/langchain-openai/AzureOpenAIEmbeddings) | [`@langchain/openai`](https://www.npmjs.com/package/@langchain/openai) |   ❌   |                                           ✅                                           | ![NPM - Downloads](https://img.shields.io/npm/dm/@langchain/openai?style=flat-square\&label=%20&) | ![NPM - Version](https://img.shields.io/npm/v/@langchain/openai?style=flat-square\&label=%20&) |

## Setup

To access Azure OpenAI embedding models you'll need to create an Azure account, get an API key, and install the `@langchain/openai` integration package.

### Credentials

You'll need to have an Azure OpenAI instance deployed. You can deploy a version on Azure Portal following [this guide](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal).

Once you have your instance running, make sure you have the name of your instance and key. You can find the key in the Azure Portal, under the "Keys and Endpoint" section of your instance.

If you're using Node.js, you can define the following environment variables to use the service:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
AZURE_OPENAI_API_INSTANCE_NAME=<YOUR_INSTANCE_NAME>
AZURE_OPENAI_API_EMBEDDINGS_DEPLOYMENT_NAME=<YOUR_EMBEDDINGS_DEPLOYMENT_NAME>
AZURE_OPENAI_API_KEY=<YOUR_KEY>
AZURE_OPENAI_API_VERSION="2024-02-01"
```

If you want to get automated tracing of your model calls you can also set your [LangSmith](/langsmith/observability) API key by uncommenting below:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}

# export LANGSMITH_TRACING="true"

# export LANGSMITH_API_KEY="your-api-key"
```

### Installation

The LangChain AzureOpenAIEmbeddings integration lives in the `@langchain/openai` package:

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

<Info>
  **You can find the list of supported API versions in the [Azure OpenAI documentation](https://learn.microsoft.com/azure/ai-services/openai/reference).**
</Info>

<Tip>
  **If `AZURE_OPENAI_API_EMBEDDINGS_DEPLOYMENT_NAME` is not defined, it will fall back to the value of `AZURE_OPENAI_API_DEPLOYMENT_NAME` for the deployment name. The same applies to the `azureOpenAIApiEmbeddingsDeploymentName` parameter in the `AzureOpenAIEmbeddings` constructor, which will fall back to the value of `azureOpenAIApiDeploymentName` if not defined.**
</Tip>

## Instantiation

Now we can instantiate our model object and embed text:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { AzureOpenAIEmbeddings } from "@langchain/openai";

const embeddings = new AzureOpenAIEmbeddings({
  azureOpenAIApiKey: "<your_key>", // In Node.js defaults to process.env.AZURE_OPENAI_API_KEY
  azureOpenAIApiInstanceName: "<your_instance_name>", // In Node.js defaults to process.env.AZURE_OPENAI_API_INSTANCE_NAME
  azureOpenAIApiEmbeddingsDeploymentName: "<your_embeddings_deployment_name>", // In Node.js defaults to process.env.AZURE_OPENAI_API_EMBEDDINGS_DEPLOYMENT_NAME
  azureOpenAIApiVersion: "<api_version>", // In Node.js defaults to process.env.AZURE_OPENAI_API_VERSION
  maxRetries: 1,
});
```

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
   -0.024253517, -0.0054218727,   0.048715446,   0.020580322,    0.03180832,
   0.0028770117,  -0.012367731,   0.037383243,  -0.054915592,   0.032225136,
     0.00825818,  -0.023888804,   -0.01184671,   0.012257014,   0.016294925,
    0.009254632,  0.0051353113,  -0.008889917,   0.016855022,    0.04207243,
  0.00082589936,  -0.011664353,    0.00818654,   0.029020859,  -0.012335167,
   -0.019603407,  0.0013945447,    0.05538451,  -0.011625277,  -0.008153976,
    0.038607642,   -0.03811267, -0.0074440846,   0.047647353,   -0.00927417,
    0.024201415, -0.0069230637,  -0.008538228,   0.003910912,   0.052805457,
   -0.023159374,  0.0014352495,  -0.038659744,   0.017141584,   0.005587948,
    0.007971618,  -0.016920151,    0.06658646, -0.0016916894,   0.045667473,
   -0.042202685,   -0.03983204,   -0.04160351,  -0.011729481,  -0.055905532,
    0.012543576,  0.0038848612,   0.007919516,   0.010915386,  0.0033117384,
   -0.007548289,  -0.030427614,  -0.041890074,   0.036002535,  -0.023771575,
   -0.008792226,  -0.049444873,   0.016490309, -0.0060568666,   0.040196754,
    0.014106638,  -0.014575557, -0.0017356506,  -0.011234511,  -0.012517525,
    0.008362384,    0.01253055,   0.036158845,   0.008297256, -0.0010908874,
   -0.014888169,  -0.020489143,   0.018965157,  -0.057937514, -0.0037122732,
    0.004402626,   -0.00840146,   0.042984217,   -0.04936672,   -0.03714878,
    0.004969236,    0.03707063,   0.015396165,   -0.02055427,    0.01988997,
    0.030219207,  -0.021257648,    0.01340326,   0.003692735,   0.012595678
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
   -0.024253517, -0.0054218727,   0.048715446,   0.020580322,    0.03180832,
   0.0028770117,  -0.012367731,   0.037383243,  -0.054915592,   0.032225136,
     0.00825818,  -0.023888804,   -0.01184671,   0.012257014,   0.016294925,
    0.009254632,  0.0051353113,  -0.008889917,   0.016855022,    0.04207243,
  0.00082589936,  -0.011664353,    0.00818654,   0.029020859,  -0.012335167,
   -0.019603407,  0.0013945447,    0.05538451,  -0.011625277,  -0.008153976,
    0.038607642,   -0.03811267, -0.0074440846,   0.047647353,   -0.00927417,
    0.024201415, -0.0069230637,  -0.008538228,   0.003910912,   0.052805457,
   -0.023159374,  0.0014352495,  -0.038659744,   0.017141584,   0.005587948,
    0.007971618,  -0.016920151,    0.06658646, -0.0016916894,   0.045667473,
   -0.042202685,   -0.03983204,   -0.04160351,  -0.011729481,  -0.055905532,
    0.012543576,  0.0038848612,   0.007919516,   0.010915386,  0.0033117384,
   -0.007548289,  -0.030427614,  -0.041890074,   0.036002535,  -0.023771575,
   -0.008792226,  -0.049444873,   0.016490309, -0.0060568666,   0.040196754,
    0.014106638,  -0.014575557, -0.0017356506,  -0.011234511,  -0.012517525,
    0.008362384,    0.01253055,   0.036158845,   0.008297256, -0.0010908874,
   -0.014888169,  -0.020489143,   0.018965157,  -0.057937514, -0.0037122732,
    0.004402626,   -0.00840146,   0.042984217,   -0.04936672,   -0.03714878,
    0.004969236,    0.03707063,   0.015396165,   -0.02055427,    0.01988997,
    0.030219207,  -0.021257648,    0.01340326,   0.003692735,   0.012595678
]
[
   -0.033366997,   0.010419146,  0.0118083665,  -0.040441725, 0.0020355924,
   -0.015808804,  -0.023629595, -0.0066180876,  -0.040004376,  0.020053642,
  -0.0010797002,   -0.03900105,  -0.009956073,  0.0027896944,  0.003305828,
   -0.034010153,   0.009833873,  0.0061164247,   0.022536227,  0.029147884,
    0.017789727,    0.03182342,   0.010869357,   0.031849146, -0.028093107,
    0.008283865, -0.0145610785,    0.01645196,  -0.029430874,  -0.02508313,
    0.046178687,   -0.01722375,  -0.010046115,   0.013101112, 0.0044538635,
     0.02197025,    0.03985002,   0.007955855,  0.0008819293,  0.012657333,
    0.014368132,  -0.014007963,   -0.03722594,   0.031617608, -0.011570398,
    0.039052505,  0.0020018267,   0.023706773, -0.0046950476,  0.056083307,
    -0.08412496,  -0.043425974,  -0.015512952,   0.015950298,  -0.03624834,
  -0.0053317733,  -0.037251666,  0.0046339477,    0.04193385,  0.023475237,
   -0.021378545,   0.013699248,  -0.026009277,   0.050757967,   -0.0494202,
   0.0007874656,   -0.07208506,   0.015885983,  -0.003259199,  0.015127057,
   0.0068946453,  -0.035373647,  -0.005875241, -0.0032238255,  -0.04185667,
   -0.022047428,  0.0014326327, -0.0070940237, -0.0027864785, -0.016271876,
    0.005097021,   0.034473225,   0.012361481,  -0.026498076, 0.0067274245,
   -0.026330855,  -0.006132504,   0.008180959,  -0.049368747, -0.032337945,
    0.011049441,    0.00186194,  -0.012097787,    0.01930758,   0.07059293,
    0.029713862,    0.04337452, -0.0048461896,  -0.019976463,  0.011473924
]
```

## Using Azure Managed identity

If you're using Azure Managed Identity, you can configure the credentials like this:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import {
  DefaultAzureCredential,
  getBearerTokenProvider,
} from "@azure/identity";
import { AzureOpenAIEmbeddings } from "@langchain/openai";

const credentials = new DefaultAzureCredential();
const azureADTokenProvider = getBearerTokenProvider(
  credentials,
  "https://cognitiveservices.azure.com/.default"
);

const modelWithManagedIdentity = new AzureOpenAIEmbeddings({
  azureADTokenProvider,
  azureOpenAIApiInstanceName: "<your_instance_name>",
  azureOpenAIApiEmbeddingsDeploymentName: "<your_embeddings_deployment_name>",
  azureOpenAIApiVersion: "<api_version>",
});

```

## Using a different domain

If your instance is hosted under a domain other than the default `openai.azure.com`, you'll need to use the alternate `AZURE_OPENAI_BASE_PATH` environment variable.
For example, here's how you would connect to the domain `https://westeurope.api.microsoft.com/openai/deployments/{DEPLOYMENT_NAME}`:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { AzureOpenAIEmbeddings } from "@langchain/openai";

const embeddingsDifferentDomain = new AzureOpenAIEmbeddings({
  azureOpenAIApiKey: "<your_key>", // In Node.js defaults to process.env.AZURE_OPENAI_API_KEY
  azureOpenAIApiEmbeddingsDeploymentName: "<your_embedding_deployment_name>", // In Node.js defaults to process.env.AZURE_OPENAI_API_EMBEDDINGS_DEPLOYMENT_NAME
  azureOpenAIApiVersion: "<api_version>", // In Node.js defaults to process.env.AZURE_OPENAI_API_VERSION
  azureOpenAIBasePath:
    "https://westeurope.api.microsoft.com/openai/deployments", // In Node.js defaults to process.env.AZURE_OPENAI_BASE_PATH
});

```

## Custom headers

You can specify custom headers by passing in a `configuration` field:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { AzureOpenAIEmbeddings } from "@langchain/openai";

const embeddingsWithCustomHeaders = new AzureOpenAIEmbeddings({
  azureOpenAIApiKey: "<your_key>",
  azureOpenAIApiInstanceName: "<your_instance_name>",
  azureOpenAIApiEmbeddingsDeploymentName: "<your_embeddings_deployment_name>",
  azureOpenAIApiVersion: "<api_version>",
  configuration: {
    defaultHeaders: {
      "x-custom-header": `SOME_VALUE`,
    },
  },
});
```

The `configuration` field also accepts other `ClientOptions` parameters accepted by the official SDK.

**Note:** The specific header `api-key` currently cannot be overridden in this manner and will pass through the value from `azureOpenAIApiKey`.

## Migration from Azure OpenAI SDK

If you are using the deprecated Azure OpenAI SDK with the `@langchain/azure-openai` package, you can update your code to use the new Azure integration following these steps:

1. Install the new `@langchain/openai` package and remove the previous `@langchain/azure-openai` package:

   ```bash npm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
   npm install @langchain/openai
   npm uninstall @langchain/azure-openai
   ```

2. Update your imports to use the new `AzureOpenAIEmbeddings` class from the `@langchain/openai` package:

   ```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
   import { AzureOpenAIEmbeddings } from "@langchain/openai";
   ```

3. Update your code to use the new `AzureOpenAIEmbeddings` class and pass the required parameters:

   ```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
   const model = new AzureOpenAIEmbeddings({
     azureOpenAIApiKey: "<your_key>",
     azureOpenAIApiInstanceName: "<your_instance_name>",
     azureOpenAIApiEmbeddingsDeploymentName:
       "<your_embeddings_deployment_name>",
     azureOpenAIApiVersion: "<api_version>",
   });
   ```

   Notice that the constructor now requires the `azureOpenAIApiInstanceName` parameter instead of the `azureOpenAIEndpoint` parameter, and adds the `azureOpenAIApiVersion` parameter to specify the API version.

   * If you were using Azure Managed Identity, you now need to use the `azureADTokenProvider` parameter to the constructor instead of `credentials`, see the [Azure Managed Identity](#using-azure-managed-identity) section for more details.

   * If you were using environment variables, you now have to set the `AZURE_OPENAI_API_INSTANCE_NAME` environment variable instead of `AZURE_OPENAI_API_ENDPOINT`, and add the `AZURE_OPENAI_API_VERSION` environment variable to specify the API version.

***

## API reference

For detailed documentation of all `AzureOpenAIEmbeddings` features and configurations head to the [API reference](https://reference.langchain.com/javascript/langchain-openai/AzureOpenAIEmbeddings).

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/javascript/integrations/embeddings/azure_openai.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# BedrockEmbeddings integration
Source: https://docs.langchain.com/oss/javascript/integrations/embeddings/bedrock

Integrate with the BedrockEmbeddings embedding model using LangChain JavaScript.

[Amazon Bedrock](https://aws.amazon.com/bedrock/) is a fully managed service that offers a choice of high-performing foundation models (FMs) from leading AI companies like AI21 Labs, Anthropic, Cohere, Meta, Stability AI, and Amazon via a single API, along with a broad set of capabilities you need to build generative AI applications with security, privacy, and responsible AI.

This will help you get started with Amazon Bedrock [embedding models](/oss/javascript/integrations/embeddings) using LangChain. For detailed documentation on `Bedrock` features and configuration options, please refer to the [API reference](https://reference.langchain.com/javascript/langchain-aws/BedrockEmbeddings).

## Overview

### Integration details

| Class                                                                                   | Package                                                          | Local | [Py support](https://python.langchain.com/docs/integrations/embeddings/bedrock/) |                                            Downloads                                           |                                           Version                                           |
| :-------------------------------------------------------------------------------------- | :--------------------------------------------------------------- | :---: | :------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------: |
| [`Bedrock`](https://reference.langchain.com/javascript/langchain-aws/BedrockEmbeddings) | [`@langchain/aws`](https://www.npmjs.com/package/@langchain/aws) |   ❌   |                                         ✅                                        | ![NPM - Downloads](https://img.shields.io/npm/dm/@langchain/aws?style=flat-square\&label=%20&) | ![NPM - Version](https://img.shields.io/npm/v/@langchain/aws?style=flat-square\&label=%20&) |

## Setup

To access Bedrock embedding models you'll need to create an AWS account, get an API key, and install the `@langchain/aws` integration package.

Head to the [AWS docs](https://docs.aws.amazon.com/bedrock/latest/userguide/getting-started.html) to sign up for AWS and setup your credentials. You'll also need to turn on model access for your account, which you can do by [following these instructions](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html).

### Credentials

If you want to get automated tracing of your model calls you can also set your [LangSmith](/langsmith/observability) API key by uncommenting below:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}

# export LANGSMITH_TRACING="true"

# export LANGSMITH_API_KEY="your-api-key"
```

### Installation

The LangChain Bedrock integration lives in the `@langchain/aws` package:

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

Now we can instantiate our model object and embed text.

There are a few different ways to authenticate with AWS - the below examples rely on an access key, secret access key and region set in your environment variables:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { BedrockEmbeddings } from "@langchain/aws";

const embeddings = new BedrockEmbeddings({
  region: process.env.BEDROCK_AWS_REGION!,
  credentials: {
    accessKeyId: process.env.BEDROCK_AWS_ACCESS_KEY_ID!,
    secretAccessKey: process.env.BEDROCK_AWS_SECRET_ACCESS_KEY!,
  },
  model: "amazon.titan-embed-text-v1",
});
```

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
         0.625,  0.111328125,      0.265625,   -0.20019531,  0.40820312,
  -0.010803223,  -0.22460938, -0.0002937317,    0.29882812, -0.14355469,
  -0.068847656,   -0.3984375,          0.75,    -0.1953125,  -0.5546875,
  -0.087402344,       0.5625,      1.390625,    -0.3515625,  0.39257812,
  -0.061767578,      0.65625,   -0.36328125,   -0.06591797,    0.234375,
   -0.36132812,   0.42382812,  -0.115234375,   -0.28710938, -0.29296875,
     -0.765625,  -0.16894531,    0.23046875,     0.6328125, -0.08544922,
    0.13671875, 0.0004272461,        0.3125,    0.12207031,   -0.546875,
    0.14257812, -0.119628906,  -0.111328125,    0.61328125,      0.6875,
     0.3671875,   -0.2578125,   -0.27734375,      0.703125,    0.203125,
    0.17675781,  -0.26757812,   -0.76171875,    0.71484375,  0.77734375,
    -0.1953125, -0.007232666,  -0.044921875,    0.23632812, -0.24121094,
  -0.012207031,    0.5078125,    0.08984375,    0.56640625,  -0.3046875,
     0.6484375,        -0.25,   -0.37890625,    -0.2421875,  0.38476562,
   -0.18164062,  -0.05810547,     0.7578125,    0.04296875,    0.609375,
    0.50390625,  0.023803711,   -0.23046875,   0.099121094,  0.79296875,
     -1.296875,     0.671875,   -0.66796875,    0.43359375, 0.087890625,
    0.14550781,  -0.37304688,  -0.068359375, 0.00012874603, -0.47265625,
     -0.765625,   0.07861328,  -0.029663086,   0.076660156, -0.32617188,
     -0.453125,   -0.5546875,   -0.45703125,     1.1015625, -0.29492188
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
         0.625,  0.111328125,      0.265625,   -0.20019531,  0.40820312,
  -0.010803223,  -0.22460938, -0.0002937317,    0.29882812, -0.14355469,
  -0.068847656,   -0.3984375,          0.75,    -0.1953125,  -0.5546875,
  -0.087402344,       0.5625,      1.390625,    -0.3515625,  0.39257812,
  -0.061767578,      0.65625,   -0.36328125,   -0.06591797,    0.234375,
   -0.36132812,   0.42382812,  -0.115234375,   -0.28710938, -0.29296875,
     -0.765625,  -0.16894531,    0.23046875,     0.6328125, -0.08544922,
    0.13671875, 0.0004272461,        0.3125,    0.12207031,   -0.546875,
    0.14257812, -0.119628906,  -0.111328125,    0.61328125,      0.6875,
     0.3671875,   -0.2578125,   -0.27734375,      0.703125,    0.203125,
    0.17675781,  -0.26757812,   -0.76171875,    0.71484375,  0.77734375,
    -0.1953125, -0.007232666,  -0.044921875,    0.23632812, -0.24121094,
  -0.012207031,    0.5078125,    0.08984375,    0.56640625,  -0.3046875,
     0.6484375,        -0.25,   -0.37890625,    -0.2421875,  0.38476562,
   -0.18164062,  -0.05810547,     0.7578125,    0.04296875,    0.609375,
    0.50390625,  0.023803711,   -0.23046875,   0.099121094,  0.79296875,
     -1.296875,     0.671875,   -0.66796875,    0.43359375, 0.087890625,
    0.14550781,  -0.37304688,  -0.068359375, 0.00012874603, -0.47265625,
     -0.765625,   0.07861328,  -0.029663086,   0.076660156, -0.32617188,
     -0.453125,   -0.5546875,   -0.45703125,     1.1015625, -0.29492188
]
[
       0.65625,    0.48242188,    0.70703125,   -0.13378906,    0.859375,
     0.2578125,   -0.13378906, -0.0002670288,      -0.34375,  0.25585938,
   -0.33984375,   -0.26367188,      0.828125,   -0.23242188, -0.61328125,
    0.12695312,    0.43359375,     1.3828125,  -0.099121094,   0.3203125,
   -0.34765625,    0.35351562,   -0.28710938,   0.009521484, 0.083496094,
   0.040283203,   -0.25390625,    0.17871094,   0.044189453, -0.19628906,
    0.45898438,    0.21191406,    0.67578125,     0.8359375, -0.29101562,
   0.021118164,    0.13671875,   0.083984375,    0.34570312,  0.30859375,
  -0.001625061,    0.31835938,   -0.18164062, -0.0058288574,  0.22460938,
    0.26757812,   -0.09082031,    0.17480469,     1.4921875, -0.24316406,
    0.36523438,    0.14550781,     -0.609375,    0.33007812,  0.10595703,
     0.3671875,    0.18359375,   -0.62109375,    0.51171875, 0.024047852,
   0.092285156,   -0.44335938,     0.4921875,      0.609375, -0.48242188,
      0.796875,   -0.47851562,      -0.53125,   -0.66796875,  0.68359375,
   -0.16796875,   0.110839844,    0.84765625,      0.703125,   0.8671875,
    0.37695312, -0.0022888184,   -0.30664062,     0.3671875,  0.16503906,
   -0.59765625,     0.3203125,      -0.34375,    0.08251953,    0.890625,
    0.38476562,   -0.24707031,        -0.125, 0.00013160706, -0.69921875,
      -0.53125,   0.052490234,    0.27734375,    0.42773438, -0.38867188,
    -0.2578125,         -0.25,      -0.46875,      0.828125, -0.94140625
]
```

## Configuring the Bedrock runtime client

You can pass in your own instance of the `BedrockRuntimeClient` if you want to customize options like
`credentials`, `region`, `retryPolicy`, etc.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { BedrockRuntimeClient } from "@aws-sdk/client-bedrock-runtime";
import { BedrockEmbeddings } from "@langchain/aws";

const getCredentials = () => {
  // do something to get credentials
}

// @lc-ts-ignore
const client = new BedrockRuntimeClient({
  region: "us-east-1",
  credentials: getCredentials(),
});

const embeddingsWithCustomClient = new BedrockEmbeddings({
  client,
});
```

***

## API reference

For detailed documentation of all Bedrock features and configurations head to the [API reference](https://reference.langchain.com/javascript/langchain-aws/BedrockEmbeddings).

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/javascript/integrations/embeddings/bedrock.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
