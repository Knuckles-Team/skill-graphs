Your data is also protected with your encryption libraries and keys.
You maintain full control over the security of your application from end to end.

## Visibility

There are two tools provided by Temporal that allow you to see behind the scenes and interact with your Workflows.
These are powerful for debugging uses and provide real-time monitoring of your applications.

### Temporal UI

The Temporal UI is a browser-based user interface that allows you to see the progress of your application.
Also known as the Web UI, it can also help you to quickly isolate, debug, and resolve production problems.

<CaptionedImage src="/img/webui/workflow-details-page-hiw.avif" title="Recent Workflows page" />

### Temporal CLI

The Temporal CLI is a command-line interface tool for managing, monitoring, and debugging Temporal Applications.
Through your terminal, you can:

- Start a Workflow
- Trace the progress of a Workflow
- Cancel or terminate a Workflow
- And perform other operations

The Temporal CLI provides developers with direct access to a Temporal Service for local development purposes.

### Event History

With Temporal, your Workflows can seamlessly recover from crashes. This is made possible by the [Event History](https://docs.temporal.io/workflow-execution/event), a complete and durable log of everything that has happened in the lifecycle of a Workflow Execution, as well as the ability of the Temporal Service to durably persist the Events during [Replay](/workflow-execution#replay).

Temporal uses the Event History to record every step taken along the way. Each time your Workflow Definition makes an API call to execute an Activity or start a Timer for instance, it doesn’t perform the action directly. Instead, it sends a Command to the Temporal Service.

A Command is a requested action issued by a Worker to the Temporal Service after a Workflow Task Execution completes. The Temporal Service will act on these Commands such as scheduling an Activity or scheduling a timer. These Commands are then mapped to Events which are persisted in case of failure. For example, if the Worker crashes, the Worker uses the Event History to replay the code and recreate the state of the Workflow Execution to what it was immediately before the crash. It then resumes progress from the point of failure as if the failure never occurred.

For a deep dive into the Event History or Commands, visit the Temporal [Encyclopedia page](/encyclopedia/event-history) or enroll in one of [our courses](https://learn.temporal.io/courses/).

## Reliable as Gravity

Temporal provides effortless durability, allowing applications to run for days, weeks, or even years without interruption even if the underlying infrastructure fails.
This is what we call _Durable Execution_. Temporal also represents a paradigm shift in software development.
It's not just about making existing patterns more reliable; it's about enabling entirely new approaches to building complex, distributed systems.

Temporal simplifies state management and developers don't have to write tons of extra code to handle every possible thing that could go wrong.
With built-in scalability, Temporal ensures that your application runs smoothly, no matter its size or complexity.

:::tip

Follow one of our tutorials to [Get Started](https://learn.temporal.io/getting_started/) learning how to use a Temporal SDK.
Or, jump straight into an [Introduction to Temporal 101](https://learn.temporal.io/courses/temporal_101/) course.

Looking for more? Explore Temporal's [Resource Library](https://temporal.io/resources).
:::

---

## Temporal use cases and design patterns

This page provides an overview of how leading organizations leverage Temporal to solve real-world problems, general use cases, and architectural design patterns.

## Use Cases of Temporal in Production

Here are some examples where Temporal is most impactful and running in production at large organizations today. For more examples, see our [Temporal Use Cases](https://temporal.io/in-use) page.

### Transactions

Actions or activities involving two or more parties or things that reciprocally affect or influence each other. For example:

- [Payment processing at Stripe](https://temporal.io/resources/on-demand/stripe)
- [Money movement at Coinbase](https://temporal.io/in-use/coinbase)
- [Content management at Box](https://temporal.io/resources/case-studies/box)

### Business processes

A sequence of tasks that find their end in the delivery of a service or product to a client. For example:

- [Bookings at Turo](https://temporal.io/replay/videos/temporal-adoption-and-integration-at-turo)
- [Orders/logistics at Maersk](https://temporal.io/replay/videos/building-a-time-machine-for-the-logistics-industry)
- [Marketing Campaigns at AirBnb](https://medium.com/airbnb-engineering/journey-platform-a-low-code-tool-for-creating-interactive-user-workflows-9954f51fa3f8)
- [Human-in-the-loop at Checkr](https://temporal.io/in-use/checkr)

### Entity lifecycle

Complex long-running processes that accumulate state over time. For example:

- [Mortgage underwriting applications at ANZ](https://temporal.io/in-use/anz-story)
- [Menu versioning at Yum! Brands](https://temporal.io/replay-2023/videos/synchronizing-concurrent-workflows)

### Operations

An automated method for getting a repeatable, mundane task accomplished. For example:

- [Infrastructure services at DataDog](https://www.youtube.com/watch?v=Hz7ZZzafBoE)
- [Custom CI/CD at Netflix](https://temporal.io/replay-2023/videos/actor-workflows-reliably-orchestrating-thousands-of-flink-clusters-at)

### AI / ML and Data Engineering

AI and ML developers face challenges in system orchestration, such as managing complex data pipelines and job coordination across GPU resources.
Temporal's code-first approach helps build reliable services faster, making it popular among AI companies. For example:

- [Orchestrating video processing at Descript](https://temporal.io/blog/ai-ml-and-data-engineering-workflows-with-temporal#descript)
- [Automating data pipelines at Neosync](https://temporal.io/blog/ai-ml-and-data-engineering-workflows-with-temporal#neosync)

### AI Agents

AI Agents present new uses for Temporal, such as maintaining state over long periods and enabling seamless human intervention when needed.
Temporal ensures Durable Execution of tools, LLMs, and conversations, letting you focus on business logic instead of handling failures. For example:

- [Creating reliable, observable Agents at Lindy](https://temporal.io/resources/case-studies/lindy-reliability-observability-ai-agents-temporal-cloud)
- [Long-running, durable Agents at Dust](https://temporal.io/blog/how-dust-builds-agentic-ai-temporal)
- [Creating account summaries with Agents at ZoomInfo](https://temporal.io/resources/on-demand/account-summaries-gen-ai)

## General Use Cases

### Human in the Loop

"Human in the Loop" systems require human interaction for certain steps, such as customer onboarding, forms, or invoice approval.
These are event-driven systems with humans generating events, and may be challenging to implement due to timing or unreliable connections between the human to the rest of the system.
They can use schedules and timers to prompt for user input.

**Example**: [Background checks example using the Go SDK](https://learn.temporal.io/examples/go/background-checks/).

**Code Sample**: [Candidate acceptance example prompting for a response](https://learn.temporal.io/examples/go/background-checks/candidate-acceptance)

### Polyglot Systems

Modern development teams often work with different programming languages based on their expertise and project requirements. Temporal supports this through built-in multi-language capabilities, allowing teams to continue using their preferred languages while working together.

The example below showcases how Workflow Executions, written in different languages, can send messages to each other. Go, Java, PHP, and TypeScript SDKs are represented in this sample. It also shows how to properly propagate errors, including how to do so across Workflows written in different languages.

**Example**: [Polyglot example](https://github.com/temporalio/temporal-polyglot).

### Long Running Tasks

This use case is particularly relevant for scenarios like shopping cart Workflows in an eCommerce app, where you can handle long-running tasks efficiently without managing state in a separate database.
It processes one message at a time, ensuring each message is processed only once.

This approach addresses issues that can arise with long message processing times, which in other systems might cause consumer failover (typically with a default 5-minute message poll timeout) and potentially result in duplicate message processing by multiple consumers.
Temporal's ability to handle extended task durations makes it well-suited for such scenarios.
The [heartbeat](/encyclopedia/detecting-activity-failures#activity-heartbeat) feature allows you to know that an activity is still working, providing insight into the progress of long-running processes.

**Example**: [eCommerce example](https://learn.temporal.io/tutorials/go/build-an-ecommerce-app/).

**Code Sample**: [Temporal eCommerce](https://github.com/temporalio/temporal-ecommerce)

## Design Patterns

### Saga

The Saga pattern is a design pattern used to manage and handle failures in complex Workflows by breaking down a transaction into a series of smaller, manageable sub-transactions.
If a step in the Workflow fails, the Saga pattern compensates for this failure by executing specific actions to undo the previous steps.
This ensures that even in the event of a failure, the system can revert to a consistent state.

**Examples:**

- [Build a trip booking application in Python](https://learn.temporal.io/tutorials/python/trip-booking-app/).
- [Saga Pattern with Temporal Whitepaper](https://pages.temporal.io/download-saga-pattern-made-easy)
- [To choreograph or orchestrate your saga, that is the question](https://temporal.io/blog/to-choreograph-or-orchestrate-your-saga-that-is-the-question)
- [Saga Webinar](https://pages.temporal.io/on-demand-webinar-what-is-a-saga.html)

### State Machine

A state machine is a software design pattern used to modify a system’s behavior in response to changes in its state.
While state machines are widely used in software development, applying them to complex business processes can be a difficult undertaking.
Temporal simplifies the complexity of state machines by providing a structured approach to workflow development, avoiding the intricate state management code required for state machines.

**Example**: [State Machine Simplified Whitepaper](https://pages.temporal.io/download-state-machines-simplified.html)

:::tip

If you're interested in code to help get you started, check out our [Temporal Example Applications](https://learn.temporal.io/examples/), [Getting Started Tutorials](https://learn.temporal.io/getting_started/), or [Project-based Tutorials](https://learn.temporal.io/tutorials/).

:::

---

## Why Temporal?

Temporal solves many problems that developers face while building distributed applications.
But most of them revolve around these three themes:

- Reliable distributed applications
- Productive development paradigms and code structure
- Visible distributed application state

You can check out a list of [use cases for Temporal](/evaluate/use-cases-design-patterns) to better understand how it can fit into your system. Temporal supports things like AI agent orchestration, enabling durable execution of LLM calls, tool use, and complex AI workflows.

:::tip See Temporal in action
Watch the following video to see how Temporal ensures an order-fulfillment system can recover from various failures, from process crashes to unreachable APIs.

    <iframe width="560" height="315"
        src="https://www.youtube.com/embed/dNVmRfWsNkM?si=cfwAJgr2zaoro97P"
        title="YouTube video player"
        frameBorder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
        referrerPolicy="strict-origin-when-cross-origin" allowFullScreen></iframe>

:::

## Reliable execution

**How does Temporal make applications reliable?**

Temporal makes it easier for developers to build and operate reliable, scalable applications without sacrificing productivity.
The design of the system ensures that, once started, an application's main function executes to completion, whether that takes minutes, hours, days, weeks, or even years.
Temporal calls this _Durable Execution._

## Code structure

**How does Temporal simplify application code for software developers?**

By shifting the burden of failure handling from the application to the platform, there is less code for application developers to write, test, and maintain.
Temporal's programming model offers developers a way to express their business logic into coherent _Workflows_ that are much easier to develop than distributed code bases.

Choose the SDK that best suits your preferred programming language and start writing your business logic.
Integrate your favorite IDE, libraries, and tools into your development process.
Temporal also supports polyglot and idiomatic programming - which enables developers to leverage the strengths of various programming languages and integrate Temporal into existing codebases.
Developers achieve all of this without having to manage queues or complex state machines.

## State visibility

**How does Temporal make it easier to view the state of the application?**

Temporal provides out-of-the-box tooling that enables developers to see the state of their applications whenever they need to.
The Temporal CLI allows developers to manage, monitor, and debug Temporal applications effectively.
The browser-based Web UI lets you quickly isolate, debug, and resolve production problems.

---

## Getting started with Temporal

Temporal offers a range of SDKs to help you build Temporal applications.
The SDKs are available for .NET, Go, Java, PHP, Python, Ruby, TypeScript.

## Temporal Go SDK

Get started with the [Temporal Go SDK](https://learn.temporal.io/getting_started/go).

[](https://learn.temporal.io/getting_started/go)

## Temporal Java SDK

Get started with the [Temporal Java SDK](https://learn.temporal.io/getting_started/java).

[](https://learn.temporal.io/getting_started/java)

## Temporal PHP SDK

Get started with the [Temporal PHP SDK](https://learn.temporal.io/getting_started/php).

[](https://learn.temporal.io/getting_started/php)

## Temporal Python SDK

Get started with the [Temporal Python SDK](https://learn.temporal.io/getting_started/python).

[](https://learn.temporal.io/getting_started/python)

## Temporal TypeScript SDK

Get started with the [Temporal TypeScript SDK](https://learn.temporal.io/getting_started/typescript).

[](https://learn.temporal.io/getting_started/typescript)

---

## Temporal Docs

<HomePageHero />

---

## Integrations(Docs)

Browse integrations for Temporal SDKs and Temporal Cloud.
Filter by SDK, tag, or search to find what you need.

<IntegrationsGrid />

---

## Codecs and Encryption

The Temporal Service persists data from your Workflow Executions, including inputs, outputs, and results. To protect
sensitive data, use a [Payload Codec](/payload-codec) to encrypt payloads before they reach the Temporal Service. With
encryption enabled, data exists unencrypted only on the Client and the Worker process, on hosts that you control.

The following data is persisted in the Event History and can be encrypted:

- Inputs and outputs/results in your [Workflow](/workflow-execution), [Activity](/activity-execution), and [Child Workflow](/child-workflows)
- [Signal](/sending-messages#sending-signals) inputs
- [Memo](/workflow-execution#memo)
- Headers (verify if applicable to your SDK)
- [Query](/sending-messages#sending-queries) inputs and results
- Results of [Local Activities](/local-activity) and [Side Effects](/workflow-execution/event#side-effect)
- [Application errors and failures](/references/failures).
  Failure messages and call stacks are not encoded as codec-capable Payloads by default; you must explicitly enable
  encoding these common attributes on failures. For more details, see [Failure Converter](/failure-converter).

To view encrypted data in the Web UI and CLI, set up a [Codec Server](/codec-server). The following sections cover how
to set up a Codec Server and configure the Web UI and CLI to use it.

For encryption implementation examples, see the following samples:

- [Go](https://github.com/temporalio/samples-go/tree/main/encryption)
- [Java](https://github.com/temporalio/samples-java/tree/main/core/src/main/java/io/temporal/samples/encryptedpayloads)
- [Python](https://github.com/temporalio/samples-python/tree/main/encryption)
- [TypeScript](https://github.com/temporalio/samples-typescript/tree/main/encryption)
- [.NET](https://github.com/temporalio/samples-dotnet/tree/main/src/Encryption)

## Codec Server setup {/* #codec-server-setup */}

Use a Codec Server to programmatically decode your encoded [payloads](/dataconversion#payload).

A Codec Server is an HTTP server that uses your custom Codec logic to decode your data remotely.
The Codec Server is independent of the Temporal Service and decodes your encrypted payloads through predefined endpoints. You create, operate, and manage access to your Codec Server in your own environment.
When you configure a Codec Server endpoint in the Web UI or CLI, the Web UI and CLI use the remote endpoint to send and receive payloads from the Codec Server.
See [API contract requirements](#api-contract-specifications).

Decoded payloads can then be displayed in the Workflow Execution Event History on the Web UI. When you use a Codec Server, the decoded payloads are decoded and returned on the client side only. Payloads on the Temporal Service (whether on Temporal Cloud or self-hosted) remain encrypted.

Because you create, operate, and manage access to your Codec Server in your controlled environment, ensure that you consider the following:

- When you register a Codec Server endpoint with your Web UI, expect the Codec Server to receive multiple requests per Workflow Execution.
- Ensure that you secure access to your Codec Server. For details, see [Authorization](#authorization). You might need some form of [Key management infrastructure](/key-management) for sharing your encryption keys between the Workers and your Codec Server.
- You will need to enable [CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) on the HTTP/HTTPS endpoints in your Codec Server to receive requests from the Temporal Web UI.
- You may introduce latency in the Web UI when sending and receiving payloads to the Codec Server.

Your Codec Server should share logic with the custom [Payload Codec](/payload-codec) used elsewhere in your application.

### API contract specifications

When you create your Codec Server to handle requests from the Web UI, the following requirements must be met.

#### Endpoints

The Web UI and CLI send POST requests to the following endpoints on your Codec Server:

- `/decode` passes incoming payloads to the decode method in your Payload Codec.
- `/encode` passes incoming payloads to the encode method in your Payload Codec.
- `/download` retrieves and decodes payloads from [External Storage](/external-storage). This endpoint is only needed if
  your Workers use External Storage. See [Codec Server with External Storage](/codec-server#external-storage) for
  details.

For examples on how to create your Codec Server, see the following Codec Server implementation samples:

- [Go](https://github.com/temporalio/samples-go/tree/main/codec-server)
- [Java](https://github.com/temporalio/sdk-java/tree/master/temporal-remote-data-encoder)
- [Python](https://github.com/temporalio/samples-python/blob/main/encryption/codec_server.py)
- [TypeScript](https://github.com/temporalio/samples-typescript/blob/main/encryption/src/codec-server.ts)
- [.NET](https://github.com/temporalio/samples-dotnet/blob/main/src/Encryption/CodecServer/Program.cs)

You can also add a [verification step](#authorization) to check whether the incoming request has the required authorization to access the decode logic in your Payload Codec.

#### Headers

Each request from the Web UI to your Codec Server includes the following headers:

- `Content-Type: application/json`: Ensure that your Codec Server can accommodate this [MIME type](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types).

- `X-Namespace: {namespace}`: This is a custom HTTP Header. Ensure that the [CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) configuration in your Codec Server includes this header.

- [Optional] `Authorization: <credentials>`: Include this in your CORS configuration when enabling authorization with your Codec Server.

For details on setting up authorization, see [Authorization](#authorization).

#### Request body

The general specification for the `POST` request body contains payloads.
By default, all field values in your payload are base64 encoded, regardless of whether they are encrypted by your custom codec implementation.

The following example shows a sample `POST` request body with base64 encoding.

```json
{
  "payloads": [{
    "metadata": {
      "encoding": <base64EncodedEncodingHint>
    },
    "data": <encryptedPayloadData>
  }, ...]
}
```

#### CORS

By default, in cross-origin Fetch/XHR invocations, browsers will not send credentials.
Enable [Cross-Origin Resource Sharing (CORS)](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) requests on your Codec Server to receive HTTP/HTTPS requests from the Temporal Web UI.

At a minimum, enable the following responses from your Codec Server to allow requests coming from the Temporal Web UI:

- `Access-Control-Allow-Origin`
- `Access-Control-Allow-Methods`
- `Access-Control-Allow-Headers`

For example, for Temporal Cloud Web UI hosted at https://cloud.temporal.io, enable the following in your Codec Server:

- `Access-Control-Allow-Origin: https://cloud.temporal.io`
- `Access-Control-Allow-Methods: POST, GET, OPTIONS`
- `Access-Control-Allow-Headers: X-Namespace, Content-Type`

For details on what a sample request/response looks like from the Temporal Web UI, see [Sample Request/Response](#sample-requestresponse).
If setting authorization, include `Authorization` in your `Access-Control-Allow-Headers`.
For details on setting up authorization, see [Authorization](#authorization).

#### Authorization

It is important to establish how you will provide access to your Codec Server.
Because it is designed to decode potentially sensitive data with a single API call, access to a production Codec Server should be restricted.

Depending on your infrastructure and risk levels, it might be sufficient to restrict HTTP ingress to your Codec Server (such as by using a VPN like [WireGuard](https://www.wireguard.com/)).
The Temporal Web UI can communicate with a Codec Server that is only accessible on `localhost`, so this is a legitimate security pattern.
However, if your Codec Server is exposed to the internet at all, you will likely need an authentication solution.

If you are already using an organization-wide authentication provider, you should integrate it with your Codec Server. Remember, a Codec Server is just a standalone HTTP server, so you can use existing libraries for OAuth, [Auth0](https://auth0.com/), or any other protocol.
[This repository](https://github.com/pvsone/codec-cors-credentials) contains an example of using Auth0 to handle browser-based auth to a Codec Server.

To enable authorization from the Web UI (for both a self-hosted Temporal Service and Temporal Cloud), your Codec Server must be an HTTPS Server.

**Temporal Cloud**

The Temporal Cloud UI provides an option to pass access tokens (JWT) to your Codec Server endpoints.
Use the access tokens to validate access and then return decoded payloads from the Codec Server.

You can enable this by selecting **Pass access token** in your Codec Server endpoint interface where you add your endpoint.
Enabling this option in the Temporal Cloud UI adds an authorization header to each request sent to the Codec Server endpoint that you set.

In your Codec Server implementation, verify the signature on this access token (in your authorization header) against [our JWKS endpoint](https://login.tmprl.cloud/.well-known/jwks.json).

{/* Commenting this for now. _/}
{/_ If you want to unpack the claims in your token to add additional checks on whether the user has valid access to the Namespace and payloads they are trying to access, you can implement it using Auth0 SDKs, middleware, or one of the third-party libraries at JWT.io. */}

The token provided from Temporal Cloud UI contains the email identifier of the person requesting access to the payloads.
Based on the permissions you have provided to the user in your access control systems, set conditions in your Codec Server whether to return decoded payloads or just return the original encoded payloads.

**Self-hosted Temporal Service**

On a self-hosted Temporal Service, configure [authorization in the Web UI configuration](/references/web-ui-configuration#auth) in your Temporal Service setup.

With this enabled, you can pass access tokens to your Codec Server and validate the requests from the Web UI to the Codec Server endpoints that you set.
Note that with a self-hosted Temporal Service, you must explicitly configure authorization specifications for the Web UI and CLI.
