## Manual installation[](https://nextjs.org/docs/app/getting-started/installation#manual-installation)
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
### Create the `app` directory[](https://nextjs.org/docs/app/getting-started/installation#create-the-app-directory)
Next.js uses file-system routing, which means the routes in your application are determined by how you structure your files.
Create an `app` folder. Then, inside `app`, create a `layout.tsx` file. This file is the [root layout](https://nextjs.org/docs/app/api-reference/file-conventions/layout#root-layout). It's required and must contain the `<html>` and `<body>` tags.
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

Create a home page `app/page.tsx` with some initial content:
app/page.tsx
TypeScript
JavaScript TypeScript
```
export default function Page() {
  return <h1>Hello, Next.js!</h1>
}
```

Both `layout.tsx` and `page.tsx` will be rendered when the user visits the root of your application (`/`).
![App Folder Structure](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Flight%2Fapp-getting-started.png&w=3840&q=75)![App Folder Structure](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Fdark%2Fapp-getting-started.png&w=3840&q=75)
> **Good to know** :
>   * If you forget to create the root layout, Next.js will automatically create this file when running the development server with `next dev`.
>   * You can optionally use a [`src` folder](https://nextjs.org/docs/app/api-reference/file-conventions/src-folder) in the root of your project to separate your application's code from configuration files.
>

### Create the `public` folder (optional)[](https://nextjs.org/docs/app/getting-started/installation#create-the-public-folder-optional)
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
