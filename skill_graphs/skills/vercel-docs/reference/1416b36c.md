##  [`sandbox snapshots list`](https://vercel.com/docs/cron-jobs#sandbox-snapshots-list)[](https://vercel.com/docs/cron-jobs#sandbox-snapshots-list)
List snapshots for the specified account and project.
terminal
```
sandbox snapshots list [OPTIONS]
```

###  [Sandbox snapshots list example](https://vercel.com/docs/cron-jobs#sandbox-snapshots-list-example)[](https://vercel.com/docs/cron-jobs#sandbox-snapshots-list-example)
terminal
```
# List snapshots for the current project
sandbox snapshots list

# List snapshots for a specific project
sandbox snapshots list --project my-app
```

###  [Sandbox snapshots list options](https://vercel.com/docs/cron-jobs#sandbox-snapshots-list-options)[](https://vercel.com/docs/cron-jobs#sandbox-snapshots-list-options)
Option | Alias | Description
---|---|---
`--token <token>` | - | Your [Vercel authentication token](https://vercel.com/kb/guide/how-do-i-use-a-vercel-api-access-token). If you don't provide it, we'll use a stored token or prompt you to log in.
`--project <project>` | - | The [project name or ID](https://vercel.com/docs/project-configuration/general-settings#project-id) you want to use with this command.
`--scope <team>` | `--team` | The team you want to use with this command.
###  [Sandbox snapshots list flags](https://vercel.com/docs/cron-jobs#sandbox-snapshots-list-flags)[](https://vercel.com/docs/cron-jobs#sandbox-snapshots-list-flags)
Flag | Short | Description
---|---|---
`--help` | `-h` | Display help information.
