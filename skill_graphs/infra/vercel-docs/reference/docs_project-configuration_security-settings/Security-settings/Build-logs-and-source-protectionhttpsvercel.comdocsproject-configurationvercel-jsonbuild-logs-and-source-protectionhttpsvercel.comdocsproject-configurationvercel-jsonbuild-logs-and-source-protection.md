##  [Build logs and source protection](https://vercel.com/docs/project-configuration/vercel-json#build-logs-and-source-protection)[](https://vercel.com/docs/project-configuration/vercel-json#build-logs-and-source-protection)
By default, the following paths mentioned below can only be accessed by you and authenticated members of your Vercel team:
  * `/_src`: Displays the source code and build output.
  * `/_logs`: Displays the build logs.


Disabling Build Logs and Source Protection will make your source code and logs publicly accessible. Do not edit this setting if you don't want them to be publicly accessible.



None of your existing deployments will be affected when you toggle this setting. If you’d like to make the source code or logs private on your existing deployments, the only option is to delete these deployments.
This setting is overwritten when a deployment is created using Vercel CLI with the [`--public` option](https://vercel.com/docs/cli/deploy#public) or the [`public` property](https://vercel.com/docs/project-configuration#public) is used in `vercel.json`.
For deployments created before July 9th, 2020 at 7:05 AM (UTC), only the Project Settings is considered for determining whether the deployment's Logs and Source are publicly accessible or not. It doesn't matter if the `--public` flag was passed when creating those Deployments.
