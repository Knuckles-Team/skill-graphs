`tcld namespace delete`

The following modifiers control the behavior of the command.

#### --namespace

**Required.** Specify the Namespace hosted on Temporal Cloud to be deleted.

Alias: `-n`

#### --request-id

The request identifier to use for the asynchronous operation. If not set, the server assigns an identifier.

Alias: `-r`

#### --resource-version

A resource version (ETag) to update from. If not set, the CLI uses the latest.

Alias: `-v`

**Example**

```bash
tcld namespace delete \
    --namespace <namespace_id>
```

## delete-region

Use `tcld namespace delete-region` to remove a <ToolTipTerm term="replica" /> for an existing Temporal Cloud
[Namespace](/namespaces). Removing a replica disables [High Availability features](/cloud/high-availability) and results
in a mandatory 7-day waiting period before you can re-enable High Availability features in the same location. Refer to
[Enable High Availability](/cloud/high-availability/enable) for more information.

The following modifiers control the behavior of the command.

#### --request-id

The request identifier to use for the asynchronous operation. If not set, the server assigns an identifier.

Alias: `-r`

#### --namespace

**Required.** Specify a Namespace hosted on Temporal Cloud. If not specified, the value of the environment variable `$TEMPORAL_CLOUD_NAMESPACE` is used.

Alias: `-n`

#### --region

**Required.** The region to remove from the Namespace. Specify the region name, for example `us-east-1`. Upon removal, Temporal stops replication and the Namespace becomes a Standard Namespace. You cannot re-add a region or add a new region for seven days after removing a Namespace region.

Alias: `--re`

**Example**

```bash
tcld namespace delete-region \
    --namespace <namespace_id> \
    --region <region_name>
```

When using API key authentication, add your API credentials before pressing Enter:

```bash
tcld --api-key <your_api_key> \
    delete-region \
    --namespace <namespace_id> \
    --region <region_name>
```

#### --cloud-provider

The cloud provider of the region to failover to. One of [aws, gcp].

Default: aws (default: "aws")

## failover

Failover a Temporal Namespace with [High Availability features](/cloud/high-availability). A failover switches a
Namespace region from a primary Namespace to its replica.

**Example**

```bash
tcld namespace failover \
    --namespace <namespace_id> \
    --region <target_region>
```

When using API key authentication, add your API credentials before pressing Enter:

```bash
tcld --api-key <your_api_key> \
    namespace failover \
    --namespace <namespace_id> \
    --region <target_region>
```

#### --request-id

Specify a request identifier to use for the asynchronous operation. If not specified, the server assigns a request
identifier.

Alias: `-r`

#### --namespace

**Required.** Specify a Namespace hosted on Temporal Cloud. If not specified, the value of the environment variable `$TEMPORAL_CLOUD_NAMESPACE` is used.

Alias: `-n`

#### --region

**Required.** The region to fail over _to_. Specify the region name, for example `us-east-1`.

See [Regions](/cloud/regions) for a list of supported regions.

Alias: `--re`

**Example**

```bash
tcld namespace failover \
    --namespace <namespace_id> \
    --region <region_name>
```

#### --ca-certificate

_Required modifier unless `--ca-certificate-file` is specified_.

A base64-encoded CA certificate.

If both `--ca-certificate` and `--ca-certificate-file` are specified, only `--ca-certificate` is used.

Alias: `-c`

#### --cloud-provider

The cloud provider of the region to failover to. One of [aws, gcp].

Default: aws (default: "aws")

## get

The `tcld namespace get` command gets information about the specified [Namespace](/namespaces) in Temporal Cloud.

Alias: `g`

`tcld namespace get`

The following modifier controls the behavior of the command.

#### --namespace

Specify a Namespace hosted on Temporal Cloud. If not specified, the value of the environment variable
$TEMPORAL_CLOUD_NAMESPACE is used.

Alias: `-n`

**Example**

```bash
tcld namespace get \
    --namespace <namespace_id>
```

## list

The `tcld namespace list` command lists all [Namespaces](/namespaces) in Temporal Cloud.

Alias: `l`

`tcld namespace list`

The command has no modifiers.

## export

The `tcld namespace export s3` commands manage Workflow History Exports.

Valid options: `s3`

Alias: `es`

- [tcld namespace export s3 create](#create)
- [tcld namespace export s3 get](#get)
- [tcld namespace export s3 delete](#delete)
- [tcld namespace export s3 list](#list)
- [tcld namespace export s3 update](#update)
- [tcld namespace export s3 validate](#validate)

### create

The `tcld namespace export s3 create` command allows users to create an export sink for the Namespace of a Temporal
Cloud account.

**Example**

```bash
tcld namespace export s3 create \
    --namespace <namespace_id> \
    --sink-name <sink_name> \
    --s3-bucket-name <bucket_name> \
    --role-arn <role_arn>
```

The following modifiers control the behavior of the command.

#### --namespace

Specify a Namespace hosted on Temporal Cloud. If not specified, the value of the environment variable
$TEMPORAL_CLOUD_NAMESPACE is used.

Alias: `-n`

#### --sink-name

Provide a name for the export sink.

_Required modifier_

#### --role-arn

Provide role arn for the IAM Role.

_Required modifier_

#### --s3-bucket-name

Provide the name of an AWS S3 bucket that Temporal will send closed workflow histories to.

_Required modifier_

#### --request-id

Specify a request identifier to use for the asynchronous operation. If not specified, the server assigns a request
identifier.

Alias: `-r`

#### --kms-arn

Provide the ARN of the KMS key to use for encryption. Note: If the KMS ARN needs to be added or updated, users should
create the IAM Role with KMS or modify the created IAM Role accordingly. Providing it as part of the input won't help.

### get

The `tcld namespace export s3 get` command allows users to retrieve details about an existing export sink from the
Namespace of a Temporal Cloud account.

**Example**

```bash
tcld namespace export s3 get \
    --namespace <namespace_id> \
    --sink-name <sink_name>
```

The following modifiers control the behavior of the command.

#### --namespace

Specify a Namespace hosted on Temporal Cloud. If not specified, the value of the environment variable
$TEMPORAL_CLOUD_NAMESPACE is used.

Alias: `-n`

#### --sink-name

Provide the name of the export sink you wish to retrieve details for.

_Required modifier_

### delete

The `tcld namespace export s3 delete` command allows users to delete an existing export sink from the Namespace of a
Temporal Cloud account.

**Example**

```bash
tcld namespace export s3 delete \
    --namespace <namespace_id> \
    --sink-name <sink_name>
```

The following modifiers control the behavior of the command.

#### --namespace

Specify a Namespace hosted on Temporal Cloud. If not specified, the value of the environment variable
$TEMPORAL_CLOUD_NAMESPACE is used.

Alias: `-n`

#### --sink-name

Provide the name of the export sink you wish to delete.

_Required modifier_

#### --resource-version

Specify a resource version (ETag) to delete from. If not specified, the CLI will use the latest version.

Alias: `-v`

#### --request-id

Specify a request identifier to use for the asynchronous operation. If not specified, the server assigns a request
identifier.

Alias: `-r`

### list

The `tcld namespace export s3 list` command allows users to list all existing export sinks within the Namespace of a
Temporal Cloud account.

**Example**

```bash
tcld namespace export s3 list \
    --namespace <namespace_id>
```

The following modifiers control the behavior of the command.

#### --namespace

Specify a Namespace hosted on Temporal Cloud. If not specified, the value of the environment variable
$TEMPORAL_CLOUD_NAMESPACE is used.

Alias: `-n`

#### --page-size

Determine the number of results to return per page for list operations. If not specified, the default value is 100.

#### --page-token

Provide the page token to continue listing results from where the previous list operation left off.

### update

The `tcld namespace export s3 update` command allows users to modify the details of an existing export sink within the
Namespace of a Temporal Cloud account.

**Example**

```bash
tcld namespace export s3 update \
    --namespace <namespace_id> \
    --sink-name <sink_name> \
    --enabled true
```

The following modifiers control the behavior of the command.

#### --namespace

Specify a Namespace hosted on Temporal Cloud. If not specified, the value of the environment variable
$TEMPORAL_CLOUD_NAMESPACE is used.

Alias: `-n`

#### --sink-name

Provide the name of the export sink you wish to update.

_Required modifier_

#### --enabled

Specify whether the export is enabled or not.

#### --role-arn

Update the role ARN for the IAM Role.

#### --s3-bucket-name

Update the name of the AWS S3 bucket that Temporal will send closed workflow histories to.

#### --resource-version

Specify a resource version (ETag) to update from. If not specified, the CLI will use the latest version.

Alias: `-v`

#### --kms-arn

Update the ARN of the KMS key used for encryption. Note: If the KMS ARN needs to be added or updated, users should
create the IAM Role with KMS or modify the created IAM Role accordingly. Providing it as part of the input won't help.

#### --request-id

Specify a request identifier to use for the asynchronous operation. If not specified, the server assigns a request
identifier.

Alias: `-r`

### validate

The `tcld namespace export s3 validate` command allows users to validate an export sink from the Namespace of a Temporal
Cloud account.

**Example**

```bash
tcld namespace export s3 validate \
    --namespace <namespace_id> \
    --sink-name <sink_name> \
    --s3-bucket-name <bucket_name> \
    --role-arn <role_arn>
```

The following modifiers control the behavior of the command.

#### --namespace

Specify a Namespace hosted on Temporal Cloud. If not specified, the value of the environment variable
$TEMPORAL_CLOUD_NAMESPACE is used.

Alias: `-n`

#### --sink-name

Provide the name of the export sink you wish to retrieve details for.

_Required modifier_

#### --role-arn

Provide role arn for the IAM Role.

_Required modifier_

#### --s3-bucket-name

Update the name of the AWS S3 bucket that Temporal will send closed workflow histories to.

#### --kms-arn

Update the ARN of the KMS key used for encryption. Note: If the KMS ARN needs to be added or updated, users should
create the IAM Role with KMS or modify the created IAM Role accordingly. Providing it as part of the input won't help.

## accepted-client-ca

The `tcld namespace accepted-client-ca` commands manage the client CA certificates of the specified
[Namespace](/namespaces) in Temporal Cloud. The certificates are used to verify client connections.

:::note

Base64 versions of the CA certificate files are accepted by these commands.

:::

Alias: `ca`

- [tcld namespace accepted-client-ca add](#add)
- [tcld namespace accepted-client-ca list](#list)
- [tcld namespace accepted-client-ca set](#set)
- [tcld namespace accepted-client-ca remove](#remove)

:::important

Do not use a CA certificate that is signed with an insecure signature algorithm, such as SHA-1. Such signatures will be
rejected. Existing CA certificates that use SHA-1 can stop working without warning.

For more information about the vulnerabilities of SHA-1, see [SHAttered](https://shattered.io/).

:::

### add

The `tcld namespace accepted-client-ca add` command adds client CA certificates to a [Namespace](/namespaces) in
Temporal Cloud.

`tcld namespace accepted-client-ca add --ca-certificate <value>`

Alias: `a`

The following modifiers control the behavior of the command.

#### --namespace

Specify a Namespace hosted on Temporal Cloud. If not specified, the value of the environment variable
$TEMPORAL_CLOUD_NAMESPACE is used.

Alias: `-n`

**Example**

```bash
tcld namespace accepted-client-ca add \
    --namespace <namespace_id> \
    --ca-certificate <encoded_certificate>
```

#### --request-id

Specify a request identifier to use for the asynchronous operation. If not specified, the server assigns a request
identifier.

Alias: `-r`

**Example**

```bash
tcld namespace accepted-client-ca add \
    --request-id <request_id> \
    --ca-certificate <encoded_certificate>
```

#### --resource-version

Specify a resource version (ETag) to update from. If not specified, the latest version is used.

Alias: `-v`

**Example**

```bash
tcld namespace accepted-client-ca add \
    --resource-version <etag> \
    --ca-certificate <encoded_certificate>
```

#### --ca-certificate

_Required modifier unless `--ca-certificate-file` is specified_

Specify a base64-encoded string of a CA certificate PEM file.

If both `--ca-certificate` and `--ca-certificate-file` are specified, only `--ca-certificate` is used.

Alias: `-c`

**Example**

```bash
tcld namespace accepted-client-ca add \
    --ca-certificate <encoded_certificate>
```

#### --ca-certificate-file

_Required modifier unless `--ca-certificate` is specified_

Specify a path to a CA certificate PEM file.

If both `--ca-certificate` and `--ca-certificate-file` are specified, only `--ca-certificate` is used.

Alias: `-f`

**Example**

```bash
tcld namespace accepted-client-ca add \
    --ca-certificate-file <path>
```

### list

The `tcld namespace accepted-client-ca list` command lists the client CA certificates that are currently configured for
a [Namespace](/namespaces) in Temporal Cloud.

`tcld namespace accepted-client-ca list`

Alias: `l`

The following modifier controls the behavior of the command.

#### --namespace

Specify a Namespace hosted on Temporal Cloud. If not specified, the value of the environment variable
$TEMPORAL_CLOUD_NAMESPACE is used.

Alias: `-n`

**Example**

```bash
tcld namespace accepted-client-ca list \
    --namespace <namespace_id>
```

### remove

The `tcld namespace accepted-client-ca remove` command removes client CA certificates from a [Namespace](/namespaces) in
Temporal Cloud.

`tcld namespace accepted-client-ca remove --ca-certificate <value>`

Alias: `r`

The following modifiers control the behavior of the command.

#### --namespace

Specify a Namespace hosted on Temporal Cloud. If not specified, the value of the environment variable
$TEMPORAL_CLOUD_NAMESPACE is used.

Alias: `-n`

**Example**

```bash
tcld namespace accepted-client-ca remove \
    --namespace <namespace_id> \
    --ca-certificate <encoded_certificate>
```

#### --request-id

Specify a request identifier to use for the asynchronous operation. If not specified, the server assigns a request
identifier.

Alias: `-r`

**Example**

```bash
tcld namespace accepted-client-ca remove \
    --request-id <request_id> \
    --ca-certificate <encoded_certificate>
```

#### --resource-version

Specify a resource version (ETag) to update from. If not specified, the latest version is used.

Alias: `-v`

**Example**

```bash
tcld namespace accepted-client-ca remove \
    --resource-version <etag> \
    --ca-certificate <encoded_certificate>
```

#### --ca-certificate

_Required modifier unless `--ca-certificate-fingerprint` or `--ca-certificate-file` is specified_

Specify the base64-encoded string of a CA certificate PEM file.

If `--ca-certificate-fingerprint` is also specified, both `--ca-certificate` and `--ca-certificate-file` are ignored.

If `--ca-certificate-file` is also specified but `--ca-certificate-fingerprint` is not, only `--ca-certificate` is used.

Alias: `-c`

**Example**

```bash
tcld namespace accepted-client-ca remove \
    --ca-certificate <encoded_certificate>
```

#### --ca-certificate-file

_Required modifier unless `--ca-certificate-fingerprint` or `--ca-certificate` is specified_

Specify a path to a CA certificate PEM file.

If `--ca-certificate-fingerprint` is also specified, both `--ca-certificate-file` and `--ca-certificate` are ignored.

If `--ca-certificate` is also specified but `--ca-certificate-fingerprint` is not, only `--ca-certificate` is used.

Alias: `-f`

**Example**

```bash
tcld namespace accepted-client-ca remove \
    --ca-certificate-file <path>
```

#### --ca-certificate-fingerprint

_Required modifier unless `--ca-certificate` or `--ca-certificate-file` is specified_

Specify the fingerprint of a CA certificate.

If `--ca-certificate`, `--ca-certificate-file`, or both are also specified, they are ignored.

Alias: `--fp`

**Example**

```bash
tcld namespace accepted-client-ca remove \
    --ca-certificate-fingerprint <fingerprint>
```

### set

The `tcld namespace accepted-client-ca set` command sets the client CA certificates for a [Namespace](/namespaces) in
Temporal Cloud.

`tcld namespace accepted-client-ca set --ca-certificate <value>`

Alias: `s`

{/* How to rollover accepted client CA certificates in Temporal Cloud using tcld */}

When updating CA certificates, it's important to follow a rollover process. Doing so enables your Namespace to serve
both CA certificates for a period of time until traffic to your old CA certificate ceases.

1. Create a single file that contains both your old and new CA certificate PEM blocks. Just concatenate the PEM blocks
   on adjacent lines.

   ```
   -----BEGIN CERTIFICATE-----
   ... old CA cert ...
   -----END CERTIFICATE-----
   -----BEGIN CERTIFICATE-----
   ... new CA cert ...
   -----END CERTIFICATE-----
   ```

1. Run the `tcld namespace accepted-client-ca set` command with the CA certificate bundle file.

   ```bash
   tcld namespace accepted-client-ca set \
       --ca-certificate-file <path>
   ```

1. Monitor traffic to your old certificate until it ceases.

1. Create another file that contains only the new CA certificate.

1. Run the `tcld namespace accepted-client-ca set` command again with the updated CA certificate bundle file.

The following modifiers control the behavior of the command.

#### --namespace

Specify a Namespace hosted on Temporal Cloud. If not specified, the value of the environment variable
$TEMPORAL_CLOUD_NAMESPACE is used.

Alias: `-n`

**Example**

```bash
tcld namespace accepted-client-ca set \
    --namespace <namespace_id>
    --ca-certificate <encoded_certificate>
```

#### --request-id

Specify a request identifier to use for the asynchronous operation. If not specified, the server assigns a request
identifier.

Alias: `-r`

**Example**

```bash
tcld namespace accepted-client-ca set \
    --request-id <request_id> \
    --ca-certificate <encoded_certificate>
```

#### --resource-version

Specify a resource version (ETag) to update from. If not specified, the latest version is used.

Alias: `-v`

**Example**

```bash
tcld namespace accepted-client-ca set \
    --resource-version <etag> \
    --ca-certificate <encoded_certificate>
```

#### --ca-certificate

_Required modifier unless `--ca-certificate-file` is specified_

Specify a base64-encoded string of a CA certificate PEM file.

If both `--ca-certificate` and `--ca-certificate-file` are specified, only `--ca-certificate` is used.

Alias: `-c`

**Example**

```bash
tcld namespace accepted-client-ca set \
    --ca-certificate <encoded_certificate>
```

#### --ca-certificate-file

_Required modifier unless `--ca-certificate` is specified_

Specify a path to a CA certificate PEM file.

If both `--ca-certificate` and `--ca-certificate-file` are specified, only `--ca-certificate` is used.

Alias: `-f`

**Example**

```bash
tcld namespace accepted-client-ca set \
    --ca-certificate-file <path>
```

## certificate-filters

The `tcld namespace certificate-filters` commands manage optional certificate filters for the specified
[Namespace](/namespaces) in Temporal Cloud. The Namespace can use certificate filters to authorize client certificates
based on distinguished name (DN) fields.

Alias: `cf`

- [tcld namespace certificate-filters import](#import)
- [tcld namespace certificate-filters export](#export)
- [tcld namespace certificate-filters clear](#clear)

### add

The `tcld namespace certificates-filter add` command adds additional certificate filters to the Namespace of a Temporal
Cloud account.

The following modifiers control the behavior of the command.

#### --namespace

Specify a Namespace hosted on Temporal Cloud. If not specified, the value of the environment variable
$TEMPORAL_CLOUD_NAMESPACE is used.

Alias: `-n`

**Example**

```bash
tcld namespace certificate-filters add \
    --namespace <namespace_id> \
    --certificate-filter-file <file>
```

#### --request-id

Specify a request identifier to use for the asynchronous operation. If not specified, the server assigns a request
identifier.

Alias: `-r`

**Example**

```bash
tcld namespace certificate-filters add \
    --request-id <request_id> \
    --certificate-filter-file <file>
```

#### --resource-version

Specify a resource version (ETag) to update from. If not specified, the latest version is used.

Alias: `-v`

**Example**

```bash
tcld namespace certificate-filters add \
    --resource-version <etag> \
    --certificate-filter-file <file>
```

#### --certificate-filter-file

_Required modifier unless `--certificate-filter-value` is specified._

Specify a path to a JSON file defining the certificate filters for the Namespace.

Aliases: `-f`, `--file`

**Example**

```bash
tcld namespace certificate-filters add \
    --certificate-filter-file <file>
```

#### --certificate-filter-input

_Required modifier unless `--certificate-filter-file` is specified._

The certificate filters, in JSON, that will be added to the Namespace.

Aliases: `-i`, `--input`

**Example**

```bash
tcld namespace certificate-filters add \
    --certificate-filter-input <JSON>
```

### clear

The `tcld namespace certificate-filters clear` command clears all certificate filters from a [Namespace](/namespaces) in
Temporal Cloud.

:::caution

Using this command allows _any_ client certificate that chains up to a configured CA certificate to connect to the
Namespace.

:::

`tcld namespace certificate-filters clear`

The following modifiers control the behavior of the command.

#### --namespace

Specify a Namespace hosted on Temporal Cloud. If not specified, the value of the environment variable
$TEMPORAL_CLOUD_NAMESPACE is used.

Alias: `-n`

**Example**

```bash
tcld namespace certificate-filters clear \
    --namespace <namespace_id>
```

#### --request-id

Specify a request identifier to use for the asynchronous operation. If not specified, the server assigns a request
identifier.

Alias: `-r`

**Example**

```bash
tcld namespace certificate-filters clear
    --request-id <request_id>
```

#### --resource-version

Specify a resource version (ETag) to update from. If not specified, the latest version is used.

Alias: `-v`

**Example**

```bash
tcld namespace certificate-filters clear \
    --resource-version <etag>
```

### export

The `tcld namespace certificate-filters export` command exports existing certificate filters from a
[Namespace](/namespaces) in Temporal Cloud.

`tcld namespace certificate-filters export --certificate-filter-file <path>`

Alias: `exp`

The following modifiers control the behavior of the command.

#### --certificate-filter-file

Specify a path to a JSON file where tcld can export the certificate filters.

Aliases: `--file`, `-f`

**Example**

```bash
tcld namespace certificate-filters export \
    --certificate-filter-file <path>
```

#### --namespace

Specify a Namespace hosted on Temporal Cloud. If not specified, the value of the environment variable
$TEMPORAL_CLOUD_NAMESPACE is used.

Alias: `-n`

**Example**

```bash
tcld namespace certificate-filters import \
    --namespace <namespace_id> \
    --certificate-filter-input <json>
```

#### --request-id

Specify a request identifier to use for the asynchronous operation. If not specified, the server assigns a request
identifier.

Alias: `-r`

**Example**

```bash
tcld namespace certificate-filters import \
    --request-id <request_id> \
    --certificate-filter-input <json>
```

#### --resource-version

Specify a resource version (ETag) to update from. If not specified, the latest version is used.

Alias: `-v`

**Example**

```bash
tcld namespace certificate-filters import \
    --resource-version <etag> \
    --certificate-filter-input <json>
```

### import

The `tcld namespace certificate-filters import` command sets certificate filters for a [Namespace](/namespaces) in
Temporal Cloud.

`tcld namespace certificate-filters import --certificate-filter-file <path>`

Alias: `imp`

A certificate filter can include any combination (and at least one) of the following:

- `commonName`
- `organization`
- `organizationalUnit`
- `subjectAlternativeName`

The following modifiers control the behavior of the command.

#### --certificate-filter-file

_Required modifier unless `--certificate-filter-input` is specified_

Specify a path to a JSON file that defines certificate filters to be applied to the Namespace, such as
`{ "filters": [ { "commonName": "test1" } ] }`. The specified filters replace any existing filters.

If both `--certificate-filter-file` and `--certificate-filter-input` are specified, the command returns an error.

Aliases: `--file`, `-f`

**Example**

```bash
tcld namespace certificate-filters import \
    --certificate-filter-file <path>
```

#### --certificate-filter-input

_Required modifier unless `--certificate-filter-file` is specified_

Specify a JSON string that defines certificate filters to be applied to the Namespace, such as
