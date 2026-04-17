##  [Usage](https://vercel.com/docs/og-image-generation#usage)[](https://vercel.com/docs/og-image-generation#usage)
###  [Requirements](https://vercel.com/docs/og-image-generation#requirements)[](https://vercel.com/docs/og-image-generation#requirements)
  * Install Node.js 22 or newer by visiting
  * Install `@vercel/og` by running the following command inside your project directory. This isn't required for Next.js App Router projects, as the package is already included:


Terminal
![](https://7nyt0uhk7sse4zvn.public.blob.vercel-storage.com/docs-assets/static/topics/icons/pnpm.svg)pnpm bun yarn npm
```
pnpm i @vercel/og
```

```
yarn add @vercel/og
```

```
npm i @vercel/og
```

```
bun add @vercel/og
```

  * For Next.js implementations, make sure you are using Next.js v12.2.3 or newer
  * Create API endpoints that you can call from your front-end to generate the images. Since the HTML code for generating the image is included as one of the parameters of the `ImageResponse` function, the use of `.jsx` or `.tsx` files is recommended as they are designed to handle this kind of syntax
  * To avoid the possibility of social media providers not being able to fetch your image, it is recommended to add your OG image API route(s) to `Allow` inside your `robots.txt` file. For example, if your OG image API route is `/api/og/`, you can add the following line:
robots.txt
```
Allow: /api/og/*
```

If you are using Next.js, review `robots.txt` file.


###  [Getting started](https://vercel.com/docs/og-image-generation#getting-started)[](https://vercel.com/docs/og-image-generation#getting-started)
Get started with an example that generates an image from static text using Next.js by setting up a new app with the following command:
Terminal
![](https://7nyt0uhk7sse4zvn.public.blob.vercel-storage.com/docs-assets/static/topics/icons/pnpm.svg)pnpm bun yarn npm
```
pnpm create next-app@latest
```

```
yarn create next-app@latest
```

```
npx create-next-app@latest
```

```
bunx create-next-app@latest
```

Create an API endpoint by adding `route.tsx` under the `app/api/og` directory in the root of your project.
Then paste the following code:
Next.js (/app)Next.js (/pages)Other frameworks
app/api/og/route.tsx
TypeScript
TypeScript JavaScript Bash
```
import { ImageResponse } from 'next/og';
// App router includes @vercel/og.
// No need to install it.

export async function GET() {
  return new ImageResponse(
    (
      <div
        style={{
          fontSize: 40,
          color: 'black',
          background: 'white',
          width: '100%',
          height: '100%',
          padding: '50px 200px',
          textAlign: 'center',
          justifyContent: 'center',
          alignItems: 'center',
        }}
      >
        👋 Hello
      </div>
    ),
    {
      width: 1200,
      height: 630,
    },
  );
}
```

If you're not using a framework, you must either add `"type": "module"` to your `package.json` or change your JavaScript Functions' file extensions from `.js` to `.mjs`
Run the following command:
Terminal
![](https://7nyt0uhk7sse4zvn.public.blob.vercel-storage.com/docs-assets/static/topics/icons/pnpm.svg)pnpm bun yarn npm
```
pnpm dev
```

```
yarn dev
```

```
npm run dev
```

```
bun run dev
```

Then, browse to `http://localhost:3000/api/og`. You will see the following image:
![](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Ffunctions%2Fog-image%2Fog-language.png&w=3840&q=75)
###  [Consume the OG route](https://vercel.com/docs/og-image-generation#consume-the-og-route)[](https://vercel.com/docs/og-image-generation#consume-the-og-route)
Deploy your project to obtain a publicly accessible path to the OG image API endpoint. You can find an example deployment at
Then, based on the
  * Create a `<meta>` tag inside the `<head>` of the webpage
  * Add the `property` attribute with value `og:image` to the `<meta>` tag
  * Add the `content` attribute with value as the absolute path of the `/api/og` endpoint to the `<meta>` tag


With the example deployment at
index.js
```
<head>
  <title>Hello world</title>
  <meta
    property="og:image"
    content="https://og-examples.vercel.sh/api/static"
  />
</head>
```

Every time you create a new social media post, you need to update the API endpoint with the new content. However, if you identify which parts of your `ImageResponse` will change for each post, you can then pass those values as parameters of the endpoint so that you can use the same endpoint for all your posts.
In the examples below, we explore using parameters and including other types of content with `ImageResponse`.
