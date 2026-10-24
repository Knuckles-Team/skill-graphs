# Custom instrumentation
Source: https://docs.langchain.com/langsmith/annotate-code

Instrument your code directly to control which functions are traced and how they appear in LangSmith.

Adding [instrumentation](/langsmith/observability-concepts#manual-instrumentation) directly to your code gives you precise control over which functions your application traces, what inputs and outputs are logged, and how your [trace](/langsmith/observability-concepts#traces) hierarchy is structured. The three core instrumentation approaches are:

* [`@traceable` decorator](#use-%40traceable-%2F-traceable): recommended for most cases
* [`trace` context manager](#use-the-trace-context-manager-python-only): Python only
* [`RunTree` API](#use-the-runtree-api): explicit, low-level control

This page also covers:

* [Specifying a custom run ID](#specify-a-custom-run-id), which is useful for attaching feedback immediately after a run or correlating with external systems.
* [Ensuring all traces are submitted](#ensure-all-traces-are-submitted-before-exiting) before your process exits.

For LangChain (Python or JS/TS), refer to the [LangChain-specific instructions](/langsmith/trace-with-langchain).

<Callout icon="plug">
  If you're using an LLM provider or agent framework with a built-in LangSmith integration, refer to the [integrations overview](/langsmith/integrations) instead
</Callout>

## Prerequisites

Before tracing, set the following environment variables:

* `LANGSMITH_TRACING=true`: enables tracing. Set this to toggle tracing on and off without changing your code.

  <Note>
    `LANGSMITH_TRACING` controls the `@traceable` decorator and the `trace` context manager. To override this at runtime for `@traceable` without changing environment variables, use [`tracing_context(enabled=True/False)`](#use-the-trace-context-manager-python-only) (Python) or pass `tracingEnabled` directly to `traceable` (JS/TS). [`RunTree` objects](#use-the-runtree-api) are not affected by any of these controls; they always send data to LangSmith when posted.
  </Note>

* `LANGSMITH_API_KEY`: your [LangSmith API key](/langsmith/create-account-api-key).

* By default, LangSmith logs traces to a project named `default`. To log to a different project, set `LANGSMITH_PROJECT`. For more details, refer to [Log traces to a specific project](/langsmith/log-traces-to-project).

## Use `@traceable` / `traceable`

Apply [`@traceable`](https://reference.langchain.com/python/langsmith/run_helpers/traceable) (Python), [`traceable`](https://reference.langchain.com/javascript/langsmith/traceable) (TypeScript), `traceable` (Kotlin) or `Tracing.traceFunction` (Java) to any function to make it a traced run. LangSmith handles context propagation across nested calls automatically.

The following example traces a simple pipeline: `run_pipeline` calls `format_prompt` to build the messages, `invoke_llm` to call the model, and `parse_output` to extract the result.

Each function is individually traced, and because they're called from within `run_pipeline` (also traced), LangSmith automatically nests them as child runs. `invoke_llm` uses `run_type="llm"` to mark it as an LLM call so LangSmith can render token counts and latency correctly:

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langsmith import traceable
  from openai import Client

  openai = Client()

  @traceable
  def format_prompt(subject):
    return [
        {
            "role": "system",
            "content": "You are a helpful assistant.",
        },
        {
            "role": "user",
            "content": f"What's a good name for a store that sells {subject}?"
        }
    ]

  @traceable(run_type="llm")
  def invoke_llm(messages):
    return openai.chat.completions.create(
        messages=messages, model="gpt-5.4-mini", temperature=0
    )

  @traceable
  def parse_output(response):
    return response.choices[0].message.content

  @traceable
  def run_pipeline():
    messages = format_prompt("colorful socks")
    response = invoke_llm(messages)
    return parse_output(response)

  run_pipeline()
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { traceable } from "langsmith/traceable";
  import OpenAI from "openai";

  const openai = new OpenAI();

  const formatPrompt = traceable((subject: string) => {
    return [
      {
        role: "system" as const,
        content: "You are a helpful assistant.",
      },
      {
        role: "user" as const,
        content: `What's a good name for a store that sells ${subject}?`,
      },
    ];
  },{ name: "formatPrompt" });

  const invokeLLM = traceable(
    async ({ messages }: { messages: { role: string; content: string }[] }) => {
        return openai.chat.completions.create({
            model: "gpt-5.4-mini",
            messages: messages,
            temperature: 0,
        });
    },
    { run_type: "llm", name: "invokeLLM" }
  );

  const parseOutput = traceable(
    (response: any) => {
        return response.choices[0].message.content;
    },
    { name: "parseOutput" }
  );

  const runPipeline = traceable(
    async () => {
        const messages = await formatPrompt("colorful socks");
        const response = await invokeLLM({ messages });
        return parseOutput(response);
    },
    { name: "runPipeline" }
  );

  await runPipeline();
  ```

  ```java Java theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import com.langchain.smith.tracing.RunType;
  import com.langchain.smith.tracing.TraceConfig;
  import com.langchain.smith.tracing.Tracing;
  import com.openai.client.OpenAIClient;
  import com.openai.client.okhttp.OpenAIOkHttpClient;
  import com.openai.models.ChatModel;
  import com.openai.models.chat.completions.ChatCompletion;
  import com.openai.models.chat.completions.ChatCompletionCreateParams;
  import com.openai.models.chat.completions.ChatCompletionMessageParam;
  import com.openai.models.chat.completions.ChatCompletionSystemMessageParam;
  import com.openai.models.chat.completions.ChatCompletionUserMessageParam;
  import java.util.Arrays;
  import java.util.List;
  import java.util.function.Function;

  public class TraceablePipeline {
    public static void main(String[] args) {
      new TraceablePipelineRunner().run();
    }

    private static final class TraceablePipelineRunner {
      private final OpenAIClient openai = OpenAIOkHttpClient.fromEnv();

      private final Function<String, List<ChatCompletionMessageParam>> formatPrompt =
          Tracing.traceFunction(
              subject ->
                  Arrays.asList(
                      ChatCompletionMessageParam.ofSystem(
                          ChatCompletionSystemMessageParam.builder()
                              .content("You are a helpful assistant.")
                              .build()),
                      ChatCompletionMessageParam.ofUser(
                          ChatCompletionUserMessageParam.builder()
                              .content("What's a good name for a store that sells " + subject + "?")
                              .build())),
              TraceConfig.builder().name("format_prompt").build());

      private final Function<List<ChatCompletionMessageParam>, ChatCompletion> invokeLlm =
          Tracing.traceFunction(
              messages ->
                  openai.chat()
                      .completions()
                      .create(
                          ChatCompletionCreateParams.builder()
                              .model(ChatModel.GPT_5_CHAT_LATEST)
                              .messages(messages)
                              .temperature(0.0)
                              .build()),
              TraceConfig.builder().name("invoke_llm").runType(RunType.LLM).build());

      private final Function<ChatCompletion, String> parseOutput =
          Tracing.traceFunction(
              response -> response.choices().get(0).message().content().orElse(""),
              TraceConfig.builder().name("parse_output").build());

      private final Function<String, String> runPipeline =
          Tracing.traceFunction(
              subject -> parseOutput.apply(invokeLlm.apply(formatPrompt.apply(subject))),
              TraceConfig.builder().name("run_pipeline").build());

      void run() {
        runPipeline.apply("colorful socks");
      }
    }
  }
  ```

  ```kotlin Kotlin theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import com.langchain.smith.tracing.RunType
  import com.langchain.smith.tracing.TraceConfig
  import com.langchain.smith.tracing.traceable
  import com.openai.client.okhttp.OpenAIOkHttpClient
  import com.openai.models.ChatModel
  import com.openai.models.chat.completions.ChatCompletion
  import com.openai.models.chat.completions.ChatCompletionCreateParams
  import com.openai.models.chat.completions.ChatCompletionMessageParam
  import com.openai.models.chat.completions.ChatCompletionSystemMessageParam
  import com.openai.models.chat.completions.ChatCompletionUserMessageParam
  import kotlin.jvm.optionals.getOrNull

  val openai = OpenAIOkHttpClient.fromEnv()

  val formatPrompt =
      traceable(
          { subject: String ->
              listOf(
                  ChatCompletionMessageParam.ofSystem(
                      ChatCompletionSystemMessageParam.builder()
                          .content("You are a helpful assistant.")
                          .build(),
                  ),
                  ChatCompletionMessageParam.ofUser(
                      ChatCompletionUserMessageParam.builder()
                          .content("What's a good name for a store that sells $subject?")
                          .build(),
                  ),
              )
          },
          TraceConfig.builder().name("format_prompt").build(),
      )

  val invokeLlm =
      traceable(
          { messages: List<ChatCompletionMessageParam> ->
              openai.chat().completions().create(
                  ChatCompletionCreateParams.builder()
                      .model(ChatModel.GPT_5_CHAT_LATEST)
                      .messages(messages)
                      .temperature(0.0)
                      .build(),
              )
          },
          TraceConfig.builder().name("invoke_llm").runType(RunType.LLM).build(),
      )

  val parseOutput =
      traceable(
          { response: ChatCompletion ->
              response.choices()[0].message().content().getOrNull().orEmpty()
          },
          TraceConfig.builder().name("parse_output").build(),
      )

  val runPipeline =
      traceable(
          { subject: String -> parseOutput(invokeLlm(formatPrompt(subject))) },
          TraceConfig.builder().name("run_pipeline").build(),
      )

  println(runPipeline("colorful socks"))
  ```
</CodeGroup>

In the [UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-annotate-code), you'll find a `run_pipeline` trace with `format_prompt`, `invoke_llm`, and `parse_output` as nested child runs.

<Note>
  When you wrap a sync function with `traceable` (e.g., `formatPrompt` in the previous example), use the `await` keyword when calling it to ensure the trace is logged correctly.
</Note>

## Use the `trace` context manager (Python only)

In Python, you can use the `trace` context manager to log traces to LangSmith. This is useful in situations where:

1. You want to log traces for a specific block of code.
2. You want control over the inputs, outputs, and other attributes of the trace.
3. It is not feasible to use a decorator or wrapper.
4. Any or all of the above.

The context manager integrates seamlessly with the `traceable` decorator and `wrap_openai` wrapper, so you can use them together in the same application.

The following example shows all three used together. `wrap_openai` wraps the OpenAI client so its calls are traced automatically. `my_tool` uses `@traceable` with `run_type="tool"` and a custom `name` to appear correctly in the trace. `chat_pipeline` itself is not decorated; instead, `ls.trace` wraps the call, letting you pass the project name and inputs explicitly and set outputs manually via `rt.end()`:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import openai
import langsmith as ls
from langsmith.wrappers import wrap_openai

client = wrap_openai(openai.Client())

@ls.traceable(run_type="tool", name="Retrieve Context")
def my_tool(question: str) -> str:
    return "During this morning's meeting, we solved all world conflict."

def chat_pipeline(question: str):
    context = my_tool(question)
    messages = [
        { "role": "system", "content": "You are a helpful assistant. Please respond to the user's request only based on the given context." },
        { "role": "user", "content": f"Question: {question}\nContext: {context}"}
    ]
    chat_completion = client.chat.completions.create(
        model="gpt-5.4-mini", messages=messages
    )
    return chat_completion.choices[0].message.content

app_inputs = {"input": "Can you summarize this morning's meetings?"}

with ls.trace("Chat Pipeline", "chain", project_name="my_test", inputs=app_inputs) as rt:
    output = chat_pipeline("Can you summarize this morning's meetings?")
    rt.end(outputs={"output": output})
```

## Use the `RunTree` API

Another, more explicit way to log traces to LangSmith is via the `RunTree` API. This API allows you more control over your tracing. You can manually create runs and children runs to assemble your trace. You still need to set your `LANGSMITH_API_KEY`, but `LANGSMITH_TRACING` is not necessary for this method.

This method is not recommended for most use cases; manually managing trace context is error-prone compared to `@traceable`, which handles context propagation automatically.

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import openai
  from langsmith.run_trees import RunTree

  # This can be a user input to your app
  question = "Can you summarize this morning's meetings?"

  # Create a top-level run
  pipeline = RunTree(
    name="Chat Pipeline",
    run_type="chain",
    inputs={"question": question}
  )
  pipeline.post()

  # This can be retrieved in a retrieval step
  context = "During this morning's meeting, we solved all world conflict."
  messages = [
    { "role": "system", "content": "You are a helpful assistant. Please respond to the user's request only based on the given context." },
    { "role": "user", "content": f"Question: {question}\nContext: {context}"}
  ]

  # Create a child run
  child_llm_run = pipeline.create_child(
    name="OpenAI Call",
    run_type="llm",
    inputs={"messages": messages},
  )
  child_llm_run.post()

  # Generate a completion
  client = openai.Client()
  chat_completion = client.chat.completions.create(
    model="gpt-5.4-mini", messages=messages
  )

  # End the runs and log them
  child_llm_run.end(outputs=chat_completion)
  child_llm_run.patch()
  pipeline.end(outputs={"answer": chat_completion.choices[0].message.content})
  pipeline.patch()
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import OpenAI from "openai";
  import { RunTree } from "langsmith";

  // This can be a user input to your app
  const question = "Can you summarize this morning's meetings?";

  const pipeline = new RunTree({
    name: "Chat Pipeline",
    run_type: "chain",
    inputs: { question }
  });
  await pipeline.postRun();

  // This can be retrieved in a retrieval step
  const context = "During this morning's meeting, we solved all world conflict.";
  const messages = [
    { role: "system", content: "You are a helpful assistant. Please respond to the user's request only based on the given context." },
    { role: "user", content: `Question: ${question}Context: ${context}` }
  ];

  // Create a child run
  const childRun = await pipeline.createChild({
    name: "OpenAI Call",
    run_type: "llm",
    inputs: { messages },
  });
  await childRun.postRun();

  // Generate a completion
  const client = new OpenAI();
  const chatCompletion = await client.chat.completions.create({
    model: "gpt-5.4-mini",
    messages: messages,
  });

  // End the runs and log them
  childRun.end(chatCompletion);
  await childRun.patchRun();
  pipeline.end({ outputs: { answer: chatCompletion.choices[0].message.content } });
  await pipeline.patchRun();
  ```

  ```java Java theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import com.langchain.smith.client.LangsmithClient;
  import com.langchain.smith.client.okhttp.LangsmithOkHttpClient;
  import com.langchain.smith.tracing.RunTree;
  import com.langchain.smith.tracing.RunType;
  import com.langchain.smith.tracing.TraceConfig;
  import com.openai.client.OpenAIClient;
  import com.openai.client.okhttp.OpenAIOkHttpClient;
  import com.openai.models.ChatModel;
  import com.openai.models.chat.completions.ChatCompletion;
  import com.openai.models.chat.completions.ChatCompletionCreateParams;
  import com.openai.models.chat.completions.ChatCompletionMessageParam;
  import com.openai.models.chat.completions.ChatCompletionSystemMessageParam;
  import com.openai.models.chat.completions.ChatCompletionUserMessageParam;
  import java.time.Instant;
  import java.util.Arrays;
  import java.util.Collections;
  import java.util.List;
  import java.util.concurrent.ExecutorService;
  import java.util.concurrent.Executors;
  import java.util.concurrent.TimeUnit;

  public class RunTreeExample {
      public static void main(String[] args) throws InterruptedException {
          LangsmithClient langsmith = LangsmithOkHttpClient.fromEnv();
          OpenAIClient openai = OpenAIOkHttpClient.fromEnv();
          ExecutorService executor = Executors.newSingleThreadExecutor();

          try {
              String question = "Can you summarize this morning's meetings?";
              String runId = "01990f3e-7f97-74c5-a9b6-8d3f7e8e2f11";

              RunTree pipeline = RunTree.builder()
                  .id(runId)
                  .name("Chat Pipeline")
                  .runType(RunType.CHAIN)
                  .inputs(Collections.singletonMap("question", question))
                  .client(langsmith)
                  .executor(executor)
                  .build();
              pipeline.postRun();

              String context = "During this morning's meeting, we solved all world conflict.";
              List<ChatCompletionMessageParam> messages = Arrays.asList(
                  ChatCompletionMessageParam.ofSystem(
                      ChatCompletionSystemMessageParam.builder()
                          .content(
                              "You are a helpful assistant. Please respond to the user's " +
                                  "request only based on the given context.")
                          .build()),
                  ChatCompletionMessageParam.ofUser(
                      ChatCompletionUserMessageParam.builder()
                          .content("Question: " + question + "\nContext: " + context)
                          .build()));

              RunTree childRun = pipeline.createChild(
                  TraceConfig.builder().name("OpenAI Call").runType(RunType.LLM).build());
              childRun.setInputs(Collections.singletonMap("messages", messages));
              childRun.postRun();

              ChatCompletion chatCompletion = openai.chat().completions().create(
                  ChatCompletionCreateParams.builder()
                      .model(ChatModel.GPT_5_CHAT_LATEST)
                      .messages(messages)
                      .build());

              String answer = chatCompletion.choices().get(0).message().content().orElse("");
              System.out.println(answer);

              childRun.setOutputs(Collections.singletonMap("response", chatCompletion.toString()));
              childRun.setEndTime(Instant.now().toString());
              childRun.patchRun();

              pipeline.setOutputs(Collections.singletonMap(
                  "answer", answer));
              pipeline.setEndTime(Instant.now().toString());
              pipeline.patchRun();
          } finally {
              executor.shutdown();
              if (!executor.awaitTermination(10, TimeUnit.SECONDS)) {
                  throw new IllegalStateException(
                      "Timed out waiting for LangSmith traces to submit");
              }
          }
      }
  }
  ```

  ```kotlin Kotlin theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import com.langchain.smith.client.okhttp.LangsmithOkHttpClient
  import com.langchain.smith.tracing.RunTree
  import com.langchain.smith.tracing.RunType
  import com.langchain.smith.tracing.TraceConfig
  import com.openai.client.okhttp.OpenAIOkHttpClient
  import com.openai.models.ChatModel
  import com.openai.models.chat.completions.ChatCompletionCreateParams
  import com.openai.models.chat.completions.ChatCompletionMessageParam
  import com.openai.models.chat.completions.ChatCompletionSystemMessageParam
  import com.openai.models.chat.completions.ChatCompletionUserMessageParam
  import java.time.Instant
  import java.util.concurrent.Executors
  import java.util.concurrent.TimeUnit

  val langsmith = LangsmithOkHttpClient.fromEnv()
  val openai = OpenAIOkHttpClient.fromEnv()
  val executor = Executors.newSingleThreadExecutor()

  try {
      val question = "Can you summarize this morning's meetings?"
      val runId = "01990f3e-7f97-74c5-a9b6-8d3f7e8e2f11"

      val pipeline =
          RunTree.builder()
              .id(runId)
              .name("Chat Pipeline")
              .runType(RunType.CHAIN)
              .inputs(mapOf("question" to question))
              .client(langsmith)
              .executor(executor)
              .build()
      println("[run-tree-example] Posting parent run to LangSmith…")
      pipeline.postRun()

      val context = "During this morning's meeting, we solved all world conflict."
      val messages =
          listOf(
              ChatCompletionMessageParam.ofSystem(
                  ChatCompletionSystemMessageParam.builder()
                      .content(
                          "You are a helpful assistant. Please respond to the user's " +
                              "request only based on the given context.",
                      )
                      .build(),
              ),
              ChatCompletionMessageParam.ofUser(
                  ChatCompletionUserMessageParam.builder()
                      .content("Question: $question\nContext: $context")
                      .build(),
              ),
          )

      val childRun =
          pipeline.createChild(
              TraceConfig.builder().name("OpenAI Call").runType(RunType.LLM).build(),
          )
      childRun.inputs = mapOf("messages" to messages)
      println("[run-tree-example] Posting child run to LangSmith…")
      childRun.postRun()

      val chatCompletion =
          openai.chat().completions().create(
              ChatCompletionCreateParams.builder()
                  .model(ChatModel.GPT_5_CHAT_LATEST)
                  .messages(messages)
                  .build(),
          )

      val answer = chatCompletion.choices()[0].message().content().orElse("")
      println("[run-tree-example] Answer:")
      println(answer)

      childRun.outputs = mapOf("response" to chatCompletion.toString())
      childRun.endTime = Instant.now().toString()
      childRun.patchRun()

      pipeline.outputs =
          mapOf(
              "answer" to answer,
          )
      pipeline.endTime = Instant.now().toString()
      pipeline.patchRun()
  } finally {
      executor.shutdown()
      check(executor.awaitTermination(10, TimeUnit.SECONDS)) {
          "Timed out waiting for LangSmith traces to submit"
      }
  }
  ```
</CodeGroup>

The Java and Kotlin examples use a custom root run ID and a dedicated executor. Shutting down the executor and awaiting termination ensures the background run submissions complete before the process exits.

## Example usage

You can extend the utilities explained in the previous section to trace any code. The following code shows some example extensions.

Trace any public method in a class:

```python expandable theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from typing import Any, Callable, Type, TypeVar

T = TypeVar("T")

def traceable_cls(cls: Type[T]) -> Type[T]:
    """Instrument all public methods in a class."""
    def wrap_method(name: str, method: Any) -> Any:
        if callable(method) and not name.startswith("__"):
            return traceable(name=f"{cls.__name__}.{name}")(method)
        return method

    # Handle __dict__ case
    for name in dir(cls):
        if not name.startswith("_"):
            try:
                method = getattr(cls, name)
                setattr(cls, name, wrap_method(name, method))
            except AttributeError:
                # Skip attributes that can't be set (e.g., some descriptors)
                pass

    # Handle __slots__ case
    if hasattr(cls, "__slots__"):
        for slot in cls.__slots__:  # type: ignore[attr-defined]
            if not slot.startswith("__"):
                try:
                    method = getattr(cls, slot)
                    setattr(cls, slot, wrap_method(slot, method))
                except AttributeError:
                    # Skip slots that don't have a value yet
                    pass

    return cls

@traceable_cls
class MyClass:
    def __init__(self, some_val: int):
        self.some_val = some_val

    def combine(self, other_val: int):
        return self.some_val + other_val

# See trace: https://smith.langchain.com/public/882f9ecf-5057-426a-ae98-0edf84fdcaf9/r
MyClass(13).combine(29)
```

## Specify a custom run ID

By default, LangSmith assigns a random ID to each run. You can override this when you need to know the run ID ahead of time (for example, to attach [feedback](/langsmith/attach-user-feedback) immediately after a run), correlate LangSmith runs with IDs from an external system, or make runs idempotent using a deterministic ID.

<Note>
  Use **UUID v7** for custom run IDs. UUIDv7 embeds a timestamp, which preserves correct time-ordering of runs in a trace. The LangSmith SDK exports a `uuid7` helper (Python v0.4.43+, JS v0.3.80+):

  * **Python**: `from langsmith import uuid7`
  * **JS/TS**: `import { uuid7 } from 'langsmith'`

  Any UUID v7 string is accepted — you can use the SDK helper or your own if your system already uses UUID v7 identifiers.
</Note>

Use one of the following:

* `@traceable`: pass `run_id` inside `langsmith_extra` when calling a `@traceable` function (Python), or pass `id` in the config object passed to `traceable` (TypeScript):

  <CodeGroup>
    ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    from langsmith import traceable, uuid7

    @traceable
    def my_pipeline(question: str) -> str:
        return "answer"

    run_id = uuid7()
    my_pipeline("What is the capital of France?", langsmith_extra={"run_id": run_id})

    # run_id can now be used to attach feedback, query the run, etc.
    ```

    ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    import { traceable } from "langsmith/traceable";
    import { uuid7 } from "langsmith";

    const runId = uuid7();

    const myPipeline = traceable(
    async (question: string) => {
        return "answer";
    },
    { name: "my-pipeline", id: runId }
    );

    await myPipeline("What is the capital of France?");

    // runId can now be used to attach feedback, query the run, etc.
    ```
  </CodeGroup>

* `trace` context manager (Python only): Pass `run_id` directly to the [trace](https://reference.langchain.com/python/langsmith/run_helpers/trace) context manager constructor:

  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langsmith import trace, uuid7

  run_id = uuid7()

  with trace("my-pipeline", run_id=run_id) as run:
      result = "answer"
      run.end(outputs={"result": result})

  # run_id can now be used to attach feedback, query the run, etc.
  ```

## Ensure all traces are submitted before exiting

LangSmith performs tracing in a background thread to avoid obstructing your production application. This means that your process may end before all traces are successfully posted to LangSmith. Refer to the following options:

* If you are using LangChain, refer to the [LangChain tracing guide](/langsmith/trace-with-langchain#ensure-all-traces-are-submitted-before-exiting).
* If you are using the [LangSmith SDK](/langsmith/reference) standalone, you can use the `flush` method before exit:

  <CodeGroup>
    ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    from langsmith import Client

    client = Client()

    @traceable(client=client)
    async def my_traced_func():
    # Your code here...
    pass

    try:
    await my_traced_func()
    finally:
    await client.flush()
    ```

    ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    import { Client } from "langsmith";

    const langsmithClient = new Client({});

    const myTracedFunc = traceable(async () => {
    // Your code here...
    },{ client: langsmithClient });

    try {
    await myTracedFunc();
    } finally {
    await langsmithClient.flush();
    }
    ```
  </CodeGroup>

## Related

* [Observability concepts](/langsmith/observability-concepts): background on runs, traces, and the LangSmith data model
* [Run (span) data format](/langsmith/run-data-format): schema reference for run fields including `dotted_order`, `trace_id`, and `parent_run_id`
* [Log user feedback using the SDK](/langsmith/attach-user-feedback): common use case for pre-specifying a run ID
* [Access the current run (span) within a traced function](/langsmith/access-current-span): read or modify the active run from inside a trace
* [Log traces to a specific project](/langsmith/log-traces-to-project): route traces to a named project instead of `default`
* [Trace with API](/langsmith/trace-with-api): low-level REST API alternative to the SDK
* [Tracing Basics video](https://academy.langchain.com/pages/intro-to-langsmith-preview) from the Introduction to LangSmith Course

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/annotate-code.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Annotate traces and runs inline
Source: https://docs.langchain.com/langsmith/annotate-traces-inline

LangSmith allows you to manually annotate traces with feedback within the application. This can be useful for adding context to a trace, such as a user's comment or a note about a specific issue.
You can annotate a trace either inline or by sending the trace to an annotation queue, which allows you to closely inspect and log feedbacks to runs one at a time.
Feedback tags are associated with your [workspace](/langsmith/administration-overview#workspaces).

<Note>
  **You can attach user feedback to ANY intermediate run (span) of the trace, not just the root span.**

  This is useful for critiquing specific parts of the LLM application, such as the retrieval step or generation step of the RAG pipeline.
</Note>

To annotate a trace inline, open the three-dot menu (`...`) in the trace view for any particular run that is part of the trace, then click **Notes**.

This will open up a pane that allows you to choose from feedback tags associated with your workspace and add a score for particular tags. You can also add a standalone comment. Follow [Set up feedback criteria](/langsmith/set-up-feedback-criteria) to set up feedback tags for your workspace.
You can also set up new feedback criteria from within the pane itself.

<img alt="Annotation sidebar" />

You can use the labeled keyboard shortcuts to streamline the annotation process.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/annotate-traces-inline.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Use annotation queues
Source: https://docs.langchain.com/langsmith/annotation-queues

*Annotation queues* give human reviewers a focused workflow for attaching feedback to specific [runs](/langsmith/observability-concepts#runs). While you can always annotate [traces](/langsmith/observability-concepts#traces) inline, annotation queues let you group runs together, prescribe rubrics, and track reviewer progress.

<Info>
  You can also manage annotation queues and feedback configs programmatically with the SDK. Refer to [Manage feedback & annotation queues programmatically](/langsmith/annotation-queues-sdk).
</Info>

LangSmith supports two queue styles:

* [**Single-run annotation queues**](#single-run-annotation-queues) present one run at a time and let reviewers submit any rubric feedback you configure. Single-run queues also support [assertions](/langsmith/assertions) to capture acceptance criteria for offline evaluation.
* [**Pairwise annotation queues (PAQs)**](#pairwise-annotation-queues) present two runs side-by-side so reviewers can quickly decide which output is better (or if they are equivalent) against the rubric items you define.

<Tip>
  For a demonstration of using annotation queues, watch the [Getting started with annotation queues](#video-guide) video guide.
</Tip>

## Single-run annotation queues

Single-run queues present one run at a time and let reviewers submit any rubric feedback you configure. They can be created directly from the **Annotation queues** section in the [LangSmith UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-annotation-queues).

### Create a single-run queue

1. Navigate to **Annotation Queues** in the left navigation.
2. Click **+ Annotation Queue** in the top-left corner.

   <img alt="Create Annotation Queue form with Basic Details, Annotation Rubric, and Feedback sections." />

#### Basic details

1. Fill in the **Name** and **Description** of the queue.
2. Optionally assign a **default dataset** to streamline exporting reviewed runs into a dataset in your LangSmith [workspace](/langsmith/administration-overview#workspaces).

#### Annotation rubric

1. Draft some high-level **Instructions** for your annotators, which will be shown in the sidebar on every run.
2. Click **+ Add a feedback rubric** to add feedback keys to your annotation queue. Annotators will be presented with these feedback keys on each run.
3. Add a description for each, as well as a short description of each category, if the feedback is categorical.

   <img alt="Annotation queue rubric form with instructions and desired feedback entered." />

   For example, with the descriptions in the previous screenshot, reviewers will see the **Annotation Rubric** details in the right-hand pane of the UI.

   <img alt="The rendered rubric for reviewers from the example instructions." />

#### Collaborator settings

Set a number of reviewers or the maximum time you want to reserve the item to a collaborator. When there are multiple annotators for a run, you can choose to have the run stay in the queue until all reviewers have marked it as **Done**. The settings are as follows:

* **All workspace members review each run**: When enabled, a run remains in the queue until every [workspace](/langsmith/administration-overview#workspaces) member has marked their review as **Done**.

* **Enable reservations on runs**: Reserving a run locks it for your review for a set amount of time. While a run is reserved, other reviewers can view it but cannot add feedback or notes. Reservations are disabled if all workspace members review each run.

  If a reviewer has viewed a run and then leaves the run without marking it **Done**, the reservation will expire after the specified **Reservation length**. The run is then released back into the queue and can be reserved by another reviewer.

  <Note>
    Clicking **Requeue** for a run's annotation will only move the current run to the end of the current user's queue; it won't affect the queue order of any other user. It will also release the reservation that the current user has on that run.
  </Note>

* **Number of reviewers per run**: This determines the number of reviewers that must mark a run as **Done** for it to be removed from the queue.

  * Reviewers cannot view the feedback left by other reviewers.
  * Comments on runs are visible to all reviewers.

  <Note>
    The **Number of reviewers per run** setting is hidden when **Use assigned reviewers** is enabled (see below).
  </Note>

* **Use assigned reviewers**: Enable this toggle to use specific workspace members instead of a count-based threshold. When enabled:

  * A multi-select user picker appears so you can choose specific workspace members as assigned reviewers.
  * A run is marked **Completed** only when every assigned reviewer has submitted their review. Queue items progress through three states: **Needs Review** → **Needs Others' Review** → **Completed**.
  * Non-assigned workspace members can still annotate runs, but their submissions do not count toward completion.
  * Any workspace member can edit the assigned reviewers list in the queue settings.

  <Note>
    When you add a new assigned reviewer to a queue that already has completed items, those items do not revert to pending. If you remove an assigned reviewer, any items they had not yet reviewed recalculate their completion status.
  </Note>

Because of these settings, the number of runs visible to each reviewer can differ from the total queue size.

### Edit a queue's settings

1. Open the **Edit Annotation Queue** panel for the annotation queue you want to edit. You can access this panel in two ways:

   * In the **Annotation queues** list, click the **Actions**  icon <Icon icon="dots-vertical" /> at the right of the queue's row. Select <Icon icon="pencil" /> **Edit** from the dropdown.
   * In the annotation queue view, click the **Settings** icon <Icon icon="settings" /> in the top-right corner.

2. In the **Edit Annotation Queue** panel, modify any of the settings you configured during queue creation and click **Save**.

### Assign runs to a single-run queue

There are several ways to populate a single-run queue with work items:

* **From the Details view**: Click **Add to Annotation Queue** in the top-right corner of any trace. You can add any intermediate [run](/langsmith/observability-concepts#runs), but not the root span.

  <img alt="Trace view with the Add to Annotation Queue button highlighted at the top of the screen." />

* **From the runs table**: Select multiple runs, then click **Add to Annotation Queue** at the bottom of the page.

  <img alt="View of the runs table with runs selected. Add to Annotation Queue button at the bottom of the page." />

* **Automation rules**: [Set up a rule](/langsmith/rules) to automatically assign runs that match a filter (for example, errors or low user scores) into a queue.

* **Datasets & experiments**: Select one or more [experiments](/langsmith/evaluation-concepts#experiment) within a dataset and click **<Icon icon="pencil" /> Annotate**. Choose an existing queue or create a new one, then confirm the (single-run) queue option.

  <img alt="Selected experiments with the Annotate button at the bottom of the page." />

### Review a single-run queue

1. Navigate to the **Annotation Queues** section through the left-hand navigation bar.

   The queue list includes an **Assigned Reviewers** column showing which reviewers are assigned to each queue. To see only queues assigned to you, click the **Assigned to me** filter at the top of the list.

2. Click on the queue you want to review. This will take you to a focused, cyclical view of the runs in the queue that require review. A left side panel shows the status of each run (**Needs Review**, **Needs Others' Review**, **Completed**).

3. Add **Reviewer Notes**, score [**Feedback**](/langsmith/observability-concepts#feedback) criteria, or mark the run as reviewed. To build a dataset, edit the run's input and output to create a corrected reference example and click **Add to Dataset**. Click **Delete** to remove the run from the queue for all users, regardless of any current reservations or queue settings.

   Instead of crafting a corrected reference output by hand, you can [write assertions](/langsmith/assertions) directly in the review side panel and save them as the example's expected output.

   <Tip>
     The keyboard shortcuts that are next to each option can help streamline the review process.
   </Tip>

## Pairwise annotation queues

Pairwise annotation queues (PAQs) present two runs side-by-side so reviewers can quickly decide which output is better (or if they are equivalent) against the rubric items you define. They are designed for fast A/B comparisons between two experiments (often a baseline vs. a candidate model) and must be created from the **Datasets & Experiments** pages.

### Create a pairwise queue

1. Navigate to **Datasets & Experiments**, open a dataset, and select **exactly two experiments** you want to compare.

2. Click **Annotate**. In the popover, choose **Add to Pairwise Annotation Queue**. (The button is disabled until exactly two experiments are selected.)

   <img alt="Popover showing the &#x22;Add to Pairwise Annotation Queue&#x22; card highlighted after two experiments are selected." />

3. Decide whether to send the experiments to an existing pairwise queue or create a new one.

4. Provide the queue details:
   * **Basic details** (name and description)
   * **Instructions & rubrics** tailored to pairwise scoring
   * **Collaborator settings** (reviewer count, reservations, reservation length)

5. Submit the form to create the queue. LangSmith immediately pairs runs from the two experiments and populates the queue.

Key differences for PAQs:

* **Experiments**: You must provide two experiment sessions up front. LangSmith automatically pairs their runs in chronological order and populates the queue during creation.
* **Rubric**: Pairwise rubric items only require a feedback key and (optionally) a description. Annotators decide whether Run A, Run B, or both are better for each rubric item.
* **Dataset**: Pairwise queues do not use a default dataset, because comparisons span two experiments.
* **Reservations & reviewers**: The same collaborator controls apply. Reservations help prevent two people from judging the same comparison simultaneously.

### Add more comparisons to a pairwise queue

If you need to add more comparisons later, return to **Datasets & Experiments**, select the two experiments again, and choose **Add to Pairwise Annotation Queue** to append new pairs.

Selecting two experiments and creating a PAQ automatically pairs the runs. When augmenting an existing PAQ, LangSmith preserves historical comparisons and appends new pairs to the queue.

### Review a pairwise queue

1. From **Annotation queues**, select the pairwise queue you want to review.
2. Each queue item displays Run A on the left and Run B on the right, along with your rubric.
3. For every rubric item:
   * Choose **A is better**, **B is better**, or **Equal**. The UI records binary feedback on both runs behind the scenes.
   * Use hotkeys `A`, `B`, or `E` to lock in your choice.
4. Once you finish all rubric items, press **Done** (or `Enter` on the final rubric item) to advance to the next comparison.
5. Optional actions:
   * Leave comments tied to either run.
   * Requeue the comparison if you need to revisit it later.
   * Open the Details view for deeper debugging.

Reservations, reviewer thresholds, and comments behave identically to those in single-run queues, enabling teams to use different queue types without modifying their existing workflow.

<img alt="Pairwise review screen showing runs side-by-side with the feedback pane containing A/B/Equal buttons and keyboard shortcuts." />

<Check>
  Consider routing runs that already have user feedback (e.g., thumbs-down) into a single-run queue for triage and a pairwise queue for head-to-head comparisons against a stronger baseline. This helps you identify regressions quickly. To learn more about how to capture user feedback from your LLM application, follow the guide on [attaching user feedback](/langsmith/attach-user-feedback).
</Check>

## Video guide

<iframe title="YouTube video player" />

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/annotation-queues.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
