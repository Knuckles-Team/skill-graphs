    from langchain_modal import ModalSandbox

    app = modal.App.lookup("your-app")
    modal_sandbox = modal.Sandbox.create(app=app)
    backend = ModalSandbox(sandbox=modal_sandbox)

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
        modal_sandbox.terminate()
    ```
  </Tab>

  <Tab title="Runloop">
    <CodeGroup>
      ```bash pip theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      pip install langchain-runloop
      ```

      ```bash uv theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      uv add langchain-runloop
      ```
    </CodeGroup>

    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    import os

    from deepagents import create_deep_agent
    from langchain_anthropic import ChatAnthropic
    from langchain_runloop import RunloopSandbox
    from runloop_api_client import RunloopSDK

    client = RunloopSDK(bearer_token=os.environ["RUNLOOP_API_KEY"])

    devbox = client.devbox.create()
    backend = RunloopSandbox(devbox=devbox)

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
        devbox.shutdown()
    ```
  </Tab>

  <Tab title="Vercel">
    <CodeGroup>
      ```bash pip theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      pip install langchain-vercel-sandbox
      ```

      ```bash uv theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      uv add langchain-vercel-sandbox
      ```
    </CodeGroup>

    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    from deepagents import create_deep_agent
    from langchain_anthropic import ChatAnthropic
    from langchain_vercel_sandbox import VercelSandbox
    from vercel.sandbox import Sandbox

    sandbox = Sandbox.create()
    backend = VercelSandbox(sandbox=sandbox)

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
</Tabs>

For more information, see [Sandboxes](/oss/python/deepagents/sandboxes).

## Human-in-the-loop

Some tool operations may be sensitive and require human approval before execution.
You can configure the approval for each tool:

<CodeGroup>
  ```python Google theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langchain.tools import tool
  from deepagents import create_deep_agent
  from langgraph.checkpoint.memory import MemorySaver

  @tool
  def remove_file(path: str) -> str:
      """Delete a file from the filesystem."""
      return f"Deleted {path}"

  @tool
  def fetch_file(path: str) -> str:
      """Read a file from the filesystem."""
      return f"Contents of {path}"

  @tool
  def notify_email(to: str, subject: str, body: str) -> str:
      """Send an email."""
      return f"Sent email to {to}"

  # Checkpointer is REQUIRED for human-in-the-loop
  checkpointer = MemorySaver()

  agent = create_deep_agent(
      model="google_genai:gemini-3.5-flash",
      tools=[remove_file, fetch_file, notify_email],
      interrupt_on={
          "remove_file": True,  # Default: approve, edit, reject, respond
          "fetch_file": False,  # No interrupts needed
          "notify_email": {"allowed_decisions": ["approve", "reject"]},  # No editing
      },
      checkpointer=checkpointer,  # Required!
  )
  ```

  ```python OpenAI theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langchain.tools import tool
  from deepagents import create_deep_agent
  from langgraph.checkpoint.memory import MemorySaver

  @tool
  def remove_file(path: str) -> str:
      """Delete a file from the filesystem."""
      return f"Deleted {path}"

  @tool
  def fetch_file(path: str) -> str:
      """Read a file from the filesystem."""
      return f"Contents of {path}"

  @tool
  def notify_email(to: str, subject: str, body: str) -> str:
      """Send an email."""
      return f"Sent email to {to}"

  # Checkpointer is REQUIRED for human-in-the-loop
  checkpointer = MemorySaver()

  agent = create_deep_agent(
      model="openai:gpt-5.5",
      tools=[remove_file, fetch_file, notify_email],
      interrupt_on={
          "remove_file": True,  # Default: approve, edit, reject, respond
          "fetch_file": False,  # No interrupts needed
          "notify_email": {"allowed_decisions": ["approve", "reject"]},  # No editing
      },
      checkpointer=checkpointer,  # Required!
  )
  ```

  ```python Anthropic theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langchain.tools import tool
  from deepagents import create_deep_agent
  from langgraph.checkpoint.memory import MemorySaver

  @tool
  def remove_file(path: str) -> str:
      """Delete a file from the filesystem."""
      return f"Deleted {path}"

  @tool
  def fetch_file(path: str) -> str:
      """Read a file from the filesystem."""
      return f"Contents of {path}"

  @tool
  def notify_email(to: str, subject: str, body: str) -> str:
      """Send an email."""
      return f"Sent email to {to}"

  # Checkpointer is REQUIRED for human-in-the-loop
  checkpointer = MemorySaver()

  agent = create_deep_agent(
      model="anthropic:claude-sonnet-4-6",
      tools=[remove_file, fetch_file, notify_email],
      interrupt_on={
          "remove_file": True,  # Default: approve, edit, reject, respond
          "fetch_file": False,  # No interrupts needed
          "notify_email": {"allowed_decisions": ["approve", "reject"]},  # No editing
      },
      checkpointer=checkpointer,  # Required!
  )
  ```

  ```python OpenRouter theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langchain.tools import tool
  from deepagents import create_deep_agent
  from langgraph.checkpoint.memory import MemorySaver

  @tool
  def remove_file(path: str) -> str:
      """Delete a file from the filesystem."""
      return f"Deleted {path}"

  @tool
  def fetch_file(path: str) -> str:
      """Read a file from the filesystem."""
      return f"Contents of {path}"

  @tool
  def notify_email(to: str, subject: str, body: str) -> str:
      """Send an email."""
      return f"Sent email to {to}"

  # Checkpointer is REQUIRED for human-in-the-loop
  checkpointer = MemorySaver()

  agent = create_deep_agent(
      model="openrouter:anthropic/claude-sonnet-4-6",
      tools=[remove_file, fetch_file, notify_email],
      interrupt_on={
          "remove_file": True,  # Default: approve, edit, reject, respond
          "fetch_file": False,  # No interrupts needed
          "notify_email": {"allowed_decisions": ["approve", "reject"]},  # No editing
      },
      checkpointer=checkpointer,  # Required!
  )
  ```

  ```python Fireworks theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langchain.tools import tool
  from deepagents import create_deep_agent
  from langgraph.checkpoint.memory import MemorySaver

  @tool
  def remove_file(path: str) -> str:
      """Delete a file from the filesystem."""
      return f"Deleted {path}"

  @tool
  def fetch_file(path: str) -> str:
      """Read a file from the filesystem."""
      return f"Contents of {path}"

  @tool
  def notify_email(to: str, subject: str, body: str) -> str:
      """Send an email."""
      return f"Sent email to {to}"

  # Checkpointer is REQUIRED for human-in-the-loop
  checkpointer = MemorySaver()

  agent = create_deep_agent(
      model="fireworks:accounts/fireworks/models/qwen3p5-397b-a17b",
      tools=[remove_file, fetch_file, notify_email],
      interrupt_on={
          "remove_file": True,  # Default: approve, edit, reject, respond
          "fetch_file": False,  # No interrupts needed
          "notify_email": {"allowed_decisions": ["approve", "reject"]},  # No editing
      },
      checkpointer=checkpointer,  # Required!
  )
  ```

  ```python Baseten theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langchain.tools import tool
  from deepagents import create_deep_agent
  from langgraph.checkpoint.memory import MemorySaver

  @tool
  def remove_file(path: str) -> str:
      """Delete a file from the filesystem."""
      return f"Deleted {path}"

  @tool
  def fetch_file(path: str) -> str:
      """Read a file from the filesystem."""
      return f"Contents of {path}"

  @tool
  def notify_email(to: str, subject: str, body: str) -> str:
      """Send an email."""
      return f"Sent email to {to}"

  # Checkpointer is REQUIRED for human-in-the-loop
  checkpointer = MemorySaver()

  agent = create_deep_agent(
      model="baseten:zai-org/GLM-5",
      tools=[remove_file, fetch_file, notify_email],
      interrupt_on={
          "remove_file": True,  # Default: approve, edit, reject, respond
          "fetch_file": False,  # No interrupts needed
          "notify_email": {"allowed_decisions": ["approve", "reject"]},  # No editing
      },
      checkpointer=checkpointer,  # Required!
  )
  ```

  ```python Ollama theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langchain.tools import tool
  from deepagents import create_deep_agent
  from langgraph.checkpoint.memory import MemorySaver

  @tool
  def remove_file(path: str) -> str:
      """Delete a file from the filesystem."""
      return f"Deleted {path}"

  @tool
  def fetch_file(path: str) -> str:
      """Read a file from the filesystem."""
      return f"Contents of {path}"

  @tool
  def notify_email(to: str, subject: str, body: str) -> str:
      """Send an email."""
      return f"Sent email to {to}"

  # Checkpointer is REQUIRED for human-in-the-loop
  checkpointer = MemorySaver()

  agent = create_deep_agent(
      model="ollama:devstral-2",
      tools=[remove_file, fetch_file, notify_email],
      interrupt_on={
          "remove_file": True,  # Default: approve, edit, reject, respond
          "fetch_file": False,  # No interrupts needed
          "notify_email": {"allowed_decisions": ["approve", "reject"]},  # No editing
      },
      checkpointer=checkpointer,  # Required!
  )
  ```
</CodeGroup>

You can configure interrupt for agents and subagents on tool call as well as from within tool calls.
For more information, see [Human-in-the-loop](/oss/python/deepagents/human-in-the-loop).

## Skills

You can use [skills](/oss/python/deepagents/overview) to provide your deep agent with new capabilities and expertise.
While [tools](/oss/python/deepagents/customization#tools) tend to cover lower level functionality like native file system actions or planning, skills can contain detailed instructions on how to complete tasks, reference info, and other assets, such as templates.
These files are only loaded by the agent when the agent has determined that the skill is useful for the current prompt.
This progressive disclosure reduces the amount of tokens and context the agent has to consider upon startup.

For example skills, see [Deep Agents example skills](https://github.com/langchain-ai/deepagentsjs/tree/main/examples/skills).

To add skills to your deep agent, pass them as an argument to `create_deep_agent`:

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

## Memory

Use [`AGENTS.md` files](https://agents.md/) to provide extra context to your deep agent.

You can pass one or more file paths to the `memory` parameter when creating your deep agent:

<Tabs>
  <Tab title="StateBackend">
    <CodeGroup>
      ```python Google theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      from urllib.request import urlopen

      from deepagents import create_deep_agent
      from deepagents.backends.utils import create_file_data
      from langgraph.checkpoint.memory import MemorySaver

      with urlopen(
          "https://raw.githubusercontent.com/langchain-ai/deepagents/refs/heads/main/examples/text-to-sql-agent/AGENTS.md"
      ) as response:
          agents_md = response.read().decode("utf-8")
      checkpointer = MemorySaver()

      agent = create_deep_agent(
          model="google_genai:gemini-3.5-flash",
          memory=[
              "/AGENTS.md"
          ],
          checkpointer=checkpointer,
      )

      result = agent.invoke(
          {
              "messages": [
                  {
                      "role": "user",
                      "content": "Please tell me what's in your memory files.",
                  }
              ],
              # Seed the default StateBackend's in-state filesystem (virtual paths must start with "/").
              "files": {"/AGENTS.md": create_file_data(agents_md)},
          },
          config={"configurable": {"thread_id": "123456"}},
      )
      ```

      ```python OpenAI theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      from urllib.request import urlopen

      from deepagents import create_deep_agent
      from deepagents.backends.utils import create_file_data
      from langgraph.checkpoint.memory import MemorySaver
