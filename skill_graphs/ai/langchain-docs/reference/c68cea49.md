        userId: z.string(),
      });

      // Schema defines the structure of user information for the LLM
      const UserInfo = z.object({
        name: z.string(),
      });

      // Tool that allows agent to update user information (useful for chat applications)
      const saveUserInfo = tool(
        async (
          userInfo: z.infer<typeof UserInfo>,
          runtime: ToolRuntime<unknown, z.infer<typeof contextSchema>>,
        ) => {
          const userId = runtime.context.userId;
          if (!userId) {
            throw new Error("userId is required");
          }
          // Store data in the store (namespace, key, data)
          await runtime.store.put(["users"], userId, userInfo);
          return "Successfully saved user info.";
        },
        {
          name: "save_user_info",
          description: "Save user info",
          schema: UserInfo,
        },
      );

      const agent = createAgent({
        model: "ollama:devstral-2",
        tools: [saveUserInfo],
        contextSchema,
        store,
      });

      // Run the agent
      await agent.invoke(
        { messages: [{ role: "user", content: "My name is John Smith" }] },
        // userId passed in context to identify whose information is being updated
        { context: { userId: "user_123" } },
      );

      // You can access the store directly to get the value
      const result = await store.get(["users"], "user_123");
      console.log(result?.value); // Output: { name: "John Smith" }
      ```
    </CodeGroup>
  </Tab>

  <Tab title="PostgreSQL">
    <CodeGroup>
      ```ts Google theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import * as z from "zod";
      import { tool, createAgent, type ToolRuntime } from "langchain";
      import { PostgresStore } from "@langchain/langgraph-checkpoint-postgres/store";

      const DB_URI =
        process.env.POSTGRES_URI ??
        "postgresql://postgres:postgres@localhost:5432/postgres?sslmode=disable";
      const store = PostgresStore.fromConnString(DB_URI);
      await store.setup();

      const contextSchema = z.object({ userId: z.string() });

      const UserInfo = z.object({ name: z.string() });

      const saveUserInfo = tool(
        async (
          userInfo: z.infer<typeof UserInfo>,
          runtime: ToolRuntime<unknown, z.infer<typeof contextSchema>>,
        ) => {
          const userId = runtime.context.userId;
          if (!userId) throw new Error("userId is required");
          await runtime.store.put(["users"], userId, userInfo);
          return "Successfully saved user info.";
        },
        { name: "save_user_info", description: "Save user info", schema: UserInfo },
      );

      const agent = createAgent({
        model: "google-genai:gemini-3.5-flash",
        tools: [saveUserInfo],
        contextSchema,
        store,
      });

      await agent.invoke(
        { messages: [{ role: "user", content: "My name is John Smith" }] },
        { context: { userId: "user_123" } },
      );

      const result = await store.get(["users"], "user_123");
      console.log(result?.value);
      ```

      ```ts OpenAI theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import * as z from "zod";
      import { tool, createAgent, type ToolRuntime } from "langchain";
      import { PostgresStore } from "@langchain/langgraph-checkpoint-postgres/store";

      const DB_URI =
        process.env.POSTGRES_URI ??
        "postgresql://postgres:postgres@localhost:5432/postgres?sslmode=disable";
      const store = PostgresStore.fromConnString(DB_URI);
      await store.setup();

      const contextSchema = z.object({ userId: z.string() });

      const UserInfo = z.object({ name: z.string() });

      const saveUserInfo = tool(
        async (
          userInfo: z.infer<typeof UserInfo>,
          runtime: ToolRuntime<unknown, z.infer<typeof contextSchema>>,
        ) => {
          const userId = runtime.context.userId;
          if (!userId) throw new Error("userId is required");
          await runtime.store.put(["users"], userId, userInfo);
          return "Successfully saved user info.";
        },
        { name: "save_user_info", description: "Save user info", schema: UserInfo },
      );

      const agent = createAgent({
        model: "openai:gpt-5.5",
        tools: [saveUserInfo],
        contextSchema,
        store,
      });

      await agent.invoke(
        { messages: [{ role: "user", content: "My name is John Smith" }] },
        { context: { userId: "user_123" } },
      );

      const result = await store.get(["users"], "user_123");
      console.log(result?.value);
      ```

      ```ts Anthropic theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import * as z from "zod";
      import { tool, createAgent, type ToolRuntime } from "langchain";
      import { PostgresStore } from "@langchain/langgraph-checkpoint-postgres/store";

      const DB_URI =
        process.env.POSTGRES_URI ??
        "postgresql://postgres:postgres@localhost:5432/postgres?sslmode=disable";
      const store = PostgresStore.fromConnString(DB_URI);
      await store.setup();

      const contextSchema = z.object({ userId: z.string() });

      const UserInfo = z.object({ name: z.string() });

      const saveUserInfo = tool(
        async (
          userInfo: z.infer<typeof UserInfo>,
          runtime: ToolRuntime<unknown, z.infer<typeof contextSchema>>,
        ) => {
          const userId = runtime.context.userId;
          if (!userId) throw new Error("userId is required");
          await runtime.store.put(["users"], userId, userInfo);
          return "Successfully saved user info.";
        },
        { name: "save_user_info", description: "Save user info", schema: UserInfo },
      );

      const agent = createAgent({
        model: "anthropic:claude-sonnet-4-6",
        tools: [saveUserInfo],
        contextSchema,
        store,
      });

      await agent.invoke(
        { messages: [{ role: "user", content: "My name is John Smith" }] },
        { context: { userId: "user_123" } },
      );

      const result = await store.get(["users"], "user_123");
      console.log(result?.value);
      ```

      ```ts OpenRouter theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import * as z from "zod";
      import { tool, createAgent, type ToolRuntime } from "langchain";
      import { PostgresStore } from "@langchain/langgraph-checkpoint-postgres/store";

      const DB_URI =
        process.env.POSTGRES_URI ??
        "postgresql://postgres:postgres@localhost:5432/postgres?sslmode=disable";
      const store = PostgresStore.fromConnString(DB_URI);
      await store.setup();

      const contextSchema = z.object({ userId: z.string() });

      const UserInfo = z.object({ name: z.string() });

      const saveUserInfo = tool(
        async (
          userInfo: z.infer<typeof UserInfo>,
          runtime: ToolRuntime<unknown, z.infer<typeof contextSchema>>,
        ) => {
          const userId = runtime.context.userId;
          if (!userId) throw new Error("userId is required");
          await runtime.store.put(["users"], userId, userInfo);
          return "Successfully saved user info.";
        },
        { name: "save_user_info", description: "Save user info", schema: UserInfo },
      );

      const agent = createAgent({
        model: "openrouter:anthropic/claude-sonnet-4-6",
        tools: [saveUserInfo],
        contextSchema,
        store,
      });

      await agent.invoke(
        { messages: [{ role: "user", content: "My name is John Smith" }] },
        { context: { userId: "user_123" } },
      );

      const result = await store.get(["users"], "user_123");
      console.log(result?.value);
      ```

      ```ts Fireworks theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import * as z from "zod";
      import { tool, createAgent, type ToolRuntime } from "langchain";
      import { PostgresStore } from "@langchain/langgraph-checkpoint-postgres/store";

      const DB_URI =
        process.env.POSTGRES_URI ??
        "postgresql://postgres:postgres@localhost:5432/postgres?sslmode=disable";
      const store = PostgresStore.fromConnString(DB_URI);
      await store.setup();

      const contextSchema = z.object({ userId: z.string() });

      const UserInfo = z.object({ name: z.string() });

      const saveUserInfo = tool(
        async (
          userInfo: z.infer<typeof UserInfo>,
          runtime: ToolRuntime<unknown, z.infer<typeof contextSchema>>,
        ) => {
          const userId = runtime.context.userId;
          if (!userId) throw new Error("userId is required");
          await runtime.store.put(["users"], userId, userInfo);
          return "Successfully saved user info.";
        },
        { name: "save_user_info", description: "Save user info", schema: UserInfo },
      );

      const agent = createAgent({
        model: "fireworks:accounts/fireworks/models/qwen3p5-397b-a17b",
        tools: [saveUserInfo],
        contextSchema,
        store,
      });

      await agent.invoke(
        { messages: [{ role: "user", content: "My name is John Smith" }] },
        { context: { userId: "user_123" } },
      );

      const result = await store.get(["users"], "user_123");
      console.log(result?.value);
      ```

      ```ts Baseten theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import * as z from "zod";
      import { tool, createAgent, type ToolRuntime } from "langchain";
      import { PostgresStore } from "@langchain/langgraph-checkpoint-postgres/store";

      const DB_URI =
        process.env.POSTGRES_URI ??
        "postgresql://postgres:postgres@localhost:5432/postgres?sslmode=disable";
      const store = PostgresStore.fromConnString(DB_URI);
      await store.setup();

      const contextSchema = z.object({ userId: z.string() });

      const UserInfo = z.object({ name: z.string() });

      const saveUserInfo = tool(
        async (
          userInfo: z.infer<typeof UserInfo>,
          runtime: ToolRuntime<unknown, z.infer<typeof contextSchema>>,
        ) => {
          const userId = runtime.context.userId;
          if (!userId) throw new Error("userId is required");
          await runtime.store.put(["users"], userId, userInfo);
          return "Successfully saved user info.";
        },
        { name: "save_user_info", description: "Save user info", schema: UserInfo },
      );

      const agent = createAgent({
        model: "baseten:zai-org/GLM-5",
        tools: [saveUserInfo],
        contextSchema,
        store,
      });

      await agent.invoke(
        { messages: [{ role: "user", content: "My name is John Smith" }] },
        { context: { userId: "user_123" } },
      );

      const result = await store.get(["users"], "user_123");
      console.log(result?.value);
      ```

      ```ts Ollama theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import * as z from "zod";
      import { tool, createAgent, type ToolRuntime } from "langchain";
      import { PostgresStore } from "@langchain/langgraph-checkpoint-postgres/store";

      const DB_URI =
        process.env.POSTGRES_URI ??
        "postgresql://postgres:postgres@localhost:5432/postgres?sslmode=disable";
      const store = PostgresStore.fromConnString(DB_URI);
      await store.setup();

      const contextSchema = z.object({ userId: z.string() });

      const UserInfo = z.object({ name: z.string() });

      const saveUserInfo = tool(
        async (
          userInfo: z.infer<typeof UserInfo>,
          runtime: ToolRuntime<unknown, z.infer<typeof contextSchema>>,
        ) => {
          const userId = runtime.context.userId;
          if (!userId) throw new Error("userId is required");
          await runtime.store.put(["users"], userId, userInfo);
          return "Successfully saved user info.";
        },
        { name: "save_user_info", description: "Save user info", schema: UserInfo },
      );

      const agent = createAgent({
        model: "ollama:devstral-2",
        tools: [saveUserInfo],
        contextSchema,
        store,
      });

      await agent.invoke(
        { messages: [{ role: "user", content: "My name is John Smith" }] },
        { context: { userId: "user_123" } },
      );

      const result = await store.get(["users"], "user_123");
      console.log(result?.value);
      ```
    </CodeGroup>
  </Tab>
</Tabs>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langchain/long-term-memory.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
