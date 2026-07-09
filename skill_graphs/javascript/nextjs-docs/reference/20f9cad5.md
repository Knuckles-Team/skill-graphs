# Pages and Layouts
Last updated February 27, 2026
The Pages Router has a file-system based router built on the concept of pages.
When a file is added to the `pages` directory, it's automatically available as a route.
In Next.js, a **page** is a `.js`, `.jsx`, `.ts`, or `.tsx` file in the `pages` directory. Each page is associated with a route based on its file name.
**Example** : If you create `pages/about.js` that exports a React component like below, it will be accessible at `/about`.
```
export default function About() {
  return <div>About</div>
}
```
