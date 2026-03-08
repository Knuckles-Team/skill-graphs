[Skip to main content](https://docs.trychroma.com/docs/cli/copy#content-area)
[Chroma Docs home page![light logo](https://mintcdn.com/chroma-8943dec5/wr97NKZIObCJm0cR/images/light-logo.svg?fit=max&auto=format&n=wr97NKZIObCJm0cR&q=85&s=4d021170bd60f2e52fcb7bc0d3eb0552)![dark logo](https://mintcdn.com/chroma-8943dec5/wr97NKZIObCJm0cR/images/dark-logo.svg?fit=max&auto=format&n=wr97NKZIObCJm0cR&q=85&s=a6f162fa88876846a979771be29f2a13)](https://docs.trychroma.com/)
Search...
Ctrl KAsk AI
  * [Dashboard](https://trychroma.com/login)
  * [Dashboard](https://trychroma.com/login)


Search...
Navigation
CLI
Copy Collections
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
  * [Arguments](https://docs.trychroma.com/docs/cli/copy#arguments)
  * [Copy from Local to Chroma Cloud](https://docs.trychroma.com/docs/cli/copy#copy-from-local-to-chroma-cloud)
  * [Copy from Chroma Cloud to Local](https://docs.trychroma.com/docs/cli/copy#copy-from-chroma-cloud-to-local)
  * [Quotas](https://docs.trychroma.com/docs/cli/copy#quotas)


CLI
# Copy Collections
Copy page
Copy collections between local Chroma and Chroma Cloud.
Copy page
Using the Chroma CLI, you can copy collections from a local Chroma server to Chroma Cloud and vice versa.
Report incorrect code
Copy
Ask AI
```
chroma copy --from-local collections [collection names]

```

###
[​](https://docs.trychroma.com/docs/cli/copy#arguments)
Arguments
  * `collections` - Space separated list of the names of the collections you want to copy. Conflicts with `all`.
  * `all` - Instructs the CLI to copy all collections from the source DB.
  * `from-local` - Sets the copy source to a local Chroma server. By default, the CLI will try to find it at `localhost:8000`. If you have a different setup, use `path` or `host`.
  * `from-cloud` - Sets the copy source to a DB on Chroma Cloud.
  * `to-local` - Sets the copy target to a local Chroma server. By default, the CLI will try to find it at `localhost:8000`. If you have a different setup, use `path` or `host`.
  * `to-cloud` - Sets the copy target to a DB on Chroma Cloud.
  * `db` - The name of the Chroma Cloud DB with the collections you want to copy. If not provided, the CLI will prompt you to select a DB from those available on your active [profile](https://docs.trychroma.com/docs/cli/profile).
  * `host` - The host of your local Chroma server. This argument conflicts with `path`.
  * `path` - The path of your local Chroma data. If provided, the CLI will use the data path to start a local Chroma server at an available port for browsing. This argument conflicts with `host`.


###
[​](https://docs.trychroma.com/docs/cli/copy#copy-from-local-to-chroma-cloud)
Copy from Local to Chroma Cloud
simple
with DB
host
path
Report incorrect code
Copy
Ask AI
```
chroma copy --from-local collections col-1 col-2

```

###
[​](https://docs.trychroma.com/docs/cli/copy#copy-from-chroma-cloud-to-local)
Copy from Chroma Cloud to Local
simple
with DB
host
path
Report incorrect code
Copy
Ask AI
```
chroma copy --from-cloud collections col-1 col-2

```

###
[​](https://docs.trychroma.com/docs/cli/copy#quotas)
Quotas
You may run into quota limitations when copying local collections to Chroma Cloud, for example if the size of your metadata values on records is too large. If the CLI notifies you that a quota has been exceeded, you can request an increase on the Chroma Cloud dashboard. Click “Settings” on your active profile’s team, and then choose the “Quotas” tab.
Was this page helpful?
YesNo
[ Browse Collections Previous ](https://docs.trychroma.com/docs/cli/browse)[ DB Management Next ](https://docs.trychroma.com/docs/cli/db)
Ctrl+I
[Chroma Docs home page![light logo](https://mintcdn.com/chroma-8943dec5/wr97NKZIObCJm0cR/images/light-logo.svg?fit=max&auto=format&n=wr97NKZIObCJm0cR&q=85&s=4d021170bd60f2e52fcb7bc0d3eb0552)![dark logo](https://mintcdn.com/chroma-8943dec5/wr97NKZIObCJm0cR/images/dark-logo.svg?fit=max&auto=format&n=wr97NKZIObCJm0cR&q=85&s=a6f162fa88876846a979771be29f2a13)](https://docs.trychroma.com/)
[Enterprise](https://trychroma.com/enterprise)[Pricing](https://trychroma.com/pricing)[Changelog](https://trychroma.com/changelog)
Assistant
Responses are generated using AI and may contain mistakes.
