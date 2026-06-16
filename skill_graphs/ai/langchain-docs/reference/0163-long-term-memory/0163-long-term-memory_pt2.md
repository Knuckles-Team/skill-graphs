      import * as z from "zod";
      import { createAgent, tool, type ToolRuntime } from "langchain";
      import { InMemoryStore } from "@langchain/langgraph";

      // InMemoryStore saves data to an in-memory dictionary. Use a DB-backed store in production.
      const store = new InMemoryStore();
      const contextSchema = z.object({
        userId: z.string(),
      });

      // Write sample data to the store using the put method
      await store.put(
        ["users"], // Namespace to group related data together (users namespace for user data)
        "user_123", // Key within the namespace (user ID as key)
        {
          name: "John Smith",
          language: "English",
        }, // Data to store for the given user
      );

      const getUserInfo = tool(
        // Look up user info.
        async (_, runtime: ToolRuntime<unknown, z.infer<typeof contextSchema>>) => {
          // Access the store - same as that provided to `createAgent`
          const userId = runtime.context.userId;
          if (!userId) {
            throw new Error("userId is required");
          }
          // Retrieve data from store - returns StoreValue object with value and metadata
          const userInfo = await runtime.store.get(["users"], userId);
          return userInfo?.value ? JSON.stringify(userInfo.value) : "Unknown user";
        },
        {
          name: "getUserInfo",
          description: "Look up user info by userId from the store.",
          schema: z.object({}),
        },
      );

      const agent = createAgent({
        model: "ollama:devstral-2",
        tools: [getUserInfo],
        contextSchema,
        // Pass store to agent - enables agent to access store when running tools
        store,
      });

      // Run the agent
      const result = await agent.invoke(
        { messages: [{ role: "user", content: "look up user information" }] },
        { context: { userId: "user_123" } },
      );

      console.log(result.messages.at(-1)?.content);

      /**
       * Outputs:
       * User Information:
       * - **Name:** John Smith
       * - **Language:** English
       */
      ```
    </CodeGroup>
  </Tab>

  <Tab title="PostgreSQL">
    <CodeGroup>
      ```ts Google theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import * as z from "zod";
      import { createAgent, tool, type ToolRuntime } from "langchain";
      import { PostgresStore } from "@langchain/langgraph-checkpoint-postgres/store";

      const DB_URI =
        process.env.POSTGRES_URI ??
        "postgresql://postgres:postgres@localhost:5432/postgres?sslmode=disable";
      const store = PostgresStore.fromConnString(DB_URI);
      await store.setup();

      const contextSchema = z.object({ userId: z.string() });

      await store.put(["users"], "user_123", {
        name: "John Smith",
        language: "English",
      });

      const getUserInfo = tool(
        async (_, runtime: ToolRuntime<unknown, z.infer<typeof contextSchema>>) => {
          const userId = runtime.context.userId;
          if (!userId) throw new Error("userId is required");
          const userInfo = await runtime.store.get(["users"], userId);
          return userInfo?.value ? JSON.stringify(userInfo.value) : "Unknown user";
        },
        {
          name: "getUserInfo",
          description: "Look up user info by userId from the store.",
          schema: z.object({}),
        },
      );

      const agent = createAgent({
        model: "google-genai:gemini-3.5-flash",
        tools: [getUserInfo],
        contextSchema,
        store,
      });

      await agent.invoke(
        { messages: [{ role: "user", content: "look up user information" }] },
        { context: { userId: "user_123" } },
      );
      ```

      ```ts OpenAI theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import * as z from "zod";
      import { createAgent, tool, type ToolRuntime } from "langchain";
      import { PostgresStore } from "@langchain/langgraph-checkpoint-postgres/store";

      const DB_URI =
        process.env.POSTGRES_URI ??
        "postgresql://postgres:postgres@localhost:5432/postgres?sslmode=disable";
      const store = PostgresStore.fromConnString(DB_URI);
      await store.setup();

      const contextSchema = z.object({ userId: z.string() });

      await store.put(["users"], "user_123", {
        name: "John Smith",
        language: "English",
      });

      const getUserInfo = tool(
        async (_, runtime: ToolRuntime<unknown, z.infer<typeof contextSchema>>) => {
          const userId = runtime.context.userId;
          if (!userId) throw new Error("userId is required");
          const userInfo = await runtime.store.get(["users"], userId);
          return userInfo?.value ? JSON.stringify(userInfo.value) : "Unknown user";
        },
        {
          name: "getUserInfo",
          description: "Look up user info by userId from the store.",
          schema: z.object({}),
        },
      );

      const agent = createAgent({
        model: "openai:gpt-5.5",
        tools: [getUserInfo],
        contextSchema,
        store,
      });

      await agent.invoke(
        { messages: [{ role: "user", content: "look up user information" }] },
        { context: { userId: "user_123" } },
      );
      ```

      ```ts Anthropic theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import * as z from "zod";
      import { createAgent, tool, type ToolRuntime } from "langchain";
      import { PostgresStore } from "@langchain/langgraph-checkpoint-postgres/store";

      const DB_URI =
        process.env.POSTGRES_URI ??
        "postgresql://postgres:postgres@localhost:5432/postgres?sslmode=disable";
      const store = PostgresStore.fromConnString(DB_URI);
      await store.setup();

      const contextSchema = z.object({ userId: z.string() });

      await store.put(["users"], "user_123", {
        name: "John Smith",
        language: "English",
      });

      const getUserInfo = tool(
        async (_, runtime: ToolRuntime<unknown, z.infer<typeof contextSchema>>) => {
          const userId = runtime.context.userId;
          if (!userId) throw new Error("userId is required");
          const userInfo = await runtime.store.get(["users"], userId);
          return userInfo?.value ? JSON.stringify(userInfo.value) : "Unknown user";
        },
        {
          name: "getUserInfo",
          description: "Look up user info by userId from the store.",
          schema: z.object({}),
        },
      );

      const agent = createAgent({
        model: "anthropic:claude-sonnet-4-6",
        tools: [getUserInfo],
        contextSchema,
        store,
      });

      await agent.invoke(
        { messages: [{ role: "user", content: "look up user information" }] },
        { context: { userId: "user_123" } },
      );
      ```

      ```ts OpenRouter theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import * as z from "zod";
      import { createAgent, tool, type ToolRuntime } from "langchain";
      import { PostgresStore } from "@langchain/langgraph-checkpoint-postgres/store";

      const DB_URI =
        process.env.POSTGRES_URI ??
        "postgresql://postgres:postgres@localhost:5432/postgres?sslmode=disable";
      const store = PostgresStore.fromConnString(DB_URI);
      await store.setup();

      const contextSchema = z.object({ userId: z.string() });

      await store.put(["users"], "user_123", {
        name: "John Smith",
        language: "English",
      });

      const getUserInfo = tool(
        async (_, runtime: ToolRuntime<unknown, z.infer<typeof contextSchema>>) => {
          const userId = runtime.context.userId;
          if (!userId) throw new Error("userId is required");
          const userInfo = await runtime.store.get(["users"], userId);
          return userInfo?.value ? JSON.stringify(userInfo.value) : "Unknown user";
        },
        {
          name: "getUserInfo",
          description: "Look up user info by userId from the store.",
          schema: z.object({}),
        },
      );

      const agent = createAgent({
        model: "openrouter:anthropic/claude-sonnet-4-6",
        tools: [getUserInfo],
        contextSchema,
        store,
      });

      await agent.invoke(
        { messages: [{ role: "user", content: "look up user information" }] },
        { context: { userId: "user_123" } },
      );
      ```

      ```ts Fireworks theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import * as z from "zod";
      import { createAgent, tool, type ToolRuntime } from "langchain";
      import { PostgresStore } from "@langchain/langgraph-checkpoint-postgres/store";

      const DB_URI =
        process.env.POSTGRES_URI ??
        "postgresql://postgres:postgres@localhost:5432/postgres?sslmode=disable";
      const store = PostgresStore.fromConnString(DB_URI);
      await store.setup();

      const contextSchema = z.object({ userId: z.string() });

      await store.put(["users"], "user_123", {
        name: "John Smith",
        language: "English",
      });

      const getUserInfo = tool(
        async (_, runtime: ToolRuntime<unknown, z.infer<typeof contextSchema>>) => {
          const userId = runtime.context.userId;
          if (!userId) throw new Error("userId is required");
          const userInfo = await runtime.store.get(["users"], userId);
          return userInfo?.value ? JSON.stringify(userInfo.value) : "Unknown user";
        },
        {
          name: "getUserInfo",
          description: "Look up user info by userId from the store.",
          schema: z.object({}),
        },
      );

      const agent = createAgent({
        model: "fireworks:accounts/fireworks/models/qwen3p5-397b-a17b",
        tools: [getUserInfo],
        contextSchema,
        store,
      });

      await agent.invoke(
        { messages: [{ role: "user", content: "look up user information" }] },
        { context: { userId: "user_123" } },
      );
      ```

      ```ts Baseten theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import * as z from "zod";
      import { createAgent, tool, type ToolRuntime } from "langchain";
      import { PostgresStore } from "@langchain/langgraph-checkpoint-postgres/store";

      const DB_URI =
        process.env.POSTGRES_URI ??
        "postgresql://postgres:postgres@localhost:5432/postgres?sslmode=disable";
      const store = PostgresStore.fromConnString(DB_URI);
      await store.setup();

      const contextSchema = z.object({ userId: z.string() });

      await store.put(["users"], "user_123", {
        name: "John Smith",
        language: "English",
      });

      const getUserInfo = tool(
        async (_, runtime: ToolRuntime<unknown, z.infer<typeof contextSchema>>) => {
          const userId = runtime.context.userId;
          if (!userId) throw new Error("userId is required");
          const userInfo = await runtime.store.get(["users"], userId);
          return userInfo?.value ? JSON.stringify(userInfo.value) : "Unknown user";
        },
        {
          name: "getUserInfo",
          description: "Look up user info by userId from the store.",
          schema: z.object({}),
        },
      );

      const agent = createAgent({
        model: "baseten:zai-org/GLM-5",
        tools: [getUserInfo],
        contextSchema,
        store,
      });

      await agent.invoke(
        { messages: [{ role: "user", content: "look up user information" }] },
        { context: { userId: "user_123" } },
      );
      ```

      ```ts Ollama theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import * as z from "zod";
      import { createAgent, tool, type ToolRuntime } from "langchain";
      import { PostgresStore } from "@langchain/langgraph-checkpoint-postgres/store";

      const DB_URI =
        process.env.POSTGRES_URI ??
        "postgresql://postgres:postgres@localhost:5432/postgres?sslmode=disable";
      const store = PostgresStore.fromConnString(DB_URI);
      await store.setup();

      const contextSchema = z.object({ userId: z.string() });

      await store.put(["users"], "user_123", {
        name: "John Smith",
        language: "English",
      });

      const getUserInfo = tool(
        async (_, runtime: ToolRuntime<unknown, z.infer<typeof contextSchema>>) => {
          const userId = runtime.context.userId;
          if (!userId) throw new Error("userId is required");
          const userInfo = await runtime.store.get(["users"], userId);
          return userInfo?.value ? JSON.stringify(userInfo.value) : "Unknown user";
        },
        {
          name: "getUserInfo",
          description: "Look up user info by userId from the store.",
          schema: z.object({}),
        },
      );

      const agent = createAgent({
        model: "ollama:devstral-2",
        tools: [getUserInfo],
        contextSchema,
        store,
      });

      await agent.invoke(
        { messages: [{ role: "user", content: "look up user information" }] },
        { context: { userId: "user_123" } },
      );
      ```
    </CodeGroup>
  </Tab>
</Tabs>

<a />

## Write long-term memory from tools

<Tabs>
  <Tab title="InMemoryStore">
    <CodeGroup>
      ```ts Google theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import * as z from "zod";
      import { tool, createAgent, type ToolRuntime } from "langchain";
      import { InMemoryStore } from "@langchain/langgraph";

      // InMemoryStore saves data to an in-memory dictionary. Use a DB-backed store in production.
      const store = new InMemoryStore();

      const contextSchema = z.object({
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
        model: "google-genai:gemini-3.5-flash",
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

      ```ts OpenAI theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import * as z from "zod";
      import { tool, createAgent, type ToolRuntime } from "langchain";
      import { InMemoryStore } from "@langchain/langgraph";

      // InMemoryStore saves data to an in-memory dictionary. Use a DB-backed store in production.
      const store = new InMemoryStore();

      const contextSchema = z.object({
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
        model: "openai:gpt-5.5",
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

      ```ts Anthropic theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import * as z from "zod";
      import { tool, createAgent, type ToolRuntime } from "langchain";
      import { InMemoryStore } from "@langchain/langgraph";

      // InMemoryStore saves data to an in-memory dictionary. Use a DB-backed store in production.
      const store = new InMemoryStore();

      const contextSchema = z.object({
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
        model: "anthropic:claude-sonnet-4-6",
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

      ```ts OpenRouter theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import * as z from "zod";
      import { tool, createAgent, type ToolRuntime } from "langchain";
      import { InMemoryStore } from "@langchain/langgraph";

      // InMemoryStore saves data to an in-memory dictionary. Use a DB-backed store in production.
      const store = new InMemoryStore();

      const contextSchema = z.object({
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
        model: "openrouter:anthropic/claude-sonnet-4-6",
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

      ```ts Fireworks theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import * as z from "zod";
      import { tool, createAgent, type ToolRuntime } from "langchain";
      import { InMemoryStore } from "@langchain/langgraph";

      // InMemoryStore saves data to an in-memory dictionary. Use a DB-backed store in production.
      const store = new InMemoryStore();

      const contextSchema = z.object({
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
        model: "fireworks:accounts/fireworks/models/qwen3p5-397b-a17b",
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

      ```ts Baseten theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import * as z from "zod";
      import { tool, createAgent, type ToolRuntime } from "langchain";
      import { InMemoryStore } from "@langchain/langgraph";

      // InMemoryStore saves data to an in-memory dictionary. Use a DB-backed store in production.
      const store = new InMemoryStore();

      const contextSchema = z.object({
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
        model: "baseten:zai-org/GLM-5",
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

      ```ts Ollama theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import * as z from "zod";
      import { tool, createAgent, type ToolRuntime } from "langchain";
      import { InMemoryStore } from "@langchain/langgraph";

      // InMemoryStore saves data to an in-memory dictionary. Use a DB-backed store in production.
      const store = new InMemoryStore();

      const contextSchema = z.object({
