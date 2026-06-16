
      with urlopen(
          "https://raw.githubusercontent.com/langchain-ai/deepagents/refs/heads/main/examples/text-to-sql-agent/AGENTS.md"
      ) as response:
          agents_md = response.read().decode("utf-8")
      checkpointer = MemorySaver()

      agent = create_deep_agent(
          model="openai:gpt-5.5",
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

      ```python Anthropic theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
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
          model="anthropic:claude-sonnet-4-6",
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

      ```python OpenRouter theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
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
          model="openrouter:anthropic/claude-sonnet-4-6",
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

      ```python Fireworks theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
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
          model="fireworks:accounts/fireworks/models/qwen3p5-397b-a17b",
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

      ```python Baseten theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
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
          model="baseten:zai-org/GLM-5",
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

      ```python Ollama theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
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
          model="ollama:devstral-2",
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
    </CodeGroup>
  </Tab>

  <Tab title="StoreBackend">
    <CodeGroup>
      ```python Google theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      from urllib.request import urlopen

      from deepagents import create_deep_agent
      from deepagents.backends import StoreBackend
      from deepagents.backends.utils import create_file_data
      from langgraph.store.memory import InMemoryStore

      with urlopen(
          "https://raw.githubusercontent.com/langchain-ai/deepagents/refs/heads/main/examples/text-to-sql-agent/AGENTS.md"
      ) as response:
          agents_md = response.read().decode("utf-8")

      # Create the store and add the file to it
      store = InMemoryStore()
      file_data = create_file_data(agents_md)
      store.put(
          namespace=("filesystem",),
          key="/AGENTS.md",
          value=file_data,
      )

      agent = create_deep_agent(
          model="google_genai:gemini-3.5-flash",
          backend=StoreBackend(namespace=lambda _rt: ("filesystem",)),
          store=store,
          memory=["/AGENTS.md"],
      )

      result = agent.invoke(
          {
              "messages": [
                  {
                      "role": "user",
                      "content": "Please tell me what's in your memory files.",
                  }
              ],
              "files": {"/AGENTS.md": create_file_data(agents_md)},
          },
          config={"configurable": {"thread_id": "12345"}},
      )
      ```

      ```python OpenAI theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      from urllib.request import urlopen

      from deepagents import create_deep_agent
      from deepagents.backends import StoreBackend
      from deepagents.backends.utils import create_file_data
      from langgraph.store.memory import InMemoryStore

      with urlopen(
          "https://raw.githubusercontent.com/langchain-ai/deepagents/refs/heads/main/examples/text-to-sql-agent/AGENTS.md"
      ) as response:
          agents_md = response.read().decode("utf-8")

      # Create the store and add the file to it
      store = InMemoryStore()
      file_data = create_file_data(agents_md)
      store.put(
          namespace=("filesystem",),
          key="/AGENTS.md",
          value=file_data,
      )

      agent = create_deep_agent(
          model="openai:gpt-5.5",
          backend=StoreBackend(namespace=lambda _rt: ("filesystem",)),
          store=store,
          memory=["/AGENTS.md"],
      )

      result = agent.invoke(
          {
              "messages": [
                  {
                      "role": "user",
                      "content": "Please tell me what's in your memory files.",
                  }
              ],
              "files": {"/AGENTS.md": create_file_data(agents_md)},
          },
          config={"configurable": {"thread_id": "12345"}},
      )
      ```

      ```python Anthropic theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      from urllib.request import urlopen

      from deepagents import create_deep_agent
      from deepagents.backends import StoreBackend
      from deepagents.backends.utils import create_file_data
      from langgraph.store.memory import InMemoryStore

      with urlopen(
          "https://raw.githubusercontent.com/langchain-ai/deepagents/refs/heads/main/examples/text-to-sql-agent/AGENTS.md"
      ) as response:
          agents_md = response.read().decode("utf-8")

      # Create the store and add the file to it
      store = InMemoryStore()
      file_data = create_file_data(agents_md)
      store.put(
          namespace=("filesystem",),
          key="/AGENTS.md",
          value=file_data,
      )

      agent = create_deep_agent(
          model="anthropic:claude-sonnet-4-6",
          backend=StoreBackend(namespace=lambda _rt: ("filesystem",)),
          store=store,
          memory=["/AGENTS.md"],
      )

      result = agent.invoke(
          {
              "messages": [
                  {
                      "role": "user",
                      "content": "Please tell me what's in your memory files.",
                  }
              ],
              "files": {"/AGENTS.md": create_file_data(agents_md)},
          },
          config={"configurable": {"thread_id": "12345"}},
      )
      ```

      ```python OpenRouter theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      from urllib.request import urlopen

      from deepagents import create_deep_agent
      from deepagents.backends import StoreBackend
      from deepagents.backends.utils import create_file_data
      from langgraph.store.memory import InMemoryStore

      with urlopen(
          "https://raw.githubusercontent.com/langchain-ai/deepagents/refs/heads/main/examples/text-to-sql-agent/AGENTS.md"
      ) as response:
          agents_md = response.read().decode("utf-8")

      # Create the store and add the file to it
      store = InMemoryStore()
      file_data = create_file_data(agents_md)
      store.put(
          namespace=("filesystem",),
          key="/AGENTS.md",
          value=file_data,
      )

      agent = create_deep_agent(
          model="openrouter:anthropic/claude-sonnet-4-6",
          backend=StoreBackend(namespace=lambda _rt: ("filesystem",)),
          store=store,
          memory=["/AGENTS.md"],
      )

      result = agent.invoke(
          {
              "messages": [
                  {
                      "role": "user",
                      "content": "Please tell me what's in your memory files.",
                  }
              ],
              "files": {"/AGENTS.md": create_file_data(agents_md)},
          },
          config={"configurable": {"thread_id": "12345"}},
      )
      ```

      ```python Fireworks theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      from urllib.request import urlopen

      from deepagents import create_deep_agent
      from deepagents.backends import StoreBackend
      from deepagents.backends.utils import create_file_data
      from langgraph.store.memory import InMemoryStore

      with urlopen(
          "https://raw.githubusercontent.com/langchain-ai/deepagents/refs/heads/main/examples/text-to-sql-agent/AGENTS.md"
      ) as response:
          agents_md = response.read().decode("utf-8")

      # Create the store and add the file to it
      store = InMemoryStore()
      file_data = create_file_data(agents_md)
      store.put(
          namespace=("filesystem",),
          key="/AGENTS.md",
          value=file_data,
      )

      agent = create_deep_agent(
          model="fireworks:accounts/fireworks/models/qwen3p5-397b-a17b",
          backend=StoreBackend(namespace=lambda _rt: ("filesystem",)),
          store=store,
          memory=["/AGENTS.md"],
      )

      result = agent.invoke(
          {
              "messages": [
                  {
                      "role": "user",
                      "content": "Please tell me what's in your memory files.",
                  }
              ],
              "files": {"/AGENTS.md": create_file_data(agents_md)},
          },
          config={"configurable": {"thread_id": "12345"}},
      )
      ```

      ```python Baseten theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      from urllib.request import urlopen

      from deepagents import create_deep_agent
      from deepagents.backends import StoreBackend
      from deepagents.backends.utils import create_file_data
      from langgraph.store.memory import InMemoryStore

      with urlopen(
          "https://raw.githubusercontent.com/langchain-ai/deepagents/refs/heads/main/examples/text-to-sql-agent/AGENTS.md"
      ) as response:
          agents_md = response.read().decode("utf-8")

      # Create the store and add the file to it
      store = InMemoryStore()
      file_data = create_file_data(agents_md)
      store.put(
          namespace=("filesystem",),
          key="/AGENTS.md",
          value=file_data,
      )

      agent = create_deep_agent(
          model="baseten:zai-org/GLM-5",
          backend=StoreBackend(namespace=lambda _rt: ("filesystem",)),
          store=store,
          memory=["/AGENTS.md"],
      )

      result = agent.invoke(
          {
              "messages": [
                  {
                      "role": "user",
                      "content": "Please tell me what's in your memory files.",
                  }
              ],
              "files": {"/AGENTS.md": create_file_data(agents_md)},
          },
          config={"configurable": {"thread_id": "12345"}},
      )
      ```

      ```python Ollama theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      from urllib.request import urlopen

      from deepagents import create_deep_agent
      from deepagents.backends import StoreBackend
      from deepagents.backends.utils import create_file_data
      from langgraph.store.memory import InMemoryStore

      with urlopen(
          "https://raw.githubusercontent.com/langchain-ai/deepagents/refs/heads/main/examples/text-to-sql-agent/AGENTS.md"
      ) as response:
          agents_md = response.read().decode("utf-8")

      # Create the store and add the file to it
      store = InMemoryStore()
      file_data = create_file_data(agents_md)
      store.put(
          namespace=("filesystem",),
          key="/AGENTS.md",
          value=file_data,
      )

      agent = create_deep_agent(
          model="ollama:devstral-2",
          backend=StoreBackend(namespace=lambda _rt: ("filesystem",)),
          store=store,
          memory=["/AGENTS.md"],
      )

      result = agent.invoke(
          {
              "messages": [
                  {
                      "role": "user",
                      "content": "Please tell me what's in your memory files.",
                  }
              ],
              "files": {"/AGENTS.md": create_file_data(agents_md)},
          },
          config={"configurable": {"thread_id": "12345"}},
      )
      ```
    </CodeGroup>
  </Tab>

  <Tab title="FilesystemBackend">
    <CodeGroup>
      ```python Google theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      from deepagents import create_deep_agent
      from deepagents.backends import FilesystemBackend
      from langgraph.checkpoint.memory import MemorySaver

      # Checkpointer is REQUIRED for human-in-the-loop
      checkpointer = MemorySaver()

      agent = create_deep_agent(
          model="google_genai:gemini-3.5-flash",
          backend=FilesystemBackend(root_dir="/Users/user/{project}"),
          memory=[
              "./AGENTS.md"
          ],
          interrupt_on={
              "write_file": True,  # Default: approve, edit, reject
              "read_file": False,  # No interrupts needed
              "edit_file": True,   # Default: approve, edit, reject
          },
          checkpointer=checkpointer,  # Required!
      )

      result = agent.invoke(
          {
              "messages": [
                  {
                      "role": "user",
                      "content": "Please tell me what's in your memory files.",
                  }
              ],
          },
          config={"configurable": {"thread_id": "12345"}},
      )
      ```

      ```python OpenAI theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      from deepagents import create_deep_agent
      from deepagents.backends import FilesystemBackend
      from langgraph.checkpoint.memory import MemorySaver

      # Checkpointer is REQUIRED for human-in-the-loop
      checkpointer = MemorySaver()

      agent = create_deep_agent(
          model="openai:gpt-5.5",
          backend=FilesystemBackend(root_dir="/Users/user/{project}"),
          memory=[
              "./AGENTS.md"
          ],
          interrupt_on={
              "write_file": True,  # Default: approve, edit, reject
              "read_file": False,  # No interrupts needed
              "edit_file": True,   # Default: approve, edit, reject
          },
          checkpointer=checkpointer,  # Required!
      )

      result = agent.invoke(
          {
              "messages": [
                  {
                      "role": "user",
                      "content": "Please tell me what's in your memory files.",
                  }
              ],
          },
          config={"configurable": {"thread_id": "12345"}},
      )
      ```

      ```python Anthropic theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      from deepagents import create_deep_agent
      from deepagents.backends import FilesystemBackend
      from langgraph.checkpoint.memory import MemorySaver

      # Checkpointer is REQUIRED for human-in-the-loop
      checkpointer = MemorySaver()

      agent = create_deep_agent(
          model="anthropic:claude-sonnet-4-6",
          backend=FilesystemBackend(root_dir="/Users/user/{project}"),
          memory=[
              "./AGENTS.md"
          ],
          interrupt_on={
              "write_file": True,  # Default: approve, edit, reject
              "read_file": False,  # No interrupts needed
              "edit_file": True,   # Default: approve, edit, reject
          },
          checkpointer=checkpointer,  # Required!
      )

      result = agent.invoke(
          {
              "messages": [
                  {
                      "role": "user",
                      "content": "Please tell me what's in your memory files.",
                  }
              ],
          },
          config={"configurable": {"thread_id": "12345"}},
      )
      ```

      ```python OpenRouter theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      from deepagents import create_deep_agent
      from deepagents.backends import FilesystemBackend
      from langgraph.checkpoint.memory import MemorySaver

      # Checkpointer is REQUIRED for human-in-the-loop
      checkpointer = MemorySaver()

      agent = create_deep_agent(
          model="openrouter:anthropic/claude-sonnet-4-6",
          backend=FilesystemBackend(root_dir="/Users/user/{project}"),
          memory=[
              "./AGENTS.md"
          ],
          interrupt_on={
              "write_file": True,  # Default: approve, edit, reject
              "read_file": False,  # No interrupts needed
              "edit_file": True,   # Default: approve, edit, reject
          },
          checkpointer=checkpointer,  # Required!
      )

      result = agent.invoke(
          {
              "messages": [
                  {
                      "role": "user",
                      "content": "Please tell me what's in your memory files.",
                  }
              ],
          },
          config={"configurable": {"thread_id": "12345"}},
      )
      ```

      ```python Fireworks theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      from deepagents import create_deep_agent
      from deepagents.backends import FilesystemBackend
      from langgraph.checkpoint.memory import MemorySaver

      # Checkpointer is REQUIRED for human-in-the-loop
      checkpointer = MemorySaver()

      agent = create_deep_agent(
          model="fireworks:accounts/fireworks/models/qwen3p5-397b-a17b",
          backend=FilesystemBackend(root_dir="/Users/user/{project}"),
          memory=[
              "./AGENTS.md"
          ],
          interrupt_on={
              "write_file": True,  # Default: approve, edit, reject
              "read_file": False,  # No interrupts needed
              "edit_file": True,   # Default: approve, edit, reject
          },
          checkpointer=checkpointer,  # Required!
      )

      result = agent.invoke(
          {
              "messages": [
                  {
                      "role": "user",
                      "content": "Please tell me what's in your memory files.",
                  }
              ],
          },
          config={"configurable": {"thread_id": "12345"}},
      )
      ```

      ```python Baseten theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      from deepagents import create_deep_agent
      from deepagents.backends import FilesystemBackend
      from langgraph.checkpoint.memory import MemorySaver

      # Checkpointer is REQUIRED for human-in-the-loop
      checkpointer = MemorySaver()

      agent = create_deep_agent(
          model="baseten:zai-org/GLM-5",
          backend=FilesystemBackend(root_dir="/Users/user/{project}"),
          memory=[
              "./AGENTS.md"
          ],
          interrupt_on={
              "write_file": True,  # Default: approve, edit, reject
              "read_file": False,  # No interrupts needed
              "edit_file": True,   # Default: approve, edit, reject
          },
          checkpointer=checkpointer,  # Required!
      )

      result = agent.invoke(
          {
              "messages": [
                  {
                      "role": "user",
                      "content": "Please tell me what's in your memory files.",
                  }
              ],
          },
          config={"configurable": {"thread_id": "12345"}},
      )
      ```

      ```python Ollama theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      from deepagents import create_deep_agent
      from deepagents.backends import FilesystemBackend
      from langgraph.checkpoint.memory import MemorySaver

      # Checkpointer is REQUIRED for human-in-the-loop
      checkpointer = MemorySaver()

      agent = create_deep_agent(
          model="ollama:devstral-2",
          backend=FilesystemBackend(root_dir="/Users/user/{project}"),
          memory=[
              "./AGENTS.md"
          ],
          interrupt_on={
              "write_file": True,  # Default: approve, edit, reject
              "read_file": False,  # No interrupts needed
              "edit_file": True,   # Default: approve, edit, reject
          },
          checkpointer=checkpointer,  # Required!
      )

      result = agent.invoke(
          {
              "messages": [
                  {
                      "role": "user",
                      "content": "Please tell me what's in your memory files.",
                  }
