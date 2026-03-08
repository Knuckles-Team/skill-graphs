## Scroll Behavior Override[](https://nextjs.org/docs/app/guides/upgrading/version-16#scroll-behavior-override)
In **previous versions of Next.js** , if you had set `scroll-behavior: smooth` globally on your `<html>` element via CSS, Next.js would override this during SPA route transitions, as follows:
  1. Temporarily set `scroll-behavior` to `auto`
  2. Perform the navigation (causing instant scroll to top)
  3. Restore your original `scroll-behavior` value


This ensured that page navigation always felt snappy and instant, even when you had smooth scrolling enabled for in-page navigation. However, this manipulation could be expensive, especially at the start of every navigation.
In **Next.js 16** , this behavior has changed. By default, Next.js will **no longer override** your `scroll-behavior` setting during navigation.
**If you want Next.js to perform this override** (the previous default behavior), add the `data-scroll-behavior="smooth"` attribute to your `<html>` element:
app/layout.tsx
```
export default function RootLayout({ children }) {
  return (
    <html lang="en" data-scroll-behavior="smooth">
      <body>{children}</body>
    </html>
  )
}
```
