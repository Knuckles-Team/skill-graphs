##  [`sandbox run`](https://vercel.com/docs/cron-jobs#sandbox-run)[](https://vercel.com/docs/cron-jobs#sandbox-run)
Create and run a command in a sandbox.
terminal
```
sandbox run [OPTIONS] <command> [...args]
```

###  [Sandbox run example](https://vercel.com/docs/cron-jobs#sandbox-run-example)[](https://vercel.com/docs/cron-jobs#sandbox-run-example)
terminal
```
# Run a simple Node.js script
sandbox run -- node --version

# Run with custom environment and timeout
sandbox run --env NODE_ENV=production --timeout 10m -- npm start

# Run interactively with port forwarding
sandbox run --interactive --publish-port 3000 --tty npm run dev

# Run with auto-cleanup
sandbox run --rm -- python3 script.py
```

###  [Sandbox run options](https://vercel.com/docs/cron-jobs#sandbox-run-options)[](https://vercel.com/docs/cron-jobs#sandbox-run-options)
Option | Alias | Description
---|---|---
`--token <token>` | - | Your [Vercel authentication token](https://vercel.com/kb/guide/how-do-i-use-a-vercel-api-access-token). If you don't provide it, we'll use a stored token or prompt you to log in.
`--project <project>` | - | The [project name or ID](https://vercel.com/docs/project-configuration/general-settings#project-id) you want to use with this command.
`--scope <team>` | `--team` | The team you want to use with this command.
`--runtime <runtime>` | - | Choose between Node.js ('node24' or 'node22') or Python ('python3.13'). We'll use Node.js 24 by default.
`--timeout <duration>` | - | How long the sandbox can run before we automatically stop it. Examples: '5m', '1h'. We'll stop it after 5 minutes by default.
`--publish-port <port>` | `-p` | Make a port from your sandbox accessible via a public URL.
`--workdir <directory>` | `-w` | Set the directory where you want the command to run.
`--env <key=value>` | `-e` | Set environment variables for your command.
###  [Sandbox run flags](https://vercel.com/docs/cron-jobs#sandbox-run-flags)[](https://vercel.com/docs/cron-jobs#sandbox-run-flags)
Flag | Short | Description
---|---|---
`--sudo` | - | Run the command with admin privileges.
`--interactive` | `-i` | Run the command in an interactive shell.
`--tty` | `-t` | Enable terminal features for interactive commands.
`--rm` | - | Automatically delete the sandbox when the command finishes.
`--help` | `-h` | Display help information.
###  [Sandbox run arguments](https://vercel.com/docs/cron-jobs#sandbox-run-arguments)[](https://vercel.com/docs/cron-jobs#sandbox-run-arguments)
Argument | Description
---|---
`<command>` | The command you want to run.
`[...args]` | Additional arguments for your command.
