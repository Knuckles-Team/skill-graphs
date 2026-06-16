# Deploy your app to cloud
Source: https://docs.langchain.com/langsmith/deployment-quickstart

Deploy your first application to LangSmith Cloud (AWS and GCP) using the LangGraph CLI.

This quickstart shows you how to deploy an application to LangSmith Cloud (AWS and GCP) using the [`langgraph deploy`](/langsmith/cli#deploy) command.

<Tip>
  For a comprehensive Cloud deployment guide including GitHub-based deployments and all configuration options, refer to the [Cloud deployment setup guide](/langsmith/deploy-to-cloud).
</Tip>

<Note>
  The `langgraph deploy` command is in **beta**.
</Note>

## Prerequisites

Before you begin, ensure you have:

* A [LangSmith account](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-deployment-quickstart) on the [Plus plan or above](https://www.langchain.com/pricing) and an [API key](/langsmith/create-account-api-key).
* [Docker](https://docs.docker.com/get-docker/) installed and running. Verify with `docker ps`.
* On Apple Silicon (M1/M2/M3): [Docker Buildx](https://docs.docker.com/build/install-buildx/) for cross-compiling to `linux/amd64`.
* The [LangGraph CLI](/langsmith/cli):

  ```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  uv tool install langgraph-cli
  ```

## 1. Create a LangGraph app

Create a new app from the [`new-langgraph-project-python` template](https://github.com/langchain-ai/new-langgraph-project):

```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
langgraph new path/to/your/app --template new-langgraph-project-python
cd path/to/your/app
```

<Tip>
  Run `langgraph new` without `--template` for an interactive menu of available templates.
</Tip>

## 2. Set your API key

Add your LangSmith API key to a `.env` file in your project root:

```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
LANGSMITH_API_KEY=lsv2_...
```

The `langgraph deploy` command reads this automatically. Alternatively, pass it inline:

```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
LANGSMITH_API_KEY=lsv2_... langgraph deploy
```

## 3. Deploy

Deploy directly from the CLI or via the UI.

<Tabs>
  <Tab title="Deploy from CLI">
    Run the deploy command from your project directory:

    ```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    langgraph deploy
    ```

    This creates a `dev` deployment named after your project directory by default. Use `--name` or `--deployment-type prod` to override.

    <Tip>
      To update an existing deployment after making code changes, re-run `langgraph deploy`. It finds the existing deployment by name and updates it in place.
    </Tip>

    You can also use `langgraph deploy list` to see all deployments, `langgraph deploy logs` to tail runtime logs, and `langgraph deploy delete <ID>` to remove a deployment. For details, refer to the [CLI reference](/langsmith/cli#deploy).
  </Tab>

  <Tab title="Deploy from Studio">
    To deploy from studio:

    1. Start the [local development server](/langsmith/local-dev-testing#langgraph-dev). This will automatically open up [Studio](/langsmith/studio), an interactive agent IDE.

    ```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    langgraph dev
    ```

    2. Click the `deploy` button.
       <img alt="Deploy from Studio" />
  </Tab>
</Tabs>

## 4. Test in Studio

[Studio](/langsmith/studio) is an interactive agent IDE connected directly to your deployment. Use it to send messages, inspect intermediate state at each node, edit state mid-run, and replay from any prior checkpoint without writing code.

Once the deployment is ready:

1. Go to [LangSmith](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-deployment-quickstart) and select **Deployments** in the left sidebar.
2. Select your deployment to view its details.
3. Click **Studio** in the top right corner to open [Studio](/langsmith/studio).

## 5. Test the API

Copy the **API URL** from the deployment details view, then use it to call your application:

<Tabs>
  <Tab title="Python SDK (Async)">
    1. Install the LangGraph Python SDK:
       ```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
       pip install langgraph-sdk
       ```
    2. Send a message to the assistant (stateless run):
       ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
       from langgraph_sdk import get_client

       client = get_client(url="your-deployment-url", api_key="your-langsmith-api-key")

       async for chunk in client.runs.stream(
           None,  # Threadless run
           "agent", # Name of assistant. Defined in langgraph.json.
           input={
               "messages": [{
                   "role": "human",
                   "content": "What is LangGraph?",
               }],
           },
           stream_mode="updates",
       ):
           print(f"Receiving new event of type: {chunk.event}...")
           print(chunk.data)
           print("\n\n")
       ```
  </Tab>

  <Tab title="Python SDK (Sync)">
    1. Install the LangGraph Python SDK:
       ```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
       pip install langgraph-sdk
       ```
    2. Send a message to the assistant (threadless run):
       ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
       from langgraph_sdk import get_sync_client

       client = get_sync_client(url="your-deployment-url", api_key="your-langsmith-api-key")

       for chunk in client.runs.stream(
           None,  # Threadless run
           "agent", # Name of assistant. Defined in langgraph.json.
           input={
               "messages": [{
                   "role": "human",
                   "content": "What is LangGraph?",
               }],
           },
           stream_mode="updates",
       ):
           print(f"Receiving new event of type: {chunk.event}...")
           print(chunk.data)
           print("\n\n")
       ```
  </Tab>

  <Tab title="JavaScript SDK">
    1. Install the LangGraph JS SDK:
       ```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
       npm install @langchain/langgraph-sdk
       ```
    2. Send a message to the assistant (threadless run):
       ```js theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
       const { Client } = await import("@langchain/langgraph-sdk");

       const client = new Client({ apiUrl: "your-deployment-url", apiKey: "your-langsmith-api-key" });

       const streamResponse = client.runs.stream(
           null, // Threadless run
           "agent", // Assistant ID
           {
               input: {
                   "messages": [
                       { "role": "user", "content": "What is LangGraph?"}
                   ]
               },
               streamMode: "messages",
           }
       );

       for await (const chunk of streamResponse) {
           console.log(`Receiving new event of type: ${chunk.event}...`);
           console.log(JSON.stringify(chunk.data));
           console.log("\n\n");
       }
       ```
  </Tab>

  <Tab title="Rest API">
    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    curl -s --request POST \
        --url <DEPLOYMENT_URL>/runs/stream \
        --header 'Content-Type: application/json' \
        --header "X-Api-Key: <LANGSMITH API KEY>" \
        --data "{
            \"assistant_id\": \"agent\",
            \"input\": {
                \"messages\": [
                    {
                        \"role\": \"human\",
                        \"content\": \"What is LangGraph?\"
                    }
                ]
            },
            \"stream_mode\": \"updates\"
        }"
    ```
  </Tab>
</Tabs>

## Next steps

<CardGroup>
  <Card title="Assistants" icon="robot" href="/langsmith/assistants">
    Deploy the same graph with different models, prompts, or tools per assistant.
  </Card>

  <Card title="Threads" icon="messages" href="/langsmith/use-threads">
    Persist state across multiple runs so your agent remembers context between interactions.
  </Card>

  <Card title="Runs" icon="player-play" href="/langsmith/background-run">
    Kick off background runs for long-running jobs and stream results back to your client.
  </Card>
</CardGroup>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/deployment-quickstart.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Deploy Managed Deep Agents
Source: https://docs.langchain.com/langsmith/deployment-quickstart-da

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/deployment-quickstart-da.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Troubleshooting for self-hosted deployments
Source: https://docs.langchain.com/langsmith/diagnostics-self-hosted

Diagnostic steps for troubleshooting self-hosted LangSmith Deployment issues before contacting support.

This page provides diagnostic steps to help you troubleshoot issues with self-hosted [LangSmith Deployment](/langsmith/deployment) before reaching out to support. Follow these steps systematically to identify and resolve common deployment issues.

<Callout icon="headset">
  If you complete these diagnostic steps and still need assistance, refer to [Support](#support) at the end of this guide for information on what to gather before reaching out.
</Callout>

## Prerequisites

Before beginning the diagnostic steps, ensure you have:

* `kubectl` access to your Kubernetes cluster.
* Appropriate permissions to view pods, deployments, services, etc.
* Familiarity with your [Helm chart configuration](/langsmith/kubernetes#configure-your-helm-charts:).

## Step 1. Understand your deployment

Verify what was deployed and understand the baseline state of your system. This helps you recognize what normal operation looks like and identify deviations when issues occur.

Run the following commands to view all deployed Kubernetes resources.

<Note>
  Ensure that you're in the correct namespace when you run the commands in this section. Or, specify the namespace explicitly with the `-n` flag. For example: `kubectl get deployments -n langsmith`.
</Note>

List all deployments:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
kubectl get deployments
```

List all pods:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
kubectl get pods
```

List all services:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
kubectl get services
```

List all `lgps` resources (only present after creating an [Agent Server](/langsmith/agent-server)):

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
kubectl get lgps
```

### Key deployed components

Your deployment includes the following core components:

* **`langsmith-frontend`**: The LangSmith frontend UI where you create Agent Server deployments. This app makes API calls to `langsmith-host-backend`. Part of the [control plane](/langsmith/control-plane).
* **`langsmith-host-backend`**: The LangSmith Deployment [control plane](/langsmith/control-plane) that receives requests from `langsmith-frontend` and persists deployment requests to the control plane Postgres database.
* **`langsmith-listener`**: Part of the LangSmith Deployment [data plane](/langsmith/data-plane). Polls `langsmith-host-backend` via HTTP API for deployments to create, update, or delete. Enqueues tasks for worker processes to handle.
* **`langsmith-redis`**: The [Redis](/langsmith/data-plane#redis) instance serving as the task queue for `langsmith-listener`. The listener enqueues tasks here and workers pull tasks from this queue.
* **`langsmith-operator`**: The `lgps` Kubernetes operator that reconciles underlying Kubernetes resources for `lgps` resources. Part of the data plane infrastructure.

<Note>
  Additional components may be present in your deployment depending on your configuration. For an overview, refer to [LangSmith Deployment components](/langsmith/components).
</Note>

## Step 2. Enable debug logging

When troubleshooting issues, the first step is typically to enable debug-level logging to gather more detailed information about what's happening in your system.

### For control plane or data plane deployments

If you are experiencing issues with a control plane deployment (for example, `langsmith-host-backend`) or a data plane deployment (for example, `langsmith-listener`), reinstall the Helm chart with the `LOG_LEVEL=DEBUG` environment variable. Add the following to your `values.yaml` file:

```yaml theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
extraEnv:
  - name: LOG_LEVEL
    value: DEBUG
```

### For Agent Server deployments

If the issue is with an individual Agent Server deployment:

1. Navigate to the **Deployments** tab in the [LangSmith UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-diagnostics-self-hosted).
2. On a deployment's view, select **+ New Revision**.
3. Add a new environment variable `LOG_LEVEL` and set it to `DEBUG`.

<Note>
  You can also find debug logs in the UI on a deployment's view, click on **Server Logs** and select **Debug** for the **Log level: Info** dropdown.
</Note>

### For widespread issues

If you are unsure where the issue originates, enable `DEBUG` logging everywhere (control plane, data plane, and all Agent Server deployments).

### Review application logs

Tail the logs of each pod to understand baseline behavior:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
kubectl logs -f <pod_name>
```

Then look for these log lines:

* **`langsmith-listener`**: `Reconciling projects...` (appears every 10 seconds)
* **`langsmith-operator`**: `Starting reconciliation` (appears periodically)

In a healthy deployment, you should not see any errors. All logs should appear normal and routine.

### Interpret debug logs

Look for the following problem indicators:

* Exceptions or stack traces.
* Error messages (the word `"ERROR"`).
* Unusual patterns that differ from normal operation.

Based on the errors you find:

* **Configuration issue**: If you suspect a configuration problem, raise the issue with the person who ran [`helm install`](/langsmith/kubernetes).
* **User code bug**: If you suspect a bug in user code (for example, the LangGraph OSS graph implementation), raise the issue with the owner of the Agent Server application who created the [`langgraph.json`](/langsmith/application-structure#configuration-file) file.

## Step 3. Describe deployments and pods

Describing Kubernetes resources reveals error events and statuses that may not appear in application logs. These errors are typically caused by configuration or infrastructure issues rather than application code bugs. Describing resources also shows their configuration (such as environment variables), which is helpful for debugging.

Run the following commands to describe your resources.

Describe a Kubernetes deployment:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
kubectl describe deployment <deployment_name>
```

Describe a Kubernetes pod:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
kubectl describe pod <pod_name>
```

Describe an `lgps` resource (only relevant after creating an Agent Server):

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
kubectl describe lgps <lgps_name>
```

### Interpret results

Review the `Events:` section of the output and verify that everything is normal. Common issues that appear include:

* Failed liveness or readiness probes
* Image pull errors
* Resource constraints (CPU, memory)
* Volume mount issues
* Configuration errors

Make sure there are no error events and that all events indicate healthy operation.

## Additional resources

For more troubleshooting information, refer to:

* [Troubleshooting](/langsmith/troubleshooting): General troubleshooting guide with solutions to common issues.
* [Self-hosted overview](/langsmith/self-hosted): Details on system architecture and component interactions.

## Support

If you have followed these diagnostic steps and still need assistance, gather the following information before contacting support:

* Output from the [diagnostic steps](#step-1-understand-your-deployment).
* Your Helm chart configuration.
* Relevant error messages and logs.
* Description of what you were trying to do when the issue occurred.

Having this information ready will help the [support](https://support.langchain.com) team diagnose and resolve your issue more quickly.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/diagnostics-self-hosted.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Implement distributed tracing
Source: https://docs.langchain.com/langsmith/distributed-tracing

Sometimes, you need to trace a request across multiple services.

LangSmith supports distributed tracing out of the box, linking runs within a trace across services using context propagation headers (`langsmith-trace` and optional `baggage` for metadata/tags).

Example client-server setup:

* Trace starts on client
* Continues on server

## Distributed tracing in Python

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}

# client.py
from langsmith.run_helpers import get_current_run_tree, traceable
import httpx

@traceable
async def my_client_function():
    headers = {}
    async with httpx.AsyncClient(base_url="...") as client:
        if run_tree := get_current_run_tree():
            # add langsmith-id to headers
            headers.update(run_tree.to_headers())
        return await client.post("/my-route", headers=headers)
```

Then the server (or other service) can continue the trace by handling the headers appropriately. If you are using an asgi app Starlette or FastAPI, you can connect the distributed trace using LangSmith's `TracingMiddleware`.

<Info>
  The `TracingMiddleware` class was added in `langsmith==0.1.133`.
</Info>

Example using FastAPI:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langsmith import traceable
from langsmith.middleware import TracingMiddleware
from fastapi import FastAPI, Request

app = FastAPI()  # Or Flask, Django, or any other framework
app.add_middleware(TracingMiddleware)

@traceable
async def some_function():
    ...

@app.post("/my-route")
async def fake_route(request: Request):
    return await some_function()
```

Or in Starlette:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from starlette.applications import Starlette
from starlette.middleware import Middleware
from langsmith.middleware import TracingMiddleware

routes = ...
middleware = [
    Middleware(TracingMiddleware),
]
app = Starlette(..., middleware=middleware)
```

If you are using other server frameworks, you can always "receive" the distributed trace by passing the headers in through `langsmith_extra`:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}

# server.py
import langsmith as ls
from fastapi import FastAPI, Request

@ls.traceable
async def my_application():
    ...

app = FastAPI()  # Or Flask, Django, or any other framework

@app.post("/my-route")
async def fake_route(request: Request):
    # request.headers:  {"langsmith-trace": "..."}
    # as well as optional metadata/tags in `baggage`
    with ls.tracing_context(parent=request.headers):
        return await my_application()
```

The example above uses the `tracing_context` context manager. You can also directly specify the parent run context in the `langsmith_extra` parameter of a method wrapped with `@traceable`.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}

# ... same as above

@app.post("/my-route")
async def fake_route(request: Request):
    # request.headers:  {"langsmith-trace": "..."}
    my_application(langsmith_extra={"parent": request.headers})
```

## Distributed tracing in TypeScript

<Note>
  Distributed tracing in TypeScript requires `langsmith` version `>=0.1.31`
</Note>

First, we obtain the current run tree from the client and convert it to `langsmith-trace` and `baggage` header values, which we can pass to the server:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
// client.mts
import { getCurrentRunTree, traceable } from "langsmith/traceable";

const client = traceable(
    async () => {
        const runTree = getCurrentRunTree();
        return await fetch("...", {
            method: "POST",
            headers: runTree.toHeaders(),
        }).then((a) => a.text());
    },
    { name: "client" }
);

await client();
```

Then, the server converts the headers back to a run tree, which it uses to further continue the tracing.

To pass the newly created run tree to a traceable function, we can use the `withRunTree` helper, which will ensure the run tree is propagated within traceable invocations.

<CodeGroup>
  ```typescript Express.JS theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  // server.mts
  import { RunTree } from "langsmith";
  import { traceable, withRunTree } from "langsmith/traceable";
  import express from "express";
  import bodyParser from "body-parser";

      const server = traceable(
          (text: string) => `Hello from the server! Received "${text}"`,
          { name: "server" }
      );

      const app = express();
      app.use(bodyParser.text());

  app.post("/", async (req, res) => {
      const runTree = RunTree.fromHeaders(req.headers);
      const result = await withRunTree(runTree, () => server(req.body));
      res.send(result);
  });
  ```

  ```typescript Hono theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  // server.mts
  import { RunTree } from "langsmith";
  import { traceable, withRunTree } from "langsmith/traceable";
  import { Hono } from "hono";

      const server = traceable(
          (text: string) => `Hello from the server! Received "${text}"`,
          { name: "server" }
      );

      const app = new Hono();

  app.post("/", async (c) => {
      const body = await c.req.text();
      const runTree = RunTree.fromHeaders(c.req.raw.headers);
      const result = await withRunTree(runTree, () => server(body));
      return c.body(result);
  });
  ```
</CodeGroup>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/distributed-tracing.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Double texting
Source: https://docs.langchain.com/langsmith/double-texting

<Info>
  **Prerequisites**

  * [Agent Server](/langsmith/agent-server)
</Info>

Many times users might interact with your graph in unintended ways.
For instance, a user may send one message and before the graph has finished running send a second message.
More generally, users may invoke the graph a second time before the first run has finished.
We call this "double texting".

[Enqueue](#enqueue-default) is the default double texting (multi-tasking) strategy when creating runs in the [Agent Server](/langsmith/agent-server).

<Note>
  Double texting is a feature of LangSmith Deployment. It is not available in the [LangGraph open source framework](/oss/python/langgraph/overview).
</Note>

<img alt="Double-text strategies across first vs. second run: Reject keeps only the first; Enqueue runs the second afterward; Interrupt halts the first to run the second; Rollback reverts the first and reruns with the second." />

## Enqueue (default)

This option allows the current run to finish before processing any new input. Incoming requests are queued and executed sequentially once prior runs complete.

For configuring the enqueue double text option, refer to the [how-to guide](/langsmith/enqueue-concurrent).

## Reject

This option rejects any additional incoming runs while a current run is in progress and prevents concurrent execution or double texting.

For configuring the reject double text option, refer to the [how-to guide](/langsmith/reject-concurrent).

## Interrupt

This option halts the current execution and preserves the progress made up to the interruption point. The new user input is then inserted, and execution continues from that state.

When using this option, your graph must account for potential edge cases. For example, a tool call may have been initiated but not yet completed at the time of interruption. In these cases, handling or removing partial tool calls may be necessary to avoid unresolved operations.

For configuring the interrupt double text option, refer to the [how-to guide](/langsmith/interrupt-concurrent).

## Rollback

This option halts the current execution and reverts all progress—including the initial run input—before processing the new user input. The new input is treated as a fresh run, starting from the initial state.

For configuring the rollback double text option, refer to the [how-to guide](/langsmith/rollback-concurrent).

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/double-texting.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Add encryption at rest
Source: https://docs.langchain.com/langsmith/encryption

Agent Server supports encryption at rest for checkpoint data and metadata. You can choose between basic encryption with a single key or custom encryption for advanced use cases.

## Choosing an encryption method

| Method                | What's encrypted                                         | Use case                                                                |
| --------------------- | -------------------------------------------------------- | ----------------------------------------------------------------------- |
| **Basic encryption**  | Checkpoint blobs, optionally JSON fields                 | Single static key, automatic AES encryption, selective field encryption |
| **Custom encryption** | Checkpoints, threads, runs, assistants, crons and stores | Per-tenant keys, KMS integration                                        |

## Basic encryption

For simple encryption with a single static key, set the `LANGGRAPH_AES_KEY` environment variable. LangGraph will automatically encrypt checkpoint blobs using AES.

1. Add `pycryptodome` to your dependencies in `langgraph.json`:
   ```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
   {
     "dependencies": [".", "pycryptodome"],
     "graphs": {
       "agent": "./agent.py:graph"
     }
   }
   ```

2. Set the `LANGGRAPH_AES_KEY` environment variable to a 16, 24, or 32-byte key (for AES-128, AES-192, or AES-256 respectively).

### Encrypting JSON fields

To also encrypt specific JSON fields, set `LANGGRAPH_AES_JSON_KEYS` to a comma-separated list of keys to encrypt:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
export LANGGRAPH_AES_KEY="your-16-24-or-32-byte-key"
export LANGGRAPH_AES_JSON_KEYS="api_key,secret_token,user_credentials"
```

These keys are encrypted wherever they appear in thread, assistant, run, cron, and store data.

<Warning>
  Encrypted fields cannot be searched or filtered.
</Warning>

System fields cannot be encrypted: `langgraph_version`, `langgraph_api_version`, `langgraph_plan`, `langgraph_host`, `langgraph_api_url`, `langgraph_request_id`, `langgraph_auth_user_id`, and `langgraph_auth_permissions`.

## Custom encryption

<Note>
  Requires Agent Server version 0.6.22+ and Python SDK version `langgraph-sdk>=0.3.1`.
</Note>

<Warning>
  Agent Server versions 0.5.34–0.6.21 included a pre-release version of custom encryption. Data encrypted with these versions will be corrupted when upgrading to 0.6.22+. Do not use custom encryption on these versions.
</Warning>

<Warning>
  Only use custom encryption if basic encryption doesn't meet your needs. Custom encryption requires you to implement and maintain encryption handlers, and adds operational complexity. If you only need a single static key with optional selective field encryption, use [basic encryption](#basic-encryption) instead.
</Warning>

Use custom encryption when you need:

* **Per-tenant key isolation** — different encryption keys for different customers
* **KMS integration** — AWS KMS, Google Cloud KMS, or HashiCorp Vault for key management, rotation, and audit logging

### How it works

1. [Configure](#configuration) the encryption module path in `langgraph.json`
2. [Define your encryption module](#defining-your-encryption-module) with handlers for blob and JSON encryption
3. [Pass encryption context](#passing-encryption-context) (like tenant ID) via the `X-Encryption-Context` header
4. LangGraph calls your handlers before storing and after retrieving data

For production deployments with key rotation and audit logging, see [Envelope encryption with AWS Encryption SDK](#envelope-encryption-with-aws-encryption-sdk).

### Configuration

Add your encryption module to `langgraph.json`:

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "dependencies": ["."],
  "graphs": {
    "agent": "./agent.py:graph"
  },
  "encryption": {
    "path": "./encryption.py:encryption"
  }
}
```

<Note>
  If you're migrating from basic encryption, keep `LANGGRAPH_AES_KEY` configured. Custom encryption handles new writes while existing AES-encrypted data remains readable.
</Note>

### Defining your encryption module

#### Blob encryption (checkpoints)

Blob handlers encrypt checkpoint data—the serialized state from graph execution. Here's a simplified example using per-tenant keys with [Fernet](https://cryptography.io/en/latest/fernet/) (a symmetric encryption scheme from the `cryptography` library):

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import os
from cryptography.fernet import Fernet
from langgraph_sdk import Encryption, EncryptionContext

encryption = Encryption()

# In production, fetch from a secrets manager
TENANT_KEYS = {
    "tenant-a": Fernet(os.environ["TENANT_A_KEY"]),
    "tenant-b": Fernet(os.environ["TENANT_B_KEY"]),
}

def _get_fernet(ctx: EncryptionContext) -> Fernet:
    tenant_id = ctx.metadata.get("tenant_id")
    if not tenant_id or tenant_id not in TENANT_KEYS:
        raise ValueError(f"Unknown tenant: {tenant_id}")
    return TENANT_KEYS[tenant_id]

@encryption.encrypt.blob
async def encrypt_blob(ctx: EncryptionContext, data: bytes) -> bytes:
    return _get_fernet(ctx).encrypt(data)

@encryption.decrypt.blob
async def decrypt_blob(ctx: EncryptionContext, data: bytes) -> bytes:
    return _get_fernet(ctx).decrypt(data)
```

The `ctx.metadata` dict comes from the `X-Encryption-Context` header and is stored in plaintext alongside encrypted data, so the correct key is used on decryption.

#### JSON encryption (metadata)

JSON handlers encrypt structured data like thread metadata, assistant context, and run kwargs. Unlike blob encryption, you choose which fields to encrypt—keeping some unencrypted for search and filtering.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import json
import os
from cryptography.fernet import Fernet
from langgraph_sdk import Encryption, EncryptionContext

encryption = Encryption()

TENANT_KEYS = {
    "tenant-a": Fernet(os.environ["TENANT_A_KEY"]),
    "tenant-b": Fernet(os.environ["TENANT_B_KEY"]),
}

SKIP_FIELDS = {
    "tenant_id", "owner",
    "run_id", "thread_id", "graph_id", "assistant_id", "user_id", "checkpoint_id",
    "source", "step", "parents", "run_attempt",
    "langgraph_version", "langgraph_api_version", "langgraph_plan", "langgraph_host",
    "langgraph_api_url", "langgraph_request_id", "langgraph_auth_user",
    "langgraph_auth_user_id", "langgraph_auth_permissions",
}
ENCRYPTED_PREFIX = "encrypted:"

def _get_fernet(ctx: EncryptionContext) -> Fernet:
    tenant_id = ctx.metadata.get("tenant_id")
    if not tenant_id or tenant_id not in TENANT_KEYS:
        raise ValueError(f"Unknown tenant: {tenant_id}")
    return TENANT_KEYS[tenant_id]

@encryption.encrypt.json
async def encrypt_json(ctx: EncryptionContext, data: dict) -> dict:
    fernet = _get_fernet(ctx)
    result = {}
    for k, v in data.items():
        if k in SKIP_FIELDS or v is None:
            result[k] = v
        else:
            value_json = json.dumps(v)
            encrypted = fernet.encrypt(value_json.encode()).decode()
            result[k] = ENCRYPTED_PREFIX + encrypted
    return result

@encryption.decrypt.json
async def decrypt_json(ctx: EncryptionContext, data: dict) -> dict:
    fernet = _get_fernet(ctx)
    result = {}
    for k, v in data.items():
        if isinstance(v, str) and v.startswith(ENCRYPTED_PREFIX):
            encrypted_value = v[len(ENCRYPTED_PREFIX):]
            decrypted = fernet.decrypt(encrypted_value.encode()).decode()
            result[k] = json.loads(decrypted)
        else:
            result[k] = v
    return result
```

#### JSON encryption considerations

<Warning>
  **Encrypted fields cannot be searched or filtered.** Design your metadata schema so that fields you need to query remain unencrypted.
</Warning>

<Warning>
  **JSON encryptors must preserve key structure.** SQL JSONB merge operations work at the key level. Encryptors that change keys—whether by consolidating fields (e.g., moving sensitive data into `__encrypted__`) or by encrypting key names themselves—cause data loss during merges. Use per-key encryption: transform values in-place while preserving keys.
</Warning>

<Note>
  **Migration consideration:** Use a recognizable prefix or format in encrypted values so your decryptor can detect and skip unencrypted data. This allows you to encrypt additional fields in the future without re-encrypting existing records. The example above uses this pattern.
</Note>

<Note>
  **Performance consideration:** Per-key encryption means one encryption call per field. If your encryption involves round-trips to an external service (e.g., KMS), this can significantly impact latency. Consider caching data keys locally or using envelope encryption where you encrypt a local data key with KMS and use it for multiple fields.
</Note>

User-defined fields for authorization (e.g., `tenant_id`, `owner`) should generally be left **unencrypted**, as should fields used for search and filtering. Additionally, **some system-managed fields will never be encrypted**:

* Resource identifiers (`thread_id`, `run_id`, `assistant_id`, `graph_id`, `checkpoint_id`, `task_id`)
* Most fields beginning with `langgraph_` (except for `langgraph_auth_user`)
* Required checkpoint metadata (`source`, `step`, `parents`, `run_attempt`)
* Internal fields used for scheduling and orchestration (`__after_seconds__`, `__request_start_time_ms__`, most fields beginning with `__pregel`)
* Run-level execution limits (`max_concurrency`, `recursion_limit`) specified in a run's `config`
* Thread TTL updates (`ttl`) specified in a run's `config.configurable`

#### What gets encrypted

**JSON handlers** (`@encryption.encrypt.json` / `@encryption.decrypt.json`) are applied recursively to the following fields:

* `thread.metadata`, `thread.values`
* `assistant.metadata`, `assistant.context`
* `run.metadata`, `run.kwargs`
* `cron.metadata`, `cron.payload`
* `store.value`

[Some fields are excluded from encryption.](#what-gets-encrypted) Unless otherwise noted, these exclusions apply at every level of a nested JSON object, not just the root level.

**Blob handlers** (`@encryption.encrypt.blob` / `@encryption.decrypt.blob`) are applied to checkpoint blobs (graph execution state).

#### Deriving context from authentication

Instead of passing `X-Encryption-Context` explicitly, derive encryption context from the authenticated user:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langgraph_sdk import Encryption, EncryptionContext
from starlette.authentication import BaseUser

encryption = Encryption()

@encryption.context
async def get_encryption_context(user: BaseUser, ctx: EncryptionContext) -> dict:
    return {
        **ctx.metadata,
        "tenant_id": user["tenant_id"],
    }
```

This handler runs once per request after authentication. The returned dict becomes `ctx.metadata` for all encryption operations in that request.

### Passing encryption context

Pass encryption context via the `X-Encryption-Context` header. The context is arbitrary data that you define—you control the schema and can include any fields your encryption logic needs (e.g., `tenant_id`, `key_version`). The context is available in your handlers as `ctx.metadata` and is stored in plaintext for use during decryption.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import base64
import json
from langgraph_sdk import get_client

encryption_context = base64.b64encode(
    json.dumps({"tenant_id": "tenant-a"}).encode()
).decode()

client = get_client(url="http://localhost:2024")

result = await client.runs.wait(
    thread_id=None,
    assistant_id="agent",
    input={"messages": [{"role": "user", "content": "Hello"}]},
    headers={"X-Encryption-Context": encryption_context},
)
```

<Note>
  The encryption context is stored in plaintext. On decryption, it's automatically restored—callers don't need to pass the header when reading.
</Note>

### Envelope encryption with AWS Encryption SDK

For production deployments on AWS, use the [AWS Encryption SDK](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/python.html) with AWS KMS, or an equivalent within your cloud provider. This approach:

* Handles envelope encryption automatically (no manual key packing)
* Provides key rotation and audit logging
* Binds ciphertext to encryption context (tenant isolation)
* Caches data keys locally to avoid repeated KMS calls, latency and rate limits

#### Complete example

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import base64
import json
import os

import aws_encryption_sdk
from aws_encryption_sdk import (
    CachingCryptoMaterialsManager,
    CommitmentPolicy,
    LocalCryptoMaterialsCache,
    StrictAwsKmsMasterKeyProvider,
)
from langgraph_sdk import Encryption, EncryptionContext

encryption = Encryption()

# The SDK uses envelope encryption: one KMS API call generates a data key,

# then encrypts/decrypts locally. The cache reuses data keys across operations.
client = aws_encryption_sdk.EncryptionSDKClient(
    commitment_policy=CommitmentPolicy.REQUIRE_ENCRYPT_REQUIRE_DECRYPT
)
key_provider = StrictAwsKmsMasterKeyProvider(key_ids=[os.environ["KMS_KEY_ARN"]])
cache = LocalCryptoMaterialsCache(capacity=100)
cmm = CachingCryptoMaterialsManager(
    master_key_provider=key_provider,
    cache=cache,
    max_age=300.0,
    max_messages_encrypted=100,
)

SKIP_FIELDS = {
    "tenant_id", "owner",
    "run_id", "thread_id", "graph_id", "assistant_id", "user_id", "checkpoint_id",
    "source", "step", "parents", "run_attempt",
    "langgraph_version", "langgraph_api_version", "langgraph_plan", "langgraph_host",
    "langgraph_api_url", "langgraph_request_id", "langgraph_auth_user",
    "langgraph_auth_user_id", "langgraph_auth_permissions",
}
ENCRYPTED_PREFIX = "encrypted:"

@encryption.encrypt.blob
async def encrypt_blob(ctx: EncryptionContext, data: bytes) -> bytes:
    ciphertext, _ = client.encrypt(
        source=data,
        materials_manager=cmm,
        encryption_context={"tenant_id": ctx.metadata["tenant_id"]},
    )
    return ciphertext

@encryption.decrypt.blob
async def decrypt_blob(ctx: EncryptionContext, data: bytes) -> bytes:
    plaintext, _ = client.decrypt(source=data, key_provider=key_provider)
    return plaintext

@encryption.encrypt.json
async def encrypt_json(ctx: EncryptionContext, data: dict) -> dict:
    tenant_id = ctx.metadata["tenant_id"]
    result = {}
    for k, v in data.items():
        if k in SKIP_FIELDS or v is None:
            result[k] = v
        else:
            ciphertext, _ = client.encrypt(
                source=json.dumps(v).encode(),
                materials_manager=cmm,
                encryption_context={"tenant_id": tenant_id},
            )
            result[k] = ENCRYPTED_PREFIX + base64.b64encode(ciphertext).decode()
    return result

@encryption.decrypt.json
async def decrypt_json(ctx: EncryptionContext, data: dict) -> dict:
    result = {}
    for k, v in data.items():
        if isinstance(v, str) and v.startswith(ENCRYPTED_PREFIX):
            ciphertext = base64.b64decode(v[len(ENCRYPTED_PREFIX):])
            plaintext, _ = client.decrypt(source=ciphertext, key_provider=key_provider)
            result[k] = json.loads(plaintext.decode())
        else:
            result[k] = v
    return result
```

The `encryption_context` is cryptographically bound to the ciphertext via KMS—decryption fails if the context doesn't match. The context is embedded in the ciphertext, so decrypt handlers don't need to reference `ctx.metadata`.

#### Key rotation

KMS handles master key rotation automatically. When you enable automatic rotation on your KMS key, old encrypted data keys can still be decrypted while new operations use the rotated key material. No re-encryption of existing data is required.

## Related

* [Custom authentication](/langsmith/custom-auth)

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/encryption.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
