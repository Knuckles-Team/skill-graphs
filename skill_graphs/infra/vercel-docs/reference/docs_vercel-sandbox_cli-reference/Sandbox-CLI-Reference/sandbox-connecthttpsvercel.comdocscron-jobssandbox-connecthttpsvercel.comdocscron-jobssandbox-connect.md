##  [`sandbox connect`](https://vercel.com/docs/cron-jobs#sandbox-connect)[](https://vercel.com/docs/cron-jobs#sandbox-connect)
Start an interactive shell in an existing sandbox.
terminal
```
sandbox connect [OPTIONS] <sandbox_id>
```

###  [Sandbox connect example](https://vercel.com/docs/cron-jobs#sandbox-connect-example)[](https://vercel.com/docs/cron-jobs#sandbox-connect-example)
terminal
```
# Connect to an existing sandbox
sandbox connect sb_1234567890

# Connect with a specific working directory
sandbox connect --workdir /app sb_1234567890

# Connect with environment variables and sudo
sandbox connect --env DEBUG=true --sudo sb_1234567890
```

###  [Sandbox connect options](https://vercel.com/docs/cron-jobs#sandbox-connect-options)[](https://vercel.com/docs/cron-jobs#sandbox-connect-options)
Option | Alias | Description
---|---|---
`--token <token>` | - | Your [Vercel authentication token](https://vercel.com/kb/guide/how-do-i-use-a-vercel-api-access-token). If you don't provide it, we'll use a stored token or prompt you to log in.
`--project <project>` | - | The [project name or ID](https://vercel.com/docs/project-configuration/general-settings#project-id) you want to use with this command.
`--scope <team>` | `--team` | The team you want to use with this command.
`--workdir <directory>` | `-w` | Set the directory where you want the command to run.
`--env <key=value>` | `-e` | Set environment variables for your command.
###  [Sandbox connect flags](https://vercel.com/docs/cron-jobs#sandbox-connect-flags)[](https://vercel.com/docs/cron-jobs#sandbox-connect-flags)
Flag | Short | Description
---|---|---
`--sudo` | - | Run the command with admin privileges.
`--no-extend-timeout` | - | Do not extend the sandbox timeout while running an interactive command. Only affects interactive executions.
`--help` | `-h` | Display help information.
###  [Sandbox connect arguments](https://vercel.com/docs/cron-jobs#sandbox-connect-arguments)[](https://vercel.com/docs/cron-jobs#sandbox-connect-arguments)
Argument | Description
---|---
`<sandbox_id>` | The ID of the sandbox where you want to start a shell.
