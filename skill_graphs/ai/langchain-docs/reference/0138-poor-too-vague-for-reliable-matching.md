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
    ```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    import { createDeepAgent, StateBackend, type FileData } from "deepagents";
    import { MemorySaver } from "@langchain/langgraph";

    const checkpointer = new MemorySaver();
    const backend = new StateBackend();

    function createFileData(content: string): FileData {
      const now = new Date().toISOString();
      return {
        content: content.split("\n"),
        created_at: now,
        modified_at: now,
      };
    }

    const skillsFiles: Record<string, FileData> = {};
    const skillUrl =
      "https://raw.githubusercontent.com/langchain-ai/deepagentsjs/refs/heads/main/examples/skills/langgraph-docs/SKILL.md";
    const response = await fetch(skillUrl);
    const skillContent = await response.text();

    skillsFiles["/skills/langgraph-docs/SKILL.md"] = createFileData(skillContent);

    const agent = await createDeepAgent({
      model: "google-genai:gemini-3.1-pro-preview",
      backend,
      checkpointer, // Required !
      // IMPORTANT: deepagents skill source paths are virtual (POSIX) paths relative to the backend root.
      skills: ["/skills/"],
    });

    const config = { configurable: { thread_id: `thread-${Date.now()}` } };
    const result = await agent.invoke(
      {
        messages: [{ role: "user", content: "what is langraph?" }],
        files: skillsFiles,
      },
      config,
    );
    ```
  </Tab>

  <Tab title="StoreBackend">
    ```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    import { createDeepAgent, StoreBackend, type FileData } from "deepagents";
    import { InMemoryStore, MemorySaver } from "@langchain/langgraph";

    const checkpointer = new MemorySaver();
    const store = new InMemoryStore();
    const backend = new StoreBackend({
      namespace: () => ["filesystem"],
    });

    function createFileData(content: string): FileData {
      const now = new Date().toISOString();
      return {
        content: content.split("\n"),
        created_at: now,
        modified_at: now,
      };
    }

    const skillUrl =
      "https://raw.githubusercontent.com/langchain-ai/deepagentsjs/refs/heads/main/examples/skills/langgraph-docs/SKILL.md";

    const response = await fetch(skillUrl);
    const skillContent = await response.text();
    const fileData = createFileData(skillContent);

    await store.put(["filesystem"], "/skills/langgraph-docs/SKILL.md", fileData);

    const agent = await createDeepAgent({
      model: "google-genai:gemini-3.1-pro-preview",
      backend,
      store,
      checkpointer,
      // IMPORTANT: deepagents skill source paths are virtual (POSIX) paths relative to the backend root.
      skills: ["/skills/"],
    });

    const config = {
      recursionLimit: 50,
      configurable: { thread_id: `thread-${Date.now()}` },
    };
    const result = await agent.invoke(
      { messages: [{ role: "user", content: "what is langraph?" }] },
      config,
    );
    ```
  </Tab>

  <Tab title="FilesystemBackend">
    ```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    import { createDeepAgent, FilesystemBackend } from "deepagents";
    import { MemorySaver } from "@langchain/langgraph";

    const checkpointer = new MemorySaver();
    const backend = new FilesystemBackend({ rootDir: process.cwd() });

    const agent = await createDeepAgent({
      model: "google-genai:gemini-3.1-pro-preview",
      backend,
      skills: ["./examples/skills/"],
      interruptOn: {
        read_file: true,
        write_file: true,
        delete_file: true,
      },
      checkpointer, // Required!
    });

    const config = { configurable: { thread_id: `thread-${Date.now()}` } };
    const result = await agent.invoke(
      { messages: [{ role: "user", content: "what is langraph?" }] },
      config,
    );
    ```
  </Tab>
</Tabs>

## Load skills at runtime

When you have a large collection of skills but only a subset is relevant for a given run, select which skills to load based on runtime context such as user role, tenant, or request type. There are two main approaches:

### Dynamic skill lists

The simplest approach is to construct the `skills` array before creating the agent. Choose which skill paths to include based on whatever runtime context you have:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { createDeepAgent } from "deepagents";

const SKILLS_BY_ROLE: Record<string, string[]> = {
  engineering: ["/skills/code-review/", "/skills/testing/", "/skills/deployment/"],
  data: ["/skills/sql-analysis/", "/skills/visualization/", "/skills/data-pipeline/"],
  support: ["/skills/ticket-triage/", "/skills/runbook/"],
};

function createAgentForUser(userRole: string) {
  return createDeepAgent({
    model: "anthropic:claude-sonnet-4-6",
    skills: SKILLS_BY_ROLE[userRole] ?? [],
  });
}
```

This works well when skills live on disk or in a shared backend and you just need to control which ones the agent sees. The skills themselves are not duplicated — you maintain one copy and vary the paths passed to each run.

<Note>
  The SDK only loads the sources you pass in `skills`. It does not automatically scan CLI directories such as `~/.deepagents/...` or `~/.agents/...`.

  For CLI storage conventions, see [App data](/oss/javascript/deepagents/code/data-locations).

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

For multi-tenant applications where each user's skill set is managed independently, route `/skills/` to a [StoreBackend](https://reference.langchain.com/javascript/deepagents/backends/StoreBackend) with a namespace factory. Populate each namespace with only the skills that user should have access to, and the middleware resolves to the correct set at runtime:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import {
  createDeepAgent,
  CompositeBackend,
  StateBackend,
  StoreBackend,
} from "deepagents";

const agent = await createDeepAgent({
  model: "anthropic:claude-sonnet-4-6",
  skills: ["/skills/"],
  backend: new CompositeBackend({
    default: new StateBackend(),
    routes: {
      "/skills/": new StoreBackend({
        namespace: (ctx) => [
          ctx.assistantId ?? "default",
          ctx.config?.configurable?.user_id ?? "anonymous",
        ],
      }),
    },
  }),
});
```

This pattern is useful when different users or tenants need fully independent skill libraries that can be updated separately. For a managed solution that handles skill access, sharing, and workspace-level visibility out of the box, see [Fleet skills](/langsmith/fleet/skills).

## Skills for subagents

When you use [subagents](/oss/javascript/deepagents/subagents), you can configure which skills each type has access to:

* **General-purpose subagent**: Automatically inherits skills from the main agent when you pass `skills` to `create_deep_agent`. No additional configuration is needed.
* **Custom subagents**: Do not inherit the main agent's skills. Add a `skills` parameter to each subagent definition with that subagent's skill source paths.

Skill state is fully isolated: the main agent's skills are not visible to subagents, and subagent skills are not visible to the main agent.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const researchSubagent = {
  name: "researcher",
  description: "Research assistant with specialized skills",
  systemPrompt: "You are a researcher.",
  tools: [webSearch],
  skills: ["/skills/research/", "/skills/web-search/"],  // Subagent-specific skills
};

const agent = await createDeepAgent({
  model: "google_genai:gemini-3.5-flash",
  skills: ["/skills/main/"],  // Main agent and GP subagent get these
  subagents: [researchSubagent],  // Researcher gets only its own skills
});
```

For more information on subagent configuration and skills inheritance, see [Subagents](/oss/javascript/deepagents/subagents).

## Skill permissions

Production deployments usually need to control three things: which skills each user can see, whether the agent can modify skill files, and whether writes require human approval. You control visibility with the `skills` argument and [backend routing](#backends-and-remote-skill-loading), access with [filesystem permissions](/oss/javascript/deepagents/permissions), and approval with [`interrupt_on`](/oss/javascript/deepagents/human-in-the-loop) or permission rules with `mode="interrupt"`.

### Share skills across users

To give every user access to the same curated library, route `/skills/` to a shared [StoreBackend](https://reference.langchain.com/javascript/deepagents/backends/StoreBackend) and seed it from your application code or an admin workflow. Use an organization-scoped namespace so all agents in that org resolve to the same store:

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

To share skills without letting agents modify them, route `/skills/` to a shared store and deny write operations under `/skills/**` with [filesystem permissions](/oss/javascript/deepagents/permissions). The agent can discover and read skills; only your application code or an admin workflow updates the store.

<CodeGroup>
  ```ts Google theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { InMemoryStore } from "@langchain/langgraph";
  import {
    createDeepAgent,
    CompositeBackend,
    StateBackend,
    StoreBackend,
  } from "deepagents";

  const store = new InMemoryStore(); // Good for local dev; omit for LangSmith Deployment

  const agent = createDeepAgent({
    model: "google-genai:gemini-3.5-flash",
    backend: new CompositeBackend(new StateBackend(), {
      "/skills/": new StoreBackend({
        namespace: (rt) => ["curated-skills", rt.context.orgId],
      }),
    }),
    skills: ["/skills/"],
    permissions: [
      {
        operations: ["write"],
        paths: ["/skills/**"],
        mode: "deny",
      },
    ],
    store,
  });
  ```

  ```ts OpenAI theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { InMemoryStore } from "@langchain/langgraph";
  import {
    createDeepAgent,
    CompositeBackend,
    StateBackend,
    StoreBackend,
  } from "deepagents";

  const store = new InMemoryStore(); // Good for local dev; omit for LangSmith Deployment

  const agent = createDeepAgent({
    model: "openai:gpt-5.5",
    backend: new CompositeBackend(new StateBackend(), {
      "/skills/": new StoreBackend({
        namespace: (rt) => ["curated-skills", rt.context.orgId],
      }),
    }),
    skills: ["/skills/"],
    permissions: [
      {
        operations: ["write"],
        paths: ["/skills/**"],
        mode: "deny",
      },
    ],
    store,
  });
  ```

  ```ts Anthropic theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { InMemoryStore } from "@langchain/langgraph";
  import {
    createDeepAgent,
    CompositeBackend,
    StateBackend,
    StoreBackend,
  } from "deepagents";

  const store = new InMemoryStore(); // Good for local dev; omit for LangSmith Deployment

  const agent = createDeepAgent({
    model: "anthropic:claude-sonnet-4-6",
    backend: new CompositeBackend(new StateBackend(), {
      "/skills/": new StoreBackend({
        namespace: (rt) => ["curated-skills", rt.context.orgId],
      }),
    }),
    skills: ["/skills/"],
    permissions: [
      {
        operations: ["write"],
        paths: ["/skills/**"],
        mode: "deny",
      },
    ],
    store,
  });
  ```

  ```ts OpenRouter theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { InMemoryStore } from "@langchain/langgraph";
  import {
    createDeepAgent,
    CompositeBackend,
    StateBackend,
    StoreBackend,
  } from "deepagents";

  const store = new InMemoryStore(); // Good for local dev; omit for LangSmith Deployment

  const agent = createDeepAgent({
    model: "openrouter:anthropic/claude-sonnet-4-6",
    backend: new CompositeBackend(new StateBackend(), {
      "/skills/": new StoreBackend({
        namespace: (rt) => ["curated-skills", rt.context.orgId],
      }),
    }),
    skills: ["/skills/"],
    permissions: [
      {
        operations: ["write"],
        paths: ["/skills/**"],
        mode: "deny",
      },
    ],
    store,
  });
  ```

  ```ts Fireworks theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { InMemoryStore } from "@langchain/langgraph";
  import {
    createDeepAgent,
    CompositeBackend,
    StateBackend,
    StoreBackend,
  } from "deepagents";

  const store = new InMemoryStore(); // Good for local dev; omit for LangSmith Deployment

  const agent = createDeepAgent({
    model: "fireworks:accounts/fireworks/models/qwen3p5-397b-a17b",
    backend: new CompositeBackend(new StateBackend(), {
      "/skills/": new StoreBackend({
        namespace: (rt) => ["curated-skills", rt.context.orgId],
      }),
    }),
    skills: ["/skills/"],
    permissions: [
      {
        operations: ["write"],
        paths: ["/skills/**"],
        mode: "deny",
      },
    ],
    store,
  });
  ```

  ```ts Baseten theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { InMemoryStore } from "@langchain/langgraph";
  import {
    createDeepAgent,
    CompositeBackend,
    StateBackend,
    StoreBackend,
  } from "deepagents";

  const store = new InMemoryStore(); // Good for local dev; omit for LangSmith Deployment

  const agent = createDeepAgent({
    model: "baseten:zai-org/GLM-5",
    backend: new CompositeBackend(new StateBackend(), {
      "/skills/": new StoreBackend({
        namespace: (rt) => ["curated-skills", rt.context.orgId],
      }),
    }),
    skills: ["/skills/"],
    permissions: [
      {
        operations: ["write"],
        paths: ["/skills/**"],
        mode: "deny",
      },
    ],
    store,
  });
  ```

  ```ts Ollama theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { InMemoryStore } from "@langchain/langgraph";
  import {
    createDeepAgent,
    CompositeBackend,
    StateBackend,
    StoreBackend,
  } from "deepagents";

  const store = new InMemoryStore(); // Good for local dev; omit for LangSmith Deployment

  const agent = createDeepAgent({
    model: "ollama:devstral-2",
    backend: new CompositeBackend(new StateBackend(), {
      "/skills/": new StoreBackend({
        namespace: (rt) => ["curated-skills", rt.context.orgId],
      }),
    }),
    skills: ["/skills/"],
    permissions: [
      {
        operations: ["write"],
        paths: ["/skills/**"],
        mode: "deny",
      },
    ],
    store,
  });
  ```
</CodeGroup>

Use this for enterprise knowledge bases, approved tool instructions, or shared skill packs where the agent should benefit from centrally managed context but should not rewrite the source of truth.

### Require approval for skill writes

If agents may write to skill files but you want a human in the loop first, use either [`interrupt_on`](/oss/javascript/deepagents/human-in-the-loop) or a permission rule with `mode="interrupt"`. Both pause before `write_file` or `edit_file` runs and use the same resume flow.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { MemorySaver } from "@langchain/langgraph";
import { createDeepAgent } from "deepagents";

const agent = await createDeepAgent({
  model: "anthropic:claude-sonnet-4-6",
  skills: ["/skills/personal/"],
  permissions: [
    {
      operations: ["write"],
      paths: ["/skills/**"],
      mode: "interrupt",
    },
  ],
  checkpointer: new MemorySaver(), // Required to pause and resume
});
```

Alternatively, configure `interrupt_on={"write_file": True, "edit_file": True}` to require approval for all filesystem writes, not only skills paths. See [Human-in-the-loop](/oss/javascript/deepagents/human-in-the-loop) for handling and resuming interrupts.

### Allow agents to edit personal skills

By default, agents can write to skill files if the backend permits it and no permission rule blocks the path. To let agents create or refine skills without touching shared libraries:

1. Route a writable path such as `/skills/personal/` to a user-scoped `StoreBackend`.
2. Pass that path (along with any shared paths) in `skills`.
3. Do not add a `deny` rule for the writable path. Place more specific rules before broader deny rules if you mix shared and personal paths ([rule ordering](/oss/javascript/deepagents/permissions#rule-ordering)).

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import {
  createDeepAgent,
  CompositeBackend,
  StateBackend,
  StoreBackend,
} from "deepagents";

const agent = await createDeepAgent({
  model: "anthropic:claude-sonnet-4-6",
  backend: new CompositeBackend({
    default: new StateBackend(),
    routes: {
      "/skills/shared/": new StoreBackend({
        namespace: (rt) => ["curated-skills", rt.context.orgId],
      }),
      "/skills/personal/": new StoreBackend({
        namespace: (ctx) => [
          "user-skills",
          ctx.config?.configurable?.user_id ?? "anonymous",
        ],
      }),
    },
  }),
  skills: ["/skills/shared/", "/skills/personal/"],
  permissions: [
    {
      operations: ["write"],
      paths: ["/skills/shared/**"],
      mode: "deny",
    },
  ],
});
```

The agent uses `write_file` and `edit_file` to create or update `SKILL.md` and supporting files under the writable path. To capture general learnings outside the skills format, route a separate path such as `/memories/` to another writable backend. See [Backends](/oss/javascript/deepagents/backends) for routing and store setup.

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
        <Tree.File name="search.ts" />
      </Tree.Folder>
    </Tree.Folder>
  </Tree.Folder>
</Tree>

```md theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
---
name: arxiv-search
description: Search the arXiv preprint repository for research papers. Use when the user asks about academic papers, recent research, or scientific literature.
---
