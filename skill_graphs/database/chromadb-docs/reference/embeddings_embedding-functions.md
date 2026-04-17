[Skip to main content](https://docs.trychroma.com/docs/embeddings/embedding-functions#content-area)
[Chroma Docs home page![light logo](https://mintcdn.com/chroma-8943dec5/wr97NKZIObCJm0cR/images/light-logo.svg?fit=max&auto=format&n=wr97NKZIObCJm0cR&q=85&s=4d021170bd60f2e52fcb7bc0d3eb0552)![dark logo](https://mintcdn.com/chroma-8943dec5/wr97NKZIObCJm0cR/images/dark-logo.svg?fit=max&auto=format&n=wr97NKZIObCJm0cR&q=85&s=a6f162fa88876846a979771be29f2a13)](https://docs.trychroma.com/)
Search...
Ctrl KAsk AI
  * [Dashboard](https://trychroma.com/login)
  * [Dashboard](https://trychroma.com/login)


Search...
Navigation
Embeddings
Embedding Functions
[](https://docs.trychroma.com/docs/overview/introduction)[](https://docs.trychroma.com/cloud/getting-started)[](https://docs.trychroma.com/guides/build/building-with-ai)[](https://docs.trychroma.com/integrations/chroma-integrations)[](https://docs.trychroma.com/reference/overview)
##### Overview
  * [Introduction](https://docs.trychroma.com/docs/overview/introduction)
  * [Getting Started](https://docs.trychroma.com/docs/overview/getting-started)
  * [Architecture](https://docs.trychroma.com/docs/overview/architecture)
  * [Open Source](https://docs.trychroma.com/docs/overview/oss)
  * [Migration](https://docs.trychroma.com/docs/overview/migration)
  * [Troubleshooting](https://docs.trychroma.com/docs/overview/troubleshooting)


##### Run Chroma
  * [Chroma Clients](https://docs.trychroma.com/docs/run-chroma/clients)
  * [Client-Server Mode](https://docs.trychroma.com/docs/run-chroma/client-server)


##### Collections
  * [Manage Collections](https://docs.trychroma.com/docs/collections/manage-collections)
  * [Add Data](https://docs.trychroma.com/docs/collections/add-data)
  * [Update Data](https://docs.trychroma.com/docs/collections/update-data)
  * [Delete Data](https://docs.trychroma.com/docs/collections/delete-data)
  * [Configure Collections](https://docs.trychroma.com/docs/collections/configure)


##### Querying Collections
  * [Query and Get](https://docs.trychroma.com/docs/querying-collections/query-and-get)
  * [Metadata Filtering](https://docs.trychroma.com/docs/querying-collections/metadata-filtering)
  * [Full Text Search](https://docs.trychroma.com/docs/querying-collections/full-text-search)


##### Embeddings
  * [Embedding Functions](https://docs.trychroma.com/docs/embeddings/embedding-functions)
  * [Multimodal Embeddings](https://docs.trychroma.com/docs/embeddings/multimodal)


##### CLI
  * [Installing the CLI](https://docs.trychroma.com/docs/cli/install)
  * [Browse Collections](https://docs.trychroma.com/docs/cli/browse)
  * [Copy Collections](https://docs.trychroma.com/docs/cli/copy)
  * [DB Management](https://docs.trychroma.com/docs/cli/db)
  * [Sample Apps](https://docs.trychroma.com/docs/cli/sample-apps)
  * [Login](https://docs.trychroma.com/docs/cli/login)
  * [Profile Management](https://docs.trychroma.com/docs/cli/profile)
  * [Run a Chroma Server](https://docs.trychroma.com/docs/cli/run)
  * [Update](https://docs.trychroma.com/docs/cli/update)
  * [Vacuum](https://docs.trychroma.com/docs/cli/vacuum)


On this page
  * [Default: all-MiniLM-L6-v2](https://docs.trychroma.com/docs/embeddings/embedding-functions#default-all-minilm-l6-v2)
  * [Using Embedding Functions](https://docs.trychroma.com/docs/embeddings/embedding-functions#using-embedding-functions)
  * [Custom Embedding Functions](https://docs.trychroma.com/docs/embeddings/embedding-functions#custom-embedding-functions)


Embeddings
# Embedding Functions
Copy page
Learn how to use embedding functions in Chroma to create vector representations of your data.
Copy page
Embeddings are the way to represent any kind of data, making them the perfect fit for working with all kinds of AI-powered tools and algorithms. They can represent text, images, and soon audio and video. Chroma collections index embeddings to enable efficient similarity search on the data they represent. There are many options for creating embeddings, whether locally using an installed library, or by calling an API. Chroma provides lightweight wrappers around popular embedding providers, making it easy to use them in your apps. You can set an embedding function when you [create](https://docs.trychroma.com/docs/collections/manage-collections) a Chroma collection, to be automatically used when adding and querying data, or you can call them directly yourself.
| Python | Typescript
---|---|---
[Cloudflare Workers AI](https://docs.trychroma.com/integrations/embedding-models/cloudflare-workers-ai) | ✓ | ✓
[Cohere](https://docs.trychroma.com/integrations/embedding-models/cohere) | ✓ | ✓
[Google Generative AI](https://docs.trychroma.com/integrations/embedding-models/google-gemini) | ✓ | ✓
[Hugging Face](https://docs.trychroma.com/integrations/embedding-models/hugging-face) | ✓ | -
[Hugging Face Embedding Server](https://docs.trychroma.com/integrations/embedding-models/hugging-face-server) | ✓ | ✓
[Jina AI](https://docs.trychroma.com/integrations/embedding-models/jina-ai) | ✓ | ✓
[Mistral](https://docs.trychroma.com/integrations/embedding-models/mistral) | ✓ | ✓
[Morph](https://docs.trychroma.com/integrations/embedding-models/morph) | ✓ | ✓
[OpenAI](https://docs.trychroma.com/integrations/embedding-models/openai) | ✓ | ✓
[Sentence Transformers](https://docs.trychroma.com/integrations/embedding-models/sentence-transformer) | ✓ | ✓
[Together AI](https://docs.trychroma.com/integrations/embedding-models/together-ai) | ✓ | ✓
For TypeScript users, Chroma provides packages for a number of embedding model providers. The Chromadb python package ships with all embedding functions included.
Provider | Embedding Function Package
---|---
All (installs all packages) |
Cloudflare Workers AI |
Cohere |
Google Gemini |
Hugging Face Server |
Jina |
Mistral |
Morph |
Ollama |
OpenAI |
Perplexity |
Qwen (via Chroma Cloud) |
Sentence Transformers |
Together AI |
Voyage AI |
We welcome pull requests to add new Embedding Functions to the community.
* * *
##
[​](https://docs.trychroma.com/docs/embeddings/embedding-functions#default-all-minilm-l6-v2)
Default: all-MiniLM-L6-v2
Chroma’s default embedding function uses the If you don’t specify an embedding function when creating a collection, Chroma will set it to be the `DefaultEmbeddingFunction`:
Report incorrect code
Copy
Ask AI
```
collection = client.create_collection(name="my_collection")

```

##
[​](https://docs.trychroma.com/docs/embeddings/embedding-functions#using-embedding-functions)
Using Embedding Functions
Embedding functions can be linked to a collection and used whenever you call `add`, `update`, `upsert` or `query`.
Report incorrect code
Copy
Ask AI
```
# Set your OPENAI_API_KEY environment variable
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction

collection = client.create_collection(
    name="my_collection",
    embedding_function=OpenAIEmbeddingFunction(
        model_name="text-embedding-3-small"
    )
)

# Chroma will use OpenAIEmbeddingFunction to embed your documents
collection.add(
    ids=["id1", "id2"],
    documents=["doc1", "doc2"]
)

```

You can also use embedding functions directly which can be handy for debugging.
Report incorrect code
Copy
Ask AI
```
from chromadb.utils.embedding_functions import DefaultEmbeddingFunction

default_ef = DefaultEmbeddingFunction()
embeddings = default_ef(["foo"])
print(embeddings) # [[0.05035809800028801, 0.0626462921500206, -0.061827320605516434...]]

collection.query(query_embeddings=embeddings)

```

##
[​](https://docs.trychroma.com/docs/embeddings/embedding-functions#custom-embedding-functions)
Custom Embedding Functions
You can create your own embedding function to use with Chroma; it just needs to implement `EmbeddingFunction`.
Report incorrect code
Copy
Ask AI
```
from typing import Dict, Any
from chromadb import Documents, EmbeddingFunction, Embeddings
from chromadb.utils.embedding_functions import register_embedding_function

@register_embedding_function
class MyEmbeddingFunction(EmbeddingFunction):

    def __init__(self, model):
        self.model = model

    def __call__(self, input: Documents) -> Embeddings:
        # embed the documents somehow
        return embeddings

    @staticmethod
    def name() -> str:
        return "my-ef"

    def get_config(self) -> Dict[str, Any]:
        return dict(model=self.model)

    @staticmethod
    def build_from_config(config: Dict[str, Any]) -> "EmbeddingFunction":
        return MyEmbeddingFunction(config['model'])

```

We welcome contributions! If you create an embedding function that you think would be useful to others, please consider
##
[​](https://docs.trychroma.com/docs/embeddings/embedding-functions#default-all-minilm-l6-v2-2)
Default: all-MiniLM-L6-v2
Chroma’s default embedding function uses the `all-MiniLM-L6-v2` model to create embeddings. This embedding model can create sentence and document embeddings that can be used for a wide variety of tasks. This embedding function runs locally on your machine, and may require you to download the model files (this will happen automatically).If you don’t specify an embedding function when creating a collection, install the `@chroma-core/default-embed` package:
npm
pnpm
bun
yarn
Report incorrect code
Copy
Ask AI
```
npm install @chroma-core/default-embed

```

Create a collection without providing an embedding function. It will automatically be set with the `DefaultEmbeddingFunction`:
Report incorrect code
Copy
Ask AI
```
const collection = await client.createCollection({ name: "my-collection" });

```

##
[​](https://docs.trychroma.com/docs/embeddings/embedding-functions#using-embedding-functions-2)
Using Embedding Functions
Embedding functions can be linked to a collection and used whenever you call `add`, `update`, `upsert` or `query`.Install the `@chroma-core/openai` package:
npm
pnpm
bun
yarn
Report incorrect code
Copy
Ask AI
```
npm install @chroma-core/openai

```

Create a collection with the `OpenAIEmbeddingFunction`:
Report incorrect code
Copy
Ask AI
```
// Set your OPENAI_API_KEY environment variable
import { OpenAIEmbeddingFunction } from "@chroma-core/openai";

collection = await client.createCollection({
  name: "my_collection",
  embedding_function: new OpenAIEmbeddingFunction({
    modelName: "text-embedding-3-small",
  }),
});

// Chroma will use OpenAIEmbeddingFunction to embed your documents
await collection.add({
  ids: ["id1", "id2"],
  documents: ["doc1", "doc2"],
});

```

You can also use embedding functions directly which can be handy for debugging.
Report incorrect code
Copy
Ask AI
```
import { DefaultEmbeddingFunction } from "@chroma-core/default-embed";

const defaultEF = new DefaultEmbeddingFunction();
const embeddings = await defaultEF.generate(["foo"]);
console.log(embeddings); // [[0.05035809800028801, 0.0626462921500206, -0.061827320605516434...]]

await collection.query({ queryEmbeddings: embeddings });

```

##
[​](https://docs.trychroma.com/docs/embeddings/embedding-functions#custom-embedding-functions-2)
Custom Embedding Functions
You can create your own embedding function to use with Chroma; it just needs to implement `EmbeddingFunction`.
Report incorrect code
Copy
Ask AI
```
export interface MyEmbeddingConfig {
  model: string;
}

export class MyEmbeddingFunction implements EmbeddingFunction {
  public readonly name = "my-embedding-function";
  private readonly model: string;

  constructor(args: { model: string }) {
    this.model = args.model;
  }

  async generate(texts: string[]): Promise<number[][]> {
    // embed the documents somehow
    return [];
  }

  getConfig(): MyEmbeddingConfig {
    return {
      model: this.model,
    };
  }

  validateConfigUpdate(config: Record<string, any>) {
    if ("model" in config) {
      throw new ChromaValueError("Model cannot be updated");
    }
  }

  static buildFromConfig(
    config: MyEmbeddingConfig,
    _client?: ChromaClient,
  ): MyEmbeddingFunction {
    return new MyEmbeddingFunction(config);
  }
}

```

We welcome contributions! If you create an embedding function that you think would be useful to others, please consider
The Rust client expects embeddings to be provided directly. Use your provider SDK to generate embeddings, then pass them to `add`, `query`, and other methods.
Report incorrect code
Copy
Ask AI
```
let embeddings = vec![vec![0.05, 0.06, -0.06]];

collection
    .add(
        vec!["id1".to_string()],
        embeddings,
        Some(vec![Some("doc1".to_string())]),
        None,
        None,
    )
    .await?;

```

Was this page helpful?
YesNo
[ Full Text Search Previous ](https://docs.trychroma.com/docs/querying-collections/full-text-search)[ Multimodal Embeddings Next ](https://docs.trychroma.com/docs/embeddings/multimodal)
Ctrl+I
[Chroma Docs home page![light logo](https://mintcdn.com/chroma-8943dec5/wr97NKZIObCJm0cR/images/light-logo.svg?fit=max&auto=format&n=wr97NKZIObCJm0cR&q=85&s=4d021170bd60f2e52fcb7bc0d3eb0552)![dark logo](https://mintcdn.com/chroma-8943dec5/wr97NKZIObCJm0cR/images/dark-logo.svg?fit=max&auto=format&n=wr97NKZIObCJm0cR&q=85&s=a6f162fa88876846a979771be29f2a13)](https://docs.trychroma.com/)
[Enterprise](https://trychroma.com/enterprise)[Pricing](https://trychroma.com/pricing)[Changelog](https://trychroma.com/changelog)
Assistant
Responses are generated using AI and may contain mistakes.
