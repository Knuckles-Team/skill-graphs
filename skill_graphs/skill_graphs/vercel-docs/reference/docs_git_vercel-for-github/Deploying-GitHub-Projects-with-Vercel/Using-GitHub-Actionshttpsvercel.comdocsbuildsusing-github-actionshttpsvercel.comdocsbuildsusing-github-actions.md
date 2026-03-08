##  [Using GitHub Actions](https://vercel.com/docs/builds#using-github-actions)[](https://vercel.com/docs/builds#using-github-actions)
You can use GitHub Actions to build and deploy your Vercel Application. This approach is necessary to enable Vercel with GitHub Enterprise Server (GHES) with Vercel, as GHES cannot use Vercel’s built-in Git integration.
  1. Create a GitHub Action to build your project and deploy it to Vercel. Make sure to install the Vercel CLI (`npm install --global vercel@latest`) and pull your environment variables `vercel pull --yes --environment=preview --token=${{ secrets.VERCEL_TOKEN }}`
  2. Use `vercel build` to build your project inside GitHub Actions, without exposing your source code to Vercel
  3. Then use `vercel deploy --prebuilt` to skip the build step on Vercel and upload the previously generated `.vercel/output` folder from your GitHub Action to Vercel


You'll need to make GitHub Actions for preview (non-`main` pushes) and production (`main` pushes) deployments. [Learn more about how to configure GitHub Actions and Vercel](https://vercel.com/kb/guide/how-can-i-use-github-actions-with-vercel) for custom CI/CD workflows.
###  [Repository dispatch events](https://vercel.com/docs/builds#repository-dispatch-events)[](https://vercel.com/docs/builds#repository-dispatch-events)
This event will only trigger a workflow run if the workflow file exists on the default branch (e.g. `main`). If you'd like to test the workflow prior to merging to `main`, we recommend adding a
Vercel sends
GitHub Actions can trigger on the following events:
```
on:
  repository_dispatch:
    - 'vercel.deployment.ready'
    - 'vercel.deployment.success'
    - 'vercel.deployment.error'
    - 'vercel.deployment.canceled'
    # canceled as a result of the ignored build script
    - 'vercel.deployment.ignored'
    # canceled as a result of automatic deployment skipping https://vercel.com/docs/monorepos#skipping-unaffected-projects
    - 'vercel.deployment.skipped'
    - 'vercel.deployment.pending'
    - 'vercel.deployment.failed'
    - 'vercel.deployment.promoted'
```

`repository_dispatch` events contain a JSON payload with information about the deployment, such as deployment `url` and deployment `environment`. GitHub Actions can access this payload through `github.event.client_payload`. For example, accessing the URL of your triggering deployment through `github.event.client_payload.url`.
Read more and see the [how can I run end-to-end tests after my Vercel preview deployment?](https://vercel.com/kb/guide/how-can-i-run-end-to-end-tests-after-my-vercel-preview-deployment) guide for a practical example.
####  [Migrating from `deployment_status`](https://vercel.com/docs/builds#migrating-from-deployment_status)[](https://vercel.com/docs/builds#migrating-from-deployment_status)
With `repository_dispatch`, the dispatch event `client_payload` contains details about your deployment allowing you to reduce GitHub Actions costs and complexity in your workflows.
For example, to migrate the GitHub Actions trigger for preview deployments for end-to-end tests:
Previously, we needed to check if the status of a deployment was successful. Now, with `repository_dispatch` we can trigger our workflow only on a successful deployment by specifying the `'vercel.deployment.success'` dispatch type.
Since we're no longer using the `deployment_status` event, we need to get the `url` from the `vercel.deployment.success` event's `client_payload`.
```
name: End to End Tests

on:
- deployment_status:
+ repository_dispatch:
+   types:
+    - 'vercel.deployment.success'
jobs:
  run-e2es:
-   if: github.event_name == 'deployment_status' && github.event.deployment_status.state == 'success'
+   if: github.event_name == 'repository_dispatch'
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Install dependencies
        run: npm ci && npx playwright install --with-deps
      - name: Run tests
        run: npx playwright test
        env:
-         BASE_URL: ${{ github.event.deployment_status.environment_url }}
+         BASE_URL: ${{ github.event.client_payload.url }}
```

* * *
[ Previous AI/ Agent Resources ](https://vercel.com/docs/agent-resources)[ Next Build Features ](https://vercel.com/docs/builds/build-features)
Was this helpful?
Send
On this page
  * [Supported GitHub Products](https://vercel.com/docs/builds#supported-github-products)
  * [Deploying a GitHub Repository](https://vercel.com/docs/builds#deploying-a-github-repository)
  * [Changing the GitHub Repository of a Project](https://vercel.com/docs/builds#changing-the-github-repository-of-a-project)
  * [A Deployment for Each Push](https://vercel.com/docs/builds#a-deployment-for-each-push)
  * [Updating the Production Domain](https://vercel.com/docs/builds#updating-the-production-domain)
  * [Preview URLs for the Latest Changes for Each Pull Request](https://vercel.com/docs/builds#preview-urls-for-the-latest-changes-for-each-pull-request)
  * [Deployment Authorizations for Forks](https://vercel.com/docs/builds#deployment-authorizations-for-forks)
  * [Configuring for GitHub](https://vercel.com/docs/builds#configuring-for-github)
  * [System environment variables](https://vercel.com/docs/builds#system-environment-variables)
  * [VERCEL_GIT_PROVIDER](https://vercel.com/docs/builds#VERCEL_GIT_PROVIDER)
  * [VERCEL_GIT_REPO_SLUG](https://vercel.com/docs/builds#VERCEL_GIT_REPO_SLUG)
  * [VERCEL_GIT_REPO_OWNER](https://vercel.com/docs/builds#VERCEL_GIT_REPO_OWNER)
  * [VERCEL_GIT_REPO_ID](https://vercel.com/docs/builds#VERCEL_GIT_REPO_ID)
  * [VERCEL_GIT_COMMIT_REF](https://vercel.com/docs/builds#VERCEL_GIT_COMMIT_REF)
  * [VERCEL_GIT_COMMIT_SHA](https://vercel.com/docs/builds#VERCEL_GIT_COMMIT_SHA)
  * [VERCEL_GIT_COMMIT_MESSAGE](https://vercel.com/docs/builds#VERCEL_GIT_COMMIT_MESSAGE)
  * [VERCEL_GIT_COMMIT_AUTHOR_LOGIN](https://vercel.com/docs/builds#VERCEL_GIT_COMMIT_AUTHOR_LOGIN)
  * [VERCEL_GIT_COMMIT_AUTHOR_NAME](https://vercel.com/docs/builds#VERCEL_GIT_COMMIT_AUTHOR_NAME)
  * [VERCEL_GIT_PULL_REQUEST_ID](https://vercel.com/docs/builds#VERCEL_GIT_PULL_REQUEST_ID)
  * [Repository Permissions](https://vercel.com/docs/builds#repository-permissions)
  * [Organization Permissions](https://vercel.com/docs/builds#organization-permissions)
  * [User Permissions](https://vercel.com/docs/builds#user-permissions)
  * [Missing Git repository](https://vercel.com/docs/builds#missing-git-repository)
  * [Personal account repositories](https://vercel.com/docs/builds#personal-account-repositories)
  * [Organization repositories](https://vercel.com/docs/builds#organization-repositories)
  * [Silence GitHub comments](https://vercel.com/docs/builds#silence-github-comments)
  * [Silence deployment notifications on pull requests](https://vercel.com/docs/builds#silence-deployment-notifications-on-pull-requests)
  * [Using GitHub Actions](https://vercel.com/docs/builds#using-github-actions)
  * [Repository dispatch events](https://vercel.com/docs/builds#repository-dispatch-events)
  * [Migrating from deployment_status](https://vercel.com/docs/builds#migrating-from-deployment_status)


Copy as MarkdownGive feedbackAsk AI about this page
