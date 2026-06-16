# set up Cassandra schema
setup_cassandra_schema() {
  #...
  # use valid schema for the version of the database you want to set up for Visibility
    VISIBILITY_SCHEMA_DIR=${TEMPORAL_HOME}/schema/cassandra/visibility/versioned
    if [[ ${SKIP_DB_CREATE} != true ]]; then
        temporal-cassandra-tool --ep "${CASSANDRA_SEEDS}" create -k "${VISIBILITY_KEYSPACE}" --rf "${CASSANDRA_REPLICATION_FACTOR}"
    fi
    temporal-cassandra-tool --ep "${CASSANDRA_SEEDS}" -k "${VISIBILITY_KEYSPACE}" setup-schema -v 0.0
    temporal-cassandra-tool --ep "${CASSANDRA_SEEDS}" -k "${VISIBILITY_KEYSPACE}" update-schema -d "${VISIBILITY_SCHEMA_DIR}"
  #...
}
#...
