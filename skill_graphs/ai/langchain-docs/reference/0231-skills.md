# Skills
Source: https://docs.langchain.com/oss/python/deepagents/skills

Learn how to extend your deep agent's capabilities with skills

Skills package domain expertise, such as workflows, best practices, scripts, reference docs, and templates, into reusable directories. The agent gets a summary of the contents on startup and discovers and reads the contained files only when relevant.

Skills help you avoid context bloat by loading only summaries at startup and reading full instructions when a task requires them. You can share skills across agents and projects, and compose multiple skills in a single agent so each one covers a distinct capability.

<Tip>
  For ready-to-use skills that improve your agent's performance on LangChain ecosystem tasks, see the [LangChain Skills](https://github.com/langchain-ai/langchain-skills) repository.
</Tip>

## Usage

<Steps>
  <Step title="Create a top-level skills directory">
    Create a directory to hold all skills for your project, such as `skills/` under your backend root.
  </Step>

  <Step title="Create a subdirectory inside your skills directory for your skill">
    Each skill is a directory containing a `SKILL.md` file: a markdown file with YAML [frontmatter](#frontmatter-fields) (`name` and `description`) followed by instructions the agent follows when the skill is activated. A skill directory can also optionally include supporting files such as scripts, reference docs, and templates.

    <Tree>
      <Tree.Folder name="skills">
        <Tree.Folder name="langgraph-docs">
          <Tree.File name="SKILL.md" />

          <Tree.Folder name="scripts">
            <Tree.File name="fetch_docs.py" />
          </Tree.Folder>

          <Tree.Folder name="references">
            <Tree.File name="api-patterns.md" />

            <Tree.File name="style-guide.md" />
          </Tree.Folder>

          <Tree.Folder name="assets">
            <Tree.File name="report-template.md" />

            <Tree.File name="schema.json" />
          </Tree.Folder>
        </Tree.Folder>
      </Tree.Folder>
    </Tree>

    Deep agent skills follow the [Agent Skills specification](https://agentskills.io/specification).
  </Step>

  <Step title="Add a `SKILL.md` file with YAML frontmatter and instructions.">
    The `SKILL.md` starts with YAML [frontmatter](#frontmatter-fields) followed by markdown instructions:

    ```md theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    ---
    name: langgraph-docs
    description: Use this skill for requests related to LangGraph in order to fetch relevant documentation to provide accurate, up-to-date guidance.
    ---

    # langgraph-docs

    ## Overview

    This skill explains how to access LangGraph documentation to help answer questions and guide implementation.

    ## Instructions

    ### 1. Fetch the documentation index

    Use the fetch_url tool to read the following URL:
    https://docs.langchain.com/llms.txt

    This provides a structured list of all available documentation with descriptions.

    ### 2. Select relevant documentation

    Based on the question, identify 2-4 most relevant documentation URLs from the index. Prioritize:

    - Specific how-to guides for implementation questions
    - Core concept pages for understanding questions
    - Tutorials for end-to-end examples
    - Reference docs for API details

    ### 3. Fetch and synthesize

    Use the fetch_url tool to read the selected documentation URLs, then answer the user's question. Give a direct answer first, include the minimum necessary context, and link to the source pages rather than quoting long passages.
    ```

    <Note>
      Reference any [supporting resources](#add-supporting-resources) in your `SKILL.md` with a description of what each file contains and when to use it. The agent discovers these files through the references in the skill instructions.
    </Note>
  </Step>

  <Step title="Pass the skills path when creating your agent">
    Pass the path to your top-level skills directory in the `skills` argument when creating your agent:

    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    from deepagents import create_deep_agent
    from deepagents.backends.filesystem import FilesystemBackend

    backend = FilesystemBackend(root_dir="./my-project")

    agent = create_deep_agent(
        model="anthropic:claude-sonnet-4-6",
        backend=backend,
        skills=["./my-project/skills/"],
    )
    ```

    This example uses `FilesystemBackend` to load skills from disk. For other storage options, including loading skills from remote sources, see [Backends and remote skill loading](#backends-and-remote-skill-loading).

    <ParamField type="list[str]">
      List of skill source paths.

      Paths must be specified using forward slashes and are relative to the backend's root.

      * If omitted, no skills are loaded.
      * When using `StateBackend` (default), provide skill files with `invoke(files={...})`. Use `create_file_data()` from `deepagents.backends.utils` to format file contents; raw strings are not supported.
      * With `FilesystemBackend`, skills are loaded from disk relative to the backend's `root_dir`.

      Later sources override earlier ones for skills with the same name (last one wins).

      <Note>
        When multiple skill sources contain a skill with the same name, the skill from the source listed later in the `skills` array takes precedence (last one wins). This lets you layer skills from different origins, such as base skills overridden by project-specific versions.
      </Note>
    </ParamField>
  </Step>

  <Step title="Invoke the agent">
    Send a task to the agent with `invoke()`. At startup, the agent loads each skill's [`name`](#frontmatter-fields) and [`description`](#frontmatter-fields) from [frontmatter](#frontmatter-fields) into the system prompt. When your task matches a skill's description, the agent reads that skill's `SKILL.md` and follows its instructions.

    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    result = agent.invoke(
        {"messages": [{"role": "user", "content": "What is LangGraph?"}]},
        config={"configurable": {"thread_id": "1"}},
    )
    ```
  </Step>
</Steps>

## How skills work

As agents take on more complex tasks, the context they need grows with them. Loading all instructions into the system prompt wastes tokens on information irrelevant to the current task, and providing the same guidance manually across sessions does not scale.

<Info>
  Skills use **progressive disclosure**: the agent loads skill information in layers instead of all at once. At startup, it sees only each skill's name and description. When a skill is invoked, it reads the full `SKILL.md` instructions. Supporting files load afterward, only when the instructions call for them.
</Info>

Skills load in three levels. Each level adds more detail only when the task needs it:

| Level               | What loads                                                                                                                | When                                                             |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| **1. Metadata**     | [`name`](#frontmatter-fields) and [`description`](#frontmatter-fields) from `SKILL.md` [frontmatter](#frontmatter-fields) | Agent startup, for every configured skill                        |
| **2. Instructions** | Full `SKILL.md` body                                                                                                      | When the skill is invoked                                        |
| **3. Resources**    | [Supporting files](#add-supporting-resources) under `scripts/`, `references/`, and `assets/`                              | As needed after invocation, when the instructions reference them |

The following diagram shows what appears in agent context at a given moment. At startup, level 1 metadata for every skill is in the system prompt. When a skill is invoked, level 2 instructions join the context. Level 3 files stay on the backend until the agent reads them after invocation.

<div>
  <img alt="How skill components map into agent context at startup and activation" />
</div>

As the agent works through a task, it loads skill information in layers:

<div>
  <img alt="How skills load in layers from metadata to instructions to resources" />
</div>

In Deep Agents, [`SkillsMiddleware`](https://reference.langchain.com/python/deepagents/middleware/skills/SkillsMiddleware) (part of the [default middleware stack](/oss/python/deepagents/customization#default-stack-main-agent) when you pass `skills`) handles the first two levels, with the third level being handled by the LLM:

1. **Discovery** (level 1): At agent start, the middleware scans the configured skill paths, parses each `SKILL.md` [frontmatter](#frontmatter-fields), and injects the [`name`](#frontmatter-fields) and [`description`](#frontmatter-fields) fields into the system prompt.
2. **Read** (level 2): When the agent invokes a skill, it reads the full `SKILL.md` content via `read_file`.
3. **Execute** (level 3): After invocation, the agent follows the skill's instructions and reads supporting files (scripts, references, assets) only as the instructions require.

## When to use skills

If you find yourself giving similar instructions to an agent, especially if they are detailed and contain multiple steps, consider codifying the instructions for the agent. That way, in future when you want to accomplish a similar task, the agent will already know what to do.

<Tip>
  You can also ask your agent to write a skill for a task you worked on with the agent.
</Tip>

Skills are especially helpful for codifying:

* **Step-by-step workflows**: Workflows that span multiple steps, similar to recipes.
* **Domain-specific knowledge**: Instruct the agent on how to use tools for the workflow. For example, include information on where to pull information from, including other reference information or scripts that the skill may have access to.
* **Instructions with executable code**: Bundle procedures with scripts or modules the agent can run, so it follows tested logic instead of regenerating it from instructions each time. See [Execute code with skills](#execute-code-with-skills).
* **Guidelines**: Provide the agent with supporting instructions about guardrails to adhere to. For example, following a specific format or style guide, or specifying to always run tests as part of the workflow.

## Write effective skills

The [Agent Skills specification](https://agentskills.io/specification) includes guidance on structuring skills for reliable discovery and activation. The following recommendations build on that foundation with practical patterns for Deep Agents.

**Keep [frontmatter](#frontmatter-fields) concise** and the `SKILL.md` body under 5,000 tokens. Every skill's frontmatter is added to the system prompt at [discovery](#how-skills-work), while the full body is only read when activated. Keeping both layers small means you can load many skills without crowding the context window.

**Write specific descriptions.** During [discovery](#how-skills-work), the [`description`](#frontmatter-fields) field is the only information the agent sees for each skill. A good description tells the agent both what the skill does and when to activate it, with specific keywords the agent can match against:

```yaml theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}

# Good: specific about what and when
description: >-
  Extract text and tables from PDF files, fill PDF forms, and merge
  multiple PDFs. Use when working with PDF documents or when the user
  mentions PDFs, forms, or document extraction.

# Poor: too vague for reliable matching
description: Helps with PDFs.
```

When you have multiple skills in related domains, differentiate their descriptions clearly. Overlapping descriptions cause the agent to activate the wrong skill or hesitate between options. If two skills serve similar purposes, consolidate them into one.

**Keep instructions focused.** The Agent Skills specification recommends keeping your `SKILL.md` under 500 lines. When instructions grow longer, move detailed reference material into [supporting resource files](#add-supporting-resources) and reference them from the main `SKILL.md`:

<Tree>
  <Tree.Folder name="skills">
    <Tree.Folder name="data-pipeline">
      <Tree.File name="SKILL.md" />

      <Tree.Folder name="references">
        <Tree.File name="schema-reference.md" />

        <Tree.File name="error-codes.md" />
      </Tree.Folder>
    </Tree.Folder>
  </Tree.Folder>
</Tree>

The agent loads reference files only when the instructions call for them, keeping each layer of progressive disclosure appropriately sized. Keep file references one level deep from `SKILL.md` and avoid deeply nested reference chains, which force the agent through multiple reads to reach the information it needs.

**Structure instructions for the agent.** Write your `SKILL.md` body as clear instructions the agent can follow:

* **Step-by-step procedures** for multi-step workflows
* **Decision criteria** for choosing between approaches
* **Examples of expected inputs and outputs** so the agent knows what success looks like
* **Edge cases** the agent should handle or flag to the user

**Manage skill count.** Fewer well-scoped skills outperform many overlapping ones. As the number of skills with similar descriptions grows, the agent's ability to select the right one degrades. If you find yourself with many related skills, consider:

* Consolidating related capabilities into a single skill with sections for each sub-task
* Using reference files to keep the main `SKILL.md` concise while covering multiple sub-tasks

<Tip>
  Use the [`skills-ref` validation tool](https://github.com/agentskills/agentskills/tree/main/skills-ref) to check that your `SKILL.md` [frontmatter](#frontmatter-fields) follows the Agent Skills specification naming and format conventions.
</Tip>

## Add supporting resources

Beyond `SKILL.md`, a skill directory can include any additional files or directories. The [Agent Skills specification](https://agentskills.io/specification) defines three optional directories for common resource types. Deep Agents does not load these files at discovery or activation. The agent reads or executes them only when your `SKILL.md` instructions say to.

### `scripts/`

The `scripts/` directory holds executable code the agent can run, such as API clients, data transforms, or validation checks. Scripts should:

* Be self-contained or clearly document dependencies
* Include helpful error messages
* Handle edge cases gracefully

Supported languages depend on your agent setup. Common options include Python, Bash, and JavaScript or TypeScript. To execute scripts rather than only read them, see [Execute code with skills](#execute-code-with-skills). Use [sandbox scripts](#sandbox-scripts) when the agent needs a shell.

### `references/`

The `references/` directory holds supplementary documentation the agent reads on demand. Use it for material that is too detailed for `SKILL.md` but still task-specific, such as:

* `REFERENCE.md` for detailed technical reference
* `FORMS.md` for form templates or structured data formats
* Domain-specific guides (`finance.md`, `legal.md`, and similar)

Keep individual reference files focused. The agent loads them only when needed, so smaller files use less context.

### `assets/`

The `assets/` directory holds static resources the agent uses but does not need to read as instructions, such as:

* Document or configuration templates
* Images (diagrams, examples)
* Data files (lookup tables, schemas)

Describe in `SKILL.md` when the agent should open or copy each asset.

### Reference files from `SKILL.md`

When you reference supporting files, use paths relative to the skill root:

```md theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
For API details, see the [reference guide](references/api-patterns.md).

To extract tables from a PDF, run:
scripts/extract.py
```

For each file you reference, state what it contains and when the agent should use it. Keep references one level deep from `SKILL.md`. Avoid deeply nested reference chains that force the agent through multiple reads to reach the information it needs.

## Backends and remote skill loading

Deep Agents supports different backends depending on how you want to store and manage skill files:

* `StateBackend`: Stores files in LangGraph agent state for the current thread.
* `StoreBackend`: Stores files in a LangGraph store for durable, cross-thread storage.
* `FilesystemBackend`: Reads and writes skill files from disk under a configurable `root_dir`.

<Tabs>
  <Tab title="StateBackend">
    <CodeGroup>
      ```python Google theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      from urllib.request import urlopen
      from deepagents import create_deep_agent
      from deepagents.backends import StateBackend
      from deepagents.backends.utils import create_file_data
      from langgraph.checkpoint.memory import MemorySaver

      checkpointer = MemorySaver()
      backend = StateBackend()

      skill_url = "https://raw.githubusercontent.com/langchain-ai/deepagents/refs/heads/main/libs/cli/examples/skills/langgraph-docs/SKILL.md"
      with urlopen(skill_url) as response:
          skill_content = response.read().decode('utf-8')

      skills_files = {
          "/skills/langgraph-docs/SKILL.md": create_file_data(skill_content),
      }

      agent = create_deep_agent(
          model="google_genai:gemini-3.5-flash",
          backend=backend,
          skills=["/skills/"],
          checkpointer=checkpointer,
      )

      result = agent.invoke(
          {
              "messages": [{"role": "user", "content": "What is langgraph?"}],
              # Seed the default StateBackend's in-state filesystem (virtual paths must start with "/").
              "files": skills_files,
          },
          config={"configurable": {"thread_id": "12345"}},
      )
      ```

      ```python OpenAI theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      from urllib.request import urlopen
      from deepagents import create_deep_agent
      from deepagents.backends import StateBackend
      from deepagents.backends.utils import create_file_data
      from langgraph.checkpoint.memory import MemorySaver

      checkpointer = MemorySaver()
      backend = StateBackend()

      skill_url = "https://raw.githubusercontent.com/langchain-ai/deepagents/refs/heads/main/libs/cli/examples/skills/langgraph-docs/SKILL.md"
      with urlopen(skill_url) as response:
          skill_content = response.read().decode('utf-8')

      skills_files = {
          "/skills/langgraph-docs/SKILL.md": create_file_data(skill_content),
      }

      agent = create_deep_agent(
          model="openai:gpt-5.5",
          backend=backend,
          skills=["/skills/"],
          checkpointer=checkpointer,
      )

      result = agent.invoke(
          {
              "messages": [{"role": "user", "content": "What is langgraph?"}],
              # Seed the default StateBackend's in-state filesystem (virtual paths must start with "/").
              "files": skills_files,
          },
          config={"configurable": {"thread_id": "12345"}},
      )
      ```

      ```python Anthropic theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      from urllib.request import urlopen
      from deepagents import create_deep_agent
      from deepagents.backends import StateBackend
      from deepagents.backends.utils import create_file_data
      from langgraph.checkpoint.memory import MemorySaver

      checkpointer = MemorySaver()
      backend = StateBackend()

      skill_url = "https://raw.githubusercontent.com/langchain-ai/deepagents/refs/heads/main/libs/cli/examples/skills/langgraph-docs/SKILL.md"
      with urlopen(skill_url) as response:
          skill_content = response.read().decode('utf-8')

      skills_files = {
          "/skills/langgraph-docs/SKILL.md": create_file_data(skill_content),
      }

      agent = create_deep_agent(
          model="anthropic:claude-sonnet-4-6",
          backend=backend,
          skills=["/skills/"],
          checkpointer=checkpointer,
      )

      result = agent.invoke(
          {
              "messages": [{"role": "user", "content": "What is langgraph?"}],
              # Seed the default StateBackend's in-state filesystem (virtual paths must start with "/").
              "files": skills_files,
          },
          config={"configurable": {"thread_id": "12345"}},
      )
      ```

      ```python OpenRouter theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      from urllib.request import urlopen
      from deepagents import create_deep_agent
      from deepagents.backends import StateBackend
      from deepagents.backends.utils import create_file_data
      from langgraph.checkpoint.memory import MemorySaver

      checkpointer = MemorySaver()
      backend = StateBackend()

      skill_url = "https://raw.githubusercontent.com/langchain-ai/deepagents/refs/heads/main/libs/cli/examples/skills/langgraph-docs/SKILL.md"
      with urlopen(skill_url) as response:
          skill_content = response.read().decode('utf-8')

      skills_files = {
          "/skills/langgraph-docs/SKILL.md": create_file_data(skill_content),
      }

      agent = create_deep_agent(
          model="openrouter:anthropic/claude-sonnet-4-6",
          backend=backend,
          skills=["/skills/"],
          checkpointer=checkpointer,
      )

      result = agent.invoke(
          {
              "messages": [{"role": "user", "content": "What is langgraph?"}],
              # Seed the default StateBackend's in-state filesystem (virtual paths must start with "/").
              "files": skills_files,
          },
          config={"configurable": {"thread_id": "12345"}},
      )
      ```

      ```python Fireworks theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      from urllib.request import urlopen
      from deepagents import create_deep_agent
      from deepagents.backends import StateBackend
      from deepagents.backends.utils import create_file_data
      from langgraph.checkpoint.memory import MemorySaver

      checkpointer = MemorySaver()
      backend = StateBackend()

      skill_url = "https://raw.githubusercontent.com/langchain-ai/deepagents/refs/heads/main/libs/cli/examples/skills/langgraph-docs/SKILL.md"
      with urlopen(skill_url) as response:
          skill_content = response.read().decode('utf-8')

      skills_files = {
          "/skills/langgraph-docs/SKILL.md": create_file_data(skill_content),
      }

      agent = create_deep_agent(
          model="fireworks:accounts/fireworks/models/qwen3p5-397b-a17b",
          backend=backend,
          skills=["/skills/"],
          checkpointer=checkpointer,
      )

      result = agent.invoke(
          {
              "messages": [{"role": "user", "content": "What is langgraph?"}],
              # Seed the default StateBackend's in-state filesystem (virtual paths must start with "/").
              "files": skills_files,
          },
          config={"configurable": {"thread_id": "12345"}},
      )
      ```

      ```python Baseten theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      from urllib.request import urlopen
      from deepagents import create_deep_agent
      from deepagents.backends import StateBackend
      from deepagents.backends.utils import create_file_data
      from langgraph.checkpoint.memory import MemorySaver

      checkpointer = MemorySaver()
      backend = StateBackend()

      skill_url = "https://raw.githubusercontent.com/langchain-ai/deepagents/refs/heads/main/libs/cli/examples/skills/langgraph-docs/SKILL.md"
      with urlopen(skill_url) as response:
          skill_content = response.read().decode('utf-8')

      skills_files = {
          "/skills/langgraph-docs/SKILL.md": create_file_data(skill_content),
      }

      agent = create_deep_agent(
          model="baseten:zai-org/GLM-5",
          backend=backend,
          skills=["/skills/"],
          checkpointer=checkpointer,
      )

      result = agent.invoke(
          {
              "messages": [{"role": "user", "content": "What is langgraph?"}],
              # Seed the default StateBackend's in-state filesystem (virtual paths must start with "/").
              "files": skills_files,
          },
          config={"configurable": {"thread_id": "12345"}},
      )
      ```

      ```python Ollama theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      from urllib.request import urlopen
      from deepagents import create_deep_agent
      from deepagents.backends import StateBackend
      from deepagents.backends.utils import create_file_data
      from langgraph.checkpoint.memory import MemorySaver

      checkpointer = MemorySaver()
      backend = StateBackend()

      skill_url = "https://raw.githubusercontent.com/langchain-ai/deepagents/refs/heads/main/libs/cli/examples/skills/langgraph-docs/SKILL.md"
      with urlopen(skill_url) as response:
          skill_content = response.read().decode('utf-8')

      skills_files = {
          "/skills/langgraph-docs/SKILL.md": create_file_data(skill_content),
      }

      agent = create_deep_agent(
          model="ollama:devstral-2",
          backend=backend,
          skills=["/skills/"],
          checkpointer=checkpointer,
      )

      result = agent.invoke(
          {
              "messages": [{"role": "user", "content": "What is langgraph?"}],
              # Seed the default StateBackend's in-state filesystem (virtual paths must start with "/").
              "files": skills_files,
          },
          config={"configurable": {"thread_id": "12345"}},
      )
      ```
    </CodeGroup>
  </Tab>

  <Tab title="StoreBackend">
    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    from urllib.request import urlopen
    from deepagents import create_deep_agent
    from deepagents.backends import StoreBackend
    from deepagents.backends.utils import create_file_data
    from langgraph.store.memory import InMemoryStore

    store = InMemoryStore()
    backend = StoreBackend(namespace=lambda _rt: ("filesystem",))

    skill_url = "https://raw.githubusercontent.com/langchain-ai/deepagents/refs/heads/main/libs/cli/examples/skills/langgraph-docs/SKILL.md"
    with urlopen(skill_url) as response:
        skill_content = response.read().decode('utf-8')

    store.put(
        namespace=("filesystem",),
        key="/skills/langgraph-docs/SKILL.md",
        value=create_file_data(skill_content),
    )

    agent = create_deep_agent(
        model="google_genai:gemini-3.5-flash",
        backend=backend,
        store=store,
        skills=["/skills/"],
    )

    result = agent.invoke(
        {"messages": [{"role": "user", "content": "What is langgraph?"}]},
        config={"configurable": {"thread_id": "12345"}},
    )
    ```
  </Tab>

  <Tab title="FilesystemBackend">
    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    from deepagents import create_deep_agent
    from deepagents.backends.filesystem import FilesystemBackend
    from langgraph.checkpoint.memory import MemorySaver

    # Checkpointer is REQUIRED for human-in-the-loop
    checkpointer = MemorySaver()
    root_dir = "/Users/user/{project}"
    backend = FilesystemBackend(root_dir=root_dir)

    agent = create_deep_agent(
        model="google_genai:gemini-3.5-flash",
        backend=backend,
        skills=[str(Path(root_dir) / "skills")],
        interrupt_on={
            "write_file": True,
            "read_file": False,
            "edit_file": True,
        },
        checkpointer=checkpointer, # Required!
    )

    result = agent.invoke(
        {"messages": [{"role": "user", "content": "What is langgraph?"}]},
        config={"configurable": {"thread_id": "12345"}},
    )
    ```
  </Tab>
</Tabs>

## Load skills at runtime

When you have a large collection of skills but only a subset is relevant for a given run, select which skills to load based on runtime context such as user role, tenant, or request type. There are two main approaches:

### Dynamic skill lists

The simplest approach is to construct the `skills` array before creating the agent. Choose which skill paths to include based on whatever runtime context you have:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from deepagents import create_deep_agent

SKILLS_BY_ROLE = {
    "engineering": ["/skills/code-review/", "/skills/testing/", "/skills/deployment/"],
    "data": ["/skills/sql-analysis/", "/skills/visualization/", "/skills/data-pipeline/"],
    "support": ["/skills/ticket-triage/", "/skills/runbook/"],
}

def create_agent_for_user(user_role: str):
    return create_deep_agent(
        model="anthropic:claude-sonnet-4-6",
        skills=SKILLS_BY_ROLE.get(user_role, []),
    )
```

This works well when skills live on disk or in a shared backend and you just need to control which ones the agent sees. The skills themselves are not duplicated — you maintain one copy and vary the paths passed to each run.

<Note>
  The SDK only loads the sources you pass in `skills`. It does not automatically scan CLI directories such as `~/.deepagents/...` or `~/.agents/...`.

  For CLI storage conventions, see [App data](/oss/python/deepagents/code/data-locations).

  <Accordion title="Emulating CLI source order in SDK">
    If you want CLI-style layering in SDK code, pass all desired sources explicitly in lowest-to-highest precedence order:

    ```text theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    [
    "<user-home>/.deepagents/{agent}/skills/",
    "<user-home>/.agents/skills/",
    "<project-root>/.deepagents/skills/",
    "<project-root>/.agents/skills/",
    ]
    ```

    Then pass that ordered list as `skills` when creating your agent.
  </Accordion>
</Note>

### Namespaced skills

For multi-tenant applications where each user's skill set is managed independently, route `/skills/` to a [StoreBackend](https://reference.langchain.com/python/deepagents/backends/store/StoreBackend) with a namespace factory. Populate each namespace with only the skills that user should have access to, and the middleware resolves to the correct set at runtime:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from deepagents import create_deep_agent
from deepagents.backends import CompositeBackend, StateBackend, StoreBackend

agent = create_deep_agent(
    model="anthropic:claude-sonnet-4-6",
    skills=["/skills/"],
    backend=CompositeBackend(
        default=StateBackend(),
        routes={
            "/skills/": StoreBackend(
                namespace=lambda rt: (
                    rt.server_info.assistant_id,
                    rt.server_info.user.identity,
                ),
            ),
        },
    ),
)
```

This pattern is useful when different users or tenants need fully independent skill libraries that can be updated separately. For a managed solution that handles skill access, sharing, and workspace-level visibility out of the box, see [Fleet skills](/langsmith/fleet/skills).

## Skills for subagents

When you use [subagents](/oss/python/deepagents/subagents), you can configure which skills each type has access to:

* **General-purpose subagent**: Automatically inherits skills from the main agent when you pass `skills` to `create_deep_agent`. No additional configuration is needed.
* **Custom subagents**: Do not inherit the main agent's skills. Add a `skills` parameter to each subagent definition with that subagent's skill source paths.

Skill state is fully isolated: the main agent's skills are not visible to subagents, and subagent skills are not visible to the main agent.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from deepagents import create_deep_agent

research_subagent = {
    "name": "researcher",
    "description": "Research assistant with specialized skills",
    "system_prompt": "You are a researcher.",
    "tools": [web_search],
    "skills": ["/skills/research/", "/skills/web-search/"],  # Subagent-specific skills
}

agent = create_deep_agent(
    model="google_genai:gemini-3.5-flash",
    skills=["/skills/main/"],  # Main agent and GP subagent get these
    subagents=[research_subagent],  # Researcher gets only its own skills
)
```

For more information on subagent configuration and skills inheritance, see [Subagents](/oss/python/deepagents/subagents).

## Skill permissions

Production deployments usually need to control three things: which skills each user can see, whether the agent can modify skill files, and whether writes require human approval. You control visibility with the `skills` argument and [backend routing](#backends-and-remote-skill-loading), access with [filesystem permissions](/oss/python/deepagents/permissions), and approval with [`interrupt_on`](/oss/python/deepagents/human-in-the-loop) or permission rules with `mode="interrupt"`.

### Share skills across users

To give every user access to the same curated library, route `/skills/` to a shared [StoreBackend](https://reference.langchain.com/python/deepagents/backends/store/StoreBackend) and seed it from your application code or an admin workflow. Use an organization-scoped namespace so all agents in that org resolve to the same store:

* Namespace by org ID for workspace-wide skills (see [Enforce read-only skills](#enforce-read-only-skills)).
* Namespace by user ID when each user needs an independent library ([namespaced skills](#namespaced-skills)).

Seed the store with keys like `/company-policies/SKILL.md` and values that include `content` and `encoding` fields. The `/skills/` route prefix is stripped before records are read from the store.

For a managed solution that handles skill access, sharing, and workspace-level visibility, see [Fleet skills](/langsmith/fleet/skills).

You can also combine shared and personal libraries: route `/skills/shared/` to an organization-scoped `StoreBackend`, route `/skills/personal/` to a user-scoped backend, and pass both paths in `skills`. See [Allow agents to edit personal skills](#allow-agents-to-edit-personal-skills).

### Limit skills by user context

Not every user should see every skill. Control which skills load at runtime based on role, tenant, or other request context. There are two main approaches:

* **[Dynamic skill lists](#dynamic-skill-lists)** — Build the `skills` array before creating the agent. Pass different path lists for different roles or request types. Works when skills live in a shared backend and you filter by path.
* **[Namespaced skills](#namespaced-skills)** — Route `/skills/` to a `StoreBackend` with a namespace factory keyed on user or tenant ID. Populate each namespace with only the skills that identity should access.

These patterns work alongside the read and write controls below. For example, you can give admins a larger skill set than engineers while keeping both libraries read-only.

### Enforce read-only skills

To share skills without letting agents modify them, route `/skills/` to a shared store and deny write operations under `/skills/**` with [filesystem permissions](/oss/python/deepagents/permissions). The agent can discover and read skills; only your application code or an admin workflow updates the store.

<CodeGroup>
  ```python Google theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from deepagents import FilesystemPermission, create_deep_agent
  from deepagents.backends import CompositeBackend, StateBackend, StoreBackend
  from langgraph.store.memory import InMemoryStore

  store = InMemoryStore()  # Good for local dev; omit for LangSmith Deployment

  agent = create_deep_agent(
      model="google_genai:gemini-3.5-flash",
      backend=CompositeBackend(
          default=StateBackend(),
          routes={
              "/skills/": StoreBackend(
                  namespace=lambda rt: ("curated-skills", rt.context.org_id),
              ),
          },
      ),
      skills=["/skills/"],
      permissions=[
          FilesystemPermission(
              operations=["write"],
              paths=["/skills/**"],
              mode="deny",
          ),
      ],
      store=store,
  )
  ```

  ```python OpenAI theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from deepagents import FilesystemPermission, create_deep_agent
  from deepagents.backends import CompositeBackend, StateBackend, StoreBackend
  from langgraph.store.memory import InMemoryStore

  store = InMemoryStore()  # Good for local dev; omit for LangSmith Deployment

  agent = create_deep_agent(
      model="openai:gpt-5.5",
      backend=CompositeBackend(
          default=StateBackend(),
          routes={
              "/skills/": StoreBackend(
                  namespace=lambda rt: ("curated-skills", rt.context.org_id),
              ),
          },
      ),
      skills=["/skills/"],
      permissions=[
          FilesystemPermission(
              operations=["write"],
              paths=["/skills/**"],
              mode="deny",
          ),
      ],
      store=store,
  )
  ```

  ```python Anthropic theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from deepagents import FilesystemPermission, create_deep_agent
  from deepagents.backends import CompositeBackend, StateBackend, StoreBackend
  from langgraph.store.memory import InMemoryStore

  store = InMemoryStore()  # Good for local dev; omit for LangSmith Deployment

  agent = create_deep_agent(
      model="anthropic:claude-sonnet-4-6",
      backend=CompositeBackend(
          default=StateBackend(),
          routes={
              "/skills/": StoreBackend(
                  namespace=lambda rt: ("curated-skills", rt.context.org_id),
              ),
          },
      ),
      skills=["/skills/"],
      permissions=[
          FilesystemPermission(
              operations=["write"],
              paths=["/skills/**"],
              mode="deny",
          ),
      ],
      store=store,
  )
  ```

  ```python OpenRouter theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from deepagents import FilesystemPermission, create_deep_agent
  from deepagents.backends import CompositeBackend, StateBackend, StoreBackend
  from langgraph.store.memory import InMemoryStore

  store = InMemoryStore()  # Good for local dev; omit for LangSmith Deployment

  agent = create_deep_agent(
      model="openrouter:anthropic/claude-sonnet-4-6",
      backend=CompositeBackend(
          default=StateBackend(),
          routes={
              "/skills/": StoreBackend(
                  namespace=lambda rt: ("curated-skills", rt.context.org_id),
              ),
          },
      ),
      skills=["/skills/"],
      permissions=[
          FilesystemPermission(
              operations=["write"],
              paths=["/skills/**"],
              mode="deny",
          ),
      ],
      store=store,
  )
  ```

  ```python Fireworks theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from deepagents import FilesystemPermission, create_deep_agent
  from deepagents.backends import CompositeBackend, StateBackend, StoreBackend
  from langgraph.store.memory import InMemoryStore

  store = InMemoryStore()  # Good for local dev; omit for LangSmith Deployment

  agent = create_deep_agent(
      model="fireworks:accounts/fireworks/models/qwen3p5-397b-a17b",
      backend=CompositeBackend(
          default=StateBackend(),
          routes={
              "/skills/": StoreBackend(
                  namespace=lambda rt: ("curated-skills", rt.context.org_id),
              ),
          },
      ),
      skills=["/skills/"],
      permissions=[
          FilesystemPermission(
              operations=["write"],
              paths=["/skills/**"],
              mode="deny",
          ),
      ],
      store=store,
  )
  ```

  ```python Baseten theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from deepagents import FilesystemPermission, create_deep_agent
  from deepagents.backends import CompositeBackend, StateBackend, StoreBackend
  from langgraph.store.memory import InMemoryStore

  store = InMemoryStore()  # Good for local dev; omit for LangSmith Deployment

  agent = create_deep_agent(
      model="baseten:zai-org/GLM-5",
      backend=CompositeBackend(
          default=StateBackend(),
          routes={
              "/skills/": StoreBackend(
                  namespace=lambda rt: ("curated-skills", rt.context.org_id),
              ),
          },
      ),
      skills=["/skills/"],
      permissions=[
          FilesystemPermission(
              operations=["write"],
              paths=["/skills/**"],
              mode="deny",
          ),
      ],
      store=store,
  )
  ```

  ```python Ollama theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from deepagents import FilesystemPermission, create_deep_agent
  from deepagents.backends import CompositeBackend, StateBackend, StoreBackend
  from langgraph.store.memory import InMemoryStore

  store = InMemoryStore()  # Good for local dev; omit for LangSmith Deployment

  agent = create_deep_agent(
      model="ollama:devstral-2",
      backend=CompositeBackend(
          default=StateBackend(),
          routes={
              "/skills/": StoreBackend(
                  namespace=lambda rt: ("curated-skills", rt.context.org_id),
              ),
          },
      ),
      skills=["/skills/"],
      permissions=[
          FilesystemPermission(
              operations=["write"],
              paths=["/skills/**"],
              mode="deny",
          ),
      ],
      store=store,
  )
  ```
</CodeGroup>

Use this for enterprise knowledge bases, approved tool instructions, or shared skill packs where the agent should benefit from centrally managed context but should not rewrite the source of truth.

### Require approval for skill writes

If agents may write to skill files but you want a human in the loop first, use either [`interrupt_on`](/oss/python/deepagents/human-in-the-loop) or a permission rule with `mode="interrupt"`. Both pause before `write_file` or `edit_file` runs and use the same resume flow.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from deepagents import FilesystemPermission, create_deep_agent
from langgraph.checkpoint.memory import MemorySaver

agent = create_deep_agent(
    model="anthropic:claude-sonnet-4-6",
    skills=["/skills/personal/"],
    permissions=[
        FilesystemPermission(
            operations=["write"],
            paths=["/skills/**"],
            mode="interrupt",
        ),
    ],
    checkpointer=MemorySaver(),  # Required to pause and resume
)
```

Alternatively, configure `interrupt_on={"write_file": True, "edit_file": True}` to require approval for all filesystem writes, not only skills paths. See [Human-in-the-loop](/oss/python/deepagents/human-in-the-loop) for handling and resuming interrupts.

<Note>
  Filesystem permission interrupts require `deepagents>=0.6.8`.
</Note>

### Allow agents to edit personal skills

By default, agents can write to skill files if the backend permits it and no permission rule blocks the path. To let agents create or refine skills without touching shared libraries:

1. Route a writable path such as `/skills/personal/` to a user-scoped `StoreBackend`.
2. Pass that path (along with any shared paths) in `skills`.
3. Do not add a `deny` rule for the writable path. Place more specific rules before broader deny rules if you mix shared and personal paths ([rule ordering](/oss/python/deepagents/permissions#rule-ordering)).

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from deepagents import FilesystemPermission, create_deep_agent
from deepagents.backends import CompositeBackend, StateBackend, StoreBackend

agent = create_deep_agent(
    model="anthropic:claude-sonnet-4-6",
    backend=CompositeBackend(
        default=StateBackend(),
        routes={
            "/skills/shared/": StoreBackend(
                namespace=lambda rt: ("curated-skills", rt.context.org_id),
            ),
            "/skills/personal/": StoreBackend(
                namespace=lambda rt: (
                    "user-skills",
                    rt.server_info.user.identity,
                ),
            ),
        },
    ),
    skills=["/skills/shared/", "/skills/personal/"],
    permissions=[
        FilesystemPermission(
            operations=["write"],
            paths=["/skills/shared/**"],
            mode="deny",
        ),
    ],
)
```

The agent uses `write_file` and `edit_file` to create or update `SKILL.md` and supporting files under the writable path. To capture general learnings outside the skills format, route a separate path such as `/memories/` to another writable backend. See [Backends](/oss/python/deepagents/backends) for routing and store setup.

## Execute code with skills

Without code execution, skills are passive: the agent reads instructions and follows them using its available tools. Code execution turns skills into active capabilities. A skill can ship a tested script that calls an API, transforms data, validates output, or runs a pipeline — and the agent executes it deterministically rather than regenerating the logic from instructions each time. This is especially valuable for workflows that require exact behavior (data transformations, API integrations, compliance checks) or that depend on libraries the agent cannot use through tool calls alone.

Skills execute code through [sandbox scripts](#sandbox-scripts): the agent runs a bundled script when it needs to install dependencies, run tests, call CLIs, or work with an operating-system filesystem.

### Sandbox scripts

Skills can include scripts alongside the `SKILL.md` file. Reference scripts in your `SKILL.md` so the agent knows they exist and when to run them:

<Tree>
  <Tree.Folder name="skills">
    <Tree.Folder name="arxiv-search">
      <Tree.File name="SKILL.md" />

      <Tree.Folder name="scripts">
        <Tree.File name="search.py" />
      </Tree.Folder>
    </Tree.Folder>
  </Tree.Folder>
</Tree>

```md theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
---
name: arxiv-search
description: Search the arXiv preprint repository for research papers. Use when the user asks about academic papers, recent research, or scientific literature.
---
