# Profiles
Source: https://docs.langchain.com/oss/python/deepagents/profiles

Package per-provider and per-model defaults that Deep Agents applies when a model is selected

**Harness profiles** let you package configuration that Deep Agents applies whenever a given provider or specific model is selected: system-prompt tweaks, tool description overrides, excluded tools or middleware, extra middleware, and general-purpose subagent edits. They are the main way to tune how the harness behaves for a particular model without changing your `create_deep_agent` call site. Use `HarnessProfile` when building profiles in Python; use `HarnessProfileConfig` when [loading or saving YAML/JSON files](#load-profiles-from-config-files). Deep Agents ships built-in harness profiles for OpenAI and Anthropic (Claude) models.

**Provider profiles** are a narrower companion API for *model-construction* kwargs, which don't affect the harness. Most callers don't need them; reach for one when you want `init_chat_model` defaults, credential checks, or runtime-derived kwargs as defaults with your provider choice (for example, when packaging a provider integration).

## Harness profiles

A `HarnessProfile` describes prompt-assembly, tool-visibility, middleware, and default-subagent adjustments that `create_deep_agent` applies after the chat model has been constructed:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from deepagents import (
    GeneralPurposeSubagentProfile,
    HarnessProfile,
    register_harness_profile,
)

register_harness_profile(
    "openai:gpt-5.5",
    HarnessProfile(
        system_prompt_suffix="Respond in under 100 words.",
        excluded_tools={"execute"},
        excluded_middleware={"SummarizationMiddleware"},
        general_purpose_subagent=GeneralPurposeSubagentProfile(enabled=False),
    ),
)
```

<ResponseField name="base_system_prompt" type="string">
  Replace the base Deep Agents system prompt (`CUSTOM` in [Prompt assembly](/oss/python/deepagents/customization#prompt-assembly)).
</ResponseField>

<ResponseField name="system_prompt_suffix" type="string">
  Append text to the assembled base prompt (`SUFFIX` in [Prompt assembly](/oss/python/deepagents/customization#prompt-assembly)); applied to the main agent, declarative subagents, and the auto-added general-purpose subagent.
</ResponseField>

<ResponseField name="tool_description_overrides" type="Mapping[str, str]">
  Override individual tool descriptions, keyed by tool name.
</ResponseField>

<ResponseField name="excluded_tools" type="frozenset[str]">
  Remove specific harness-level tools from the tool set. Matched by tool name (string), applied as a post-injection filter so it can drop both user-supplied tools and tools added by harness middleware. See [Running without the default filesystem tools](/oss/python/deepagents/harness#virtual-filesystem-access) for a worked example.
</ResponseField>

<ResponseField name="excluded_middleware" type="frozenset[type[AgentMiddleware] | str]">
  Strip specific middleware classes from the [default stack](/oss/python/deepagents/customization#default-stack-main-agent). Accepts middleware classes or string names.
</ResponseField>

<ResponseField name="extra_middleware" type="Sequence[AgentMiddleware] | Callable[[], Sequence[AgentMiddleware]]">
  Append middleware to every stack this profile applies to. See the [default middleware stack](/oss/python/deepagents/customization#middleware) for the built-in ordering.
</ResponseField>

<ResponseField name="general_purpose_subagent" type="GeneralPurposeSubagentProfile">
  Disable, rename, or re-prompt the general-purpose subagent. When this field's `system_prompt` is set alongside `base_system_prompt`, the general-purpose-specific subagent prompt wins—see [General-purpose subagent prompt](/oss/python/deepagents/customization#general-purpose-subagent-prompt).
</ResponseField>

<Note>
  Caller-supplied `system_prompt=` always sits at the front of the assembled prompt, and `system_prompt_suffix` always sits at the end—regardless of which model is selected. The same overlay rules apply to subagents: each subagent re-runs profile resolution against its own model. See [Prompt assembly](/oss/python/deepagents/customization#prompt-assembly) for the full per-case breakdown (main agent, subagents, and the general-purpose subagent).
</Note>

<Warning>
  To run an agent without the `task` tool, see [Running without subagents](/oss/python/deepagents/subagents#running-without-subagents) — set `general_purpose_subagent=GeneralPurposeSubagentProfile(enabled=False)` and pass no synchronous subagents via `subagents=`. `SubAgentMiddleware` (and the `task` tool) is only attached when at least one synchronous subagent exists, so this configuration leaves it out cleanly. Async subagents are unaffected.

  Listing `FilesystemMiddleware`, `SubAgentMiddleware`, or the internal permission middleware in `excluded_middleware` raises a `ValueError` — they're required scaffolding in the [default middleware stack](/oss/python/deepagents/customization#default-stack-main-agent). To hide their tools from the model without removing the middleware, use `excluded_tools` instead — see [Running without the default filesystem tools](/oss/python/deepagents/harness#virtual-filesystem-access).
</Warning>

Entries in `excluded_middleware` accept two forms:

* A middleware *class* (matched by exact type), or a plain string that matches `AgentMiddleware.name`. Use plain strings for built-ins and public aliases such as `"SummarizationMiddleware"`.
* An `module:Class` import ref (for example, `"my_pkg.middleware:TelemetryMiddleware"`) to target an exact middleware class from a config file. Import refs resolve lazily, so use them only for trusted local configuration — loading one imports Python code.

<Accordion title="Lookup order for preconfigured model instances">
  When you pass a preconfigured chat model instance instead of a `provider:model` string, the harness synthesizes the canonical `provider:identifier` key from the instance and looks it up in this order:

  1. Exact `provider:identifier` match
  2. Identifier-only (only when the identifier already contains `:`)
  3. Provider-only fallback
</Accordion>

## Registration keys

Both profile types use the same key format:

* **Provider-level** — a bare provider name like `"openai"` applies to every model from that provider.
* **Model-level** — a fully qualified `provider:model` key like `"openai:gpt-5.5"` applies only to that specific model.

When both a provider-level and a model-level profile exist, they are merged at resolution time. Unset model-level fields inherit from the provider-level profile; explicit model-level values override them.

Re-registering under an existing key merges the new profile on top of the prior one—it does not replace it. See [Merge semantics](#merge-semantics) for the per-field rules.

<Note>
  There is no wildcard key that matches every provider. To apply the same overrides everywhere—say, dropping `TodoListMiddleware` regardless of which model is selected—register the profile under each provider key you use. Profiles are intended for adjustments that depend on the model being selected. Global adjustments that should apply regardless of model should be made on the `create_deep_agent` call site.
</Note>

## Merge semantics

| Field                                        | Merge behavior                                                                                 |
| -------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `base_system_prompt`, `system_prompt_suffix` | New value wins when set; otherwise inherits                                                    |
| `tool_description_overrides`                 | Mappings merge per key; new value wins on a shared key                                         |
| `excluded_tools`, `excluded_middleware`      | Set union                                                                                      |
| `extra_middleware`                           | Merged by concrete class: new instance replaces existing at its position, novel classes append |
| `general_purpose_subagent`                   | Merged field-wise (unset fields inherit)                                                       |
| `init_kwargs` (provider)                     | Dicts merge key-wise; new value wins on a shared key                                           |
| `pre_init` (provider)                        | Callables chain: existing runs first, then the new one                                         |
| `init_kwargs_factory` (provider)             | Factories chain with their outputs merged every `resolve_model` call                           |

## Provider profiles

A `ProviderProfile` declares how Deep Agents should construct a chat model for a given provider or specific model spec. It applies only when you provide a `provider:model` string when creating the deep agent, not when you pass a preconfigured model with [`init_chat_model`](https://reference.langchain.com/python/langchain/chat_models/base/init_chat_model):

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from deepagents import ProviderProfile, register_provider_profile

register_provider_profile(
    "openai",
    ProviderProfile(init_kwargs={"temperature": 0}),
)
```

<ResponseField name="init_kwargs" type="Mapping[str, Any]">
  Static initialization arguments forwarded to `init_chat_model`.
</ResponseField>

<ResponseField name="pre_init" type="Callable[[str], None]">
  Side effects to run before construction (for example, credential validation).
</ResponseField>

<ResponseField name="init_kwargs_factory" type="Callable[[], dict[str, Any]]">
  Kwargs derived from runtime state (for example, headers pulled from environment variables).
</ResponseField>

## Load profiles from config files

For YAML/JSON-backed workflows, use `HarnessProfileConfig`. It mirrors the declarative subset of `HarnessProfile` (prompt text, tool-description overrides, excluded tools and middleware, general-purpose subagent edits) and owns `to_dict` / `from_dict`. Runtime-only state — middleware instances, factories, and class-form `excluded_middleware` entries — stays on `HarnessProfile`.

`register_harness_profile` accepts either type, so config-backed callers don't need a manual conversion step:

```yaml theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}

# openai.yaml
base_system_prompt: You are helpful.
system_prompt_suffix: Respond briefly.
excluded_tools:
  - execute
  - grep
excluded_middleware:
  - SummarizationMiddleware
  - my_pkg.middleware:TelemetryMiddleware
general_purpose_subagent:
  enabled: false
```

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import yaml
from deepagents import HarnessProfileConfig, register_harness_profile

with open("openai.yaml") as f:
    register_harness_profile(
        "openai",
        HarnessProfileConfig.from_dict(yaml.safe_load(f)),
    )
```

To go the other direction, `HarnessProfileConfig.from_harness_profile(...)` exports a runtime profile back to the declarative shape when it only uses serializable features:

* Class-form `excluded_middleware` entries serialize as a public alias (when the class exposes one via `serialized_name: ClassVar[str]`) or as a `module:Class` import ref.
* Non-empty `extra_middleware` and middleware classes declared in `__main__` or inside a function scope cannot be serialized — export raises `ValueError`.

## Ship a profile as a plugin

Distributable profiles can register themselves via `importlib.metadata` entry points instead of requiring callers to run `register_*_profile` by hand. Load order is **built-ins first, then entry-point plugins, then any direct `register_*_profile` calls in user code**; all three paths funnel through the same additive registration, so later registrations layer on top of earlier ones under the same key.

Declare an entry point in the distribution's own `pyproject.toml` under the appropriate group:

```toml theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
[project.entry-points."deepagents.harness_profiles"]
my_provider = "my_pkg.profiles:register_harness"

[project.entry-points."deepagents.provider_profiles"]
my_provider = "my_pkg.profiles:register_provider"
```

Each target resolves to a zero-arg callable that performs the registrations when `deepagents.profiles` is imported:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from deepagents import (
    HarnessProfile,
    ProviderProfile,
    register_harness_profile,
    register_provider_profile,
)

def register_harness() -> None:
    register_harness_profile(
        "my_provider",
        HarnessProfile(system_prompt_suffix="Batch independent tool calls in parallel."),
    )

def register_provider() -> None:
    register_provider_profile(
        "my_provider",
        ProviderProfile(init_kwargs={"temperature": 0}),
    )
```

## Related

* [Harness](/oss/python/deepagents/harness) — overview of harness capabilities
* [Models](/oss/python/deepagents/models) — configure model providers and parameters
* [Customization](/oss/python/deepagents/customization) — full `create_deep_agent` configuration surface

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/deepagents/profiles.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Programmatic subagents
Source: https://docs.langchain.com/oss/python/deepagents/programmatic-subagents

Use interpreters to dispatch and orchestrate Deep Agents subagents from code

Programmatic subagents let an agent dispatch [subagents](/oss/python/deepagents/subagents) from interpreter code. Instead of asking the model to choose one subagent call at a time, the agent can use JavaScript loops, branches, and parallel batches to route work across configured subagents and synthesize the results.

Use this pattern when work spans many independent units, needs multiple perspectives, or benefits from recursive analysis. For general interpreter setup, see [Interpreters](/oss/python/deepagents/interpreters).

<Warning>
  Programmatic subagents use the interpreter runtime, which is in [**beta**](/oss/python/versioning). APIs and lifecycle behavior may change between releases.
</Warning>

<Note>
  Interpreters require `langchain-quickjs>=0.1.0` and Python `>=3.11`.
</Note>

## How it works

When an agent has [subagents](/oss/python/deepagents/subagents) and interpreter middleware, the interpreter exposes a built-in `task()` global that dispatches subagents from code. A task spanning many independent units (reviewing every file in a directory, triaging a batch of tickets) becomes a loop that fans the work out, so it runs deterministically instead of one model-chosen tool call at a time.

Subagent orchestration also supports recursive language model (RLM) workflows, the approach described in the [Recursive Language Models paper](https://arxiv.org/abs/2512.24601): keep the working set in interpreter variables, select slices, call subagents with `task()`, and synthesize the results.

`task()` takes the following inputs:

* `description`: The prompt for the subagent
* `subagentType`: Which configured subagent to run
* `responseSchema` (optional): Structured output

A `task()` runs a full agentic loop and resolves to the subagent's result:

```javascript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const review = await task({
  description: "Review src/auth/login.ts for auth issues. Cite line numbers.",
  subagentType: "reviewer",
  responseSchema: {
    type: "object",
    properties: {
      issues: { type: "array", items: { type: "object", properties: {
        file: { type: "string" }, line: { type: "number" },
        severity: { type: "string" }, description: { type: "string" },
      }}},
    },
  },
});

// With responseSchema, the result is already a typed value, so no JSON.parse is needed.
const critical = review.issues.filter((issue) => issue.severity === "high");
```

When you pass `responseSchema`, the resolved value is already a typed JavaScript object; only call `JSON.parse` if a subagent intentionally returned a JSON string.

## Guide orchestration

The interpreter middleware ships orchestration guidance in the system prompt, so the agent already knows how to fan out in bounded batches, filter between passes, and synthesize results. You do not hand-write that logic or prompt for it turn by turn.

To shape what the agent orchestrates, work through the inputs it already responds to:

* **The subagents you configure.** Their `name` and `description` define the roles available. A `reviewer` paired with a `verifier` invites a two-pass check; a single `analyzer` invites a straight fan-out.
* **The task message.** Phrasing like "I only want confirmed issues, not maybes" or "be exhaustive" nudges the agent toward verification or an open-ended sweep.
* **The system prompt.** Use `systemPrompt` (or the agent's instructions) to add standing guidance when you want a consistent strategy across runs.

## Patterns

The agent picks a strategy from the shape of the task; these emerge from how it writes interpreter code, not from configuration, and the subagents you make available determine what it can do. Every pattern shares one model: hold work in JS variables, dispatch subagents with `task()`, and combine results in code. The diagrams below show the common shapes, each with a runnable example.

### Classify and act

Items are classified first, then each item is handled by a specialized subagent based on its classification. This lets you process mixed inputs where different items need different expertise.

```mermaid theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
graph LR
    Task[Task] --> Classify{Classifier}
    Classify --> |bug| A[Agent A]
    Classify --> |feature| B[Agent B]
    Classify --> |question| C[Agent C]
```

**Use cases:** Triaging support tickets, error logs, user feedback, or any batch of items that need different handling depending on their type.

<Accordion title="Example: classify and act">
  **What you configure**

  ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  agent = create_deep_agent(
      model="openai:gpt-5.5",
      subagents=[
          {
              "name": "bug-fixer",
              "description": "Investigates bug reports and provides reproduction steps",
              "system_prompt": "You are a bug triage specialist. Investigate each bug report and provide clear reproduction steps.",
          },
          {
              "name": "feature-analyst",
              "description": "Evaluates feature requests for feasibility and effort",
              "system_prompt": "You are a product analyst. Evaluate each feature request for technical feasibility, estimated effort, and potential impact.",
          },
          {
              "name": "support-agent",
              "description": "Answers user questions based on documentation",
              "system_prompt": "You are a support specialist. Answer user questions clearly based on the available documentation.",
          },
      ],
      middleware=[CodeInterpreterMiddleware()],
  )

  result = await agent.ainvoke({
      "messages": [{"role": "user", "content": "Go through these 30 support tickets. Categorize each one, then for bugs give me reproduction steps, and for feature requests give me a feasibility assessment."}]
  })
  ```

  **What the agent writes**

  ```javascript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  // The agent has already classified each ticket; this routes every item to
  // the right specialist and collects the handled results.
  const SPECIALIST = { bug: "bug-fixer", feature: "feature-analyst", question: "support-agent" };

  const handled = await Promise.all(
    tickets.map((ticket) =>
      task({
        description: `Handle this ${ticket.category}:\n${ticket.text}`,
        subagentType: SPECIALIST[ticket.category],
      }),
    ),
  );
  // ... group handled results by category into a single triage report
  handled;
  ```
</Accordion>

### Fan-out and synthesize

The agent dispatches the same kind of work across many items in parallel, then combines the results.

```mermaid theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
graph LR
    Items[Items] --> W1[Worker]
    Items --> W2[Worker]
    Items --> W3[Worker]
    W1 --> Collect[Collect]
    W2 --> Collect
    W3 --> Collect
    Collect --> Synth[Synthesize]
```

**Use cases:** Code review across a directory, analyzing a batch of documents, processing log files, running the same check across many services.

<Accordion title="Example: fan-out and synthesize">
  **What you configure**

  ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from deepagents import create_deep_agent
  from langchain_quickjs import CodeInterpreterMiddleware

  agent = create_deep_agent(
      model="openai:gpt-5.5",
      subagents=[{
          "name": "reviewer",
          "description": "Reviews code for security issues, citing lines and severity",
          "system_prompt": "You are a security-focused code reviewer. Read the file carefully and report any authentication or authorization issues with line numbers and severity.",
      }],
      middleware=[CodeInterpreterMiddleware()],
  )

  result = await agent.ainvoke({
      "messages": [{"role": "user", "content": "Review all the route handlers in src/routes/ for authentication issues. Summarize the top risks."}]
  })
  ```

  **What the agent writes**

  ```javascript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  // One reviewer per file, dispatched in parallel, then findings merged.
  const files = (await tools.glob({ pattern: "src/routes/**/*.ts" }))
    .split("\n")
    .filter(Boolean);

  const reviews = await Promise.all(
    files.map((file) =>
      task({
        description: `Review ${file} for authentication issues. Cite line numbers.`,
        subagentType: "reviewer",
        responseSchema: issuesSchema, // -> { issues: [{ file, line, severity }] }
      }),
    ),
  );

  const issues = reviews.flatMap((r) => r.issues);
  // ... sort by severity, drop duplicates, summarize the top risks
  issues;
  ```
</Accordion>

### Adversarial verification

A two-pass pattern. The first pass produces findings. The second pass sends each finding to independent verifiers, and only findings that survive agreement are kept. This reduces false positives when confidence matters more than speed.

```mermaid theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
graph LR
    Items[Items] --> Workers[Workers]
    Workers --> Findings[Findings]
    Findings --> V1[Verifier]
    Findings --> V2[Verifier]
    Findings --> V3[Verifier]
    V1 --> Vote[Majority vote]
    V2 --> Vote
    V3 --> Vote
    Vote --> Confirmed[Confirmed]
```

**Use cases:** Security audits where false positives are costly, compliance checks, any review where you need high confidence in findings.

<Accordion title="Example: adversarial verification">
  **What you configure**

  ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  agent = create_deep_agent(
      model="openai:gpt-5.5",
      subagents=[
          {
              "name": "reviewer",
              "description": "Finds potential security vulnerabilities in code",
              "system_prompt": "You are a security auditor. Find potential vulnerabilities and report each with file, line, and description.",
          },
          {
              "name": "verifier",
              "description": "Independently verifies whether a reported vulnerability is real",
              "system_prompt": "You are a security verification specialist. Given a reported vulnerability, independently verify whether it is exploitable. Be skeptical. Only confirm real issues.",
          },
      ],
      middleware=[CodeInterpreterMiddleware()],
  )

  result = await agent.ainvoke({
      "messages": [{"role": "user", "content": "Do a thorough security audit of the payments module. I only want confirmed vulnerabilities, not maybes."}]
  })
  ```

  **What the agent writes**

  ```javascript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  // Pass 1: audit. Pass 2: verify each finding independently; keep only confirmed.
  const { findings } = await task({
    description: "Audit the payments module for vulnerabilities.",
    subagentType: "auditor",
    responseSchema: findingsSchema, // -> { findings: [{ id, file, line, description }] }
  });

  const verdicts = await Promise.all(
    findings.map((f) =>
      task({
        description: `Verify ${f.file}:${f.line} (${f.description}). Confirm or refute.`,
        subagentType: "verifier",
        responseSchema: verdictSchema, // -> { confirmed: boolean }
      }),
    ),
  );

  const confirmed = findings.filter((_, i) => verdicts[i]?.confirmed);
  // ... report only the confirmed vulnerabilities
  confirmed;
  ```
</Accordion>

### Generate and filter

Multiple subagents generate independent solutions to the same problem. The agent compares, scores, and filters the results in code, keeping only the best.

```mermaid theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
graph LR
    Prompt[Prompt] --> G1[Generator]
    Prompt --> G2[Generator]
    Prompt --> G3[Generator]
    G1 --> Filter[Filter + rank]
    G2 --> Filter
    G3 --> Filter
    Filter --> Best[Best result]
```

**Use cases:** Architecture proposals, refactoring strategies, content variations, any task where exploring multiple options before committing produces a better outcome.

<Accordion title="Example: generate and filter">
  **What you configure**

  ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  agent = create_deep_agent(
      model="openai:gpt-5.5",
      subagents=[{
          "name": "architect",
          "description": "Proposes a database schema design with tradeoff analysis",
          "system_prompt": "You are a database architect. Propose a schema design for the given requirements. Include tradeoffs, migration considerations, and a clear rationale.",
      }],
      middleware=[CodeInterpreterMiddleware()],
  )

  result = await agent.ainvoke({
      "messages": [{"role": "user", "content": "Generate three different approaches to restructure the database schema for the orders system, then pick the best one."}]
  })
  ```

  **What the agent writes**

  ```javascript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  // Generate independent proposals in parallel, then score and keep the best.
  const proposals = await Promise.all(
    [1, 2, 3].map((n) =>
      task({
        description: `Approach ${n}: redesign the orders schema, with tradeoffs.`,
        subagentType: "architect",
        responseSchema: designSchema, // -> { design, tradeoffs }
      }),
    ),
  );

  // ... score each proposal against the requirements
  const best = proposals.sort((a, b) => score(b) - score(a))[0];
  best;
  ```
</Accordion>

### Tournament

Variations are compared head-to-head by a judge subagent, with winners advancing through elimination rounds.

```mermaid theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
graph LR
    A1[Attempt] --> J1{Judge}
    A2[Attempt] --> J1
    A3[Attempt] --> J2{Judge}
    A4[Attempt] --> J2
    J1 --> JF{Final}
    J2 --> JF
    JF --> Winner[Winner]
```

**Use cases:** Optimization under subjective criteria, style selection, choosing between competing implementations.

<Accordion title="Example: tournament">
  **What you configure**

  ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  agent = create_deep_agent(
      model="openai:gpt-5.5",
      subagents=[
          {
              "name": "writer",
              "description": "Rewrites a function with a focus on readability and clarity",
              "system_prompt": "You are an expert programmer focused on clean code. Rewrite the given function to maximize readability. Explain your choices.",
          },
          {
              "name": "judge",
              "description": "Compares two code implementations and picks the more readable one",
              "system_prompt": "You are a code quality judge. Compare two implementations and pick the more readable one. Justify your choice with specific criteria.",
          },
      ],
      middleware=[CodeInterpreterMiddleware()],
  )

  result = await agent.ainvoke({
      "messages": [{"role": "user", "content": "Rewrite the processOrder function in src/checkout.ts five different ways and find the most readable version."}]
  })
  ```

  **What the agent writes**

  ```javascript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  // Generate variants, then judge pairwise until a single winner remains.
  let bracket = await Promise.all(
    [1, 2, 3, 4, 5].map((n) =>
      task({ description: `Rewrite processOrder for readability (variant ${n}).`, subagentType: "writer" }),
    ),
  );

  while (bracket.length > 1) {
    const winners = [];
    for (let i = 0; i < bracket.length; i += 2) {
      if (bracket[i + 1] === undefined) { winners.push(bracket[i]); break; }
      const { winner } = await task({
        description: `Pick the more readable:\n\nA:\n${bracket[i]}\n\nB:\n${bracket[i + 1]}`,
        subagentType: "judge",
        responseSchema: pickSchema, // -> { winner: "A" | "B" }
      });
      winners.push(winner === "A" ? bracket[i] : bracket[i + 1]);
    }
    bracket = winners;
  }
  bracket[0]; // the winning rewrite
  ```
</Accordion>

### Loop until done

The agent runs a discovery loop, deduplicating against what it has already found, until no new results appear. Useful when the scope of the work is not known upfront.

```mermaid theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
graph LR
    Agent[Agent] --> Check{New findings?}
    Check --> |yes| Agent
    Check --> |no| Done[Done]
```

**Use cases:** Exhaustive search, dead code detection, dependency audits, any sweep where you want completeness rather than a fixed number of results.

<Accordion title="Example: loop until done">
  **What you configure**

  ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  agent = create_deep_agent(
      model="openai:gpt-5.5",
      subagents=[{
          "name": "analyzer",
          "description": "Analyzes code for unused exports, functions, and dead code paths",
          "system_prompt": "You are a code analyst specializing in dead code detection. Find unused exports, unreachable functions, and orphaned modules. Report each with file path and evidence.",
      }],
      middleware=[CodeInterpreterMiddleware()],
  )

  result = await agent.ainvoke({
      "messages": [{"role": "user", "content": "Find all the dead code in this repo. Be thorough. I want every unused export and unreachable function."}]
  })
  ```

  **What the agent writes**

  ```javascript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  // Keep dispatching rounds, deduping against what's found, until a round adds nothing.
  const seen = new Set();
  const found = [];

  while (true) {
    const { items } = await task({
      description: `Find dead code. Already found: ${[...seen].join(", ") || "(none)"}.`,
      subagentType: "analyzer",
      responseSchema: itemsSchema, // -> { items: [{ id, file }] }
    });
    const fresh = items.filter((i) => !seen.has(i.id));
    if (fresh.length === 0) break; // converged: nothing new
    for (const i of fresh) { seen.add(i.id); found.push(i); }
  }
  found;
  ```
</Accordion>

<Warning>
  `task()` dispatches from inside an already-running `eval` call. It does not go through the normal tool calling path, so `interrupt_on` approval workflows on the parent agent are not enforced per dispatch. Gate the `eval` tool itself if you need approval before subagent orchestration runs.
</Warning>

## Disable programmatic subagents

Subagent dispatch is on by default whenever the agent has subagents. Disable it if you want subagents to be available only through the normal `task` tool path.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from deepagents import create_deep_agent
from langchain_quickjs import CodeInterpreterMiddleware

agent = create_deep_agent(
    model="openai:gpt-5.5",
    subagents=[{"name": "reviewer", "description": "Reviews code", "system_prompt": "Review code."}],
    middleware=[CodeInterpreterMiddleware(subagents=False)],
)
```

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/deepagents/programmatic-subagents.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Quickstart
Source: https://docs.langchain.com/oss/python/deepagents/quickstart

Build your first deep agent in minutes

This guide walks you through creating your first deep agent with planning, file system tools, and subagent capabilities. You'll build a research agent that can conduct research and write reports.

<Tip>
  **Using an AI coding assistant?**

  * Install the [LangChain Docs MCP server](/use-these-docs) to give your agent access to up-to-date LangChain documentation and examples.
  * Install [LangChain Skills](https://github.com/langchain-ai/langchain-skills) to improve your agent's performance on LangChain ecosystem tasks.
</Tip>

## Prerequisites

Before you begin, make sure you have an API key from a model provider (e.g., Gemini, Anthropic, OpenAI).

<Note>
  Deep Agents require a model that supports [tool calling](/oss/python/langchain/models#tool-calling). See [customization](/oss/python/deepagents/customization#model) for how to configure your model.
</Note>

## Step 1: Install dependencies

<CodeGroup>
  ```bash pip theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  pip install deepagents tavily-python
  ```

  ```bash uv theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  uv init
  uv add deepagents tavily-python
  uv sync
  ```
</CodeGroup>

<Note>
  This guide uses [Tavily](https://tavily.com/) as an example search provider, but you can substitute any search API (e.g., DuckDuckGo, SerpAPI, Brave Search).
</Note>

## Step 2: Set up your API keys

<Tabs>
  <Tab title="Google">
    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    export GOOGLE_API_KEY="your-api-key"
    export TAVILY_API_KEY="your-tavily-api-key"
    ```
  </Tab>

  <Tab title="OpenAI">
    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    export OPENAI_API_KEY="your-api-key"
    export TAVILY_API_KEY="your-tavily-api-key"
    ```
  </Tab>

  <Tab title="Anthropic">
    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    export ANTHROPIC_API_KEY="your-api-key"
    export TAVILY_API_KEY="your-tavily-api-key"
    ```
  </Tab>

  <Tab title="OpenRouter">
    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    export OPENROUTER_API_KEY="your-api-key"
    export TAVILY_API_KEY="your-tavily-api-key"
    ```
  </Tab>

  <Tab title="Fireworks">
    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    export FIREWORKS_API_KEY="your-api-key"
    export TAVILY_API_KEY="your-tavily-api-key"
    ```
  </Tab>

  <Tab title="Baseten">
    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    export BASETEN_API_KEY="your-api-key"
    export TAVILY_API_KEY="your-tavily-api-key"
    ```
  </Tab>

  <Tab title="Ollama">
    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    # Local: Ollama must be running on your machine
    # Cloud: Set your Ollama API key for hosted inference
    export OLLAMA_API_KEY="your-api-key"
    export TAVILY_API_KEY="your-tavily-api-key"
    ```
  </Tab>

  <Tab title="Other">
    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    # Set the API key for your provider
    export <PROVIDER>_API_KEY="your-api-key"
    export TAVILY_API_KEY="your-tavily-api-key"
    ```

    Deep Agents work with any [LangChain chat model](/oss/python/deepagents/models#supported-models). Set the API key for your provider.
  </Tab>
</Tabs>

## Step 3: Create a search tool

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import os
from typing import Literal

from tavily import TavilyClient
from deepagents import create_deep_agent

tavily_client = TavilyClient(api_key=os.environ["TAVILY_API_KEY"])

def internet_search(
    query: str,
    max_results: int = 5,
    topic: Literal["general", "news", "finance"] = "general",
    include_raw_content: bool = False,
):
    """Run a web search"""
    return tavily_client.search(
        query,
        max_results=max_results,
        include_raw_content=include_raw_content,
        topic=topic,
    )
```

## Step 4: Create a deep agent

Pass a `model` string in `provider:model` format, or an [initialized model instance](/oss/python/deepagents/models#configure-model-parameters). See [supported models](/oss/python/deepagents/models#supported-models) for all providers and [suggested models](/oss/python/deepagents/models#suggested-models) for tested recommendations.

<CodeGroup>
  ```python Google theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  # System prompt to steer the agent to be an expert researcher
  research_instructions = """You are an expert researcher. Your job is to conduct thorough research and then write a polished report.

  You have access to an internet search tool as your primary means of gathering information.

  ## `internet_search`

  Use this to run an internet search for a given query. You can specify the max number of results to return, the topic, and whether raw content should be included.
  """

  agent = create_deep_agent(
      model="google_genai:gemini-3.5-flash",
      tools=[internet_search],
      system_prompt=research_instructions,
  )
  ```

  ```python OpenAI theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  # System prompt to steer the agent to be an expert researcher
  research_instructions = """You are an expert researcher. Your job is to conduct thorough research and then write a polished report.

  You have access to an internet search tool as your primary means of gathering information.

  ## `internet_search`

  Use this to run an internet search for a given query. You can specify the max number of results to return, the topic, and whether raw content should be included.
  """

  agent = create_deep_agent(
      model="openai:gpt-5.5",
      tools=[internet_search],
      system_prompt=research_instructions,
  )
  ```

  ```python Anthropic theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  # System prompt to steer the agent to be an expert researcher
  research_instructions = """You are an expert researcher. Your job is to conduct thorough research and then write a polished report.

  You have access to an internet search tool as your primary means of gathering information.

  ## `internet_search`

  Use this to run an internet search for a given query. You can specify the max number of results to return, the topic, and whether raw content should be included.
  """

  agent = create_deep_agent(
      model="anthropic:claude-sonnet-4-6",
      tools=[internet_search],
      system_prompt=research_instructions,
  )
  ```

  ```python OpenRouter theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  # System prompt to steer the agent to be an expert researcher
  research_instructions = """You are an expert researcher. Your job is to conduct thorough research and then write a polished report.

  You have access to an internet search tool as your primary means of gathering information.

  ## `internet_search`

  Use this to run an internet search for a given query. You can specify the max number of results to return, the topic, and whether raw content should be included.
  """

  agent = create_deep_agent(
      model="openrouter:anthropic/claude-sonnet-4-6",
      tools=[internet_search],
      system_prompt=research_instructions,
  )
  ```

  ```python Fireworks theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  # System prompt to steer the agent to be an expert researcher
  research_instructions = """You are an expert researcher. Your job is to conduct thorough research and then write a polished report.

  You have access to an internet search tool as your primary means of gathering information.

  ## `internet_search`

  Use this to run an internet search for a given query. You can specify the max number of results to return, the topic, and whether raw content should be included.
  """

  agent = create_deep_agent(
      model="fireworks:accounts/fireworks/models/qwen3p5-397b-a17b",
      tools=[internet_search],
      system_prompt=research_instructions,
  )
  ```

  ```python Baseten theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  # System prompt to steer the agent to be an expert researcher
  research_instructions = """You are an expert researcher. Your job is to conduct thorough research and then write a polished report.

  You have access to an internet search tool as your primary means of gathering information.

  ## `internet_search`

  Use this to run an internet search for a given query. You can specify the max number of results to return, the topic, and whether raw content should be included.
  """

  agent = create_deep_agent(
      model="baseten:zai-org/GLM-5",
      tools=[internet_search],
      system_prompt=research_instructions,
  )
  ```

  ```python Ollama theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  # System prompt to steer the agent to be an expert researcher
  research_instructions = """You are an expert researcher. Your job is to conduct thorough research and then write a polished report.

  You have access to an internet search tool as your primary means of gathering information.

  ## `internet_search`

  Use this to run an internet search for a given query. You can specify the max number of results to return, the topic, and whether raw content should be included.
  """

  agent = create_deep_agent(
      model="ollama:devstral-2",
      tools=[internet_search],
      system_prompt=research_instructions,
  )
  ```
</CodeGroup>

## Step 5: Run the agent

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
result = agent.invoke({"messages": [{"role": "user", "content": "What is langgraph?"}]})

# Print the agent's response
print(result["messages"][-1].content)
```

<Tip>
  Trace your agent's planning steps, tool calls, and subagent delegation with [LangSmith](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=oss-deepagents-quickstart). Follow the [observability quickstart](/langsmith/observability-quickstart) to get set up.

  We recommend you also set up [LangSmith Engine](/langsmith/engine), which monitors your traces, detects issues, and proposes fixes.
</Tip>

## How does it work?

Your deep agent automatically:

1. **Plans its approach** using the built-in [`write_todos`](/oss/python/deepagents/harness#task-planning) tool to break down the research task.
2. **Conducts research** by calling the `internet_search` tool to gather information.
3. **Manages context** by using file system tools ([`write_file`](/oss/python/deepagents/harness#virtual-filesystem-access), [`read_file`](/oss/python/deepagents/harness#virtual-filesystem-access)) to offload large search results.
4. **Spawns subagents** as needed to delegate complex subtasks to specialized subagents.
5. **Synthesizes a report** to compile findings into a coherent response.

## Examples

For agents, patterns, and applications you can build with Deep Agents, see [Examples](https://github.com/langchain-ai/deepagents/tree/main/examples).

## Streaming

Deep Agents have built-in [streaming](/oss/python/langchain/event-streaming) for real-time updates from agent execution using LangGraph.
This allows you to observe output progressively and review and debug agent and subagent work, such as tool calls, tool results, and LLM responses.

## Next steps

Now that you've built your first deep agent:

* **Customize your agent**: Learn about [customization options](/oss/python/deepagents/customization), including custom system prompts, tools, and subagents.
* **Add long-term memory**: Enable [persistent memory](/oss/python/deepagents/memory) across conversations.
* **Deploy to production**: Use [Managed Deep Agents](/langsmith/managed-deep-agents-overview) to create, run, and operate deep agents in LangSmith.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/deepagents/quickstart.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
