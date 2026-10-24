##  [Exporting the Express application](https://vercel.com/docs/getting-started-with-vercel#exporting-the-express-application)[](https://vercel.com/docs/getting-started-with-vercel#exporting-the-express-application)
To run an Express application on Vercel, create a file that imports the `express` package at any one of the following locations:
  * `app.{js,cjs,mjs,ts,cts,mts}`
  * `index.{js,cjs,mjs,ts,cts,mts}`
  * `server.{js,cjs,mjs,ts,cts,mts}`
  * `src/app.{js,cjs,mjs,ts,cts,mts}`
  * `src/index.{js,cjs,mjs,ts,cts,mts}`
  * `src/server.{js,mjs,cjs,ts,cts,mts}`


The file must also export the application as a default export of the module or use a port listener.
###  [Using a default export](https://vercel.com/docs/getting-started-with-vercel#using-a-default-export)[](https://vercel.com/docs/getting-started-with-vercel#using-a-default-export)
For example, use the following code that exports your Express app:
###  [Using a port listener](https://vercel.com/docs/getting-started-with-vercel#using-a-port-listener)[](https://vercel.com/docs/getting-started-with-vercel#using-a-port-listener)
You may also run your application using the `app.listen` pattern that exposes the server on a port.
###  [Local development](https://vercel.com/docs/getting-started-with-vercel#local-development)[](https://vercel.com/docs/getting-started-with-vercel#local-development)
Use `vercel dev` to run your application locally
terminal
```
vercel dev
```

Minimum CLI version required: 47.0.5
###  [Deploying the application](https://vercel.com/docs/getting-started-with-vercel#deploying-the-application)[](https://vercel.com/docs/getting-started-with-vercel#deploying-the-application)
To deploy, [connect your Git repository](https://vercel.com/new) or [use Vercel CLI](https://vercel.com/docs/cli/deploy):
terminal
```
vc deploy
```

Minimum CLI version required: 47.0.5
