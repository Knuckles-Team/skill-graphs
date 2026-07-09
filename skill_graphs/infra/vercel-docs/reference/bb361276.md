##  [`sandbox exec`](https://vercel.com/docs/cron-jobs#sandbox-exec)[](https://vercel.com/docs/cron-jobs#sandbox-exec)
Execute a command in an existing sandbox.
terminal
```
sandbox exec [OPTIONS] <sandbox_id> <command> [...args]
```

###  [Sandbox exec example](https://vercel.com/docs/cron-jobs#sandbox-exec-example)[](https://vercel.com/docs/cron-jobs#sandbox-exec-example)
terminal
```
# Execute a simple command in a sandbox
sandbox exec sb_1234567890 ls -la

# Run with environment variables
sandbox exec --env DEBUG=true sb_1234567890 npm test

# Execute interactively with sudo
sandbox exec --interactive --sudo sb_1234567890 sh

# Run command in specific working directory
sandbox exec --workdir /app sb_1234567890 python script.py
```

###  [Sandbox exec options](https://vercel.com/docs/cron-jobs#sandbox-exec-options)[](https://vercel.com/docs/cron-jobs#sandbox-exec-options)
Option | Alias | Description
---|---|---
`--token <token>` | - | Your [Vercel authentication token](https://vercel.com/kb/guide/how-do-i-use-a-vercel-api-access-token). If you don't provide it, we'll use a stored token or prompt you to log in.
`--project <project>` | - | The [project name or ID](https://vercel.com/docs/project-configuration/general-settings#project-id) you want to use with this command.
`--scope <team>` | `--team` | The team you want to use with this command.
`--workdir <directory>` | `-w` | Set the directory where you want the command to run.
`--env <key=value>` | `-e` | Set environment variables for your command.
###  [Sandbox exec flags](https://vercel.com/docs/cron-jobs#sandbox-exec-flags)[](https://vercel.com/docs/cron-jobs#sandbox-exec-flags)
Flag | Short | Description
---|---|---
`--sudo` | - | Run the command with admin privileges.
`--interactive` | `-i` | Run the command in an interactive shell.
`--tty` | `-t` | Enable terminal features for interactive commands.
`--help` | `-h` | Display help information.
###  [Sandbox exec arguments](https://vercel.com/docs/cron-jobs#sandbox-exec-arguments)[](https://vercel.com/docs/cron-jobs#sandbox-exec-arguments)
Argument | Description
---|---
`<sandbox_id>` | The ID of the sandbox where you want to run the command.
`<command>` | The command you want to run.
`[...args]` | Additional arguments for your command.
