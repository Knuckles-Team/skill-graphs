##  [Available Commands](https://vercel.com/docs/cli#available-commands)[](https://vercel.com/docs/cli#available-commands)
###  [alias](https://vercel.com/docs/cli#alias)[](https://vercel.com/docs/cli#alias)
Apply custom domain aliases to your Vercel deployments.
```
vercel alias set [deployment-url] [custom-domain]
vercel alias rm [custom-domain]
vercel alias ls
```

[Learn more about the alias command](https://vercel.com/docs/cli/alias)
###  [bisect](https://vercel.com/docs/cli#bisect)[](https://vercel.com/docs/cli#bisect)
Perform a binary search on your deployments to help surface issues.
```
vercel bisect
vercel bisect --good [deployment-url] --bad [deployment-url]
```

[Learn more about the bisect command](https://vercel.com/docs/cli/bisect)
###  [blob](https://vercel.com/docs/cli#blob)[](https://vercel.com/docs/cli#blob)
Interact with Vercel Blob storage to upload, download, list, delete, and copy files.
```
vercel blob list
vercel blob put [path-to-file]
vercel blob get [url-or-pathname]
vercel blob del [url-or-pathname]
vercel blob copy [from-url] [to-pathname]
```

[Learn more about the blob command](https://vercel.com/docs/cli/blob)
###  [build](https://vercel.com/docs/cli#build)[](https://vercel.com/docs/cli#build)
Build a Vercel Project locally or in your own CI environment.
```
vercel build
vercel build --prod
```

[Learn more about the build command](https://vercel.com/docs/cli/build)
###  [cache](https://vercel.com/docs/cli#cache)[](https://vercel.com/docs/cli#cache)
Manage cache for your project (CDN cache and Data cache).
```
vercel cache purge
vercel cache purge --type cdn
vercel cache purge --type data
vercel cache invalidate --tag foo
vercel cache dangerously-delete --tag foo
```

[Learn more about the cache command](https://vercel.com/docs/cli/cache)
###  [certs](https://vercel.com/docs/cli#certs)[](https://vercel.com/docs/cli#certs)
Manage certificates for your domains.
```
vercel certs ls
vercel certs issue [domain]
vercel certs rm [certificate-id]
```

[Learn more about the certs command](https://vercel.com/docs/cli/certs)
###  [curl](https://vercel.com/docs/cli#curl)[](https://vercel.com/docs/cli#curl)
Make HTTP requests to your Vercel deployments with automatic deployment protection bypass. This is a beta command.
```
vercel curl [path]
vercel curl /api/hello
vercel curl /api/data --deployment [deployment-url]
```

[Learn more about the curl command](https://vercel.com/docs/cli/curl)
###  [deploy](https://vercel.com/docs/cli#deploy)[](https://vercel.com/docs/cli#deploy)
Deploy your Vercel projects. Default command when no subcommand is specified.
```
vercel
vercel deploy
vercel deploy --prod
```

[Learn more about the deploy command](https://vercel.com/docs/cli/deploy)
###  [dev](https://vercel.com/docs/cli#dev)[](https://vercel.com/docs/cli#dev)
Replicate the Vercel deployment environment locally and test your project.
```
vercel dev
vercel dev --port 3000
```

[Learn more about the dev command](https://vercel.com/docs/cli/dev)
###  [dns](https://vercel.com/docs/cli#dns)[](https://vercel.com/docs/cli#dns)
Manage your DNS records for your domains.
```
vercel dns ls [domain]
vercel dns add [domain] [name] [type] [value]
vercel dns rm [record-id]
```

[Learn more about the dns command](https://vercel.com/docs/cli/dns)
###  [domains](https://vercel.com/docs/cli#domains)[](https://vercel.com/docs/cli#domains)
Buy, sell, transfer, and manage your domains.
```
vercel domains ls
vercel domains add [domain] [project]
vercel domains rm [domain]
vercel domains buy [domain]
```

[Learn more about the domains command](https://vercel.com/docs/cli/domains)
###  [env](https://vercel.com/docs/cli#env)[](https://vercel.com/docs/cli#env)
Manage environment variables in your Vercel Projects.
```
vercel env ls
vercel env add [name] [environment]
vercel env update [name] [environment]
vercel env rm [name] [environment]
vercel env pull [file]
vercel env run -- <command>
```

[Learn more about the env command](https://vercel.com/docs/cli/env)
###  [git](https://vercel.com/docs/cli#git)[](https://vercel.com/docs/cli#git)
Manage your Git provider connections.
```
vercel git ls
vercel git connect
vercel git disconnect [provider]
```

[Learn more about the git command](https://vercel.com/docs/cli/git)
###  [guidance](https://vercel.com/docs/cli#guidance)[](https://vercel.com/docs/cli#guidance)
Enable or disable guidance messages shown after CLI commands.
```
vercel guidance enable
vercel guidance disable
vercel guidance status
```

[Learn more about the guidance command](https://vercel.com/docs/cli/guidance)
###  [help](https://vercel.com/docs/cli#help)[](https://vercel.com/docs/cli#help)
Get information about all available Vercel CLI commands.
```
vercel help
vercel help [command]
```

[Learn more about the help command](https://vercel.com/docs/cli/help)
###  [httpstat](https://vercel.com/docs/cli#httpstat)[](https://vercel.com/docs/cli#httpstat)
Visualize HTTP request timing statistics for your Vercel deployments with automatic deployment protection bypass.
```
vercel httpstat [path]
vercel httpstat /api/hello
vercel httpstat /api/data --deployment [deployment-url]
```

[Learn more about the httpstat command](https://vercel.com/docs/cli/httpstat)
###  [init](https://vercel.com/docs/cli#init)[](https://vercel.com/docs/cli#init)
Initialize example Vercel Projects locally from the examples repository.
```
vercel init
vercel init [project-name]
```

[Learn more about the init command](https://vercel.com/docs/cli/init)
###  [inspect](https://vercel.com/docs/cli#inspect)[](https://vercel.com/docs/cli#inspect)
Retrieve information about your Vercel deployments.
```
vercel inspect [deployment-id-or-url]
vercel inspect [deployment-id-or-url] --logs
vercel inspect [deployment-id-or-url] --wait
```

[Learn more about the inspect command](https://vercel.com/docs/cli/inspect)
###  [install](https://vercel.com/docs/cli#install)[](https://vercel.com/docs/cli#install)
Install a marketplace integration and provision a resource. Alias for `vercel integration add`.
```
vercel install <integration-name>
```

[Learn more about the install command](https://vercel.com/docs/cli/install)
###  [integration](https://vercel.com/docs/cli#integration)[](https://vercel.com/docs/cli#integration)
Manage marketplace integrations: provision resources, discover available integrations, view setup guides, check balances, and more.
```
vercel integration add <integration-name>
vercel integration list [project-name]
vercel integration discover
vercel integration guide <integration-name>
vercel integration balance <integration-name>
vercel integration open <integration-name> [resource-name]
vercel integration remove <integration-name>
```

[Learn more about the integration command](https://vercel.com/docs/cli/integration)
###  [integration-resource](https://vercel.com/docs/cli#integration-resource)[](https://vercel.com/docs/cli#integration-resource)
Manage individual resources from marketplace integrations: remove, disconnect from projects, and configure auto-recharge thresholds.
```
vercel integration-resource remove <resource-name>
vercel integration-resource disconnect <resource-name> [project-name]
vercel integration-resource create-threshold <resource-name> <minimum> <spend> <limit>
```

[Learn more about the integration-resource command](https://vercel.com/docs/cli/integration-resource)
###  [link](https://vercel.com/docs/cli#link)[](https://vercel.com/docs/cli#link)
Link a local directory to a Vercel Project.
```
vercel link
vercel link [path-to-directory]
```

[Learn more about the link command](https://vercel.com/docs/cli/link)
###  [list](https://vercel.com/docs/cli#list)[](https://vercel.com/docs/cli#list)
List recent deployments for the current Vercel Project.
```
vercel list
vercel list [project-name]
```

[Learn more about the list command](https://vercel.com/docs/cli/list)
###  [login](https://vercel.com/docs/cli#login)[](https://vercel.com/docs/cli#login)
Login to your Vercel account through CLI.
```
vercel login
vercel login [email]
vercel login --github
```

[Learn more about the login command](https://vercel.com/docs/cli/login)
###  [logout](https://vercel.com/docs/cli#logout)[](https://vercel.com/docs/cli#logout)
Logout from your Vercel account through CLI.
```
vercel logout
```

[Learn more about the logout command](https://vercel.com/docs/cli/logout)
###  [logs](https://vercel.com/docs/cli#logs)[](https://vercel.com/docs/cli#logs)
List runtime logs for a specific deployment.
```
vercel logs [deployment-url]
vercel logs [deployment-url] --follow
```

[Learn more about the logs command](https://vercel.com/docs/cli/logs)
###  [mcp](https://vercel.com/docs/cli#mcp)[](https://vercel.com/docs/cli#mcp)
Set up MCP client configuration for your Vercel Project.
```
vercel mcp
vercel mcp --project
```

[Learn more about the mcp command](https://vercel.com/docs/cli/mcp)
###  [microfrontends](https://vercel.com/docs/cli#microfrontends)[](https://vercel.com/docs/cli#microfrontends)
Work with microfrontends configuration.
```
vercel microfrontends pull
vercel microfrontends pull --dpl [deployment-id-or-url]
```

[Learn more about the microfrontends command](https://vercel.com/docs/cli/microfrontends)
###  [open](https://vercel.com/docs/cli#open)[](https://vercel.com/docs/cli#open)
Open your current project in the Vercel Dashboard.
```
vercel open
```

[Learn more about the open command](https://vercel.com/docs/cli/open)
###  [project](https://vercel.com/docs/cli#project)[](https://vercel.com/docs/cli#project)
List, add, inspect, remove, and manage your Vercel Projects.
```
vercel project ls
vercel project add
vercel project rm
vercel project inspect [project-name]
```

[Learn more about the project command](https://vercel.com/docs/cli/project)
###  [promote](https://vercel.com/docs/cli#promote)[](https://vercel.com/docs/cli#promote)
Promote an existing deployment to be the current deployment.
```
vercel promote [deployment-id-or-url]
vercel promote status [project]
```

[Learn more about the promote command](https://vercel.com/docs/cli/promote)
###  [pull](https://vercel.com/docs/cli#pull)[](https://vercel.com/docs/cli#pull)
Update your local project with remote environment variables and project settings.
```
vercel pull
vercel pull --environment=production
```

[Learn more about the pull command](https://vercel.com/docs/cli/pull)
###  [redeploy](https://vercel.com/docs/cli#redeploy)[](https://vercel.com/docs/cli#redeploy)
Rebuild and redeploy an existing deployment.
```
vercel redeploy [deployment-id-or-url]
```

[Learn more about the redeploy command](https://vercel.com/docs/cli/redeploy)
###  [redirects](https://vercel.com/docs/cli#redirects)[](https://vercel.com/docs/cli#redirects)
Manage project-level redirects.
```
vercel redirects list
vercel redirects add /old /new --status 301
vercel redirects upload redirects.csv --overwrite
vercel redirects promote <version-id>
```

[Learn more about the redirects command](https://vercel.com/docs/cli/redirects)
###  [remove](https://vercel.com/docs/cli#remove)[](https://vercel.com/docs/cli#remove)
Remove deployments either by ID or for a specific Vercel Project.
```
vercel remove [deployment-url]
vercel remove [project-name]
```

[Learn more about the remove command](https://vercel.com/docs/cli/remove)
###  [rollback](https://vercel.com/docs/cli#rollback)[](https://vercel.com/docs/cli#rollback)
Roll back production deployments to previous deployments.
```
vercel rollback
vercel rollback [deployment-id-or-url]
vercel rollback status [project]
```

[Learn more about the rollback command](https://vercel.com/docs/cli/rollback)
###  [rolling-release](https://vercel.com/docs/cli#rolling-release)[](https://vercel.com/docs/cli#rolling-release)
Manage your project's rolling releases to gradually roll out new deployments.
```
vercel rolling-release configure --cfg='[config]'
vercel rolling-release start --dpl=[deployment-id]
vercel rolling-release approve --dpl=[deployment-id]
vercel rolling-release complete --dpl=[deployment-id]
```

[Learn more about the rolling-release command](https://vercel.com/docs/cli/rolling-release)
###  [switch](https://vercel.com/docs/cli#switch)[](https://vercel.com/docs/cli#switch)
Switch between different team scopes.
```
vercel switch
vercel switch [team-name]
```

[Learn more about the switch command](https://vercel.com/docs/cli/switch)
###  [teams](https://vercel.com/docs/cli#teams)[](https://vercel.com/docs/cli#teams)
List, add, remove, and manage your teams.
```
vercel teams list
vercel teams add
vercel teams invite [email]
```

[Learn more about the teams command](https://vercel.com/docs/cli/teams)
###  [target](https://vercel.com/docs/cli#target)[](https://vercel.com/docs/cli#target)
Manage custom environments (targets) and use the `--target` flag on relevant commands.
```
vercel target list
vercel target ls
vercel deploy --target=staging
```

[Learn more about the target command](https://vercel.com/docs/cli/target)
###  [telemetry](https://vercel.com/docs/cli#telemetry)[](https://vercel.com/docs/cli#telemetry)
Enable or disable telemetry collection.
```
vercel telemetry status
vercel telemetry enable
vercel telemetry disable
```

[Learn more about the telemetry command](https://vercel.com/docs/cli/telemetry)
###  [webhooks](https://vercel.com/docs/cli#webhooks)[](https://vercel.com/docs/cli#webhooks)
Manage webhooks for your account. This command is in beta.
```
vercel webhooks list
vercel webhooks get <id>
vercel webhooks create <url> --event <event>
vercel webhooks rm <id>
```

[Learn more about the webhooks command](https://vercel.com/docs/cli/webhooks)
###  [whoami](https://vercel.com/docs/cli#whoami)[](https://vercel.com/docs/cli#whoami)
Display the username of the currently logged in user.
```
vercel whoami
```

[Learn more about the whoami command](https://vercel.com/docs/cli/whoami)
* * *
[ Previous CDN/ Pricing & Usage ](https://vercel.com/docs/manage-cdn-usage)[ Next Deploying from CLI ](https://vercel.com/docs/cli/deploying-from-cli)
Was this helpful?
Send
On this page
  * [Installing Vercel CLI](https://vercel.com/docs/cli#installing-vercel-cli)
  * [Updating Vercel CLI](https://vercel.com/docs/cli#updating-vercel-cli)
  * [Checking the version](https://vercel.com/docs/cli#checking-the-version)
  * [Using in a CI/CD environment](https://vercel.com/docs/cli#using-in-a-ci/cd-environment)
  * [Available Commands](https://vercel.com/docs/cli#available-commands)
  * [alias](https://vercel.com/docs/cli#alias)
  * [bisect](https://vercel.com/docs/cli#bisect)
  * [blob](https://vercel.com/docs/cli#blob)
  * [build](https://vercel.com/docs/cli#build)
  * [cache](https://vercel.com/docs/cli#cache)
  * [certs](https://vercel.com/docs/cli#certs)
  * [curl](https://vercel.com/docs/cli#curl)
  * [deploy](https://vercel.com/docs/cli#deploy)
  * [dev](https://vercel.com/docs/cli#dev)
  * [dns](https://vercel.com/docs/cli#dns)
  * [domains](https://vercel.com/docs/cli#domains)
  * [env](https://vercel.com/docs/cli#env)
  * [git](https://vercel.com/docs/cli#git)
  * [guidance](https://vercel.com/docs/cli#guidance)
  * [help](https://vercel.com/docs/cli#help)
  * [httpstat](https://vercel.com/docs/cli#httpstat)
  * [init](https://vercel.com/docs/cli#init)
  * [inspect](https://vercel.com/docs/cli#inspect)
  * [install](https://vercel.com/docs/cli#install)
  * [integration](https://vercel.com/docs/cli#integration)
  * [integration-resource](https://vercel.com/docs/cli#integration-resource)
  * [link](https://vercel.com/docs/cli#link)
  * [list](https://vercel.com/docs/cli#list)
  * [login](https://vercel.com/docs/cli#login)
  * [logout](https://vercel.com/docs/cli#logout)
  * [logs](https://vercel.com/docs/cli#logs)
  * [mcp](https://vercel.com/docs/cli#mcp)
  * [microfrontends](https://vercel.com/docs/cli#microfrontends)
  * [open](https://vercel.com/docs/cli#open)
  * [project](https://vercel.com/docs/cli#project)
  * [promote](https://vercel.com/docs/cli#promote)
  * [pull](https://vercel.com/docs/cli#pull)
  * [redeploy](https://vercel.com/docs/cli#redeploy)
  * [redirects](https://vercel.com/docs/cli#redirects)
  * [remove](https://vercel.com/docs/cli#remove)
  * [rollback](https://vercel.com/docs/cli#rollback)
  * [rolling-release](https://vercel.com/docs/cli#rolling-release)
  * [switch](https://vercel.com/docs/cli#switch)
  * [teams](https://vercel.com/docs/cli#teams)
  * [target](https://vercel.com/docs/cli#target)
  * [telemetry](https://vercel.com/docs/cli#telemetry)
  * [webhooks](https://vercel.com/docs/cli#webhooks)
  * [whoami](https://vercel.com/docs/cli#whoami)


Copy as MarkdownGive feedbackAsk AI about this page
CLI
