##  [`sandbox snapshot`](https://vercel.com/docs/cron-jobs#sandbox-snapshot)[](https://vercel.com/docs/cron-jobs#sandbox-snapshot)
Take a snapshot of the filesystem of a sandbox.
terminal
```
sandbox snapshot [OPTIONS] <SANDBOX_ID>
```

###  [Sandbox snapshot example](https://vercel.com/docs/cron-jobs#sandbox-snapshot-example)[](https://vercel.com/docs/cron-jobs#sandbox-snapshot-example)
terminal
```
# Create a snapshot of a running sandbox
sandbox snapshot sb_1234567890 --stop

# Create a snapshot that expires in 14 days
sandbox snapshot sb_1234567890 --stop --expiration 14d

# Create a snapshot that never expires
sandbox snapshot sb_1234567890 --stop --expiration 0
```

###  [Sandbox snapshot options](https://vercel.com/docs/cron-jobs#sandbox-snapshot-options)[](https://vercel.com/docs/cron-jobs#sandbox-snapshot-options)
Option | Alias | Description
---|---|---
`--token <token>` | - | Your [Vercel authentication token](https://vercel.com/kb/guide/how-do-i-use-a-vercel-api-access-token). If you don't provide it, we'll use a stored token or prompt you to log in.
`--project <project>` | - | The [project name or ID](https://vercel.com/docs/project-configuration/general-settings#project-id) you want to use with this command.
`--scope <team>` | `--team` | The team you want to use with this command.
`--expiration <expiration>` | - | The snapshot [expiration period](https://vercel.com/docs/vercel-sandbox/concepts/snapshots#snapshot-limits). Examples: `1d`, `14d`. The default is 30 days.
###  [Sandbox snapshot flags](https://vercel.com/docs/cron-jobs#sandbox-snapshot-flags)[](https://vercel.com/docs/cron-jobs#sandbox-snapshot-flags)
Flag | Short | Description
---|---|---
`--stop` | - | Confirm that the sandbox will be stopped when snapshotting.
`--silent` | - | Don't write snapshot ID to stdout.
`--help` | `-h` | Display help information.
###  [Sandbox snapshot arguments](https://vercel.com/docs/cron-jobs#sandbox-snapshot-arguments)[](https://vercel.com/docs/cron-jobs#sandbox-snapshot-arguments)
Argument | Description
---|---
`<sandbox_id>` | The ID of the sandbox to snapshot.
