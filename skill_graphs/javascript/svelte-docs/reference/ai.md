[Skip to main content](https://svelte.dev/docs/ai/overview#main) [](https://svelte.dev/ "Homepage")
Docs
[Docs ](https://svelte.dev/docs)
[Svelte](https://svelte.dev/docs/svelte)[SvelteKit](https://svelte.dev/docs/kit)[CLI](https://svelte.dev/docs/cli)[AI](https://svelte.dev/docs/ai)
[Tutorial](https://svelte.dev/tutorial)[Packages](https://svelte.dev/packages)[Playground](https://svelte.dev/playground)[Blog](https://svelte.dev/blog)
`Ctrl` `K`
[](https://svelte.dev/chat)
  * ### Introduction
    * [Overview](https://svelte.dev/docs/ai/overview)
  * ### Setup
    * [Local setup](https://svelte.dev/docs/ai/local-setup)
    * [Remote setup](https://svelte.dev/docs/ai/remote-setup)
  * ### Capabilities
    * [Tools](https://svelte.dev/docs/ai/tools)
    * [Resources](https://svelte.dev/docs/ai/resources)
    * [Prompts](https://svelte.dev/docs/ai/prompts)
  * ### Claude Code Plugin
    * [Overview](https://svelte.dev/docs/ai/plugin)
    * [Subagent](https://svelte.dev/docs/ai/subagent)
  * ### OpenCode Plugin
    * [Overview](https://svelte.dev/docs/ai/opencode-plugin)
    * [Subagent](https://svelte.dev/docs/ai/opencode-subagent)
  * ### Skills
    * [Overview](https://svelte.dev/docs/ai/skills)


AIIntroduction
#  Overview
### On this page
  * [Overview](https://svelte.dev/docs/ai/overview)
  * [Setup](https://svelte.dev/docs/ai/overview#Setup)
  * [Usage](https://svelte.dev/docs/ai/overview#Usage)
  * [Available Svelte MCP Tools:](https://svelte.dev/docs/ai/overview#Available-Svelte-MCP-Tools:)
    * [1. list-sections](https://svelte.dev/docs/ai/overview#Available-Svelte-MCP-Tools:-1.-list-sections)
    * [2. get-documentation](https://svelte.dev/docs/ai/overview#Available-Svelte-MCP-Tools:-2.-get-documentation)
    * [3. svelte-autofixer](https://svelte.dev/docs/ai/overview#Available-Svelte-MCP-Tools:-3.-svelte-autofixer)
    * [4. playground-link](https://svelte.dev/docs/ai/overview#Available-Svelte-MCP-Tools:-4.-playground-link)


The Svelte MCP (
##  Setup[](https://svelte.dev/docs/ai/overview#Setup)
The setup varies based on the version of the MCP you prefer — remote or local — and your chosen MCP client (e.g. Claude Code, Codex CLI or GitHub Copilot):
  * [local setup](https://svelte.dev/docs/ai/local-setup) using `@sveltejs/mcp`
  * [remote setup](https://svelte.dev/docs/ai/remote-setup) using `https://mcp.svelte.dev/mcp`


##  Usage[](https://svelte.dev/docs/ai/overview#Usage)
To get the most out of the MCP server we recommend including the following prompt in your
> This is already setup for you when using `npx sv add mcp`
You are able to use the Svelte MCP server, where you have access to comprehensive Svelte 5 and SvelteKit documentation. Here's how to use the available tools effectively:
##  Available Svelte MCP Tools:[](https://svelte.dev/docs/ai/overview#Available-Svelte-MCP-Tools:)
###  1. list-sections[](https://svelte.dev/docs/ai/overview#Available-Svelte-MCP-Tools:-1.-list-sections)
Use this FIRST to discover all available documentation sections. Returns a structured list with titles, use_cases, and paths. When asked about Svelte or SvelteKit topics, ALWAYS use this tool at the start of the chat to find relevant sections.
###  2. get-documentation[](https://svelte.dev/docs/ai/overview#Available-Svelte-MCP-Tools:-2.-get-documentation)
Retrieves full documentation content for specific sections. Accepts single or multiple sections. After calling the list-sections tool, you MUST analyze the returned documentation sections (especially the use_cases field) and then use the get-documentation tool to fetch ALL documentation sections that are relevant for the user's task.
###  3. svelte-autofixer[](https://svelte.dev/docs/ai/overview#Available-Svelte-MCP-Tools:-3.-svelte-autofixer)
Analyzes Svelte code and returns issues and suggestions. You MUST use this tool whenever writing Svelte code before sending it to the user. Keep calling it until no issues or suggestions are returned.
###  4. playground-link[](https://svelte.dev/docs/ai/overview#Available-Svelte-MCP-Tools:-4.-playground-link)
Generates a Svelte Playground link with the provided code. After completing the code, ask the user if they want a playground link. Only call this tool after user confirmation and NEVER if code was written to files in their project.
If your MCP client supports it, we also recommend using the [svelte-task](https://svelte.dev/docs/ai/prompts#svelte-task) prompt to instruct the LLM on the best way to use the MCP server.
[ llms.txt](https://svelte.dev/docs/ai/overview/llms.txt)
previous next
[Local setup](https://svelte.dev/docs/ai/local-setup)
