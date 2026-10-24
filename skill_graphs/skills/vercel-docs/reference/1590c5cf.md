##  [Setting up your CI provider](https://vercel.com/docs/getting-started-with-vercel#setting-up-your-ci-provider)[](https://vercel.com/docs/getting-started-with-vercel#setting-up-your-ci-provider)
The instructions below are for
  1. Create a [Vercel authentication token](https://vercel.com/docs/rest-api#creating-an-access-token) on the [Tokens](https://vercel.com/account/tokens) page. For security reasons, you should use a different token from the one you created for Vercel in the previous step
  2. Once you have a new token, add it as a secret named `VERCEL_TOKEN` to your GitHub repository or organization. To learn more about how to add secrets,
  3. Finally, create a [Conformance](https://vercel.com/docs/conformance) and assumes that you're using


.github/workflows/conformance.yml
```
name: Conformance

on:
  pull_request:
    branches:
      - main

jobs:
  conformance:
    name: 'Run Conformance'
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v3

      - name: Set up Node.js
        uses: actions/setup-node@v4
        with:
          node-version-file: '.node-version'

      - name: Set up pnpm
        uses: pnpm/action-setup@v3

      - name: Set up Vercel private registry
        run: npm config set //vercel-private-registry.vercel.sh/:_authToken $VERCEL_TOKEN
        env:
          VERCEL_TOKEN: ${{ secrets.VERCEL_TOKEN }}

      - name: Install dependencies
        run: pnpm install

      - name: Run Conformance
        run: pnpm conformance
        env:
          VERCEL_TOKEN: ${{ secrets.VERCEL_TOKEN }}
```

By default, GitHub workflows are not required. To require the workflow in your repository, Require status checks to pass before merging.
* * *
[ Previous Vercel Documentation ](https://vercel.com/docs)[ Next Projects and Deployments ](https://vercel.com/docs/getting-started-with-vercel/projects-deployments)
Was this helpful?
Send
On this page
  * [Setting up your local environment](https://vercel.com/docs/getting-started-with-vercel#setting-up-your-local-environment)
  * [Set up your workspace](https://vercel.com/docs/getting-started-with-vercel#set-up-your-workspace)
  * [Setting registry server using modern versions of Yarn](https://vercel.com/docs/getting-started-with-vercel#setting-registry-server-using-modern-versions-of-yarn)
  * [Log in to the private registry](https://vercel.com/docs/getting-started-with-vercel#log-in-to-the-private-registry)
  * [Setting token using modern versions of Yarn](https://vercel.com/docs/getting-started-with-vercel#setting-token-using-modern-versions-of-yarn)
  * [Verify your setup](https://vercel.com/docs/getting-started-with-vercel#verify-your-setup)
  * [Optionally set up a pre-install message for missing credentials](https://vercel.com/docs/getting-started-with-vercel#optionally-set-up-a-pre-install-message-for-missing-credentials)
  * [Setting up Vercel](https://vercel.com/docs/getting-started-with-vercel#setting-up-vercel)
  * [Setting up your CI provider](https://vercel.com/docs/getting-started-with-vercel#setting-up-your-ci-provider)


Copy as MarkdownGive feedbackAsk AI about this page
