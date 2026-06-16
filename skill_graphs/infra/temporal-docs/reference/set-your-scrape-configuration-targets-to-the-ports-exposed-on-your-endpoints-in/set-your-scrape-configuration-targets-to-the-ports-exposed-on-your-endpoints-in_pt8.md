`{ "filters": [ { "commonName": "test1" } ] }`. The specified filters replace any existing filters.

If both `--certificate-filter-input` and `--certificate-filter-file` are specified, the command returns an error.

Aliases: `--input`, `-i`

**Example**

```bash
tcld namespace certificate-filters import \
    --certificate-filter-input <json>
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

## search-attributes

The `tcld namespace search-attributes` commands manage [Search Attributes](/search-attribute) of the specified
[Namespace](/namespaces) in Temporal Cloud.

Alias: `sa`

- [tcld namespace search-attributes add](#add)
- [tcld namespace search-attributes rename](#rename)

If you wish to delete a Search Attribute, please contact [Support](/cloud/support) at
[support.temporal.io](https://support.temporal.io).

### add

The `tcld namespace search-attributes add` command adds custom [Search Attributes](/search-attribute) to a Namespace in
Temporal Cloud.

`tcld namespace search-attributes add --search-attribute <value>`

Alias: `a`

The following modifiers control the behavior of the command.

#### --namespace

Specify a Namespace hosted on Temporal Cloud. If not specified, the value of the environment variable
$TEMPORAL_CLOUD_NAMESPACE is used.

Alias: `-n`

**Example**

```bash
tcld namespace search-attributes add \
    --namespace <namespace_id> \
    --search-attribute <value>
```

#### --request-id

Specify a request identifier to use for the asynchronous operation. If not specified, the server assigns a request
identifier.

Alias: `-r`

**Example**

```bash
tcld namespace search-attributes add \
    --request-id <request_id> \
    --search-attribute <value>
```

#### --resource-version

Specify a resource version (ETag) to update from. If not specified, the latest version is used.

Alias: `-v`

**Example**

```bash
tcld namespace search-attributes add \
    --resource-version <etag> \
    --search-attribute <value>
```

#### --search-attribute

_Required modifier; can be specified more than once_

Specify a custom Search Attribute in the form "_name_=_type_". Valid values for _type_ are as follows:

- Bool
- Datetime
- Double
- Int
- Keyword
- Text

Alias: `--sa`

**Example**

```bash
tcld namespace search-attributes add \
    --search-attribute "YourSearchAttribute1=Text" \
    --search-attribute "YourSearchAttribute2=Double"
```

### rename

The `tcld namespace search-attributes rename` command renames a custom [Search Attribute](/search-attribute) in Temporal
Cloud.

`tcld namespace search-attributes rename --existing-name <value> --new-name <value>`

The following modifiers control the behavior of the command.

#### --namespace

Specify a Namespace hosted on Temporal Cloud. If not specified, the value of the environment variable
$TEMPORAL_CLOUD_NAMESPACE is used.

Alias: `-n`

**Example**

```bash
tcld namespace search-attributes rename \
    --namespace <namespace_id> \
    --existing-name <value> \
    --new-name <value>
```

#### --request-id

Specify a request identifier to use for the asynchronous operation. If not specified, the server assigns a request
identifier.

Alias: `-r`

**Example**

```bash
tcld namespace search-attributes rename \
    --request-id <request_id> \
    --existing-name <value> \
    --new-name <value>
```

#### --resource-version

Specify a resource version (ETag) to update from. If not specified, the latest version is used.

Alias: `-v`

**Example**

```bash
tcld namespace search-attributes rename \
    --resource-version <etag> \
    --existing-name <value> \
    --new-name <value>
```

#### --existing-name

_Required modifier_

Specify the name of an existing Search Attribute.

Alias: `--en`

**Example**

```bash
tcld namespace search-attributes rename \
    --existing-name <value> \
    --new-name <value>
```

#### --new-name

_Required modifier_

Specify a new name for the Search Attribute.

Alias: `--nn`

**Example**

```bash
tcld namespace search-attributes rename \
    --existing-name <value> \
    --new-name <value>
```

## retention

The `tcld namespace retention` commands manage the length of time (in days) a closed Workflow is preserved before
deletion for a given Namespace in Temporal Cloud.

Alias: `r`

- [tcld namespace retention get](#get)
- [tcld namespace retention set](#set)

### get

Retrieve the length of time (in days) a closed Workflow will be preserved before deletion for the specified Namespace.

Alias: `g`

The following modifier controls the behavior of the command.

#### --namespace

_Required modifier_

Specify a Namespace hosted on Temporal Cloud. If not specified, the value of the environment variable
$TEMPORAL_CLOUD_NAMESPACE is used.

Alias: `-n`

**Example**

```bash
tcld namespace retention get \
    --namespace <namespace_id>
```

### set

Set the length of time (in days) a closed Workflow will be preserved before deletion for the specified Namespace.

Alias: `s`

The following modifiers control the behavior of the command.

#### --namespace

_Required modifier_

Specify a Namespace hosted on Temporal Cloud. If not specified, the value of the environment variable
$TEMPORAL_CLOUD_NAMESPACE is used.

Alias: `-n`

#### --retention-days

_Required modifier_

Specify the number of days a closed Workflow will be preserved before deletion.

Alias: `--rd`

**Example**

```bash
tcld namespace retention set \
    --namespace <namespace_id> \
    --retention-days <retention_days>
```

## update-codec-server

The `tcld namespace update-codec-server` command updates the configuration of a codec server for Temporal Cloud, which
allows payloads to be decoded through a remote endpoint.

Alias: `ucs`

The following modifiers control the behavior of the command.

#### --namespace

_Required modifier._

Specify a Namespace hosted on Temporal Cloud. If not specified, the value of the environment variable
$TEMPORAL_CLOUD_NAMESPACE is used.

Alias: `-n`

**Example**

```bash
tcld namespace update-codec-server \
    --namespace <namespace_id> \
    --endpoint <http_url>
```

#### --endpoint

_Required modifier._

Specify an endpoint to decode payloads for all users interacting with this Namespace. Endpoints must be valid https
URLs.

Alias: `-e`

**Example**

```bash
tcld namespace update-codec-server \
    --namespace <namespace_id> \
    --endpoint <https_url>
```

#### --pass-access-token

Enables a user access token to be passed with the remote endpoint. This is set to `false` by default.

Alias: `--pat`

**Example**

```bash
tcld namespace update-codec-server \
    --namespace <namespace_id> \
    --endpoint <https_url> \
    --pass-access-token <bool>
```

#### --include-credentials

Enables the inclusion of cross-origin credentials. This is set to `false` by default.

Alias: `--ic`

**Example**

```bash
tcld namespace update-codec-server \
    --namespace <namespace_id> \
    --endpoint <https_url> \
    --include-credentials true
```

## update-high-availability {/* #update-high-availability */}

The `tcld namespace update-high-availability` command enables you to adjust settings for your [Namespace](/namespaces)
with [High Availability features](/cloud/high-availability). This is set to `false` by default.

Alias: `uha`

The following modifiers control the behavior of the command.

#### --namespace

_Required modifier._

Specify a Namespace hosted on Temporal Cloud. If not specified, the value of the environment variable
$TEMPORAL_CLOUD_NAMESPACE is used.

Alias: `-n`

#### --disable-auto-failover

Specify whether Temporal Cloud should perform <ToolTipTerm term="health checks" src="health check" /> and trigger
automatic failovers.

Pass `true` or `false` (default).

**Example**

```
tcld namespace update-high-availability \
    --namespace <namespace_id> \
    --disable-auto-failover=true
```

When using API key authentication, add your API credentials before pressing Enter:

```
tcld --api-key <your_api_key> \
    namespace update-high-availability \
    --namespace <namespace_id> \
    --disable-auto-failover=true
```

Alias: `-daf`

## tags

The `tcld namespace tags` commands manage [Tags](/cloud/namespaces#tag-a-namespace) of the specified
[Namespace](/namespaces) in Temporal Cloud.

Alias: `t`

- [tcld namespace tags upsert](#upsert)
- [tcld namespace tags remove](#remove)

### upsert

Add new tags or update existing tag values for the specified Namespace.

Alias: `u`

The following modifier controls the behavior of the command.

#### --namespace

_Required modifier_

Specify a Namespace hosted on Temporal Cloud. If not specified, the value of the environment variable
$TEMPORAL_CLOUD_NAMESPACE is used.

Alias: `-n`

#### --request-id

The request identifier to use for the asynchronous operation. If not set, the server assigns an identifier.

Alias: `-r`

#### --tag

_Required modifier; can be specified more than once_

A tag in the form "_key_=_value_".

[Tag structure and limits](/cloud/namespaces#tag-structure-and-limits).

Alias: `--t`

**Example**

```bash
tcld namespace tags upsert \
    --namespace <namespace_id> \
    --tag "key1=value1" \
    --tag "key2=updated"
```

### remove

Remove existing tags for the specified Namespace using the key.

Alias: `rm`

The following modifiers control the behavior of the command.

#### --namespace

_Required modifier_

Specify a Namespace hosted on Temporal Cloud. If not specified, the value of the environment variable
$TEMPORAL_CLOUD_NAMESPACE is used.

Alias: `-n`

#### --request-id

The request identifier to use for the asynchronous operation. If not set, the server assigns an identifier.

Alias: `-r`

#### --tag-key

_Required modifier; can be specified more than once_

A tag key string.

[Tag Key structure and limits](/cloud/namespaces#tag-structure-and-limits).

Alias: `--tk`

**Example**

```bash
tcld namespace tags remove \
    --namespace <namespace_id> \
    --tag-key "key1" \
    --tag-key "key2"
```

## set-connectivity-rules

The `tcld namespace set-connectivity-rules` command enables you to set connectivity rules on your
[Namespace](/namespaces).

Alias: `scrs`

#### --connectivity-rule-ids

The list of connectivity rule IDs, can be used in create namespace and update namespace. example: --ids id1 --ids id2
--ids id3.

Alias: `ids`

#### --namespace

The namespace hosted on temporal cloud.

Alias: `n`

#### --remove-all

Acknowledge that all connectivity rules will be removed, enabling connectivity from any source.

---

## tcld nexus command reference

The `tcld nexus` commands manage Nexus resources in Temporal Cloud.

Alias: `nxs`

- [tcld nexus endpoint](#endpoint)

## endpoint

The `tcld nexus endpoint` commands manage Nexus Endpoints in Temporal Cloud.

Alias: `ep`

- [tcld nexus endpoint allowed-namespace](#allowed-namespace)
- [tcld nexus endpoint create](#create)
- [tcld nexus endpoint delete](#delete)
- [tcld nexus endpoint get](#get)
- [tcld nexus endpoint list](#list)
- [tcld nexus endpoint update](#update)

### allowed-namespace

The `tcld nexus endpoint allowed-namespace` commands manage the allowed namespaces for a Nexus Endpoint.

Alias: `an`

- [tcld nexus endpoint allowed-namespace add](#add)
- [tcld nexus endpoint allowed-namespace list](#list)
- [tcld nexus endpoint allowed-namespace remove](#remove)
- [tcld nexus endpoint allowed-namespace set](#set)

#### add

The `tcld nexus endpoint allowed-namespace add` command adds allowed namespaces to a Nexus Endpoint.

Alias: `a`

##### --name

Endpoint name.

Alias: `n`

##### --namespace

Namespace that is allowed to call this endpoint.

Alias: `ns`

##### --request-id

The request-id to use for the asynchronous operation, if not set the server will assign one (optional).

Alias: `r`

##### --resource-version

The resource-version (etag) to update from, if not set the cli will use the latest (optional).

Alias: `v`

#### list

The `tcld nexus endpoint allowed-namespace list` command lists the allowed namespaces of a Nexus Endpoint.

Alias: `l`

##### --name

Endpoint name.

Alias: `n`

#### remove

The `tcld nexus endpoint allowed-namespace remove` command removes allowed namespaces from a Nexus Endpoint.

Alias: `r`

##### --name

Endpoint name.

Alias: `n`

##### --namespace

Namespace that is allowed to call this endpoint.

Alias: `ns`

##### --request-id

The request-id to use for the asynchronous operation, if not set the server will assign one (optional).

Alias: `r`

##### --resource-version

The resource-version (etag) to update from, if not set the cli will use the latest (optional).

Alias: `v`

#### set

The `tcld nexus endpoint allowed-namespace set` command sets the allowed namespaces of a Nexus Endpoint.

Alias: `s`

##### --name

Endpoint name.

Alias: `n`

##### --namespace

Namespace that is allowed to call this endpoint.

Alias: `ns`

##### --request-id

The request-id to use for the asynchronous operation, if not set the server will assign one (optional).

Alias: `r`

##### --resource-version

The resource-version (etag) to update from, if not set the cli will use the latest (optional).

Alias: `v`

### create

The `tcld nexus endpoint create` command creates a new Nexus Endpoint on the Cloud Account.
An endpoint name is used by in workflow code to invoke Nexus operations.
The endpoint target is a worker and `--target-namespace` and `--target-task-queue` must both be provided.
This will fail if an endpoint with the same name is already registered.

Alias: `c`

#### --allow-namespace

Namespace that is allowed to call this endpoint (optional).

Alias: `ans`

#### --description

Endpoint description in markdown format (optional).

Alias: `d`

#### --description-file

Endpoint description file in markdown format (optional).

Alias: `df`

#### --name

Endpoint name.

Alias: `n`

#### --request-id

The request-id to use for the asynchronous operation, if not set the server will assign one (optional).

Alias: `r`

#### --target-namespace

Namespace in which a handler worker will be polling for Nexus tasks on.

Alias: `tns`

#### --target-task-queue

Task Queue in which a handler worker will be polling for Nexus tasks on.

Alias: `ttq`

### delete

The `tcld nexus endpoint delete` command deletes a Nexus Endpoint on the Cloud Account.
.

Alias: `d`

#### --name

Endpoint name.

Alias: `n`

#### --request-id

The request-id to use for the asynchronous operation, if not set the server will assign one (optional).

Alias: `r`

#### --resource-version

The resource-version (etag) to update from, if not set the cli will use the latest (optional).

Alias: `v`

### get

The `tcld nexus endpoint get` command gets a Nexus Endpoint configuration by name from the Cloud Account.

Alias: `g`

#### --name

Endpoint name.

Alias: `n`

### list

The `tcld nexus endpoint list` command lists all Nexus Endpoint configurations on the Cloud Account.

Alias: `l`

### update

The `tcld nexus endpoint update` command updates an existing Nexus Endpoint on the Cloud Account.
An endpoint name is used by in workflow code to invoke Nexus operations.
The endpoint target is a worker and `--target-namespace` and `--target-task-queue` must both be provided.

The endpoint is patched leaving any existing fields for which flags are not provided as they were.

Alias: `u`

#### --description

Endpoint description in markdown format (optional).

Alias: `d`

#### --description-file

Endpoint description file in markdown format (optional).

Alias: `df`

#### --name

Endpoint name.

Alias: `n`

#### --request-id

The request-id to use for the asynchronous operation, if not set the server will assign one (optional).

Alias: `r`

#### --resource-version

The resource-version (etag) to update from, if not set the cli will use the latest (optional).

Alias: `v`

#### --target-namespace

Namespace in which a handler worker will be polling for Nexus tasks on (optional).

Alias: `tns`

#### --target-task-queue

Task Queue in which a handler worker will be polling for Nexus tasks on (optional).

Alias: `ttq`

#### --unset-description

Unset endpoint description.

---

## tcld request command reference

The `tcld request` commands manage asynchronous requests in Temporal Cloud.

Alias: `r`

- [tcld request get](#get)

## get

The `tcld request get` command gets the status of the specified request in Temporal Cloud.

`tcld request get --request-id <request_id>`

Alias: `g`

The following modifiers control the behavior of the command.

#### --request

_Required modifier_

Specify a request identifier.

Alias: `-r`

**Example**

```bash
tcld request get --request-id <request_id>
```

---

## tcld user group command reference

The `tcld user-group` commands manage user groups in Temporal Cloud.

Alias: `ug`

- [tcld user-group add-users](#add-users)
- [tcld user-group create](#create)
- [tcld user-group delete](#delete)
- [tcld user-group get](#get)
- [tcld user-group list](#list)
- [tcld user-group list-members](#list-members)
- [tcld user-group remove-users](#remove-users)
- [tcld user-group set-access](#set-access)

## add-users

The `tcld user-group add-users` command adds users to the specified user group in Temporal Cloud.
You must set `--group-id` to specify the group to add users to.

Alias: `au`

The following flags control the behavior of the command.

#### --group-id (-id)

Specify the ID of the group to add users to.

#### --user-email (-e)

Specify the email of the user to add. This flag can be specified multiple times to add
multiple users in one command

## create

Creates a user group.

Alias: `c`

The following flags control the behavior of the command.

#### --display-name

The display name of the group.

#### --account-role

The account role that the group should have. One of `admin`, `read`, `developer`, `owner`, `financeadmin`, `none`.

#### --namespace-role (-nr)

Specifies a namespace role that the group should have. Can be repeated multiple times to add
multiple namespace roles to the group. Value is the form of `<namespaceid>-<role>` where the namespace ID is the full ID of the namespace and role is one of `admin`, `read`, or `write`. Example: `mynamespace.abc123-read` adds the read role for the `mynamespace.abc123` namespace.

## delete

Deletes the user group.

Alias: `d`

The following flags control the behavior of the command.

#### --group-id (-id)

Specify the ID of the group to delete.

## get

Gets the user group details.

Alias: `g`

The following flags control the behavior of the command.

#### --group-id (-id)

Specify the ID of the group to list.

## list

List the user groups in your Temporal Cloud account.

Alias: `l`

The following flags control the behavior of the command.

#### --page-size (-s)

The number of groups to list per page. Defaults to 10.

#### --page-token (-p)

The page token used when paginating through result pages.

## list-members

Lists all of the members of a group.

Alias: `lm`

The following flags control the behavior of the command.

#### --group-id (-id)

Specify the ID of the group to list.

## remove-users

Removes one or more users as members of the group.

Alias: `ru`

The following flags control the behavior of the command.

#### --group-id (-id)

Specify the ID of the group to remove users from.

#### --user-email (-e)

The email address of the user to remove from the group. This flag can be specified multiple times in order to remove multiple users with one command.

## set-access

This command sets the access roles that for a group. It follows the same conventions as the [create](#create) command by specifying an optional account role and 0 or more namespace roles.

Alias: `sa`

#### --group-id (-id)

Specify the ID of the group to set access.

#### --account-role

The account role that the group should have. One of `admin`, `read`, `developer`, `owner`, `financeadmin`, `none`.

#### --namespace-role (-nr)

Specifies a namespace role that the group should have. Can be repeated multiple times to add
multiple namespace roles to the group. Value is the form of `<namespaceid>-<role>` where the namespace ID is the full ID of the namespace and role is one of `admin`, `read`, or `write`. Example: `mynamespace.abc123-read` adds the read role for the `mynamespace.abc123` namespace.

#### --append (-a)

Will append namespace roles instead of replacing all existing roles already assigned. This allows namespace roles to be added without knowing what roles are already assigned to the group.

#### --remove (-r)

Will remove the given namespace roles instead of replacing all existing roles already assigned. This allows namespace roles to be removed without knowing what roles are already assigned to the group.

---

## tcld user command reference

The `tcld user` commands manage users in Temporal Cloud.

Alias: `u`

- [tcld user delete](#delete)
- [tcld user get](#get)
- [tcld user invite](#invite)
- [tcld user list](#list)
- [tcld user resend-invite](#resend-invite)
- [tcld user set-account-role](#set-account-role)
- [tcld user set-namespace-permissions](#set-namespace-permissions)

## delete

The `tcld user delete` command deletes the specified user in Temporal Cloud.
You must set either `--user-email` or `--user-id` to specify the user to be deleted.

Alias: `d`

The following modifiers control the behavior of the command.

#### --user-email

Specify the email address of the user to delete.

**Example**

```command
tcld user delete --user-email <test@example.com>
```

#### --user-id

Specify the user identifier of the user to delete.

**Example**

```command
tcld user delete --user-id <test-user-id>
```

#### --request-id

The request identifier to use for the asynchronous operation.

If not set, the server assigns an identifier.

Alias: `-r`

#### --resource-version

Specify a resource version (ETag) to update from.
If not specified, the latest version is used.

Alias: `-v`

## get

The `tcld user get` command gets information about the specified user in Temporal Cloud.
You must set either `--user-email` or `--user-id`.

Alias: `g`

The following modifiers control the behavior of the command.

#### --user-email

Specify the email address of the user to get information about.

**Example**

```command
tcld user delete --user-email <test@example.com>
```

#### --user-id

Specify the user identifier of the user to get information about.

**Example**

```command
tcld user delete --user-id <test-user-id>
```

## invite

The `tcld namespace invite` command invites the specified user to join Temporal Cloud.

Alias: `i`

The following modifiers control the behavior of the command.

#### --user-email

_Required modifier_

Specify the email address of the user to be invited.
You can supply this modifier multiple times to invite multiple users in a single request.

Alias: `-e`

#### --account-role

_Required modifier_

Specify the [account-level Role](/cloud/manage-access/roles-and-permissions#account-level-roles) for the invited user.

Available account roles: `admin` | `developer` | `read`.

Alias: `--ar`

#### --namespace-permission

Specify the [Namespace-level permissions](/cloud/manage-access/roles-and-permissions#namespace-level-permissions) for the invited user.
You can supply this modifier multiple times to set multiple Namespace permissions in a single request.

Each value must be in the format of `namespace=permission-type`.

Available namespace permissions: `Admin` | `Write` | `Read`.

Alias: `-p`

#### --request-id

The request identifier to use for the asynchronous operation.

If not set, the server assigns an identifier.

Alias: `-r`

```command
tcld user invite --user-email <test@example.com> --account-role developer --namespace-permission ns1=Admin --namespace-permission ns2=Write --request-id <123456>
```

## list

The `tcld user list` command returns a paginated list of users in Temporal Cloud.

Alias: `l`

**Example**

```command
tcld user list
```

The following modifiers control the behavior of the command.

#### --namespace

List users that have permissions to the Namespace.

Alias: `-n`

**Example**

```command
tcld user list --namespace <namespace_id>
```

#### --page-token

Page token for paging list users request.

Alias: `-p`

#### --page-size

Page size for paging list users request.

Defaults to 10.

Alias: `-s`

## resend-invite

The `tcld user resend-invite` command resends an invitation to the specified user in Temporal Cloud.
You must set either `--user-email` or `--user-id` to specify the user to receive another invitation.

Alias: `ri`

The following modifiers control the behavior of the command.

#### --user-email

Specify the email address of the user to resend an invitation to.

**Example**

```bash
tcld user resend-invite --user-email <test@example.com>
```

#### --user-id

Specify the user identifier of the user to resend an invitation to.

**Example**
