# List of standard content blocks
human_message = HumanMessage(content_blocks=[
    {"type": "text", "text": "Hello, how are you?"},
    {"type": "image", "url": "https://example.com/image.jpg"},
])
```

<Tip>
  Specifying `content_blocks` when initializing a message will still populate message
  `content`, but provides a type-safe interface for doing so.
</Tip>

### Standard content blocks

LangChain provides a standard representation for message content that works across providers.

Message objects implement a `content_blocks` property that will lazily parse the `content` attribute into a standard, type-safe representation. For example, messages generated from [`ChatAnthropic`](/oss/python/integrations/chat/anthropic) or [`ChatOpenAI`](/oss/python/integrations/chat/openai) will include `thinking` or `reasoning` blocks in the format of the respective provider, but can be lazily parsed into a consistent [`ReasoningContentBlock`](#content-block-reference) representation:

<Tabs>
  <Tab title="Anthropic">
    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    from langchain.messages import AIMessage

    message = AIMessage(
        content=[
            {"type": "thinking", "thinking": "...", "signature": "WaUjzkyp..."},
            {"type": "text", "text": "..."},
        ],
        response_metadata={"model_provider": "anthropic"}
    )
    message.content_blocks
    ```

    ```
    [{'type': 'reasoning',
      'reasoning': '...',
      'extras': {'signature': 'WaUjzkyp...'}},
     {'type': 'text', 'text': '...'}]
    ```
  </Tab>

  <Tab title="OpenAI">
    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    from langchain.messages import AIMessage

    message = AIMessage(
        content=[
            {
                "type": "reasoning",
                "id": "rs_abc123",
                "summary": [
                    {"type": "summary_text", "text": "summary 1"},
                    {"type": "summary_text", "text": "summary 2"},
                ],
            },
            {"type": "text", "text": "...", "id": "msg_abc123"},
        ],
        response_metadata={"model_provider": "openai"}
    )
    message.content_blocks
    ```

    ```
    [{'type': 'reasoning', 'id': 'rs_abc123', 'reasoning': 'summary 1'},
     {'type': 'reasoning', 'id': 'rs_abc123', 'reasoning': 'summary 2'},
     {'type': 'text', 'text': '...', 'id': 'msg_abc123'}]
    ```
  </Tab>
</Tabs>

See the [integrations guides](/oss/python/integrations/providers/overview) to get started with the
inference provider of your choice.

<Note>
  **Serializing standard content**

  If an application outside of LangChain needs access to the standard content block
  representation, you can opt-in to storing content blocks in message content.

  To do this, you can set the `LC_OUTPUT_VERSION` environment variable to `v1`. Or,
  initialize any chat model with `output_version="v1"`:

  ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langchain.chat_models import init_chat_model

  model = init_chat_model("gpt-5-nano", output_version="v1")
  ```
</Note>

### Multimodal

**Multimodality** refers to the ability to work with data that comes in different
forms, such as text, audio, images, and video. LangChain includes standard types
for these data that can be used across providers.

[Chat models](/oss/python/langchain/models) can accept multimodal data as input and generate
it as output. Below we show short examples of input messages featuring multimodal data.

<Note>
  Extra keys can be included top-level in the content block or nested in `"extras": {"key": value}`.

  [OpenAI](/oss/python/integrations/chat/openai),
  for example, requires a filename for PDFs. See the [provider page](/oss/python/integrations/providers/overview)
  for your chosen model for specifics.
</Note>

<CodeGroup>
  ```python Image input theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  # From URL
  message = {
      "role": "user",
      "content": [
          {"type": "text", "text": "Describe the content of this image."},
          {"type": "image", "url": "https://example.com/path/to/image.jpg"},
      ]
  }

  # From base64 data
  message = {
      "role": "user",
      "content": [
          {"type": "text", "text": "Describe the content of this image."},
          {
              "type": "image",
              "base64": "AAAAIGZ0eXBtcDQyAAAAAGlzb21tcDQyAAACAGlzb2...",
              "mime_type": "image/jpeg",
          },
      ]
  }

  # From provider-managed File ID
  message = {
      "role": "user",
      "content": [
          {"type": "text", "text": "Describe the content of this image."},
          {"type": "image", "file_id": "file-abc123"},
      ]
  }
  ```

  ```python PDF document input theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  # From URL
  message = {
      "role": "user",
      "content": [
          {"type": "text", "text": "Describe the content of this document."},
          {"type": "file", "url": "https://example.com/path/to/document.pdf"},
      ]
  }

  # From base64 data
  message = {
      "role": "user",
      "content": [
          {"type": "text", "text": "Describe the content of this document."},
          {
              "type": "file",
              "base64": "AAAAIGZ0eXBtcDQyAAAAAGlzb21tcDQyAAACAGlzb2...",
              "mime_type": "application/pdf",
          },
      ]
  }

  # From provider-managed File ID
  message = {
      "role": "user",
      "content": [
          {"type": "text", "text": "Describe the content of this document."},
          {"type": "file", "file_id": "file-abc123"},
      ]
  }
  ```

  ```python Audio input theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  # From base64 data
  message = {
      "role": "user",
      "content": [
          {"type": "text", "text": "Describe the content of this audio."},
          {
              "type": "audio",
              "base64": "AAAAIGZ0eXBtcDQyAAAAAGlzb21tcDQyAAACAGlzb2...",
              "mime_type": "audio/wav",
          },
      ]
  }

  # From provider-managed File ID
  message = {
      "role": "user",
      "content": [
          {"type": "text", "text": "Describe the content of this audio."},
          {"type": "audio", "file_id": "file-abc123"},
      ]
  }
  ```

  ```python Video input theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  # From base64 data
  message = {
      "role": "user",
      "content": [
          {"type": "text", "text": "Describe the content of this video."},
          {
              "type": "video",
              "base64": "AAAAIGZ0eXBtcDQyAAAAAGlzb21tcDQyAAACAGlzb2...",
              "mime_type": "video/mp4",
          },
      ]
  }

  # From provider-managed File ID
  message = {
      "role": "user",
      "content": [
          {"type": "text", "text": "Describe the content of this video."},
          {"type": "video", "file_id": "file-abc123"},
      ]
  }
  ```
</CodeGroup>

<Warning>
  Not all models support all file types. Check the model provider's [reference](https://reference.langchain.com/python/integrations/) for supported formats and size limits.
</Warning>

### Content block reference

Content blocks are represented (either when creating a message or accessing the `content_blocks` property) as a list of typed dictionaries. Each item in the list must adhere to one of the following block types:

<AccordionGroup>
  <Accordion title="Core" icon="cube">
    <AccordionGroup>
      <Accordion title="TextContentBlock" icon="typography">
        **Purpose:** Standard text output

        <ParamField type="string">
          Always `"text"`
        </ParamField>

        <ParamField type="string">
          The text content
        </ParamField>

        <ParamField type="object[]">
          List of annotations for the text
        </ParamField>

        <ParamField type="object">
          Additional provider-specific data
        </ParamField>

        **Example:**

        ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
        {
            "type": "text",
            "text": "Hello world",
            "annotations": []
        }
        ```
      </Accordion>

      <Accordion title="ReasoningContentBlock" icon="brain">
        **Purpose:** Model reasoning steps

        <ParamField type="string">
          Always `"reasoning"`
        </ParamField>

        <ParamField type="string">
          The reasoning content
        </ParamField>

        <ParamField type="object">
          Additional provider-specific data
        </ParamField>

        **Example:**

        ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
        {
            "type": "reasoning",
            "reasoning": "The user is asking about...",
            "extras": {"signature": "abc123"},
        }
        ```
      </Accordion>
    </AccordionGroup>
  </Accordion>

  <Accordion title="Multimodal" icon="photo">
    <AccordionGroup>
      <Accordion title="ImageContentBlock" icon="photo">
        **Purpose:** Image data

        <ParamField type="string">
          Always `"image"`
        </ParamField>

        <ParamField type="string">
          URL pointing to the image location.
        </ParamField>

        <ParamField type="string">
          Base64-encoded image data.
        </ParamField>

        <ParamField type="string">
          Unique identifier for this content block (either generated by the provider or by LangChain).
        </ParamField>

        <ParamField type="string">
          Image [MIME type](https://www.iana.org/assignments/media-types/media-types.xhtml#image) (e.g., `image/jpeg`, `image/png`). Required for base64 data.
        </ParamField>
      </Accordion>

      <Accordion title="AudioContentBlock" icon="volume">
        **Purpose:** Audio data

        <ParamField type="string">
          Always `"audio"`
        </ParamField>

        <ParamField type="string">
          URL pointing to the audio location.
        </ParamField>

        <ParamField type="string">
          Base64-encoded audio data.
        </ParamField>

        <ParamField type="string">
          Unique identifier for this content block (either generated by the provider or by LangChain).
        </ParamField>

        <ParamField type="string">
          Audio [MIME type](https://www.iana.org/assignments/media-types/media-types.xhtml#audio) (e.g., `audio/mpeg`, `audio/wav`). Required for base64 data.
        </ParamField>
      </Accordion>

      <Accordion title="VideoContentBlock" icon="video">
        **Purpose:** Video data

        <ParamField type="string">
          Always `"video"`
        </ParamField>

        <ParamField type="string">
          URL pointing to the video location.
        </ParamField>

        <ParamField type="string">
          Base64-encoded video data.
        </ParamField>

        <ParamField type="string">
          Unique identifier for this content block (either generated by the provider or by LangChain).
        </ParamField>

        <ParamField type="string">
          Video [MIME type](https://www.iana.org/assignments/media-types/media-types.xhtml#video) (e.g., `video/mp4`, `video/webm`). Required for base64 data.
        </ParamField>
      </Accordion>

      <Accordion title="FileContentBlock" icon="file">
        **Purpose:** Generic files (PDF, etc)

        <ParamField type="string">
          Always `"file"`
        </ParamField>

        <ParamField type="string">
          URL pointing to the file location.
        </ParamField>

        <ParamField type="string">
          Base64-encoded file data.
        </ParamField>

        <ParamField type="string">
          Unique identifier for this content block (either generated by the provider or by LangChain).
        </ParamField>

        <ParamField type="string">
          File [MIME type](https://www.iana.org/assignments/media-types/media-types.xhtml) (e.g., `application/pdf`). Required for base64 data.
        </ParamField>
      </Accordion>

      <Accordion title="PlainTextContentBlock" icon="align-left">
        **Purpose:** Document text (`.txt`, `.md`)

        <ParamField type="string">
          Always `"text-plain"`
        </ParamField>

        <ParamField type="string">
          The text content
        </ParamField>

        <ParamField type="string">
          [MIME type](https://www.iana.org/assignments/media-types/media-types.xhtml) of the text (e.g., `text/plain`, `text/markdown`)
        </ParamField>
      </Accordion>
    </AccordionGroup>
  </Accordion>

  <Accordion title="Tool Calling" icon="tool">
    <AccordionGroup>
      <Accordion title="ToolCall" icon="function">
        **Purpose:** Function calls

        <ParamField type="string">
          Always `"tool_call"`
        </ParamField>

        <ParamField type="string">
          Name of the tool to call
        </ParamField>

        <ParamField type="object">
          Arguments to pass to the tool
        </ParamField>

        <ParamField type="string">
          Unique identifier for this tool call
        </ParamField>

        **Example:**

        ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
        {
            "type": "tool_call",
            "name": "search",
            "args": {"query": "weather"},
            "id": "call_123"
        }
        ```
      </Accordion>

      <Accordion title="ToolCallChunk" icon="puzzle">
        **Purpose:** Streaming tool call fragments

        <ParamField type="string">
          Always `"tool_call_chunk"`
        </ParamField>

        <ParamField type="string">
          Name of the tool being called
        </ParamField>

        <ParamField type="string">
          Partial tool arguments (may be incomplete JSON)
        </ParamField>

        <ParamField type="string">
          Tool call identifier
        </ParamField>

        <ParamField type="number | string">
          Position of this chunk in the stream
        </ParamField>
      </Accordion>

      <Accordion title="InvalidToolCall" icon="alert-triangle">
        **Purpose:** Malformed calls, intended to catch JSON parsing errors.

        <ParamField type="string">
          Always `"invalid_tool_call"`
        </ParamField>

        <ParamField type="string">
          Name of the tool that failed to be called
        </ParamField>

        <ParamField type="object">
          Arguments to pass to the tool
        </ParamField>

        <ParamField type="string">
          Description of what went wrong
        </ParamField>
      </Accordion>
    </AccordionGroup>
  </Accordion>

  <Accordion title="Server-Side Tool Execution" icon="server">
    <AccordionGroup>
      <Accordion title="ServerToolCall" icon="tool">
        **Purpose:** Tool call that is executed server-side.

        <ParamField type="string">
          Always `"server_tool_call"`
        </ParamField>

        <ParamField type="string">
          An identifier associated with the tool call.
        </ParamField>

        <ParamField type="string">
          The name of the tool to be called.
        </ParamField>

        <ParamField type="string">
          Partial tool arguments (may be incomplete JSON)
        </ParamField>
      </Accordion>

      <Accordion title="ServerToolCallChunk" icon="puzzle">
        **Purpose:** Streaming server-side tool call fragments

        <ParamField type="string">
          Always `"server_tool_call_chunk"`
        </ParamField>

        <ParamField type="string">
          An identifier associated with the tool call.
        </ParamField>

        <ParamField type="string">
          Name of the tool being called
        </ParamField>

        <ParamField type="string">
          Partial tool arguments (may be incomplete JSON)
        </ParamField>

        <ParamField type="number | string">
          Position of this chunk in the stream
        </ParamField>
      </Accordion>

      <Accordion title="ServerToolResult" icon="package">
        **Purpose:** Search results

        <ParamField type="string">
          Always `"server_tool_result"`
        </ParamField>

        <ParamField type="string">
          Identifier of the corresponding server tool call.
        </ParamField>

        <ParamField type="string">
          Identifier associated with the server tool result.
        </ParamField>

        <ParamField type="string">
          Execution status of the server-side tool. `"success"` or `"error"`.
        </ParamField>

        <ParamField>
          Output of the executed tool.
        </ParamField>
      </Accordion>
    </AccordionGroup>
  </Accordion>

  <Accordion title="Provider-Specific Blocks" icon="plug">
    <Accordion title="NonStandardContentBlock" icon="asterisk">
      **Purpose:** Provider-specific escape hatch

      <ParamField type="string">
        Always `"non_standard"`
      </ParamField>

      <ParamField type="object">
        Provider-specific data structure
      </ParamField>

      **Usage:** For experimental or provider-unique features
    </Accordion>

    Additional provider-specific content types may be found within the [reference documentation](/oss/python/integrations/providers/overview) of each model provider.
  </Accordion>
</AccordionGroup>

<Tip>
  View the canonical type definitions in the [API reference](https://reference.langchain.com/python/langchain/messages).
</Tip>

<Info>
  Content blocks were introduced as a new property on messages in LangChain v1 to standardize content formats across providers while maintaining backward compatibility with existing code.

  Content blocks are not a replacement for the [`content`](https://reference.langchain.com/python/langchain-core/messages/base/BaseMessage) property, but rather a new property that can be used to access the content of a message in a standardized format.
</Info>

## Use with chat models

[Chat models](/oss/python/langchain/models) accept a sequence of message objects as input and return an [`AIMessage`](https://reference.langchain.com/python/langchain-core/messages/ai/AIMessage) as output. Interactions are often stateless, so that a simple conversational loop involves invoking a model with a growing list of messages.

Refer to the below guides to learn more:

* Built-in features for [persisting and managing conversation histories](/oss/python/langchain/short-term-memory)
* Strategies for managing context windows, including [trimming and summarizing messages](/oss/python/langchain/short-term-memory#common-patterns)

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langchain/messages.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Prebuilt middleware
Source: https://docs.langchain.com/oss/python/langchain/middleware/built-in

Prebuilt middleware for common agent use cases

LangChain and [Deep Agents](/oss/python/deepagents/overview) provide prebuilt middleware for common use cases. Each middleware is production-ready and configurable for your specific needs.

## Provider-agnostic middleware

The following middleware work with any LLM provider:

| Middleware                                    | Description                                                                      |
| --------------------------------------------- | -------------------------------------------------------------------------------- |
| [Summarization](#summarization)               | Automatically summarize conversation history when approaching token limits.      |
| [Human-in-the-loop](#human-in-the-loop)       | Pause execution for human approval of tool calls.                                |
| [Model call limit](#model-call-limit)         | Limit the number of model calls to prevent excessive costs.                      |
| [Tool call limit](#tool-call-limit)           | Control tool execution by limiting call counts.                                  |
| [Model fallback](#model-fallback)             | Automatically fallback to alternative models when primary fails.                 |
| [PII detection](#pii-detection)               | Detect and handle Personally Identifiable Information (PII).                     |
| [To-do list](#to-do-list)                     | Equip agents with task planning and tracking capabilities.                       |
| [LLM tool selector](#llm-tool-selector)       | Use an LLM to select relevant tools before calling main model.                   |
| [Tool retry](#tool-retry)                     | Automatically retry failed tool calls with exponential backoff.                  |
| [Model retry](#model-retry)                   | Automatically retry failed model calls with exponential backoff.                 |
| [LLM tool emulator](#llm-tool-emulator)       | Emulate tool execution using an LLM for testing purposes.                        |
| [Context editing](#context-editing)           | Manage conversation context by trimming or clearing tool uses.                   |
| [Provider tool search](#provider-tool-search) | Defer tools behind providers' server-side tool search, surfacing them on demand. |
| [Shell tool](#shell-tool)                     | Expose a persistent shell session to agents for command execution.               |
| [File search](#file-search)                   | Provide Glob and Grep search tools over filesystem files.                        |
| [Filesystem](#filesystem-middleware)          | Provide agents with a filesystem for storing context and long-term memories.     |
| [Subagent](#subagent)                         | Add the ability to spawn subagents.                                              |

### Summarization

Automatically summarize conversation history when approaching token limits, preserving recent messages while compressing older context. Summarization is useful for the following:

* Long-running conversations that exceed context windows.
* Multi-turn dialogues with extensive history.
* Applications where preserving full conversation context matters.

<Note>
  Summarization is text-oriented context compression. It does not resize, downsample, or otherwise compress image/audio/video payloads. Recent messages retained by `keep` still include their original multimodal blocks, while older multimodal messages that are summarized are represented only by the generated text summary. For image-heavy applications, store media in a filesystem or object store and pass URLs or file references through message history.
</Note>

**API reference:** [`SummarizationMiddleware`](https://reference.langchain.com/python/langchain/agents/middleware/summarization/SummarizationMiddleware)

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain.agents import create_agent
from langchain.agents.middleware import SummarizationMiddleware

agent = create_agent(
    model="gpt-5.5",
    tools=[your_weather_tool, your_calculator_tool],
    middleware=[
        SummarizationMiddleware(
            model="gpt-5.4-mini",
            trigger=("tokens", 4000),
            keep=("messages", 20),
        ),
    ],
)
```

<Accordion title="Configuration options">
  <Tip>
    The `fraction` conditions for `trigger` and `keep` (shown below) rely on a chat model's [profile data](/oss/python/langchain/models#model-profiles) if using `langchain>=1.1`. If data are not available, use another condition or specify manually:

    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    from langchain.chat_models import init_chat_model

    custom_profile = {
        "max_input_tokens": 100_000,
        # ...
    }
    model = init_chat_model("gpt-5.5", profile=custom_profile)
    ```
  </Tip>

  <ParamField type="string | BaseChatModel">
    Model for generating summaries. Can be a model identifier string (e.g., `'openai:gpt-5.4-mini'`) or a `BaseChatModel` instance. See [`init_chat_model`](https://reference.langchain.com/python/langchain/chat_models/base/init_chat_model) for more information.
  </ParamField>

  <ParamField type="ContextSize | TriggerClause | list[ContextSize | TriggerClause] | None">
    Condition(s) for triggering summarization. Can be:

    * A single [`ContextSize`](https://reference.langchain.com/python/langchain/agents/middleware/summarization/ContextSize) tuple (the specified threshold must be met)
    * A single [`TriggerClause`](https://reference.langchain.com/python/langchain/agents/middleware/summarization/TriggerClause) dict (all specified thresholds must be met - AND logic)
    * A list mixing either form (any item must be met - OR logic)

    Supported thresholds are:

    * `fraction` (float): Fraction of model's context size (0-1)
    * `tokens` (int): Absolute token count
    * `messages` (int): Message count

    A [`ContextSize`](https://reference.langchain.com/python/langchain/agents/middleware/summarization/ContextSize) tuple expresses exactly one threshold. A [`TriggerClause`](https://reference.langchain.com/python/langchain/agents/middleware/summarization/TriggerClause) dict can include one or more thresholds, e.g. `{"tokens": 4000, "messages": 10}`, and all thresholds in the dict must be met (AND).

    Each [`TriggerClause`](https://reference.langchain.com/python/langchain/agents/middleware/summarization/TriggerClause) dict must specify at least one threshold. If `trigger` is not provided, summarization will not trigger automatically.

    See the API reference for [`ContextSize`](https://reference.langchain.com/python/langchain/agents/middleware/summarization/ContextSize) and [`TriggerClause`](https://reference.langchain.com/python/langchain/agents/middleware/summarization/TriggerClause) for more information.
  </ParamField>

  <ParamField type="ContextSize">
    How much context to preserve after summarization. Specify exactly one of:

    * `fraction` (float): Fraction of model's context size to keep (0-1)
    * `tokens` (int): Absolute token count to keep
    * `messages` (int): Number of recent messages to keep

    See the API reference for [`ContextSize`](https://reference.langchain.com/python/langchain/agents/middleware/summarization/ContextSize) for more information.
  </ParamField>

  <ParamField type="function">
    Custom token counting function. Defaults to character-based counting.
  </ParamField>

  <ParamField type="string">
    Custom prompt template for summarization. Uses built-in template if not specified. The template should include `{messages}` placeholder where conversation history will be inserted.
  </ParamField>

  <ParamField type="number">
    Maximum number of tokens to include when generating the summary. Messages will be trimmed to fit this limit before summarization.
  </ParamField>

  <ParamField type="string">
    **Deprecated:** Use `summary_prompt` to provide the full prompt instead.
  </ParamField>

  <ParamField type="number">
    **Deprecated:** Use `trigger: ("tokens", value)` instead. Token threshold for triggering summarization.
  </ParamField>

  <ParamField type="number">
    **Deprecated:** Use `keep: ("messages", value)` instead. Recent messages to preserve.
  </ParamField>
</Accordion>

<Accordion title="Full example">
  The summarization middleware monitors message token counts and automatically summarizes older messages when thresholds are reached.

  **Trigger conditions** control when summarization runs:

  * A single threshold triggers when that threshold is met
  * A trigger clause with multiple thresholds triggers only when all thresholds are met (AND logic)
  * A list of trigger conditions triggers when any item is met (OR logic)
  * Each threshold can use `fraction` (of model's context size), `tokens` (absolute count), or `messages` (message count)

  **Keep condition** control how much context to preserve (specify exactly one):

  * `fraction` - Fraction of model's context size to keep
  * `tokens` - Absolute token count to keep
  * `messages` - Number of recent messages to keep

  ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langchain.agents import create_agent
  from langchain.agents.middleware import SummarizationMiddleware

  # Single condition: trigger if tokens >= 4000
  agent = create_agent(
      model="gpt-5.5",
      tools=[your_weather_tool, your_calculator_tool],
      middleware=[
          SummarizationMiddleware(
              model="gpt-5.4-mini",
              trigger=("tokens", 4000),
              keep=("messages", 20),
          ),
      ],
  )

  # Multiple conditions: trigger if number of tokens >= 3000 OR messages >= 6
  agent2 = create_agent(
      model="gpt-5.5",
      tools=[your_weather_tool, your_calculator_tool],
      middleware=[
          SummarizationMiddleware(
              model="gpt-5.4-mini",
              trigger=[
                  ("tokens", 3000),
                  ("messages", 6),
              ],
              keep=("messages", 20),
          ),
      ],
  )

  # AND logic: trigger only when tokens >= 4000 AND messages >= 10
  agent3 = create_agent(
      model="gpt-5.5",
      tools=[your_weather_tool, your_calculator_tool],
      middleware=[
          SummarizationMiddleware(
              model="gpt-5.4-mini",
              trigger={"tokens": 4000, "messages": 10},
              keep=("messages", 20),
          ),
      ],
  )

  # Combine AND and OR: trigger if (tokens >= 5000 AND messages >= 3)
  # OR (tokens >= 3000 AND messages >= 6)
  agent4 = create_agent(
      model="gpt-5.5",
      tools=[your_weather_tool, your_calculator_tool],
      middleware=[
          SummarizationMiddleware(
              model="gpt-5.4-mini",
              trigger=[
                  {"tokens": 5000, "messages": 3},
                  {"tokens": 3000, "messages": 6},
              ],
              keep=("messages", 20),
          ),
      ],
  )

  # Using fractional limits
  agent5 = create_agent(
      model="gpt-5.5",
      tools=[your_weather_tool, your_calculator_tool],
      middleware=[
          SummarizationMiddleware(
              model="gpt-5.4-mini",
              trigger=("fraction", 0.8),
              keep=("fraction", 0.3),
          ),
      ],
  )
  ```
</Accordion>

### Human-in-the-loop

Pause agent execution for human approval, editing, or rejection of tool calls before they execute. [Human-in-the-loop](/oss/python/langchain/human-in-the-loop) is useful for the following:

* High-stakes operations requiring human approval (e.g. database writes, financial transactions).
* Compliance workflows where human oversight is mandatory.
* Long-running conversations where human feedback guides the agent.

**API reference:** [`HumanInTheLoopMiddleware`](https://reference.langchain.com/python/langchain/agents/middleware/human_in_the_loop/HumanInTheLoopMiddleware)

<Warning>
  Human-in-the-loop middleware requires a [checkpointer](/oss/python/langgraph/checkpointers#checkpoints) to maintain state across interruptions.
</Warning>

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain.agents import create_agent
from langchain.agents.middleware import HumanInTheLoopMiddleware
from langgraph.checkpoint.memory import InMemorySaver

def your_read_email_tool(email_id: str) -> str:
    """Mock function to read an email by its ID."""
    return f"Email content for ID: {email_id}"

def your_send_email_tool(recipient: str, subject: str, body: str) -> str:
    """Mock function to send an email."""
    return f"Email sent to {recipient} with subject '{subject}'"

agent = create_agent(
    model="gpt-5.5",
    tools=[your_read_email_tool, your_send_email_tool],
    checkpointer=InMemorySaver(),
    middleware=[
        HumanInTheLoopMiddleware(
            interrupt_on={
                "your_send_email_tool": {
                    "allowed_decisions": ["approve", "edit", "reject"],
                },
                "your_read_email_tool": False,
            }
        ),
    ],
)
```

<Tip>
  For complete examples, configuration options, and integration patterns, see the [Human-in-the-loop documentation](/oss/python/langchain/human-in-the-loop).
</Tip>

<Callout icon="player-play">
  Watch this [video guide](https://www.youtube.com/watch?v=SpfT6-YAVPk) demonstrating Human-in-the-loop middleware behavior.
</Callout>

### Model call limit

Limit the number of model calls to prevent infinite loops or excessive costs. Model call limit is useful for the following:

* Preventing runaway agents from making too many API calls.
* Enforcing cost controls on production deployments.
* Testing agent behavior within specific call budgets.

**API reference:** [`ModelCallLimitMiddleware`](https://reference.langchain.com/python/langchain/agents/middleware/model_call_limit/ModelCallLimitMiddleware)

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain.agents import create_agent
from langchain.agents.middleware import ModelCallLimitMiddleware
from langgraph.checkpoint.memory import InMemorySaver

agent = create_agent(
    model="gpt-5.5",
    checkpointer=InMemorySaver(),  # Required for thread limiting
    tools=[],
    middleware=[
        ModelCallLimitMiddleware(
            thread_limit=10,
            run_limit=5,
            exit_behavior="end",
        ),
    ],
)
```

<Callout icon="player-play">
  Watch this [video guide](https://www.youtube.com/watch?v=nJEER0uaNkE) demonstrating Model Call Limit middleware behavior.
</Callout>

<Accordion title="Configuration options">
  <ParamField type="number">
    Maximum model calls across all runs in a thread. Defaults to no limit.
  </ParamField>

  <ParamField type="number">
    Maximum model calls per single invocation. Defaults to no limit.
  </ParamField>

  <ParamField type="string">
    Behavior when limit is reached. Options: `'end'` (graceful termination) or `'error'` (raise exception)
  </ParamField>
</Accordion>

### Tool call limit

Control agent execution by limiting the number of tool calls, either globally across all tools or for specific tools. Tool call limits are useful for the following:

* Preventing excessive calls to expensive external APIs.
* Limiting web searches or database queries.
* Enforcing rate limits on specific tool usage.
* Protecting against runaway agent loops.

**API reference:** [`ToolCallLimitMiddleware`](https://reference.langchain.com/python/langchain/agents/middleware/tool_call_limit/ToolCallLimitMiddleware)

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain.agents import create_agent
from langchain.agents.middleware import ToolCallLimitMiddleware

agent = create_agent(
    model="gpt-5.5",
    tools=[search_tool, database_tool],
    middleware=[
        # Global limit
        ToolCallLimitMiddleware(thread_limit=20, run_limit=10),
        # Tool-specific limit
        ToolCallLimitMiddleware(
            tool_name="search",
            thread_limit=5,
            run_limit=3,
        ),
    ],
)
```

<Callout icon="player-play">
  Watch this [video guide](https://www.youtube.com/watch?v=6gYlaJJ8t0w) demonstrating Tool Call Limit middleware behavior.
</Callout>

<Accordion title="Configuration options">
  <ParamField type="string">
    Name of specific tool to limit. If not provided, limits apply to **all tools globally**.
  </ParamField>

  <ParamField type="number">
    Maximum tool calls across all runs in a thread (conversation). Persists across multiple invocations with the same thread ID. Requires a checkpointer to maintain state. `None` means no thread limit.
  </ParamField>

  <ParamField type="number">
    Maximum tool calls per single invocation (one user message → response cycle). Resets with each new user message. `None` means no run limit.

    **Note:** At least one of `thread_limit` or `run_limit` must be specified.
  </ParamField>

  <ParamField type="string">
    Behavior when limit is reached:

    * `'continue'` (default) - Block exceeded tool calls with error messages, let other tools and the model continue. The model decides when to end based on the error messages.
    * `'error'` - Raise a `ToolCallLimitExceededError` exception, stopping execution immediately
    * `'end'` - Stop execution immediately with a `ToolMessage` and AI message for the exceeded tool call. Only works when limiting a single tool; raises `NotImplementedError` if other tools have pending calls.
  </ParamField>
</Accordion>

<Accordion title="Full example">
  Specify limits with:

  * **Thread limit** - Max calls across all runs in a conversation (requires checkpointer)
  * **Run limit** - Max calls per single invocation (resets each turn)

  Exit behaviors:

  * `'continue'` (default) - Block exceeded calls with error messages, agent continues
  * `'error'` - Raise exception immediately
  * `'end'` - Stop with ToolMessage + AI message (single-tool scenarios only)

  ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langchain.agents import create_agent
  from langchain.agents.middleware import ToolCallLimitMiddleware

  global_limiter = ToolCallLimitMiddleware(thread_limit=20, run_limit=10)
  search_limiter = ToolCallLimitMiddleware(tool_name="search", thread_limit=5, run_limit=3)
  database_limiter = ToolCallLimitMiddleware(tool_name="query_database", thread_limit=10)
  strict_limiter = ToolCallLimitMiddleware(tool_name="scrape_webpage", run_limit=2, exit_behavior="error")

  agent = create_agent(
      model="gpt-5.5",
      tools=[search_tool, database_tool, scraper_tool],
      middleware=[global_limiter, search_limiter, database_limiter, strict_limiter],
  )
  ```
</Accordion>

### Model fallback

Automatically fallback to alternative models when the primary model fails. Model fallback is useful for the following:

* Building resilient agents that handle model outages.
* Cost optimization by falling back to cheaper models.
* Provider redundancy across OpenAI, Anthropic, etc.

**API reference:** [`ModelFallbackMiddleware`](https://reference.langchain.com/python/langchain/agents/middleware/model_fallback/ModelFallbackMiddleware)

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain.agents import create_agent
from langchain.agents.middleware import ModelFallbackMiddleware

agent = create_agent(
    model="gpt-5.5",
    tools=[],
    middleware=[
        ModelFallbackMiddleware(
            "gpt-5.4-mini",
            "claude-3-5-sonnet-20241022",
        ),
    ],
)
```

<Callout icon="player-play">
  Watch this [video guide](https://www.youtube.com/watch?v=8rCRO0DUeIM) demonstrating Model Fallback middleware behavior.
</Callout>

<Accordion title="Configuration options">
  <ParamField type="string | BaseChatModel">
    First fallback model to try when the primary model fails. Can be a model identifier string (e.g., `'openai:gpt-5.4-mini'`) or a `BaseChatModel` instance.
  </ParamField>

  <ParamField type="string | BaseChatModel">
    Additional fallback models to try in order if previous models fail
  </ParamField>
</Accordion>

### PII detection

Detect and handle Personally Identifiable Information (PII) in conversations using configurable strategies. PII detection is useful for the following:

* Healthcare and financial applications with compliance requirements.
* Customer service agents that need to sanitize logs.
* Any application handling sensitive user data.

<Note>
  With `apply_to_output=True`, `PIIMiddleware` also redacts streamed wire output—text deltas, tool-call args, tool outputs, and state snapshots—via a registered stream transformer. Requires `langchain>=1.3.2`. See [Register transformers on middleware](/oss/python/langchain/event-streaming#register-transformers-on-middleware).
</Note>

**API reference:** [`PIIMiddleware`](https://reference.langchain.com/python/langchain/agents/middleware/pii/PIIMiddleware)

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain.agents import create_agent
from langchain.agents.middleware import PIIMiddleware

agent = create_agent(
    model="gpt-5.5",
    tools=[],
    middleware=[
        PIIMiddleware("email", strategy="redact", apply_to_input=True),
        PIIMiddleware("credit_card", strategy="mask", apply_to_input=True),
    ],
)
```

#### Custom PII types

You can create custom PII types by providing a `detector` parameter. This allows you to detect patterns specific to your use case beyond the built-in types.

**Three ways to create custom detectors:**

1. **Regex pattern string** - Simple pattern matching

2. **Custom function** - Complex detection logic with validation

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain.agents import create_agent
from langchain.agents.middleware import PIIMiddleware
import re

# Method 1: Regex pattern string
agent1 = create_agent(
    model="gpt-5.5",
    tools=[],
    middleware=[
        PIIMiddleware(
            "api_key",
            detector=r"sk-[a-zA-Z0-9]{32}",
            strategy="block",
        ),
    ],
)

# Method 2: Compiled regex pattern
agent2 = create_agent(
    model="gpt-5.5",
    tools=[],
    middleware=[
        PIIMiddleware(
            "phone_number",
            detector=re.compile(r"\+?\d{1,3}[\s.-]?\d{3,4}[\s.-]?\d{4}"),
            strategy="mask",
        ),
    ],
)
