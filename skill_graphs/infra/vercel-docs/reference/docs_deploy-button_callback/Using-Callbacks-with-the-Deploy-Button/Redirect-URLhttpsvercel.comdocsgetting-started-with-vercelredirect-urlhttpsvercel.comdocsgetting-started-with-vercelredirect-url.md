##  [Redirect URL](https://vercel.com/docs/getting-started-with-vercel#redirect-url)[](https://vercel.com/docs/getting-started-with-vercel#redirect-url)
Parameter | Type | Value
---|---|---
`redirect-url` | `string` | The URL to redirect the user to in the event of a successful deployment.
The Redirect URL parameter allows you to define a URL, other than the newly created Vercel project, to send the user to after a successful deployment.
This parameter is helpful if you are sending a user from an application, to deploy a project with Vercel, but want the user to continue with your application with a project created and deployed.
The example below shows a Deploy Button source URL using the Redirect URL parameter:
redirect url
```
https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Ftree%2Fcanary%2Fexamples%2Fhello-world&redirect-url=https%3A%2F%2Fmy-headless-application.com
```

Provide a custom name and logo for the redirect UI by using the [Developer ID](https://vercel.com/docs/getting-started-with-vercel#developer-id) parameter.
###  [Callback Parameters](https://vercel.com/docs/getting-started-with-vercel#callback-parameters)[](https://vercel.com/docs/getting-started-with-vercel#callback-parameters)
Vercel additionally attaches some "Callback Parameters" to the defined Redirect URL when the user is redirected. The following parameters give you access to information about the project the user has created and deployed, for you to integrate with Vercel after the user is sent back to you.
Parameter | Description
---|---
`project-dashboard-url` | The URL to view the Project that was created through the Project creation flow on the Vercel Dashboard.
`project-name` | The Name of the Project that was created through the Project creation flow.
`deployment-dashboard-url` | The URL to view the Deployment that was created through the Project creation flow on the Vercel Dashboard.
`deployment-url` | The URL of the deployment that was created through the Project creation flow. This contains the default production domain that was automatically generated for the project that was created.
`repository-url` | The URL of the Git repository that was created through the Project creation flow, within the user's selected Git account (GitHub, GitLab, or Bitbucket).
`production-deploy-hook-url` ([conditional](https://vercel.com/docs/getting-started-with-vercel#deploy-hook)) | The URL of a Deploy Hook. Requires [the `production-deploy-hook` parameter](https://vercel.com/docs/getting-started-with-vercel#deploy-hook).
