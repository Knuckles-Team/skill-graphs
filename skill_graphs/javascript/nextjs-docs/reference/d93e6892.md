## Tailwind CSS[](https://nextjs.org/docs/pages/getting-started/css#tailwind-css)
Install Tailwind CSS:
pnpmnpmyarnbun
Terminal
```
pnpm add -D tailwindcss @tailwindcss/postcss
```

Add the PostCSS plugin to your `postcss.config.mjs` file:
postcss.config.mjs
```
export default {
  plugins: {
    '@tailwindcss/postcss': {},
  },
}
```

Import Tailwind in your global CSS file:
styles/globals.css
```
@import 'tailwindcss';
```

Import the CSS file in your `pages/_app.js` file:
pages/_app.js
```
import '@/styles/globals.css'

export default function MyApp({ Component, pageProps }) {
  return <Component {...pageProps} />
}
```

Now you can start using Tailwind's utility classes in your application:
pages/index.tsx
TypeScript
JavaScript TypeScript
```
export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      <h1 className="text-4xl font-bold">Welcome to Next.js!</h1>
    </main>
  )
}
```

> **Good to know:** If you need broader browser support for very old browsers, see the [Tailwind CSS v3 setup instructions](https://nextjs.org/docs/app/guides/tailwind-v3-css).
