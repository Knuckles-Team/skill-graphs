# Prompt engineering quickstart
Source: https://docs.langchain.com/langsmith/prompt-engineering-quickstart

Prompts guide the behavior of Large Language Models (LLM). [*Prompt engineering*](/langsmith/prompt-engineering-concepts) is the process of crafting, testing, and refining the instructions you give to an LLM so it produces reliable and useful responses.

LangSmith provides tools to create, version, test, and collaborate on prompts. You’ll also encounter common concepts like [*prompt templates*](/langsmith/prompt-engineering-concepts#prompts-vs-prompt-templates), which let you reuse structured prompts, and [*variables*](/langsmith/prompt-engineering-concepts#f-string-vs-mustache), which allow you to dynamically insert values (such as a user’s question) into a prompt.

In this quickstart, you’ll create, test, and improve prompts using either the UI or the SDK. This quickstart will use OpenAI as the example LLM provider, but the same workflow applies across other providers.

## Prerequisites

Before you begin, make sure you have:

* **A LangSmith account**: Sign up or log in at [smith.langchain.com](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-prompt-engineering-quickstart).
* **A LangSmith API key**: Follow the [Create an API key](/langsmith/create-account-api-key) guide.
* **An OpenAI API key**: Generate this from the [OpenAI dashboard](https://platform.openai.com/account/api-keys).

Select the tab for UI or SDK workflows:

<Tabs>
  <Tab title="UI" icon="window">
    ## 1. Set workspace secret

    In the [LangSmith UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=snippets-langsmith-set-workspace-secrets), ensure that your API key is set as a [workspace secret](/langsmith/set-up-hierarchy#configure-workspace-settings).

    1. Navigate to <Icon icon="settings" /> **Settings** and then move to the **Secrets** tab.
    2. Select **Add secret** and enter the key environment variable (e.g.,`OPENAI_API_KEY` or `ANTHROPIC_API_KEY`) and your API key as the **Value**.
    3. Select **Save secret**.

    <Note> When adding workspace secrets in the LangSmith UI, make sure the secret keys match the environment variable names expected by your model provider.</Note>

    ## 2. Create a prompt

    1. In the [LangSmith UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-prompt-engineering-quickstart), navigate to the **Prompts** section in the left-hand menu.
    2. Click on **+ Prompt** to create a prompt.
    3. Modify the prompt by editing or adding prompts and input variables as needed.

    <div>
      <img alt="Playground with the system prompt ready for editing." />

      <img alt="Playground with the system prompt ready for editing." />
    </div>

    ## 3. Test a prompt

    1. Under the **Prompts** heading select the gear <Icon icon="settings" /> icon next to the model name, which will launch the **Prompt Settings** window on the **Model Configuration** tab.

    2. Set the [model configuration](/langsmith/managing-model-configurations) you want to use. The **Provider** and **Model** you select will determine the parameters that are configurable on this configuration page. Once set, click **Save as**.

       <div>
         <img alt="Model Configuration window in the LangSmith UI, settings for Provider, Model, Temperature, Max Output Tokens, Top P, Presence Penalty, Frequency Penalty, Reasoning Effort, etc." />

         <img alt="Model Configuration window in the LangSmith UI, settings for Provider, Model, Temperature, Max Output Tokens, Top P, Presence Penalty, Frequency Penalty, Reasoning Effort, etc." />
       </div>

    3. Specify the input variables you would like to test in the **Inputs** box and then click <Icon icon="player-play" /> **Start**.

       <div>
         <img alt="The input box with a question entered. The output box contains the response to the prompt." />

         <img alt="The input box with a question entered. The output box contains the response to the prompt." />
       </div>

       To learn about more options for configuring your prompt in the Playground, refer to [Configure prompt settings](/langsmith/managing-model-configurations).

    4. After testing and refining your prompt, click **Save** to store it for future use.

    ## 4. Iterate on a prompt

    LangSmith allows for team-based prompt iteration. [Workspace](/langsmith/administration-overview#workspaces) members can experiment with prompts in the Playground and save their changes as a new [*commit*](/langsmith/prompt-engineering-concepts#commits) when ready.

    To improve your prompts:

    * Reference the documentation provided by your model provider for best practices in prompt creation, such as:
      * [Best practices for prompt engineering with the OpenAI API](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-the-openai-api)
      * [Gemini's Introduction to prompt design](https://ai.google.dev/gemini-api/docs/prompting-intro)
    * Build and refine your prompts with the Prompt Canvas—an interactive tool in LangSmith. Learn more in the [Prompt Canvas guide](/langsmith/write-prompt-with-ai).
    * Tag specific commits to mark important moments in your commit history.
      1. To create a commit, navigate to the **Playground** and select **Commit**. Choose the prompt to commit changes to and then **Commit**.
      2. Navigate to **Prompts** in the left-hand menu. Select the prompt. On the prompt detail page, select **Tag** on the top right to add a [commit tag](/langsmith/manage-prompts#commit-tags).
  </Tab>

  <Tab title="SDK" icon="code">
    ## 1. Set up your environment

    1. In your terminal, prepare your environment:

       <CodeGroup>
         ```bash Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
         mkdir ls-prompt-quickstart && cd ls-prompt-quickstart
         python -m venv .venv
         source .venv/bin/activate
         pip install -qU langsmith openai langchain_core
         ```

         ```bash TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
         mkdir ls-prompt-quickstart-ts && cd ls-prompt-quickstart-ts
         npm init -y
         npm install langsmith openai typescript ts-node
         npx tsc --init
         ```
       </CodeGroup>

    2. Set your API keys:

       ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
       export LANGSMITH_API_KEY='<your_api_key>'
       export OPENAI_API_KEY='<your_api_key>'
       ```

    ## 2. Create a prompt

    To create a prompt, you'll define a list of messages that you want in your prompt and then push to LangSmith.

    Use the language-specific constructor and push method:

    * Python: [`ChatPromptTemplate`](https://reference.langchain.com/python/langchain-core/prompts/chat/ChatPromptTemplate) → [`client.push_prompt(...)`](https://docs.smith.langchain.com/reference/python/client/langsmith.client.Client#langsmith.client.Client.push_prompt)
    * TypeScript: [`ChatPromptTemplate.fromMessages(...)`](https://reference.langchain.com/javascript/langchain-core/prompts/ChatPromptTemplate) → [`client.pushPrompt(...)`](https://reference.langchain.com/javascript/langsmith/client/Client/pushPrompt)

    1. Add the following code to a `create_prompt` file:

       <CodeGroup>
         ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
         from langsmith import Client
         from langchain_core.prompts import ChatPromptTemplate

         client = Client()

         prompt = ChatPromptTemplate([
             ("system", "You are a helpful chatbot."),
             ("user", "{question}"),
         ])

         client.push_prompt("prompt-quickstart", object=prompt)
         ```

         ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
         import { Client } from "langsmith";
         import { ChatPromptTemplate } from "@langchain/core/prompts";

         const client = new Client();

         const prompt = ChatPromptTemplate.fromMessages([
         ["system", "You are a helpful chatbot."],
         ["user", "{question}"],
         ]);

         await client.pushPrompt("prompt-quickstart", {
         object: prompt,
         });
         ```
       </CodeGroup>

       This creates an ordered list of messages, wraps them in `ChatPromptTemplate`, and then pushes the prompt by name to your [workspace](/langsmith/administration-overview#workspaces) for versioning and reuse.

    2. Run `create_prompt`:

       <CodeGroup>
         ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
         python create_prompt.py
         ```

         ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
         npx tsx create_prompt.ts
         ```
       </CodeGroup>

    Follow the resulting link to view the newly created Prompt Hub prompt in the LangSmith UI.

    ## 3. Test a prompt

    In this step, you'll pull the prompt you created in [step 2](#2-create-a-prompt) by name (`"prompt-quickstart"`), format it with a test input, convert it to OpenAI’s chat format, and call the OpenAI Chat Completions API.

    Then, you'll iterate on the prompt by creating a new version. Members of your workspace can open an existing prompt, experiment with changes in the [UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-prompt-engineering-quickstart), and save those changes as a new commit on the same prompt, which preserves history for the whole team.

    1. Add the following to a `test_prompt` file:

       <CodeGroup>
         ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
         from langsmith import Client
         from openai import OpenAI
         from langchain_core.messages import convert_to_openai_messages

         client = Client()
         oai_client = OpenAI()

         prompt = client.pull_prompt("prompt-quickstart")

         # Since the prompt only has one variable you could also pass in the value directly
         # Equivalent to formatted_prompt = prompt.invoke("What is the color of the sky?")
         formatted_prompt = prompt.invoke({"question": "What is the color of the sky?"})

         response = oai_client.chat.completions.create(
             model="gpt-5.5",
             messages=convert_to_openai_messages(formatted_prompt.messages),
         )
         ```

         ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
         import { OpenAI } from "openai";
         import { pull } from "langchain/hub"
         import { convertPromptToOpenAI } from "@langchain/openai";

         const oaiClient = new OpenAI();

         const prompt = await pull("prompt-quickstart");

         // Format the prompt with the question
         const formattedPrompt = await prompt.invoke({ question: "What is the color of the sky?" });

         const response = await oaiClient.chat.completions.create({
             model: "gpt-5.5",
             messages: convertPromptToOpenAI(formattedPrompt).messages,
         });
         ```
       </CodeGroup>

       This loads the prompt by name using `pull` for the latest committed version of the prompt that you're testing. You can also specify a specific commit by passing the commit hash `"<prompt-name>:<commit-hash>"`

    2. Run `test_prompt` :

       <CodeGroup>
         ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
         python test_prompt.py
         ```

         ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
         npx tsx test_prompt.ts
         ```
       </CodeGroup>

    3. To create a new version of a prompt, call the same push method you used initially with the same prompt name and your updated template. LangSmith will record it as a new commit and preserve prior versions.

       Copy the following code to an `iterate_prompt` file:

       <CodeGroup>
         ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
         from langsmith import Client
         from langchain_core.prompts import ChatPromptTemplate

         client = Client()

         new_prompt = ChatPromptTemplate([
             ("system", "You are a helpful chatbot. Respond in Spanish."),
             ("user", "{question}"),
         ])

         client.push_prompt("prompt-quickstart", object=new_prompt)
         ```

         ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
         import { Client } from "langsmith";
         import { ChatPromptTemplate } from "@langchain/core/prompts";

         const client = new Client();

         const newPrompt = ChatPromptTemplate.fromMessages([
             ["system", "You are a helpful chatbot. Speak in Spanish."],
             ["user", "{question}"]
         ]);

         await client.pushPrompt("prompt-quickstart", {
             object: newPrompt
         });
         ```
       </CodeGroup>

    4. Run `iterate_prompt` :

       <CodeGroup>
         ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
         python iterate_prompt.py
         ```

         ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
         npx tsx iterate_prompt.ts
         ```
       </CodeGroup>

       Now your prompt will contain two commits.

    To improve your prompts:

    * Reference the documentation provided by your model provider for best practices in prompt creation, such as:
      * [Best practices for prompt engineering with the OpenAI API](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-the-openai-api)
      * [Gemini's Introduction to prompt design](https://ai.google.dev/gemini-api/docs/prompting-intro)
    * Build and refine your prompts with the Prompt Canvas—an interactive tool in LangSmith. Learn more in the [Prompt Canvas guide](/langsmith/write-prompt-with-ai).
  </Tab>
</Tabs>

## Next steps

* Learn more about how to store and manage prompts using the Prompt Hub in the [Create a prompt guide](/langsmith/create-a-prompt).
* Learn how to set up the Playground to [Test multi-turn conversations](/langsmith/multiple-messages) in this tutorial.
* Learn how to test your prompt's performance over a dataset instead of individual examples, refer to [Run an evaluation from the Playground](/langsmith/run-evaluation-from-playground).

<Callout type="info" icon="feather">
  Use the **[Chat](/langsmith/chat)** in the Playground to help optimize your prompts, generate tools, and create output schemas.
</Callout>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/prompt-engineering-quickstart.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Prompt template format guide
Source: https://docs.langchain.com/langsmith/prompt-template-format

This page describes the [prompt template](/langsmith/prompt-engineering-concepts#prompts-vs-prompt-templates) formats supported in the [Playground](/langsmith/prompt-engineering-concepts#playground), [prompt hub](/langsmith/manage-prompts#public-prompt-hub), and [evaluators](/langsmith/evaluation-concepts#evaluators). Prompt templates allow you to create reusable prompts with dynamic placeholders that get filled in at runtime.

<Tip>
  For a general overview of prompt engineering and prompt templates, refer to the [Concepts](/langsmith/prompt-engineering-concepts#prompts-vs-prompt-templates) page.
</Tip>

LangSmith supports two prompt template formats, which work for different levels of complexity:

| Format       | Syntax         | Best for                                                             |
| ------------ | -------------- | -------------------------------------------------------------------- |
| **f-string** | `{variable}`   | Simple prompts with basic variable substitution                      |
| **mustache** | `{{variable}}` | Complex prompts with loops, conditionals, nested data, or evaluators |

[F-string syntax](#f-string-syntax) is ideal for straightforward prompts. [Mustache](#mustache-syntax) provides features for handling complex data structures and logic, which is helpful for evaluators and advanced use cases.

You can switch between formats in the [UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-prompt-template-format). LangSmith will automatically [convert your template](#conversion-between-formats) when possible, though some mustache features (like loops and conditionals) cannot be converted to f-string format.

<Callout icon="test-pipe">
  Use the [Playground](https://smith.langchain.com/playground) to test out the examples on this page. Switch the **Prompt format** under the prompt settings <Icon icon="settings" /> menu in the Playground.
</Callout>

## F-string syntax

F-string templates use Python-style formatting with single curly braces `{variable}`. LangSmith uses a [simplified subset](#limitations) of Python's [f-string syntax](https://realpython.com/python-f-strings/): it only supports basic variable substitution, not the full range of Python expressions and formatting options. When you have a flat data structure and only need to insert values into your prompt, f-strings are ideal.

### Basic variables

Variables are replaced with their values from the input data. Variable names must match exactly (case-sensitive):

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}

# Template
Hello, {name}! Welcome to {company}.

# Input
{
  "name": "Ashley",
  "company": "LangChain"
}

# Output
Hello, Ashley! Welcome to LangChain.
```

When the template runs, LangSmith looks up each variable name in the input object and replaces `{name}` with the value of the `name` key.

### Variable names

F-string variable names are treated as simple string identifiers. They cannot contain dots, brackets, or special characters—just alphanumeric characters and underscores.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}

# Template
Hello, {name}!
Your topic is: {topic}

# Input
{
  "name": "Ashley",
  "topic": "LangSmith"
}

# Output
Hello, Ashley!
Your topic is: LangSmith
```

If your input has nested objects like `{"user": {"name": "Ashley"}}`, you **cannot** access the nested value with `{user.name}` in f-string format. The dot would be treated as part of the variable name (literally looking for a key called `"user.name"`), not as a path separator. For nested access, use [mustache format](#mustache-syntax) instead.

### Literal braces

Sometimes you need to include actual curly braces in your output (for example, in JSON examples or code snippets). To do this, **double the braces**:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}

# Template
Use double braces for literals: {{not_a_variable}}
But single braces for variables: {variable}

# Input
{
  "variable": "value"
}

# Output
Use double braces for literals: {not_a_variable}
But single braces for variables: value
```

The template parser recognizes `{{` as an escaped brace, not a variable placeholder. Only single braces `{...}` are treated as variables.

### Limitations

LangSmith's f-string implementation is limited to keep templates simple and predictable. The following features are **not supported**:

* **Dot notation for nested access:** Cannot use `{user.name}` to access nested objects. The entire string `"user.name"` would be treated as a single variable name.
* **Format specifiers:** Cannot use `{price:.2f}` for number formatting or `{rate:.1%}` for percentages.
* **Expressions:** Cannot use `{x + y}`, `{len(items)}`, or `{value if condition else default}`.
* **Function calls:** Cannot use `{str.upper()}` or other method calls.
* **Loops or conditionals:** No control flow structures.
* **Array indexing:** Cannot use `{items[0]}` to access array elements.

For any of these advanced features, **use mustache format instead**.

## Mustache syntax

[Mustache](https://mustache.github.io/mustache.5.html) is a "logic-less" templating language, meaning it doesn't allow arbitrary code execution but does provide structured control flow through sections. It's called "logic-less" because you can't write complex expressions—instead, you structure your data to control what renders.

Mustache is designed for complex data structures and dynamic rendering. It's essential for:

* **Evaluators:** Processing thread histories and conversation context.
* **Few-shot prompting:** Iterating over example lists.
* **Nested data:** Accessing deeply nested objects and arrays.
* **Conditional content:** Showing different text based on data presence.

The double-brace syntax `{{variable}}` distinguishes it from f-strings.

### Basic variables

Like f-strings, mustache replaces variables with their values:

```mustache theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{{!-- Template --}}
Hello, {{name}}! Welcome to {{company}}.

{{!-- Input --}}
{
  "name": "Ashley",
  "company": "LangChain"
}

{{!-- Output --}}
Hello, Ashley! Welcome to LangChain.
```

<Note>
  `{{!-- ... --}}` is a mustache comment and won't appear in the output. Refer to the [Comments](#comments) section.
</Note>

### Nested object access

You can traverse nested objects using dot notation:

```mustache theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{{!-- Template --}}
User: {{user.name}}
Email: {{user.profile.email}}

{{!-- Input --}}
{
  "user": {
    "name": "Billy",
    "profile": {
      "email": "billy@example.com"
    }
  }
}

{{!-- Output --}}
User: Billy
Email: billy@example.com
```

The template engine follows the path `user` → `profile` → `email` through your data structure. Each dot represents one level of nesting.

Real-world data is often nested (for example: API responses, database records, etc.). Mustache lets you work with this data naturally without flattening it first.

### Sections

Sections are mustache's core feature. A section starts with `{{#name}}` and ends with `{{/name}}`. What happens inside depends on the value:

* **Array:** Repeats the content for each element.
* **Object:** Renders once with that object as context.
* **Truthy value:** Renders once.
* **Falsy value (false, null, undefined, empty array):** Doesn't render.

In the following example, the section `{{#items}}` iterates over the `items` array. For each iteration, the variables inside the section (like `{{name}}` and `{{price}}`) are resolved against the current array element:

```mustache theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{{!-- Template --}}
Shopping List:
{{#items}}
  - {{name}}: ${{price}}
{{/items}}

{{!-- Input --}}
{
  "items": [
    {"name": "Apple", "price": "1.50"},
    {"name": "Banana", "price": "0.75"},
    {"name": "Orange", "price": "2.00"}
  ]
}

{{!-- Output --}}
Shopping List:
  - Apple: $1.50
  - Banana: $0.75
  - Orange: $2.00
```

Sections eliminate the need to manually construct repetitive text. In evaluators, you'll use sections to iterate over conversation messages or [few-shot examples](#few-shot-examples).

For deeply nested hierarchical data, you can nest multiple sections to handle complex structures with multiple levels of arrays and objects:

```mustache theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{{!-- Template --}}
{{#company}}
Company: {{name}}
{{#departments}}
  Department: {{dept_name}}
  {{#employees}}
    - {{employee_name}} ({{role}})
  {{/employees}}
{{/departments}}
{{/company}}

{{!-- Input --}}
{
  "company": {
    "name": "TechCorp",
    "departments": [
      {
        "dept_name": "Engineering",
        "employees": [
          {"employee_name": "Ashley", "role": "Senior Engineer"},
          {"employee_name": "Billy", "role": "Engineer"}
        ]
      },
      {
        "dept_name": "Sales",
        "employees": [
          {"employee_name": "Carol", "role": "Sales Manager"}
        ]
      }
    ]
  }
}

{{!-- Output --}}
Company: TechCorp
  Department: Engineering
    - Ashley (Senior Engineer)
    - Billy (Engineer)
  Department: Sales
    - Carol (Sales Manager)
```

<Tip>
  You can create a structure as deep as you need, but consider flattening very deep structures before templating for readability. This approach is useful for nested categories, conversation threads with metadata, or any hierarchical data representation.
</Tip>

### Nested loops

You can nest sections to handle multi-level data structures:

```mustache theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{{!-- Template --}}
{{#categories}}
Category: {{name}}
{{#products}}
  - {{title}} ({{price}})
{{/products}}
{{/categories}}

{{!-- Input --}}
{
  "categories": [
    {
      "name": "Fruits",
      "products": [
        {"title": "Apple", "price": "$1.50"},
        {"title": "Banana", "price": "$0.75"}
      ]
    },
    {
      "name": "Vegetables",
      "products": [
        {"title": "Carrot", "price": "$0.50"},
        {"title": "Lettuce", "price": "$1.25"}
      ]
    }
  ]
}

{{!-- Output --}}
Category: Fruits
  - Apple ($1.50)
  - Banana ($0.75)
Category: Vegetables
  - Carrot ($0.50)
  - Lettuce ($1.25)
```

The outer section `{{#categories}}` sets the context to each category object. Inside that context, `{{name}}` refers to the category name, and the inner section `{{#products}}` iterates over that category's products.

Use nested loops when your data has hierarchical relationships—categories with products, departments with employees, or conversation threads with multiple exchanges.

### Array elements by index

Sometimes you need a specific element rather than looping. Use dot notation with numeric indices:

```mustache theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{{!-- Template --}}
First item: {{items.0}}
Second item: {{items.1}}
Last item: {{items.2}}

{{!-- Input --}}
{
  "items": ["Apple", "Banana", "Orange"]
}

{{!-- Output --}}
First item: Apple
Second item: Banana
Last item: Orange
```

You must know the index when you're writing the template.

Evaluators often need the first user message or last AI response from a conversation thread. Use `{{all_messages.0}}` for the first message or pre-calculate the last message in your data.

### Conditionals

You can use sections as conditionals. They only render if the value exists, is non-empty, and is not `false`:

```mustache theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{{!-- Template --}}
{{#user}}
Welcome back, {{name}}!
{{/user}}

{{!-- Input (user exists) --}}
{
  "user": {
    "name": "Ashley"
  }
}

{{!-- Output --}}
Welcome back, Ashley!

{{!-- Input (no user) --}}
{}

{{!-- Output --}}
(empty - section doesn't render)
```

The section `{{#user}}` checks if `user` exists and is truthy. If so, it renders the content inside with `user` as the context (so `{{name}}` looks for `name` inside `user`).

Show optional content like "Welcome back" messages only when user data is available, or display error messages only when errors exist.

### Inverted sections

Inverted sections render only when a value doesn’t exist, is false, null, undefined, or an empty array. Inverted sections are commonly used to handle empty states, such as missing data or empty lists.

In the following example:

* `{{#results}}` iterates over each result and renders one line per item.
* `{{^results}}` renders only when the results array is empty or missing.
* The inverted section provides a clear fallback when there are no results to display.

```mustache theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{{!-- Template --}}
Search results for "{{query}}":

{{#results}}
  - {{title}} ({{year}})
{{/results}}

{{^results}}
No results found. Try a different search term.
{{/results}}

{{!-- Input (with results)--}}
{
  "query": "matrix",
  "results": [
    {"title": "The Matrix", "year": 1999},
    {"title": "The Matrix Reloaded", "year": 2003}
  ]
}

{{!-- Output --}}
Search results for "matrix":

  - The Matrix (1999)
  - The Matrix Reloaded (2003)

{{!-- Input (no results) --}}
{
    "query": "asdlkjasd",
    "results": []
}

{{!-- Output --}}
Search results for "asdlkjasd":

No results found. Try a different search term.
```

You can also combine regular and inverted sections to create if/else logic, providing default values when variables are missing.

The regular section `{{#username}}` renders only if `username` exists. The inverted section `{{^username}}` renders only if it doesn't. Together, they create an if/else branch. This is useful for personalizing prompts when user data is optional or showing default instructions when custom ones aren't provided:

```mustache theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{{!-- Template --}}
{{#username}}
Hello, {{username}}!
{{/username}}
{{^username}}
Hello, Guest!
{{/username}}

{{!-- Input (with username) --}}
{"username": "Ashley"}
{{!-- Output: Hello, Ashley! --}}

{{!-- Input (no username) --}}
{}
{{!-- Output: Hello, Guest! --}}
```

This pattern extends to boolean flags, allowing you to change output formatting based on data conditions:

```mustache theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{{!-- Template --}}
Status: {{status}}
{{#is_urgent}}
⚠️ URGENT - Immediate attention required!
{{/is_urgent}}
{{^is_urgent}}
Standard priority
{{/is_urgent}}

{{!-- Input --}}
{
  "status": "Open",
  "is_urgent": true
}

{{!-- Output --}}
Status: Open
⚠️ URGENT - Immediate attention required!
```

Use boolean flags in your data to control which content blocks render. This keeps formatting logic out of your application code and in the template instead. This approach is useful for highlighting important information, adjusting tone based on context (formal vs. casual), or showing different instructions for different user types.

### Comments

Comments document your templates without affecting output. Use `{{! comment }}` or `{{!-- comment --}}`:

```mustache theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{{!-- Template --}}
Hello, {{name}}!
{{! This is a comment and won't appear in output }}
Welcome to our service.

{{!-- Input --}}
{
  "name": "Ashley"
}

{{!-- Output --}}
Hello, Ashley!
Welcome to our service.
```

Use comments to explain complex sections, document expected data structures, or note why certain logic exists. This helps collaborators understand your templates.

## Special variables for evaluators and threads

When building [evaluators](/langsmith/evaluation-concepts#evaluators) or working with conversational AI, LangSmith automatically provides special variables that structure conversation data in useful ways. These variables are **only available in evaluator contexts**, not in regular Playground prompts.

Evaluators need to analyze conversations holistically—looking at patterns across multiple messages, comparing the first question to the final answer, or examining how well the AI responds to follow-up questions. These variables make it easy to access conversation structure without manual data manipulation.

### Thread message variables

LangSmith provides three pre-structured views of conversation [threads](/langsmith/evaluation-concepts#threads):

```mustache theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{{!-- Access all messages in the thread --}}
{{#all_messages}}
{{role}}: {{content}}
{{/all_messages}}

{{!-- Access human-AI message pairs --}}
{{#human_ai_pairs}}
Human: {{human}}
AI: {{ai}}
{{/human_ai_pairs}}

{{!-- Access first human and last AI message --}}
{{#first_human_last_ai}}
Original question: {{first_human}}
Final answer: {{last_ai}}
{{/first_human_last_ai}}

{{!-- Access specific message by index --}}
First message: {{all_messages.0}}
Second message: {{all_messages.1}}
```

* **`all_messages`**: Every message in chronological order with `role` (user/assistant/system) and `content` fields. Use this to show the full conversation flow.
* **`human_ai_pairs`**: Messages grouped into question-answer pairs. Each pair has `human` (user message) and `ai` (assistant response). Use this when evaluating response quality.
* **`first_human_last_ai`**: Just the initial question (`first_human`) and final answer (`last_ai`). Use this to check if the AI ultimately answered the original question, ignoring the middle conversation.

### Example with thread context

The following example is a practical evaluator prompt that uses thread context:

```mustache theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{{!-- Template --}}
Evaluate this conversation:

{{#all_messages}}
{{role}}: {{content}}
{{/all_messages}}

Was the AI helpful? Rate from 1-5.

{{!-- Input (provided by LangSmith) --}}
{
  "all_messages": [
    {"role": "user", "content": "What's the weather?"},
    {"role": "assistant", "content": "I don't have access to weather data."},
    {"role": "user", "content": "Can you tell me a joke instead?"},
    {"role": "assistant", "content": "Why did the chicken cross the road?"}
  ]
}

{{!-- Output --}}
Evaluate this conversation:

user: What's the weather?
assistant: I don't have access to weather data.
user: Can you tell me a joke instead?
assistant: Why did the chicken cross the road?

Was the AI helpful? Rate from 1-5.
```

The template uses the mustache section `{{#all_messages}}` to loop over the conversation array. For each iteration, the section sets the context to that message object, so `{{role}}` and `{{content}}` access the properties of the current message. The loop automatically iterates through all four messages in order, displaying each as `"role: content"`. This gives the evaluator LLM the full conversation history to assess helpfulness.

When you create an evaluator in LangSmith, select which thread variables you want to include. LangSmith will automatically populate them from the conversation being evaluated.

## Few-shot examples

Few-shot prompting teaches the LLM by example. You provide several input-output pairs demonstrating the task, then ask it to perform the same task on new input.

[Few-shot examples](/langsmith/create-few-shot-evaluators#how-few-shot-examples-work) help the LLM understand:

* **Format expectations** (e.g., "respond with JSON" or "use this tone")
* **Edge cases** (e.g., how to handle ambiguous input)
* **Task nuances** (e.g., the difference between "positive" and "very positive" sentiment)

It is especially useful for classification, formatting, and stylistic tasks where showing is clearer than telling.

### Few-shot placeholder

In LangSmith, use the `{{few_shot_examples}}` placeholder where you want your examples to appear:

```mustache theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{{!-- Template --}}
You are a sentiment classifier.

{{few_shot_examples}}

Now classify this text:
Text: {{text}}
Sentiment:
```

When you enable few-shot examples in the [LangSmith UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-prompt-template-format) (in evaluators or Prompt Hub), you configure the example format separately. LangSmith automatically injects those formatted examples wherever you place the `{{few_shot_examples}}` placeholder. This keeps your prompt template clean and lets you manage examples independently.

**Example output with configured examples:**

```
You are a sentiment classifier.

Text: I love this!
Sentiment: positive
Text: This is terrible.
Sentiment: negative
Text: It's okay.
Sentiment: neutral

Now classify this text:
Text: This is amazing!
Sentiment:
```

Configure your few-shot examples in the LangSmith UI to match the format you use for the actual task. This consistency helps the LLM generalize correctly. The placeholder approach separates prompt structure from example data, making both easier to maintain.

## Conversion between formats

**F-string to mustache** always works for basic variables. Format specifiers are converted, but the formatting is removed.

**Mustache to f-string** only works for basic variables. Mustache features like dot notation, sections, conditionals, and comments have no equivalent in f-strings and cannot be converted:

* **Dot notation:** `{{user.name}}` F-strings would treat `"user.name"` as a single variable name rather than nested access.
* **Sections/loops:** `{{#items}}...{{/items}}` No equivalent in f-strings.
* **Conditionals:** `{{#value}}...{{/value}}` No equivalent in f-strings.
* **Inverted sections:** `{{^value}}...{{/value}}` No equivalent in f-strings.
* **Comments:** `{{! comment }}` No equivalent in f-strings.

If you try to convert a mustache template with these features, LangSmith will either refuse the conversion or convert only the simple parts, breaking the template's functionality. Always preview after conversion.

## Additional resources

* **[LangSmith Prompt Engineering Concepts](https://docs.langchain.com/langsmith/prompt-engineering-concepts)**: Higher-level guidance on effective prompting strategies.
* **[Mustache Manual](https://mustache.github.io/mustache.5.html)**: Full mustache specification with all features.
* **[Python f-string Documentation](https://docs.python.org/3/reference/lexical_analysis.html#f-strings)**: Official Python f-string syntax (note: LangSmith uses a simplified subset).

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/prompt-template-format.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
