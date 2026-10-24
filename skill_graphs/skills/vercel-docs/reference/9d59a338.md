##  [`sandbox stop`](https://vercel.com/docs/cron-jobs#sandbox-stop)[](https://vercel.com/docs/cron-jobs#sandbox-stop)
Stop one or more running sandboxes.
terminal
```
sandbox stop [OPTIONS] <sandbox_id> [...sandbox_id]
```

###  [Sandbox stop example](https://vercel.com/docs/cron-jobs#sandbox-stop-example)[](https://vercel.com/docs/cron-jobs#sandbox-stop-example)
terminal
```
# Stop a single sandbox
sandbox stop sb_1234567890

# Stop multiple sandboxes
sandbox stop sb_1234567890 sb_0987654321

# Stop sandbox for a specific project
sandbox stop --project my-app sb_1234567890
```

###  [Sandbox stop options](https://vercel.com/docs/cron-jobs#sandbox-stop-options)[](https://vercel.com/docs/cron-jobs#sandbox-stop-options)
Option | Alias | Description
---|---|---
`--token <token>` | - | Your [Vercel authentication token](https://vercel.com/kb/guide/how-do-i-use-a-vercel-api-access-token). If you don't provide it, we'll use a stored token or prompt you to log in.
`--project <project>` | - | The [project name or ID](https://vercel.com/docs/project-configuration/general-settings#project-id) you want to use with this command.
`--scope <team>` | `--team` | The team you want to use with this command.
###  [Sandbox stop flags](https://vercel.com/docs/cron-jobs#sandbox-stop-flags)[](https://vercel.com/docs/cron-jobs#sandbox-stop-flags)
Flag | Short | Description
---|---|---
`--help` | `-h` | Display help information.
###  [Sandbox stop arguments](https://vercel.com/docs/cron-jobs#sandbox-stop-arguments)[](https://vercel.com/docs/cron-jobs#sandbox-stop-arguments)
Argument | Description
---|---
`<sandbox_id>` | The ID of the sandbox you want to stop.
`[...sandbox_id]` | Additional sandbox IDs to stop.
