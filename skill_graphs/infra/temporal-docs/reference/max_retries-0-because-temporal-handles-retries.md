# max_retries=0 because Temporal handles retries
client = wrap_openai(AsyncOpenAI(max_retries=0))
```

Use this client in your Activities:

```python
from temporalio import activity

@activity.defn
async def invoke_model(prompt: str) -> str:
    client = wrap_openai(AsyncOpenAI(max_retries=0))

    response = await client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
    )

    return response.choices[0].message.content
```

After running a Workflow, you'll see a trace hierarchy in Braintrust:

```
my-workflow-request (client span)
└── temporal.workflow.MyWorkflow
    └── temporal.activity.invoke_model
        └── Chat Completion (gpt-4o)
```

## Add custom spans for application context

Add your own spans to capture business-level context like user queries, workflow inputs, and final outputs.

```python
from braintrust import start_span

async def run_research(query: str):
    with start_span(name="research-request", type="task") as span:
        span.log(input={"query": query})

        result = await client.execute_workflow(
            ResearchWorkflow.run,
            query,
            id=f"research-{uuid.uuid4()}",
            task_queue="research-task-queue",
        )

        span.log(output={"result": result})
        return result
```

## Manage prompts with load_prompt

Braintrust lets you manage prompts in a UI and deploy changes without code deploys. The workflow is:

1. **Develop** prompts in code, see results in Braintrust traces
2. **Create** a prompt in the Braintrust UI from your best version
3. **Evaluate** different versions using Braintrust's eval tools
4. **Deploy** by pointing your code at the Braintrust prompt
5. **Iterate** in the UI—changes go live without code deploys

To load a prompt from Braintrust in your Activity:

```python

from temporalio import activity

@activity.defn
async def invoke_model(prompt_slug: str, user_input: str) -> str:
    # Load prompt from Braintrust
    prompt = braintrust.load_prompt(
        project=os.environ.get("BRAINTRUST_PROJECT", "my-project"),
        slug=prompt_slug,
    )

    # Build returns the full prompt configuration
    built = prompt.build()

    # Extract system message
    system_content = None
    for msg in built.get("messages", []):
        if msg.get("role") == "system":
            system_content = msg["content"]
            break

    client = wrap_openai(AsyncOpenAI(max_retries=0))

    response = await client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": system_content},
            {"role": "user", "content": user_input},
        ],
    )

    return response.choices[0].message.content
```

:::tip

Provide a fallback prompt in your code for resilience. If Braintrust is unavailable, your Workflow continues with the
hardcoded prompt.

```python
DEFAULT_SYSTEM_PROMPT = "You are a helpful assistant."

try:
    prompt = braintrust.load_prompt(project="my-project", slug="my-prompt")
    system_content = extract_system_message(prompt.build())
except Exception as e:
    activity.logger.warning(f"Failed to load prompt: {e}. Using fallback.")
    system_content = DEFAULT_SYSTEM_PROMPT
```

:::

## Example: Deep Research Agent

The [deep research sample](https://github.com/braintrustdata/braintrust-cookbook/blob/main/examples/TemporalDeepResearch/TemporalDeepResearch.mdx) demonstrates a complete AI
agent that:

- Plans research strategies
- Generates search queries
- Executes web searches in parallel
- Synthesizes findings into comprehensive reports

The sample shows all integration patterns: wrapped OpenAI client, BraintrustPlugin on Worker and Client, custom spans,
and prompt management with `load_prompt()`.

To run the sample:

```bash
