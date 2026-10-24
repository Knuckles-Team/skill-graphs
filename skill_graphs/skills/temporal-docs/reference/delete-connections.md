# Delete connections
temporal operator cluster remove --name="someClusterName"
```

---

## Managing Namespaces

:::info Open source Temporal

This page covers namespace operations for **open source Temporal**. For core namespace concepts, see
[Temporal Namespace](/namespaces). For Temporal Cloud, see [Temporal Cloud Namespaces](/cloud/namespaces).

:::

A [Namespace](/namespaces) is a unit of isolation within the Temporal Platform. Before you can run Workflows, you must
register at least one Namespace with your Temporal Service.

## Create a Namespace

Registering a Namespace creates it on the Temporal Service. When you register a Namespace, you must set a
[Retention Period](/temporal-service/temporal-server#retention-period) that determines how long closed Workflow
execution history is kept.

You can create Namespaces using:

- **Temporal CLI** (recommended): [`temporal operator namespace create`](/cli/command-reference/operator#create)
- **Go SDK**: [`RegisterNamespace`](/develop/go/client/namespaces#register-namespace)
- **Java SDK**: [`RegisterNamespace`](/develop/java/client/namespaces#register-namespace)
- **TypeScript SDK**: [Namespace management](/develop/typescript/client/namespaces#register-namespace)

### The default Namespace

If no Namespace is specified, SDKs and CLI use the `default` Namespace. You must register this Namespace before using
it.

For local development, the [`temporal server start-dev`](/cli/command-reference/server#start-dev) command automatically creates the
`default` Namespace.

For all other deployment methods, create the `default` Namespace manually using the Temporal CLI:

```bash
temporal operator namespace create --namespace default
```

Namespace registration takes up to 15 seconds to complete. Wait for this process to finish before making calls to the
Namespace.

## Manage Namespaces

Common namespace management operations:

| Operation | CLI Command                                                                        | Description                         |
| --------- | ---------------------------------------------------------------------------------- | ----------------------------------- |
| List      | [`temporal operator namespace list`](/cli/command-reference/operator#list)         | List all registered Namespaces      |
| Describe  | [`temporal operator namespace describe`](/cli/command-reference/operator#describe) | Get details for a Namespace         |
| Update    | [`temporal operator namespace update`](/cli/command-reference/operator#update)     | Update Namespace configuration      |
| Delete    | [`temporal operator namespace delete`](/cli/command-reference/operator#delete)     | Delete a Namespace and all its data |

For SDK-based namespace management:

- [Go SDK namespace management](/develop/go/client/namespaces#manage-namespaces)
- [Java SDK namespace management](/develop/java/client/namespaces#manage-namespaces)
- [TypeScript SDK namespace management](/develop/typescript/client/namespaces#manage-namespaces)

### Deprecate vs Delete

- **Deprecate**: Prevents new Workflow Executions from starting, but existing Workflows continue to run.
- **Delete**: Removes the Namespace and all Workflow Executions. This is irreversible.

## Security

Use a custom [Authorizer](/self-hosted-guide/security#authorizer-plugin) on your Frontend Service to control who can
create, update, or deprecate Namespaces.

Without an Authorizer configured, Temporal uses the `nopAuthority` authorizer that allows all API calls unconditionally.

For Temporal Cloud, [role-based access controls](/cloud/manage-access/roles-and-permissions#namespace-level-permissions) provide namespace-level authorization without custom configuration.

## Best practices

For namespace naming conventions, organizational patterns, and production safeguards, see
[Namespace Best Practices](/best-practices/managing-namespace).

---

## Server frontend API reference

While it's usually easiest to interact with [Temporal Server](/temporal-service/temporal-server) via a
[Client SDK](/encyclopedia/temporal-sdks#temporal-client) or the [Temporal CLI](https://docs.temporal.io/cli), you can
also use its gRPC API.

Our Client and Worker SDKs use the gRPC API. The API reference is located here:

[`api-docs.temporal.io`](https://api-docs.temporal.io/)

## Use with code

Usually you interact with the API via high-level methods like `client.workflow.start()`. However, Client SDKs also
expose the underlying gRPC services. For instance, the TypeScript SDK has:

- WorkflowService:
  [`Client.connection.workflowService`](https://typescript.temporal.io/api/classes/client.Connection#workflowservice)
- OperatorService:
  [`Client.connection.operatorService`](https://typescript.temporal.io/api/classes/client.Connection/#operatorservice)
- HealthService:
  [`Client.connection.healthService`](https://typescript.temporal.io/api/classes/client.Connection/#healthservice)

If you're not using an SDK Client (rare), you can generate gRPC client stubs by:

- Cloning [`temporalio/api`](https://github.com/temporalio/api) (repo with the protobuf files)
- Generating code in [your language](https://grpc.io/docs/languages/)

## Use manually

To query the API manually via command line or a GUI, first:

- If you don't already have a Server to connect to, run [`temporal server start-dev`](/cli/command-reference/server#start-dev)
- Clone this repo:

```shell
git clone https://github.com/temporalio/api.git
cd api
```

### With command line

Install [`evans`](https://github.com/ktr0731/evans#installation).

```shell
cd /path/to/api
evans --proto temporal/api/workflowservice/v1/service.proto --port 7233
```

To connect to Temporal Cloud, set the host, cert, cert key, and TLS flag:

```shell
evans --proto temporal/api/workflowservice/v1/service.proto --host devrel.a2dd6.tmprl.cloud --port 7233 --tls --cert /Users/me/certs/temporal.pem --certkey /Users/me/certs/temporal.key
```

Once inside the evans prompt, you can run commands like `help`, `show service` to list available methods, and
`call ListWorkflowExecutions`.

### With a GUI

- Install [BloomRPC](https://github.com/bloomrpc/bloomrpc#installation).
- Open the app
- Select "Import Paths" button on the top-left and enter the path to the cloned repo: `/path/to/api`
- Select the "Import protos" + button and select this file:

```shell
/path/to/api/temporal/api/workflowservice/v1/service.proto
```

- A list of methods should appear in the sidebar. Select one.
- Edit the JSON in the left pane.
- Hit `Cmd/Ctrl-Enter` or click the play button to get a response from the server on the right.

<CaptionedImage src="/img/proto/ListWorkflowExecutions.png" title="ListWorkflowExecutions" />

One downside compared to [command line](#with-command-line) is it doesn't show enum names, just numbers like
`"task_queue_type": 1`.

<CaptionedImage src="/img/proto/DescribeTaskQueue.png" title="DescribeTaskQueue" />

---

## Self-hosted Temporal Nexus

:::info NEW TO NEXUS?

This page explains how to self-host Nexus. To learn about Nexus, see the [how Nexus works page](/nexus). To evaluate whether Nexus fits your use case, see the [evaluation guide](/evaluate/nexus).

:::

## Enable Nexus

Nexus can be configured by setting static configuration and dynamic configuration entries.

:::note
Nexus is supported in single-cluster setups only. See [Nexus Architecture](https://github.com/temporalio/temporal/blob/main/docs/architecture/nexus.md) for operational details.
:::

:::note
Replace `$PUBLIC_URL` with a URL value that's accessible to external callers or internally within the cluster.
Currently, external Nexus calls are considered experimental so it should be safe to use the address of an internal load balancer for the Frontend Service.
:::

To enable Nexus in your deployment:

1. Enable the HTTP API in the server's static configuration.

   ```yaml
   services:
     frontend:
       rpc:
         # NOTE: keep other fields as they were
         httpPort: 7243

   clusterMetadata:
     # NOTE: keep other fields as they were
     clusterInformation:
       active:
         # NOTE: keep other fields as they were
         httpAddress: $PUBLIC_URL:7243
   ```

2. Set the required dynamic configuration
    1. **Prior to version 1.30.X**, you must set the public callback URL and the allowed callback addresses.

       **NOTE**: the callback endpoint template and allowed addresses should be set when using the experimental
       "external" endpoint targets.

       ```yaml
       component.nexusoperations.callback.endpoint.template:
         # The URL must be publicly accessible if the callback is meant to be called by external services.
         # When using Nexus for cross namespace calls, the URL's host is irrelevant as the address is resolved using
         # membership. The URL is a Go template that interpolates the `NamepaceName` and `NamespaceID` variables.
         - value: https://$PUBLIC_URL:7243/namespaces/{{.NamespaceName}}/nexus/callback
       component.callbacks.allowedAddresses:
         # Limits which callback URLs are accepted by the server.
         # Wildcard patterns (*) and insecure (HTTP) callbacks are intended for development only.
         # For production, restrict allowed hosts and set AllowInsecure to false
         # whenever HTTPS/TLS is supported. Allowing HTTP increases MITM and data exposure risk.
         - value:
             - Pattern: "*" # Update to restrict allowed callers, e.g. "*.example.com"
               AllowInsecure: true # In production, set to false and ensure traffic is HTTPS/TLS encrypted
       ```

    2. **Version 1.30.X+**: Nexus is enabled by default. Only the system callback URL is needed.
       ```yaml
       component.nexusoperations.useSystemCallbackURL:
         - value: true
       ```

## Build and use Nexus Services

See [how Nexus works](/nexus) for an architectural overview, then follow an SDK guide to build your first Nexus Service.

:::tip SDK GUIDES

- [Go](/develop/go/nexus/feature-guide) |
  [Java](/develop/java/nexus) |
  [Python](/develop/python/nexus) |
  [TypeScript](/develop/typescript/nexus) |
  [.NET](/develop/dotnet/nexus)

:::

---

## Upgrade the Temporal Server

## How to upgrade the Temporal Server version {/* #upgrade-server */}

If a newer version of the [Temporal Server](/temporal-service/temporal-server) is available, a notification appears in
the Temporal Web UI.

:::info

If you are using a version that is older than 1.0.0, reach out to us at
[community.temporal.io](http://community.temporal.io) to ask how to upgrade.

:::

First check to see if an upgrade to the database schema is required for the version you wish to upgrade to. If a
database schema upgrade is required, it will be called out directly in the
[release notes](https://github.com/temporalio/temporal/releases). Some releases require changes to the schema, and some
do not. We ensure that any consecutive versions are compatible in terms of database schema upgrades, features, and
system behavior; however there is no guarantee that there is compatibility between _any_ two non-consecutive versions.

### Key considerations

When upgrading the Temporal Server, there are two key considerations to keep in mind:

1. **Sequential Upgrades:** Temporal Server should be upgraded sequentially, one minor version at a time. Before
   bumping to the next minor version, first upgrade to the highest available patch version of your current minor
   version. For example, if you're on \(v1.n.0\), upgrade to \(v1.n.latest\) first, then proceed to
   \(v1.(n+1).latest\). Repeat this sequence until you reach your desired version.

2. **Data Compatibility:** During an upgrade, the Temporal Server either updates or restructures the existing version
   data to match the data format of the newer version. Temporal Server ensures backward compatibility only between two
   successive minor versions. Consequently, skipping versions during an upgrade may lead to older data formats becoming
   unreadable. If the previous data format cannot be interpreted and converted to the newer format, the upgrade process
   will be unsuccessful.

### Step-by-Step Upgrade Procedure:

Upgrading the Temporal Server requires a methodical approach to ensure data integrity, compatibility, and seamless
transition between versions. The following documentation outlines the step-by-step process to successfully upgrade your
Temporal Server.

When upgrading your Temporal Server version, ensure that you upgrade sequentially.

1. **Upgrade Database Schema:** Before initiating the Temporal Server upgrade, use one of the recommended upgrade tools
   to update your database schema. This ensures it is aligned with the version of Temporal Server you aim to upgrade to.
2. **Upgrade Temporal Server:** Once the database schema is updated, proceed to upgrade the Temporal Server deployment
   to the next sequential version.
3. **Iterative Upgrades** (optional): Continue this process (steps 1 and 2) iteratively until you reach the desired
   Temporal Server version.

By adhering to the above guidelines and following the step-by-step procedure, you can ensure a smooth and successful
upgrade of your Temporal Server.

The Temporal Server upgrade updates or rewrites the old version data with the format introduced in the newer version.
Because Temporal Server guarantees backward compatibility between two consecutive minor versions, and because older
versions of the code are eventually removed from the code base, skipping versions when upgrading might cause older
formats to become unrecognizable. If the old format of the data can't be read to be rewritten to the new format, the
upgrades fail.

Check the [Temporal Server releases](https://github.com/temporalio/temporal/releases) and follow these releases in
order. Before upgrading to the next minor version, upgrade to the highest available patch version of your current minor
version first.

Also, be aware that each upgrade requires the History Service to load all Shards and update the Shard metadata, so allow
approximately 10 minutes on each version for these processes to complete before upgrading to the next version.

Use one of the upgrade tools to upgrade your database schema to be compatible with the Temporal Server version being
upgraded to.

### Upgrade Cassandra schema

If you are using Cassandra for your Temporal Service's persistence, use the `temporal-cassandra-tool` to upgrade both
the default Persistence and Visibility schemas.

**Example default schema upgrade:**

```bash
temporal_v1.2.1 $ temporal-cassandra-tool \
   --tls \
   --tls-ca-file <...> \
   --user <cassandra-user> \
   --password <cassandra-password> \
   --endpoint <cassandra.example.com> \
   --keyspace temporal \
   --timeout 120 \
   update \
   --schema-dir ./schema/cassandra/temporal/versioned
```

**Example visibility schema upgrade:**

```bash
temporal_v1.2.1 $ temporal-cassandra-tool \
   --tls \
   --tls-ca-file <...> \
   --user <cassandra-user> \
   --password <cassandra-password> \
   --endpoint <cassandra.example.com> \
   --keyspace temporal_visibility \
   --timeout 120 \
   update \
   --schema-dir ./schema/cassandra/visibility/versioned
```

### Upgrade Elasticsearch schema

If you are using Elasticsearch for your Temporal Service's Visibility, use the `temporal-elasticsearch-tool` to upgrade
the schema.

**Example schema upgrade:**

```bash
echo "Updating index mappings: $ES_VISIBILITY_INDEX"
temporal-elasticsearch-tool \
	--endpoint "$ES_SCHEME://$ES_HOST:$ES_PORT" \
	--user "$ES_USER" \
	--password "$ES_PWD" \
	update-schema \
	--index "$ES_VISIBILITY_INDEX"
```

### Upgrade PostgreSQL or MySQL schema

If you are using MySQL or PostgreSQL use the `temporal-sql-tool`, which works similarly to the
`temporal-cassandra-tool`.

Refer to this [Makefile](https://github.com/temporalio/temporal/blob/v1.4.1/Makefile#L367-L383) for context.

#### PostgreSQL

**Example default schema upgrade:**

```bash
./temporal-sql-tool \
	--tls \
	--tls-enable-host-verification \
	--tls-cert-file <path to your client cert> \
	--tls-key-file <path to your client key> \
	--tls-ca-file <path to your CA> \
	--ep localhost -p 5432 -u temporal -pw temporal --pl postgres --db temporal update-schema -d ./schema/postgresql/v96/temporal/versioned
```

**Example visibility schema upgrade:**

```bash
./temporal-sql-tool \
	--tls \
	--tls-enable-host-verification \
	--tls-cert-file <path to your client cert> \
	--tls-key-file <path to your client key> \
	--tls-ca-file <path to your CA> \
	--ep localhost -p 5432 -u temporal -pw temporal --pl postgres --db temporal_visibility update-schema -d ./schema/postgresql/v96/visibility/versioned
```

If you're upgrading PostgreSQL to v12 or later to enable advanced Visibility features with Temporal Server v1.20,
upgrade your PostgreSQL version first, and then run `temporal-sql-tool` with the `postgres12` plugin, as shown in the
following example:

```bash
./temporal-sql-tool \
	--tls \
	--tls-enable-host-verification \
	--tls-cert-file <path to your client cert> \
	--tls-key-file <path to your client key> \
	--tls-ca-file <path to your CA> \
	--ep localhost -p 5432 -u temporal -pw temporal --pl postgres12 --db temporal_visibility update-schema -d ./schema/postgresql/v12/visibility/versioned
```

#### MySQL

**Example default schema upgrade:**

```bash
./temporal-sql-tool \
	--tls \
	--tls-enable-host-verification \
	--tls-cert-file <path to your client cert> \
	--tls-key-file <path to your client key> \
	--tls-ca-file <path to your CA> \
	--ep localhost -p 3036 -u root -pw root --pl mysql --db temporal update-schema -d ./schema/mysql/v57/temporal/versioned/
```

**Example visibility schema upgrade:**

```bash
./temporal-sql-tool \
	--tls \
	--tls-enable-host-verification \
	--tls-cert-file <path to your client cert> \
	--tls-key-file <path to your client key> \
	--tls-ca-file <path to your CA> \
	--ep localhost -p 3036 -u root -pw root --pl mysql --db temporal_visibility update-schema -d ./schema/mysql/v57/visibility/versioned/
```

If you're upgrading MySQL to v8.0.17 or later to enable advanced Visibility features with Temporal Server v1.20, upgrade
your MySQL version first, and then run `temporal-sql-tool` with the `mysql8` plugin, as shown in the following example:

```bash
./temporal-sql-tool \
	--tls \
	--tls-enable-host-verification \
	--tls-cert-file <path to your client cert> \
	--tls-key-file <path to your client key> \
	--tls-ca-file <path to your CA> \
	--ep localhost -p 5432 -u temporal -pw temporal --pl mysql8 --db temporal_visibility update-schema -d ./schema/mysql/v8/visibility/versioned.
```

### Roll-out technique

We recommend preparing a staging Temporal Service and then doing the following to verify the upgrade is successful:

1. Create some simulation load on the staging Temporal Service.
2. Upgrade the database schema in the staging Temporal Service.
3. Wait and observe for a few minutes to verify that there is no unstable behavior from both the server and the
   simulation load logic.
4. Upgrade the server.
5. Now do the same to the live environment Temporal Service.

---

## Self-hosted Visibility feature setup

A [Visibility](/temporal-service/visibility) store is set up as a part of your
[Persistence store](/temporal-service/persistence) to enable listing and filtering details about Workflow Executions
that exist on your Temporal Service.

A Visibility store is required in a Temporal Service setup because it is used by [Temporal Web UI](/web-ui) and
[Temporal CLI](/cli) to pull [Workflow Execution](/workflow-execution) data and enables features like batch operations
on a group of Workflow Executions.

With the Visibility store, you can use [List Filters](/list-filter) with [Search Attributes](/search-attribute) to list
and filter Workflow Executions that you want to review or act upon.

Supported Visibility stores include:

- Elasticsearch v7 with Temporal Server v1.7 and later
- Elasticsearch v8 with Temporal Server v1.18 and later
- OpenSearch 2+ with Temporal Server v1.30.1 and later
- MySQL v8.0.17 and later with Temporal Server v1.20 and later
- PostgreSQL v12 and later with Temporal Server v1.20 and later
- SQLite v3.31.0 and later with Temporal Server v1.20 and later

## Current and legacy Visibility support {/* #supported-databases */}

[Advanced Visibility](/visibility#advanced-visibility) is the current generation of Temporal Visibility. It supports the
modern query model, including [custom Search Attributes](/search-attribute#custom-search-attribute).

This page also includes guidance for the legacy (deprecated in Temporal Server v1.21 and removed in v1.24)
[standard Visibility](#legacy-standard-visibility) model for older deployments and migration work. In this context,
"advanced" and "standard (legacy)" refer to the current and legacy generations of Temporal Visibility, respectively.

The following compatibility matrix summarizes which generation of Visibility each store supports and the Temporal Server
versions required:

| Store                                                                                                               | Advanced Visibility (current)                                                                                                                                    | Standard Visibility (legacy)                                          |
| :------------------------------------------------------------------------------------------------------------------ | :--------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------- |
| [Elasticsearch](#elasticsearch) Recommended for any setup that spawns more than a few Workflow Executions | v7 on Temporal Server v1.7+, v8 on Temporal Server v1.18+                                                                                                        | Not supported                                                         |
| [OpenSearch](#elasticsearch)                                                                                        | 2+ on Temporal Server v1.30.1+                                                                                                                                   | Not supported                                                         |
| [MySQL](#mysql)                                                                                                     | v8.0.17+ on Temporal Server v1.20+                                                                                                                               | v5.7+ on older deployments before Temporal Server v1.24               |
| [PostgreSQL](#postgresql)                                                                                           | v12+ on Temporal Server v1.20+                                                                                                                                   | v9.6+ on older deployments before Temporal Server v1.24               |
| [SQLite](#sqlite)                                                                                                   | v3.31.0+ on Temporal Server v1.20+                                                                                                                               | Not supported                                                         |
| [Cassandra](#cassandra)                                                                                             | Not supported.To migrate from Cassandra to a supported advanced Visibility store, see [Migrating Visibility database](#migrating-visibility-database). | Deprecated in Temporal Server v1.21, removed in Temporal Server v1.24 |

You can use any combination of the supported databases for your Persistence and Visibility stores. For updates, check
[Server release notes](https://github.com/temporalio/temporal/releases).

Temporal Server v1.21 introduced support for a secondary Visibility store in your Temporal Service to enable
[Dual Visibility](/dual-visibility). This is useful for migrating your Visibility store database.

## How to set up MySQL Visibility store {/* #mysql */}

:::tip Support, stability, and dependency info

- MySQL v5.7 and later.
- Advanced Visibility is available on MySQL v8.0.17 and later with Temporal Server v1.20 and later.
- MySQL v5.7 support applied to older standard Visibility deployments before Temporal Server v1.24.

:::

You can set MySQL as your [Visibility store](/temporal-service/visibility). Verify
[supported versions](/self-hosted-guide/visibility) before you proceed.

If using MySQL v8.0.17 or later as your Visibility store with Temporal Server v1.20 and later, any
[custom Search Attributes](/search-attribute#custom-search-attribute) that you create must be associated with a
Namespace in that Temporal Service.

### Persistence configuration

Set your MySQL Visibility store name in the `visibilityStore` parameter in your Persistence configuration, and then
define the Visibility store configuration under `datastores`.

The following example shows how to set a Visibility store `mysql-visibility` and define the datastore configuration in
your Temporal Service configuration YAML.

```yaml
#...
persistence:
  #...
  visibilityStore: mysql-visibility
  #...
  datastores:
    default:
      #...
    mysql-visibility:
      sql:
        pluginName: 'mysql8' # For MySQL v8.0.17 and later. For earlier versions, use "mysql" plugin.
        databaseName: 'temporal_visibility'
        connectAddr: ' ' # Remote address of this database; for example, 127.0.0.0:3306
        connectProtocol: ' ' # Protocol example: tcp
        user: 'username_for_auth'
        password: 'password_for_auth'
        maxConns: 2
        maxIdleConns: 2
        maxConnLifetime: '1h'
#...
```

For details on the configuration parameters and values, see
[Temporal Service configuration](/references/configuration#sql).

To enable advanced Visibility features on your MySQL Visibility store, upgrade to MySQL v8.0.17 or later with Temporal
Server v1.20 or later. See [Upgrade Server](/self-hosted-guide/upgrade-server#upgrade-server) on how to upgrade your
Temporal Server and database schemas.

For example configuration templates, see
[MySQL Visibility store configuration](https://github.com/temporalio/temporal/blob/main/config/development-mysql8.yaml).

### Database schema and setup

Visibility data is stored in a database table called `executions_visibility` and must be created using the schema for
[MySQL v8.0.17 and later](https://github.com/temporalio/temporal/tree/main/schema/mysql/v8/visibility).

The following example shows how to set up your MySQL as both your persistence and Visibility store using
`temporal-sql-tool`. Refer to the
[samples-server repository](https://github.com/temporalio/samples-server/tree/main/compose/scripts) for more examples
with different databases.

{/* SNIPSTART compose-mysql-setup */}
[compose/scripts/setup-mysql.sh](https://github.com/temporalio/samples-server/blob/main/compose/scripts/setup-mysql.sh)
```sh
set -eu
