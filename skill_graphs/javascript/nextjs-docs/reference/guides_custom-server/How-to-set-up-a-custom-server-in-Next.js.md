# How to set up a custom server in Next.js
Last updated February 27, 2026
Next.js includes its own server with `next start` by default. If you have an existing backend, you can still use it with Next.js (this is not a custom server). A custom Next.js server allows you to programmatically start a server for custom patterns. The majority of the time, you will not need this approach. However, it's available if you need to eject.
> **Good to know** :
>   * Before deciding to use a custom server, keep in mind that it should only be used when the integrated router of Next.js can't meet your app requirements. A custom server will remove important performance optimizations, like **[Automatic Static Optimization](https://nextjs.org/docs/pages/building-your-application/rendering/automatic-static-optimization).**
>   * When using standalone output mode, it does not trace custom server files. This mode outputs a separate minimal `server.js` file, instead. These cannot be used together.
>

Take a look at the
server.ts
TypeScript
JavaScript TypeScript
```
import { createServer } from 'http'
import next from 'next'

const port = parseInt(process.env.PORT || '3000', 10)
const dev = process.env.NODE_ENV !== 'production'
const app = next({ dev })
const handle = app.getRequestHandler()

app.prepare().then(() => {
  createServer((req, res) => {
    handle(req, res)
  }).listen(port)

  console.log(
    `> Server listening at http://localhost:${port} as ${
      dev ? 'development' : process.env.NODE_ENV
    }`
  )
})
```

> `server.js` does not run through the Next.js Compiler or bundling process. Make sure the syntax and source code this file requires are compatible with the current Node.js version you are using.
To run the custom server, you'll need to update the `scripts` in `package.json` like so:
package.json
```
{
  "scripts": {
    "dev": "node server.js",
    "build": "next build",
    "start": "NODE_ENV=production node server.js"
  }
}
```

Alternatively, you can set up `nodemon` (
```
import next from 'next'

const app = next({})
```

The above `next` import is a function that receives an object with the following options:
Option | Type | Description
---|---|---
`conf` | `Object` | The same object you would use in `next.config.js`. Defaults to `{}`
`dev` | `Boolean` | (_Optional_) Whether or not to launch Next.js in dev mode. Defaults to `false`
`dir` | `String` | (_Optional_) Location of the Next.js project. Defaults to `'.'`
`quiet` | `Boolean` | (_Optional_) Hide error messages containing server information. Defaults to `false`
`hostname` | `String` | (_Optional_) The hostname the server is running behind
`port` | `Number` | (_Optional_) The port the server is running behind
`httpServer` | `node:http#Server` | (_Optional_) The HTTP Server that Next.js is running behind
`turbopack` | `Boolean` | (_Optional_) Enable Turbopack (enabled by default)
`webpack` | `Boolean` | (_Optional_) Enable webpack
The returned `app` can then be used to let Next.js handle requests as required.
[PreviousCSS-in-JS](https://nextjs.org/docs/app/guides/css-in-js)[NextData Security](https://nextjs.org/docs/app/guides/data-security)
Was this helpful?
Send
* * *
* * *
#### Resources
[Docs](https://nextjs.org/docs)[Support Policy](https://nextjs.org/support-policy)[Learn](https://nextjs.org/learn)[Showcase](https://nextjs.org/showcase)[Blog](https://nextjs.org/blog)[Team](https://nextjs.org/team)[Next.js Conf](https://nextjs.org/conf)[Evals](https://nextjs.org/evals)
#### More
[Telemetry](https://nextjs.org/telemetry)[Governance](https://nextjs.org/governance)
#### About Vercel
#### Legal
Cookie Preferences
#### Subscribe to our newsletter
Stay updated on new releases and features, guides, and case studies.
Subscribe
© 2026 Vercel, Inc.
* * *
* * *
