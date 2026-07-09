## Examples[](https://nextjs.org/docs/pages/guides/instrumentation#examples)
### Importing files with side effects[](https://nextjs.org/docs/pages/guides/instrumentation#importing-files-with-side-effects)
Sometimes, it may be useful to import a file in your code because of the side effects it will cause. For example, you might import a file that defines a set of global variables, but never explicitly use the imported file in your code. You would still have access to the global variables the package has declared.
We recommend importing files using JavaScript `import` syntax within your `register` function. The following example demonstrates a basic usage of `import` in a `register` function:
instrumentation.ts
TypeScript
JavaScript TypeScript
```
export async function register() {
  await import('package-with-side-effect')
}
```

> **Good to know:**
> We recommend importing the file from within the `register` function, rather than at the top of the file. By doing this, you can colocate all of your side effects in one place in your code, and avoid any unintended consequences from importing globally at the top of the file.
### Importing runtime-specific code[](https://nextjs.org/docs/pages/guides/instrumentation#importing-runtime-specific-code)
Next.js calls `register` in all environments, so it's important to conditionally import any code that doesn't support specific runtimes (e.g. [Edge or Node.js](https://nextjs.org/docs/app/api-reference/edge)). You can use the `NEXT_RUNTIME` environment variable to get the current environment:
instrumentation.ts
TypeScript
JavaScript TypeScript
```
export async function register() {
  if (process.env.NEXT_RUNTIME === 'nodejs') {
    await import('./instrumentation-node')
  }

  if (process.env.NEXT_RUNTIME === 'edge') {
    await import('./instrumentation-edge')
  }
}
```

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
