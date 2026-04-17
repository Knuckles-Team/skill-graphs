##  [`sandbox create`](https://vercel.com/docs/cron-jobs#sandbox-create)[](https://vercel.com/docs/cron-jobs#sandbox-create)
Create a sandbox in the specified account and project.
terminal
```
sandbox create [OPTIONS]
```

###  [Sandbox create example](https://vercel.com/docs/cron-jobs#sandbox-create-example)[](https://vercel.com/docs/cron-jobs#sandbox-create-example)
terminal
```
# Create a basic Node.js sandbox
sandbox create

# Create a Python sandbox with custom timeout
sandbox create --runtime python3.13 --timeout 1h

# Create sandbox with port forwarding
sandbox create --publish-port 8080 --project my-app

# Create sandbox silently (no output)
sandbox create --silent

# Create sandbox from a snapshot
sandbox create --snapshot snap_abc123

# Create sandbox without Internet access
sandbox create --network-policy deny-all

# Create sandbox with restricted Internet access (limited to Vercel's AI gateway)
sandbox create --allowed-domain ai-gateway.vercel.sh
```

###  [Sandbox create options](https://vercel.com/docs/cron-jobs#sandbox-create-options)[](https://vercel.com/docs/cron-jobs#sandbox-create-options)
Option | Alias | Description
---|---|---
`--token <token>` | - | Your [Vercel authentication token](https://vercel.com/kb/guide/how-do-i-use-a-vercel-api-access-token). If you don't provide it, we'll use a stored token or prompt you to log in.
`--project <project>` | - | The [project name or ID](https://vercel.com/docs/project-configuration/general-settings#project-id) you want to use with this command.
`--scope <team>` | `--team` | The team you want to use with this command.
`--runtime <runtime>` | - | Choose between Node.js ('node24' or 'node22') or Python ('python3.13'). We'll use Node.js 24 by default.
`--timeout <duration>` | - | How long the sandbox can run before we automatically stop it. Examples: '5m', '1h'. We'll stop it after 5 minutes by default.
`--publish-port <port>` | `-p` | Make a port from your sandbox accessible via a public URL.
`--snapshot <snapshot_id>` | - | Create the sandbox from a previously saved snapshot.
`--network-policy <mode>` | - | Base network mode to start the sandbox with ('allow-all' - default or 'deny-all'). Leave unset if using more specific rules.
`--allowed-domain <domain>` | - | List of domains (or pattern) to allow access to (only applicable in 'custom' mode). Use wildcard `*` to match multiple domains or subdomains.
`--allowed-cidr <cidr>` | - | List of address ranges to allow access to (only applicable in 'custom' mode). Traffic to those addresses will bypass domain matching.
`--denied-cidr <cidr>` | - | List of address ranges to deny access to (only applicable in 'custom' mode). Those take precedence over allowed domains and addresses.
###  [Sandbox create flags](https://vercel.com/docs/cron-jobs#sandbox-create-flags)[](https://vercel.com/docs/cron-jobs#sandbox-create-flags)
Flag | Short | Description
---|---|---
`--silent` | - | Create the sandbox without showing you the sandbox ID.
`--connect` | - | Start an interactive shell session after creating the sandbox.
`--help` | `-h` | Display help information.
