# Remove access to a namespace:
temporal cloud user set-namespace-permissions --user-id my-user-id \
  --namespace-access my-namespace.my-account=
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--api-key` | No | **string** API key for authenticating with Temporal Cloud. Can be used instead of interactive login for automation and CI/CD pipelines. |
| `--async` | No | **bool** Return immediately after initiating the operation instead of waiting for completion. Use the returned operation ID to check status later. |
| `--async-operation-id` | No | **string** Custom identifier for tracking this async operation. If not provided, a unique ID is generated automatically. |
| `--idempotent` | No | **bool** Succeed silently if the resource already exists or matches the specification. Without this flag, the command errors when no changes are needed. |
| `--namespace-access` | Yes | **string[]** Namespace access change in the format 'namespace=permission'. Permission must be one of: admin, write, read. Can be repeated. Use an empty permission (e.g. 'testns=') to remove access to a namespace. Changes are additive: namespaces not listed are left unchanged. |
| `--poll-interval` | No | **duration** Time to wait between status checks when waiting for operation completion. Cannot be greater than 10 minutes. Supports minutes (m) and seconds (s). |
| `--resource-version`, `-v` | No | **string** Resource version for optimistic concurrency control. If not provided, the current version is fetched automatically. |
| `--server` | No | **string** Override the Temporal Cloud API server address. Used for connecting to non-production environments. |
| `--user-email` | No | **string** The email address of the user. Mutually exclusive with --user-id. |
| `--user-id` | No | **string** The ID of the user. Mutually exclusive with --user-email. |

## Global Flags

The following options can be used with any command.

| Flag | Required | Description | Default |
|------|----------|-------------|--------|
| `--api-key` | No | **string** API key for authenticating with Temporal Cloud. Can be used instead of interactive login for automation and CI/CD pipelines. |  |
| `--auto-confirm` | No | **bool** Automatically confirm prompts and actions that require user confirmation. Useful for scripting and automation. |  |
| `--config-dir` | No | **string** Directory path where CLI configuration files are stored, including authentication tokens and settings. |  |
| `--disable-pop-up` | No | **bool** Prevent the CLI from opening a browser window during authentication. Useful for headless environments or when using alternative auth methods. |  |
| `--server` | No | **string** Override the Temporal Cloud API server address. Used for connecting to non-production environments. | `saas-api.tmprl.cloud:443` |

---

## Temporal CLI cloud whoami command reference

{/* NOTE: This is an auto-generated file. Any edit to this file will be overwritten.
This file is generated from https://github.com/temporalio/cli via cmd/gen-docs */}

<ReleaseNoteHeader featureName="cloudCli" />

This page provides a reference for the `temporal cloud whoami` command.

Display information about the currently authenticated identity.

Shows whether you are authenticated as a user or service account, along
with the associated API key if one is in use.

Example:

```
temporal cloud whoami
```

| Flag | Required | Description |
|------|----------|-------------|
| `--api-key` | No | **string** API key for authenticating with Temporal Cloud. Can be used instead of interactive login for automation and CI/CD pipelines. |
| `--server` | No | **string** Override the Temporal Cloud API server address. Used for connecting to non-production environments. |

---

## Temporal CLI config command reference

{/* NOTE: This is an auto-generated file. Any edit to this file will be overwritten.
This file is generated from https://github.com/temporalio/cli/blob/main/internal/commandsgen/commands.yml via internal/cmd/gen-docs */}

This page provides a reference for the `temporal` CLI `config` command. The flags applicable to each subcommand are presented in a table within the heading for the subcommand. Refer to [Global Flags](#global-flags) for flags that you can use with every subcommand.

## delete

Remove a property within a profile.

```
temporal config delete \
    --prop tls.client_cert_path
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--prop`, `-p` | Yes | **string** Specific property to delete. If unset, deletes entire profile. |

## delete-profile

Remove a full profile entirely. The `--profile` must be set explicitly.

```
temporal config delete-profile \
    --profile my-profile
```

Use [global flags](#global-flags) to customize the connection to the Temporal Service for this command.

## get

Display specific properties or the entire profile.

```
temporal config get \
    --prop address
```

or

```
temporal config get
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--prop`, `-p` | No | **string** Specific property to get. |

## list

List profile names in the config file.

```
temporal config list
```

Use [global flags](#global-flags) to customize the connection to the Temporal Service for this command.

## set

Assign a value to a property and store it in the config file:

```
temporal config set \
    --prop address \
    --value us-west-2.aws.api.temporal.io:7233
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--prop`, `-p` | Yes | **string** Property name. |
| `--value`, `-v` | Yes | **string** Property value. |

## Global Flags

The following options can be used with any command.

| Flag | Required | Description | Default |
|------|----------|-------------|--------|
| `--address` | No | **string** Temporal Service gRPC endpoint. | `localhost:7233` |
| `--api-key` | No | **string** API key for request. |  |
| `--client-authority` | No | **string** Temporal gRPC client :authority pseudoheader. |  |
| `--client-connect-timeout` | No | **duration** The client connection timeout. 0s means no timeout. |  |
| `--codec-auth` | No | **string** Authorization header for Codec Server requests. |  |
| `--codec-endpoint` | No | **string** Remote Codec Server endpoint. |  |
| `--codec-header` | No | **string[]** HTTP headers for requests to codec server. Format as a `KEY=VALUE` pair. May be passed multiple times to set multiple headers. |  |
| `--color` | No | **string-enum** Output coloring. Accepted values: always, never, auto. | `auto` |
| `--command-timeout` | No | **duration** The command execution timeout. 0s means no timeout. |  |
| `--config-file` | No | **string** File path to read TOML config from, defaults to `$CONFIG_PATH/temporalio/temporal.toml` where `$CONFIG_PATH` is defined as `$HOME/.config` on Unix, `$HOME/Library/Application Support` on macOS, and `%AppData%` on Windows. |  |
| `--disable-config-env` | No | **bool** If set, disables loading environment config from environment variables. |  |
| `--disable-config-file` | No | **bool** If set, disables loading environment config from config file. |  |
| `--env` | No | **string** Active environment name (`ENV`). | `default` |
| `--env-file` | No | **string** Path to environment settings file. Defaults to `$HOME/.config/temporalio/temporal.yaml`. |  |
| `--grpc-meta` | No | **string[]** HTTP headers for requests. Format as a `KEY=VALUE` pair. May be passed multiple times to set multiple headers. Can also be made available via environment variable as `TEMPORAL_GRPC_META_[name]`. |  |
| `--identity` | No | **string** The identity of the user or client submitting this request. Defaults to "temporal-cli:$USER@$HOST". |  |
| `--log-format` | No | **string-enum** Log format. Accepted values: text, json. | `text` |
| `--log-level` | No | **string-enum** Log level. Default is "never" for most commands and "warn" for "server start-dev". Accepted values: debug, info, warn, error, never. | `never` |
| `--namespace`, `-n` | No | **string** Temporal Service Namespace. | `default` |
| `--no-json-shorthand-payloads` | No | **bool** Raw payload output, even if the JSON option was used. |  |
| `--output`, `-o` | No | **string-enum** Non-logging data output format. Accepted values: text, json, jsonl, none. | `text` |
| `--profile` | No | **string** Profile to use for config file. |  |
| `--time-format` | No | **string-enum** Time format. Accepted values: relative, iso, raw. | `relative` |
| `--tls` | No | **bool** Enable base TLS encryption. Does not have additional options like mTLS or client certs. This is defaulted to true if api-key or any other TLS options are present. Use --tls=false to explicitly disable. |  |
| `--tls-ca-data` | No | **string** Data for server CA certificate. Can't be used with --tls-ca-path. |  |
| `--tls-ca-path` | No | **string** Path to server CA certificate. Can't be used with --tls-ca-data. |  |
| `--tls-cert-data` | No | **string** Data for x509 certificate. Can't be used with --tls-cert-path. |  |
| `--tls-cert-path` | No | **string** Path to x509 certificate. Can't be used with --tls-cert-data. |  |
| `--tls-disable-host-verification` | No | **bool** Disable TLS host-name verification. |  |
| `--tls-key-data` | No | **string** Private certificate key data. Can't be used with --tls-key-path. |  |
| `--tls-key-path` | No | **string** Path to x509 private key. Can't be used with --tls-key-data. |  |
| `--tls-server-name` | No | **string** Override target TLS server name. |  |

---

## Temporal CLI env command reference

{/* NOTE: This is an auto-generated file. Any edit to this file will be overwritten.
This file is generated from https://github.com/temporalio/cli/blob/main/internal/commandsgen/commands.yml via internal/cmd/gen-docs */}

This page provides a reference for the `temporal` CLI `env` command. The flags applicable to each subcommand are presented in a table within the heading for the subcommand. Refer to [Global Flags](#global-flags) for flags that you can use with every subcommand.

## delete

Remove a presets environment entirely _or_ remove a key-value pair within an
environment. If you don't specify an environment (with `--env` or by setting
the `TEMPORAL_ENV` variable), this command updates the "default" environment:

```
temporal env delete \
    --env YourEnvironment
```

or

```
temporal env delete \
    --env prod \
    --key tls-key-path
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--key`, `-k` | No | **string** Property name. |

## get

List the properties for a given environment:

```
temporal env get \
    --env YourEnvironment
```

Print a single property:

```
temporal env get \
    --env YourEnvironment \
    --key YourPropertyKey
```

If you don't specify an environment (with `--env` or by setting the
`TEMPORAL_ENV` variable), this command lists properties of the "default"
environment.

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--key`, `-k` | No | **string** Property name. |

## list

List the environments you have set up on your local computer. Environments are
stored in "$HOME/.config/temporalio/temporal.yaml".

Use [global flags](#global-flags) to customize the connection to the Temporal Service for this command.

## set

Assign a value to a property key and store it to an environment:

```
temporal env set \
    --env environment \
    --key property \
    --value value
```

If you don't specify an environment (with `--env` or by setting the
`TEMPORAL_ENV` variable), this command sets properties in the "default"
environment.

Storing keys with CLI option names lets the CLI automatically set those
options for you. This reduces effort and helps avoid typos when issuing
commands.

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--key`, `-k` | No | **string** Property name (required). |
| `--value`, `-v` | No | **string** Property value (required). |

## Global Flags

The following options can be used with any command.

| Flag | Required | Description | Default |
|------|----------|-------------|--------|
| `--address` | No | **string** Temporal Service gRPC endpoint. | `localhost:7233` |
| `--api-key` | No | **string** API key for request. |  |
| `--client-authority` | No | **string** Temporal gRPC client :authority pseudoheader. |  |
| `--client-connect-timeout` | No | **duration** The client connection timeout. 0s means no timeout. |  |
| `--codec-auth` | No | **string** Authorization header for Codec Server requests. |  |
| `--codec-endpoint` | No | **string** Remote Codec Server endpoint. |  |
| `--codec-header` | No | **string[]** HTTP headers for requests to codec server. Format as a `KEY=VALUE` pair. May be passed multiple times to set multiple headers. |  |
| `--color` | No | **string-enum** Output coloring. Accepted values: always, never, auto. | `auto` |
| `--command-timeout` | No | **duration** The command execution timeout. 0s means no timeout. |  |
| `--config-file` | No | **string** File path to read TOML config from, defaults to `$CONFIG_PATH/temporalio/temporal.toml` where `$CONFIG_PATH` is defined as `$HOME/.config` on Unix, `$HOME/Library/Application Support` on macOS, and `%AppData%` on Windows. |  |
| `--disable-config-env` | No | **bool** If set, disables loading environment config from environment variables. |  |
| `--disable-config-file` | No | **bool** If set, disables loading environment config from config file. |  |
| `--env` | No | **string** Active environment name (`ENV`). | `default` |
| `--env-file` | No | **string** Path to environment settings file. Defaults to `$HOME/.config/temporalio/temporal.yaml`. |  |
| `--grpc-meta` | No | **string[]** HTTP headers for requests. Format as a `KEY=VALUE` pair. May be passed multiple times to set multiple headers. Can also be made available via environment variable as `TEMPORAL_GRPC_META_[name]`. |  |
| `--identity` | No | **string** The identity of the user or client submitting this request. Defaults to "temporal-cli:$USER@$HOST". |  |
| `--log-format` | No | **string-enum** Log format. Accepted values: text, json. | `text` |
| `--log-level` | No | **string-enum** Log level. Default is "never" for most commands and "warn" for "server start-dev". Accepted values: debug, info, warn, error, never. | `never` |
| `--namespace`, `-n` | No | **string** Temporal Service Namespace. | `default` |
| `--no-json-shorthand-payloads` | No | **bool** Raw payload output, even if the JSON option was used. |  |
| `--output`, `-o` | No | **string-enum** Non-logging data output format. Accepted values: text, json, jsonl, none. | `text` |
| `--profile` | No | **string** Profile to use for config file. |  |
| `--time-format` | No | **string-enum** Time format. Accepted values: relative, iso, raw. | `relative` |
| `--tls` | No | **bool** Enable base TLS encryption. Does not have additional options like mTLS or client certs. This is defaulted to true if api-key or any other TLS options are present. Use --tls=false to explicitly disable. |  |
| `--tls-ca-data` | No | **string** Data for server CA certificate. Can't be used with --tls-ca-path. |  |
| `--tls-ca-path` | No | **string** Path to server CA certificate. Can't be used with --tls-ca-data. |  |
| `--tls-cert-data` | No | **string** Data for x509 certificate. Can't be used with --tls-cert-path. |  |
| `--tls-cert-path` | No | **string** Path to x509 certificate. Can't be used with --tls-cert-data. |  |
| `--tls-disable-host-verification` | No | **bool** Disable TLS host-name verification. |  |
| `--tls-key-data` | No | **string** Private certificate key data. Can't be used with --tls-key-path. |  |
| `--tls-key-path` | No | **string** Path to x509 private key. Can't be used with --tls-key-data. |  |
| `--tls-server-name` | No | **string** Override target TLS server name. |  |

---

## Temporal CLI command reference

This section includes the complete command reference for the `temporal` CLI, including the cloud extension.

- [activity](/cli/command-reference/activity)
- [batch](/cli/command-reference/batch)
- [cloud](/cli/command-reference/cloud)
- [config](/cli/command-reference/config)
- [env](/cli/command-reference/env)
- [operator](/cli/command-reference/operator)
- [schedule](/cli/command-reference/schedule)
- [server](/cli/command-reference/server)
- [task-queue](/cli/command-reference/task-queue)
- [worker](/cli/command-reference/worker)
- [workflow](/cli/command-reference/workflow)

---

## Temporal CLI operator command reference

{/* NOTE: This is an auto-generated file. Any edit to this file will be overwritten.
This file is generated from https://github.com/temporalio/cli/blob/main/internal/commandsgen/commands.yml via internal/cmd/gen-docs */}

This page provides a reference for the `temporal` CLI `operator` command. The flags applicable to each subcommand are presented in a table within the heading for the subcommand. Refer to [Global Flags](#global-flags) for flags that you can use with every subcommand.

## cluster

Perform operator actions on Temporal Services (also known as Clusters).

```
temporal operator cluster [subcommand] [options]
```

For example to check Service/Cluster health:

```
temporal operator cluster health
```

### describe

View information about a Temporal Cluster (Service), including Cluster Name,
persistence store, and visibility store. Add `--detail` for additional info:

```
temporal operator cluster describe [--detail]
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--detail` | No | **bool** Show history shard count and Cluster/Service version information. |

### health

View information about the health of a Temporal Service:

```
temporal operator cluster health
```

Use [global flags](#global-flags) to customize the connection to the Temporal Service for this command.

### list

Print a list of remote Temporal Clusters (Services) registered to the local
Service. Report details include the Cluster's name, ID, address, History Shard
count, Failover version, and availability:

```
temporal operator cluster list [--limit max-count]
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--limit` | No | **int** Maximum number of Clusters to display. |

### remove

Remove a registered remote Temporal Cluster (Service) from the local Service.

```
temporal operator cluster remove \
    --name YourClusterName
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--name` | Yes | **string** Cluster/Service name. |

### system

Show Temporal Server information for Temporal Clusters (Service): Server
version, scheduling support, and more. This information helps diagnose
problems with the Temporal Server.

The command defaults to the local Service. Otherwise, use the
`--frontend-address` option to specify a Cluster (Service) endpoint:

```
temporal operator cluster system \
    --frontend-address "YourRemoteEndpoint:YourRemotePort"
```

Use [global flags](#global-flags) to customize the connection to the Temporal Service for this command.

### upsert

Add, remove, or update a registered ("remote") Temporal Cluster (Service).

```
temporal operator cluster upsert [options]
```

For example:

```
temporal operator cluster upsert \
    --frontend-address "YourRemoteEndpoint:YourRemotePort"
    --enable-connection false
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--enable-connection` | No | **bool** Set the connection to "enabled". |
| `--enable-replication` | No | **bool** Set the replication to "enabled". |
| `--frontend-address` | Yes | **string** Remote endpoint. |

## namespace

Manage Temporal Cluster (Service) Namespaces:

```
temporal operator namespace [command] [command options]
```

For example:

```
temporal operator namespace create \
    --namespace YourNewNamespaceName
```

### create

Create a new Namespace on the Temporal Service:

```
temporal operator namespace create \
    --namespace YourNewNamespaceName \
    [options]
```

Create a Namespace with multi-region data replication:

```
temporal operator namespace create \
    --global \
    --namespace YourNewNamespaceName
```

Configure settings like retention and Visibility Archival State as needed.
For example, the Visibility Archive can be set on a separate URI:

```
temporal operator namespace create \
    --retention 5d \
    --visibility-archival-state enabled \
    --visibility-uri YourURI \
    --namespace YourNewNamespaceName
```

Note: URI values for archival states can't be changed once enabled.

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--active-cluster` | No | **string** Active Cluster (Service) name. |
| `--cluster` | No | **string[]** Cluster (Service) names for Namespace creation. Can be passed multiple times. |
| `--data` | No | **string[]** Namespace data as `KEY=VALUE` pairs. Keys must be identifiers, and values must be JSON values. For example: `YourKey={"your": "value"}` Can be passed multiple times. |
| `--description` | No | **string** Namespace description. |
| `--email` | No | **string** Owner email. |
| `--global` | No | **bool** Enable multi-region data replication. |
| `--history-archival-state` | No | **string-enum** History archival state. Accepted values: disabled, enabled. |
| `--history-uri` | No | **string** Archive history to this `URI`. Once enabled, can't be changed. |
| `--retention` | No | **duration** Time to preserve closed Workflows before deletion. |
| `--visibility-archival-state` | No | **string-enum** Visibility archival state. Accepted values: disabled, enabled. |
| `--visibility-uri` | No | **string** Archive visibility data to this `URI`. Once enabled, can't be changed. |

### delete

Removes a Namespace from the Service.

```
temporal operator namespace delete [options]
```

For example:

```
temporal operator namespace delete \
    --namespace YourNamespaceName
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--yes`, `-y` | No | **bool** Request confirmation before deletion. |

### describe

Provide long-form information about a Namespace identified by its ID or name:

```
temporal operator namespace describe \
    --namespace-id YourNamespaceId
```

or

```
temporal operator namespace describe \
    --namespace YourNamespaceName
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--namespace-id` | No | **string** Namespace ID. |

### list

Display a detailed listing for all Namespaces on the Service:

```
temporal operator namespace list
```

Use [global flags](#global-flags) to customize the connection to the Temporal Service for this command.

### update

Update a Namespace using properties you specify.

```
temporal operator namespace update [options]
```

Assign a Namespace's active Cluster (Service):

```
temporal operator namespace update \
    --namespace YourNamespaceName \
    --active-cluster NewActiveCluster
```

Promote a Namespace for multi-region data replication:

```
temporal operator namespace update \
    --namespace YourNamespaceName \
    --promote-global
```

You may update archives that were previously enabled or disabled. Note: URI
values for archival states can't be changed once enabled.

```
temporal operator namespace update \
    --namespace YourNamespaceName \
    --history-archival-state enabled \
    --visibility-archival-state disabled
