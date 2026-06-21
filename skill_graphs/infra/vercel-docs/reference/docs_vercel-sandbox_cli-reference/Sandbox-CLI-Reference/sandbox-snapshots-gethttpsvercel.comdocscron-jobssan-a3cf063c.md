##  [`sandbox snapshots get`](https://vercel.com/docs/cron-jobs#sandbox-snapshots-get)[](https://vercel.com/docs/cron-jobs#sandbox-snapshots-get)
Get details of a snapshot.
terminal
```
sandbox snapshots get [OPTIONS] <snapshot_id>
```

###  [Sandbox snapshots get example](https://vercel.com/docs/cron-jobs#sandbox-snapshots-get-example)[](https://vercel.com/docs/cron-jobs#sandbox-snapshots-get-example)
terminal
```
# Get details of a specific snapshot
sandbox snapshots get snap_1234567890

# Get snapshot details for a specific project
sandbox snapshots get --project my-app snap_1234567890
```

###  [Sandbox snapshots get options](https://vercel.com/docs/cron-jobs#sandbox-snapshots-get-options)[](https://vercel.com/docs/cron-jobs#sandbox-snapshots-get-options)
Option | Alias | Description
---|---|---
`--token <token>` | - | Your [Vercel authentication token](https://vercel.com/kb/guide/how-do-i-use-a-vercel-api-access-token). If you don't provide it, we'll use a stored token or prompt you to log in.
`--project <project>` | - | The [project name or ID](https://vercel.com/docs/project-configuration/general-settings#project-id) you want to use with this command.
`--scope <team>` | `--team` | The team you want to use with this command.
###  [Sandbox snapshots get flags](https://vercel.com/docs/cron-jobs#sandbox-snapshots-get-flags)[](https://vercel.com/docs/cron-jobs#sandbox-snapshots-get-flags)
Flag | Short | Description
---|---|---
`--help` | `-h` | Display help information.
###  [Sandbox snapshots get arguments](https://vercel.com/docs/cron-jobs#sandbox-snapshots-get-arguments)[](https://vercel.com/docs/cron-jobs#sandbox-snapshots-get-arguments)
Argument | Description
---|---
`<snapshot_id>` | The ID of the snapshot to retrieve.
