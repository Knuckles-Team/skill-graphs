##  [Finalizing the deployment](https://vercel.com/docs/getting-started-with-vercel#finalizing-the-deployment)[](https://vercel.com/docs/getting-started-with-vercel#finalizing-the-deployment)
Once the build produces its output, Vercel uploads everything to the appropriate storage. Static assets go to globally distributed storage where they can be served from [CDN](https://vercel.com/docs/cdn) locations close to your users. Vercel Functions are deployed to [compute regions](https://vercel.com/docs/functions/configuring-functions/region) where they can handle dynamic requests.
The routing metadata propagates across Vercel's network, ensuring every point of presence knows how to handle requests for your new deployment. Finally, Vercel assigns a unique URL to the [deployment](https://vercel.com/docs/deployments/overview) and, if this is a production deployment, updates your [production domain](https://vercel.com/docs/projects/domains) to point to the new build.
Your application is now live. When users visit your site, their requests flow through the infrastructure described in [How requests flow through Vercel](https://vercel.com/docs/getting-started-with-vercel/fundamental-concepts/infrastructure), hitting the cache for static content and invoking your functions for dynamic responses.
### [Configure a Build Customize build commands, output directories, environment variables, and build machine resources. ](https://vercel.com/docs/deployments/configure-a-build)### [Build Output API Learn about the specification that enables any framework to deploy to Vercel. ](https://vercel.com/docs/build-output-api)
* * *
[ Previous Vercel Documentation ](https://vercel.com/docs)[ Next Projects and Deployments ](https://vercel.com/docs/getting-started-with-vercel/projects-deployments)
Was this helpful?
Send
On this page
  * [Starting a build](https://vercel.com/docs/getting-started-with-vercel#starting-a-build)
  * [The build environment](https://vercel.com/docs/getting-started-with-vercel#the-build-environment)
  * [Understanding your project](https://vercel.com/docs/getting-started-with-vercel#understanding-your-project)
  * [Installing dependencies](https://vercel.com/docs/getting-started-with-vercel#installing-dependencies)
  * [Running the build](https://vercel.com/docs/getting-started-with-vercel#running-the-build)
  * [Producing output](https://vercel.com/docs/getting-started-with-vercel#producing-output)
  * [Finalizing the deployment](https://vercel.com/docs/getting-started-with-vercel#finalizing-the-deployment)


Copy as MarkdownGive feedbackAsk AI about this page
