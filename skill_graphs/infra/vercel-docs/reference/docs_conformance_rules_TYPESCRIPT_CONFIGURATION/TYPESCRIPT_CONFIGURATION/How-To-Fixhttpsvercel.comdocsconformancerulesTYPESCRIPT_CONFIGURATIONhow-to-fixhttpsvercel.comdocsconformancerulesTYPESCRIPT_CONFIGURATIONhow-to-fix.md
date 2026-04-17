##  [How To Fix](https://vercel.com/docs/conformance/rules/TYPESCRIPT_CONFIGURATION#how-to-fix)[](https://vercel.com/docs/conformance/rules/TYPESCRIPT_CONFIGURATION#how-to-fix)
The shared `tsconfig.json` should have at least the following defined:
tsconfig.json
```
{
  "compilerOptions": {
    "incremental": true,
    "noUncheckedIndexedAccess": true,
    "strict": true
  }
}
```

For other configuration issues, the project's `tsconfig.json` may need to be updated. Most files that don't require customization should look like:
tsconfig.json
```
{
  "extends": "your_shared_tsconfig/base.json",
  "exclude": ["dist", "node_modules"],
  "compilerOptions": {
    "tsBuildInfoFile": "node_modules/.cache/tsbuildinfo.json"
  }
}
```

Additionally, the project's `package.json` file may need to be updated. A `type-check` command needs to be added to the `scripts` section:
package.json
```
{
  "scripts": {
    ...,
    "type-check": "tsc -p tsconfig.json --noEmit"
  }
}
```

The dependency on the repository's shared TypeScript must also exist:
```
{
  "devDependencies": {
    "your_shared_tsconfig": "workspace:*"
  }
}
```

* * *
Was this helpful?
Send
On this page
  * [Example](https://vercel.com/docs/conformance/rules/TYPESCRIPT_CONFIGURATION#example)
  * [How To Fix](https://vercel.com/docs/conformance/rules/TYPESCRIPT_CONFIGURATION#how-to-fix)


Copy as MarkdownGive feedbackAsk AI about this page
