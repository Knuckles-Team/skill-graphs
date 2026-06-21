##  [Project Redirects](https://vercel.com/docs/how-vercel-cdn-works#project-redirects)[](https://vercel.com/docs/how-vercel-cdn-works#project-redirects)
Project-level redirects let you create and update bulk redirects without needing to redeploy. Redirects are staged when created and can be immediately published to production without a new deployment.
  1. ###  [Navigate to the Redirects tab](https://vercel.com/docs/how-vercel-cdn-works#navigate-to-the-redirects-tab)[](https://vercel.com/docs/how-vercel-cdn-works#navigate-to-the-redirects-tab)
From your [dashboard](https://vercel.com/dashboard), select your project and click the [Redirects](https://vercel.com/d?to=%2F%5Bteam%5D%2F%5Bproject%5D%2Fredirects&title=Go+to+Redirects).
  2. ###  [Create a redirect](https://vercel.com/docs/how-vercel-cdn-works#create-a-redirect)[](https://vercel.com/docs/how-vercel-cdn-works#create-a-redirect)
Click Create and enter the following:
     * Source: The path to redirect from (e.g., `/old-page`)
     * Destination: The path or URL to redirect to (e.g., `/new-page`)
     * Status code: Select `307` (temporary) or `308` (permanent)
You can also configure whether the redirect should be case sensitive (default `false`) or whether query parameters should be preserved (default `false`).
  3. ###  [Test your changes](https://vercel.com/docs/how-vercel-cdn-works#test-your-changes)[](https://vercel.com/docs/how-vercel-cdn-works#test-your-changes)
New redirects are staged until you publish them. From the review redirects dialog, click on the source path for each redirect to open a staging URL where the new redirects are applied.
  4. ###  [Publish your changes](https://vercel.com/docs/how-vercel-cdn-works#publish-your-changes)[](https://vercel.com/docs/how-vercel-cdn-works#publish-your-changes)
After testing your redirects, click Publish to make your changes live.


###  [Editing and deleting redirects](https://vercel.com/docs/how-vercel-cdn-works#editing-and-deleting-redirects)[](https://vercel.com/docs/how-vercel-cdn-works#editing-and-deleting-redirects)
To edit or delete a redirect:
  1. From the Redirects tab, find the redirect you want to modify.
  2. Click the three dots menu on the right side of the redirect row.
  3. Select Edit or Delete.
  4. Click Publish to apply your changes.


###  [Bulk upload](https://vercel.com/docs/how-vercel-cdn-works#bulk-upload)[](https://vercel.com/docs/how-vercel-cdn-works#bulk-upload)
You can upload multiple redirects at once:
  1. From the Redirects tab, click the Create button and click CSV.
  2. Select a CSV file containing your redirects.
  3. Review the changes and click Publish.


###  [Using the CLI](https://vercel.com/docs/how-vercel-cdn-works#using-the-cli)[](https://vercel.com/docs/how-vercel-cdn-works#using-the-cli)
You can manage redirects using the [Vercel CLI](https://vercel.com/docs/cli/redirects). Make sure that you are using at least version `49.1.3` of the CLI.
terminal
```
# List all redirects
vercel redirects ls

# List all redirects versions
vercel redirects ls-versions

# Add a redirect
vercel redirects add /old-path /new-path --permanent

# Bulk upload CSV files
vercel redirects upload my-redirects.csv

# Remove a redirect
vercel redirects rm /old-path

# Promote staging redirects
vercel redirects promote 596558a5-24cd-4b94-b91a-d1f4171b7c3f
```

###  [Using the API](https://vercel.com/docs/how-vercel-cdn-works#using-the-api)[](https://vercel.com/docs/how-vercel-cdn-works#using-the-api)
You can also manage redirects programmatically through the [Vercel REST API](https://vercel.com/docs/rest-api/reference/endpoints/bulk-redirects). This is useful for automating redirect management from webhook events, such as managing redirects in a CMS and instantly updating Vercel with changes.
terminal
```
curl -X PUT "https://api.vercel.com/v1/bulk-redirects" \
  -H "Authorization: Bearer $VERCEL_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "teamId": "team_123",
    "projectId": "project_123",
    "redirects": [
      {
        "source": "/old-path",
        "destination": "/new-path",
        "permanent": true
      }
    ]
  }'
```

* * *
[ Previous Overview ](https://vercel.com/docs/cdn)[ Next Compression ](https://vercel.com/docs/how-vercel-cdn-works/compression)
Was this helpful?
Send
On this page
  * [Deployment-time redirects](https://vercel.com/docs/how-vercel-cdn-works#deployment-time-redirects)
  * [Create your redirect file](https://vercel.com/docs/how-vercel-cdn-works#create-your-redirect-file)
  * [Configure bulkRedirectsPath](https://vercel.com/docs/how-vercel-cdn-works#configure-bulkredirectspath)
  * [Deploy](https://vercel.com/docs/how-vercel-cdn-works#deploy)
  * [Project Redirects](https://vercel.com/docs/how-vercel-cdn-works#project-redirects)
  * [Navigate to the Redirects tab](https://vercel.com/docs/how-vercel-cdn-works#navigate-to-the-redirects-tab)
  * [Create a redirect](https://vercel.com/docs/how-vercel-cdn-works#create-a-redirect)
  * [Test your changes](https://vercel.com/docs/how-vercel-cdn-works#test-your-changes)
  * [Publish your changes](https://vercel.com/docs/how-vercel-cdn-works#publish-your-changes)
  * [Editing and deleting redirects](https://vercel.com/docs/how-vercel-cdn-works#editing-and-deleting-redirects)
  * [Bulk upload](https://vercel.com/docs/how-vercel-cdn-works#bulk-upload)
  * [Using the CLI](https://vercel.com/docs/how-vercel-cdn-works#using-the-cli)
  * [Using the API](https://vercel.com/docs/how-vercel-cdn-works#using-the-api)


Copy as MarkdownGive feedbackAsk AI about this page
