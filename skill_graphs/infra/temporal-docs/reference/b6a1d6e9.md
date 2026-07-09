
Invoices are emailed to Account Owners or the designated billing contacts.
Account Owners and Finance Admins can view their [detailed billing information](https://cloud.temporal.io/billing) at any time.
See our [billing](/cloud/billing) page for details.
You need appropriate administrative permissions to access this section.
Alternatively, to view invoices and billing history, contact Temporal Finance at [ar@temporal.io](mailto: ar@temporal.io).

**Does Temporal charge sales tax/VAT?**

We charge applicable sales tax in US jurisdictions as required.

**How do I cancel my account?**

Account Owners can delete their account and cancel their subscription in the Plans tab in the billing center.
See the [billing and cost](/cloud/billing) page for details on how to access the billing center.

**Will I lose access immediately if I cancel my account?**

Customers lose access to Temporal Cloud once Temporal completes the off-boarding process.
Billing is independent of this process.

**Can I reactivate my account after cancellation?**

No.
When your account is canceled, your account data is deleted and cannot be restored.
To return to Temporal Cloud, you must sign up again.
We will assign you a new Temporal account and consider you as a new customer.

---

## Service regions - Temporal Cloud

You can access Temporal Cloud from anywhere with Internet connectivity, no matter where your Temporal Cloud Namespaces are physically located.
Your applications can live in the cloud environment or data center of your choice.
With that in mind, you _will_ reduce latency by creating Namespaces in a region close to where you host your Workers.

This page enumerates the current regions supported by Temporal Cloud Namespaces.

:::tip Service Availability

Visit [status.temporal.io](https://status.temporal.io) to check the status of our supported regions.
On that page, you can also subscribe to updates to receive email notifications whenever Temporal creates, updates or resolves an incident.

:::

## AWS Service Regions

Temporal Cloud operates in the following Amazon Web Services (AWS) regions:

<AWSRegions />

## GCP Service Regions

Temporal Cloud operates the following Google Cloud (GCP) regions:

<GCPRegions />

---

## Service availability - Temporal Cloud

The operating envelope of Temporal Cloud includes throughput, latency, and limits.
Service regions are listed on [this page](/cloud/regions).
If you need more details, [contact us](https://pages.temporal.io/contact-us).

## Throughput expectations {/* #throughput */}

**What kind of throughput can I get with Temporal Cloud?**

Each Namespace in Temporal has a rate limit, which is measured in [Actions](/cloud/pricing#action) per second.
Temporal offers two different modes for adjusting capacity: On-Demand Capacity or Provisioned Capacity.
With On-Demand Capacity, Namespace capacity is increased automatically along with usage.
With Provisioned Capacity, you can control your capacity limits by requesting Temporal Resource Units (TRUs).

## Latency Service Level Objective (SLO) {/* #latency */}

**What kind of latency can I expect from Temporal Cloud?**

Temporal Cloud has a p99 latency SLO of 200ms per region.

The same SLO for normal Worker requests (commands and polling) apply to Nexus in both the caller and handler Namespaces.

### Historical latency data

Latency over a week-long period for starting and signaling Workflow Executions was as follows:

#### January 2026

| Operation                          |  p50   | p90  |  p99 |
| :--------------------------------- | :----: | :--: | ---: |
| `StartWorkflowExecution`           | 14ms | 21ms | 69ms |
| `SignalWorkflowExecution`          | 11ms | 19ms | 46ms |
| `SignalWithStartWorkflowExecution` | 19ms | 37ms | 95ms |

#### March 2024

| Operation                          | p90  |  p99 |
| :--------------------------------- | :--: | ---: |
| `StartWorkflowExecution`           | 24ms | 54ms |
| `SignalWorkflowExecution`          | 14ms | 40ms |
| `SignalWithStartWorkflowExecution` | 24ms | 61ms |

Latency observed from the Temporal Client is influenced by other system components like the Codec Server, egress proxy, and the network itself.
Also, concurrent operations on the same Workflow Execution may result in higher latency.

---

## Service Level Agreement (SLA) - Temporal Cloud

**What is Temporal Cloud's Service Level Agreement? SLA?**

Temporal Cloud provides two availability levels: the [service availability](https://en.wikipedia.org/wiki/Reliability,_availability_and_serviceability) and the contractual [service level agreement](https://en.wikipedia.org/wiki/Service-level_agreement) (SLA).
These levels are set by your deployment mode:

- **Temporal Cloud with standard single-region deployment**:
  Standard Temporal Cloud deployment provides 99.99% availability and a contractual service level agreement (SLA) of 99.9% guarantee against service errors.
- **Temporal Cloud with High Availability feature Namespace deployment**:
  Temporal Cloud Namespaces that use the High Availability feature provide 99.99% availability and contractual service level agreement (SLA) of 99.99% guarantee against service errors.

The same SLA for normal Worker requests (commands and polling) apply to Nexus in both the caller and handler Namespaces.

To calculate the service-error rate, Temporal Cloud captures all requests that arrive in a Namespace during a five-minute interval.
We record the number of gRPC service errors that occurred.
For each Namespace, we calculate the service-error rate as 1 - (count of errors / count of requests).
Rates are averaged per month and reset quarterly.

Errors recorded against the SLA are service errors, such as the `UNAVAILABLE` [gRPC status code](https://grpc.github.io/grpc/core/md_doc_statuscodes.html).
The following errors are _not_ counted against the SLA:

- `ClientVersionNotSupported`
- `InvalidArgument`
- `NamespaceAlreadyExists`
- `NamespaceInvalidState`
- `NamespaceNotActive`
- `NamespaceNotFound`
- `NotFound`
- `PermissionDenied`
- `QueryFailed`
- `RetryReplication`
- `StickyWorkerUnavailable`
- `TaskAlreadyStarted`
- `Throttling (resources exhausted; triggers retry)`
- `WorkflowExecutionAlreadyStarted`
- `WorkflowNotReady`

Our internal alerting system is based on a [service level objective](https://en.wikipedia.org/wiki/Service-level_objective) (SLO) for all errors, not just errors that count against the SLA.
When we receive an alert that an SLO is not being met, we page our on-call engineers, which often means that issues are resolved before they become noticeable.

Internally, our components are distributed across a minimum of three availability zones per region.
We implement a cell architecture.
Each cell contains the software and services necessary to host a Namespace.
Within each cell, the components are distributed across a minimum of three availability zones per region.

For current system status and information about recent incidents, see [Temporal Status](https://status.temporal.io).

---

## Services, support, and training - Temporal Cloud

Temporal Cloud includes the right level of technical support and guidance, services and training needed to onboard you successfully, assist with design and deployment of your application efficiently and at scale.
Our team has extensive knowledge of Temporal, and a broad set of skills to help you succeed with any project.

Temporal Cloud provides several levels of support, from assisting with break/fix scenarios to issues and services to helping with onboarding, design/code reviews for your application, and pre-production optimizations and operational readiness.

:::note

The content of this page applies to Temporal Cloud customers only.

:::

## Services offered by Temporal Cloud {/* #support */}

|                             | Essentials                                                                      | Business                                                                                                                                                            | Enterprise                                                                                      | Mission Critical                                                                                                                  |
| --------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| Support Staff               | Trained staff providing break-fix support and general guidance.                 | Trained staff providing break-fix support and general guidance.                                                                                                     | Developer experts who provide advanced support                                                  | Developer experts who provide advanced support                                                                                    |
| Technical Guidance          | Core platform config, platform access, documented features, and basic inquiries | Advanced technical support, Workflow troubleshooting, SDK implementations, and Worker configuration, Quarterly code review or design implementation best practices. | Business+ expert-led code reviews and design implementation best practices, available as needed | Enterprise+ expert guidance on Workflow latency monitoring and optimization; performance recommendations based on real time tests |
| Billing & Cost Optimization | Generic Billing Questions                                                       | Generic Billing Questions                                                                                                                                           | Quarterly review of spend                                                                       | Quarterly review of spend, proactive cost optimization                                                                            |

## Temporal Cloud support guarantees {/* #guarantees */}

Temporal endeavors to ensure you are successful with Temporal Cloud.
We offer explicit guarantees for support.
Temporal Cloud customers get break/fix support with an agreed-upon set of SLAs for prioritized issues.
We use a ticketing system for entering, tracking, and closing these issues.

If an issue occurs, the team also provides support through a dedicated Slack channel, forums, and a knowledge base.
We offer two levels of support defined by their availability and SLAs in the following table:

|                                                  | Essentials                                                                                                     | Business                                                                                                           | Enterprise                                                                                                   | Mission Critical                                                                                             |
| ------------------------------------------------ | -------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| **Availability**(Based onTime-zones) | **P0–3**: 9–5 Mon–Fri                                                                                          | **P0–3**: 9–5 Mon–Fri                                                                                              | **P0**: 24×7, (On Page Service) **P1–3**: 9–5 Mon–Fri                                            | **P0**: 24×7 (On Page Service) **P1**: 9-5, 7 days/week **P2–3**: Mon–Fri                        |
| **Response Time**                                | **P0**: 1 business day **P1**: 1 business day **P2**: 1 business day **P3**: 2 business days | **P0**: 2 business hours **P1**: 2 business hours **P2**: 1 business day **P3**: 2 business days | **P0**: 30 minutes **P1**: 1 business hour **P2**: 4 business hours **P3**: 1 business day | **P0**: 15 minutes **P1**: 1 business hour **P2**: 4 business hours **P3**: 1 business day |
| **DSE**                                          | -                                                                                                              | -                                                                                                                  | Add-on                                                                                                       | DSE Included (1 Unit)                                                                                        |
| **Channels**                                     | CommunityTemporal Support Portal                                                                          | CommunityTemporal Support Portal                                                                             | CommunityTemporal Support PortalPrivate Slack                                                    | CommunityTemporal Support PortalPrivate Slack                                                    |

:::info Business Hours Timezones

Business Hours will be specified in your contract, including one of three locations: US Pacific time, European Central time, Australia Eastern time

:::

**Priority definitions**

- **P0 - Critical** (Production impacted)
  - The Temporal Cloud service is unavailable or degraded with a significant impact.
- **P1 - High** (Production issue)
  - An issue related to production workloads running on the Temporal Cloud service, or a significant project is blocked.
- **P2 - Normal** (General issues)
  - General Temporal Cloud service or other issues where there is no production impact, or a workaround exists to mitigate the impact.
- **P3 - Low** (General guidance)
  - Questions or an issue with the Temporal Cloud service that is not impacting system availability or functionality.

:::note On Page Service

P0: 24×7 (On Page Service) is offered for Enterprise and Mission Critical accounts.

:::

For pricing details of these support levels, please visit our [pricing page](/cloud/pricing).

## Temporal Dedicated Support Engineer {/* #dedicated-support-engineer */}

Customers on the Mission Critical Plan and (by opting in) Enterprise customers receive access to a Dedicated Support Engineer.
We offer:

- Direct access to a senior developer expert, who becomes part of your Temporal account team, adding deep technical expertise.
  - Our high-touch engagement model goes beyond traditional support to deliver transformative value through hands-on collaboration, proactive optimization, implementation design and operations.
  - Faster issue resolution with direct assistance from someone who already knows your implementation.
  - Focused advisory on best practices and development pairing to ensure high-quality code and scalability.
  - Optimizations through regular checks and recommendations to improve performance and efficiency.
- Priority access to a senior engineer for up to 20 hours per month, providing expert guidance and proactive support for one business unit or major group, specifically within a single region.

Our Services focus on local time zone alignment to ensure optimal responsiveness and efficiency.
Additional service units for this service can be purchased to cover additional groups or regions at &#36;6,000/Mo/Unit.
One unit of Mission Critical Support includes:

- Up to 20 hours per month
- One major group or business unit
- Limited to one region
- Quarterly onsite visits

## Ticketing

Temporal offers a ticketing system for Temporal Cloud customers.
We have an active [community Slack](https://temporalio.slack.com) and an active [community Discourse forum](https://community.temporal.io/) where you can post questions and ask for help.

:::info

The Temporal Support Portal is for Cloud customers only.
Other Temporal users (non-cloud) have full community access excluding the "#support-cloud" channel.
All Cloud customers pay for support as part of their plan.

:::

### Access Temporal Support

1. Go to [support.temporal.io](https://support.temporal.io/).
2. If prompted, log in to Temporal Cloud using the same method you normally use (e.g., Google, Microsoft, email-password, or other methods).
3. You will be presented with a screen where you can view open and closed tickets for your Temporal account, as well as submit a new ticket.

To request assistance from Temporal Support, see [Create a ticket](#support-ticket).

### Create a Ticket {/* #support-ticket */}

:::info

This procedure applies only to Temporal Cloud customers whose contracts include paid support.
If you need assistance and don't have paid support, post your request in the [Temporal Community Forum](https://community.temporal.io) or the `#support-cloud` channel of the [Temporal workspace](https://t.mp/slack) in Slack.

:::

To create a ticket in the Temporal Support Portal:

1. Go to [support.temporal.io](https://support.temporal.io/).
2. If prompted, log in to Temporal Cloud using the same method you normally use (e.g., Google, Microsoft, email-password, or other methods).
3. Click the **Create Ticket** button in the top right corner.
4. On the **Submit a ticket** page, enter the details of your request into the form. **Name**, **Subject**, and **Description** are required.
5. At the bottom of the form, choose **Submit**.

## Developer resources {/* #developer-resources */}

Temporal offers developer resources and a variety of hands-on tutorials to get you started and learn more advanced Temporal concepts.

- [Get started with Temporal](https://learn.temporal.io/getting_started): Start your journey with Temporal with this guide that helps you set up your development environment, run an existing Temporal app, and then build your first app from scratch using our SDKs.
- [Courses](https://learn.temporal.io/courses): Learn and apply Temporal concepts in our free, self-paced, hands-on courses.
- [Tutorials](https://learn.temporal.io/tutorials): Apply Temporal concepts to build real-world applications with these hands-on tutorials.
- [Example applications](https://learn.temporal.io/examples): Explore example applications that use Temporal and gain a clearer understanding of how Temporal concepts work in a complex application.

---

## Understanding Temporal

Temporal offers an entirely new way to build scalable and reliable applications.

## Build Invincible Apps

In any complex system, failures are bound to happen.
Software engineers spend a lot of time ensuring that what they build can withstand potential failures.
Temporal makes your code execution reliable and durable by default.

Normally, if a crash occurs then the state of your application's execution is lost.
The application has no memory of what happened before the failure, requiring extensive error handling logic and complex recovery code to resume.
The process is time-consuming and error-prone, making it difficult to ensure reliability.

Temporal tracks the progress of your application.
If something goes wrong, like a power outage, it guarantees that your application can pick up right where it left off — it’s like having the ultimate autosave.
Offloading the responsibility of failure management from the application to the platform removes the need for extensive recovery coding, testing, and maintenance tasks.

### Durable Execution

Temporal is a Durable Execution Platform.
Durable Execution ensures that your application behaves correctly despite adverse conditions by guaranteeing that it will run to completion.
This shift simplifies the development process. If a failure or a crash happens, your business processes keep running seamlessly without interruptions.
Developers shift their focus to business logic rather than infrastructure concerns and create applications that are inherently scalable and maintainable.

Thousands of developers trust Temporal for use cases like order processing, customer onboarding, and payment handling because it enables them to build invincible applications that are resilient, durable, and _just work_.
With Temporal, your applications keep running, no matter what happens.

## Temporal Application: The Building Blocks

### Workflow

Conceptually, a Workflow is a sequence of steps.
You've likely encountered Workflows in your daily life, whether it's:

- Using a mobile app to transfer money
- Booking a vacation
- Filing an expense report
- Creating a new employee onboarding process
- Deploying cloud infrastructure
- Training an AI model

A Temporal Workflow is your business logic, defined in code, outlining each step in your process.

Temporal isn’t a no-code Workflow engine — it is **Workflows-as-Code**.
Instead of dragging and dropping steps in a visual interface, you write your Workflows in code in your favorite programming language, code editor, and other tools.
No-code engines eventually hit their limitations however, Temporal gives you full control and flexibility over your business processes.
This allows you to build exactly what you need.

### Activities

Activities are the individual units of work in your Workflow.
Activities are defined as either functions or methods, depending on the programming language.
Activities often involve interacting with the outside world, such as sending emails, making network requests, writing to a database, or calling an API, which are prone to failure.
You can call Activities directly from your Workflow code.

If an Activity fails, Temporal automatically retries it based on your configuration.
Since Activities often rely on external systems, transient issues can occur.
These include temporary but critical problems like network failures, timeouts, or service outages.
You have full control over how often and how many times these retries should happen for each Activity.

### SDK

Developers create Temporal applications by writing code, just like you would to create any other software.

A Temporal SDK (software development kit) is an open-source library that developers add to their application to use Temporal.
It provides everything needed to build Workflows, Activities, and various other Temporal features in a specific programming language.

Temporal offers seven SDKs: .NET, Go, Java, PHP, Python, Ruby, TypeScript.
Since Temporal supports multiple programming languages, you can mix-and-match between languages for polyglot teams.
You can easily add any Temporal SDK to your current projects without changing the tools you're already using to build and deploy.
Temporal fits right into your existing tech stack.

## Temporal Service

Temporal has two main parts:

1. Your application
2. The Temporal Service (a set of services and components)

At the heart of Temporal architecture is the Temporal Service, which provides durability, scalability, and reliability for your application.
Your application communicates with the Temporal Service and the Temporal Service oversees the execution of critical tasks such as making an API call, then records their completion.
It maintains a detailed history of each event, which it reliably persists to a database.

One of the biggest advantages of the Temporal Service is how it handles failures.
The Temporal Service maintains a meticulous record of every step in your Workflows.
By keeping a history of every step in your Workflow, it ensures that even if something goes wrong your Workflow can continue from the last successful point.
The Temporal Service knows exactly where to resume without losing any work.
This saves you from having to write complex error handling code or painstaking recovery mechanisms yourself.

You can run the Temporal Service on your own infrastructure or use Temporal Cloud, a managed service that handles operational overhead and offers scalability and expert support.

## Workers

The real strength of Temporal comes from the combination of your application and the Temporal Service.
Whenever your application needs to perform a task, like sending a notification or processing a payment, the Temporal Service orchestrates what needs to be done.
Workers, which are part of your application and provided by the Temporal SDK, then carry out the tasks defined in your Workflow.

The Worker polls the Temporal Service to see if there are tasks available and the Temporal Service matches the task with the Worker.
The Worker runs the Workflow code based on the details specified in the task.

This collaboration is crucial for building reliable, scalable, and durable applications.
You can run multiple Workers — often dozens, hundreds, or even thousands — to improve application performance and scalability.

A common misconception is that the Temporal Service runs your code.
In fact, the Worker runs your code and works with your data directly.
Temporal applications are secure by design.
Workflows and Activities are seamlessly deployed within your infrastructure, fully integrated into your application.
