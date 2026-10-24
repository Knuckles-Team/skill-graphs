# Configure threads
Source: https://docs.langchain.com/langsmith/threads

Many LLM applications have a chatbot-like interface in which the user and the LLM application engage in a multi-turn conversation. In order to track these conversations, you can use [*threads*](/langsmith/observability-concepts#threads) in LangSmith.

## Group traces into threads

To associate traces together into a thread, you need to pass in a special `metadata` key where the value is the unique identifier for that thread. The key name should be one of:

* `session_id`
* `thread_id`
* `conversation_id`

The value can be any string you want, but we recommend using **UUID v7** thread IDs.

The [LangSmith SDK](/langsmith/reference) exports a `uuid7` helper (Python v0.4.43+, JS v0.3.80+):

* **Python**: `from langsmith import uuid7`
* **JS/TS**: `import { uuid7 } from 'langsmith'`

For instructions, refer to [Add metadata and tags to traces](/langsmith/add-metadata-tags).

<Warning>
  **Important:** To ensure filtering and token counting work correctly across your entire thread, you must set the thread metadata (`session_id`, `thread_id`, or `conversation_id`) on **all runs**, including child runs within a trace.

  If child runs don't have the thread\_id metadata, they won't be included when:

  * Filtering runs by thread.
  * Calculating token usage for a thread.
  * Aggregating costs across a thread.

  When creating child runs (e.g., using `@traceable` for nested functions or creating child spans), ensure you propagate the thread metadata to all child runs.
</Warning>

### Example

This example demonstrates how to log and retrieve conversation history using a structured message format to maintain long-running chats.

The example sets a `THREAD_ID` and passes it via `metadata` to the tracing wrapper, linking every run from that session into the same thread in LangSmith. Conversation history is persisted locally between turns—replace the file-based or in-memory store with a database or cache in production. The `get_chat_history` flag controls whether the pipeline continues an existing thread or starts a fresh one:

<CodeGroup>
  ```python Python expandable wrap theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import os
  import json
  from dotenv import load_dotenv

  # Load environment variables from .env file
  load_dotenv()

  import openai
  from langsmith import traceable, Client, uuid7
  from langsmith.wrappers import wrap_openai

  # Initialize clients
  langsmith_client = Client()
  client = wrap_openai(openai.Client())

  # Configuration
  THREAD_ID = str(uuid7())

  # Using a local directory to store thread history. For production use, use a persistent storage solution.
  THREADS_DIR = os.path.join(os.path.dirname(__file__), "threads")

  # gets a history of all LLM calls in the thread to construct conversation history
  def get_thread_history(thread_id: str) -> list:
      path = os.path.join(THREADS_DIR, f"{thread_id}.json")
      if not os.path.exists(path):
          return []
      with open(path, "r") as f:
          return json.load(f)

  def save_thread_history(thread_id: str, messages: list):
      os.makedirs(THREADS_DIR, exist_ok=True)
      with open(os.path.join(THREADS_DIR, f"{thread_id}.json"), "w") as f:
          json.dump(messages, f, indent=2, default=str)

  @traceable(name="Chat Bot", metadata={"thread_id": THREAD_ID})
  def chat_pipeline(messages: list, get_chat_history: bool = False):
      # Whether to continue an existing thread or start a new one
      if get_chat_history:
          history_messages = get_thread_history(THREAD_ID)
          # Get existing conversation history and append new messages
          all_messages = history_messages + messages
      else:
          all_messages = messages

      # Invoke the model
      chat_completion = client.chat.completions.create(
          model="gpt-5.4-mini", messages=all_messages
      )

      response_message = chat_completion.choices[0].message
      print("Response from model:", response_message)

      full_conversation = all_messages + [{"role": response_message.role, "content": response_message.content}]
      save_thread_history(THREAD_ID, full_conversation)

      return {"messages": full_conversation}

  # Format message
  messages = [
      {
          "content": "Hi, my name is Sally",
          "role": "user"
      }
  ]

  # Call the chat pipeline
  result = chat_pipeline(messages, get_chat_history=False)
  ```

  ```typescript TypeScript expandable wrap theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import * as fs from "fs";
  import * as path from "path";
  import { fileURLToPath } from "url";
  import * as dotenv from "dotenv";
  import OpenAI from "openai";
  import { traceable } from "langsmith/traceable";
  import { wrapOpenAI } from "langsmith/wrappers";
  import { uuid7 } from "langsmith";

  const __dirname = path.dirname(fileURLToPath(import.meta.url));

  // Load environment variables from .env file
  dotenv.config();

  // Initialize client
  const client = wrapOpenAI(new OpenAI());

  // Configuration
  const THREAD_ID = uuid7();

  // Using a local directory to store thread history. For production use, use a persistent storage solution.
  const THREADS_DIR = path.join(__dirname, "threads");

  type Message = { role: string; content: string };

  // Gets a history of all LLM calls in the thread to construct conversation history
  function getThreadHistory(threadId: string): Message[] {
    const filePath = path.join(THREADS_DIR, `${threadId}.json`);
    if (!fs.existsSync(filePath)) return [];
    return JSON.parse(fs.readFileSync(filePath, "utf-8"));
  }

  function saveThreadHistory(threadId: string, messages: Message[]): void {
    fs.mkdirSync(THREADS_DIR, { recursive: true });
    fs.writeFileSync(
      path.join(THREADS_DIR, `${threadId}.json`),
      JSON.stringify(messages, null, 2)
    );
  }

  const chatPipeline = traceable(
    async function chatPipeline({ messages, get_chat_history = false }: { messages: Message[]; get_chat_history?: boolean }) {
      // Whether to continue an existing thread or start a new one
      if (get_chat_history) {
        const historyMessages = getThreadHistory(THREAD_ID);
        // Get existing conversation history and append new messages
        messages = [...historyMessages, ...messages];
      }

      // Invoke the model
      const chatCompletion = await client.chat.completions.create({
        model: "gpt-5.4-mini",
        messages,
      });

      const responseMessage = chatCompletion.choices[0].message;
      console.log("Response from model:", responseMessage);

      const fullConversation: Message[] = [
        ...messages,
        { role: responseMessage.role, content: responseMessage.content ?? "" },
      ];
      saveThreadHistory(THREAD_ID, fullConversation);

      return { messages: fullConversation };
    },
    { name: "Chat Bot", metadata: { thread_id: THREAD_ID } }
  );

  // Format message
  const messages: Message[] = [{ role: "user", content: "Hi! My name is Sally" }];

  // Call the chat pipeline
  await chatPipeline({ messages, get_chat_history: false });
  ```

  ```java Java expandable wrap theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import com.langchain.smith.client.LangsmithClient;
  import com.langchain.smith.client.okhttp.LangsmithOkHttpClient;
  import com.langchain.smith.tracing.TraceConfig;
  import com.langchain.smith.tracing.Tracing;
  import com.langchain.smith.wrappers.openai.OpenAITracing;
  import com.openai.client.OpenAIClient;
  import com.openai.client.okhttp.OpenAIOkHttpClient;
  import com.openai.models.ChatModel;
  import com.openai.models.chat.completions.ChatCompletion;
  import com.openai.models.chat.completions.ChatCompletionAssistantMessageParam;
  import com.openai.models.chat.completions.ChatCompletionCreateParams;
  import com.openai.models.chat.completions.ChatCompletionMessageParam;
  import com.openai.models.chat.completions.ChatCompletionUserMessageParam;
  import java.util.ArrayList;
  import java.util.Collections;
  import java.util.HashMap;
  import java.util.List;
  import java.util.Map;
  import java.util.concurrent.ExecutorService;
  import java.util.concurrent.Executors;
  import java.util.concurrent.TimeUnit;
  import java.util.function.Function;

  class ThreadsChatPipeline {
    private static final String THREAD_ID = "01990f3e-7f97-74c5-a9b6-8d3f7e8e2f11";

    private static final class OpenAiResources {
      private static final LangsmithClient langsmith = LangsmithOkHttpClient.fromEnv();
      private static final ExecutorService executor = Executors.newSingleThreadExecutor();
      private static final Map<String, Object> threadMetadata = new HashMap<>();

      static {
        threadMetadata.put("thread_id", THREAD_ID);
      }

      private static final OpenAIClient openai =
          OpenAITracing.wrapOpenAI(
              OpenAIOkHttpClient.fromEnv(),
              TraceConfig.builder()
                  .client(langsmith)
                  .executor(executor)
                  .metadata(threadMetadata)
                  .build());

      private static final List<ChatCompletionMessageParam> threadHistory = new ArrayList<>();

      static final Function<ChatRequest, Map<String, List<ChatCompletionMessageParam>>> CHAT_PIPELINE =
          Tracing.traceFunction(
              request -> {
                List<ChatCompletionMessageParam> allMessages = new ArrayList<>();
                if (request.getChatHistory()) {
                  allMessages.addAll(threadHistory);
                }
                allMessages.addAll(request.getMessages());

                ChatCompletion chatCompletion =
                    openai
                        .chat()
                        .completions()
                        .create(
                            ChatCompletionCreateParams.builder()
                                .model(ChatModel.GPT_5_CHAT_LATEST)
                                .messages(allMessages)
                                .build());

                String content = chatCompletion.choices().get(0).message().content().orElse("");
                List<ChatCompletionMessageParam> fullConversation = new ArrayList<>(allMessages);
                fullConversation.add(
                    ChatCompletionMessageParam.ofAssistant(
                        ChatCompletionAssistantMessageParam.builder().content(content).build()));
                threadHistory.clear();
                threadHistory.addAll(fullConversation);

                return Collections.singletonMap("messages", fullConversation);
              },
              TraceConfig.builder()
                  .name("Chat Bot")
                  .client(langsmith)
                  .executor(executor)
                  .metadata(threadMetadata)
                  .build());

      private OpenAiResources() {}

      static ExecutorService executor() {
        return executor;
      }
    }

    static Function<ChatRequest, Map<String, List<ChatCompletionMessageParam>>> chatPipeline() {
      return OpenAiResources.CHAT_PIPELINE;
    }

    public static void main(String[] args) throws InterruptedException {
      try {
        List<ChatCompletionMessageParam> messages =
            Collections.singletonList(
                ChatCompletionMessageParam.ofUser(
                    ChatCompletionUserMessageParam.builder()
                        .content("Hi, my name is Sally")
                        .build()));
        chatPipeline().apply(new ChatRequest(messages, false));
      } finally {
        OpenAiResources.executor().shutdown();
        if (!OpenAiResources.executor().awaitTermination(10, TimeUnit.SECONDS)) {
          throw new IllegalStateException("Timed out waiting for LangSmith traces to submit");
        }
      }
    }

    static class ChatRequest {
      private final List<ChatCompletionMessageParam> messages;
      private final boolean getChatHistory;

      ChatRequest(List<ChatCompletionMessageParam> messages, boolean getChatHistory) {
        this.messages = messages;
        this.getChatHistory = getChatHistory;
      }

      List<ChatCompletionMessageParam> getMessages() {
        return messages;
      }

      boolean getChatHistory() {
        return getChatHistory;
      }
    }
  }
  ```

  ```kotlin Kotlin expandable wrap theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import com.langchain.smith.client.okhttp.LangsmithOkHttpClient
  import com.langchain.smith.tracing.TraceConfig
  import com.langchain.smith.tracing.traceable
  import com.langchain.smith.wrappers.openai.wrapOpenAI
  import com.openai.client.okhttp.OpenAIOkHttpClient
  import com.openai.models.ChatModel
  import com.openai.models.chat.completions.ChatCompletionAssistantMessageParam
  import com.openai.models.chat.completions.ChatCompletionCreateParams
  import com.openai.models.chat.completions.ChatCompletionMessageParam
  import com.openai.models.chat.completions.ChatCompletionUserMessageParam
  import java.util.concurrent.Executors
  import java.util.concurrent.TimeUnit

  val threadId = "01990f3e-7f97-74c5-a9b6-8d3f7e8e2f11"
  val langsmith by lazy { LangsmithOkHttpClient.fromEnv() }
  val executor by lazy { Executors.newSingleThreadExecutor() }
  val threadMetadata by lazy { mapOf("thread_id" to threadId) }
  val openai by lazy {
      wrapOpenAI(
          OpenAIOkHttpClient.fromEnv(),
          TraceConfig.builder()
              .client(langsmith)
              .executor(executor)
              .metadata(threadMetadata)
              .build(),
      )
  }
  val threadHistory = mutableListOf<ChatCompletionMessageParam>()

  data class ChatRequest(
      val messages: List<ChatCompletionMessageParam>,
      val getChatHistory: Boolean = false,
  )

  val chatPipeline by lazy {
      traceable(
          { request: ChatRequest ->
              val allMessages =
                  if (request.getChatHistory) {
                      threadHistory + request.messages
                  } else {
                      request.messages
                  }

              val chatCompletion =
                  openai.chat().completions().create(
                      ChatCompletionCreateParams.builder()
                          .model(ChatModel.GPT_5_CHAT_LATEST)
                          .messages(allMessages)
                          .build(),
                  )

              val content = chatCompletion.choices()[0].message().content().orElse("")
              val fullConversation =
                  allMessages +
                      ChatCompletionMessageParam.ofAssistant(
                          ChatCompletionAssistantMessageParam.builder().content(content).build(),
                      )
              threadHistory.clear()
              threadHistory.addAll(fullConversation)

              mapOf("messages" to fullConversation)
          },
          TraceConfig.builder()
              .name("Chat Bot")
              .client(langsmith)
              .executor(executor)
              .metadata(threadMetadata)
              .build(),
      )
  }

  fun main() {
      try {
          val messages =
              listOf(
                  ChatCompletionMessageParam.ofUser(
                      ChatCompletionUserMessageParam.builder()
                          .content("Hi, my name is Sally")
                          .build(),
                  ),
              )
          chatPipeline(ChatRequest(messages))
      } finally {
          executor.shutdown()
          check(executor.awaitTermination(10, TimeUnit.SECONDS)) {
              "Timed out waiting for LangSmith traces to submit"
          }
      }
  }
  ```
</CodeGroup>

The Java and Kotlin examples use a dedicated executor. Shutting down the executor and awaiting termination ensures background trace submissions complete before the process exits.

Make the following calls to continue the conversation. By passing `get_chat_history=True` / `get_chat_history: true` / `getChatHistory = true`, you can continue the conversation from where it left off. This means that the LLM receives the entire message history and responds to it, instead of just responding to the latest message:

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  # Format message
  messages = [
      {
          "content": "What is my name",
          "role": "user"
      }
  ]

  # Call the chat pipeline
  result = chat_pipeline(messages, get_chat_history=True)
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  // Continue the conversation.
  const messages: Message[] = [{ role: "user", content: "What is my name" }];

  await chatPipeline({ messages, get_chat_history: true });
  ```

  ```java Java theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  List<ChatCompletionMessageParam> messages =
      Collections.singletonList(
          ChatCompletionMessageParam.ofUser(
              ChatCompletionUserMessageParam.builder()
                  .content("What is my name")
                  .build()));

  ThreadsChatPipeline.chatPipeline().apply(new ThreadsChatPipeline.ChatRequest(messages, true));
  ```

  ```kotlin Kotlin theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  val messages =
      listOf(
          ChatCompletionMessageParam.ofUser(
              ChatCompletionUserMessageParam.builder()
                  .content("What is my name")
                  .build(),
          ),
      )

  chatPipeline(ChatRequest(messages, getChatHistory = true))
  ```
</CodeGroup>

Keep the conversation going. Since past messages are included, the LLM will remember the conversation:

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  # Continue the conversation.
  messages = [
      {
          "content": "What was the first message I sent you?",
          "role": "user"
      }
  ]

  chat_pipeline(messages, get_chat_history=True)
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  // Continue the conversation.
  const messages: Message[] = [{ role: "user", content: "What was the first message I sent you?" }];

  await chatPipeline({ messages, get_chat_history: true });
  ```

  ```java Java theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  List<ChatCompletionMessageParam> messages =
      Collections.singletonList(
          ChatCompletionMessageParam.ofUser(
              ChatCompletionUserMessageParam.builder()
                  .content("What was the first message I sent you?")
                  .build()));

  ThreadsChatPipeline.chatPipeline().apply(new ThreadsChatPipeline.ChatRequest(messages, true));
  ```

  ```kotlin Kotlin theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  val messages =
      listOf(
          ChatCompletionMessageParam.ofUser(
              ChatCompletionUserMessageParam.builder()
                  .content("What was the first message I sent you?")
                  .build(),
          ),
      )

  chatPipeline(ChatRequest(messages, getChatHistory = true))
  ```
</CodeGroup>

## View threads

You can view threads in the [UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-threads) by clicking on the **Threads** tab in any [project details](https://smith.langchain.com/tracing) page. The table shows each thread's first input, last output, start times, turn count, latency (P50/P99), token usage, cost, and feedback score.

The right panel displays aggregate stats for the project, including thread and trace counts, total and median token usage, error rate, and P50/P99 latency.

<Callout type="info" icon="feather">
  Use the **[Chat](/langsmith/chat)** in thread views to analyze conversation threads, understand user sentiment, identify pain points, and track whether issues were resolved.
</Callout>

You can then click into a particular thread. You can view the thread in three different ways:

* **Messages** view (Beta): the conversation layer. Scan each turn as a chat-style thread showing user and assistant messages, tool calls, and subagent activity.
* **Turns** view: the per-turn summary. View each turn as a card showing its inputs and outputs, with expand/collapse and customizable input/output fields.
* **Details** view: the debugging layer. Drill into a specific run to inspect inputs, outputs, metadata, timing, errors, and child runs. The surrounding thread context stays visible so you can see where the run fits in the broader conversation.

Switch between views using the buttons at the top of the page or keyboard shortcuts `M` (Messages), `T` (Turns), and `D` (Details). While the Messages view is in beta, the thread side panel defaults to the Details view. The right panel shows stats for the thread, including turn count, first and last start times, P50/P99 latency, and a cost breakdown by input and output tokens. For a full description of each view, see [View traces](/langsmith/view-traces).

### View feedback

Feedback scores are visible in the **Feedback** column of the threads table on the project's **Threads** tab.

Within a thread, open the Messages view and click the **LLM call** link in a turn's metadata row to go to the Details view for that run, where you can review feedback for the run. You can also see [thread-level feedback](/langsmith/online-evaluations-multi-turn) there.

### Save thread-level filter

<Note>
  Thread filters look through all runs and surface a thread if at least 1 run matches the filter.
</Note>

On the **Threads** tab of a project, you can save commonly used filters: [Set a filter](/langsmith/filter-traces-in-application#create-and-apply-filters) using the **Add filter** button, then click **Save view**.

## Related

* [Observability concepts](/langsmith/observability-concepts#threads): background on threads and how they relate to runs and traces.
* [Add metadata and tags to traces](/langsmith/add-metadata-tags): how to pass `thread_id` and other metadata keys.
* [Filter traces](/langsmith/filter-traces-in-application): filter by thread metadata in the tracing UI.
* [Set up multi-turn online evaluators](/langsmith/online-evaluations-multi-turn): evaluate threads rather than individual runs.
* [Log user feedback using the SDK](/langsmith/attach-user-feedback): attach feedback to runs within a thread.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/threads.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Trace Anthropic applications
Source: https://docs.langchain.com/langsmith/trace-anthropic

The Anthropic wrapper methods in Python ([`wrap_anthropic`](https://reference.langchain.com/python/langsmith/wrappers/_anthropic/wrap_anthropic)) and Typescript ([`wrapAnthropic`](https://reference.langchain.com/javascript/functions/langsmith.wrappers_anthropic.wrapAnthropic.html)) allow you to wrap your Anthropic client in order to log traces automatically. Using the wrapper ensures that messages, including tool calls and multimodal content blocks will be rendered nicely in LangSmith. The wrapper works seamlessly alongside the `@traceable` decorator (Python) or `traceable` function (TypeScript), so you can trace your Anthropic calls with the wrapper and trace other parts of your application with the decorator or function.

<Note>
  The `LANGSMITH_TRACING` environment variable must be set to `'true'` in order for traces to be logged to LangSmith, even when using `wrap_anthropic` or `wrapAnthropic`. This allows you to toggle tracing on and off without changing your code.

  Additionally, you will need to set the `LANGSMITH_API_KEY` environment variable to your API key (see [Setup](/) for more information).

  If your LangSmith API key is linked to multiple workspaces, set the `LANGSMITH_WORKSPACE_ID` environment variable to specify which workspace to use.

  By default, the traces will be logged to a project named `default`. To log traces to a different project, see [Log traces to a specific project](/langsmith/log-traces-to-project).
</Note>

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import anthropic
  from langsmith import traceable
  from langsmith.wrappers import wrap_anthropic

  client = wrap_anthropic(anthropic.Anthropic())

  @traceable(run_type="tool", name="Retrieve Context")
  def my_tool(question: str) -> str:
    return "During this morning's meeting, we solved all world conflict."

  @traceable(name="Chat Pipeline")
  def chat_pipeline(question: str):
    context = my_tool(question)
    messages = [
        { "role": "user", "content": f"Question: {question}\nContext: {context}"}
    ]
    message = client.messages.create(
        model="claude-sonnet-4-6",
        messages=messages,
        max_tokens=1024,
        system="You are a helpful assistant. Please respond to the user's request only based on the given context."
    )
    return message

  chat_pipeline("Can you summarize this morning's meetings?")
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import Anthropic from "@anthropic-ai/sdk";
  import { traceable } from "langsmith/traceable";
  import { wrapAnthropic } from "langsmith/wrappers/anthropic";

  const client = wrapAnthropic(new Anthropic());

  const myTool = traceable(async (question: string) => {
    return "During this morning's meeting, we solved all world conflict.";
  }, { name: "Retrieve Context", run_type: "tool" });

  const chatPipeline = traceable(async (question: string) => {
    const context = await myTool(question);
    const messages = [
        { role: "user", content: `Question: ${question}\nContext: ${context}` }
    ];
    const message = await client.messages.create({
        model: "claude-sonnet-4-6",
        messages: messages,
        max_tokens: 1024,
        system: "You are a helpful assistant. Please respond to the user's request only based on the given context."
    });
    return message;
  }, { name: "Chat Pipeline" });

  await chatPipeline("Can you summarize this morning's meetings?");
  ```
</CodeGroup>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/trace-anthropic.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Trace Amazon Bedrock applications
Source: https://docs.langchain.com/langsmith/trace-bedrock

This guide shows you how to trace [Amazon Bedrock](https://aws.amazon.com/bedrock) model calls with LangSmith using the native AWS SDKs. LangSmith also works seamlessly with [LangChain's Bedrock integrations](/oss/python/integrations/providers/aws). Either approach provides insights into:

* Request and response payloads
* Token usage and costs
* Latency and performance metrics
* Custom tags and metadata for filtering and analysis
* Multi-step chains and agent workflows

## Installation

<CodeGroup>
  ```bash pip theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  pip install boto3 langsmith
  ```

  ```bash npm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  npm install @aws-sdk/client-bedrock-runtime langsmith
  ```
</CodeGroup>

This integration uses the native AWS SDKs with LangSmith's tracing capabilities. For Python, you'll use [`boto3`](https://pypi.org/project/boto3/) (the AWS SDK for Python) along with [`langsmith`](https://pypi.org/project/langsmith/) to capture traces. For JavaScript/TypeScript, you'll use [`@aws-sdk/client-bedrock-runtime`](https://www.npmjs.org/package/@aws-sdk/client-bedrock-runtime) with the [`langsmith`](https://www.npmjs.org/package/langsmith) package. Both implementations use the [Bedrock Converse API](https://docs.aws.amazon.com/bedrock/latest/userguide/conversation-inference.html), which provides a unified interface for interacting with foundation models.

## Setup

To enable LangSmith tracing, configure your [LangSmith API key](/langsmith/create-account-api-key) and project settings. You'll also need to set up your AWS credentials to authenticate with Bedrock.

### LangSmith configuration

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
export LANGSMITH_API_KEY=<your_langsmith_api_key>
export LANGSMITH_PROJECT=<your_project_name> # optional, defaults to "default"
export LANGSMITH_TRACING=true
```

You can obtain your LangSmith API key from [smith.langchain.com](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-trace-bedrock) by navigating to **Settings** > **API Keys**. The `LANGSMITH_PROJECT` variable allows you to organize traces into different projects.

### AWS credentials

Configure your AWS credentials to authenticate with Bedrock. You'll need an AWS account with Bedrock access enabled. Follow the [AWS setup instructions](https://docs.aws.amazon.com/bedrock/latest/userguide/setting-up.html) to create your credentials and [enable model access](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html):

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
export AWS_ACCESS_KEY_ID=<your_aws_access_key_id>
export AWS_SECRET_ACCESS_KEY=<your_aws_secret_key>
export AWS_SESSION_TOKEN=<your_session_token> # only if using temporary credentials
export AWS_DEFAULT_REGION=<your_bedrock_region> # e.g., us-east-1 or us-west-2
```

## Configure tracing

Once your environment variables are set, you can trace Bedrock model calls by wrapping your invocation functions with LangSmith's `@traceable` decorator (Python) or `traceable` function (TypeScript).

The following example demonstrates how to use the Bedrock Converse API with LangSmith tracing. The Converse API is AWS's recommended unified interface for foundation models, providing consistent request and response handling across different model providers. You can enhance traces with custom tags and metadata—tags help you categorize traces (e.g., by environment, feature, or test type), while metadata allows you to attach arbitrary key-value pairs for detailed context:

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import boto3
  from langsmith import traceable

  # Initialize Bedrock runtime client (ensure AWS creds and region are set)
  bedrock = boto3.client("bedrock-runtime", region_name="us-east-1")
  model_id = "anthropic.claude-haiku-4-5-20251001-v1:0"  # Example Bedrock model ID

  # Decorate the model invocation function to auto-capture a trace with tags/metadata
  @traceable(tags=["aws-bedrock", "langsmith", "integration-test"],
             metadata={"env": "dev", "model_provider": "bedrock", "model_id": "claude-3-haiku"})
  def generate_text(prompt: str) -> str:
      # Prepare a single-turn conversation input for the Converse API
      messages = [
          {"role": "user", "content": [{"text": prompt}]}
      ]
      # Invoke the Bedrock model using the unified Converse API
      response = bedrock.converse(
          modelId=model_id,
          messages=messages,
          inferenceConfig={"maxTokens": 512, "temperature": 0.5, "topP": 0.9}
      )
      # Extract the model's reply text from the response
      output_text = response["output"]["message"]["content"][0]["text"]
      return output_text

  # Call the traced function with a prompt
  result = generate_text("How can I trace AWS Bedrock model outputs to LangSmith for debugging?")
  print(result)
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { BedrockRuntimeClient, ConverseCommand } from "@aws-sdk/client-bedrock-runtime";
  import { traceable } from "langsmith";

  const client = new BedrockRuntimeClient({ region: "us-east-1" });
  const modelId = "anthropic.claude-haiku-4-5-20251001-v1:0";

  // Wrap the Bedrock invocation in a traceable function with tags and metadata
  const invokeBedrock = traceable(
    async (userInput: string) => {
      // Prepare the conversation message for the Bedrock Converse API
      const conversation = [
        { role: "user", content: [{ text: userInput }] }
      ];
      // Create and send a Bedrock Converse command (single-turn chat)
      const command = new ConverseCommand({
        modelId,
        messages: conversation,
        inferenceConfig: { maxTokens: 512, temperature: 0.5, topP: 0.9 }
      });
      const response = await client.send(command);
      // Extract the assistant's reply text from the response
      const outputText = response.output?.message?.content[0]?.text;
      return outputText;
    },
    {
      tags: ["aws-bedrock", "langsmith", "integration-test"],
      metadata: { env: "dev", model_provider: "bedrock", model_id: "claude-3-haiku" }
    }
  );

  // Invoke the traced function with a prompt
  const answer = await invokeBedrock("How can I trace AWS Bedrock model outputs to LangSmith for debugging?");
  console.log(answer);
  ```
</CodeGroup>

<Tabs>
  <Tab title="Python">
    * `boto3.client("bedrock-runtime")` creates a Bedrock Runtime client.
    * The `converse` method sends a chat prompt (as a list of messages) to the specified model and returns a structured response.
    * The `generate_text` function is decorated with `@traceable`, logging each call to LangSmith as a trace (using the function name as the default trace name).
    * Custom tags (`aws-bedrock`, `langsmith`, `integration-test`) and metadata (environment, model info) are passed into the decorator and attached to the trace record for filtering in the LangSmith UI.
    * When you run this code (with `LANGSMITH_TRACING=true` and your API key set), LangSmith automatically captures the input prompt, model output, token usage, and latency.
  </Tab>

  <Tab title="TypeScript">
    * `BedrockRuntimeClient` from the AWS SDK v3 provides the Bedrock runtime interface.
    * `ConverseCommand` offers a unified chat interface that sends a user message and returns the assistant's response in a structured format (no manual JSON parsing needed).
    * The Bedrock call is wrapped with LangSmith's `traceable` function, converting `invokeBedrock` into a traced function that logs its execution to LangSmith.
    * Custom tags and metadata are provided in the traceable options object and attached to each trace.
    * When you run this script (with `LANGSMITH_TRACING=true` and your API key configured), check your LangSmith dashboard for trace entries that include the input prompt, model output, timing info, and specified tags/metadata.
  </Tab>
</Tabs>

## View traces in LangSmith

After running your code, navigate to your LangSmith project at [smith.langchain.com](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-trace-bedrock) to view the traces. Each trace includes:

* **Request details**: Input messages, model parameters, and configuration
* **Response details**: Model output, token usage, and response metadata
* **Performance metrics**: Latency, tokens per second, and cost estimates
* **Custom metadata**: Tags and metadata you provided to the `@traceable` decorator

You can filter traces by tags (e.g., `aws-bedrock` or `integration-test`), search by metadata fields, or drill into specific traces to debug issues.

## Next steps

* Learn more about [LangSmith features](/langsmith) including evaluation, datasets, and feedback
* Explore [Bedrock model capabilities](https://docs.aws.amazon.com/bedrock/latest/userguide/models-features.html) like tool calling, streaming, and prompt caching
* Review [LangChain Bedrock integration documentation](/oss/python/integrations/chat/bedrock) for advanced features like extended thinking and citations

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/trace-bedrock.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Trace Claude Agent SDK applications
Source: https://docs.langchain.com/langsmith/trace-claude-agent-sdk

The [Claude Agent SDK](https://platform.claude.com/docs/en/agent-sdk/overview) is an SDK for building agentic applications with Claude. LangSmith provides native integration with the Claude Agent SDK to automatically trace your agent executions, tool calls, and interactions with Claude models.

## Installation

Install the LangSmith integration for Claude Agent SDK

<CodeGroup>
  ```bash uv theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  uv add langsmith[claude-agent-sdk]
  ```

  ```bash pip theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  pip install langsmith[claude-agent-sdk]
  ```

  ```bash pnpm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  pnpm add @anthropic-ai/claude-agent-sdk langsmith zod
  ```

  ```bash npm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  npm install @anthropic-ai/claude-agent-sdk langsmith zod
  ```
</CodeGroup>

## Setup

Set your [API keys](/langsmith/create-account-api-key):

<CodeGroup>
  ```bash shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  export LANGSMITH_TRACING=true
  export LANGSMITH_ENDPOINT=https://api.smith.langchain.com
  export LANGSMITH_API_KEY=<your_langsmith_api_key>
  export LANGSMITH_PROJECT=<your_langsmith_project>

  export ANTHROPIC_API_KEY=<your_anthropic_api_key>
  ```

  ```dotenv .env theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  LANGSMITH_TRACING=true
  LANGSMITH_ENDPOINT=https://api.smith.langchain.com
  LANGSMITH_API_KEY=<your_langsmith_api_key>
  LANGSMITH_PROJECT=<your_langsmith_project>

  ANTHROPIC_API_KEY=<your_anthropic_api_key>
  ```
</CodeGroup>

You can find your LangSmith API key and project name in the [LangSmith UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-trace-claude-agent-sdk) under **Settings**.

For an Anthropic API key, refer to the [Claude console](https://claude.ai/login).

## Quickstart

To enable LangSmith tracing for your Claude Agent SDK application, call `configure_claude_agent_sdk()` at the start of your application:

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import asyncio
  from typing import Any

  from claude_agent_sdk import (
      ClaudeAgentOptions,
      ClaudeSDKClient,
      create_sdk_mcp_server,
      tool,
  )
  from langsmith.integrations.claude_agent_sdk import configure_claude_agent_sdk

  configure_claude_agent_sdk()

  @tool(
      "get_weather",
      "Gets the current weather for a given city",
      {"city": str},
  )
  async def get_weather(args: dict[str, Any]) -> dict[str, Any]:
      city = args["city"]
      weather_data = {
          "San Francisco": "Foggy, 62°F",
          "New York": "Sunny, 75°F",
          "London": "Rainy, 55°F",
          "Tokyo": "Clear, 68°F",
      }
      weather = weather_data.get(city, "Weather data not available")
      return {"content": [{"type": "text", "text": f"Weather in {city}: {weather}"}]}

  async def main() -> None:
      weather_server = create_sdk_mcp_server(
          name="weather",
          version="1.0.0",
          tools=[get_weather],
      )

      options = ClaudeAgentOptions(
          model="claude-sonnet-4-5-20250929",
          system_prompt="You are a friendly travel assistant who helps with weather information.",
          mcp_servers={"weather": weather_server},
          allowed_tools=["mcp__weather__get_weather"],
      )

      async with ClaudeSDKClient(options=options) as client:
          await client.query("What's the weather like in San Francisco and Tokyo?")

          async for message in client.receive_response():
              print(message)

  if __name__ == "__main__":
      asyncio.run(main())
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import * as originalSdk from '@anthropic-ai/claude-agent-sdk';

  import { wrapClaudeAgentSDK } from 'langsmith/experimental/anthropic';
  import { z } from 'zod/v4';

  const sdk = wrapClaudeAgentSDK(originalSdk);

  const getWeather = sdk.tool(
    'get_weather',
    'Gets the current weather for a given city',
    {
      city: z.string(),
    },
    async ({ city }) => {
      const weatherData: Record<string, string> = {
        'San Francisco': 'Foggy, 62°F',
        'New York': 'Sunny, 75°F',
        London: 'Rainy, 55°F',
        Tokyo: 'Clear, 68°F',
      };
      const weather = weatherData[city] ?? 'Weather data not available';
      return {
        content: [{ type: 'text' as const, text: weather }],
      };
    }
  );

  const weatherServer = sdk.createSdkMcpServer({
    name: 'weather',
    version: '1.0.0',
    tools: [getWeather],
  });

  const query = sdk.query({
    prompt: "What's the weather like in San Francisco and Tokyo?",
    options: {
      model: 'claude-sonnet-4-5-20250929',
      systemPrompt:
        'You are a friendly travel assistant who helps with weather information.',
      mcpServers: { weather: weatherServer },
      allowedTools: ['mcp__weather__get_weather'],
    },
  });

  for await (const chunk of query) {
    console.log(chunk);
  }
  ```
</CodeGroup>

Once configured, all Claude Agent SDK operations will be automatically traced to LangSmith, including:

* Agent queries and responses
* Tool invocations and results
* Claude model interactions
* MCP server operations

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/trace-claude-agent-sdk.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
