        - Limit the number of attempts to 5.
        - If you are not successful after 5 attempts, return a note to the user.
        - Prefer explicit column lists; avoid SELECT *.
        `);

        export const agent = createAgent({
          model: "ollama:devstral-2",
          tools: [executeSql],
          systemPrompt: await getSystemPrompt(),
        });
        ```
      </CodeGroup>
    </Accordion>
  </Step>

  <Step title="Implement human-in-the-loop review">
    It can be prudent to check the agent's SQL queries before they are executed for any unintended actions or inefficiencies.

    LangChain agents feature support for built-in [human-in-the-loop middleware](/oss/javascript/langchain/human-in-the-loop) to add oversight to agent tool calls. Let's configure the agent to pause for human review on calling the `execute_sql` tool:

    <CodeGroup>
      ```ts Google theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import { createAgent, humanInTheLoopMiddleware } from "langchain"; // [!code highlight]
      import { MemorySaver } from "@langchain/langgraph"; // [!code highlight]

      agent = createAgent({
        model: "google-genai:gemini-3.5-flash",
        tools: [executeSql],
        systemPrompt: await getSystemPrompt(),
        middleware: [
          // [!code highlight]
          humanInTheLoopMiddleware({
            // [!code highlight]
            interruptOn: {
              execute_sql: true, // [!code highlight]
            },
            descriptionPrefix: "Tool execution pending approval", // [!code highlight]
          }),
        ], // [!code highlight]
        checkpointer: new MemorySaver(), // [!code highlight]
      });
      ```

      ```ts OpenAI theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import { createAgent, humanInTheLoopMiddleware } from "langchain"; // [!code highlight]
      import { MemorySaver } from "@langchain/langgraph"; // [!code highlight]

      agent = createAgent({
        model: "openai:gpt-5.5",
        tools: [executeSql],
        systemPrompt: await getSystemPrompt(),
        middleware: [
          // [!code highlight]
          humanInTheLoopMiddleware({
            // [!code highlight]
            interruptOn: {
              execute_sql: true, // [!code highlight]
            },
            descriptionPrefix: "Tool execution pending approval", // [!code highlight]
          }),
        ], // [!code highlight]
        checkpointer: new MemorySaver(), // [!code highlight]
      });
      ```

      ```ts Anthropic theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import { createAgent, humanInTheLoopMiddleware } from "langchain"; // [!code highlight]
      import { MemorySaver } from "@langchain/langgraph"; // [!code highlight]

      agent = createAgent({
        model: "anthropic:claude-sonnet-4-6",
        tools: [executeSql],
        systemPrompt: await getSystemPrompt(),
        middleware: [
          // [!code highlight]
          humanInTheLoopMiddleware({
            // [!code highlight]
            interruptOn: {
              execute_sql: true, // [!code highlight]
            },
            descriptionPrefix: "Tool execution pending approval", // [!code highlight]
          }),
        ], // [!code highlight]
        checkpointer: new MemorySaver(), // [!code highlight]
      });
      ```

      ```ts OpenRouter theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import { createAgent, humanInTheLoopMiddleware } from "langchain"; // [!code highlight]
      import { MemorySaver } from "@langchain/langgraph"; // [!code highlight]

      agent = createAgent({
        model: "openrouter:anthropic/claude-sonnet-4-6",
        tools: [executeSql],
        systemPrompt: await getSystemPrompt(),
        middleware: [
          // [!code highlight]
          humanInTheLoopMiddleware({
            // [!code highlight]
            interruptOn: {
              execute_sql: true, // [!code highlight]
            },
            descriptionPrefix: "Tool execution pending approval", // [!code highlight]
          }),
        ], // [!code highlight]
        checkpointer: new MemorySaver(), // [!code highlight]
      });
      ```

      ```ts Fireworks theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import { createAgent, humanInTheLoopMiddleware } from "langchain"; // [!code highlight]
      import { MemorySaver } from "@langchain/langgraph"; // [!code highlight]

      agent = createAgent({
        model: "fireworks:accounts/fireworks/models/qwen3p5-397b-a17b",
        tools: [executeSql],
        systemPrompt: await getSystemPrompt(),
        middleware: [
          // [!code highlight]
          humanInTheLoopMiddleware({
            // [!code highlight]
            interruptOn: {
              execute_sql: true, // [!code highlight]
            },
            descriptionPrefix: "Tool execution pending approval", // [!code highlight]
          }),
        ], // [!code highlight]
        checkpointer: new MemorySaver(), // [!code highlight]
      });
      ```

      ```ts Baseten theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import { createAgent, humanInTheLoopMiddleware } from "langchain"; // [!code highlight]
      import { MemorySaver } from "@langchain/langgraph"; // [!code highlight]

      agent = createAgent({
        model: "baseten:zai-org/GLM-5",
        tools: [executeSql],
        systemPrompt: await getSystemPrompt(),
        middleware: [
          // [!code highlight]
          humanInTheLoopMiddleware({
            // [!code highlight]
            interruptOn: {
              execute_sql: true, // [!code highlight]
            },
            descriptionPrefix: "Tool execution pending approval", // [!code highlight]
          }),
        ], // [!code highlight]
        checkpointer: new MemorySaver(), // [!code highlight]
      });
      ```

      ```ts Ollama theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import { createAgent, humanInTheLoopMiddleware } from "langchain"; // [!code highlight]
      import { MemorySaver } from "@langchain/langgraph"; // [!code highlight]

      agent = createAgent({
        model: "ollama:devstral-2",
        tools: [executeSql],
        systemPrompt: await getSystemPrompt(),
        middleware: [
          // [!code highlight]
          humanInTheLoopMiddleware({
            // [!code highlight]
            interruptOn: {
              execute_sql: true, // [!code highlight]
            },
            descriptionPrefix: "Tool execution pending approval", // [!code highlight]
          }),
        ], // [!code highlight]
        checkpointer: new MemorySaver(), // [!code highlight]
      });
      ```
    </CodeGroup>

    <Note>
      We've added a [checkpointer](/oss/javascript/langchain/short-term-memory) to our agent to allow execution to be paused and resumed. See the [human-in-the-loop guide](/oss/javascript/langchain/human-in-the-loop) for detalis on this as well as available middleware configurations.
    </Note>

    On running the agent, it will now pause for review before executing the `execute_sql` tool:

    ```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    question = "Which genre, on average, has the longest tracks?";
    const config = { configurable: { thread_id: "1" } }; // [!code highlight]

    for await (const step of await agent.stream(
      { messages: [{ role: "user", content: question }] },
      { ...config, streamMode: "values" }, // [!code highlight]
    )) {
      if ("__interrupt__" in step) {
        // [!code highlight]
        console.log("INTERRUPTED:"); // [!code highlight]
        for (const interrupt of step.__interrupt__) {
          // [!code highlight]
          for (const request of interrupt.value.actionRequests) {
            // [!code highlight]
            console.log(request.description); // [!code highlight]
          }
        }
      } else if (step.messages) {
        const message = step.messages.at(-1);
        console.log(`${message.role}: ${JSON.stringify(message.content, null, 2)}`);
      }
    }
    ```

    ```
    ...

    INTERRUPTED:
    Tool execution pending approval

    Tool: execute_sql
    Args: {'query': 'SELECT g.Name AS Genre, AVG(t.Milliseconds) AS AvgTrackLength FROM Track t JOIN Genre g ON t.GenreId = g.GenreId GROUP BY g.Name ORDER BY AvgTrackLength DESC LIMIT 1;'}
    ```

    We can resume execution, in this case accepting the query, using [Command](/oss/javascript/langgraph/use-graph-api#combine-control-flow-and-state-updates-with-command):

    ```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    import { Command } from "@langchain/langgraph"; // [!code highlight]

    for await (const step of await agent.stream(
      new Command({ resume: { decisions: [{ type: "approve" }] } }), // [!code highlight]
      { ...config, streamMode: "values" },
    )) {
      if (step.messages) {
        const message = step.messages.at(-1);
        console.log(`${message.role}: ${JSON.stringify(message.content, null, 2)}`);
      }
      if ("__interrupt__" in step) {
        console.log("INTERRUPTED:");
        for (const interrupt of step.__interrupt__) {
          for (const request of interrupt.value.actionRequests) {
            console.log(request.description);
          }
        }
      }
    }
    ```

    ```
    ================================== Ai Message ==================================
    Tool Calls:
      execute_sql (call_7oz86Epg7lYRqi9rQHbZPS1U)
     Call ID: call_7oz86Epg7lYRqi9rQHbZPS1U
      Args:
        query: SELECT Genre.Name, AVG(Track.Milliseconds) AS AvgDuration FROM Track JOIN Genre ON Track.GenreId = Genre.GenreId GROUP BY Genre.Name ORDER BY AvgDuration DESC LIMIT 5;
    ================================= Tool Message =================================
    Name: execute_sql

    [('Sci Fi & Fantasy', 2911783.0384615385), ('Science Fiction', 2625549.076923077), ('Drama', 2575283.78125), ('TV Shows', 2145041.0215053763), ('Comedy', 1585263.705882353)]
    ================================== Ai Message ==================================

    The genre with the longest average track length is "Sci Fi & Fantasy" with an average duration of about 2,911,783 milliseconds, followed by "Science Fiction" and "Drama."
    ```

    Refer to the [human-in-the-loop guide](/oss/javascript/langchain/human-in-the-loop) for details.
  </Step>
</Steps>

## Next steps

For deeper customization, check out [this tutorial](/oss/javascript/langgraph/sql-agent) for implementing a SQL agent directly using LangGraph primitives.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langchain/sql-agent.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
