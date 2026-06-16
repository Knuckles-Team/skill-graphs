
```bash
tcld user resend-invite --user-id <test-user-id>
```

#### --request-id

The request identifier to use for the asynchronous operation.

If not set, the server assigns an identifier.

Alias: `-r`

## set-account-role

The `tcld user set-account-role` command sets an [account-level Role](/cloud/manage-access/roles-and-permissions#account-level-roles) for the specified user in Temporal Cloud.
You must set either `--user-email` or `--user-id`.

Alias: `ri`

The following modifiers control the behavior of the command.

#### --account-role

_Required modifier_

Specify the account-level Role to assign to the user.

Available account roles: `admin` | `developer` | `read`.

Alias: `-ar`

#### --user-email

Specify the email address of the user to assign an account-level Role to.

Alias: `-e`

**Example**

```command
tcld user set-account-role --user-email <test@example.com> --account-role Developer
```

#### --user-id

Specify the user identifier of the user to assign an account-level Role to.

Alias: `--id`

**Example**

```command
tcld user set-account-role --user-id <test-user-id> --account-role Developer
```

#### --request-id

The request identifier to use for the asynchronous operation.

If not set, the server assigns an identifier.

Alias: `-r`

#### --resource-version

Specify a resource version (ETag) to update from.
If not specified, the latest version is used.

Alias: `-v`

## set-namespace-permissions

The `tcld user set-namespace-permissions` command sets [Namespace-level permissions](/cloud/manage-access/roles-and-permissions#namespace-level-permissions) for a specified user in Temporal Cloud.
You must set either `--user-email` or `--user-id`.

Alias: `snp`

The following modifiers control the behavior of the command.

#### --user-email

Specify the email address of the user to assign Namespace-level permissions to.

**Example**

```command
tcld user set-namespace-permissions --user-email <test@example.com>
```

#### --user-id

Specify the user identifier of the user to assign Namespace-level permissions to.

**Example**

```command
tcld user set-namespace-permissions --user-id <test-user-id>
```

#### --request-id

The request identifier to use to assign Namespace-level permissions to.

If not set, the server assigns an identifier.

Alias: `-r`

#### --resource-version

Specify a resource version (ETag) to assign Namespace-level permissions to.
If not specified, the latest version is used.

Alias: `-v`

#### --namespace-permission

Specify the [Namespace-level permissions](/cloud/manage-access/roles-and-permissions#namespace-level-permissions) for the invited user.
You can supply this modifier multiple times to set multiple Namespace permissions in a single request.

Each value must be in the format of `namespace=permission-type`.

Available namespace permissions: `Admin` | `Write` | `Read`.

Alias: `-p`

---

## tcld version command reference

The `tcld version` command gets version information about tcld.

Alias: `v`

`tcld version`

The command has no modifiers.

---

## Temporal Cloud Terraform provider

The Terraform Temporal Cloud provider allows you to use Terraform to manage resources for Temporal Cloud. The Terraform
tool manages infrastructure as code (IaC). With this provider, you can use Terraform to automate Temporal Cloud resource
management, including Namespaces, Users, Service Accounts, API Keys and more.

:::note Terraform Management

Once a resource is managed by Terraform, you should only use Terraform to manage that resource.

:::

Resources:

- The [Temporal Cloud Terraform provider](https://registry.terraform.io/providers/temporalio/temporalcloud/latest) is
  available in the Terraform Registry, where you can find detailed documentation on the Provider's supported resources
  and data sources.
- The GitHub repository for the Terraform provider is
  [terraform-provider-temporalcloud](https://github.com/temporalio/terraform-provider-temporalcloud/tree/main), where
  you can report bugs, provide feature requests, and
  [contribute](https://github.com/temporalio/terraform-provider-temporalcloud/blob/main/CONTRIBUTING.md) to the
  provider. We encourage your input as we develop the provider with the community.
- To view the list of available Temporal Cloud resources supported by Terraform provider, visit the resources section of
  the Terraform documentation in Hashi's
  [registry](https://registry.terraform.io/providers/temporalio/temporalcloud/latest/docs).

### Prerequisites

To use the Terraform provider, you'll need the following:

- The [Terraform CLI](https://developer.hashicorp.com/terraform/cli)
- An [API Key](/cloud/api-keys): an API Key is required to use the Terraform provider.
  - See [the API docs](https://docs.temporal.io/cloud/api-keys#generate-an-api-key) for instructions on generating an
    API Key.

:::note OpenTofu Registry

Our Terraform Provider is registered with [OpenTofu](https://opentofu.org), but that registration is not maintained or
managed by Temporal Technologies.

:::

## Setup

Generate an [API Key](https://docs.temporal.io/cloud/api-keys#generate-an-api-key) to authenticate Terraform operations
with your Temporal Cloud account or a Service Account. Then, either use an environment variable or pass the API Key into
the provider manually to manage your Temporal Cloud Terraform resources.

Follow these examples to use an environment variable to pass in your API Key to the provider.

<Tabs>
  <TabItem value="macos" label="macOS" default>
Export your environment variable for secure access to the API Keys.

```bash
