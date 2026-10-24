# Create and setup visibility database
temporal-sql-tool --plugin postgres12 --ep ${POSTGRES_SEEDS} -u ${POSTGRES_USER} -p ${DB_PORT:-5432} --db temporal_visibility create
temporal-sql-tool --plugin postgres12 --ep ${POSTGRES_SEEDS} -u ${POSTGRES_USER} -p ${DB_PORT:-5432} --db temporal_visibility setup-schema -v 0.0
temporal-sql-tool --plugin postgres12 --ep ${POSTGRES_SEEDS} -u ${POSTGRES_USER} -p ${DB_PORT:-5432} --db temporal_visibility update-schema -d /etc/temporal/schema/postgresql/v12/visibility/versioned

echo 'PostgreSQL schema setup complete'
```
{/* SNIPEND */}

Note that the script uses
[temporal-sql-tool](https://github.com/temporalio/temporal/blob/3b982585bf0124839e697952df4bba01fe4d9543/tools/sql/main.go)
to run the setup.

## How to set up SQLite Visibility store {/* #sqlite */}

:::tip Support, stability, and dependency info

- SQLite v3.31.0 and later.

:::

You can set SQLite as your [Visibility store](/temporal-service/visibility). Verify
[supported versions](/self-hosted-guide/visibility) before you proceed.

Temporal supports only an in-memory database with SQLite; this means that the database is automatically created when
Temporal Server starts and is destroyed when Temporal Server stops.

You can change the configuration to use a file-based database so that it is preserved when Temporal Server stops.
However, if you use a file-based SQLite database, upgrading your database schema to enable advanced Visibility features
is not supported; in this case, you must delete the database and create it again to upgrade.

If using SQLite v3.31.0 and later as your Visibility store with Temporal Server v1.20 and later, any
[custom Search Attributes](/search-attribute#custom-search-attribute) that you create must be associated with a
Namespace in that Temporal Service.

### Persistence configuration

Set your SQLite Visibility store name in the `visibilityStore` parameter in your Persistence configuration, and then
define the Visibility store configuration under `datastores`.

The following example shows how to set a Visibility store `sqlite-visibility` and define the datastore configuration in
your Temporal Service configuration YAML.

```yaml
persistence:
  # ...
  visibilityStore: sqlite-visibility
  # ...
  datastores:
    # ...
    sqlite-visibility:
      sql:
        user: 'username_for_auth'
        password: 'password_for_auth'
        pluginName: 'sqlite'
        databaseName: 'default'
        connectAddr: 'localhost'
        connectProtocol: 'tcp'
        connectAttributes:
          mode: 'memory'
          cache: 'private'
        maxConns: 1
        maxIdleConns: 1
        maxConnLifetime: '1h'
        tls:
          enabled: false
          caFile: ''
          certFile: ''
          keyFile: ''
          enableHostVerification: false
          serverName: ''
```

SQLite (v3.31.0 and later) has advanced Visibility enabled by default.

### Database schema and setup

Visibility data is stored in a database table called `executions_visibility` that must be set up according to the
schemas defined (by supported versions) in
https://github.com/temporalio/temporal/blob/main/schema/sqlite/v3/visibility/schema.sql.

For an example of setting up the SQLite schema, see
[Temporalite](https://github.com/temporalio/temporalite/blob/main/server.go) setup.

## Legacy standard Visibility configuration {/* #legacy-standard-visibility */}

The following section applies to older self-hosted deployments that still use standard Visibility. For new deployments,
use one of the advanced Visibility backends described earlier on this page.

### How to set up Cassandra Visibility store {/* #cassandra */}

:::tip Support, stability, and dependency info

- Cassandra supported only standard Visibility. Standard Visibility was deprecated in Temporal Server v1.21 and removed
  in v1.24. For updates, check the [Temporal Server release notes](https://github.com/temporalio/temporal/releases).
- We recommend migrating from Cassandra to any of the other supported databases for Visibility.

:::

Advanced Visibility is not supported with Cassandra.

To enable current Visibility features, use MySQL, PostgreSQL, SQLite, Elasticsearch, or OpenSearch as your Visibility
store. We recommend Elasticsearch or OpenSearch for any Temporal Service setup that handles more than a few Workflow
Executions because these backends support the Visibility request load and help optimize performance.

To migrate from Cassandra to a supported SQL database, see
[Migrating Visibility database](#migrating-visibility-database).

### Persistence configuration

Set your Cassandra Visibility store name in the `visibilityStore` parameter in your Persistence configuration, and then
define the Visibility store configuration under `datastores`.

The following example shows how to set a Visibility store `cass-visibility` and define the datastore configuration in
your Temporal Service configuration YAML.

```yaml
#...
persistence:
  #...
  visibilityStore: cass-visibility
  #...
  datastores:
    default:
    #...
    cass-visibility:
      cassandra:
        hosts: '127.0.0.1'
        keyspace: 'temporal_visibility'
#...
```

### Database schema and setup

Visibility data is stored in a database table called `executions_visibility` that must be set up according to the
schemas defined (by supported versions) in https://github.com/temporalio/temporal/tree/main/schema/cassandra/visibility.

The following example shows how to set up your Cassandra Visibility store using `temporal-cassandra-tool`. For more
examples with different databases, refer to the
[samples-server repository](https://github.com/temporalio/samples-server/tree/main/compose/scripts).

```bash
#...
