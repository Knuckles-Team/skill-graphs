##  [Exporting the Hono application](https://vercel.com/docs/getting-started-with-vercel#exporting-the-hono-application)[](https://vercel.com/docs/getting-started-with-vercel#exporting-the-hono-application)
To run a Hono application on Vercel, create a file that imports the `hono` package at any one of the following locations:
  * `app.{js,cjs,mjs,ts,cts,mts}`
  * `index.{js,cjs,mjs,ts,cts,mts}`
  * `server.{js,cjs,mjs,ts,cts,mts}`
  * `src/app.{js,cjs,mjs,ts,cts,mts}`
  * `src/index.{js,cjs,mjs,ts,cts,mts}`
  * `src/server.{js,mjs,cjs,ts,cts,mts}`


server.ts
```
import { Hono } from 'hono';

const app = new Hono();

// ...

export default app;
```

###  [Local development](https://vercel.com/docs/getting-started-with-vercel#local-development)[](https://vercel.com/docs/getting-started-with-vercel#local-development)
To run your Hono application locally, use [Vercel CLI](https://vercel.com/docs/cli/dev):
```
vc dev
```

This ensures that the application will use the default export to run the same as when deployed to Vercel. The application will be available on your `localhost`.
