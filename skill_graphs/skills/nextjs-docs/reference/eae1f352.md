## Set up a CDN[](https://nextjs.org/docs/app/api-reference/config/next-config-js/assetPrefix#set-up-a-cdn)
To set up a
Open `next.config.mjs` and add the `assetPrefix` config based on the [phase](https://nextjs.org/docs/app/api-reference/config/next-config-js#async-configuration):
next.config.mjs
```
// @ts-check
import { PHASE_DEVELOPMENT_SERVER } from 'next/constants'

export default (phase) => {
  const isDev = phase === PHASE_DEVELOPMENT_SERVER
  /**
   * @type {import('next').NextConfig}
   */
  const nextConfig = {
    assetPrefix: isDev ? undefined : 'https://cdn.mydomain.com',
  }
  return nextConfig
}
```

Next.js will automatically use your asset prefix for the JavaScript and CSS files it loads from the `/_next/` path (`.next/static/` folder). For example, with the above configuration, the following request for a JS chunk:
```
/_next/static/chunks/4b9b41aaa062cbbfeff4add70f256968c51ece5d.4d708494b3aed70c04f0.js

```

Would instead become:
```
https://cdn.mydomain.com/_next/static/chunks/4b9b41aaa062cbbfeff4add70f256968c51ece5d.4d708494b3aed70c04f0.js

```

The exact configuration for uploading your files to a given CDN will depend on your CDN of choice. The only folder you need to host on your CDN is the contents of `.next/static/`, which should be uploaded as `_next/static/` as the above URL request indicates. **Do not upload the rest of your`.next/` folder**, as you should not expose your server code and other configuration to the public.
While `assetPrefix` covers requests to `_next/static`, it does not influence the following paths:
  * Files in the [public](https://nextjs.org/docs/app/api-reference/file-conventions/public-folder) folder; if you want to serve those assets over a CDN, you'll have to introduce the prefix yourself


[PreviousappDir](https://nextjs.org/docs/app/api-reference/config/next-config-js/appDir)[NextauthInterrupts](https://nextjs.org/docs/app/api-reference/config/next-config-js/authInterrupts)
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
