##  [`sandbox --help`](https://vercel.com/docs/cron-jobs#sandbox---help)[](https://vercel.com/docs/cron-jobs#sandbox---help)
Get help information for all available sandbox commands:
terminal
```
sandbox <subcommand>
```

Description: Interfacing with Vercel Sandbox
Available subcommands:
  * [`list`](https://vercel.com/docs/cron-jobs#sandbox-list): List all sandboxes for the specified account and project. [alias: `ls`]
  * [`create`](https://vercel.com/docs/cron-jobs#sandbox-create): Create a sandbox in the specified account and project.
  * [`config`](https://vercel.com/docs/cron-jobs#sandbox-config): Update configuration of a running sandbox (e.g. network firewall)
  * [`copy`](https://vercel.com/docs/cron-jobs#sandbox-copy): Copy files between your local filesystem and a remote sandbox [alias: `cp`]
  * [`exec`](https://vercel.com/docs/cron-jobs#sandbox-exec): Execute a command in an existing sandbox
  * [`connect`](https://vercel.com/docs/cron-jobs#sandbox-connect): Start an interactive shell in an existing sandbox [aliases: `ssh`, `shell`]
  * [`stop`](https://vercel.com/docs/cron-jobs#sandbox-stop): Stop one or more running sandboxes [aliases: `rm`, `remove`]
  * [`run`](https://vercel.com/docs/cron-jobs#sandbox-run): Create and run a command in a sandbox
  * [`snapshot`](https://vercel.com/docs/cron-jobs#sandbox-snapshot): Take a snapshot of the filesystem of a sandbox
  * [`snapshots`](https://vercel.com/docs/cron-jobs#sandbox-snapshots): Manage sandbox snapshots
  * [`login`](https://vercel.com/docs/cron-jobs#sandbox-login): Log in to the Sandbox CLI
  * [`logout`](https://vercel.com/docs/cron-jobs#sandbox-logout): Log out of the Sandbox CLI


For more help, try running `sandbox <subcommand> --help`
