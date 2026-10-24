# Set up Elasticsearch index
setup_es_index() {
    ES_SERVER="${ES_SCHEME}://${ES_SEEDS%%,*}:${ES_PORT}"
    # ES_SERVER is the URL of Elasticsearch server i.e. "http://localhost:9200".
    SETTINGS_URL="${ES_SERVER}/_cluster/settings"
    SETTINGS_FILE=${TEMPORAL_HOME}/schema/elasticsearch/visibility/cluster_settings_${ES_VERSION}.json
    TEMPLATE_URL="${ES_SERVER}/_template/temporal_visibility_v1_template"
    SCHEMA_FILE=${TEMPORAL_HOME}/schema/elasticsearch/visibility/index_template_${ES_VERSION}.json
    INDEX_URL="${ES_SERVER}/${ES_VIS_INDEX}"
    curl --fail --user "${ES_USER}":"${ES_PWD}" -X PUT "${SETTINGS_URL}" -H "Content-Type: application/json" --data-binary "@${SETTINGS_FILE}" --write-out "\n"
    curl --fail --user "${ES_USER}":"${ES_PWD}" -X PUT "${TEMPLATE_URL}" -H 'Content-Type: application/json' --data-binary "@${SCHEMA_FILE}" --write-out "\n"
    curl --user "${ES_USER}":"${ES_PWD}" -X PUT "${INDEX_URL}" --write-out "\n"

    # Checks for and sets up Elasticsearch as a secondary Visibility store
    if [[ ! -z "${ES_SEC_VIS_INDEX}" ]]; then
      SEC_INDEX_URL="${ES_SERVER}/${ES_SEC_VIS_INDEX}"
      curl --user "${ES_USER}":"${ES_PWD}" -X PUT "${SEC_INDEX_URL}" --write-out "\n"
    fi
}
```

#### Update Temporal Service configuration

With the primary and secondary stores set, update the `system.secondaryVisibilityWritingMode` and
`system.enableReadFromSecondaryVisibility` configuration keys in your self-hosted Temporal Service's dynamic
configuration YAML file to enable read and/or write operations to the secondary Visibility store.

For example, to enable write operations to both primary and secondary stores, but disable reading from the secondary
store, use the following.

```yaml
system.secondaryVisibilityWritingMode:
  - value: 'dual'
    constraints: {}
system.enableReadFromSecondaryVisibility:
  - value: false
    constraints: {}
```

For details on the configuration options, see:

- [Secondary Visibility dynamic configuration reference](/references/dynamic-configuration#secondary-visibility-settings)
- [Migrating Visibility databases](#migrating-visibility-database)

## How to migrate Visibility database {/* #migrating-visibility-database */}

To migrate your Visibility database, [set up a secondary Visibility store](#dual-visibility) to enable
[Dual Visibility](/dual-visibility), and update the dynamic configuration in your Temporal Service to update the read
and write operations for the Visibility store.

Dual Visibility setup is optional but useful in gradually migrating your Visibility data to another database.

Before you begin, verify [supported databases and versions](/self-hosted-guide/visibility) for a Visibility store.

The following steps describe how to migrate your Visibility database.

After you make any changes to your [Temporal Service configuration](/temporal-service/configuration), ensure that you
restart your services.

#### Set up secondary Visibility store

1. In your Temporal Service configuration,
   [add a secondary Visibility store](/references/configuration#secondaryvisibilitystore) to your Visibility setup under
   the Persistence configuration.

   Example: To migrate from Cassandra to Elasticsearch, add Elasticsearch as your secondary database and set it up. For
   details, see [secondary Visibility database schema and setup](#dual-visibility).

   ```yaml
   persistence:
   visibilityStore: cass-visibility
   secondaryVisibilityStore: es-visibility
   datastores:
     cass-visibility:
     cassandra:
       hosts: '127.0.0.1'
       keyspace: 'temporal_visibility'
     es-visibility:
     elasticsearch:
       version: 'v7'
       logLevel: 'error'
       url:
       scheme: 'http'
       host: '127.0.0.1:9200'
       indices:
       visibility: temporal_visibility_v1_dev
       closeIdleConnectionsInterval: 15s
   ```

1. Update the [dynamic configuration](/temporal-service/configuration#dynamic-configuration) keys on your self-hosted
   Temporal Service to enable write operations to the secondary store and disable read operations. Example:

   ```yaml
   system.secondaryVisibilityWritingMode:
   - value: "dual"
   constraints: {}
   system.enableReadFromSecondaryVisibility:
   - value: false
   constraints: {}
   ```

At this point, Visibility data is read from the primary store, and all Visibility data is written to both the primary
and secondary store. This setting applies only to new Visibility data generated after Dual Visibility is enabled. It
does not migrate any existing data in the primary store to the secondary store.

For details on write options to the secondary store, see
[Secondary Visibility dynamic configuration reference](/references/dynamic-configuration#secondary-visibility-settings).

#### Run in dual mode

When you enable a secondary store, only new Visibility data is written to both primary and secondary stores. The primary
store still holds the Workflow Execution data from before the secondary store was set up.

Running in dual mode lets you plan for closed and open Workflow Executions data from before the secondary store was set
up in your self-hosted Temporal Service.

Example:

- To manage closed Workflow Executions data, run in dual mode until the Namespace
  [Retention Period](/temporal-service/temporal-server#retention-period) is reached. After the Retention Period,
  Workflow Execution data is removed from the Persistence and Visibility stores. If you want to keep the closed Workflow
  Executions data after the set Retention Period, you must set up [Archival](/self-hosted-guide/archival).
- To manage data for all open Workflow Executions, run in dual mode until all the Workflow Executions started before
  enabling Dual Visibility mode are closed. After the Workflow Executions are closed, verify the Retention Period and
  set up Archival if you need to keep the data beyond the Retention Period.

You can run your Visibility setup in dual mode for an indefinite period, or until you are ready to deprecate the primary
store and move completely to the secondary store without losing data.

#### Deprecate primary Visibility store

When you are ready to deprecate your primary store, follow these steps.

1. Update the dynamic configuration YAML to enable read operations from the secondary store. Example:

   ```yaml
   system.secondaryVisibilityWritingMode:
   - value: "dual"
   constraints: {}
   system.enableReadFromSecondaryVisibility:
   - value: true
   constraints: {}
   ```

   At this point, Visibility data is read from the secondary store only. Verify whether data on the secondary store is
   correct.

1. When the secondary store is vetted and ready to replace your current primary store, change your Temporal Service
   configuration to set the secondary store as your primary, and remove the dynamic configuration set in the previous
   steps. Example:

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
       visibility: temporal_visibility_v1_dev
       closeIdleConnectionsInterval: 15s
   ```

## Managing custom Search Attributes {/* #custom-search-attributes */}

To manage custom Search Attributes on Temporal Cloud, use the [`tcld`](/cloud/tcld/namespace#search-attributes) CLI tool.
With Temporal Cloud, you can create and rename custom Search Attributes. If you need to delete a custom Search Attribute, contact Support at [support.temporal.io](https://support.temporal.io).
To manage custom Search Attributes on a self-hosted Temporal Service, use the [Temporal CLI](/cli/command-reference/operator#search-attribute).
With a self-hosted Temporal Service, you can create and remove custom Search Attributes.

If you're self-hosting, verify whether your [Visibility database](/self-hosted-guide/visibility#supported-databases) version supports custom Search Attributes before proceeding.

:::caution Do not use sensitive data or PII in Search Attributes

Do not include sensitive data, secrets, or personally identifiable information (PII) in Search Attribute **names or values**.
Search Attribute values are stored unencrypted in the Visibility store and are not processed by a custom [Payload Codec](/payload-codec#payload-codec).
The Temporal Server must be able to read these values in plain text to support filtering and ordering, so encryption is not possible without breaking search functionality.

Attribute names are also visible in Namespace configuration, query expressions, and Temporal UI.
Using sensitive data in either names or values risks exposure to anyone with Namespace access and may violate data protection regulations such as GDPR, HIPAA, or SOC 2.

:::

### How to create custom Search Attributes {/* #create-custom-search-attributes */}

Creating a custom Search Attribute in your Visibility store makes it available to use in your Workflow metadata and
[List Filters](/list-filter).

**On Temporal Cloud**

To create custom Search Attributes on Temporal Cloud, use
[`tcld namespace search-attributes add`](/cloud/tcld/namespace/#search-attributes). For example, to add a custom Search
Attributes "CustomSA" to your Temporal Cloud Namespace "YourNamespace", run the following command.
`tcld namespace search-attributes add --namespace YourNamespace --search-attribute "CustomSA"`

**On self-hosted Temporal Service**

To create custom Search Attributes in your self-hosted Temporal Service Visibility store, use
`temporal operator search-attribute create` with `--name` and `--type` command options.

For example, to create a Search Attribute called `CustomSA` of type `Keyword`, run the following command:

```
temporal operator search-attribute create --name="CustomSA" --type="Keyword"
```

Note that if you use a SQL database with advanced Visibility capabilities, you are required to specify a Namespace when
creating a custom Search Attribute. For example:

```
temporal operator search-attribute create --name="CustomSA" --type="Keyword" --namespace="yournamespace"
```

You can also create multiple custom Search Attributes when you set up your Visibility store.

The following example shows how custom Search Attributes can be created during Visibility store setup for SQL databases.
For setup examples, refer to the [samples-server repository](https://github.com/temporalio/samples-server)

```bash
add_custom_search_attributes() {
    until temporal operator search-attribute list --namespace "${DEFAULT_NAMESPACE}"; do
      echo "Waiting for namespace cache to refresh..."
      sleep 1
    done
    echo "Namespace cache refreshed."

    echo "Adding Custom*Field search attributes."

    temporal operator search-attribute create --namespace "${DEFAULT_NAMESPACE}" --yes \
        --name="CustomKeywordField" --type="Keyword" \
        --name="CustomStringField" --type="Text" \
        --name="CustomTextField" --type="Text" \
        --name="CustomIntField" --type="Int" \
        --name="CustomDatetimeField" --type="Datetime" \
        --name="CustomDoubleField" --type="Double" \
        --name="CustomBoolField" --type="Bool"
}
```

For Temporal Server v1.19 and earlier, or if using Elasticsearch for advanced Visibility, you can create custom Search
Attributes without a Namespace association, as shown in the following example.

{/* CHECK FOR ACCURACY */}

```bash
add_custom_search_attributes() {
       echo "Adding Custom*Field search attributes."
       temporal operator search-attribute create \
        --name="CustomKeywordField" --type="Keyword" \
        --name="CustomStringField" --type="Text" \
        --name="CustomTextField" --type="Text" \
        --name="CustomIntField" --type="Int" \
        --name="CustomDatetimeField" --type="Datetime" \
        --name="CustomDoubleField" --type="Double" \
        --name="CustomBoolField" --type="Bool"
}
```

When your Visibility store is set up and running, these custom Search Attributes are available to use in your Workflow
code.

### How to remove custom Search Attributes {/* #remove-custom-search-attributes */}

To remove a Search Attribute key from your self-hosted Temporal Service Visibility store, use the command
`temporal operator search-attribute remove`. Removing Search Attributes is not supported on Temporal Cloud.

For example, if using Elasticsearch for advanced Visibility, to remove a custom Search Attribute called `CustomSA` of
type Keyword use the following command:

```
temporal operator search-attribute remove \
    --name="your_custom_attribute"
```

If you use a SQL database for advanced Visibility on Temporal Server v1.20 and later, you need to specify the Namespace
in your command, as shown in the following command:

```
temporal operator search-attribute remove \
    --name="your_custom_attribute" \
    --namespace="your_namespace"
```

To check whether the Search Attribute was removed, run

```
temporal operator search-attribute list
```

and check the list.

If you're on Temporal Server v1.20 and later, specify the Namespace from which you removed the Search Attribute. For
example,

```
temporal search-attribute list --namespace="yournamespace"
```

Note that if you use [SQL databases](/self-hosted-guide/visibility) with Temporal Server v1.20 and later, a new custom
Search Attribute is mapped to a database field name in the Visibility store `custom_search_attributes` table. Removing
this custom Search Attribute removes the mapping with the database field name but does not remove the data. If you
remove a custom Search Attribute and add a new one, the new custom Search Attribute might be mapped to the database
field of the one that was recently removed. This might cause unexpected results when you use the List API to retrieve
results using the new custom Search Attribute. These constraints do not apply if you use Elasticsearch.

---

## Quick launch - Deploying your Workers on Amazon EKS

Temporal Workers running in [Kubernetes](https://kubernetes.io)-based deployments deliver scale, resilience, and flexible resource management.
Amazon Elastic Kubernetes Service (EKS) offers one of the most popular choices for running Temporal Workers.
It integrates smoothly with AWS services and supports auto-scaling and fault tolerance.

Follow this guide to deploy and manage your Temporal Workers in EKS.
This guide walks you through writing Temporal Worker code, containerizing and publishing the Worker to the Amazon Elastic Container Registry (ECR), and deploying the worker to Amazon EKS.
The example on this page uses Temporal’s Python SDK and Temporal Cloud.

For production Kubernetes deployments that use [Worker Versioning](/production-deployment/worker-deployments/worker-versioning),
use the [Temporal Worker Controller](/production-deployment/worker-deployments/kubernetes-controller) so deployment
rollouts and autoscaling stay attached to each Worker Deployment Version.

:::tip

This guide applies to running Workers for both Temporal OSS and Temporal Cloud.
However, there are some differences when working with Temporal OSS.
For example, you'll need to use mTLS certificates instead of API keys.
You must modify your Kubernetes deployments to handle and mount the TLS certificates for your use case.
The specifics will vary depending on your deployment.

:::

## Before you begin

To get started deploying your Workers to EKS, you’ll need:

- Your Temporal Cloud account, including:
  - A Namespace using [API key authentication](/cloud/api-keys#namespace-authentication)
  - Your API Key for a [Service Account](/cloud/api-keys#generate-an-api-key-for-a-service-account)
- An AWS account, including:
  - A deployed EKS cluster within your AWS Account
- An installed version of the [`aws` CLI](https://aws.amazon.com/cli/)
- [`docker`](https://www.docker.com/get-started/)
- The [`kubectl`](https://kubernetes.io/docs/reference/kubectl/) command line tool, configured with your deployed EKS cluster

## Write your Worker code

In Temporal applications, business logic lives within your main Workflow code.
Your Worker code runs separately, and is responsible for executing your Workflows and Activities.
Make sure to configure your Worker to use environment variables so you can dynamically route your Worker to different Temporal Instances, Namespaces, and Task Queues on the fly:

```python
TEMPORAL_ADDRESS = os.environ.get("TEMPORAL_ADDRESS", "localhost:7233")
TEMPORAL_NAMESPACE = os.environ.get("TEMPORAL_NAMESPACE", "default")
TEMPORAL_TASK_QUEUE = os.environ.get("TEMPORAL_TASK_QUEUE", "test-task-queue")
TEMPORAL_API_KEY = os.environ.get("TEMPORAL_API_KEY", "")
```

After configuration, instantiate your Temporal client:

```python
client = await Client.connect(
    TEMPORAL_ADDRESS,
    namespace=TEMPORAL_NAMESPACE,
    rpc_metadata={"temporal-namespace": TEMPORAL_NAMESPACE},
    api_key=TEMPORAL_API_KEY,
    tls=True
)
```

Here is a complete Python boilerplate that showcases how to instantiate a Client and pass it to the Worker before starting the Worker execution:

```python

from temporalio.worker import Worker
from temporalio.client import Client

from workflows import your_workflow
from activities import your_first_activity, your_second_activity, your_third_activity

TEMPORAL_ADDRESS = os.environ.get("TEMPORAL_ADDRESS", "localhost:7233")
TEMPORAL_NAMESPACE = os.environ.get("TEMPORAL_NAMESPACE", "default")
TEMPORAL_TASK_QUEUE = os.environ.get("TEMPORAL_TASK_QUEUE", "test-task-queue")
TEMPORAL_API_KEY = os.environ.get("TEMPORAL_API_KEY", "your-api-key")

async def main():
  client = await Client.connect(
    TEMPORAL_ADDRESS,
    namespace=TEMPORAL_NAMESPACE,
    rpc_metadata={"temporal-namespace": TEMPORAL_NAMESPACE},
    api_key=TEMPORAL_API_KEY,
    tls=True
  )

  print("Initializing worker...")

  # Run the worker
  worker = Worker(
    client,
    task_queue=TEMPORAL_TASK_QUEUE,
    workflows=[your_workflow],
    activities=[
      your_first_activity,
      your_second_activity,
      your_third_activity
    ]
  )

  print("Starting worker... Waiting for tasks.")
  await worker.run()

if __name__ == "__main__":
  asyncio.run(main())
```

## Containerize the Worker for Kubernetes

You need to containerize your Worker code to run it with Kubernetes.
Here is a sample Python Dockerfile, complete with the Temporal Python SDK installed:

```docker
