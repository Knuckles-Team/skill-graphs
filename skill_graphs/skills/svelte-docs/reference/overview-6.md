# Overview

This is the list of available skills provided by the Svelte MCP package. Skills are sets of instructions that AI agents can load on-demand to help with specific tasks.

Skills are available in both the Claude Code plugin (installed via the marketplace) and the OpenCode plugin (`@sveltejs/opencode`). They can also be manually installed in your `.claude/skills` or `.opencode/skills` folder.

You can download the latest skills from the [releases page](https://github.com/sveltejs/ai-tools/releases) of the repo, or find them in the [`tools/skills`](https://github.com/sveltejs/ai-tools/tree/main/tools/skills) folder.

## `svelte-code-writer`

CLI tools for Svelte 5 documentation lookup and code analysis. MUST be used whenever creating, editing or analyzing any Svelte component (.svelte) or Svelte module (.svelte.ts/.svelte.js). If possible, this skill should be executed within the svelte-file-editor agent for optimal results.

<a href="https://github.com/sveltejs/ai-tools/releases?q=svelte-code-writer" target="_blank" rel="noopener noreferrer">Open Releases page</a>

<details>
	<summary>View skill content</summary>

<!-- prettier-ignore-start -->
````markdown
