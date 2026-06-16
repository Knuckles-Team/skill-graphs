# Self-hosted LangSmith on GCP
Source: https://docs.langchain.com/langsmith/gcp-self-hosted

When running LangSmith on [Google Cloud Platform (GCP)](https://cloud.google.com/), [self-hosted](/langsmith/self-hosted) mode deploys a complete LangSmith platform with observability functionality.

This page provides:

* [Initial setup steps](#initial-setup) for deploying to GKE, configuring managed services, and setting up authentication.
* [GCP-specific architecture patterns](#reference-architecture) and reference diagrams.
* [Service recommendations](#compute-options) and best practices.
* [Google Cloud Well-Architected best practices](#google-cloud-well-architected-best-practices) for operational excellence, security, and reliability.

<Note>
  LangChain provides Terraform modules specifically for GCP to help provision infrastructure for LangSmith. These modules can quickly set up GKE clusters, Cloud SQL, Memorystore Redis, Cloud Storage, and networking resources.

  View the [GCP Terraform modules](https://github.com/langchain-ai/terraform/tree/main/modules/gcp) for documentation and examples.
</Note>

## Initial setup

<Steps>
  <Step title="Deploy to Kubernetes">
    Follow the [Kubernetes installation guide](/langsmith/kubernetes). LangSmith is tested on Google Kubernetes Engine (GKE).

    **GKE-specific notes:**

    * LangSmith works with standard GKE clusters
    * Use GCE persistent disk storage class
  </Step>

  <Step title="Configure external services">
    For production deployments, connect to GCP managed services:

    <CardGroup>
      <Card title="Google Cloud Storage" icon="database" href="/langsmith/self-host-blob-storage#google-cloud-storage">
        Store trace data in GCS
      </Card>

      <Card title="Cloud SQL" icon="database" href="/langsmith/self-host-external-postgres#google-cloud-sql">
        PostgreSQL database
      </Card>

      <Card title="Memorystore" icon="cpu" href="/langsmith/self-host-external-redis#google-cloud-memorystore">
        Redis or Valkey for caching
      </Card>

      <Card title="ClickHouse Cloud" icon="chart-line" href="/langsmith/self-host-external-clickhouse">
        Analytics database
      </Card>
    </CardGroup>
  </Step>

  <Step title="Set up authentication">
    Use [Workload Identity](https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) to authenticate LangSmith pods to GCP services.

    **Key pages:**

    * [GCS HMAC key authentication](/langsmith/self-host-blob-storage#google-cloud-storage)
    * [Cloud SQL IAM authentication](/langsmith/self-host-external-postgres#iam-authentication)
    * [Memorystore IAM authentication](/langsmith/self-host-external-redis#iam-authentication)
  </Step>
</Steps>

After completing these initial setup steps, you can review the complete GCP architecture and best practices below.

## Reference architecture

We recommend leveraging GCP's managed services to provide a scalable, secure, and resilient platform. The following architecture applies to both self-hosted and hybrid and aligns with the [Google Cloud Well-Architected Framework](https://docs.cloud.google.com/architecture/framework):

<img alt="Architecture diagram showing GCP relations to LangSmith services" />

* <Icon icon="globe" /> **Ingress & networking**: Requests enter via [Cloud Load Balancing](https://cloud.google.com/load-balancing) within your [VPC](https://cloud.google.com/vpc), secured using [Cloud Armor](https://cloud.google.com/armor) and [IAM](https://cloud.google.com/iam)-based authentication.

* <Icon icon="cube" /> **Frontend & backend services:** Containers run on [Google Kubernetes Engine (GKE)](https://cloud.google.com/kubernetes-engine), orchestrated behind the load balancer. Routes requests to other services within the cluster as necessary.

* <Icon icon="database" /> **Storage & databases:**
  * [Cloud SQL for PostgreSQL](https://cloud.google.com/sql/docs/postgres): metadata, projects, users, and short-term and long-term memory for deployed agents. LangSmith supports PostgreSQL version 14 or higher.
  * [Memorystore](https://cloud.google.com/memorystore) ([Redis](https://cloud.google.com/memorystore/docs/redis) or [Valkey](https://cloud.google.com/memorystore/docs/valkey)): caching and job queues. Memorystore can be in single-instance or cluster mode. LangSmith requires Redis OSS version 5 or higher, or Valkey 8.
  * ClickHouse + [Persistent Disks](https://cloud.google.com/compute/docs/disks): analytics and trace storage.
    * We recommend using an [externally managed ClickHouse solution](/langsmith/self-host-external-clickhouse) unless security or compliance reasons
      prevent you from doing so.
    * ClickHouse is not required for hybrid deployments.
  * [Cloud Storage](https://cloud.google.com/storage): object storage for trace artifacts and telemetry.

* <Icon icon="sparkles" /> **LLM integration:** Optionally proxy requests to [Vertex AI](https://cloud.google.com/vertex-ai) for LLM inference.

* <Icon icon="chart-line" /> **Monitoring & observability:** Integrate with [Cloud Monitoring](https://cloud.google.com/monitoring) and [Cloud Logging](https://cloud.google.com/logging)

## Compute options

LangSmith supports multiple compute options depending on your requirements:

| Compute option                           | Description                               | Suitable for                         |
| ---------------------------------------- | ----------------------------------------- | ------------------------------------ |
| **Google Kubernetes Engine (preferred)** | Advanced scaling and multi-tenant support | Large enterprises                    |
| **Compute Engine-based**                 | Full control, BYO-infra                   | Regulated or air-gapped environments |

## Google cloud Well-Architected best practices

This reference is designed to align with the six pillars of the Google Cloud Well-Architected Framework:

### Operational excellence

* Automate deployments with IaC ([Terraform](https://www.terraform.io/) / [Deployment Manager](https://cloud.google.com/deployment-manager)).
* Use [Secret Manager](https://cloud.google.com/secret-manager) for configuration and sensitive data.
* Configure your LangSmith instance to [export telemetry data](/langsmith/export-backend) and continuously monitor via [Cloud Logging](https://cloud.google.com/logging).
* The preferred method to manage [LangSmith deployments](/langsmith/deployment) is to create a CI process that builds [Agent Server](/langsmith/agent-server) images and pushes them to [Artifact Registry](https://cloud.google.com/artifact-registry). Create a test deployment for pull requests before deploying a new revision to staging or production upon PR merge.

### Security

* Use [IAM](https://cloud.google.com/iam) roles with least-privilege policies and [Workload Identity](https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) for secure pod-to-GCP-service authentication.
* Enable encryption at rest ([Cloud SQL](https://docs.cloud.google.com/sql/docs/postgres/cmek), [Cloud Storage](https://cloud.google.com/storage/docs/encryption), Persistent Disks) and in transit (TLS 1.2+).
* Integrate with [Secret Manager](https://cloud.google.com/secret-manager) for credentials.
* Use [Identity Platform](https://cloud.google.com/identity-platform) or [Workload Identity Federation](https://cloud.google.com/iam/docs/workload-identity-federation) as an IDP in conjunction with LangSmith's built-in authentication and authorization features to secure access to agents and their tools.

### Reliability

* Replicate the LangSmith [data plane](/langsmith/data-plane) across regions: Deploy identical data planes to Kubernetes clusters in different regions for LangSmith Deployment. Deploy [Cloud SQL](https://cloud.google.com/sql/docs/postgres/high-availability) and [GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/configuration-overview) services across multiple zones.
* Implement [autoscaling](https://cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler) for backend workers using [Horizontal Pod Autoscaler](https://cloud.google.com/kubernetes-engine/docs/concepts/horizontalpodautoscaler) and [Cluster Autoscaler](https://cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler).
* Use [Cloud DNS](https://cloud.google.com/dns) health checks and failover policies.

### Performance optimization

* Leverage [Compute Engine](https://cloud.google.com/compute) instances for optimized compute with [machine type selection](https://cloud.google.com/compute/docs/machine-types).
* Use [Cloud Storage lifecycle policies](https://cloud.google.com/storage/docs/lifecycle) for infrequently accessed trace data, moving to [Nearline](https://cloud.google.com/storage/docs/storage-classes#nearline) or [Coldline](https://cloud.google.com/storage/docs/storage-classes#coldline) storage classes.

### Cost optimization

* Right-size [GKE](https://cloud.google.com/kubernetes-engine) clusters using [Committed Use Discounts](https://cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts) and [Sustained Use Discounts](https://cloud.google.com/compute/docs/sustained-use-discounts).
* Monitor cost KPIs using [Cloud Billing](https://cloud.google.com/billing/docs) dashboards and [Cost Management](https://cloud.google.com/cost-management) tools.

### Sustainability

* Minimize idle workloads with on-demand compute and [autoscaling](https://cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler).
* Store telemetry in low-latency, low-cost tiers using [Cloud Storage lifecycle policies](https://cloud.google.com/storage/docs/lifecycle).
* Enable auto-shutdown for non-prod environments using [scheduled actions](https://cloud.google.com/compute/docs/instances/schedule-instance-start-stop).

## Security and compliance

LangSmith can be configured for:

* [Private Service Connect](https://cloud.google.com/vpc/docs/private-service-connect)-only access (no public internet exposure, besides egress necessary for billing).
* [Cloud KMS](https://cloud.google.com/kms)-based encryption keys for Cloud Storage, Cloud SQL, and Persistent Disks.
* Audit logging to [Cloud Logging](https://cloud.google.com/logging) and [Cloud Audit Logs](https://cloud.google.com/logging/docs/audit).

Customers can deploy in [Assured Workloads](https://cloud.google.com/assured-workloads) regions for compliance with ISO, HIPAA, or other regulatory requirements as needed.

## Monitoring and evals

Use LangSmith to:

* Capture traces from LLM apps running on [Vertex AI](https://cloud.google.com/vertex-ai).
* Evaluate model outputs via [LangSmith datasets](/langsmith/manage-datasets).
* Track latency, token usage, and success rates.

Integrate with:

* [Cloud Monitoring](https://cloud.google.com/monitoring) dashboards.
* [OpenTelemetry](https://opentelemetry.io/) and [Prometheus](https://prometheus.io/) exporters.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/gcp-self-hosted.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# How to implement generative user interfaces with LangGraph
Source: https://docs.langchain.com/langsmith/generative-ui-react

<Info>
  **Prerequisites**

  * [LangSmith](/langsmith/observability)
  * [Agent Server](/langsmith/agent-server)
  * [`useStream()` React Hook](/oss/python/langchain/frontend/overview)
</Info>

Generative user interfaces (Generative UI) allows agents to go beyond text and generate rich user interfaces. This enables creating more interactive and context-aware applications where the UI adapts based on the conversation flow and AI responses.

<img alt="Agent Chat showing a prompt about booking/lodging and a generated set of hotel listing cards (images, titles, prices, locations) rendered inline as UI components." />

LangSmith supports colocating your React components with your graph code. This allows you to focus on building specific UI components for your graph while easily plugging into existing chat interfaces such as [Agent Chat](https://agentchat.vercel.app) and loading the code only when actually needed.

## Tutorial

### 1. Define and configure UI components

First, create your first UI component. For each component you need to provide an unique identifier that will be used to reference the component in your graph code.

```tsx title="src/agent/ui.tsx" theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const WeatherComponent = (props: { city: string }) => {
  return <div>Weather for {props.city}</div>;
};

export default {
  weather: WeatherComponent,
};
```

Next, define your UI components in your `langgraph.json` configuration:

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "node_version": "20",
  "graphs": {
    "agent": "./src/agent/index.ts:graph"
  },
  "ui": {
    "agent": "./src/agent/ui.tsx"
  }
}
```

The `ui` section points to the UI components that will be used by graphs. By default, we recommend using the same key as the graph name, but you can split out the components however you like, see [Customise the namespace of UI components](#customise-the-namespace-of-ui-components) for more details.

LangSmith will automatically bundle your UI components code and styles and serve them as external assets that can be loaded by the `LoadExternalComponent` component. Some dependencies such as `react` and `react-dom` will be automatically excluded from the bundle.

CSS and Tailwind 4.x is also supported out of the box, so you can freely use Tailwind classes as well as `shadcn/ui` in your UI components.

<Tabs>
  <Tab title="src/agent/ui.tsx">
    ```tsx theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    import "./styles.css";

    const WeatherComponent = (props: { city: string }) => {
      return <div className="bg-red-500">Weather for {props.city}</div>;
    };

    export default {
      weather: WeatherComponent,
    };
    ```
  </Tab>

  <Tab title="src/agent/styles.css">
    ```css theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    @import "tailwindcss";
    ```
  </Tab>
</Tabs>

### 2. Send the UI components in your graph

<Tabs>
  <Tab title="Python">
    ```python title="src/agent.py" theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    import uuid
    from typing import Annotated, Sequence, TypedDict

    from langchain.messages import AIMessage
    from langchain_core.messages import BaseMessage
    from langchain_openai import ChatOpenAI
    from langgraph.graph import StateGraph
    from langgraph.graph.message import add_messages
    from langgraph.graph.ui import AnyUIMessage, ui_message_reducer, push_ui_message

    class AgentState(TypedDict):  # noqa: D101
        messages: Annotated[Sequence[BaseMessage], add_messages]
        ui: Annotated[Sequence[AnyUIMessage], ui_message_reducer]

    async def weather(state: AgentState):
        class WeatherOutput(TypedDict):
            city: str

        weather: WeatherOutput = (
            await ChatOpenAI(model="gpt-5.4-mini")
            .with_structured_output(WeatherOutput)
            .with_config({"tags": ["nostream"]})
            .ainvoke(state["messages"])
        )

        message = AIMessage(
            id=str(uuid.uuid4()),
            content=f"Here's the weather for {weather['city']}",
        )

        # Emit UI elements associated with the message
        push_ui_message("weather", weather, message=message)
        return {"messages": [message]}

    workflow = StateGraph(AgentState)
    workflow.add_node(weather)
    workflow.add_edge("__start__", "weather")
    graph = workflow.compile()
    ```
  </Tab>

  <Tab title="JS">
    Use the `typedUi` utility to emit UI elements from your agent nodes:

    ```typescript title="src/agent/index.ts" theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    import {
      typedUi,
      uiMessageReducer,
    } from "@langchain/langgraph-sdk/react-ui/server";

    import { ChatOpenAI } from "@langchain/openai";
    import { z } from "zod";

    import type ComponentMap from "./ui.js";

    import {
      Annotation,
      MessagesAnnotation,
      StateGraph,
      type LangGraphRunnableConfig,
    } from "@langchain/langgraph";

    const AgentState = Annotation.Root({
      ...MessagesAnnotation.spec,
      ui: Annotation({ reducer: uiMessageReducer, default: () => [] }),
    });

    export const graph = new StateGraph(AgentState)
      .addNode("weather", async (state, config) => {
        // Provide the type of the component map to ensure
        // type safety of `ui.push()` calls as well as
        // pushing the messages to the `ui` and sending a custom event as well.
        const ui = typedUi<typeof ComponentMap>(config);

        const weather = await new ChatOpenAI({ model: "gpt-5.4-mini" })
          .withStructuredOutput(z.object({ city: z.string() }))
          .withConfig({ tags: ["nostream"] })
          .invoke(state.messages);

        const response = {
          id: crypto.randomUUID(),
          type: "ai",
          content: `Here's the weather for ${weather.city}`,
        };

        // Emit UI elements associated with the AI message
        ui.push({ name: "weather", props: weather }, { message: response });

        return { messages: [response] };
      })
      .addEdge("__start__", "weather")
      .compile();
    ```
  </Tab>
</Tabs>

### 3. Handle UI elements in your React application

On the client side, you can use `useStream()` and `LoadExternalComponent` to display the UI elements.

```tsx title="src/app/page.tsx" theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
"use client";

import { useStream } from "@langchain/langgraph-sdk/react";
import { LoadExternalComponent } from "@langchain/langgraph-sdk/react-ui";

export default function Page() {
  const { thread, values } = useStream({
    apiUrl: "http://localhost:2024",
    assistantId: "agent",
  });

  return (
    <div>
      {thread.messages.map((message) => (
        <div key={message.id}>
          {message.content}
          {values.ui
            ?.filter((ui) => ui.metadata?.message_id === message.id)
            .map((ui) => (
              <LoadExternalComponent key={ui.id} stream={thread} message={ui} />
            ))}
        </div>
      ))}
    </div>
  );
}
```

Behind the scenes, `LoadExternalComponent` will fetch the JS and CSS for the UI components from LangSmith and render them in a shadow DOM, thus ensuring style isolation from the rest of your application.

## How-to guides

### Provide custom components on the client side

If you already have the components loaded in your client application, you can provide a map of such components to be rendered directly without fetching the UI code from LangSmith.

```tsx theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const clientComponents = {
  weather: WeatherComponent,
};

<LoadExternalComponent
  stream={thread}
  message={ui}
  components={clientComponents}
/>;
```

### Show loading UI when components are loading

You can provide a fallback UI to be rendered when the components are loading.

```tsx theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
<LoadExternalComponent
  stream={thread}
  message={ui}
  fallback={<div>Loading...</div>}
/>
```

### Customise the namespace of UI components.

By default `LoadExternalComponent` will use the `assistantId` from `useStream()` hook to fetch the code for UI components. You can customise this by providing a `namespace` prop to the `LoadExternalComponent` component.

<Tabs>
  <Tab title="src/app/page.tsx">
    ```tsx theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    <LoadExternalComponent
      stream={thread}
      message={ui}
      namespace="custom-namespace"
    />
    ```
  </Tab>

  <Tab title="langgraph.json">
    ```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    {
      "ui": {
        "custom-namespace": "./src/agent/ui.tsx"
      }
    }
    ```
  </Tab>
</Tabs>

### Access and interact with the thread state from the UI component

You can access the thread state inside the UI component by using the `useStreamContext` hook.

```tsx theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { useStreamContext } from "@langchain/langgraph-sdk/react-ui";

const WeatherComponent = (props: { city: string }) => {
  const { thread, submit } = useStreamContext();
  return (
    <>
      <div>Weather for {props.city}</div>

      <button
        onClick={() => {
          const newMessage = {
            type: "human",
            content: `What's the weather in ${props.city}?`,
          };

          submit({ messages: [newMessage] });
        }}
      >
        Retry
      </button>
    </>
  );
};
```

### Pass additional context to the client components

You can pass additional context to the client components by providing a `meta` prop to the `LoadExternalComponent` component.

```tsx theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
<LoadExternalComponent stream={thread} message={ui} meta={{ userId: "123" }} />
```

Then, you can access the `meta` prop in the UI component by using the `useStreamContext` hook.

```tsx theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { useStreamContext } from "@langchain/langgraph-sdk/react-ui";

const WeatherComponent = (props: { city: string }) => {
  const { meta } = useStreamContext<
    { city: string },
    { MetaType: { userId?: string } }
  >();

  return (
    <div>
      Weather for {props.city} (user: {meta?.userId})
    </div>
  );
};
```

### Streaming UI messages from the server

You can stream UI messages before the node execution is finished by using the `onCustomEvent` callback of the `useStream()` hook. This is especially useful when updating the UI component as the LLM is generating the response.

```tsx theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { uiMessageReducer } from "@langchain/langgraph-sdk/react-ui";

const { thread, submit } = useStream({
  apiUrl: "http://localhost:2024",
  assistantId: "agent",
  onCustomEvent: (event, options) => {
    options.mutate((prev) => {
      const ui = uiMessageReducer(prev.ui ?? [], event);
      return { ...prev, ui };
    });
  },
});
```

Then you can push updates to the UI component by calling `ui.push()` / `push_ui_message()` with the same ID as the UI message you wish to update.

<Tabs>
  <Tab title="Python">
    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    from typing import Annotated, Sequence, TypedDict

    from langchain_anthropic import ChatAnthropic
    from langchain.messages import AIMessage, AIMessageChunk, BaseMessage
    from langgraph.graph import StateGraph
    from langgraph.graph.message import add_messages
    from langgraph.graph.ui import AnyUIMessage, push_ui_message, ui_message_reducer

    class AgentState(TypedDict):  # noqa: D101
        messages: Annotated[Sequence[BaseMessage], add_messages]
        ui: Annotated[Sequence[AnyUIMessage], ui_message_reducer]

    class CreateTextDocument(TypedDict):
        """Prepare a document heading for the user."""

        title: str

    async def writer_node(state: AgentState):
        model = ChatAnthropic(model="claude-sonnet-4-6")
        message: AIMessage = await model.bind_tools(
            tools=[CreateTextDocument],
            tool_choice={"type": "tool", "name": "CreateTextDocument"},
        ).ainvoke(state["messages"])

        tool_call = next(
            (x["args"] for x in message.tool_calls if x["name"] == "CreateTextDocument"),
            None,
        )

        if tool_call:
            ui_message = push_ui_message("writer", tool_call, message=message)
            ui_message_id = ui_message["id"]

            # We're already streaming the LLM response to the client through UI messages
            # so we don't need to stream it again to the `messages` stream mode.
            content_stream = model.with_config({"tags": ["nostream"]}).astream(
                f"Create a document with the title: {tool_call['title']}"
            )

            content: AIMessageChunk | None = None
            async for chunk in content_stream:
                content = content + chunk if content else chunk

                push_ui_message(
                    "writer",
                    {"content": content.text()},
                    id=ui_message_id,
                    message=message,
                    # Use `merge=True` to merge props with the existing UI message
                    merge=True,
                )

        return {"messages": [message]}
    ```
  </Tab>

  <Tab title="JS">
    ```tsx theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    import {
      Annotation,
      MessagesAnnotation,
      type LangGraphRunnableConfig,
    } from "@langchain/langgraph";
    import { z } from "zod";
    import { ChatAnthropic } from "@langchain/anthropic";
    import {
      typedUi,
      uiMessageReducer,
    } from "@langchain/langgraph-sdk/react-ui/server";
    import type { AIMessageChunk } from "@langchain/core/messages";

    import type ComponentMap from "./ui";

    const AgentState = Annotation.Root({
      ...MessagesAnnotation.spec,
      ui: Annotation({ reducer: uiMessageReducer, default: () => [] }),
    });

    async function writerNode(
      state: typeof AgentState.State,
      config: LangGraphRunnableConfig
    ): Promise<typeof AgentState.Update> {
      const ui = typedUi<typeof ComponentMap>(config);

      const model = new ChatAnthropic({ model: "claude-sonnet-4-6" });
      const message = await model
        .bindTools(
          [
            {
              name: "create_text_document",
              description: "Prepare a document heading for the user.",
              schema: z.object({ title: z.string() }),
            },
          ],
          { tool_choice: { type: "tool", name: "create_text_document" } }
        )
        .invoke(state.messages);

      type ToolCall = { name: "create_text_document"; args: { title: string } };
      const toolCall = message.tool_calls?.find(
        (tool): tool is ToolCall => tool.name === "create_text_document"
      );

      if (toolCall) {
        const { id, name } = ui.push(
          { name: "writer", props: { title: toolCall.args.title } },
          { message }
        );

        const contentStream = await model
          // We're already streaming the LLM response to the client through UI messages
          // so we don't need to stream it again to the `messages` stream mode.
          .withConfig({ tags: ["nostream"] })
          .stream(`Create a short poem with the topic: ${message.text}`);

        let content: AIMessageChunk | undefined;
        for await (const chunk of contentStream) {
          content = content?.concat(chunk) ?? chunk;

          ui.push(
            { id, name, props: { content: content?.text } },
            // Use `merge: true` to merge props with the existing UI message
            { message, merge: true }
          );
        }
      }

      return { messages: [message] };
    }
    ```
  </Tab>

  <Tab title="ui.tsx">
    ```tsx theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    function WriterComponent(props: { title: string; content?: string }) {
      return (
        <article>
          <h2>{props.title}</h2>
          <p style={{ whiteSpace: "pre-wrap" }}>{props.content}</p>
        </article>
      );
    }

    export default {
      weather: WriterComponent,
    };
    ```
  </Tab>
</Tabs>

### Remove UI messages from state

Similar to how messages can be removed from the state by appending a RemoveMessage you can remove an UI message from the state by calling `remove_ui_message` / `ui.delete` with the ID of the UI message.

<Tabs>
  <Tab title="Python">
    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    from langgraph.graph.ui import push_ui_message, delete_ui_message

    # push message
    message = push_ui_message("weather", {"city": "London"})

    # remove said message
    delete_ui_message(message["id"])
    ```
  </Tab>

  <Tab title="JS">
    ```tsx theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    // push message
    const message = ui.push({ name: "weather", props: { city: "London" } });

    // remove said message
    ui.delete(message.id);
    ```
  </Tab>
</Tabs>

## Learn more

* [JS/TS SDK Reference](https://langchain-ai.github.io/langgraphjs/reference/modules/sdk.html)

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/generative-ui-react.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Integrations
Source: https://docs.langchain.com/langsmith/get-started-integrations

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/get-started-integrations.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Governance
Source: https://docs.langchain.com/langsmith/govern

Govern model access, spending, data handling, and compliance across your LangSmith organization.

Govern how your organization uses models and data: route and control LLM access through the gateway, enforce spend and redaction policies, and meet audit and compliance requirements.

## Explore

<CardGroup>
  <Card title="LLM Gateway" icon="route" href="/langsmith/llm-gateway">
    Proxy LLM calls through LangSmith to enforce spend limits, redact sensitive data, and centrally manage provider credentials.
  </Card>

  <Card title="Audit & compliance" icon="shield-lock" href="/langsmith/audit-logs">
    Review audit logs and the data storage, privacy, and compliance model.
  </Card>
</CardGroup>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/govern.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
