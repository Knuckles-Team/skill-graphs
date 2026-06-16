# Tracing quickstart
Source: https://docs.langchain.com/langsmith/observability-quickstart

Add LangSmith tracing to an LLM application in minutes.

LangSmith gives you end-to-end visibility into your LLM application by capturing [*traces*](/langsmith/observability-concepts#traces); a complete record of every step that ran during a request, from the inputs passed in to the final output returned.

In this quickstart, you will add tracing to an AI assistant and view the results in LangSmith.

<Tip>
  If you're building with [LangChain](https://docs.langchain.com/oss/python/langchain/overview) or [LangGraph](https://docs.langchain.com/oss/python/langgraph/overview), you can enable LangSmith tracing with a single environment variable. Refer to [trace with LangChain](/langsmith/trace-with-langchain) or [trace with LangGraph](/langsmith/trace-with-langgraph).
</Tip>

## Prerequisites

Before you begin, make sure you have:

* **A LangSmith account**: Sign up or log in at [smith.langchain.com](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-observability-quickstart).
* **A LangSmith API key**: Follow the [Create an API key](/langsmith/create-account-api-key) guide.
* **An OpenAI API key**: Generate this from the [OpenAI dashboard](https://platform.openai.com/account/api-keys).

This example uses OpenAI as the LLM provider. You can adapt it for your own provider.

## 1. Set up your environment

1. Create a project directory, install the dependencies, and configure the required environment variables:

   <CodeGroup>
     ```bash Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
     mkdir ls-quickstart && cd ls-quickstart
     python -m venv .venv && source .venv/bin/activate
     pip install -U langsmith openai
     ```

     ```bash TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
     mkdir ls-quickstart-ts && cd ls-quickstart-ts
     npm init -y
     npm install langsmith openai
     npm install -D typescript tsx
     ```

     ```kotlin Java/Kotlin (Gradle) theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
     implementation("com.langchain.smith:langsmith-java:0.1.0-alpha.28")
     ```
   </CodeGroup>

2. Export your environment variables in your shell:

   ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
   export LANGSMITH_TRACING=true
   export LANGSMITH_API_KEY="<your-langsmith-api-key>"
   export OPENAI_API_KEY="<your-openai-api-key>"
   ```

   To send traces to a specific project, use the [`LANGSMITH_PROJECT` environment variable](/langsmith/log-traces-to-project). If this is not set, LangSmith will create a default tracing project automatically on trace ingestion.

   <Note>
     If your account is in a region other than US (the default), also set `LANGSMITH_ENDPOINT` to the API URL for your region. Without this, your API key won't be recognized and requests will fail to authenticate.

     <table>
       <thead>
         <tr>
           <th>Region</th>
         </tr>
       </thead>

       <tbody>
         <tr>
           <td>GCP US</td>
         </tr>

         <tr>
           <td>GCP EU</td>
         </tr>

         <tr>
           <td>GCP APAC</td>
         </tr>

         <tr>
           <td>AWS US</td>
         </tr>
       </tbody>
     </table>

     For example, EU accounts: `export LANGSMITH_ENDPOINT="https://eu.api.smith.langchain.com"`.
   </Note>

   If you are using Anthropic, use the [Anthropic wrapper](/langsmith/trace-anthropic). If you are using Google Gemini, use the [Gemini wrapper](/langsmith/trace-with-google-gemini). For other providers, use the [`@traceable` decorator](/langsmith/annotate-code#use-%40traceable-%2F-traceable) to trace calls manually.

## 2. Build the app

The following app uses two LangSmith tools to add tracing:

* **OpenAI wrapper**: wraps the OpenAI client so every LLM call is automatically logged as a nested span.
* **Traceable wrapper**: wraps a function so its inputs, outputs, and any nested spans appear as a single trace in LangSmith. Use `@traceable` in Python, `traceable` in TypeScript and Kotlin, and `Tracing.traceFunction` in Java.

The `assistant` function calls a tool (`get_context`) to retrieve relevant context, then passes that context to the model. Using the traceable wrapper on both functions captures the full pipeline in one trace, with the tool call and LLM call as nested spans.

Create a file called `app.py`, `index.ts`, `App.java`, or `App.kt` with the following code:

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from openai import OpenAI
  from langsmith.wrappers import wrap_openai
  from langsmith import traceable

  client = wrap_openai(OpenAI())  # log every OpenAI call automatically

  @traceable(run_type="tool")  # trace this as a tool span
  def get_context(question: str) -> str:
      # In a real app, this would query a knowledge base or vector store
      return "LangSmith traces are stored for 14 days on the Developer plan."

  @traceable  # capture the full pipeline as a single trace
  def assistant(question: str) -> str:
      context = get_context(question)
      response = client.chat.completions.create(
          model="gpt-5.4-mini",
          messages=[
              {
                  "role": "system",
                  "content": f"Answer using the context below.\n\nContext: {context}",
              },
              {"role": "user", "content": question},
          ],
      )
      return response.choices[0].message.content

  if __name__ == "__main__":
      print(assistant("How long are LangSmith traces stored?"))
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import OpenAI from "openai";
  import { wrapOpenAI } from "langsmith/wrappers";
  import { traceable } from "langsmith/traceable";

  const client = wrapOpenAI(new OpenAI()); // log every OpenAI call automatically

  const getContext = traceable(
      async function getContext(question: string): Promise<string> { // trace this as a tool span
          // In a real app, this would query a knowledge base or vector store
          return "LangSmith traces are stored for 14 days on the Developer plan.";
      },
      { run_type: "tool" }
  );

  const assistant = traceable(async function assistant(question: string) { // capture the full pipeline as a single trace
      const context = await getContext(question);
      const response = await client.chat.completions.create({
          model: "gpt-5.4-mini",
          messages: [
              {
                  role: "system",
                  content: `Answer using the context below.\n\nContext: ${context}`,
              },
              { role: "user", content: question },
          ],
      });
      return response.choices[0]?.message?.content ?? null;
  });

  (async () => {
      console.log(await assistant("How long are LangSmith traces stored?"));
  })();
  ```

  ```java Java theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import com.langchain.smith.tracing.RunType;
  import com.langchain.smith.tracing.TraceConfig;
  import com.langchain.smith.tracing.Tracing;
  import com.langchain.smith.wrappers.openai.OpenAITracing;
  import com.openai.client.OpenAIClient;
  import com.openai.client.okhttp.OpenAIOkHttpClient;
  import com.openai.models.ChatModel;
  import com.openai.models.chat.completions.ChatCompletion;
  import com.openai.models.chat.completions.ChatCompletionCreateParams;
  import com.openai.models.chat.completions.ChatCompletionMessageParam;
  import com.openai.models.chat.completions.ChatCompletionSystemMessageParam;
  import com.openai.models.chat.completions.ChatCompletionUserMessageParam;
  import java.util.function.Function;

  class ObservabilityQuickstartApp {
    public static void main(String[] args) {
      new ObservabilityQuickstartRunner().run();
    }

    private static final class ObservabilityQuickstartRunner {
      private final OpenAIClient client =
          OpenAITracing.wrapOpenAI(OpenAIOkHttpClient.fromEnv());

      private final Function<String, String> getContext =
          Tracing.traceFunction(
              question -> "LangSmith traces are stored for 14 days on the Developer plan.",
              TraceConfig.builder().name("get_context").runType(RunType.TOOL).build());

      private final Function<String, String> assistant =
          Tracing.traceFunction(
              question -> {
                String context = getContext.apply(question);
                ChatCompletion response =
                    client.chat()
                        .completions()
                        .create(
                            ChatCompletionCreateParams.builder()
                                .model(ChatModel.GPT_5_CHAT_LATEST)
                                .addMessage(
                                    ChatCompletionMessageParam.ofSystem(
                                        ChatCompletionSystemMessageParam.builder()
                                            .content(
                                                "Answer using the context below.\n\nContext: " + context)
                                            .build()))
                                .addMessage(
                                    ChatCompletionMessageParam.ofUser(
                                        ChatCompletionUserMessageParam.builder()
                                            .content(question)
                                            .build()))
                                .build());
                return response.choices().get(0).message().content().orElse("");
              },
              TraceConfig.builder().name("assistant").build());

      void run() {
        System.out.println(assistant.apply("How long are LangSmith traces stored?"));
      }
    }
  }
  ```

  ```kotlin Kotlin theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import com.langchain.smith.tracing.RunType
  import com.langchain.smith.tracing.TraceConfig
  import com.langchain.smith.tracing.traceable
  import com.langchain.smith.wrappers.openai.wrapOpenAI
  import com.openai.client.okhttp.OpenAIOkHttpClient
  import com.openai.models.ChatModel
  import com.openai.models.chat.completions.ChatCompletionCreateParams
  import com.openai.models.chat.completions.ChatCompletionMessageParam
  import com.openai.models.chat.completions.ChatCompletionSystemMessageParam
  import com.openai.models.chat.completions.ChatCompletionUserMessageParam
  import kotlin.jvm.optionals.getOrNull

  val client = wrapOpenAI(OpenAIOkHttpClient.fromEnv())

  val getContext =
      traceable(
          { _: String -> "LangSmith traces are stored for 14 days on the Developer plan." },
          TraceConfig.builder().name("get_context").runType(RunType.TOOL).build(),
      )

  val assistant =
      traceable(
          { question: String ->
              val context = getContext(question)
              val response =
                  client.chat().completions().create(
                      ChatCompletionCreateParams.builder()
                          .model(ChatModel.GPT_5_CHAT_LATEST)
                          .addMessage(
                              ChatCompletionMessageParam.ofSystem(
                                  ChatCompletionSystemMessageParam.builder()
                                      .content("Answer using the context below.\n\nContext: $context")
                                      .build(),
                              ),
                          )
                          .addMessage(
                              ChatCompletionMessageParam.ofUser(
                                  ChatCompletionUserMessageParam.builder()
                                      .content(question)
                                      .build(),
                              ),
                          )
                          .build(),
                  )
              response.choices()[0].message().content().getOrNull().orEmpty()
          },
          TraceConfig.builder().name("assistant").build(),
      )

  println(assistant("How long are LangSmith traces stored?"))
  ```
</CodeGroup>

## 3. Run the app

<CodeGroup>
  ```bash Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  python app.py
  ```

  ```bash TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  npx tsx index.ts
  ```

  ```bash Java/Kotlin theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  ./gradlew run
  ```
</CodeGroup>

## 4. View your trace

In the [LangSmith UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-observability-quickstart), go to **Tracing** and select your **default** project. Click the `assistant` row to open the trace. The **Messages** tab shows the conversation as it was sent to the model. Select the **Details** tab to see the full run tree, including the `assistant` function with the `get_context` tool call and the OpenAI call nested inside it.

<img alt="LangSmith UI showing a trace with an outer application span and a nested LLM call span." />

<img alt="LangSmith UI showing a trace with an outer application span and a nested LLM call span." />

The outer span captures your `assistant` function's inputs and outputs. The nested **get\_context** span records the tool call, and the **ChatOpenAI** span records the exact prompt sent to the model and the response returned.

<Tip>
  You can also inspect traces from the terminal using the [LangSmith CLI](/langsmith/langsmith-cli).
</Tip>

## Next steps

* [Tracing integrations](/langsmith/integrations): LangChain, LangGraph, Anthropic, and other providers.
* [Trace an LLM application](/langsmith/observability-llm-tutorial): a full lifecycle tutorial, from prototyping through production.
* [Filter traces](/langsmith/filter-traces-in-application): search and navigate large tracing projects.
* [Log to a specific project](/langsmith/log-traces-to-project): send traces to a named project instead of **default**.

<Callout type="info" icon="feather">
  After logging traces, use **[Chat](/langsmith/chat)** to analyze them and get AI-powered insights into your application's performance.
</Callout>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/observability-quickstart.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Deploy an observability stack for your LangSmith deployment
Source: https://docs.langchain.com/langsmith/observability-stack

<Danger>
  **Deprecated**: The LangSmith Observability Helm chart is deprecated. We no longer maintain or provide support for it. The documentation below is preserved for reference only.
</Danger>

<Warning>
  **This section is only applicable for Kubernetes deployments.**
</Warning>

LangSmith applications expose telemetry data that can be sent to the backend of your choice. If you don’t already have an observability stack, or prefer to keep LangSmith telemetry separate from your main application, you can use the LangSmith Observability Helm chart to deploy a basic observability stack.

# Section 1: Prometheus exporters

Use this section if you would like to only deploy metrics exporters for the components in your self hosted deployment, which you can then scrape using your telemetry. If you would like a full observability stack deployed for you, go to the [End-to-End Deployment Section](/langsmith/observability-stack#prerequisites).

The helm chart provides a set of Prometheus exporters to expose metrics from [Redis](https://github.com/prometheus-community/helm-charts/tree/main/charts/prometheus-redis-exporter), [Postgres](https://github.com/prometheus-community/helm-charts/tree/main/charts/prometheus-postgres-exporter), [Nginx](https://github.com/prometheus-community/helm-charts/tree/main/charts/prometheus-nginx-exporter), and [Kube state metrics](https://github.com/prometheus-community/helm-charts/tree/main/charts/kube-state-metrics).

1. Create a local file called `langsmith_obs_config.yaml`
2. Copy over the values from this [file](https://github.com/langchain-ai/helm/blob/main/charts/langsmith-observability/examples/metric-exporters-only.yaml) into `langsmith_obs_config.yaml`, making sure to modify the values to match your LangSmith deployment.
3. Find the latest version of the chart by running `helm search repo langchain/langsmith-observability --versions`.
4. Grab the latest version number, and run `helm install langsmith-observability langchain/langsmith-observability --values langsmith_obs_config.yaml --version <version> -n <namespace> --wait --debug`

This will allow you to scrape metrics at the following service endpoints:

* Postgres: `langsmith-observability-postgres-exporter:9187/metrics`
* Redis: `langsmith-observability-redis-exporter:9121/metrics`
* Nginx: `langsmith-observability-nginx-exporter:9113/metrics`
* KubeStateMetrics: `langsmith-observability-kube-state-metrics:8080/metrics`

You should see the following if the installation went through:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
Release "langsmith-observability" has been installed. Happy Helming!NAME: langsmith-observabilityLAST DEPLOYED: Wed Jun 25 11:17:34 2025NAMESPACE: langsmith-observabilitySTATUS: deployedREVISION: 1
```

And if you run `kubectl get pods -n langsmith-observability`, you should see:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
langsmith-observability-kube-state-metrics-b58bb8db4-bm4g5        1/1     Running   0          2m22slangsmith-observability-nginx-exporter-6d686d9d4b-5qw9v           1/1     Running   0          2m22slangsmith-observability-postgres-exporter-67d5db5684-tffbm        1/1     Running   0          2m22slangsmith-observability-redis-exporter-846c4d65cb-vbtwd           1/1     Running   0          2m22s
```

# Section 2: Full observability stack

<Warning>
  **This is not a production observability stack. Use this to gain quick insight into logs, metrics and traces for your deployment. This is only made to handle a few dozen GB of data per day.**
</Warning>

This section will show you how to deploy the end-to-end observability stack for LangSmith, using the [Helm Chart](https://github.com/langchain-ai/helm/tree/main/charts/langsmith-observability).

This chart is built around the open-source LGTM Stack from Grafana. It consists of:

* [Loki](https://grafana.com/docs/loki/latest/) for logs.
* [Mimir](https://grafana.com/docs/mimir/latest/) for metrics + alerting.
* [Tempo](https://grafana.com/docs/tempo/latest/) for traces.
* [Grafana](https://grafana.com/docs/grafana/latest/) for monitoring UI.

As well as [OpenTelemetry Collectors](https://opentelemetry.io/docs/collector/) for gathering the telemetry data.

## Prerequisites

### 1. Compute resources

The resource requests and limits for each part of the stack can be modified in the helm chart. Here are the current allocations (request/limit):

* Loki: `2vCPU/3vCPU + 2Gi/4Gi`
* Mimir: `1vCPU/2vCPU + 2Gi/4Gi`
* Tempo: `1vCPU/2vCPU + 4Gi/6Gi`

Make sure you have those resources allocated before bringing up the helm chart, or modify the resource values in your helm configuration file.

### 2. Cert-Manager

The helm chart uses the OpenTelemetry Operator to provision collectors. The operator require that you have [cert-manager](https://cert-manager.io/docs/installation/) installed in your Kubernetes cluster.

If you do not have it installed, you can run the following commands:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
helm repo add jetstack https://charts.jetstack.iohelm repo updatehelm install cert-manager jetstack/cert-manager -n cert-manager --create-namespace
```

### 3. OpenTelemetry operator

Use the following to install the OpenTelemetry Operator:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
helm repo add open-telemetry https://open-telemetry.github.io/opentelemetry-helm-chartshelm repo updatehelm install opentelemetry-operator open-telemetry/opentelemetry-operator -n <namespace>
```

## Installation

The following instructions will bring up OTel collectors, the LGTM stack, Grafana and Prometheus exporters.

1. Create a local file called `langsmith_obs_config.yaml`
2. Copy over the values from this [file](https://github.com/langchain-ai/helm/blob/main/charts/langsmith-observability/examples/e2e-stack.yaml) into `langsmith_obs_config.yaml`, making sure to modify the values to match your LangSmith deployment.
3. Find the latest version of the chart by running `helm search repo langchain/langsmith-observability --versions`.
4. Grab the latest version number, and run `helm install langsmith-observability langchain/langsmith-observability --values langsmith_obs_config.yaml --version <version> -n <namespace> --wait --debug`

<Note>
  **You can selectively collect logs, metrics or traces by modifying the boolean values under `otelCollector` in your config file. You can also selectively bring up each respective piece of the backend (Loki, Mimir, Tempo).**
</Note>

You should see the following if the install went through:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
Release "langsmith-observability" has been installed. Happy Helming!NAME: langsmith-observabilityLAST DEPLOYED: Wed Jun 25 11:17:34 2025NAMESPACE: langsmith-observabilitySTATUS: deployedREVISION: 1
```

And if you run `kubectl get pods -n langsmith-observability`, you should see:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
langsmith-observability-collector-gateway-collector-7746fb8pzbg   1/1     Running   0          5m26slangsmith-observability-grafana-7c6fc976f9-cdbvr                  1/1     Running   0          2m49slangsmith-observability-kube-state-metrics-b58bb8db4-bm4g5        1/1     Running   0          5m27slangsmith-observability-loki-0                                    2/2     Running   0          5m27slangsmith-observability-loki-chunks-cache-0                       2/2     Running   0          5m27slangsmith-observability-loki-gateway-769fb6fff8-zjsn5             1/1     Running   0          5m27slangsmith-observability-loki-results-cache-0                      2/2     Running   0          5m27slangsmith-observability-mimir-0                                   1/1     Running   0          5m26slangsmith-observability-nginx-exporter-6d686d9d4b-5qw9v           1/1     Running   0          5m27slangsmith-observability-postgres-exporter-67d5db5684-tffbm        1/1     Running   0          5m27slangsmith-observability-redis-exporter-846c4d65cb-vbtwd           1/1     Running   0          5m27slangsmith-observability-tempo-0                                   1/1     Running   0          5m27sopentelemetry-operator-756dff697-vblbn                            2/2     Running   0          12m
```

## Post-Installation

### Enable logs and traces in LangSmith

Once you have installed the observability helm chart, you need to set the following values in your *LangSmith* helm configuration file to enable collection of logs and traces.

```yaml theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
commonPodAnnotations:
  # E.g.: "langsmith-observability/langsmith-observability-collector-sidecar"
  sidecar.opentelemetry.io/inject: "${LANGSMITH_OBS_NAMESPACE}/${LANGSMITH_OTEL_CRD_NAME}"
observability:
  tracing:
    enabled: true
    # Replace this with the endpoint of your trace collector.
    # E.g.: "http://langsmith-observability-collector-gateway-collector.langsmith-observability.svc.cluster.local:4318/v1/traces"
    endpoint: "http://${GATEWAY_COLLECTOR_SERVICE_NAME}.${LANGSMITH_OBS_NAMESPACE}.svc.cluster.local:4318/v1/traces"
```

<Info>
  1. To get `${LANGSMITH_OTEL_CRD_NAME}`, you can run `kubectl get opentelemetrycollectors -n ${LANGSMITH_OBS_NAMESPACE}` and select the name of the one with MODE = `sidecar`
  2. To get `${GATEWAY_COLLECTOR_SERVICE_NAME}` name, run `kubectl get services -n ${LANGSMITH_OBS_NAMESPACE}` and select the one with Ports 4317/4318 AND a ClusterIP set. It should be something like `langsmith-observability-collector-gateway-collector`
</Info>

Now run `helm upgrade langsmith langchain/langsmith --values langsmith_config.yaml -n <langsmith-namespace> --wait --debug`

Once upgraded, if you run `kubectl get pods -n <langsmith-namespace>` you should see the following (note the 2/2 for sidecar collectors):

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
langsmith-ace-backend-7dc85f7dff-xjbkj         2/2     Running     0               7m53slangsmith-backend-566b66979c-rgcfh             2/2     Running     1               7m53slangsmith-clickhouse-0                         2/2     Running     0               7m49slangsmith-frontend-7cf8549885-vpkns            2/2     Running     0               7m53slangsmith-platform-backend-5d46db7d9d-f6gh7    2/2     Running     0               7m52slangsmith-platform-backend-5d46db7d9d-lrr4d    2/2     Running     1               7m41slangsmith-platform-backend-5d46db7d9d-pcp27    2/2     Running     0               7m28slangsmith-playground-65d4c9699c-h656r          2/2     Running     0               7m52slangsmith-postgres-0                           2/2     Running     0               7m51slangsmith-queue-bdcd45bd6-htssd                2/2     Running     0               7m52slangsmith-queue-bdcd45bd6-pwdx4                2/2     Running     0               6m31slangsmith-queue-bdcd45bd6-xqrb8                2/2     Running     0               5m11slangsmith-redis-0                              2/2     Running     0               7m51s
```

## Grafana usage

Once everything is installed, do the following: to get your Grafana password:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
kubectl get secret langsmith-observability-grafana -n <langsmith_observability_namespace> -o jsonpath="{.data.admin-password}" | base64 --decode
```

Then port-forward into the `langsmith-observability-grafana` container at port 3000, and open your browser as `localhost:3000`. Use the username `admin` and the password from the secret above to log into Grafana.

Once in Grafana, you can use the UI to monitor logs, metrics and traces. Grafana also comes pre-packaged with sets of dashboards for monitoring the main components of your deployment.

<img alt="LangSmith Grafana Dashboards" />

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/observability-stack.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Observability in Studio
Source: https://docs.langchain.com/langsmith/observability-studio

LangSmith [Studio](/langsmith/studio) provides tools to inspect, debug, and improve your app beyond execution. By working with traces, datasets, and prompts, you can see how your application behaves in detail, measure its performance, and refine its outputs:

* [Iterate on prompts](#iterate-on-prompts): Modify prompts inside graph nodes directly or with the Playground.
* [Run experiments over a dataset](#run-experiments-over-a-dataset): Execute your assistant over a LangSmith dataset to score and compare results.
* [Debug LangSmith traces](#debug-langsmith-traces): Import traced runs into Studio and optionally clone them into your local agent.
* [Add a node to a dataset](#add-node-to-dataset): Turn parts of thread history into dataset examples for evaluation or further analysis.

## Iterate on prompts

Studio supports the following methods for modifying prompts in your graph:

* [Direct node editing](#direct-node-editing)
* [Playground interface](#playground)

### Direct node editing

Studio allows you to edit prompts used inside individual nodes, directly from the graph interface.

### Graph configuration

Define your [configuration](/oss/python/langgraph/use-graph-api#add-runtime-configuration) to specify prompt fields and their associated nodes using `langgraph_nodes` and `langgraph_type` keys.

#### `langgraph_nodes`

* **Description**: Specifies which nodes of the graph a configuration field is associated with.
* **Value Type**: Array of strings, where each string is the name of a node in your graph.
* **Usage Context**: Include in the `json_schema_extra` dictionary for Pydantic models or the `metadata["json_schema_extra"]` dictionary for dataclasses.
* **Example**:
  ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  system_prompt: str = Field(
      default="You are a helpful AI assistant.",
      json_schema_extra={"langgraph_nodes": ["call_model", "other_node"]},
  )
  ```

#### `langgraph_type`

* **Description**: Specifies the type of configuration field, which determines how it's handled in the UI.
* **Value Type**: String
* **Supported Values**:
  * `"prompt"`: Indicates the field contains prompt text that should be treated specially in the UI.
* **Usage Context**: Include in the `json_schema_extra` dictionary for Pydantic models or the `metadata["json_schema_extra"]` dictionary for dataclasses.
* **Example**:
  ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  system_prompt: str = Field(
      default="You are a helpful AI assistant.",
      json_schema_extra={
          "langgraph_nodes": ["call_model"],
          "langgraph_type": "prompt",
      },
  )
  ```

<Accordion title="Full example configuration">
  ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  ## Using Pydantic
  from pydantic import BaseModel, Field
  from typing import Annotated, Literal

  class Configuration(BaseModel):
      """The configuration for the agent."""

      system_prompt: str = Field(
          default="You are a helpful AI assistant.",
          description="The system prompt to use for the agent's interactions. "
          "This prompt sets the context and behavior for the agent.",
          json_schema_extra={
              "langgraph_nodes": ["call_model"],
              "langgraph_type": "prompt",
          },
      )

      model: Annotated[
          Literal[
              "anthropic/claude-sonnet-4-6",
              "anthropic/claude-haiku-4-5-20251001",
              "openai/o1",
              "openai/gpt-5.4-mini",
              "openai/o1-mini",
              "openai/o3-mini",
          ],
          {"__template_metadata__": {"kind": "llm"}},
      ] = Field(
          default="openai/gpt-5.4-mini",
          description="The name of the language model to use for the agent's main interactions. "
          "Should be in the form: provider/model-name.",
          json_schema_extra={"langgraph_nodes": ["call_model"]},
      )

  ## Using Dataclasses
  from dataclasses import dataclass, field

  @dataclass(kw_only=True)
  class Configuration:
      """The configuration for the agent."""

      system_prompt: str = field(
          default="You are a helpful AI assistant.",
          metadata={
              "description": "The system prompt to use for the agent's interactions. "
              "This prompt sets the context and behavior for the agent.",
              "json_schema_extra": {"langgraph_nodes": ["call_model"]},
          },
      )

      model: Annotated[str, {"__template_metadata__": {"kind": "llm"}}] = field(
          default="anthropic/claude-3-5-sonnet-20240620",
          metadata={
              "description": "The name of the language model to use for the agent's main interactions. "
              "Should be in the form: provider/model-name.",
              "json_schema_extra": {"langgraph_nodes": ["call_model"]},
          },
      )

  ```
</Accordion>

#### Editing prompts in the UI

1. Locate the gear icon on nodes with associated configuration fields.
2. Click to open the configuration modal.
3. Edit the values.
4. Save to update the current assistant version or create a new one.

### Playground

The [Playground](/langsmith/create-a-prompt) interface allows testing individual LLM calls without running the full graph:

1. Select a thread.
2. Click **View LLM Runs** on a node. This lists all the LLM calls (if any) made inside the node.
3. Select an LLM run to open in the Playground.
4. Modify prompts and test different model and tool settings.
5. Copy updated prompts back to your graph.

## Run experiments over a dataset

Studio lets you run [evaluations](/langsmith/evaluation-concepts) by executing your assistant against a predefined LangSmith [dataset](/langsmith/evaluation-concepts#datasets). This allows you to test performance across a variety of inputs, compare outputs to reference answers, and score results with configured [evaluators](/langsmith/evaluation-concepts#evaluators).

This guide shows you how to run a full end-to-end experiment directly from Studio.

### Prerequisites

Before running an experiment, ensure you have the following:

* **A LangSmith dataset**: Your dataset should contain the inputs you want to test and optionally, reference outputs for comparison. The schema for the inputs must match the required input schema for the assistant. For more information on schemas, see the [graph API schema documentation](/oss/python/langgraph/graph-api#schema). For more on creating datasets, refer to [How to Manage Datasets](/langsmith/manage-datasets-in-application#create-a-dataset-and-add-examples).
* **(Optional) Evaluators**: You can attach evaluators (e.g., LLM-as-a-Judge, heuristics, or custom functions) to your dataset in LangSmith. These will run automatically after the graph has processed all inputs.
* **A running application**: The experiment can be run against:
  * An application deployed on [LangSmith](/langsmith/deployment).
  * A locally running application started via the [langgraph-cli](/langsmith/local-dev-testing).

<Note>
  Studio experiments follow the same [data retention](/langsmith/usage-and-billing#data-retention) rules as other experiments. By default, traces have base tier retention (14 days). However, traces will automatically upgrade to extended tier retention (400 days) if feedback is added to them. Feedback can be added in one of two ways:

  * The [dataset has evaluators configured](/langsmith/bind-evaluator-to-dataset).
  * [Feedback](/langsmith/observability-concepts#feedback) is manually added to a trace.

  This auto-upgrade increases both the retention period and the cost of the trace. For more details, refer to [Data retention auto-upgrades](/langsmith/usage-and-billing#how-it-works).
</Note>

### Experiment setup

1. Launch the experiment. Click the **Run experiment** button in the top right corner of the Studio page.
2. Select your dataset. In the modal that appears, select the dataset (or a specific dataset split) to use for the experiment and click **Start**.
3. Monitor the progress. All of the inputs in the dataset will now be run against the active assistant. Monitor the experiment's progress via the badge in the top right corner.
4. You can continue to work in Studio while the experiment runs in the background. Click the arrow icon button at any time to navigate to LangSmith and view the detailed experiment results.

## Debug LangSmith traces

This guide explains how to open LangSmith traces in Studio for interactive investigation and debugging.

### Open deployed threads

1. Open the LangSmith trace, selecting the root run.
2. Click **Run in Studio**.

This will open Studio connected to the associated deployment with the trace's parent thread selected.

### Testing local agents with remote traces

This section explains how to test a local agent against remote traces from LangSmith. This enables you to use production traces as input for local testing, allowing you to debug and verify agent modifications in your development environment.

#### Prerequisites

* A LangSmith traced thread
* A [locally running agent](/langsmith/local-dev-testing).

<Info>
  **Local agent requirements**

  * langgraph>=0.3.18
  * langgraph-api>=0.0.32
  * Contains the same set of nodes present in the remote trace
</Info>

#### Clone thread

1. Open the LangSmith trace, selecting the root run.
2. Click the dropdown next to **Run in Studio**.
3. Enter your local agent's URL.
4. Select **Clone thread locally**.
5. If multiple graphs exist, select the target graph.

A new thread will be created in your local agent with the thread history inferred and copied from the remote thread, and you will be navigated to Studio for your locally running application.

## Add node to dataset

Add [examples](/langsmith/evaluation-concepts#examples) to [LangSmith datasets](/langsmith/manage-datasets) from nodes in the thread log. This is useful to evaluate individual steps of the agent.

1. Select a thread.
2. Click **Add to Dataset**.
3. Select nodes whose input/output you want to add to a dataset.
4. For each selected node, select the target dataset to create the example in. By default a dataset for the specific assistant and node will be selected. If this dataset does not yet exist, it will be created.
5. Edit the example's input/output as needed before adding it to the dataset.
6. Select **Add to dataset** at the bottom of the page to add all selected nodes to their respective datasets.

For more details, refer to [How to evaluate an application's intermediate steps](/langsmith/evaluate-on-intermediate-steps).

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/observability-studio.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Set up online code evaluators
Source: https://docs.langchain.com/langsmith/online-evaluations-code

[Online evaluations](/langsmith/evaluation-concepts#online-evaluations) provide real-time feedback on your production [traces](/langsmith/observability-concepts#traces). This is useful to continuously monitor the performance of your application: identify issues, measure improvements, and ensure consistent quality over time.

Code evaluators allow you to write an evaluator in Python or JavaScript directly in LangSmith. Often used for validating structure or statistical properties of your data.

<Note>When an online evaluator runs on any run within a trace, the trace will be auto-upgraded to [extended data retention](/langsmith/usage-and-billing#data-retention-auto-upgrades). This upgrade will impact trace pricing, but ensures that traces meeting your evaluation criteria (typically those most valuable for analysis) are preserved for investigation. </Note>

## View online evaluators

Navigate to the **Tracing** page and select a tracing project. To view existing online evaluators for that project, click on the **Evaluators** tab.

## Configure online evaluators

### 1. Navigate to online evaluators

Navigate to the **Tracing** page and select a tracing project. Click the **Evaluators** tab, then click **+ Evaluator** to open the **Add Evaluator** panel. Select **Code Evaluator** under **Create from scratch** to build a new evaluator, or select an existing code evaluator from your workspace under **Attach an existing evaluator**.

### 2. Name your evaluator

Provide a name for your evaluator. This name will be used when referencing the evaluator in your code, and will also be the name of the feedback that is generated by this evaluator.

### 3. Create a filter

For example, you may want to apply specific evaluators based on:

* Runs where a [user left feedback](/langsmith/attach-user-feedback) indicating the response was unsatisfactory.
* Runs that invoke a specific tool call. See [filtering for tool calls](/langsmith/filter-traces-in-application#example-filtering-for-tool-calls) for more information.
* Runs that match a particular piece of metadata (e.g. if you log traces with a `plan_type` and only want to run evaluations on traces from your enterprise customers). See [adding metadata to your traces](/langsmith/add-metadata-tags) for more information.

Filters on evaluators work the same way as when you're filtering traces in a project. For more information on filters, you can refer to [Filter traces](/langsmith/filter-traces-in-application).

<Tip>
  It's often helpful to inspect runs as you're creating a filter for your evaluator. With the evaluator configuration panel open, you can inspect runs and apply filters to them. Any filters you apply to the runs table will automatically be reflected in filters on your evaluator.
</Tip>

### 4. (Optional) Configure a sampling rate

Configure a sampling rate to control the percentage of filtered runs that trigger the automation action. For example, to control costs, you may want to set a filter to only apply the evaluator to 10% of traces. In order to do this, you would set the sampling rate to 0.1.

### 5. (Optional) Apply rule to past runs

Apply rule to past runs by toggling the **Apply to past runs** and entering a "Backfill from" date. This is only possible upon rule creation. Note: the backfill is processed as a background job, so you will not see the results immediately.

In order to track progress of the backfill, you can view logs for your evaluator by heading to the **Evaluators** tab within a tracing project and clicking the Logs button for the evaluator you created. Online evaluator logs are similar to [automation rule logs](/langsmith/rules#view-logs-for-your-automations).

* Add an evaluator name
* Optionally filter runs that you would like to apply your evaluator on or configure a sampling rate.
* Select **Apply Evaluator**

## Write your evaluation function

<Note>
  **Code evaluators restrictions.**

  **Allowed Libraries**: You can import all standard library functions, as well as the following public packages:

  ```
  numpy (v2.2.2): "numpy"
  pandas (v1.5.2): "pandas"
  jsonschema (v4.21.1): "jsonschema"
  scipy (v1.14.1): "scipy"
  sklearn (v1.26.4): "scikit-learn"
  ```

  **Network Access**: You cannot access the internet from a code evaluator.
</Note>

Code evaluators must be written inline. We recommend testing locally before setting up your code evaluator in LangSmith.

In the UI, you will find a panel that lets you write your code inline, with some starter code.

Code evaluators take in one argument:

* A `Run` ([reference](/langsmith/run-data-format)). This represents the sampled run to evaluate.

They return a single value:

* Feedback(s) Dictionary: A dictionary whose keys are the type of feedback you want to return, and values are the score you will give for that feedback key. For example, `{"correctness": 1, "silliness": 0}` would create two types of feedback on the run, one saying it is correct, and the other saying it is not silly.

The following example shows a function that validates that each run in the experiment has a known JSON field:

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import json

  def perform_eval(run):
    output_to_validate = run['outputs']
    is_valid_json = 0

    # assert you can serialize/deserialize as json
    try:
      json.loads(json.dumps(output_to_validate))
    except Exception as e:
      return { "formatted": False }

    # assert output facts exist
    if "facts" not in output_to_validate:
      return { "formatted": False }

    # assert required fields exist
    if "years_mentioned" not in output_to_validate["facts"]:
      return { "formatted": False }

    return {"formatted": True}
  ```

  ```javascript JavaScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  function perform_eval(run) {
      const outputToValidate = run.outputs;

      // Assert you can serialize/deserialize as json
      try {
          JSON.stringify(outputToValidate);
          JSON.parse(JSON.stringify(outputToValidate));
      } catch (e) {
          return { "formatted": false };
      }

      // Assert output facts exist
      if (!("facts" in outputToValidate)) {
          return { "formatted": false };
      }

      // Assert required fields exist
      if (!outputToValidate["facts"].hasOwnProperty("years_mentioned")) {
          return { "formatted": false };
      }

      return { "formatted": true };
  }
  ```
</CodeGroup>

## Test and save your evaluation function

Before saving, you can test your evaluator function on a recent run by clicking **Test Code** to make sure that your code executes properly.

Once you **Save**, your online evaluator will run over newly sampled runs (or backfilled ones too if you chose the backfill option).

If you prefer a video tutorial, check out the [Online Evaluations video](https://academy.langchain.com/pages/intro-to-langsmith-preview) from the Introduction to LangSmith Course.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/online-evaluations-code.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
