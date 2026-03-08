## Code Blocks[](https://nextjs.org/docs/community/contribution-guide#code-blocks)
Code blocks should contain a minimum working example that can be copied and pasted. This means that the code should be able to run without any additional configuration.
For example, if you're showing how to use the `<Link>` component, you should include the `import` statement and the `<Link>` component itself.
app/page.tsx
```
import Link from 'next/link'

export default function Page() {
  return <Link href="/about">About</Link>
}
```

Always run examples locally before committing them. This will ensure that the code is up-to-date and working.
### Language and Filename[](https://nextjs.org/docs/community/contribution-guide#language-and-filename)
Code blocks should have a header that includes the language and the `filename`. For example:
code-example.mdx
```
```tsx filename="app/page.tsx"
export default function Page() {
  return <h1>Hello, Next.js!</h1>
}
```
```

For CLI commands, use the `package` prop to show the command for each package manager:
code-example.mdx
```
```bash package="pnpm"
pnpm create next-app
```

```bash package="npm"
npx create-next-app@latest
```

```bash package="yarn"
yarn create next-app
```

```bash package="bun"
bun create next-app
```
```

Most examples in the docs are written in `tsx` and `jsx`, and a few in `bash`. However, you can use any supported language, here's the
When writing JavaScript code blocks, we use the following language and extension combinations.
| Language | Extension
---|---|---
JavaScript files with JSX code | ```jsx | .js
JavaScript files without JSX | ```js | .js
TypeScript files with JSX | ```tsx | .tsx
TypeScript files without JSX | ```ts | .ts
> **Good to know** :
>   * Make sure to use **`.js`**extension for JavaScript files with**JSX** code.
>   * For example, ```jsx filename="app/layout.js"
>

### TS and JS Switcher[](https://nextjs.org/docs/community/contribution-guide#ts-and-js-switcher)
Add a language switcher to toggle between TypeScript and JavaScript. Code blocks should be TypeScript first with a JavaScript version to accommodate users.
Currently, we write TS and JS examples one after the other, and link them with `switcher` prop:
code-example.mdx
```
```tsx filename="app/page.tsx" switcher

```

```jsx filename="app/page.js" switcher

```
```

> **Good to know** : We plan to automatically compile TypeScript snippets to JavaScript in the future. In the meantime, you can use
### Line Highlighting[](https://nextjs.org/docs/community/contribution-guide#line-highlighting)
Code lines can be highlighted. This is useful when you want to draw attention to a specific part of the code. You can highlight lines by passing a number to the `highlight` prop.
**Single Line:** `highlight={1}`
app/page.tsx
```
import Link from 'next/link'

export default function Page() {
  return <Link href="/about">About</Link>
}
```

**Multiple Lines:** `highlight={1,3}`
app/page.tsx
```
import Link from 'next/link'

export default function Page() {
  return <Link href="/about">About</Link>
}
```

**Range of Lines:** `highlight={1-5}`
app/page.tsx
```
import Link from 'next/link'

export default function Page() {
  return <Link href="/about">About</Link>
}
```
