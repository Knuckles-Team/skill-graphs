# Keep our test users from the previous tutorial
VALID_TOKENS = {
    "user1-token": {"id": "user1", "name": "Alice"},
    "user2-token": {"id": "user2", "name": "Bob"},
}

auth = Auth()

@auth.authenticate
async def get_current_user(authorization: str | None) -> Auth.types.MinimalUserDict:
    """Our authentication handler from the previous tutorial."""
    assert authorization
    scheme, token = authorization.split()
    assert scheme.lower() == "bearer"

    if token not in VALID_TOKENS:
        raise Auth.exceptions.HTTPException(status_code=401, detail="Invalid token")

    user_data = VALID_TOKENS[token]
    return {
        "identity": user_data["id"],
    }

@auth.on
async def add_owner(
    ctx: Auth.types.AuthContext,  # Contains info about the current user
    value: dict,  # The resource being created/accessed
):
    """Make resources private to their creator."""
    # Examples:
    # ctx: AuthContext(
    #     permissions=[],
    #     user=ProxyUser(
    #         identity='user1',
    #         is_authenticated=True,
    #         display_name='user1'
    #     ),
    #     resource='threads',
    #     action='create_run'
    # )
    # value:
    # {
    #     'thread_id': UUID('1e1b2733-303f-4dcd-9620-02d370287d72'),
    #     'assistant_id': UUID('fe096781-5601-53d2-b2f6-0d3403f7e9ca'),
    #     'run_id': UUID('1efbe268-1627-66d4-aa8d-b956b0f02a41'),
    #     'status': 'pending',
    #     'metadata': {},
    #     'prevent_insert_if_inflight': True,
    #     'multitask_strategy': 'reject',
    #     'if_not_exists': 'reject',
    #     'after_seconds': 0,
    #     'kwargs': {
    #         'input': {'messages': [{'role': 'user', 'content': 'Hello!'}]},
    #         'command': None,
    #         'config': {
    #             'configurable': {
    #                 'langgraph_auth_user': ... Your user object...
    #                 'langgraph_auth_user_id': 'user1'
    #             }
    #         },
    #         'stream_mode': ['values'],
    #         'interrupt_before': None,
    #         'interrupt_after': None,
    #         'webhook': None,
    #         'feedback_keys': None,
    #         'temporary': False,
    #         'subgraphs': False
    #     }
    # }

    # Does 2 things:
    # 1. Add the user's ID to the resource's metadata. Each LangGraph resource has a `metadata` dict that persists with the resource.
    # this metadata is useful for filtering in read and update operations
    # 2. Return a filter that lets users only see their own resources
    filters = {"owner": ctx.user.identity}
    metadata = value.setdefault("metadata", {})
    metadata.update(filters)

    # Only let users see their own resources
    return filters
```

The handler receives two parameters:

1. `ctx` ([AuthContext](https://reference.langchain.com/python/langgraph-sdk/auth/types/AuthContext)): contains info about the current `user`, the user's `permissions`, the `resource` ("threads", "crons", "assistants"), and the `action` being taken ("create", "read", "update", "delete", "search", "create\_run")
2. `value` (`dict`): data that is being created or accessed. The contents of this dict depend on the resource and action being accessed. See [adding scoped authorization handlers](#scoped-authorization) below for information on how to get more tightly scoped access control.

Notice that the simple handler does two things:

1. Adds the user's ID to the resource's metadata.
2. Returns a metadata filter so users only see resources they own.

## 2. Test private conversations

Test your authorization. If you have set things up correctly, you will see all ✅ messages. Be sure to have your development server running (run `langgraph dev`):

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langgraph_sdk import get_client

# Create clients for both users
alice = get_client(
    url="http://localhost:2024",
    headers={"Authorization": "Bearer user1-token"}
)

bob = get_client(
    url="http://localhost:2024",
    headers={"Authorization": "Bearer user2-token"}
)

# Alice creates an assistant
alice_assistant = await alice.assistants.create()
print(f"✅ Alice created assistant: {alice_assistant['assistant_id']}")

# Alice creates a thread and chats
alice_thread = await alice.threads.create()
print(f"✅ Alice created thread: {alice_thread['thread_id']}")

await alice.runs.create(
    thread_id=alice_thread["thread_id"],
    assistant_id="agent",
    input={"messages": [{"role": "user", "content": "Hi, this is Alice's private chat"}]}
)

# Bob tries to access Alice's thread
try:
    await bob.threads.get(alice_thread["thread_id"])
    print("❌ Bob shouldn't see Alice's thread!")
except Exception as e:
    print("✅ Bob correctly denied access:", e)

# Bob creates his own thread
bob_thread = await bob.threads.create()
await bob.runs.create(
    thread_id=bob_thread["thread_id"],
    assistant_id="agent",
    input={"messages": [{"role": "user", "content": "Hi, this is Bob's private chat"}]}
)
print(f"✅ Bob created his own thread: {bob_thread['thread_id']}")

# List threads - each user only sees their own
alice_threads = await alice.threads.search()
bob_threads = await bob.threads.search()
print(f"✅ Alice sees {len(alice_threads)} thread")
print(f"✅ Bob sees {len(bob_threads)} thread")
```

Output:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
✅ Alice created assistant: fc50fb08-78da-45a9-93cc-1d3928a3fc37
✅ Alice created thread: 533179b7-05bc-4d48-b47a-a83cbdb5781d
✅ Bob correctly denied access: Client error '404 Not Found' for url 'http://localhost:2024/threads/533179b7-05bc-4d48-b47a-a83cbdb5781d'
For more information check: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/404
✅ Bob created his own thread: 437c36ed-dd45-4a1e-b484-28ba6eca8819
✅ Alice sees 1 thread
✅ Bob sees 1 thread
```

This means:

1. Each user can create and chat in their own threads
2. Users can't see each other's threads
3. Listing threads only shows your own

<a />

## 3. Add scoped authorization handlers

The broad `@auth.on` handler matches on all [authorization events](/langsmith/auth#supported-resources). This is concise, but it means the contents of the `value` dict are not well-scoped, and the same user-level access control is applied to every resource. If you want to be more fine-grained, you can also control specific actions on resources.

Update `src/security/auth.py` to add handlers for specific resource types:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}

# Keep our previous handlers...

from langgraph_sdk import Auth

@auth.on.threads.create
async def on_thread_create(
    ctx: Auth.types.AuthContext,
    value: Auth.types.on.threads.create.value,
):
    """Add owner when creating threads.

    This handler runs when creating new threads and does two things:
    1. Sets metadata on the thread being created to track ownership
    2. Returns a filter that ensures only the creator can access it
    """
    # Example value:
    #  {'thread_id': UUID('99b045bc-b90b-41a8-b882-dabc541cf740'), 'metadata': {}, 'if_exists': 'raise'}

    # Add owner metadata to the thread being created
    # This metadata is stored with the thread and persists
    metadata = value.setdefault("metadata", {})
    metadata["owner"] = ctx.user.identity

    # Return filter to restrict access to just the creator
    return {"owner": ctx.user.identity}

@auth.on.threads.read
async def on_thread_read(
    ctx: Auth.types.AuthContext,
    value: Auth.types.on.threads.read.value,
):
    """Only let users read their own threads.

    This handler runs on read operations. We don't need to set
    metadata since the thread already exists - we just need to
    return a filter to ensure users can only see their own threads.
    """
    return {"owner": ctx.user.identity}

@auth.on.assistants
async def on_assistants(
    ctx: Auth.types.AuthContext,
    value: Auth.types.on.assistants.value,
):
    # For illustration purposes, we will deny all requests
    # that touch the assistants resource
    # Example value:
    # {
    #     'assistant_id': UUID('63ba56c3-b074-4212-96e2-cc333bbc4eb4'),
    #     'graph_id': 'agent',
    #     'config': {},
    #     'metadata': {},
    #     'name': 'Untitled'
    # }
    raise Auth.exceptions.HTTPException(
        status_code=403,
        detail="User lacks the required permissions.",
    )

# Assumes you organize information in store like (user_id, resource_type, resource_id)
@auth.on.store()
async def authorize_store(ctx: Auth.types.AuthContext, value: dict):
    # The "namespace" field for each store item is a tuple you can think of as the directory of an item.
    namespace: tuple = value["namespace"]
    assert namespace[0] == ctx.user.identity, "Not authorized"
```

Notice that instead of one global handler, you now have specific handlers for:

1. Creating threads
2. Reading threads
3. Accessing assistants

The first three of these match specific **actions** on each resource (see [resource actions](/langsmith/auth#resource-specific-handlers)), while the last one (`@auth.on.assistants`) matches *any* action on the `assistants` resource. For each request, LangGraph will run the most specific handler that matches the resource and action being accessed. This means that the four handlers above will run rather than the broadly scoped "`@auth.on`" handler.

Try adding the following test code to your test file:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}

# ... Same as before

# Try creating an assistant. This should fail
try:
    await alice.assistants.create("agent")
    print("❌ Alice shouldn't be able to create assistants!")
except Exception as e:
    print("✅ Alice correctly denied access:", e)

# Try searching for assistants. This also should fail
try:
    await alice.assistants.search()
    print("❌ Alice shouldn't be able to search assistants!")
except Exception as e:
    print("✅ Alice correctly denied access to searching assistants:", e)

# Alice can still create threads
alice_thread = await alice.threads.create()
print(f"✅ Alice created thread: {alice_thread['thread_id']}")
```

Output:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
✅ Alice created thread: dcea5cd8-eb70-4a01-a4b6-643b14e8f754
✅ Bob correctly denied access: Client error '404 Not Found' for url 'http://localhost:2024/threads/dcea5cd8-eb70-4a01-a4b6-643b14e8f754'
For more information check: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/404
✅ Bob created his own thread: 400f8d41-e946-429f-8f93-4fe395bc3eed
✅ Alice sees 1 thread
✅ Bob sees 1 thread
✅ Alice correctly denied access:
For more information check: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/500
✅ Alice correctly denied access to searching assistants:
```

Congratulations! You've built a chatbot where each user has their own private conversations. While this system uses simple token-based authentication, these authorization patterns will work with implementing any real authentication system. In the next tutorial, you'll replace your test users with real user accounts using OAuth2.

## Next steps

Now that you can control access to resources, you might want to:

1. Move on to [Connect an authentication provider](/langsmith/add-auth-server) to add real user accounts.
2. Read more about [authorization patterns](/langsmith/auth#authorization).
3. Check out the [API reference](https://reference.langchain.com/python/langgraph-sdk/auth/Auth) for details about the interfaces and methods used in this tutorial.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/resource-auth.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Rollback Concurrent
Source: https://docs.langchain.com/langsmith/rollback-concurrent

This guide assumes knowledge of what double-texting is, which you can learn about in the [double-texting conceptual guide](/langsmith/double-texting).

The guide covers the `rollback` option for double texting, which interrupts the prior run of the graph and starts a new one with the double-text. This option is very similar to the `interrupt` option, but in this case the first run is completely deleted from the database and cannot be restarted. Below is a quick example of using the `rollback` option.

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
    import asyncio

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

Now let's run a thread with the multitask parameter set to "rollback":

<Tabs>
  <Tab title="Python">
    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    # the first run will be rolled back
    rolled_back_run = await client.runs.create(
        thread["thread_id"],
        assistant_id,
        input={"messages": [{"role": "user", "content": "what's the weather in sf?"}]},
    )
    run = await client.runs.create(
        thread["thread_id"],
        assistant_id,
        input={"messages": [{"role": "user", "content": "what's the weather in nyc?"}]},
        multitask_strategy="rollback",
    )
    # wait until the second run completes
    await client.runs.join(thread["thread_id"], run["run_id"])
    ```
  </Tab>

  <Tab title="Javascript">
    ```js theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    // the first run will be interrupted
    let rolledBackRun = await client.runs.create(
      thread["thread_id"],
      assistantId,
      { input: { messages: [{ role: "human", content: "what's the weather in sf?" }] } }
    );

    let run = await client.runs.create(
      thread["thread_id"],
      assistant_id,
      {
        input: { messages: [{ role: "human", content: "what's the weather in nyc?" }] },
        multitaskStrategy: "rollback"
      }
    );

    // wait until the second run completes
    await client.runs.join(thread["thread_id"], run["run_id"]);
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
      \"multitask_strategy\": \"rollback\"
    }" && curl --request GET \
    --url <DEPLOYMENT_URL>/threads/<THREAD_ID>/runs/<RUN_ID>/join
    ```
  </Tab>
</Tabs>

## View run results

We can see that the thread has data only from the second run

<Tabs>
  <Tab title="Python">
    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    state = await client.threads.get_state(thread["thread_id"])

    for m in convert_to_messages(state["values"]["messages"]):
        m.pretty_print()
    ```
  </Tab>

  <Tab title="Javascript">
    ```js theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    const state = await client.threads.getState(thread["thread_id"]);

    for (const m of state['values']['messages']) {
      prettyPrint(m);
    }
    ```
  </Tab>

  <Tab title="CURL">
    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    source pretty_print.sh && curl --request GET \
    --url <DEPLOYMENT_URL>/threads/<THREAD_ID>/state | \
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

what's the weather in nyc?
================================== Ai Message ==================================

[{'id': 'toolu_01JzPqefao1gxwajHQ3Yh3JD', 'input': {'query': 'weather in nyc'}, 'name': 'tavily_search_results_json', 'type': 'tool_use'}]
Tool Calls:
tavily_search_results_json (toolu_01JzPqefao1gxwajHQ3Yh3JD)
Call ID: toolu_01JzPqefao1gxwajHQ3Yh3JD
Args:
query: weather in nyc
================================= Tool Message =================================
Name: tavily_search_results_json

[{"url": "https://www.weatherapi.com/", "content": "{'location': {'name': 'New York', 'region': 'New York', 'country': 'United States of America', 'lat': 40.71, 'lon': -74.01, 'tz_id': 'America/New_York', 'localtime_epoch': 1718734479, 'localtime': '2024-06-18 14:14'}, 'current': {'last_updated_epoch': 1718733600, 'last_updated': '2024-06-18 14:00', 'temp_c': 29.4, 'temp_f': 84.9, 'is_day': 1, 'condition': {'text': 'Sunny', 'icon': '//cdn.weatherapi.com/weather/64x64/day/113.png', 'code': 1000}, 'wind_mph': 2.2, 'wind_kph': 3.6, 'wind_degree': 158, 'wind_dir': 'SSE', 'pressure_mb': 1025.0, 'pressure_in': 30.26, 'precip_mm': 0.0, 'precip_in': 0.0, 'humidity': 63, 'cloud': 0, 'feelslike_c': 31.3, 'feelslike_f': 88.3, 'windchill_c': 28.3, 'windchill_f': 82.9, 'heatindex_c': 29.6, 'heatindex_f': 85.3, 'dewpoint_c': 18.4, 'dewpoint_f': 65.2, 'vis_km': 16.0, 'vis_miles': 9.0, 'uv': 7.0, 'gust_mph': 16.5, 'gust_kph': 26.5}}"}]
================================== Ai Message ==================================

The weather API results show that the current weather in New York City is sunny with a temperature of around 85°F (29°C). The wind is light at around 2-3 mph from the south-southeast. Overall it looks like a nice sunny summer day in NYC.
```

Verify that the original, rolled back run was deleted

<Tabs>
  <Tab title="Python">
    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    try:
        await client.runs.get(thread["thread_id"], rolled_back_run["run_id"])
    except httpx.HTTPStatusError as _:
        print("Original run was correctly deleted")
    ```
  </Tab>

  <Tab title="Javascript">
    ```js theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    try {
      await client.runs.get(thread["thread_id"], rolledBackRun["run_id"]);
    } catch (e) {
      console.log("Original run was correctly deleted");
    }
    ```
  </Tab>
</Tabs>

Output:

```
Original run was correctly deleted
```

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/rollback-concurrent.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Set up automation rules
Source: https://docs.langchain.com/langsmith/rules

While you can manually sift through and process production logs from your LLM application, it often becomes difficult as your application scales to more users. LangSmith provides **Automations** that allow you to trigger certain actions on your trace data. You can define an automations by a **filter**, **sampling rate**, and **action**.

Automation rules can trigger actions such as: adding traces to a dataset, adding to an annotation queue, triggering a webhook (e.g., for remote evaluations) or extending data retention. Some examples of automations you can set up:

* Send all traces with negative feedback to an annotation queue for human review.
* Send 10% of all traces to an annotation queue for human review to spot check for issues.
* Upgrade all traces with errors for extended data retention.

<Info>
  To configure online evaluations, visit the [online evaluations](/langsmith/online-evaluations-llm-as-judge) page.
</Info>

<Note>If an automation rule matches any run within a trace, the trace will be auto-upgraded to [extended data retention](/langsmith/usage-and-billing#data-retention-auto-upgrades). This upgrade will impact trace pricing, but ensures that traces meeting your automation criteria (typically those most valuable for analysis) are preserved for investigation. </Note>

## How automation rules execute

Each automation rule runs on an independent polling schedule. If you have multiple rules on the same project, a webhook rule may process a run before an evaluator rule has scored it, or vice versa.

Within a single rule, if multiple actions are configured, they execute in this order:

1. Add to annotation queue.
2. Add to dataset.
3. Trigger webhook.
4. Run online evaluator.
5. Run custom code evaluator.
6. Trigger alert.

If your workflow requires data produced by one rule to be present when another fires—for example, you want a webhook to include an evaluation score—use a filter on the downstream rule to create that dependency explicitly. For an example, refer to [Ensuring evaluations complete before the webhook fires](/langsmith/webhooks#ensuring-evaluations-complete-before-the-webhook-fires).

## View automation rules

In the [UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-rules), navigate to the **Tracing** in the sidebar and select a tracing project. To view existing automation rules for that tracing project, click on the **Automations** tab.

## Create a rule

1. In the [UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-rules), navigate to the **Tracing** in the sidebar and select a tracing project. Click on **+ New** in the top right corner of the tracing project page, then click on **New Automation**.

2. Name your rule.

3. Create a filter. Automation rule filters work the same way as filters applied to traces in the project. For more information on filters, you can refer to [Filter traces](/langsmith/filter-traces-in-application).

4. Configure a **Sampling Rate** to control the percentage of filtered runs that trigger the automation action. You can specify a sampling rate between 0 and 1 for automations. This will control the percent of the filtered runs that are sent to an automation action. For example, if you set the sampling rate to 0.5, then 50% of the traces that pass the filter will be sent to the action.

5. (Optional) Apply rule to past runs by toggling the **Apply to past runs** and entering a **Backfill from** date. This is only possible upon rule creation.

   <Note>
     The backfill is processed as a background job, so you will not see the results immediately. In order to track progress of the backfill, you can [view logs for your automations](#view-logs-for-your-automations).
   </Note>

6. Select an action to trigger when the rule is applied. There are four actions you can take with an automation rule:

   * **Add to dataset**: Add the inputs and outputs of the trace to a [dataset](/langsmith/evaluation-concepts#datasets).
   * **Add to annotation queue**: Add the trace to an [annotation queue](/langsmith/annotation-queues).
   * **Trigger webhook**: Trigger a [webhook](/langsmith/use-webhooks) with the trace data.
   * **Extend data retention**: Extends the data retention period on matching traces that use base retention [(refer to the data retention docs for more details)](/langsmith/usage-and-billing#data-retention).
     Note that all other rules will also extend data retention on matching traces through the
     auto-upgrade mechanism described in the data retention docs,
     but this rule takes no additional action.

## View logs for your automations

Logs allow you to gain confidence that your rules are working as expected. You can view logs for your automations by navigating to the **Automations** tab within a tracing project and clicking the **Logs** button for the rule you created.

The logs tab allows you to:

* View all runs processed by a given rule for the time period selected.
* If a particular rule execution has triggered an error, you can view the error message by hovering over the error icon.
* You can monitor the progress of a backfill job by filtering to the rule's creation timestamp. This is because the backfill starts from when the rule was created.
* Inspect the run that the automation rule applied to using the **View run** button. For rules that add runs as examples to datasets, you can view the example produced.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/rules.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Run backtests on a new version of an agent
Source: https://docs.langchain.com/langsmith/run-backtests-new-agent

Deploying your application is just the beginning of a continuous improvement process. After you deploy to production, you'll want to refine your system by enhancing prompts, language models, tools, and architectures. Backtesting involves assessing new versions of your application using historical data and comparing the new outputs to the original ones. Compared to evaluations using pre-production datasets, backtesting offers a clearer indication of whether the new version of your application is an improvement over the current deployment.

Here are the basic steps for backtesting:

1. Select sample runs from your production tracing project to test against.
2. Transform the run inputs into a dataset and record the run outputs as an initial experiment against that dataset.
3. Execute your new system on the new dataset and compare the results of the experiments.

This process will provide you with a new dataset of representative inputs, which you can version and use for backtesting your models.

<Info>
  Often, you won't have definitive "ground truth" answers available. In such cases, you can manually label the outputs or use evaluators that don't rely on reference data. If your application allows for capturing ground-truth labels, for example by allowing users to leave feedback, we strongly recommend doing so.
</Info>

## Setup

### Configure the environment

Install and set environment variables. This guide requires `langsmith>=0.2.4`.

<Info>
  For convenience we'll use the LangChain OSS framework in this tutorial, but the LangSmith functionality shown is framework-agnostic.
</Info>

<CodeGroup>
  ```bash pip theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  pip install -U langsmith langchain langchain-anthropic langchainhub emoji
  ```

  ```bash uv theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  uv add langsmith langchain langchain-anthropic langchainhub emoji
  ```
</CodeGroup>

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import getpass
import os

# Set the project name to whichever project you'd like to be testing against
project_name = "Tweet Writing Task"
os.environ["LANGSMITH_PROJECT"] = project_name
os.environ["LANGSMITH_TRACING"] = "true"

if not os.environ.get("LANGSMITH_API_KEY"):
    os.environ["LANGSMITH_API_KEY"] = getpass.getpass("YOUR API KEY")

# Optional. You can swap OpenAI for any other tool-calling chat model.
os.environ["OPENAI_API_KEY"] = "YOUR OPENAI API KEY"

# Optional. You can swap Tavily for the free DuckDuckGo search tool if preferred.

# Get Tavily API key: https://tavily.com
os.environ["TAVILY_API_KEY"] = "YOUR TAVILY API KEY"
```

### Define the application

For this example lets create a simple Tweet-writing application that has access to some internet search tools:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from langchain_community.tools import DuckDuckGoSearchRun, TavilySearchResults
from langchain_core.rate_limiters import InMemoryRateLimiter

# We will use GPT-3.5 Turbo as the baseline and compare against GPT-4o
gpt_3_5_turbo = init_chat_model(
    "gpt-3.5-turbo",
    temperature=1,
    configurable_fields=("model", "model_provider"),
)

# The instructions are passed as a system message to the agent
instructions = """You are a tweet writing assistant. Given a topic, do some research and write a relevant and engaging tweet about it.
- Use at least 3 emojis in each tweet
- The tweet should be no longer than 280 characters
- Always use the search tool to gather recent information on the tweet topic
- Write the tweet only based on the search content. Do not rely on your internal knowledge
- When relevant, link to your sources
- Make your tweet as engaging as possible"""

# Define the tools our agent can use

# If you have a higher tiered Tavily API plan you can increase this
rate_limiter = InMemoryRateLimiter(requests_per_second=0.08)

# Use DuckDuckGo if you don't have a Tavily API key:

# tools = [DuckDuckGoSearchRun(rate_limiter=rate_limiter)]
tools = [TavilySearchResults(max_results=5, rate_limiter=rate_limiter)]

agent = create_agent(gpt_3_5_turbo, tools=tools, system_prompt=instructions)
```

### Simulate production data

Now lets simulate some production data:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
fake_production_inputs = [
    "Alan turing's early childhood",
    "Economic impacts of the European Union",
    "Underrated philosophers",
    "History of the Roxie theater in San Francisco",
    "ELI5: gravitational waves",
    "The arguments for and against a parliamentary system",
    "Pivotal moments in music history",
    "Big ideas in programming languages",
    "Big questions in biology",
    "The relationship between math and reality",
    "What makes someone funny",
]

agent.batch(
    [{"messages": [{"role": "user", "content": content}]} for content in fake_production_inputs],
)
```

## Convert production traces to experiment

The first step is to generate a dataset based on the production *inputs*. Then copy over all the traces to serve as a baseline experiment.

### Select runs to backtest on

You can select the runs to backtest on using the `filter` argument of `list_runs`. The `filter` argument uses the LangSmith [trace query syntax](/langsmith/trace-query-syntax) to select runs.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from datetime import datetime, timedelta, timezone
from uuid import uuid4
from langsmith import Client
from langsmith.beta import convert_runs_to_test

# Fetch the runs we want to convert to a dataset/experiment
client = Client()

# How we are sampling runs to include in our dataset
end_time = datetime.now(tz=timezone.utc)
start_time = end_time - timedelta(days=1)
run_filter = f'and(gt(start_time, "{start_time.isoformat()}"), lt(end_time, "{end_time.isoformat()}"))'
prod_runs = list(
    client.list_runs(
        project_name=project_name,
        is_root=True,
        filter=run_filter,
    )
)
```

### Convert runs to experiment

`convert_runs_to_test` is a function which takes some runs and does the following:

1. The inputs, and optionally the outputs, are saved to a dataset as Examples.
2. The inputs and outputs are stored as an experiment, as if you had run the `evaluate` function and received those outputs.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}

# Name of the dataset we want to create
dataset_name = f'{project_name}-backtesting {start_time.strftime("%Y-%m-%d")}-{end_time.strftime("%Y-%m-%d")}'

# Name of the experiment we want to create from the historical runs
baseline_experiment_name = f"prod-baseline-gpt-3.5-turbo-{str(uuid4())[:4]}"

# This converts the runs to a dataset + experiment
convert_runs_to_test(
    prod_runs,
    # Name of the resulting dataset
    dataset_name=dataset_name,
    # Whether to include the run outputs as reference/ground truth
    include_outputs=False,
    # Whether to include the full traces in the resulting experiment
    # (default is to just include the root run)
    load_child_runs=True,
    # Name of the experiment so we can apply evalautors to it after
    test_project_name=baseline_experiment_name
)
```

Once this step is complete, you should see a new dataset in your LangSmith project called "Tweet Writing Task-backtesting TODAYS DATE", with a single experiment like so:

<img alt="Baseline experiment" />

## Benchmark against new system

Now we can start the process of benchmarking our production runs against a new system.

### Define evaluators

First let's define the evaluators we will use to compare the two systems. Note that we have no reference outputs, so we'll need to come up with evaluation metrics that only require the actual outputs.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import emoji
from pydantic import BaseModel, Field
from langchain_core.messages import convert_to_openai_messages

class Grade(BaseModel):
    """Grade whether a response is supported by some context."""
    grounded: bool = Field(..., description="Is the majority of the response supported by the retrieved context?")

grounded_instructions = f"""You have given somebody some contextual information and asked them to write a statement grounded in that context.

Grade whether their response is fully supported by the context you have provided. \
If any meaningful part of their statement is not backed up directly by the context you provided, then their response is not grounded. \
Otherwise it is grounded."""
grounded_model = init_chat_model(model="gpt-5.5").with_structured_output(Grade)

def lt_280_chars(outputs: dict) -> bool:
    messages = convert_to_openai_messages(outputs["messages"])
    return len(messages[-1]['content']) <= 280

def gte_3_emojis(outputs: dict) -> bool:
    messages = convert_to_openai_messages(outputs["messages"])
    return len(emoji.emoji_list(messages[-1]['content'])) >= 3

async def is_grounded(outputs: dict) -> bool:
    context = ""
    messages = convert_to_openai_messages(outputs["messages"])
    for message in messages:
        if message["role"] == "tool":
            # Tool message outputs are the results returned from the Tavily/DuckDuckGo tool
            context += "\n\n" + message["content"]
    tweet = messages[-1]["content"]
    user = f"""CONTEXT PROVIDED:
    {context}

    RESPONSE GIVEN:
    {tweet}"""
    grade = await grounded_model.ainvoke([
        {"role": "system", "content": grounded_instructions},
        {"role": "user", "content": user}
    ])
    return grade.grounded
```

### Evaluate baseline

Now, let's run our evaluators against the baseline experiment.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
baseline_results = await client.aevaluate(
    baseline_experiment_name,
    evaluators=[lt_280_chars, gte_3_emojis, is_grounded],
)

# If you have pandas installed can easily explore results as df:

# baseline_results.to_pandas()
```

### Define and evaluate new system

Now, let's define and evaluate our new system. In this example our new system will be the same as the old system, but will use GPT-4o instead of GPT-3.5. Since we've made our model configurable we can just update the default config passed to our agent:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
candidate_results = await client.aevaluate(
    agent.with_config(model="gpt-5.5"),
    data=dataset_name,
    evaluators=[lt_280_chars, gte_3_emojis, is_grounded],
    experiment_prefix="candidate-gpt-5.5",
)

# If you have pandas installed can easily explore results as df:

# candidate_results.to_pandas()
```

## Comparing the results

After running both experiments, you can view them in your dataset:

<img alt="Dataset page" />

The results reveal an interesting tradeoff between the two models:

1. GPT-4o shows improved performance in following formatting rules, consistently including the requested number of emojis
2. However, GPT-4o is less reliable at staying grounded in the provided search results

To illustrate the grounding issue: in [this example run](https://smith.langchain.com/public/be060e19-0bc0-4798-94f5-c3d35719a5f6/r/07d43e7a-8632-479d-ae28-c7eac6e54da4), GPT-4o included facts about Abū Bakr Muhammad ibn Zakariyyā al-Rāzī's medical contributions that weren't present in the search results. This demonstrates how it's pulling from its internal knowledge rather than strictly using the provided information.

This backtesting exercise revealed that while GPT-4o is generally considered a more capable model, simply upgrading to it wouldn't improve our tweet-writer. To effectively use GPT-4o, we would need to:

* Refine our prompts to more strongly emphasize using only provided information
* Or modify our system architecture to better constrain the model's outputs

This insight demonstrates the value of backtesting - it helped us identify potential issues before deployment.

<img alt="Tutorial comparison view" />

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/run-backtests-new-agent.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
