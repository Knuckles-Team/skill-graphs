# Ollama integrations
Source: https://docs.langchain.com/oss/python/integrations/providers/ollama

Integrate with Ollama using LangChain Python.

This page covers all LangChain integrations with [Ollama](https://ollama.com/).

Ollama allows you to run open-source models (like [`gpt-oss`](https://ollama.com/library/gpt-oss)) locally.

For a complete list of supported models and variants, see the [Ollama model library](https://ollama.ai/library).

## Model interfaces

<Columns>
  <Card title="ChatOllama" href="/oss/python/integrations/chat/ollama" icon="message">
    Ollama chat models.
  </Card>

  <Card title="OllamaEmbeddings" href="/oss/python/integrations/embeddings/ollama" icon="message">
    Ollama embedding models.
  </Card>
</Columns>

## Other

<Columns>
  <Card title="OllamaLLM" href="/oss/python/integrations/llms/ollama" icon="cursor-text">
    (Legacy) Ollama text completion models.
  </Card>
</Columns>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/providers/ollama.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# OpenAI integrations
Source: https://docs.langchain.com/oss/python/integrations/providers/openai

Integrate with OpenAI using LangChain Python.

This page covers all LangChain integrations with [OpenAI](https://en.wikipedia.org/wiki/OpenAI)

## Model interfaces

<Columns>
  <Card title="ChatOpenAI" href="/oss/python/integrations/chat/openai" icon="message">
    OpenAI chat models.
  </Card>

  <Card title="AzureChatOpenAI" href="/oss/python/integrations/chat/azure_chat_openai" icon="brand-windows">
    Azure OpenAI chat models with enterprise features.
  </Card>

  <Card title="OpenAIEmbeddings" href="/oss/python/integrations/embeddings/openai" icon="stack-2">
    OpenAI embedding models.
  </Card>

  <Card title="AzureOpenAIEmbeddings" href="/oss/python/integrations/embeddings/azure_openai" icon="brand-windows">
    Azure OpenAI embedding models with enterprise features.
  </Card>
</Columns>

## Other

<Columns>
  <Card title="OpenAI" href="/oss/python/integrations/llms/openai" icon="cursor-text">
    (Legacy) OpenAI text completion models.
  </Card>

  <Card title="AzureOpenAI" href="/oss/python/integrations/llms/azure_openai" icon="brand-windows">
    Wrapper for (legacy) OpenAI text completion models hosted on Azure.
  </Card>

  <Card title="OpenAIModerationChain" href="https://python.langchain.com/v0.1/docs/guides/productionization/safety/moderation" icon="link">
    Detect text that could be hateful, violent, etc.
  </Card>
</Columns>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/providers/openai.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# LangChain Python integrations
Source: https://docs.langchain.com/oss/python/integrations/providers/overview

Integrate with providers using LangChain Python.

LangChain offers an extensive ecosystem with 1000+ integrations across chat & embedding models, tools & toolkits, document loaders, vector stores, and more.

A **provider** is a company or platform that hosts AI models and exposes them through an API (e.g., OpenAI, Anthropic, Google). Many providers have a dedicated `langchain-<provider>` package that implements one or more of LangChain's standard interfaces—chat models, embedding models, vector stores, and more—giving you a consistent API regardless of the underlying provider. Install the package, pick a model name, and swap providers without changing your code.

<Columns>
  <Card title="Chat models" icon="message" href="/oss/python/integrations/chat" />

  <Card title="Embedding models" icon="layers-difference" href="/oss/python/integrations/embeddings" />

  <Card title="Tools and toolkits" icon="tool" href="/oss/python/integrations/tools" />

  <Card title="Middleware" icon="arrows-shuffle" href="/oss/python/integrations/middleware" />

  <Card title="Checkpointers" icon="database" href="/oss/python/integrations/checkpointers" />

  <Card title="Sandboxes" icon="cube" href="/oss/python/integrations/sandboxes" />
</Columns>

To see a full list of integrations by component type, refer to the categories in the sidebar.

<Tip>
  For a conceptual overview of how providers and models work in LangChain, including how to find model names, use new models immediately, and work with routers—see [Providers and models](/oss/python/concepts/providers-and-models).
</Tip>

## Popular providers

| Provider                                                            | Package                                                                                                               | Downloads                                                                                               | Latest version                                                                                            | <Tooltip>JS/TS support</Tooltip>                              |
| :------------------------------------------------------------------ | :-------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------ | :-------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------ |
| [OpenAI](/oss/python/integrations/providers/openai/)                | [`langchain-openai`](https://reference.langchain.com/python/integrations/langchain_openai/)                           | <a href="https://pypi.org/project/langchain-openai/"><img alt="Downloads per month" /></a>              | <a href="https://pypi.org/project/langchain-openai/"><img alt="PyPI - Latest version" /></a>              | [✅](https://www.npmjs.com/package/@langchain/openai)          |
| [Google (Vertex AI)](/oss/python/integrations/providers/google)     | [`langchain-google-vertexai`](https://reference.langchain.com/python/integrations/langchain_google_vertexai/)         | <a href="https://pypi.org/project/langchain-google-vertexai/"><img alt="Downloads per month" /></a>     | <a href="https://pypi.org/project/langchain-google-vertexai/"><img alt="PyPI - Latest version" /></a>     | [✅](https://www.npmjs.com/package/@langchain/google-vertexai) |
| [Anthropic (Claude)](/oss/python/integrations/providers/anthropic/) | [`langchain-anthropic`](https://reference.langchain.com/python/integrations/langchain_anthropic/)                     | <a href="https://pypi.org/project/langchain-anthropic/"><img alt="Downloads per month" /></a>           | <a href="https://pypi.org/project/langchain-anthropic/"><img alt="PyPI - Latest version" /></a>           | [✅](https://www.npmjs.com/package/@langchain/anthropic)       |
| [Google (GenAI)](/oss/python/integrations/providers/google)         | [`langchain-google-genai`](https://reference.langchain.com/python/integrations/langchain_google_genai/)               | <a href="https://pypi.org/project/langchain-google-genai/"><img alt="Downloads per month" /></a>        | <a href="https://pypi.org/project/langchain-google-genai/"><img alt="PyPI - Latest version" /></a>        | [✅](https://www.npmjs.com/package/@langchain/google-genai)    |
| [AWS](/oss/python/integrations/providers/aws/)                      | [`langchain-aws`](https://reference.langchain.com/python/integrations/langchain_aws/)                                 | <a href="https://pypi.org/project/langchain-aws/"><img alt="Downloads per month" /></a>                 | <a href="https://pypi.org/project/langchain-aws/"><img alt="PyPI - Latest version" /></a>                 | [✅](https://www.npmjs.com/package/@langchain/aws)             |
| [Ollama](/oss/python/integrations/providers/ollama/)                | [`langchain-ollama`](https://reference.langchain.com/python/integrations/langchain_ollama/)                           | <a href="https://pypi.org/project/langchain-ollama/"><img alt="Downloads per month" /></a>              | <a href="https://pypi.org/project/langchain-ollama/"><img alt="PyPI - Latest version" /></a>              | [✅](https://www.npmjs.com/package/@langchain/ollama)          |
| [Databricks](/oss/python/integrations/providers/databricks/)        | [`databricks-langchain`](https://pypi.org/project/databricks-langchain/)                                              | <a href="https://pypi.org/project/databricks-langchain/"><img alt="Downloads per month" /></a>          | <a href="https://pypi.org/project/databricks-langchain/"><img alt="PyPI - Latest version" /></a>          | [✅](https://www.npmjs.com/package/@langchain/community)       |
| [Chroma](/oss/python/integrations/providers/chroma/)                | [`langchain-chroma`](https://reference.langchain.com/python/integrations/langchain_chroma/)                           | <a href="https://pypi.org/project/langchain-chroma/"><img alt="Downloads per month" /></a>              | <a href="https://pypi.org/project/langchain-chroma/"><img alt="PyPI - Latest version" /></a>              | [✅](https://www.npmjs.com/package/@langchain/community)       |
| [Groq](/oss/python/integrations/providers/groq/)                    | [`langchain-groq`](https://reference.langchain.com/python/integrations/langchain_groq/)                               | <a href="https://pypi.org/project/langchain-groq/"><img alt="Downloads per month" /></a>                | <a href="https://pypi.org/project/langchain-groq/"><img alt="PyPI - Latest version" /></a>                | [✅](https://www.npmjs.com/package/@langchain/groq)            |
| [Huggingface](/oss/python/integrations/providers/huggingface/)      | [`langchain-huggingface`](https://reference.langchain.com/python/integrations/langchain_huggingface/)                 | <a href="https://pypi.org/project/langchain-huggingface/"><img alt="Downloads per month" /></a>         | <a href="https://pypi.org/project/langchain-huggingface/"><img alt="PyPI - Latest version" /></a>         | [✅](https://www.npmjs.com/package/@langchain/community)       |
| [Azure AI](/oss/python/integrations/providers/azure_ai)             | [`langchain-azure-ai`](https://reference.langchain.com/python/integrations/langchain_azure_ai/)                       | <a href="https://pypi.org/project/langchain-azure-ai/"><img alt="Downloads per month" /></a>            | <a href="https://pypi.org/project/langchain-azure-ai/"><img alt="PyPI - Latest version" /></a>            | [✅](https://www.npmjs.com/package/@langchain/openai)          |
| [MongoDB](/oss/python/integrations/providers/mongodb_atlas)         | [`langchain-mongodb`](https://reference.langchain.com/python/integrations/langchain_mongodb/)                         | <a href="https://pypi.org/project/langchain-mongodb/"><img alt="Downloads per month" /></a>             | <a href="https://pypi.org/project/langchain-mongodb/"><img alt="PyPI - Latest version" /></a>             | [✅](https://www.npmjs.com/package/@langchain/mongodb)         |
| [LiteLLM](/oss/python/integrations/providers/litellm/)              | [`langchain-litellm`](https://reference.langchain.com/python/integrations/langchain_litellm/)                         | <a href="https://pypi.org/project/langchain-litellm/"><img alt="Downloads per month" /></a>             | <a href="https://pypi.org/project/langchain-litellm/"><img alt="PyPI - Latest version" /></a>             | N/A                                                           |
| [Fireworks](/oss/python/integrations/providers/fireworks/)          | [`langchain-fireworks`](https://reference.langchain.com/python/integrations/langchain_fireworks/)                     | <a href="https://pypi.org/project/langchain-fireworks/"><img alt="Downloads per month" /></a>           | <a href="https://pypi.org/project/langchain-fireworks/"><img alt="PyPI - Latest version" /></a>           | [✅](https://www.npmjs.com/package/@langchain/community)       |
| [MistralAI](/oss/python/integrations/providers/mistralai/)          | [`langchain-mistralai`](https://reference.langchain.com/python/integrations/langchain_mistralai/)                     | <a href="https://pypi.org/project/langchain-mistralai/"><img alt="Downloads per month" /></a>           | <a href="https://pypi.org/project/langchain-mistralai/"><img alt="PyPI - Latest version" /></a>           | [✅](https://www.npmjs.com/package/@langchain/mistralai)       |
| [Cohere](/oss/python/integrations/providers/cohere/)                | [`langchain-cohere`](https://reference.langchain.com/python/integrations/langchain_cohere/)                           | <a href="https://pypi.org/project/langchain-cohere/"><img alt="Downloads per month" /></a>              | <a href="https://pypi.org/project/langchain-cohere/"><img alt="PyPI - Latest version" /></a>              | [✅](https://www.npmjs.com/package/@langchain/cohere)          |
| [Pinecone](/oss/python/integrations/providers/pinecone/)            | [`langchain-pinecone`](https://reference.langchain.com/python/integrations/langchain_pinecone/)                       | <a href="https://pypi.org/project/langchain-pinecone/"><img alt="Downloads per month" /></a>            | <a href="https://pypi.org/project/langchain-pinecone/"><img alt="PyPI - Latest version" /></a>            | [✅](https://www.npmjs.com/package/@langchain/pinecone)        |
| [xAI (Grok)](/oss/python/integrations/providers/xai/)               | [`langchain-xai`](https://reference.langchain.com/python/integrations/langchain_xai/)                                 | <a href="https://pypi.org/project/langchain-xai/"><img alt="Downloads per month" /></a>                 | <a href="https://pypi.org/project/langchain-xai/"><img alt="PyPI - Latest version" /></a>                 | [✅](https://www.npmjs.com/package/@langchain/xai)             |
| [Nvidia AI Endpoints](/oss/python/integrations/providers/nvidia)    | [`langchain-nvidia-ai-endpoints`](https://reference.langchain.com/python/integrations/langchain_nvidia_ai_endpoints/) | <a href="https://pypi.org/project/langchain-nvidia-ai-endpoints/"><img alt="Downloads per month" /></a> | <a href="https://pypi.org/project/langchain-nvidia-ai-endpoints/"><img alt="PyPI - Latest version" /></a> | ❌                                                             |
| [Tavily](/oss/python/integrations/providers/tavily/)                | [`langchain-tavily`](https://reference.langchain.com/python/integrations/langchain_tavily/)                           | <a href="https://pypi.org/project/langchain-tavily/"><img alt="Downloads per month" /></a>              | <a href="https://pypi.org/project/langchain-tavily/"><img alt="PyPI - Latest version" /></a>              | [✅](https://www.npmjs.com/package/@langchain/tavily)          |
| [DeepSeek](/oss/python/integrations/providers/deepseek/)            | [`langchain-deepseek`](https://reference.langchain.com/python/integrations/langchain_deepseek/)                       | <a href="https://pypi.org/project/langchain-deepseek/"><img alt="Downloads per month" /></a>            | <a href="https://pypi.org/project/langchain-deepseek/"><img alt="PyPI - Latest version" /></a>            | [✅](https://www.npmjs.com/package/@langchain/deepseek)        |
| [Milvus](/oss/python/integrations/providers/milvus/)                | [`langchain-milvus`](https://reference.langchain.com/python/integrations/langchain_milvus/)                           | <a href="https://pypi.org/project/langchain-milvus/"><img alt="Downloads per month" /></a>              | <a href="https://pypi.org/project/langchain-milvus/"><img alt="PyPI - Latest version" /></a>              | [✅](https://www.npmjs.com/package/@langchain/community)       |
| [IBM](/oss/python/integrations/providers/ibm/)                      | [`langchain-ibm`](https://reference.langchain.com/python/integrations/langchain_ibm/)                                 | <a href="https://pypi.org/project/langchain-ibm/"><img alt="Downloads per month" /></a>                 | <a href="https://pypi.org/project/langchain-ibm/"><img alt="PyPI - Latest version" /></a>                 | [✅](https://www.npmjs.com/package/@langchain/ibm)             |
| [Qdrant](/oss/python/integrations/providers/qdrant/)                | [`langchain-qdrant`](https://reference.langchain.com/python/integrations/langchain_qdrant/)                           | <a href="https://pypi.org/project/langchain-qdrant/"><img alt="Downloads per month" /></a>              | <a href="https://pypi.org/project/langchain-qdrant/"><img alt="PyPI - Latest version" /></a>              | [✅](https://www.npmjs.com/package/@langchain/qdrant)          |
| [Elasticsearch](/oss/python/integrations/providers/elasticsearch/)  | [`langchain-elasticsearch`](https://reference.langchain.com/python/integrations/langchain_elasticsearch/)             | <a href="https://pypi.org/project/langchain-elasticsearch/"><img alt="Downloads per month" /></a>       | <a href="https://pypi.org/project/langchain-elasticsearch/"><img alt="PyPI - Latest version" /></a>       | [✅](https://www.npmjs.com/package/@langchain/community)       |
| [DataStax Astra DB](/oss/python/integrations/providers/astradb/)    | [`langchain-astradb`](https://reference.langchain.com/python/integrations/langchain_astradb/)                         | <a href="https://pypi.org/project/langchain-astradb/"><img alt="Downloads per month" /></a>             | <a href="https://pypi.org/project/langchain-astradb/"><img alt="PyPI - Latest version" /></a>             | [✅](https://www.npmjs.com/package/@langchain/community)       |
| [Perplexity](/oss/python/integrations/providers/perplexity/)        | [`langchain-perplexity`](https://reference.langchain.com/python/integrations/langchain_perplexity/)                   | <a href="https://pypi.org/project/langchain-perplexity/"><img alt="Downloads per month" /></a>          | <a href="https://pypi.org/project/langchain-perplexity/"><img alt="PyPI - Latest version" /></a>          | [✅](https://www.npmjs.com/package/@langchain/community)       |
| [OpenRouter](/oss/python/integrations/providers/openrouter/)        | [`langchain-openrouter`](https://reference.langchain.com/python/integrations/langchain_openrouter/)                   | <a href="https://pypi.org/project/langchain-openrouter/"><img alt="Downloads per month" /></a>          | <a href="https://pypi.org/project/langchain-openrouter/"><img alt="PyPI - Latest version" /></a>          | ❌                                                             |
| [Redis](/oss/python/integrations/providers/redis/)                  | [`langchain-redis`](https://reference.langchain.com/python/integrations/langchain_redis/)                             | <a href="https://pypi.org/project/langchain-redis/"><img alt="Downloads per month" /></a>               | <a href="https://pypi.org/project/langchain-redis/"><img alt="PyPI - Latest version" /></a>               | [✅](https://www.npmjs.com/package/@langchain/redis)           |
| [Together](/oss/python/integrations/providers/together/)            | [`langchain-together`](https://reference.langchain.com/python/integrations/langchain_together/)                       | <a href="https://pypi.org/project/langchain-together/"><img alt="Downloads per month" /></a>            | <a href="https://pypi.org/project/langchain-together/"><img alt="PyPI - Latest version" /></a>            | [✅](https://www.npmjs.com/package/@langchain/community)       |
| [MCP Toolbox (Google)](/oss/python/integrations/providers/toolbox/) | [`toolbox-langchain`](https://pypi.org/project/toolbox-langchain/)                                                    | <a href="https://pypi.org/project/toolbox-langchain/"><img alt="Downloads per month" /></a>             | <a href="https://pypi.org/project/toolbox-langchain/"><img alt="PyPI - Latest version" /></a>             | ❌                                                             |
| [Google (Community)](/oss/python/integrations/providers/google)     | [`langchain-google-community`](https://reference.langchain.com/python/integrations/langchain_google_community/)       | <a href="https://pypi.org/project/langchain-google-community/"><img alt="Downloads per month" /></a>    | <a href="https://pypi.org/project/langchain-google-community/"><img alt="PyPI - Latest version" /></a>    | ❌                                                             |
| [Nebius](/oss/python/integrations/providers/nebius/)                | [`langchain-nebius`](https://pypi.org/project/langchain-nebius/)                                                      | <a href="https://pypi.org/project/langchain-nebius/"><img alt="Downloads per month" /></a>              | <a href="https://pypi.org/project/langchain-nebius/"><img alt="PyPI - Latest version" /></a>              | ❌                                                             |
| [Unstructured](/oss/python/integrations/providers/unstructured/)    | [`langchain-unstructured`](https://reference.langchain.com/python/integrations/langchain_unstructured/)               | <a href="https://pypi.org/project/langchain-unstructured/"><img alt="Downloads per month" /></a>        | <a href="https://pypi.org/project/langchain-unstructured/"><img alt="PyPI - Latest version" /></a>        | [✅](https://www.npmjs.com/package/@langchain/community)       |
| [Sambanova](/oss/python/integrations/providers/sambanova/)          | [`langchain-sambanova`](https://pypi.org/project/langchain-sambanova/)                                                | <a href="https://pypi.org/project/langchain-sambanova/"><img alt="Downloads per month" /></a>           | <a href="https://pypi.org/project/langchain-sambanova/"><img alt="PyPI - Latest version" /></a>           | ❌                                                             |
| [Graph RAG](/oss/python/integrations/providers/graph_rag)           | [`langchain-graph-retriever`](https://pypi.org/project/langchain-graph-retriever/)                                    | <a href="https://pypi.org/project/langchain-graph-retriever/"><img alt="Downloads per month" /></a>     | <a href="https://pypi.org/project/langchain-graph-retriever/"><img alt="PyPI - Latest version" /></a>     | ❌                                                             |
| [Neo4J](/oss/python/integrations/providers/neo4j/)                  | [`langchain-neo4j`](https://reference.langchain.com/python/integrations/langchain_neo4j/)                             | <a href="https://pypi.org/project/langchain-neo4j/"><img alt="Downloads per month" /></a>               | <a href="https://pypi.org/project/langchain-neo4j/"><img alt="PyPI - Latest version" /></a>               | [✅](https://www.npmjs.com/package/@langchain/community)       |
| [Docling](/oss/python/integrations/providers/docling/)              | [`langchain-docling`](https://pypi.org/project/langchain-docling/)                                                    | <a href="https://pypi.org/project/langchain-docling/"><img alt="Downloads per month" /></a>             | <a href="https://pypi.org/project/langchain-docling/"><img alt="PyPI - Latest version" /></a>             | ❌                                                             |
| [Weaviate](/oss/python/integrations/providers/weaviate/)            | [`langchain-weaviate`](https://reference.langchain.com/python/integrations/langchain_weaviate/)                       | <a href="https://pypi.org/project/langchain-weaviate/"><img alt="Downloads per month" /></a>            | <a href="https://pypi.org/project/langchain-weaviate/"><img alt="PyPI - Latest version" /></a>            | [✅](https://www.npmjs.com/package/@langchain/weaviate)        |
| [Exa](/oss/python/integrations/providers/exa_search)                | [`langchain-exa`](https://reference.langchain.com/python/integrations/langchain_exa/)                                 | <a href="https://pypi.org/project/langchain-exa/"><img alt="Downloads per month" /></a>                 | <a href="https://pypi.org/project/langchain-exa/"><img alt="PyPI - Latest version" /></a>                 | [✅](https://www.npmjs.com/package/@langchain/exa)             |
| [Cerebras](/oss/python/integrations/providers/cerebras/)            | [`langchain-cerebras`](https://reference.langchain.com/python/integrations/langchain_cerebras/)                       | <a href="https://pypi.org/project/langchain-cerebras/"><img alt="Downloads per month" /></a>            | <a href="https://pypi.org/project/langchain-cerebras/"><img alt="PyPI - Latest version" /></a>            | [✅](https://www.npmjs.com/package/@langchain/cerebras)        |

## All providers

[See all providers](/oss/python/integrations/providers/all_providers) or search for a provider using the search field.

<Info>
  If you'd like to contribute an integration, see the [contributing guide](/oss/python/contributing).
</Info>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/providers/overview.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Retriever integrations
Source: https://docs.langchain.com/oss/python/integrations/retrievers/index

Integrate with retrievers using LangChain Python.

A [retriever](/oss/python/langchain/retrieval#building-blocks) is an interface that returns documents given an unstructured query.
It is more general than a vector store.
A retriever does not need to be able to store documents, only to return (or retrieve) them.
Retrievers can be created from vector stores, but are also broad enough to include other sources.

Retrievers accept a string query as input and return a list of [`Document`](https://reference.langchain.com/python/langchain-core/documents/base/Document) objects as output.

Note that all [vector stores](/oss/python/integrations/vectorstores) can be cast to retrievers. Refer to the vector store [integration docs](/oss/python/integrations/vectorstores/) for available vector stores.
This page lists custom retrievers, implemented via subclassing BaseRetriever.

## Bring-your-own documents

The below retrievers allow you to index and search a custom corpus of documents.

| Retriever                                                                                | Self-host | Cloud offering | Package                                                                                                                                    |
| ---------------------------------------------------------------------------------------- | --------- | -------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| [`AmazonKnowledgeBasesRetriever`](/oss/python/integrations/retrievers/bedrock)           | ❌         | ✅              | [`langchain-aws`](https://reference.langchain.com/python/langchain-aws/retrievers/bedrock/AmazonKnowledgeBasesRetriever)                   |
| [`ElasticsearchRetriever`](/oss/python/integrations/retrievers/elasticsearch_retriever)  | ✅         | ✅              | [`langchain-elasticsearch`](https://reference.langchain.com/python/langchain-elasticsearch/retrievers/ElasticsearchRetriever)              |
| [`NVIDIARAGRetriever`](/oss/python/integrations/retrievers/nvidia)                       | ✅         | ❌              | [`langchain-nvidia-ai-endpoints`](https://reference.langchain.com/python/langchain-nvidia-ai-endpoints/retrievers/NVIDIARAGRetriever)      |
| [`VertexAISearchRetriever`](/oss/python/integrations/retrievers/google_vertex_ai_search) | ❌         | ✅              | [`langchain-google-community`](https://reference.langchain.com/python/langchain-google-community/vertex_ai_search/VertexAISearchRetriever) |

## External index

The below retrievers will search over an external index (e.g., constructed from Internet data or similar).

| Retriever                                                                            | Source                                                                                             | Package                                                                                                                    |
| ------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| [`ParallelSearchRetriever`](/oss/python/integrations/retrievers/parallel)            | Internet search via the [Parallel Search API](https://docs.parallel.ai/search/search-quickstart)   | [`langchain-parallel`](https://reference.langchain.com/python/langchain-parallel/retrievers/ParallelSearchRetriever)       |
| [`PerplexitySearchRetriever`](/oss/python/integrations/retrievers/perplexity_search) | Internet search via the [Perplexity Search API](https://docs.perplexity.ai/docs/search/quickstart) | [`langchain-perplexity`](https://reference.langchain.com/python/langchain-perplexity/retrievers/PerplexitySearchRetriever) |
| [`YouRetriever`](/oss/python/integrations/retrievers/you-retriever)                  | Internet search                                                                                    | [`langchain-youdotcom`](https://pypi.org/project/langchain-youdotcom/)                                                     |

## All retrievers

<Columns>
  <Card title="AgentMail" icon="link" href="/oss/python/integrations/retrievers/agentmail" />

  <Card title="Bedrock (Knowledge Bases)" icon="link" href="/oss/python/integrations/retrievers/bedrock" />

  <Card title="Box" icon="link" href="/oss/python/integrations/retrievers/box" />

  <Card title="Cognee" icon="link" href="/oss/python/integrations/retrievers/cognee" />

  <Card title="Cohere reranker" icon="link" href="/oss/python/integrations/retrievers/cohere-reranker" />

  <Card title="Cohere RAG" icon="link" href="/oss/python/integrations/retrievers/cohere" />

  <Card title="Contextual AI Reranker" icon="link" href="/oss/python/integrations/retrievers/contextual" />

  <Card title="Dappier" icon="link" href="/oss/python/integrations/retrievers/dappier" />

  <Card title="Elasticsearch" icon="link" href="/oss/python/integrations/retrievers/elasticsearch_retriever" />

  <Card title="Egnyte" icon="link" href="/oss/python/integrations/retrievers/egnyte" />

  <Card title="Galaxia" icon="link" href="/oss/python/integrations/retrievers/galaxia-retriever" />

  <Card title="Google Drive" icon="link" href="/oss/python/integrations/retrievers/google_drive" />

  <Card title="Google Vertex AI Search" icon="link" href="/oss/python/integrations/retrievers/google_vertex_ai_search" />

  <Card title="Graph RAG" icon="link" href="/oss/python/integrations/retrievers/graph_rag" />

  <Card title="GreenNode" icon="link" href="/oss/python/integrations/retrievers/greennode_reranker" />

  <Card title="IBM watsonx.ai" icon="link" href="/oss/python/integrations/retrievers/ibm_watsonx_ranker" />

  <Card title="IMAP" icon="link" href="/oss/python/integrations/retrievers/imap" />

  <Card title="Kinetica Vectorstore" icon="link" href="/oss/python/integrations/retrievers/kinetica" />

  <Card title="LinkupSearchRetriever" icon="link" href="/oss/python/integrations/retrievers/linkup_search" />

  <Card title="Nebius" icon="link" href="/oss/python/integrations/retrievers/nebius" />

  <Card title="Nimble Extract" icon="link" href="/oss/python/integrations/retrievers/nimble_extract" />

  <Card title="Nimble Search" icon="link" href="/oss/python/integrations/retrievers/nimble_search" />

  <Card title="NVIDIA RAG Blueprint" icon="link" href="/oss/python/integrations/retrievers/nvidia" />

  <Card title="Parallel Search" icon="link" href="/oss/python/integrations/retrievers/parallel" />

  <Card title="Permit" icon="link" href="/oss/python/integrations/retrievers/permit" />

  <Card title="Perigon" icon="link" href="/oss/python/integrations/retrievers/perigon" />

  <Card title="Perplexity Search" icon="link" href="/oss/python/integrations/retrievers/perplexity_search" />

  <Card title="Pinecone Rerank" icon="link" href="/oss/python/integrations/retrievers/pinecone_rerank" />

  <Card title="RAGatouille" icon="link" href="/oss/python/integrations/retrievers/ragatouille" />

  <Card title="SpiceDB" icon="link" href="/oss/python/integrations/retrievers/spicedb" />

  <Card title="ValyuContext" icon="link" href="/oss/python/integrations/retrievers/valyu" />

  <Card title="Vectorize" icon="link" href="/oss/python/integrations/retrievers/vectorize" />

  <Card title="You.com" icon="link" href="/oss/python/integrations/retrievers/you-retriever" />

  <Card title="Zotero" icon="link" href="/oss/python/integrations/retrievers/zotero" />
</Columns>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/retrievers/index.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Sandbox integrations
Source: https://docs.langchain.com/oss/python/integrations/sandboxes/index

Integrate with sandbox providers using LangChain Python.

Sandboxes provide isolated execution environments for running agent-generated code safely. Learn more about [sandboxes](/oss/python/deepagents/sandboxes).

<div>
  <a href="/oss/python/integrations/sandboxes/langsmith">
    <img alt="" />

    <span>LangSmith</span>
  </a>

  <a href="/oss/python/integrations/sandboxes/aws">
    <img alt="" />

    <img alt="" />

    <span>AgentCore</span>
  </a>

  <a href="/oss/python/integrations/sandboxes/daytona">
    <img alt="" />

    <img alt="" />

    <span>Daytona</span>
  </a>

  <a href="/oss/python/integrations/sandboxes/e2b">
    <img alt="" />

    <img alt="" />

    <span>E2B</span>
  </a>

  <a href="/oss/python/integrations/sandboxes/modal">
    <img alt="" />

    <img alt="" />

    <span>Modal</span>
  </a>

  <a href="/oss/python/integrations/sandboxes/runloop">
    <img alt="" />

    <img alt="" />

    <span>Runloop</span>
  </a>

  <a href="/oss/python/integrations/sandboxes/vercel">
    <img alt="" />

    <img alt="" />

    <span>Vercel</span>
  </a>
</div>

If you'd like to contribute a sandbox, see [Implement a sandbox integration](/oss/python/contributing/implement-langchain#sandboxes).

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/sandboxes/index.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Text splitter integrations
Source: https://docs.langchain.com/oss/python/integrations/splitters/index

Integrate with text splitters using LangChain.

<CodeGroup>
  ```bash pip theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  pip install -U langchain-text-splitters
  ```

  ```bash uv theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  uv add langchain-text-splitters
  ```
</CodeGroup>

**Text splitters** break large docs into smaller chunks that will be retrievable individually and fit within model context window limit.

There are several strategies for splitting documents, each with its own advantages.

<Tip>
  For most use cases, start with the [`RecursiveCharacterTextSplitter`](/oss/python/integrations/splitters/recursive_text_splitter). It provides a solid balance between keeping context intact and managing chunk size. This default strategy works well out of the box, and you should only consider adjusting it if you need to fine-tune performance for your specific application.
</Tip>

## Text structure-based

Text is naturally organized into hierarchical units such as paragraphs, sentences, and words. We can leverage this inherent structure to inform our splitting strategy, creating split that maintain natural language flow, maintain semantic coherence within split, and adapts to varying levels of text granularity. LangChain's `RecursiveCharacterTextSplitter` implements this concept:

* The [`RecursiveCharacterTextSplitter`](/oss/python/integrations/splitters/recursive_text_splitter) attempts to keep larger units (e.g., paragraphs) intact.
* If a unit exceeds the chunk size, it moves to the next level (e.g., sentences).
* This process continues down to the word level if necessary.

Example usage:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain_text_splitters import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=0)
texts = text_splitter.split_text(document)
```

**Available text splitters**:

* [Recursively split text](/oss/python/integrations/splitters/recursive_text_splitter)

## Length-based

An intuitive strategy is to split documents based on their length. This simple yet effective approach ensures that each chunk doesn't exceed a specified size limit. Key benefits of length-based splitting:

* Straightforward implementation
* Consistent chunk sizes
* Easily adaptable to different model requirements

Types of length-based splitting:

* Token-based: Splits text based on the number of tokens, which is useful when working with language models.
* Character-based: Splits text based on the number of characters, which can be more consistent across different types of text.

Example implementation using LangChain's `CharacterTextSplitter` with token-based splitting:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain_text_splitters import CharacterTextSplitter

text_splitter = CharacterTextSplitter.from_tiktoken_encoder(
    encoding_name="cl100k_base", chunk_size=100, chunk_overlap=0
)
texts = text_splitter.split_text(document)
```

**Available text splitters**:

* [Split by tokens](/oss/python/integrations/splitters/split_by_token)
* [Split by characters](/oss/python/integrations/splitters/character_text_splitter)

## Document structure-based

Some documents have an inherent structure, such as HTML, Markdown, or JSON files. In these cases, it's beneficial to split the document based on its structure, as it often naturally groups semantically related text. Key benefits of structure-based splitting:

* Preserves the logical organization of the document
* Maintains context within each chunk
* Can be more effective for downstream tasks like retrieval or summarization

Examples of structure-based splitting:

* Markdown: Split based on headers (e.g., `#`, `##`, `###`)
* HTML: Split using tags
* JSON: Split by object or array elements
* Code: Split by functions, classes, or logical blocks

**Available text splitters**:

* [Split Markdown](/oss/python/integrations/splitters/markdown_header_metadata_splitter)
* [Split JSON](/oss/python/integrations/splitters/recursive_json_splitter)
* [Split code](/oss/python/integrations/splitters/code_splitter)
* [Split HTML](/oss/python/integrations/splitters/split_html)

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/integrations/splitters/index.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
