##  [Example](https://vercel.com/docs/getting-started-with-vercel#example)[](https://vercel.com/docs/getting-started-with-vercel#example)
The repository configures pnpm workspaces in this file:
pnpm-workspace.yaml
```
packages:
  - 'apps/*'
  - 'packages/*'
```

If a directory is defined in `packages/not-a-package`, then this test will fail saying that the `not-a-package` directory must contain a `package.json` file.
