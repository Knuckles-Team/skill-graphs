##  [`sandbox snapshots delete`](https://vercel.com/docs/cron-jobs#sandbox-snapshots-delete)[](https://vercel.com/docs/cron-jobs#sandbox-snapshots-delete)
Delete one or more snapshots.
terminal
```
sandbox snapshots delete [OPTIONS] <snapshot_id> [...snapshot_id]
```

###  [Sandbox snapshots delete example](https://vercel.com/docs/cron-jobs#sandbox-snapshots-delete-example)[](https://vercel.com/docs/cron-jobs#sandbox-snapshots-delete-example)
terminal
```
# Delete a single snapshot
sandbox snapshots delete snap_1234567890

# Delete multiple snapshots for a specific project
sandbox snapshots delete --project my-app snap_1234567890 snap_0987654321
```

###  [Sandbox snapshots delete options](https://vercel.com/docs/cron-jobs#sandbox-snapshots-delete-options)[](https://vercel.com/docs/cron-jobs#sandbox-snapshots-delete-options)
Option | Alias | Description
---|---|---
`--token <token>` | - | Your [Vercel authentication token](https://vercel.com/kb/guide/how-do-i-use-a-vercel-api-access-token). If you don't provide it, we'll use a stored token or prompt you to log in.
`--project <project>` | - | The [project name or ID](https://vercel.com/docs/project-configuration/general-settings#project-id) you want to use with this command.
`--scope <team>` | `--team` | The team you want to use with this command.
###  [Sandbox snapshots delete flags](https://vercel.com/docs/cron-jobs#sandbox-snapshots-delete-flags)[](https://vercel.com/docs/cron-jobs#sandbox-snapshots-delete-flags)
Flag | Short | Description
---|---|---
`--help` | `-h` | Display help information.
###  [Sandbox snapshots delete arguments](https://vercel.com/docs/cron-jobs#sandbox-snapshots-delete-arguments)[](https://vercel.com/docs/cron-jobs#sandbox-snapshots-delete-arguments)
Argument | Description
---|---
`<snapshot_id>` | Snapshot ID to delete.
`[...snapshot_id]` | Additional snapshot IDs to delete.
