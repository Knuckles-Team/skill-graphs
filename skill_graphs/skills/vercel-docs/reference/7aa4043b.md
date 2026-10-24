##  [How to link projects together in a monorepo](https://vercel.com/docs/deployment-checks#how-to-link-projects-together-in-a-monorepo)[](https://vercel.com/docs/deployment-checks#how-to-link-projects-together-in-a-monorepo)
When working in a monorepo with multiple applications (such as a frontend and a backend), it can be challenging to manage the connection strings between environments to ensure a seamless experience. Traditionally, referencing one project from another requires manually setting URLs or environment variables for each deployment, in _every_ environment.
With Related Projects, this process is streamlined, enabling teams to:
  * Verify changes in pre-production environments without manually updating URLs or environment variables.
  * Eliminate misconfigurations when referencing internal services across multiple deployments, and environments.


For example, if your monorepo contains:
  1. A frontend project that fetches data from an API
  2. A backend API project that serves the data


Related Projects can ensure that each preview deployment of the frontend automatically references the corresponding preview deployment of the backend, avoiding the need for hardcoded environment variables when testing changes that span both projects.
###  [Requirements](https://vercel.com/docs/deployment-checks#requirements)[](https://vercel.com/docs/deployment-checks#requirements)
  * A maximum of 3 projects can be linked together
  * Only supports projects within the same repository
  * CLI deployments are not supported


###  [Getting started](https://vercel.com/docs/deployment-checks#getting-started)[](https://vercel.com/docs/deployment-checks#getting-started)
  1. ###  [Define Related Projects](https://vercel.com/docs/deployment-checks#define-related-projects)[](https://vercel.com/docs/deployment-checks#define-related-projects)
Specify the projects your app needs to reference in a `vercel.json` configuration file at the root of the app. While every app in your monorepo can list related projects in their own `vercel.json`, you can only specify up to three related projects per app.
apps/frontend/vercel.json
```
{
  "relatedProjects": ["prj_123"]
}
```

This will make the preview, and production hosts of `prj_123` available as an environment variable in the deployment of the `frontend` project.
You can [find your project ID](https://vercel.com/d?to=%2F%5Bteam%5D%2F%5Bproject%5D%2Fsettings%23project-id&title=Find+your+Vercel+project+ID) in the project Settings page in the Vercel dashboard.
  2. ###  [Retrieve Related Project Information](https://vercel.com/docs/deployment-checks#retrieve-related-project-information)[](https://vercel.com/docs/deployment-checks#retrieve-related-project-information)
The next deployment will have the `VERCEL_RELATED_PROJECTS` environment variable set containing the urls of the related projects for use.
View the data provided for each project in the
To access this information, you can use the
Terminal
```
```
npm i @vercel/related-projects
```
`
```

```
```
bun add @vercel/related-projects
```
`
```

```
```
yarn add @vercel/related-projects
```
`
```

```
```
pnpm add @vercel/related-projects
```
`
```

    1. Easily reference hosts of related projects
```
import { withRelatedProject } from '@vercel/related-projects';

const apiHost = withRelatedProject({
  projectName: 'my-api-project',
  /**
   * Specify a default host that will be used for my-api-project if the related project
   * data cannot be parsed or is missing.
   */
  defaultHost: process.env.API_HOST,
});
```

    1. Retrieve just the related project data:
index.ts
```
import {
  relatedProjects,
  type VercelRelatedProject,
} from '@vercel/related-projects';

// fully typed project data
const projects: VercelRelatedProject[] = relatedProjects();
```



* * *
[ Previous Deploy Hooks ](https://vercel.com/docs/deploy-hooks)[ Next Deployment Retention ](https://vercel.com/docs/deployment-retention)
Was this helpful?
Send
On this page
  * [Deploy a template monorepo](https://vercel.com/docs/deployment-checks#deploy-a-template-monorepo)
  * [Add a monorepo through the Vercel Dashboard](https://vercel.com/docs/deployment-checks#add-a-monorepo-through-the-vercel-dashboard)
  * [Add a monorepo through Vercel CLI](https://vercel.com/docs/deployment-checks#add-a-monorepo-through-vercel-cli)
  * [When does a monorepo build occur?](https://vercel.com/docs/deployment-checks#when-does-a-monorepo-build-occur)
  * [Skipping unaffected projects](https://vercel.com/docs/deployment-checks#skipping-unaffected-projects)
  * [Requirements](https://vercel.com/docs/deployment-checks#requirements)
  * [Disable the skipping unaffected projects feature](https://vercel.com/docs/deployment-checks#disable-the-skipping-unaffected-projects-feature)
  * [Ignoring the build step](https://vercel.com/docs/deployment-checks#ignoring-the-build-step)
  * [How to link projects together in a monorepo](https://vercel.com/docs/deployment-checks#how-to-link-projects-together-in-a-monorepo)
  * [Requirements](https://vercel.com/docs/deployment-checks#requirements)
  * [Getting started](https://vercel.com/docs/deployment-checks#getting-started)
  * [Define Related Projects](https://vercel.com/docs/deployment-checks#define-related-projects)
  * [Retrieve Related Project Information](https://vercel.com/docs/deployment-checks#retrieve-related-project-information)


Copy as MarkdownGive feedbackAsk AI about this page
