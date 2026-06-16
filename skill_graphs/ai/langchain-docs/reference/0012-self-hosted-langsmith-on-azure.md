# Self-hosted LangSmith on Azure
Source: https://docs.langchain.com/langsmith/azure-self-hosted

When running LangSmith on [Microsoft Azure](https://azure.microsoft.com/), [self-hosted](/langsmith/self-hosted) mode deploys a complete LangSmith platform with observability functionality.

This page provides:

* [Initial setup steps](#initial-setup) for deploying to AKS, configuring managed services, and setting up authentication.
* [Azure-specific architecture patterns](#reference-architecture) and reference diagrams.
* [Compute and networking guidance](#compute-and-networking-on-azure) and best practices.
* [Security and access control](#security-and-access-control) recommendations for Azure deployments.

<Note>
  LangChain provides Terraform modules specifically for Azure to help provision infrastructure for LangSmith. These modules can quickly set up AKS clusters, Azure Database for PostgreSQL, Azure Managed Redis, Blob Storage, and networking resources.

  View the [Azure Terraform modules](https://github.com/langchain-ai/terraform/tree/main/modules/azure) for documentation and examples.
</Note>

## Initial setup

<Steps>
  <Step title="Deploy to Kubernetes">
    Follow the [Kubernetes installation guide](/langsmith/kubernetes). LangSmith is tested on Azure Kubernetes Service (AKS).

    **AKS-specific notes:**

    * LangSmith works with standard AKS clusters
    * Use Azure Disk storage class for persistent volumes
  </Step>

  <Step title="Configure external services">
    For production deployments, connect to Azure managed services:

    <CardGroup>
      <Card title="Azure Blob Storage" icon="database" href="/langsmith/self-host-blob-storage#azure-blob-storage">
        Store trace data in Azure Blob
      </Card>

      <Card title="Azure Database" icon="database" href="/langsmith/self-host-external-postgres#azure-database-for-postgresql">
        PostgreSQL database
      </Card>

      <Card title="Azure Cache" icon="cpu" href="/langsmith/self-host-external-redis#azure-cache-for-redis">
        Redis for caching
      </Card>

      <Card title="ClickHouse Cloud" icon="chart-line" href="/langsmith/self-host-external-clickhouse">
        Analytics database
      </Card>
    </CardGroup>
  </Step>

  <Step title="Set up authentication">
    Use [Azure Workload Identity](https://azure.github.io/azure-workload-identity/docs/introduction.html) to authenticate LangSmith pods to Azure services.

    **Key pages:**

    * [Azure Blob managed identity](/langsmith/self-host-blob-storage#azure-blob-storage)
    * [Azure Database Entra authentication](/langsmith/self-host-external-postgres#iam-authentication)
    * [Azure Cache Entra authentication](/langsmith/self-host-external-redis#iam-authentication)
  </Step>
</Steps>

After completing these initial setup steps, you can review the complete Azure architecture and best practices below.

## Reference architecture

We recommend using Azure's managed services to provide a scalable, secure, and resilient platform. The following architecture applies to both self-hosted and hybrid deployments.

|                            | Components                                                                                                              | How it's installed                                                                                                                   |
| -------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| **LangSmith Helm release** | Frontend, backend, queue, platform backend, Playground, ACE, and optionally the LangSmith Deployment control/data plane | One `helm upgrade --install` from the [`langchain/langsmith`](https://github.com/langchain-ai/helm/tree/main/charts/langsmith) chart |
| **You provision**          | AKS, PostgreSQL, Managed Redis, Blob Storage, Key Vault, ingress, and ClickHouse                                        | Your IaC tooling (Terraform, ARM templates, or Azure portal) before installing LangSmith                                             |

<img alt="Architecture diagram showing Azure relations to LangSmith services" />

<img alt="Architecture diagram showing Azure relations to LangSmith services" />

**Installation order:** provision Azure infrastructure → provision or subscribe to ClickHouse → configure Entra ID and Workload Identity → run `helm upgrade --install`. LangSmith Deployment, Fleet, Insights, and Chat are enabled through the same Helm release, not as separate installs.

**Compliance surface:** one application review for the LangSmith chart and its container images, plus standard Azure service reviews for each managed resource. ClickHouse Cloud adds one third-party SaaS review.

* **Client interfaces**: Users interact with LangSmith via a web browser or the LangChain SDK. All traffic terminates at an [Azure Load Balancer](https://azure.microsoft.com/en-us/products/load-balancer/) and is routed to the frontend (NGINX) within the [AKS](https://azure.microsoft.com/en-us/products/kubernetes-service/) cluster before being routed to another service within the cluster if necessary.
* **Storage services**: The platform requires persistent storage for traces, metadata and caching. On Azure the recommended services are:
  * <Icon icon="database" /> **[Azure Database for PostgreSQL (Flexible Server)](https://azure.microsoft.com/en-us/products/postgresql/)** for transactional data (e.g., runs, projects). Azure's high-availability options provision a standby replica in another zone; data is synchronously committed to both primary and standby servers. LangSmith requires PostgreSQL version 14 or higher.
  * <Icon icon="database" /> **[Azure Managed Redis](https://azure.microsoft.com/en-us/products/managed-redis/)** for queues and caching. Best practices include storing small values and breaking large objects into multiple keys, using pipelining to maximize throughput and ensuring the client and server reside in the same region. You can also use [Azure Cache for Redis](https://azure.microsoft.com/en-us/products/cache), running either in single-instance or cluster mode. LangSmith requires Redis OSS version 5 or higher.
  * <Icon icon="chart-line" /> **ClickHouse** for high-volume analytics of traces. We recommend using an [externally managed ClickHouse solution](/langsmith/self-host-external-clickhouse). If, for security or compliance reasons, that is not an option, deploy a ClickHouse cluster on AKS using the open-source operator. Ensure replication across [availability zones](https://learn.microsoft.com/en-us/azure/reliability/availability-zones-overview) for durability. Clickhouse is not required for a hybrid deployment.
  * <Icon icon="cube" /> **[Azure Blob Storage](https://azure.microsoft.com/en-us/products/storage/blobs/)** for large artifacts. Use redundant storage configurations such as read-access geo-redundant (RA-GRS) or geo-zone-redundant (RA-GZRS) storage and design applications to read from the secondary region during an outage.

## Compute and networking on Azure

### Azure Kubernetes Service (AKS)

[AKS](https://azure.microsoft.com/en-us/products/kubernetes-service/) is the recommended compute platform for production deployments. This section outlines the key considerations for planning your setup.

#### Network model

Use [Azure CNI](https://learn.microsoft.com/en-us/azure/aks/configure-azure-cni) networking for production clusters. This model integrates the cluster into an existing virtual network, assigns IP addresses to each pod and node, and allows direct connectivity to on-premises or other Azure services. Ensure the subnet has enough IPs for nodes and pods, avoid overlapping address ranges and allocate additional IP space for scale-out events.

#### Ingress and load balancing

Use Kubernetes Ingress resources and controllers to distribute HTTP/HTTPS traffic. Ingress controllers operate at layer 7 and can route traffic based on URL paths and handle TLS termination. They reduce the number of public IP addresses compared to layer-4 load balancers. Use the [application routing add-on](https://learn.microsoft.com/en-us/azure/aks/app-routing) for managed NGINX ingress controllers integrated with [Azure DNS](https://azure.microsoft.com/en-us/products/dns/) and [Key Vault](https://azure.microsoft.com/en-us/products/key-vault/) for SSL certificates.

#### Web Application Firewall (WAF)

For additional protection against attacks, deploy a [WAF](https://learn.microsoft.com/en-us/azure/web-application-firewall/overview) such as [Azure Application Gateway](https://azure.microsoft.com/en-us/products/application-gateway/). A WAF filters traffic using OWASP rules and can terminate TLS before the traffic reaches your AKS cluster.

#### Network policies

Apply [Kubernetes network policies](https://learn.microsoft.com/en-us/azure/aks/use-network-policies) to restrict pod-to-pod traffic and reduce the impact of compromised workloads. Enable network policy support when creating the cluster and design rules based on application connectivity.

#### High availability

Configure node pools across [availability zones](https://learn.microsoft.com/en-us/azure/reliability/availability-zones-overview) and use Pod Disruption Budgets (PDB) and multiple replicas for all deployments. Set pod resource requests and limits; the [AKS resource management best practices](https://learn.microsoft.com/en-us/azure/aks/developer-best-practices-resource-management) recommend setting CPU and memory limits to prevent pods from consuming all resources. Use [Cluster Autoscaler](https://learn.microsoft.com/en-us/azure/aks/cluster-autoscaler) and [Vertical Pod Autoscaler](https://learn.microsoft.com/en-us/azure/aks/vertical-pod-autoscaler) to scale node pools and adjust pod resources automatically.

### Networking and identity

#### Virtual network integration

Deploy AKS into its own [virtual network](https://azure.microsoft.com/en-us/products/virtual-network/) and create separate subnets for the cluster, database, Redis, and storage endpoints. Use [Private Link](https://azure.microsoft.com/en-us/products/private-link/) and [service endpoints](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-service-endpoints-overview) to keep traffic within your virtual network and avoid exposure to the public internet.

#### Authentication

Integrate LangSmith with [Microsoft Entra ID](https://www.microsoft.com/en-us/security/business/identity-access/microsoft-entra-id) (Azure AD) for single sign-on. Use Azure AD OAuth2 for bearer tokens and assign roles to control access to the UI and API.

## Storage and data services

### Azure Database for PostgreSQL

#### High availability

Use [Flexible Server](https://learn.microsoft.com/en-us/azure/postgresql/flexible-server/overview) with high-availability mode. Azure provisions a standby replica either within the same availability zone (zonal) or across zones (zone-redundant). Data is synchronously committed to both the primary and standby servers, ensuring that committed data is not lost. Zone-redundant configurations place the standby in a different zone to protect against zone outages but may add write latency.

#### Backups and disaster recovery

Enable [automatic backups](https://learn.microsoft.com/en-us/azure/postgresql/flexible-server/concepts-backup-restore) and configure geo-redundant backup storage to protect against region-wide outages. For critical applications, create read replicas in a secondary region.

#### Scaling

Choose an appropriate SKU that matches your workload; Flexible Server allows scaling compute and storage independently. Monitor metrics and configure alerts through [Azure Monitor](https://azure.microsoft.com/en-us/products/monitor/).

### Azure Managed Redis

#### Persistence and redundancy

Choose a tier that provides replication and persistence. Configure Redis persistence or data backup for durability. For high-availability, use [active geo-replication](https://learn.microsoft.com/en-us/azure/redis/how-to-active-geo-replication) or zone-redundant caches depending on the tier.

### ClickHouse on Azure

ClickHouse is used for analytical workloads (traces and feedback). If you cannot use an externally managed solution, deploy a ClickHouse cluster on AKS using Helm or the official operator. For resilience, replicate data across nodes and availability zones. Consider using [Azure Disks](https://azure.microsoft.com/en-us/products/storage/disks/) for local storage and mount them as StatefulSets.

### Azure Blob Storage

#### Redundancy

Choose a redundancy configuration based on your recovery objectives. Use [read-access geo-redundant (RA-GRS) or geo-zone-redundant (RA-GZRS) storage](https://learn.microsoft.com/en-us/azure/storage/common/storage-redundancy) and design applications to switch reads to the secondary region during a primary region outage.

#### Naming and partitioning

Use naming conventions that improve load balancing across partitions and plan for the maximum number of concurrent clients. Stay within Azure's scalability and capacity targets and partition data across multiple storage accounts if necessary.

#### Networking

Access blob storage through [private endpoints](https://learn.microsoft.com/en-us/azure/storage/common/storage-private-endpoints) or by using SAS tokens and CORS rules to enable direct client access.

## Security and access control

### Azure Key Vault

#### Separate vaults per application and environment

Store secrets such as database connection strings and API keys in [Azure Key Vault](https://azure.microsoft.com/en-us/products/key-vault/). Use a dedicated vault for each application and environment (dev, test, prod) to limit the impact of a security breach.

#### Access control

Use the [RBAC permission model](https://learn.microsoft.com/en-us/azure/key-vault/general/rbac-guide) to assign roles at the vault scope and restrict access to required principals. Restrict network access using Private Link and firewalls.

#### Data protection and logging

Enable [soft delete and purge protection](https://learn.microsoft.com/en-us/azure/key-vault/general/soft-delete-overview) to prevent accidental deletion. Turn on logging and configure alerts for Key Vault access events.

### Network security

#### Ingress isolation

Expose only the frontend service through the ingress controller or WAF. Other services should be internal and communicate through cluster networking.

#### RBAC and pod security

Use [Kubernetes RBAC](https://kubernetes.io/docs/reference/access-authn-authz/rbac/) to control who can deploy, modify, or read resources. Enable [pod security admission](https://kubernetes.io/docs/concepts/security/pod-security-admission/) to enforce baseline, restricted, or privileged profiles.

#### Secrets management

Mount secrets from Key Vault into pods using [CSI Secret Store](https://learn.microsoft.com/en-us/azure/aks/csi-secrets-store-driver). Avoid storing secrets in environment variables or configuration files.

## Observability and monitoring

Configure your LangSmith instance to [export telemetry data](/langsmith/export-backend) so you can use Azure's services to monitor it.

### Azure Monitor

Use [Azure Monitor](https://azure.microsoft.com/en-us/products/monitor/) for metrics, logs, and alerting. Proactive monitoring involves configuring alerts on key signals like node CPU/memory utilization, pod status, and service latency. Azure Monitor alerts notify you when predefined thresholds are exceeded.

### Managed Prometheus and Grafana

Enable [Azure Monitor managed Prometheus](https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/prometheus-metrics-overview) to collect Kubernetes metrics. Combine it with [Grafana dashboards](https://azure.microsoft.com/en-us/products/managed-grafana/) for visualization. Define service-level objectives (SLOs) and configure alerts accordingly.

### Container Insights

Install [Container Insights](https://learn.microsoft.com/en-us/azure/azure-monitor/containers/container-insights-overview) to capture logs and metrics from AKS nodes and pods. Use [Azure Log Analytics workspaces](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/log-analytics-overview) to query and analyze logs.

### Application logging

Ensure LangSmith services emit logs to stdout/stderr and forward them via [Fluent Bit](https://fluentbit.io/) or the Azure Monitor agent.

## Continuous integration

* The preferred method to manage [LangSmith deployments](/langsmith/deployment) is to create a CI process that builds [Agent Server](/langsmith/agent-server) images and pushes them to [Azure Container Registry](https://azure.microsoft.com/en-us/products/container-registry). Create a test deployment for pull requests before deploying a new revision to staging or production upon PR merge.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/azure-self-hosted.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# How to kick off background runs
Source: https://docs.langchain.com/langsmith/background-run

This guide covers how to kick off background runs for your agent.
This can be useful for long running jobs.

## Setup

First let's set up our client and thread:

<Tabs>
  <Tab title="Python">
    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    from langgraph_sdk import get_client

    client = get_client(url=<DEPLOYMENT_URL>)
    # Using the graph deployed with the name "agent"
    assistant_id = "agent"
    # create thread
    thread = await client.threads.create()
    print(thread)
    ```
  </Tab>

  <Tab title="Javascript">
    ```js theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    import { Client } from "@langchain/langgraph-sdk";

    const client = new Client({ apiUrl: <DEPLOYMENT_URL> });
    // Using the graph deployed with the name "agent"
    const assistantID = "agent";
    // create thread
    const thread = await client.threads.create();
    console.log(thread);
    ```
  </Tab>

  <Tab title="CURL">
    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    curl --request POST \
      --url <DEPLOYMENT_URL>/threads \
      --header 'Content-Type: application/json' \
      --data '{}'
    ```
  </Tab>
</Tabs>

Output:

```
{
'thread_id': '5cb1e8a1-34b3-4a61-a34e-71a9799bd00d',
'created_at': '2024-08-30T20:35:52.062934+00:00',
'updated_at': '2024-08-30T20:35:52.062934+00:00',
'metadata': {},
'status': 'idle',
'config': {},
'values': None
}
```

## Check runs on thread

If we list the current runs on this thread, we will see that it's empty:

<Tabs>
  <Tab title="Python">
    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    runs = await client.runs.list(thread["thread_id"])
    print(runs)
    ```
  </Tab>

  <Tab title="Javascript">
    ```js theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    let runs = await client.runs.list(thread['thread_id']);
    console.log(runs);
    ```
  </Tab>

  <Tab title="CURL">
    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    curl --request GET \
        --url <DEPLOYMENT_URL>/threads/<THREAD_ID>/runs
    ```
  </Tab>
</Tabs>

Output:

```
[]
```

## Start runs on thread

Now let's kick off a run:

<Tabs>
  <Tab title="Python">
    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    input = {"messages": [{"role": "user", "content": "what's the weather in sf"}]}
    run = await client.runs.create(thread["thread_id"], assistant_id, input=input)
    ```
  </Tab>

  <Tab title="Javascript">
    ```js theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    let input = {"messages": [{"role": "user", "content": "what's the weather in sf"}]};
    let run = await client.runs.create(thread["thread_id"], assistantID, { input });
    ```
  </Tab>

  <Tab title="CURL">
    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    curl --request POST \
        --url <DEPLOYMENT_URL>/threads/<THREAD_ID>/runs \
        --header 'Content-Type: application/json' \
        --data '{
            "assistant_id": <ASSISTANT_ID>
        }'
    ```
  </Tab>
</Tabs>

The first time we poll it, we can see `status=pending`:

<Tabs>
  <Tab title="Python">
    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    print(await client.runs.get(thread["thread_id"], run["run_id"]))
    ```
  </Tab>

  <Tab title="Javascript">
    ```js theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    console.log(await client.runs.get(thread["thread_id"], run["run_id"]));
    ```
  </Tab>

  <Tab title="CURL">
    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    curl --request GET \
        --url <DEPLOYMENT_URL>/threads/<THREAD_ID>/runs/<RUN_ID>
    ```
  </Tab>
</Tabs>

Output:

```
{
"run_id": "1ef6a5f8-bd86-6763-bbd6-bff042db7b1b",
"thread_id": "7885f0cf-94ad-4040-91d7-73f7ba007c8a",
"assistant_id": "fe096781-5601-53d2-b2f6-0d3403f7e9ca",
"created_at": "2024-09-04T01:46:47.244887+00:00",
"updated_at": "2024-09-04T01:46:47.244887+00:00",
"metadata": {},
"status": "pending",
"kwargs": {
"input": {
"messages": [
{
"role": "user",
"content": "what's the weather in sf"
}
]
},
"config": {
"metadata": {
"created_by": "system"
},
"configurable": {
"run_id": "1ef6a5f8-bd86-6763-bbd6-bff042db7b1b",
"user_id": "",
"graph_id": "agent",
"thread_id": "7885f0cf-94ad-4040-91d7-73f7ba007c8a",
"assistant_id": "fe096781-5601-53d2-b2f6-0d3403f7e9ca",
"checkpoint_id": null
}
},
"webhook": null,
"temporary": false,
"stream_mode": [
"values"
],
"feedback_keys": null,
"interrupt_after": null,
"interrupt_before": null
},
"multitask_strategy": "reject"
}
```

Now we can join the run, wait for it to finish and check that status again:

<Tabs>
  <Tab title="Python">
    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    await client.runs.join(thread["thread_id"], run["run_id"])
    print(await client.runs.get(thread["thread_id"], run["run_id"]))
    ```
  </Tab>

  <Tab title="Javascript">
    ```js theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    await client.runs.join(thread["thread_id"], run["run_id"]);
    console.log(await client.runs.get(thread["thread_id"], run["run_id"]));
    ```
  </Tab>

  <Tab title="CURL">
    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    curl --request GET \
        --url <DEPLOYMENT_URL>/threads/<THREAD_ID>/runs/<RUN_ID>/join &&
    curl --request GET \
        --url <DEPLOYMENT_URL>/threads/<THREAD_ID>/runs/<RUN_ID>
    ```
  </Tab>
</Tabs>

Output:

```
{
"run_id": "1ef6a5f8-bd86-6763-bbd6-bff042db7b1b",
"thread_id": "7885f0cf-94ad-4040-91d7-73f7ba007c8a",
"assistant_id": "fe096781-5601-53d2-b2f6-0d3403f7e9ca",
"created_at": "2024-09-04T01:46:47.244887+00:00",
"updated_at": "2024-09-04T01:46:47.244887+00:00",
"metadata": {},
"status": "success",
"kwargs": {
"input": {
"messages": [
{
"role": "user",
"content": "what's the weather in sf"
}
]
},
"config": {
"metadata": {
"created_by": "system"
},
"configurable": {
"run_id": "1ef6a5f8-bd86-6763-bbd6-bff042db7b1b",
"user_id": "",
"graph_id": "agent",
"thread_id": "7885f0cf-94ad-4040-91d7-73f7ba007c8a",
"assistant_id": "fe096781-5601-53d2-b2f6-0d3403f7e9ca",
"checkpoint_id": null
}
},
"webhook": null,
"temporary": false,
"stream_mode": [
"values"
],
"feedback_keys": null,
"interrupt_after": null,
"interrupt_before": null
},
"multitask_strategy": "reject"
}
```

Perfect! The run succeeded as we would expect. We can double check that the run worked as expected by printing out the final state:

<Tabs>
  <Tab title="Python">
    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    final_result = await client.threads.get_state(thread["thread_id"])
    print(final_result)
    ```
  </Tab>

  <Tab title="Javascript">
    ```js theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    let finalResult = await client.threads.getState(thread["thread_id"]);
    console.log(finalResult);
    ```
  </Tab>

  <Tab title="CURL">
    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    curl --request GET \
        --url <DEPLOYMENT_URL>/threads/<THREAD_ID>/state
    ```
  </Tab>
</Tabs>

Output:

```
{
"values": {
"messages": [
{
"content": "what's the weather in sf",
"additional_kwargs": {},
"response_metadata": {},
"type": "human",
"name": null,
"id": "beba31bf-320d-4125-9c37-cadf526ac47a",
"example": false
},
{
"content": [
{
"id": "toolu_01AaNPSPzqia21v7aAKwbKYm",
"input": {},
"name": "tavily_search_results_json",
"type": "tool_use",
"index": 0,
"partial_json": "{\"query\": \"weather in san francisco\"}"
}
],
"additional_kwargs": {},
"response_metadata": {
"stop_reason": "tool_use",
"stop_sequence": null
},
"type": "ai",
"name": null,
"id": "run-f220faf8-1d27-4f73-ad91-6bb3f47e8639",
"example": false,
"tool_calls": [
{
"name": "tavily_search_results_json",
"args": {
"query": "weather in san francisco"
},
"id": "toolu_01AaNPSPzqia21v7aAKwbKYm",
"type": "tool_call"
}
],
"invalid_tool_calls": [],
"usage_metadata": {
"input_tokens": 273,
"output_tokens": 61,
"total_tokens": 334
}
},
{
"content": "[{\"url\": \"https://www.weatherapi.com/\", \"content\": \"{'location': {'name': 'San Francisco', 'region': 'California', 'country': 'United States of America', 'lat': 37.78, 'lon': -122.42, 'tz_id': 'America/Los_Angeles', 'localtime_epoch': 1725052131, 'localtime': '2024-08-30 14:08'}, 'current': {'last_updated_epoch': 1725051600, 'last_updated': '2024-08-30 14:00', 'temp_c': 21.1, 'temp_f': 70.0, 'is_day': 1, 'condition': {'text': 'Partly cloudy', 'icon': '//cdn.weatherapi.com/weather/64x64/day/116.png', 'code': 1003}, 'wind_mph': 11.9, 'wind_kph': 19.1, 'wind_degree': 290, 'wind_dir': 'WNW', 'pressure_mb': 1018.0, 'pressure_in': 30.07, 'precip_mm': 0.0, 'precip_in': 0.0, 'humidity': 59, 'cloud': 25, 'feelslike_c': 21.1, 'feelslike_f': 70.0, 'windchill_c': 18.6, 'windchill_f': 65.5, 'heatindex_c': 18.6, 'heatindex_f': 65.5, 'dewpoint_c': 12.2, 'dewpoint_f': 54.0, 'vis_km': 16.0, 'vis_miles': 9.0, 'uv': 5.0, 'gust_mph': 15.0, 'gust_kph': 24.2}}\"}]",
"additional_kwargs": {},
"response_metadata": {},
"type": "tool",
"name": "tavily_search_results_json",
"id": "686b2487-f332-4e58-9508-89b3a814cd81",
"tool_call_id": "toolu_01AaNPSPzqia21v7aAKwbKYm",
"artifact": {
"query": "weather in san francisco",
"follow_up_questions": null,
"answer": null,
"images": [],
"results": [
{
"title": "Weather in San Francisco",
"url": "https://www.weatherapi.com/",
"content": "{'location': {'name': 'San Francisco', 'region': 'California', 'country': 'United States of America', 'lat': 37.78, 'lon': -122.42, 'tz_id': 'America/Los_Angeles', 'localtime_epoch': 1725052131, 'localtime': '2024-08-30 14:08'}, 'current': {'last_updated_epoch': 1725051600, 'last_updated': '2024-08-30 14:00', 'temp_c': 21.1, 'temp_f': 70.0, 'is_day': 1, 'condition': {'text': 'Partly cloudy', 'icon': '//cdn.weatherapi.com/weather/64x64/day/116.png', 'code': 1003}, 'wind_mph': 11.9, 'wind_kph': 19.1, 'wind_degree': 290, 'wind_dir': 'WNW', 'pressure_mb': 1018.0, 'pressure_in': 30.07, 'precip_mm': 0.0, 'precip_in': 0.0, 'humidity': 59, 'cloud': 25, 'feelslike_c': 21.1, 'feelslike_f': 70.0, 'windchill_c': 18.6, 'windchill_f': 65.5, 'heatindex_c': 18.6, 'heatindex_f': 65.5, 'dewpoint_c': 12.2, 'dewpoint_f': 54.0, 'vis_km': 16.0, 'vis_miles': 9.0, 'uv': 5.0, 'gust_mph': 15.0, 'gust_kph': 24.2}}",
"score": 0.976148,
"raw_content": null
}
],
"response_time": 3.07
},
"status": "success"
},
{
"content": [
{
"text": "\n\nThe search results provide the current weather conditions in San Francisco. According to the data, as of 2:00 PM on August 30, 2024, the temperature in San Francisco is 70\u00b0F (21.1\u00b0C) with partly cloudy skies. The wind is blowing from the west-northwest at around 12 mph (19 km/h). The humidity is 59% and visibility is 9 miles (16 km). Overall, it looks like a nice late summer day in San Francisco with comfortable temperatures and partly sunny conditions.",
"type": "text",
"index": 0
}
],
"additional_kwargs": {},
"response_metadata": {
"stop_reason": "end_turn",
"stop_sequence": null
},
"type": "ai",
"name": null,
"id": "run-8fecc61d-3d9f-4e16-8e8a-92f702be498a",
"example": false,
"tool_calls": [],
"invalid_tool_calls": [],
"usage_metadata": {
"input_tokens": 837,
"output_tokens": 124,
"total_tokens": 961
}
}
]
},
"next": [],
"tasks": [],
"metadata": {
"step": 3,
"run_id": "1ef67140-eb23-684b-8253-91d4c90bb05e",
"source": "loop",
"writes": {
"agent": {
"messages": [
{
"id": "run-8fecc61d-3d9f-4e16-8e8a-92f702be498a",
"name": null,
"type": "ai",
"content": [
{
"text": "\n\nThe search results provide the current weather conditions in San Francisco. According to the data, as of 2:00 PM on August 30, 2024, the temperature in San Francisco is 70\u00b0F (21.1\u00b0C) with partly cloudy skies. The wind is blowing from the west-northwest at around 12 mph (19 km/h). The humidity is 59% and visibility is 9 miles (16 km). Overall, it looks like a nice late summer day in San Francisco with comfortable temperatures and partly sunny conditions.",
"type": "text",
"index": 0
}
],
"example": false,
"tool_calls": [],
"usage_metadata": {
"input_tokens": 837,
"total_tokens": 961,
"output_tokens": 124
},
"additional_kwargs": {},
"response_metadata": {
"stop_reason": "end_turn",
"stop_sequence": null
},
"invalid_tool_calls": []
}
]
}
},
"user_id": "",
"graph_id": "agent",
"thread_id": "5cb1e8a1-34b3-4a61-a34e-71a9799bd00d",
"created_by": "system",
"assistant_id": "fe096781-5601-53d2-b2f6-0d3403f7e9ca"
},
"created_at": "2024-08-30T21:09:00.079909+00:00",
"checkpoint_id": "1ef67141-3ca2-6fae-8003-fe96832e57d6",
"parent_checkpoint_id": "1ef67141-2129-6b37-8002-61fc3bf69cb5"
}
```

We can also just print the content of the last AIMessage:

<Tabs>
  <Tab title="Python">
    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    print(final_result['values']['messages'][-1]['content'][0]['text'])
    ```
  </Tab>

  <Tab title="Javascript">
    ```js theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    console.log(finalResult['values']['messages'][finalResult['values']['messages'].length-1]['content'][0]['text']);
    ```
  </Tab>

  <Tab title="CURL">
    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    curl --request GET \
        --url <DEPLOYMENT_URL>/threads/<THREAD_ID>/state | jq -r '.values.messages[-1].content.[0].text'
    ```
  </Tab>
</Tabs>

Output:

```
The search results provide the current weather conditions in San Francisco. According to the data, as of 2:00 PM on August 30, 2024, the temperature in San Francisco is 70°F (21.1°C) with partly cloudy skies. The wind is blowing from the west-northwest at around 12 mph (19 km/h). The humidity is 59% and visibility is 9 miles (16 km). Overall, it looks like a nice late summer day in San Francisco with comfortable temperatures and partly sunny conditions.
```

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/background-run.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Export trace data to BigQuery
Source: https://docs.langchain.com/langsmith/big-query-bulk-export

Load LangSmith trace data into BigQuery using bulk export to GCS.

<Info>
  **Plan restrictions apply**

  Bulk export is only available on [LangSmith Plus or Enterprise tiers](https://www.langchain.com/pricing-langsmith).
</Info>

LangSmith can export trace data to a Google Cloud Storage (GCS) bucket in Parquet format. From there, you can load it into BigQuery as an external table (queried in place from GCS) or as a native table (copied into BigQuery storage).

This guide covers:

* Setting up a GCS bucket and HMAC credentials for LangSmith.
* Creating a bulk export destination and export job.
* Loading the exported data into BigQuery.

For full details on bulk export configuration options, refer to [Bulk export trace data](/langsmith/data-export) and [Manage bulk export destinations](/langsmith/data-export-destinations).

## Prerequisites

* Data in your LangSmith [Tracing project](https://smith.langchain.com/projects).
* [`gcloud` CLI installed](https://docs.cloud.google.com/sdk/docs/install-sdk). (You can also use the Google Cloud console for setup.)

## 1. Create a GCS bucket

Create a dedicated GCS bucket for LangSmith exports. Using a dedicated bucket makes it easier to grant scoped permissions without affecting other data:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
gcloud storage buckets create gs://YOUR_BUCKET_NAME \
  --location=US \
  --uniform-bucket-level-access
```

Choose a region close to your BigQuery dataset to minimize latency and avoid cross-region egress charges.

## 2. Create a service account and grant access

Create a GCP service account that LangSmith will use to write data to GCS:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
gcloud iam service-accounts create langsmith-bulk-export \
  --display-name="LangSmith Bulk Export"
```

Grant the service account write access to your bucket. The minimum required permission is `storage.objects.create`. Granting `storage.objects.delete` is optional, but recommended. LangSmith uses it to clean up a temporary test file created during destination validation. If this permission is absent, a `tmp/` folder may remain in your bucket.

The "Storage Object Admin" predefined role covers all required and recommended permissions:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
gcloud storage buckets add-iam-policy-binding gs://YOUR_BUCKET_NAME \
  --member="serviceAccount:langsmith-bulk-export@YOUR_PROJECT.iam.gserviceaccount.com" \
  --role="roles/storage.objectAdmin"
```

To use a minimal custom role instead, grant only:

* `storage.objects.create` (required)
* `storage.objects.delete` (optional, for test file cleanup)
* `storage.objects.get` (optional but recommended, for file size verification)
* `storage.multipartUploads.create` (optional but recommended, for large file uploads)

## 3. Generate HMAC keys

LangSmith connects to GCS using the S3-compatible XML API, which requires HMAC keys rather than a service account JSON key.

Generate HMAC keys for your service account:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
gcloud storage hmac create \
  langsmith-bulk-export@YOUR_PROJECT.iam.gserviceaccount.com
```

Save the `accessId` and `secret` from the output. You can also generate HMAC keys in the GCP Console under **Cloud Storage → Settings → Interoperability → Create a key for a service account**.

## 4. Create a bulk export destination

Create a destination in LangSmith pointing to your GCS bucket. Set `endpoint_url` to `https://storage.googleapis.com` to use the GCS S3-compatible API.

You will need your [LangSmith API key](/langsmith/create-account-api-key) and [workspace ID](/langsmith/set-up-hierarchy#set-up-a-workspace).

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
curl --request POST \
  --url 'https://api.smith.langchain.com/api/v1/bulk-exports/destinations' \
  --header 'Content-Type: application/json' \
  --header 'X-API-Key: YOUR_API_KEY' \
  --header 'X-Tenant-Id: YOUR_WORKSPACE_ID' \
  --data '{
    "destination_type": "s3",
    "display_name": "GCS for BigQuery",
    "config": {
      "bucket_name": "YOUR_BUCKET_NAME",
      "prefix": "YOUR_PREFIX",
      "endpoint_url": "https://storage.googleapis.com"
    },
    "credentials": {
      "access_key_id": "YOUR_HMAC_ACCESS_ID",
      "secret_access_key": "YOUR_HMAC_SECRET"
    }
  }'
```

`prefix` is a path within the bucket where LangSmith will write exported files. For example, `langsmith-exports` or `data/traces`. Choose any value that works for your bucket layout.

LangSmith validates the credentials by performing a test write before saving the destination. If the request returns a `400` error, refer to [Debug destination errors](/langsmith/data-export-destinations#debug-destination-errors).

Save the `id` from the response; you will need it in the next step.

### Temporary validation file

During destination creation (and [credential rotation](#credential-rotation)), LangSmith writes a temporary `.txt` file to `YOUR_PREFIX/tmp/` to verify write access, then attempts to delete it. The deletion is best-effort: if the service account lacks `storage.objects.delete`, the file is not deleted and the `tmp/` folder remains in your bucket.

The `tmp/` folder does not affect exports, but it will be included in broad GCS URI globs (e.g., `gs://YOUR_BUCKET_NAME/YOUR_PREFIX/*`).

## 5. Create a bulk export job

Create an export targeting a specific project. Use `format_version: v2_beta` for BigQuery compatibility—it produces UTC timezone-aware timestamps that BigQuery handles correctly.

You will need the project ID (`session_id`), which you can copy from the project view in the [**Tracing Projects** list](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-big-query-bulk-export).

**One-time export:**

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
curl --request POST \
  --url 'https://api.smith.langchain.com/api/v1/bulk-exports' \
  --header 'Content-Type: application/json' \
  --header 'X-API-Key: YOUR_API_KEY' \
  --header 'X-Tenant-Id: YOUR_WORKSPACE_ID' \
  --data '{
    "bulk_export_destination_id": "YOUR_DESTINATION_ID",
    "session_id": "YOUR_PROJECT_ID",
    "start_time": "2024-01-01T00:00:00Z",
    "end_time": "2024-02-01T00:00:00Z",
    "format_version": "v2_beta",
    "compression": "snappy"
  }'
```

**Scheduled (recurring) export:**

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
curl --request POST \
  --url 'https://api.smith.langchain.com/api/v1/bulk-exports' \
  --header 'Content-Type: application/json' \
  --header 'X-API-Key: YOUR_API_KEY' \
  --header 'X-Tenant-Id: YOUR_WORKSPACE_ID' \
  --data '{
    "bulk_export_destination_id": "YOUR_DESTINATION_ID",
    "session_id": "YOUR_PROJECT_ID",
    "start_time": "2024-01-01T00:00:00Z",
    "interval_hours": 24,
    "format_version": "v2_beta",
    "compression": "snappy"
  }'
```

Snappy compression is fast and widely supported by BigQuery. For all available options, refer to [Bulk export trace data](/langsmith/data-export#2-create-an-export-job), including field filtering and filter expressions.

### Output file structure

Exported files land in GCS using a Hive-partitioned path structure:

```
gs://YOUR_BUCKET_NAME/YOUR_PREFIX/export_id=<uuid>/tenant_id=<uuid>/session_id=<uuid>/resource=runs/year=<year>/month=<month>/day=<day>/<filename>.parquet
```

The partition columns in the path (`export_id`, `tenant_id`, `session_id`, `resource`, `year`, `month`, `day`) are available as queryable columns in BigQuery when Hive partition detection is enabled.

## 6. Load data into BigQuery

BigQuery offers two ways to access your exported data. Both require granting the BigQuery service account read access to your GCS bucket first. Choose based on your needs:

* **External table:** data stays in GCS and BigQuery queries it in place. No storage costs in BigQuery, but query performance is slower than native storage. Refer to [Required roles](https://docs.cloud.google.com/bigquery/docs/query-cloud-storage-data#required-roles).
* **Native table:** data is copied into BigQuery storage. Faster queries and full support for BigQuery features, but incurs BigQuery storage costs. Refer to [Required permissions](https://docs.cloud.google.com/bigquery/docs/cloud-storage-transfer#required_permissions).

### Create the table

<Tabs>
  <Tab title="External table">
    An external table queries data directly from GCS without copying it into BigQuery.

    1. In the BigQuery console, expand your project and dataset in the **Explorer** pane.
    2. Click the dataset's **Actions** menu (three dots) and select **Create table**.
    3. Under **Source**:
       * Set **Create table from** to **Google Cloud Storage**.
       * Set the file path to `gs://YOUR_BUCKET_NAME/YOUR_PREFIX/export_id=*`. Using `export_id=*` scopes BigQuery to Hive-partitioned export directories and excludes the `tmp/` folder that LangSmith writes during destination validation (see [Temporary validation file](#temporary-validation-file)).
       * Set **File format** to **Parquet**.
    4. Check **Source data partitioning**, then:
       * Set **Source URI prefix** to `gs://YOUR_BUCKET_NAME/YOUR_PREFIX`.
       * Set **Partition inference mode** to **Automatically infer types**.
    5. Under **Destination**:
       * Select your project and dataset.
       * Enter a table name, for example `langsmith_runs`.
       * Set **Table type** to **External table**.
    6. Under **Schema**, enable **Auto-detect**.
    7. Click **Create table**.

    The partition path columns (`export_id`, `tenant_id`, `session_id`, `resource`, `year`, `month`, `day`) are available as queryable columns. Filter on `year`, `month`, or `day` in your queries to enable partition pruning.
  </Tab>

  <Tab title="Native table">
    A native table transfers the Parquet data into BigQuery storage for full query performance.

    1. Go to the [Data Transfer page](https://console.cloud.google.com/bigquery/transfers) in the Google Cloud console and select **+ Create transfer**.

    2. For **Source type**, select **Google Cloud Storage**.

    3. Enter a **Transfer name**. You'll have access to edit the transfer at a point if necessary.

    4. Select a **Schedule option**. If you do not want to repeat the export, you can select **On demand** and trigger the export manually.

    5. In the BigQuery console, expand your project and dataset in the **Explorer** pane.

    6. Click the dataset's **Actions** menu (three dots) and select **Create table**.

    7. Under **Source**:
       * Set **Create table from** to **Google Cloud Storage**.
       * Set the file path to `gs://YOUR_BUCKET_NAME/YOUR_PREFIX/export_id=*`. Using `export_id=*` excludes the `tmp/` folder that LangSmith writes during destination validation (see [Temporary validation file](#temporary-validation-file)).
       * Set **File format** to **Parquet**.

    8. Check **Source data partitioning**, then:
       * Set **Source URI prefix** to `gs://YOUR_BUCKET_NAME/YOUR_PREFIX`.
       * Set **Partition inference mode** to **Automatically infer types**.

    9. Under **Destination**:
       * Select your project and dataset.
       * Enter a table name, for example `langsmith_runs`.
       * Set **Table type** to **Native table**.

    10. Under **Advanced options**, set **Write preference** to **Write if empty** for a new table.

    11. Click **Create table**.

    BigQuery runs a load job to copy the data. The Hive partition columns appear as regular columns in the table. For the full list of available data columns, see [Exportable fields](/langsmith/data-export#exportable-fields).
  </Tab>
</Tabs>

## Credential rotation

To rotate your HMAC keys without interrupting active exports:

1. **Generate new HMAC keys** in GCP for the same service account.

2. **Call the PATCH endpoint** with the new credentials:

   ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
   curl --request PATCH \
     --url 'https://api.smith.langchain.com/api/v1/bulk-exports/destinations/YOUR_DESTINATION_ID' \
     --header 'Content-Type: application/json' \
     --header 'X-API-Key: YOUR_API_KEY' \
     --header 'X-Tenant-Id: YOUR_WORKSPACE_ID' \
     --data '{
       "credentials": {
         "access_key_id": "NEW_HMAC_ACCESS_ID",
         "secret_access_key": "NEW_HMAC_SECRET"
       }
     }'
   ```

   LangSmith validates the new credentials with a test write before saving. A new `tmp/` file may appear in your bucket during this validation (see [Temporary validation file](#temporary-validation-file)).

3. **Keep old HMAC keys active** until all in-flight export runs complete. Both credential sets are valid simultaneously during the transition window.

4. **Delete the old HMAC keys** in GCP once you have confirmed no in-flight runs are using them.

For full details, see [Rotate destination credentials](/langsmith/data-export-destinations#rotate-destination-credentials).

## Troubleshooting

| Symptom                                     | Likely cause                           | Fix                                                                                         |
| ------------------------------------------- | -------------------------------------- | ------------------------------------------------------------------------------------------- |
| `400 Access denied` on destination creation | HMAC credentials lack write permission | Verify the service account has `storage.objects.create` on the bucket                       |
| `400 Key ID you provided does not exist`    | HMAC access ID is invalid              | Regenerate HMAC keys in GCP                                                                 |
| `400 Invalid endpoint`                      | Endpoint URL is malformed              | Use exactly `https://storage.googleapis.com`                                                |
| BigQuery table shows no rows                | Export not yet complete                | Check export status with `GET /api/v1/bulk-exports/{export_id}`                             |
| BigQuery partition pruning not working      | Incorrect source URI prefix            | Ensure the source URI prefix ends before the first partition key, e.g. `gs://BUCKET/PREFIX` |
| BigQuery picks up `tmp/` files              | Broad file path glob                   | Use `export_id=*` in your file path instead of `*`                                          |

For additional error codes and export status details, see [Monitor and troubleshoot bulk exports](/langsmith/data-export-monitor).

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/big-query-bulk-export.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
