:::

This behavior is consistent across all Temporal SDKs.
For language-specific examples and correct wrapping patterns, see the error handling guide for your SDK.

## Failures in Event History {/* #event-history */}

Failures are recorded in Event History, which provides a detailed record for debugging.

### Activity failures

An Activity Execution that completes results in three Events: `ActivityTaskScheduled`, `ActivityTaskStarted`, and `ActivityTaskCompleted`.

If an Activity fails and the Retry Policy does not cause it to retry, the Temporal Service adds an `ActivityTaskFailed` Event that contains the error details.
If an Activity times out, an `ActivityTaskTimedOut` Event is added instead.

While an Activity is running, `ActivityTaskScheduled` is the most recent Event visible for that Activity.
The `ActivityTaskStarted` Event is not written until the Activity Task closes, because the final retry attempt number (an attribute of `ActivityTaskStarted`) is not known until then.

You can view pending Activity Executions in the Web UI's Pending Activities section, which shows the Activity Type, current retry attempt, remaining attempts, and heartbeat information.

### Workflow Execution failures

An Activity failure does not directly cause a Workflow Execution failure.
If an Activity fails and the error propagates out of the Workflow function without being caught (or is caught and intentionally re-raised as an Application Failure), the Workflow Execution fails.

When a Workflow Execution fails, the Temporal Service adds a `WorkflowExecutionFailed` Event.
If the failure was caused by an unhandled Activity error, the `activityFailureInfo` is attached to that Event.

---

## Child Workflows

A Child Workflow Execution is a [Workflow Execution](/workflow-execution) that is spawned from within another Workflow in the same Namespace.

- [Go SDK Child Workflow feature guide](/develop/go/workflows/child-workflows)
- [Java SDK Child Workflow feature guide](/develop/java/workflows/child-workflows)
- [PHP SDK Child Workflow feature guide](/develop/php/workflows/child-workflows)
- [Python SDK Child Workflow feature guide](/develop/python/workflows/child-workflows)
- [TypeScript SDK Child Workflow feature guide](/develop/typescript/workflows/child-workflows)
- [.NET SDK Child Workflow feature guide](/develop/dotnet/workflows/child-workflows)
- [Ruby SDK Child Workflow feature guide](/develop/ruby/workflows/child-workflows)
- [Rust SDK Child Workflow feature guide](/develop/rust/workflows/child-workflows)

A Workflow Execution can be both a Parent and a Child Workflow Execution because any Workflow can spawn another Workflow.

<CaptionedImage
    src="/diagrams/parent-child-workflow-execution-relationship.svg"
    title="Parent and Child Workflow Execution entity relationship"
    />

A Parent Workflow Execution must await on the Child Workflow Execution to spawn.
The Parent can optionally await on the result of the Child Workflow Execution.
Consider the Child's [Parent Close Policy](/parent-close-policy) if the Parent does not await on the result of the Child, which includes any use of Continue-As-New by the Parent.

:::note

Child Workflows do not carry over when the Parent uses [Continue-As-New](/workflow-execution/continue-as-new).
This means that if a Parent Workflow Execution uses Continue-As-New, any ongoing Child Workflow Executions will not be retained in the new continued instance of the Parent.

:::

When a Parent Workflow Execution reaches a Closed status, the Temporal Service propagates Cancellation Requests or Terminations to Child Workflow Executions depending on the Child's [Parent Close Policy](/parent-close-policy).

If a Child Workflow Execution uses Continue-As-New, from the Parent Workflow Execution's perspective the entire chain of Runs is treated as a single execution.

<CaptionedImage
    src="/diagrams/parent-child-workflow-execution-with-continue-as-new.svg"
    title="Parent and Child Workflow Execution entity relationship with Continue As New"
    />

## When to use Child Workflows

There is no reason to use Child Workflows just for code organization.
You can use object oriented structure and other code organization techniques to deal with complexities.
It is typically recommended to start from a single Workflow Definition if your problem has bounded size in terms of the number of Activity Executions and processed Signals.
It is simpler than multiple asynchronously communicating Workflows.

However, there are several valid reasons for using Child Workflows.

### Create a separate service

Because a Child Workflow Execution can be processed by a completely separate set of [Workers](/workers#worker) than the Parent Workflow Execution, it can act as an entirely separate service.
However, this also means that a Parent Workflow Execution and a Child Workflow Execution do not share any local state.
As all Workflow Executions, they can communicate only via asynchronous [Signals](/sending-messages#sending-signals).

### Partition problems into smaller chunks

An individual Workflow Execution has an [Event History](/workflow-execution/event#event-history) size limit, which imposes a couple of considerations for using Child Workflows.

On one hand, because Child Workflow Executions have their own Event Histories, they are often used to partition large workloads into smaller chunks.
For example, a single Workflow Execution does not have enough space in its Event History to spawn 100,000 [Activity Executions](/activity-execution).
But a Parent Workflow Execution can spawn 1,000 Child Workflow Executions that each spawn 1,000 Activity Executions to achieve a total of 1,000,000 Activity Executions.

However, because a Parent Workflow Execution Event History contains [Events](/workflow-execution/event#event) that correspond to the status of the Child Workflow Execution, a single Parent should not spawn more than 1,000 Child Workflow Executions.

In general, however, Child Workflow Executions result in more overall Events recorded in Event Histories than Activities.
Because each entry in an Event History is a _cost_ in terms of compute resources, this could become a factor in very large workloads.
Therefore, we recommend starting with a single Workflow implementation that uses Activities until there is a clear need for Child Workflows.

### Represent a single resource

As all Workflow Executions, a Child Workflow Execution can create a one to one mapping with a resource.
It can be used to manage the resource using its ID to guarantee uniqueness.
For example, a Workflow that manages host upgrades could spawn a Child Workflow Execution per host (hostname being a Workflow ID) and use them to ensure that all operations on the host are serialized.

### Periodic logic execution

A Child Workflow can be used to execute some periodic logic without overwhelming the Parent Workflow Event History.
In this scenario, the Parent Workflow starts a Child Workflow which executes periodic logic calling [Continue-As-New](/workflow-execution/continue-as-new) as many times as needed, then completes.
From the Parent point of view, it is just a single Child Workflow invocation.

### Child Workflow versus an Activity

Child Workflow Executions and Activity Executions are both started from Workflows, so you might feel confused about when to use which.
Here are some important differences:

- A Child Workflow has access to all Workflow APIs but is subject to the same [deterministic constraints](/workflow-definition#deterministic-constraints) as other Workflows.
  An Activity has the inverse pros and cons—no access to Workflow APIs but no Workflow constraints.
- A Child Workflow Execution can continue on if its Parent is canceled with a [Parent Close Policy](/parent-close-policy) of `ABANDON`.
  An Activity Execution is _always_ canceled when its Workflow Execution is canceled.
  (It can react to a cancellation Signal for cleanup.)
  The decision is roughly analogous to spawning a child process in a terminal to do work versus doing work in the same process.
- Temporal tracks all state changes within a Child Workflow Execution in Event History.
  Only the input, output, and retry attempts of an Activity Execution is tracked.

A Workflow models composite operations that consist of multiple Activities or other Child Workflows.
An Activity usually models a single operation on the external world.

Our advice: **When in doubt, use an Activity.**

---

## Parent Close Policy

This page discusses [Parent Close Policy](#parent-close-policy).

## What is a Parent Close Policy? {/* #parent-close-policy */}

A Parent Close Policy determines what happens to a Child Workflow Execution if its Parent changes to a Closed status (Completed, Failed, or Timed out).

- [How to set a Parent Close Policy using the Go SDK](/develop/go/workflows/child-workflows#parent-close-policy)
- [How to set a Parent Close Policy using the Java SDK](/develop/java/workflows/child-workflows#parent-close-policy)
- [How to set a Parent Close Policy using the PHP SDK](/develop/php/workflows/child-workflows#parent-close-policy)
- [How to set a Parent Close Policy using the Python SDK](/develop/python/workflows/child-workflows#parent-close-policy)
- [How to set a Parent Close Policy using the TypeScript SDK](/develop/typescript/workflows/child-workflows#parent-close-policy)
- [How to set a Parent Close Policy using the .NET SDK](/develop/dotnet/workflows/child-workflows#parent-close-policy)
- [How to set a Parent Close Policy using the Rust SDK](/develop/rust/workflows/child-workflows#parent-close-policy)

There are three possible values:

- **Abandon:** the Child Workflow Execution is not affected.
- **Request Cancel:** a Cancellation request is sent to the Child Workflow Execution.
- **Terminate** (default): the Child Workflow Execution is forcefully Terminated.

[`ParentClosePolicy`](https://github.com/temporalio/api/blob/c1f04d0856a3ba2995e92717607f83536b5a44f5/temporal/api/enums/v1/workflow.proto#L44) proto definition.

Each Child Workflow Execution may have its own Parent Close Policy.
This policy applies only to Child Workflow Executions and has no effect otherwise.

<CaptionedImage
    src="/diagrams/parent-close-policy.svg"
    title="Parent Close Policy entity relationship"
    />

You can set policies per child, which means you can opt out of propagating terminates / cancels on a per-child basis.
This is useful for starting Child Workflows asynchronously (see [relevant issue here](https://community.temporal.io/t/best-way-to-create-an-async-child-workflow/114) or the corresponding SDK docs).

---

## Context Propagation

Context propagation lets you pass custom key-value data from a Client to Workflows, and from Workflows to Activities and Child Workflows, without threading values through every function signature.

Common use cases:

- Propagating distributed tracing IDs (e.g., OpenTelemetry trace context)
- Passing tenant IDs for multi-tenant applications
- Forwarding auth tokens or request-scoped metadata

Each SDK provides a **context propagator** interface you implement to control which values are injected and extracted. You register propagators on the Client, and the SDK calls them automatically at every boundary.

## Implementing Context Propagation

Here are SDK-specific guides:

- [Go](/develop/go/best-practices/context-propagation)

---

## Codec Server

A Codec Server is an HTTP/HTTPS server that you host and operate. It runs your [Payload Codec](/payload-codec) logic to
encode and decode [Payloads](/dataconversion#payload) on behalf of the Temporal CLI and Web UI. The Codec Server is
independent of the Temporal Service. Encryption keys and codec logic remain in your environment.

For setup instructions, see [Codec Server setup](/production-deployment/data-encryption#codec-server-setup).

## Why use a Codec Server

When you apply a custom [Payload Codec](/payload-codec) for encryption or compression, data stored in the Temporal
Service is encoded. The Temporal Service never has access to your encryption keys, so it cannot decode this data.
Without a Codec Server, the Web UI and CLI display raw encoded payloads.

A Codec Server solves this by giving the Web UI and CLI a way to decode payloads on demand, without exposing keys to the
Temporal Service. Common reasons to run a Codec Server include:

- **Debugging Workflows.** View decoded Workflow inputs, outputs, and Event History in the Web UI instead of reading
  base64-encoded or encrypted blobs.
- **Operating from the CLI.** Use commands like `temporal workflow show` and `temporal workflow execute` with readable
  data, even when payloads are encrypted at rest.
- **Encoding inputs from the UI and CLI.** When you start or signal a Workflow from the Web UI or CLI, the Codec Server
  can encode the input before it reaches the Temporal Service, so the Temporal Service never sees plaintext (the input
  still travels from your browser or CLI to the Codec Server, which is why HTTPS matters in any non-loopback
  deployment).
- **Compliance and access control.** Because the Codec Server runs in your environment, you control who can decode
  payloads and under what conditions. You can layer authorization on top of the decode endpoint to restrict access per
  user or per Namespace.

## How a Codec Server works

A Codec Server follows the Temporal
[Codec Server Protocol](https://github.com/temporalio/samples-go/tree/main/codec-server#codec-server-protocol). It
exposes two HTTP POST endpoints:

- **`/encode`** accepts plaintext payloads and returns encoded payloads. Used for sending payloads.
- **`/decode`** accepts encoded payloads and returns decoded payloads. Used for retrieving payloads.

Both endpoints receive and respond with a JSON body containing a `payloads` array of [Payload](/dataconversion#payload)
objects. The Codec Server passes each payload through your [Payload Codec](/payload-codec), which applies the same
encoding or decoding logic that your Workers use.

<CaptionedImage
  src="/diagrams/codec-server.svg"
  srcDark="/diagrams/codec-server-dark.svg"
  width="100%"
  title="Codec Server"
/>

When the Web UI or CLI needs to display decoded data, it sends the encoded payloads to your Codec Server's `/decode`
endpoint. The Codec Server decodes the payloads and returns them to the client. The Temporal Service never sees the
decoded data.

The `/encode` endpoint works in the other direction. When you start a Workflow or send a Signal from the Web UI or CLI,
the input is sent to the Codec Server's `/encode` endpoint first, so data reaches the Temporal Service in its encoded
form.

Your Codec Server should use the same Payload Codec implementation as your Workers to ensure consistent encoding and
decoding.

## Codec Server with External Storage {/* #external-storage */}

When your Workers and Clients use [External Storage](/external-storage), your storage drivers replace some payloads in
the Event History with small references that point to data in an external store like Amazon S3. The Temporal Service and
the Web UI only see these references, not the actual payload data. This is further complicated by setups where you run
Codecs in proxy that encode payloads after the Data Converter has returned on the Worker. Your Codec Server must be able
to handle downloading and decoding in the correct order for you to be able to view the Workflow data in the UI or CLI.

To support External Storage, create a handler using `NewPayloadHTTPHandler` with `PayloadHTTPHandlerOptions`. The options
accept your storage drivers, your pre-storage codecs (the Payload Codecs configured in your Worker's Data Converter),
and any post-storage codecs (codecs applied by a proxy after external storage). The handler applies them in the correct
order across all endpoints automatically. When you configure the handler with storage drivers, the existing endpoints
become storage-aware and a new `/download` endpoint becomes available:

:::caution

`NewPayloadHTTPHandler` runs the full encode-store-encode and decode-retrieve-decode pipeline. Do not use it as a target
for a remote Data Converter or remote codec on your Workers. For remote codecs, use `NewPayloadCodecHTTPHandler`
separately. If you need both, set up `NewPayloadHTTPHandler` for the Web UI and CLI alongside
`NewPayloadCodecHTTPHandler` for your Workers, and configure both with the same codecs.

:::

- **`/download`** retrieves the actual payload data from external storage and decodes it through the Payload Codec. This
  endpoint is used internally by `/decode` when it encounters storage references, but you can also call it directly from the Web UI
  to retrieve the decoded payload. The Temporal Web UI uses this endpoint when you click to view the full payload for a
  storage reference.
- **`/decode`** still decodes encoded payloads, but also handles storage references. By default, `/decode` uses the
  download logic internally to retrieve and decode any storage references in the request alongside regular payloads.
  With the `?preserveStorageRefs=true` query parameter, `/decode` skips retrieval and returns storage references as-is.
- **`/encode`** applies the Payload Codec, then uploads payloads that exceed the size threshold to external storage and
  replaces them with reference tokens.

<CaptionedImage
  src="/diagrams/codec-server-with-external-storage.svg"
  srcDark="/diagrams/codec-server-with-external-storage-dark.svg"
  width="100%"
  title="Codec Server with External Storage"
/>

The following example walks through how all three endpoints work together:

1. A user starts a Workflow from the CLI with a plaintext input. The CLI sends the input to the Codec Server's `/encode`
   endpoint.
2. The Codec Server encodes the payload through the Payload Codec. The encoded payload exceeds the storage threshold,
   so the Codec Server uploads it to external storage and returns a small reference token.
3. The CLI sends the reference token to the Temporal Service, which stores it in the Event History.
4. Later, a user views the Workflow in the Web UI. The Web UI retrieves the Event History from the Temporal Service and
   sends the payloads to the Codec Server's `/decode` endpoint with the `?preserveStorageRefs=true` query parameter.
5. The Codec Server decodes any non-reference payloads through the Payload Codec, but returns storage references as-is.
   The Web UI displays the reference metadata, indicating the payload is stored externally.
6. The user clicks to view the full payload. The Web UI sends the storage reference to the `/download` endpoint.
7. The Codec Server retrieves the encoded payload from external storage, decodes it through the Payload Codec, and
   returns the plaintext result to the Web UI.

## Codec Server vs. Payload Codec

A Codec Server runs a [Payload Codec](/payload-codec) internally, so the two are directly connected. The difference is
where the codec logic runs and who calls it.

|                                   | Payload Codec                                                                                       | Codec Server                                                                                            |
| --------------------------------- | --------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| **Purpose**                       | Encodes and decodes Payloads. Applies encryption, compression, or other byte-level transformations. | Hosts a Payload Codec as an HTTP service so the Web UI and CLI can encode and decode Payloads remotely. |
| **Runs where**                    | In-process, inside your Workers and Clients. Also runs inside the Codec Server.                     | As a standalone HTTP service in your environment, with a Payload Codec inside it.                       |
| **Called by**                     | The Temporal SDK, automatically on every serialization and deserialization.                         | The Web UI and CLI, over HTTP, when a user views or submits Payload data.                               |
| **Has access to encryption keys** | Yes. Keys are available in the Worker or Client process.                                            | Yes. Must be configured with the same keys the Payload Codec uses.                                      |

You implement the transformation logic once in a Payload Codec, then host that logic in a Codec Server so the Web UI and
CLI can use it remotely.

## Securing a Codec Server

Because a Codec Server can decode sensitive data, treat it with the same trust as a Worker. Anyone who can call it has
effective decrypt access. Use HTTPS for any deployment that is not strictly loopback (`localhost`).

### Network-level restrictions

Restrict network access to the Codec Server. The Web UI can communicate with a Codec Server that is only accessible on
`localhost`, so running the Codec Server locally is a viable security pattern. For team access, place the Codec Server
behind a VPN.

### Authentication

When the Codec Server is accessible beyond `localhost`, authenticate requests to verify the identity of the caller. The
Web UI supports two approaches:

**Include cross-origin credentials (recommended).** Enable **Include cross-origin credentials** in the Web UI Codec
Server settings. The browser sends cookies scoped to the Codec Server's domain with each request. Your Codec Server must
have its own authentication mechanism (its own login page and session cookies), so the user must have independently
authenticated with the Codec Server. This is the recommended approach because the Codec Server maintains its own auth
boundary, separate from the Temporal UI.

**Pass access token.** Enable **Pass access token** in the Web UI Codec Server settings. The Web UI includes the same
JSON Web Token (JWT) the user used to log into the Temporal UI in the `Authorization` header of each request. Your Codec
Server validates the token signature against the OpenID Connect (OIDC) provider's JSON Web Key Set (JWKS) endpoint. On
Temporal Cloud, verify against the
[Temporal Cloud JWKS endpoint](https://login.tmprl.cloud/.well-known/jwks.json). On a self-hosted Temporal Service, the
token comes from whatever auth provider you have [configured for the Web UI](/references/web-ui-configuration#auth).
This approach requires less setup but reuses the same token across the Temporal UI and the Codec Server.

:::note

If you have a step in your process for token validation to ensure access isn't granted to the wrong token, you can validate the `audience` claim with:

```bash
"aud": [
  "https://saas-api.tmprl.cloud"
]
```

:::

### Namespace-level authorization

Authentication identifies the caller, but does not confirm the caller is authorized to decode payloads for a specific
Namespace. Each request from the Web UI includes an `X-Namespace` header identifying the Namespace. To enforce
Namespace-level access control, your Codec Server must enforce an additional check on whether the authenticated user has
permissions for the requested Namespace. This applies regardless of which authentication approach you use.

### Key management

You may also need [key management infrastructure](/key-management) to share encryption keys between your Workers and the
Codec Server.

## SDK Codec Server samples

Most Temporal SDKs provide example Codec Server implementations:

- [Go](https://github.com/temporalio/samples-go/tree/main/codec-server)
- [Java](https://github.com/temporalio/sdk-java/tree/master/temporal-remote-data-encoder)
- [Python](https://github.com/temporalio/samples-python/blob/main/encryption/codec_server.py) | [Python with External Storage](https://github.com/temporalio/samples-python/tree/main/external_storage)
- [TypeScript](https://github.com/temporalio/samples-typescript/blob/main/encryption/src/codec-server.ts)
- [.NET](https://github.com/temporalio/samples-dotnet/blob/main/src/Encryption/CodecServer/Program.cs)

---

## How does Temporal handle application data?

This guide provides an overview of data handling using a Data Converter on the Temporal Platform.

Data Converters in Temporal are SDK components that handle the serialization and encoding of data entering and exiting a Temporal Service.
Workflow inputs and outputs need to be serialized and deserialized so they can be sent as JSON to a Temporal Service.

<CaptionedImage
    src="/diagrams/default-data-converter.svg"
    title="Data Converter encodes and decodes data"
    />

The Data Converter encodes data from your application to a [Payload](/dataconversion#payload) before it is sent to the Temporal Service in the Client call.
When the Temporal Server sends the encoded data back to the Worker, the Data Converter decodes it for processing within your application.
This ensures that all your sensitive data exists in its original format only on hosts that you control.

Data Converter steps are followed when data is sent to a Temporal Service (as input to a Workflow) and when it is returned from a Workflow (as output).
Due to how Temporal provides access to Workflow output, this implementation is asymmetric:

- Data encoding is performed automatically using the default converter provided by Temporal or your custom Data Converter when passing input to a Temporal Service. For example, plain text input is usually serialized into a JSON object.
- Data decoding may be performed by your application logic during your Workflows or Activities as necessary, but decoded Workflow results are never persisted back to the Temporal Service. Instead, they are stored encoded on the Temporal Service, and you need to provide an additional parameter when using [`temporal workflow show`](/cli/command-reference/workflow#show) or when browsing the Web UI to view output.
