# Create and setup visibility database
temporal-sql-tool --plugin mysql8 --ep ${MYSQL_SEEDS} -u ${MYSQL_USER} -p ${DB_PORT:-3306} --db temporal_visibility create
temporal-sql-tool --plugin mysql8 --ep ${MYSQL_SEEDS} -u ${MYSQL_USER} -p ${DB_PORT:-3306} --db temporal_visibility setup-schema -v 0.0
temporal-sql-tool --plugin mysql8 --ep ${MYSQL_SEEDS} -u ${MYSQL_USER} -p ${DB_PORT:-3306} --db temporal_visibility update-schema -d /etc/temporal/schema/mysql/v8/visibility/versioned

echo 'MySQL schema setup complete'
```
{/* SNIPEND */}

Note that the script uses
[temporal-sql-tool](https://github.com/temporalio/temporal/blob/3b982585bf0124839e697952df4bba01fe4d9543/tools/sql/main.go)
to run the setup.

## How to set up PostgreSQL Visibility store {/* #postgresql */}

:::tip Support, stability, and dependency info

- PostgreSQL v9.6 and later.
- Advanced Visibility is available on PostgreSQL v12 and later with Temporal Server v1.20 and later.
- PostgreSQL v9.6 through v11 support applied to older standard Visibility deployments before Temporal Server v1.24. We
  recommend upgrading to PostgreSQL 12 or later.

:::

You can set PostgreSQL as your [Visibility store](/temporal-service/visibility). Verify
[supported versions](/self-hosted-guide/visibility) before you proceed.

If using PostgreSQL v12 or later as your Visibility store with Temporal Server v1.20 and later, any
[custom Search Attributes](/search-attribute#custom-search-attribute) that you create must be associated with a
Namespace in that Temporal Service.

### Persistence configuration

Set your PostgreSQL Visibility store name in the `visibilityStore` parameter in your Persistence configuration, and then
define the Visibility store configuration under `datastores`.

The following example shows how to set a Visibility store `postgres-visibility` and define the datastore configuration
in your Temporal Service configuration YAML.

```yaml
#...
persistence:
  #...
  visibilityStore: postgres-visibility
  #...
  datastores:
    default:
    #...
    postgres-visibility:
      sql:
        pluginName: 'postgres12' # For PostgreSQL v12 and later. For earlier versions, use "postgres" plugin.
        databaseName: 'temporal_visibility'
        connectAddr: ' ' # remote address of this database; for example, 127.0.0.0:5432
        connectProtocol: ' ' # protocol example: tcp
        user: 'username_for_auth'
        password: 'password_for_auth'
        maxConns: 2
        maxIdleConns: 2
        maxConnLifetime: '1h'
#...
```

To enable advanced Visibility features on your PostgreSQL Visibility store, upgrade to PostgreSQL v12 or later with
Temporal Server v1.20 or later. See [Upgrade Server](/self-hosted-guide/upgrade-server#upgrade-server) for details on
how to upgrade your Temporal Server and database schemas.

### Database schema and setup

Visibility data is stored in a database table called `executions_visibility` and must be created using the schema for
[PostgreSQL v12 and later](https://github.com/temporalio/temporal/tree/main/schema/postgresql/v12/visibility)

The following example shows how to set up your PostgreSQL as both persistence and Visibility store using
`temporal-sql-tool`. Refer to the
[samples-server repository](https://github.com/temporalio/samples-server/tree/main/compose/scripts) for more examples
with different databases.

{/* SNIPSTART compose-postgres-setup */}
[compose/scripts/setup-postgres.sh](https://github.com/temporalio/samples-server/blob/main/compose/scripts/setup-postgres.sh)
```sh
set -eu
