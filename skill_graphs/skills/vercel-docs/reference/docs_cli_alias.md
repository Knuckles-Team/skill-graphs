[CLI](https://vercel.com/docs/cli)
vercel alias
[CLI](https://vercel.com/docs/cli)
vercel alias
# vercel alias
Last updated January 13, 2026
The `vercel alias` command allows you to apply [custom domains](https://vercel.com/docs/projects/custom-domains) to your deployments.
When a new deployment is created (with our [Git Integration](https://vercel.com/docs/git), Vercel CLI, or the [REST API](https://vercel.com/docs/rest-api)), the platform will automatically apply any [custom domains](https://vercel.com/docs/projects/custom-domains) configured in the project settings.
Any custom domain that doesn't have a [custom preview branch](https://vercel.com/docs/domains/working-with-domains/assign-domain-to-a-git-branch) configured (there can only be one Production Branch and it's [configured separately](https://vercel.com/docs/git#production-branch) in the project settings) will be applied to production deployments created through any of the available sources.
Custom domains that do have a custom preview branch configured, however, only get applied when using the [Git Integration](https://vercel.com/docs/git).
If you're not using the [Git Integration](https://vercel.com/docs/git), `vercel alias` is a great solution if you still need to apply custom domains based on Git branches, or other heuristics.
##  [Preferred production commands](https://vercel.com/docs/cli/alias#preferred-production-commands)[](https://vercel.com/docs/cli/alias#preferred-production-commands)
The `vercel alias` command is not the recommended way to promote production deployments to specific domains. Instead, you can use the following commands:
  * [`vercel --prod --skip-domain`](https://vercel.com/docs/cli/deploy#prod): Use to skip custom domain assignment when deploying to production and creating a staged deployment
  * [`vercel promote [deployment-id or url]`](https://vercel.com/docs/cli/promote): Use to promote your staged deployment to your custom domains
  * [`vercel rollback [deployment-id or url]`](https://vercel.com/docs/cli/rollback): Use to alias an earlier production deployment to your custom domains


##  [Usage](https://vercel.com/docs/cli/alias#usage)[](https://vercel.com/docs/cli/alias#usage)
In general, the command allows for assigning custom domains to any deployment.
Make sure to not include the HTTP protocol (e.g. `https://`) for the `[custom-domain]` parameter.
terminal
```
vercel alias set [deployment-url] [custom-domain]
```

Using the `vercel alias` command to assign a custom domain to a deployment.
terminal
```
vercel alias rm [custom-domain]
```

Using the `vercel alias` command to remove a custom domain from a deployment.
terminal
```
vercel alias ls
```

Using the `vercel alias` command to list custom domains that were assigned to deployments.
##  [Unique options](https://vercel.com/docs/cli/alias#unique-options)[](https://vercel.com/docs/cli/alias#unique-options)
These are options that only apply to the `vercel alias` command.
###  [Yes](https://vercel.com/docs/cli/alias#yes)[](https://vercel.com/docs/cli/alias#yes)
The `--yes` option can be used to bypass the confirmation prompt when removing an alias.
terminal
```
vercel alias rm [custom-domain] --yes
```

Using the `vercel alias rm` command with the `--yes` option.
###  [Limit](https://vercel.com/docs/cli/alias#limit)[](https://vercel.com/docs/cli/alias#limit)
The `--limit` option can be used to specify the maximum number of aliases returned when using `ls`. The default value is `20` and the maximum is `100`.
terminal
```
vercel alias ls --limit 100
```

Using the `vercel alias ls` command with the `--limit` option.
##  [Global Options](https://vercel.com/docs/cli/alias#global-options)[](https://vercel.com/docs/cli/alias#global-options)
The following [global options](https://vercel.com/docs/cli/global-options) can be passed when using the `vercel alias` command:
  * [`--cwd`](https://vercel.com/docs/cli/global-options#current-working-directory)
  * [`--debug`](https://vercel.com/docs/cli/global-options#debug)
  * [`--global-config`](https://vercel.com/docs/cli/global-options#global-config)
  * [`--help`](https://vercel.com/docs/cli/global-options#help)
  * [`--local-config`](https://vercel.com/docs/cli/global-options#local-config)
  * [`--no-color`](https://vercel.com/docs/cli/global-options#no-color)
  * [`--scope`](https://vercel.com/docs/cli/global-options#scope)
  * [`--token`](https://vercel.com/docs/cli/global-options#token)


For more information on global options and their usage, refer to the [options section](https://vercel.com/docs/cli/global-options).
##  [Related guides](https://vercel.com/docs/cli/alias#related-guides)[](https://vercel.com/docs/cli/alias#related-guides)
  * [How do I resolve alias related errors on Vercel?](https://vercel.com/kb/guide/how-to-resolve-alias-errors-on-vercel)


* * *
[ Previous Global Options ](https://vercel.com/docs/cli/global-options)[ Next vercel bisect ](https://vercel.com/docs/cli/bisect)
Was this helpful?
Send
