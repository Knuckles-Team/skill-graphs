##  [Triggering a Deploy Hook](https://vercel.com/docs/getting-started-with-vercel#triggering-a-deploy-hook)[](https://vercel.com/docs/getting-started-with-vercel#triggering-a-deploy-hook)
To trigger a Deploy Hook, send a GET or POST request to the provided URL.
Deploy Hooks will not be triggered if you have the `github.enabled = false` [configuration](https://vercel.com/docs/project-configuration/git-configuration#github.enabled) present in your `vercel.json` file.
Here's an example request and response you can use for testing:
####  [Example Request](https://vercel.com/docs/getting-started-with-vercel#example-request)[](https://vercel.com/docs/getting-started-with-vercel#example-request)
example-request
```
curl -X POST https://api.vercel.com/v1/integrations/deploy/prj_98g22o5YUFVHlKOzj9vKPTyN2SDG/tKybBxqhQs
```

####  [Example Response](https://vercel.com/docs/getting-started-with-vercel#example-response)[](https://vercel.com/docs/getting-started-with-vercel#example-response)
example-response
```
{
  "job": {
    "id": "okzCd50AIap1O31g0gne",
    "state": "PENDING",
    "createdAt": 1662825789999
  }
}
```

You do not need to add an authorization header. See [Security](https://vercel.com/docs/getting-started-with-vercel#security) to learn more.
After sending a request, you can see that it triggered a deployment on your project dashboard.
![](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fgit%2Fdeploy-hook-deployed-light.png&w=3840&q=75)![](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fgit%2Fdeploy-hook-deployed-dark.png&w=3840&q=75)
Deployments triggered by a Deploy Hook are marked in the list.
