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
```

## How to integrate Elasticsearch or OpenSearch into a Temporal Service {/* #elasticsearch */}

You can integrate Elasticsearch or OpenSearch with your Temporal Service as your Visibility store. We recommend using
one of these backends for large-scale operations on the Temporal Service.

To integrate Elasticsearch or OpenSearch with your Temporal Service, edit the `persistence` section of your
`development.yaml` configuration file to add the search backend as the `visibilityStore`, and run the index schema setup
commands.

Use the following version guidance:

- Elasticsearch v7 is supported with Temporal Server v1.7 and later.
- Elasticsearch v8 is supported with Temporal Server v1.18 and later.
- OpenSearch 2+ is supported with Temporal Server v1.30.1 and later.

The examples in this section use Elasticsearch. For OpenSearch, use the same datastore configuration shape and
operational flow unless a release note for your target Temporal Server version says otherwise.

### Persistence configuration

Set your Visibility store name in the `visibilityStore` parameter in your Persistence configuration, and then define the
search backend configuration under `datastores`.

The following example shows how to set a Visibility store named `es-visibility` and define the Elasticsearch datastore
configuration in your Temporal Service configuration YAML.

```yaml
persistence:
  ...
  visibilityStore: es-visibility
  datastores:
    ...
    es-visibility: # Define the Elasticsearch datastore connection information under the `es-visibility` key
      elasticsearch:
        version: "v7"
        url:
          scheme: "http"
          host: "127.0.0.1:9200"
        indices:
          visibility: temporal_visibility_v1_dev
```

### Index schema and index

To set up Elasticsearch as your Visibility store, use the `temporal-elasticsearch-tool` available in the
`temporalio/admin-tools` image.

The following example shows how to set up an Elasticsearch Visibility store with a MySQL persistence store using
`temporal-elasticsearch-tool`. For more examples with different databases, refer to the
[samples-server repository](https://github.com/temporalio/samples-server/tree/main/compose/scripts).

{/* SNIPSTART compose-mysql-es-setup */}
[compose/scripts/setup-mysql-es.sh](https://github.com/temporalio/samples-server/blob/main/compose/scripts/setup-mysql-es.sh)
```sh
set -eu
