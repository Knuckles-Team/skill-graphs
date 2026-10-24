# Install Mission Control
Source: https://docs.langchain.com/langsmith/self-hosted-mission-control

Install Mission Control, an in-cluster console for monitoring, configuring, and operating self-hosted LangSmith on Kubernetes.

Mission Control is an in-cluster console for monitoring, configuring, and operating LangSmith on Kubernetes. It runs inside your cluster and is accessed with `kubectl port-forward` by default, so no ingress is required.

There are two install paths:

| Path                              | Best for                                                                                    |
| --------------------------------- | ------------------------------------------------------------------------------------------- |
| [Quick install](#quick-install)   | Customers who can run a reviewed shell installer and want the shortest setup.               |
| [Manual install](#manual-install) | Organizations that do not allow installer scripts or need each Kubernetes command reviewed. |

The public install assets are:

* `install-script.sh`: one installer with separate `prereqs`, `namespace`, `secret`, `values`, `install`, and `forward` steps.
* `values.yaml`: default Helm values for a port-forward-only install.

Mission Control images are published to two Docker Hub repositories: `langchain/mission-control-backend` and `langchain/mission-control-frontend`. The latest images can be checked with:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
docker pull langchain/mission-control-backend:latest
docker pull langchain/mission-control-frontend:latest
```

Browser review links:

* `https://github.com/langchain-ai/helm/tree/main/charts/mission-control/install-script.sh`
* `https://github.com/langchain-ai/helm/tree/main/charts/mission-control/values.yaml`

The commands below use raw GitHub URLs so `curl` can download the files directly. If you publish these files from a different repo or branch, replace the raw base URL below.

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
MC_RAW_BASE=https://raw.githubusercontent.com/langchain-ai/helm/main/charts/mission-control
```

## Prerequisites

| Tool      | Minimum version     | Install example        |
| --------- | ------------------- | ---------------------- |
| `kubectl` | 1.24+               | `brew install kubectl` |
| `helm`    | 3.x                 | `brew install helm`    |
| `curl`    | any current version | Usually preinstalled   |

You must run the installer against the Kubernetes cluster where LangSmith is installed or will be installed. Confirm the active context before continuing:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
kubectl config current-context
```

The installer identity needs permission to create the Mission Control namespace resources and cluster-scoped RBAC:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
kubectl auth can-i create clusterrole
kubectl auth can-i create clusterrolebinding
kubectl auth can-i create serviceaccount -n langsmith
kubectl auth can-i create deployment -n langsmith
kubectl auth can-i create secret -n langsmith
```

All five commands should return `yes`. See [Permissions reference](#permissions-reference) for the runtime permissions granted to Mission Control.

## Quick install

Run these three commands:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
curl -fsSLO https://raw.githubusercontent.com/langchain-ai/helm/main/charts/mission-control/install-script.sh && chmod +x install-script.sh
curl -fsSL https://raw.githubusercontent.com/langchain-ai/helm/main/charts/mission-control/values.yaml -o values.yaml
./install-script.sh all -f values.yaml
```

The `all` step:

* Checks required tools and RBAC.
* Creates the `langsmith` namespace.
* Prompts for a Mission Control username and password.
* Stores those credentials in the `mission-control-auth` Kubernetes Secret.
* Writes `values.yaml` if one does not already exist.
* Installs from the public Helm chart repository if you are not running from a local chart checkout.
* Installs Mission Control with Helm.

The RBAC check runs:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
kubectl auth can-i create clusterrole
kubectl auth can-i create clusterrolebinding
kubectl auth can-i create serviceaccount -n langsmith
kubectl auth can-i create deployment -n langsmith
kubectl auth can-i create secret -n langsmith
```

If your organization intentionally blocks `kubectl auth can-i` but Helm installs are approved through another control path, run:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
./install-script.sh all -f values.yaml --skip-rbac-check
```

### Access the UI

After the install finishes, start a local port-forward:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
./install-script.sh forward
```

Open [http://localhost:3000](http://localhost:3000/) and log in with the username and password you entered.

### Review the script first

The quick install path downloads the script before running it, so you can review `install-script.sh` locally before the third command.

### Edit values before install

The quick install path also downloads `values.yaml` before running the installer. Review or edit that file before the third command if you need to change namespace, resources, ingress, feature flags, or diagnostic persistence.

Common edits:

| Setting                                                        | When to change it                                                                                   |
| -------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| `namespace`                                                    | Install Mission Control somewhere other than `langsmith`. Also pass `-n <namespace>` to the script. |
| `resources`                                                    | Your namespace has a `ResourceQuota` or your platform requires specific requests/limits.            |
| `ingress.enabled` and `ingress.host`                           | You want to expose Mission Control through your ingress controller instead of port-forwarding.      |
| `config.features.*`                                            | You need to remove specific write permissions or external egress features.                          |
| `diagnostics.persistence.enabled`                              | You want diagnostic bundles to survive pod restarts and Helm upgrades.                              |
| `backend.podSecurityContext` and `frontend.podSecurityContext` | Your platform requires containers to run as a specific non-root UID, such as `1001`.                |

Example with a custom namespace:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
curl -fsSLO https://raw.githubusercontent.com/langchain-ai/helm/main/charts/mission-control/install-script.sh && chmod +x install-script.sh
curl -fsSL https://raw.githubusercontent.com/langchain-ai/helm/main/charts/mission-control/values.yaml -o values.yaml
./install-script.sh all -n mission-control -f values.yaml
```

### Script command reference

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
./install-script.sh prereqs
./install-script.sh namespace
./install-script.sh secret
./install-script.sh values
./install-script.sh install
./install-script.sh forward
./install-script.sh all
```

Useful flags:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
./install-script.sh all -n langsmith -f values.yaml
./install-script.sh all -u admin
printf '%s\n' 'your-password' | ./install-script.sh secret -u admin --password-stdin
./install-script.sh all -f values.yaml --skip-rbac-check
./install-script.sh install --chart-ref langchain/mission-control
./install-script.sh install --chart-path /path/to/mission-control
./install-script.sh forward --port 3001:3000
```

## Manual install

Use this path when installer scripts are not allowed. These steps use normal `kubectl`, `helm`, and `curl` commands only.

<Steps>
  <Step title="Add the Helm repo and get the values file">
    Add the LangChain Helm repo:

    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    helm repo add langchain https://langchain-ai.github.io/helm
    helm repo update langchain
    ```

    Download the customer values file:

    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    curl -fsSL https://raw.githubusercontent.com/langchain-ai/helm/main/charts/mission-control/values.yaml -o values.yaml
    ```

    Review `values.yaml` before installing. Keep `config.auth.enabled: true` for production.

    If your platform requires non-root containers, Mission Control can run as UID `1001`. Add this to `values.yaml` before installing:

    ```yaml theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    backend:
      podSecurityContext:
        runAsNonRoot: true
        runAsUser: 1001
        runAsGroup: 1001
        fsGroup: 1001
      securityContext:
        allowPrivilegeEscalation: false
        capabilities:
          drop:
            - ALL
      extraEnv:
        - name: HOME
          value: /tmp
        - name: HELM_CACHE_HOME
          value: /tmp/.cache/helm
        - name: HELM_CONFIG_HOME
          value: /tmp/.config/helm
        - name: HELM_DATA_HOME
          value: /tmp/.local/share/helm

    frontend:
      podSecurityContext:
        runAsNonRoot: true
        runAsUser: 1001
        runAsGroup: 1001
      securityContext:
        allowPrivilegeEscalation: false
        capabilities:
          drop:
            - ALL
    ```
  </Step>

  <Step title="Create the namespace">
    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    kubectl create namespace langsmith --dry-run=client -o yaml | kubectl apply -f -
    ```
  </Step>

  <Step title="Create the auth credentials Secret">
    Credentials are stored in a Kubernetes Secret. They are not written to `values.yaml`.

    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    read -r -p "Username: " MC_USER
    read -r -s -p "Password: " MC_PASS; echo

    kubectl create secret generic mission-control-auth \
      --namespace=langsmith \
      --from-literal=username="$MC_USER" \
      --from-literal=password="$MC_PASS" \
      --dry-run=client -o yaml | kubectl apply -f -
    ```

    For multi-replica backend deployments, include a shared JWT signing key in the same Secret and set `config.auth.jwtSecretKey: jwtSecret` in `values.yaml`:

    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    JWT_SECRET="$(openssl rand -base64 32)"

    kubectl create secret generic mission-control-auth \
      --namespace=langsmith \
      --from-literal=username="$MC_USER" \
      --from-literal=password="$MC_PASS" \
      --from-literal=jwtSecret="$JWT_SECRET" \
      --dry-run=client -o yaml | kubectl apply -f -
    ```
  </Step>

  <Step title="Install with Helm">
    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    helm upgrade --install mission-control langchain/mission-control \
      --namespace langsmith \
      --create-namespace \
      --values values.yaml \
      --rollback-on-failure
    ```

    Wait for both workloads to become ready (the backend runs as a StatefulSet, the frontend as a Deployment):

    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    kubectl rollout status statefulset/mission-control-backend -n langsmith
    kubectl rollout status deployment/mission-control-frontend -n langsmith
    ```

    You can also inspect the pods directly:

    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    kubectl get pods -n langsmith
    ```
  </Step>

  <Step title="Access the UI">
    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    kubectl port-forward svc/mission-control-frontend 3000:3000 -n langsmith
    ```

    Open [http://localhost:3000](http://localhost:3000/) and log in with the credentials from step 3.
  </Step>
</Steps>

## Upgrade

Download the latest public values file, merge in any local changes you need, then run:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
helm repo update langchain

helm upgrade --install mission-control langchain/mission-control \
  --namespace langsmith \
  --values values.yaml \
  --rollback-on-failure
```

If you are working from a local chart checkout instead:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
helm upgrade --install mission-control . \
  --namespace langsmith \
  --values values.yaml \
  --rollback-on-failure
```

If you installed with the quick script and kept it locally:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
./install-script.sh install -f values.yaml
```

## Uninstall

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
helm uninstall mission-control -n langsmith
```

This removes the Mission Control release. It does not delete your namespace or unrelated LangSmith resources.

Optional cleanup of Mission Control-owned Secrets:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
kubectl delete secret -n langsmith \
  mission-control-auth \
  mission-control-draft \
  mission-control-deployed \
  mission-control-backup \
  mission-control-history \
  mission-control-alerts-config \
  mission-control-alerts-log \
  mission-control-alerts-key \
  mission-control-setup-token \
  --ignore-not-found
```

## Additional resources

### Troubleshooting

| Symptom                               | What to check                                                                                                                |
| ------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `kubectl auth can-i ...` returns `no` | Ask a cluster admin to grant install-time RBAC or run the install for you.                                                   |
| Pods stay `Pending`                   | Check namespace `ResourceQuota`, node capacity, and PVC/storage class events with `kubectl describe pod -n langsmith <pod>`. |
| Image pull errors                     | Confirm the cluster can pull `langchain/mission-control-backend:latest` and `langchain/mission-control-frontend:latest`.     |
| Login fails                           | Confirm `mission-control-auth` exists in the same namespace and has `username` and `password` keys.                          |
| Browser cannot connect                | Confirm the port-forward command is still running and no other local process is using port `3000`.                           |

### Permissions reference

The Helm chart creates a `ServiceAccount`, `ClusterRole`, and `ClusterRoleBinding` named `mission-control`. Most permissions are read-only. Write verbs are narrow and controlled by feature flags.

Install or upgrade requires the ability to create cluster-scoped RBAC (`ClusterRole` and `ClusterRoleBinding`), usually `cluster-admin` or a custom equivalent. The broadest runtime permission set is only used when `config.features.deploy: true`; that flag is enabled by default, set it to `false` for read-only installs.

#### Always-present read-only permissions

| Resource group      | Resources                                                                           | Verbs            |
| ------------------- | ----------------------------------------------------------------------------------- | ---------------- |
| Workloads           | pods, pods/log, deployments, statefulsets, replicasets, daemonsets, jobs, cronjobs  | get, list, watch |
| Networking          | services, endpoints, ingresses, ingressclasses                                      | get, list, watch |
| Storage             | persistentvolumeclaims, storageclasses                                              | get, list, watch |
| Cluster             | nodes, namespaces, events, serviceaccounts, resourcequotas                          | get, list, watch |
| Config              | configmaps, secrets                                                                 | get, list        |
| Metrics             | metrics.k8s.io pods/nodes                                                           | get, list, watch |
| RBAC                | roles, rolebindings, clusterroles, clusterrolebindings                              | get, list, watch |
| CRDs and extensions | customresourcedefinitions, leases, scaledobjects, httproutes, virtualservices, lgps | get, list, watch |

#### Feature-gated permissions

| Feature flag                     | Resources                                                          | Extra verbs                   |
| -------------------------------- | ------------------------------------------------------------------ | ----------------------------- |
| `config.features.configSave`     | secrets (`mission-control-draft`)                                  | create, update, delete        |
| `config.features.alerts`         | secrets (`mission-control-alerts-*`)                               | create, update, delete        |
| `config.features.fixIssue`       | pods                                                               | delete                        |
| `config.features.adopt`          | secrets, configmaps, serviceaccounts, deployments, statefulsets    | patch                         |
| `config.auth.enabled`            | secrets (`mission-control-auth`, setup-token), backend statefulset | create, update, delete, patch |
| `config.features.valuesOverride` | secrets (`mission-control-values-overrides`)                       | create, update, delete        |
| `config.features.deploy`         | workloads, networking, RBAC, CRDs, Helm release secrets            | create, update, patch, delete |

Set feature flags to `false` in `values.yaml` to remove the corresponding write verbs. With all feature flags disabled, Mission Control is effectively read-only except for authentication setup permissions when `config.auth.enabled: true`.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/self-hosted-mission-control.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# How to add semantic search to your agent deployment
Source: https://docs.langchain.com/langsmith/semantic-search

This guide explains how to add semantic search to your deployment's cross-thread [store](/oss/python/langgraph/stores), so that your agent can search for memories and other documents by semantic similarity.

## Prerequisites

* A deployment (refer to [how to set up an application for deployment](/langsmith/setup-app-requirements-txt)) and details on [hosting options](/langsmith/platform-setup).
* API keys for your embedding provider (in this case, OpenAI).
* `langchain >= 0.3.8` (if you specify using the string format below).

## Steps

1. Update your `langgraph.json` configuration file to include the store configuration:

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
    ...
    "store": {
        "index": {
            "embed": "openai:text-embedding-3-small",
            "dims": 1536,
            "fields": ["$"]
        }
    }
}
```

This configuration:

* Uses OpenAI's text-embedding-3-small model for generating embeddings
* Sets the embedding dimension to 1536 (matching the model's output)
* Indexes all fields in your stored data (`["$"]` means index everything, or specify specific fields like `["text", "metadata.title"]`)

<Note>
  Each deployment supports a single embedding model. Configuring multiple embedding models is not supported, as it would cause ambiguity in `/store` endpoints and result in mixed-index issues.
</Note>

1. To use the string embedding format above, make sure your dependencies include `langchain >= 0.3.8`:

```toml theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}

# In pyproject.toml
[project]
dependencies = [
    "langchain>=0.3.8"
]
```

Or if using [requirements.txt](/langsmith/setup-app-requirements-txt):

```
langchain>=0.3.8
```

## Usage

Once configured, you can use semantic search in your [nodes](/oss/python/langgraph/graph-api#nodes). The store requires a namespace tuple to organize memories:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
async def search_memory(state: State, *, store: BaseStore):
    # Search the store using semantic similarity
    # The namespace tuple helps organize different types of memories
    # e.g., ("user_facts", "preferences") or ("conversation", "summaries")
    results = await store.asearch(
        namespace=("memory", "facts"),  # Organize memories by type
        query="your search query",
        limit=3  # number of results to return
    )
    return results
```

Each result is a `SearchItem` (extends `Item` with an additional `score` field). When semantic search is configured, `score` contains the similarity score:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
results[0].key       # "07e0caf4-1631-47b7-b15f-65515d4c1843"
results[0].value     # {"text": "User prefers dark mode"}
results[0].namespace # ("memory", "facts")
results[0].score     # 0.92 (similarity score, present when semantic search is configured)
```

### Changing your embedding model

<Warning>
  Changing the embedding model or dimensions requires re-embedding all existing data. There is currently no automated migration tooling for this. Plan accordingly if you need to switch models.
</Warning>

## Custom embeddings

If you want to use custom embeddings, you can pass a path to a custom embedding function:

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
    ...
    "store": {
        "index": {
            "embed": "path/to/embedding_function.py:embed",
            "dims": 1536,
            "fields": ["$"]
        }
    }
}
```

The deployment will look for the function in the specified path. The function must be async and accept a list of strings:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}

# path/to/embedding_function.py
from openai import AsyncOpenAI

client = AsyncOpenAI()

async def aembed_texts(texts: list[str]) -> list[list[float]]:
    """Custom embedding function that must:
    1. Be async
    2. Accept a list of strings
    3. Return a list of float arrays (embeddings)
    """
    response = await client.embeddings.create(
        model="text-embedding-3-small",
        input=texts
    )
    return [e.embedding for e in response.data]
```

## Querying via the API

You can also query the store using the LangGraph SDK. Since the SDK uses async operations:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langgraph_sdk import get_client

async def search_store():
    client = get_client()
    results = await client.store.search_items(
        ("memory", "facts"),
        query="your search query",
        limit=3  # number of results to return
    )
    return results

# Use in an async context
results = await search_store()
```

Each result item includes a `score` field when semantic search is configured:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
results["items"][0]["key"]       # "07e0caf4-1631-47b7-b15f-65515d4c1843"
results["items"][0]["value"]     # {"text": "User prefers dark mode"}
results["items"][0]["namespace"] # ["memory", "facts"]
results["items"][0]["score"]     # 0.92 (similarity score)
```

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/semantic-search.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# A2A endpoint in Agent Server
Source: https://docs.langchain.com/langsmith/server-a2a

Use the A2A protocol to enable agent-to-agent communication with distributed tracing in LangSmith.

[Agent2Agent (A2A)](https://a2a-protocol.org/latest/) is Google's protocol for enabling communication between conversational AI agents. [LangSmith implements A2A support](https://docs.langchain.com/langsmith/server-api-ref#tag/a2a/post/a2a/\{assistant_id}), allowing your agents to communicate with other A2A-compatible agents through a standardized protocol.

The A2A endpoint is available in [Agent Server](/langsmith/agent-server) at `/a2a/{assistant_id}`.

## Supported methods

Agent Server supports the following A2A RPC methods:

* **message/send**: Send a message to an assistant and receive a complete response
* **message/stream**: Send a message and stream responses in real-time using Server-Sent Events (SSE)
* **tasks/get**: Retrieve the status and results of a previously created task

## Agent card discovery

Each assistant automatically exposes an A2A Agent Card that describes its capabilities and provides the information needed for other agents to connect. You can retrieve the agent card for any assistant using:

```
GET /.well-known/agent-card.json?assistant_id={assistant_id}
```

The agent card includes the assistant's name, description, available skills, supported input/output modes, and the A2A endpoint URL for communication.

## Requirements

To use A2A, ensure you have the following dependencies installed:

* `langgraph-api >= 0.4.21`

Install with:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
pip install "langgraph-api>=0.4.21"
```

## Usage overview

To enable A2A:

* Upgrade to use langgraph-api>=0.4.21.
* Deploy your agent with message-based state structure.
* Connect with other A2A-compatible agents using the endpoint.

## Creating an A2A-compatible agent

This example creates an A2A-compatible agent that processes incoming messages using OpenAI's API and maintains conversational state. The agent defines a message-based state structure and handles the A2A protocol's message format.

To be compatible with the [A2A "text" parts](https://a2a-protocol.org/dev/specification/#651-textpart-object), the agent must have a `messages` key in state.

The A2A protocol uses two identifiers to maintain conversational continuity:

* `contextId`: Groups messages into a conversation thread (like a session ID)
* `taskId`: Identifies each individual request within that conversation

On the first message, omit `contextId` and `taskId` - the agent will generate and return them. For all subsequent messages in the conversation, include the `contextId` and `taskId` from the prior response to maintain thread continuity.

**LangSmith Tracing:** The Langsmith Deployment A2A endpoint automatically converts the A2A `contextId` to `thread_id` for LangSmith tracing, grouping all messages in the conversation under a single thread.

For example:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
"""LangGraph A2A conversational agent.

Supports the A2A protocol with messages input for conversational interactions.
"""

from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Any, Dict, List, TypedDict

from langgraph.graph import StateGraph
from langgraph.runtime import Runtime
from openai import AsyncOpenAI

class Context(TypedDict):
    """Context parameters for the agent."""
    my_configurable_param: str

@dataclass
class State:
    """Input state for the agent.

    Defines the initial structure for A2A conversational messages.
    """
    messages: List[Dict[str, Any]]

async def call_model(state: State, runtime: Runtime[Context]) -> Dict[str, Any]:
    """Process conversational messages and returns output using OpenAI."""
    # Initialize OpenAI client
    client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    # Process the incoming messages
    latest_message = state.messages[-1] if state.messages else {}
    user_content = latest_message.get("content", "No message content")

    # Create messages for OpenAI API
    openai_messages = [
        {
            "role": "system",
            "content": "You are a helpful conversational agent. Keep responses brief and engaging."
        },
        {
            "role": "user",
            "content": user_content
        }
    ]

    try:
        # Make OpenAI API call
        response = await client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=openai_messages,
            max_tokens=100,
            temperature=0.7
        )

        ai_response = response.choices[0].message.content

    except Exception as e:
        ai_response = f"I received your message but had trouble processing it. Error: {str(e)[:50]}..."

    # Create a response message
    response_message = {
        "role": "assistant",
        "content": ai_response
    }

    return {
        "messages": state.messages + [response_message]
    }

# Define the graph
graph = (
    StateGraph(State, context_schema=Context)
    .add_node(call_model)
    .add_edge("__start__", "call_model")
    .compile()
)
```

## Agent-to-agent communication

Once your agents are running locally via `langgraph dev` or [deployed to production](/langsmith/deployment), you can facilitate communication between them using the A2A protocol.

This example demonstrates how two agents can communicate by sending JSON-RPC messages to each other's A2A endpoints. The script simulates a multi-turn conversation where each agent processes the other's response and continues the dialogue.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
#!/usr/bin/env python3
"""Agent-to-Agent conversation simulation using the LangGraph A2A endpoint."""

import asyncio
import aiohttp
import os
import uuid

def extract_text(result: dict) -> str:
    """Best-effort extraction of response text from an A2A result."""
    for art in result.get("result", {}).get("artifacts", []) or []:
        for part in art.get("parts", []) or []:
            if part.get("kind") == "text" and part.get("text"):
                return part["text"]

    msg = (result.get("result", {}).get("status", {}) or {}).get("message", {}) or {}
    for part in msg.get("parts", []) or []:
        if part.get("kind") == "text" and part.get("text"):
            return part["text"]

    return "(no text found)"

async def send_message(session, port, assistant_id, text, context_id=None, task_id=None):
    """Send an A2A message. Returns (response_text, returned_context_id, returned_task_id)."""
    url = f"http://127.0.0.1:{port}/a2a/{assistant_id}"

    message = {
        "role": "user",
        "parts": [{"kind": "text", "text": text}],
        "messageId": str(uuid.uuid4()),
    }

    # A2A multi-turn continuity: reuse contextId and taskId across turns/agents
    if context_id:
        message["contextId"] = context_id
    if task_id:
        message["taskId"] = task_id

    payload = {
        "jsonrpc": "2.0",
        "id": str(uuid.uuid4()),
        "method": "message/send",
        "params": {"message": message},
    }

    headers = {"Accept": "application/json"}
    async with session.post(url, json=payload, headers=headers) as response:
        result = await response.json()

    returned_context_id = result.get("result", {}).get("contextId") or context_id
    returned_task_id = result.get("result", {}).get("id")
    return extract_text(result), returned_context_id, returned_task_id

async def simulate_conversation():
    """Simulate a conversation between two agents."""

    #Assistant IDs
    agent_a_id = os.getenv("AGENT_A_ID")
    agent_b_id = os.getenv("AGENT_B_ID")

    if not agent_a_id or not agent_b_id:
        print("Set AGENT_A_ID and AGENT_B_ID environment variables")
        return

    message = "Hello! Let's have a conversation."
    context_id = None
    task_id = None

    async with aiohttp.ClientSession() as session:
        for i in range(3):
            print(f"--- Round {i + 1} ---")

            message, context_id, task_id = await send_message(
                session, 2024, agent_a_id, message,
                context_id=context_id,
                task_id=task_id,
            )
            print(f"🔵 Agent A: {message}")

            message, context_id, task_id = await send_message(
                session, 2025, agent_b_id, message,
                context_id=context_id,
                task_id=task_id,
            )
            print(f"🔴 Agent B: {message}\n")

if __name__ == "__main__":
    asyncio.run(simulate_conversation())
```

For complete working examples, see:

* [Two LangGraph agents communicating](https://github.com/langchain-samples/A2A-langgraph) - Example of two LangGraph agents using the A2A protocol
* [Google ADK agent with LangChain agent](https://github.com/langchain-samples/A2A-google-adk) - Example of a Google ADK agent interacting with a LangChain agent using the A2A protocol

## Distributed tracing

When multiple agents communicate over A2A, LangSmith can group all their [traces](/langsmith/observability-concepts#traces) into a single [thread](/langsmith/observability-concepts#threads), which gives you a unified view of the entire multi-agent conversation.

### How contextId maps to thread\_id

The Agent Server A2A endpoint automatically converts the A2A `contextId` to `thread_id` for LangSmith tracing. This means every message in a conversation, across all participating agents, is grouped under the same thread in LangSmith without any extra configuration on your part.

The flow works as follows:

1. On the first message, the client omits `contextId`. The server generates one and returns it in the response.
2. The client passes the `contextId` in all subsequent messages to maintain conversation continuity.
3. Agent Server maps the `contextId` to `thread_id` in LangSmith [metadata](/langsmith/add-metadata-tags), so all turns appear in the same thread.

### Tracing across multiple agents

When agents from different frameworks communicate over A2A, you can unify their traces in LangSmith by sharing the same `thread_id` across all agents. Use the `contextId` returned by the first agent as the `thread_id` for all subsequent requests.

The following code snippet demonstrates the key concepts. For a complete runnable implementation with two agents, refer to the [Google ADK + LangChain example](https://github.com/langchain-samples/A2A-google-adk/blob/main/test_agent_conversation.py).

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import asyncio
import aiohttp
import uuid

async def send_message(session, url, text, context_id=None, task_id=None, thread_id=None):
    """Send an A2A message and return (response_text, context_id, task_id)."""

    # --- 1. Build the message ---
    # On follow-up turns, include contextId and taskId inside the message object
    # so the server associates them with the ongoing conversation.
    message = {
        "role": "user",
        "parts": [{"kind": "text", "text": text}],
        "messageId": str(uuid.uuid4()),
    }
    if context_id:
        message["contextId"] = context_id
    if task_id:
        message["taskId"] = task_id

    # --- 2. Set thread_id in metadata ---
    # thread_id goes at the top level of the JSON-RPC payload, not inside params.
    payload = {
        "jsonrpc": "2.0",
        "id": str(uuid.uuid4()),
        "method": "message/send",
        "params": {"message": message},
        "metadata": {"thread_id": thread_id},
    }

    async with session.post(url, json=payload, headers={"Accept": "application/json"}) as response:
        if response.status != 200:
            raise RuntimeError(f"HTTP {response.status}: {await response.text()}")
        result = await response.json()

    if "error" in result:
        raise RuntimeError(result["error"].get("message", "Unknown error"))

    result_obj = result.get("result", {})
    returned_context_id = result_obj.get("contextId") or context_id
    returned_task_id = result_obj.get("id")
    text_out = next(
        (
            part.get("text", "")
            for art in result_obj.get("artifacts", []) or []
            for part in art.get("parts", []) or []
            if part.get("kind") == "text"
        ),
        "(no text)",
    )
    return text_out, returned_context_id, returned_task_id

async def run_conversation(agent_a_url, agent_b_url):
    # --- 3. Share thread_id across agents ---
    # Generate a shared thread_id upfront. Once the server returns a contextId,
    # use that instead — this keeps the A2A context and LangSmith thread in sync.
    thread_id = str(uuid.uuid4())
    context_id = None
    task_id = None
    message = "Hello! Let's collaborate."

    async with aiohttp.ClientSession() as session:
        for _ in range(3):
            message, context_id, task_id = await send_message(
                session, agent_a_url, message,
                context_id=context_id, task_id=task_id,
                thread_id=context_id or thread_id,
            )

            # Passing the same thread_id to every agent groups all traces in LangSmith
            message, context_id, task_id = await send_message(
                session, agent_b_url, message,
                context_id=context_id, task_id=task_id,
                thread_id=context_id or thread_id,
            )

asyncio.run(run_conversation(
    "http://localhost:2024/a2a/<agent_a_assistant_id>",
    "http://localhost:2025/a2a/<agent_b_assistant_id>",
))
```

**1. Build the message**: Include `contextId` and `taskId` inside the `message` object on follow-up turns so the server can associate them with the ongoing conversation. Omit them on the first message, because the server generates a `contextId` and returns it in the response.

**2. Set thread\_id in metadata**: Pass `thread_id` in the top-level `metadata` field of the JSON-RPC payload, not inside `params`.

**3. Share thread\_id across agents**: Generate a random `thread_id` before the first message. Once the server returns a `contextId`, use it as the `thread_id` for all subsequent requests, which keeps the A2A conversation context and the LangSmith thread in sync. Pass the same `thread_id` to every agent so all traces are grouped into one thread.

### Receive thread\_id in non-LangGraph agents

The [previous section](#tracing-across-multiple-agents) covers the client side—propagating `thread_id` when sending messages. If one of your agents is not built on LangGraph, it also needs to extract and attach the `thread_id` on the receiving end so its traces land in the same LangSmith thread. Use `langsmith.integrations.otel.configure()` to set up automatic tracing, and extract the `thread_id` from incoming A2A request metadata to group traces in the same thread.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from fastapi import FastAPI, Request
from langsmith.integrations.otel import configure as configure_otel
from opentelemetry import trace
import json

# --- 1. Configure OTel ---

# Set up automatic tracing to LangSmith for your non-LangGraph agent.
configure_otel(project_name="my-a2a-project")
tracer = trace.get_tracer(__name__)

app = FastAPI()

@app.middleware("http")
async def set_thread_id_middleware(request: Request, call_next):
    thread_id = None
    if request.method == "POST":
        body_bytes = await request.body()
        if body_bytes:
            # --- 2. Extract thread_id from incoming A2A metadata ---
            try:
                body = json.loads(body_bytes)
                thread_id = body.get("metadata", {}).get("thread_id")
            except Exception:
                pass
            # Re-inject the body so downstream handlers can still read it
            async def receive():
                return {"type": "http.request", "body": body_bytes}
            request._receive = receive

    # --- 3. Attach thread_id to the trace ---
    # langsmith.metadata.thread_id groups this trace with others in the same thread.
    with tracer.start_as_current_span("agent") as span:
        if thread_id:
            span.set_attribute("langsmith.metadata.thread_id", thread_id)
        return await call_next(request)
```

Register your agent routes on `app` after this middleware.

<Note>
  Set `LANGSMITH_API_KEY` and optionally `LANGSMITH_PROJECT` in your environment to enable tracing. All agents in the conversation should use the same project so their traces are visible together.
</Note>

### View traces in LangSmith

After running a multi-agent conversation, open the [LangSmith UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-server-a2a) and navigate to **Threads**. All turns from all participating agents will appear under a single thread, identified by the shared `thread_id`.

## Disable A2A

To disable the A2A endpoint, set `disable_a2a` to `true` in your `langgraph.json` configuration file:

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "$schema": "https://langgra.ph/schema.json",
  "http": {
    "disable_a2a": true
  }
}
```

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/server-a2a.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Agent Server API reference for LangSmith Deployment
Source: https://docs.langchain.com/langsmith/server-api-ref

The Agent Server API reference is available within each [deployment](/langsmith/deployment) at the `/docs` endpoint (e.g. `http://localhost:8124/docs`).

Browse the full API reference in the **Agent Server API** section in the sidebar, or see the endpoint groups below:

* [Assistants](/langsmith/agent-server-api/assistants) - Configured instances of a graph
* [Threads](/langsmith/agent-server-api/threads) - Accumulated outputs of a group of runs
* [Thread Runs](/langsmith/agent-server-api/thread-runs) - Invocations of a graph/assistant on a thread
* [Stateless Runs](/langsmith/agent-server-api/stateless-runs) - Invocations with no state persistence
* [Crons](/langsmith/agent-server-api/crons) - Periodic runs on a schedule
* [Store](/langsmith/agent-server-api/store) - Persistent key-value store for long-term memory
* [A2A](/langsmith/agent-server-api/a2a) - Agent-to-Agent Protocol endpoints
* [MCP](/langsmith/agent-server-api/mcp) - Model Context Protocol endpoints
* [System](/langsmith/agent-server-api/system) - Health checks and server info

## Authentication

For deployments to LangSmith, authentication is required. Pass the `X-Api-Key` header with each request to the Agent Server. The value of the header should be set to a valid LangSmith API key for the organization where the Agent Server is deployed.

Example `curl` command:

```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
curl --request POST \
  --url http://localhost:8124/assistants/search \
  --header 'Content-Type: application/json' \
  --header 'X-Api-Key: LANGSMITH_API_KEY' \
  --data '{
  "metadata": {},
  "limit": 10,
  "offset": 0
}'
```

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/server-api-ref.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
