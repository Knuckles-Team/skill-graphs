# Guardrails
Source: https://docs.langchain.com/oss/javascript/langchain/guardrails

Implement safety checks and content filtering for your agents

Guardrails help you build safe, compliant AI applications by validating and filtering content at key points in your agent's execution. They can detect sensitive information, enforce content policies, validate outputs, and prevent unsafe behaviors before they cause problems.

Common use cases include:

* Preventing PII leakage
* Detecting and blocking prompt injection attacks
* Blocking inappropriate or harmful content
* Enforcing business rules and compliance requirements
* Validating output quality and accuracy

You can implement guardrails using [middleware](/oss/javascript/langchain/middleware) to intercept execution at strategic points - before the agent starts, after it completes, or around model and tool calls.

<div>
  <img alt="Middleware flow diagram" />
</div>

Guardrails can be implemented using two complementary approaches:

<CardGroup>
  <Card title="Deterministic guardrails" icon="list-check">
    Use rule-based logic like regex patterns, keyword matching, or explicit checks. Fast, predictable, and cost-effective, but may miss nuanced violations.
  </Card>

  <Card title="Model-based guardrails" icon="brain">
    Use LLMs or classifiers to evaluate content with semantic understanding. Catch subtle issues that rules miss, but are slower and more expensive.
  </Card>
</CardGroup>

LangChain provides both built-in guardrails (e.g., [PII detection](#pii-detection), [human-in-the-loop](#human-in-the-loop)) and a flexible middleware system for building custom guardrails using either approach.

## Built-in guardrails

### PII detection

LangChain provides built-in middleware for detecting and handling Personally Identifiable Information (PII) in conversations. This middleware can detect common PII types like emails, credit cards, IP addresses, and more.

PII detection middleware is helpful for cases such as health care and financial applications with compliance requirements, customer service agents that need to sanitize logs, and generally any application handling sensitive user data.

The PII middleware supports multiple strategies for handling detected PII:

| Strategy | Description                             | Example               |
| -------- | --------------------------------------- | --------------------- |
| `redact` | Replace with `[REDACTED_{PII_TYPE}]`    | `[REDACTED_EMAIL]`    |
| `mask`   | Partially obscure (e.g., last 4 digits) | `****-****-****-1234` |
| `hash`   | Replace with deterministic hash         | `a8f5f167...`         |
| `block`  | Raise exception when detected           | Error thrown          |

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { createAgent, piiRedactionMiddleware } from "langchain";

const agent = createAgent({
  model: "gpt-5.5",
  tools: [customerServiceTool, emailTool],
  middleware: [
    // Redact emails in user input before sending to model
    piiRedactionMiddleware({
      piiType: "email",
      strategy: "redact",
      applyToInput: true,
    }),
    // Mask credit cards in user input
    piiRedactionMiddleware({
      piiType: "credit_card",
      strategy: "mask",
      applyToInput: true,
    }),
    // Block API keys - raise error if detected
    piiRedactionMiddleware({
      piiType: "api_key",
      detector: /sk-[a-zA-Z0-9]{32}/,
      strategy: "block",
      applyToInput: true,
    }),
  ],
});

// When user provides PII, it will be handled according to the strategy
const result = await agent.invoke({
  messages: [{
    role: "user",
    content: "My email is john.doe@example.com and card is 5105-1051-0510-5100"
  }]
});
```

<Accordion title="Built-in PII types and configuration">
  **Built-in PII types:**

  * `email` - Email addresses
  * `credit_card` - Credit card numbers (Luhn validated)
  * `ip` - IP addresses
  * `mac_address` - MAC addresses
  * `url` - URLs

  **Configuration options:**

  | Parameter            | Description                                                            | Default                     |
  | -------------------- | ---------------------------------------------------------------------- | --------------------------- |
  | `piiType`            | Type of PII to detect (built-in or custom)                             | Required                    |
  | `strategy`           | How to handle detected PII (`"block"`, `"redact"`, `"mask"`, `"hash"`) | `"redact"`                  |
  | `detector`           | Custom detector regex pattern                                          | `undefined` (uses built-in) |
  | `applyToInput`       | Check user messages before model call                                  | `true`                      |
  | `applyToOutput`      | Check AI messages after model call                                     | `false`                     |
  | `applyToToolResults` | Check tool result messages after execution                             | `false`                     |
</Accordion>

See the [middleware documentation](/oss/javascript/langchain/middleware#pii-detection) for complete details on PII detection capabilities.

### Human-in-the-loop

LangChain provides built-in middleware for requiring human approval before executing sensitive operations. This is one of the most effective guardrails for high-stakes decisions.

Human-in-the-loop middleware is helpful for cases such as financial transactions and transfers, deleting or modifying production data, sending communications to external parties, and any operation with significant business impact.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { createAgent, humanInTheLoopMiddleware } from "langchain";
import { MemorySaver, Command } from "@langchain/langgraph";

const agent = createAgent({
  model: "gpt-5.5",
  tools: [searchTool, sendEmailTool, deleteDatabaseTool],
  middleware: [
    humanInTheLoopMiddleware({
      interruptOn: {
        // Require approval for sensitive operations
        send_email: { allowAccept: true, allowEdit: true, allowRespond: true },
        delete_database: { allowAccept: true, allowEdit: true, allowRespond: true },
        // Auto-approve safe operations
        search: false,
      }
    }),
  ],
  checkpointer: new MemorySaver(),
});

// Human-in-the-loop requires a thread ID for persistence
const config = { configurable: { thread_id: "some_id" } };

// Agent will pause and wait for approval before executing sensitive tools
let result = await agent.invoke(
  { messages: [{ role: "user", content: "Send an email to the team" }] },
  config
);

result = await agent.invoke(
  new Command({ resume: { decisions: [{ type: "approve" }] } }),
  config  // Same thread ID to resume the paused conversation
);
```

<Tip>
  See the [human-in-the-loop documentation](/oss/javascript/langchain/human-in-the-loop) for complete details on implementing approval workflows.
</Tip>

## Custom guardrails

For more sophisticated guardrails, you can create custom middleware that runs before or after the agent executes. This gives you full control over validation logic, content filtering, and safety checks.

### Before agent guardrails

Use "before agent" hooks to validate requests once at the start of each invocation. This is useful for session-level checks like authentication, rate limiting, or blocking inappropriate requests before any processing begins.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { createMiddleware, AIMessage } from "langchain";

const contentFilterMiddleware = (bannedKeywords: string[]) => {
  const keywords = bannedKeywords.map(kw => kw.toLowerCase());

  return createMiddleware({
    name: "ContentFilterMiddleware",
    beforeAgent: {
      hook: (state) => {
        // Get the first user message
        if (!state.messages || state.messages.length === 0) {
          return;
        }

        const firstMessage = state.messages[0];
        if (firstMessage._getType() !== "human") {
          return;
        }

        const content = firstMessage.content.toString().toLowerCase();

        // Check for banned keywords
        for (const keyword of keywords) {
          if (content.includes(keyword)) {
            // Block execution before any processing
            return {
              messages: [
                new AIMessage(
                  "I cannot process requests containing inappropriate content. Please rephrase your request."
                )
              ],
              jumpTo: "end",
            };
          }
        }

        return;
      },
      canJumpTo: ['end']
    }
  });
};

// Use the custom guardrail
import { createAgent } from "langchain";

const agent = createAgent({
  model: "gpt-5.5",
  tools: [searchTool, calculatorTool],
  middleware: [
    contentFilterMiddleware(["hack", "exploit", "malware"]),
  ],
});

// This request will be blocked before any processing
const result = await agent.invoke({
  messages: [{ role: "user", content: "How do I hack into a database?" }]
});
```

### After agent guardrails

Use "after agent" hooks to validate final outputs once before returning to the user. This is useful for model-based safety checks, quality validation, or final compliance scans on the complete agent response.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { createMiddleware, AIMessage, initChatModel } from "langchain";

const safetyGuardrailMiddleware = () => {
  const safetyModel = initChatModel("gpt-5.4-mini");

  return createMiddleware({
    name: "SafetyGuardrailMiddleware",
    afterAgent: {
      hook: async (state) => {
        // Get the final AI response
        if (!state.messages || state.messages.length === 0) {
          return;
        }

        const lastMessage = state.messages[state.messages.length - 1];
        if (lastMessage._getType() !== "ai") {
          return;
        }

        // Use a model to evaluate safety
        const safetyPrompt = `Evaluate if this response is safe and appropriate.
        Respond with only 'SAFE' or 'UNSAFE'.

        Response: ${lastMessage.content.toString()}`;

        const result = await safetyModel.invoke([
          { role: "user", content: safetyPrompt }
        ]);

        if (result.content.toString().includes("UNSAFE")) {
          return {
            messages: [
              new AIMessage(
                "I cannot provide that response. Please rephrase your request."
              )
            ],
            jumpTo: "end",
          };
        }

        return;
      },
      canJumpTo: ['end']
    }
  });
};

// Use the safety guardrail
import { createAgent } from "langchain";

const agent = createAgent({
  model: "gpt-5.5",
  tools: [searchTool, calculatorTool],
  middleware: [safetyGuardrailMiddleware()],
});

const result = await agent.invoke({
  messages: [{ role: "user", content: "How do I make explosives?" }]
});
```

### Combine multiple guardrails

You can stack multiple guardrails by adding them to the middleware array. They execute in order, allowing you to build layered protection:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { createAgent, piiRedactionMiddleware, humanInTheLoopMiddleware } from "langchain";

const agent = createAgent({
  model: "gpt-5.5",
  tools: [searchTool, sendEmailTool],
  middleware: [
    // Layer 1: Deterministic input filter (before agent)
    contentFilterMiddleware(["hack", "exploit"]),

    // Layer 2: PII protection (before and after model)
    piiRedactionMiddleware({
      piiType: "email",
      strategy: "redact",
      applyToInput: true,
    }),
    piiRedactionMiddleware({
      piiType: "email",
      strategy: "redact",
      applyToOutput: true,
    }),

    // Layer 3: Human approval for sensitive tools
    humanInTheLoopMiddleware({
      interruptOn: {
        send_email: { allowAccept: true, allowEdit: true, allowRespond: true },
      }
    }),

    // Layer 4: Model-based safety check (after agent)
    safetyGuardrailMiddleware(),
  ],
});
```

## Additional resources

* [Middleware documentation](/oss/javascript/langchain/middleware) - Complete guide to custom middleware
* [Middleware API reference](https://reference.langchain.com/python/langchain/middleware/) - Complete guide to custom middleware
* [Human-in-the-loop](/oss/javascript/langchain/human-in-the-loop) - Add human review for sensitive operations
* [Testing agents](/oss/javascript/langchain/test/) - Strategies for testing safety mechanisms

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langchain/guardrails.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Human-in-the-loop
Source: https://docs.langchain.com/oss/javascript/langchain/human-in-the-loop

The Human-in-the-Loop (HITL) [middleware](/oss/javascript/langchain/middleware/built-in#human-in-the-loop) lets you add human oversight to agent tool calls.
When a model proposes an action that might require review—for example, writing to a file or executing SQL—the middleware can pause execution and wait for a decision.

It does this by checking each tool call against a configurable policy. If intervention is needed, the middleware issues an [interrupt](https://reference.langchain.com/javascript/langchain-langgraph/index/interrupt) that halts execution. The graph state is saved using LangGraph's [persistence layer](/oss/javascript/langgraph/persistence), so execution can pause safely and resume later.

A human decision then determines what happens next: the action can be approved as-is (`approve`), modified before running (`edit`), rejected with feedback (`reject`), or responded to directly (`respond`) for "ask user" style tools.

## Interrupt decision types

The [middleware](/oss/javascript/langchain/middleware/built-in#human-in-the-loop) defines four built-in ways a human can respond to an interrupt:

| Decision Type | Description                                                               | Example Use Case                                 |
| ------------- | ------------------------------------------------------------------------- | ------------------------------------------------ |
| ✅ `approve`   | The action is approved as-is and executed without changes.                | Send an email draft exactly as written           |
| ✏️ `edit`     | The tool call is executed with modifications.                             | Change the recipient before sending an email     |
| ❌ `reject`    | The tool call is rejected, with an explanation added to the conversation. | Deny file deletion and explain why               |
| 💬 `respond`  | Tool execution is skipped; the human's message becomes the tool result.   | Answer an "ask\_user" prompt with a direct reply |

The available decision types for each tool depend on the policy you configure in `interrupt_on`.
When multiple tool calls are paused at the same time, each action requires a separate decision.
Decisions must be provided in the same order as the actions appear in the interrupt request.

Use `reject` when the human is denying the requested action. Use `respond` only when the human is acting as the tool, such as answering an `ask_user` prompt. Do not use `respond` to deny side-effecting tools, because its message is treated as a successful tool result.

<Tip>
  When **editing** tool arguments, make changes conservatively. Significant modifications to the original arguments may cause the model to re-evaluate its approach and potentially execute the tool multiple times or take unexpected actions.
</Tip>

## Configuring interrupts

To use HITL, add the [middleware](/oss/javascript/langchain/middleware/built-in#human-in-the-loop) to the agent's `middleware` list when creating the agent.

You configure it with a mapping of tool actions to the decision types that are allowed for each action. The middleware will interrupt execution when a tool call matches an action in the mapping.

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { createAgent, humanInTheLoopMiddleware } from "langchain"; // [!code highlight]
import { MemorySaver } from "@langchain/langgraph"; // [!code highlight]

const agent = createAgent({
    model: "gpt-5.5",
    tools: [writeFileTool, executeSQLTool, readDataTool],
    middleware: [
        humanInTheLoopMiddleware({
            interruptOn: {
                write_file: true, // All decisions (approve, edit, reject, respond) allowed
                execute_sql: {
                    allowedDecisions: ["approve", "reject"],
                    // No editing allowed
                    description: "🚨 SQL execution requires DBA approval",
                },
                // Safe operation, no approval needed
                read_data: false,
            },
            // Prefix for interrupt messages - combined with tool name and args to form the full message
            // e.g., "Tool execution pending approval: execute_sql with query='DELETE FROM...'"
            // Individual tools can override this by specifying a "description" in their interrupt config
            descriptionPrefix: "Tool execution pending approval",
        }),
    ],
    // Human-in-the-loop requires checkpointing to handle interrupts.
    // In production, use a persistent checkpointer like AsyncPostgresSaver.
    checkpointer: new MemorySaver(), // [!code highlight]
});
```

<Info>
  You must configure a checkpointer to persist the graph state across interrupts.
  In production, use a persistent checkpointer like [`AsyncPostgresSaver`](https://reference.langchain.com/javascript/classes/_langchain_langgraph-checkpoint-postgres.AsyncPostgresSaver.html). For testing or prototyping, use [`InMemorySaver`](https://reference.langchain.com/javascript/classes/_langchain_langgraph-checkpoint.MemorySaver.html).

  When invoking the agent, pass a `config` that includes the **thread ID** to associate execution with a conversation thread.
  See the [LangGraph interrupts documentation](/oss/javascript/langgraph/interrupts) for details.
</Info>

<Accordion title="Configuration options">
  <ParamField type="object">
    Mapping of tool names to approval configs
  </ParamField>

  **Tool approval config options:**

  <ParamField type="boolean">
    Whether approval is allowed
  </ParamField>

  <ParamField type="boolean">
    Whether editing is allowed
  </ParamField>

  <ParamField type="boolean">
    Whether responding/rejection is allowed
  </ParamField>
</Accordion>

## Conditional interrupts

By default, every tool call listed in `interrupt_on` pauses for review. To pause only some calls, add a `when` predicate to a tool's `InterruptOnConfig`. The predicate receives a `ToolCallRequest` and returns `True` to interrupt or `False` to auto-approve, so you can gate on the tool's arguments.

Conditional interrupts are currently available in Python only.

## Responding to interrupts

When you invoke the agent, it runs until it either completes or an interrupt is raised. An interrupt is triggered when a tool call matches the policy you configured in `interrupt_on`. With `version="v2"`, the result is a `GraphOutput` with an `interrupts` attribute containing the actions that require review. You can then present those actions to a reviewer and resume execution once decisions are provided.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { HumanMessage } from "@langchain/core/messages";
import { Command } from "@langchain/langgraph";

// You must provide a thread ID to associate the execution with a conversation thread,
// so the conversation can be paused and resumed (as is needed for human review).
const config = { configurable: { thread_id: "some_id" } }; // [!code highlight]

// Run the graph until the interrupt is hit.
const result = await agent.invoke(
    {
        messages: [new HumanMessage("Delete old records from the database")],
    },
    config // [!code highlight]
);

// The interrupt contains the full HITL request with action_requests and review_configs
console.log(result.__interrupt__);
// > [
// >    Interrupt(
// >       value: {
// >          actionRequests: [
// >             {
// >                name: 'execute_sql',
// >                arguments: { query: 'DELETE FROM records WHERE created_at < NOW() - INTERVAL \'30 days\';' },
// >                description: 'Tool execution pending approval\n\nTool: execute_sql\nArgs: {...}'
// >             }
// >          ],
// >          reviewConfigs: [
// >             {
// >                actionName: 'execute_sql',
// >                allowedDecisions: ['approve', 'reject']
// >             }
// >          ]
// >       }
// >    )
// > ]

// Resume with approval decision
await agent.invoke(
    new Command({ // [!code highlight]
        resume: { decisions: [{ type: "approve" }] }, // or "reject" [!code highlight]
    }), // [!code highlight]
    config // Same thread ID to resume the paused conversation
);
```

### Decision types

<Tabs>
  <Tab title="✅ approve">
    Use `approve` to approve the tool call as-is and execute it without changes.

    ```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    await agent.invoke(
        new Command({
            // Decisions are provided as a list, one per action under review.
            // The order of decisions must match the order of actions
            // in the interrupt request.
            resume: {
                decisions: [
                    {
                        type: "approve",
                    }
                ]
            }
        }),
        config  // Same thread ID to resume the paused conversation
    );
    ```
  </Tab>

  <Tab title="✏️ edit">
    Use `edit` to modify the tool call before execution.
    Provide the edited action with the new tool name and arguments.

    ```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    await agent.invoke(
        new Command({
            // Decisions are provided as a list, one per action under review.
            // The order of decisions must match the order of actions
            // in the interrupt request.
            resume: {
                decisions: [
                    {
                        type: "edit",
                        // Edited action with tool name and args
                        editedAction: {
                            // Tool name to call.
                            // Will usually be the same as the original action.
                            name: "new_tool_name",
                            // Arguments to pass to the tool.
                            args: { key1: "new_value", key2: "original_value" },
                        }
                    }
                ]
            }
        }),
        config  // Same thread ID to resume the paused conversation
    );
    ```

    <Tip>
      When **editing** tool arguments, make changes conservatively. Significant modifications to the original arguments may cause the model to re-evaluate its approach and potentially execute the tool multiple times or take unexpected actions.
    </Tip>
  </Tab>

  <Tab title="❌ reject">
    Use `reject` to deny the tool call and provide feedback instead of execution. The tool is not executed.

    ```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    await agent.invoke(
        new Command({
            // Decisions are provided as a list, one per action under review.
            // The order of decisions must match the order of actions
            // in the interrupt request.
            resume: {
                decisions: [
                    {
                        type: "reject",
                        // Optional: explain why the action was rejected
                        // and whether the agent should retry a different approach.
                        message: "User rejected this action. Do not retry this tool call.",
                    }
                ]
            }
        }),
        config  // Same thread ID to resume the paused conversation
    );
    ```

    The `message` is added to the conversation as feedback to help the agent understand why the action was rejected and what it should do instead. When you omit `message`, the middleware uses a default rejection message that tells the model the tool was not executed and not to retry the same tool call unless the user asks. For side-effecting tools, provide a domain-specific message that is explicit about whether the agent should abandon the action, ask a follow-up question, or try a safer alternative.
  </Tab>

  <Tab title="💬 respond">
    Use `respond` for "ask user" style tools where the tool's real implementation is the human's reply. The `message` content is returned directly as the tool result; the tool itself is not executed.

    ```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    await agent.invoke(
        new Command({
            // Decisions are provided as a list, one per action under review.
            // The order of decisions must match the order of actions
            // in the interrupt request.
            resume: {
                decisions: [
                    {
                        type: "respond",
                        // The human's reply, returned directly as the tool result
                        message: "Blue.",
                    }
                ]
            }
        }),
        config  // Same thread ID to resume the paused conversation
    );
    ```

    The `message` is returned to the agent as a successful `ToolMessage`. Use `respond` when the tool is intentionally a placeholder for human input, for example, an `ask_user` tool that prompts for clarification. Do not use `respond` to deny a proposed action, because it tells the model that the tool completed successfully.
  </Tab>
</Tabs>

***

### Multiple decisions

When multiple actions are under review, provide a decision for each action in the same order as they appear in the interrupt:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
    decisions: [
        { type: "approve" },
        {
            type: "edit",
            editedAction: {
                name: "tool_name",
                args: { param: "new_value" }
            }
        },
        {
            type: "reject",
            message: "This action is not allowed"
        }
    ]
}
```

## Streaming with human-in-the-loop

You can use `stream()` instead of `invoke()` to get real-time updates while the agent runs and handles interrupts. Use `stream_mode=['updates', 'messages']` with `version="v2"` to stream both agent progress and LLM tokens in the unified v2 format.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { Command } from "@langchain/langgraph";

const config = { configurable: { thread_id: "some_id" } };

// Stream agent progress and LLM tokens until interrupt
for await (const [mode, chunk] of await agent.stream(
    { messages: [{ role: "user", content: "Delete old records from the database" }] },
    { ...config, streamMode: ["updates", "messages"] }  // [!code highlight]
)) {
    if (mode === "messages") {
        // LLM token
        const [token, metadata] = chunk;
        if (token.content) {
            process.stdout.write(token.content);
        }
    } else if (mode === "updates") {
        // Check for interrupt
        if ("__interrupt__" in chunk) {
            console.log(`\n\nInterrupt: ${JSON.stringify(chunk.__interrupt__)}`);
        }
    }
}

// Resume with streaming after human decision
for await (const [mode, chunk] of await agent.stream(
    new Command({ resume: { decisions: [{ type: "approve" }] } }),
    { ...config, streamMode: ["updates", "messages"] }
)) {
    if (mode === "messages") {
        const [token, metadata] = chunk;
        if (token.content) {
            process.stdout.write(token.content);
        }
    }
}
```

See the [Streaming](/oss/javascript/langchain/streaming) guide for more details on stream modes.

## Execution lifecycle

The middleware defines an `after_model` hook that runs after the model generates a response but before any tool calls are executed:

1. The agent invokes the model to generate a response.
2. The middleware inspects the response for tool calls.
3. If any calls require human input, the middleware builds a `HITLRequest` with `action_requests` and `review_configs` and calls [interrupt](https://reference.langchain.com/javascript/langchain-langgraph/index/interrupt).
4. The agent waits for human decisions.
5. Based on the `HITLResponse` decisions, the middleware executes approved or edited calls, synthesizes [ToolMessage](https://reference.langchain.com/javascript/langchain-core/messages/ToolMessage)'s for rejected calls, returns human replies directly as [ToolMessage](https://reference.langchain.com/javascript/langchain-core/messages/ToolMessage)'s for `respond` decisions, and resumes execution.

## Custom HITL logic

For more specialized workflows, you can build custom HITL logic directly using the [interrupt](https://reference.langchain.com/javascript/langchain-langgraph/index/interrupt) primitive and [middleware](/oss/javascript/langchain/middleware) abstraction.

Review the [execution lifecycle](#execution-lifecycle) above to understand how to integrate interrupts into the agent's operation.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langchain/human-in-the-loop.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Install LangChain
Source: https://docs.langchain.com/oss/javascript/langchain/install

To install the LangChain package:

<CodeGroup>
  ```bash npm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  npm install langchain @langchain/core
  # Requires Node.js 20+
  ```

  ```bash pnpm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  pnpm add langchain @langchain/core
  # Requires Node.js 20+
  ```

  ```bash yarn theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  yarn add langchain @langchain/core
  # Requires Node.js 20+
  ```

  ```bash bun theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  bun add langchain @langchain/core
  # Requires Bun v1.0.0+
  ```
</CodeGroup>

LangChain provides integrations to hundreds of LLMs and thousands of other integrations. These live in independent provider packages.

<CodeGroup>
  ```bash npm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  # Installing the OpenAI integration
  npm install @langchain/openai
  # Installing the Anthropic integration
  npm install @langchain/anthropic
  ```

  ```bash pnpm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  # Installing the OpenAI integration
  pnpm install @langchain/openai
  # Installing the Anthropic integration
  pnpm install @langchain/anthropic
  ```

  ```bash yarn theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  # Installing the OpenAI integration
  yarn add @langchain/openai
  # Installing the Anthropic integration
  yarn add @langchain/anthropic
  ```

  ```bash bun theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  # Installing the OpenAI integration
  bun add @langchain/openai
  # Installing the Anthropic integration
  bun add @langchain/anthropic
  ```
</CodeGroup>

<Tip>
  See the [Integrations tab](/oss/javascript/integrations/providers/overview) for a full list of available integrations.
</Tip>

Now that you have LangChain installed, you can get started by following the [Quickstart guide](/oss/javascript/langchain/quickstart).

<Tip>
  Set up [LangSmith](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=oss-langchain-install) tracing to debug your first LangChain app. Follow the [tracing quickstart](/langsmith/trace-with-langchain) to get started. We recommend you also set up [LangSmith Engine](/langsmith/engine) which monitors your traces, detects issues, and proposes fixes.
</Tip>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langchain/install.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
