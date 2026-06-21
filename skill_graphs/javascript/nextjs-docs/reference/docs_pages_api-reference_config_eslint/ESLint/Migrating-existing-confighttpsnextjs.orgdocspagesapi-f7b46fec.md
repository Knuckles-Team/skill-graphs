## Migrating existing config[](https://nextjs.org/docs/pages/api-reference/config/eslint#migrating-existing-config)
If you already have ESLint configured in your application, there are two approaches to integrate Next.js linting rules, depending on your setup.
#### Using the plugin directly[](https://nextjs.org/docs/pages/api-reference/config/eslint#using-the-plugin-directly)
Use `@next/eslint-plugin-next` directly if you have any of the following already configured:
  * Conflicting plugins installed separately or through another config (such as `airbnb` or `react-app`):
    * `react`
    * `react-hooks`
    * `jsx-a11y`
    * `import`
  * Custom `parserOptions` different from Next.js defaults (only if you have [customized your Babel configuration](https://nextjs.org/docs/pages/guides/babel))
  * `eslint-plugin-import` with custom Node.js and/or TypeScript


In these cases, use `@next/eslint-plugin-next` directly to avoid conflicts:
First, install the plugin:
pnpmnpmyarnbun
Terminal
```
pnpm add -D @next/eslint-plugin-next
```

Then add it to your ESLint config:
eslint.config.mjs
```
import { defineConfig } from 'eslint/config'
import nextPlugin from '@next/eslint-plugin-next'

const eslintConfig = defineConfig([
  // Your other configurations...
  {
    files: ['**/*.{js,jsx,ts,tsx}'],
    plugins: {
      '@next/next': nextPlugin,
    },
    rules: {
      ...nextPlugin.configs.recommended.rules,
    },
  },
])

export default eslintConfig
```

This approach eliminates the risk of collisions or errors that can occur when the same plugins or parsers are imported across multiple configurations.
#### Adding to existing config[](https://nextjs.org/docs/pages/api-reference/config/eslint#adding-to-existing-config)
If you're adding Next.js to an existing ESLint setup, spread the Next.js config into your array:
eslint.config.mjs
```
import nextConfig from 'eslint-config-next/core-web-vitals'
// Your other config imports...

const eslintConfig = [
  // Your other configurations...
  ...nextConfig,
]

export default eslintConfig
```

When you spread `...nextConfig`, you're adding multiple config objects that include file patterns, plugins, rules, ignores, and parser settings. ESLint applies configs in order, so later rules can override earlier ones for matching files.
> **Good to know:** This approach works well for straightforward setups. If you have a complex existing config with specific file patterns or plugin configurations that conflict, consider using the plugin directly (as shown above) for more granular control.
Version | Changes
---|---
`v16.0.0` |  `next lint` and the `eslint` next.config.js option were removed in favor of the ESLint CLI. A [codemod](https://nextjs.org/docs/app/guides/upgrading/codemods#migrate-from-next-lint-to-eslint-cli) is available to help you migrate.
Was this helpful?
Send
* * *
* * *
#### Resources
[Docs](https://nextjs.org/docs)[Support Policy](https://nextjs.org/support-policy)[Learn](https://nextjs.org/learn)[Showcase](https://nextjs.org/showcase)[Blog](https://nextjs.org/blog)[Team](https://nextjs.org/team)[Next.js Conf](https://nextjs.org/conf)[Evals](https://nextjs.org/evals)
#### More
[Telemetry](https://nextjs.org/telemetry)[Governance](https://nextjs.org/governance)
#### About Vercel
#### Legal
Cookie Preferences
#### Subscribe to our newsletter
Stay updated on new releases and features, guides, and case studies.
Subscribe
© 2026 Vercel, Inc.
* * *
* * *
