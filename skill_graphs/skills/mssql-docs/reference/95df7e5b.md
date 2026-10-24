# Intelligent applications and AI
Feedback
Summarize this article for me
##  In this article
  1. [Overview](https://learn.microsoft.com/en-us/sql/sql-server/ai/artificial-intelligence-intelligent-applications?view=sql-server-ver17#overview)
  2. [Key concepts for implementing RAG with Azure OpenAI](https://learn.microsoft.com/en-us/sql/sql-server/ai/artificial-intelligence-intelligent-applications?view=sql-server-ver17#key-concepts-for-implementing-rag-with-azure-openai)
  3. [Azure OpenAI](https://learn.microsoft.com/en-us/sql/sql-server/ai/artificial-intelligence-intelligent-applications?view=sql-server-ver17#azure-openai)
  4. [Vector examples](https://learn.microsoft.com/en-us/sql/sql-server/ai/artificial-intelligence-intelligent-applications?view=sql-server-ver17#vector-examples)
  5. [Azure AI Search](https://learn.microsoft.com/en-us/sql/sql-server/ai/artificial-intelligence-intelligent-applications?view=sql-server-ver17#azure-ai-search)
  6. [Intelligent applications](https://learn.microsoft.com/en-us/sql/sql-server/ai/artificial-intelligence-intelligent-applications?view=sql-server-ver17#intelligent-applications)
  7. [Related content](https://learn.microsoft.com/en-us/sql/sql-server/ai/artificial-intelligence-intelligent-applications?view=sql-server-ver17#related-content)

Show 3 more
**Applies to:** ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) SQL Server 2025 (17.x) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [Azure SQL Database](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [Azure SQL Managed Instance](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [SQL database in Microsoft Fabric](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to)
This article provides an overview of using artificial intelligence (AI) options, such as OpenAI and vectors, to build intelligent applications with the SQL Database Engine in SQL Server and Azure SQL Managed Instance.
For Azure SQL Database, review [Intelligent applications and AI](https://learn.microsoft.com/en-us/azure/azure-sql/database/ai-artificial-intelligence-intelligent-applications).
For samples and examples, visit the
[](https://learn.microsoft.com/en-us/sql/sql-server/ai/artificial-intelligence-intelligent-applications?view=sql-server-ver17#overview)
## Overview
Large language models (LLMs) enable developers to create AI-powered applications with a familiar user experience.
Using LLMs in applications brings greater value and an improved user experience when the models can access the right data, at the right time, from your application's database. This process is known as Retrieval Augmented Generation (RAG) and the SQL Database Engine has many features that support this new pattern, making it a great database to build intelligent applications.
The following links provide sample code of various options to build intelligent applications:
Expand table
AI Option | Description
---|---
**[Azure OpenAI](https://learn.microsoft.com/en-us/sql/sql-server/ai/artificial-intelligence-intelligent-applications?view=sql-server-ver17#azure-openai)** | Generate embeddings for RAG and integrate with any model supported by Azure OpenAI.
**[Vectors](https://learn.microsoft.com/en-us/sql/sql-server/ai/artificial-intelligence-intelligent-applications?view=sql-server-ver17#vectors)** | Learn how to store vectors and use vector functions in the database.
**[Azure AI Search](https://learn.microsoft.com/en-us/sql/sql-server/ai/artificial-intelligence-intelligent-applications?view=sql-server-ver17#azure-ai-search)** | Use your database together with Azure AI Search to train LLM on your data.
**[Intelligent applications](https://learn.microsoft.com/en-us/sql/sql-server/ai/artificial-intelligence-intelligent-applications?view=sql-server-ver17#intelligent-applications)** | Learn how to create an end-to-end solution using a common pattern that can be replicated in any scenario.
[](https://learn.microsoft.com/en-us/sql/sql-server/ai/artificial-intelligence-intelligent-applications?view=sql-server-ver17#key-concepts-for-implementing-rag-with-azure-openai)
## Key concepts for implementing RAG with Azure OpenAI
This section includes key concepts that are critical to implement RAG with Azure OpenAI in the SQL Database Engine.
[](https://learn.microsoft.com/en-us/sql/sql-server/ai/artificial-intelligence-intelligent-applications?view=sql-server-ver17#retrieval-augmented-generation-rag)
### Retrieval Augmented Generation (RAG)
RAG is a technique that enhances the LLM's ability to produce relevant and informative responses by retrieving additional data from external sources. For example, RAG can query articles or documents that contain domain-specific knowledge related to the user's question or prompt. The LLM can then use this retrieved data as a reference when generating its response. For example, a simple RAG pattern using the SQL Database Engine could be:
  1. Insert data into a table.
  2. Link your instance to Azure AI Search.
  3. Create an Azure OpenAI GPT4 model and connect it to Azure AI Search.
  4. Chat and ask questions about your data using the trained Azure OpenAI model from your application and from data in your instance.


The RAG pattern, with prompt engineering, serves the purpose of enhancing response quality by offering more contextual information to the model. RAG enables the model to apply a broader knowledgebase by incorporating relevant external sources into the generation process, resulting in more comprehensive and informed responses. For more information on _grounding_ LLMs, see [Grounding LLMs - Microsoft Community Hub](https://techcommunity.microsoft.com/blog/fasttrackforazureblog/grounding-llms/3843857).
[](https://learn.microsoft.com/en-us/sql/sql-server/ai/artificial-intelligence-intelligent-applications?view=sql-server-ver17#prompts-and-prompt-engineering)
### Prompts and prompt engineering
A prompt refers to specific text or information that serves as an instruction to an LLM, or as contextual data that the LLM can build upon. A prompt can take various forms, such as a question, a statement, or even a code snippet.
Sample prompts that can be used to generate a response from an LLM:
  * **Instructions** : provide directives to the LLM
  * **Primary content** : gives information to the LLM for processing
  * **Examples** : help condition the model to a particular task or process
  * **Cues** : direct the LLM's output in the right direction
  * **Supporting content** : represents supplemental information the LLM can use to generate output


The process of creating good prompts for a scenario is called _prompt engineering_. For more information about prompts and best practices for prompt engineering, see [Prompt engineering techniques](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/prompt-engineering).
[](https://learn.microsoft.com/en-us/sql/sql-server/ai/artificial-intelligence-intelligent-applications?view=sql-server-ver17#tokens)
### Tokens
Tokens are small chunks of text generated by splitting the input text into smaller segments. These segments can either be words or groups of characters, varying in length from a single character to an entire word. For instance, the word `hamburger` would be divided into tokens such as `ham`, `bur`, and `ger` while a short and common word like `pear` would be considered a single token.
In Azure OpenAI, input text provided to the API is turned into tokens (tokenized). The number of tokens processed in each API request depends on factors such as the length of the input, output, and request parameters. The quantity of tokens being processed also impacts the response time and throughput of the models. There are limits to the number of tokens each model can take in a single request/response from Azure OpenAI. To learn more, see [Azure OpenAI in Azure AI Foundry Models quotas and limits](https://learn.microsoft.com/en-us/azure/ai-services/openai/quotas-limits).
[](https://learn.microsoft.com/en-us/sql/sql-server/ai/artificial-intelligence-intelligent-applications?view=sql-server-ver17#vectors)
### Vectors
Vectors are ordered arrays of numbers (typically floats) that can represent information about some data. For example, an image can be represented as a vector of pixel values, or a string of text can be represented as a vector of ASCII values. The process to turn data into a vector is called _vectorization_. For more information, see [Vector examples](https://learn.microsoft.com/en-us/sql/sql-server/ai/artificial-intelligence-intelligent-applications?view=sql-server-ver17#vector-examples).
Working with vector data is easier with the introduction of the [vector data type](https://learn.microsoft.com/en-us/sql/t-sql/data-types/vector-data-type?view=azuresqldb-mi-current&preserve-view=true) and [vector functions](https://learn.microsoft.com/en-us/sql/t-sql/functions/vector-functions-transact-sql?view=azuresqldb-mi-current&preserve-view=true).
[](https://learn.microsoft.com/en-us/sql/sql-server/ai/artificial-intelligence-intelligent-applications?view=sql-server-ver17#embeddings)
### Embeddings
Embeddings are vectors that represent important features of data. Embeddings are often learned by using a deep learning model, and machine learning and AI models utilize them as features. Embeddings can also capture semantic similarity between similar concepts. For example, in generating an embedding for the words `person` and `human`, we would expect their embeddings (vector representation) to be similar in value since the words are also semantically similar.
Azure OpenAI features models to create embeddings from text data. The service breaks text out into tokens and generates embeddings using models pretrained by OpenAI. To learn more, see [Understand embeddings in Azure OpenAI in Azure AI Foundry Models](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/understand-embeddings).
[](https://learn.microsoft.com/en-us/sql/sql-server/ai/artificial-intelligence-intelligent-applications?view=sql-server-ver17#vector-search)
### Vector search
Vector search refers to the process of finding all vectors in a dataset that are semantically similar to a specific query vector. Therefore, a query vector for the word `human` searches the entire dictionary for semantically similar words, and should find the word `person` as a close match. This closeness, or distance, is measured using a similarity metric such as cosine similarity. The closer vectors are in similarity, the smaller is the distance between them.
Consider a scenario where you run a query over millions of document to find the most similar documents in your data. You can create embeddings for your data and query documents using Azure OpenAI. Then, you can perform a vector search to find the most similar documents from your dataset. However, performing a vector search across a few examples is trivial. Performing this same search across thousands, or millions, of data points becomes challenging. There are also trade-offs between exhaustive search and approximate nearest neighbor (ANN) search methods including latency, throughput, accuracy, and cost, all of which depends on the requirements of your application.
Vectors in the SQL Database Engine can be efficiently stored and queried, as described in the next sections, allowing exact nearest neighbor search with great performance. You don't have to decide between accuracy and speed: you can have both. Storing vector embeddings alongside the data in an integrated solution minimizes the need to manage data synchronization and accelerates your time-to-market for AI application development.
[](https://learn.microsoft.com/en-us/sql/sql-server/ai/artificial-intelligence-intelligent-applications?view=sql-server-ver17#azure-openai)
## Azure OpenAI
Embedding is the process of representing the real world as data. Text, images, or sounds can be converted into embeddings. Azure OpenAI models are able to transform real-world information into embeddings. The models are available as REST endpoints and thus can easily be consumed from the SQL Database Engine using the [sp_invoke_external_rest_endpoint](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-invoke-external-rest-endpoint-transact-sql?view=sql-server-ver17) system stored procedure, available starting in SQL Server 2025 (17.x) and Azure SQL Managed Instance configured with the [Always-up-to-date update policy](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/update-policy#always-up-to-date-update-policy).
SQL
Copy
```
DECLARE @retval AS INT,
        @response AS NVARCHAR (MAX),
        @payload AS NVARCHAR (MAX);

SET @payload = JSON_OBJECT('input':@text);

EXECUTE
    @retval = sp_invoke_external_rest_endpoint
    @url = 'https://<openai-url>/openai/deployments/<model-name>/embeddings?api-version = 2023-03-15-preview',
    @method = 'POST',
    @credential = [https://<openai-url>/openai/deployments/<model-name>],
    @payload = @payload,
    @response = @response OUTPUT;

DECLARE @e AS VECTOR(1536) = JSON_QUERY(@response, '$.result.data[0].embedding');

```

Using a call to a REST service to get embeddings is just one of the integration options you have when working with SQL Managed Instance and OpenAI. You can let any of the [available models](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/models) access data stored in the SQL Database Engine to create solutions where your users can interact with the data, such as the following example:
![Screenshot of an AI bot answering the question using data stored in SQL Server.](https://learn.microsoft.com/en-us/sql/sql-server/media/ai-artificial-intelligence-intelligent-applications/data-chatbot.png?view=sql-server-ver17)
For additional examples on using Azure SQL and OpenAI, see the following articles, which also apply to SQL Server and Azure SQL Managed Instance:
  * [Generate images with Azure OpenAI Service (DALL-E) and Azure SQL](https://devblogs.microsoft.com/azure-sql/generate-images-with-openai-and-azure-sql/)
  * [Using OpenAI REST Endpoints with Azure SQL](https://devblogs.microsoft.com/azure-sql/using-openai-rest-endpoints-with-azure-sql-database/)


[](https://learn.microsoft.com/en-us/sql/sql-server/ai/artificial-intelligence-intelligent-applications?view=sql-server-ver17#vector-examples)
## Vector examples
The dedicated **vector** data type allows for efficient and optimized storing of vector data, and comes with a set of functions to help developers streamline vector and similarity search implementation. Calculating distance between two vectors can be done in one line of code using the new `VECTOR_DISTANCE` function. For more information and examples, review [Vector search and vector indexes in the SQL Database Engine](https://learn.microsoft.com/en-us/sql/sql-server/ai/vectors?view=sql-server-ver17).
For example:
SQL
Copy
```
CREATE TABLE [dbo].[wikipedia_articles_embeddings_titles_vector]
(
    [article_id] [int] NOT NULL,
    [embedding] [vector](1536) NOT NULL,
)
GO

SELECT TOP(10)
    *
FROM
    [dbo].[wikipedia_articles_embeddings_titles_vector]
ORDER BY
    VECTOR_DISTANCE('cosine', @my_reference_vector, embedding)

```

[](https://learn.microsoft.com/en-us/sql/sql-server/ai/artificial-intelligence-intelligent-applications?view=sql-server-ver17#azure-ai-search)
## Azure AI Search
Implement RAG-patterns with the SQL Database Engine and Azure AI Search. You can run supported chat models on data stored in the SQL Database Engine, without having to train or fine-tune models, thanks to the integration of Azure AI Search with Azure OpenAI and the SQL Database Engine. Running models on your data enables you to chat on top of, and analyze, your data with greater accuracy and speed.
To learn more about the integration of Azure AI Search with Azure OpenAI and the SQL Database Engine, see the following articles, which also apply to SQL Server and Azure SQL Managed Instance:
  * [Azure OpenAI on your data](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/use-your-data)
  * [Retrieval Augmented Generation (RAG) in Azure AI Search](https://learn.microsoft.com/en-us/azure/search/retrieval-augmented-generation-overview)
  * [Vector Search with Azure SQL and Azure AI Search](https://devblogs.microsoft.com/azure-sql/vector-search-with-azure-sql-database/)


[](https://learn.microsoft.com/en-us/sql/sql-server/ai/artificial-intelligence-intelligent-applications?view=sql-server-ver17#intelligent-applications)
## Intelligent applications
The SQL Database Engine can be used to build intelligent applications that include AI features, such as recommenders, and Retrieval Augmented Generation (RAG) as the following diagram demonstrates:
[ ![Diagram of different AI features to build intelligent applications with Azure SQL Database.](https://learn.microsoft.com/en-us/sql/sql-server/media/ai-artificial-intelligence-intelligent-applications/session-recommender-architecture.png?view=sql-server-ver17) ](https://learn.microsoft.com/en-us/sql/sql-server/media/ai-artificial-intelligence-intelligent-applications/session-recommender-architecture.png?view=sql-server-ver17#lightbox)
For an end-to-end sample to build an AI-enabled application using sessions abstract as a sample dataset, see:
  * [How I built a session recommender in 1 hour using OpenAI](https://devblogs.microsoft.com/azure-sql/how-i-built-a-session-recommender-in-1-hour-using-open-ai/).


LangChain integration and Semantic Kernel integration rely on the [vector data type](https://learn.microsoft.com/en-us/sql/t-sql/data-types/vector-data-type?view=sql-server-ver17), which is available starting with SQL Server 2025 (17.x) and in Azure SQL Managed Instance configured with the [Always-up-to-date or SQL Server 2025 update policy](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/update-policy), Azure SQL Database, and SQL database in Microsoft Fabric.
[](https://learn.microsoft.com/en-us/sql/sql-server/ai/artificial-intelligence-intelligent-applications?view=sql-server-ver17#langchain-integration)
### LangChain integration
LangChain is a well-known framework for developing applications powered by language models. For examples that show how LangChain can be used to create a Chatbot on your own data, see:
A few of samples on using Azure SQL with LangChain:
End-to-end examples:
  * [Build a chatbot on your own data in 1 hour with Azure SQL, Langchain, and Chainlit](https://devblogs.microsoft.com/azure-sql/build-a-chatbot-on-your-own-data-in-1-hour-with-azure-sql-langchain-and-chainlit/): Build a chatbot using the RAG pattern on your own data using Langchain for orchestrating LLM calls and Chainlit for the UI.


[](https://learn.microsoft.com/en-us/sql/sql-server/ai/artificial-intelligence-intelligent-applications?view=sql-server-ver17#semantic-kernel-integration)
### Semantic Kernel integration
[Semantic Kernel is an open-source SDK](https://learn.microsoft.com/en-us/semantic-kernel/overview/) that lets you easily build agents that can call your existing code. As a highly extensible SDK, you can use Semantic Kernel with models from OpenAI, Azure OpenAI, Hugging Face, and more. By combining your existing C#, Python, and Java code with these models, you can build agents that answer questions and automate processes.
  * [Microsoft.SemanticKernel.Connectors.SqlServer](https://learn.microsoft.com/en-us/dotnet/api/microsoft.semantickernel.connectors.sqlserver)


An example of how easily Semantic Kernel helps to build AI-enabled solutions is here:
  * [The ultimate chatbot?](https://devblogs.microsoft.com/azure-sql/the-ultimate-chatbot/): Build a chatbot on your own data using both NL2SQL and RAG patterns for the ultimate user experience.


[](https://learn.microsoft.com/en-us/sql/sql-server/ai/artificial-intelligence-intelligent-applications?view=sql-server-ver17#related-content)
## Related content
  * [Intelligent applications and AI Frequently Asked Questions (FAQ)](https://learn.microsoft.com/en-us/sql/sql-server/ai/artificial-intelligence-intelligent-applications-faq?view=sql-server-ver17)
  * [Vector and embeddings: Frequently asked questions (FAQ)](https://learn.microsoft.com/en-us/sql/sql-server/ai/vectors-faq?view=sql-server-ver17)
  * [Create and deploy an Azure OpenAI Service resource](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/create-resource?pivots=web-portal)
  * [Embeddings models](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/models#embeddings-models)


* * *
## Feedback
Was this page helpful?
Yes No No
Need help with this topic?
Want to try using Ask Learn to clarify or guide you through this topic?
Ask Learn Ask Learn
Suggest a fix?
* * *
##  Additional resources
  * [ What Is SQL Server? - SQL Server ](https://learn.microsoft.com/en-us/sql/sql-server/what-is-sql-server?source=recommendations)
An overview of the relational database engine and components of SQL Server
  * [ Databases - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/databases/databases?source=recommendations)
Learn about database schemas, tables, filegroups, logins, and roles. See how you can use the SQL Server Management Studio tool to work with databases.
  * [ How to Contribute to SQL Server Documentation - SQL Server ](https://learn.microsoft.com/en-us/sql/sql-server/sql-server-docs-contribute?source=recommendations)
How to contribute to SQL Server Documentation
  * [ Connect to the SQL Server Database Engine - SQL Server ](https://learn.microsoft.com/en-us/sql/sql-server/connect-to-database-engine?source=recommendations)
Learn how to connect to the Database Engine used by SQL Server and Azure SQL services
  * [ Intelligent Applications and AI - SQL Server ](https://learn.microsoft.com/en-us/sql/sql-server/artificial-intelligence-intelligent-applications?source=recommendations)
Use AI options such as OpenAI and vectors to build intelligent applications with SQL Server and Azure SQL Managed Instance.
  * [ What's New in SQL Server 2022 - SQL Server ](https://learn.microsoft.com/en-us/sql/sql-server/what-s-new-in-sql-server-2022?source=recommendations)
Learn about new features for SQL Server 2022 (16.x), which gives you choices of development languages, data types, environments, and operating systems.
  * [ SQL Tools Overview - SQL Server ](https://learn.microsoft.com/en-us/sql/tools/overview-sql-tools?source=recommendations)
SQL query and management tools for SQL Server, Azure SQL (Azure SQL database, Azure SQL managed instance, SQL virtual machines), and Azure Synapse Analytics.


Show 4 more
Mar 8, 4 PM - Mar 8, 4 PM
Experiment with what's next in AI-driven apps and agent design
* * *
  * Last updated on 02/25/2026


##  In this article
  1. [Overview](https://learn.microsoft.com/en-us/sql/sql-server/ai/artificial-intelligence-intelligent-applications?view=sql-server-ver17#overview)
  2. [Key concepts for implementing RAG with Azure OpenAI](https://learn.microsoft.com/en-us/sql/sql-server/ai/artificial-intelligence-intelligent-applications?view=sql-server-ver17#key-concepts-for-implementing-rag-with-azure-openai)
  3. [Azure OpenAI](https://learn.microsoft.com/en-us/sql/sql-server/ai/artificial-intelligence-intelligent-applications?view=sql-server-ver17#azure-openai)
  4. [Vector examples](https://learn.microsoft.com/en-us/sql/sql-server/ai/artificial-intelligence-intelligent-applications?view=sql-server-ver17#vector-examples)
  5. [Azure AI Search](https://learn.microsoft.com/en-us/sql/sql-server/ai/artificial-intelligence-intelligent-applications?view=sql-server-ver17#azure-ai-search)
  6. [Intelligent applications](https://learn.microsoft.com/en-us/sql/sql-server/ai/artificial-intelligence-intelligent-applications?view=sql-server-ver17#intelligent-applications)
  7. [Related content](https://learn.microsoft.com/en-us/sql/sql-server/ai/artificial-intelligence-intelligent-applications?view=sql-server-ver17#related-content)


Was this page helpful?
Yes No No
Need help with this topic?
Want to try using Ask Learn to clarify or guide you through this topic?
Ask Learn Ask Learn
Suggest a fix?
##
Ask Learn
Preview
Ask Learn is an AI assistant that can answer questions, clarify concepts, and define terms using trusted Microsoft documentation.
Please sign in to use Ask Learn.
[ Sign in ](https://learn.microsoft.com/en-us/sql/sql-server/ai/artificial-intelligence-intelligent-applications?view=sql-server-ver17)
[English (United States)](https://learn.microsoft.com/en-us/locale?target=https%3A%2F%2Flearn.microsoft.com%2Fen-us%2Fsql%2Fsql-server%2Fai%2Fartificial-intelligence-intelligent-applications%3Fview%3Dsql-server-ver17)
Theme
  * Light
  * Dark
  * High contrast


  * [AI Disclaimer](https://learn.microsoft.com/en-us/principles-for-ai-generated-content)
  * [Previous Versions](https://learn.microsoft.com/en-us/previous-versions/)
  * [Blog](https://techcommunity.microsoft.com/t5/microsoft-learn-blog/bg-p/MicrosoftLearnBlog)
  * [Contribute](https://learn.microsoft.com/en-us/contribute)
  * [Privacy](https://go.microsoft.com/fwlink/?LinkId=521839)
  * [Consumer Health Privacy](https://go.microsoft.com/fwlink/?linkid=2259814)
  * [Terms of Use](https://learn.microsoft.com/en-us/legal/termsofuse)
  * [Trademarks](https://www.microsoft.com/legal/intellectualproperty/Trademarks/)
  * © Microsoft 2026
