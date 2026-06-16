
Alias: `-v`

**Example**

```bash
tcld account metrics accepted-client-ca remove --resource-version <etag> --ca-certificate <encoded_certificate>
```

##### --ca-certificate

_Required modifier unless `--ca-certificate-fingerprint` or `--ca-certificate-file` is specified_

Specify a base64-encoded string of a CA certificate PEM file.

If `--ca-certificate-fingerprint` is also specified, both `--ca-certificate` and `--ca-certificate-file` are ignored.

If `--ca-certificate-file` is also specified but `--ca-certificate-fingerprint` is not, only `--ca-certificate` is used.

Alias: `-c`

**Example**

```bash
tcld account metrics accepted-client-ca remove --ca-certificate <encoded_certificate>
```

##### --ca-certificate-file

_Required modifier unless `--ca-certificate-fingerprint` or `--ca-certificate` is specified_

Specify a path to a CA certificate PEM file.

If `--ca-certificate-fingerprint` is also specified, both `--ca-certificate-file` and `--ca-certificate` are ignored.

If `--ca-certificate` is also specified but `--ca-certificate-fingerprint` is not, only `--ca-certificate` is used.

Alias: `-f`

**Example**

```bash
tcld account metrics accepted-client-ca remove --ca-certificate-file <path>
```

##### --ca-certificate-fingerprint

_Required modifier unless `--ca-certificate` or `--ca-certificate-file` is specified_

Specify the fingerprint of a CA certificate.

If `--ca-certificate`, `--ca-certificate-file`, or both are also specified, they are ignored.

Alias: `--fp`

**Example**

```bash
tcld account metrics accepted-client-ca remove --ca-certificate-fingerprint <fingerprint>
```

#### set

The `tcld account metrics accepted-client-ca set` command sets the end-entity certificates for the metrics endpoint of a Temporal Cloud account.

:::info

The end-entity certificates for the metrics endpoint must chain up to the CA certificate used for the account. For more information, see [Certificate requirements](/cloud/certificates#certificate-requirements).

:::

`tcld account metrics accepted-client-ca set --ca-certificate <value>`

Alias: `s`

The following modifiers control the behavior of the command.

##### --request-id

Specify a request identifier to use for the asynchronous operation. If not specified, the server assigns a request identifier.

Alias: `-r`

**Example**

```bash
tcld account metrics accepted-client-ca set --request-id <request_id> --ca-certificate <encoded_certificate>
```

##### --resource-version

Specify a resource version (ETag) to update from. If not specified, the latest version is used.

Alias: `-v`

**Example**

```bash
tcld account metrics accepted-client-ca set --resource-version <etag> --ca-certificate <encoded_certificate>
```

##### --ca-certificate

_Required modifier unless `--ca-certificate-file` is specified_

Specify a base64-encoded string of a CA certificate PEM file.

If both `--ca-certificate` and `--ca-certificate-file` are specified, only `--ca-certificate` is used.

Alias: `-c`

**Example**

```bash
tcld account metrics accepted-client-ca set --ca-certificate <encoded_certificate>
```

##### --ca-certificate-file

_Required modifier unless `--ca-certificate` is specified_

Specify a path to a CA certificate PEM file.

If both `--ca-certificate` and `--ca-certificate-file` are specified, only `--ca-certificate` is used.

Alias: `-f`

**Example**

```bash
tcld account metrics accepted-client-ca set --ca-certificate-file <path>
```

### enable

The `tcld account metrics enable` command enables the metrics endpoint for the Temporal Cloud account that is currently logged in.

:::info

The end-entity for the metrics endpoint _must_ be configured before the endpoint can be enabled. See the [tcld account metrics accepted-client-ca](#accepted-client-ca) commands.

:::

`tcld account metrics enable`

The command has no modifiers.

### disable

The `tcld account metrics disable` command disables the metrics endpoint for the Temporal Cloud account that is currently logged in.

`tcld account metrics disable`

The command has no modifiers.

---

## tcld apikey command reference

The `tcld apikey` commands manage API Keys in Temporal Cloud.

Alias: `ak`

- [tcld apikey create](#create)
- [tcld apikey get](#get)
- [tcld apikey list](#list)
- [tcld apikey delete](#delete)
- [tcld apikey disable](#disable)
- [tcld apikey enable](#enable)

## create

The `tcld apikey create` command creates an API Key in Temporal Cloud.

`tcld apikey create --name <name> --description <description> --duration <duration> --expiry <expiry> --request-id <request_id>`

The following options control the behavior of the command.

#### --name

_Required modifier_

Specify the display name of the API Key.

Alias: `-n`

**Example**

```bash
tcld apikey create --name <name>
```

#### --description

Specify a description for the API Key.

Alias: `-desc`

**Example**

```bash
tcld apikey create --name <name> --description "Your API Key"
```

#### --duration

Specify the duration from now when the API Key will expire.
This will be ignored if the expiry flag is set.

Example format: `24h` (default: 0s).

Alias: `-d`

**Example**

```bash
tcld apikey create --name <name> --duration 24h
```

#### --expiry

Specify the absolute timestamp (RFC3339) when the API Key will expire.

Example: `2023-11-28T09:23:24-08:00`.

Alias: `-e`

**Example**

```bash
tcld apikey create --name <name> --expiry '2023-11-28T09:23:24-08:00'
```

#### --request-id

Specify a request-id for the asynchronous operation.
If not set, the server will assign one.

Alias: `-r`

**Example**

```bash
tcld apikey create --name <name> --request-id <request_id>
```

## get

The `tcld apikey get` command retrieves the details of a specified API Key in Temporal Cloud.

`tcld apikey get --id <id>`

The following option controls the behavior of the command.

#### --id

_Required modifier_

Specify the ID of the API Key to retrieve.

Alias: `-i`

**Example**

```bash
tcld apikey get --id <apikey_id>
```

## list

The `tcld apikey list` command lists all API Keys in Temporal Cloud.

`tcld apikey list`

This command does not require any specific options.

Alias: `l`

**Example**

```bash
tcld apikey list
```

## delete

The `tcld apikey delete` command deletes an API Key in Temporal Cloud.

`tcld apikey delete --id <id> [--resource-version <version>] [--request-id <request_id>]`

The following options control the behavior of the command.

#### --id

_Required modifier_

Specify the ID of the API Key to delete.

Alias: `-i`

**Example**

```bash
tcld apikey delete --id <apikey_id>
```

#### --resource-version

Specify the resource-version (etag) to update from.
If not set, the CLI will use the latest.

Alias: `-v`

**Example**

```bash
tcld apikey delete --id <apikey_id> --resource-version <version>
```

#### --request-id

Specify a request-id for the asynchronous operation.
If not set, the server will assign one.

Alias: `-r`

**Example**

```bash
tcld apikey delete --id <apikey_id> --request-id <request_id>
```

## disable

The `tcld apikey disable` command disables an API Key in Temporal Cloud.

`tcld apikey disable --id <id> [--resource-version <version>] [--request-id <request_id>]`

The following options control the behavior of the command.

#### --id

_Required modifier_

Specify the ID of the API Key to disable.

Alias: `-i`

**Example**

```bash
tcld apikey disable --id <apikey_id>
```

#### --resource-version

Specify the resource-version (etag) to update from. If not set, the CLI will use the latest.

Alias: `-v`

**Example**

```bash
tcld apikey disable --id <apikey_id> --resource-version <version>
```

#### --request-id

Specify a request-id for the asynchronous operation. If not set, the server will assign one.

Alias: `-r`

**Example**

```bash
tcld apikey disable --id <apikey_id> --request-id <request_id>
```

## enable

The `tcld apikey enable` command enables a disabled API Key in Temporal Cloud.

`tcld apikey enable --id <id> [--resource-version <version>] [--request-id <request_id>]`

The following options control the behavior of the command.

#### --id

_Required modifier_

Specify the ID of the API Key to enable.

Alias: `-i`

**Example**

```bash
tcld apikey enable --id <apikey_id>
```

#### --resource-version

Specify the resource-version (etag) to update from.
If not set, the CLI will use the latest.

Alias: `-v`

**Example**

```bash
tcld apikey enable --id <apikey_id> --resource-version <version>
```

#### --request-id

Specify a request-id for the asynchronous operation.
If not set, the server will assign one.

Alias: `-r`

**Example**

```bash
tcld apikey enable --id <apikey_id> --request-id <request_id>
```

---

## tcld connectivity-rule command reference

The `tcld connectivity-rule` commands manage [connectivity rules](/cloud/connectivity#connectivity-rules) in Temporal Cloud.

Alias: `cr`

- [tcld connectivity-rule create](#create)
- [tcld connectivity-rule delete](#delete)
- [tcld connectivity-rule get](#get)
- [tcld connectivity-rule list](#list)

## create

The `tcld connectivity-rule create` command creates a connectivity rule.

Alias: `c`

#### --connection-id

The connection ID of the private connection.

Alias: `ci`

#### --connectivity-type

The type of connectivity, currently only support 'private' and 'public'.

Alias: `ct`

#### --enable-stable-ips

Enable Stable IPs on a public Connectivity Rule. When set, Namespaces attached to this rule resolve their Namespace endpoint to a published, fixed set of IP addresses that you can allowlist in your firewall. Only valid with `--connectivity-type public`. See [Stable IPs](/cloud/connectivity/ip-addresses#stable-ip-addresses) for details.

Alias: `esi`

#### --gcp-project-id

The GCP project ID of the connection, required if the cloud provider is 'gcp'.

Alias: `gpi`

#### --region

The region of the connection.

Alias: `r`

## delete

The `tcld connectivity-rule delete` command deletes a connectivity rule.

Alias: `d`

#### --connectivity-rule-id

The connectivity rule ID.

Alias: `id`

## get

The `tcld connectivity-rule get` command gets a connectivity rule.

Alias: `g`

#### --connectivity-rule-id

The connectivity rule ID.

Alias: `id`

## list

The `tcld connectivity-rule list` command lists connectivity rules.

Alias: `l`

#### --namespace

The namespace hosted on temporal cloud.

Alias: `n`

---

## tcld feature command reference

The `tcld feature` commands manage features in Temporal Cloud.

Alias: `f`

- [tcld feature get](#get)
- [tcld feature toggle](#toggle)

## get

The `tcld feature get` command gets information about the Temporal Cloud features you've enabled.

Alias: `g`

`tcld feature get`

The command has no modifiers.

**Example**

`tcld feature get`

The following is an example output:

```json
[
  {
    "Name": "enable-apikey",
    "Value": true
  }
]
```

## toggle

The `tcld feature toggle-*` command turns on or off the `*` feature in Temporal Cloud.

:::note

The `*` symbol represents the name of the feature.
Replace `*` with the name of the available feature to toggle.

:::

Alias: `tak`

`tcld feature toggle-*`

The command has no modifiers.

**Example**

`tcld feature toggle-apikey`

The following is an example output:

```json
Feature flag enable-apikey is now true
```

:::note

The feature `apikey` is an example.
Update the feature name to toggle a different feature.

:::

---

## tcld generate-certificates command reference

The `tcld generate-certificates` commands generate certificate authority (CA) and end-entity TLS certificates for Temporal Cloud.

Alias: `gen`

- [tcld generate-certificates certificate-authority-certificate](#certificate-authority-certificate)
- [tcld generate-certificates end-entity-certificate](#end-entity-certificate)

## tcld generate-certificates certificate-authority-certificate {/* #certificate-authority-certificate */}

The `tcld generate-certificates certificate-authority-certificate` command generates certificate authority (CA) certificates for Temporal Cloud.

`tcld generate-certificates certificate-authority-certificate <modifiers>`

Alias: `ca`

The following modifiers control the behavior of the command.

#### --organization

Specify an organization name for certificate generation.

Alias: `--org`

**Example**

```bash
tcld generate-certificates certificate-authority-certificate --organization <value>
```

#### --validity-period

Specify the duration for which the certificate is valid.
Format values as d/h (for example, `30d10h` for a certificate lasting 30 days and 10 hours).

Alias: `-d`

**Example**

```bash
tcld generate-certificates certificate-authority-certificate --validity-period <value>
```

#### --ca-certificate-file

Specify a path to a `.pem` file where the generated X.509 certificate file will be stored.

Alias: `--ca-cert`

**Example**

```bash
tcld generate-certificates certificate-authority-certificate --ca-certificate-file <path>
```

#### --ca-key-file

Specify a path to a `.key` file where the certificate's private key will be stored.

Alias: `--ca-key`

**Example**

```bash
tcld generate-certificates certificate-authority-certificate --ca-key-file <path>
```

#### --rsa-algorithm

When enabled, a 4096-bit RSA key pair is generated for the certificate instead of an ECDSA P-384 key pair.
Because an ECDSA P-384 key pair is the recommended default, this option is disabled.

Alias: `--rsa`

**Example**

```bash
tcld generate-certificates certificate-authority-certificate --rsa-algorithm <boolean>
```

## tcld generate-certificates end-entity-certificate {/* #end-entity-certificate */}

The `tcld generate-certificates end-entity-certificate` command generates end-entity (leaf) certificates for Temporal Cloud.

`tcld generate-certificates end-entity-certificate <modifiers>`

Alias: `leaf`

The following modifiers control the behavior of the command.

#### --organization

Specify an organization name for certificate generation.

Alias: `--org`

**Example**

```bash
tcld generate-certificates end-entity-certificate --organization <value>
```

#### --organization-unit

Optional: Specify the name of the organization unit.

**Example**

```bash
tcld generate-certificates end-entity-certificate --organization-unit <value>
```

#### --validity-period

Specify the duration for which the certificate is valid.
Format values as d/h (for example, `30d10h` for a certificate lasting 30 days and 10 hours).

Alias: `-d`

**Example**

```bash
tcld generate-certificates end-entity-certificate --validity-period <value>
```

#### --ca-certificate-file

Specify the path of the X.509 CA certificate in a `.pem` file for the certificate authority.

Alias: `--ca-cert`

**Example**

```bash
tcld generate-certificates end-entity-certificate --ca-certificate-file <path>
```

#### --ca-key-file

Specify the path of the private key in a `.key` file for the certificate authority.

Alias: `--ca-key`

**Example**

```bash
tcld generate-certificates end-entity-certificate --ca-key-file <path>
```

#### --certificate-file

Specify a path to a `.pem` file where the generated X.509 leaf certificate file will be stored.

Alias: `--cert`

**Example**

```bash
tcld generate-certificates end-entity-certificate --certificate-file <path>
```

#### --key-file

Specify a path to a `.key` file where the leaf certificate's private key will be stored.

Alias: `--key`

**Example**

```bash
tcld generate-certificates end-entity-certificate --key-file <path>
```

---

## tcld command reference

The Temporal Cloud CLI (tcld) is a command-line tool that you can use to interact with Temporal Cloud.

- [How to install tcld](#install-tcld)

### tcld commands

- [tcld account](/cloud/tcld/account)
- [tcld apikey](/cloud/tcld/apikey)
- [tcld connectivity-rule](/cloud/tcld/connectivity-rule)
- [tcld feature](/cloud/tcld/feature)
- [tcld generate-certificates](/cloud/tcld/generate-certificates)
- [tcld login](/cloud/tcld/login)
- [tcld logout](/cloud/tcld/logout/)
- [tcld namespace](/cloud/tcld/namespace)
- [tcld nexus](/cloud/tcld/nexus)
- [tcld request](/cloud/tcld/request)
- [tcld user](/cloud/tcld/user)
- [tcld version](/cloud/tcld/version/)

### Global modifiers

#### --auto_confirm

Automatically confirm all prompts.

You can specify the value for this modifier by setting the AUTO_CONFIRM environment variable.
The default value is `false`.

## How to install tcld {/* #install-tcld */}

You can install [tcld](/cloud/tcld) in two ways.

### Install tcld by using Homebrew

```bash
brew install temporalio/brew/tcld
```

### Build tcld from source

1. Verify that you have Go 1.18 or later installed.

   ```bash
   go version
   ```

   If Go 1.18 or later is not installed, follow the [Download and install](https://go.dev/doc/install) instructions on the Go website.

1. Clone the tcld repository and run make.

   ```bash
   git clone https://github.com/temporalio/tcld.git
   cd tcld
   make
   ```

1. Copy the tcld executable to any directory that appears in the PATH environment variable, such as `/usr/local/bin`.

   ```bash
   cp tcld /usr/local/bin/tcld
   ```

1. Verify that tcld is installed.

   ```bash
   tcld version
   ```

---

## tcld login command reference

The `tcld login` command logs in a user to Temporal Cloud.

Follow instructions in the browser to log in to your Temporal account.

Alias: `l`

`tcld login`

The command has no modifiers.

---

## tcld logout command reference

The `tcld logout` command logs a user out of Temporal Cloud.

Alias: `lo`

`tcld logout`

The following modifier controls the behavior of the command.

#### --disable-pop-up

Disables a browser pop-up if set to `true`. The default value is `false`.

---

## tcld namespace command reference

The `tcld namespace` commands enable [Namespace](/namespaces) operations in Temporal Cloud.

Alias: `n`

:::info Namespace ID Format

The `--namespace` flag accepts a **Namespace ID** in the format `<namespace_name>.<account_suffix>` (e.g., `your-namespace.a1b2c`). This is the full identifier shown in Temporal Cloud, not just the [Namespace Name](/cloud/namespaces#temporal-cloud-namespace-name). You can find your account suffix in the Temporal Cloud UI.

:::

- [tcld namespace add-region](#add-region)
- [tcld namespace create](#create)
- [tcld namespace delete](#delete)
- [tcld namespace failover](#failover)
- [tcld namespace get](#get)
- [tcld namespace list](#list)
- [tcld namespace export](#export)
- [tcld namespace accepted-client-ca](#accepted-client-ca)
- [tcld namespace certificate-filters](#certificate-filters)
- [tcld namespace search-attributes](#search-attributes)
- [tcld namespace retention](#retention)
- [tcld namespace update-codec-server](#update-codec-server)
- [tcld namespace update-high-availability](#update-high-availability)
- [tcld namespace tags](#tags)
- [tcld namespace set-connectivity-rules](#set-connectivity-rules)

## add-region

Use `tcld namespace add-region` to add a <ToolTipTerm term="replica" /> region to an existing Temporal Cloud [Namespace](/namespaces), upgrading it to support [High Availability](/cloud/high-availability).

See [Regions](/cloud/regions) for available regions and their supported replication options.

The following modifiers control the behavior of the command.

#### --request-id

The request identifier to use for the asynchronous operation. If not set, the server assigns an identifier.

Alias: `-r`

#### --namespace

**Required.** Specify a Namespace hosted on Temporal Cloud. If not specified, the value of the environment variable `$TEMPORAL_CLOUD_NAMESPACE` is used.

Alias: `-n`

#### --region

**Required.** The region to add to the existing Namespace. See [Regions](/cloud/regions) for a list of supported regions.

:::tip Choosing Replica Regions

See [Regions](/cloud/regions) for available regions and their supported replication options. See [High Availability](/cloud/high-availability) to learn how replication and failover work.

:::

Alias: `--re`

**Example**

```bash
tcld namespace add-region \
    --namespace <namespace_id> \
    --region <replica_region_name>
```

Specify the region name (for example, `us-east-1`) of the region where you want to create the replica as an argument to the `--region` flag.
See [High Availability](/cloud/high-availability) for details on same-region, multi-region, and multi-cloud replication options.

Temporal Cloud sends an email alert once your Namespace is ready for use.

#### --cloud-provider

The cloud provider of the region. One of [`aws`, `gcp`].

Default: `aws`

## create

The `tcld namespace create` command creates a Temporal [Namespace](/namespaces) in Temporal Cloud.

Alias: `c`

The following modifiers control the behavior of the command.

#### --namespace

**Required.** The name for the new Namespace. This becomes part of the Namespace ID (`<namespace_name>.<account_suffix>`).

Alias: `-n`

#### --region

**Required.** The cloud provider region to create the Namespace in. Supply one `--region` for a standard Namespace, or two for a Namespace with [High Availability](/cloud/high-availability).

See [Regions](/cloud/regions) for available regions and their supported replication options.

Alias: `--re`

#### --auth-method

The authentication method for the Namespace. One of [`mtls`, `api_key`].

- `mtls` (default): Requires `--ca-certificate` or `--ca-certificate-file`
- `api_key`: No other modifiers

**Example**

```bash
tcld namespace create \
    --namespace test-namespace.a1b2c \
    --region us-east-1 \
    --auth-method api_key
```

#### --ca-certificate

A base64-encoded [CA certificate](/cloud/certificates). If both `--ca-certificate` and `--ca-certificate-file` are specified, only `--ca-certificate` is used.

Alias: `-c`

#### --ca-certificate-file

A path to a [CA certificate](/cloud/certificates) PEM file. If both options are specified, only `--ca-certificate` is used.

Alias: `--cf`

#### --certificate-filter-file

Path to a JSON file that defines the [certificate filters](/cloud/certificates#manage-certificate-filters) to be applied to the Namespace.

Sample JSON: `{ "filters": [ { "commonName": "test1" } ] }`

If both `--certificate-filter-file` and `--certificate-filter-input` are specified, the command returns an error.

Alias: `--cff`

#### --certificate-filter-input

A JSON string that defines the [certificate filters](/cloud/certificates#manage-certificate-filters) to be applied to the Namespace.

Sample JSON: `{ "filters": [ { "commonName": "test1" } ] }`

If both `--certificate-filter-input` and `--certificate-filter-file` are specified, the command returns an error.

Alias: `--cfi`

#### --cloud-provider

The cloud provider of the region. One of [`aws`, `gcp`].

Default: `aws`

Alias: `--cp`

#### --connectivity-rule-ids

A list of [connectivity rule](/cloud/connectivity#connectivity-rules) IDs to apply to the Namespace. Can be specified more than once.

Alias: `--ids`

**Example**

```bash
tcld namespace create \
    --namespace test-namespace.a1b2c \
    --region us-east-1 \
    --auth-method api_key \
    --connectivity-rule-ids <rule_id1> \
    --connectivity-rule-ids <rule_id2>
```

#### --enable-delete-protection

Enable [delete protection](/cloud/namespaces#delete-protection) on the Namespace.

Default: `false`

Alias: `--edp`

#### --endpoint

The [codec server](/production-deployment/data-encryption) endpoint to decode payloads for all users interacting with this Namespace. Must be HTTPS.

Alias: `-e`

#### --include-credentials

Include cross-origin credentials when calling the [codec server](/production-deployment/data-encryption).

Default: `false`

Alias: `--ic`

#### --pass-access-token

Pass the user access token to the [codec server](/production-deployment/data-encryption) endpoint.

Default: `false`

Alias: `--pat`

#### --request-id

The request identifier to use for the asynchronous operation. If not set, the server assigns an identifier.

Alias: `-r`

#### --retention-days

The [retention period](/temporal-service/temporal-server#retention-period) in days for closed Workflow Executions.

Default: `30`

Alias: `--rd`

#### --search-attribute

A custom [Search Attribute](/search-attribute) in the form '_name_=_type_'. Can be specified more than once.

Valid values for _type_: `Bool` | `Datetime` | `Double` | `Int` | `Keyword` | `Text`

Alias: `--sa`

**Example**

```bash
tcld namespace create \
    --namespace test-namespace.a1b2c \
    --region us-east-1 \
    --auth-method api_key \
    --search-attribute "customer_id=Int" \
    --search-attribute "customer_name=Text"
```

#### --tag

A [tag](/cloud/namespaces#tag-a-namespace) in the form "_key_=_value_". Can be specified more than once.

See [Tag structure and limits](/cloud/namespaces#tag-structure-and-limits).

Alias: `--t`

**Example**

```bash
tcld namespace create \
    --namespace test-namespace.a1b2c \
    --region us-east-1 \
    --auth-method api_key \
    --tag "key=value" \
    --tag "key2=value2"
```

#### --user-namespace-permission

A [Namespace-level permission](/cloud/manage-access/roles-and-permissions#namespace-level-permissions) for a user in the form '_email_=_permission_'. Can be specified more than once.

Valid values for _permission_: `Admin` | `Write` | `Read`

Alias: `-p`

**Example**

```bash
tcld namespace create \
    --namespace test-namespace.a1b2c \
    --region us-east-1 \
    --auth-method api_key \
    --user-namespace-permission "user@example.com=Admin" \
    --user-namespace-permission "user2@example.com=Write"
```

## delete

The `tcld namespace delete` command deletes the specified [Namespace](/namespaces) in Temporal Cloud.

Alias: `d`

