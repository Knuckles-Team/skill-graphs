##  [`sandbox list`](https://vercel.com/docs/cron-jobs#sandbox-list)[](https://vercel.com/docs/cron-jobs#sandbox-list)
List all sandboxes for the specified account and project.
terminal
```
sandbox list [OPTIONS]
```

###  [Sandbox list example](https://vercel.com/docs/cron-jobs#sandbox-list-example)[](https://vercel.com/docs/cron-jobs#sandbox-list-example)
terminal
```
# List all running sandboxes
sandbox list

# List all sandboxes (including stopped ones)
sandbox list --all

# List sandboxes for a specific project
sandbox list --project my-nextjs-app
```

###  [Sandbox list options](https://vercel.com/docs/cron-jobs#sandbox-list-options)[](https://vercel.com/docs/cron-jobs#sandbox-list-options)
Option | Alias | Description
---|---|---
`--token <token>` | - | Your [Vercel authentication token](https://vercel.com/kb/guide/how-do-i-use-a-vercel-api-access-token). If you don't provide it, we'll use a stored token or prompt you to log in.
`--project <project>` | - | The [project name or ID](https://vercel.com/docs/project-configuration/general-settings#project-id) you want to use with this command.
`--scope <team>` | `--team` | The team you want to use with this command.
###  [Sandbox list flags](https://vercel.com/docs/cron-jobs#sandbox-list-flags)[](https://vercel.com/docs/cron-jobs#sandbox-list-flags)
Flag | Short | Description
---|---|---
`--all` | `-a` | Show all sandboxes, including stopped ones (we only show running ones by default).
`--help` | `-h` | Display help information.
