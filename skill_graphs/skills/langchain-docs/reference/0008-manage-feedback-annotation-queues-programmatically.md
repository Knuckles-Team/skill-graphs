# Manage feedback & annotation queues programmatically
Source: https://docs.langchain.com/langsmith/annotation-queues-sdk

Use the LangSmith SDK to manage feedback configurations and [annotation queue](/langsmith/evaluation-concepts#human) rubrics programmatically. Define reusable feedback schemas at the organization level (like accuracy scores or pass/fail judgments), then assign them to specific queues with custom instructions. This enables version control, automation across projects, and consistency—particularly useful for CI/CD pipelines or replicating evaluation setups across environments.

<Callout icon="code">
  This guide uses the Python and TypeScript SDKs. For installation and setup, refer to the [Python SDK documentation](https://reference.langchain.com/python/langsmith) and [TypeScript SDK documentation](https://reference.langchain.com/javascript/modules/langsmith.html).
</Callout>

<Note>
  To write free-form acceptance criteria on individual runs while reviewing in the [LangSmith UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-annotation-queues-sdk), refer to [Use assertions](/langsmith/assertions).
</Note>

## Feedback layers

LangSmith uses a three-layer architecture for structured human feedback:

1. **Feedback configs**: Organization-wide definitions of feedback keys that establish the schema for evaluation metrics. For example, you might define "accuracy" as a continuous 0–1 score or "correctness" as a pass/fail categorical choice. These configs are reusable across all annotation queues in your organization.
2. **Annotation queue rubric items**: Queue-specific assignments that determine which feedback configs annotators must fill out when reviewing [runs](/langsmith/observability-concepts#runs) in a particular queue. Each rubric item can include custom descriptions, guidance for specific score values, and whether the feedback is required or optional.
3. **Feedback**: Individual scores and values that annotators submit on specific [runs](/langsmith/observability-concepts#runs). This is the actual evaluation data collected using the schemas you've defined. Learn more about [feedback in LangSmith](/langsmith/observability-concepts#feedback).

## Feedback configs

### Create a feedback config

Feedback configs define the schema for a feedback key—whether it's a continuous score, a categorical choice, or freeform text. A unique key identifies each config within your organization and specifies how annotators can submit feedback for that metric.

<Note>
  Calling [`create_feedback_config`](https://reference.langchain.com/python/langsmith/client/Client/create_feedback_config) with an identical config that already exists returns the existing config. If a different config already exists for the same key, the system raises a 400 error.
</Note>

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langsmith import Client

  client = Client()

  # Continuous score
  client.create_feedback_config(
      "accuracy",
      feedback_config={
          "type": "continuous",
          "min": 0,
          "max": 1,
      },
      is_lower_score_better=False,
  )

  # Categorical
  client.create_feedback_config(
      "correctness",
      feedback_config={
          "type": "categorical",
          "categories": [
              {"value": 1, "label": "Pass"},
              {"value": 0, "label": "Fail"},
          ],
      },
  )

  # Freeform text
  client.create_feedback_config(
      "notes",
      feedback_config={"type": "freeform"},
  )
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { Client } from "langsmith";

  const client = new Client();

  // Continuous score
  await client.createFeedbackConfig({
    feedbackKey: "accuracy",
    feedbackConfig: { type: "continuous", min: 0, max: 1 },
    isLowerScoreBetter: false,
  });

  // Categorical
  await client.createFeedbackConfig({
    feedbackKey: "correctness",
    feedbackConfig: {
      type: "categorical",
      categories: [
        { value: 1, label: "Pass" },
        { value: 0, label: "Fail" },
      ],
    },
  });

  // Freeform text
  await client.createFeedbackConfig({
    feedbackKey: "notes",
    feedbackConfig: { type: "freeform" },
  });
  ```
</CodeGroup>

* **Continuous** (`"accuracy"`): Defines a numeric scale from 0 to 1. The `is_lower_score_better` parameter indicates whether lower values represent better performance. Use continuous configs for rating scales or percentage-based metrics.
* **Categorical** (`"correctness"`): Provides predefined options with associated values. Each category requires a `value` (used for scoring and analytics) and a `label` (shown to annotators). Use categorical configs for binary choices or multi-class classifications.
* **Freeform** (`"notes"`): Allows open-ended text input with no predefined structure. Use freeform configs for qualitative observations or explanations.

### List feedback configs

Retrieve feedback configs to see what evaluation criteria are available in your organization with [`list_feedback_configs`](https://reference.langchain.com/python/langsmith/client/Client/list_feedback_configs). You can list all configs or filter by specific keys. Each returned config object includes the key, type, configuration details (like `min`/`max` or `categories`), and metadata like `is_lower_score_better`:

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  # List all configs
  for config in client.list_feedback_configs():
      print(f"{config.feedback_key}: {config.feedback_config}")

  # Filter by specific keys
  for config in client.list_feedback_configs(
      feedback_key=["accuracy", "correctness"]
  ):
      print(config.feedback_key)
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  // List all configs
  for await (const config of client.listFeedbackConfigs()) {
    console.log(`${config.feedback_key}: ${JSON.stringify(config.feedback_config)}`);
  }

  // Filter by specific keys
  for await (const config of client.listFeedbackConfigs({
    feedbackKeys: ["accuracy", "correctness"],
  })) {
    console.log(config.feedback_key);
  }
  ```
</CodeGroup>

### Update a feedback config

Modify an existing feedback config with [`update_feedback_config`](https://reference.langchain.com/python/langsmith/client/Client/update_feedback_config) by updating specific fields. The method only changes the fields you provide—the rest remain unchanged. This is a partial update that preserves other configuration settings:

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  client.update_feedback_config(
      "accuracy",
      is_lower_score_better=True,
  )
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  await client.updateFeedbackConfig("accuracy", {
    isLowerScoreBetter: true,
  });
  ```
</CodeGroup>

### Delete a feedback config

Remove a feedback config from your organization with [`delete_feedback_config`](https://reference.langchain.com/python/langsmith/client/Client/delete_feedback_config). This performs a soft delete, which marks the config as deleted but doesn't permanently remove it from the system. You can recreate a config with the same key later if needed:

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  client.delete_feedback_config("accuracy")
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  await client.deleteFeedbackConfig("accuracy");
  ```
</CodeGroup>

## Annotation queue rubric items

Rubric items assign feedback configs to a specific annotation queue. They control which feedback forms annotators see when reviewing [runs](/langsmith/observability-concepts#runs) in that queue, and whether each form is required or optional.

### Create a queue with rubric items

Create an annotation queue with [`create_annotation_queue`](https://reference.langchain.com/python/langsmith/client/Client/create_annotation_queue) and assign feedback configs to it through rubric items. Each rubric item references a feedback config by its key and customizes how it appears to annotators in this specific queue.

The example creates a queue with three rubric items. The queue-level `rubric_instructions` provides general guidance shown at the top of the annotation interface:

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  queue = client.create_annotation_queue(
      name="QA Review Queue",
      description="Review LLM outputs for accuracy and correctness",
      rubric_instructions="Score each response. Add notes for anything unusual.",
      rubric_items=[
          {
              "feedback_key": "accuracy",
              "description": "How accurate is the response?",
              "score_descriptions": {
                  "0": "Completely wrong",
                  "1": "Perfectly accurate",
              },
              "is_required": True,
          },
          {
              "feedback_key": "correctness",
              "description": "Did the response pass or fail?",
              "value_descriptions": {
                  "Pass": "Factually correct",
                  "Fail": "Contains errors",
              },
              "is_required": True,
          },
          {
              "feedback_key": "notes",
              "description": "Any additional observations",
              "is_required": False,
          },
      ],
  )
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  const queue = await client.createAnnotationQueue({
    name: "QA Review Queue",
    description: "Review LLM outputs for accuracy and correctness",
    rubricInstructions: "Score each response. Add notes for anything unusual.",
    rubricItems: [
      {
        feedback_key: "accuracy",
        description: "How accurate is the response?",
        score_descriptions: { "0": "Completely wrong", "1": "Perfectly accurate" },
        is_required: true,
      },
      {
        feedback_key: "correctness",
        description: "Did the response pass or fail?",
        value_descriptions: { Pass: "Factually correct", Fail: "Contains errors" },
        is_required: true,
      },
      {
        feedback_key: "notes",
        description: "Any additional observations",
        is_required: false,
      },
    ],
  });
  ```
</CodeGroup>

* `feedback_key`: The key of an existing feedback config (create this first).
* `description`: Queue-specific guidance for annotators about this metric.
* `score_descriptions` / `value_descriptions`: Optional labels that explain what specific values mean (use `score_descriptions` for continuous configs, `value_descriptions` for categorical).
* `is_required`: Whether annotators must complete this feedback before submitting.

### Update rubric items on an existing queue

Modify the rubric items assigned to an annotation queue with [`update_annotation_queue`](https://reference.langchain.com/python/langsmith/client/Client/update_annotation_queue). This operation replaces the entire rubric items list, so you must include all items you want to keep—the operation removes any items you don't include.

You'll need the queue ID, which you get when you create the queue or by listing queues:

<Note>
  Updating rubric items replaces the full list. Include all items you want to keep.
</Note>

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  client.update_annotation_queue(
      queue.id,
      rubric_items=[
          {"feedback_key": "accuracy", "is_required": True},
          {"feedback_key": "correctness", "is_required": True},
          {
              "feedback_key": "tone",
              "description": "Is the tone appropriate?",
              "is_required": False,
          },
      ],
  )
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  await client.updateAnnotationQueue(queue.id, {
    rubricItems: [
      { feedback_key: "accuracy", is_required: true },
      { feedback_key: "correctness", is_required: true },
      { feedback_key: "tone", description: "Is the tone appropriate?", is_required: false },
    ],
  });
  ```
</CodeGroup>

## Feedback config types (detailed)

### Continuous

Continuous configs define numeric rating scales with minimum and maximum values. Annotators can select any value within the range, making this ideal for scoring dimensions like accuracy, quality, or relevance on a numeric scale:

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  # Simple continuous score
  client.create_feedback_config(
      "accuracy",
      feedback_config={
          "type": "continuous",
          "min": 0,
          "max": 1,
      },
  )

  # Continuous with labeled points on the scale
  client.create_feedback_config(
      "quality",
      feedback_config={
          "type": "continuous",
          "min": 1,
          "max": 5,
          "categories": [
              {"value": 1, "label": "Poor"},
              {"value": 3, "label": "Average"},
              {"value": 5, "label": "Excellent"},
          ],
      },
  )
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  await client.createFeedbackConfig({
    feedbackKey: "accuracy",
    feedbackConfig: { type: "continuous", min: 0, max: 1 },
  });

  await client.createFeedbackConfig({
    feedbackKey: "quality",
    feedbackConfig: {
      type: "continuous",
      min: 1,
      max: 5,
      categories: [
        { value: 1, label: "Poor" },
        { value: 3, label: "Average" },
        { value: 5, label: "Excellent" },
      ],
    },
  });
  ```
</CodeGroup>

The first example shows a 0–1 scale without labels. The second example demonstrates adding `categories` with labeled anchor points on the scale (like "Poor", "Average", "Excellent") to help annotators understand what different values represent. These labels are optional but can improve consistency in how annotators interpret the scale.

### Categorical

Categorical configs provide a discrete set of predefined options for annotators to choose from. Each category must have a `value` (a numeric identifier used for scoring and analytics) and a `label` (the text shown to annotators). You must define at least 2 categories.

Use categorical configs for binary decisions (pass/fail, correct/incorrect), multi-class classifications (sentiment, topic categories), or any evaluation with a fixed set of discrete options. Do not set `min` or `max` for categorical configs:

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  # Binary pass/fail
  client.create_feedback_config(
      "correctness",
      feedback_config={
          "type": "categorical",
          "categories": [
              {"value": 1, "label": "Pass"},
              {"value": 0, "label": "Fail"},
          ],
      },
  )

  # Multi-class
  client.create_feedback_config(
      "sentiment",
      feedback_config={
          "type": "categorical",
          "categories": [
              {"value": 0, "label": "Negative"},
              {"value": 1, "label": "Neutral"},
              {"value": 2, "label": "Positive"},
          ],
      },
  )
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  await client.createFeedbackConfig({
    feedbackKey: "correctness",
    feedbackConfig: {
      type: "categorical",
      categories: [
        { value: 1, label: "Pass" },
        { value: 0, label: "Fail" },
      ],
    },
  });

  await client.createFeedbackConfig({
    feedbackKey: "sentiment",
    feedbackConfig: {
      type: "categorical",
      categories: [
        { value: 0, label: "Negative" },
        { value: 1, label: "Neutral" },
        { value: 2, label: "Positive" },
      ],
    },
  });
  ```
</CodeGroup>

The first example shows a binary pass/fail config. The second example demonstrates a multi-class config for sentiment with three options. The numeric values allow you to compute aggregate scores even for categorical feedback.

### Freeform

Freeform configs allow annotators to provide open-ended text feedback without any predefined structure or constraints. This type has no `min`, `max`, or `categories` fields—annotators can enter any text they want.

Freeform feedback is valuable for capturing nuanced insights but is harder to aggregate and analyze compared to structured feedback types:

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  client.create_feedback_config(
      "notes",
      feedback_config={"type": "freeform"},
  )
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  await client.createFeedbackConfig({
    feedbackKey: "notes",
    feedbackConfig: { type: "freeform" },
  });
  ```
</CodeGroup>

## Validation rules

| Type          | min/max         | categories                      | Constraints                                         |
| ------------- | --------------- | ------------------------------- | --------------------------------------------------- |
| `continuous`  | Optional        | Optional (labeled scale points) | `min < max`; category values within \[`min`, `max`] |
| `categorical` | Must not be set | Required, min 2                 | Unique values and labels                            |
| `freeform`    | Must not be set | Must not be set                 | N/A                                                 |

## Reference

### Feedback config types

| Type          | Fields                                | Description                       |
| ------------- | ------------------------------------- | --------------------------------- |
| `continuous`  | `min`, `max`                          | Numeric score within a range      |
| `categorical` | categories (list of `{value, label}`) | Selection from predefined options |
| `freeform`    | None                                  | Free-text input                   |

### Rubric item fields

| Field                | Type                     | Description                                                                      |
| -------------------- | ------------------------ | -------------------------------------------------------------------------------- |
| `feedback_key`       | `string`                 | Required. Must match an existing feedback config key.                            |
| `description`        | `string`                 | Shows annotators guidance for this item.                                         |
| `score_descriptions` | `Record<string, string>` | Labels for specific score values (continuous).                                   |
| `value_descriptions` | `Record<string, string>` | Labels for specific category values (categorical).                               |
| `is_required`        | `boolean`                | Whether annotators must complete this item before submitting. Defaults to false. |

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/annotation-queues-sdk.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Control plane API reference for LangSmith Deployment
Source: https://docs.langchain.com/langsmith/api-ref-control-plane

The control plane API is part of [LangSmith Deployment](/langsmith/deployment). With the control plane API, you can programmatically create, manage, and automate your [Agent Server](/langsmith/agent-server) deployments—for example, as part of a custom CI/CD workflow.

Browse the full API reference in the **Control Plane API** section in the sidebar, or refer to the endpoint groups:

* [Integrations (v1)](/api-reference/integrations-v1/list-github-integrations): GitHub integrations and repository listings
* [Deployments (v2)](/api-reference/deployments-v2): Create, manage, and update Agent Server deployments
* [Listeners (v2)](/api-reference/listeners-v2): Listener resources for self-hosted enterprise organizations
* [Auth Service (v2)](/api-reference/auth-service-v2): OAuth provider configuration and authentication flows

## Host

The control plane hosts for Cloud data regions:

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

**Note**: Self-hosted deployments of LangSmith will have a custom host for the control plane. The control plane APIs can be accessed at the path `/api-host`. For example, `http(s)://<host>/api-host/v2/deployments`. See [the self-host usage guide](/langsmith/self-host-usage#configuring-the-application-you-want-to-use-with-langsmith) for more details.

## Authentication

To authenticate with the control plane API, set the `X-Api-Key` header to a valid LangSmith API key and set the `X-Tenant-Id` header to a valid workspace ID to target.

Example `curl` command:

```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
curl --request GET \
  --url http://localhost:8124/v2/deployments \
  --header 'X-Api-Key: LANGSMITH_API_KEY'
  --header 'X-Tenant-Id': WORKSPACE_ID'
```

## Versioning

Each endpoint path is prefixed with a version (e.g. `v1`, `v2`).

## Quick start

1. Call `POST /v2/deployments` to create a new Deployment. The response body contains the Deployment ID (`id`) and the ID of the latest (and first) revision (`latest_revision_id`).
2. Call `GET /v2/deployments/{deployment_id}` to retrieve the Deployment. Set `deployment_id` in the URL to the value of Deployment ID (`id`).
3. Poll for revision `status` until `status` is `DEPLOYED` by calling `GET /v2/deployments/{deployment_id}/revisions/{latest_revision_id}`.
4. Call `PATCH /v2/deployments/{deployment_id}` to update the deployment.

## Example Code

Below is example Python code that demonstrates how to orchestrate the control plane APIs to create a deployment, update the deployment, and delete the deployment.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import os
import time

import requests
from dotenv import load_dotenv

load_dotenv()

# required environment variables
CONTROL_PLANE_HOST = os.getenv("CONTROL_PLANE_HOST")
LANGSMITH_API_KEY = os.getenv("LANGSMITH_API_KEY")
WORKSPACE_ID = os.getenv("WORKSPACE_ID")
INTEGRATION_ID = os.getenv("INTEGRATION_ID")
MAX_WAIT_TIME = 1800  # 30 mins

def get_headers() -> dict:
    """Return common headers for requests to the control plane API."""
    return {
        "X-Api-Key": LANGSMITH_API_KEY,
        "X-Tenant-Id": WORKSPACE_ID,
    }

def create_deployment() -> str:
    """Create deployment. Return deployment ID."""
    headers = get_headers()
    headers["Content-Type"] = "application/json"

    deployment_name = "my_deployment"

    request_body = {
        "name": deployment_name,
        "source": "github",
        "source_config": {
            "integration_id": INTEGRATION_ID,
            "repo_url": "https://github.com/langchain-ai/langgraph-example",
            "deployment_type": "dev",
            "build_on_push": False,
            "custom_url": None,
            "resource_spec": None,
        },
        "source_revision_config": {
            "repo_ref": "main",
            "langgraph_config_path": "langgraph.json",
            "image_uri": None,
        },
        "secrets": [
            {
                "name": "OPENAI_API_KEY",
                "value": "test_openai_api_key",
            },
            {
                "name": "ANTHROPIC_API_KEY",
                "value": "test_anthropic_api_key",
            },
            {
                "name": "TAVILY_API_KEY",
                "value": "test_tavily_api_key",
            },
        ],
    }

    response = requests.post(
        url=f"{CONTROL_PLANE_HOST}/v2/deployments",
        headers=headers,
        json=request_body,
    )

    if response.status_code != 201:
        raise Exception(f"Failed to create deployment: {response.text}")

    deployment_id = response.json()["id"]
    print(f"Created deployment {deployment_name} ({deployment_id})")
    return deployment_id

def get_deployment(deployment_id: str) -> dict:
    """Get deployment."""
    response = requests.get(
        url=f"{CONTROL_PLANE_HOST}/v2/deployments/{deployment_id}",
        headers=get_headers(),
    )

    if response.status_code != 200:
        raise Exception(f"Failed to get deployment ID {deployment_id}: {response.text}")

    return response.json()

def list_revisions(deployment_id: str) -> list[dict]:
    """List revisions.

    Return list is sorted by created_at in descending order (latest first).
    """
    response = requests.get(
        url=f"{CONTROL_PLANE_HOST}/v2/deployments/{deployment_id}/revisions",
        headers=get_headers(),
    )

    if response.status_code != 200:
        raise Exception(
            f"Failed to list revisions for deployment ID {deployment_id}: {response.text}"
        )

    return response.json()

def get_revision(
    deployment_id: str,
    revision_id: str,
) -> dict:
    """Get revision."""
    response = requests.get(
        url=f"{CONTROL_PLANE_HOST}/v2/deployments/{deployment_id}/revisions/{revision_id}",
        headers=get_headers(),
    )

    if response.status_code != 200:
        raise Exception(f"Failed to get revision ID {revision_id}: {response.text}")

    return response.json()

def patch_deployment(deployment_id: str) -> None:
    """Patch deployment."""
    headers = get_headers()
    headers["Content-Type"] = "application/json"

    # This creates a new revision because source_revision_config is included
    response = requests.patch(
        url=f"{CONTROL_PLANE_HOST}/v2/deployments/{deployment_id}",
        headers=headers,
        json={
            "source_config": {
                "build_on_push": True,
            },
            "source_revision_config": {
                "repo_ref": "main",
                "langgraph_config_path": "langgraph.json",
            },
        },
    )

    if response.status_code != 200:
        raise Exception(f"Failed to patch deployment: {response.text}")

    print(f"Patched deployment ID {deployment_id}")

def wait_for_deployment(deployment_id: str, revision_id: str) -> None:
    """Wait for revision status to be DEPLOYED."""
    start_time = time.time()
    revision, status = None, None
    while time.time() - start_time < MAX_WAIT_TIME:
        revision = get_revision(deployment_id, revision_id)
        status = revision["status"]
        if status == "DEPLOYED":
            break
        elif "FAILED" in status:
            raise Exception(f"Revision ID {revision_id} failed: {revision}")

        print(f"Waiting for revision ID {revision_id} to be DEPLOYED...")
        time.sleep(60)

    if status != "DEPLOYED":
        raise Exception(
            f"Timeout waiting for revision ID {revision_id} to be DEPLOYED: {revision}"
        )

def delete_deployment(deployment_id: str) -> None:
    """Delete deployment."""
    response = requests.delete(
        url=f"{CONTROL_PLANE_HOST}/v2/deployments/{deployment_id}",
        headers=get_headers(),
    )

    if response.status_code != 204:
        raise Exception(
            f"Failed to delete deployment ID {deployment_id}: {response.text}"
        )

    print(f"Deployment ID {deployment_id} deleted")

if __name__ == "__main__":
    # create deployment and get the latest revision
    deployment_id = create_deployment()
    revisions = list_revisions(deployment_id)
    latest_revision = revisions["resources"][0]
    latest_revision_id = latest_revision["id"]

    # wait for latest revision to be DEPLOYED
    wait_for_deployment(deployment_id, latest_revision_id)

    # patch the deployment and get the latest revision
    patch_deployment(deployment_id)
    revisions = list_revisions(deployment_id)
    latest_revision = revisions["resources"][0]
    latest_revision_id = latest_revision["id"]

    # wait for latest revision to be DEPLOYED
    wait_for_deployment(deployment_id, latest_revision_id)

    # delete the deployment
    delete_deployment(deployment_id)
```

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/api-ref-control-plane.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Application structure
Source: https://docs.langchain.com/langsmith/application-structure

To deploy on LangSmith, an application must consist of one or more graphs, a configuration file (`langgraph.json`), a file that specifies dependencies, and an optional `.env` file that specifies environment variables.

This page explains how a LangSmith application is organized and how to provide the configuration details required for deployment.

## Key concepts

To deploy using LangSmith, provide the following information:

1. A [configuration file](#configuration-file-concepts) (`langgraph.json`) that specifies the dependencies, graphs, and environment variables to use for the application.
2. The [graphs](#graphs) that implement the logic of the application.
3. A file that specifies [dependencies](#dependencies) required to run the application.
4. [Environment variables](#environment-variables) that are required for the application to run.

<Tip>
  **Framework agnostic**

  LangSmith Deployment supports deploying a [LangGraph](/oss/python/langgraph/overview) *graph*. However, the implementation of a *node* of a graph can contain arbitrary code. This means any framework can be implemented within a node and deployed on LangSmith Deployment. This lets you implement your core application logic without using additional LangGraph OSS APIs while still using LangSmith for [deployment](/langsmith/deployment), scaling, and [observability](/langsmith/observability). For more details, refer to [Use any framework with LangSmith Deployment](/langsmith/application-structure#use-any-framework-with-langsmith-deployment).
</Tip>

## File structure

The following are examples of directory structures for Python and JavaScript applications:

<Tabs>
  <Tab title="Python (requirements.txt)">
    ```plaintext theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    my-app/
    ├── my_agent # all project code lies within here
    │   ├── utils # utilities for your graph
    │   │   ├── __init__.py
    │   │   ├── tools.py # tools for your graph
    │   │   ├── nodes.py # node functions for your graph
    │   │   └── state.py # state definition of your graph
    │   ├── __init__.py
    │   └── agent.py # code for constructing your graph
    ├── .env # environment variables
    ├── requirements.txt # package dependencies
    └── langgraph.json # configuration file for LangGraph
    ```
  </Tab>

  <Tab title="Python (pyproject.toml)">
    ```plaintext theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    my-app/
    ├── my_agent # all project code lies within here
    │   ├── utils # utilities for your graph
    │   │   ├── __init__.py
    │   │   ├── tools.py # tools for your graph
    │   │   ├── nodes.py # node functions for your graph
    │   │   └── state.py # state definition of your graph
    │   ├── __init__.py
    │   └── agent.py # code for constructing your graph
    ├── .env # environment variables
    ├── langgraph.json  # configuration file for LangGraph
    └── pyproject.toml # dependencies for your project
    ```
  </Tab>

  <Tab title="JS (package.json)">
    ```plaintext theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    my-app/
    ├── src # all project code lies within here
    │   ├── utils # optional utilities for your graph
    │   │   ├── tools.ts # tools for your graph
    │   │   ├── nodes.ts # node functions for your graph
    │   │   └── state.ts # state definition of your graph
    │   └── agent.ts # code for constructing your graph
    ├── package.json # package dependencies
    ├── .env # environment variables
    └── langgraph.json # configuration file for LangGraph
    ```
  </Tab>
</Tabs>

<Note>
  The directory structure of an application can vary depending on the programming language and the package manager used.
</Note>

<a />

## Configuration file

The `langgraph.json` file is a JSON file that specifies the dependencies, graphs, environment variables, and other settings required to deploy an application.

For details on all supported keys in the JSON file, refer to the [LangGraph configuration file reference](/langsmith/cli#configuration-file).

<Tip>
  The [LangGraph CLI](/langsmith/cli) defaults to using the configuration file `langgraph.json` in the current directory.
</Tip>

### Examples

<Tabs>
  <Tab title="Python">
    * The dependencies involve a custom local package and the `langchain_openai` package.
    * A single graph will be loaded from the file `./your_package/your_file.py` with the variable `agent`.
    * The environment variables are loaded from the `.env` file.

    ```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    {
        "dependencies": [
            "langchain_openai",
            "./your_package"
        ],
        "graphs": {
            "my_agent": "./your_package/your_file.py:agent"
        },
        "env": "./.env"
    }
    ```
  </Tab>

  <Tab title="JavaScript">
    * The dependencies will be loaded from a dependency file in the local directory (e.g., `package.json`).
    * A single graph will be loaded from the file `./your_package/your_file.js` with the function `agent`.
    * The environment variable `OPENAI_API_KEY` is set inline.

    ```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    {
        "dependencies": [
            "."
        ],
        "graphs": {
            "my_agent": "./your_package/your_file.js:agent"
        },
        "env": {
            "OPENAI_API_KEY": "secret-key"
        }
    }
    ```
  </Tab>
</Tabs>

## Dependencies

An application may depend on other Python packages or JavaScript libraries (depending on the programming language in which the application is written).

You will generally need to specify the following information for dependencies to be set up correctly:

1. A file in the directory that specifies the dependencies (e.g., `requirements.txt`, `pyproject.toml`, or `package.json`).
2. A `dependencies` key in the [configuration file](#configuration-file-concepts) that specifies the dependencies required to run the application.
3. Any additional binaries or system libraries can be specified using `dockerfile_lines` key in the [LangGraph configuration file](#configuration-file-concepts).

## Graphs

Use the `graphs` key in the [configuration file](#configuration-file-concepts) to specify which graphs will be available in the deployed application.

You can specify one or more graphs in the configuration file. Each graph is identified by a unique name and a path to either (1) a compiled graph or (2) a function that defines a graph.

### Use any framework with LangSmith Deployment

While LangSmith Deployment requires applications to be structured as a LangGraph graph, individual nodes within that graph can contain arbitrary code. This means you can use any framework or library within your nodes while still benefiting from LangSmith's deployment infrastructure.

The graph structure serves as a deployment interface, but your core application logic can use whichever tools and frameworks best suit your needs.

To deploy with LangSmith, you need:

<Tabs>
  <Tab title="Python">
    1. **A LangGraph graph structure**: Define a graph using [`StateGraph`](https://reference.langchain.com/python/langgraph/graph/state/StateGraph) with [`add_node`](https://reference.langchain.com/python/langgraph/graph/state/StateGraph/add_node) and [`add_edge`](https://reference.langchain.com/python/langgraph/pregel/_draw/add_edge).
    2. **Node functions with arbitrary logic**: Your node functions can call any framework or library.
    3. **A compiled graph**: [Compile](https://reference.langchain.com/python/langgraph/graph/state/StateGraph/compile) the graph to create a deployable application.

    The following example shows how to wrap your existing application logic within a minimal LangGraph structure:

    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    from langgraph.graph import StateGraph, START, END
    from typing import TypedDict

    # Your existing application logic using any framework
    from app_logic import process_data
    from app_logic import fetch_data

    class State(TypedDict):
        input: str
        result: str

    def my_app_node(state: State) -> State:
        """Node containing arbitrary framework code."""
        # Use any framework or library here
        raw_data = fetch_data(state["input"])
        processed = process_data(raw_data)
        return {"result": processed}

    # Define the graph structure
    graph = StateGraph(State)
    graph.add_node("process", my_app_node)  # Add node with your logic
    graph.add_edge(START, "process")  # Connect start to your node
    graph.add_edge("process", END)  # Connect your node to end

    # Compile for deployment
    app = graph.compile()
    ```
  </Tab>

  <Tab title="JavaScript">
    1. **A LangGraph graph structure**: Define a graph using [`StateGraph`](https://reference.langchain.com/javascript/classes/_langchain_langgraph.index.StateGraph.html) with [`addNode`](https://reference.langchain.com/javascript/classes/_langchain_langgraph.index.StateGraph.html#addnode) and [`addEdge`](https://reference.langchain.com/javascript/classes/_langchain_langgraph.index.StateGraph.html#addedge).
    2. **Node functions with arbitrary logic**: Your node functions can call any framework or library.
    3. **A compiled graph**: [Compile](https://reference.langchain.com/javascript/classes/_langchain_langgraph.index.StateGraph.html#compile) the graph to create a deployable application.

    The following example shows how to wrap your existing application logic within a minimal LangGraph structure:

    ```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    import { StateGraph, START, END } from "@langchain/langgraph";
    import { Annotation } from "@langchain/langgraph";

    // Your existing application logic using any framework
    import { processData } from "./app-logic";
    import { fetchData } from "./app-logic";

    const State = Annotation.Root({
      input: Annotation<string>,
      result: Annotation<string>
    });

    async function myAppNode(state: typeof State.State) {
      // Use any framework or library here
      const rawData = await fetchData(state.input);
      const processed = await processData(rawData);
      return { result: processed };
    }

    // Define the graph structure
    const graph = new StateGraph(State)
      .addNode("process", myAppNode)  // Add node with your logic
      .addEdge(START, "process")  // Connect start to your node
      .addEdge("process", END);  // Connect your node to end

    // Compile for deployment
    export const app = graph.compile();
    ```
  </Tab>
</Tabs>

In this example, the node functions (`my_app_node` for Python and `myAppNode` for JavaScript) can contain calls to any framework or library. The LangGraph structure simply provides the deployment interface and orchestration layer.

## Environment variables

If you're working with a deployed LangGraph application [locally](/langsmith/local-dev-testing), you can configure environment variables in the `env` key of the [configuration file](#configuration-file-concepts).

For a production deployment, you will typically want to configure the environment variables in the deployment environment.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/application-structure.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Use assertions
Source: https://docs.langchain.com/langsmith/assertions

Capture free-form acceptance criteria as dataset examples by writing assertions while reviewing runs in an annotation queue.

Assertions turn a reviewer's English-language standards into an automated check. They are short, free-form claims about what a correct answer should or shouldn't include. You write them while reviewing a run in a [single-run annotation queue](/langsmith/annotation-queues#single-run-annotation-queues), and LangSmith saves each one on a [dataset example](/langsmith/example-data-format). Any [offline evaluator](/langsmith/evaluation-concepts#offline-evaluations) can then check whether new outputs from your application satisfy each claim.

Use assertions when:

* The run's actual output is wrong, and you'd rather describe what a correct answer looks like than write one by hand.
* You want to capture acceptance criteria in plain English without leaving the review flow.

<Note>
  Assertions are available on [single-run annotation queues](/langsmith/annotation-queues#single-run-annotation-queues). [Pairwise queues](/langsmith/annotation-queues#pairwise-annotation-queues) are unchanged. Assertions are available in the LangSmith UI only.
</Note>

<Tip>
  [LangSmith Engine](/langsmith/engine#add-offline-examples) can auto-propose assertions for production traces flagged as recurring issues. Open an issue's offline examples flow to review, edit, or extend the Engine's proposed assertions before saving them to a dataset.
</Tip>

## Add assertions

1. In the [LangSmith UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-assertions), navigate to **Annotation Queues** in the left sidebar. Open a single-run queue and select a run.

2. In the side panel, find the **Assertions** section below **Feedback**.

3. Click **+ Add** to create an assertion row.

4. Enter a **key** that summarizes the claim (for example, `must_cite_source`, `must_not_invent_url`) and a one-sentence **comment** describing the claim.

   The key is free-form. The `must_` / `must_not_` prefixes are just a naming convention; LangSmith doesn't treat them specially.

5. Repeat Steps 3 and 4 for each criterion you want to capture.

   The run editor shows the run's inputs and outputs alongside the assertions side panel. As soon as you add at least one assertion, the run editor's **Outputs** panel switches from the run's actual output to a read-only preview of the assertions you've added. This preview is what gets saved to the dataset. The run's actual output is not saved, because assertions describe what a correct answer should include, not what this run produced.

   <img alt="Annotation queue run editor with assertions added in the side panel and the Outputs panel showing a read-only preview of those assertions." />

   <img alt="Annotation queue run editor with assertions added in the side panel and the Outputs panel showing a read-only preview of those assertions." />

   You can keep editing the run's **Inputs** at any time, for example to refine the prompt before saving the example. The **Outputs** panel stays locked to the assertion preview while any assertions remain.

6. Click **Add to Dataset & Next** in the side panel footer (keyboard shortcut: <kbd>⌘ Enter</kbd> on macOS or <kbd>Ctrl Enter</kbd> elsewhere). LangSmith adds the current run to the queue's [default dataset](/langsmith/annotation-queues#basic-details), or prompts you to pick one if no default is configured. The queue then moves you to the next run.

The saved example's `outputs` field is stored as JSON. For example:

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "assertions": [
    {
      "key": "must_cite_source",
      "comment": "The response cites the source URL it is drawing from."
    },
    {
      "key": "must_not_invent_url",
      "comment": "The response does not include URLs that do not appear in the inputs."
    }
  ]
}
```

The example's `inputs` field stores the run's inputs, or your edited version if you changed them. See [Example data format](/langsmith/example-data-format) for the full shape of a saved example.

## Evaluate against assertions

Write an [offline evaluator](/langsmith/evaluation-concepts#offline-evaluations) that reads the saved assertions from `reference_outputs["assertions"]` and returns one feedback score per assertion. The minimal shape:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
def grade_against_assertions(outputs: dict, reference_outputs: dict) -> list[dict]:
    """Return one feedback score per assertion."""
    feedback = []
    for assertion in reference_outputs["assertions"]:
        # Replace with your scoring logic: LLM judge, regex, schema check, and so on.
        score = ...
        feedback.append({"key": assertion["key"], "score": score})
    return feedback
```

How you score each claim is up to you. Three patterns are common and can be combined in a single evaluator:

* **[LLM-as-a-judge](/langsmith/llm-as-judge)**: For each assertion, prompt a model with the application's output and the assertion's `comment`, and have it return a score. Best when claims are subjective or hard to verify mechanically.
* **[Code-based checks](/langsmith/code-evaluator-ui)**: For each assertion, run a deterministic check keyed off the assertion's `key`, such as a regex match, schema validation, or substring presence. Best when the claim has a crisp, mechanical answer.
* **[Partial-credit scoring](/langsmith/multiple-scores)**: Return a numeric score (for example, between 0.0 and 1.0) instead of a boolean to grade on a scale and give "partial credit" to outputs that fulfill some, but not all, claims.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/assertions.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
