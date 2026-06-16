
      # By default we provide a StateBackend
      agent = create_deep_agent(model="anthropic:claude-sonnet-4-6")

      # Under the hood, it looks like
      agent2 = create_deep_agent(
          model="openai:gpt-5.5",
          backend=StateBackend(),
      )
      ```

      ```python OpenRouter theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      from deepagents import create_deep_agent
      from deepagents.backends import StateBackend

      # By default we provide a StateBackend
      agent = create_deep_agent(model="openrouter:anthropic/claude-sonnet-4-6")

      # Under the hood, it looks like
      agent2 = create_deep_agent(
          model="openai:gpt-5.5",
          backend=StateBackend(),
      )
      ```

      ```python Fireworks theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      from deepagents import create_deep_agent
      from deepagents.backends import StateBackend

      # By default we provide a StateBackend
      agent = create_deep_agent(model="fireworks:accounts/fireworks/models/qwen3p5-397b-a17b")

      # Under the hood, it looks like
      agent2 = create_deep_agent(
          model="openai:gpt-5.5",
          backend=StateBackend(),
      )
      ```

      ```python Baseten theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      from deepagents import create_deep_agent
      from deepagents.backends import StateBackend

      # By default we provide a StateBackend
      agent = create_deep_agent(model="baseten:zai-org/GLM-5")

      # Under the hood, it looks like
      agent2 = create_deep_agent(
          model="openai:gpt-5.5",
          backend=StateBackend(),
      )
      ```

      ```python Ollama theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      from deepagents import create_deep_agent
      from deepagents.backends import StateBackend

      # By default we provide a StateBackend
      agent = create_deep_agent(model="ollama:devstral-2")

      # Under the hood, it looks like
      agent2 = create_deep_agent(
          model="openai:gpt-5.5",
          backend=StateBackend(),
      )
      ```
    </CodeGroup>
  </Tab>

  <Tab title="FilesystemBackend">
    The local machine's filesystem.

    <Warning>
      This backend grants agents direct filesystem read/write access.
      Use with caution and only in appropriate environments.
      For more information, see [`FilesystemBackend`](/oss/python/deepagents/backends#filesystembackend-local-disk).
    </Warning>

    <CodeGroup>
      ```python Google theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      from deepagents import create_deep_agent
      from deepagents.backends import FilesystemBackend

      agent = create_deep_agent(
          model="google_genai:gemini-3.5-flash",
          backend=FilesystemBackend(root_dir=".", virtual_mode=True),
      )
      ```

      ```python OpenAI theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      from deepagents import create_deep_agent
      from deepagents.backends import FilesystemBackend

      agent = create_deep_agent(
          model="openai:gpt-5.5",
          backend=FilesystemBackend(root_dir=".", virtual_mode=True),
      )
      ```

      ```python Anthropic theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      from deepagents import create_deep_agent
      from deepagents.backends import FilesystemBackend

      agent = create_deep_agent(
          model="anthropic:claude-sonnet-4-6",
          backend=FilesystemBackend(root_dir=".", virtual_mode=True),
      )
      ```

      ```python OpenRouter theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      from deepagents import create_deep_agent
      from deepagents.backends import FilesystemBackend

      agent = create_deep_agent(
          model="openrouter:anthropic/claude-sonnet-4-6",
          backend=FilesystemBackend(root_dir=".", virtual_mode=True),
      )
      ```

      ```python Fireworks theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      from deepagents import create_deep_agent
      from deepagents.backends import FilesystemBackend

      agent = create_deep_agent(
          model="fireworks:accounts/fireworks/models/qwen3p5-397b-a17b",
          backend=FilesystemBackend(root_dir=".", virtual_mode=True),
      )
      ```

      ```python Baseten theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      from deepagents import create_deep_agent
      from deepagents.backends import FilesystemBackend

      agent = create_deep_agent(
          model="baseten:zai-org/GLM-5",
          backend=FilesystemBackend(root_dir=".", virtual_mode=True),
      )
      ```

      ```python Ollama theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      from deepagents import create_deep_agent
      from deepagents.backends import FilesystemBackend

      agent = create_deep_agent(
          model="ollama:devstral-2",
          backend=FilesystemBackend(root_dir=".", virtual_mode=True),
      )
      ```
    </CodeGroup>

    <Tip>
      Wrap `FilesystemBackend` in a `CompositeBackend` to prevent internal agent data (offloaded tool results, conversation history) from being written to disk alongside your project files. See the [recommended pattern](/oss/python/deepagents/backends#filesystembackend-local-disk).
    </Tip>
  </Tab>

  <Tab title="LocalShellBackend">
    A filesystem with shell execution directly on the host. Provides filesystem tools plus the `execute` tool for running commands.

    <Warning>
      This backend grants agents direct filesystem read/write access **and** unrestricted shell execution on your host.
      Use with extreme caution and only in appropriate environments.
      For more information, see [`LocalShellBackend`](/oss/python/deepagents/backends#localshellbackend-local-shell).
    </Warning>

    <CodeGroup>
      ```python Google theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      from deepagents import create_deep_agent
      from deepagents.backends import LocalShellBackend

      agent = create_deep_agent(
          model="google_genai:gemini-3.5-flash",
          backend=LocalShellBackend(root_dir=".", virtual_mode=True, env={"PATH": "/usr/bin:/bin"}),
      )
      ```

      ```python OpenAI theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      from deepagents import create_deep_agent
      from deepagents.backends import LocalShellBackend

      agent = create_deep_agent(
          model="openai:gpt-5.5",
          backend=LocalShellBackend(root_dir=".", virtual_mode=True, env={"PATH": "/usr/bin:/bin"}),
      )
      ```

      ```python Anthropic theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      from deepagents import create_deep_agent
      from deepagents.backends import LocalShellBackend

      agent = create_deep_agent(
          model="anthropic:claude-sonnet-4-6",
          backend=LocalShellBackend(root_dir=".", virtual_mode=True, env={"PATH": "/usr/bin:/bin"}),
      )
      ```

      ```python OpenRouter theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      from deepagents import create_deep_agent
      from deepagents.backends import LocalShellBackend

      agent = create_deep_agent(
          model="openrouter:anthropic/claude-sonnet-4-6",
          backend=LocalShellBackend(root_dir=".", virtual_mode=True, env={"PATH": "/usr/bin:/bin"}),
      )
      ```

      ```python Fireworks theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      from deepagents import create_deep_agent
      from deepagents.backends import LocalShellBackend

      agent = create_deep_agent(
          model="fireworks:accounts/fireworks/models/qwen3p5-397b-a17b",
          backend=LocalShellBackend(root_dir=".", virtual_mode=True, env={"PATH": "/usr/bin:/bin"}),
      )
      ```

      ```python Baseten theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      from deepagents import create_deep_agent
      from deepagents.backends import LocalShellBackend

      agent = create_deep_agent(
          model="baseten:zai-org/GLM-5",
          backend=LocalShellBackend(root_dir=".", virtual_mode=True, env={"PATH": "/usr/bin:/bin"}),
      )
      ```

      ```python Ollama theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      from deepagents import create_deep_agent
      from deepagents.backends import LocalShellBackend

      agent = create_deep_agent(
          model="ollama:devstral-2",
          backend=LocalShellBackend(root_dir=".", virtual_mode=True, env={"PATH": "/usr/bin:/bin"}),
      )
      ```
    </CodeGroup>
  </Tab>

  <Tab title="StoreBackend">
    A filesystem that provides long-term storage that is *persisted across threads*.

    <CodeGroup>
      ```python Google theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      from deepagents import create_deep_agent
      from deepagents.backends import StoreBackend
      from langgraph.store.memory import InMemoryStore

      agent = create_deep_agent(
          model="google_genai:gemini-3.5-flash",
          backend=StoreBackend(
              namespace=lambda rt: (rt.server_info.user.identity,),
          ),
          store=InMemoryStore(),  # Good for local dev; omit for LangSmith Deployment
      )
      ```

      ```python OpenAI theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      from deepagents import create_deep_agent
      from deepagents.backends import StoreBackend
      from langgraph.store.memory import InMemoryStore

      agent = create_deep_agent(
          model="openai:gpt-5.5",
          backend=StoreBackend(
              namespace=lambda rt: (rt.server_info.user.identity,),
          ),
          store=InMemoryStore(),  # Good for local dev; omit for LangSmith Deployment
      )
      ```

      ```python Anthropic theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      from deepagents import create_deep_agent
      from deepagents.backends import StoreBackend
      from langgraph.store.memory import InMemoryStore

      agent = create_deep_agent(
          model="anthropic:claude-sonnet-4-6",
          backend=StoreBackend(
              namespace=lambda rt: (rt.server_info.user.identity,),
          ),
          store=InMemoryStore(),  # Good for local dev; omit for LangSmith Deployment
      )
      ```

      ```python OpenRouter theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      from deepagents import create_deep_agent
      from deepagents.backends import StoreBackend
      from langgraph.store.memory import InMemoryStore

      agent = create_deep_agent(
          model="openrouter:anthropic/claude-sonnet-4-6",
          backend=StoreBackend(
              namespace=lambda rt: (rt.server_info.user.identity,),
          ),
          store=InMemoryStore(),  # Good for local dev; omit for LangSmith Deployment
      )
      ```

      ```python Fireworks theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      from deepagents import create_deep_agent
      from deepagents.backends import StoreBackend
      from langgraph.store.memory import InMemoryStore

      agent = create_deep_agent(
          model="fireworks:accounts/fireworks/models/qwen3p5-397b-a17b",
          backend=StoreBackend(
              namespace=lambda rt: (rt.server_info.user.identity,),
          ),
          store=InMemoryStore(),  # Good for local dev; omit for LangSmith Deployment
      )
      ```

      ```python Baseten theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      from deepagents import create_deep_agent
      from deepagents.backends import StoreBackend
      from langgraph.store.memory import InMemoryStore

      agent = create_deep_agent(
          model="baseten:zai-org/GLM-5",
          backend=StoreBackend(
              namespace=lambda rt: (rt.server_info.user.identity,),
          ),
          store=InMemoryStore(),  # Good for local dev; omit for LangSmith Deployment
      )
      ```

      ```python Ollama theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      from deepagents import create_deep_agent
      from deepagents.backends import StoreBackend
      from langgraph.store.memory import InMemoryStore

      agent = create_deep_agent(
          model="ollama:devstral-2",
          backend=StoreBackend(
              namespace=lambda rt: (rt.server_info.user.identity,),
          ),
          store=InMemoryStore(),  # Good for local dev; omit for LangSmith Deployment
      )
      ```
    </CodeGroup>

    <Note>
      When deploying to [LangSmith Deployment](/langsmith/deployment), omit the `store` parameter. The platform automatically provisions a store for your agent.
    </Note>

    <Tip>
      The `namespace` parameter controls data isolation. For multi-user deployments, always set a [namespace factory](/oss/python/deepagents/backends#namespace-factories) to isolate data per user or tenant.
    </Tip>
  </Tab>

  <Tab title="ContextHubBackend">
    Durable filesystem storage in a LangSmith Hub repo.

    <CodeGroup>
      ```python Google theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      from deepagents import create_deep_agent
      from deepagents.backends import ContextHubBackend

      agent = create_deep_agent(
          model="google_genai:gemini-3.5-flash",
          backend=ContextHubBackend("my-agent"),
      )
      ```

      ```python OpenAI theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      from deepagents import create_deep_agent
      from deepagents.backends import ContextHubBackend

      agent = create_deep_agent(
          model="openai:gpt-5.5",
          backend=ContextHubBackend("my-agent"),
      )
      ```

      ```python Anthropic theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      from deepagents import create_deep_agent
      from deepagents.backends import ContextHubBackend

      agent = create_deep_agent(
          model="anthropic:claude-sonnet-4-6",
          backend=ContextHubBackend("my-agent"),
      )
      ```

      ```python OpenRouter theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      from deepagents import create_deep_agent
      from deepagents.backends import ContextHubBackend

      agent = create_deep_agent(
          model="openrouter:anthropic/claude-sonnet-4-6",
          backend=ContextHubBackend("my-agent"),
      )
      ```

      ```python Fireworks theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      from deepagents import create_deep_agent
      from deepagents.backends import ContextHubBackend

      agent = create_deep_agent(
          model="fireworks:accounts/fireworks/models/qwen3p5-397b-a17b",
          backend=ContextHubBackend("my-agent"),
      )
      ```

      ```python Baseten theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      from deepagents import create_deep_agent
      from deepagents.backends import ContextHubBackend

      agent = create_deep_agent(
          model="baseten:zai-org/GLM-5",
          backend=ContextHubBackend("my-agent"),
      )
      ```

      ```python Ollama theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      from deepagents import create_deep_agent
      from deepagents.backends import ContextHubBackend

      agent = create_deep_agent(
          model="ollama:devstral-2",
          backend=ContextHubBackend("my-agent"),
      )
      ```
    </CodeGroup>

    For more details, see [`ContextHubBackend`](/oss/python/deepagents/backends#contexthubbackend).
  </Tab>

  <Tab title="CompositeBackend">
    A flexible backend where you can specify different routes in the filesystem to point towards different backends.

    <CodeGroup>
      ```python Google theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      from deepagents import create_deep_agent
      from deepagents.backends import CompositeBackend, StateBackend, StoreBackend
      from langgraph.store.memory import InMemoryStore

      agent = create_deep_agent(
          model="google_genai:gemini-3.5-flash",
          backend=CompositeBackend(
              default=StateBackend(),
              routes={
                  "/memories/": StoreBackend(namespace=lambda _rt: ("memories",)),
              },
          ),
          store=InMemoryStore(),  # Store passed to create_deep_agent, not backend
      )
      ```

      ```python OpenAI theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      from deepagents import create_deep_agent
      from deepagents.backends import CompositeBackend, StateBackend, StoreBackend
      from langgraph.store.memory import InMemoryStore

      agent = create_deep_agent(
          model="openai:gpt-5.5",
          backend=CompositeBackend(
              default=StateBackend(),
              routes={
                  "/memories/": StoreBackend(namespace=lambda _rt: ("memories",)),
              },
          ),
          store=InMemoryStore(),  # Store passed to create_deep_agent, not backend
      )
      ```

      ```python Anthropic theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      from deepagents import create_deep_agent
      from deepagents.backends import CompositeBackend, StateBackend, StoreBackend
      from langgraph.store.memory import InMemoryStore

      agent = create_deep_agent(
          model="anthropic:claude-sonnet-4-6",
          backend=CompositeBackend(
              default=StateBackend(),
              routes={
                  "/memories/": StoreBackend(namespace=lambda _rt: ("memories",)),
              },
          ),
          store=InMemoryStore(),  # Store passed to create_deep_agent, not backend
      )
      ```

      ```python OpenRouter theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      from deepagents import create_deep_agent
      from deepagents.backends import CompositeBackend, StateBackend, StoreBackend
      from langgraph.store.memory import InMemoryStore

      agent = create_deep_agent(
          model="openrouter:anthropic/claude-sonnet-4-6",
          backend=CompositeBackend(
              default=StateBackend(),
              routes={
                  "/memories/": StoreBackend(namespace=lambda _rt: ("memories",)),
              },
          ),
          store=InMemoryStore(),  # Store passed to create_deep_agent, not backend
      )
      ```

      ```python Fireworks theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      from deepagents import create_deep_agent
      from deepagents.backends import CompositeBackend, StateBackend, StoreBackend
      from langgraph.store.memory import InMemoryStore

      agent = create_deep_agent(
          model="fireworks:accounts/fireworks/models/qwen3p5-397b-a17b",
          backend=CompositeBackend(
              default=StateBackend(),
              routes={
                  "/memories/": StoreBackend(namespace=lambda _rt: ("memories",)),
              },
          ),
          store=InMemoryStore(),  # Store passed to create_deep_agent, not backend
      )
      ```

      ```python Baseten theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      from deepagents import create_deep_agent
      from deepagents.backends import CompositeBackend, StateBackend, StoreBackend
      from langgraph.store.memory import InMemoryStore

      agent = create_deep_agent(
          model="baseten:zai-org/GLM-5",
          backend=CompositeBackend(
              default=StateBackend(),
              routes={
                  "/memories/": StoreBackend(namespace=lambda _rt: ("memories",)),
              },
          ),
          store=InMemoryStore(),  # Store passed to create_deep_agent, not backend
      )
      ```

      ```python Ollama theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      from deepagents import create_deep_agent
      from deepagents.backends import CompositeBackend, StateBackend, StoreBackend
      from langgraph.store.memory import InMemoryStore

      agent = create_deep_agent(
          model="ollama:devstral-2",
          backend=CompositeBackend(
              default=StateBackend(),
              routes={
                  "/memories/": StoreBackend(namespace=lambda _rt: ("memories",)),
              },
          ),
          store=InMemoryStore(),  # Store passed to create_deep_agent, not backend
      )
      ```
    </CodeGroup>
  </Tab>
</Tabs>

For more information, see [Backends](/oss/python/deepagents/backends).

### Sandboxes

Sandboxes are specialized [backends](/oss/python/deepagents/backends) that run agent code in an isolated environment with their own filesystem and an `execute` tool for shell commands.
Use a sandbox backend when you want your deep agent to write files, install dependencies, and run commands without changing anything on your local machine.

You configure sandboxes by passing a sandbox backend to `backend` when creating your deep agent:

<Tabs>
  <Tab title="LangSmith">
    <CodeGroup>
      ```bash pip theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      pip install "langsmith[sandbox]"
      ```

      ```bash uv theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      uv add "langsmith[sandbox]"
      ```
    </CodeGroup>

    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    from deepagents import create_deep_agent
    from deepagents.backends import LangSmithSandbox
    from langchain_anthropic import ChatAnthropic
    from langsmith.sandbox import SandboxClient

    client = SandboxClient()
    ls_sandbox = client.create_sandbox()
    backend = LangSmithSandbox(sandbox=ls_sandbox)

    agent = create_deep_agent(
        model=ChatAnthropic(model="claude-sonnet-4-6"),
        system_prompt="You are a Python coding assistant with sandbox access.",
        backend=backend,
    )
    try:
        result = agent.invoke(
            {
                "messages": [
                    {
                        "role": "user",
                        "content": "Create a small Python package and run pytest",
                    }
                ]
            }
        )
    finally:
        client.delete_sandbox(ls_sandbox.name)
    ```
  </Tab>

  <Tab title="Daytona">
    <CodeGroup>
      ```bash pip theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      pip install langchain-daytona
      ```

      ```bash uv theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      uv add langchain-daytona
      ```
    </CodeGroup>

    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    from daytona import Daytona
    from deepagents import create_deep_agent
    from langchain_anthropic import ChatAnthropic
    from langchain_daytona import DaytonaSandbox

    sandbox = Daytona().create()
    backend = DaytonaSandbox(sandbox=sandbox)

    agent = create_deep_agent(
        model=ChatAnthropic(model="claude-sonnet-4-6"),
        system_prompt="You are a Python coding assistant with sandbox access.",
        backend=backend,
    )

    try:
        result = agent.invoke(
            {
                "messages": [
                    {
                        "role": "user",
                        "content": "Create a small Python package and run pytest",
                    }
                ]
            }
        )
    finally:
        sandbox.stop()
    ```
  </Tab>

  <Tab title="E2B">
    <CodeGroup>
      ```bash pip theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      pip install langchain-e2b
      ```

      ```bash uv theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      uv add langchain-e2b
      ```
    </CodeGroup>

    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    from e2b import Sandbox
    from deepagents import create_deep_agent
    from langchain_anthropic import ChatAnthropic
    from langchain_e2b import E2BSandbox

    e2b_sandbox = Sandbox.create()
    backend = E2BSandbox(sandbox=e2b_sandbox)

    agent = create_deep_agent(
        model=ChatAnthropic(model="claude-sonnet-4-6"),
        system_prompt="You are a Python coding assistant with sandbox access.",
        backend=backend,
    )

    try:
        result = agent.invoke(
            {
                "messages": [
                    {
                        "role": "user",
                        "content": "Create a small Python package and run pytest",
                    }
                ]
            }
        )
    finally:
        e2b_sandbox.kill()
    ```
  </Tab>

  <Tab title="Modal">
    <CodeGroup>
      ```bash pip theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      pip install langchain-modal
      ```

      ```bash uv theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      uv add langchain-modal
      ```
    </CodeGroup>

    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    import modal
    from deepagents import create_deep_agent
    from langchain_anthropic import ChatAnthropic
