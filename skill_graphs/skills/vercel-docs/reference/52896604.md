##  [Deploying to Vercel](https://vercel.com/docs/integrations/cms/agility-cms#deploying-to-vercel)[](https://vercel.com/docs/integrations/cms/agility-cms#deploying-to-vercel)
  1. ###  [Push to Git](https://vercel.com/docs/integrations/cms/agility-cms#push-to-git)[](https://vercel.com/docs/integrations/cms/agility-cms#push-to-git)
Ensure your integrated application code is pushed to your git repository.
terminal
```
git init
git add .
git commit -m "Initial commit"
git remote add origin [repository url]
git push -u origin main
```

  2. ###  [Import to Vercel](https://vercel.com/docs/integrations/cms/agility-cms#import-to-vercel)[](https://vercel.com/docs/integrations/cms/agility-cms#import-to-vercel)
Log in to your Vercel account (or create one) and import your project into Vercel using the [import flow](https://vercel.com/new).
![](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fintegrations%2Fsitecore%2Fimport-vercel-light.png&w=3840&q=75)![](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fintegrations%2Fsitecore%2Fimport-vercel-dark.png&w=3840&q=75)
  3. ###  [Configure environment variables](https://vercel.com/docs/integrations/cms/agility-cms#configure-environment-variables)[](https://vercel.com/docs/integrations/cms/agility-cms#configure-environment-variables)
Add the `FETCH_WITH`, `JSS_APP_NAME`, `GRAPH_QL_ENDPOINT` , `SITECORE_API_KEY`, and `SITECORE_API_HOST` environment variables to the Environment Variables section.
.env.local
```
JSS_APP_NAME='your-jss-app-name'
GRAPH_QL_ENDPOINT='your-graphql-endpoint'
SITECORE_API_KEY='your-sitecore-api-key'
SITECORE_API_HOST='host-from-endpoint'
FETCH_WITH='GraphQL'
```

Select "Deploy" and your application will be live on Vercel!
![](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fintegrations%2Fsitecore%2Fsuccess-vercel-light.png&w=3840&q=75)![](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fintegrations%2Fsitecore%2Fsuccess-vercel-dark.png&w=3840&q=75)


* * *
[ Previous CMS Integrations ](https://vercel.com/docs/integrations/cms)[ Next ButterCMS ](https://vercel.com/docs/integrations/cms/butter-cms)
Was this helpful?
Send
On this page
  * [Setting up an XM Cloud project, environment, and website](https://vercel.com/docs/integrations/cms/agility-cms#setting-up-an-xm-cloud-project-environment-and-website)
  * [Access XM Cloud Deploy app](https://vercel.com/docs/integrations/cms/agility-cms#access-xm-cloud-deploy-app)
  * [Initiate project creation](https://vercel.com/docs/integrations/cms/agility-cms#initiate-project-creation)
  * [Select project foundation](https://vercel.com/docs/integrations/cms/agility-cms#select-project-foundation)
  * [Select starter template](https://vercel.com/docs/integrations/cms/agility-cms#select-starter-template)
  * [Name your project](https://vercel.com/docs/integrations/cms/agility-cms#name-your-project)
  * [Select source control provider](https://vercel.com/docs/integrations/cms/agility-cms#select-source-control-provider)
  * [Set up source control connection](https://vercel.com/docs/integrations/cms/agility-cms#set-up-source-control-connection)
  * [Specify repository name](https://vercel.com/docs/integrations/cms/agility-cms#specify-repository-name)
  * [Configure environment details](https://vercel.com/docs/integrations/cms/agility-cms#configure-environment-details)
  * [Finalize setup](https://vercel.com/docs/integrations/cms/agility-cms#finalize-setup)
  * [Create a new website](https://vercel.com/docs/integrations/cms/agility-cms#create-a-new-website)
  * [Publish the site](https://vercel.com/docs/integrations/cms/agility-cms#publish-the-site)
  * [Creating a Next.js JSS application](https://vercel.com/docs/integrations/cms/agility-cms#creating-a-next.js-jss-application)
  * [Clone the repository](https://vercel.com/docs/integrations/cms/agility-cms#clone-the-repository)
  * [Retrieve your API key, GraphQL endpoint, and JSS app name](https://vercel.com/docs/integrations/cms/agility-cms#retrieve-your-api-key-graphql-endpoint-and-jss-app-name)
  * [Configure your Next.js JSS application](https://vercel.com/docs/integrations/cms/agility-cms#configure-your-next.js-jss-application)
  * [Start your application](https://vercel.com/docs/integrations/cms/agility-cms#start-your-application)
  * [How it works](https://vercel.com/docs/integrations/cms/agility-cms#how-it-works)
  * [Deploying to Vercel](https://vercel.com/docs/integrations/cms/agility-cms#deploying-to-vercel)
  * [Push to Git](https://vercel.com/docs/integrations/cms/agility-cms#push-to-git)
  * [Import to Vercel](https://vercel.com/docs/integrations/cms/agility-cms#import-to-vercel)
  * [Configure environment variables](https://vercel.com/docs/integrations/cms/agility-cms#configure-environment-variables)


Copy as MarkdownGive feedbackAsk AI about this page
