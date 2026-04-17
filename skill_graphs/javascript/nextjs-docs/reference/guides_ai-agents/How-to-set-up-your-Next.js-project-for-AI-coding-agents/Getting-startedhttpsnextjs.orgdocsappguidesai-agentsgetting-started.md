## Getting started[](https://nextjs.org/docs/app/guides/ai-agents#getting-started)
### New projects[](https://nextjs.org/docs/app/guides/ai-agents#new-projects)
[`create-next-app`](https://nextjs.org/docs/app/api-reference/cli/create-next-app) generates `AGENTS.md` and `CLAUDE.md` automatically. No additional setup is needed:
pnpmnpmyarnbun
Terminal
```
pnpm create next-app@canary
```

If you don't want the agent files, pass `--no-agents-md`:
```
npx create-next-app@canary --no-agents-md
```

### Existing projects[](https://nextjs.org/docs/app/guides/ai-agents#existing-projects)
Ensure you are on Next.js `v16.2.0-canary.37` or later, then add the following files to the root of your project.
`AGENTS.md` contains the instructions that agents will read:
AGENTS.md
```
<!-- BEGIN:nextjs-agent-rules -->

# Next.js: ALWAYS read docs before coding

Before any Next.js work, find and read the relevant doc in `node_modules/next/dist/docs/`. Your training data is outdated — the docs are the source of truth.

<!-- END:nextjs-agent-rules -->
```

`CLAUDE.md` uses the `@` import syntax to include `AGENTS.md`, so
CLAUDE.md
```
@AGENTS.md
```
