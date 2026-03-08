[Skip to main content](https://docs.trychroma.com/docs/cli/browse#content-area)
[Chroma Docs home page![light logo](https://mintcdn.com/chroma-8943dec5/wr97NKZIObCJm0cR/images/light-logo.svg?fit=max&auto=format&n=wr97NKZIObCJm0cR&q=85&s=4d021170bd60f2e52fcb7bc0d3eb0552)![dark logo](https://mintcdn.com/chroma-8943dec5/wr97NKZIObCJm0cR/images/dark-logo.svg?fit=max&auto=format&n=wr97NKZIObCJm0cR&q=85&s=a6f162fa88876846a979771be29f2a13)](https://docs.trychroma.com/)
Search...
Ctrl KAsk AI
  * [Dashboard](https://trychroma.com/login)
  * [Dashboard](https://trychroma.com/login)


Search...
Navigation
CLI
Browse Collections
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
  * [Arguments](https://docs.trychroma.com/docs/cli/browse#arguments)
  * [The Collection Browser UI](https://docs.trychroma.com/docs/cli/browse#the-collection-browser-ui)
  * [Main View](https://docs.trychroma.com/docs/cli/browse#main-view)
  * [Search](https://docs.trychroma.com/docs/cli/browse#search)


CLI
# Browse Collections
Copy page
Inspect your Chroma collections with an in-terminal UI.
Copy page
You can use the Chroma CLI to inspect your collections with an in-terminal UI. The CLI supports browsing collections from DBs on Chroma Cloud or a local Chroma server.
Report incorrect code
Copy
Ask AI
```
chroma browse [collection_name] [--local]

```

###
[​](https://docs.trychroma.com/docs/cli/browse#arguments)
Arguments
  * `collection_name` - The name of the collection you want to browse. This is a required argument.
  * `db_name` - The name of the Chroma Cloud DB with the collection you want to browse. If not provided, the CLI will prompt you to select a DB from those available on your active [profile](https://docs.trychroma.com/docs/cli/profile). For local Chroma, the CLI uses the `default_database`.
  * `local` - Instructs the CLI to find your collection on a local Chroma server at `http://localhost:8000`. If your local Chroma server is available on a different hostname, use the `host` argument instead.
  * `host` - The host of your local Chroma server. This argument conflicts with `path`.
  * `path` - The path of your local Chroma data. If provided, the CLI will use the data path to start a local Chroma server at an available port for browsing. This argument conflicts with `host`.
  * `theme` - The theme of your terminal (`light` or `dark`). Optimizes the UI colors for your terminal’s theme. You only need to provide this argument once, and the CLI will persist it in `~/.chroma/config.json`.


cloud
cloud with DB
local default
local with host
local with path
Report incorrect code
Copy
Ask AI
```
chroma browse my-collection

```

###
[​](https://docs.trychroma.com/docs/cli/browse#the-collection-browser-ui)
The Collection Browser UI
####
[​](https://docs.trychroma.com/docs/cli/browse#main-view)
Main View
The main view of the Collection Browser shows you a tabular view of your data with record IDs, documents, and metadata. You can navigate the table using arrows, and expand each cell with `Return`. Only 100 records are loaded initially, and the next batch will load as you scroll down the table. ![CLI browse](https://mintcdn.com/chroma-8943dec5/N-xA4EbmHOvIcCcs/images/cli/cli-browse.png?fit=max&auto=format&n=N-xA4EbmHOvIcCcs&q=85&s=69d82373482ee9f5ee3a51f6f0a02104)
####
[​](https://docs.trychroma.com/docs/cli/browse#search)
Search
You can enter the query editor by hitting `s` on the main view. This form allows you to submit `.get()` queries on your collection. You can edit the form by hitting `e` to enter edit mode, use `space` to toggle the metadata operator, and `Esc` to quit editing mode. To submit a query use `Return`. The query editor persists your edits after you submit. You can clear it by hitting `c`. When viewing the results you can hit `s` to get back to the query editor, or `Esc` to get back to the main view. ![CLI browse query](https://mintcdn.com/chroma-8943dec5/N-xA4EbmHOvIcCcs/images/cli/cli-browse-query.png?fit=max&auto=format&n=N-xA4EbmHOvIcCcs&q=85&s=81449441f0c28ace4659ef8833f89cb9)
Was this page helpful?
YesNo
[ Installing the CLI Previous ](https://docs.trychroma.com/docs/cli/install)[ Copy Collections Next ](https://docs.trychroma.com/docs/cli/copy)
Ctrl+I
[Chroma Docs home page![light logo](https://mintcdn.com/chroma-8943dec5/wr97NKZIObCJm0cR/images/light-logo.svg?fit=max&auto=format&n=wr97NKZIObCJm0cR&q=85&s=4d021170bd60f2e52fcb7bc0d3eb0552)![dark logo](https://mintcdn.com/chroma-8943dec5/wr97NKZIObCJm0cR/images/dark-logo.svg?fit=max&auto=format&n=wr97NKZIObCJm0cR&q=85&s=a6f162fa88876846a979771be29f2a13)](https://docs.trychroma.com/)
[Enterprise](https://trychroma.com/enterprise)[Pricing](https://trychroma.com/pricing)[Changelog](https://trychroma.com/changelog)
Assistant
Responses are generated using AI and may contain mistakes.
![CLI browse](https://mintcdn.com/chroma-8943dec5/N-xA4EbmHOvIcCcs/images/cli/cli-browse.png?w=840&fit=max&auto=format&n=N-xA4EbmHOvIcCcs&q=85&s=1fe3f719a68d560e7b155b8ed55e39bf)
![CLI browse query](https://mintcdn.com/chroma-8943dec5/N-xA4EbmHOvIcCcs/images/cli/cli-browse-query.png?w=840&fit=max&auto=format&n=N-xA4EbmHOvIcCcs&q=85&s=719e8e5dc97ac5fd03e519f51b61cc40)
