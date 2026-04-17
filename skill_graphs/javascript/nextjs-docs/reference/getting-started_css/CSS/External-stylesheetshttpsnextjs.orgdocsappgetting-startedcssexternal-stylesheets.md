## External stylesheets[](https://nextjs.org/docs/app/getting-started/css#external-stylesheets)
Stylesheets published by external packages can be imported anywhere in the `app` directory, including colocated components:
app/layout.tsx
TypeScript
JavaScript TypeScript
```
import 'bootstrap/dist/css/bootstrap.css'

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body className="container">{children}</body>
    </html>
  )
}
```

> **Good to know:** In React 19, `<link rel="stylesheet" href="..." />` can also be used. See the
