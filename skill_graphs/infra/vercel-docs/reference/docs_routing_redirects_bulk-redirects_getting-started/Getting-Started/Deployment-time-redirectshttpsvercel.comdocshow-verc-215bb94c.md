##  [Deployment-time redirects](https://vercel.com/docs/how-vercel-cdn-works#deployment-time-redirects)[](https://vercel.com/docs/how-vercel-cdn-works#deployment-time-redirects)
Bulk redirects in deployments are specified in the `bulkRedirectsPath` field in `vercel.json`. `bulkRedirectsPath` can point to either a single file or a folder with up to 100 files. Vercel supports any combination of CSV, JSON, and JSONL files containing redirects, and they can be generated at build time.
Learn more about bulk redirects fields and file formats in the [project configuration documentation](https://vercel.com/docs/projects/project-configuration#bulkredirectspath).
  1. ###  [Create your redirect file](https://vercel.com/docs/how-vercel-cdn-works#create-your-redirect-file)[](https://vercel.com/docs/how-vercel-cdn-works#create-your-redirect-file)
You can create fixed files of redirects, or generate them at build time as long as they end up in the location specified by `bulkRedirectsPath` before the build completes.
redirects.csv
```
source,destination,permanent
/old-blog,/blog,true
/old-about,/about,false
/legacy-contact,https://example.com/contact,true
```

  2. ###  [Configure bulkRedirectsPath](https://vercel.com/docs/how-vercel-cdn-works#configure-bulkredirectspath)[](https://vercel.com/docs/how-vercel-cdn-works#configure-bulkredirectspath)
Add the `bulkRedirectsPath` property to your `vercel.json` file, pointing to your redirect file. You can also point to a folder containing multiple redirect files if needed.
vercel.json
```
{
  "bulkRedirectsPath": "redirects.csv"
}
```

  3. ###  [Deploy](https://vercel.com/docs/how-vercel-cdn-works#deploy)[](https://vercel.com/docs/how-vercel-cdn-works#deploy)
Deploy your project to Vercel. Your bulk redirects will be processed and applied automatically.
```
vercel deploy
```

Any errors processing the bulk redirects will appear in the build logs for the deployment.
