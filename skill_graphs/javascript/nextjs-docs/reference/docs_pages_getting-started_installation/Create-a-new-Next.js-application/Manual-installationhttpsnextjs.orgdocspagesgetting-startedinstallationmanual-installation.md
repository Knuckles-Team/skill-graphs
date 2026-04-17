## Manual installation[](https://nextjs.org/docs/pages/getting-started/installation#manual-installation)
To manually create a new Next.js app, install the required packages:
pnpmnpmyarnbun
Terminal
```
pnpm i next@latest react@latest react-dom@latest
```

> **Good to know** :
>   * The `App Router` uses
>   * The `Pages Router` uses the React version from your `package.json`.
>

Then, add the following scripts to your `package.json` file:
package.json
```
{
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "lint": "eslint",
    "lint:fix": "eslint --fix"
  }
}
```

These scripts refer to the different stages of developing an application:
  * `next dev`: Starts the development server using Turbopack (default bundler).
  * `next build`: Builds the application for production.
  * `next start`: Starts the production server.
  * `eslint`: Runs ESLint.


Turbopack is now the default bundler. To use Webpack run `next dev --webpack` or `next build --webpack`. See the [Turbopack docs](https://nextjs.org/docs/app/api-reference/turbopack) for configuration details.
### Create the `pages` directory[](https://nextjs.org/docs/pages/getting-started/installation#create-the-pages-directory)
Next.js uses file-system routing, which means the routes in your application are determined by how you structure your files.
Create a `pages` directory at the root of your project. Then, add an `index.tsx` file inside your `pages` folder. This will be your home page (`/`):
pages/index.tsx
TypeScript
JavaScript TypeScript
```
export default function Page() {
  return <h1>Hello, Next.js!</h1>
}
```

Next, add an `_app.tsx` file inside `pages/` to define the global layout. Learn more about the [custom App file](https://nextjs.org/docs/pages/building-your-application/routing/custom-app).
pages/_app.tsx
TypeScript
JavaScript TypeScript
```
import type { AppProps } from 'next/app'

export default function App({ Component, pageProps }: AppProps) {
  return <Component {...pageProps} />
}
```

Finally, add a `_document.tsx` file inside `pages/` to control the initial response from the server. Learn more about the [custom Document file](https://nextjs.org/docs/pages/building-your-application/routing/custom-document).
pages/_document.tsx
TypeScript
JavaScript TypeScript
```
import { Html, Head, Main, NextScript } from 'next/document'

export default function Document() {
  return (
    <Html>
      <Head />
      <body>
        <Main />
        <NextScript />
      </body>
    </Html>
  )
}
```

### Create the `public` folder (optional)[](https://nextjs.org/docs/pages/getting-started/installation#create-the-public-folder-optional)
Create a [`public` folder](https://nextjs.org/docs/app/api-reference/file-conventions/public-folder) at the root of your project to store static assets such as images, fonts, etc. Files inside `public` can then be referenced by your code starting from the base URL (`/`).
You can then reference these assets using the root path (`/`). For example, `public/profile.png` can be referenced as `/profile.png`:
app/page.tsx
TypeScript
JavaScript TypeScript
```
import Image from 'next/image'

export default function Page() {
  return <Image src="/profile.png" alt="Profile" width={100} height={100} />
}
```
