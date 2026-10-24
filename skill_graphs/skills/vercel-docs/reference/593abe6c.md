# vercel build
Last updated January 13, 2026
The `vercel build` command can be used to build a Vercel Project locally or in your own CI environment. Build artifacts are placed into the `.vercel/output` directory according to the [Build Output API](https://vercel.com/docs/build-output-api/v3).
When used in conjunction with the `vercel deploy --prebuilt` command, this allows a Vercel Deployment to be created _without_ sharing the Vercel Project's source code with Vercel.
This command can also be helpful in debugging a Vercel Project by receiving error messages for a failed build locally, or by inspecting the resulting build artifacts to get a better understanding of how Vercel will create the Deployment.
It is recommended to run the `vercel pull` command before invoking `vercel build` to ensure that you have the most recent Project Settings and Environment Variables stored locally.
