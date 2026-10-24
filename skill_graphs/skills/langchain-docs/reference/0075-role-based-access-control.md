# Role-based access control
Source: https://docs.langchain.com/langsmith/rbac

This reference explains LangSmith's Role-Based Access Control (RBAC) system for managing organization-level and workspace-level permissions.

<Note>
  RBAC (Role-Based Access Control) is an Enterprise feature for managing workspace-level permissions. If you are interested in this feature, [contact our sales team](https://www.langchain.com/contact-sales). Other plans default to using the Admin role for all users.
</Note>

LangSmith's RBAC system manages user permissions within workspaces. RBAC allows you to control who can access your LangSmith [workspace](/langsmith/administration-overview#workspaces) and what they can do within it.

In LangSmith, each user has:

* One [**organization role**](#organization-roles) that applies across the entire organization (separate from workspace RBAC).
  * The Organization User and Organization Viewer roles are only available in organizations on [Plus and Enterprise plans](https://langchain.com/pricing). In Developer organizations (single workspace), all users are assigned the Organization Admin role by default.
* One [**workspace role**](#workspace-roles) per workspace they're a member of (requires Enterprise RBAC feature).

On Enterprise plans, organizations can create [custom workspace roles](#custom-roles) with granular permission combinations.

To learn how to set up RBAC and assign roles to users, refer to the [User Management guide](/langsmith/user-management#set-up-access-control). Your identity provider can also assign roles automatically via [SCIM groups](/langsmith/user-management#set-up-scim-for-your-organization) or [SSO Groups Sync](/langsmith/user-management#sso-groups-sync-alternative).

<Note>
  For a comprehensive list of required permissions along with the operations and roles that can perform them, refer to the [Organization and workspace reference](/langsmith/organization-workspace-operations).
</Note>

## Role types

### Organization roles

Organization roles are **distinct from the workspace RBAC feature** and are used to manage organization-wide capabilities. The roles are system-defined and cannot be modified or extended. The [Organization User](#organization-user) and [Organization Viewer](#organization-viewer) roles are only available in organizations on [Plus and Enterprise plans](https://langchain.com/pricing). In Developer organizations (single workspace), all users are assigned the [Organization Admin](#organization-admin) role by default.

| Role                                            | Description                                                                                           |
| ----------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| [Organization Admin](#organization-admin)       | Full permissions to manage organization configuration, users, billing, and workspaces                 |
| [Organization Operator](#organization-operator) | Management access to workspaces and users for day-to-day operations, excluding admin-level privileges |
| [Organization User](#organization-user)         | Read access to organization information and ability to create personal access tokens                  |
| [Organization Viewer](#organization-viewer)     | Read-only access to organization information                                                          |

#### Organization admin

**Description**: Full permissions to manage all organization configuration, users, billing, and workspaces.

**Permissions**:

* `organization:manage` - Full control over organization settings, SSO, security, billing
* `organization:read` - Read access to all organization information
* `organization:pats:create` - Create organization-level [personal access tokens](/langsmith/administration-overview#personal-access-tokens-pats)

For a comprehensive list of required permissions along with the operations and roles that can perform them, refer to the [Organization and workspace reference](/langsmith/organization-workspace-operations).

**Key Capabilities**:

* Manage [organization settings](/langsmith/set-up-hierarchy#set-up-an-organization) and branding
* Configure [SSO and authentication methods](/langsmith/user-management#set-up-saml-sso-for-your-organization)
* Manage [billing](/langsmith/billing) and subscription plans
* Create and delete [workspaces](/langsmith/set-up-hierarchy)
* Invite and remove organization members
* Assign organization and workspace roles to members
* Create and manage [custom roles](#custom-roles)
* Configure RBAC and ABAC (Attribute-Based Access Control) policies
* View organization [usage](/langsmith/usage-and-billing#usage-limits) and analytics
* View [audit logs](/langsmith/audit-logs) (Enterprise)

For details on setting up and managing your organization, refer to the [Administration Overview](/langsmith/administration-overview#organizations).

#### Organization Operator

Management access for day-to-day operations including workspace and user management, but cannot manage Organization Admins or create organization-wide service keys.

**Permissions:**

* `organization:manage` - Control over organization settings, workspaces, and non-admin users
* `organization:read` - Read access to all organization information
* `organization:pats:create` - Create personal access tokens

For a comprehensive list of required permissions along with the operations and roles that can perform them, refer to the [Organization and workspace reference](/langsmith/organization-workspace-operations).

**Key Capabilities:**

* Create and manage [workspaces](/langsmith/set-up-hierarchy#set-up-a-workspace)
* Invite organization members (Organization User and Viewer roles only)
* Manage non-admin organization members (modify and remove Organization Users and Viewers)
* Assign workspace roles to members
* Create workspace-scoped service keys and service accounts
* View organization [usage](/langsmith/usage-and-billing#usage-limits) and analytics
* View [audit logs](/langsmith/audit-logs) (Enterprise)

**Restrictions:**

* Cannot invite, modify, or remove Organization Admins
* Cannot assign the Organization Admin role to users
* Cannot create organization-wide (non-workspace-specific) service keys
* Not automatically added to existing workspaces (only added to workspaces they create or are explicitly invited to)
* Cannot manage organization [billing](/langsmith/billing) or subscription plans
* Cannot configure [SSO or authentication methods](/langsmith/user-management#set-up-saml-sso-for-your-organization)
* Cannot create or manage [custom roles](#custom-roles)

#### Organization User

**Description**: Read access to organization information and ability to create personal access tokens.

**Permissions**:

* `organization:read` - Read access to organization information
* `organization:pats:create` - Create personal access tokens

For a comprehensive list of required permissions along with the operations and roles that can perform them, refer to the [Organization and workspace reference](/langsmith/organization-workspace-operations).

**Key Capabilities**:

* View organization members and workspaces
* View organization settings (but not modify)
* Create [personal access tokens](/langsmith/administration-overview#personal-access-tokens-pats) for API access
* Join workspaces they're invited to

**Restrictions**:

* Cannot modify organization settings
* Cannot manage billing or subscriptions
* Cannot create or delete workspaces
* Cannot invite or remove organization members
* Cannot manage roles or permissions

You can add an Organization User to a subset of workspaces and assigned workspace roles (if RBAC is enabled), which specify permissions at the workspace level.

#### Organization viewer

**Description**: Read-only access to organization information.

**Permissions**:

* `organization:read` - Read access to organization information

For a comprehensive list of required permissions along with the operations and roles that can perform them, refer to the [Organization and workspace reference](/langsmith/organization-workspace-operations).

**Key Capabilities**:

* View organization members and workspaces
* View organization settings

**Restrictions**:

* Cannot modify anything at the organization level
* Cannot create personal access tokens
* Cannot manage billing, workspaces, or members

### Workspace roles

Workspace roles are part of the **Enterprise RBAC feature** and control what users can do with resources inside a workspace:

| Role                                  | Description                                                                                       |
| ------------------------------------- | ------------------------------------------------------------------------------------------------- |
| [Workspace Admin](#workspace-admin)   | Full permissions for all resources, including workspace settings and member management            |
| [Workspace Editor](#workspace-editor) | Full permissions for most resources, cannot manage workspace settings or delete certain resources |
| [Workspace Viewer](#workspace-viewer) | Read-only access to all workspace resources                                                       |

<Note>
  RBAC (Role-Based Access Control) is a feature that is only available to [Enterprise](https://langchain.com/pricing) customers. If you are interested in this feature, [contact our sales team](https://www.langchain.com/contact-sales). Other plans default to using the Admin role for all users.
</Note>

#### Workspace admin

**Description**: Role with full permissions for all resources and ability to manage workspace.

**Permissions**:

* All create, read, update, delete, and share permissions for all resource types
* Workspace management capabilities

For a comprehensive list of required permissions along with the operations and roles that can perform them, refer to the [Organization and workspace reference](/langsmith/organization-workspace-operations).

#### Workspace editor

**Description**: Role with full permissions for most resources. Cannot manage workspace settings or delete certain critical resources.

**Key Differences from Admin**:

* Cannot delete [runs](/langsmith/observability-concepts#runs)
* Cannot manage workspace settings (change workspace name, etc.)
* Cannot manage workspace members (add, remove, or update member roles)

#### Workspace viewer

**Description**: Read-only access to all workspace resources.

**Permissions**: Read-only access to all resource types.

For a comprehensive list of required permissions along with the operations and roles that can perform them, refer to the [Organization and workspace reference](/langsmith/organization-workspace-operations).

<Tip>
  For step-by-step instructions on assigning workspace roles to users, refer to the [User Management guide](/langsmith/user-management#assign-a-role-to-a-user).
</Tip>

## Custom roles

<Info>Creating custom roles is available for organizations on the Enterprise plan.</Info>

[Organization Admins](#organization-admin) can create custom roles with specific combinations of permissions tailored to their organization's needs.

### Creating custom roles

Custom roles are created at the [organization](/langsmith/administration-overview#organizations) level and can be assigned to users in any [workspace](/langsmith/administration-overview#workspaces) within that organization.

**Steps**:

1. Navigate to Organization **Settings** > **Roles**.
2. Click **Create Custom Role**.
3. Select the permissions to include in the role.
4. Assign the custom role to users in specific workspaces.

For details on which specific permissions are required for each operation, refer to the [Organization and workspace operations reference](/langsmith/organization-workspace-operations).

Note the following details on custom roles:

* Custom roles can only be created and managed by Organization Admins.
* Custom roles are organization-specific (not transferable between organizations).
* Each custom role can have any combination of workspace-level permissions.
* Custom roles cannot have organization-level permissions.
* Users can have different roles (including custom roles) in different workspaces.

### Understand permission behavior

Some permissions offer granular control when used in custom roles:

* `workspaces:manage` does **not** include the ability to manage workspace members. To allow a custom role to add, remove, or update workspace members, you must explicitly grant `workspaces:manage-members`. The built-in Workspace Admin role includes both permissions automatically.
* `bulk-exports:read` and `bulk-exports:manage` cover the bulk export endpoints (listing, creating, cancelling exports, and managing destinations). Use them in a custom role to grant least-privilege bulk export access without `workspaces:manage`. The built-in Workspace Admin role includes `bulk-exports:manage` and all read-capable roles include `bulk-exports:read` automatically.
* `projects:increase-trace-tier` and `projects:decrease-trace-tier` are independent and can be granted separately. For example, you can allow a role to decrease retention without allowing it to increase retention. If a user lacks both permissions, the retention settings UI is hidden entirely. If they have only one, the UI is partially enabled (the disallowed direction is disabled).
* `projects:update` covers only metadata updates (name, description, tags) and does **not** grant the ability to change trace retention. To allow a custom role to modify trace tier, you must explicitly grant `projects:increase-trace-tier`, `projects:decrease-trace-tier`, or both.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/rbac.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# How to read experiment results locally
Source: https://docs.langchain.com/langsmith/read-local-experiment-results

When running [evaluations](/langsmith/evaluation-concepts), you may want to process results programmatically in your script rather than viewing them in the [LangSmith UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-read-local-experiment-results). This is useful for scenarios like:

* **CI/CD pipelines**: Implement quality gates that fail builds if evaluation scores drop below a threshold.
* **Local debugging**: Inspect and analyze results without API calls.
* **Custom aggregations**: Calculate metrics and statistics using your own logic.
* **Integration testing**: Use evaluation results to gate merges or deployments.

This guide shows you how to iterate over and process [experiment](/langsmith/evaluation-concepts#experiment) results from the [`ExperimentResults`](https://reference.langchain.com/python/langsmith/schemas/ExperimentResults) object returned by [`Client.evaluate()`](https://reference.langchain.com/python/langsmith/client/Client/evaluate).

<Note>
  This page focuses on processing results programmatically while still uploading them to LangSmith.

  If you want to run evaluations locally **without** recording anything to LangSmith (for quick testing or validation), refer to [Run an evaluation locally](/langsmith/local) which uses `upload_results=False`.
</Note>

## Iterate over evaluation results

The [`evaluate()`](https://reference.langchain.com/python/langsmith/client/Client/evaluate) function returns an [`ExperimentResults`](https://reference.langchain.com/python/langsmith/schemas/ExperimentResults) object that you can iterate over. The `blocking` parameter controls when results become available:

* `blocking=False`: Returns immediately with an iterator that yields results as they're produced. This allows you to process results in real-time as the evaluation runs.
* `blocking=True` (default): Blocks until all evaluations complete before returning. When you iterate over the results, all data is already available.

Both modes return the same `ExperimentResults` type; the difference is whether the function waits for completion before returning. Use `blocking=False` for streaming and real-time debugging, or `blocking=True` for batch processing when you need the complete dataset.

The following example demonstrates `blocking=False`. It iterates over results as they stream in, collects them in a list, then processes them in a separate loop:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langsmith import Client
import random

client = Client()

def target(inputs):
    """Your application or LLM chain"""
    return {"output": "MY OUTPUT"}

def evaluator(run, example):
    """Your evaluator function"""
    return {"key": "randomness", "score": random.randint(0, 1)}

# Run evaluation with blocking=False to get an iterator
streamed_results = client.evaluate(
    target,
    data="MY_DATASET_NAME",
    evaluators=[evaluator],
    blocking=False
)

# Collect results as they stream in
aggregated_results = []
for result in streamed_results:
    aggregated_results.append(result)

# Separate loop to avoid logging at the same time as logs from evaluate()
for result in aggregated_results:
    print("Input:", result["run"].inputs)
    print("Output:", result["run"].outputs)
    print("Evaluation Results:", result["evaluation_results"]["results"])
    print("--------------------------------")
```

This produces output like:

```
Input: {'input': 'MY INPUT'}
Output: {'output': 'MY OUTPUT'}
Evaluation Results: [EvaluationResult(key='randomness', score=1, value=None, comment=None, correction=None, evaluator_info={}, feedback_config=None, source_run_id=UUID('7ebb4900-91c0-40b0-bb10-f2f6a451fd3c'), target_run_id=None, extra=None)]
--------------------------------
```

## Understand the result structure

Each result in the iterator contains:

* `result["run"]`: The execution of your target function.
  * `result["run"].inputs`: The inputs from your [dataset](/langsmith/evaluation-concepts#datasets) example.
  * `result["run"].outputs`: The outputs produced by your target function.
  * `result["run"].id`: The unique ID for this run.

* `result["evaluation_results"]["results"]`: A list of `EvaluationResult` objects, one per evaluator.
  * `key`: The metric name (from your evaluator's return value).
  * `score`: The numeric score (typically 0-1 or boolean).
  * `comment`: Optional explanatory text.
  * `source_run_id`: The ID of the evaluator run.

* `result["example"]`: The dataset example that was evaluated.
  * `result["example"].inputs`: The input values.
  * `result["example"].outputs`: The reference outputs (if any).

## Examples

### Implement a quality gate

This example uses evaluation results to pass or fail a CI/CD build automatically based on quality thresholds. The script iterates through results, calculates an average accuracy score, and exits with a non-zero status code if the accuracy falls below 85%. This ensures that you can deploy code changes that meet quality standards.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langsmith import Client
import sys

client = Client()

def my_application(inputs):
    # Your application logic
    return {"response": "..."}

def accuracy_evaluator(run, example):
    # Your evaluation logic
    is_correct = run.outputs["response"] == example.outputs["expected"]
    return {"key": "accuracy", "score": 1 if is_correct else 0}

# Run evaluation
results = client.evaluate(
    my_application,
    data="my_test_dataset",
    evaluators=[accuracy_evaluator],
    blocking=False
)

# Calculate aggregate metrics
total_score = 0
count = 0

for result in results:
    eval_result = result["evaluation_results"]["results"][0]
    total_score += eval_result.score
    count += 1

average_accuracy = total_score / count

print(f"Average accuracy: {average_accuracy:.2%}")

# Fail the build if accuracy is too low
if average_accuracy < 0.85:
    print("❌ Evaluation failed! Accuracy below 85% threshold.")
    sys.exit(1)

print("✅ Evaluation passed!")
```

### Batch processing with blocking=True

When you need to perform operations that require the complete dataset (like calculating percentiles, sorting by score, or generating summary reports), use `blocking=True` to wait for all evaluations to complete before processing:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}

# Run evaluation and wait for all results
results = client.evaluate(
    target,
    data=dataset,
    evaluators=[evaluator],
    blocking=True  # Wait for all evaluations to complete
)

# Process all results after evaluation completes
for result in results:
    print("Input:", result["run"].inputs)
    print("Output:", result["run"].outputs)

    # Access individual evaluation results
    for eval_result in result["evaluation_results"]["results"]:
        print(f"  {eval_result.key}: {eval_result.score}")
```

With `blocking=True`, your processing code runs only after all evaluations are complete, avoiding mixed output with evaluation logs.

For more information on running evaluations without uploading results, refer to [Run an evaluation locally](/langsmith/local).

## Related

* [Evaluate your LLM application](/langsmith/evaluate-llm-application)
* [Run an evaluation locally](/langsmith/local)
* [Fetch performance metrics from an experiment](/langsmith/fetch-perf-metrics-experiment)

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/read-local-experiment-results.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# LangSmith reference
Source: https://docs.langchain.com/langsmith/reference

The following sections provide API references and SDK documentation for LangSmith:

## LangSmith SDKs

<CardGroup>
  <Card title="Python SDK" icon="brand-python" href="/langsmith/smith-python-sdk">
    Reference documentation for the LangSmith Python SDK.
  </Card>

  <Card title="JavaScript/TypeScript SDK" icon="brand-javascript" href="/langsmith/smith-js-ts-sdk">
    Reference documentation for the LangSmith JavaScript/TypeScript SDK.
  </Card>

  <Card title="Go SDK" icon="brand-golang" href="/langsmith/smith-go-sdk">
    Reference documentation for the LangSmith Go SDK.
  </Card>

  <Card title="Java SDK" icon="coffee" href="/langsmith/smith-java-sdk">
    Reference documentation for the LangSmith Java SDK.
  </Card>
</CardGroup>

## LangGraph SDKs

<CardGroup>
  <Card title="LangGraph Python SDK" icon="sitemap" href="/langsmith/langgraph-python-sdk">
    Reference documentation for deploying LangGraph applications with Python.
  </Card>

  <Card title="LangGraph JS/TS SDK" icon="sitemap" href="/langsmith/langgraph-js-ts-sdk">
    Reference documentation for deploying LangGraph applications with JavaScript/TypeScript.
  </Card>
</CardGroup>

## APIs

<CardGroup>
  <Card title="LangSmith API" icon="code" href="/langsmith/smith-api-ref">
    Complete REST API reference for LangSmith platform features.
  </Card>

  <Card title="Deployment APIs" icon="server" href="/langsmith/server-api-ref">
    API references for self-hosted and hybrid LangSmith deployments.
  </Card>
</CardGroup>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/reference.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Regions FAQ
Source: https://docs.langchain.com/langsmith/regions-faq

<Note>
  See the [cloud architecture reference](/langsmith/cloud#cloud-architecture-and-scalability) for additional details.
</Note>

## Legal and compliance

#### *What privacy and data protection frameworks does LangSmith, including its regional instances, comply with?*

LangSmith complies with the General Data Protection Regulation (GDPR) and other laws and regulations applicable to the LangSmith service. We are also SOC 2 Type 2 certified and are HIPAA compliant. You can request more information about our security policies and posture at [trust.langchain.com](https://trust.langchain.com). If you would like to sign a Data Processing Addendum (DPA) with us, please contact support via [support.langchain.com](https://support.langchain.com). Please note we only enter into Business Associate Agreements (BAAs) with customers on our Enterprise plan.

#### *My company isn't based in a region, can I still have my data hosted there?*

Yes, you can host your LangSmith data in a supported regional instance independent of your location.

#### *Do you have a legal entity in the EU that we can contract with?*

We do not have a legal entity in the EU for customer contracting today.

#### *Do different legal terms apply if I choose a specific region?*

The terms are the same across supported cloud regions.

## Features

#### *How do I use a specific regional instance?*

Follow the [account and API key setup guide](/langsmith/create-account-api-key) to create an account and an API key. Make sure to choose the correct region in the region dropdown.

#### *Are there any functional differences between cloud-managed LangSmith regions?*

There may be a small delay between launches to each region depending on the feature. Besides that, supported cloud regions are functionally equivalent.

#### *Can an organization have workspaces in different regions?*

LangSmith does not support this at the moment, but if you are interested, please contact support via [support.langchain.com](https://support.langchain.com) and share your use case.

#### *Can I connect organizations across regions and share billing?*

LangSmith does not support this at the moment, but if you are interested, please contact support via [support.langchain.com](https://support.langchain.com) and share your use case.

#### *What data will be stored in my selected region?*

See the [cloud architecture reference](/langsmith/cloud#cloud-architecture-and-scalability) for details.

#### *How can I see my organization's region?*

Check your URL - organizations on [https://smith.langchain.com?utm\_source=docs\&utm\_medium=cta\&utm\_campaign=langsmith-signup\&utm\_content=langsmith-regions-faq](https://smith.langchain.com) are in GCP US, organizations on [https://eu.smith.langchain.com](https://eu.smith.langchain.com) are in GCP EU, organizations on [https://apac.smith.langchain.com](https://apac.smith.langchain.com) are in GCP APAC, and organizations on [https://aws.smith.langchain.com](https://aws.smith.langchain.com) are in AWS US.

#### *Can I switch my organization between regions?*

We do not support migration between regions at this time, but if you are interested in this feature, please contact support via [support.langchain.com](https://support.langchain.com).

## Plans and pricing

#### *Are regional instances available on all LangSmith plans?*

Yes, you can sign up for supported regional instances on all plans including free plans.

#### *Is pricing different by region?*

No, pricing is the same across supported cloud regions.

#### *What currency is used for payment if I use a regional instance?*

All LangSmith plans are paid in USD.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/regions-faq.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Reject Concurrent
Source: https://docs.langchain.com/langsmith/reject-concurrent

This guide assumes knowledge of what double-texting is, which you can learn about in the [double-texting conceptual guide](/langsmith/double-texting).

The guide covers the `reject` option for double texting, which rejects the new run of the graph by throwing an error and continues with the original run until completion. Below is a quick example of using the `reject` option.

## Setup

First, we will define a quick helper function for printing out JS and CURL model outputs (you can skip this if using Python):

<Tabs>
  <Tab title="Javascript">
    ```js theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    function prettyPrint(m) {
      const padded = " " + m['type'] + " ";
      const sepLen = Math.floor((80 - padded.length) / 2);
      const sep = "=".repeat(sepLen);
      const secondSep = sep + (padded.length % 2 ? "=" : "");

      console.log(`${sep}${padded}${secondSep}`);
      console.log("\n\n");
      console.log(m.content);
    }
    ```
  </Tab>

  <Tab title="CURL">
    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    # PLACE THIS IN A FILE CALLED pretty_print.sh
    pretty_print() {
      local type="$1"
      local content="$2"
      local padded=" $type "
      local total_width=80
      local sep_len=$(( (total_width - ${#padded}) / 2 ))
      local sep=$(printf '=%.0s' $(eval "echo {1.."${sep_len}"}"))
      local second_sep=$sep
      if (( (total_width - ${#padded}) % 2 )); then
        second_sep="${second_sep}="
      fi

      echo "${sep}${padded}${second_sep}"
      echo
      echo "$content"
    }
    ```
  </Tab>
</Tabs>

Now, let's import our required packages and instantiate our client, assistant, and thread.

<Tabs>
  <Tab title="Python">
    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    import httpx
    from langchain_core.messages import convert_to_messages
    from langgraph_sdk import get_client

    client = get_client(url=<DEPLOYMENT_URL>)
    # Using the graph deployed with the name "agent"
    assistant_id = "agent"
    thread = await client.threads.create()
    ```
  </Tab>

  <Tab title="Javascript">
    ```js theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    import { Client } from "@langchain/langgraph-sdk";

    const client = new Client({ apiUrl: <DEPLOYMENT_URL> });
    // Using the graph deployed with the name "agent"
    const assistantId = "agent";
    const thread = await client.threads.create();
    ```
  </Tab>

  <Tab title="CURL">
    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    curl --request POST \
      --url <DEPLOYMENT_URL>/threads \
      --header 'Content-Type: application/json' \
      --data '{}'
    ```
  </Tab>
</Tabs>

## Create runs

Now we can run a thread and try to run a second one with the "reject" option, which should fail since we have already started a run:

<Tabs>
  <Tab title="Python">
    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    run = await client.runs.create(
        thread["thread_id"],
        assistant_id,
        input={"messages": [{"role": "user", "content": "what's the weather in sf?"}]},
    )
    try:
        await client.runs.create(
            thread["thread_id"],
            assistant_id,
            input={
                "messages": [{"role": "user", "content": "what's the weather in nyc?"}]
            },
            multitask_strategy="reject",
        )
    except httpx.HTTPStatusError as e:
        print("Failed to start concurrent run", e)
    ```
  </Tab>

  <Tab title="Javascript">
    ```js theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    const run = await client.runs.create(
      thread["thread_id"],
      assistantId,
      input={"messages": [{"role": "user", "content": "what's the weather in sf?"}]},
    );

    try {
      await client.runs.create(
        thread["thread_id"],
        assistantId,
        {
          input: {"messages": [{"role": "user", "content": "what's the weather in nyc?"}]},
          multitask_strategy:"reject"
        },
      );
    } catch (e) {
      console.error("Failed to start concurrent run", e);
    }
    ```
  </Tab>

  <Tab title="CURL">
    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    curl --request POST \
    --url <DEPLOY<ENT_URL>>/threads/<THREAD_ID>/runs \
    --header 'Content-Type: application/json' \
    --data "{
      \"assistant_id\": \"agent\",
      \"input\": {\"messages\": [{\"role\": \"human\", \"content\": \"what\'s the weather in sf?\"}]},
    }" && curl --request POST \
    --url <DEPLOY<ENT_URL>>/threads/<THREAD_ID>/runs \
    --header 'Content-Type: application/json' \
    --data "{
      \"assistant_id\": \"agent\",
      \"input\": {\"messages\": [{\"role\": \"human\", \"content\": \"what\'s the weather in nyc?\"}]},
      \"multitask_strategy\": \"reject\"
    }" || { echo "Failed to start concurrent run"; echo "Error: $?" >&2; }
    ```
  </Tab>
</Tabs>

Output:

```
Failed to start concurrent run Client error '409 Conflict' for url 'http://localhost:8123/threads/f9e7088b-8028-4e5c-88d2-9cc9a2870e50/runs'
For more information check: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/409
```

## View run results

We can verify that the original thread finished executing:

<Tabs>
  <Tab title="Python">
    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    # wait until the original run completes
    await client.runs.join(thread["thread_id"], run["run_id"])

    state = await client.threads.get_state(thread["thread_id"])

    for m in convert_to_messages(state["values"]["messages"]):
        m.pretty_print()
    ```
  </Tab>

  <Tab title="Javascript">
    ```js theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    await client.runs.join(thread["thread_id"], run["run_id"]);

    const state = await client.threads.getState(thread["thread_id"]);

    for (const m of state["values"]["messages"]) {
      prettyPrint(m);
    }
    ```
  </Tab>

  <Tab title="CURL">
    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    source pretty_print.sh && curl --request GET \
    --url <DEPLOYMENT_URL>/threads/<THREAD_ID>/runs/<RUN_ID>/join && \
    curl --request GET --url <DEPLOYMENT_URL>/threads/<THREAD_ID>/state | \
    jq -c '.values.messages[]' | while read -r element; do
        type=$(echo "$element" | jq -r '.type')
        content=$(echo "$element" | jq -r '.content | if type == "array" then tostring else . end')
        pretty_print "$type" "$content"
    done
    ```
  </Tab>
</Tabs>

Output:

```
================================ Human Message =================================

what's the weather in sf?
================================== Ai Message ==================================

[{'id': 'toolu_01CyewEifV2Kmi7EFKHbMDr1', 'input': {'query': 'weather in san francisco'}, 'name': 'tavily_search_results_json', 'type': 'tool_use'}]
Tool Calls:
tavily_search_results_json (toolu_01CyewEifV2Kmi7EFKHbMDr1)
Call ID: toolu_01CyewEifV2Kmi7EFKHbMDr1
Args:
query: weather in san francisco
================================= Tool Message =================================
Name: tavily_search_results_json

[{"url": "https://www.accuweather.com/en/us/san-francisco/94103/june-weather/347629", "content": "Get the monthly weather forecast for San Francisco, CA, including daily high/low, historical averages, to help you plan ahead."}]
================================== Ai Message ==================================

According to the search results from Tavily, the current weather in San Francisco is:

The average high temperature in San Francisco in June is around 65°F (18°C), with average lows around 54°F (12°C). June tends to be one of the cooler and foggier months in San Francisco due to the marine layer of fog that often blankets the city during the summer months.

Some key points about the typical June weather in San Francisco:

* Mild temperatures with highs in the 60s F and lows in the 50s F
* Foggy mornings that often burn off to sunny afternoons
* Little to no rainfall, as June falls in the dry season
* Breezy conditions, with winds off the Pacific Ocean
* Layers are recommended for changing weather conditions

In summary, you can expect mild, foggy mornings giving way to sunny but cool afternoons in San Francisco this time of year. The marine layer keeps temperatures moderate compared to other parts of California in June.
```

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/reject-concurrent.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Release policy
Source: https://docs.langchain.com/langsmith/release-versions

Release channels, cadence, and version support for self-hosted LangSmith.

Self-hosted LangSmith ships on two release channels: a stable channel that customers run in production, and a preview channel that tracks the next major version.

## Release channels

### Stable

The current generally available major version. LangSmith recommends this channel for production. Stable receives weekly patch releases containing critical bug fixes and security patches only. No new features, data migrations, or infrastructure changes land on stable between major versions.

At any given time, the latest major version (N) is the preview channel and the previous major version (N-1) is stable.

### Preview

The development build of the next major version. Preview includes new features and fixes as they merge into LangSmith SaaS, so you can evaluate the next major version before it becomes stable. Preview builds may include data migrations, but never add or remove services or introduce breaking changes.

Preview is intended for evaluation in test and staging environments. LangSmith does not recommend running preview in production.

## Release cadence

| Channel                      | Cadence                                                                                                |
| ---------------------------- | ------------------------------------------------------------------------------------------------------ |
| Preview                      | Published mirroring the LangSmith SaaS release cadence                                                 |
| Stable: new major (`v0.X.0`) | Approximately every 6 weeks (two per quarter)                                                          |
| Stable: patch (`v0.X.Y`)     | Weekly (typically Friday), skipped if no changes. Ad-hoc releases issued for critical customer issues. |

## What ships in each channel

|                               | Preview |  Stable patch | Next major |
| ----------------------------- | :-----: | :-----------: | :--------: |
| New features                  |   yes   |       no      |     yes    |
| Bug fixes                     |   yes   | critical only |     yes    |
| Security patches              |   yes   |      yes      |     yes    |
| Data migrations and backfills |   yes   |       no      |     yes    |
| New or removed services       |    no   |       no      |     yes    |
| Breaking changes              |    no   |       no      |     yes    |

Service additions, service removals, and breaking changes only land in a new major version, so plan upgrades to new majors with this in mind.

## Version numbering

Self-hosted LangSmith uses the following scheme:

* `v0.X.0`: Major version (stable GA release)
* `v0.X.Y`: Stable patch release (critical fixes only)
* `v0.X.0-rcN`: Preview build (release candidate) for the next major version, where `N` is an incrementing build number

## Version support

LangSmith supports the current stable major version and the two previous stable major versions. When `N` represents the current stable major version:

* `N` receives active support, including critical bug fixes, security patches, and new patch releases.
* `N-1` and `N-2` receive critical support, including critical bug fixes and security patches.
* Versions older than `N-2` are end of life and do not receive new patch releases, bug fixes, or security updates.

## Recommendations

* **Run stable in production.** Preview is for evaluation only and may contain unreleased features still under validation.
* **Use preview in test or staging.** Running preview in a non-production environment is the best way to catch issues early and prepare for the next major upgrade.
* **Plan for major upgrades.** Data migrations, service additions or removals, and breaking changes only land in new major versions. Review the [self-hosted changelog](/langsmith/self-hosted-changelog) before upgrading and plan for any required data or infrastructure changes.
* **Stay on a supported version.** LangSmith recommends upgrading to each new major version soon after it is released to pick up architectural improvements on the recommended cadence.

## Current version

To check the current stable and preview versions, refer to the [self-hosted changelog](/langsmith/self-hosted-changelog).

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/release-versions.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# RemoteGraph
Source: https://docs.langchain.com/langsmith/remote-graph

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/remote-graph.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# How to evaluate with repetitions
Source: https://docs.langchain.com/langsmith/repetition

Running multiple repetitions can give a more accurate estimate of the performance of your system since LLM outputs are not deterministic. Outputs can differ from one repetition to the next. Repetitions are a way to reduce noise in systems prone to high variability, such as agents.

## Configuring repetitions on an experiment

Add the optional `num_repetitions` param to the `evaluate` / `aevaluate` function ([Python](https://docs.smith.langchain.com/reference/python/evaluation/langsmith.evaluation._runner.evaluate), [TypeScript](https://docs.smith.langchain.com/reference/js/interfaces/evaluation.EvaluateOptions#numrepetitions)) to specify how many times to evaluate over each example in your dataset. For instance, if you have 5 examples in the dataset and set `num_repetitions=5`, each example will be run 5 times, for a total of 25 runs.

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langsmith import evaluate

  results = evaluate(
      lambda inputs: label_text(inputs["text"]),
      data=dataset_name,
      evaluators=[correct_label],
      experiment_prefix="Toxic Queries",
      num_repetitions=3,
  )
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { evaluate } from "langsmith/evaluation";

  await evaluate((inputs) => labelText(inputs["input"]), {
    data: datasetName,
    evaluators: [correctLabel],
    experimentPrefix: "Toxic Queries",
    numRepetitions: 3,
  });
  ```
</CodeGroup>

## Viewing results of experiments run with repetitions

If you've run your experiment with [repetitions](/langsmith/repetition), there will be arrows in the output results column so you can view outputs in the table. To view each run from the repetition, hover over the output cell and click the expanded view. When you run an experiment with repetitions, LangSmith displays the average for each feedback score in the table. Click on the feedback score to view the feedback scores from individual runs, or to view the standard deviation across repetitions.

<img alt="Repetitions" />

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/repetition.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Make conversations private
Source: https://docs.langchain.com/langsmith/resource-auth

In this tutorial, you will extend [the chatbot created in the last tutorial](/langsmith/set-up-custom-auth) to give each user their own private conversations. You'll add [resource-level access control](/langsmith/auth#single-owner-resources) so users can only see their own threads.

<img alt="Authorization flow: after authentication, an authorization handler tags each resource with owner=user id and returns a filter so users only see their own threads." />

## Prerequisites

Before you start this tutorial, ensure you have the [bot from the first tutorial](/langsmith/set-up-custom-auth) running without errors.

## 1. Add resource authorization

Recall that in the last tutorial, the [`Auth`](https://reference.langchain.com/python/langgraph-sdk/auth/Auth) object lets you register an [authentication function](/langsmith/auth#authentication), which LangSmith uses to validate the bearer tokens in incoming requests. Now you'll use it to register an **authorization** handler.

Authorization handlers are functions that run **after** authentication succeeds. These handlers can add [metadata](/langsmith/auth#filter-operations) to resources (like who owns them) and filter what each user can see.

Update your `src/security/auth.py` and add one authorization handler to run on every request:

```python {highlight={29-39}} title="src/security/auth.py" theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langgraph_sdk import Auth
