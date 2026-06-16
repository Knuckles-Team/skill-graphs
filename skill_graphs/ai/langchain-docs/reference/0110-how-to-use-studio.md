# How to use Studio
Source: https://docs.langchain.com/langsmith/use-studio

This page describes the core workflows you’ll use in Studio. It explains how to run your application, manage assistant configurations, and work with conversation threads. Each section includes steps in both graph mode (full-featured view of your graph’s execution) and chat mode (lightweight conversational interface):

* [Run application](#run-application): Execute your application or agent and observe its behavior.
* [Manage assistants](#manage-assistants): Create, edit, and select the assistant configuration used by your application.
* [Manage threads](#manage-threads): View and organize the threads, including forking or editing past runs for debugging.

## Run application

<Tabs>
  <Tab title="Graph">
    ### Specify input

    1. Define the input to your graph in the **Input** section on the left side of the page, below the graph interface. Studio will attempt to render a form for your input based on the graph's defined [state schema](/oss/python/langgraph/graph-api/#schema). To disable this, click the **View Raw** button, which will present you with a JSON editor.
    2. Click the up or down arrows at the top of the **Input** section to toggle through and use previously submitted inputs.

    ### Run settings

    #### Assistant

    To specify the [assistant](/langsmith/assistants) that is used for the run:

    1. Click the **Settings** button in the bottom left corner. If an assistant is currently selected the button will also list the assistant name. If no assistant is selected it will say **Manage Assistants**.
    2. Select the assistant to run.
    3. Click the **Active** toggle at the top of the modal to activate it.

    For more information, refer to [Manage assistants](#manage-assistants).

    #### Streaming

    Click the dropdown next to **Submit** and click the toggle to enable or disable streaming.

    #### Breakpoints

    To run your graph with breakpoints:

    1. Click **Interrupt**.
    2. Select a node and whether to pause before or after that node has executed.
    3. Click **Continue** in the thread log to resume execution.

    For more information on breakpoints, refer to [Human-in-the-loop](/oss/python/langchain/human-in-the-loop).

    ### Submit run

    To submit the run with the specified input and run settings:

    1. Click the **Submit** button. This will add a [run](/langsmith/runs) to the existing selected [thread](/oss/python/langgraph/checkpointers#threads). If no thread is currently selected, a new one will be created.
    2. To cancel the ongoing run, click the **Cancel** button.
  </Tab>

  <Tab title="Chat">
    Specify the input to your chat application in the bottom of the conversation panel.

    1. Click the **Send message** button to submit the input as a Human message and have the response streamed back.

    To cancel the ongoing run:

    1. Click **Cancel**.
    2. Click the **Show tool calls** toggle to hide or show tool calls in the conversation.
  </Tab>
</Tabs>

## Manage assistants

Studio lets you view, edit, and update your assistants, and allows you to run your graph using these assistant configurations.

For more conceptual details, refer to the [Assistants overview](/langsmith/assistants/).

<Tabs>
  <Tab title="Graph">
    To view your assistants:

    1. Click **Manage Assistants** in the bottom left corner. This opens a modal for you to view all the assistants for the selected graph.
    2. Specify the assistant and its version you would like to mark as **Active**. LangSmith will use this assistant when runs are submitted.

    The **Default configuration** option will be active, which reflects the default configuration defined in your graph. Edits made to this configuration will be used to update the run-time configuration, but will not update or create a new assistant unless you click **Create new assistant**.
  </Tab>

  <Tab title="Chat">
    Chat mode enables you to switch through the different assistants in your graph via the dropdown selector at the top of the page. To create, edit, or delete assistants, use Graph mode.
  </Tab>
</Tabs>

## Manage threads

Studio provides tools to view all [threads](/oss/python/langgraph/checkpointers#threads) saved on the server and edit their state. You can create new threads, switch between threads, and modify past states both in graph mode and chat mode.

<Tabs>
  <Tab title="Graph">
    ### View threads

    1. In the top of the right-hand pane, select the dropdown menu to view existing threads.
    2. Select the desired thread, and the thread history will populate in the right-hand side of the page.
    3. To create a new thread, click **+ New Thread** and [submit a run](#run-application).
    4. To view more granular information in the thread, drag the slider at the top of the page to the right. To view less information, drag the slider to the left. Additionally, collapse or expand individual turns, nodes, and keys of the state.
    5. Switch between `Pretty` and `JSON` mode for different rendering formats.

    ### Edit thread history

    To edit the state of the thread:

    1. Select <Icon icon="pencil" /> **Edit node state** next to the desired node.
    2. Edit the node's output as desired and click **Fork** to confirm. This will create a new forked run from the checkpoint of the selected node.

    If you instead want to re-run the thread from a given checkpoint without editing the state, click **Re-run from here**. This will again create a new forked run from the selected checkpoint. This is useful for re-running with changes that are not specific to the state, such as the selected assistant.
  </Tab>

  <Tab title="Chat">
    1. View all threads in the right-hand pane of the page.
    2. Select the desired thread and the thread history will populate in the center panel.
    3. To create a new thread, click **+** and submit a run.

    To edit a human message in the thread:

    1. Click <Icon icon="pencil" /> **Edit node state** below the human message.
    2. Edit the message as desired and submit. This will create a new fork of the conversation history.
    3. To re-generate an AI message, click the retry icon below the AI message.
  </Tab>
</Tabs>

## Next steps

Refer to the following guides for more detail on tasks you can complete in Studio:

* [Iterate on prompts](/langsmith/observability-studio)
* [Run experiments over datasets](/langsmith/observability-studio#run-experiments-over-a-dataset)

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/use-studio.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Use the Context Hub
Source: https://docs.langchain.com/langsmith/use-the-context-hub

Learn how to create, view, and promote context in the LangSmith Context Hub.

The **Context Hub** gives your team version-controlled, environment-aware management of the instructions and tools your agents use in production. A *context* is a versioned bundle of agent instructions and tools, either a skill or a full agent, that you manage in LangSmith.

Use this guide to create your first context, view its files and history, and promote it to an environment so your agents can pull it.

## 1. Open the Context Hub

<Note>
  If you don't see **Context** in the left-hand navigation, verify that Context Hub is enabled for your workspace and that you have the required permissions.
</Note>

In the [LangSmith UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-use-the-context-hub), select **Context** in the
left-hand navigation. The Context Hub lists every agent and skill in your workspace.

<img alt="The Context Hub home view listing existing Agent and Skill contexts with their commit metadata." />

## 2. Create a context

1. Click **+ Create** in the top left of the Context Hub.

2. Choose the context type:

   * **Agent:** a full agent bundle including an `AGENTS.md` file and tools.
   * **Skill:** a reusable capability that agents can use, including a `SKILL.md` file.

   <img alt="The Create dropdown showing the Agent and Skill context type options." />

3. Fill in a name and description. For skills, a description is required. You can also enter the initial file contents (`SKILL.md` for a skill, `AGENTS.md` for an agent) now, or add them after creation. Click **Create Agent** or **Create Skill**. LangSmith creates the repo and opens it for editing.

## 3. View a context

Click on an agent or skill from the Context Hub to view it.

<img alt="An Agent context with an AGENTS.md file open, showing the environments panel, commit history, and file tree." />

The middle panel shows the file tree for the current commit and the right panel previews the selected file. Click a file in the middle panel to open it, then edit it in the right panel and save your changes to create a new commit.

Each saved change creates a new **commit** in the **Commit History** panel on
the left, so you can browse, compare, and revert prior versions without losing
work.

## 4. Tag and promote a commit

Once a commit is ready to ship, promote it to an environment so downstream
agents can pull it.

<Note>
  Context Hub currently supports two environment tags for promotion: `staging` and `production`.
</Note>

1. With the target commit selected, click **Promote** in the top right.

2. Choose the destination environment:

   * **Promote to Production:** the commit your production agents pull.
   * **Promote to Staging:** a pre-production environment for validation.

   <img alt="The Promote dropdown with options to promote a commit to Production or Staging." />

3. The environment label (for example, `Production 7ca95573`) moves to the
   promoted commit. Use the **Tag** button next to **Promote** to attach a
   human-readable label to any commit for easy reference.

Agent runtimes that resolve context by environment tag (for example, `:production`) now pull this promoted commit.

## Next steps

* [Context engineering concepts](/langsmith/context-engineering-concepts): learn about skills, agents, versioning, and sharing.
* [Manage contexts with the SDK](/langsmith/manage-contexts-sdk): push, pull, list, and delete contexts programmatically.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/use-the-context-hub.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Use threads
Source: https://docs.langchain.com/langsmith/use-threads

This guide shows you how to create, view, and inspect *threads*. Threads work with [assistants](/langsmith/assistants) to enable [stateful](/oss/python/langgraph/persistence) execution of your [deployed graphs](/langsmith/deployment).

## Understand threads

A thread is a persistent conversation container that maintains state across multiple runs. Each time you execute a run on a thread, the graph processes the input with the thread's current state and updates that state with new information.

Threads enable stateful interactions by preserving conversation history and context between runs. Without threads, each run would be stateless, with no memory of previous interactions. Threads are particularly useful for:

* Multi-turn conversations where the assistant needs to remember what was discussed.
* Long-running tasks that require maintaining context across multiple steps.
* User-specific state management where each user has their own conversation history.

The diagram illustrates how a thread maintains state across two runs. The second run has access to the messages from the first run, allowing the assistant to understand that the context of "What about tomorrow?" refers to the weather query from the first run:

```mermaid actions={false} theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
sequenceDiagram
    participant User
    participant Thread
    participant Assistant
    participant Graph

    Note over Thread: Thread ID: abc-123<br/>Persistent conversation

    User->>Thread: Run 1: "What's the weather?"
    Thread->>Assistant: Use Assistant Config
    Assistant->>Graph: Execute with context
    Graph-->>Thread: Update State<br/>{messages: [user_msg, ai_response]}
    Thread-->>User: Response

    Note over Thread: State persisted ✓

    User->>Thread: Run 2: "What about tomorrow?"
    Note over Thread: Previous messages<br/>still in state
    Thread->>Assistant: Use Assistant Config
    Assistant->>Graph: Execute with full history
    Graph-->>Thread: Update State<br/>{messages: [...prev, new_msgs]}
    Thread-->>User: Response with context
```

* A thread maintains a persistent conversation with a unique thread ID.
* Each run applies the assistant's configuration to the graph execution.
* State is updated after each run and persists for subsequent runs.
* Later runs have access to the full conversation history.

<Note>
  - **[Assistants](/langsmith/assistants)** define the configuration (model, prompts, tools) for how your graph executes. When creating a run, you can specify either a **graph ID** (e.g., `"agent"`) to use the default assistant, or an **assistant ID** (UUID) to use a specific configuration.
  - **Threads** maintain the state and conversation history.
  - **Runs** combine an assistant and thread to execute your graph with a specific configuration and state.
</Note>

<Tip>
  Best practice: When tracing runs in a thread (conversation), ensure that `thread_id` is set on all runs—both parent and child runs. This is required for thread filtering, token counting, and thread-level evaluations to work correctly.
</Tip>

## Create a thread

To run your graph with state persistence, you must first create a thread:

<Tabs>
  <Tab title="SDK">
    ### Empty thread

    To create a new thread, use one of:

    <CodeGroup>
      ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      from langgraph_sdk import get_client

      # Initialize the client with your deployment URL
      client = get_client(url=<DEPLOYMENT_URL>)

      # Create an empty thread
      # This creates a new thread with no initial state
      thread = await client.threads.create()

      print(thread)
      ```

      ```javascript JavaScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import { Client } from "@langchain/langgraph-sdk";

      // Initialize the client with your deployment URL
      const client = new Client({ apiUrl: <DEPLOYMENT_URL> });

      // Create an empty thread
      // This creates a new thread with no initial state
      const thread = await client.threads.create();

      console.log(thread);
      ```

      ```bash cURL theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      curl --request POST \
          --url <DEPLOYMENT_URL>/threads \
          --header 'Content-Type: application/json' \
          --data '{}'
      ```
    </CodeGroup>

    For more information, refer to the [Python](https://reference.langchain.com/python/langsmith/deployment/sdk/#langgraph_sdk.client.ThreadsClient.create) and [JS](https://reference.langchain.com/python/langsmith/deployment/sdk/#langgraph_sdk.client.ThreadsClient.create) SDK docs, or the [REST API](/langsmith/agent-server-api/threads/create-thread) reference.

    Output:

    ```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    {
      "thread_id": "123e4567-e89b-12d3-a456-426614174000",
      "created_at": "2025-05-12T14:04:08.268Z",
      "updated_at": "2025-05-12T14:04:08.268Z",
      "metadata": {},
      "status": "idle",
      "values": {}
    }
    ```

    ### Copy thread

    Alternatively, if you already have a thread in your application whose state you wish to copy, you can use the `copy` method. This will create an independent thread whose history is identical to the original thread at the time of the operation:

    <CodeGroup>
      ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      # Copy an existing thread
      # The new thread will have the same state as the original at the time of copying
      copied_thread = await client.threads.copy(thread["thread_id"])
      ```

      ```javascript JavaScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      // Copy an existing thread
      // The new thread will have the same state as the original at the time of copying
      const copiedThread = await client.threads.copy(thread["thread_id"]);
      ```

      ```bash cURL theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      curl --request POST --url <DEPLOYMENT_URL>/threads/thread["thread_id"]/copy \
      --header 'Content-Type: application/json'
      ```
    </CodeGroup>

    For more information, refer to the [Python](https://reference.langchain.com/python/langsmith/deployment/sdk/#langgraph_sdk.client.ThreadsClient.copy) and [JS](https://reference.langchain.com/python/langsmith/deployment/sdk/#langgraph_sdk.client.ThreadsClient.copy) SDK docs, or the [REST API](/langsmith/agent-server-api/threads/copy-thread) reference.

    ### Prepopulated state

    You can create a thread with an arbitrary pre-defined state by providing a list of `supersteps` into the `create` method. The `supersteps` describe a sequence of state updates that establish the initial state of the thread. This is useful when you want to:

    * Create a thread with existing conversation history.
    * Migrate conversations from another system.
    * Set up test scenarios with specific initial states.
    * Resume conversations from a previous session.

    For more information on checkpoints and state management, refer to the [LangGraph persistence documentation](/oss/python/langgraph/persistence).

    <CodeGroup>
      ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      from langgraph_sdk import get_client

      # Initialize the client
      client = get_client(url=<DEPLOYMENT_URL>)

      # Create a thread with pre-populated conversation history
      # The supersteps define a sequence of state updates that build up the initial state
      thread = await client.threads.create(
        graph_id="agent",  # Specify which graph this thread is for
        supersteps=[
          {
            updates: [
              {
                values: {},
                as_node: '__input__',  # Initial input node
              },
            ],
          },
          {
            updates: [
              {
                values: {
                  messages: [
                    {
                      type: 'human',
                      content: 'hello',
                    },
                  ],
                },
                as_node: '__start__',  # User's first message
              },
            ],
          },
          {
            updates: [
              {
                values: {
                  messages: [
                    {
                      content: 'Hello! How can I assist you today?',
                      type: 'ai',
                    },
                  ],
                },
                as_node: 'call_model',  # Assistant's response
              },
            ],
          },
        ])

      print(thread)
      ```

      ```javascript JavaScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import { Client } from "@langchain/langgraph-sdk";

      // Initialize the client
      const client = new Client({ apiUrl: <DEPLOYMENT_URL> });

      // Create a thread with pre-populated conversation history
      // The supersteps define a sequence of state updates that build up the initial state
      const thread = await client.threads.create({
          graphId: 'agent',  // Specify which graph this thread is for
          supersteps: [
          {
            updates: [
              {
                values: {},
                asNode: '__input__',  // Initial input node
              },
            ],
          },
          {
            updates: [
              {
                values: {
                  messages: [
                    {
                      type: 'human',
                      content: 'hello',
                    },
                  ],
                },
                asNode: '__start__',  // User's first message
              },
            ],
          },
          {
            updates: [
              {
                values: {
                  messages: [
                    {
                      content: 'Hello! How can I assist you today?',
                      type: 'ai',
                    },
                  ],
                },
                asNode: 'call_model',  // Assistant's response
              },
            ],
          },
        ],
      });

      console.log(thread);
      ```

      ```bash cURL theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      curl --request POST \
          --url <DEPLOYMENT_URL>/threads \
          --header 'Content-Type: application/json' \
          --data '{"metadata":{"graph_id":"agent"},"supersteps":[{"updates":[{"values":{},"as_node":"__input__"}]},{"updates":[{"values":{"messages":[{"type":"human","content":"hello"}]},"as_node":"__start__"}]},{"updates":[{"values":{"messages":[{"content":"Hello\u0021 How can I assist you today?","type":"ai"}]},"as_node":"call_model"}]}]}'
      ```
    </CodeGroup>

    Output:

    ```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    {
      "thread_id": "f15d70a1-27d4-4793-a897-de5609920b7d",
      "created_at": "2025-05-12T15:37:08.935038+00:00",
      "updated_at": "2025-05-12T15:37:08.935046+00:00",
      "metadata": {
        "graph_id": "agent"
      },
      "status": "idle",
      "config": {},
      "values": {
        "messages": [
          {
            "content": "hello",
            "additional_kwargs": {},
            "response_metadata": {},
            "type": "human",
            "name": null,
            "id": "8701f3be-959c-4b7c-852f-c2160699b4ab",
            "example": false
          },
          {
            "content": "Hello! How can I assist you today?",
            "additional_kwargs": {},
            "response_metadata": {},
            "type": "ai",
            "name": null,
            "id": "4d8ea561-7ca1-409a-99f7-6b67af3e1aa3",
            "example": false,
            "tool_calls": [],
            "invalid_tool_calls": [],
            "usage_metadata": null
          }
        ]
      }
    }
    ```
  </Tab>

  <Tab title="UI">
    You can also create threads directly from the [LangSmith UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-use-threads):

    1. Navigate to your [deployment](/langsmith/deployment).
    2. Select the **Threads** tab.
    3. Click **+ New thread**.
    4. Optionally provide metadata or initial state for the thread.
    5. Click **Create thread**.

    The newly created thread will appear in the threads table and can be used for runs immediately.
  </Tab>
</Tabs>

## List threads

<Tabs>
  <Tab title="SDK">
    To list threads, use the `search` method. This will list the threads in the application that match the provided filters:

    ### Filter by thread status

    Use the `status` field to filter threads based on their status. Supported values are `idle`, `busy`, `interrupted`, and `error`. For example, to view `idle` threads:

    <CodeGroup>
      ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      # Search for idle threads
      # The status filter accepts: idle, busy, interrupted, error
      print(await client.threads.search(status="idle", limit=1))
      ```

      ```javascript JavaScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      // Search for idle threads
      // The status filter accepts: idle, busy, interrupted, error
      console.log(await client.threads.search({ status: "idle", limit: 1 }));
      ```

      ```bash cURL theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      curl --request POST \
      --url <DEPLOYMENT_URL>/threads/search \
      --header 'Content-Type: application/json' \
      --data '{"status": "idle", "limit": 1}'
      ```
    </CodeGroup>

    For more information, refer to the [Python](https://reference.langchain.com/python/langsmith/deployment/sdk/#langgraph_sdk.client.ThreadsClient.search) and [JS](https://reference.langchain.com/python/langsmith/deployment/sdk/#langgraph_sdk.client.ThreadsClient.search) SDK docs, or the [REST API](/langsmith/agent-server-api/threads/search-threads) reference.

    Output:

    ```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    [
      {
        "thread_id": "cacf79bb-4248-4d01-aabc-938dbd60ed2c",
        "created_at": "2024-08-14T17:36:38.921660+00:00",
        "updated_at": "2024-08-14T17:36:38.921660+00:00",
        "metadata": {
          "graph_id": "agent"
        },
        "status": "idle",
        "config": {
          "configurable": {}
        }
      }
    ]
    ```

    ### Filter by metadata

    The `search` method allows you to filter on metadata. This is useful for finding threads associated with specific graphs, users, or custom metadata you've added to threads.

    Common metadata fields you can filter on include:

    | Metadata key             | Description                                                                                                      |
    | ------------------------ | ---------------------------------------------------------------------------------------------------------------- |
    | `graph_id`               | The graph (deployment) the thread belongs to.                                                                    |
    | `assistant_id`           | The [assistant](/langsmith/assistants) used to create runs on the thread.                                        |
    | `langgraph_auth_user_id` | The authenticated user who owns the thread (set automatically when using [custom auth](/langsmith/custom-auth)). |
    | `cron_id`                | The [cron job](/langsmith/cron-jobs) that created runs on the thread.                                            |

    You can also filter on any custom metadata you attach when creating or updating threads.

    #### Filter by graph

    <CodeGroup>
      ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      print(await client.threads.search(metadata={"graph_id": "agent"}, limit=1))
      ```

      ```javascript JavaScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      console.log(await client.threads.search({ metadata: { "graph_id": "agent" }, limit: 1 }));
      ```

      ```bash cURL theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      curl --request POST \
      --url <DEPLOYMENT_URL>/threads/search \
      --header 'Content-Type: application/json' \
      --data '{"metadata": {"graph_id": "agent"}, "limit": 1}'
      ```
    </CodeGroup>

    Output:

    ```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    [
      {
        "thread_id": "cacf79bb-4248-4d01-aabc-938dbd60ed2c",
        "created_at": "2024-08-14T17:36:38.921660+00:00",
        "updated_at": "2024-08-14T17:36:38.921660+00:00",
        "metadata": {
          "graph_id": "agent"
        },
        "status": "idle",
        "config": {
          "configurable": {}
        }
      }
    ]
    ```

    #### Filter by assistant

    <CodeGroup>
      ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      print(await client.threads.search(
          metadata={"assistant_id": "fe096781-5601-53d2-b2f6-0d3403f7e9ca"},
          limit=1,
      ))
      ```

      ```javascript JavaScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      console.log(await client.threads.search({
        metadata: { "assistant_id": "fe096781-5601-53d2-b2f6-0d3403f7e9ca" },
        limit: 1,
      }));
      ```

      ```bash cURL theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      curl --request POST \
      --url <DEPLOYMENT_URL>/threads/search \
      --header 'Content-Type: application/json' \
      --data '{"metadata": {"assistant_id": "fe096781-5601-53d2-b2f6-0d3403f7e9ca"}, "limit": 1}'
      ```
    </CodeGroup>

    #### Filter by cron job

    <CodeGroup>
      ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      print(await client.threads.search(
          metadata={"cron_id": "8b98a268-e49a-4228-a0d3-1a354e3a54d0"},
          limit=10,
      ))
      ```

      ```javascript JavaScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      console.log(await client.threads.search({
        metadata: { "cron_id": "8b98a268-e49a-4228-a0d3-1a354e3a54d0" },
        limit: 10,
      }));
      ```

      ```bash cURL theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      curl --request POST \
      --url <DEPLOYMENT_URL>/threads/search \
      --header 'Content-Type: application/json' \
      --data '{"metadata": {"cron_id": "8b98a268-e49a-4228-a0d3-1a354e3a54d0"}, "limit": 10}'
      ```
    </CodeGroup>

    ### Sorting

    The SDK also supports sorting threads by `thread_id`, `status`, `created_at`, and `updated_at` using the `sort_by` and `sort_order` parameters.
  </Tab>

  <Tab title="UI">
    You can also view and manage threads in a deployment via the [LangSmith UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-use-threads):

    1. Navigate to your [deployment](/langsmith/deployment).
    2. Select the **Threads** tab.

    This will load a table of all threads in your deployment.

    **Filter by thread status:** Select a status in the top bar to filter threads by `idle`, `busy`, `interrupted`, or `error`.

    **Sort threads:** Click on the arrow icon for any column header to sort by that property (`thread_id`, `status`, `created_at`, or `updated_at`).
  </Tab>
</Tabs>

## Inspect threads

<Tabs>
  <Tab title="SDK">
    ### Get thread

    To view a specific thread given its `thread_id`, use the [`get`](https://reference.langchain.com/python/langsmith/deployment/sdk/#langgraph_sdk.client.ThreadsClient.get) method:

    <CodeGroup>
      ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      # Retrieve a specific thread by its ID
      # Returns the thread metadata including status, creation time, and metadata
      print((await client.threads.get(thread["thread_id"])))
      ```

      ```javascript JavaScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      // Retrieve a specific thread by its ID
      // Returns the thread metadata including status, creation time, and metadata
      console.log((await client.threads.get(thread["thread_id"])));
      ```

      ```bash cURL theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      curl --request GET \
      --url <DEPLOYMENT_URL>/threads/thread["thread_id"] \
      --header 'Content-Type: application/json'
      ```
    </CodeGroup>

    Output:

    ```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    {
      "thread_id": "cacf79bb-4248-4d01-aabc-938dbd60ed2c",
      "created_at": "2024-08-14T17:36:38.921660+00:00",
      "updated_at": "2024-08-14T17:36:38.921660+00:00",
      "metadata": {
        "graph_id": "agent"
      },
      "status": "idle",
      "config": {
        "configurable": {}
      }
    }
    ```

    For more information, refer to the [Python](https://reference.langchain.com/python/langsmith/deployment/sdk/#langgraph_sdk.client.ThreadsClient.get) and [JS](https://reference.langchain.com/python/langsmith/deployment/sdk/#langgraph_sdk.client.ThreadsClient.get) SDK docs, or the [REST API](/langsmith/agent-server-api/threads/get-thread) reference.

    ### Inspect thread state

    To view the current state of a given thread, use the [`get_state`](https://reference.langchain.com/python/langsmith/deployment/sdk/#langgraph_sdk.client.ThreadsClient.get_state) method. This returns the current values, next nodes to execute, and checkpoint information:

    <CodeGroup>
      ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      # Get the current state of a thread
      # Returns values, next nodes, tasks, checkpoint info, and metadata
      print((await client.threads.get_state(thread["thread_id"])))
      ```

      ```javascript JavaScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      // Get the current state of a thread
      // Returns values, next nodes, tasks, checkpoint info, and metadata
      console.log((await client.threads.getState(thread["thread_id"])));
      ```

      ```bash cURL theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      curl --request GET \
      --url <DEPLOYMENT_URL>/threads/thread["thread_id"]/state \
      --header 'Content-Type: application/json'
      ```
    </CodeGroup>

    Output:

    ```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    {
      "values": {
        "messages": [
          {
            "content": "hello",
            "additional_kwargs": {},
            "response_metadata": {},
            "type": "human",
            "name": null,
            "id": "8701f3be-959c-4b7c-852f-c2160699b4ab",
            "example": false
          },
          {
            "content": "Hello! How can I assist you today?",
            "additional_kwargs": {},
            "response_metadata": {},
            "type": "ai",
            "name": null,
            "id": "4d8ea561-7ca1-409a-99f7-6b67af3e1aa3",
            "example": false,
            "tool_calls": [],
            "invalid_tool_calls": [],
            "usage_metadata": null
          }
        ]
      },
      "next": [],
      "tasks": [],
      "metadata": {
        "thread_id": "f15d70a1-27d4-4793-a897-de5609920b7d",
        "checkpoint_id": "1f02f46f-7308-616c-8000-1b158a9a6955",
        "graph_id": "agent_with_quite_a_long_name",
        "source": "update",
        "step": 1,
        "writes": {
          "call_model": {
            "messages": [
              {
                "content": "Hello! How can I assist you today?",
                "type": "ai"
              }
            ]
          }
        },
        "parents": {}
      },
      "created_at": "2025-05-12T15:37:09.008055+00:00",
      "checkpoint": {
        "checkpoint_id": "1f02f46f-733f-6b58-8001-ea90dcabb1bd",
        "thread_id": "f15d70a1-27d4-4793-a897-de5609920b7d",
        "checkpoint_ns": ""
      },
      "parent_checkpoint": {
        "checkpoint_id": "1f02f46f-7308-616c-8000-1b158a9a6955",
        "thread_id": "f15d70a1-27d4-4793-a897-de5609920b7d",
        "checkpoint_ns": ""
      },
      "checkpoint_id": "1f02f46f-733f-6b58-8001-ea90dcabb1bd",
      "parent_checkpoint_id": "1f02f46f-7308-616c-8000-1b158a9a6955"
    }
    ```

    For more information, refer to the [Python](https://reference.langchain.com/python/langsmith/deployment/sdk/#langgraph_sdk.client.ThreadsClient.get_state) and [JS](https://reference.langchain.com/python/langsmith/deployment/sdk/#langgraph_sdk.client.ThreadsClient.get_state) SDK docs, or the [REST API](/langsmith/agent-server-api/threads/get-thread-state) reference.

    Optionally, to view the state of a thread at a given checkpoint, pass in the checkpoint ID. This is useful for inspecting the thread state at a specific point in its execution history.

    First, get the checkpoint ID from the thread's history:

    <CodeGroup>
      ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      # Get the thread history to find checkpoint IDs
      history = await client.threads.get_history(thread_id=thread["thread_id"])
      checkpoint_id = history[0]["checkpoint_id"]  # Get the most recent checkpoint
      ```

      ```javascript JavaScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      // Get the thread history to find checkpoint IDs
      const history = await client.threads.getHistory(thread["thread_id"]);
      const checkpointId = history[0].checkpoint_id;  // Get the most recent checkpoint
      ```

      ```bash cURL theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      # Get the thread history to find checkpoint IDs
      curl --request POST \
      --url <DEPLOYMENT_URL>/threads/thread["thread_id"]/history \
      --header 'Content-Type: application/json' \
      --data '{"limit": 1}'
      ```
    </CodeGroup>

    Then use the checkpoint ID to get the state at that specific point:

    <CodeGroup>
      ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      # Get thread state at a specific checkpoint
      # Useful for inspecting historical state or debugging
      thread_state = await client.threads.get_state(
        thread_id=thread["thread_id"],
        checkpoint_id=checkpoint_id
      )
      ```

      ```javascript JavaScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      // Get thread state at a specific checkpoint
      // Useful for inspecting historical state or debugging
      const threadState = await client.threads.getState(thread["thread_id"], checkpointId);
      ```

      ```bash cURL theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      curl --request GET \
      --url <DEPLOYMENT_URL>/threads/thread["thread_id"]/state/<CHECKPOINT_ID> \
      --header 'Content-Type: application/json'
      ```
    </CodeGroup>

    ### Inspect full thread history

    To view a thread's history, use the [`get_history`](https://reference.langchain.com/python/langsmith/deployment/sdk/#langgraph_sdk.client.ThreadsClient.get_history) method. This returns a list of every state the thread experienced, allowing you to trace the full execution path:

    <CodeGroup>
      ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      # Get the full history of a thread
      # Returns a list of all state snapshots from the thread's execution
      history = await client.threads.get_history(
        thread_id=thread["thread_id"],
        limit=10  # Optional: limit the number of states returned
      )

      for state in history:
          print(f"Checkpoint: {state['checkpoint_id']}")
          print(f"Step: {state['metadata']['step']}")
      ```

      ```javascript JavaScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      // Get the full history of a thread
      // Returns a list of all state snapshots from the thread's execution
      const history = await client.threads.getHistory(
        thread["thread_id"],
        {
          limit: 10  // Optional: limit the number of states returned
        }
      );

      for (const state of history) {
        console.log(`Checkpoint: ${state.checkpoint_id}`);
        console.log(`Step: ${state.metadata.step}`);
      }
      ```

      ```bash cURL theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      curl --request POST \
      --url <DEPLOYMENT_URL>/threads/thread["thread_id"]/history \
      --header 'Content-Type: application/json' \
      --data '{"limit": 10}'
      ```
    </CodeGroup>

    This method is particularly useful for:

    * Debugging execution flow by seeing how state evolved.
    * Understanding decision points in your graph's execution.
    * Auditing conversation history and state changes.
    * Replaying or analyzing past interactions.

    For more information, refer to the [Python](https://reference.langchain.com/python/langsmith/deployment/sdk/#langgraph_sdk.client.ThreadsClient.get_history) and [JS](https://reference.langchain.com/python/langsmith/deployment/sdk/#langgraph_sdk.client.ThreadsClient.get_history) SDK docs, or the [REST API](/langsmith/agent-server-api/threads/get-thread-history) reference.
  </Tab>

  <Tab title="UI">
    You can also view and inspect threads in the [LangSmith UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-use-threads):

    1. Navigate to your [deployment](/langsmith/deployment).
    2. Select the **Threads** tab to view all threads.
    3. Click on a thread to inspect its current state.

    To view the full thread history and perform detailed debugging, click **Open in Studio** to open the thread in [Studio](/langsmith/studio). Studio provides a visual interface for exploring the thread's execution history, state changes, and checkpoint details.
  </Tab>
</Tabs>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/use-threads.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Use tools in a prompt
Source: https://docs.langchain.com/langsmith/use-tools

Tools allow language models to interact with external systems and perform actions beyond just generating text. In the Playground, you can use two types of tools:

1. [**Built-in tools**](#built-in-tools): Pre-configured tools provided by model providers (like OpenAI and Anthropic) that are ready to use. Use built-in tools when you need common capabilities like web search or code interpretation.
2. [**Custom tools**](#create-a-custom-tool): Functions you define to perform specific tasks. These are useful when you need to integrate with your own systems or create specialized functionality. When you define custom tools within the Playground, you can verify that the model correctly identifies and calls these tools with the correct arguments.

LangSmith automatically saves tools you create to a workspace-wide [tool registry](#manage-tools-with-the-registry), which makes them available for reuse across all your prompts and sessions.

## Built-in tools

The Playground has native support for a variety of tools from OpenAI and Anthropic. If you want to use a tool that isn't explicitly listed in the Playground, you can still add it by manually specifying its `type` and any required arguments.

### OpenAI tools

* **Web search**: [Search the web for real-time information](https://platform.openai.com/docs/guides/tools-web-search?api-mode=responses).
* **Image generation**: [Generate images based on a text prompt](https://platform.openai.com/docs/guides/tools-image-generation).
* **MCP**: [Gives the model access to tools hosted on a remote MCP server](https://platform.openai.com/docs/guides/tools-remote-mcp).
* [View all OpenAI tools](https://platform.openai.com/docs/guides/tools?api-mode=responses).

### Anthropic tools

* **Web search**: [Search the web for up-to-date information](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool).
* [View all Anthropic tools](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview).

## Add and use tools

The Playground lets you quickly [add tools](#add-a-tool) to any prompt with a single click. You can choose from built-in tools provided by model providers like OpenAI and Anthropic, or define your own [custom tools](#create-a-custom-tool) tailored to your specific needs. Once you create a custom tool, it's automatically added to a workspace-wide [tool registry](#manage-tools-with-the-registry) where you can enable, disable, or edit it across different prompts without recreating it.

### Add a tool

To add a tool to your prompt, click the **+ Tool** button at the bottom of the prompt editor.

<img alt="The prompt interface with the + Tool button following the editing boxes." />

<img alt="The prompt interface with the + Tool button following the editing boxes." />

### Use a built-in tool

1. In the tool section, select the built-in tool you want to use. You'll only see the tools that are compatible with the provider and model you've chosen.
2. When the model calls the tool, the Playground will display the response.

   <img alt="Web search tool" />

### Create a custom tool

To create a custom tool, you'll need to provide:

* **Name**: A descriptive name for your tool.
* **Description**: Clear explanation of what the tool does.
* **Arguments**: The inputs your tool requires.

<img alt="Custom tool" />

When running a custom tool in the Playground, the model will respond with a JSON object containing the tool name and the tool call.

<img alt="Tool call" />

### Manage tools with the registry

The Playground includes a [workspace](/langsmith/administration-overview#workspaces)-scoped **tool registry** that persists both custom and built-in tools across prompts and sessions. When you create a custom tool or add a built-in tool, it's automatically saved to your workspace registry and becomes available for reuse in any prompt. You can enable or disable tools per prompt to control which tools are active for each specific prompt, and when editing a shared tool, you can choose to update the registry version or save as a new tool.

Click the **+ Tool** button in the Playground to open **Manage tools**. You can do the following:

* Select and view existing tools in the **Available Tools** tab.
* Toggle individual tools on/off using the **Enabled** switch.
* Edit existing tools by clicking on them in the list.
* Delete tools using the **Delete** at the bottom of **Manage tools**.

<img alt="Manage tools with a list of available tools, Enabled switch, and edit functionality." />

<img alt="Manage tools with a list of available tools, Enabled switch, and edit functionality." />

Tools are stored with their complete configuration including name, description, parameters, and metadata. The registry supports both custom function tools and built-in tool configurations.

## Tool choice settings

Some models provide control over which tools are called. To configure this:

1. Select **+ Tool** under the prompt editor.
2. Navigate to the **Tool Choice Setting** tab.
3. Select your tool choice.

To understand the available tool choice options, check the documentation for your specific provider. For example, [OpenAI's documentation on tool choice](https://platform.openai.com/docs/guides/function-calling/function-calling-behavior?api-mode=responses#tool-choice).

<img alt="Select tools from the Tool Choice Settings tab." />

<img alt="Select tools from the Tool Choice Settings tab." />

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/use-tools.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
