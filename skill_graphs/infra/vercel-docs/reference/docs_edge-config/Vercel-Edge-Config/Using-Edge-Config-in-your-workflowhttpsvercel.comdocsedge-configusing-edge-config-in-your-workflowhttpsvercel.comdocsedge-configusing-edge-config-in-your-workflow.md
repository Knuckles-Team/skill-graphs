##  [Using Edge Config in your workflow](https://vercel.com/docs/edge-config#using-edge-config-in-your-workflow)[](https://vercel.com/docs/edge-config#using-edge-config-in-your-workflow)
If you'd like to know whether or not Edge Config can be integrated into your workflow, it's worth knowing the following:
  * You can have one or more Edge Configs per Vercel account, depending on your plan as explained in [Limits](https://vercel.com/docs/edge-config/edge-config-limits)
  * You can use multiple Edge Configs in one Vercel project
  * Each Edge Config can be accessed by multiple Vercel projects
  * Edge Configs can be scoped to different environments within projects using environment variables
  * Edge Config access is secure by default. A [read access token](https://vercel.com/docs/edge-config/using-edge-config#creating-a-read-access-token) is required to read from them, and an [API token](https://vercel.com/docs/rest-api#creating-an-access-token) is required to write to them


See [our Edge Config limits docs to learn more](https://vercel.com/docs/edge-config/edge-config-limits)
