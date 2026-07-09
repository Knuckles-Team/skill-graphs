# forbidden-dependencies
Last updated September 24, 2025
Conformance is available on [Enterprise plans](https://vercel.com/docs/plans/enterprise)
The `forbidden-dependencies` rule type enables you to disallow one or more files from depending on one or more predefined modules.
Unlike [`forbidden-imports`](https://vercel.com/docs/conformance/custom-rules/forbidden-imports), this rule type will check for indirect (or transitive) dependencies, where a module may not directly import the disallowed dependency, but the disallowed dependency is present in the dependency chain. This makes it slower, but more powerful than the `forbidden-imports` rule type.
For example, below we have a `logger` utility that imports a package that may cause security keys to be exposed.
src/utils/logger.ts
```
import { SECURITY_KEY } from 'secret-package';
```

We can use this rule type to create a custom rule that prevents any module in `src/app` from importing any file that depends on our potentially dangerous `secret-package`.
src/app/page.ts
```
import { log } from '../utils/logger';
// Would result in an error
```
