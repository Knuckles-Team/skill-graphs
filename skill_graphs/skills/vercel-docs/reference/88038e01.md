##  [Starting a build](https://vercel.com/docs/getting-started-with-vercel#starting-a-build)[](https://vercel.com/docs/getting-started-with-vercel#starting-a-build)
A build begins when Vercel receives new code to deploy. This can happen when:
  * you push a commit to a [connected Git repository](https://vercel.com/docs/deployments/git)
  * you trigger a build through the [Vercel CLI](https://vercel.com/docs/cli)
  * you deploy from the dashboard
  * you deploy from the [REST API](https://vercel.com/docs/rest-api)


When a build request arrives, Vercel first validates the request and checks your [project configuration](https://vercel.com/docs/projects/project-configuration). [Providing there is availability](https://vercel.com/docs/builds/build-queues), the build will start.
