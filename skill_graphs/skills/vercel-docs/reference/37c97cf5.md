##  [`sandbox copy`](https://vercel.com/docs/cron-jobs#sandbox-copy)[](https://vercel.com/docs/cron-jobs#sandbox-copy)
Copy files between your local filesystem and a remote sandbox.
terminal
```
sandbox copy [OPTIONS] <SANDBOX_ID:PATH> <SANDBOX_ID:PATH>
```

###  [Sandbox copy example](https://vercel.com/docs/cron-jobs#sandbox-copy-example)[](https://vercel.com/docs/cron-jobs#sandbox-copy-example)
terminal
```
# Copy file from local to sandbox
sandbox copy ./local-file.txt sb_1234567890:/app/remote-file.txt

# Copy file from sandbox to local
sandbox copy sb_1234567890:/app/output.log ./output.log

# Copy directory from sandbox to local
sandbox copy sb_1234567890:/app/dist/ ./build/
```

###  [Sandbox copy options](https://vercel.com/docs/cron-jobs#sandbox-copy-options)[](https://vercel.com/docs/cron-jobs#sandbox-copy-options)
Option | Alias | Description
---|---|---
`--token <token>` | - | Your [Vercel authentication token](https://vercel.com/kb/guide/how-do-i-use-a-vercel-api-access-token). If you don't provide it, we'll use a stored token or prompt you to log in.
`--project <project>` | - | The [project name or ID](https://vercel.com/docs/project-configuration/general-settings#project-id) you want to use with this command.
`--scope <team>` | `--team` | The team you want to use with this command.
###  [Sandbox copy flags](https://vercel.com/docs/cron-jobs#sandbox-copy-flags)[](https://vercel.com/docs/cron-jobs#sandbox-copy-flags)
Flag | Short | Description
---|---|---
`--help` | `-h` | Display help information.
###  [Sandbox copy arguments](https://vercel.com/docs/cron-jobs#sandbox-copy-arguments)[](https://vercel.com/docs/cron-jobs#sandbox-copy-arguments)
Argument | Description
---|---
`<SANDBOX_ID:PATH>` | The source file path (either a local file or sandbox_id:path for remote files).
`<SANDBOX_ID:PATH>` | The destination file path (either a local file or sandbox_id:path for remote files).
