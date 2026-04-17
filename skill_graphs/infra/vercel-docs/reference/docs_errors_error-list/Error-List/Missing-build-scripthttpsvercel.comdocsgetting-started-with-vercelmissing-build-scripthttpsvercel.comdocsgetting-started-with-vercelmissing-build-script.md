##  [Missing build script](https://vercel.com/docs/getting-started-with-vercel#missing-build-script)[](https://vercel.com/docs/getting-started-with-vercel#missing-build-script)
This is only relevant if you’re using Vercel CLI 16.7.3 or older.
Suppose your project contains a `package.json` file, no `api` directory, and no `vercel.json` configuration. In that case, it is expected to provide a `build` `public` directory at the root of your project.
When properly configured, your `package.json` file would look similar to this:
package.json
```
{
  "scripts": {
    "build": "[my-framework] build --output public"
  }
}
```

An example `build` script in a `package.json` file that specifies the output directory.
Once you have defined the `build` `package.json` purely to provide dependencies for your Vercel functions located inside the `api` directory.
