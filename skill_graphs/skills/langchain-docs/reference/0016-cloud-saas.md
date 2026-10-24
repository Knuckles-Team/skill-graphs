# Cloud (SaaS)
Source: https://docs.langchain.com/langsmith/cloud

<Callout icon="rocket">
  If you're ready to deploy your app to LangSmith Cloud (AWS or GCP), follow the [Cloud deployment quickstart](/langsmith/deployment-quickstart) or the [full setup guide](/langsmith/deploy-to-cloud). This page explains the Cloud managed architecture for reference.
</Callout>

The **Cloud** option is a fully managed model where LangChain hosts and operates all LangSmith infrastructure and services:

* **Fully managed infrastructure**: LangChain handles all infrastructure, updates, scaling, and maintenance.
* **Deploy from GitHub**: Connect your repositories and deploy with a few clicks.
* **Automated CI/CD**: Build process is handled automatically by the platform.
* **LangSmith UI**: Full access to [observability](/langsmith/observability), [evaluation](/langsmith/evaluation), [deployment management](/langsmith/deployment), and [Studio](/langsmith/studio).

|                                               | **Who manages it** | **Where it runs**               |
| --------------------------------------------- | ------------------ | ------------------------------- |
| **LangSmith platform (UI, APIs, datastores)** | LangChain          | LangChain's cloud (AWS and GCP) |
| **Your Agent Servers**                        | LangChain          | LangChain's cloud (AWS and GCP) |
| **CI/CD for your apps**                       | LangChain          | LangChain's cloud (AWS and GCP) |

<img alt="Cloud deployment: LangChain hosts and manages all components including the UI, APIs, and your Agent Servers." />

## Get started

To deploy your first application to Cloud, follow the [Cloud deployment quickstart](/langsmith/deployment-quickstart) or refer to the [comprehensive setup guide](/langsmith/deploy-to-cloud).

## Cloud architecture and scalability

<Note>
  This section is only relevant for cloud-managed LangSmith at [https://smith.langchain.com?utm\_source=docs\&utm\_medium=cta\&utm\_campaign=langsmith-signup\&utm\_content=langsmith-cloud](https://smith.langchain.com), [https://eu.smith.langchain.com](https://eu.smith.langchain.com), [https://apac.smith.langchain.com](https://apac.smith.langchain.com), and [https://aws.smith.langchain.com](https://aws.smith.langchain.com).

  For information on the self-hosted LangSmith solution, please refer to the [self-hosted documentation](/langsmith/self-hosted).
</Note>

LangSmith is deployed on Google Cloud Platform (GCP) for the US, EU, and APAC SaaS regions and on Amazon Web Services (AWS) for the AWS-hosted US SaaS region. The platform is designed to be highly scalable. Many customers run production workloads on LangSmith for LLM application observability, evaluation, and agent deployment.

The US-based LangSmith service (default GCP region) is deployed in the `us-central1` (Iowa) region of GCP.

<Note>
  The [EU-based LangSmith service](https://eu.smith.langchain.com) is now available (as of mid-July 2024) and is deployed in the `europe-west4` (Netherlands) region of GCP. If you are interested in an enterprise plan in this region, [contact our sales team](https://www.langchain.com/contact-sales).
</Note>

<Note>
  As of April 2026, LangSmith SaaS is available on AWS in `us-east-2` (Ohio).
</Note>

<Note>
  As of May 2026, LangSmith SaaS is available in APAC on GCP in `australia-southeast1` (Sydney).
</Note>

### Regional storage

The resources and services in this table are stored in the location corresponding to the URL where sign-up occurred (GCP US, GCP EU, GCP APAC, or AWS US). Cloud-managed LangSmith uses [Supabase](https://supabase.com) for authentication/authorization and [ClickHouse Cloud](https://clickhouse.com/cloud) for the data warehouse.

|                                               | GCP US                                                                                                                                                     | GCP EU                                                                   | GCP APAC                                                                     | AWS US                                                                     |
| --------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------ | ---------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| URL                                           | [https://smith.langchain.com?utm\_source=docs\&utm\_medium=cta\&utm\_campaign=langsmith-signup\&utm\_content=langsmith-cloud](https://smith.langchain.com) | [https://eu.smith.langchain.com](https://eu.smith.langchain.com)         | [https://apac.smith.langchain.com](https://apac.smith.langchain.com)         | [https://aws.smith.langchain.com](https://aws.smith.langchain.com)         |
| API URL                                       | [https://api.smith.langchain.com](https://api.smith.langchain.com)                                                                                         | [https://eu.api.smith.langchain.com](https://eu.api.smith.langchain.com) | [https://apac.api.smith.langchain.com](https://apac.api.smith.langchain.com) | [https://aws.api.smith.langchain.com](https://aws.api.smith.langchain.com) |
| Cloud                                         | GCP us-central1 (Iowa)                                                                                                                                     | GCP europe-west4 (Netherlands)                                           | GCP australia-southeast1 (Sydney)                                            | AWS us-east-2 (Ohio)                                                       |
| Supabase                                      | AWS us-east-1 (N. Virginia)                                                                                                                                | AWS eu-central-1 (Germany)                                               | AWS ap-southeast-2 (Sydney)                                                  | AWS us-east-2 (Ohio)                                                       |
| ClickHouse Cloud                              | us-central1 (Iowa)                                                                                                                                         | europe-west4 (Netherlands)                                               | australia-southeast1 (Sydney)                                                | us-east-2 (Ohio)                                                           |
| [LangSmith deployment](/langsmith/deployment) | GCP us-central1 (Iowa); `*.us.langgraph.app`                                                                                                               | GCP europe-west4 (Netherlands); `*.eu.langgraph.app`                     | GCP australia-southeast1 (Sydney); `*.apac.langgraph.app`                    | AWS us-east-2 (Ohio); `*.aws.us.langgraph.app`                             |

See the [Regions FAQ](/langsmith/regions-faq) for more information.

### Region-independent storage

Data listed here is stored exclusively in the US:

* Payment and billing information with Stripe and Metronome

### GCP services

The following applies to the **US, EU, and APAC** SaaS regions on GCP.

LangSmith is composed of the following services, all deployed on Google Kubernetes Engine (GKE):

* LangSmith Frontend: serves the LangSmith UI.
* LangSmith Backend: serves the LangSmith API.
* LangSmith Platform Backend: handles authentication and other high-volume tasks. (Internal service)
* LangSmith Playground: handles forwarding requests to various LLM providers for the Playground feature.
* LangSmith Queue: handles processing of asynchronous tasks. (Internal service)

LangSmith uses the following GCP storage services:

* Google Cloud Storage (GCS) for runs inputs and outputs.
* Google Cloud SQL PostgreSQL for transactional workloads.
* Google Cloud Memorystore for Redis for queuing and caching.
* Clickhouse Cloud on GCP for trace ingestion and analytics. Our services connect to Clickhouse Cloud, which is hosted in the same GCP region, via a private endpoint.

Some additional GCP services we use include:

* Google Cloud Load Balancer for routing traffic to the LangSmith services.
* Google Cloud CDN for caching static assets.
* Google Cloud Armor for security and rate limits. For more information on rate limits we enforce, please refer to [Rate limits](/langsmith/usage-and-billing#rate-limits).

### AWS services

The following applies to the **AWS US** SaaS region in `us-east-2` (Ohio). The same logical LangSmith components run on **Amazon EKS** instead of GKE.

LangSmith is composed of the following services, all deployed on Amazon EKS:

* LangSmith Frontend: serves the LangSmith UI.
* LangSmith Backend: serves the LangSmith API.
* LangSmith Platform Backend: handles authentication and other high-volume tasks. (Internal service)
* LangSmith Playground: handles forwarding requests to various LLM providers for the Playground feature.
* LangSmith Queue: handles processing of asynchronous tasks. (Internal service)

LangSmith uses the following AWS storage and data services:

* Amazon S3 for runs inputs and outputs.
* Amazon RDS for PostgreSQL for transactional workloads.
* Amazon ElastiCache for Redis for queuing and caching.
* ClickHouse Cloud over AWS PrivateLink in `us-east-2` for trace ingestion and analytics, consistent with the [regional storage](#regional-storage) table above.

Some additional AWS services we use include:

* Elastic Load Balancing (Network Load Balancers) and Istio ingress for routing traffic to the LangSmith services. Documented API rate limits are enforced at the Istio ingress gateway. For details, see [Rate limits](/langsmith/usage-and-billing#rate-limits).
* Amazon CloudFront for caching static assets (including the web UI hostname `aws.smith.langchain.com`).
* AWS WAF on CloudFront for managed rule groups at the edge (for example, AWS Managed Rules common protections and Bot Control).

<div>
  <img alt="Light mode overview" />

  <img alt="Dark mode overview" />
</div>

## Allowlisting IP addresses

### Egress from LangChain SaaS

All traffic leaving LangSmith services will be routed through a NAT gateway. All traffic will appear to originate from the following IP addresses:

| GCP US         | GCP EU         | GCP APAC       | AWS US         |
| -------------- | -------------- | -------------- | -------------- |
| 34.59.65.97    | 34.13.192.67   | 34.151.89.217  | 18.188.147.158 |
| 34.67.51.221   | 34.147.105.64  | 34.116.97.4    | 18.219.86.202  |
| 34.46.212.37   | 34.90.22.166   | 34.151.162.199 | 3.21.57.192    |
| 34.132.150.88  | 34.147.36.213  | 34.116.66.129  |                |
| 35.188.222.201 | 34.32.137.113  | 35.189.8.125   |                |
| 34.58.194.127  | 34.91.238.184  | 35.201.9.237   |                |
| 34.59.97.173   | 35.204.101.241 | 35.189.57.29   |                |
| 104.198.162.55 | 35.204.48.32   | 34.40.198.11   |                |

It may be helpful to allowlist these IP addresses if connecting to your own AzureOpenAI service or other endpoints that may be required by the Playground or Online Evaluation.

<Note>
  Traffic from agents deployed on LangSmith Deployment egresses through a separate set of NAT IPs. For that list, refer to [Allowlist IP addresses](/langsmith/deploy-to-cloud#allowlist-ip-addresses) in the Cloud deployment guide.
</Note>

### Ingress into LangChain SaaS

The LangChain endpoints map to the following static IP addresses for traffic that terminates on our **GCP load balancers** (US/EU/APAC) or, for **AWS US**, on the **Network Load Balancer** in `us-east-2` (API and gateway hostnames):

| GCP US         | GCP EU       | GCP APAC       | AWS US        |
| -------------- | ------------ | -------------- | ------------- |
| 34.8.121.39    | 34.95.92.214 | 34.149.149.213 | 3.129.27.169  |
| 34.107.251.234 | 34.13.73.122 |                | 13.58.107.119 |
|                |              |                | 16.59.151.49  |
|                |              |                | 16.59.98.147  |
|                |              |                | 3.134.146.243 |
|                |              |                | 3.150.87.246  |

You may need to allowlist these to enable traffic from your private network to LangSmith SaaS endpoints (`api.smith.langchain.com`, `smith.langchain.com`, `beacon.langchain.com`, `eu.api.smith.langchain.com`, `eu.smith.langchain.com`, `eu.beacon.langchain.com`, `apac.api.smith.langchain.com`, `apac.smith.langchain.com`, `apac.beacon.langchain.com`, `aws.api.smith.langchain.com`, `aws.smith.langchain.com`).

## Private connectivity (Enterprise)

<Callout icon="lock">
  **Enterprise only.** Private connectivity is available exclusively for Enterprise customers. Contact your account representative or [sales@langchain.dev](mailto:sales@langchain.dev) to enable this feature.
</Callout>

Enterprise customers can connect to LangSmith without exposing traffic to the public internet using **AWS PrivateLink** or **GCP Private Service Connect (PSC)**.

### AWS PrivateLink

Customers on **AWS** can connect to LangSmith via [AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/), providing private connectivity from any VPC. Cross-region connectivity is supported natively.

#### Endpoint service name

| Region           | Service Name                                              |
| ---------------- | --------------------------------------------------------- |
| US (`us-east-2`) | `com.amazonaws.vpce.us-east-2.vpce-svc-054f37092752bff6b` |

#### Setup

**1. Request access:** Contact your account representative or [sales@langchain.dev](mailto:sales@langchain.dev) with your AWS account ID. LangChain will add your account to the endpoint service's allowed principals list.

**2. Create an Interface VPC Endpoint** in your AWS account. Attach a security group that allows **TCP 443 inbound** from your VPC CIDR (or from the instances that need to reach LangSmith):

<CodeGroup>
  ```bash AWS CLI theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  aws ec2 create-vpc-endpoint \
    --vpc-id <YOUR_VPC_ID> \
    --service-name <SERVICE_NAME_FROM_TABLE_ABOVE> \
    --vpc-endpoint-type Interface \
    --subnet-ids <YOUR_SUBNET_IDS> \
    --security-group-ids <YOUR_SECURITY_GROUP_ID> \
    --region <YOUR_REGION>
  ```

  ```hcl Terraform theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  resource "aws_vpc_endpoint" "langsmith" {
    vpc_id              = "<YOUR_VPC_ID>"
    service_name        = "<SERVICE_NAME_FROM_TABLE_ABOVE>"
    vpc_endpoint_type   = "Interface"
    subnet_ids          = ["<YOUR_SUBNET_IDS>"]
    security_group_ids  = ["<YOUR_SECURITY_GROUP_ID>"]
  }
  ```
</CodeGroup>

**3. Wait for acceptance.** LangChain will accept the connection. The endpoint status will change from `pendingAcceptance` to `available`. Allow a few minutes after acceptance for the change to fully propagate before testing connectivity.

#### Configure DNS

Configure DNS so that `aws.api.smith.langchain.com` resolves to your VPC endpoint's private DNS name within your VPC. You can use any private DNS solution — Route 53 Private Hosted Zones, a corporate DNS resolver, or any DNS server reachable from your VPC.

First, get your endpoint's DNS name:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
aws ec2 describe-vpc-endpoints \
  --vpc-endpoint-ids <YOUR_ENDPOINT_ID> \
  --query 'VpcEndpoints[0].DnsEntries[0].DnsName' \
  --output text --region <YOUR_REGION>
```

Then create a CNAME record for `aws.api.smith.langchain.com` pointing to that DNS name. Here's an example using Route 53:

<CodeGroup>
  ```bash AWS CLI theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  aws route53 create-hosted-zone \
    --name aws.api.smith.langchain.com \
    --vpc VPCRegion=<YOUR_REGION>,VPCId=<YOUR_VPC_ID> \
    --caller-reference langsmith-privatelink-$(date +%s) \
    --hosted-zone-config PrivateZone=true

  aws route53 change-resource-record-sets \
    --hosted-zone-id <HOSTED_ZONE_ID> \
    --change-batch '{
      "Changes": [{
        "Action": "CREATE",
        "ResourceRecordSet": {
          "Name": "aws.api.smith.langchain.com",
          "Type": "CNAME",
          "TTL": 300,
          "ResourceRecords": [{"Value": "<ENDPOINT_DNS_NAME>"}]
        }
      }]
    }'
  ```

  ```hcl Terraform theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  resource "aws_route53_zone" "langsmith_privatelink" {
    name = "aws.api.smith.langchain.com"

    vpc {
      vpc_id = "<YOUR_VPC_ID>"
    }
  }

  resource "aws_route53_record" "langsmith_privatelink" {
    zone_id = aws_route53_zone.langsmith_privatelink.zone_id
    name    = "aws.api.smith.langchain.com"
    type    = "CNAME"
    ttl     = 300
    records = [aws_vpc_endpoint.langsmith.dns_entry[0]["dns_name"]]
  }
  ```
</CodeGroup>

#### Verify connectivity

From an EC2 instance or container in your VPC:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
curl https://aws.api.smith.langchain.com/ok
```

### GCP Private Service Connect

Enterprise customers on **GCP** can connect to LangSmith via [Private Service Connect (PSC)](https://cloud.google.com/vpc/docs/private-service-connect), providing private connectivity without exposing traffic to the public internet.

#### Service attachment URIs

Use the following service attachment URIs to create a PSC endpoint in your VPC:

| Region                        | Service Attachment URI                                                                             |
| ----------------------------- | -------------------------------------------------------------------------------------------------- |
| US (`us-central1`)            | `projects/langchain-prod/regions/us-central1/serviceAttachments/gateway-psc-publish`               |
| EU (`europe-west4`)           | `projects/langchain-prod/regions/europe-west4/serviceAttachments/gateway-psc-publish`              |
| APAC (`australia-southeast1`) | `projects/langchain-apac-prod/regions/australia-southeast1/serviceAttachments/gateway-psc-publish` |

#### PSC domains

After setup, use the following domains to connect to LangSmith over your PSC connection:

| Region | Domain                                           |
| ------ | ------------------------------------------------ |
| US     | `us-central1.p.api.smith.langchain.com`          |
| EU     | `europe-west4.p.api.smith.langchain.com`         |
| APAC   | `australia-southeast1.p.api.smith.langchain.com` |

#### Setup

**Request access:** Contact your account representative or [sales@langchain.dev](mailto:sales@langchain.dev) with your GCP project ID. LangChain will add your project to the service attachment's allowed consumer list.

After access is granted, create a PSC endpoint and configure DNS using either the gcloud CLI or Terraform.

#### Create a PSC endpoint

Create a forwarding rule in your VPC targeting the service attachment:

<CodeGroup>
  ```bash gcloud CLI theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  # Create the PSC endpoint
  gcloud compute forwarding-rules create langsmith-psc-endpoint \
    --region=<REGION> \
    --network=<YOUR_VPC_NETWORK> \
    --subnet=<YOUR_SUBNET> \
    --target-service-attachment=projects/langchain-prod/regions/<REGION>/serviceAttachments/gateway-psc-publish \
    --load-balancing-scheme=""

  # Get the assigned IP address
  gcloud compute forwarding-rules describe langsmith-psc-endpoint \
    --region=<REGION> \
    --format="value(IPAddress)"
  ```

  ```hcl Terraform theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  resource "google_compute_forwarding_rule" "langsmith_psc" {
    name                  = "langsmith-psc-endpoint"
    project               = "<YOUR_PROJECT_ID>"
    region                = "<REGION>"
    network               = "<YOUR_VPC_NETWORK>"
    subnetwork            = "<YOUR_SUBNET>"
    target                = "projects/langchain-prod/regions/<REGION>/serviceAttachments/gateway-psc-publish"
    load_balancing_scheme = ""
  }
  ```
</CodeGroup>

#### Configure DNS

Create a private DNS zone in your VPC and add an A record pointing to the PSC endpoint IP:

<CodeGroup>
  ```bash gcloud CLI theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  # Create a private DNS zone
  gcloud dns managed-zones create langsmith-psc \
    --dns-name="<REGION>.p.api.smith.langchain.com." \
    --visibility=private \
    --networks=<YOUR_VPC_NETWORK>

  # Add an A record pointing to the PSC endpoint IP
  gcloud dns record-sets create "<REGION>.p.api.smith.langchain.com." \
    --zone=langsmith-psc \
    --type=A \
    --rrdatas=<PSC_ENDPOINT_IP>
  ```

  ```hcl Terraform theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  resource "google_dns_managed_zone" "langsmith_psc" {
    name        = "langsmith-psc"
    project     = "<YOUR_PROJECT_ID>"
    dns_name    = "<REGION>.p.api.smith.langchain.com."
    visibility  = "private"

    private_visibility_config {
      networks {
        network_url = "<YOUR_VPC_NETWORK_SELF_LINK>"
      }
    }
  }

  resource "google_dns_record_set" "langsmith_psc" {
    name         = "<REGION>.p.api.smith.langchain.com."
    project      = "<YOUR_PROJECT_ID>"
    managed_zone = google_dns_managed_zone.langsmith_psc.name
    type         = "A"
    ttl          = 300
    rrdatas      = [google_compute_forwarding_rule.langsmith_psc.ip_address]
  }
  ```
</CodeGroup>

#### Verify connectivity

From a VM in your VPC:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
curl https://<REGION>.p.api.smith.langchain.com/ok
```

## API rate limits

LangSmith enforces rate limits on API endpoints to ensure service stability and fair usage. The following table shows the rate limits for different endpoints in the GCP US and GCP EU regions. GCP APAC and AWS US enforce comparable service-specific limits; contact support if you need exact limits for your organization. Note that:

* Rate limits are expressed as `count / interval` where count is the number of requests allowed within the interval (in seconds). For example, `2000 / 10` means 2000 requests per 10 seconds.
* When no HTTP method is specified in the endpoint column, the rate limit applies to all HTTP methods for that endpoint.
* When a specific method is listed (e.g., `POST`, `GET`), the rate limit applies only to that method.

| Match / Endpoint (method)                   | Identity key     | US prod limit | EU prod limit | Category                                     |
| ------------------------------------------- | ---------------- | ------------- | ------------- | -------------------------------------------- |
| OPTIONS, `/info`, `*/v1/metadata/submit`    | IP               | 2000 / 10     | 2000 / 10     | [High throughput](#rate-limit-categories)    |
| `/auth`                                     | `x-api-key`      | 2000 / 10     | 2000 / 10     | [High throughput](#rate-limit-categories)    |
| `/auth`                                     | `x-user-id` + IP | 2000 / 10     | 2000 / 10     | [High throughput](#rate-limit-categories)    |
| `/v1/beacon`                                | IP               | 2000 / 10     | 2000 / 10     | [High throughput](#rate-limit-categories)    |
| `/repos`                                    | `x-api-key`      | 100 / 60      | 100 / 60      | [Repository](#rate-limit-categories)         |
| `/repos`                                    | `x-user-id` + IP | 100 / 60      | 100 / 60      | [Repository](#rate-limit-categories)         |
| `POST /runs/batch`                          | `x-api-key`      | 2000 / 10     | 2000 / 10     | [High throughput](#rate-limit-categories)    |
| `POST /otel/v1/traces`                      | `x-api-key`      | 2000 / 10     | 2000 / 10     | [Run ingest](#rate-limit-categories)         |
| `POST` containing `/charts`                 | `x-api-key`      | 750 / 600     | 750 / 600     | [Charts](#rate-limit-categories)             |
| `POST` containing `/charts`                 | `x-user-id` + IP | 750 / 600     | 750 / 600     | [Charts](#rate-limit-categories)             |
| `POST /runs/multipart`                      | `x-api-key`      | 6000 / 10     | 6000 / 10     | [Multipart ingest](#rate-limit-categories)   |
| `POST /runs/query`                          | `x-api-key`      | 15 / 10       | 15 / 10       | [Run query (API)](#rate-limit-categories)    |
| `POST /runs/query`                          | `x-user-id` + IP | 300 / 10      | 300 / 10      | [Run query (User)](#rate-limit-categories)   |
| `/generate`                                 | `x-api-key`      | 30 / 3600     | 30 / 3600     | [Generation](#rate-limit-categories)         |
| `/generate`                                 | `x-user-id` + IP | 30 / 3600     | 30 / 3600     | [Generation](#rate-limit-categories)         |
| `/commits`                                  | `x-api-key`      | 10000 / 60    | 2000 / 60     | [Commits](#rate-limit-categories)            |
| `/commits`                                  | `x-user-id` + IP | 10000 / 60    | 2000 / 60     | [Commits](#rate-limit-categories)            |
| `DELETE /sessions` or `*/trigger`           | `x-api-key`      | 10 / 60       | 10 / 60       | [Deletion](#rate-limit-categories)           |
| `DELETE /sessions` or `*/trigger`           | `x-user-id` + IP | 30 / 60       | 30 / 60       | [Deletion](#rate-limit-categories)           |
| `POST /runs` (single run ingest)            | `x-api-key`      | 2000 / 10     | 2000 / 10     | [Run ingest](#rate-limit-categories)         |
| `PATCH` containing `/runs`                  | `x-api-key`      | 2000 / 10     | 2000 / 10     | [Run ingest](#rate-limit-categories)         |
| `POST /feedback`                            | `x-api-key`      | 2000 / 10     | 2000 / 10     | [High throughput](#rate-limit-categories)    |
| `GET /runs/{uuid}` or `/api/v1/runs/{uuid}` | `x-api-key`      | 30 / 60       | 30 / 60       | [Run lookup](#rate-limit-categories)         |
| `GET` containing `/examples`                | `x-api-key`      | 5000 / 60     | 5000 / 60     | [Examples](#rate-limit-categories)           |
| Any request with `x-api-key`                | `x-api-key`      | 1000 / 10     | 1000 / 10     | [Default (API key)](#rate-limit-categories)  |
| Any request with `x-user-id`                | `x-user-id` + IP | 1000 / 10     | 1000 / 10     | [Default (User)](#rate-limit-categories)     |
| `/public/download`                          | IP               | 5000 / 60     | 5000 / 60     | [Public download](#rate-limit-categories)    |
| `/runs/stats`                               | `x-api-key`      | 1 / 10        | 20 / 10       | [Stats](#rate-limit-categories)              |
| All other IPs (catch-all)                   | IP               | 100 / 60      | 100 / 60      | [Public (catch-all)](#rate-limit-categories) |

### Rate limit categories

* **High throughput**: General high-volume endpoints for core operations like authentication, metadata, and feedback.
* **Repository**: Repository and prompt management operations.
* **Run ingest**: Individual trace/run ingestion endpoints for observability.
* **Charts**: Chart generation and visualization endpoints.
* **Multipart ingest**: Bulk run ingestion via multipart upload for high-volume tracing.
* **Run query (API)**: API key-based run query operations with stricter limits for complex queries.
* **Run query (User)**: User-based run query operations with higher limits for interactive use.
* **Generation**: AI-powered code and content generation endpoints (limited to prevent abuse).
* **Commits**: Prompt versioning and commit operations.
* **Deletion**: Session deletion and workflow trigger operations.
* **Run lookup**: Retrieving specific runs by UUID.
* **Examples**: Fetching dataset examples for few-shot prompting.
* **Default (API key)**: Fallback rate limit for authenticated API requests not matching specific patterns.
* **Default (User)**: Fallback rate limit for authenticated user requests not matching specific patterns.
* **Public download**: High-volume public download endpoints for shared resources.
* **Stats**: Run statistics and analytics endpoints (region-specific limits apply).
* **Public (catch-all)**: Default rate limit for unauthenticated public access.

For more information on rate limits and other service limits, refer to the [Administration overview](/langsmith/usage-and-billing#rate-limits).

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/cloud.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# How to define a code evaluator
Source: https://docs.langchain.com/langsmith/code-evaluator-sdk

Code evaluators are functions that take a dataset example and the resulting application output, and return one or more metrics. These functions can be passed directly into the [`evaluate()`](https://reference.langchain.com/python/langsmith/client/Client/evaluate) or [`aevaluate()`](https://reference.langchain.com/python/langsmith/client/Client/aevaluate) functions.

<Tip>
  To define code evaluators in the LangSmith UI, refer to [How to define a code evaluator (UI)](/langsmith/code-evaluator-ui). To grade outputs against assertions saved on dataset examples, refer to [Use assertions](/langsmith/assertions).
</Tip>

## Basic example

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langsmith import evaluate

  def correct(outputs: dict, reference_outputs: dict) -> bool:
      """Check if the answer exactly matches the expected answer."""
      return outputs["answer"] == reference_outputs["answer"]

  def dummy_app(inputs: dict) -> dict:
      return {"answer": "hmm i'm not sure", "reasoning": "i didn't understand the question"}

  results = evaluate(
      dummy_app,
      data="dataset_name",
      evaluators=[correct]
  )
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import type { EvaluationResult } from "langsmith/evaluation";

  const correct = async ({ outputs, referenceOutputs }: {
    outputs: Record<string, any>;
    referenceOutputs?: Record<string, any>;
  }): Promise<EvaluationResult> => {
    const score = outputs?.answer === referenceOutputs?.answer;
    return { key: "correct", score };
  }
  ```
</CodeGroup>

## Evaluator args

code evaluator functions must have specific argument names. They can take any subset of the following arguments:

* `run: Run`: The full [Run](/langsmith/run-data-format) object generated by the application on the given example.
* `example: Example`: The full dataset [Example](/langsmith/example-data-format), including the example inputs, outputs (if available), and metadata (if available).
* `inputs: dict`: A dictionary of the inputs corresponding to a single example in a dataset.
* `outputs: dict`: A dictionary of the outputs generated by the application on the given `inputs`.
* `reference_outputs/referenceOutputs: dict`: A dictionary of the reference outputs associated with the example, if available.

For most use cases you'll only need `inputs`, `outputs`, and `reference_outputs`. `run` and `example` are useful only if you need some extra trace or example metadata outside of the actual inputs and outputs of the application.

When using JS/TS these should all be passed in as part of a single object argument.

## Evaluator output

Code evaluators are expected to return one of the following types:

Python and JS/TS

* `dict`: dicts of the form `{"score" | "value": ..., "key": ...}` allow you to customize the metric type ("score" for numerical and "value" for categorical) and metric name. This if useful if, for example, you want to log an integer as a categorical metric.

Python only

* `int | float | bool`: this is interpreted as a continuous metric that can be averaged, sorted, etc. The function name is used as the name of the metric.
* `str`: this is interpreted as a categorical metric. The function name is used as the name of the metric.
* `list[dict]`: return multiple metrics using a single function.

## Additional examples

Requires `langsmith>=0.2.0`

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langsmith import evaluate, wrappers
  from langsmith.schemas import Run, Example
  from openai import AsyncOpenAI
  # Assumes you've installed pydantic.
  from pydantic import BaseModel

  # We can still pass in Run and Example objects if we'd like
  def correct_old_signature(run: Run, example: Example) -> dict:
      """Check if the answer exactly matches the expected answer."""
      return {"key": "correct", "score": run.outputs["answer"] == example.outputs["answer"]}

  # Just evaluate actual outputs
  def concision(outputs: dict) -> int:
      """Score how concise the answer is. 1 is the most concise, 5 is the least concise."""
      return min(len(outputs["answer"]) // 1000, 4) + 1

  # Use an LLM-as-a-judge
  oai_client = wrappers.wrap_openai(AsyncOpenAI())

  async def valid_reasoning(inputs: dict, outputs: dict) -> bool:
      """Use an LLM to judge if the reasoning and the answer are consistent."""
      instructions = """
  Given the following question, answer, and reasoning, determine if the reasoning for the
  answer is logically valid and consistent with question and the answer."""

      class Response(BaseModel):
          reasoning_is_valid: bool

      msg = f"Question: {inputs['question']}\nAnswer: {outputs['answer']}\nReasoning: {outputs['reasoning']}"
      response = await oai_client.beta.chat.completions.parse(
          model="gpt-5.4-mini",
          messages=[{"role": "system", "content": instructions,}, {"role": "user", "content": msg}],
          response_format=Response
      )
      return response.choices[0].message.parsed.reasoning_is_valid

  def dummy_app(inputs: dict) -> dict:
      return {"answer": "hmm i'm not sure", "reasoning": "i didn't understand the question"}

  results = evaluate(
      dummy_app,
      data="dataset_name",
      evaluators=[correct_old_signature, concision, valid_reasoning]
  )
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { Client } from "langsmith";
  import { evaluate } from "langsmith/evaluation";
  import { Run, Example } from "langsmith/schemas";
  import OpenAI from "openai";

  // Type definitions
  interface AppInputs {
      question: string;
  }

  interface AppOutputs {
      answer: string;
      reasoning: string;
  }

  interface Response {
      reasoning_is_valid: boolean;
  }

  // Old signature evaluator
  function correctOldSignature(run: Run, example: Example) {
      return {
          key: "correct",
          score: run.outputs?.["answer"] === example.outputs?.["answer"],
      };
  }

  // Output-only evaluator
  function concision({ outputs }: { outputs: AppOutputs }) {
      return {
          key: "concision",
          score: Math.min(Math.floor(outputs.answer.length / 1000), 4) + 1,
      };
  }

  // LLM-as-judge evaluator
  const openai = new OpenAI();

  async function validReasoning({
      inputs,
      outputs
  }: {
      inputs: AppInputs;
      outputs: AppOutputs;
  }) {
      const instructions = `\
    Given the following question, answer, and reasoning, determine if the reasoning for the \
    answer is logically valid and consistent with question and the answer.`;

      const msg = `Question: ${inputs.question}
  Answer: ${outputs.answer}
  Reasoning: ${outputs.reasoning}`;

      const response = await openai.chat.completions.create({
          model: "gpt-4",
          messages: [
              { role: "system", content: instructions },
              { role: "user", content: msg }
          ],
          response_format: { type: "json_object" },
          functions: [{
              name: "parse_response",
              parameters: {
                  type: "object",
                  properties: {
                      reasoning_is_valid: {
                          type: "boolean",
                          description: "Whether the reasoning is valid"
                      }
                  },
                  required: ["reasoning_is_valid"]
              }
          }]
      });

      const parsed = JSON.parse(response.choices[0].message.content ?? "{}") as Response;
      return {
          key: "valid_reasoning",
          score: parsed.reasoning_is_valid ? 1 : 0
      };
  }

  // Example application
  function dummyApp(inputs: AppInputs): AppOutputs {
      return {
          answer: "hmm i'm not sure",
          reasoning: "i didn't understand the question"
      };
  }

  const results = await evaluate(dummyApp, {
      data: "dataset_name",
      evaluators: [correctOldSignature, concision, validReasoning],
      client: new Client()
  });
  ```
</CodeGroup>

## Related

* [Evaluate aggregate experiment results](/langsmith/summary): Define summary evaluators, which compute metrics for an entire experiment.
* [Run an evaluation comparing two experiments](/langsmith/evaluate-pairwise): Define pairwise evaluators, which compute metrics by comparing two (or more) experiments against each other.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/code-evaluator-sdk.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# How to define a code evaluator
Source: https://docs.langchain.com/langsmith/code-evaluator-ui

Code evaluators in the [LangSmith UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-code-evaluator-ui) allow you to write custom evaluation logic using Python or TypeScript code directly in the interface. Unlike [LLM-as-a-judge](/langsmith/llm-as-judge) evaluators that use a model to evaluate outputs, code evaluators use deterministic logic you define.

<Note>
  To define code evaluators programmatically using the SDK, refer to [How to define a code evaluator (SDK)](/langsmith/code-evaluator-sdk). To grade outputs against assertions saved on dataset examples, refer to [Use assertions](/langsmith/assertions).
</Note>

## Step 1. Create the evaluator

1. Create an evaluator from one of the following pages in the [LangSmith UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-code-evaluator-ui):
   * In the Playground or from a dataset: Select the **+ Evaluator** button.
   * Select **Add rules**, configure your rule and select **Apply evaluator**.
2. Give your evaluator a clear name that describes what it measures (e.g., "Exact Match").
3. Select **Create code evaluator** from the evaluator type options.

## Step 2. Write your evaluator code

<Note>
  **Custom code evaluators restrictions.**

  **Allowed Libraries**: You can import all standard library functions, as well as the following public packages:

  ```
  numpy (v2.2.2): "numpy"
  pandas (v1.5.2): "pandas"
  jsonschema (v4.21.1): "jsonschema"
  scipy (v1.14.1): "scipy"
  sklearn (v1.26.4): "scikit-learn"
  ```

  **Network Access**: You cannot access the internet from a custom code evaluator.
</Note>

In the **Add Custom Code Evaluator** page, define your evaluation logic using Python or TypeScript.

Your evaluator function must be named `perform_eval` and should:

1. Accept `run` and `example` parameters.
2. Access data via `run['inputs']`, `run['outputs']`, and `example['outputs']`.
3. Return a dictionary where each key is a metric name and each value is the score for that metric. Each key represents a piece of feedback you want to return. For example, `{"correctness": 1, "silliness": 0}` would create two pieces of feedback on the run.

### Function signature

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
def perform_eval(run, example):
    # Access the data
    inputs = run['inputs']
    outputs = run['outputs']
    reference_outputs = example['outputs']  # Optional: reference/expected outputs

    # Your evaluation logic here
    score = ...

    # Return a dict with your metric name
    return {"metric_name": score}
```

### Example: Exact match evaluator

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
def perform_eval(run, example):
    """Check if the answer exactly matches the expected answer."""
    actual = run['outputs']['answer']
    expected = example['outputs']['answer']

    is_correct = actual == expected
    return {"exact_match": is_correct}
```

### Example: Input-based evaluator

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
def perform_eval(run, example):
    """Check if the input text contains toxic language."""
    text = run['inputs'].get('text', '').lower()
    toxic_words = ["idiot", "stupid", "hate", "awful"]

    is_toxic = any(word in text for word in toxic_words)
    return {"is_toxic": is_toxic}
```

## Step 3. Test and save

1. Test your evaluator on example data to ensure it works as expected
2. Click **Save** to make the evaluator available for use

## Use your code evaluator

Once created, you can use your code evaluator:

* When running evaluations from the [Playground](/langsmith/prompt-engineering-concepts#playground)
* As part of a dataset to [automatically run evaluations on experiments](/langsmith/bind-evaluator-to-dataset)

## Related

* [LLM-as-a-judge evaluator (UI)](/langsmith/llm-as-judge): Use an LLM to evaluate outputs
* [Composite evaluators](/langsmith/composite-evaluators-ui): Combine multiple evaluator scores

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/code-evaluator-ui.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
