## Configuring Tailwind v3[](https://nextjs.org/docs/app/guides/tailwind-v3-css#configuring-tailwind-v3)
Configure your template paths in your `tailwind.config.js` file:
tailwind.config.js
```
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './app/**/*.{js,ts,jsx,tsx,mdx}',
    './pages/**/*.{js,ts,jsx,tsx,mdx}',
    './components/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
```

Add the Tailwind directives to your global CSS file:
app/globals.css
```
@tailwind base;
@tailwind components;
@tailwind utilities;
```

Import the CSS file in your root layout:
app/layout.tsx
TypeScript
JavaScript TypeScript
```
import './globals.css'

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
