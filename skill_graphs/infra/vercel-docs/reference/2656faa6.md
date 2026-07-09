##  [outputDirectory](https://vercel.com/docs/project-configuration/vercel-json#outputdirectory)[](https://vercel.com/docs/project-configuration/vercel-json#outputdirectory)
This value overrides the [Output Directory](https://vercel.com/docs/deployments/configure-a-build#output-directory) in Project Settings.
Type: `string | null`
The `outputDirectory` property can be used to override the Output Directory in the Project Settings dashboard for a given deployment.
In the following example, the deployment will look for the `build` directory rather than the default `public` or `.` root directory. For more information on the default behavior of the Output Directory see the [Configure a Build - Output Directory](https://vercel.com/docs/deployments/configure-a-build#output-directory) section. The following example is a `vercel.json` file that overrides the `outputDirectory` to `build`:
vercel.json
```
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "outputDirectory": "build"
}
```
