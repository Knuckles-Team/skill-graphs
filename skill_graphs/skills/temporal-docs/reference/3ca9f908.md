
```
temporal task-queue get-build-id-reachability \
    --task-queue YourTaskQueue \
    --build-id "YourBuildId"
```

You can specify the `--build-id` and `--task-queue` flags multiple times. If
`--task-queue` is omitted, the command checks Build ID reachability against
all Task Queues.

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--build-id` | No | **string[]** One or more Build ID strings. Can be passed multiple times. |
| `--reachability-type` | No | **string-enum** Reachability filter. `open`: reachable by one or more open workflows. `closed`: reachable by one or more closed workflows. `existing`: reachable by either. New Workflow Executions reachable by a Build ID are always reported. Accepted values: open, closed, existing. |
| `--task-queue`, `-t` | No | **string[]** Search only the specified task queue(s). Can be passed multiple times. |

## get-build-ids

```
+-----------------------------------------------------------------------------+
| CAUTION: This command is deprecated and will be removed in a later release. |
+-----------------------------------------------------------------------------+
```

Fetch sets of compatible Build IDs for specified Task Queues and display their
information:

```
temporal task-queue get-build-ids \
    --task-queue YourTaskQueue
```

This command is limited to Namespaces that support Worker versioning.

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--max-sets` | No | **int** Max return count. Use 1 for default major version. Use 0 for all sets. |
| `--task-queue`, `-t` | Yes | **string** Task Queue name. |

## list-partition

Display a Task Queue's partition list with assigned matching nodes:

```
temporal task-queue list-partition \
    --task-queue YourTaskQueue
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--task-queue`, `-t` | Yes | **string** Task Queue name. |

## update-build-ids

```
+-----------------------------------------------------------------------------+
| CAUTION: This command is deprecated and will be removed in a later release. |
+-----------------------------------------------------------------------------+
```

Add or change a Task Queue's compatible Build IDs for Namespaces using Worker
versioning:

```
temporal task-queue update-build-ids [subcommands] [options] \
    --task-queue YourTaskQueue
```

### add-new-compatible

Add a compatible Build ID to a Task Queue's existing version set. Provide an
existing Build ID and a new Build ID:

```
temporal task-queue update-build-ids add-new-compatible \
    --task-queue YourTaskQueue \
    --existing-compatible-build-id "YourExistingBuildId" \
    --build-id "YourNewBuildId"
```

The new ID is stored in the set containing the existing ID and becomes the new
default for that set.

This command is limited to Namespaces that support Worker versioning.

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--build-id` | Yes | **string** Build ID to be added. |
| `--existing-compatible-build-id` | Yes | **string** Pre-existing Build ID in this Task Queue. |
| `--set-as-default` | No | **bool** Set the expanded Build ID set as the Task Queue default. |
| `--task-queue`, `-t` | Yes | **string** Task Queue name. |

### add-new-default

```
+-----------------------------------------------------------------------------+
| CAUTION: This command is deprecated and will be removed in a later release. |
+-----------------------------------------------------------------------------+
```

Create a new Task Queue Build ID set, add a Build ID to it, and make it the
overall Task Queue default. The new set will be incompatible with previous
sets and versions.

```
temporal task-queue update-build-ids add-new-default \
    --task-queue YourTaskQueue \
    --build-id "YourNewBuildId"
```

```
+------------------------------------------------------------------------+
| NOTICE: This command is limited to Namespaces that support Worker      |
| versioning. Worker versioning is experimental. Versioning commands are |
| subject to change.                                                     |
+------------------------------------------------------------------------+
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--build-id` | Yes | **string** Build ID to be added. |
| `--task-queue`, `-t` | Yes | **string** Task Queue name. |

### promote-id-in-set

```
+-----------------------------------------------------------------------------+
| CAUTION: This command is deprecated and will be removed in a later release. |
+-----------------------------------------------------------------------------+
```

Establish an existing Build ID as the default in its Task Queue set. New tasks
compatible with this set will now be dispatched to this ID:

```
temporal task-queue update-build-ids promote-id-in-set \
    --task-queue YourTaskQueue \
    --build-id "YourBuildId"
```

```
+------------------------------------------------------------------------+
| NOTICE: This command is limited to Namespaces that support Worker      |
| versioning. Worker versioning is experimental. Versioning commands are |
| subject to change.                                                     |
+------------------------------------------------------------------------+
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--build-id` | Yes | **string** Build ID to set as default. |
| `--task-queue`, `-t` | Yes | **string** Task Queue name. |

### promote-set

```
+-----------------------------------------------------------------------------+
| CAUTION: This command is deprecated and will be removed in a later release. |
+-----------------------------------------------------------------------------+
```

Promote a Build ID set to be the default on a Task Queue. Identify the set by
providing a Build ID within it. If the set is already the default, this
command has no effect:

```
temporal task-queue update-build-ids promote-set \
    --task-queue YourTaskQueue \
    --build-id "YourBuildId"
```

```
+------------------------------------------------------------------------+
| NOTICE: This command is limited to Namespaces that support Worker      |
| versioning. Worker versioning is experimental. Versioning commands are |
| subject to change.                                                     |
+------------------------------------------------------------------------+
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--build-id` | Yes | **string** Build ID within the promoted set. |
| `--task-queue`, `-t` | Yes | **string** Task Queue name. |

## versioning

```
+---------------------------------------------------------------------+
| CAUTION: This API has been deprecated by Worker Deployment.         |
+---------------------------------------------------------------------+
```

Provides commands to add, list, remove, or replace Worker Build ID assignment
and redirect rules associated with Task Queues:

```
temporal task-queue versioning [subcommands] [options] \
    --task-queue YourTaskQueue
```

Task Queues support the following versioning rules and policies:

- Assignment Rules: manage how new executions are assigned to run on specific
  Worker Build IDs. Each Task Queue stores a list of ordered Assignment Rules,
  which are evaluated from first to last. Assignment Rules also allow for
  gradual rollout of new Build IDs by setting ramp percentage.
- Redirect Rules: automatically assign work for a source Build ID to a target
  Build ID. You may add at most one redirect rule for each source Build ID.
  Redirect rules require that a target Build ID is fully compatible with
  the source Build ID.

### add-redirect-rule

Add a new redirect rule for a given Task Queue. You may add at most one
redirect rule for each distinct source build ID:

```
temporal task-queue versioning add-redirect-rule \
    --task-queue YourTaskQueue \
    --source-build-id "YourSourceBuildID" \
    --target-build-id "YourTargetBuildID"
```

```
+---------------------------------------------------------------------+
| CAUTION: This API has been deprecated by Worker Deployment.         |
+---------------------------------------------------------------------+
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--source-build-id` | Yes | **string** Source build ID. |
| `--target-build-id` | Yes | **string** Target build ID. |
| `--yes`, `-y` | No | **bool** Don't prompt to confirm. |

### commit-build-id

Complete a Build ID's rollout and clean up unnecessary rules that might have
been created during a gradual rollout:

```
temporal task-queue versioning commit-build-id \
    --task-queue YourTaskQueue
    --build-id "YourBuildId"
```

This command automatically applies the following atomic changes:

- Adds an unconditional assignment rule for the target Build ID at the
  end of the list.
- Removes all previously added assignment rules to the given target
  Build ID.
- Removes any unconditional assignment rules for other Build IDs.

Rejects requests when there have been no recent pollers for this Build ID.
This prevents committing invalid Build IDs. Use the `--force` option to
override this validation.

```
+---------------------------------------------------------------------+
| CAUTION: This API has been deprecated by Worker Deployment.         |
+---------------------------------------------------------------------+
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--build-id` | Yes | **string** Target build ID. |
| `--force` | No | **bool** Bypass recent-poller validation. |
| `--yes`, `-y` | No | **bool** Don't prompt to confirm. |

### delete-assignment-rule

Deletes a rule identified by its index in the Task Queue's list of assignment
rules.

```
temporal task-queue versioning delete-assignment-rule \
    --task-queue YourTaskQueue \
    --rule-index YourIntegerRuleIndex
```

By default, the Task Queue must retain one unconditional rule, such as "no
hint filter" or "percentage". Otherwise, the delete operation is rejected.
Use the `--force` option to override this validation.

```
+---------------------------------------------------------------------+
| CAUTION: This API has been deprecated by Worker Deployment.         |
+---------------------------------------------------------------------+
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--force` | No | **bool** Bypass one-unconditional-rule validation. |
| `--rule-index`, `-i` | Yes | **int** Position of the assignment rule to be replaced. Requests for invalid indices will fail. |
| `--yes`, `-y` | No | **bool** Don't prompt to confirm. |

### delete-redirect-rule

Deletes the routing rule for the given source Build ID.

```
temporal task-queue versioning delete-redirect-rule \
    --task-queue YourTaskQueue \
    --source-build-id "YourBuildId"
```

```
+---------------------------------------------------------------------+
| CAUTION: This API has been deprecated by Worker Deployment.         |
+---------------------------------------------------------------------+
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--source-build-id` | Yes | **string** Source Build ID. |
| `--yes`, `-y` | No | **bool** Don't prompt to confirm. |

### get-rules

Retrieve all the Worker Build ID assignments and redirect rules associated
with a Task Queue:

```
temporal task-queue versioning get-rules \
    --task-queue YourTaskQueue
```

Task Queues support the following versioning rules:

- Assignment Rules: manage how new executions are assigned to run on specific
  Worker Build IDs. Each Task Queue stores a list of ordered Assignment Rules,
  which are evaluated from first to last. Assignment Rules also allow for
  gradual rollout of new Build IDs by setting ramp percentage.
- Redirect Rules: automatically assign work for a source Build ID to a target
  Build ID. You may add at most one redirect rule for each source Build ID.
  Redirect rules require that a target Build ID is fully compatible with
  the source Build ID.
```
+---------------------------------------------------------------------+
| CAUTION: This API has been deprecated by Worker Deployment.         |
+---------------------------------------------------------------------+
```

Use [global flags](#global-flags) to customize the connection to the Temporal Service for this command.

### insert-assignment-rule

Inserts a new assignment rule for this Task Queue. Rules are evaluated in
order, starting from index 0. The first applicable rule is applied, and the
rest ignored:

```
temporal task-queue versioning insert-assignment-rule \
    --task-queue YourTaskQueue \
    --build-id "YourBuildId"
```

If you do not specify a `--rule-index`, this command inserts at index 0.

```
+---------------------------------------------------------------------+
| CAUTION: This API has been deprecated by Worker Deployment.         |
+---------------------------------------------------------------------+
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--build-id` | Yes | **string** Target Build ID. |
| `--percentage` | No | **int** Traffic percent to send to target Build ID. |
| `--rule-index`, `-i` | No | **int** Insertion position. Ranges from 0 (insert at start) to count (append). Any number greater than the count is treated as "append". |
| `--yes`, `-y` | No | **bool** Don't prompt to confirm. |

### replace-assignment-rule

Change an assignment rule for this Task Queue. By default, this enforces one
unconditional rule (no hint filter or percentage). Otherwise, the operation
will be rejected. Set `force` to true to bypass this validation.

```
temporal task-queue versioning replace-assignment-rule \
    --task-queue YourTaskQueue \
    --rule-index AnIntegerIndex \
    --build-id "YourBuildId"
```

To assign multiple assignment rules to a single Build ID, use
'insert-assignment-rule'.

To update the percent:

```
temporal task-queue versioning replace-assignment-rule \
    --task-queue YourTaskQueue \
    --rule-index AnIntegerIndex \
    --build-id "YourBuildId" \
    --percentage AnIntegerPercent
```

Percent may vary between 0 and 100 (default).

```
+---------------------------------------------------------------------+
| CAUTION: This API has been deprecated by Worker Deployment.         |
+---------------------------------------------------------------------+
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--build-id` | Yes | **string** Target Build ID. |
| `--force` | No | **bool** Bypass the validation that one unconditional rule remains. |
| `--percentage` | No | **int** Divert percent of traffic to target Build ID. |
| `--rule-index`, `-i` | Yes | **int** Position of the assignment rule to be replaced. Requests for invalid indices will fail. |
| `--yes`, `-y` | No | **bool** Don't prompt to confirm. |

### replace-redirect-rule

Updates a Build ID's redirect rule on a Task Queue by replacing its target
Build ID:

```
temporal task-queue versioning replace-redirect-rule \
    --task-queue YourTaskQueue \
    --source-build-id YourSourceBuildId \
    --target-build-id YourNewTargetBuildId
```

```
+---------------------------------------------------------------------+
| CAUTION: This API has been deprecated by Worker Deployment.         |
+---------------------------------------------------------------------+
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--source-build-id` | Yes | **string** Source Build ID. |
| `--target-build-id` | Yes | **string** Target Build ID. |
| `--yes`, `-y` | No | **bool** Don't prompt to confirm. |

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

## Temporal CLI worker command reference

{/* NOTE: This is an auto-generated file. Any edit to this file will be overwritten.
This file is generated from https://github.com/temporalio/cli/blob/main/internal/commandsgen/commands.yml via internal/cmd/gen-docs */}

This page provides a reference for the `temporal` CLI `worker` command. The flags applicable to each subcommand are presented in a table within the heading for the subcommand. Refer to [Global Flags](#global-flags) for flags that you can use with every subcommand.

## deployment

Deployment commands perform operations on Worker Deployments:

```
temporal worker deployment [command] [options]
```

For example:

```
temporal worker deployment list
```

Lists the Deployments in the client's namespace.

Arguments can be Worker Deployment Versions associated with
a Deployment, specified using the Deployment name and Build ID.

For example:

```
temporal worker deployment set-current-version \
         --deployment-name YourDeploymentName --build-id YourBuildID
```

Sets the current Deployment Version for a given Deployment.

### create

Create a new Worker Deployment:

```
temporal worker deployment create [options]
```

Worker Deployments are lazily created the first time a Worker polls the
Temporal Server and specifies a VersionOverride. However, if you need to
pre-define a compute configuration (for instance to set up a serverless
Worker), you need to call `temporal worker deployment create-version` and
pass in the name of the Worker Deployment. The `temporal worker
deployment create` command allows you to pre-define a Worker Deployment
so that calls to `temporal worker deployment create-version` will
succeed.

If a Worker Deployment with the supplied name already exists, this
command will return an error.

Note: This is an experimental feature and may change in the future.

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--name`, `-d` | Yes | **string** Name for a Worker Deployment. |

### create-version

Create a new Worker Deployment Version:

```
temporal worker deployment create-version [options]
```

Configure a Worker Deployment Version's compute configuration as needed.
For example, pass compute provider information for an AWS Lambda function
that spawns a Worker in the Worker Deployment:

```
temporal worker deployment create-version \
    --namespace YourNamespaceName \
    --deployment-name YourDeploymentName \
    --build-id YourBuildID \
    --aws-lambda-function-arn LambdaFunctionARN \
    --aws-lambda-assume-role-arn LambdaAssumeRoleARN \
    --aws-lambda-assume-role-external-id LambdaAssumeRoleExternalID
```

If a Worker Deployment Version with the supplied BuildID already exists,
this command will return an error.

Note: This is an experimental feature and may change in the future.

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--aws-lambda-assume-role-arn` | No | **string** AWS IAM role ARN that the Temporal server will assume when invoking the Lambda function that spawns a new Worker in this Worker Deployment Version. Required when --aws-lambda-function-arn is specified. |
| `--aws-lambda-assume-role-external-id` | No | **string** Temporal server will enforce that the AWS IAM trust policy associated with the AWS IAM role specified in --aws-lambda-assume-role-arn has an aws:ExternalId condition that matches the supplied value. Required when --aws-lambda-function-arn is specified. |
