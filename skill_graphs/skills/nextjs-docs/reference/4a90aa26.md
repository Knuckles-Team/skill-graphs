## Automatically prerendered content[](https://nextjs.org/docs/app/getting-started/cache-components#automatically-prerendered-content)
Operations like synchronous I/O, module imports, and pure computations can complete during prerendering. Components using only these operations have their rendered output included in the static HTML shell.
Because all operations in the `Page` component below complete during rendering, its rendered output is automatically included in the static shell. When both the layout and page prerender successfully, the entire route is the static shell.
page.tsx
```
import fs from 'node:fs'

export default async function Page() {
  // Synchronous file system read
  const content = fs.readFileSync('./config.json', 'utf-8')

  // Module imports
  const constants = await import('./constants.json')

  // Pure computations
  const processed = JSON.parse(content).items.map((item) => item.value * 2)

  return (
    <div>
      <h1>{constants.appName}</h1>
      <ul>
        {processed.map((value, i) => (
          <li key={i}>{value}</li>
        ))}
      </ul>
    </div>
  )
}
```

> **Good to know** : You can verify that a route was fully prerendered by checking the build output summary. Alternatively, see what content was added to the static shell of any page by viewing the page source in your browser.
