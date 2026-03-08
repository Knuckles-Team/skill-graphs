## Global CSS[](https://nextjs.org/docs/app/getting-started/css#global-css)
You can use global CSS to apply styles across your application.
Create a `app/global.css` file and import it in the root layout to apply the styles to **every route** in your application:
app/global.css
```
body {
  padding: 20px 20px 60px;
  max-width: 680px;
  margin: 0 auto;
}
```

app/layout.tsx
TypeScript
JavaScript TypeScript
```
// These styles apply to every route in the application
import './global.css'

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  )
}
```

> **Good to know:** Global styles can be imported into any layout, page, or component inside the `app` directory. However, since Next.js uses React's built-in support for stylesheets to integrate with Suspense, this currently does not remove stylesheets as you navigate between routes which can lead to conflicts. We recommend using global styles for _truly_ global CSS (like Tailwind's base styles), [Tailwind CSS](https://nextjs.org/docs/app/getting-started/css#tailwind-css) for component styling, and [CSS Modules](https://nextjs.org/docs/app/getting-started/css#css-modules) for custom scoped CSS when needed.
