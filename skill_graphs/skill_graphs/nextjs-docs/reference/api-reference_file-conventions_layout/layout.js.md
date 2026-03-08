# layout.js
Last updated February 27, 2026
The `layout` file is used to define a layout in your Next.js application.
app/dashboard/layout.tsx
TypeScript
JavaScript TypeScript
```
export default function DashboardLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return <section>{children}</section>
}
```

A **root layout** is the top-most layout in the root `app` directory. It is used to define the `<html>` and `<body>` tags and other globally shared UI.
app/layout.tsx
TypeScript
JavaScript TypeScript
```
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
