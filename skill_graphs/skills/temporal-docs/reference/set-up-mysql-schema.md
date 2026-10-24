# set up MySQL schema
setup_mysql_schema() {
    #...
    # use valid schema for the version of the database you want to set up for Visibility
    VISIBILITY_SCHEMA_DIR=${TEMPORAL_HOME}/schema/mysql/${MYSQL_VERSION_DIR}/visibility/versioned
    if [[ ${SKIP_DB_CREATE} != true ]]; then
        temporal-sql-tool --ep "${MYSQL_SEEDS}" -u "${MYSQL_USER}" -p "${DB_PORT}" "${MYSQL_CONNECT_ATTR[@]}" --db "${VISIBILITY_DBNAME}" create
    fi
    temporal-sql-tool --ep "${MYSQL_SEEDS}" -u "${MYSQL_USER}" -p "${DB_PORT}" "${MYSQL_CONNECT_ATTR[@]}" --db "${VISIBILITY_DBNAME}" setup-schema -v 0.0
    temporal-sql-tool --ep "${MYSQL_SEEDS}" -u "${MYSQL_USER}" -p "${DB_PORT}" "${MYSQL_CONNECT_ATTR[@]}" --db "${VISIBILITY_DBNAME}" update-schema -d "${VISIBILITY_SCHEMA_DIR}"
#...
}
```

For Elasticsearch as both primary and secondary Visibility store configuration in the previous example, an example setup
script would be as follows.

```bash
#...
