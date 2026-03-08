##  [`sandbox config`](https://vercel.com/docs/cron-jobs#sandbox-config)[](https://vercel.com/docs/cron-jobs#sandbox-config)
Update configuration of a running sandbox (e.g. network firewall)
terminal
```
sandbox config <command> <SANDBOX_ID> [OPTIONS]
```

###  [Sandbox config example](https://vercel.com/docs/cron-jobs#sandbox-config-example)[](https://vercel.com/docs/cron-jobs#sandbox-config-example)
terminal
```
# Update the sandbox firewall to deny all egress traffic
sandbox config network-policy sb_1234567890 --network-policy deny-all

# Update the sandbox firewall to allow all egress traffic
sandbox config network-policy sb_1234567890 --mode allow-all

# Update the sandbox firewall to specific rules
sandbox config network-policy sb_1234567890 --allowed-domain vercel.com --allowed-domain ai-gateway.vercel.sh
```

###  [Sandbox config network-policy options](https://vercel.com/docs/cron-jobs#sandbox-config-network-policy-options)[](https://vercel.com/docs/cron-jobs#sandbox-config-network-policy-options)
Option | Alias | Description
---|---|---
`--network-policy <mode>` | `--mode` | Base network mode to update the sandbox to ('allow-all' - default, 'deny-all'). Leave unset if using more specific rules.
`--allowed-domain <domain>` | - | List of domains (or pattern) to allow access to (only applicable in 'custom' mode). Use wildcard `*` to match multiple domains or subdomains.
`--allowed-cidr <cidr>` | - | List of address ranges to allow access to (only applicable in 'custom' mode). Traffic to those addresses will bypass domain matching.
`--denied-cidr <cidr>` | - | List of address ranges to deny access to (only applicable in 'custom' mode). Those take precedence over allowed domains and addresses.
###  [Sandbox config network-policy flags](https://vercel.com/docs/cron-jobs#sandbox-config-network-policy-flags)[](https://vercel.com/docs/cron-jobs#sandbox-config-network-policy-flags)
Flag | Short | Description
---|---|---
`--help` | `-h` | Display help information.
###  [Sandbox config network-policy arguments](https://vercel.com/docs/cron-jobs#sandbox-config-network-policy-arguments)[](https://vercel.com/docs/cron-jobs#sandbox-config-network-policy-arguments)
Argument | Description
---|---
`<SANDBOX_ID>` | The running sandbox to update.
