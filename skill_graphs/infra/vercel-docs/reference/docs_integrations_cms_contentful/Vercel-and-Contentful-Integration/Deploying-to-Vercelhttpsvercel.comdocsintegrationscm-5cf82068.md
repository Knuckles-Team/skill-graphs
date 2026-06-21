##  [Deploying to Vercel](https://vercel.com/docs/integrations/cms/contentful#deploying-to-vercel)[](https://vercel.com/docs/integrations/cms/contentful#deploying-to-vercel)
Now that you have your application wired up to Contentful, you can deploy it to Vercel to get your site online. You can either use the Vercel CLI or the Git integrations to deploy your code. Let’s use the Git integration.
  1. ###  [Publish your code to Git](https://vercel.com/docs/integrations/cms/contentful#publish-your-code-to-git)[](https://vercel.com/docs/integrations/cms/contentful#publish-your-code-to-git)
Push your code to your git repository (e.g. GitHub, GitLab, or BitBucket).
terminal
```
git init
git add .
git commit -m "Initial commit"
git remote add origin
git push -u origin master
```

  2. ###  [Import your project into Vercel](https://vercel.com/docs/integrations/cms/contentful#import-your-project-into-vercel)[](https://vercel.com/docs/integrations/cms/contentful#import-your-project-into-vercel)
Log in to your Vercel account (or create one) and import your project into Vercel using the [import flow](https://vercel.com/new).
![](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fintegrations%2Fcontentful%2Fimport-to-vercel.png&w=3840&q=75)![](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fintegrations%2Fcontentful%2Fimport-vercel-dark.png&w=3840&q=75)
Vercel will detect that you are using Next.js and will enable the correct settings for your deployment.
  3. ###  [Add Environment Variables](https://vercel.com/docs/integrations/cms/contentful#add-environment-variables)[](https://vercel.com/docs/integrations/cms/contentful#add-environment-variables)
Add the `CONTENTFUL_SPACE_ID` and `CONTENTFUL_ACCESS_TOKEN` Environment Variables from your `.env.local` file by copying and pasting it under the Environment Variables section.
terminal
```
CONTENTFUL_SPACE_ID='your-space-id'
CONTENTFUL_ACCESS_TOKEN='your-content-api-token'
```

![](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fintegrations%2Fcontentful%2Fadd-env-vars.png&w=3840&q=75)![](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fintegrations%2Fcontentful%2Fadd-env-vars-dark.png&w=3840&q=75)
Click "Deploy" and your application will be live on Vercel!
![](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fintegrations%2Fcontentful%2Fdeployed.png&w=3840&q=75)![](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fintegrations%2Fcontentful%2Fdeployed-dark.png&w=3840&q=75)


###  [Content Link](https://vercel.com/docs/integrations/cms/contentful#content-link)[](https://vercel.com/docs/integrations/cms/contentful#content-link)
Content Link is available on [Enterprise](https://vercel.com/docs/plans/enterprise) and [Pro](https://vercel.com/docs/plans/pro) plans
Content Link enables you to edit content on websites using headless CMSs by providing links on elements that match a content model in the CMS. This real-time content visualization allows collaborators to make changes without needing a developer's assistance.
You can enable Content Link on a preview deployment by selecting Edit Mode in the [Vercel Toolbar](https://vercel.com/docs/vercel-toolbar) menu.
The corresponding model in the CMS determines an editable field. You can hover over an element to display a link in the top-right corner of the element and then select the link to open the related CMS field for editing.
You don't need any additional configuration or code changes on the page to use this feature.
To implement Content Link in your project, follow the steps in
* * *
[ Previous ButterCMS ](https://vercel.com/docs/integrations/cms/butter-cms)[ Next DatoCMS ](https://vercel.com/docs/integrations/cms/dato-cms)
Was this helpful?
Send
On this page
  * [Getting started](https://vercel.com/docs/integrations/cms/contentful#getting-started)
  * [Clone the repository](https://vercel.com/docs/integrations/cms/contentful#clone-the-repository)
  * [Create a Contentful Account](https://vercel.com/docs/integrations/cms/contentful#create-a-contentful-account)
  * [Retrieve your Contentful Space ID](https://vercel.com/docs/integrations/cms/contentful#retrieve-your-contentful-space-id)
  * [Create a Content Management API token](https://vercel.com/docs/integrations/cms/contentful#create-a-content-management-api-token)
  * [Import the Content Model](https://vercel.com/docs/integrations/cms/contentful#import-the-content-model)
  * [Adding Content in Contentful](https://vercel.com/docs/integrations/cms/contentful#adding-content-in-contentful)
  * [Publish Contentful entries](https://vercel.com/docs/integrations/cms/contentful#publish-contentful-entries)
  * [Retrieve your Contentful Secrets](https://vercel.com/docs/integrations/cms/contentful#retrieve-your-contentful-secrets)
  * [Start your application](https://vercel.com/docs/integrations/cms/contentful#start-your-application)
  * [How it works](https://vercel.com/docs/integrations/cms/contentful#how-it-works)
  * [Deploying to Vercel](https://vercel.com/docs/integrations/cms/contentful#deploying-to-vercel)
  * [Publish your code to Git](https://vercel.com/docs/integrations/cms/contentful#publish-your-code-to-git)
  * [Import your project into Vercel](https://vercel.com/docs/integrations/cms/contentful#import-your-project-into-vercel)
  * [Add Environment Variables](https://vercel.com/docs/integrations/cms/contentful#add-environment-variables)
  * [Content Link](https://vercel.com/docs/integrations/cms/contentful#content-link)


Copy as MarkdownGive feedbackAsk AI about this page
