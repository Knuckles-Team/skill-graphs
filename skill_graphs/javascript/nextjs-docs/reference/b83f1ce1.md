## Set up linting[](https://nextjs.org/docs/pages/getting-started/installation#set-up-linting)
Next.js supports linting with either ESLint or Biome. Choose a linter and run it directly via `package.json` scripts.
  * Use **ESLint** (comprehensive rules):


package.json
```
{
  "scripts": {
    "lint": "eslint",
    "lint:fix": "eslint --fix"
  }
}
```

  * Or use **Biome** (fast linter + formatter):


package.json
```
{
  "scripts": {
    "lint": "biome check",
    "format": "biome format --write"
  }
}
```

If your project previously used `next lint`, migrate your scripts to the ESLint CLI with the codemod:
Terminal
```
npx @next/codemod@canary next-lint-to-eslint-cli .
```

If you use ESLint, create an explicit config (recommended `eslint.config.mjs`). ESLint supports both [ESLint API reference](https://nextjs.org/docs/app/api-reference/config/eslint#with-core-web-vitals) for a recommended setup.
> **Good to know** : Starting with Next.js 16, `next build` no longer runs the linter automatically. Instead, you can run your linter through NPM scripts.
See the [ESLint Plugin](https://nextjs.org/docs/app/api-reference/config/eslint) page for more information.
