# Cohere
Source: https://docs.trychroma.com/integrations/embedding-models/cohere

Chroma provides a convenient wrapper around Cohere's embedding API. This embedding function runs remotely on Cohere's servers, and requires an API key. You can get an API key by signing up for an account at [Cohere](https://dashboard.cohere.ai/welcome/register).

<Tabs>
  <Tab title="Python" icon="python">
    This embedding function relies on the `cohere` python package, which you can install with `pip install cohere`.

    ```python theme={null}
    import chromadb.utils.embedding_functions as embedding_functions
    cohere_ef  = embedding_functions.CohereEmbeddingFunction(api_key="YOUR_API_KEY",  model_name="large")
    cohere_ef(input=["document1","document2"])
    ```
  </Tab>

  <Tab title="TypeScript" icon="js">
    ```typescript theme={null}
    // npm install @chroma-core/cohere

    import { CohereEmbeddingFunction } from "@chroma-core/cohere";

    const embedder = new CohereEmbeddingFunction({ apiKey: "apiKey" });

    // use directly
    const embeddings = embedder.generate(["document1", "document2"]);

    // pass documents to query for .add and .query
    const collection = await client.createCollection({
        name: "name",
        embeddingFunction: embedder,
    });
    const collectionGet = await client.getCollection({
        name: "name",
        embeddingFunction: embedder,
    });
    ```
  </Tab>
</Tabs>

You can pass in an optional `model_name` argument, which lets you choose which Cohere embeddings model to use. By default, Chroma uses `large` model. You can see the available models under `Get embeddings` section [here](https://docs.cohere.ai/reference/embed).

### Multilingual model example

<CodeGroup>
  ```python Python theme={null}
  cohere_ef  = embedding_functions.CohereEmbeddingFunction(
      api_key="YOUR_API_KEY",
      model_name="multilingual-22-12"
  )

  multilingual_texts  = [
      'Hello from Cohere!', 'مرحبًا من كوهير!',
      'Hallo von Cohere!', 'Bonjour de Cohere!',
      '¡Hola desde Cohere!', 'Olá do Cohere!',
      'Ciao da Cohere!', '您好，来自 Cohere！',
      'कोहिअर से नमस्ते!'
  ]

  cohere_ef(input=multilingual_texts)

  ```

  ```typescript TypeScript theme={null}
  import { CohereEmbeddingFunction } from "chromadb";

  const embedder = new CohereEmbeddingFunction("apiKey");

  multilingual_texts = [
      "Hello from Cohere!",
      "مرحبًا من كوهير!",
      "Hallo von Cohere!",
      "Bonjour de Cohere!",
      "¡Hola desde Cohere!",
      "Olá do Cohere!",
      "Ciao da Cohere!",
      "您好，来自 Cohere！",
      "कोहिअर से नमस्ते!",
  ];

  const embeddings = embedder.generate(multilingual_texts);
  ```
</CodeGroup>

For more information on multilingual model you can read [here](https://docs.cohere.ai/docs/multilingual-language-models).

### Multimodal model example

```python theme={null}
import os
from datasets import load_dataset, Image

dataset = load_dataset(path="detection-datasets/coco", split="train", streaming=True)

IMAGE_FOLDER = "images"
N_IMAGES = 5
