## Setup ESLint[](https://nextjs.org/docs/pages/api-reference/config/eslint#setup-eslint)
Get linting working quickly with the ESLint CLI (flat config):
  1. Install ESLint and the Next.js config:
pnpmnpmyarnbun
Terminal
```
pnpm add -D eslint eslint-config-next
```

  2. Create `eslint.config.mjs` with the Next.js config:
eslint.config.mjs
```
import { defineConfig, globalIgnores } from 'eslint/config'
import nextVitals from 'eslint-config-next/core-web-vitals'

const eslintConfig = defineConfig([
  ...nextVitals,
  // Override default ignores of eslint-config-next.
  globalIgnores([
    // Default ignores of eslint-config-next:
    '.next/**',
    'out/**',
    'build/**',
    'next-env.d.ts',
  ]),
])

export default eslintConfig
```

  3. Run ESLint:
pnpmnpmyarnbun
Terminal
```
pnpm exec eslint .
```
