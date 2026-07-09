
The Worker Service runs background processing for the replication queue, system Workflows, and (in versions older than 1.5.0) the Kafka visibility processor.

    Worker Service

It talks to the Frontend Service.

- It uses port 6939 for membership-related communication.

Ports are configurable in the Temporal Service configuration.

## What is a Retention Period? {/* #retention-period */}

Retention Period is the duration for which the Temporal Service stores data associated with closed Workflow Executions on a Namespace in the Persistence store.

- [How to set the Retention Period for a Namespace](/cli/command-reference/operator#create)
- [How to set the Retention Period for a Namespace using the Go SDK](/develop/go/client/namespaces)
- [How to set the Retention Period for a Namespace using the Java SDK](/develop/java/client/namespaces)

A Retention Period applies to all closed Workflow Executions within a [Namespace](/namespaces) and is set when the Namespace is registered.

The Temporal Service triggers a Timer task at the end of the Retention Period that cleans up the data associated with the closed Workflow Execution on that Namespace.

The minimum Retention Period is 1 day.
On Temporal Service version 1.18 and later, the maximum Retention Period value for Namespaces can be set to anything over the minimum requirement of 1 day. Ensure that your Persistence store has enough capacity for the storage.
On Temporal Service versions 1.17 and earlier, the maximum Retention Period you can set is 30 days.
Setting the Retention Period to 0 results in the error _A valid retention period is not set on request_.

If you don't set the Retention Period value when using the [`temporal operator namespace create`](/cli/command-reference/operator#create) command, it defaults to 3 days.
If you don't set the Retention Period value when using the Register Namespace Request API, it returns an error.

When changing the Retention Period (with [`temporal operator namespace update`](/cli/command-reference/operator#update) or the `UpdateNamespace` API), the new duration applies to Workflow Executions that close after the change is saved.

:::info

Changing the Retention Period does NOT affect existing closed Workflow Executions: they retain their original cleanup timers based on the Retention Period that was in effect when they closed.

:::

### Manual cleanup of closed Workflow Executions

For cases where you need to remove closed Workflow Executions before their retention timer expires, you can use [`temporal workflow delete`](/cli/command-reference/workflow#delete) or the `DeleteWorkflowExecution` command.
This is particularly useful along with reducing the Retention Period to clean up previously closed Workflow Executions to reduce storage costs.

---

## Temporal Service configuration

This page discusses the following:

- [Static Configuration](#static-configuration)
- [Dynamic Configuration](#dynamic-configuration)
- [Security Configuration](#temporal-cluster-security-configuration)
- [Observability](#monitoring-and-observation)

## What is Temporal Service configuration? {/* #cluster-configuration */}

Temporal Service configuration is the setup and configuration details of your self-hosted Temporal Service, defined using YAML.
You must define your Temporal Service configuration when setting up your self-hosted Temporal Service.

For details on using Temporal Cloud, see [Temporal Cloud documentation](/cloud).

Temporal Service configuration is composed of two types of configuration: [Static configuration](#static-configuration) and [Dynamic configuration](#dynamic-configuration).

### Static configuration

Static configuration contains details of how the Temporal Service should be set up.
The static configuration is read just once and used to configure service nodes at startup.
Depending on how you want to deploy your self-hosted Temporal Service, your static configuration must contain details for setting up:

- Temporal Services—Frontend, History, Matching, Worker
- Membership ports for the Temporal Services
- Persistence (including History Shard count), Visibility, Archival store setups.
- TLS, authentication, authorization
- Server log level
- Metrics
- Temporal Service metadata
- Dynamic config Client

Static configuration values cannot be changed at runtime.
Some values, such as the Metrics configuration or Server log level can be changed in the static configuration but require restarting the Temporal Service for the changes to take effect.

For details on static configuration keys, see [Temporal Service configuration reference](/references/configuration).

For static configuration examples, see [https://github.com/temporalio/temporal/tree/main/config](https://github.com/temporalio/temporal/tree/main/config).

### Dynamic configuration

Dynamic configuration contains configuration keys that you can update in your Temporal Service setup without having to restart the server processes.

All dynamic configuration keys provided by Temporal have default values that are used by the Temporal Service.
You can override the default values by setting different values for the keys in a YAML file and setting the [dynamic configuration client](/references/configuration#dynamicconfigclient) to poll this file for updates.
Setting dynamic configuration for your Temporal Service is optional.

Setting overrides for some configuration keys updates the Temporal Service configuration immediately.
However, for configuration fields that are checked at startup (such as thread pool size), you must restart the server for the changes to take effect.

Use dynamic configuration keys to fine-tune your self-deployed Temporal Service setup.

For details on dynamic configuration keys, see [Dynamic configuration reference](/references/dynamic-configuration).

For dynamic configuration examples, see [https://github.com/temporalio/temporal/tree/master/config/dynamicconfig](https://github.com/temporalio/temporal/tree/master/config/dynamicconfig).

## What is Temporal Service security configuration? {/* #temporal-cluster-security-configuration */}

Secure your Temporal Service (self-hosted and Temporal Cloud) by encrypting your network communication and setting authentication and authorization protocols for API calls.

For details on setting up your Temporal Service security, see [Temporal Platform security features](/security).

### mTLS encryption

Temporal supports Mutual Transport Layer Security (mTLS) to encrypt network traffic between services within a Temporal Service, or between application processes and a Temporal Service.

On the self-hosted Temporal Service, configure mTLS in the `tls` section of the [Temporal Service configuration](/references/configuration#tls).
mTLS configuration is a [static configuration](#static-configuration) property.

You can then use either the [`WithConfig`](/references/server-options#withconfig) or [`WithConfigLoader`](/references/server-options#withconfigloader) server option to start your Temporal Service with this configuration.

The mTLS configuration includes two sections that serve to separate communication within a Temporal Service and client calls made from your application to the Temporal Service.

- `internode`: configuration for encrypting communication between nodes within the Temporal Service.
- `frontend`: configuration for encrypting the public endpoints of the Frontend Service.

Setting mTLS for `internode` and `frontend` separately lets you use different certificates and settings to encrypt each section of traffic.

### Using certificates for Client connections

Use CA certificates to authenticate client connections to your Temporal Service.

On Temporal Cloud, you can [set your CA certificates in your Temporal Cloud settings](/cloud/certificates) and use the end-entity certificates in your client calls.

On the self-hosted Temporal Service, you can restrict access to Temporal Service endpoints by using the `clientCAFiles` or `clientCAData` property and the [`requireClientAuth`](/references/configuration#tls) property in your Temporal Service configuration.
These properties can be specified in both the `internode` and `frontend` sections of the [mTLS configuration](/references/configuration#tls).
For details, see the [tls configuration reference](/references/configuration#tls).

### Server name specification

On the self-hosted Temporal Service, you can specify `serverName` in the `client` section of your mTLS configuration to prevent spoofing and [MITM attacks](https://en.wikipedia.org/wiki/Man-in-the-middle_attack).

Entering a value for `serverName` enables established connections to authenticate the endpoint.
This ensures that the server certificate presented to any connected client has the specified server name in its CN property.

This measure can be used for `internode` and `frontend` endpoints.

For more information on mTLS configuration, see [tls configuration reference](/references/configuration#tls).

### Authentication and authorization

{/* commenting this very generic explanation out. Can include it back in if everyone feels strongly.
**Authentication** is the process of verifying users who want to access your application are actually the users you want accessing it.
**Authorization** is the verification of applications and data that a user on your Temporal Service or application has access to. */}

Temporal provides authentication interfaces that can be set to restrict access to your data.
These protocols address three areas: servers, client connections, and users.

Temporal offers two plugin interfaces for authentication and authorization of API calls.

- [`ClaimMapper`](/self-hosted-guide/security#claim-mapper)
- [`Authorizer`](/self-hosted-guide/security#authorizer-plugin)

The logic of both plugins can be customized to fit a variety of use cases.
When plugins are provided, the Frontend Service invokes their implementation before running the requested operation.

## What is Temporal Service observability? {/* #monitoring-and-observation */}

You can monitor and observe performance with metrics emitted by your self-hosted Temporal Service or by Temporal Cloud.

Temporal emits metrics by default in a format that is supported by Prometheus.
Any metrics software that supports the same format can be used.
Currently, we test with the following Prometheus and Grafana versions:

- **Prometheus >= v2.0**
- **Grafana >= v2.5**

Temporal Cloud emits metrics through a Prometheus HTTP API endpoint, which can be directly used as a Prometheus data source in Grafana or to query and export Cloud metrics to any observability platform.

For details on Cloud metrics and setup, see the following:

- [Temporal Cloud metrics reference](/cloud/metrics/)
- [Set up Grafana with Temporal Cloud observability to view metrics](/cloud/metrics/prometheus-grafana#grafana-data-source-configuration)

On the self-hosted Temporal Service, expose Prometheus endpoints in your Temporal Service configuration and configure Prometheus to scrape metrics from the endpoints.
You can then set up your observability platform (such as Grafana) to use Prometheus as a data source.

For details on self-hosted Temporal Service metrics and setup, see the following:

- [Temporal Service OSS metrics reference](/references/cluster-metrics)
- [Set up Prometheus and Grafana to view SDK and self-hosted Temporal Service metrics](/self-hosted-guide/monitoring)

---

## Temporal Service

:::info
Please note an important update in our terminology.

We now refer to the Temporal Cluster as the Temporal Service.
:::

This guide provides a comprehensive technical overview of a Temporal Service.

A Temporal Service is the group of services, known as the [Temporal Server](/temporal-service/temporal-server), combined with [Persistence](/temporal-service/persistence) and [Visibility](/temporal-service/visibility) stores, that together act as a component of the Temporal Platform.

See the Self-hosted Temporal Service [production deployment guide](/self-hosted-guide) for implementation guidance.

<Components.CaptionedImage
src="/diagrams/temporal-cluster.svg"
title="A Temporal Service (Server + persistence)"
/>

---

## Visibility

This page discusses [Visibility](#visibility).

## What is Visibility? {/* #visibility */}

The term [Visibility](/visibility), within the Temporal Platform, refers to the subsystems and APIs that enable an operator to view, filter, and search for Workflow Executions that currently exist within a Temporal Service.

The [Visibility store](/self-hosted-guide/visibility) in your Temporal Service stores persisted Workflow Execution Event History data and is set up as a part of your [Persistence store](/temporal-service/persistence) to enable listing and filtering details about Workflow Executions that exist on your Temporal Service.

- [How to set up a Visibility store](/self-hosted-guide/visibility)

With Temporal Server v1.21, you can set up [Dual Visibility](/dual-visibility) to migrate your Visibility store from one database to another.

Support for separate standard and advanced Visibility setups will be deprecated from Temporal Server v1.21 onwards.
Check [Supported databases](/self-hosted-guide/visibility) for updates.

---

## What is Temporal?

Temporal is a scalable and reliable runtime for durable function executions called [Temporal Workflow Executions](/workflow-execution).

Said another way, it's a platform that guarantees the [Durable Execution](#durable-execution) of your application code.

It enables you to develop as if failures don't even exist.
Your application will run reliably even if it encounters problems, such as network outages or server crashes, which would be catastrophic for a typical application.
The Temporal Platform handles these types of problems, allowing you to focus on the business logic, instead of writing application code to detect and recover from failures.

<CaptionedImage
    src="/diagrams/temporal-system-simple.svg"
    title="The Temporal System"
    />

## Durable Execution {/* #durable-execution */}

Durable Execution in the context of Temporal refers to the ability of a Workflow Execution to maintain its state and progress even in the face of failures, crashes, or server outages.
This is achieved through Temporal's use of an [Event History](/workflow-execution/event#event-history), which records the state of a Workflow Execution at each step.
If a failure occurs, the Workflow Execution can resume from the last recorded event, ensuring that progress isn't lost.
This durability is a key feature of Temporal Workflow Executions, making them reliable and resilient.
It enables application code to execute effectively once and to completion, regardless of whether it takes seconds or years.

## What is the Temporal Platform? {/* #temporal-platform */}

The Temporal Platform consists of a [Temporal Service](/temporal-service) and [Worker Processes](/workers#worker-process).
Together these components create a runtime for Workflow Executions.

The Temporal Platform consists of a supervising software typically called the [Temporal Service](/temporal-service) and application code bundled as Worker Processes.
Together these components create a runtime for your application.

<CaptionedImage
    src="/diagrams/temporal-platform-simple.svg"
    title="The Temporal Platform"
    />

A Temporal Service consists of the [Temporal Server](https://github.com/temporalio/temporal), written in Go, and a database.

Our software as a service (SaaS) offering, Temporal Cloud, offers an alternative to hosting the Temporal Service yourself.

Worker Processes are hosted and operated by you and execute your code. Workers run using one of our SDKs.

<CaptionedImage
    src="/diagrams/temporal-platform-component-topology.svg"
    title="Basic component topology of the Temporal Platform"
    width="90%"
    />

## What is a Temporal Application? {/* #temporal-application */}

A Temporal Application is a set of [Temporal Workflow Executions](/workflow-execution).
Each Temporal Workflow Execution has exclusive access to its local state, executes concurrently to all other Workflow Executions, and communicates with other Workflow Executions and the environment via message passing.

A Temporal Application can consist of millions to billions of Workflow Executions.
Workflow Executions are lightweight
A Workflow Execution consumes few compute resources; in fact, if a Workflow Execution is suspended, such as when it is in a waiting state, the Workflow Execution consumes no compute resources at all.

**Reentrant Process**

A Temporal Workflow Execution is a Reentrant Process. A Reentrant Process is resumable, recoverable, and reactive.

- Resumable: Ability of a process to continue execution after execution was suspended on an _awaitable_.
- Recoverable: Ability of a process to continue execution after execution was suspended on a _failure_.
- Reactive: Ability of a process to react to external events.

Therefore, a Temporal Workflow Execution executes a [Temporal Workflow Definition](/workflow-definition), also called a Temporal Workflow Function, your application code, exactly once and to completion—whether your code executes for seconds or years, in the presence of arbitrary load and arbitrary failures.

## What is a Failure? {/* #failure */}

[Temporal Failures](/references/failures) are representations (in the SDKs and Event History) of various types of errors that occur in the system.

Failure handling is an essential part of development.
For more information, including the difference between application-level and platform-level failures, see [Handling Failure From First Principles](https://dominik-tornow.medium.com/handling-failures-from-first-principles-1ed976b1b869).
For the practical application of those concepts in Temporal, see [Failure Handling in Practice](https://temporal.io/blog/failure-handling-in-practice).

For languages that throw (or raise) errors (or exceptions), throwing an error that is not a Temporal Failure from a Workflow fails the Workflow Task (and the Task will be retried until it succeeds), whereas throwing a Temporal Failure (or letting a Temporal Failure propagate from Temporal calls, like an [Activity Failure](/references/failures#activity-failure) from an Activity call) fails the Workflow Execution.
For more information, see [Application Failure](/references/failures#application-failure).

---

## Dual Visibility

This page discusses [Dual Visibility](#dual-visibility).

## What is Dual Visibility? {/* #dual-visibility */}

Dual Visibility is a feature that lets you set a secondary Visibility store in addition to a primary store in your Temporal Service.
Setting up Dual Visibility is optional and can be used to [migrate your Visibility database](/self-hosted-guide/visibility#migrating-visibility-database) or create a backup Visibility store.

For example, if you have Cassandra configured as your Visibility database, you can set up a supported SQL database as your secondary Visibility store and gradually migrate your data to the secondary store before deprecating your primary one.

A Dual Visibility setup requires two Visibility store configurations:

- **Primary Visibility:** The primary Visibility store where Visibility data is written to and read from by default. The primary Visibility store is set with the `visibilityStore` configuration key in your Temporal Service.
- **Secondary Visibility:** A secondary storage for your Visibility data. The secondary Visibility store is set with the `secondaryVisibilityStore` configuration key in your Temporal Service.

For configuration details, see [Dual Visibility setup](/self-hosted-guide/visibility#dual-visibility).

The following combinations are allowed in a Dual Visibility setting.

| Primary                     | Secondary                       |
| --------------------------- | ------------------------------- |
| Standard (Cassandra or SQL) | Advanced (SQL or Elasticsearch) |
| Advanced (SQL)              | Advanced (SQL)                  |
| Advanced (Elasticsearch)    | Advanced (Elasticsearch)        |

With Dual Visibility, you can read from only one Visibility store at a time, but can configure your Temporal Service to write to primary only, secondary only, or to both primary and secondary Visibility stores.
When migrating from one Visibility store database to another, set up the database you want to migrate to as your secondary Visibility store.

You can plan your migration using specific dynamic configuration keys that help you transition your read and write operations from the primary to the secondary Visibility store.
For details on migrating your Visibility store databases, see [Dual Visibility](/self-hosted-guide/visibility#dual-visibility).

---

## List Filter

This page discusses [List Filter](#list-filter).

## What is a List Filter? {/* #list-filter */}

The [Visibility](/temporal-service/visibility) List API requires you to provide a List Filter as an SQL-like string parameter.

A List Filter includes [Search Attribute](/search-attribute) names, Search Attribute values, and [operators](#supported-operators) so that it can retrieve a filtered list of Workflow Executions from the Visibility Store.

List Filter [Search Attribute](/search-attribute) names are case sensitive.
A single [Namespace](/namespaces) scopes each List Filter.

A List Filter using a time range provides a resolution of 1 ns on [Elasticsearch](/self-hosted-guide/visibility#elasticsearch) and 1 µs for [SQL databases](/self-hosted-guide/visibility).

### Supported operators

List Filters support the following operators:

- **`=, !=, >, >=, <, <=`**
- **`AND, OR, ()`**
- **`BETWEEN ... AND`**
- **`IN`**
- **STARTS_WITH**

:::note

The **ORDER BY** operator is currently not supported in Temporal Cloud.

The default ordering is: `ClosedTime DESC NULL FIRST`, `StartTime DESC`. {/* `RunID DESC` depends on which visibility store is used. */}

Custom Search Attributes of the `Text` type cannot be used in **ORDER BY** clauses.

:::

### Partial string match

There are different options for partial string matching when the type of the Search Attribute is [Text](#text) versus [Keyword](#keyword).

#### Text

`Text` Search Attributes support word-level search.
Both stored values and query strings are analyzed by the [Elasticsearch standard analyzer](https://www.elastic.co/guide/en/elasticsearch/reference/current/analysis-standard-analyzer.html), and the `=` operator returns a result if any query token matches any indexed token.

If you need exact matching on identifiers, UUIDs, or other structured strings, use `Keyword` instead.
See [Choose a string type](/search-attribute#choose-a-string-type).

##### Tokenization {/* #text-tokenization */}

The standard analyzer applies [Unicode word boundary rules](https://unicode.org/reports/tr29/) to split values into tokens.
All tokens are lowercased by the analyzer's lowercase filter.

Most punctuation and whitespace act as delimiters.
For example, `order-processing-v2` produces three tokens: `order`, `processing`, `v2`.

The following characters do **not** split when they appear between two letters or between two digits:

| Character | Example | Tokens |
| --- | --- | --- |
| Underscores (`_`) | `payment_retry_handler` | one token |
| Dots (`.`) | `com.example.workflows.ProcessOrder` | one token |
| Colons (`:`) | `alpha:bravo` | one token |
| Apostrophes (`'`) | `it's` | one token |

Dots and colons between digits also stay connected (`v1.2.3` → one token).
However, a dot or colon between a digit and a letter does split: `v1.ProcessOrder` → `v1`, `processorder`.

##### Search matching {/* #text-search-matching */}

The `=` operator on `Text` Search Attributes uses **OR matching**: the query string is tokenized using the same rules as above, and a result is returned if **any** query token matches **any** indexed token.

For example, if you have a custom `Text` Search Attribute named `Description` with either of the following values—

```
my-business-id-foobar
my business id foobar
```

—then the following List Filter matches—

```
Description = 'foobar'
```

—but a partial word does not:

```
// Doesn't match
Description = 'foo'
```

Because the query string is also tokenized, a query like `= "processing-v2"` is split into `processing` and `v2`, matching any workflow that contains **either** token.
This can return unexpected results when tokens are shared across different values.

:::note

Broader tokenizer and matching improvements for `Text` Search Attributes are being evaluated as part of future Visibility enhancements.

:::

#### Keyword

For Search Attributes of type `Keyword` like `WorkflowId`, perform partial string matching using STARTS_WITH for prefixes and BETWEEN for suffixes.

- `WorkflowId STARTS_WITH "order-"` matches Workflow Ids with the "order-" prefix, regardless of the following text.

  ```
  order-
  order-1234
  order-abracadabra
  order-~~~abracadabra
  ```

- `WorkflowId BETWEEN "order-" AND "order-~"` matches Workflow Ids that have characters after `order-` with ASCII values lower than `~` (126, the highest-value printable character), such as the following:

  ```
  order-
  order-1234
  order-abracadabra
  ```

  It does not match `order-~~`.

:::note Filter Composition Quick Reference

**Composition**

- Data types:
  - String literals with single or double quotes
  - Numbers (Integer and Floating Point)
  - Booleans
- Comparison: `=`, `!=`, `>`, `>=`, `<`, `<=`
- Expressions/Operators:
