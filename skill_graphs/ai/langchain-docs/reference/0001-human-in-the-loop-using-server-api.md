# Human-in-the-loop using server API
Source: https://docs.langchain.com/langsmith/add-human-in-the-loop

To review, edit, and approve tool calls in an agent or workflow, use LangGraph's [human-in-the-loop](/oss/python/langgraph/interrupts) features.

## Dynamic interrupts

<Tabs>
  <Tab title="Python">
    ```python {highlight={2,34}} theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    from langgraph_sdk import get_client
    from langgraph_sdk.schema import Command
    client = get_client(url=<DEPLOYMENT_URL>)

    # Using the graph deployed with the name "agent"
    assistant_id = "agent"

    # create a thread
    thread = await client.threads.create()
    thread_id = thread["thread_id"]

    # Run the graph until the interrupt is hit.
    result = await client.runs.wait(
        thread_id,
        assistant_id,
        input={"some_text": "original text"}   # (1)!
    )

    print(result['__interrupt__']) # (2)!
    # > [
    # >     {
    # >         'value': {'text_to_revise': 'original text'},
    # >         'resumable': True,
    # >         'ns': ['human_node:fc722478-2f21-0578-c572-d9fc4dd07c3b'],
    # >         'when': 'during'
    # >     }
    # > ]

    # Resume the graph
    print(await client.runs.wait(
        thread_id,
        assistant_id,
        command=Command(resume="Edited text")   # (3)!
    ))
    # > {'some_text': 'Edited text'}
    ```

    1. The graph is invoked with some initial state.
    2. When the graph hits the interrupt, it returns an interrupt object with the payload and metadata.
       3\. The graph is resumed with a `Command(resume=...)`, injecting the human's input and continuing execution.
  </Tab>

  <Tab title="JavaScript">
    ```javascript {highlight={32}} theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    import { Client } from "@langchain/langgraph-sdk";
    const client = new Client({ apiUrl: <DEPLOYMENT_URL> });

    // Using the graph deployed with the name "agent"
    const assistantID = "agent";

    // create a thread
    const thread = await client.threads.create();
    const threadID = thread["thread_id"];

    // Run the graph until the interrupt is hit.
    const result = await client.runs.wait(
      threadID,
      assistantID,
      { input: { "some_text": "original text" } }   # (1)!
    );

    console.log(result['__interrupt__']); # (2)!
    // > [
    # >     {
    # >         'value': {'text_to_revise': 'original text'},
    # >         'resumable': True,
    # >         'ns': ['human_node:fc722478-2f21-0578-c572-d9fc4dd07c3b'],
    # >         'when': 'during'
    # >     }
    # > ]

    // Resume the graph
    console.log(await client.runs.wait(
        threadID,
        assistantID,
        { command: { resume: "Edited text" }}   # (3)!
    ));
    # > {'some_text': 'Edited text'}
    ```

    1. The graph is invoked with some initial state.
    2. When the graph hits the interrupt, it returns an interrupt object with the payload and metadata.
    3. The graph is resumed with a `{ resume: ... }` command object, injecting the human's input and continuing execution.
  </Tab>

  <Tab title="cURL">
    Create a thread:

    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    curl --request POST \
    --url <DEPLOYMENT_URL>/threads \
    --header 'Content-Type: application/json' \
    --data '{}'
    ```

    Run the graph until the interrupt is hit.:

    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    curl --request POST \
    --url <DEPLOYMENT_URL>/threads/<THREAD_ID>/runs/wait \
    --header 'Content-Type: application/json' \
    --data "{
      \"assistant_id\": \"agent\",
      \"input\": {\"some_text\": \"original text\"}
    }"
    ```

    Resume the graph:

    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    curl --request POST \
     --url <DEPLOYMENT_URL>/threads/<THREAD_ID>/runs/wait \
     --header 'Content-Type: application/json' \
     --data "{
       \"assistant_id\": \"agent\",
       \"command\": {
         \"resume\": \"Edited text\"
       }
     }"
    ```
  </Tab>
</Tabs>

<Accordion title="Extended example: using `interrupt`">
  This is an example graph you can run in the Agent Server.
  See [LangSmith quickstart](/langsmith/deployment-quickstart) for more details.

  ```python {highlight={7,13}} theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from typing import TypedDict
  import uuid

  from langgraph.checkpoint.memory import InMemorySaver
  from langgraph.constants import START
  from langgraph.graph import StateGraph
  from langgraph.types import interrupt, Command

  class State(TypedDict):
      some_text: str

  def human_node(state: State):
      value = interrupt( # (1)!
          {
              "text_to_revise": state["some_text"] # (2)!
          }
      )
      return {
          "some_text": value # (3)!
      }

  # Build the graph
  graph_builder = StateGraph(State)
  graph_builder.add_node("human_node", human_node)
  graph_builder.add_edge(START, "human_node")

  graph = graph_builder.compile()
  ```

  1. `interrupt(...)` pauses execution at `human_node`, surfacing the given payload to a human.
  2. Any JSON serializable value can be passed to the [`interrupt`](https://reference.langchain.com/python/langgraph/types/interrupt) function. Here, a dict containing the text to revise.
  3. Once resumed, the return value of `interrupt(...)` is the human-provided input, which is used to update the state.

  Once you have a running Agent Server, you can interact with it using
  [LangGraph SDK](/langsmith/langgraph-python-sdk)

  <Tabs>
    <Tab title="Python">
      ```python {highlight={2,34}} theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      from langgraph_sdk import get_client
      from langgraph_sdk.schema import Command
      client = get_client(url=<DEPLOYMENT_URL>)

      # Using the graph deployed with the name "agent"
      assistant_id = "agent"

      # create a thread
      thread = await client.threads.create()
      thread_id = thread["thread_id"]

      # Run the graph until the interrupt is hit.
      result = await client.runs.wait(
          thread_id,
          assistant_id,
          input={"some_text": "original text"}   # (1)!
      )

      print(result['__interrupt__']) # (2)!
      # > [
      # >     {
      # >         'value': {'text_to_revise': 'original text'},
      # >         'resumable': True,
      # >         'ns': ['human_node:fc722478-2f21-0578-c572-d9fc4dd07c3b'],
      # >         'when': 'during'
      # >     }
      # > ]

      # Resume the graph
      print(await client.runs.wait(
          thread_id,
          assistant_id,
          command=Command(resume="Edited text")   # (3)!
      ))
      # > {'some_text': 'Edited text'}
      ```

      1. The graph is invoked with some initial state.
      2. When the graph hits the interrupt, it returns an interrupt object with the payload and metadata.
         3\. The graph is resumed with a `Command(resume=...)`, injecting the human's input and continuing execution.
    </Tab>

    <Tab title="JavaScript">
      ```javascript {highlight={32}} theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import { Client } from "@langchain/langgraph-sdk";
      const client = new Client({ apiUrl: <DEPLOYMENT_URL> });

      // Using the graph deployed with the name "agent"
      const assistantID = "agent";

      // create a thread
      const thread = await client.threads.create();
      const threadID = thread["thread_id"];

      // Run the graph until the interrupt is hit.
      const result = await client.runs.wait(
        threadID,
        assistantID,
        { input: { "some_text": "original text" } }   # (1)!
      );

      console.log(result['__interrupt__']); # (2)!
      # > [
      # >     {
      # >         'value': {'text_to_revise': 'original text'},
      # >         'resumable': True,
      # >         'ns': ['human_node:fc722478-2f21-0578-c572-d9fc4dd07c3b'],
      # >         'when': 'during'
      # >     }
      # > ]

      // Resume the graph
      console.log(await client.runs.wait(
          threadID,
          assistantID,
          { command: { resume: "Edited text" }}   # (3)!
      ));
      # > {'some_text': 'Edited text'}
      ```

      1. The graph is invoked with some initial state.
      2. When the graph hits the interrupt, it returns an interrupt object with the payload and metadata.
      3. The graph is resumed with a `{ resume: ... }` command object, injecting the human's input and continuing execution.
    </Tab>

    <Tab title="cURL">
      Create a thread:

      ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      curl --request POST \
      --url <DEPLOYMENT_URL>/threads \
      --header 'Content-Type: application/json' \
      --data '{}'
      ```

      Run the graph until the interrupt is hit:

      ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      curl --request POST \
      --url <DEPLOYMENT_URL>/threads/<THREAD_ID>/runs/wait \
      --header 'Content-Type: application/json' \
      --data "{
        \"assistant_id\": \"agent\",
        \"input\": {\"some_text\": \"original text\"}
      }"
      ```

      Resume the graph:

      ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      curl --request POST \
      --url <DEPLOYMENT_URL>/threads/<THREAD_ID>/runs/wait \
      --header 'Content-Type: application/json' \
      --data "{
        \"assistant_id\": \"agent\",
        \"command\": {
          \"resume\": \"Edited text\"
        }
      }"
      ```
    </Tab>
  </Tabs>
</Accordion>

## Static interrupts

Static interrupts (also known as static breakpoints) are triggered either before or after a node executes.

<Warning>
  Static interrupts are **not** recommended for human-in-the-loop workflows. They are best used for debugging and testing.
</Warning>

You can set static interrupts by specifying `interrupt_before` and `interrupt_after` at compile time:

```python {highlight={1,2,3}} theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
graph = graph_builder.compile( # (1)!
    interrupt_before=["node_a"], # (2)!
    interrupt_after=["node_b", "node_c"], # (3)!
)
```

1. The breakpoints are set during `compile` time.
2. `interrupt_before` specifies the nodes where execution should pause before the node is executed.
3. `interrupt_after` specifies the nodes where execution should pause after the node is executed.

Alternatively, you can set static interrupts at run time:

<Tabs>
  <Tab title="Python">
    ```python {highlight={1,5,6}} theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    await client.runs.wait( # (1)!
        thread_id,
        assistant_id,
        inputs=inputs,
        interrupt_before=["node_a"], # (2)!
        interrupt_after=["node_b", "node_c"] # (3)!
    )
    ```

    1. `client.runs.wait` is called with the `interrupt_before` and `interrupt_after` parameters. This is a run-time configuration and can be changed for every invocation.
    2. `interrupt_before` specifies the nodes where execution should pause before the node is executed.
    3. `interrupt_after` specifies the nodes where execution should pause after the node is executed.
  </Tab>

  <Tab title="JavaScript">
    ```javascript {highlight={1,6,7}} theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    await client.runs.wait( // (1)!
        threadID,
        assistantID,
        {
        input: input,
        interruptBefore: ["node_a"], // (2)!
        interruptAfter: ["node_b", "node_c"] // (3)!
        }
    )
    ```

    1. `client.runs.wait` is called with the `interruptBefore` and `interruptAfter` parameters. This is a run-time configuration and can be changed for every invocation.
    2. `interruptBefore` specifies the nodes where execution should pause before the node is executed.
    3. `interruptAfter` specifies the nodes where execution should pause after the node is executed.
  </Tab>

  <Tab title="cURL">
    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    curl --request POST \
    --url <DEPLOYMENT_URL>/threads/<THREAD_ID>/runs/wait \
    --header 'Content-Type: application/json' \
    --data "{
        \"assistant_id\": \"agent\",
        \"interrupt_before\": [\"node_a\"],
        \"interrupt_after\": [\"node_b\", \"node_c\"],
        \"input\": <INPUT>
    }"
    ```
  </Tab>
</Tabs>

The following example shows how to add static interrupts:

<Tabs>
  <Tab title="Python">
    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    from langgraph_sdk import get_client
    client = get_client(url=<DEPLOYMENT_URL>)

    # Using the graph deployed with the name "agent"
    assistant_id = "agent"

    # create a thread
    thread = await client.threads.create()
    thread_id = thread["thread_id"]

    # Run the graph until the breakpoint
    result = await client.runs.wait(
        thread_id,
        assistant_id,
        input=inputs   # (1)!
    )

    # Resume the graph
    await client.runs.wait(
        thread_id,
        assistant_id,
        input=None   # (2)!
    )
    ```

    1. The graph is run until the first breakpoint is hit.
    2. The graph is resumed by passing in `None` for the input. This will run the graph until the next breakpoint is hit.
  </Tab>

  <Tab title="JavaScript">
    ```js theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    import { Client } from "@langchain/langgraph-sdk";
    const client = new Client({ apiUrl: <DEPLOYMENT_URL> });

    // Using the graph deployed with the name "agent"
    const assistantID = "agent";

    // create a thread
    const thread = await client.threads.create();
    const threadID = thread["thread_id"];

    // Run the graph until the breakpoint
    const result = await client.runs.wait(
      threadID,
      assistantID,
      { input: input }   # (1)!
    );

    // Resume the graph
    await client.runs.wait(
      threadID,
      assistantID,
      { input: null }   # (2)!
    );
    ```

    1. The graph is run until the first breakpoint is hit.
    2. The graph is resumed by passing in `null` for the input. This will run the graph until the next breakpoint is hit.
  </Tab>

  <Tab title="cURL">
    Create a thread:

    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    curl --request POST \
    --url <DEPLOYMENT_URL>/threads \
    --header 'Content-Type: application/json' \
    --data '{}'
    ```

    Run the graph until the breakpoint:

    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    curl --request POST \
    --url <DEPLOYMENT_URL>/threads/<THREAD_ID>/runs/wait \
    --header 'Content-Type: application/json' \
    --data "{
      \"assistant_id\": \"agent\",
      \"input\": <INPUT>
    }"
    ```

    Resume the graph:

    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    curl --request POST \
    --url <DEPLOYMENT_URL>/threads/<THREAD_ID>/runs/wait \
    --header 'Content-Type: application/json' \
    --data "{
      \"assistant_id\": \"agent\"
    }"
    ```
  </Tab>
</Tabs>

## Learn more

* [Human-in-the-loop conceptual guide](/oss/python/langgraph/interrupts): learn more about LangGraph human-in-the-loop features.
* [Common patterns](/oss/python/langgraph/interrupts#common-patterns): learn how to implement patterns like approving/rejecting actions, requesting user input, tool call review, and validating human input.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/add-human-in-the-loop.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Add metadata and tags to traces
Source: https://docs.langchain.com/langsmith/add-metadata-tags

LangSmith supports sending arbitrary metadata and tags along with traces.

Tags are strings that can be used to categorize or label a trace. Metadata is a dictionary of key-value pairs that can be used to store additional information about a trace.

Both are useful for associating additional information with a trace, such as the environment in which it was executed, the user who initiated it, or an internal correlation ID. For more information on tags and metadata, see the [Concepts](/langsmith/observability-concepts#tags) page. For information on how to query traces and runs by metadata and tags, see the [Filter traces in the application](/langsmith/filter-traces-in-application) page.

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import openai
  import langsmith as ls
  from langsmith.wrappers import wrap_openai

  client = openai.Client()
  messages = [
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": "Hello!"}
  ]

      # You can set metadata & tags **statically** when decorating a function
      # Use the @traceable decorator with tags and metadata
      # Ensure that the LANGSMITH_TRACING environment variables are set for @traceable to work
      @ls.traceable(
          run_type="llm",
          name="OpenAI Call Decorator",
          tags=["my-tag"],
          metadata={"my-key": "my-value"}
      )
      def call_openai(
          messages: list[dict], model: str = "gpt-5.4-mini"
      ) -> str:
          # You can also dynamically set metadata on the parent run:
          rt = ls.get_current_run_tree()
          rt.metadata["some-conditional-key"] = "some-val"
          rt.tags.extend(["another-tag"])
          return client.chat.completions.create(
              model=model,
              messages=messages,
          ).choices[0].message.content

      call_openai(
          messages,
          # To add at **invocation time**, when calling the function.
          # via the langsmith_extra parameter
          langsmith_extra={"tags": ["my-other-tag"], "metadata": {"my-other-key": "my-value"}}
      )

      # or you can dynamically set default metadata for runs in the given scope
      # tracing_context doesn't create a span itself, but it does initialize the
      # context for child spans that are created.
      with ls.tracing_context(metadata={"default-key": "default-value"}):
          call_openai(messages)

      # Alternatively, you can use the trace context manager
      # This creates a new span with the given metadata and tags
      with ls.trace(
          name="OpenAI Call Trace",
          run_type="llm",
          inputs={"messages": messages},
          tags=["my-tag"],
          metadata={"my-key": "my-value"},
      ) as rt:
          chat_completion = client.chat.completions.create(
              model="gpt-5.4-mini",
              messages=messages,
          )
          rt.metadata["some-conditional-key"] = "some-val"
          rt.end(outputs={"output": chat_completion})

  # You can use the same techniques with the wrapped client
  patched_client = wrap_openai(
      client, tracing_extra={"metadata": {"my-key": "my-value"}, "tags": ["a-tag"]}
  )
  chat_completion = patched_client.chat.completions.create(
      model="gpt-5.4-mini",
      messages=messages,
      langsmith_extra={
          "tags": ["my-other-tag"],
          "metadata": {"my-other-key": "my-value"},
      },
  )
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import OpenAI from "openai";
  import { traceable, getCurrentRunTree } from "langsmith/traceable";
  import { wrapOpenAI } from "langsmith/wrappers";

      const client = wrapOpenAI(new OpenAI());
      const messages: OpenAI.Chat.ChatCompletionMessageParam[] = [
          { role: "system", content: "You are a helpful assistant." },
          { role: "user", content: "Hello!" },
      ];

      const traceableCallOpenAI = traceable(
          async (messages: OpenAI.Chat.ChatCompletionMessageParam[]) => {
              const completion = await client.chat.completions.create({
                  model: "gpt-5.4-mini",
                  messages,
              });
              const runTree = getCurrentRunTree();
              runTree.extra.metadata = {
                  ...runTree.extra.metadata,
                  someKey: "someValue",
              };
              runTree.tags = [...(runTree.tags ?? []), "runtime-tag"];
              return completion.choices[0].message.content;
          },
          {
              run_type: "llm",
              name: "OpenAI Call Traceable",
              tags: ["my-tag"],
              metadata: { "my-key": "my-value" },
          }
      );

  // Call the traceable function
  await traceableCallOpenAI(messages);
  ```
</CodeGroup>

<Tip>
  **LangSmith Deployments**: To add metadata dynamically per invocation in Agent Server deployments, we recommend using `tracing_context` in a [factory function](/langsmith/graph-rebuild). See [Customize tracing in deployed agents](/langsmith/conditional-tracing#customize-tracing-in-deployed-agents) for examples.
</Tip>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/add-metadata-tags.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Account
Source: https://docs.langchain.com/langsmith/admin

Administer your LangSmith organization, including accounts, users, access control, and platform tools.

Administer your LangSmith organization: set up accounts and API keys, organize workspaces, manage users and access control, and configure platform tools.

## Get started

<Steps>
  <Step title="Create an account" icon="user-plus">
    Sign up at [smith.langchain.com](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=snippets-langsmith-account-api-key-quickstart) (no credit card required).
    You can log in with **Google**, **GitHub**, or **email**.
  </Step>

  <Step title="Create an API key" icon="key">
    Go to your [Settings page](https://smith.langchain.com/settings) → **API Keys** → **Create API Key**.
    Copy the key and save it securely.
  </Step>
</Steps>

Once your account and API key are ready, [set up your organization](/langsmith/administration-overview).

## Explore

<CardGroup>
  <Card title="Account administration" icon="users-group" href="/langsmith/administration-overview">
    Organizations, workspaces, applications, billing, and usage.
  </Card>

  <Card title="Users & access control" icon="lock" href="/langsmith/user-management">
    Manage users, roles (RBAC), attribute-based access (ABAC), and authentication.
  </Card>

  <Card title="Tools" icon="tool" href="/langsmith/chat">
    Administrative tools and the LangSmith CLI.
  </Card>
</CardGroup>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/admin.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
