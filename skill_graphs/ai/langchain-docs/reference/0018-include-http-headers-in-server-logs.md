# Include HTTP headers in server logs
Source: https://docs.langchain.com/langsmith/configurable-logs

By default, the [Agent Server](/langsmith/agent-server) omits HTTP headers from server logs for privacy reasons. However, logging request and correlation IDs can help you debug issues and trace requests across distributed systems. You can opt-in to logging headers for all API calls by modifying the `logging_headers` section in your [`langgraph.json`](/langsmith/application-structure#configuration-file) file.

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "$schema": "https://langgra.ph/schema.json",
  "http": {
    "logging_headers": {
      "includes": ["request-id", "x-purchase-id", "*-trace-*"],
      "excludes": ["authorization", "x-api-key", "x-organization-id", "x-user-id"]
    }
  }
}
```

The `includes` and `excludes` lists accept exact header names or glob patterns using `*` as a wildcard to match any number of characters (case-insensitive). For your security, no other pattern types are supported.

Note that exclusions take precedence over inclusions. For example, if you include `*-id` but exclude `x-user-id`, the `x-user-id` header will not be logged.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/configurable-logs.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Manage assistants
Source: https://docs.langchain.com/langsmith/configuration-cloud

This page describes how to create, configure, and manage [assistants](/langsmith/assistants). Assistants allow you to customize your [deployed](/langsmith/deployment) graph's behavior through configuration—such as model selection, prompts, and tool availability—without changing the underlying graph code.

You can work with the [SDK](https://reference.langchain.com/python/langsmith/deployment/sdk/) or in the [LangSmith UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-configuration-cloud).

## Understand assistant configuration

Assistants store *context* values that customize graph behavior at runtime. You define a context schema in your graph code, then provide specific context values when creating an assistant via the [`context` parameter](https://reference.langchain.com/python/langsmith/deployment/sdk/#langgraph_sdk.client.AssistantsClient.create).

Consider this example of a `call_model` node that reads the `model_name` from the context:

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  class ContextSchema(TypedDict):
      model_name: str

  builder = StateGraph(AgentState, context_schema=ContextSchema)

  def call_model(state, runtime: Runtime[ContextSchema]):
      messages = state["messages"]
      model = _get_model(runtime.context.get("model_name", "anthropic"))
      response = model.invoke(messages)
      return {"messages": [response]}
  ```

  ```javascript JavaScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { Annotation } from "@langchain/langgraph";

  const ContextSchema = Annotation.Root({
      model_name: Annotation<string>,
      system_prompt: Annotation<string>,
  });

  const builder = new StateGraph(AgentState, ContextSchema)

  function callModel(state: State, runtime: Runtime[ContextSchema]) {
    const messages = state.messages;
    const model = _getModel(runtime.context.model_name ?? "anthropic");
    const response = model.invoke(messages);
    return { messages: [response] };
  }
  ```
</CodeGroup>

When you create an assistant, you provide specific values for these configuration fields. The assistant stores this configuration and applies it whenever the graph runs.

For more information on configuration in [LangGraph](/oss/python/langgraph/overview), refer to the [runtime context documentation](/oss/python/langgraph/graph-api#runtime-context).

**Select SDK or UI for your workflow:**

<Tabs>
  <Tab title="SDK">
    ## Create an assistant

    Use the [AssistantsClient.create](https://reference.langchain.com/python/langsmith/deployment/sdk/#langgraph_sdk.client.AssistantsClient.create) method to create a new assistant. This method requires:

    * **Graph ID**: The name of the deployed graph this assistant will use (e.g., `"agent"`).
    * **Context**: Configuration values matching your graph's context schema.
    * **Name**: A descriptive name for the assistant.

    The following example creates an assistant with `model_name` set to `openai`:

    <CodeGroup>
      ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      from langgraph_sdk import get_client

      # Initialize the client with your deployment URL
      client = get_client(url=<DEPLOYMENT_URL>)

      # Create an assistant for the "agent" graph
      # The first parameter is the graph ID (also called graph name)
      openai_assistant = await client.assistants.create(
          "agent",  # Graph ID of the deployed graph
          context={"model_name": "openai"},
          name="Open AI Assistant"
      )

      print(openai_assistant)
      # Output includes the assistant_id (UUID) that uniquely identifies this assistant
      ```

      ```javascript JavaScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import { Client } from "@langchain/langgraph-sdk";

      // Initialize the client with your deployment URL
      const client = new Client({ apiUrl: <DEPLOYMENT_URL> });

      // Create an assistant for the "agent" graph
      const openAIAssistant = await client.assistants.create({
          graphId: 'agent',  // Graph ID of the deployed graph
          name: "Open AI Assistant",
          context: { "model_name": "openai" },
      });

      console.log(openAIAssistant);
      // Output includes the assistant_id (UUID) that uniquely identifies this assistant
      ```

      ```bash cURL theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      curl --request POST \
          --url <DEPLOYMENT_URL>/assistants \
          --header 'Content-Type: application/json' \
          --data '{"graph_id":"agent", "context":{"model_name":"openai"}, "name": "Open AI Assistant"}'
      ```
    </CodeGroup>

    **Response:**

    The API returns an assistant object containing:

    * `assistant_id`: A UUID that uniquely identifies this assistant
    * `graph_id`: The graph this assistant is configured for
    * `context`: The configuration values you provided
    * `name`, `metadata`, timestamps, and other fields

    ```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    {
      "assistant_id": "62e209ca-9154-432a-b9e9-2d75c7a9219b",
      "graph_id": "agent",
      "name": "Open AI Assistant",
      "context": {
        "model_name": "openai"
      },
      "metadata": {},
      "created_at": "2024-08-31T03:09:10.230718+00:00",
      "updated_at": "2024-08-31T03:09:10.230718+00:00"
    }
    ```

    The `assistant_id` (a UUID like `"62e209ca-9154-432a-b9e9-2d75c7a9219b"`) uniquely identifies this assistant configuration. You'll use this ID when running your graph to specify which configuration to apply.

    <Note>
      **Graph ID vs Assistant ID**

      When creating an assistant, you specify a **graph ID** (graph name like `"agent"`). This returns an **assistant ID** (UUID like `"62e209ca..."`). You can use either when running your graph:

      * **Graph ID** (e.g., `"agent"`): Uses the default assistant for that graph
      * **Assistant ID** (UUID): Uses the specific assistant configuration

      See [Use an assistant](#use-an-assistant) for examples.
    </Note>

    ## Use an assistant

    To use an assistant, pass its `assistant_id` when creating a run. The example below uses the assistant we created above:

    <CodeGroup>
      ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      # Create a thread for the conversation
      thread = await client.threads.create()

      # Prepare the input
      input = {"messages": [{"role": "user", "content": "who made you?"}]}

      # Run the graph using the assistant's configuration
      # Pass the assistant_id (UUID) as the second parameter
      async for event in client.runs.stream(
          thread["thread_id"],
          openai_assistant["assistant_id"],  # Assistant ID (UUID)
          input=input,
          stream_mode="updates",
      ):
          print(f"Receiving event of type: {event.event}")
          print(event.data)
          print("\n\n")
      ```

      ```javascript JavaScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      // Create a thread for the conversation
      const thread = await client.threads.create();

      // Prepare the input
      const input = { "messages": [{ "role": "user", "content": "who made you?" }] };

      // Run the graph using the assistant's configuration
      // Pass the assistant_id (UUID) as the second parameter
      const streamResponse = client.runs.stream(
        thread["thread_id"],
        openAIAssistant["assistant_id"],  // Assistant ID (UUID)
        {
          input,
          streamMode: "updates"
        }
      );

      for await (const event of streamResponse) {
        console.log(`Receiving event of type: ${event.event}`);
        console.log(event.data);
        console.log("\n\n");
      }
      ```

      ```bash cURL theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      # First, create a thread
      thread_id=$(curl --request POST \
          --url <DEPLOYMENT_URL>/threads \
          --header 'Content-Type: application/json' \
          --data '{}' | jq -r '.thread_id')

      # Run the graph with the assistant ID (UUID)
      curl --request POST \
          --url "<DEPLOYMENT_URL>/threads/${thread_id}/runs/stream" \
          --header 'Content-Type: application/json' \
          --data '{
              "assistant_id": "<ASSISTANT_ID>",
              "input": {
                  "messages": [
                      {
                          "role": "user",
                          "content": "who made you?"
                      }
                  ]
              },
              "stream_mode": ["updates"]
          }' | \
          sed 's/\r$//' | \
          awk '
          /^event:/ {
              if (data_content != "") {
                  print data_content "\n"
              }
              sub(/^event: /, "Receiving event of type: ", $0)
              printf "%s...\n", $0
              data_content = ""
          }
          /^data:/ {
              sub(/^data: /, "", $0)
              data_content = $0
          }
          END {
              if (data_content != "") {
                  print data_content "\n\n"
              }
          }
      '
      ```
    </CodeGroup>

    **Response:**

    The stream returns events as the graph executes with your assistant's configuration:

    ```
    Receiving event of type: metadata
    {'run_id': '1ef6746e-5893-67b1-978a-0f1cd4060e16'}

    Receiving event of type: updates
    {'agent': {'messages': [{'content': 'I was created by OpenAI...', ...}]}}
    ```

    <Note>
      **Using graph ID vs assistant ID**

      You can pass either a **graph ID** or **assistant ID** when running your graph:

      ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      # Option 1: Use graph ID to get the default assistant
      client.runs.stream(thread_id, "agent", input=input)

      # Option 2: Use assistant ID (UUID) for a specific configuration
      client.runs.stream(thread_id, "62e209ca-9154-432a-b9e9-2d75c7a9219b", input=input)
      ```
    </Note>

    ## Create a new version for your assistant

    Use the [AssistantsClient.update](https://reference.langchain.com/python/langsmith/deployment/sdk/#langgraph_sdk.client.AssistantsClient.update) method to create a new version of an assistant.

    <Warning>
      **Updates require full configuration**

      You must provide the **entire** configuration when updating. The update endpoint creates new versions from scratch and does not merge with previous versions. Include all configuration fields you want to retain.
    </Warning>

    For example, to add a system prompt to the assistant:

    <CodeGroup>
      ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      # Update the assistant with a new configuration
      # IMPORTANT: Include ALL configuration fields, not just the ones you're changing
      openai_assistant_v2 = await client.assistants.update(
          openai_assistant["assistant_id"],  # Assistant ID (UUID)
          context={
                "model_name": "openai",  # Must include existing fields
                "system_prompt": "You are a mindful assistant!",  # New field
          },
      )

      # This creates version 2 and sets it as the active version
      # Future runs using this assistant_id will use version 2
      ```

      ```javascript JavaScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      // Update the assistant with a new configuration
      // IMPORTANT: Include ALL configuration fields, not just the ones you're changing
      const openaiAssistantV2 = await client.assistants.update(
          openAIAssistant["assistant_id"],  // Assistant ID (UUID)
          {
              context: {
                  model_name: 'openai',  // Must include existing fields
                  system_prompt: 'You are a mindful assistant!',  // New field
              },
          },
      );

      // This creates version 2 and sets it as the active version
      // Future runs using this assistant_id will use version 2
      ```

      ```bash cURL theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      curl --request PATCH \
      --url <DEPLOYMENT_URL>/assistants/<ASSISTANT_ID> \
      --header 'Content-Type: application/json' \
      --data '{
      "context": {"model_name": "openai", "system_prompt": "You are a mindful assistant!"}
      }'
      ```
    </CodeGroup>

    The update creates a new version and automatically sets it as active. All future runs using this assistant ID will use the new configuration.

    ## Use a previous assistant version

    Use the `setLatest` method to change which version is active:

    <CodeGroup>
      ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      # Roll back to version 1 of the assistant
      await client.assistants.set_latest(
          openai_assistant['assistant_id'],  # Assistant ID (UUID)
          1  # Version number
      )

      # All future runs using this assistant_id will now use version 1
      ```

      ```javascript JavaScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      // Roll back to version 1 of the assistant
      await client.assistants.setLatest(
          openaiAssistant['assistant_id'],  // Assistant ID (UUID)
          1  // Version number
      );

      // All future runs using this assistant_id will now use version 1
      ```

      ```bash cURL theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      curl --request POST \
      --url <DEPLOYMENT_URL>/assistants/<ASSISTANT_ID>/latest \
      --header 'Content-Type: application/json' \
      --data '{
      "version": 1
      }'
      ```
    </CodeGroup>

    After changing the active version, all runs using this assistant ID will use the specified version's configuration.
  </Tab>

  <Tab title="UI">
    ## Create an assistant

    You can create assistants from the [LangSmith UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-configuration-cloud):

    1. Navigate to your deployment and select the **Assistants** tab.
    2. Click **+ New assistant**.
    3. In the form that opens:
       * Select the graph this assistant is for.
       * Provide a name and description.
       * Configure the assistant using the configuration schema for that graph.
    4. Click **Create assistant**.

    This will take you to [Studio](/langsmith/studio) where you can test the assistant. Return to the **Assistants** tab to see your newly created assistant in the table.

    ## Use an assistant

    To use an assistant in the LangSmith UI:

    1. Navigate to your deployment and select the **Assistants** tab.
    2. Find the assistant you want to use.
    3. Click **Studio** for that assistant.

    This opens [Studio](/langsmith/studio) with the selected assistant. When you submit an input (in **Graph** or **Chat** mode), the assistant's configuration will be applied to the run.

    ## Create a new version for your assistant

    To update an assistant and create a new version from the UI, you can use either the Assistants tab or Studio. Either method creates a new version and sets it as the active version:

    <Tabs>
      <Tab title="Assistants tab">
        1. Navigate to your deployment and select the **Assistants** tab.
        2. Find the assistant you want to edit.
        3. Click **Edit**.
        4. Modify the assistant's name, description, or configuration.
        5. Save your changes.
      </Tab>

      <Tab title="Studio">
        1. Open Studio for the assistant.
        2. Click **Manage Assistants**.
        3. Edit the assistant's configuration.
        4. Save your changes.
      </Tab>
    </Tabs>

    ## Use a previous assistant version

    To set a previous version as active from Studio:

    1. Open Studio for the assistant.
    2. Click **Manage Assistants**.
    3. Locate the assistant and select the version you want to use.
    4. Toggle the **Active** switch for that version.

    This updates the assistant to use the selected version for all future runs.

    <Warning>
      Deleting an assistant will delete **all** of its versions. There is currently no way to delete a single version. To skip a version, simply set a different version as active.
    </Warning>
  </Tab>
</Tabs>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/configuration-cloud.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Configure checkpointer backend
Source: https://docs.langchain.com/langsmith/configure-checkpointer

Configure Agent Server to use PostgreSQL, MongoDB, or a custom implementation for checkpoint storage.

[Agent Server](/langsmith/agent-server) persists graph state using a checkpointer backend. By default, LangSmith stores checkpoints in PostgreSQL alongside other server data. You can switch to MongoDB or provide a custom implementation.

<Note>
  Regardless of the checkpointer backend, LangSmith always requires PostgreSQL for threads, runs, assistants, crons, and the [memory store](/oss/python/langgraph/stores). The checkpointer backend only controls where checkpoint data is stored.
</Note>

## Available backends

| Backend   | Storage       | Configuration                                                 | Use case                                                                            |
| --------- | ------------- | ------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `default` | PostgreSQL    | None (built-in)                                               | Standard deployments                                                                |
| `mongo`   | MongoDB       | `langgraph.json` or `LS_DEFAULT_CHECKPOINTER_BACKEND` env var | Teams with existing MongoDB infrastructure                                          |
| `custom`  | User-provided | `langgraph.json`                                              | Custom storage backends (see [custom checkpointer](/langsmith/custom-checkpointer)) |

## Default (PostgreSQL)

PostgreSQL is the default checkpointer backend. No configuration is needed. To use a custom PostgreSQL instance, set the [`POSTGRES_URI_CUSTOM`](/langsmith/env-var#postgres_uri_custom) environment variable.

## Set up MongoDB checkpointing

<Info>
  Requires Agent Server v0.7.64 or later.
</Info>

### Prerequisites

* A MongoDB **replica set** (standalone `mongod` is not supported). This can be a self-managed replica set, a `mongos` router, or a managed service like MongoDB Atlas.
* A connection URI that includes the database name in the path (e.g., `/langgraph`).

### Select the backend

Set the backend to `"mongo"` using one of these methods:

**In `langgraph.json`** (app-level—bundled with your application code):

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "dependencies": ["."],
  "graphs": {
    "agent": "./agent.py:graph"
  },
  "checkpointer": {
    "backend": "mongo",
    "ttl": {
      "strategy": "delete",
      "default_ttl": 43200,
      "sweep_interval_minutes": 10
    }
  }
}
```

**Via environment variable** (platform-level—for operators managing standalone deployments):

```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
LS_DEFAULT_CHECKPOINTER_BACKEND=mongo
```

The environment variable sets the default backend for agent servers that don't specify one in `langgraph.json`. If `langgraph.json` includes a `backend` value, it takes precedence.

### Provide the MongoDB URI

Set the `LS_MONGODB_URI` environment variable at deploy time:

```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
LS_MONGODB_URI="mongodb://user:password@host:27017/langgraph?replicaSet=rs0"
```

### Connection URI requirements

The URI must:

* Point to a replica set member or `mongos` router
* Include the target database name in the path

Valid examples:

```
mongodb://user:password@host:27017/langgraph?replicaSet=rs0
mongodb://host1:27017,host2:27017,host3:27017/mydb?replicaSet=prod-rs
mongodb+srv://user:password@cluster.example.net/langgraph
```

### Deploy by environment

<Tabs>
  <Tab title="Standalone (Kubernetes)">
    The [langgraph-cloud Helm chart](https://github.com/langchain-ai/helm/blob/main/charts/langgraph-cloud/README.md) (v0.2.6+) has built-in MongoDB support. Enable it in your values file:

    **Bundled MongoDB** (development and testing):

    ```yaml theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    mongo:
      enabled: true
      resources:
        requests:
          cpu: 500m
          memory: 1Gi
      persistence:
        size: 8Gi
    ```

    The chart deploys a single-node MongoDB replica set and automatically configures the server to use it.

    **External MongoDB** (production):

    ```yaml theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    mongo:
      enabled: true
      external:
        enabled: true
        connectionUrl: "mongodb://user:password@mongo.example.net:27017/langgraph?replicaSet=rs0"
    ```

    Or reference an existing Kubernetes secret:

    ```yaml theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    mongo:
      enabled: true
      external:
        enabled: true
        existingSecretName: "my-mongo-secret"
    ```

    The secret must contain a `mongodb_connection_url` key.
  </Tab>

  <Tab title="Standalone (Docker)">
    If your `langgraph.json` already sets `backend` to `"mongo"`, you only need to provide the URI. Otherwise, set both environment variables:

    ```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    docker run \
        --env-file .env \
        -p 8123:8000 \
        -e REDIS_URI="redis://redis:6379" \
        -e DATABASE_URI="postgres://postgres:postgres@postgres:5432/postgres" \
        -e LS_DEFAULT_CHECKPOINTER_BACKEND=mongo \
        -e LS_MONGODB_URI="mongodb://mongo:27017/langgraph?replicaSet=rs0" \
        -e LANGSMITH_API_KEY="..." \
        my-image
    ```

    See the [standalone server guide](/langsmith/deploy-standalone-server) for a full Docker Compose example with MongoDB.
  </Tab>

  <Tab title="Cloud">
    Set `backend` to `"mongo"` in your `langgraph.json`, then add `LS_MONGODB_URI` as an environment variable in your deployment settings in the LangSmith UI.

    Your MongoDB instance must be reachable from the Cloud data plane. A managed service like [MongoDB Atlas](https://www.mongodb.com/atlas) works well for this.

    PostgreSQL is still auto-provisioned for non-checkpoint data.
  </Tab>
</Tabs>

## Custom checkpointer

To use a storage backend other than PostgreSQL or MongoDB, implement a custom [BaseCheckpointSaver](https://reference.langchain.com/python/langgraph/checkpoints/#langgraph.checkpoint.base.BaseCheckpointSaver). See [Add custom checkpointer](/langsmith/custom-checkpointer) for details.

## Related

* [Configure TTLs](/langsmith/configure-ttl) for checkpoint and store item expiration
* [Persistence concepts](/oss/python/langgraph/persistence) in LangGraph
* [Data plane](/langsmith/data-plane) architecture
* [Environment variables](/langsmith/env-var) reference

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/configure-checkpointer.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Configure run input and output preview
Source: https://docs.langchain.com/langsmith/configure-input-output-preview

Customize what appears in the Input and Output columns of the Runs table by configuring custom preview paths for specific trace types.

By default, LangSmith uses a heuristic to determine what to display in the **Input** and **Output** columns of your **Runs** table. However, you can customize exactly what appears in these columns by configuring custom preview paths for specific trace types.

This is particularly useful when:

* Your traces have deeply nested structures.
* You want to focus on specific fields in your data.
* The default heuristic doesn't show the most relevant information for your use case.

## Configure preview format in the UI

### Access preview settings

1. Navigate to a trace in your project.
2. Select the **Runs** tab.
3. Locate the format icon <Icon icon="adjustments-horizontal" /> at the top right of the runs table.
4. In the **Configure Input and Output previews** side window, select a trace name from the dropdown.

When you select a trace name, LangSmith loads a successful trace example and renders its structure as an expandable tree. Each node in the tree represents a field in your data, showing:

* Field names (e.g., `messages` for LLM conversation history, `output`, `metadata`).
* Array indices (e.g., \[0], \[1], \[-1] for last item).
* Item counts for arrays (e.g., (3) indicating 3 items).
* Preview values for strings and numbers displayed inline.

<img alt="Configure Input and Output previews side panel showing the tree view of trace data structure" />

<img alt="Configure Input and Output previews side panel showing the tree view of trace data structure" />

### Set the path

1. Select the **Input** or **Output** tab. Then, either the:

   * Dropdown to specify the path directly from your input data that should be shown in the preview.
   * Interactive tree view of a sample trace's data structure, which you can explore and select the exact field you want to display.

   To select a field:

   1. Navigate the tree by clicking the arrow icons (▶) to expand or collapse nested objects and arrays.
   2. Click the checkbox next to the field you want to display in the preview. The selected path appears in the text input preceding the tree.

   When you select a checkbox, the path is automatically constructed using the correct syntax (e.g., messages\[-1].content).

| Method         | Best For                                                   | Example                                   |
| -------------- | ---------------------------------------------------------- | ----------------------------------------- |
| Tree selection | Exploring unfamiliar data structures, seeing sample values | Click through: messages → \[-1] → content |
| Manual typing  | When you know exactly what you want, faster for deep paths | Type: output.data.results\[0].answer      |

Arrays with more than 3 items are automatically condensed to prevent overwhelming views:

```
☐ messages (15)
  ☐ [0]
  ☐ [1]
  ... (click to expand all 15 items)
```

Click the **...** button to expand and view all array items.

## Example

For example, your trace input is this:

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "messages": [
    {"role": "system", "content": "You are a helpful assistant"},
    {"role": "user", "content": "What is the weather today?"}
  ],
  "metadata": {
    "user_id": "user123",
    "session_id": "sess456"
  }
}
```

In this example, `messages` is an array of message objects, each with a `role` (such as `system` or `user`) and a `content` field.

To display the user's question:

1. Expand the **messages** node (shows array items).
2. Expand `[1]` (the second message, which is the user message).
3. Click the checkbox next to **content**.
4. The input field shows: `messages[1].content`.

Or, use negative indexing for the last message:

1. Expand **messages**.
2. Expand `[-1]`.
3. Click **content**.
4. Result: `messages[-1].content` (always shows the last message).

<Note>
  If you see `"No paths available"` in the tree:

  * Ensure you have at least one successful trace with the selected trace name in the last 7 days.
  * The trace must have data in the input/output field you're configuring.
  * Try sending a test trace if needed.
</Note>

## Next steps

* Learn more about [viewing and filtering traces](/langsmith/filter-traces-in-application).
* Explore [custom output rendering](/langsmith/custom-output-rendering) for advanced visualization.
* Set up [metadata and tags](/langsmith/add-metadata-tags) to organize your traces.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/configure-input-output-preview.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# How to add TTLs to your application
Source: https://docs.langchain.com/langsmith/configure-ttl

<Tip>
  **Prerequisites**
  This guide assumes familiarity with [LangSmith](/langsmith/observability), [Persistence](/oss/python/langgraph/persistence), and [Cross-thread persistence](/oss/python/langgraph/stores) concepts.
</Tip>

LangSmith persists both [checkpoints](/oss/python/langgraph/checkpointers#checkpoints) (thread state) and [cross-thread memories](/oss/python/langgraph/stores) (store items). You can configure Time-to-Live (TTL) policies in [`langgraph.json`](/langsmith/application-structure#configuration-file) to manage the lifecycle of this data automatically, preventing indefinite accumulation.

## Configuring thread and checkpoint TTL

Checkpoints capture the state of conversation threads. Setting a TTL ensures old checkpoints and thread metadata are automatically deleted.

Add a `checkpointer.ttl` configuration to your `langgraph.json` file:

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "dependencies": ["."],
  "graphs": {
    "agent": "./agent.py:graph"
  },
  "checkpointer": {
    "ttl": {
      "strategy": "delete",
      "sweep_interval_minutes": 60,
      "default_ttl": 43200
    }
  }
}
```

* `strategy`: Specifies the action taken on expiration.
  * `"delete"`: Removes the entire thread including all associated run and checkpoint data when the TTL expires.
  * `"keep_latest"`: Retains the thread and latest checkpoint, but deletes older checkpoint data that subsequent runs won't need.
* `sweep_interval_minutes`: Defines how often, in minutes, the system checks for expired checkpoints.
* `default_ttl`: Sets the default lifespan of threads (and corresponding checkpoints) in minutes (e.g., 43200 minutes = 30 days). Applies only to checkpoints created after this configuration is deployed; existing checkpoints/threads are not changed. To clear older data, delete it explicitly.

## Configuring store item TTL

Store items allow cross-thread data persistence. Configuring TTL for store items helps manage memory by removing stale data.

Add a `store.ttl` configuration to your `langgraph.json` file:

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "dependencies": ["."],
  "graphs": {
    "agent": "./agent.py:graph"
  },
  "store": {
    "ttl": {
      "refresh_on_read": true,
      "sweep_interval_minutes": 120,
      "default_ttl": 10080
    }
  }
}
```

* `refresh_on_read`: (Optional, default `true`) If `true`, accessing an item via `get` or `search` resets its expiration timer. If `false`, TTL only refreshes on `put`.
* `sweep_interval_minutes`: (Optional) Defines how often, in minutes, the system checks for expired items. If omitted, no sweeping occurs.
* `default_ttl`: (Optional) Sets the default lifespan of store items in minutes (e.g., 10080 minutes = 7 days). Applies only to items created after this configuration is deployed; existing items are not changed. If you need to clear older items, delete them manually. If omitted, items do not expire by default.

## Combining TTL configurations

You can configure TTLs for both checkpoints and store items in the same `langgraph.json` file to set different policies for each data type. Here is an example:

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "dependencies": ["."],
  "graphs": {
    "agent": "./agent.py:graph"
  },
  "checkpointer": {
    "ttl": {
      "strategy": "delete",
      "sweep_interval_minutes": 60,
      "default_ttl": 43200
    }
  },
  "store": {
    "ttl": {
      "refresh_on_read": true,
      "sweep_interval_minutes": 120,
      "default_ttl": 10080
    }
  }
}
```

## Configure per-thread TTL

You can apply [TTL configurations per-thread](https://reference.langchain.com/python/langsmith/deployment/sdk/#langgraph_sdk.client.ThreadsClient.create).

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
thread = await client.threads.create(
    ttl={
        "strategy": "delete",
        "ttl": 43200  # 30 days in minutes
    }
)
```

<Note>
  Thread-level TTLs will also delete all associated checkpoints. As a result, you can set a thread-level TTL and avoid setting a separate TTL for checkpoints.
</Note>

## Runtime overrides

The default `store.ttl` settings from `langgraph.json` can be overridden at runtime by providing specific TTL values in SDK method calls like `get`, `put`, and `search`.

## Deployment process

After configuring TTLs in `langgraph.json`, deploy or restart your LangGraph application for the changes to take effect. Use [`langgraph dev`](/langsmith/local-dev-testing#langgraph-dev) for local development or [`langgraph up`](/langsmith/local-dev-testing#langgraph-up) for Docker deployment.

For details on other configurable options, refer to the [LangGraph CLI reference page](/langsmith/cli#configuration-file).

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/configure-ttl.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Context engineering concepts
Source: https://docs.langchain.com/langsmith/context-engineering-concepts

Core concepts for context engineering in LangSmith, including skills, agents, versioning, and sharing.

Agents behave inconsistently in production when their context is poorly managed. *Context* is the information an agent relies on to act, such as system instructions, tool definitions, and reference material. *Context engineering* is the practice of building and optimizing that context to improve agent performance and capabilities.

This page covers the core concepts of context engineering in LangSmith: [skills](#skills), [agents](#agents), [the Context Hub](#context-hub-vs-store-backend), [versioning](#versioning), and [sharing](#sharing-and-permissions).

## Skills

A *skill* is a versioned repo in the Context Hub that packages a reusable capability an agent can invoke.

Skill repos usually contain:

**Common files:**

* `SKILL.md` in the root directory for instructions and usage guidance.
* Optional supporting files such as references, templates, and schemas.

Examples include email formatting, code review, and web research.

## Agents

An *agent* is an AI system that completes tasks end to end using tools, skills, and subagents. An *agent repo* packages its configuration, including high-level instructions, linked skills and subagents, and tool configuration.

Agent repos usually contain:

**Common files:**

* `AGENTS.md` for system prompt and operating instructions.
* Optional files such as `tools.json` and linked `agents/*` or `skills/*` entries.

Examples include an email assistant, coding copilot, or customer support agent.

## Choose between skills and agents

Skills are reusable context modules. Agent repos are top-level bundles that define how an agent should operate.

* Use skills for reusable instructions, policies, or examples shared across agents.
* Use agent repos for one agent's operating instructions, tools, and linked dependencies.

## Linked repos

Context Hub commits support three entry types in `files`:

* `file`: inline file content.
* `agent`: link to another agent repo.
* `skill`: link to another skill repo.

When a linked agent or skill repo gets a new commit, LangSmith propagates that update to parent repos that reference it.

<Tip>
  If you find yourself copying the same block of context into several agents, pull it out into a skill repo and reference it from each agent.
</Tip>

## Context Hub vs. store backend

Context in LangSmith can be managed by two different backends: the
**Context Hub** and a **store backend**. They serve different purposes, and most agents use both.

The [Context Hub](/langsmith/use-the-context-hub) is your agents' long-term context store. It tracks every change as a commit and supports versioning, sharing, and continuous improvement.

A *store backend* is built for runtime state. It holds the information an agent accumulates while running: memories, conversation history, user preferences, learned facts, and other data that evolves per session or per user.

## Versioning

Every change to a repo in the **Context Hub** creates a new commit. Commits are immutable, browsable, and comparable, so you can:

* See exactly what changed between two versions of an agent.
* Revert to any prior commit if a change regresses behavior.
* Tag important commits (for example, the commit you shipped on a
  specific date) for easy reference.
* Promote a commit to an **environment** like `Staging` or `Production`
  so downstream agents pull a stable version rather than the latest
  edit.

If this workflow looks familiar, that is intentional: Context Hub brings the same discipline to agent instructions that Git brings to code.

## Sharing and permissions

The **Context Hub** is designed for teams. Every repo lives in a [workspace](/langsmith/administration-overview#workspaces), and access depends on workspace permissions plus repo visibility:

* **Private** repos are visible only inside the workspace.
* **Public** repos can be discovered and pulled by anyone.
* Creating commits, adding tags, and promoting environments requires update access in the workspace.

Workspace-level sharing and visibility controls make the Hub a natural place to collaborate on agents and skills, and improve them over time.

## Next steps

* [Use the Context Hub](/langsmith/use-the-context-hub) to create your first skill or agent.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/context-engineering-concepts.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Context Hub
Source: https://docs.langchain.com/langsmith/context-hub

Manage the instructions and tools your agents use with version control and environment promotion in the LangSmith Context Hub.

The Context Hub gives your team version-controlled, environment-aware management of the instructions and tools your agents use in production. A *context* is a versioned bundle of agent instructions and tools, either a skill or a full agent, that you manage in LangSmith and promote to an environment so your agents can pull it.

<CardGroup>
  <Card title="Concepts" icon="bulb" href="/langsmith/context-engineering-concepts">
    Learn the core concepts of context engineering: skills, agents, versioning, and sharing.
  </Card>

  <Card title="Use the Context Hub" icon="pointer" href="/langsmith/use-the-context-hub">
    Create a context, view its files and history, and promote it to an environment.
  </Card>

  <Card title="Manage contexts with the SDK" icon="code" href="/langsmith/manage-contexts-sdk">
    Push, pull, list, and delete agent and skill repos in the Context Hub programmatically.
  </Card>
</CardGroup>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/context-hub.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
