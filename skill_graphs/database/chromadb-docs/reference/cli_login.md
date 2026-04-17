[Skip to main content](https://docs.trychroma.com/docs/cli/login#content-area)
[Chroma Docs home page![light logo](https://mintcdn.com/chroma-8943dec5/wr97NKZIObCJm0cR/images/light-logo.svg?fit=max&auto=format&n=wr97NKZIObCJm0cR&q=85&s=4d021170bd60f2e52fcb7bc0d3eb0552)![dark logo](https://mintcdn.com/chroma-8943dec5/wr97NKZIObCJm0cR/images/dark-logo.svg?fit=max&auto=format&n=wr97NKZIObCJm0cR&q=85&s=a6f162fa88876846a979771be29f2a13)](https://docs.trychroma.com/)
Search...
Ctrl KAsk AI
  * [Dashboard](https://trychroma.com/login)
  * [Dashboard](https://trychroma.com/login)


Search...
Navigation
CLI
Login
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


The Chroma CLI allows you to perform various operations with your Chroma Cloud account. These include [DB management](https://docs.trychroma.com/docs/cli/db), [collection copying](https://docs.trychroma.com/docs/cli/copy) and [browsing](https://docs.trychroma.com/docs/cli/browse), and many more to come in the future. Use the `login` command, to authenticate the CLI with your Chroma Cloud account, to enable these features. First, in your browser [create](https://trychroma.com/signup?utm_source=docs-cli-login) a Chroma Cloud account or [login](https://docs.trychroma.com/docs/cli/trychroma.com/login) into your existing account. Then, in your terminal, run
Report incorrect code
Copy
Ask AI
```
chroma login

```

The CLI will open a browser window verifying that the authentication was successful. If so, you should see the following: ![CLI login success](https://mintcdn.com/chroma-8943dec5/N-xA4EbmHOvIcCcs/images/cli/cli-login-success.png?fit=max&auto=format&n=N-xA4EbmHOvIcCcs&q=85&s=71d6a0db04743b124eb5953ed7faaa54) Back in the CLI, you will be prompted to select the team you want to authenticate with. Each team login gets its own [profile](https://docs.trychroma.com/docs/cli/profile) in the CLI. Profiles persist the API key and tenant ID for the team you log-in with. You can find all your profiles in `.chroma/credentials` under your home directory. By default, the name of the profile is the same name of the team you logged-in with. However, the CLI will let you edit that name during the login, or later using the `chroma profile rename` command. Upon your first login, the first created profile will be automatically set as your “active” profile. On subsequent logins, the CLI will instruct you how to switch to a new profile you added (using the `chroma profile use` command).
Was this page helpful?
YesNo
[ Sample Apps Previous ](https://docs.trychroma.com/docs/cli/sample-apps)[ Profile Management Next ](https://docs.trychroma.com/docs/cli/profile)
Ctrl+I
Assistant
Responses are generated using AI and may contain mistakes.
![CLI login success](https://mintcdn.com/chroma-8943dec5/N-xA4EbmHOvIcCcs/images/cli/cli-login-success.png?w=840&fit=max&auto=format&n=N-xA4EbmHOvIcCcs&q=85&s=7f24538760fa12b720ebcf5d9065238c)
