# temporal-elasticsearch-tool is available in v1.30+ server releases
if [ -x /usr/local/bin/temporal-elasticsearch-tool ]; then
  echo 'Using temporal-elasticsearch-tool for Elasticsearch setup'
  temporal-elasticsearch-tool --ep "$ES_SCHEME://$ES_HOST:$ES_PORT" setup-schema
  temporal-elasticsearch-tool --ep "$ES_SCHEME://$ES_HOST:$ES_PORT" create-index --index $ES_VISIBILITY_INDEX
else
  echo 'Using curl for Elasticsearch setup'
  echo 'WARNING: curl will be removed from admin-tools in v1.30.'
  echo 'Waiting for Elasticsearch to be ready...'
  max_attempts=30
  attempt=0
  until curl -s -f "$ES_SCHEME://$ES_HOST:$ES_PORT/_cluster/health?wait_for_status=yellow&timeout=1s"; do
    attempt=$((attempt + 1))
    if [ $attempt -ge $max_attempts ]; then
      echo "ERROR: Elasticsearch did not become ready after $max_attempts attempts"
      echo "Last error from curl:"
      curl "$ES_SCHEME://$ES_HOST:$ES_PORT/_cluster/health?wait_for_status=yellow&timeout=1s" 2>&1 || true
      exit 1
    fi
    echo "Elasticsearch not ready yet, waiting... (attempt $attempt/$max_attempts)"
    sleep 2
  done
  echo ''
  echo 'Elasticsearch is ready'
  echo 'Creating index template...'
  curl -X PUT --fail "$ES_SCHEME://$ES_HOST:$ES_PORT/_template/temporal_visibility_v1_template" -H 'Content-Type: application/json' --data-binary "@/etc/temporal/schema/elasticsearch/visibility/index_template_$ES_VERSION.json"
  echo ''
  echo 'Creating index...'
  curl --head --fail "$ES_SCHEME://$ES_HOST:$ES_PORT/$ES_VISIBILITY_INDEX" 2>/dev/null || curl -X PUT --fail "$ES_SCHEME://$ES_HOST:$ES_PORT/$ES_VISIBILITY_INDEX"
  echo ''
fi

echo 'MySQL and Elasticsearch setup complete'
```
{/* SNIPEND */}

### Elasticsearch privileges

Ensure that the following privileges are granted for the Elasticsearch Temporal index:

- **Read**
  - [index privileges](https://www.elastic.co/guide/en/elasticsearch/reference/current/security-privileges.html#privileges-list-indices):
    `create`, `index`, `delete`, `read`
- **Write**
  - [index privileges](https://www.elastic.co/guide/en/elasticsearch/reference/current/security-privileges.html#privileges-list-indices):
    `write`
- **Custom Search Attributes**
  - [index privileges](https://www.elastic.co/guide/en/elasticsearch/reference/current/security-privileges.html#privileges-list-indices):
    `manage`
  - [cluster privileges](https://www.elastic.co/guide/en/elasticsearch/reference/current/security-privileges.html#privileges-list-cluster):
    `monitor` or `manage`.

## How to set up Dual Visibility {/* #dual-visibility */}

To enable [Dual Visibility](/dual-visibility), set up a secondary Visibility store with your primary Visibility store,
and configure your Temporal Service to enable read and/or write operations on the secondary Visibility store.

With Dual Visibility, you can read from only one Visibility store at a time, but can configure your Temporal Service to
write to primary only, secondary only, or to both primary and secondary stores.

#### Set up secondary Visibility store

Set the secondary store with the `secondaryVisibilityStore` configuration key in your Persistence configuration, and
then define the secondary Visibility store configuration under `datastores`.

You can configure any of the [supported databases](/self-hosted-guide/visibility) as your secondary store.

Examples:

To configure MySQL as a secondary store with Cassandra as your primary store, do the following.

```yaml
persistence:
  visibilityStore: cass-visibility # This is your primary Visibility store
  secondaryVisibilityStore: mysql-visibility # This is your secondary Visibility store
  datastores:
    cass-visibility:
      cassandra:
        hosts: '127.0.0.1'
        keyspace: 'temporal_primary_visibility'
    mysql-visibility:
      sql:
        pluginName: 'mysql8' # Verify supported versions. Use a version of SQL that supports advanced Visibility.
        databaseName: 'temporal_secondary_visibility'
        connectAddr: '127.0.0.1:3306'
        connectProtocol: 'tcp'
        user: 'temporal'
        password: 'temporal'
```

To configure Elasticsearch as both your primary and secondary store, use the configuration key
`elasticsearch.indices.secondary_visibility`, as shown in the following example.

```yaml
persistence:
  visibilityStore: es-visibility
  datastores:
    es-visibility:
      elasticsearch:
        version: 'v7'
        logLevel: 'error'
        url:
          scheme: 'http'
          host: '127.0.0.1:9200'
        indices:
          visibility: temporal_visibility_v1
          secondary_visibility: temporal_visibility_v1_new
        closeIdleConnectionsInterval: 15s
```

#### Database schema and setup

The database schema and setup for a secondary store depends on the database you plan to use.

- [MySQL](#mysql)
- [PostgreSQL](#postgresql)
- [SQLite](#sqlite)
- [Elasticsearch](#elasticsearch)

For the Cassandra and MySQL configuration in the previous example, an example setup script would be as follows.

```bash
#...
