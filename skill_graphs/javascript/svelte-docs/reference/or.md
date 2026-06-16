# or
npx -y @sveltejs/mcp get-documentation 'svelte/$state,svelte/await-expressions'
```

Each section can be matched by title or by documentation path. If a section cannot be found, the CLI returns an error plus similar matches when available.

## `svelte-autofixer`

Runs the Svelte autofixer against either inline code or a file path:

```bash
npx -y @sveltejs/mcp svelte-autofixer 'src/routes/+page.svelte'
```

If the argument is an existing path, the CLI reads the file automatically. Otherwise it treats the argument as raw Svelte code.

Because most shells expand `$`, inline code should be quoted or escaped correctly. In practice, passing a file path is usually easier than passing source directly.

Available options:

- `--svelte-version <4|5>` - choose which Svelte version to validate against (defaults to `5`)
- `--async` - enable async Svelte analysis for Svelte 5 projects

The command prints an object with:

- `issues`
- `suggestions`
- `require_another_tool_call_after_fixing`

This makes it easy to use in an agentic loop: run the autofixer, apply fixes, then run it again until it reports no remaining issues or suggestions.
