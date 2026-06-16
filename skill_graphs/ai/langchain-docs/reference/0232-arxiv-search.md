# arxiv-search

Search arXiv for papers matching the user's query.

## Instructions

1. Run `scripts/search.py` with the user's query as an argument.
2. Parse the results and present them with title, authors, abstract summary, and link.
3. If the user asks for more detail on a specific paper, fetch the full abstract.
```

The agent can *read* scripts from any backend, but to *execute* them, the agent needs access to a shell, which only [sandbox backends](/oss/python/deepagents/sandboxes) provide.

[Sandbox backends](/oss/python/deepagents/sandboxes) run in isolated containers. Skill files stored outside the sandbox are not available inside it, which means the agent cannot execute skill scripts or access skill resources unless they are transferred in first. Use [custom middleware](/oss/python/langchain/middleware/custom) to handle this transfer:

* **`before_agent`**: Read skill files from the backend and upload them into the sandbox so the agent can execute scripts from the start.
* **`after_agent`**: Download any updated or newly created skill files from the sandbox and write them back to the backend so changes persist across runs.

<CodeGroup>
  ```python Google theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import asyncio
  from pathlib import Path
  from typing import Any

  from daytona import Daytona
  from deepagents import create_deep_agent
  from deepagents.backends import CompositeBackend, StoreBackend
  from deepagents.backends.utils import create_file_data
  from langchain.agents.middleware import AgentMiddleware, AgentState

  from langchain_daytona import DaytonaSandbox
  from langgraph.runtime import Runtime
  from langgraph.store.memory import InMemoryStore

  # Identical skill bundles for every user: one shared store namespace.
  SKILLS_SHARED_NAMESPACE = ("skills", "builtin")

  class SkillSandboxSyncMiddleware(AgentMiddleware[AgentState, Any, Any]):
      """Copy shared skill files from the store into the sandbox before each agent run."""

      def __init__(self, backend: CompositeBackend) -> None:
          super().__init__()
          self.backend = backend

      async def abefore_agent(self, state: AgentState, runtime: Runtime[Any]) -> None:
          store = runtime.store

          files: list[tuple[str, bytes]] = []
          for item in await store.asearch(SKILLS_SHARED_NAMESPACE):
              key = str(item.key)
              if ".." in key or any(c in key for c in ("*", "?")):
                  msg = f"Invalid key: {key}"
                  raise ValueError(msg)
              normalized = key if key.startswith("/") else f"/{key}"
              # CompositeBackend routes paths and batches uploads to the right backend.
              files.append((f"/skills{normalized}", item.value["content"].encode()))

          if files:
              await self.backend.aupload_files(files)

  async def seed_skill_store(store: InMemoryStore) -> None:
      """Load canonical skill files from disk into the shared store namespace (run once at deploy).
      You can retrieve skills from any source (local filesystem, remote URL, etc.).
      """
      skills_dir = Path(__file__).resolve().parent / "skills"
      for file_path in sorted(p for p in skills_dir.rglob("*") if p.is_file()):
          rel = file_path.relative_to(skills_dir).as_posix()
          key = f"/{rel}"
          await store.aput(
              SKILLS_SHARED_NAMESPACE,
              key,
              create_file_data(file_path.read_text(encoding="utf-8")),
          )

  async def main() -> None:
      store = InMemoryStore()
      await seed_skill_store(store)

      daytona = Daytona()
      sandbox = daytona.create()
      sandbox_backend = DaytonaSandbox(sandbox=sandbox)

      backend = CompositeBackend(
          default=sandbox_backend,
          routes={
              "/skills/": StoreBackend(
                  store=store,
                  namespace=lambda _rt: SKILLS_SHARED_NAMESPACE,
              ),
          },
      )

      try:
          agent = create_deep_agent(
              model="google_genai:gemini-3.5-flash",
              backend=backend,
              skills=["/skills/"],
              store=store,
              middleware=[SkillSandboxSyncMiddleware(backend)],
          )

      finally:
          sandbox.stop()

  if __name__ == "__main__":
      asyncio.run(main())
  ```

  ```python OpenAI theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import asyncio
  from pathlib import Path
  from typing import Any

  from daytona import Daytona
  from deepagents import create_deep_agent
  from deepagents.backends import CompositeBackend, StoreBackend
  from deepagents.backends.utils import create_file_data
  from langchain.agents.middleware import AgentMiddleware, AgentState

  from langchain_daytona import DaytonaSandbox
  from langgraph.runtime import Runtime
  from langgraph.store.memory import InMemoryStore

  # Identical skill bundles for every user: one shared store namespace.
  SKILLS_SHARED_NAMESPACE = ("skills", "builtin")

  class SkillSandboxSyncMiddleware(AgentMiddleware[AgentState, Any, Any]):
      """Copy shared skill files from the store into the sandbox before each agent run."""

      def __init__(self, backend: CompositeBackend) -> None:
          super().__init__()
          self.backend = backend

      async def abefore_agent(self, state: AgentState, runtime: Runtime[Any]) -> None:
          store = runtime.store

          files: list[tuple[str, bytes]] = []
          for item in await store.asearch(SKILLS_SHARED_NAMESPACE):
              key = str(item.key)
              if ".." in key or any(c in key for c in ("*", "?")):
                  msg = f"Invalid key: {key}"
                  raise ValueError(msg)
              normalized = key if key.startswith("/") else f"/{key}"
              # CompositeBackend routes paths and batches uploads to the right backend.
              files.append((f"/skills{normalized}", item.value["content"].encode()))

          if files:
              await self.backend.aupload_files(files)

  async def seed_skill_store(store: InMemoryStore) -> None:
      """Load canonical skill files from disk into the shared store namespace (run once at deploy).
      You can retrieve skills from any source (local filesystem, remote URL, etc.).
      """
      skills_dir = Path(__file__).resolve().parent / "skills"
      for file_path in sorted(p for p in skills_dir.rglob("*") if p.is_file()):
          rel = file_path.relative_to(skills_dir).as_posix()
          key = f"/{rel}"
          await store.aput(
              SKILLS_SHARED_NAMESPACE,
              key,
              create_file_data(file_path.read_text(encoding="utf-8")),
          )

  async def main() -> None:
      store = InMemoryStore()
      await seed_skill_store(store)

      daytona = Daytona()
      sandbox = daytona.create()
      sandbox_backend = DaytonaSandbox(sandbox=sandbox)

      backend = CompositeBackend(
          default=sandbox_backend,
          routes={
              "/skills/": StoreBackend(
                  store=store,
                  namespace=lambda _rt: SKILLS_SHARED_NAMESPACE,
              ),
          },
      )

      try:
          agent = create_deep_agent(
              model="openai:gpt-5.5",
              backend=backend,
              skills=["/skills/"],
              store=store,
              middleware=[SkillSandboxSyncMiddleware(backend)],
          )

      finally:
          sandbox.stop()

  if __name__ == "__main__":
      asyncio.run(main())
  ```

  ```python Anthropic theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import asyncio
  from pathlib import Path
  from typing import Any

  from daytona import Daytona
  from deepagents import create_deep_agent
  from deepagents.backends import CompositeBackend, StoreBackend
  from deepagents.backends.utils import create_file_data
  from langchain.agents.middleware import AgentMiddleware, AgentState

  from langchain_daytona import DaytonaSandbox
  from langgraph.runtime import Runtime
  from langgraph.store.memory import InMemoryStore

  # Identical skill bundles for every user: one shared store namespace.
  SKILLS_SHARED_NAMESPACE = ("skills", "builtin")

  class SkillSandboxSyncMiddleware(AgentMiddleware[AgentState, Any, Any]):
      """Copy shared skill files from the store into the sandbox before each agent run."""

      def __init__(self, backend: CompositeBackend) -> None:
          super().__init__()
          self.backend = backend

      async def abefore_agent(self, state: AgentState, runtime: Runtime[Any]) -> None:
          store = runtime.store

          files: list[tuple[str, bytes]] = []
          for item in await store.asearch(SKILLS_SHARED_NAMESPACE):
              key = str(item.key)
              if ".." in key or any(c in key for c in ("*", "?")):
                  msg = f"Invalid key: {key}"
                  raise ValueError(msg)
              normalized = key if key.startswith("/") else f"/{key}"
              # CompositeBackend routes paths and batches uploads to the right backend.
              files.append((f"/skills{normalized}", item.value["content"].encode()))

          if files:
              await self.backend.aupload_files(files)

  async def seed_skill_store(store: InMemoryStore) -> None:
      """Load canonical skill files from disk into the shared store namespace (run once at deploy).
      You can retrieve skills from any source (local filesystem, remote URL, etc.).
      """
      skills_dir = Path(__file__).resolve().parent / "skills"
      for file_path in sorted(p for p in skills_dir.rglob("*") if p.is_file()):
          rel = file_path.relative_to(skills_dir).as_posix()
          key = f"/{rel}"
          await store.aput(
              SKILLS_SHARED_NAMESPACE,
              key,
              create_file_data(file_path.read_text(encoding="utf-8")),
          )

  async def main() -> None:
      store = InMemoryStore()
      await seed_skill_store(store)

      daytona = Daytona()
      sandbox = daytona.create()
      sandbox_backend = DaytonaSandbox(sandbox=sandbox)

      backend = CompositeBackend(
          default=sandbox_backend,
          routes={
              "/skills/": StoreBackend(
                  store=store,
                  namespace=lambda _rt: SKILLS_SHARED_NAMESPACE,
              ),
          },
      )

      try:
          agent = create_deep_agent(
              model="anthropic:claude-sonnet-4-6",
              backend=backend,
              skills=["/skills/"],
              store=store,
              middleware=[SkillSandboxSyncMiddleware(backend)],
          )

      finally:
          sandbox.stop()

  if __name__ == "__main__":
      asyncio.run(main())
  ```

  ```python OpenRouter theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import asyncio
  from pathlib import Path
  from typing import Any

  from daytona import Daytona
  from deepagents import create_deep_agent
  from deepagents.backends import CompositeBackend, StoreBackend
  from deepagents.backends.utils import create_file_data
  from langchain.agents.middleware import AgentMiddleware, AgentState

  from langchain_daytona import DaytonaSandbox
  from langgraph.runtime import Runtime
  from langgraph.store.memory import InMemoryStore

  # Identical skill bundles for every user: one shared store namespace.
  SKILLS_SHARED_NAMESPACE = ("skills", "builtin")

  class SkillSandboxSyncMiddleware(AgentMiddleware[AgentState, Any, Any]):
      """Copy shared skill files from the store into the sandbox before each agent run."""

      def __init__(self, backend: CompositeBackend) -> None:
          super().__init__()
          self.backend = backend

      async def abefore_agent(self, state: AgentState, runtime: Runtime[Any]) -> None:
          store = runtime.store

          files: list[tuple[str, bytes]] = []
          for item in await store.asearch(SKILLS_SHARED_NAMESPACE):
              key = str(item.key)
              if ".." in key or any(c in key for c in ("*", "?")):
                  msg = f"Invalid key: {key}"
                  raise ValueError(msg)
              normalized = key if key.startswith("/") else f"/{key}"
              # CompositeBackend routes paths and batches uploads to the right backend.
              files.append((f"/skills{normalized}", item.value["content"].encode()))

          if files:
              await self.backend.aupload_files(files)

  async def seed_skill_store(store: InMemoryStore) -> None:
      """Load canonical skill files from disk into the shared store namespace (run once at deploy).
      You can retrieve skills from any source (local filesystem, remote URL, etc.).
      """
      skills_dir = Path(__file__).resolve().parent / "skills"
      for file_path in sorted(p for p in skills_dir.rglob("*") if p.is_file()):
          rel = file_path.relative_to(skills_dir).as_posix()
          key = f"/{rel}"
          await store.aput(
              SKILLS_SHARED_NAMESPACE,
              key,
              create_file_data(file_path.read_text(encoding="utf-8")),
          )

  async def main() -> None:
      store = InMemoryStore()
      await seed_skill_store(store)

      daytona = Daytona()
      sandbox = daytona.create()
      sandbox_backend = DaytonaSandbox(sandbox=sandbox)

      backend = CompositeBackend(
          default=sandbox_backend,
          routes={
              "/skills/": StoreBackend(
                  store=store,
                  namespace=lambda _rt: SKILLS_SHARED_NAMESPACE,
              ),
          },
      )

      try:
          agent = create_deep_agent(
              model="openrouter:anthropic/claude-sonnet-4-6",
              backend=backend,
              skills=["/skills/"],
              store=store,
              middleware=[SkillSandboxSyncMiddleware(backend)],
          )

      finally:
          sandbox.stop()

  if __name__ == "__main__":
      asyncio.run(main())
  ```

  ```python Fireworks theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import asyncio
  from pathlib import Path
  from typing import Any

  from daytona import Daytona
  from deepagents import create_deep_agent
  from deepagents.backends import CompositeBackend, StoreBackend
  from deepagents.backends.utils import create_file_data
  from langchain.agents.middleware import AgentMiddleware, AgentState

  from langchain_daytona import DaytonaSandbox
  from langgraph.runtime import Runtime
  from langgraph.store.memory import InMemoryStore

  # Identical skill bundles for every user: one shared store namespace.
  SKILLS_SHARED_NAMESPACE = ("skills", "builtin")

  class SkillSandboxSyncMiddleware(AgentMiddleware[AgentState, Any, Any]):
      """Copy shared skill files from the store into the sandbox before each agent run."""

      def __init__(self, backend: CompositeBackend) -> None:
          super().__init__()
          self.backend = backend

      async def abefore_agent(self, state: AgentState, runtime: Runtime[Any]) -> None:
          store = runtime.store

          files: list[tuple[str, bytes]] = []
          for item in await store.asearch(SKILLS_SHARED_NAMESPACE):
              key = str(item.key)
              if ".." in key or any(c in key for c in ("*", "?")):
                  msg = f"Invalid key: {key}"
                  raise ValueError(msg)
              normalized = key if key.startswith("/") else f"/{key}"
              # CompositeBackend routes paths and batches uploads to the right backend.
              files.append((f"/skills{normalized}", item.value["content"].encode()))

          if files:
              await self.backend.aupload_files(files)

  async def seed_skill_store(store: InMemoryStore) -> None:
      """Load canonical skill files from disk into the shared store namespace (run once at deploy).
      You can retrieve skills from any source (local filesystem, remote URL, etc.).
      """
      skills_dir = Path(__file__).resolve().parent / "skills"
      for file_path in sorted(p for p in skills_dir.rglob("*") if p.is_file()):
          rel = file_path.relative_to(skills_dir).as_posix()
          key = f"/{rel}"
          await store.aput(
              SKILLS_SHARED_NAMESPACE,
              key,
              create_file_data(file_path.read_text(encoding="utf-8")),
          )

  async def main() -> None:
      store = InMemoryStore()
      await seed_skill_store(store)

      daytona = Daytona()
      sandbox = daytona.create()
      sandbox_backend = DaytonaSandbox(sandbox=sandbox)

      backend = CompositeBackend(
          default=sandbox_backend,
          routes={
              "/skills/": StoreBackend(
                  store=store,
                  namespace=lambda _rt: SKILLS_SHARED_NAMESPACE,
              ),
          },
      )

      try:
          agent = create_deep_agent(
              model="fireworks:accounts/fireworks/models/qwen3p5-397b-a17b",
              backend=backend,
              skills=["/skills/"],
              store=store,
              middleware=[SkillSandboxSyncMiddleware(backend)],
          )

      finally:
          sandbox.stop()

  if __name__ == "__main__":
      asyncio.run(main())
  ```

  ```python Baseten theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import asyncio
  from pathlib import Path
  from typing import Any

  from daytona import Daytona
  from deepagents import create_deep_agent
  from deepagents.backends import CompositeBackend, StoreBackend
  from deepagents.backends.utils import create_file_data
  from langchain.agents.middleware import AgentMiddleware, AgentState

  from langchain_daytona import DaytonaSandbox
  from langgraph.runtime import Runtime
  from langgraph.store.memory import InMemoryStore

  # Identical skill bundles for every user: one shared store namespace.
  SKILLS_SHARED_NAMESPACE = ("skills", "builtin")

  class SkillSandboxSyncMiddleware(AgentMiddleware[AgentState, Any, Any]):
      """Copy shared skill files from the store into the sandbox before each agent run."""

      def __init__(self, backend: CompositeBackend) -> None:
          super().__init__()
          self.backend = backend

      async def abefore_agent(self, state: AgentState, runtime: Runtime[Any]) -> None:
          store = runtime.store

          files: list[tuple[str, bytes]] = []
          for item in await store.asearch(SKILLS_SHARED_NAMESPACE):
              key = str(item.key)
              if ".." in key or any(c in key for c in ("*", "?")):
                  msg = f"Invalid key: {key}"
                  raise ValueError(msg)
              normalized = key if key.startswith("/") else f"/{key}"
              # CompositeBackend routes paths and batches uploads to the right backend.
              files.append((f"/skills{normalized}", item.value["content"].encode()))

          if files:
              await self.backend.aupload_files(files)

  async def seed_skill_store(store: InMemoryStore) -> None:
      """Load canonical skill files from disk into the shared store namespace (run once at deploy).
      You can retrieve skills from any source (local filesystem, remote URL, etc.).
      """
      skills_dir = Path(__file__).resolve().parent / "skills"
      for file_path in sorted(p for p in skills_dir.rglob("*") if p.is_file()):
          rel = file_path.relative_to(skills_dir).as_posix()
          key = f"/{rel}"
          await store.aput(
              SKILLS_SHARED_NAMESPACE,
              key,
              create_file_data(file_path.read_text(encoding="utf-8")),
          )

  async def main() -> None:
      store = InMemoryStore()
      await seed_skill_store(store)

      daytona = Daytona()
      sandbox = daytona.create()
      sandbox_backend = DaytonaSandbox(sandbox=sandbox)

      backend = CompositeBackend(
          default=sandbox_backend,
          routes={
              "/skills/": StoreBackend(
                  store=store,
                  namespace=lambda _rt: SKILLS_SHARED_NAMESPACE,
              ),
          },
      )

      try:
          agent = create_deep_agent(
              model="baseten:zai-org/GLM-5",
              backend=backend,
              skills=["/skills/"],
              store=store,
              middleware=[SkillSandboxSyncMiddleware(backend)],
          )

      finally:
          sandbox.stop()

  if __name__ == "__main__":
      asyncio.run(main())
  ```

  ```python Ollama theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import asyncio
  from pathlib import Path
  from typing import Any

  from daytona import Daytona
  from deepagents import create_deep_agent
  from deepagents.backends import CompositeBackend, StoreBackend
  from deepagents.backends.utils import create_file_data
  from langchain.agents.middleware import AgentMiddleware, AgentState

  from langchain_daytona import DaytonaSandbox
  from langgraph.runtime import Runtime
  from langgraph.store.memory import InMemoryStore

  # Identical skill bundles for every user: one shared store namespace.
  SKILLS_SHARED_NAMESPACE = ("skills", "builtin")

  class SkillSandboxSyncMiddleware(AgentMiddleware[AgentState, Any, Any]):
      """Copy shared skill files from the store into the sandbox before each agent run."""

      def __init__(self, backend: CompositeBackend) -> None:
          super().__init__()
          self.backend = backend

      async def abefore_agent(self, state: AgentState, runtime: Runtime[Any]) -> None:
          store = runtime.store

          files: list[tuple[str, bytes]] = []
          for item in await store.asearch(SKILLS_SHARED_NAMESPACE):
              key = str(item.key)
              if ".." in key or any(c in key for c in ("*", "?")):
                  msg = f"Invalid key: {key}"
                  raise ValueError(msg)
              normalized = key if key.startswith("/") else f"/{key}"
              # CompositeBackend routes paths and batches uploads to the right backend.
              files.append((f"/skills{normalized}", item.value["content"].encode()))

          if files:
              await self.backend.aupload_files(files)

  async def seed_skill_store(store: InMemoryStore) -> None:
      """Load canonical skill files from disk into the shared store namespace (run once at deploy).
      You can retrieve skills from any source (local filesystem, remote URL, etc.).
      """
      skills_dir = Path(__file__).resolve().parent / "skills"
      for file_path in sorted(p for p in skills_dir.rglob("*") if p.is_file()):
          rel = file_path.relative_to(skills_dir).as_posix()
          key = f"/{rel}"
          await store.aput(
              SKILLS_SHARED_NAMESPACE,
              key,
              create_file_data(file_path.read_text(encoding="utf-8")),
          )

  async def main() -> None:
      store = InMemoryStore()
      await seed_skill_store(store)

      daytona = Daytona()
      sandbox = daytona.create()
      sandbox_backend = DaytonaSandbox(sandbox=sandbox)

      backend = CompositeBackend(
          default=sandbox_backend,
          routes={
              "/skills/": StoreBackend(
                  store=store,
                  namespace=lambda _rt: SKILLS_SHARED_NAMESPACE,
              ),
          },
      )

      try:
          agent = create_deep_agent(
              model="ollama:devstral-2",
              backend=backend,
              skills=["/skills/"],
              store=store,
              middleware=[SkillSandboxSyncMiddleware(backend)],
          )

      finally:
          sandbox.stop()

  if __name__ == "__main__":
      asyncio.run(main())
  ```
</CodeGroup>

For a complete example that seeds both skills and memories before execution and syncs both back afterward, see [syncing skills and memories with custom middleware](/oss/python/deepagents/going-to-production#example-syncing-skills-and-memories-with-custom-middleware).

## Troubleshooting

Use [LangSmith](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=oss-deepagents-skills) traces to debug skill discovery, `read_file` calls on `SKILL.md`, and supporting resource access. Follow the [tracing quickstart](/langsmith/observability-quickstart) to get set up. We recommend you also set up [LangSmith Engine](/langsmith/engine), which monitors your traces, detects issues, and proposes fixes.

### Skill not activated

**Problem**: The agent handles the task without reading the skill's `SKILL.md`.

**Solutions**:

1. **Make the description more specific.** The agent selects skills from the [`description`](#frontmatter-fields) field alone at [discovery](#how-skills-work). Include what the skill does, when to use it, and keywords the agent can match:

   ```yaml theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
   # Good
   description: >-
     Search the arXiv preprint repository for research papers. Use when the
     user asks about academic papers, recent research, or scientific literature.

   # Poor
   description: Helps with research.
   ```

2. **Reduce overlap between skills.** If multiple skills have similar descriptions, the agent may skip the right one or pick the wrong one. Differentiate descriptions or [consolidate related skills](#write-effective-skills).

3. **Confirm the skill is in the `skills` array.** Skills load only from paths you pass at agent creation or from subagent-specific `skills` parameters.

### Skills missing at startup

**Problem**: The agent does not list a skill in its system prompt, or `read_file` on `SKILL.md` fails.

**Solutions**:

1. **Check the skill path.** Paths must use forward slashes and be relative to the backend root. With `FilesystemBackend`, the path is relative to `root_dir`. With `StateBackend`, pass skill files in `invoke(files={...})` using `create_file_data()`.

2. **Validate `SKILL.md` [frontmatter](#frontmatter-fields).** The [`name`](#frontmatter-fields) must match the parent directory name and follow the [Agent Skills specification](https://agentskills.io/specification). Use the [`skills-ref` validation tool](https://github.com/agentskills/agentskills/tree/main/skills-ref) to check formatting.

3. **Check file size.** Deep Agents skips `SKILL.md` files over 10 MB during discovery.

4. **Check layered sources.** When the same skill name appears in multiple sources, the [last source wins](#usage). An older or empty skill from a later path can override the one you expect.

### Supporting files not found

**Problem**: The agent reads `SKILL.md` but cannot access scripts, references, or assets.

**Solutions**:

1. **Reference files from `SKILL.md`.** The agent does not auto-discover supporting files. State what each file contains and when to use it. Use [relative paths](#reference-files-from-skill-md) from the skill root.

2. **Keep paths within the skill directory.** File paths resolve against the backend. Confirm supporting files exist at the paths your instructions reference.

3. **Sync skills into sandboxes.** If you use [sandbox backends](/oss/python/deepagents/sandboxes), skill files outside the container are not available until you copy them in. See [Sandbox scripts](#sandbox-scripts) and [syncing skills and memories with custom middleware](/oss/python/deepagents/going-to-production#example-syncing-skills-and-memories-with-custom-middleware).

### Scripts fail to run

**Problem**: The agent reads a script but cannot run it.

**Solution**: The agent can read scripts from any backend, but running them requires a [sandbox backend](/oss/python/deepagents/sandboxes). See [Execute code with skills](#execute-code-with-skills).

### Subagent cannot access a skill

**Problem**: A custom subagent does not see skills that the main agent uses.

**Solution**: Custom subagents do not inherit the main agent's skills. Add a `skills` parameter to each [subagent definition](#skills-for-subagents) with that subagent's skill source paths. The general-purpose subagent inherits skills from `create_deep_agent` automatically.

## Reference

### Skills, memory, and tools

Skills, [memory](/oss/python/deepagents/memory) (`AGENTS.md` files), and tools all provide context or capabilities to the agent. The following table summarizes when to reach for each:

|              | Skills                                                           | Memory                                                        | Tools                                                                             |
| ------------ | ---------------------------------------------------------------- | ------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| **Purpose**  | On-demand capabilities discovered through progressive disclosure | Persistent context loaded at startup                          | Programmatic actions the agent can call                                           |
| **Loading**  | Read only when the agent determines relevance                    | Loaded at agent start                                         | Available every turn                                                              |
| **Format**   | `SKILL.md` in named directories                                  | `AGENTS.md` files                                             | Functions bound to the agent                                                      |
| **Layering** | User, then project (last wins)                                   | User, then project (combined)                                 | Defined at agent creation                                                         |
| **Use when** | Instructions are task-specific and potentially large             | Context is always relevant (project conventions, preferences) | The agent needs a programmatic action, or does not have access to the file system |

These are guidelines, not hard boundaries. In practice, skills and memory sit on a spectrum. An agent can update its own skills as it works, capturing new procedures and refining instructions over time. In this way, skills can function as a form of progressive-disclosure memory: context the agent builds up and retrieves on demand rather than loading on every prompt.

### Frontmatter fields

The [Agent Skills specification](https://agentskills.io/specification) defines the following frontmatter fields:

| Field           | Required | Description                                                                                 |
| --------------- | -------- | ------------------------------------------------------------------------------------------- |
| `name`          | Yes      | Lowercase alphanumeric with hyphens, 1-64 characters. Must match the parent directory name. |
| `description`   | Yes      | What the skill does and when to use it. Max 1,024 characters.                               |
| `license`       | No       | License name or reference to a bundled license file.                                        |
| `compatibility` | No       | Environment requirements (system packages, network access). Max 500 characters.             |
| `metadata`      | No       | Arbitrary key-value pairs for additional properties.                                        |
| `allowed-tools` | No       | Space-separated list of pre-approved tools the skill can use. Experimental.                 |

```md expandable theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
---
name: langgraph-docs
description: Use this skill for requests related to LangGraph in order to fetch relevant documentation to provide accurate, up-to-date guidance.
license: MIT
compatibility: Requires internet access for fetching documentation URLs
metadata:
  author: langchain
  version: "1.0"
allowed-tools: fetch_url
---

# langgraph-docs

Instructions for the agent go here. See [Usage](#usage) for a complete example of skill instructions.
```

<Warning>
  Refer to the full [Agent Skills specification](https://agentskills.io/specification) for detailed constraints and validation rules. In Deep Agents, `SKILL.md` files must be under 10 MB. Files exceeding this limit are skipped during skill loading.
</Warning>

For more example skills, see [Deep Agents example skills](https://github.com/langchain-ai/deepagents/tree/main/libs/cli/examples/skills).

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/deepagents/skills.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Streaming
Source: https://docs.langchain.com/oss/python/deepagents/streaming

Stream real-time updates from deep agent runs and subagent execution

<Tip>
  For new applications, we recommend [event streaming](/oss/python/deepagents/event-streaming)—the typed-projection API introduced in Deep Agents v0.6. Event streaming gives you separate iterators per projection (subagents, messages, tool calls, values) so you can consume them independently instead of branching on `stream_mode` chunks.
</Tip>

Deep Agents build on LangGraph's streaming infrastructure with first-class support for subagent streams. When a deep agent delegates work to subagents, you can stream updates from each subagent independently—tracking progress, LLM tokens, and tool calls in real time.

What's possible with deep agent streaming:

* <Icon icon="diagram-subtask" /> [**Stream subagent progress**](#subagent-progress)—track each subagent's execution as it runs in parallel.
* <Icon icon="square-binary" /> [**Stream LLM tokens**](#llm-tokens)—stream tokens from the main agent and each subagent.
* <Icon icon="screwdriver-wrench" /> [**Stream tool calls**](#tool-calls)—see tool calls and results from within subagent execution.
* <Icon icon="table" /> [**Stream custom updates**](#custom-updates)—emit user-defined signals from inside subagent nodes.

## Enable subgraph streaming

Deep Agents use LangGraph's subgraph streaming to surface events from subagent execution. To receive subagent events, enable `stream_subgraphs` when streaming.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from deepagents import create_deep_agent

agent = create_deep_agent(
    model="google_genai:gemini-3.5-flash",
    system_prompt="You are a helpful research assistant",
    subagents=[
        {
            "name": "researcher",
            "description": "Researches a topic in depth",
            "system_prompt": "You are a thorough researcher.",
        },
    ],
)

for chunk in agent.stream(
    {"messages": [{"role": "user", "content": "Research quantum computing advances"}]},
    stream_mode="updates",
    subgraphs=True,  # [!code highlight]
    version="v2",  # [!code highlight]
):
    if chunk["type"] == "updates":
        if chunk["ns"]:
            # Subagent event - namespace identifies the source
            print(f"[subagent: {chunk['ns']}]")
        else:
            # Main agent event
            print("[main agent]")
        print(chunk["data"])
```

## Namespaces

When `subgraphs` is enabled, each streaming event includes a **namespace** that identifies which agent produced it. The namespace is a path of node names and task IDs that represents the agent hierarchy.

| Namespace                                  | Source                                                           |
| ------------------------------------------ | ---------------------------------------------------------------- |
| `()` (empty)                               | Main agent                                                       |
| `("tools:abc123",)`                        | A subagent spawned by the main agent's `task` tool call `abc123` |
| `("tools:abc123", "model_request:def456")` | The model request node inside a subagent                         |

Use namespaces to route events to the correct UI component:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
for chunk in agent.stream(
    {"messages": [{"role": "user", "content": "Plan my vacation"}]},
    stream_mode="updates",
    subgraphs=True,
    version="v2",
):
    if chunk["type"] == "updates":
        # Check if this event came from a subagent
        is_subagent = any(
            segment.startswith("tools:") for segment in chunk["ns"]
        )

        if is_subagent:
            # Extract the tool call ID from the namespace
            tool_call_id = next(
                s.split(":")[1] for s in chunk["ns"] if s.startswith("tools:")
            )
            print(f"Subagent {tool_call_id}: {chunk['data']}")
        else:
            print(f"Main agent: {chunk['data']}")
```

## Subagent progress

Use `stream_mode="updates"` to track subagent progress as each step completes. This is useful for showing which subagents are active and what work they've completed.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from deepagents import create_deep_agent

agent = create_deep_agent(
    model="google_genai:gemini-3.5-flash",
    system_prompt=(
        "You are a project coordinator. Always delegate research tasks "
        "to your researcher subagent using the task tool. Keep your final response to one sentence."
    ),
    subagents=[
        {
            "name": "researcher",
            "description": "Researches topics thoroughly",
            "system_prompt": (
                "You are a thorough researcher. Research the given topic "
                "and provide a concise summary in 2-3 sentences."
            ),
        },
    ],
)

for chunk in agent.stream(
    {"messages": [{"role": "user", "content": "Write a short summary about AI safety"}]},
    stream_mode="updates",
    subgraphs=True,
    version="v2",
):
    if chunk["type"] == "updates":
        # Main agent updates (empty namespace)
        if not chunk["ns"]:
            for node_name, data in chunk["data"].items():
                if node_name == "tools":
                    # Subagent results returned to main agent
                    for msg in data.get("messages", []):
                        if msg.type == "tool":
                            print(f"\nSubagent complete: {msg.name}")
                            print(f"  Result: {str(msg.content)[:200]}...")
                else:
                    print(f"[main agent] step: {node_name}")

        # Subagent updates (non-empty namespace)
        else:
            for node_name, data in chunk["data"].items():
                print(f"  [{chunk['ns'][0]}] step: {node_name}")
```

```shell title="Output" theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
[main agent] step: model_request
  [tools:call_abc123] step: model_request
  [tools:call_abc123] step: tools
  [tools:call_abc123] step: model_request

Subagent complete: task
  Result: ## AI Safety Report...
[main agent] step: model_request
```

## LLM tokens

Use `stream_mode="messages"` to stream individual tokens from both the main agent and subagents. Each message event includes metadata that identifies the source agent.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
current_source = ""

for chunk in agent.stream(
    {"messages": [{"role": "user", "content": "Research quantum computing advances"}]},
    stream_mode="messages",
    subgraphs=True,
    version="v2",
):
    if chunk["type"] == "messages":
        token, metadata = chunk["data"]

        # Check if this event came from a subagent (namespace contains "tools:")
        is_subagent = any(s.startswith("tools:") for s in chunk["ns"])

        if is_subagent:
            # Token from a subagent
            subagent_ns = next(s for s in chunk["ns"] if s.startswith("tools:"))
            if subagent_ns != current_source:
                print(f"\n\n--- [subagent: {subagent_ns}] ---")
                current_source = subagent_ns
            if token.content:
                print(token.content, end="", flush=True)
        else:
            # Token from the main agent
            if "main" != current_source:
                print("\n\n--- [main agent] ---")
                current_source = "main"
            if token.content:
                print(token.content, end="", flush=True)

print()
```

## Tool calls

When subagents use tools, you can stream tool call events to display what each subagent is doing. Tool call chunks appear in the `messages` stream mode.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
for chunk in agent.stream(
    {"messages": [{"role": "user", "content": "Research recent quantum computing advances"}]},
    stream_mode="messages",
    subgraphs=True,
    version="v2",
):
    if chunk["type"] == "messages":
        token, metadata = chunk["data"]

        # Identify source: "main" or the subagent namespace segment
        is_subagent = any(s.startswith("tools:") for s in chunk["ns"])
        source = next((s for s in chunk["ns"] if s.startswith("tools:")), "main") if is_subagent else "main"

        # Tool call chunks (streaming tool invocations)
        if token.tool_call_chunks:
            for tc in token.tool_call_chunks:
                if tc.get("name"):
                    print(f"\n[{source}] Tool call: {tc['name']}")
                # Args stream in chunks - write them incrementally
                if tc.get("args"):
                    print(tc["args"], end="", flush=True)

        # Tool results
        if token.type == "tool":
            print(f"\n[{source}] Tool result [{token.name}]: {str(token.content)[:150]}")

        # Regular AI content (skip tool call messages)
        if token.type == "ai" and token.content and not token.tool_call_chunks:
            print(token.content, end="", flush=True)

print()
```

## Custom updates

Use [`get_stream_writer`](https://reference.langchain.com/python/langgraph/config/get_stream_writer) inside your subagent tools to emit custom progress events:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import time
from langchain.tools import tool
from langgraph.config import get_stream_writer
from deepagents import create_deep_agent

@tool
def analyze_data(topic: str) -> str:
    """Run a data analysis on a given topic.

    This tool performs the actual analysis and emits progress updates.
    You MUST call this tool for any analysis request.
    """
    writer = get_stream_writer()

    writer({"status": "starting", "topic": topic, "progress": 0})
    time.sleep(0.5)

    writer({"status": "analyzing", "progress": 50})
    time.sleep(0.5)

    writer({"status": "complete", "progress": 100})
    return (
        f'Analysis of "{topic}": Customer sentiment is 85% positive, '
        "driven by product quality and support response times."
    )

agent = create_deep_agent(
    model="google_genai:gemini-3.5-flash",
    system_prompt=(
        "You are a coordinator. For any analysis request, you MUST delegate "
        "to the analyst subagent using the task tool. Never try to answer directly. "
        "After receiving the result, summarize it in one sentence."
    ),
    subagents=[
        {
            "name": "analyst",
            "description": "Performs data analysis with real-time progress tracking",
            "system_prompt": (
                "You are a data analyst. You MUST call the analyze_data tool "
                "for every analysis request. Do not use any other tools. "
                "After the analysis completes, report the result."
            ),
            "tools": [analyze_data],
        },
    ],
)

for chunk in agent.stream(
    {"messages": [{"role": "user", "content": "Analyze customer satisfaction trends"}]},
    stream_mode="custom",
    subgraphs=True,
    version="v2",
):
    if chunk["type"] == "custom":
        is_subagent = any(s.startswith("tools:") for s in chunk["ns"])
        if is_subagent:
            subagent_ns = next(s for s in chunk["ns"] if s.startswith("tools:"))
            print(f"[{subagent_ns}]", chunk["data"])
        else:
            print("[main]", chunk["data"])
```

```shell title="Output" theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
[tools:call_abc123] {'status': 'starting', 'topic': 'customer satisfaction trends', 'progress': 0}
[tools:call_abc123] {'status': 'analyzing', 'progress': 50}
[tools:call_abc123] {'status': 'complete', 'progress': 100}
```

## Stream multiple modes

Combine multiple stream modes to get a complete picture of agent execution:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
