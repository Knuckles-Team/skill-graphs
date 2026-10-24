# Create a prompt
Source: https://docs.langchain.com/langsmith/create-a-prompt

In the [LangSmith UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-create-a-prompt), navigate to the **Playground** in the left-hand sidebar or from the application homepage.

<img alt="Empty playground" />

<img alt="Empty playground" />

## Compose your prompt

The left panel of the playground is an editable view of the prompt.

The prompt is made up of messages, each of which has a *role*, including:

* **System**: The "instruction manual". Use this to define the AI's persona, tone, and ground rules (e.g., "You are a helpful assistant that explains things like the weather").
* **Human**: The "user". This represents the person asking questions or providing instructions to the AI.
* **AI**: The "assistant". This is the model’s response. In the playground, you can use this to provide "few-shot" examples—showing the AI exactly how you want it to respond.
* **Tool / Function**: These roles represent the output from external tools (like a calculator or a search engine). They help you test how the AI should behave after receiving specific data.
* **Chat**: A general-purpose role, often used when importing logs or conversation history where specific labels haven't been assigned.
* **Messages List**: A dynamic placeholder. This allows you to add a variable that contains an entire list of previous messages, making it easy to manage long conversation histories.

### Template format

The default [template format](/langsmith/prompt-template-format) is f-string, but you can change the prompt template format to mustache by clicking on the dropbox below the prompt boxes.

### Add a template variable

Prompts become particularly useful when you add variables in your prompt. You can use variables to add dynamic content to your prompt. Add a template variable in one of two ways:

* Add `{variable_name}` to your prompt (with one curly brace on each side for f-string or two for mustache).

  <img alt="Variable in prompt box." />

  <img alt="Variable in prompt box." />

* Highlight text you want to templatize and click **Convert to variable** tooltip button that displays. Enter a name for your variable, and convert.

  <img alt="Double clicking on a prompt displays the variable icon." />

  <img alt="Double clicking on a prompt displays the variable icon." />

Once you've added a variable, the right panel of the playground will have an **Input** box for a sample input for the prompt variable. Fill these in with values to test the prompt.

<Callout icon="book">
  For more details on the prompt template formats generally and examples in both syntax, refer to the [Prompt template format](/langsmith/prompt-template-format) guide.
</Callout>

### Structured output

Adding an output schema to your prompt will get output in a structured format. Learn more about [structured output](/langsmith/prompt-engineering-concepts#structured-output).

### Tools

You can also add a tool by clicking the **+ Tool** button at the bottom of the prompt editor. For more information on how to use tools, refer to [Use tools](/langsmith/use-tools).

<Callout type="info" icon="feather">
  Use the **[Chat](/langsmith/chat)** in the Playground to generate tools, create output schemas, and optimize your prompts with AI assistance.
</Callout>

## Run the prompt

To run a prompt, use <Icon icon="player-play" /> **Start** at the top of the right panel in the playground.

## Save your prompt

To save your prompt, click the **Save** button and name your prompt.

The model and configuration you select in the playground settings will be saved with the prompt. When you reopen the prompt, the model and configuration will automatically load from the saved version.

<Check>
  The first time you create a public prompt, you'll be asked to set a LangChain Hub handle. All your public prompts will be linked to this handle. In a shared workspace, this handle will be set for the whole workspace.
</Check>

## View your prompts

After you've created a prompt, you can view a table of your prompts under **Prompts** in the left-hand side bar.

## Add metadata

To add metadata to your prompt, click the <Icon icon="dots-vertical" /> **More** icon on the top right-hand side of the page and then click the <Icon icon="pencil" /> **Update metadata** from the dropdown. This brings you to a page where you can add additional information about the prompt, including a description and README.

# Next steps

Now that you've created a prompt, you can use it in your application code. See [how to pull a prompt programmatically](/langsmith/manage-prompts-programmatically#pull-a-prompt).

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/create-a-prompt.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Create an account and API key
Source: https://docs.langchain.com/langsmith/create-account-api-key

To get started with LangSmith, you need to create an account. You can sign up for a free account in the [LangSmith UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-create-account-api-key). LangSmith supports sign in with Google, GitHub, and email.

## API keys

LangSmith supports two types of API keys. You can use both types of token to authenticate requests to the LangSmith API, but they have different use cases:

* [**Personal Access Tokens (PATs)**](/langsmith/administration-overview#personal-access-tokens-pats) inherit the permissions of the user who created them. Use PATs for personal scripts or tools.
* [**Service keys**](/langsmith/administration-overview#service-keys) can be scoped to specific [workspaces](/langsmith/administration-overview#workspaces) or the entire [organization](/langsmith/administration-overview#organizations). Use service keys for applications and production services.

To log traces and run evaluations with LangSmith, create an API key to authenticate your requests.

<Steps>
  <Step title="Open API Keys settings" icon="settings">
    Navigate to the [Settings page](https://smith.langchain.com/settings) and select the **API Keys** section.
  </Step>

  <Step title="Configure the key type" icon="key">
    For service keys, choose between an organization-scoped and workspace-scoped key. If the key is workspace-scoped, you must specify the workspaces.

    [Enterprise](/langsmith/pricing-plans) users can also [assign specific workspace roles](/langsmith/administration-overview#workspace-roles-rbac) to service keys, which adjusts their permissions independently of any user.
  </Step>

  <Step title="Set expiration" icon="calendar">
    Set the key's expiration. The key becomes unusable after the number of days chosen, or never, if that is selected.
  </Step>

  <Step title="Create the key" icon="circle-check">
    Click **Create API Key.** LangSmith will display the API key only once, so make sure to copy it and store it in a safe place.
  </Step>
</Steps>

<Tip>
  To delete an API key, navigate to the [Settings page](https://smith.langchain.com/settings), find the key in the **API Keys** section, and select the trash icon <Icon icon="trash" /> in the **Actions** column.
</Tip>

<Tip>
  [Enterprise](/langsmith/pricing-plans) organization admins can edit the [role](/langsmith/administration-overview#workspace-roles-rbac) on an existing service key without rotating the key. On the [Settings page](https://smith.langchain.com/settings) **API Keys** section, switch to the **Service** tab and click any service key row to open the edit dialog. Update the workspace role (and, for organization-scoped keys, the org role) and click **Save**—the key string itself is unchanged.
</Tip>

## Configure the SDK

Install the SDK for your language:

<Tabs>
  <Tab title="Python">
    <CodeGroup>
      ```bash pip theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      pip install langsmith
      ```

      ```bash uv theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      uv add langsmith
      ```
    </CodeGroup>
  </Tab>

  <Tab title="TypeScript">
    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    npm install langsmith
    ```
  </Tab>
</Tabs>

For full details, refer to the [Python SDK](/langsmith/smith-python-sdk) or [JS/TS SDK](/langsmith/smith-js-ts-sdk) reference.

Then, set your API key and enable tracing:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
export LANGSMITH_API_KEY=<your-api-key>
export LANGSMITH_TRACING=true
```

You may also need the following additional environment variables.

`LANGSMITH_ENDPOINT` controls which LangSmith server the SDK sends data to. It defaults to `https://api.smith.langchain.com` (GCP US). Set it only if you are on a different deployment. For regional SaaS, set it to the API URL for your region:

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

`LANGSMITH_WORKSPACE_ID` is required only if your API key is scoped to more than one [workspace](/langsmith/administration-overview#workspaces). Find your Workspace ID on the [Settings page](https://smith.langchain.com/settings) under **General**:

`LANGSMITH_WORKSPACE_ID=<Workspace ID>`

To reuse endpoint, API key, and workspace settings across local shells or remote runtimes, see [Profile configuration](/langsmith/profile-configuration).

## Use API keys outside of the SDK

See [instructions for managing your organization via API](/langsmith/manage-organization-by-api).

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/create-account-api-key.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# How to improve your evaluator with few-shot examples
Source: https://docs.langchain.com/langsmith/create-few-shot-evaluators

Using LLM-as-a-judge evaluators can be very helpful when you can't evaluate your system programmatically. However, their effectiveness depends on their quality and how well they align with human reviewer feedback. LangSmith provides the ability to improve the alignment of LLM-as-a-judge evaluator to human preferences using few-shot examples.

Human corrections are automatically inserted into your evaluator prompt using few-shot examples. Few-shot examples is a technique inspired by [few-shot prompting](https://www.promptingguide.ai/techniques/fewshot) that guides the models output with a few high-quality examples.

This guide covers how to set up few-shot examples as part of your LLM-as-a-judge evaluator and apply corrections to feedback scores.

## How few-shot examples work

* Few-shot examples are added to your evaluator prompt using the `{{Few-shot examples}}` variable.
* Creating an evaluator with few-shot examples, will automatically create a dataset for you, which will be auto-populated with few-shot examples once you start making corrections.
* At runtime, these examples will be inserted into the evaluator to serve as a guide for its outputs. This will help the evaluator to better align with human preferences.

## Configure your evaluator

<Note>
  Few-shot examples are not currently supported in LLM-as-a-judge evaluators that use the prompt hub and are only compatible with prompts that use mustache formatting.

  Few-shot examples are only supported for run-level evaluators, not thread-level. Toggle on **Runs** in the [**Configure Evaluator** panel](/langsmith/evaluators#edit-an-evaluator).
</Note>

Before enabling few-shot examples, set up your LLM-as-a-judge evaluator. If you haven't done this yet, follow the steps in the [LLM-as-a-judge evaluator guide](/langsmith/llm-as-judge).

### 1. Configure variable mapping

Each few-shot example is formatted according to the variable mapping specified in the configuration. The variable mapping for few-shot examples, should contain the same variables as your main prompt, plus a `few_shot_explanation` and a `score` variable which should have the same name as your feedback key.

For example, if your main prompt has variables `question` and `response`, and your evaluator outputs a `correctness` score, then your few-shot prompt should have the variables `question`, `response`, `few_shot_explanation`, and `correctness`.

### 2. Specify the number of few-shot examples to use

You may also specify the number of few-shot examples to use. The default is 5. If your examples are very long, you may want to set this number lower to save tokens - whereas if your examples tend to be short, you can set a higher number in order to give your evaluator more examples to learn from. If you have more examples in your dataset than this number, we will randomly choose them for you.

## Make corrections

<Info>
  [Audit evaluator scores](/langsmith/audit-evaluator-scores)
</Info>

As you start logging traces or running experiments, you will likely disagree with some of the scores that your evaluator has given. When you [make corrections to these scores](/langsmith/audit-evaluator-scores), you will begin seeing examples populated inside your corrections dataset. As you make corrections, make sure to attach explanations - these will get populated into your evaluator prompt in place of the `few_shot_explanation` variable.

The inputs to the few-shot examples will be the relevant fields from the inputs, outputs, and reference (if this an offline evaluator) of your chain/dataset. The outputs will be the corrected evaluator score and the explanations that you created when you left the corrections. Feel free to edit these to your liking. Here is an example of a few-shot example in a corrections dataset:

<img alt="Few-shot example" />

Note that the corrections may take a minute or two to be populated into your few-shot dataset. Once they are there, future runs of your evaluator will include them in the prompt!

## View your corrections dataset

In order to view your corrections dataset:

* **Online evaluators**: Select your run rule and click **Edit Rule**
* **Offline evaluators**: Select your evaluator and click **Edit Evaluator**

<img alt="Edit Evaluator" />

Head to your dataset of corrections linked in the **Improve evaluator accuracy using few-shot examples** section. You can view and update your few-shot examples in the dataset.

<img alt="View few-shot dataset" />

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/create-few-shot-evaluators.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Use cron jobs
Source: https://docs.langchain.com/langsmith/cron-jobs

There are many situations in which it is useful to run an assistant on a schedule.

For example, say that you're building an assistant that runs daily and sends an email summary
of the day's news. You could use a cron job to run the assistant every day at 8:00 PM.

LangSmith Deployment supports cron jobs, which run on a user-defined schedule. The user specifies a schedule, an assistant, and some input. After that, on the specified schedule, the server will:

* Create a new thread with the specified assistant
* Send the specified input to that thread

Note that this sends the same input to the thread every time.

The LangSmith Deployment API provides several endpoints for creating and managing cron jobs. See the [API reference](https://langchain-ai.github.io/langgraph/cloud/reference/api/api_ref/) for more details.

Sometimes you don't want to run your graph based on user interaction, but rather you would like to schedule your graph to run on a schedule - for example if you wish for your graph to compose and send out a weekly email of to-dos for your team. LangSmith Deployment allows you to do this without having to write your own script by using the `Crons` client. To schedule a graph job, you need to pass a [cron expression](https://crontab.cronhub.io/) to inform the client when you want to run the graph. `Cron` jobs are run in the background and do not interfere with normal invocations of the graph.

<Note>
  All cron schedules are interpreted in **UTC**. Make sure to convert your desired execution time to UTC when specifying the schedule.
</Note>

## Setup

First, let's set up our SDK client, assistant, and thread:

<Tabs>
  <Tab title="Python">
    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    from langgraph_sdk import get_client

    client = get_client(url=<DEPLOYMENT_URL>)
    # Using the graph deployed with the name "agent"
    assistant_id = "agent"
    # create thread
    thread = await client.threads.create()
    print(thread)
    ```
  </Tab>

  <Tab title="Javascript">
    ```js theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    import { Client } from "@langchain/langgraph-sdk";

    const client = new Client({ apiUrl: <DEPLOYMENT_URL> });
    // Using the graph deployed with the name "agent"
    const assistantId = "agent";
    // create thread
    const thread = await client.threads.create();
    console.log(thread);
    ```
  </Tab>

  <Tab title="CURL">
    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    curl --request POST \
        --url <DEPLOYMENT_URL>/assistants/search \
        --header 'Content-Type: application/json' \
        --data '{
            "limit": 10,
            "offset": 0
        }' | jq -c 'map(select(.config == null or .config == {})) | .[0].graph_id' && \
    curl --request POST \
        --url <DEPLOYMENT_URL>/threads \
        --header 'Content-Type: application/json' \
        --data '{}'
    ```
  </Tab>
</Tabs>

Output:

```
{
'thread_id': '9dde5490-2b67-47c8-aa14-4bfec88af217',
'created_at': '2024-08-30T23:07:38.242730+00:00',
'updated_at': '2024-08-30T23:07:38.242730+00:00',
'metadata': {},
'status': 'idle',
'config': {},
'values': None
}
```

## Cron job on a thread

To create a cron job associated with a specific thread, you can write:

<Tabs>
  <Tab title="Python">
    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    # This schedules a job to run at 15:27 (3:27PM) UTC every day
    cron_job = await client.crons.create_for_thread(
        thread["thread_id"],
        assistant_id,
        schedule="27 15 * * *",
        input={"messages": [{"role": "user", "content": "What time is it?"}]},
    )
    ```
  </Tab>

  <Tab title="Javascript">
    ```js theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    // This schedules a job to run at 15:27 (3:27PM) UTC every day
    const cronJob = await client.crons.create_for_thread(
      thread["thread_id"],
      assistantId,
      {
        schedule: "27 15 * * *",
        input: { messages: [{ role: "user", content: "What time is it?" }] }
      }
    );
    ```
  </Tab>

  <Tab title="CURL">
    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    curl --request POST \
        --url <DEPLOYMENT_URL>/threads/<THREAD_ID>/runs/crons \
        --header 'Content-Type: application/json' \
        --data '{
            "assistant_id": <ASSISTANT_ID>,
        }'
    ```
  </Tab>
</Tabs>

Note that it is **very** important to delete `Cron` jobs that are no longer useful. Otherwise you could rack up unwanted API charges to the LLM! You can delete a `Cron` job using the following code:

<Tabs>
  <Tab title="Python">
    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    await client.crons.delete(cron_job["cron_id"])
    ```
  </Tab>

  <Tab title="Javascript">
    ```js theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    await client.crons.delete(cronJob["cron_id"]);
    ```
  </Tab>

  <Tab title="CURL">
    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    curl --request DELETE \
        --url <DEPLOYMENT_URL>/runs/crons/<CRON_ID>
    ```
  </Tab>
</Tabs>

## Cron job stateless

You can also create stateless cron jobs by using the following code. Stateless cron jobs create a new thread for each execution:

<Tabs>
  <Tab title="Python">
    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    # This schedules a job to run at 15:27 (3:27PM) UTC every day
    cron_job_stateless = await client.crons.create(
        assistant_id,
        schedule="27 15 * * *",
        input={"messages": [{"role": "user", "content": "What time is it?"}]},
    )
    ```
  </Tab>

  <Tab title="Javascript">
    ```js theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    // This schedules a job to run at 15:27 (3:27PM) UTC every day
    const cronJobStateless = await client.crons.create(
      assistantId,
      {
        schedule: "27 15 * * *",
        input: { messages: [{ role: "user", content: "What time is it?" }] }
      }
    );
    ```
  </Tab>

  <Tab title="CURL">
    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    curl --request POST \
        --url <DEPLOYMENT_URL>/runs/crons \
        --header 'Content-Type: application/json' \
        --data '{
            "assistant_id": <ASSISTANT_ID>,
        }'
    ```
  </Tab>
</Tabs>

Again, remember to delete your job once you are done with it!

<Tabs>
  <Tab title="Python">
    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    await client.crons.delete(cron_job_stateless["cron_id"])
    ```
  </Tab>

  <Tab title="Javascript">
    ```js theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    await client.crons.delete(cronJobStateless["cron_id"]);
    ```
  </Tab>

  <Tab title="CURL">
    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    curl --request DELETE \
        --url <DEPLOYMENT_URL>/runs/crons/<CRON_ID>
    ```
  </Tab>
</Tabs>

## Thread cleanup for stateless crons

<Note>
  This feature requires LangGraph API version **0.5.18** or later and Python SDK **0.3.2** or later, or JavaScript SDK **1.4.0** or later.
</Note>

Every time a stateless cron is triggered, a new thread is created. Control what happens to that thread after the run completes using the `on_run_completed` parameter:

* **`"delete"`** (default): Automatically deletes the thread after the run completes.
* **`"keep"`**: Preserves the thread for later retrieval. You are responsible for cleaning up these threads. See [how to add TTLs to your application](/langsmith/configure-ttl) for the recommended approach.

### Example: Keeping threads for later retrieval

<Tabs>
  <Tab title="Python">
    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    # Create a stateless cron that keeps threads after execution.
    # Configure checkpointer.ttl in langgraph.json to auto-delete old threads.
    # See: https://docs.langchain.com/langsmith/configure-ttl
    cron_job = await client.crons.create(
        assistant_id,
        schedule="27 15 * * *",
        input={"messages": [{"role": "user", "content": "Daily report"}]},
        on_run_completed="keep"
    )

    # You can later retrieve the runs and their results
    runs = await client.runs.search(
        metadata={"cron_id": cron_job["cron_id"]}
    )
    ```
  </Tab>

  <Tab title="Javascript">
    ```js theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    // Create a stateless cron that keeps threads after execution.
    // Configure checkpointer.ttl in langgraph.json to auto-delete old threads.
    // See: https://docs.langchain.com/langsmith/configure-ttl
    const cronJob = await client.crons.create(
      assistantId,
      {
        schedule: "27 15 * * *",
        input: { messages: [{ role: "user", content: "Daily report" }] },
        onRunCompleted: "keep"
      }
    );

    // You can later retrieve the runs and their results
    const runs = await client.runs.search({
      metadata: { cron_id: cronJob["cron_id"] }
    });
    ```
  </Tab>

  <Tab title="CURL">
    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    # Create a stateless cron that keeps threads after execution.
    # Configure checkpointer.ttl in langgraph.json to auto-delete old threads.
    # See: https://docs.langchain.com/langsmith/configure-ttl
    curl --request POST \
        --url <DEPLOYMENT_URL>/runs/crons \
        --header 'Content-Type: application/json' \
        --data '{
            "assistant_id": "<ASSISTANT_ID>",
            "schedule": "27 15 * * *",
            "input": {"messages": [{"role": "user", "content": "Daily report"}]},
            "on_run_completed": "keep"
        }'
    ```
  </Tab>
</Tabs>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/cron-jobs.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Add custom authentication
Source: https://docs.langchain.com/langsmith/custom-auth

This guide shows you how to add custom authentication to your LangSmith application. The steps on this page apply to both [cloud](/langsmith/cloud) and [self-hosted](/langsmith/self-hosted) deployments. It does not apply to isolated usage of the [LangGraph open source library](/oss/python/langgraph/overview) in your own custom server.

## Add custom authentication to your deployment

To leverage custom authentication and access user-level metadata in your deployments, set up custom authentication to automatically populate the `config["configurable"]["langgraph_auth_user"]` object through a custom authentication handler. You can then access this object in your graph with the `langgraph_auth_user` key to [allow an agent to perform authenticated actions on behalf of the user](#enable-agent-authentication).

1. Implement authentication:

   <Note>
     Without a custom `@auth.authenticate` handler, LangGraph sees only the API-key owner (usually the developer), so requests aren’t scoped to individual end-users. To propagate custom tokens, you must implement your own handler.
   </Note>

   ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
   from langgraph_sdk import Auth
   import requests

   auth = Auth()

   def is_valid_key(api_key: str) -> bool:
       is_valid = # your API key validation logic
       return is_valid

   @auth.authenticate # (1)!
   async def authenticate(headers: dict) -> Auth.types.MinimalUserDict:
       api_key = headers.get(b"x-api-key")
       if not api_key or not is_valid_key(api_key):
           raise Auth.exceptions.HTTPException(status_code=401, detail="Invalid API key")

       # Fetch user-specific tokens from your secret store
       user_tokens = await fetch_user_tokens(api_key)

       return { # (2)!
           "identity": api_key,  #  fetch user ID from LangSmith
           "github_token" : user_tokens.github_token
           "jira_token" : user_tokens.jira_token
           # ... custom fields/secrets here
       }
   ```

* This handler receives the request (headers, etc.), validates the user, and returns a dictionary with at least an identity field.
* You can add any custom fields you want (e.g., OAuth tokens, roles, org IDs, etc.).

2. In your [`langgraph.json`](/langsmith/application-structure#configuration-file), add the path to your auth file:

   ```json highlight={7-9} theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
   {
       "dependencies": ["."],
       "graphs": {
       "agent": "./agent.py:graph"
       },
       "env": ".env",
       "auth": {
           "path": "./auth.py:my_auth"
       }
   }
   ```
3. Once you've set up authentication in your server, requests must include the required authorization information based on your chosen scheme. Assuming you are using JWT token authentication, you could access your deployments using any of the following methods:

   <Tabs>
     <Tab title="Python Client">
       ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
       from langgraph_sdk import get_client

       my_token = "your-token" # In practice, you would generate a signed token with your auth provider
       client = get_client(
           url="http://localhost:2024",
           headers={"Authorization": f"Bearer {my_token}"}
       )
       threads = await client.threads.search()
       ```
     </Tab>

     <Tab title="Python RemoteGraph">
       ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
       from langgraph.pregel.remote import RemoteGraph

       my_token = "your-token" # In practice, you would generate a signed token with your auth provider
       remote-graph = RemoteGraph(
           "agent",
           url="http://localhost:2024",
           headers={"Authorization": f"Bearer {my_token}"}
       )
       threads = await remote-graph.ainvoke(...)
       ```
     </Tab>

     <Tab title="JavaScript Client">
       ```javascript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
       import { Client } from "@langchain/langgraph-sdk";

       const my_token = "your-token"; // In practice, you would generate a signed token with your auth provider
       const client = new Client({
       apiUrl: "http://localhost:2024",
       defaultHeaders: { Authorization: `Bearer ${my_token}` },
       });
       const threads = await client.threads.search();
       ```
     </Tab>

     <Tab title="JavaScript RemoteGraph">
       ```javascript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
       import { RemoteGraph } from "@langchain/langgraph/remote";

       const my_token = "your-token"; // In practice, you would generate a signed token with your auth provider
       const remoteGraph = new RemoteGraph({
       graphId: "agent",
       url: "http://localhost:2024",
       headers: { Authorization: `Bearer ${my_token}` },
       });
       const threads = await remoteGraph.invoke(...);
       ```
     </Tab>

     <Tab title="CURL">
       ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
       curl -H "Authorization: Bearer ${your-token}" http://localhost:2024/threads
       ```
     </Tab>
   </Tabs>

   For more details on RemoteGraph, refer to the [Use RemoteGraph](/langsmith/use-remote-graph) guide.

## Enable agent authentication

After [authentication](#add-custom-authentication-to-your-deployment), the platform creates a special configuration object (`config`) that is passed to LangSmith deployment. This object contains information about the current user, including any custom fields you return from your `@auth.authenticate` handler.

To allow an agent to perform authenticated actions on behalf of the user, access this object in your graph with the `langgraph_auth_user` key:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
def my_node(state, config):
    user_config = config["configurable"].get("langgraph_auth_user")
    # token was resolved during the @auth.authenticate function
    token = user_config.get("github_token","")
    ...
```

<Note>
  Fetch user credentials from a secure secret store. Storing secrets in graph state is not recommended.
</Note>

### Authorizing a user for Studio

By default, if you add custom authorization on your resources, this will also apply to interactions made from [Studio](/langsmith/studio). If you want, you can handle logged-in Studio users differently by checking [is\_studio\_user()](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/#langgraph_sdk.auth.types.StudioUser).

<Note>
  `is_studio_user` was added in version 0.1.73 of the langgraph-sdk. If you're on an older version, you can still check whether `isinstance(ctx.user, StudioUser)`.
</Note>

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langgraph_sdk.auth import is_studio_user, Auth
auth = Auth()

# ... Setup authenticate, etc.

@auth.on
async def add_owner(
    ctx: Auth.types.AuthContext,
    value: dict  # The payload being sent to this access method
) -> dict:  # Returns a filter dict that restricts access to resources
    if is_studio_user(ctx.user):
        return {}

    filters = {"owner": ctx.user.identity}
    metadata = value.setdefault("metadata", {})
    metadata.update(filters)
    return filters
```

Only use this if you want to permit developer access to a graph deployed on the managed LangSmith SaaS.

## Learn more

* [Authentication & Access Control](/langsmith/auth)
* [Setting up custom authentication tutorial](/langsmith/set-up-custom-auth)

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/custom-auth.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# How to use a custom checkpointer
Source: https://docs.langchain.com/langsmith/custom-checkpointer

Replace the built-in Postgres checkpointer with a custom BaseCheckpointSaver implementation in your agent deployment.

When deploying agents to LangSmith, the server provides a built-in Postgres-backed checkpointer that handles state persistence across graph runs. You can replace this with your own [BaseCheckpointSaver](https://reference.langchain.com/python/langgraph/checkpoints/#langgraph.checkpoint.base.BaseCheckpointSaver) implementation to use a different storage backend.

You provide a path to an async context manager that yields a `BaseCheckpointSaver` instance, and the server manages its lifecycle automatically.

<Warning>
  Custom checkpointers are in **alpha**. This feature may experience breaking changes in minor version updates.
</Warning>

<Tip>
  To use MongoDB instead of PostgreSQL for checkpoint storage, see [Configure checkpointer backend](/langsmith/configure-checkpointer). This page is for implementing a fully custom storage backend.
</Tip>

## Define the checkpointer

Starting from an **existing** LangSmith application, create a file that defines an async context manager yielding your custom checkpointer. If you are beginning a new project, you can create an app from a template using the CLI.

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
langgraph new --template=new-langgraph-project-python my_new_project
```

The async context manager pattern lets the server open and close the database connection at the right points in the application lifecycle:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}

# ./src/agent/checkpointer.py
import contextlib

class MyCheckpointer(BaseCheckpointSaver):
    def __init__(self):
        super().__init__()
        # Initialize your custom checkpointer here
    ...

    @contextlib.asynccontextmanager
    async def aget(self, config: RunnableConfig):
        # Your custom logic to create a connection pool and initialize your checkpointer here.
        yield

@contextlib.asynccontextmanager
async def generate_checkpointer():
    """Yield a BaseCheckpointSaver, open for the duration of the server."""
    async with AsyncSqliteSaver.from_conn_string("./checkpoints.db") as saver:
        await saver.setup()
        yield saver
```

## Test against the conformance suite

Most open source checkpointer implementations do not yet implement all the operations required by Agent Server. Before configuring your checkpointer, validate it against the conformance test suite to ensure compatibility.

Install the package:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
pip install langgraph-checkpoint-conformance
```

Register your checkpointer and run validation:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import asyncio

from langgraph.checkpoint.conformance import checkpointer_test, validate

@checkpointer_test(name="MyCheckpointer")
async def my_checkpointer():
    async with MyCheckpointer(...) as saver:
        yield saver

async def main():
    report = await validate(my_checkpointer)
    report.print_report()
    assert report.passed_all_base()

asyncio.run(main())
```

The suite auto-detects which extended capabilities your checkpointer implements and runs the appropriate tests. You can also run it as a pytest test:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import pytest

from langgraph.checkpoint.conformance import checkpointer_test, validate

@checkpointer_test(name="MyCheckpointer")
async def my_checkpointer():
    async with MyCheckpointer(...) as saver:
        yield saver

@pytest.mark.asyncio
async def test_conformance():
    report = await validate(my_checkpointer)
    report.print_report()
    assert report.passed_all_base()
```

To view the full list of base and extended operations that the suite validates, refer to the [capabilities](#capabilities) section.

## Configure `langgraph.json`

Add the `checkpointer` key to your [`langgraph.json` configuration file](/langsmith/application-structure#configuration-file-concepts). The `path` points to the async context manager you [defined earlier](#define-the-checkpointer).

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "dependencies": ["."],
  "graphs": {
    "agent": "./src/agent/graph.py:graph"
  },
  "env": ".env",
  "checkpointer": {
    "path": "./src/agent/checkpointer.py:generate_checkpointer"
  }
}
```

## Start server

Test the server out locally:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
langgraph dev --no-browser
```

The server logs will confirm that your custom checkpointer is active.

## Capabilities

The server checks your checkpointer for **base** (required) and **extended** (optional) capabilities at startup. If an extended capability is missing, the server either uses a fallback or disables the corresponding feature.

### Base capabilities (required)

| Method           | Description           |
| ---------------- | --------------------- |
| `aput`           | Store a checkpoint    |
| `aput_writes`    | Store pending writes  |
| `aget_tuple`     | Retrieve a checkpoint |
| `alist`          | List checkpoints      |
| `adelete_thread` | Delete a thread       |

### Extended capabilities (optional)

| Method             | Description                          | Fallback if missing                               |
| ------------------ | ------------------------------------ | ------------------------------------------------- |
| `adelete_for_runs` | Delete checkpoints for specific runs | Rollback multitask strategy unavailable           |
| `acopy_thread`     | Copy a thread                        | Slow fallback (re-inserts checkpoints one by one) |
| `aprune`           | Prune thread history                 | Thread history pruning unavailable                |

## Deploying

You can deploy this app as-is to LangSmith or to your self-hosted platform.

## Next steps

* [Build a custom checkpointer](/oss/python/langgraph/checkpointers#build-a-custom-checkpointer) including delta channel support.
* [Use a custom store](/langsmith/custom-store) to replace the built-in long-term memory store.
* Learn about [persistence and memory](/oss/python/langgraph/persistence) in LangGraph.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/custom-checkpointer.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# How to customize the Dockerfile
Source: https://docs.langchain.com/langsmith/custom-docker

Users can add an array of additional lines to add to the Dockerfile following the import from the parent LangGraph image. In order to do this, you simply need to modify your `langgraph.json` file by passing in the commands you want run to the `dockerfile_lines` key. For example, if we wanted to use `Pillow` in our graph you would need to add the following dependencies:

```
{
    "dependencies": ["."],
    "graphs": {
        "openai_agent": "./openai_agent.py:agent",
    },
    "env": "./.env",
    "dockerfile_lines": [
        "RUN apt-get update && apt-get install -y libjpeg-dev zlib1g-dev libpng-dev",
        "RUN pip install Pillow"
    ]
}
```

This would install the system packages required to use Pillow if we were working with `jpeg` or `png` image formats.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/custom-docker.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Connect to a custom model
Source: https://docs.langchain.com/langsmith/custom-endpoint

The Playground allows you to use your own custom models. You can deploy a model server that exposes your model's API via [LangServe](https://github.com/langchain-ai/langserve), an open source library for serving LangChain applications. Behind the scenes, the Playground will interact with your model server to generate responses.

## Deploy a custom model server

For your convenience, we have provided a [sample model server](https://github.com/langchain-ai/langsmith-model-server) that you can use as a reference. We highly recommend using the sample model server as a starting point.

Depending on your model is an instruct-style or chat-style model, you will need to implement either `custom_model.py` or `custom_chat_model.py` respectively.

## Adding configurable fields

It is often useful to configure your model with different parameters. These might include temperature, model\_name, max\_tokens, etc.

To make your model configurable in the Playground, you need to add configurable fields to your model server. These fields can be used to change model parameters from the Playground.

You can add configurable fields by implementing the `with_configurable_fields` function in the `config.py` file. You can

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
def with_configurable_fields(self) -> Runnable:
    """Expose fields you want to be configurable in the Playground. We will automatically expose these to the
    Playground. If you don't want to expose any fields, you can remove this method."""
    return self.configurable_fields(n=ConfigurableField(
        id="n",
        name="Num Characters",
        description="Number of characters to return from the input prompt.",
    ))
```

## Use the model in the Playground

Once you have deployed a model server, you can use it in the Playground. Enter the Playground and select either the `ChatCustomModel` or the `CustomModel` provider for chat-style model or instruct-style models.

Enter the `URL`. The Playground will automatically detect the available endpoints and configurable fields. You can then invoke the model with the desired parameters.

<img alt="ChatCustomModel in Playground" />

If everything is set up correctly, you should see the model's response in the Playground as well as the configurable fields specified in the `with_configurable_fields`.

For more information, see [how to store your model configuration for later use](/langsmith/managing-model-configurations).

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/custom-endpoint.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# How to add custom lifespan events
Source: https://docs.langchain.com/langsmith/custom-lifespan

When deploying agents to LangSmith, you often need to initialize resources like database connections when your server starts up, and ensure they're properly closed when it shuts down. Lifespan events let you hook into your server's startup and shutdown sequence to handle these critical setup and teardown tasks.

This works the same way as [adding custom routes](/langsmith/custom-routes). You just need to provide your own [`Starlette`](https://www.starlette.io/applications/) app (including [`FastAPI`](https://fastapi.tiangolo.com/), [`FastHTML`](https://fastht.ml/) and other compatible apps).

Below is an example using FastAPI.

<Note>
  "Python only"
  We currently only support custom lifespan events in Python deployments with `langgraph-api>=0.0.26`.
</Note>

## Create app

Starting from an **existing** LangSmith application, add the following lifespan code to your `webapp.py` file. If you are starting from scratch, you can create a new app from a template using the CLI.

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
langgraph new --template=new-langgraph-project-python my_new_project
```

Once you have a LangGraph project, add the following app code:

```python {highlight={19}} theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}

# ./src/agent/webapp.py
from contextlib import asynccontextmanager
from fastapi import FastAPI
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

@asynccontextmanager
async def lifespan(app: FastAPI):
    # for example...
    engine = create_async_engine("postgresql+asyncpg://user:pass@localhost/db")
    # Create reusable session factory
    async_session = sessionmaker(engine, class_=AsyncSession)
    # Store in app state
    app.state.db_session = async_session
    yield
    # Clean up connections
    await engine.dispose()

app = FastAPI(lifespan=lifespan)
