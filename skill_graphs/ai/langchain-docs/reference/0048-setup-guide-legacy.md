# Setup guide (legacy)
Source: https://docs.langchain.com/langsmith/hybrid-legacy

Legacy hybrid deployment model with a LangChain-managed control plane and a self-managed data plane.

<Warning>
  This page describes the legacy hybrid deployment model, which uses a LangChain-managed control plane to orchestrate Agent Servers in your cloud. For the current hybrid model, see [Hybrid](/langsmith/hybrid).
</Warning>

<Info>
  The hybrid option requires an [Enterprise](https://langchain.com/pricing) plan. [Get a demo](https://www.langchain.com/contact-sales) to learn more.
</Info>

The **hybrid** model splits LangSmith infrastructure between LangChain's cloud and yours:

* **Control plane** (LangSmith UI, APIs, and orchestration) runs in LangChain's cloud, managed by LangChain.
* **Data plane** (your <Tooltip>Agent Servers</Tooltip> and agent workloads) runs in your cloud, managed by you.

This combines the convenience of a managed interface with the flexibility of running workloads in your own environment.

<Note>
  Learn more about the [control plane](/langsmith/control-plane), [data plane](/langsmith/data-plane), and [Agent Server](/langsmith/agent-server) architecture concepts.
</Note>

| Component                        | Responsibilities                                                                                                                                    | Where it runs     | Who manages it |
| -------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- | -------------- |
| <Tooltip>Control plane</Tooltip> | <ul><li>UI for creating deployments and revisions</li><li>APIs for managing deployments</li><li>Observability data storage</li></ul>                | LangChain's cloud | LangChain      |
| <Tooltip>Data plane</Tooltip>    | <ul><li>Operator/listener to reconcile deployments</li><li>Agent Servers (agents/graphs)</li><li>Backing services (Postgres, Redis, etc.)</li></ul> | Your cloud        | You            |

When running LangSmith in a hybrid model, you authenticate with a [LangSmith API key](/langsmith/create-account-api-key).

### Workflow

1. Use the `langgraph-cli` or [Studio](/langsmith/studio) to test your graph locally.
2. Build a Docker image using the `langgraph build` command.
3. Deploy your Agent Server from the [control plane UI](/langsmith/control-plane#control-plane-ui).

<Note>
  Supported Compute Platforms: [Kubernetes](https://kubernetes.io/). See [Kubernetes setup](#kubernetes-setup) below.
</Note>

### Architecture

<img alt="Hybrid deployment: LangChain-hosted control plane (LangSmith UI/APIs) manages deployments. Your cloud runs a listener, Agent Server instances, and backing stores (Postgres/Redis) on Kubernetes." />

<img alt="Hybrid deployment: LangChain-hosted control plane (LangSmith UI/APIs) manages deployments. Your cloud runs a listener, Agent Server instances, and backing stores (Postgres/Redis) on Kubernetes." />

### Compute platforms

* **Kubernetes**: Hybrid supports running the data plane on any Kubernetes cluster.

<Tip>
  For setup in Kubernetes, see [Kubernetes setup](#kubernetes-setup) below.
</Tip>

### Egress to LangSmith and the control plane

In the hybrid deployment model, your self-hosted data plane will send network requests to the control plane to poll for changes that need to be implemented in the data plane. Traces from data plane deployments also get sent to the LangSmith instance integrated with the control plane. This traffic to the control plane is encrypted, over HTTPS. The data plane authenticates with the control plane with a LangSmith API key.

In order to enable this egress, you may need to update internal firewall rules or cloud resources (such as Security Groups) to [allow certain IP addresses](/langsmith/cloud#ingress-into-langchain-saas).

<Warning>
  AWS/Azure PrivateLink or GCP Private Service Connect is currently not supported. This traffic will go over the internet.
</Warning>

## Kubernetes setup

The following steps describe how to connect your self-hosted data plane to the managed LangSmith control plane.

### Prerequisites

1. `KEDA` is installed on your cluster.

   ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
     helm repo add kedacore https://kedacore.github.io/charts
     helm install keda kedacore/keda --namespace keda --create-namespace
   ```

   <Info>
     `KEDA` is used to automatically scale the deployment system based on queue size.
   </Info>

2. A valid `Ingress` controller is installed on your cluster. For more information about configuring ingress for your deployment, refer to [Create an ingress for installations](/langsmith/self-host-ingress). We highly recommend using the modern [Gateway API](/langsmith/self-host-ingress#option-2%3A-gateway-api) in a production setup.

3. If you plan to have the listener watch multiple namespaces, you **MUST** use the [Gateway API](/langsmith/self-host-ingress#option-2%3A-gateway-api) or an [Istio Gateway](/langsmith/self-host-ingress#option-3%3A-istio-gateway) instead of the [standard ingress](/langsmith/self-host-ingress#option-1%3A-standard-ingress) resource. A standard ingress resource can only route traffic to services in the same namespace, whereas a Gateway or Istio Gateway can route traffic to services across multiple namespaces.

4. You have slack space in your cluster for multiple deployments. `Cluster-Autoscaler` is recommended to automatically provision new nodes.

5. You will need to enable egress to two control plane URLs. The listener polls these endpoints for deployments. Use the pair that matches your LangSmith region.

LangSmith Deployment control plane:

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

LangSmith API:

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

### Setup

1. Provide your LangSmith organization ID to us. Your LangSmith organization will be configured to deploy the data plane in your cloud.
2. Create a listener from the LangSmith UI. The `Listener` data model is configured for the actual ["listener" application](/langsmith/data-plane#listener-application).
   1. In the left-hand navigation, select `Deployments` > `Listeners`.
   2. In the top-right of the page, select `+ Create Listener`.
   3. Enter a unique `Compute ID` for the listener. The `Compute ID` is a user-defined identifier that should be unique across all listeners in the current LangSmith workspace. The `Compute ID` is displayed to end users when they are creating a new deployment. Ensure that the `Compute ID` provides context to the end user about where their Agent Server deployments will be deployed to. For example, a `Compute ID` can be set to `k8s-cluster-name-dev-01`. In this example, the name of the Kubernetes cluster is `k8s-cluster-name`, `dev` denotes that the cluster is reserved for "development" workloads, and `01` is a numerical suffix to reduce naming collisions.
   4. Enter one or more Kubernetes namespaces. Later, the "listener" application will be configured to deploy to each of these namespaces.
   5. In the top-right on the page, select `Submit`.
   6. After the listener is created, copy the listener ID. You will use it later when installing the actual "listener" application in the Kubernetes cluster (step 5).
   <Info>
     **Important**
     Creating a listener from the LangSmith UI does not install the "listener" application in the Kubernetes cluster.
   </Info>
3. A [Helm chart](https://github.com/langchain-ai/helm/tree/main/charts/langgraph-dataplane) is provided to install the necessary components in your Kubernetes cluster.
   * `langgraph-dataplane-listener`: This is a service that listens to LangChain's [control plane](/langsmith/control-plane) for changes to your deployments and creates/updates downstream CRDs. This is the ["listener" application](/langsmith/data-plane#listener-application).
   * `LangGraphPlatform CRD`: A CRD for LangSmith Deployment. This contains the spec for managing an instance of a LangSmith Deployment.
   * `langgraph-dataplane-operator`: This operator handles changes to your LangSmith CRDs.
   * `langgraph-dataplane-redis`: A Redis instance is used by the `langgraph-dataplane-listener` to manage various tasks (mainly creating and deleting deployments).
4. Configure your `langgraph-dataplane-values.yaml` file.
   ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
     config:
       langsmithApiKey: "" # API Key of your Workspace
       langsmithWorkspaceId: "" # Workspace ID
       hostBackendUrl: "https://api.host.langchain.com" # Use the matching regional LangSmith Deployment control plane URL from the table above
       smithBackendUrl: "https://api.smith.langchain.com" # Use the matching regional LangSmith API URL from the table above
       langgraphListenerId: "" # Listener ID from Step 2f
       watchNamespaces: "" # comma-separated list of Kubernetes namespaces that the listener and operator will deploy to
       enableLGPDeploymentHealthCheck: true # enable/disable health check step for deployments

     ingress:
       hostname: "" # specify a hostname that will be configured for all deployments

     operator:
       enabled: true
       createCRDs: true # set this to `false` if the CRD has been previously installed in the current Kubernetes cluster
   ```
   * `config.langsmithApiKey`: The `langgraph-listener` deployment authenticates with LangChain's LangGraph control plane API with the `langsmithApiKey`.
   * `config.langsmithWorkspaceId`: The `langgraph-listener` deployment is coupled to Agent Server deployments in the LangSmith workspace. In other words, the `langgraph-listener` deployment can only manage Agent Server deployments in the specified LangSmith workspace ID.
   * `config.langgraphListenerId`: In addition to being coupled with a LangSmith workspace, the `langgraph-listener` deployment is also coupled to a listener. When a new Agent Server deployment is created, it is automatically coupled to a `langgraphListenerId`. Specifying `langgraphListenerId` ensures that the `langgraph-listener` deployment can only manage Agent Server deployments that are coupled to `langgraphListenerId`.
   * `config.watchNamespaces`: A comma-separated list of Kubernetes namespaces that the `langgraph-listener` deployment will deploy to. This list should match the list of namespaces specified in step 2d.
   * `config.enableLGPDeploymentHealthCheck`: To disable the Agent Server health check, set this to `false`.
   * `ingress.hostname`: As part of the deployment workflow, the `langgraph-listener` deployment attempts to call the Agent Server health check endpoint (`GET /ok`) to verify that the application has started up correctly. A typical setup involves creating a shared DNS record or domain for Agent Server deployments. This is not managed by LangSmith. Once created, set `ingress.hostname` to the domain, which will be used to complete the health check.
   * `operator.createCRDs`: Set this value to `false` if the Kubernetes cluster already has the `LangGraphPlatform CRD` installed. During installation, an error will occur if the CRD is already installed. This situation may occur if multiple listeners are deployed on the same Kubernetes cluster.
5. Deploy `langgraph-dataplane` Helm chart.
   ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
     helm repo add langchain https://langchain-ai.github.io/helm/
     helm repo update
     helm upgrade -i langgraph-dataplane langchain/langgraph-dataplane --values langgraph-dataplane-values.yaml --wait --debug
   ```
6. If successful, you will see three services start up in your namespace.

   ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
     NAME                                            READY   STATUS              RESTARTS   AGE
     langgraph-dataplane-listener-6dd4749445-zjmr4   0/1     ContainerCreating   0          26s
     langgraph-dataplane-operator-6b88879f9b-t76gk   1/1     Running             0          26s
     langgraph-dataplane-redis-0                     1/1     Running             0          25s
   ```

   Your hybrid infrastructure is now ready to create deployments.

### Configuring additional data planes in the same cluster

To create a data plane in a different namespace in the same cluster, repeat the above steps and pass a `-n` option to `helm upgrade` to specify a different namespace.

**When installing multiple data planes in the same cluster, it is very important to follow the rules below:**

1. The `config.watchNamespaces` list should never intersect with other installations `config.watchNamespaces`. For example, if installation A is watching namespaces `foo,bar`, installation B cannot watch either `foo` or `bar`. Multiple operators or listeners watching the same namespace will lead to unexpected behavior. This means that multiple LangSmith workspaces cannot deploy to the same namespace! Please review the [cluster organization](#kubernetes-cluster-organization) section to understand this better.
2. It is required to use the [Gateway API](/langsmith/self-host-ingress#option-2%3A-gateway-api) or an [Istio Gateway](/langsmith/self-host-ingress#option-3%3A-istio-gateway). Relying on the [standard ingress](/langsmith/self-host-ingress#option-1%3A-standard-ingress) resource can cause conflicts with Ingress objects created by other data planes in the same cluster. Because behavior in these cases depends on the specific ingress controller, this may result in unpredictable or undesired outcomes.

## Listeners

In the hybrid option, one or more ["listener" applications](/langsmith/data-plane#listener-application) can run depending on how your LangSmith workspaces and Kubernetes clusters are organized.

### Kubernetes cluster organization

* One or more listeners can run in a Kubernetes cluster.
* A listener can deploy into one or more namespaces in that cluster.
* Multiple listeners cannot deploy to the same namespace.
* Cluster owners are responsible for planning listener layout and Agent Server deployments.

### LangSmith workspace organization

* A workspace can be associated with one or more listeners.
* A listener can only be associated with one workspace. LangSmith workspace to listener is a one-to-many relationship.
* A workspace can only deploy to Kubernetes clusters where all of its listeners are deployed.

## Use cases

Here are some common listener configurations (not strict requirements):

### Each LangSmith workspace → separate Kubernetes cluster

* Cluster `alpha` runs workspace `A`
* Cluster `beta` runs workspace `B`

### One cluster, one namespace per workspace

* Cluster `alpha`, namespace `1` runs workspace `A`
* Cluster `alpha`, namespace `2` runs workspace `B`

### Separate clusters, with shared “dev” cluster

* Cluster `alpha` runs workspace `A`
* Cluster `beta` runs workspace `B`
* Cluster `dev` runs workspaces `A` and `B`
* Both workspaces have two listeners; cluster `dev` has two listener deployments

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/hybrid-legacy.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Improve LLM-as-judge evaluators using human feedback
Source: https://docs.langchain.com/langsmith/improve-judge-evaluator-feedback

<Check>
  Before working through this page, it might be helpful to read the following:

  * [Evaluation concepts](/langsmith/evaluation-concepts#evaluators)
  * [Creating LLM-as-a-judge evaluators](/langsmith/llm-as-judge)
</Check>

Reliable [*LLM-as-a-judge evaluators*](/langsmith/evaluation-concepts#llm-as-judge) are critical for making informed decisions about your AI applications (e.g., prompt, model, architecture changes). Defining the evaluator prompt correctly can be difficult, but it directly affects the trustworthiness of your evaluations.

This guide describes how to align your LLM-as-a-judge evaluator using human feedback to improve your evaluator's quality and help you build reliable AI applications.

## How it works

LangSmith's **Align Evaluator** feature has a series of steps that help you align your LLM-as-a-judge evaluator with human expert feedback. You can use this feature to align evaluators that run on a dataset for [offline evaluations](/langsmith/evaluation-concepts#offline-evaluations) or for [online evaluations](/langsmith/evaluation-concepts#online-evaluations). In either case, the steps are similar:

1. **Select experiments or runs** that contain outputs from your application.
2. Add the selected experiments or runs to an **annotation queue** where a human expert can label the data.
3. **Test your LLM-as-a-judge evaluator prompt** against the labeled examples. Check the cases where your evaluator result is not aligned with the labeled data. This indicates areas where your evaluator prompt needs improvement.
4. **Refine and repeat** to improve evaluator alignment. Update your LLM-as-a-judge evaluator prompt and test again.

## Prerequisites

You'll need the following before starting this guide for [offline evaluations](#offline-evaluations) or [online evaluations](#online-evaluations):

### Offline evaluations

* A [dataset](/langsmith/evaluation-concepts#datasets) with at least one [experiment](/langsmith/evaluation-concepts#experiment).
* You'll need to upload or create datasets via the [SDK](/langsmith/manage-datasets-programmatically#create-a-dataset) or the [UI](/langsmith/manage-datasets-in-application#create-a-dataset-and-add-examples) and run an experiment via the [SDK](/langsmith/evaluate-llm-application#run-the-evaluation) or the [Playground](/langsmith/run-evaluation-from-playground).

### Online evaluations

* An application that’s already sending traces to LangSmith.
* Configure this with one of the [tracing integrations](/langsmith/observability-concepts) to start.

## Getting started

You can enter the alignment flow for both new and existing evaluators in datasets and tracing projects.

|                                              | Dataset Evaluators                                                                                                                                                                                     | Tracing Project Evaluators                                                                                                                                                                         |
| -------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Create an aligned evaluator from scratch** | 1. **Datasets & Experiments** and select your dataset<br />2. Click **+ Evaluator** > **Create from labeled data**<br />3. Enter a descriptive feedback key name (e.g. `correctness`, `hallucination`) | 1. **Projects** and select your project<br />2. Click **+ New** > **Evaluator** > **Create from labeled data**<br />3. Enter a descriptive feedback‑key name (e.g. `correctness`, `hallucination`) |
| **Align an existing evaluator**              | 1. **Datasets & Experiments** > select your dataset > **Evaluators** tab<br />2. In the **Align Evaluator with experiment data** box, click **Select Experiments**                                     | 1. **Projects** > select your project > **Evaluators** tab<br />2. In the **Align Evaluator with experiment data** box, click **Select Experiments**                                               |

## 1. Select experiments or runs

Select one or more experiments (or runs) to send for human labeling. This will add runs to an [annotation queue](/langsmith/annotation-queues).

<img alt="Add to evaluator queue" />

To add any new experiments/runs to an existing annotation queue, head to the **Evaluators** tab, select the evaluator you are aligning and click **Add to Queue.**

<Check>
  Datasets should be representative of inputs and outputs you expect to see in production.

  While you don’t need to cover every possible scenario, it’s important to include examples across the full range of expected use cases. For example, if you're building a sports bot that answers questions about baseball, basketball, and football, your dataset should include at least one labeled example from each sport.
</Check>

## 2. Label examples

Label examples in the annotation queue by adding a feedback score. Once you've labeled an example, click **Add to Reference Dataset**.

<Check>
  If you have a large number of examples in your experiments, you don't need to label every example to get started. We recommend starting with at least 20 examples, you can always add more later. We recommend that the examples that you label are diverse (balanced in both 0 and 1 labels) to ensure that you're building a well rounded evaluator prompt.
</Check>

## 3. Test your evaluator prompt against the labeled examples

Once you have labeled examples, the next step is iterating on your evaluator prompt to mimic the labeled data as well as possible. This iteration is done in the **Evaluator Playground**.

To go to the evaluator playground: Click the **View evaluator** button on the top right of the evaluator queue. This will take you to the detail page of the evaluator you are aligning. Click the **Evaluator Playground** button to access the playground.

<img alt="Evaluator Playground" />

In the evaluator playground you can create or edit your evaluator prompt and click **Start Alignment** to run it over the set of labeled examples that you created in Step 2. After running your evaluator, you'll see how its generated scores compare to your human labels. The alignment score is the percentage of examples where the evaluator's judgment matches that of the human expert.

## 4. Repeat to improve evaluator alignment

Iterate by updating your prompt and testing again to improve evaluator alignment.

<Check>
  Updates to your evaluator prompt are **not saved by default**. We recommend saving your evaluator prompt regularly, and especially after you see your alignment score improve.

  The evaluator playground will show the alignment score for the most recently saved version of your evaluator prompt for comparison when you're iterating on your prompt.
</Check>

Improving the alignment score of your evaluator isn't an exact science but there are a few strategies that are helpful in increasing the alignment score.

### Tips for improving evaluator alignment

**1. Investigate misaligned examples**

Digging into misaligned examples and trying to group them into common failure modes is a great first step for improving your evaluator alignment.

Once you have identified the common failure modes, add instructions to your evaluator prompt so the LLM knows about them. For example, you could explain that "MFA stands for "multi-factor authentication" if you notice it not understanding that specific acronym. Or you could tell it that "a good response will always contain at least 3 potential hotels to book" if it is confused on what good/bad means in your evaluator's context.

**2. Inspect the reasoning behind the LLM score**

To understand why the LLM scored an example the way it did, you can enable reasoning for your LLM-as-a-judge evaluator. Reasoning is helpful to understand the LLM's thought process and can help you identify common failure modes to incorporate into your evaluator prompt as well..

In order to see the reasoning in the evaluator playground, hover over the LLM score.

<img alt="Enable reasoning" />

This will show the reasoning behind the LLM's score in the evaluator playground.

**3. Add more labeled examples and validate performance**

To avoid overfitting to the labeled examples, it's important to add more labeled examples and test performance, especially if you started off with a small number of examples.

## Video guide

<iframe title="YouTube video player" />

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/improve-judge-evaluator-feedback.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Discover errors and usage patterns with Insights
Source: https://docs.langchain.com/langsmith/insights

Insights automatically analyzes your traces to detect usage patterns, common agent behaviors, and failure modes, so you do not need to review thousands of traces manually.

Insights uses hierarchical categorization to make sense of your data and highlight actionable trends.

<Note>
  Insights is available for LangSmith Plus and Enterprise [plans](/langsmith/pricing-plans).
</Note>

## Prerequisites

* A [model configuration](/langsmith/model-configurations) set up for Insights in your workspace.
* [Permissions](/langsmith/organization-workspace-operations#projects) to create rules in LangSmith (required to generate new Insights Reports).
* [Permissions](/langsmith/organization-workspace-operations#projects) to view tracing projects in LangSmith (required to view existing Insights Reports).

## Generate your first Insights report

<Tabs>
  <Tab title="UI" icon="layout-dashboard">
    1. Navigate to **Tracing Projects** in the left-hand menu and select a tracing project.
    2. Click **+New** in the top right corner then **New Insights Report** to generate new insights over the project.
    3. Enter a name for your job.
    4. If you haven't already, [configure a model](/langsmith/model-configurations) for Insights in your workspace settings.
    5. Answer the guided questions to focus your Insights Report on what you want to learn about your agent, then click **Run job**.

    <Tip>Toggle to Manual mode to [configure the job manually](#configure-a-job).</Tip>

    This will kick off a background Insights Report. Reports can take up to 30 minutes to complete.
  </Tab>

  <Tab title="SDK" icon="code">
    You can generate Insights Reports over data stored outside LangSmith using the [Python SDK](/langsmith/smith-python-sdk). This allows you to analyze chat histories from your production systems, logs, or other sources.

    When you call `generate_insights()`, the SDK will:

    1. Upload your chat histories as traces to a new LangSmith project.
    2. Generate an Insights Report over those uploaded traces.
    3. Return a link to your results in the [LangSmith UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-insights).

    <CodeGroup>
      ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import os
      from langsmith import Client

      client = Client()

      chat_histories = [
          [
              {"role": "user", "content": "how are you"},
              {"role": "assistant", "content": "good!"},
          ],
          [
              {"role": "user", "content": "do you like art"},
              {"role": "assistant", "content": "only Tarkovsky"},
          ],
      ]

      report = client.generate_insights(
          chat_histories=chat_histories,
          name="Customer Support Topics - March 2024",
          instructions="What are the main topics and questions users are asking about?",
          openai_api_key=os.environ["OPENAI_API_KEY"],  # optional if already set as workspace secret
      )

      # client.poll_insights(report=report)
      ```
    </CodeGroup>
  </Tab>
</Tabs>

<Note>
  Generating insights over 1,000 threads typically costs \$1.00-\$2.00 with OpenAI models and \$3.00-\$4.00 with current Anthropic models. The cost scales with the number of threads sampled and the size of each thread.
</Note>

## Understand the results

Once your job has completed, you can navigate to the **Insights** tab where you'll see a table of Insights Report. Each Report contains insights generated over a specific sample of traces from the tracing project.

<Frame>
  <img />
</Frame>

Click into your job to see traces organized into a set of auto-generated categories.

You can drill down through categories and subcategories to view the underlying traces, feedback, and run statistics.

<Frame>
  <img />
</Frame>

### Executive summary

At the top of each report, you'll find an executive summary that surfaces the most important patterns discovered in your traces. This includes:

* Key findings with percentages showing how often each pattern appears.
* Clickable references (e.g., #1, #2, #3) to traces the agent identified as exceptionally relevant to your question.

### Top-level categories

Your traces are automatically grouped into top-level categories that represent the broadest patterns in your data.

The distribution bars show how frequently each pattern occurs, making it easy to spot behaviors that happen more or less than expected.

Each category has a brief description and displays aggregated metrics over the traces it contains, including:

* Typical trace stats (like error rates, latency, cost)
* Feedback scores from your evaluators
* [Attributes](#attributes) extracted as part of the job

### Subcategories

Clicking on any category shows a breakdown into subcategories, which gives you a more granular understanding of interaction patterns in that category of traces.

In the [Chat Langchain](https://chat.langchain.com) example, under **Data & Retrieval** there are subcategories like **Vector Stores** and **Data Ingestion**.

### Individual traces

You can view the traces assigned to each category or subcategory by clicking through to see the traces table. From there, you can click into any trace to see the full conversation details.

## Configure a job

You can create an Insights Report using the auto-generated flow or by configuring it manually.

### Autogenerating a config

1. Open **New Insights** and make sure the **Auto** toggle is active.
2. Answer the natural-language questions about your agent's purpose, what you want to learn, and how traces are structured. Insights will translate your answers into a draft config (job name, summary prompt, attributes, and sampling defaults).
3. Choose a provider, then click **Generate config** to preview or **Run job** to launch immediately.

**Providing useful context**

For best results, write a sentence or two for each prompt that gives Insights the context it needs—what you're trying to learn, which signals or fields matter most, and anything you already know isn't useful. The clearer you are about what your agent does and how its traces are structured, the more Insights can group examples in a way that's specific, actionable, and aligned with how you reason about your data.

**Describing your traces**

Explain how your data is organized: are these single runs or multi-turn conversations? Which inputs and outputs contain the key information? This helps Insights generate summary prompts and attributes that focus on what matters. You can also directly specify variables from the [summary prompt](#summary-prompt) section if needed.

### Choose models

Insights uses two models:

* **Thinking model**: performs the clustering step (more capable, higher cost).
* **Summarization model**: generates the per-trace summaries (faster, lower cost).

Both models are selected from the providers you have configured in your workspace. When specific models have been enabled for Insights in your [model configurations](/langsmith/model-configurations), you can select them individually. If no individual models are configured, you select a provider (OpenAI or Anthropic) and Insights uses default models for that provider.

For best results, use models from the same provider for both roles.

### Manual configuration

Manual configuration gives you more control—for example, predefining categories you want your data grouped into or targeting traces that match specific feedback scores and filters.

#### Select traces

* **Sample size**: The maximum number of traces to analyze (1,000 limit).
* **Time range**: Traces are sampled from this time range.
* **Filters**: Additional trace filters. As you adjust filters, you'll see how many traces match your criteria.

#### Categories

By default, top-level categories are automatically generated bottom-up from the underlying traces.

In some instances, you know specific categories you're interested in upfront and want the job to bucket traces into those predefined categories.

The **Categories** section of the config lets you do this by enumerating the names and descriptions of the top-level categories you want to be used.

Subcategories are still auto-generated by the algorithm within the predefined top-level categories.

When a job completes, the discovered top-level categories are automatically saved back to the config—but only if the config had no categories defined beforehand. This means subsequent scheduled runs will reuse those categories for consistency.

#### Summary prompt

The first step of the job is to create a brief summary of every trace. These summaries are then categorized.

Extracting the right information in the summary is essential for getting useful categories.

You can edit the prompt used to generate these summaries. The two things to think about when editing the prompt are:

* Summarization instructions: Any information that isn't in the trace summary won't affect the categories that get generated, so make sure to provide clear instructions on what information is important to extract from each trace.
* Trace content: Use mustache formatting to specify which parts of each trace are passed to the summarizer. Large traces with lots of inputs and outputs can be expensive and noisy. Reducing the prompt to only include the most relevant parts of the trace can improve your results.

You must specify what parts of each trace to send to the summarizer using at least one of these template variables:

| Variable              | Description                                                                                          | Example                        |
| --------------------- | ---------------------------------------------------------------------------------------------------- | ------------------------------ |
| `run.inputs`          | Inputs of the most recent root run                                                                   | `{{run.inputs}}`               |
| `run.outputs`         | Outputs of the most recent root run                                                                  | `{{run.outputs}}`              |
| `run.error`           | Error string, if the run failed                                                                      | `{{run.error}}`                |
| `run.feedback`        | All feedback scores as a JSON blob                                                                   | `{{run.feedback}}`             |
| `run.feedback.<key>`  | A specific feedback score by key                                                                     | `{{run.feedback.correctness}}` |
| `all_thread_messages` | Full message history for the thread (only available for projects with [threads](/langsmith/threads)) | `{{all_thread_messages}}`      |

You can access nested fields using dot notation. For example, `{{run.inputs.foo.bar}}` includes only the `bar` field within `foo` in the last run's inputs.

<Note>
  For projects with [threads](/langsmith/threads), Insights analyzes full conversations. Only the most recent root run from each thread is used for `run.*` variables. Use `all_thread_messages` to access the complete conversation history.
</Note>

#### Attributes

Along with a summary, you can define additional string, numerical, and boolean attributes to be extracted from each trace.
These attributes will influence the categorization step—traces with similar attribute values will tend to be categorized together.
You can also see aggregations of these attributes per category.

As an example, you might want to extract the attribute `user_satisfied: boolean` from each trace to steer the algorithm towards categories that split up positive and negative user experiences, and to see the average user satisfaction per category.

#### Filter attributes

You can use the `filter_by` parameter on boolean attributes to pre-filter traces before generating insights. When enabled, only traces where the attribute evaluates to `true` are included in the analysis.

This is useful when you want to focus your Insights Report on a specific subset of traces. For example, only analyzing errors, only examining English-language conversations, or only including traces that meet certain quality criteria.

**How it works:**

* Add `"filter_by": true` to any boolean attribute when creating a config for Insights.
* The LLM evaluates each trace against the attribute description during summarization.
* Traces where the attribute is `false` or missing are excluded before insights are generated.

## Schedule Insights Reports

Schedule Insights reports to run automatically on a recurring basis. When creating or editing a configuration, use the **Schedule** section to choose:

* **Daily**: Runs every day at 8:00 UTC.
* **Weekly on Monday**: Runs every Monday at 8:00 UTC.
* **Custom**: Enter your own cron expression (in UTC).

Each scheduled run generates a new report using your saved configuration. Time ranges are computed dynamically. For example, "last 24 hours" always analyzes the most recent 24-hour window at execution time.

## Save your config

You can optionally save configs for future reuse using the **Save as** button.
This is especially useful if you want to compare Insights Reports over time to identify changes in user and agent behavior.

Select from previously saved configs in the dropdown in the top-left corner of the pane when creating a new Insights Report.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/insights.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Integrations
Source: https://docs.langchain.com/langsmith/integrations

[LangSmith](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-integrations) provides integrations for a growing set of popular [LLM providers](#llm-providers) and [agent frameworks](#agent-frameworks) as well as [Deep Agents](/oss/python/deepagents/overview), [LangChain](/oss/python/langchain/overview), and [LangGraph](/oss/python/langgraph/overview). For setup and usage, refer to the guides listed on this page.

## LLM providers

<div>
  <a href="/langsmith/trace-bedrock">
    <img alt="" />

    <img alt="" />

    <span>Amazon Bedrock</span>
  </a>

  <a href="/langsmith/trace-anthropic">
    <img alt="" />

    <img alt="" />

    <span>Anthropic</span>
  </a>

  <a href="/langsmith/trace-deepseek">
    <img alt="" />

    <img alt="" />

    <span>DeepSeek</span>
  </a>

  <a href="/langsmith/trace-with-google-gemini">
    <img alt="" />

    <img alt="" />

    <span>Google Gemini</span>
  </a>

  <a href="/langsmith/trace-litellm">
    <img alt="" />

    <img alt="" />

    <span>LiteLLM</span>
  </a>

  <a href="/langsmith/trace-with-mistral">
    <img alt="" />

    <img alt="" />

    <span>Mistral</span>
  </a>

  <a href="/langsmith/trace-openai">
    <img alt="" />

    <img alt="" />

    <span>OpenAI</span>
  </a>

  <a href="/langsmith/trace-with-openai-compatible">
    <img alt="" />

    <img alt="" />

    <span>OpenAI-compatible APIs</span>
  </a>
</div>

<Callout icon="arrows-transfer-down">
  **Using LangChain?** LangChain provides a unified interface to 100+ LLM providers, which allows you to switch between models by setting environment variables. [Initialize a model](/oss/python/langchain/models#initialize-a-model) and LangSmith will automatically trace your application.
</Callout>

## Agent frameworks

<div>
  <a href="/langsmith/trace-with-autogen">
    <img alt="" />

    <img alt="" />

    <span>AutoGen</span>
  </a>

  <a href="/langsmith/trace-claude-agent-sdk">
    <img alt="" />

    <img alt="" />

    <span>Claude Agent SDK</span>
  </a>

  <a href="/langsmith/trace-with-crewai">
    <img alt="" />

    <img alt="" />

    <span>CrewAI</span>
  </a>

  <a href="/langsmith/trace-deep-agents">
    <img alt="" />

    <span>Deep Agents</span>
  </a>

  <a href="/langsmith/trace-with-google-adk">
    <img alt="" />

    <img alt="" />

    <span>Google ADK</span>
  </a>

  <a href="/langsmith/trace-with-langchain">
    <img alt="" />

    <span>LangChain</span>
  </a>

  <a href="/langsmith/trace-with-langgraph">
    <img alt="" />

    <span>LangGraph</span>
  </a>

  <a href="/langsmith/trace-with-mastra">
    <img alt="" />

    <img alt="" />

    <span>Mastra</span>
  </a>

  <a href="/langsmith/trace-with-microsoft-agent-framework">
    <img alt="" />

    <img alt="" />

    <span>Microsoft Agent Framework</span>
  </a>

  <a href="/langsmith/trace-with-openai-agents-sdk">
    <img alt="" />

    <img alt="" />

    <span>OpenAI Agents</span>
  </a>

  <a href="/langsmith/trace-with-opentelemetry">
    <img alt="" />

    <img alt="" />

    <span>OpenTelemetry</span>
  </a>

  <a href="/langsmith/trace-with-pydantic-ai">
    <img alt="" />

    <img alt="" />

    <span>PydanticAI</span>
  </a>

  <a href="/langsmith/trace-with-semantic-kernel">
    <img alt="" />

    <img alt="" />

    <span>Semantic Kernel</span>
  </a>

  <a href="/langsmith/trace-with-strands-agents">
    <img alt="" />

    <img alt="" />

    <span>Strands Agents</span>
  </a>

  <a href="/langsmith/trace-with-vercel-ai-sdk">
    <img alt="" />

    <img alt="" />

    <span>Vercel AI SDK</span>
  </a>
</div>

## Voice AI frameworks

<div>
  <a href="/langsmith/trace-openai-realtime">
    <img alt="" />

    <img alt="" />

    <span>OpenAI Realtime</span>
  </a>

  <a href="/langsmith/trace-gemini-live">
    <img alt="" />

    <img alt="" />

    <span>Gemini Live</span>
  </a>

  <a href="/langsmith/trace-with-livekit">
    <img alt="" />

    <img alt="" />

    <span>Livekit</span>
  </a>

  <a href="/langsmith/trace-with-pipecat">
    <img alt="" />

    <img alt="" />

    <span>Pipecat</span>
  </a>
</div>

## Developer tools

<div>
  <a href="/langsmith/trace-claude-code">
    <img alt="" />

    <img alt="" />

    <span>Claude Code</span>
  </a>

  <a href="/langsmith/trace-with-codex">
    <img alt="" />

    <img alt="" />

    <span>OpenAI Codex</span>
  </a>

  <a href="/langsmith/trace-with-opencode">
    <img alt="" />

    <img alt="" />

    <span>OpenCode</span>
  </a>

  <a href="/langsmith/trace-with-instructor">
    <img alt="" />

    <img alt="" />

    <span>Instructor</span>
  </a>

  <a href="/langsmith/trace-with-n8n">
    <img alt="" />

    <img alt="" />

    <span>n8n</span>
  </a>

  <a href="/langsmith/trace-with-pi">
    <img alt="" />

    <img alt="" />

    <span>Pi</span>
  </a>

  <a href="/langsmith/trace-with-temporal">
    <img alt="" />

    <img alt="" />

    <span>Temporal</span>
  </a>

  <a href="/langsmith/trace-with-vscode-copilot">
    <img alt="" />

    <img alt="" />

    <span>VS Code Copilot</span>
  </a>
</div>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/integrations.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
