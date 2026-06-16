# CLI

The `@sveltejs/mcp` npm package normally launches the local `stdio` MCP server:

```bash
npx -y @sveltejs/mcp
```

If you invoke it with a subcommand, it behaves like a regular CLI and prints the result directly in your terminal instead. This is useful for agents, scripts and quick manual checks.

## Usage

```bash
npx -y @sveltejs/mcp <command> [options]
```

Available commands:

- `list-sections`
- `get-documentation <sections>`
- `svelte-autofixer <code_or_path>`

You can learn more about the commands with

```bash
npx -y @sveltejs/mcp --help
npx -y @sveltejs/mcp <command> --help
npx -y @sveltejs/mcp --version
```

## `list-sections`

Lists all available Svelte and SvelteKit documentation sections.

```bash
npx -y @sveltejs/mcp list-sections
```

The output is a structured text list of sections, including each section's title, `use_cases`, and documentation path. This is the same catalog the MCP tool uses before calling `get-documentation`.

## `get-documentation`

Fetches the full documentation for one or more sections.

```bash
npx -y @sveltejs/mcp get-documentation 'svelte/$state'
