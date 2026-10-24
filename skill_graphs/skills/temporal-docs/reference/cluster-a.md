# cluster A
clusterMetadata:
  enableGlobalNamespace: true
  failoverVersionIncrement: 100
  masterClusterName: "clusterA"
  currentClusterName: "clusterA"
  clusterInformation:
    clusterA:
      enabled: true
      initialFailoverVersion: 1
      rpcAddress: "127.0.0.1:7233"
    clusterB:
      enabled: true
      initialFailoverVersion: 2
      rpcAddress: "127.0.0.1:8233"
