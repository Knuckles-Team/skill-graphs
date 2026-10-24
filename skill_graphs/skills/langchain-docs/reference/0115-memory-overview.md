# Memory overview
Source: https://docs.langchain.com/oss/javascript/concepts/memory

[Memory](/oss/javascript/langgraph/add-memory) is a system that remembers information about previous interactions. For AI agents, memory is crucial because it lets them remember previous interactions, learn from feedback, and adapt to user preferences. As agents tackle more complex tasks with numerous user interactions, this capability becomes essential for both efficiency and user satisfaction.

This conceptual guide covers two types of memory, based on their recall scope:

* [Short-term memory](#short-term-memory), or [thread](/oss/javascript/langgraph/checkpointers#threads)-scoped memory, tracks the ongoing conversation by maintaining message history within a session. LangGraph manages short-term memory as a part of your agent's [state](/oss/javascript/langgraph/graph-api#state). State is persisted to a database using a [checkpointer](/oss/javascript/langgraph/checkpointers#checkpoints) so the thread can be resumed at any time. Short-term memory updates when the graph is invoked or a step is completed, and the State is read at the start of each step.
* [Long-term memory](#long-term-memory) stores user-specific or application-level data across sessions and is shared *across* conversational threads. It can be recalled *at any time* and *in any thread*. Memories are scoped to any custom namespace, not just within a single thread ID. LangGraph provides [stores](/oss/javascript/langgraph/stores) ([reference doc](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.BaseStore)) to let you save and recall long-term memories.

<img alt="Short vs long" />

## Short-term memory

[Short-term memory](/oss/javascript/langgraph/add-memory#add-short-term-memory) lets your application remember previous interactions within a single [thread](/oss/javascript/langgraph/checkpointers#threads) or conversation. A [thread](/oss/javascript/langgraph/checkpointers#threads) organizes multiple interactions in a session, similar to the way email groups messages in a single conversation.

LangGraph manages short-term memory as part of the agent's state, persisted via thread-scoped checkpoints. This state can normally include the conversation history along with other stateful data, such as uploaded files, retrieved documents, or generated artifacts. By storing these in the graph's state, the bot can access the full context for a given conversation while maintaining separation between different threads.

### Manage short-term memory

Conversation history is the most common form of short-term memory, and long conversations pose a challenge to today's LLMs. A full history may not fit inside an LLM's context window, resulting in an irrecoverable error. Even if your LLM supports the full context length, most LLMs still perform poorly over long contexts. They get "distracted" by stale or off-topic content, all while suffering from slower response times and higher costs.

Chat models accept context using messages, which include developer provided instructions (a system message) and user inputs (human messages). In chat applications, messages alternate between human inputs and model responses, resulting in a list of messages that grows longer over time. Because context windows are limited and token-rich message lists can be costly, many applications can benefit from using techniques to manually remove or forget stale information.

<img alt="Filter" />

For more information on common techniques for managing messages, see the [Add and manage memory](/oss/javascript/langgraph/add-memory#manage-short-term-memory) guide.

## Long-term memory

[Long-term memory](/oss/javascript/langgraph/add-memory#add-long-term-memory) in LangGraph allows systems to retain information across different conversations or sessions. Unlike short-term memory, which is **thread-scoped**, long-term memory is saved within custom "namespaces."

Long-term memory is a complex challenge without a one-size-fits-all solution. However, the following questions provide a framework to help you navigate the different techniques:

* What is the type of memory? Humans use memories to remember facts ([semantic memory](#semantic-memory)), experiences ([episodic memory](#episodic-memory)), and rules ([procedural memory](#procedural-memory)). AI agents can use memory in the same ways. For example, AI agents can use memory to remember specific facts about a user to accomplish a task.
* [When do you want to update memories?](#writing-memories) Memory can be updated as part of an agent's application logic (e.g., "on the hot path"). In this case, the agent typically decides to remember facts before responding to a user. Alternatively, memory can be updated as a background task (logic that runs in the background / asynchronously and generates memories). We explain the tradeoffs between these approaches in the [section below](#writing-memories).

Different applications require various types of memory. Although the analogy isn't perfect, examining [human memory types](https://www.psychologytoday.com/us/basics/memory/types-of-memory?ref=blog.langchain.dev) can be insightful. Some research (e.g., the [CoALA paper](https://arxiv.org/pdf/2309.02427)) have even mapped these human memory types to those used in AI agents.

| Memory Type                      | What is Stored | Human Example              | Agent Example       |
| -------------------------------- | -------------- | -------------------------- | ------------------- |
| [Semantic](#semantic-memory)     | Facts          | Things I learned in school | Facts about a user  |
| [Episodic](#episodic-memory)     | Experiences    | Things I did               | Past agent actions  |
| [Procedural](#procedural-memory) | Instructions   | Instincts or motor skills  | Agent system prompt |

### Semantic memory

[Semantic memory](https://en.wikipedia.org/wiki/Semantic_memory), both in humans and AI agents, involves the retention of specific facts and concepts. In humans, it can include information learned in school and the understanding of concepts and their relationships. For AI agents, semantic memory is often used to personalize applications by remembering facts or concepts from past interactions.

<Note>
  Semantic memory is different from "semantic search," which is a technique for finding similar content using "meaning" (usually as embeddings). Semantic memory is a term from psychology, referring to storing facts and knowledge, while semantic search is a method for retrieving information based on meaning rather than exact matches.
</Note>

Semantic memories can be managed in different ways:

#### Profile

Memories can be a single, continuously updated "profile" of well-scoped and specific information about a user, organization, or other entity (including the agent itself). A profile is generally just a JSON document with various key-value pairs you've selected to represent your domain.

When remembering a profile, you will want to make sure that you are **updating** the profile each time. As a result, you will want to pass in the previous profile and [ask the model to generate a new profile](https://github.com/langchain-ai/memory-template) (or some [JSON patch](https://github.com/hinthornw/trustcall) to apply to the old profile). This can be become error-prone as the profile gets larger, and may benefit from splitting a profile into multiple documents or **strict** decoding when generating documents to ensure the memory schemas remains valid.

<img alt="Update profile" />

#### Collection

Alternatively, memories can be a collection of documents that are continuously updated and extended over time. Each individual memory can be more narrowly scoped and easier to generate, which means that you're less likely to **lose** information over time. It's easier for an LLM to generate *new* objects for new information than reconcile new information with an existing profile. As a result, a document collection tends to lead to [higher recall downstream](https://en.wikipedia.org/wiki/Precision_and_recall).

However, this shifts some complexity memory updating. The model must now *delete* or *update* existing items in the list, which can be tricky. In addition, some models may default to over-inserting and others may default to over-updating. See the [Trustcall](https://github.com/hinthornw/trustcall) package for one way to manage this and consider evaluation (e.g., with a tool like [LangSmith](/langsmith/evaluation)) to help you tune the behavior.

Working with document collections also shifts complexity to memory **search** over the list. The `Store` currently supports both [semantic search](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.SearchOp.query) and [filtering by content](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.SearchOp.filter).

Finally, using a collection of memories can make it challenging to provide comprehensive context to the model. While individual memories may follow a specific schema, this structure might not capture the full context or relationships between memories. As a result, when using these memories to generate responses, the model may lack important contextual information that would be more readily available in a unified profile approach.

<img alt="Update list" />

Regardless of memory management approach, the central point is that the agent will use the semantic memories to [ground its responses](/oss/javascript/langchain/retrieval), which often leads to more personalized and relevant interactions.

### Episodic memory

[Episodic memory](https://en.wikipedia.org/wiki/Episodic_memory), in both humans and AI agents, involves recalling past events or actions. The [CoALA paper](https://arxiv.org/pdf/2309.02427) frames this well: facts can be written to semantic memory, whereas *experiences* can be written to episodic memory. For AI agents, episodic memory is often used to help an agent remember how to accomplish a task.

In practice, episodic memories are often implemented through few-shot example prompting, where agents learn from past sequences to perform tasks correctly. Sometimes it's easier to "show" than "tell" and LLMs learn well from examples. Few-shot learning lets you ["program"](https://x.com/karpathy/status/1627366413840322562) your LLM by updating the prompt with input-output examples to illustrate the intended behavior. While various best-practices can be used to generate few-shot examples, often the challenge lies in selecting the most relevant examples based on user input.

Note that the memory [store](/oss/javascript/langgraph/stores) is just one way to store data as few-shot examples. If you want to have more developer involvement, or tie few-shots more closely to your evaluation harness, you can also use a LangSmith Dataset to store your data and implement your own retrieval logic to select the most relevant examples based on user input.

See this [blog post](https://blog.langchain.dev/few-shot-prompting-to-improve-tool-calling-performance/) showcasing few-shot prompting to improve tool calling performance and this [blog post](https://blog.langchain.dev/aligning-llm-as-a-judge-with-human-preferences/) using few-shot examples to align an LLM to human preferences.

### Procedural memory

[Procedural memory](https://en.wikipedia.org/wiki/Procedural_memory), in both humans and AI agents, involves remembering the rules used to perform tasks. In humans, procedural memory is like the internalized knowledge of how to perform tasks, such as riding a bike via basic motor skills and balance. Episodic memory, on the other hand, involves recalling specific experiences, such as the first time you successfully rode a bike without training wheels or a memorable bike ride through a scenic route. For AI agents, procedural memory is a combination of model weights, agent code, and agent's prompt that collectively determine the agent's functionality.

In practice, it is fairly uncommon for agents to modify their model weights or rewrite their code. However, it is more common for agents to modify their own prompts.

One effective approach to refining an agent's instructions is through ["Reflection"](https://blog.langchain.dev/reflection-agents/) or meta-prompting. This involves prompting the agent with its current instructions (e.g., the system prompt) along with recent conversations or explicit user feedback. The agent then refines its own instructions based on this input. This method is particularly useful for tasks where instructions are challenging to specify upfront, as it allows the agent to learn and adapt from its interactions.

For example, we built a [Tweet generator](https://www.youtube.com/watch?v=Vn8A3BxfplE) using external feedback and prompt re-writing to produce high-quality paper summaries for Twitter. In this case, the specific summarization prompt was difficult to specify *a priori*, but it was fairly easy for a user to critique the generated Tweets and provide feedback on how to improve the summarization process.

The below pseudo-code shows how you might implement this with the LangGraph memory [store](/oss/javascript/langgraph/stores), using the store to save a prompt, the `update_instructions` node to get the current prompt (as well as feedback from the conversation with the user captured in `state["messages"]`), update the prompt, and save the new prompt back to the store. Then, the `call_model` get the updated prompt from the store and uses it to generate a response.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
// Node that *uses* the instructions
const callModel = async (state: State, store: BaseStore) => {
    const namespace = ["agent_instructions"];
    const instructions = await store.get(namespace, "agent_a");
    // Application logic
    const prompt = promptTemplate.format({
        instructions: instructions[0].value.instructions
    });
    // ...
};

// Node that updates instructions
const updateInstructions = async (state: State, store: BaseStore) => {
    const namespace = ["instructions"];
    const currentInstructions = await store.search(namespace);
    // Memory logic
    const prompt = promptTemplate.format({
        instructions: currentInstructions[0].value.instructions,
        conversation: state.messages
    });
    const output = await llm.invoke(prompt);
    const newInstructions = output.new_instructions;
    await store.put(["agent_instructions"], "agent_a", {
        instructions: newInstructions
    });
    // ...
};
```

<img alt="Update instructions" />

### Writing memories

There are two primary methods for agents to write memories: ["in the hot path"](#in-the-hot-path) and ["in the background"](#in-the-background).

<img alt="Hot path vs background" />

#### In the hot path

Creating memories during runtime offers both advantages and challenges. On the positive side, this approach allows for real-time updates, making new memories immediately available for use in subsequent interactions. It also enables transparency, as users can be notified when memories are created and stored.

However, this method also presents challenges. It may increase complexity if the agent requires a new tool to decide what to commit to memory. In addition, the process of reasoning about what to save to memory can impact agent latency. Finally, the agent must multitask between memory creation and its other responsibilities, potentially affecting the quantity and quality of memories created.

As an example, ChatGPT uses a [save\_memories](https://openai.com/index/memory-and-new-controls-for-chatgpt/) tool to upsert memories as content strings, deciding whether and how to use this tool with each user message. See our [memory-agent](https://github.com/langchain-ai/memory-agent) template as an reference implementation.

#### In the background

Creating memories as a separate background task offers several advantages. It eliminates latency in the primary application, separates application logic from memory management, and allows for more focused task completion by the agent. This approach also provides flexibility in timing memory creation to avoid redundant work.

However, this method has its own challenges. Determining the frequency of memory writing becomes crucial, as infrequent updates may leave other threads without new context. Deciding when to trigger memory formation is also important. Common strategies include scheduling after a set time period (with rescheduling if new events occur), using a cron schedule, or allowing manual triggers by users or the application logic.

See our [memory-service](https://github.com/langchain-ai/memory-template) template as an reference implementation.

### Memory storage

LangGraph stores long-term memories as JSON documents in a [store](/oss/javascript/langgraph/stores). Each memory is organized under a custom `namespace` (similar to a folder) and a distinct `key` (like a file name). Namespaces often include user or org IDs or other labels that makes it easier to organize information. This structure enables hierarchical organization of memories. Cross-namespace searching is then supported through content filters.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { InMemoryStore } from "@langchain/langgraph";

const embed = (texts: string[]): number[][] => {
    // Replace with an actual embedding function or LangChain embeddings object
    return texts.map(() => [1.0, 2.0]);
};

// InMemoryStore saves data to an in-memory dictionary. Use a DB-backed store in production use.
const store = new InMemoryStore({ index: { embed, dims: 2 } });
const userId = "my-user";
const applicationContext = "chitchat";
const namespace = [userId, applicationContext];

await store.put(
    namespace,
    "a-memory",
    {
        rules: [
            "User likes short, direct language",
            "User only speaks English & TypeScript",
        ],
        "my-key": "my-value",
    }
);

// get the "memory" by ID
const item = await store.get(namespace, "a-memory");

// search for "memories" within this namespace, filtering on content equivalence, sorted by vector similarity
const items = await store.search(
    namespace,
    {
        filter: { "my-key": "my-value" },
        query: "language preferences"
    }
);
```

For more information about the memory store, see the [Persistence](/oss/javascript/langgraph/stores) guide.

## Learn more

* [Context conceptual overview](/oss/javascript/concepts/context)
* [Short-term memory in LangChain](/oss/javascript/langchain/short-term-memory)
* [Memory in LangGraph](/oss/javascript/langgraph/add-memory)

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/concepts/memory.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Frameworks, runtimes, and harnesses
Source: https://docs.langchain.com/oss/javascript/concepts/products

Understand the differences between LangChain, LangGraph, and Deep Agents and when to use each one

LangChain maintains several open source packages to help you build agents. Each serves a different purpose in the agent development stack. Understanding the distinctions between [agent frameworks](#agent-frameworks-like-langchain), [agent runtimes](#agent-runtimes-like-langgraph), and [agent harnesses](#agent-harnesses-like-the-deep-agents-sdk) helps you choose the right tool for your needs.

<table>
  <thead>
    <tr>
      <th />

      <th>Framework</th>
      <th>Runtime</th>
      <th>Harness</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>Value add</td>
      <td><ul><li>Abstractions</li><li>Integrations</li></ul></td>
      <td><ul><li>Durable execution</li><li>Streaming</li><li>HITL</li><li>Persistence</li></ul></td>
      <td><ul><li>Predefined tools</li><li>Prompts</li><li>Subagents</li></ul></td>
    </tr>

    <tr>
      <td>When to use</td>
      <td><ul><li>Getting started quickly</li><li>Standardizing how a team builds</li></ul></td>
      <td><ul><li>Low-level control</li><li>Long running, stateful workflows and agents</li></ul></td>
      <td><ul><li>More autonomous agents</li><li>Agents faced with complex, non-deterministic tasks</li></ul></td>
    </tr>

    <tr>
      <td>Options</td>
      <td><ul><li>LangChain</li><li>Vercel's AI SDK</li><li>CrewAI</li><li>OpenAI Agents SDK</li><li>Google ADK</li><li>LlamaIndex</li></ul></td>
      <td><ul><li>LangGraph</li><li>Temporal</li><li>Inngest</li></ul></td>
      <td><ul><li>Deep Agents SDK</li><li>Claude Agent SDK</li><li>Manus</li></ul></td>
    </tr>
  </tbody>
</table>

## Agent frameworks (like LangChain)

Agent frameworks provide abstractions that make it easier to get started when building with LLMs.

[LangChain](/oss/javascript/langchain/overview) is an agent framework that provides abstractions like structured content blocks, the agent loop, and middleware.

LangChain's abstractions are designed to be easy to get started with while still providing the flexibility needed for advanced use cases.

While LangChain is built on top of [LangGraph](/oss/javascript/langgraph/overview), you don't need to know LangGraph to use LangChain.

Other examples of agent frameworks include [Vercel's AI SDK](https://ai-sdk.dev/docs/introduction), [CrewAI](https://www.crewai.com/), [OpenAI Agents SDK](https://openai.github.io/openai-agents-python/), [Google ADK](https://google.github.io/adk-docs/), [LlamaIndex](https://www.llamaindex.ai/), and many more.

### When to use LangChain

Use LangChain when:

* You want to quickly build agents and autonomous applications.
* You need standard abstractions for models, tools, and agent loops.
* You want an easy-to-use framework that still provides flexibility.
* You're building straightforward agent applications without complex orchestration needs.

## Agent runtimes (like LangGraph)

Agent runtimes provide the tooling for running agents in production.
Supported tools may include:

* **Durable execution**: Agents persist through failures and can run for extended periods, resuming from where they left off.
* **Streaming**: Support for streaming workflows and responses.
* **Human-in-the-loop**: Incorporate human oversight by inspecting and modifying agent state.
* **Persistence**: Thread-level and cross-thread persistence for state management.
* **Low-level control**: Direct control over agent orchestration without high-level abstractions.

[LangGraph](/oss/javascript/langgraph/overview) is a low-level orchestration framework and runtime for building, managing, and deploying long-running, stateful agents.

Agent frameworks are generally higher level and run on agent runtimes.
For example, LangChain 1.0 is built on top of LangGraph.

Other examples of agent runtimes include [Temporal](https://temporal.io/), [Inngest](https://www.inngest.com/), and other durable execution engines.

### When to use LangGraph

Use LangGraph when:

* You need fine-grained, low-level control over agent orchestration.
* You need durable execution for long-running, stateful agents.
* You're building complex workflows that combine deterministic and agentic steps.
* You need production-ready infrastructure for agent deployment.

## Agent harnesses (like the Deep Agents SDK)

Agent harnesses are opinionated, batteries-included frameworks with built-in tools and capabilities for building sophisticated, long-running agents.
Supported tools may include:

* **Planning capabilities**: Track multiple tasks with a to-do list.
* **Task delegation**: Delegate work and keep context clean with subagents.
* **File system**: Read and write access to files on different pluggable storage backends.
* **Token management**: Conversation history summarization and large tool result eviction.

The [Deep Agents SDK](/oss/javascript/deepagents/overview) builds on top of LangGraph and adds planning capabilities, file systems for context management, the ability to spawn subagents, and more.
Deep Agents is designed for complex, multi-step tasks that require planning and decomposition.

Example tasks include working with search results, scripts, and other artifacts in state.

Other examples of agent harnesses include [Claude Agent SDK](https://platform.claude.com/docs/en/agent-sdk/overview), [Manus](https://manus.im/), and other coding CLIs.

### When to use the Deep Agents SDK

Use the [Deep Agents SDK](/oss/javascript/deepagents/overview) when:

* You are building agents that run over long time periods.
* You are building agents that need to handle complex, multi-step tasks.
* You want to use predefined tools, such as filesystem operations, bash execution, and automated context engineering.
* You want to use predefined prompts and subagents.

## Feature comparison

While you can accomplish similar tasks with LangChain, LangGraph, and Deep Agents, the level at which you integrate them differ:

| Feature           | LangChain                                                                   | LangGraph                                                                       | Deep Agents                                                                      |
| ----------------- | --------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| Short-term memory | [Short-term memory](/oss/javascript/langchain/short-term-memory)            | [Short-term memory](/oss/javascript/langgraph/add-memory#add-short-term-memory) | [`StateBackend`](/oss/javascript/deepagents/backends#statebackend)               |
| Long-term memory  | [Long-term memory](/oss/javascript/langchain/long-term-memory)              | [Long-term memory](/oss/javascript/langgraph/add-memory#add-long-term-memory)   | [Long-term memory](/oss/javascript/deepagents/memory)                            |
| Skills            | [Multi-agent skills](/oss/javascript/langchain/multi-agent/skills)          | -                                                                               | [Skills](/oss/javascript/deepagents/skills)                                      |
| Subagents         | [Multi-agent subagents](/oss/javascript/langchain/multi-agent/subagents)    | [Subgraphs](/oss/javascript/langgraph/use-subgraphs)                            | [Subagents](/oss/javascript/deepagents/subagents)                                |
| Human-in-the-loop | [Human-in-the-loop middleware](/oss/javascript/langchain/human-in-the-loop) | [Interrupts](/oss/javascript/langgraph/interrupts)                              | [`interrupt_on` parameter](/oss/javascript/deepagents/harness#human-in-the-loop) |
| Streaming         | [Agent Streaming](/oss/javascript/langchain/event-streaming)                | [Streaming](/oss/javascript/langgraph/streaming)                                | [Streaming](/oss/javascript/deepagents/event-streaming)                          |

## Learn more

* [LangChain overview](/oss/javascript/langchain/overview)
* [LangGraph overview](/oss/javascript/langgraph/overview)
* [Deep Agents overview](/oss/javascript/deepagents/overview)

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/concepts/products.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Providers and models
Source: https://docs.langchain.com/oss/javascript/concepts/providers-and-models

Understand how LangChain uses providers to give you a single API for any model from any provider

LangChain gives you a single, unified API to work with models from any provider. Install a provider package, pick a model name, and start building—the same code works whether you use OpenAI, Anthropic, Google, or any other supported provider.

```mermaid theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
graph LR
    subgraph "Your code"
        A["LangChain API<br/>(invoke, stream, bind_tools)"]
    end

    subgraph "Providers"
        B["OpenAI"]
        C["Anthropic"]
        D["Google"]
        E["AWS Bedrock"]
        F["...and more"]
    end

    A --> B
    A --> C
    A --> D
    A --> E
    A --> F

    classDef code fill:#E5F4FF,stroke:#006DDD,stroke-width:2px,color:#030710
    classDef provider fill:#EBD0F0,stroke:#885270,stroke-width:2px,color:#441E33

    class A code
    class B,C,D,E,F provider
```

## One API for any model

Every LangChain chat model, regardless of provider, implements the same interface. This means you can:

* **Swap providers** without rewriting application logic
* **Compare models** side-by-side with identical code
* **Use advanced features** like [tool calling](/oss/javascript/langchain/tools), [structured output](/oss/javascript/langchain/structured-output), and [streaming](/oss/javascript/langchain/streaming) across all providers

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { initChatModel } from "langchain/chat_models/universal";

const openaiModel = await initChatModel("openai:gpt-5.5");
const anthropicModel = await initChatModel("anthropic:claude-opus-4-8");
const googleModel = await initChatModel("google-genai:gemini-3.1-pro-preview");

for (const model of [openaiModel, anthropicModel, googleModel]) {
    const response = await model.invoke("Explain quantum computing in one sentence.");
    console.log(response.text);
}
```

## What is a provider?

A **provider** is a company or platform that hosts AI models and exposes them through an API. Examples include OpenAI, Anthropic, Google, and AWS Bedrock.

In LangChain, each provider has a dedicated **integration package** (for example `langchain-openai`, `langchain-anthropic`) that implements the standard LangChain interface for that provider's models. This means:

* **Dedicated packages** for each provider with proper versioning and dependency management
* **Provider-specific features** are available when you need them (for example OpenAI's Responses API, Anthropic's extended thinking)
* **Automatic API key handling** through environment variables

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
npm install @langchain/openai       # For OpenAI models
npm install @langchain/anthropic    # For Anthropic models
npm install @langchain/google-genai # For Google models
```

For a full list of provider packages, see the [integrations page](/oss/javascript/integrations/providers/overview).

## Find model names

Each provider supports specific model names that you pass when initializing a chat model. There are two ways to specify a model:

<CodeGroup>
  ```typescript Provider prefix format theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { initChatModel } from "langchain/chat_models/universal";

  const model = await initChatModel("openai:gpt-5.5");
  ```

  ```typescript Direct class instantiation theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { ChatOpenAI } from "@langchain/openai";

  const model = new ChatOpenAI({ model: "gpt-5.5" });
  ```
</CodeGroup>

When using [`init_chat_model`](https://reference.langchain.com/javascript/langchain/chat_models/universal/initChatModel) with the `provider:model` format, LangChain automatically resolves the provider and loads the correct integration package. You can also omit the provider prefix if the model name is unambiguous (e.g., `"gpt-5.5"` resolves to OpenAI).

To find available model names for a provider, refer to the provider's own documentation. Here are some popular providers:

| Provider                                                      | Where to find model names                                                                              |
| :------------------------------------------------------------ | :----------------------------------------------------------------------------------------------------- |
| [OpenAI](/oss/javascript/integrations/providers/openai)       | [OpenAI models page](https://platform.openai.com/docs/models)                                          |
| [Anthropic](/oss/javascript/integrations/providers/anthropic) | [Anthropic models page](https://docs.anthropic.com/en/docs/about-claude/models)                        |
| [Google](/oss/javascript/integrations/providers/google)       | [Google AI models page](https://ai.google.dev/gemini-api/docs/models)                                  |
| [AWS Bedrock](/oss/javascript/integrations/providers/aws)     | [Bedrock supported models](https://docs.aws.amazon.com/bedrock/latest/userguide/models-supported.html) |

## Use new models immediately

Because LangChain provider packages pass model names directly to the provider's API, you can use new models the moment a provider releases them (no LangChain update required). Simply pass the new model name:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const model = await initChatModel("google_genai:gemini-mythos");
```

New model names work immediately as long as your provider package version supports the API version the model requires. In most cases, model releases are backward-compatible and require no package update.

## Model capabilities

Different providers and models support different features.
For a list of the chat model integrations and their capabilities, see the [chat models integrations page](/oss/javascript/integrations/chat).

## Routers and proxies

**Routers** (also called proxies or gateways) give you access to models from multiple providers through a single API and credential. They can simplify billing, let you switch between models without changing integrations, and offer features like automatic fallbacks and load balancing.

| Provider                             | Integration                                                      | Description                                                             |
| :----------------------------------- | :--------------------------------------------------------------- | :---------------------------------------------------------------------- |
| [OpenRouter](https://openrouter.ai/) | [`ChatOpenRouter`](/oss/javascript/integrations/chat/openrouter) | Unified access to models from OpenAI, Anthropic, Google, Meta, and more |

Routers are useful when you want to:

* **Access many providers** with a single API key and billing account
* **Switch models dynamically** without managing multiple provider credentials
* **Use fallback models** that automatically retry with a different model if the primary one fails

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { initChatModel } from "langchain/chat_models/universal";

const model = await initChatModel("openrouter:anthropic/claude-sonnet-4-6");
const response = await model.invoke("Hello!");
```

## OpenAI-compatible endpoints

Many providers offer endpoints compatible with OpenAI's [Chat Completions API](https://platform.openai.com/docs/api-reference/chat). You can connect to these using [`ChatOpenAI`](/oss/javascript/integrations/chat/openai) with a custom `base_url`:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { ChatOpenAI } from "@langchain/openai";

const model = new ChatOpenAI({
    configuration: { baseURL: "https://your-provider.com/v1" },
    apiKey: "your-api-key",
    model: "provider-model-name",
});
```

<Warning>
  `ChatOpenAI` targets [official OpenAI API specifications](https://github.com/openai/openai-openapi) only. Non-standard response fields from third-party providers are not extracted or preserved. Use a dedicated provider package or router when you need access to non-standard features.
</Warning>

## Next steps

<CardGroup>
  <Card title="Models guide" icon="cpu" href="/oss/javascript/langchain/models">
    Learn how to use models: invoke, stream, batch, tool calling, and more.
  </Card>

  <Card title="Chat model integrations" icon="message" href="/oss/javascript/integrations/chat">
    Browse all chat model integrations and their capabilities.
  </Card>

  <Card title="All providers" icon="grid-dots" href="/oss/javascript/integrations/providers/overview">
    See the full list of provider packages and integrations.
  </Card>

  <Card title="Agents" icon="robot" href="/oss/javascript/langchain/agents">
    Build agents that use models as their reasoning engine.
  </Card>
</CardGroup>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/concepts/providers-and-models.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
