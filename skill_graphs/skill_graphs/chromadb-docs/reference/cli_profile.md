[Skip to main content](https://docs.trychroma.com/docs/cli/profile#content-area)
[Chroma Docs home page![light logo](https://mintcdn.com/chroma-8943dec5/wr97NKZIObCJm0cR/images/light-logo.svg?fit=max&auto=format&n=wr97NKZIObCJm0cR&q=85&s=4d021170bd60f2e52fcb7bc0d3eb0552)![dark logo](https://mintcdn.com/chroma-8943dec5/wr97NKZIObCJm0cR/images/dark-logo.svg?fit=max&auto=format&n=wr97NKZIObCJm0cR&q=85&s=a6f162fa88876846a979771be29f2a13)](https://docs.trychroma.com/)
Search...
Ctrl KAsk AI
  * [Dashboard](https://trychroma.com/login)
  * [Dashboard](https://trychroma.com/login)


Search...
Navigation
CLI
Profile Management
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
  * [Delete](https://docs.trychroma.com/docs/cli/profile#delete)
  * [List](https://docs.trychroma.com/docs/cli/profile#list)
  * [Show](https://docs.trychroma.com/docs/cli/profile#show)
  * [Rename](https://docs.trychroma.com/docs/cli/profile#rename)
  * [Use](https://docs.trychroma.com/docs/cli/profile#use)


A **profile** in the Chroma CLI persists the credentials (API key and tenant ID) for authenticating with Chroma Cloud. Each time you use the [`login`](https://docs.trychroma.com/docs/cli/login) command, the CLI will create a profile for the team you logged in with. All profiles are saved in the `.chroma/credentials` file in your home directory. The CLI also keeps track of your “active” profile in `.chroma/config.json`. This is the profile that will be used for all CLI commands with Chroma Cloud. For example, if you [logged](https://docs.trychroma.com/docs/cli/login) into your “staging” team on Chroma Cloud, and set it as your active profile. Later, when you use the `chroma db create my-db` command, you will see `my-db` created under your “staging” team. The `profile` command lets you manage your profiles.
###
[​](https://docs.trychroma.com/docs/cli/profile#delete)
Delete
Deletes a profile. The CLI will ask you to confirm if you are trying to delete your active profile. If this is the case, be sure to use the `profile use` command to set a new active profile, otherwise all future Chrom Cloud CLI commands will fail.
Report incorrect code
Copy
Ask AI
```
chroma profile delete [profile_name]

```

###
[​](https://docs.trychroma.com/docs/cli/profile#list)
List
Lists all your available profiles
Report incorrect code
Copy
Ask AI
```
chroma profile list

```

###
[​](https://docs.trychroma.com/docs/cli/profile#show)
Show
Outputs the name of your active profile
Report incorrect code
Copy
Ask AI
```
chroma profile show

```

###
[​](https://docs.trychroma.com/docs/cli/profile#rename)
Rename
Rename a profile
Report incorrect code
Copy
Ask AI
```
chroma profile rename [old_name] [new_name]

```

###
[​](https://docs.trychroma.com/docs/cli/profile#use)
Use
Set a new profile as the active profile
Report incorrect code
Copy
Ask AI
```
chroma profile use [profile_name]

```

Was this page helpful?
YesNo
[ Login Previous ](https://docs.trychroma.com/docs/cli/login)[ Run a Chroma Server Next ](https://docs.trychroma.com/docs/cli/run)
Ctrl+I
Assistant
Responses are generated using AI and may contain mistakes.
