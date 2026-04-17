[Skip to main content](https://docs.trychroma.com/docs/run-chroma/clients#content-area)
[Chroma Docs home page![light logo](https://mintcdn.com/chroma-8943dec5/wr97NKZIObCJm0cR/images/light-logo.svg?fit=max&auto=format&n=wr97NKZIObCJm0cR&q=85&s=4d021170bd60f2e52fcb7bc0d3eb0552)![dark logo](https://mintcdn.com/chroma-8943dec5/wr97NKZIObCJm0cR/images/dark-logo.svg?fit=max&auto=format&n=wr97NKZIObCJm0cR&q=85&s=a6f162fa88876846a979771be29f2a13)](https://docs.trychroma.com/)
Search...
Ctrl KAsk AI
  * [Dashboard](https://trychroma.com/login)
  * [Dashboard](https://trychroma.com/login)


Search...
Navigation
Run Chroma
Chroma Clients
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
  * [Cloud Client](https://docs.trychroma.com/docs/run-chroma/clients#cloud-client)
  * [In-Memory Client](https://docs.trychroma.com/docs/run-chroma/clients#in-memory-client)
  * [Persistent Client](https://docs.trychroma.com/docs/run-chroma/clients#persistent-client)


Run Chroma
# Chroma Clients
Copy page
Learn how to instantiate Chroma clients for Cloud, in-memory, and persistent use cases.
Copy page
There are several ways you can instantiate clients to connect to your Chroma database.
##
[​](https://docs.trychroma.com/docs/run-chroma/clients#cloud-client)
Cloud Client
You can use the `CloudClient` to create a client connecting to Chroma Cloud.
Python
TypeScript
Rust
Report incorrect code
Copy
Ask AI
```
import chromadb

client = chromadb.CloudClient(
    tenant='Tenant ID',
    database='Database name',
    api_key='Chroma Cloud API key'
)

```

The `CloudClient` can be instantiated just with the API key argument. In which case, we will resolve the tenant and DB from Chroma Cloud. Note our auto-resolution will work only if the provided API key is scoped to a single DB. If you set the `CHROMA_API_KEY`, `CHROMA_TENANT`, and the `CHROMA_DATABASE` environment variables, you can simply instantiate a `CloudClient` with no arguments:
Python
TypeScript
Rust
Report incorrect code
Copy
Ask AI
```
client = chromadb.CloudClient()

```

##
[​](https://docs.trychroma.com/docs/run-chroma/clients#in-memory-client)
In-Memory Client
In Python, you can run a Chroma server in-memory and connect to it with the ephemeral client:
Report incorrect code
Copy
Ask AI
```
import chromadb

client = chromadb.Client()

```

The `Client()` method starts a Chroma server in-memory and also returns a client with which you can connect to it. This is a great tool for experimenting with different embedding functions and retrieval techniques in a Python notebook, for example. If you don’t need data persistence, the ephemeral client is a good choice for getting up and running with Chroma.
##
[​](https://docs.trychroma.com/docs/run-chroma/clients#persistent-client)
Persistent Client
You can configure Chroma to save and load the database from your local machine, using the `PersistentClient`.Data will be persisted automatically and loaded on start (if it exists).
Report incorrect code
Copy
Ask AI
```
import chromadb

client = chromadb.PersistentClient(path="/path/to/save/to")

```

The `path` is where Chroma will store its database files on disk, and load them on start. If you don’t provide a path, the default is `.chroma`The client object has a few useful convenience methods.
  * `heartbeat()` - returns a nanosecond heartbeat. Useful for making sure the client remains connected.
  * `reset()` - empties and completely resets the database. WARNING: This is destructive and not reversible.


Report incorrect code
Copy
Ask AI
```
client.heartbeat()
client.reset()

```

To connect with the JS/TS client, you must connect to a Chroma server.To run a Chroma server locally that will persist your data, install Chroma from npm using any npm compatible client.
Report incorrect code
Copy
Ask AI
```
npm install chromadb

```

And run the server using our CLI:
Report incorrect code
Copy
Ask AI
```
npx chroma run --path ./getting-started

```

The `path` is where Chroma will store its database files on disk, and load them on start. The default is `.chroma`.Alternatively, you can also use our official Docker image:
Report incorrect code
Copy
Ask AI
```
docker pull chromadb/chroma
docker run -p 8000:8000 chromadb/chroma

```

With a Chroma server running locally, you can connect to it by instantiating a new `ChromaClient`:
Report incorrect code
Copy
Ask AI
```
import { ChromaClient } from "chromadb";

const client = new ChromaClient();

```

By default, the `ChromaClient` is wired to connect to a Chroma server at `http://localhost:8000`, with `default_tenant` and `default_database`. If you have different settings you can provide them to the `ChromaClient` constructor:
Report incorrect code
Copy
Ask AI
```
const client = new ChromaClient({
  ssl: false,
  host: "localhost",
  port: 9000, // non-standard port based on your server config
  database: "my-db",
  headers: {},
});

```

The client object has a few useful convenience methods.
  * `heartbeat()` - returns a nanosecond heartbeat. Useful for making sure the client remains connected.
  * `reset()` - empties and completely resets the database. WARNING: This is destructive and not reversible.


Report incorrect code
Copy
Ask AI
```
await client.heartbeat();
await client.reset();

```

The Rust client connects to a running Chroma server. For local persistence, run the server with a data path and connect over HTTP.
Report incorrect code
Copy
Ask AI
```
chroma run --path /db_path

```

Report incorrect code
Copy
Ask AI
```
use chroma::{ChromaHttpClient, ChromaHttpClientOptions};

let mut options = ChromaHttpClientOptions::default();
options.endpoint = "http://localhost:8000".parse()?;

let client = ChromaHttpClient::new(options);
client.heartbeat().await?;

```

Was this page helpful?
YesNo
[ Troubleshooting Previous ](https://docs.trychroma.com/docs/overview/troubleshooting)[ Client-Server Mode Next ](https://docs.trychroma.com/docs/run-chroma/client-server)
Ctrl+I
[Chroma Docs home page![light logo](https://mintcdn.com/chroma-8943dec5/wr97NKZIObCJm0cR/images/light-logo.svg?fit=max&auto=format&n=wr97NKZIObCJm0cR&q=85&s=4d021170bd60f2e52fcb7bc0d3eb0552)![dark logo](https://mintcdn.com/chroma-8943dec5/wr97NKZIObCJm0cR/images/dark-logo.svg?fit=max&auto=format&n=wr97NKZIObCJm0cR&q=85&s=a6f162fa88876846a979771be29f2a13)](https://docs.trychroma.com/)
[Enterprise](https://trychroma.com/enterprise)[Pricing](https://trychroma.com/pricing)[Changelog](https://trychroma.com/changelog)
Assistant
Responses are generated using AI and may contain mistakes.
