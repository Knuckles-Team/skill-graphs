# cluster B
clusterMetadata:
  enableGlobalNamespace: true
  failoverVersionIncrement: 100
  masterClusterName: "clusterA"
  currentClusterName: "clusterB"
  clusterInformation:
    clusterA:
      enabled: true
      initialFailoverVersion: 1
      rpcAddress: "127.0.0.1:7233"
    clusterB:
      enabled: true
      initialFailoverVersion: 2
      rpcAddress: "127.0.0.1:8233"
```

#### Set up Multi-Cluster Replication in v1.14 and later

You still need to set up local cluster [`clusterMetadata` configuration](/references/configuration#clustermetadata)

For example:

```yaml
