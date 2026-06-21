
Note: `certFile` and `keyFile` are optional depending on server config, but both fields must be omitted to avoid using a client certificate.

## log

The `log` section is optional and contains the following possible values:

- `stdout` - _boolean_ - `true` if the output needs to go to standard out.
- `level` - sets the logging level.
  - _Valid values_ - debug, info, warn, error or fatal, default to info.
- `outputFile` - path to output log file.

## clusterMetadata

`clusterMetadata` contains the local cluster information. The information is used in [Multi-Cluster Replication](/temporal-service/multi-cluster-replication).

An example `clusterMetadata` section:

```yaml
clusterMetadata:
  enableGlobalNamespace: true
  failoverVersionIncrement: 10
  masterClusterName: 'active'
  currentClusterName: 'active'
  clusterInformation:
    active:
      enabled: true
      initialFailoverVersion: 0
      rpcAddress: '127.0.0.1:7233'
  #replicationConsumer:
  #type: kafka
```

- `currentClusterName` - _required_ - the name of the current cluster. **Warning:** This value is immutable and will be ignored after the first run.
- `enableGlobalNamespace` - _Default:_ `false`.
- `replicationConsumer` - determines which method to use to consume replication tasks. The type may be either `kafka` or `rpc`.
- `failoverVersionIncrement` - the increment of each cluster version when failover happens.
- `masterClusterName` - the master cluster name, only the master cluster can register/update namespace. All clusters can do namespace failover.
- `clusterInformation` - contains the local cluster name to `ClusterInformation` definition. The local cluster name should be consistent with `currentClusterName`. `ClusterInformation` sections consist of:
  - `enabled` - _boolean_ - whether a remote cluster is enabled for replication.
  - `initialFailoverVersion`
  - `rpcAddress` - indicate the remote service address (host:port). Host can be DNS name. Use `dns:///` prefix to enable round-robin between IP address for DNS name.

## services

The `services` section contains configuration keyed by service role type.
There are four supported service roles:

- `frontend`
- `matching`
- `worker`
- `history`

Below is a minimal example of a `frontend` service definition under `services`:

```yaml
services:
  frontend:
    rpc:
      grpcPort: 8233
      membershipPort: 8933
      bindOnIP: '0.0.0.0'
```

There are two sections defined under each service heading:

### rpc

_Required_

`rpc` contains settings related to the way a service interacts with other services. The following values are supported:

- `grpcPort`: Port on which gRPC will listen.
- `membershipPort`: Port used to communicate with other hosts in the same Cluster for membership info.
  Each service should use different port.
  If there are multiple Temporal Clusters in your environment (Kubernetes for example), and they have network access to each other, each Cluster should use a different membership port.
- `bindOnLocalHost`: Determines whether uses `127.0.0.1` as the listener address.
- `bindOnIP`: Used to bind service on specific IP, or `0.0.0.0`.
  Check `net.ParseIP` for supported syntax, only IPv4 is supported, mutually exclusive with `BindOnLocalHost` option.

**Note:** Port values are currently expected to be consistent among role types across all hosts.

## publicClient

The `publicClient` is a required section describing the configuration needed for a worker to connect to Temporal server for background server maintenance.

- `hostPort` IPv4 host port or DNS name to reach Temporal frontend, [reference](https://github.com/grpc/grpc/blob/master/doc/naming.md)

Example:

```yaml
publicClient:
  hostPort: 'localhost:8933'
```

Use `dns:///` prefix to enable round-robin between IP address for DNS name.

## archival

_Optional_

Archival is an optional configuration needed to set up the [Archival store](/temporal-service/archival).
It can be enabled on `history` and `visibility` data.

The following list describes supported values for each configuration on the `history` and `visibility` data.

- `state`: State for Archival setting. Supported values are `enabled`, `disabled`. This value must be `enabled` to use Archival with any Namespace in your Cluster.
  - `enabled`: Enables Archival in your Cluster setup. When set to `enabled`, `URI` and `namespaceDefaults` values must be provided.
  - `disabled`: Disables Archival in your Cluster setup. When set to `disabled`, the `enableRead` value must be set to `false`, and under `namespaceDefaults`, `state` must be set to `disabled`, with no values set for `provider` and `URI` fields.
- `enableRead`: Supported values are `true` or `false`. Set to `true` to allow read operations from the archived Event History data.
- `provider`: Location where data should be archived. Subprovider configs are `filestore`, `gstorage`, `s3`, or `your_custom_provider`. Default configuration specifies `filestore`.

Example:

- To enable Archival in your Cluster configuration:

  ```yaml
  # Cluster-level Archival config enabled
  archival:
    # Event History configuration
    history:
      # Archival is enabled for the History Service data.
      state: 'enabled'
      enableRead: true
      # Namespaces can use either the local filestore provider or the Google Cloud provider.
      provider:
        filestore:
          fileMode: '0666'
          dirMode: '0766'
        gstorage:
          credentialsPath: '/tmp/gcloud/keyfile.json'
    # Configuration for archiving Visibility data.
    visibility:
      # Archival is enabled for Visibility data.
      state: 'enabled'
      enableRead: true
      provider:
        filestore:
          fileMode: '0666'
          dirMode: '0766'
  ```

- To disable Archival in your Cluster configuration:

  ```yaml
  # Cluster-level Archival config disabled
  archival:
    history:
      state: 'disabled'
      enableRead: false
    visibility:
      state: 'disabled'
      enableRead: false

  namespaceDefaults:
    archival:
      history:
        state: 'disabled'
      visibility:
        state: 'disabled'
  ```

For more details on Archival setup, see [Set up Archival](/self-hosted-guide/archival#set-up-archival).

## namespaceDefaults

_Optional_

Sets default Archival configuration for each Namespace using `namespaceDefaults` for `history` and `visibility` data.

- `state`: Default state of the Archival for the Namespace. Supported values are `enabled` or `disabled`.
- `URI`: Default URI for the Namespace.

For more details on setting Namespace defaults on Archival, see [Create an Archiving Namespace in Archival setup](/self-hosted-guide/archival#create-an-archiving-namespace)

Example:

```yaml
