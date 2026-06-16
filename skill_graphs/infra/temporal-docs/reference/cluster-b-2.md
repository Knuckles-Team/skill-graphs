# cluster B
clusterMetadata:
  enableGlobalNamespace: true
  failoverVersionIncrement: 100
  masterClusterName: "clusterB"
  currentClusterName: "clusterB"
  clusterInformation:
    clusterB:
      enabled: true
      initialFailoverVersion: 2
      rpcAddress: "127.0.0.1:8233"
```

Then you can use the Temporal CLI tool to add cluster connections. All operations should be executed in both Clusters.

{/* tctl -address 127.0.0.1:7233 admin cluster upsert-remote-cluster --frontend_address "localhost:8233" */}

{/* tctl -address 127.0.0.1:8233 admin cluster upsert-remote-cluster --frontend_address "localhost:7233" */}

{/* tctl -address 127.0.0.1:7233 admin cluster upsert-remote-cluster --frontend_address "localhost:8233" --enable_connection false
tctl -address 127.0.0.1:8233 admin cluster upsert-remote-cluster --frontend_address "localhost:7233" --enable_connection false */}

{/* tctl -address 127.0.0.1:7233 admin cluster remove-remote-cluster --cluster "clusterB"
tctl -address 127.0.0.1:8233 admin cluster remove-remote-cluster --cluster "clusterA" */}

{/* THIS MUST BE CHECKED FOR ACCURACY */}

```shell
