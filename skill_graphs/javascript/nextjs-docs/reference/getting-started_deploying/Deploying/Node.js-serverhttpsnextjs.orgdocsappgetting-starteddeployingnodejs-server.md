## Node.js server[](https://nextjs.org/docs/app/getting-started/deploying#nodejs-server)
Next.js can be deployed to any provider that supports Node.js. Ensure your `package.json` has the `"build"` and `"start"` scripts:
package.json
```
{
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start"
  }
}
```

Then, run `npm run build` to build your application and `npm run start` to start the Node.js server. This server supports all Next.js features. If needed, you can also eject to a [custom server](https://nextjs.org/docs/app/guides/custom-server).
Node.js deployments support all Next.js features. Learn how to [configure them](https://nextjs.org/docs/app/guides/self-hosting) for your infrastructure.
### Templates[](https://nextjs.org/docs/app/getting-started/deploying#templates)
