##  [Using Vite to make SPAs](https://vercel.com/docs/getting-started-with-vercel#using-vite-to-make-spas)[](https://vercel.com/docs/getting-started-with-vercel#using-vite-to-make-spas)
If your Vite app is
To enable deep linking in SPA Vite apps, create a `vercel.json` file at the root of your project, and add the following code:
vercel.json
```
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "rewrites": [
    {
      "source": "/(.*)",
      "destination": "/index.html"
    }
  ]
}
```

If [`cleanUrls`](https://vercel.com/docs/project-configuration#cleanurls) is set to `true` in your project's `vercel.json`, do not include the file extension in the source or destination path. For example, `/index.html` would be `/`
Deploying your app in Multi-Page App mode is recommended for production builds.
Learn more about
