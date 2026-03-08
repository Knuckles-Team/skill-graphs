[Skip to main content](https://docs.trychroma.com/docs/run-chroma/client-server#content-area)
[Chroma Docs home page![light logo](https://mintcdn.com/chroma-8943dec5/wr97NKZIObCJm0cR/images/light-logo.svg?fit=max&auto=format&n=wr97NKZIObCJm0cR&q=85&s=4d021170bd60f2e52fcb7bc0d3eb0552)![dark logo](https://mintcdn.com/chroma-8943dec5/wr97NKZIObCJm0cR/images/dark-logo.svg?fit=max&auto=format&n=wr97NKZIObCJm0cR&q=85&s=a6f162fa88876846a979771be29f2a13)](https://docs.trychroma.com/)
Search...
Ctrl KAsk AI
  * [Dashboard](https://trychroma.com/login)
  * [Dashboard](https://trychroma.com/login)


Search...
Navigation
Run Chroma
Client-Server Mode
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


Run Chroma
# Client-Server Mode
Copy page
Learn how to run Chroma in client-server mode.
Copy page
Chroma can also be configured to run in client/server mode. In this mode, the Chroma client connects to a Chroma server running in a separate process. To start the Chroma server, run the following command:
Report incorrect code
Copy
Ask AI
```
chroma run --path /db_path

```

Then use the Chroma `HttpClient` to connect to the server:
Report incorrect code
Copy
Ask AI
```
import chromadb

chroma_client = chromadb.HttpClient(host='localhost', port=8000)

```

That’s it! Chroma’s API will run in `client-server` mode with just this change.Chroma also provides the async HTTP client. The behaviors and method signatures are identical to the synchronous client, but all methods that would block are now async. To use it, call `AsyncHttpClient` instead:
Report incorrect code
Copy
Ask AI
```
import asyncio
import chromadb

async def main():
    client = await chromadb.AsyncHttpClient()

    collection = await client.create_collection(name="my_collection")
    await collection.add(
        documents=["hello world"],
        ids=["id1"]
    )

asyncio.run(main())

```

If you [deploy](https://docs.trychroma.com/guides/deploy/client-server-mode) your Chroma server, you can also use our [http-only](https://docs.trychroma.com/guides/deploy/python-thin-client) package.
Then you can connect to it by instantiating a new `ChromaClient`:
Report incorrect code
Copy
Ask AI
```
import { ChromaClient } from "chromadb";

const client = new ChromaClient();

```

If you run your Chroma server using a different configuration, or [deploy](https://docs.trychroma.com/guides/deploy/client-server-mode) your Chroma server, you can specify the `host`, `port`, and whether the client should connect over `ssl`:
Report incorrect code
Copy
Ask AI
```
import { ChromaClient } from "chromadb";

const client = new ChromaClient({
  host: "YOUR-HOST",
  port: "YOUR-PORT",
  ssl: true,
});

```

You can connect to it by instantiating a new `ChromaHttpClient`:
Report incorrect code
Copy
Ask AI
```
let options = ChromaHttpClientOptions {
    endpoint: "http://localhost:8000".parse()?,
    ..Default::default()
};
let client = ChromaHttpClient::new(options);

```

Was this page helpful?
YesNo
[ Chroma Clients Previous ](https://docs.trychroma.com/docs/run-chroma/clients)[ Manage Collections Next ](https://docs.trychroma.com/docs/collections/manage-collections)
Ctrl+I
[Chroma Docs home page![light logo](https://mintcdn.com/chroma-8943dec5/wr97NKZIObCJm0cR/images/light-logo.svg?fit=max&auto=format&n=wr97NKZIObCJm0cR&q=85&s=4d021170bd60f2e52fcb7bc0d3eb0552)![dark logo](https://mintcdn.com/chroma-8943dec5/wr97NKZIObCJm0cR/images/dark-logo.svg?fit=max&auto=format&n=wr97NKZIObCJm0cR&q=85&s=a6f162fa88876846a979771be29f2a13)](https://docs.trychroma.com/)
[Enterprise](https://trychroma.com/enterprise)[Pricing](https://trychroma.com/pricing)[Changelog](https://trychroma.com/changelog)
Assistant
Responses are generated using AI and may contain mistakes.
