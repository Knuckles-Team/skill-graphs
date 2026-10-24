# Model providers
Source: https://docs.langchain.com/oss/python/deepagents/code/providers

Configure any LangChain-compatible model provider for Deep Agents Code

Deep Agents Code supports any [chat model provider compatible with LangChain](/oss/python/integrations/chat), unlocking use for virtually any LLM that supports tool calling. Any service that exposes an OpenAI-compatible or Anthropic-compatible API also works out of the box—see [Compatible APIs](/oss/python/deepagents/code/configuration#compatible-apis).

## Quickstart

Deep Agents Code integrates automatically with the [following model providers](#provider-reference): no extra configuration needed beyond installing the relevant provider package.

1. **Install provider packages**

   Each model provider requires its corresponding LangChain integration package. These ship as optional extras to keep the application lightweight. OpenAI, Anthropic, and Gemini are included by default. Install any other extra from within a session with `/install`, or from the shell with `dcode --install`:

   <CodeGroup>
     ```txt In session theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
     /install groq
     ```

     ```bash Shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
     dcode --install groq
     ```
   </CodeGroup>

   Run `/install` with no argument to list the valid extras. To preinstall extras during the initial CLI install, set `DEEPAGENTS_CODE_EXTRAS`:

   ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
   DEEPAGENTS_CODE_EXTRAS="baseten,groq" curl -LsSf https://langch.in/dcode | bash
   ```

2. **Set credentials**

   Add an API key for your provider with the [`/auth`](/oss/python/deepagents/code/configuration#use-%2Fauth-recommended) credential manager:

   ```txt theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
   /auth
   ```

   For non-interactive runs, CI/CD, or anywhere a TUI isn't available, store the same key from the shell with [`dcode auth set`](/oss/python/deepagents/code/configuration#manage-credentials-from-the-shell-dcode-auth) or set the provider's environment variable instead. See [Provider credentials](/oss/python/deepagents/code/configuration#provider-credentials) for the full key resolution order, the [`DEEPAGENTS_CODE_` prefix](/oss/python/deepagents/code/configuration#deepagents_code_-prefix) for scoping a key to Deep Agents Code, and the [Provider reference](#provider-reference) for each provider's environment variable.

   To configure model parameters, see [Model parameters](#model-parameters).

## Provider reference

Using a provider not listed here? See [Arbitrary providers](/oss/python/deepagents/code/configuration#arbitrary-providers): any LangChain-compatible provider can be used in Deep Agents Code with additional setup.

| Provider             | Package                                                                                    | Credential env var                                   | Model profiles |
| -------------------- | ------------------------------------------------------------------------------------------ | ---------------------------------------------------- | -------------- |
| OpenAI               | [`langchain-openai`](/oss/python/integrations/chat/openai)                                 | `OPENAI_API_KEY`                                     | ✅              |
| OpenAI (Codex)       | [`langchain-openai`](/oss/python/integrations/chat/openai)                                 | None — [sign in with ChatGPT](#sign-in-with-chatgpt) | ✅              |
| Azure OpenAI         | [`langchain-openai`](/oss/python/integrations/chat/azure_chat_openai)                      | `AZURE_OPENAI_API_KEY`                               | ✅              |
| Anthropic            | [`langchain-anthropic`](/oss/python/integrations/chat/anthropic)                           | `ANTHROPIC_API_KEY`                                  | ✅              |
| Google Gemini API    | [`langchain-google-genai`](/oss/python/integrations/chat/google_generative_ai)             | `GOOGLE_API_KEY`                                     | ✅              |
| Google Vertex AI     | [`langchain-google-genai`](/oss/python/integrations/chat/google_generative_ai#credentials) | `GOOGLE_CLOUD_PROJECT`                               | ✅              |
| Baseten              | [`langchain-baseten`](https://github.com/basetenlabs/langchain-baseten)                    | `BASETEN_API_KEY`                                    | ✅              |
| AWS Bedrock          | [`langchain-aws`](/oss/python/integrations/chat/bedrock)                                   | `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`         | ✅              |
| AWS Bedrock Converse | [`langchain-aws`](/oss/python/integrations/chat/bedrock)                                   | `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`         | ✅              |
| Hugging Face         | [`langchain-huggingface`](/oss/python/integrations/chat/huggingface)                       | `HUGGINGFACEHUB_API_TOKEN`                           | ✅              |
| Ollama               | [`langchain-ollama`](/oss/python/integrations/chat/ollama)                                 | `OLLAMA_API_KEY` (cloud only; optional)              | ❌              |
| Groq                 | [`langchain-groq`](/oss/python/integrations/chat/groq)                                     | `GROQ_API_KEY`                                       | ✅              |
| Cohere               | [`langchain-cohere`](/oss/python/integrations/chat/cohere)                                 | `COHERE_API_KEY`                                     | ❌              |
| Fireworks            | [`langchain-fireworks`](/oss/python/integrations/chat/fireworks)                           | `FIREWORKS_API_KEY`                                  | ✅              |
| Together             | [`langchain-together`](/oss/python/integrations/chat/together)                             | `TOGETHER_API_KEY`                                   | ❌              |
| Mistral AI           | [`langchain-mistralai`](/oss/python/integrations/chat/mistralai)                           | `MISTRAL_API_KEY`                                    | ✅              |
| DeepSeek             | [`langchain-deepseek`](/oss/python/integrations/chat/deepseek)                             | `DEEPSEEK_API_KEY`                                   | ✅              |
| IBM (watsonx.ai)     | [`langchain-ibm`](/oss/python/integrations/chat/ibm_watsonx)                               | `WATSONX_APIKEY`                                     | ❌              |
| Nvidia               | [`langchain-nvidia-ai-endpoints`](/oss/python/integrations/chat/nvidia_ai_endpoints)       | `NVIDIA_API_KEY`                                     | ✅              |
| xAI                  | [`langchain-xai`](/oss/python/integrations/chat/xai)                                       | `XAI_API_KEY`                                        | ✅              |
| Perplexity           | [`langchain-perplexity`](/oss/python/integrations/chat/perplexity)                         | `PERPLEXITY_API_KEY` (or `PPLX_API_KEY`)             | ✅              |
| OpenRouter           | [`langchain-openrouter`](/oss/python/integrations/chat/openrouter)                         | `OPENROUTER_API_KEY`                                 | ✅              |
| LiteLLM              | [`langchain-litellm`](/oss/python/integrations/chat/litellm)                               | Per-provider (see [docs](https://docs.litellm.ai/))  | ❌              |

<Tip>
  You can scope any credential to Deep Agents Code by adding a `DEEPAGENTS_CODE_` prefix. For example, `DEEPAGENTS_CODE_OPENAI_API_KEY` takes priority over `OPENAI_API_KEY` within Deep Agents Code without affecting other tools. See [`DEEPAGENTS_CODE_` prefix](/oss/python/deepagents/code/configuration#deepagents_code_-prefix) for details.
</Tip>

<Tip>
  [Model profiles](/oss/python/langchain/models#model-profiles) provide model metadata used by the interactive `/model` switcher. If a model is missing from the switcher, pass the model name directly or add it via `config.toml`.
</Tip>

### Sign in with ChatGPT

The `openai_codex` provider lets you use OpenAI's Codex models with your paid **ChatGPT** subscription instead of an `OPENAI_API_KEY`. You sign in with your ChatGPT account, and it shows up as its own provider in both `/auth` and the `/model` switcher, separate from the API-key-based `openai` provider.

<Steps>
  <Step title="Start the sign-in">
    Run `/auth` in any session and select **`openai_codex`**. Because ChatGPT signs you in through your browser, this starts a browser sign-in instead of asking for an API key.
  </Step>

  <Step title="Authorize in your browser">
    Deep Agents Code opens your browser to the ChatGPT sign-in page. If it can't open a browser (for example, over SSH), it also shows the sign-in URL on screen so you can copy it to a browser on another device.
  </Step>

  <Step title="Select a Codex model">
    Once signed in, the Codex models appear in the `/model` switcher under the `openai_codex` provider. Switch to one directly with its spec:

    ```txt theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    /model openai_codex:gpt-5.5
    ```
  </Step>
</Steps>

Your sign-in persists across sessions. To check your status or sign out, run `/auth`, select `openai_codex`, and choose to re-authenticate or sign out.

<Note>
  `openai_codex` is separate from `openai`. To use OpenAI models with a standard API key instead, use the regular `openai` provider (e.g. `/model openai:gpt-5.5`).
</Note>

### Model routers and proxies

Model routers like [OpenRouter](https://openrouter.ai/) and [LiteLLM](https://docs.litellm.ai/) provide access to models from multiple providers through a single endpoint.

Use the dedicated integration packages for these services:

| Router     | Package                                                            | Config                                                                         |
| ---------- | ------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| OpenRouter | [`langchain-openrouter`](/oss/python/integrations/chat/openrouter) | `openrouter:<model>` (built-in, see [Provider reference](#provider-reference)) |
| LiteLLM    | [`langchain-litellm`](/oss/python/integrations/chat/litellm)       | `litellm:<model>` (built-in, see [Provider reference](#provider-reference))    |

**OpenRouter** is a built-in provider—install the extra and use it directly:

<CodeGroup>
  ```txt In session theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  /install openrouter
  ```

  ```bash Shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  dcode --install openrouter
  ```
</CodeGroup>

**LiteLLM** is also a built-in provider:

<CodeGroup>
  ```txt In session theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  /install litellm
  ```

  ```bash Shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  dcode --install litellm
  ```
</CodeGroup>

## Switch models

To switch models in Deep Agents Code, either:

1. **Use the interactive model switcher** with the `/model` command.

   <Note>
     Not all models appear here. If yours is missing, pass the model name directly (e.g. `/model gpt-5.5`) or add it to `config.toml`.
   </Note>
2. **Specify a model name directly** as an argument, e.g. `/model gpt-5.5`. You can use any model supported by the chosen provider, regardless of whether it appears in the list from option 1. The model name will be passed to the API request.
3. **Specify the model at launch** via `--model`, e.g.

   ```txt theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
   dcode --model openai:gpt-5.5
   ```

<Accordion title="Model resolution order" icon="list-numbers">
  When Deep Agents Code launches, it resolves which model to use in the following order:

  1. **`--model` flag** always wins when provided.
  2. **`[models].default`** in `~/.deepagents/config.toml`—the user's intentional long-term preference.
  3. **`[models].recent`** in `~/.deepagents/config.toml`—the last model switched to via `/model`. Written automatically; never overwrites `[models].default`.
  4. **Environment auto-detection**: falls back to the first available startup credential, checked in order: `OPENAI_API_KEY`, `ANTHROPIC_API_KEY`, `GOOGLE_API_KEY`, `GOOGLE_CLOUD_PROJECT` (Vertex AI).

  This startup fallback intentionally checks only those four credentials. Other supported providers (for example, Groq) are still available via `--model`, `/model`, and saved defaults (`[models].default` / `[models].recent`).
</Accordion>

### Which models appear in the switcher

The `/model` selector dynamically builds its list from installed provider packages. Expand below for the full criteria and troubleshooting.

<Accordion title="How the switcher builds its model list" icon="list-search">
  The interactive `/model` selector builds its list from installed provider packages and models configured in `config.toml`.

  A model appears when:

  1. The provider package is installed.
  2. The model is available from the provider package, a local provider, or your `config.toml`.
  3. The model profile does not mark text input or output as unsupported.

  If a model is missing, use `/model <provider>:<model>` directly or add it to [`[models.providers.<name>].models`](/oss/python/deepagents/code/configuration#adding-models-to-the-interactive-switcher).

  <Tip>
    Credential status does **not** affect whether a model is listed. You can still select a model with missing credentials. The provider reports an authentication error at request time.
  </Tip>
</Accordion>

### Open weights models

If you want to use an open weights model, there are two common paths depending on whether you prefer local or cloud-hosted inference.

**Local inference with Ollama** is the easiest way to get started for free, with no API key required:

1. [Install Ollama](https://ollama.com/) and pull a model, for example:

   ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
   ollama pull qwen3:4b
   ```

2. Install the Ollama extra:

   <CodeGroup>
     ```txt In session theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
     /install ollama
     ```

     ```bash Shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
     dcode --install ollama
     ```
   </CodeGroup>

3. Select the model:

   <CodeGroup>
     ```txt In session theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
     /model
     ```

     ```bash Shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
     dcode --model ollama:qwen3:4b
     ```
   </CodeGroup>

   Use the interactive switcher, or pass the model directly with `/model ollama:qwen3:4b`.

**Cloud-hosted open weights via Groq** gives you fast inference without running anything locally:

1. Get a free API key at [console.groq.com](https://console.groq.com/).

2. Install the Groq extra:

   <CodeGroup>
     ```txt In session theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
     /install groq
     ```

     ```bash Shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
     dcode --install groq
     ```
   </CodeGroup>

3. Select a model:

   <CodeGroup>
     ```txt In session theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
     /model
     ```

     ```bash Shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
     GROQ_API_KEY="your-api-key" dcode --model groq:openai/gpt-oss-120b
     ```
   </CodeGroup>

   Use the interactive switcher, or pass the model directly with `/model groq:openai/gpt-oss-120b`.

**Fireworks** is another popular cloud provider for open weights models:

<CodeGroup>
  ```txt In session theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  /install fireworks
  /model
  ```

  ```bash Shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  dcode --install fireworks
  FIREWORKS_API_KEY="your-api-key" dcode --model fireworks:accounts/fireworks/models/deepseek-v4-pro
  ```
</CodeGroup>

Use the interactive switcher, or pass the model directly with `/model fireworks:accounts/fireworks/models/deepseek-v4-pro`.

**Baseten** is another cloud provider for open weights models:

<CodeGroup>
  ```txt In session theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  /install baseten
  /model
  ```

  ```bash Shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  dcode --install baseten
  BASETEN_API_KEY="your-api-key" dcode --model baseten:moonshotai/Kimi-K2.6
  ```
</CodeGroup>

Use the interactive switcher, or pass the model directly with `/model baseten:moonshotai/Kimi-K2.6`.

<Tip>
  If you want a provider preinstalled at the same time as the CLI itself, use `DEEPAGENTS_CODE_EXTRAS` during the initial install:

  ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  DEEPAGENTS_CODE_EXTRAS="fireworks" curl -LsSf https://langch.in/dcode | bash
  ```

  You can combine multiple providers: `DEEPAGENTS_CODE_EXTRAS="groq,fireworks,ollama"`. If Deep Agents Code is already installed, use `/install <extra>` in a session or `dcode --install <extra>` from the shell instead.
</Tip>

**Together**, **OpenRouter**, and **Hugging Face** (`langchain-huggingface`) are other options for cloud-hosted open weights. See the [Provider reference](#provider-reference) for credentials and package names.

### Set a default model

You can set a persistent default model that applies to all future CLI launches:

* **Via model selector:** Open `/model`, navigate to the desired model, and press `Ctrl+S` to pin it as the default. Pressing `Ctrl+S` again on the current default clears it.
* **Via command:** `/model --default provider:model` (e.g., `/model --default anthropic:claude-opus-4-8`)
* **Via config file:** Set `[models].default` in `~/.deepagents/config.toml` (see [Configuration](/oss/python/deepagents/code/configuration)).
* **From the shell:**

  ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  dcode --default-model anthropic:claude-opus-4-8
  ```

To view the current default:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
dcode --default-model
```

To clear the default:

* **From the shell:**

  ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  dcode --clear-default-model
  ```

* **Via command:** `/model --default --clear`

* **Via model selector:** Press `Ctrl+S` on the currently pinned default model.

Without a default, Deep Agents Code uses the most recently used model.

### Model parameters

Pass extra constructor kwargs to the model—sampling controls, reasoning/thinking budgets, context window sizes, request timeouts, and anything else the underlying chat-model class accepts. Three places to set them, in priority order (highest first):

1. **One-off at launch with `--model-params`.** JSON string, session-only:

   ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
   # OpenAI reasoning effort
   dcode --model openai:gpt-5.5 --model-params '{"reasoning": {"effort": "high"}}'

   # Anthropic extended thinking
   dcode --model anthropic:claude-opus-4-8 --model-params '{"thinking": {"type": "enabled", "budget_tokens": 10000}, "max_tokens": 16000}'
   ```

2. **Mid-session via `/model --model-params`.** Same JSON syntax—swaps params (and optionally the model) without restarting:

   ```txt theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
   /model --model-params '{"temperature": 0.7}' anthropic:claude-opus-4-8
   /model --model-params '{"num_ctx": 16384}'           # opens selector, applies params to choice
   ```

3. **Persistent in `config.toml`.** Provider-level defaults (with optional per-model sub-tables) that apply on every launch:

   ```toml theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
   [models.providers.anthropic.params]
   thinking = { type = "enabled", budget_tokens = 10000 }
   max_tokens = 16000

   [models.providers.openai.params]
   reasoning = { effort = "high", summary = "auto" }
   output_version = "responses/v1"

   [models.providers.ollama.params]
   num_ctx = 16384
   temperature = 0

   # Per-model override—wins over provider-level keys
   [models.providers.ollama.params."qwen3:4b"]
   temperature = 0.5
   ```

CLI flags override config-file `params` and are session-only (mid-session changes are not persisted). Per-model sub-tables in `config.toml` override provider-level keys (shallow merge—see [Model constructor params](/oss/python/deepagents/code/configuration#model-constructor-params) for full semantics). `--model-params` cannot be combined with `--default`.

For retry counts, prefer `--max-retries` or the top-level [`[retries]` config](/oss/python/deepagents/code/configuration#retries).

<Tip>
  Any kwarg accepted by the underlying chat-model constructor is valid. Refer to the provider's reference docs for the full list—e.g. [`ChatAnthropic`](https://reference.langchain.com/python/langchain-anthropic/langchain_anthropic/chat_models/ChatAnthropic), [`ChatOpenAI`](https://reference.langchain.com/python/langchain-openai/langchain_openai/chat_models/base/ChatOpenAI), [`ChatOllama`](https://reference.langchain.com/python/langchain-ollama/langchain_ollama/chat_models/ChatOllama). Unknown kwargs are forwarded to the upstream API request, so newly released parameters work without a CLI update.
</Tip>

<Note>
  Don't put credentials (`api_key`) in `params`—use [`api_key_env`](/oss/python/deepagents/code/configuration#provider-configuration) to point at an environment variable instead.
</Note>

To override fields on the model's runtime *profile* (`max_input_tokens`, `tool_calling`, capability flags)—distinct from constructor params—see [Profile overrides](/oss/python/deepagents/code/configuration#profile-overrides-advanced).

## Advanced configuration

For detailed configuration of provider params, profile overrides, custom base URLs, compatible APIs, arbitrary providers, and lifecycle hooks, see [Configuration](/oss/python/deepagents/code/configuration).

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/deepagents/code/providers.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Use remote sandboxes
Source: https://docs.langchain.com/oss/python/deepagents/code/remote-sandboxes

Run Deep Agents Code tool execution in LangSmith, Daytona, Modal, Runloop, Vercel, or AgentCore sandboxes. Install provider extras, set credentials, and use flags and setup scripts.

Deep Agents Code uses the [sandbox as tool](/oss/python/deepagents/sandboxes#sandbox-as-tool-pattern) pattern: the `dcode` process (LLM loop, memory, tool dispatch) runs on your machine, but agent tool calls (`read_file`, `write_file`, `execute`, etc.) target the remote sandbox, not your local filesystem. To get files into the sandbox, use a [setup script](#setup-scripts) or the provider's file transfer APIs (see [Working with files](/oss/python/deepagents/sandboxes#working-with-files)).

For a deeper look at sandbox architecture, integration patterns, and security best practices, see [Sandboxes](/oss/python/deepagents/sandboxes).

<Steps>
  <Step title="Install provider dependency" icon="download">
    Each provider ships as an optional extra. Install one from within a session with `/install`, or from the shell with `dcode --install`:

    <Tabs>
      <Tab title="LangSmith">
        Included by default when installing `deepagents-code`. No extra installation needed.
      </Tab>

      <Tab title="Daytona">
        <CodeGroup>
          ```txt In session theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
          /install daytona
          ```

          ```bash Shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
          dcode --install daytona
          ```
        </CodeGroup>
      </Tab>

      <Tab title="Modal">
        <CodeGroup>
          ```txt In session theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
          /install modal
          ```

          ```bash Shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
          dcode --install modal
          ```
        </CodeGroup>
      </Tab>

      <Tab title="Runloop">
        <CodeGroup>
          ```txt In session theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
          /install runloop
          ```

          ```bash Shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
          dcode --install runloop
          ```
        </CodeGroup>
      </Tab>

      <Tab title="Vercel">
        <CodeGroup>
          ```txt In session theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
          /install vercel
          ```

          ```bash Shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
          dcode --install vercel
          ```
        </CodeGroup>
      </Tab>

      <Tab title="AgentCore">
        <CodeGroup>
          ```txt In session theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
          /install agentcore
          ```

          ```bash Shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
          dcode --install agentcore
          ```
        </CodeGroup>
      </Tab>
    </Tabs>

    To install support for every sandbox provider at once, use the `all-sandboxes` extra: `/install all-sandboxes` in a session, or `dcode --install all-sandboxes` from the shell.
  </Step>

  <Step title="Set provider credentials" icon="key">
    <Tabs>
      <Tab title="LangSmith">
        ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
        export LANGSMITH_API_KEY="your-key"
        ```
      </Tab>

      <Tab title="Daytona">
        ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
        export DAYTONA_API_KEY="your-key"
        ```
      </Tab>

      <Tab title="Modal">
        ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
        modal setup
        ```
      </Tab>

      <Tab title="Runloop">
        ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
        export RUNLOOP_API_KEY="your-key"
        ```
      </Tab>

      <Tab title="Vercel">
        ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
        export VERCEL_TOKEN="your-token"
        export VERCEL_PROJECT_ID="your-project-id"
        export VERCEL_TEAM_ID="your-team-id"
        ```

        When running on Vercel, [OIDC](https://vercel.com/docs/oidc) credentials are used automatically instead.
      </Tab>

      <Tab title="AgentCore">
        ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
        export AWS_ACCESS_KEY_ID="your-key"
        export AWS_SECRET_ACCESS_KEY="your-secret"
        export AWS_REGION="us-west-2"

        # Only when using temporary/STS credentials:
        export AWS_SESSION_TOKEN="session-token"
        ```
      </Tab>
    </Tabs>
  </Step>

  <Step title="Run Deep Agents Code with a sandbox" icon="player-play">
    <Tabs>
      <Tab title="LangSmith">
        ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
        dcode --sandbox langsmith
        ```
      </Tab>

      <Tab title="Daytona">
        ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
        dcode --sandbox daytona
        ```
      </Tab>

      <Tab title="Modal">
        ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
        dcode --sandbox modal
        ```
      </Tab>

      <Tab title="Runloop">
        ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
        dcode --sandbox runloop
        ```
      </Tab>

      <Tab title="Vercel">
        ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
        dcode --sandbox vercel
        ```
      </Tab>

      <Tab title="AgentCore">
        ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
        dcode --sandbox agentcore
        ```
      </Tab>
    </Tabs>
  </Step>
</Steps>

## Sandbox flags and examples

| Flag                           | Description                                                                                                                                                                                                                                                                                                                |
| ------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `--sandbox TYPE`               | Sandbox provider to use. Built-ins: `langsmith`, `agentcore`, `modal`, `daytona`, `runloop`, `vercel` (default: `none`). [Third-party](#third-party-providers) and [config-declared](#config-declared-providers) providers are also accepted. Pass `--sandbox` with no value to use `[sandboxes].default` from your config |
| `--sandbox-id ID`              | Reuse an existing sandbox by ID instead of creating a new one. Skips creation and cleanup. Only for providers that support reattaching by ID. Refer to your sandbox documentation for more                                                                                                                                 |
| `--sandbox-snapshot-name NAME` | Use or create a sandbox snapshot. Supported by `langsmith` and `runloop` (and any third-party provider that advertises snapshot support). Cannot be combined with `--sandbox-id`                                                                                                                                           |
| `--sandbox-setup PATH`         | Path to a setup script to run inside the sandbox upon creation                                                                                                                                                                                                                                                             |

Each provider exposes a default working directory inside the sandbox. Setup scripts and `execute` commands run from this directory unless overridden:

| Provider  | Working directory |
| --------- | ----------------- |
| LangSmith | `/root`           |
| Daytona   | `/home/daytona`   |
| Modal     | `/workspace`      |
| Runloop   | `/home/user`      |
| Vercel    | `/vercel/sandbox` |
| AgentCore | `/tmp`            |

Examples:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}

# Create a new Daytona sandbox
dcode --sandbox daytona

# Reuse an existing sandbox (skips creation and cleanup)
dcode --sandbox runloop --sandbox-id dbx_abc123

# Run a setup script after sandbox creation
dcode --sandbox modal --sandbox-setup ./setup.sh

# Use the provider set as [sandboxes].default in config
dcode --sandbox
```

<Note>
  Because `--sandbox` accepts an optional value, keep the bare form **last** on the command line. Otherwise a following argument (e.g. `dcode --sandbox agents`) is consumed as the flag's value. Pass an explicit provider name to avoid ambiguity.
</Note>

## Pluggable providers

The six built-in providers above aren't the only options. Deep Agents Code discovers sandbox providers from three sources, so you can use providers shipped by other packages or declare your own without changing Deep Agents Code:

1. **Built-in providers** — the curated set above, installed as `deepagents-code` extras.
2. **[Third-party providers](#third-party-providers)** — published by other installed packages via a Python entry point.
3. **[Config-declared providers](#config-declared-providers)** — defined in your `~/.deepagents/config.toml`.

When two sources define the same provider name, **config wins over third-party entry points, which win over built-ins**, so your config file can always override discovery.

### Third-party providers

A package can publish a sandbox provider under the `deepagents_code.sandbox_providers` [entry-point group](https://packaging.python.org/en/latest/specifications/entry-points/). Once you install such a package, its provider is available to `--sandbox` automatically—no config needed:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}

# Install the package that publishes the provider, then use it
dcode --sandbox acme
```

If you pass a `--sandbox` name that isn't installed or declared, Deep Agents Code lists the available providers and explains how to install or configure the missing one.

<Accordion title="Publishing a sandbox provider" icon="package">
  To distribute a provider so users can run `dcode --sandbox <name>` after installing your package, implement a `SandboxProvider` subclass and register it under the `deepagents_code.sandbox_providers` entry-point group.

  Override the `metadata` property so Deep Agents Code can surface your working directory and capability flags without instantiating the provider:

  ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from deepagents_code.integrations.sandbox_provider import (
      SandboxInstallHint,
      SandboxProvider,
      SandboxProviderMetadata,
  )

  class AcmeProvider(SandboxProvider):
      @property
      def metadata(self) -> SandboxProviderMetadata:
          return SandboxProviderMetadata(
              name="acme",
              working_dir="/workspace",
              install=SandboxInstallHint(kind="package", name="acme-dcode-sandbox"),
              supports_sandbox_id=True,
              supports_snapshot_name=False,
          )

      def get_or_create(self, *, sandbox_id=None, **kwargs):
          ...  # return a SandboxBackendProtocol

      def delete(self, *, sandbox_id, **kwargs):
          ...
  ```

  Implement `get_or_create` and `delete`; async callers are handled by the base class. Then register the entry point in your package's `pyproject.toml`:

  ```toml theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  [project.entry-points."deepagents_code.sandbox_providers"]
  acme = "acme_sandbox.provider:AcmeProvider"
  ```

  If you omit the `metadata` property, a generic default (`/workspace`, no snapshot support) is used.
</Accordion>

### Config-declared providers

For an in-house or local provider you don't want to package, declare it under `[sandboxes.providers]` in `~/.deepagents/config.toml`. This parallels [arbitrary model providers](/oss/python/deepagents/code/configuration#arbitrary-providers) and uses the same `class_path` trust model.

```toml theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
[sandboxes]

# Used when you run `dcode --sandbox` with no value.
default = "acme"

[sandboxes.providers.acme]

# Required: the provider class to import, in module.path:ClassName format.
class_path = "acme_sandbox.provider:AcmeProvider"

# Default working directory inside the sandbox.
working_dir = "/workspace"

# Package suggested when the provider's dependencies are missing.
package = "acme-dcode-sandbox"

# Capability flags (defaults: supports_sandbox_id = true, supports_snapshot_name = false).
supports_sandbox_id = true
supports_snapshot_name = false

# Extra keyword arguments forwarded to the provider's get_or_create().
[sandboxes.providers.acme.params]
region = "us-east-1"
```

<ResponseField name="class_path" type="string">
  Fully-qualified provider class in `module.path:ClassName` format. Deep Agents Code imports and instantiates this class for the provider.
</ResponseField>

<ResponseField name="working_dir" type="string">
  Default working directory inside the sandbox. Defaults to `/workspace`.
</ResponseField>

<ResponseField name="package" type="string">
  Package name suggested in error messages when the provider's dependencies are missing.
</ResponseField>

<ResponseField name="supports_sandbox_id" type="boolean">
  Whether `--sandbox-id` reattach is allowed for this provider. Defaults to `true`.
</ResponseField>

<ResponseField name="supports_snapshot_name" type="boolean">
  Whether `--sandbox-snapshot-name` is allowed for this provider. Defaults to `false`.
</ResponseField>

<ResponseField name="params" type="object">
  Extra keyword arguments forwarded to the provider's `get_or_create()`.
</ResponseField>

A config entry that reuses a built-in provider's name **overrides** that built-in while keeping its dependency pre-flight check. Malformed entries are skipped with a warning rather than crashing startup.

<Warning>
  Setting `class_path` causes Deep Agents Code to import and run arbitrary Python from the named module—module-level code executes on import. This is the same trust model as the model [`class_path`](/oss/python/deepagents/code/configuration#arbitrary-providers): you control your own machine and your own config file.
</Warning>

## Setup scripts

Use `--sandbox-setup` to run a shell script inside the sandbox after creation. This is useful for cloning repos, installing dependencies, and configuring environment variables.

```bash title="setup.sh" theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
#!/bin/bash
set -e

# Clone repository using GitHub token
git clone https://x-access-token:${GITHUB_TOKEN}@github.com/username/repo.git $HOME/workspace
cd $HOME/workspace

# Make environment variables persistent
cat >> ~/.bashrc <<'EOF'
export GITHUB_TOKEN="${GITHUB_TOKEN}"
export OPENAI_API_KEY="${OPENAI_API_KEY}"
cd $HOME/workspace
EOF
source ~/.bashrc
```

Deep Agents Code expands `${VAR}` references in setup scripts using your local environment variables. Store secrets in a local `.env` file for the setup script to access.

<Warning>
  Sandboxes isolate code execution, but agents remain vulnerable to prompt injection with untrusted inputs. Use human-in-the-loop approval, short-lived secrets, and trusted setup scripts only. See [Security considerations](/oss/python/deepagents/sandboxes#security-considerations) for details.
</Warning>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/deepagents/code/remote-sandboxes.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Use subagents in Deep Agents Code
Source: https://docs.langchain.com/oss/python/deepagents/code/subagents

Define custom Deep Agents Code subagents as AGENTS.md files with YAML frontmatter. Covers project and user paths, optional model overrides, and examples.

Define custom synchronous [subagents](/oss/python/deepagents/subagents) as markdown files so Deep Agents Code can delegate specialized tasks to them.

<Note>
  Async subagents are not available in Deep Agents Code at this time.
</Note>

Each subagent lives in its own folder with an `AGENTS.md` file:

```text theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
.deepagents/agents/{subagent-name}/AGENTS.md   # Project-level
~/.deepagents/{agent}/agents/{subagent-name}/AGENTS.md  # User-level
```

Project subagents override user subagents with the same name (see [precedence rules](/oss/python/deepagents/code/data-locations#subagents)).

The frontmatter requires `name` and `description` (same as the [`SubAgent` dictionary spec](/oss/python/deepagents/subagents#subagent-dictionary-based)). The markdown body becomes the subagent's `system_prompt`. In addition to the base spec, `AGENTS.md` files support an optional `model` frontmatter field that overrides the main agent's model for this subagent. Uses the `provider:model-name` format (e.g., `anthropic:claude-opus-4-8`, `openai:gpt-5.5`). Omit to inherit the main agent's model.

<Note>
  Other `SubAgent` fields (`tools`, `middleware`, `interrupt_on`, `skills`) are currently not configurable via `AGENTS.md` frontmatter—custom subagents defined this way inherit the main agent's tools. Use the SDK directly for full control.
</Note>

## File format

Subagent `AGENTS.md` files use YAML frontmatter followed by a markdown body:

```markdown theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
---
name: researcher
description: Research topics on the web before writing content
model: anthropic:claude-haiku-4-5-20251001
---

You are a research assistant with access to web search.

## Your Process
1. Search for relevant information
2. Summarize findings clearly
```

## Example: cost-efficient subagents

Use a cheaper, faster model for simple delegation tasks while keeping the main agent on a more capable model:

```markdown theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
---
name: general-purpose
description: General-purpose agent for research and multi-step tasks
model: anthropic:claude-haiku-4-5-20251001
---

You are a general-purpose assistant. Complete the task efficiently and return a concise summary.
```

This overrides the built-in general-purpose subagent, routing all delegated tasks to a cheaper model. See [Override the general-purpose subagent](/oss/python/deepagents/subagents#override-the-general-purpose-subagent) for more.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/deepagents/code/subagents.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
