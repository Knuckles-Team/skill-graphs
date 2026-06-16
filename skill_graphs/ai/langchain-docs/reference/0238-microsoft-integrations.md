# Microsoft integrations
Source: https://docs.langchain.com/oss/python/integrations/providers/microsoft

Integrate with Microsoft using LangChain Python.

This page covers all LangChain integrations with [Microsoft Azure](https://portal.azure.com) and other [Microsoft](https://www.microsoft.com) products.

<Tip>
  **Recommended: Azure OpenAI**

  We recommend using [Azure OpenAI](https://reference.langchain.com/python/langchain-openai/llms/azure/AzureOpenAI) across [chat models](#chat-models), [LLMs](#llms), and [embedding models](#embedding-models). With the [v1 API](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/api-version-lifecycle?tabs=python) (Generally Available as of August 2025), you can use your Azure endpoint and API keys directly with the [`langchain-openai`](https://reference.langchain.com/python/langchain-openai/) package to call any model deployed in [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/) (including OpenAI, Llama, DeepSeek, Mistral, and Phi) through a single interface. You also get native support for Microsoft Entra ID authentication and access to the latest features including the [Responses API](#responses-api) and [reasoning models](/oss/python/integrations/chat/azure_chat_openai). [Get started here](#azure-openai).

  **Samples and tutorials:**

  * [Azure-Samples/langchain-azure-openai-starter](https://github.com/Azure-Samples/langchain-azure-openai-starter): Start with a production-ready LangChain and Azure OpenAI app template that lets you deploy directly to Azure with a single `azd` command.
  * [microsoft/langchain-for-beginners](https://github.com/microsoft/langchain-for-beginners): A hands-on course introducing LangChain with Azure OpenAI.
  * [Azure-Samples/langchain-agent-python](https://github.com/Azure-Samples/langchain-agent-python): Build and deploy LangChain agents on Azure.
</Tip>

<Note>
  **Claude on Azure**

  Microsoft Foundry also offers access to all [Anthropic Claude models](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/how-to/use-foundry-models-claude), including Opus, Sonnet, and Haiku. Claude models are served through a dedicated Anthropic-native endpoint rather than the Azure OpenAI v1 API. Use [`langchain-anthropic`](/oss/python/integrations/chat/anthropic) pointed at your Foundry Anthropic endpoint.
</Note>

## Chat models

Microsoft offers three main options for accessing chat models through Azure:

1. **[Azure OpenAI](https://learn.microsoft.com/en-us/azure/ai-services/openai/)** (recommended) — Access any model deployed in Microsoft Foundry (including OpenAI, Llama, DeepSeek, Mistral, and Phi) through a single interface, with enterprise features such as keyless authentication through [Microsoft Entra ID](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/managed-identity), regional data residency, and private networking. Use [`ChatOpenAI`](https://reference.langchain.com/python/langchain-openai/chat_models/base/ChatOpenAI) on the v1 API, or [`AzureChatOpenAI`](https://reference.langchain.com/python/langchain-openai/chat_models/azure/AzureChatOpenAI) for traditional deployments.

   Azure OpenAI also supports the [Responses API](#responses-api), which gives you access to server-side tools like code interpreter, image generation, and file search directly from your chat model.
2. **[Azure AI](https://learn.microsoft.com/en-us/azure/ai-studio/how-to/deploy-models)** — Recommended for accessing tools, storage, and custom middleware from the broader Azure ecosystem alongside your chat model.
3. **[Azure ML](https://learn.microsoft.com/en-us/azure/machine-learning/)** — Allows deployment and management of custom or fine-tuned open-source models with Azure Machine Learning.

### Azure OpenAI

To get started with Azure OpenAI, [create an Azure deployment](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/create-resource) and install the `langchain-openai` package:

<CodeGroup>
  ```bash pip theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  pip install -U langchain-openai
  ```

  ```bash uv theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  uv add langchain-openai
  ```
</CodeGroup>

On the v1 API, use [`ChatOpenAI`](https://reference.langchain.com/python/langchain-openai/chat_models/base/ChatOpenAI) directly against your Azure endpoint—no `api_version` required:

<Tabs>
  <Tab title="Entra ID (recommended)">
    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    pip install azure-identity
    ```

    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    from azure.identity import DefaultAzureCredential, get_bearer_token_provider
    from langchain_openai import ChatOpenAI

    token_provider = get_bearer_token_provider(
        DefaultAzureCredential(),
        "https://cognitiveservices.azure.com/.default",
    )

    llm = ChatOpenAI(
        model="gpt-5.4-mini",  # your Azure deployment name
        base_url="https://YOUR-RESOURCE-NAME.openai.azure.com/openai/v1/",
        api_key=token_provider,  # callable that handles token refresh
    )
    ```
  </Tab>

  <Tab title="API key">
    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    from langchain_openai import ChatOpenAI

    llm = ChatOpenAI(
        model="gpt-5.4-mini",  # your Azure deployment name
        base_url="https://YOUR-RESOURCE-NAME.openai.azure.com/openai/v1/",
        api_key="your-azure-api-key",
    )
    ```
  </Tab>
</Tabs>

For traditional Azure OpenAI API versions, use [`AzureChatOpenAI`](https://reference.langchain.com/python/langchain-openai/chat_models/azure/AzureChatOpenAI):

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain_openai import AzureChatOpenAI
```

See the [Azure ChatOpenAI integration page](/oss/python/integrations/chat/azure_chat_openai) for end-to-end setup, Entra ID authentication, tool calling, and reasoning examples.

#### Responses API

Azure OpenAI supports the [Responses API](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/responses), which provides stateful conversations, built-in tools (web search, file search, code interpreter), and structured reasoning summaries. [`ChatOpenAI`](https://reference.langchain.com/python/langchain-openai/chat_models/base/ChatOpenAI) automatically routes to the Responses API when you set the `reasoning` parameter, or you can opt in explicitly with `use_responses_api=True`:

<Tabs>
  <Tab title="Entra ID (recommended)">
    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    from azure.identity import DefaultAzureCredential, get_bearer_token_provider
    from langchain_openai import ChatOpenAI

    token_provider = get_bearer_token_provider(
        DefaultAzureCredential(),
        "https://cognitiveservices.azure.com/.default",
    )

    llm = ChatOpenAI(
        model="gpt-5.4-mini",
        base_url="https://YOUR-RESOURCE-NAME.openai.azure.com/openai/v1/",
        api_key=token_provider,
        use_responses_api=True,
    )

    response = llm.invoke("Summarize the bitter lesson.")
    print(response.text)
    ```
  </Tab>

  <Tab title="API key">
    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    from langchain_openai import ChatOpenAI

    llm = ChatOpenAI(
        model="gpt-5.4-mini",
        base_url="https://YOUR-RESOURCE-NAME.openai.azure.com/openai/v1/",
        api_key="your-azure-api-key",
        use_responses_api=True,
    )

    response = llm.invoke("Summarize the bitter lesson.")
    print(response.text)
    ```
  </Tab>
</Tabs>

For a walkthrough of reasoning effort, reasoning summaries, and streaming with the Responses API, see the [Azure ChatOpenAI integration page](/oss/python/integrations/chat/azure_chat_openai).

### Azure AI

> [Azure AI Foundry](https://learn.microsoft.com/en-us/azure/developer/python/get-started) is the broader Azure AI platform. The `langchain-azure-ai` package lets you bring Azure-native tools, storage, and custom middleware into your LangChain app, and exposes chat models deployed in Foundry through the `AzureAIOpenAIApiChatModel` class.

<CodeGroup>
  ```bash pip theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  pip install -U langchain-azure-ai
  ```

  ```bash uv theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  uv add langchain-azure-ai
  ```
</CodeGroup>

See a [usage example](/oss/python/integrations/chat/azure_ai).

## LLMs

Microsoft offers two main options for accessing LLMs through Azure:

1. **[Azure OpenAI](https://learn.microsoft.com/en-us/azure/ai-services/openai/)** (recommended) — Access any model deployed in Microsoft Foundry (including OpenAI, Llama, DeepSeek, Mistral, and Phi) as a completion LLM with [`AzureOpenAI`](https://reference.langchain.com/python/langchain-openai/llms/azure/AzureOpenAI).
2. **[Azure ML](https://learn.microsoft.com/en-us/azure/machine-learning/)** — Use custom or open-source models hosted on Azure Machine Learning online endpoints.

### Azure OpenAI

See a [usage example](/oss/python/integrations/llms/azure_openai).

<CodeGroup>
  ```bash pip theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  pip install -U langchain-openai
  ```

  ```bash uv theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  uv add langchain-openai
  ```
</CodeGroup>

<Tabs>
  <Tab title="Entra ID (recommended)">
    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    from azure.identity import DefaultAzureCredential, get_bearer_token_provider
    from langchain_openai import AzureOpenAI

    token_provider = get_bearer_token_provider(
        DefaultAzureCredential(),
        "https://cognitiveservices.azure.com/.default",
    )

    llm = AzureOpenAI(
        azure_deployment="gpt-5.4-mini",  # your Azure deployment name
        api_version="2025-04-01-preview",
        azure_ad_token_provider=token_provider,
    )

    print(llm.invoke("Write a haiku about the ocean."))
    ```
  </Tab>

  <Tab title="API key">
    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    from langchain_openai import AzureOpenAI

    llm = AzureOpenAI(
        azure_deployment="gpt-5.4-mini",  # your Azure deployment name
        api_version="2025-04-01-preview",
        azure_endpoint="https://YOUR-RESOURCE-NAME.openai.azure.com/",
        api_key="your-azure-api-key",
    )

    print(llm.invoke("Write a haiku about the ocean."))
    ```
  </Tab>
</Tabs>

## Embedding models

Microsoft offers two main options for accessing embedding models through Azure:

1. **[Azure OpenAI](https://learn.microsoft.com/en-us/azure/ai-services/openai/)** (recommended) — Use embedding models deployed in Microsoft Foundry (including OpenAI `text-embedding-3-small`, `text-embedding-3-large`, and Cohere) with [`AzureOpenAIEmbeddings`](https://reference.langchain.com/python/langchain-openai/embeddings/azure/AzureOpenAIEmbeddings).
2. **[Azure AI](https://learn.microsoft.com/en-us/azure/ai-studio/how-to/deploy-models)** — Recommended for accessing tools, storage, and custom middleware from the broader Azure ecosystem alongside your embedding model.

### Azure OpenAI

See a [usage example](/oss/python/integrations/embeddings/azure_openai).

<CodeGroup>
  ```bash pip theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  pip install -U langchain-openai
  ```

  ```bash uv theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  uv add langchain-openai
  ```
</CodeGroup>

<Tabs>
  <Tab title="Entra ID (recommended)">
    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    from azure.identity import DefaultAzureCredential, get_bearer_token_provider
    from langchain_openai import AzureOpenAIEmbeddings

    token_provider = get_bearer_token_provider(
        DefaultAzureCredential(),
        "https://cognitiveservices.azure.com/.default",
    )

    embeddings = AzureOpenAIEmbeddings(
        azure_deployment="text-embedding-3-small",  # your Azure deployment name
        api_version="2025-04-01-preview",
        azure_ad_token_provider=token_provider,
    )

    vector = embeddings.embed_query("LangChain makes agents easy.")
    ```
  </Tab>

  <Tab title="API key">
    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    from langchain_openai import AzureOpenAIEmbeddings

    embeddings = AzureOpenAIEmbeddings(
        azure_deployment="text-embedding-3-small",  # your Azure deployment name
        api_version="2025-04-01-preview",
        azure_endpoint="https://YOUR-RESOURCE-NAME.openai.azure.com/",
        api_key="your-azure-api-key",
    )

    vector = embeddings.embed_query("LangChain makes agents easy.")
    ```
  </Tab>
</Tabs>

### Azure AI

<CodeGroup>
  ```bash pip theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  pip install -U langchain-azure-ai
  ```

  ```bash uv theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  uv add langchain-azure-ai
  ```
</CodeGroup>

See a [usage example](/oss/python/integrations/providers/azure_ai#azure-ai-model-inference-for-embeddings).

## Middleware

### Azure AI Content Safety middleware

> [Azure AI Content Safety](https://learn.microsoft.com/en-us/azure/ai-services/content-safety/overview) provides guardrails you can apply to LangChain agents through middleware. The `langchain-azure-ai` package currently exports middleware for text moderation, image moderation, prompt injection detection, protected material detection, and groundedness evaluation.

Install the middleware package:

<CodeGroup>
  ```bash pip theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  pip install -U langchain-azure-ai
  ```

  ```bash uv theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  uv add langchain-azure-ai
  ```
</CodeGroup>

See the [Microsoft Foundry middleware guide](/oss/python/integrations/middleware/azure_ai).

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain_azure_ai.agents.middleware import AzureContentModerationMiddleware
```

## Document loaders

### Azure Blob Storage

> [Azure Blob Storage](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blobs-introduction) is Microsoft's object storage solution for the cloud. Blob Storage is optimized for storing massive amounts of unstructured data. Unstructured data is data that doesn't adhere to a particular data model or definition, such as text or binary data.

`Azure Blob Storage` is designed for:

* Serving images or documents directly to a browser.
* Storing files for distributed access.
* Streaming video and audio.
* Writing to log files.
* Storing data for backup and restore, disaster recovery, and archiving.
* Storing data for analysis by an on-premises or Azure-hosted service.

<CodeGroup>
  ```bash pip theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  pip install langchain-azure-storage
  ```

  ```bash uv theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  uv add langchain-azure-storage
  ```
</CodeGroup>

See [usage examples for the Azure Blob Storage Loader](/oss/python/integrations/document_loaders/azure_blob_storage).

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain_azure_storage.document_loaders import AzureBlobStorageLoader
```

## Memory

### Azure cosmos DB chat message history

> [Azure Cosmos DB](https://learn.microsoft.com/azure/cosmos-db/) provides chat message history storage for conversational AI applications, enabling you to persist and retrieve conversation history with low latency and high availability.

<CodeGroup>
  ```bash pip theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  pip install langchain-azure-cosmosdb
  ```

  ```bash uv theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  uv add langchain-azure-cosmosdb
  ```
</CodeGroup>

Configure your Azure Cosmos DB connection (sync or async, with access key or Microsoft Entra ID):

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain_azure_cosmosdb import CosmosDBChatMessageHistory

history = CosmosDBChatMessageHistory(
    cosmos_endpoint="https://<your-account>.documents.azure.com:443/",
    cosmos_database="<your-database>",
    cosmos_container="<your-container>",
    session_id="<session-id>",
    user_id="<user-id>",
    credential="<your-key-or-token-credential>",
    ttl=3600,  # optional: messages expire after 1 hour
)
history.prepare_cosmos()

history.add_user_message("Hello!")
history.add_ai_message("Hi there!")
```

For async usage, import `AsyncCosmosDBChatMessageHistory` from the same package.

### Azure cosmos DB semantic cache

> [`AzureCosmosDBNoSqlSemanticCache`](https://github.com/langchain-ai/langchain-azure/tree/main/libs/azure-cosmosdb) caches LLM responses in Azure Cosmos DB for NoSQL using vector similarity, returning cached results when a semantically similar prompt is seen again.

<CodeGroup>
  ```bash pip theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  pip install langchain-azure-cosmosdb
  ```

  ```bash uv theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  uv add langchain-azure-cosmosdb
  ```
</CodeGroup>

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from azure.cosmos import CosmosClient, PartitionKey
from langchain_core.globals import set_llm_cache
from langchain_azure_cosmosdb import AzureCosmosDBNoSqlSemanticCache

cosmos_client = CosmosClient("<endpoint>", "<key>")

cache = AzureCosmosDBNoSqlSemanticCache(
    cosmos_client=cosmos_client,
    embedding=embedding,
    vector_embedding_policy=vector_embedding_policy,
    indexing_policy=indexing_policy,
    cosmos_container_properties={"partition_key": PartitionKey(path="/id")},
    cosmos_database_properties={"id": "cache-db"},
    vector_search_fields={"text_field": "text", "embedding_field": "embedding"},
    database_name="cache-db",
    container_name="cache-container",
)

set_llm_cache(cache)
```

For async usage, import `AsyncAzureCosmosDBNoSqlSemanticCache`.

## Vector stores

### Azure cosmos DB

AI agents can rely on Azure Cosmos DB as a unified [memory system](https://learn.microsoft.com/en-us/azure/cosmos-db/ai-agents#memory-can-make-or-break-agents) solution, enjoying speed, scale, and simplicity. This service successfully [enabled OpenAI's ChatGPT service](https://www.youtube.com/watch?v=6IIUtEFKJec\&t) to scale dynamically with high reliability and low maintenance. Powered by an atom-record-sequence engine, it is the world's first globally distributed [NoSQL](https://learn.microsoft.com/en-us/azure/cosmos-db/distributed-nosql), [relational](https://learn.microsoft.com/en-us/azure/cosmos-db/distributed-relational), and [vector database](https://learn.microsoft.com/en-us/azure/cosmos-db/vector-database) service that offers a serverless mode.

Below are two available Azure Cosmos DB APIs that can provide vector store functionalities.

#### Azure cosmos DB for MongoDB (vCore)

> [Azure Cosmos DB for MongoDB vCore](https://learn.microsoft.com/en-us/azure/cosmos-db/mongodb/vcore/) makes it easy to create a database with full native MongoDB support.
> You can apply your MongoDB experience and continue to use your favorite MongoDB drivers, SDKs, and tools by pointing your application to the API for MongoDB vCore account's connection string.
> Use vector search in Azure Cosmos DB for MongoDB vCore to seamlessly integrate your AI-based applications with your data that's stored in Azure Cosmos DB.

##### Installation and setup

See [detailed configuration instructions](/oss/python/integrations/vectorstores/azure_cosmos_db_mongo_vcore).

We need to install `langchain-azure-ai` and `pymongo` python packages.

<CodeGroup>
  ```bash pip theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  pip install langchain-azure-ai pymongo
  ```

  ```bash uv theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  uv add langchain-azure-ai pymongo
  ```
</CodeGroup>

##### Deploy Azure cosmos DB on Microsoft Azure

Azure Cosmos DB for MongoDB vCore provides developers with a fully managed MongoDB-compatible database service for building modern applications with a familiar architecture.

With Cosmos DB for MongoDB vCore, developers can enjoy the benefits of native Azure integrations, low total cost of ownership (TCO), and the familiar vCore architecture when migrating existing applications or building new ones.

[Sign Up](https://azure.microsoft.com/en-us/free/) for free to get started today.

See a [usage example](/oss/python/integrations/vectorstores/azure_cosmos_db_mongo_vcore).

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain_azure_ai.vectorstores import AzureCosmosDBMongoVCoreVectorSearch
```

#### Azure cosmos DB NoSQL

> [Azure Cosmos DB for NoSQL](https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/vector-search) now offers vector indexing and search in preview.
> This feature is designed to handle high-dimensional vectors, enabling efficient and accurate vector search at any scale. You can now store vectors
> directly in the documents alongside your data. This means that each document in your database can contain not only traditional schema-free data,
> but also high-dimensional vectors as other properties of the documents. This colocation of data and vectors allows for efficient indexing and searching,
> as the vectors are stored in the same logical unit as the data they represent. This simplifies data management, AI application architectures, and the
> efficiency of vector-based operations.

##### Installation and setup

See [detail configuration instructions](/oss/python/integrations/vectorstores/azure_cosmos_db_no_sql).

We need to install `langchain-azure-cosmosdb` and `azure-cosmos` python packages.

<CodeGroup>
  ```bash pip theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  pip install langchain-azure-cosmosdb azure-cosmos
  ```

  ```bash uv theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  uv add langchain-azure-cosmosdb azure-cosmos
  ```
</CodeGroup>

##### Deploy Azure cosmos DB on Microsoft Azure

Azure Cosmos DB offers a solution for modern apps and intelligent workloads by being very responsive with dynamic and elastic autoscale. It is available
in every Azure region and can automatically replicate data closer to users. It has SLA guaranteed low-latency and high availability.

[Sign Up](https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/quickstart-python?pivots=devcontainer-codespace) for free to get started today.

See a [usage example](/oss/python/integrations/vectorstores/azure_cosmos_db_no_sql).

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain_azure_cosmosdb import AzureCosmosDBNoSqlVectorSearch
```

### Azure Database for PostgreSQL

> [Azure Database for PostgreSQL - Flexible Server](https://learn.microsoft.com/en-us/azure/postgresql/flexible-server/service-overview) is a relational database service based on the open-source Postgres database engine. It's a fully managed database-as-a-service that can handle mission-critical workloads with predictable performance, security, high availability, and dynamic scalability.

See [set up instructions](https://learn.microsoft.com/en-us/azure/postgresql/flexible-server/quickstart-create-server-portal) for Azure Database for PostgreSQL.

Simply use the [connection string](https://learn.microsoft.com/en-us/azure/postgresql/flexible-server/connect-python?tabs=cmd%2Cpassword#add-authentication-code) from your Azure Portal.

Since Azure Database for PostgreSQL is open-source Postgres, you can use the [LangChain's Postgres support](/oss/python/integrations/vectorstores/pgvector/) to connect to Azure Database for PostgreSQL.

### Azure SQL Database

> [Azure SQL Database](https://learn.microsoft.com/azure/azure-sql/database/sql-database-paas-overview?view=azuresql) is a robust service that combines scalability, security, and high availability, providing all the benefits of a modern database solution.  It also provides a dedicated Vector data type & built-in functions that simplifies the storage and querying of vector embeddings directly within a relational database. This eliminates the need for separate vector databases and related integrations, increasing the security of your solutions while reducing the overall complexity.

By leveraging your current SQL Server databases for vector search, you can enhance data capabilities while minimizing expenses and avoiding the challenges of transitioning to new systems.

##### Installation and setup

See [detail configuration instructions](/oss/python/integrations/vectorstores/sqlserver).

We need to install the `langchain-sqlserver` python package.

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
!pip install langchain-sqlserver==0.1.1
```

##### Deploy Azure SQL DB on Microsoft Azure

[Sign Up](https://learn.microsoft.com/azure/azure-sql/database/free-offer?view=azuresql) for free to get started today.

See a [usage example](/oss/python/integrations/vectorstores/sqlserver).

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain_sqlserver import SQLServer_VectorStore
```

## Vector store

### Azure Database for PostgreSQL

> [Azure Database for PostgreSQL - Flexible Server](https://learn.microsoft.com/en-us/azure/postgresql/flexible-server/service-overview) is a relational database service based on the open-source Postgres database engine. It's a fully managed database-as-a-service that can handle mission-critical workloads with predictable performance, security, high availability, and dynamic scalability.

See [set up instructions](https://learn.microsoft.com/en-us/azure/postgresql/flexible-server/quickstart-create-server-portal) for Azure Database for PostgreSQL.

You need to [enable pgvector extension](https://learn.microsoft.com/en-us/azure/postgresql/flexible-server/how-to-use-pgvector) in your database to use Postgres as a vector store. Once you have the extension enabled, you can use the [PGVector in LangChain](/oss/python/integrations/vectorstores/pgvector/) to connect to Azure Database for PostgreSQL.

See a [usage example](/oss/python/integrations/vectorstores/pgvector/). Simply use the [connection string](https://learn.microsoft.com/en-us/azure/postgresql/flexible-server/connect-python?tabs=cmd%2Cpassword#add-authentication-code) from your Azure Portal.

## Tools

### Microsoft Foundry tools

Microsoft Foundry exposes LangChain service tools for Azure AI Content Understanding, Document Intelligence, Image Analysis, and Text Analytics for Health.

Install the package with the `tools` extra:

<CodeGroup>
  ```bash pip theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  pip install -U "langchain-azure-ai[tools]"
  ```

  ```bash uv theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  uv add "langchain-azure-ai[tools]"
  ```
</CodeGroup>

See the [Microsoft Foundry Tools guide](/oss/python/integrations/tools/azure_ai_services).

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain_azure_ai.tools import AzureAIDocumentIntelligenceTool
```

### Image generation tool

Microsoft Foundry Models has several models available in the catalog for image generation.

See the [Microsoft Foundry tools guide](/oss/python/integrations/tools/azure_ai).

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain_azure_ai.tools import AzureOpenAIModelImageGenTool
```

### Transcriptions tool

Microsoft Foundry Models has Whisper models available in the catalog for speech-to-text transcriptions.

See the [Microsoft Foundry tools guide](/oss/python/integrations/tools/azure_ai).

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain_azure_ai.tools import AzureOpenAITranscriptionsTool
```

### Code interpreter tool (server-side)

Run Python code server-side in a sandboxed container with the Code Interpreter tool.

See the [Microsoft Foundry tools guide](/oss/python/integrations/tools/azure_ai).

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain_azure_ai.tools.builtin import CodeInterpreterTool
```

### Web search tool (server-side)

Search the internet for current information and sources.

See the [Microsoft Foundry tools guide](/oss/python/integrations/tools/azure_ai).

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain_azure_ai.tools.builtin import WebSearchTool
```

### File search tool (server-side)

Search vector stores for relevant document content.

See the [Microsoft Foundry tools guide](/oss/python/integrations/tools/azure_ai).

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain_azure_ai.tools.builtin import FileSearchTool
```

### Image generation tool (server-side)

Generate or edit images using GPT image models server-side in Azure AI Foundry.

See the [Microsoft Foundry tools guide](/oss/python/integrations/tools/azure_ai).

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain_azure_ai.tools.builtin import ImageGenerationTool
```

### MCP tool (server-side)

Access external Model Context Protocol (MCP) servers.

See the [Microsoft Foundry tools guide](/oss/python/integrations/tools/azure_ai).

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain_azure_ai.tools.builtin import McpTool
```

### Azure Container Apps Dynamic Sessions

We need to get the `POOL_MANAGEMENT_ENDPOINT` environment variable from the Azure Container Apps service.
See the [Azure dynamic sessions setup instructions](/oss/python/integrations/tools/azure_dynamic_sessions/#setup).

We need to install a python package.

<CodeGroup>
  ```bash pip theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  pip install langchain-azure-dynamic-sessions
  ```

  ```bash uv theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  uv add langchain-azure-dynamic-sessions
  ```
</CodeGroup>

See a [usage example](/oss/python/integrations/tools/azure_dynamic_sessions).

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain_azure_dynamic_sessions import SessionsPythonREPLTool
```

### Azure Logic Apps

Trigger Azure Logic Apps workflows to automate business processes and integrations.

Install the package with the `tools` extra:

<CodeGroup>
  ```bash pip theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  pip install -U "langchain-azure-ai[tools]"
  ```

  ```bash uv theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  uv add "langchain-azure-ai[tools]"
  ```
</CodeGroup>

See the [Azure Logic Apps integration guide](/oss/python/integrations/tools/azure_logic_apps).

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain_azure_ai.tools import AzureLogicAppTool
```

## Toolkits

### Microsoft Foundry Project Toolbox

Load tools dynamically from an Azure AI Foundry Toolbox via the Model Context Protocol (MCP).

Install the package with the `tools` extra:

<CodeGroup>
  ```bash pip theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  pip install -U "langchain-azure-ai[tools]" langchain-mcp-adapters httpx
  ```

  ```bash uv theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  uv add "langchain-azure-ai[tools]" langchain-mcp-adapters httpx
  ```
</CodeGroup>

See the [Azure AI Foundry Toolbox guide](/oss/python/integrations/tools/azure_ai#azureaiprojecttoolbox).

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain_azure_ai.tools import AzureAIProjectToolbox
```

### Microsoft Foundry tools (formerly Azure AI Services)

Install the integration package:

<CodeGroup>
  ```bash pip theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  pip install -U "langchain-azure-ai[tools]"
  ```

  ```bash uv theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  uv add "langchain-azure-ai[tools]"
  ```
</CodeGroup>

See a [usage example](/oss/python/integrations/tools/azure_ai_services).

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain_azure_ai.tools import AzureAIServicesToolkit
```

The `AzureAIServicesToolkit` toolkit includes the following tools:

* Image Analysis: [AzureAIImageAnalysisTool](/oss/python/integrations/tools/azure_ai_services#azureaiimageanalysistool)
* Document Intelligence: [AzureAIDocumentIntelligenceTool](/oss/python/integrations/tools/azure_ai_services#azureaidocumentintelligencetool)
* Speech to Text: [AzureAISpeechToTextTool](/oss/python/integrations/tools/azure_ai_services#azureaispeechtotexttool)
* Text to Speech: [AzureAITextToSpeechTool](/oss/python/integrations/tools/azure_ai_services#azureaitexttospeechtool)
* Text Analytics for Health: [AzureAITextAnalyticsHealthTool](/oss/python/integrations/tools/azure_ai_services#azureaitextanalyticshealthtool)

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/providers/microsoft.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# NVIDIA
Source: https://docs.langchain.com/oss/python/integrations/providers/nvidia

Integrate with NVIDIA using LangChain Python.

LangChain and NVIDIA have partnered to accelerate agents through four mechanisms:

1. [Components](#components)
2. [LangGraph acceleration primitives](#accelerate-langgraph-with-nvidia)
3. [NeMo Agent Toolkit optimizations](#nemo-agent-toolkit-optimizations-with-langsmith-telemetry)
4. [Full Stack blueprints](#full-stack-blueprints)

## Components

The `langchain-nvidia-ai-endpoints` package provides LangChain integrations for chat, embeddings, reranking, and retrieval powered by NVIDIA AI—including [Nemotron](https://www.nvidia.com/en-us/ai-data-science/foundation-models/nemotron/), NVIDIA's open model family built for agentic AI, and hundreds of community models on the [NVIDIA API Catalog](https://build.nvidia.com/).

Models run on NVIDIA NIM microservices: container images that expose a standard OpenAI-compatible API, optimized with TensorRT-LLM for peak throughput on NVIDIA hardware. They can be accessed via the hosted API Catalog or self-hosted on-premises.

| Component     | Class                                                 | Description                                                     |
| :------------ | :---------------------------------------------------- | :-------------------------------------------------------------- |
| Chat          | [`ChatNVIDIA`](#chat-chatnvidia)                      | Chat completions with any NVIDIA-hosted model or local NIM      |
| Chat (Dynamo) | [`ChatNVIDIADynamo`](#chat-chatnvidiadynamo)          | `ChatNVIDIA` with KV cache routing hints for Dynamo deployments |
| Embeddings    | [`NVIDIAEmbeddings`](#embeddings-nvidiaembeddings)    | Dense vector embeddings for semantic search and RAG             |
| Reranking     | [`NVIDIARerank`](#reranking-nvidiarerank)             | Document reranking by query relevance                           |
| Retrieval     | [`NVIDIARAGRetriever`](#retrieval-nvidiaragretriever) | Retrieval from an NVIDIA RAG Blueprint server                   |

### Chat: ChatNVIDIA

`ChatNVIDIA` provides chat completions over NVIDIA-hosted models and local NIM deployments. It supports tool calling, structured output, image inputs, and streaming.

#### Install

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
pip install -qU langchain-nvidia-ai-endpoints
```

#### Access the NVIDIA API Catalog

1. Create a free account on the [NVIDIA API Catalog](https://build.nvidia.com/) and log in.
2. Click your profile icon, then **API Keys** > **Generate API Key**.
3. Copy and save the key as `NVIDIA_API_KEY`.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import getpass
import os

if os.environ.get("NVIDIA_API_KEY", "").startswith("nvapi-"):
    print("Valid NVIDIA_API_KEY already in environment. Delete to reset")
else:
    nvapi_key = getpass.getpass("NVAPI Key (starts with nvapi-): ")
    assert nvapi_key.startswith(
        "nvapi-"
    ), f"{nvapi_key[:5]}... is not a valid key"
    os.environ["NVIDIA_API_KEY"] = nvapi_key
```

#### Nemotron: featured models for agentic AI

[Nemotron](https://www.nvidia.com/en-us/ai-data-science/foundation-models/nemotron/) is NVIDIA's open model family designed for agentic AI. The models use a hybrid Mamba-Transformer mixture-of-experts architecture that delivers leading benchmark performance with high throughput and support for up to 1M token context windows. Nemotron model weights, training data, and implementation recipes are published openly under the NVIDIA Open Model License.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain_nvidia_ai_endpoints import ChatNVIDIA

# Nemotron 3 Super — efficient reasoning and agentic tasks
llm = ChatNVIDIA(model="nvidia/nemotron-3-super-120b-a12b")
result = llm.invoke("Plan a three-step research workflow for competitive analysis.")
print(result.content)
```

See the [`ChatNVIDIA` integration page](/oss/python/integrations/chat/nvidia_ai_endpoints) for full documentation including tool calling, multimodal inputs, and Nemotron-specific examples.

### Chat: ChatNVIDIADynamo

`ChatNVIDIADynamo` is a drop-in replacement for `ChatNVIDIA` for use with [NVIDIA Dynamo](https://developer.nvidia.com/dynamo) deployments. It automatically injects KV cache routing hints into every request, allowing the Dynamo scheduler to optimize memory allocation, load routing, and request priority.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain_nvidia_ai_endpoints import ChatNVIDIADynamo

llm = ChatNVIDIADynamo(
    base_url="http://localhost:8099/v1",
    model="nvidia/nemotron-3-super-120b-a12b",
    osl=512,             # expected output sequence length (tokens)
    iat=250,             # expected inter-arrival time (ms)
    latency_sensitivity=1.0,
    priority=1,
)
result = llm.invoke("Summarize KV cache routing in one sentence.")
print(result.content)
```

See the [`ChatNVIDIA` integration page](/oss/python/integrations/chat/nvidia_ai_endpoints#use-with-nvidia-dynamo) for the full `ChatNVIDIADynamo` reference including per-invocation overrides and streaming.

### Embeddings: NVIDIAEmbeddings

`NVIDIAEmbeddings` generates dense vector embeddings for use in semantic search and RAG pipelines.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain_nvidia_ai_endpoints import NVIDIAEmbeddings

embedder = NVIDIAEmbeddings(model="NV-Embed-QA")
embedder.embed_query("What's the temperature today?")
```

See the [`NVIDIAEmbeddings` integration page](/oss/python/integrations/embeddings/nvidia_ai_endpoints) for full documentation.

### Reranking: NVIDIARerank

`NVIDIARerank` reranks a list of documents by relevance to a query using a NeMo Retriever reranking NIM.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain_core.documents import Document
from langchain_nvidia_ai_endpoints import NVIDIARerank

ranker = NVIDIARerank(model="nvidia/llama-3.2-nv-rerankqa-1b-v1")
docs = ranker.compress_documents(
    query="What is GPU memory bandwidth?",
    documents=[Document(page_content=p) for p in passages],
)
```

### Retrieval: NVIDIARAGRetriever

`NVIDIARAGRetriever` connects LangChain to a running [NVIDIA RAG Blueprint](https://docs.nvidia.com/rag/latest/index.html) server and retrieves relevant documents via the `/v1/search` endpoint. It supports reranking, query rewriting, and metadata filtering.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain_nvidia_ai_endpoints import NVIDIARAGRetriever

retriever = NVIDIARAGRetriever(base_url="http://localhost:8081", k=4)
docs = retriever.invoke("What is NVIDIA NIM?")
```

See the [`NVIDIARAGRetriever` integration page](/oss/python/integrations/retrievers/nvidia) for full documentation.

### Self-host with NVIDIA NIM Microservices

When you are ready to deploy your AI application, you can self-host models with NVIDIA NIM. For more information, refer to [NVIDIA NIM Microservices](https://www.nvidia.com/en-us/ai-data-science/products/nim-microservices/).

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain_nvidia_ai_endpoints import ChatNVIDIA, NVIDIAEmbeddings, NVIDIARerank

# connect to a chat NIM running at localhost:8000, specifying a model
llm = ChatNVIDIA(base_url="http://localhost:8000/v1", model="nvidia/nemotron-3-super-120b-a12b")

# connect to an embedding NIM running at localhost:8080
embedder = NVIDIAEmbeddings(base_url="http://localhost:8080/v1")

# connect to a reranking NIM running at localhost:2016
ranker = NVIDIARerank(base_url="http://localhost:2016/v1")
```

## Accelerate LangGraph with NVIDIA

The `langchain-nvidia-langgraph` package provides NVIDIA-optimized execution strategies for LangGraph graphs. It offers two complementary optimizations applied at compile time:

* **Parallel execution**: independent nodes are automatically identified and run concurrently, eliminating unnecessary sequential bottlenecks.
* **Speculative execution**: both branches of a conditional edge run simultaneously; the wrong branch is discarded once the routing condition resolves.

Neither optimization requires changes to node logic or graph edges.

### Install

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
pip install -qU langchain-nvidia-langgraph
```

### Parallel execution

Replace `StateGraph` from LangGraph with `StateGraph` from `langchain_nvidia_langgraph.graph`. The rest of your graph definition stays the same.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain_nvidia_langgraph.graph import StateGraph, OptimizationConfig
from langgraph.graph import END
from typing import TypedDict

class AgentState(TypedDict):
  ...

graph = StateGraph(AgentState)
app = graph.compile(optimization=OptimizationConfig(enable_parallel=True))
```

Or wrap an existing `StateGraph`:

```
from langgraph.graph import StateGraph as LangGraphStateGraph
graph = LangGraphStateGraph(AgentState)
app = with_app_compile(graph).compile(optimization=OptimizationConfig(enable_parallel=True))
```

Decorators give explicit control over which nodes participate in optimization:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain_nvidia_langgraph.graph import sequential, depends_on, speculation_unsafe

# Prevent a node from being parallelized (e.g., it writes to shared state)
@sequential
def write_to_db(state):
    ...

# Declare a dependency not expressed in graph edges
@depends_on("write_to_db")
def next_action(state):
    ...
```

### Speculative execution

Enable speculation via `OptimizationConfig` at compile time. The executor runs conditional branches in parallel and keeps the result that matches the routing decision.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
app = graph.compile(optimization=OptimizationConfig(enable_speculation=True))
```

## NeMo Agent Toolkit Optimizations with LangSmith Telemetry

The NVIDIA NeMo Agent Toolkit is an open-source AI toolkit for building, profiling, and optimizing agents. Developers can use LangChain with NeMo Agent Toolkit with minimal code changes to enable profiling, evaluation, GPU capacity plans, and automated optimization. NeMo Agent Toolkit is interoperable with LangSmith.

* [Get Started with NeMo Agent Toolkit and LangChain](https://github.com/NVIDIA/NeMo-Agent-Toolkit/blob/develop/examples/frameworks/auto_wrapper/langchain_deep_research/langgraph_deep_research.ipynb)

* [Optimize LangChain with NeMo Agent Toolkit and LangSmith](https://github.com/NVIDIA/NeMo-Agent-Toolkit/blob/develop/docs/source/run-workflows/observe/observe-workflow-with-langsmith.md)

## Full Stack Blueprints

NVIDIA and LangChain have collaborated on [full stack examples](https://github.com/langchain-ai/deepagents/tree/main/examples) showing how all these components are combined for two enterprise use cases, with focus on production readiness:

* [NVIDIA AI-Q](https://github.com/NVIDIA-AI-Blueprints/aiq/tree/develop) is a blueprint for deep research across enterprise data sources using LangChain Deep Agents
* [NVIDIA VSS](https://github.com/NVIDIA-AI-Blueprints/video-search-and-summarization) is a blueprint for video search and summarization using LangChain and LangGraph

## Additional Resources

* [`langchain-nvidia-ai-endpoints` package README](https://github.com/langchain-ai/langchain-nvidia/blob/main/libs/ai-endpoints/README.md)
* [`langchain-nvidia-langgraph` package](https://github.com/langchain-ai/langchain-nvidia/tree/main/libs/langgraph)
* [Nemotron model family](https://www.nvidia.com/en-us/ai-data-science/foundation-models/nemotron/)
* [Overview of NVIDIA NIM for Large Language Models (LLMs)](https://docs.nvidia.com/nim/large-language-models/latest/introduction.html)
* [Overview of NeMo Retriever Embedding NIM](https://docs.nvidia.com/nim/nemo-retriever/text-embedding/latest/overview.html)
* [Overview of NeMo Retriever Reranking NIM](https://docs.nvidia.com/nim/nemo-retriever/text-reranking/latest/overview.html)
* [`ChatNVIDIA` Model](/oss/python/integrations/chat/nvidia_ai_endpoints)
* [`NVIDIAEmbeddings` Model for RAG Workflows](/oss/python/integrations/embeddings/nvidia_ai_endpoints)
* [`NVIDIARAGRetriever`](/oss/python/integrations/retrievers/nvidia)
* [NVIDIA Dynamo](https://developer.nvidia.com/dynamo)

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/providers/nvidia.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
