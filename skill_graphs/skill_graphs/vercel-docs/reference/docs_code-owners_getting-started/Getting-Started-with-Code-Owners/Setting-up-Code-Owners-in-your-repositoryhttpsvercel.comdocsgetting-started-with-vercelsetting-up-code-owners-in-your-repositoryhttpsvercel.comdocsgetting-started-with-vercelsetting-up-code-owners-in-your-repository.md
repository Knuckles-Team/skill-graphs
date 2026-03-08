##  [Setting up Code Owners in your repository](https://vercel.com/docs/getting-started-with-vercel#setting-up-code-owners-in-your-repository)[](https://vercel.com/docs/getting-started-with-vercel#setting-up-code-owners-in-your-repository)
A GitHub App enables Code Owners functionality by adding reviewers and enforcing review checks for merging PRs.
  1. ###  [Set up the Vercel CLI](https://vercel.com/docs/getting-started-with-vercel#set-up-the-vercel-cli)[](https://vercel.com/docs/getting-started-with-vercel#set-up-the-vercel-cli)
The Code Owners CLI is separate to the [Vercel CLI](https://vercel.com/docs/cli), however it uses the Vercel CLI for authentication.
Before continuing, please ensure that the Vercel CLI is [installed](https://vercel.com/docs/cli#installing-vercel-cli) and that you are [logged in](https://vercel.com/docs/cli/login).
  2. ###  [Initializing Code Owners](https://vercel.com/docs/getting-started-with-vercel#initalizing-code-owners)[](https://vercel.com/docs/getting-started-with-vercel#initalizing-code-owners)
If you have an existing `CODEOWNERS` file in your repository, you can use the CLI to automatically migrate your repository to use Vercel Code Owners. Otherwise, you can skip this step.
Start by running this command in your repository's root:
Terminal
![](https://7nyt0uhk7sse4zvn.public.blob.vercel-storage.com/docs-assets/static/topics/icons/pnpm.svg)pnpm bun yarn npm
```
pnpm --package=@vercel-private/code-owners dlx vercel-code-owners init
```

```
yarn --package=@vercel-private/code-owners dlx vercel-code-owners init
```

```
npx --package=@vercel-private/code-owners -- vercel-code-owners init
```

```
bunx --package=@vercel-private/code-owners vercel-code-owners init
```

`yarn dlx` only works with Yarn version 2 or newer, for Yarn v1 use the npx command.
After running, check the installation success by executing:
Terminal
![](https://7nyt0uhk7sse4zvn.public.blob.vercel-storage.com/docs-assets/static/topics/icons/pnpm.svg)pnpm bun yarn npm
```
pnpm vercel-code-owners
```

```
yarn vercel-code-owners
```

```
npx vercel-code-owners
```

```
bunx vercel-code-owners
```

  3. ###  [Install the GitHub App into a repository](https://vercel.com/docs/getting-started-with-vercel#install-the-github-app-into-a-repository)[](https://vercel.com/docs/getting-started-with-vercel#install-the-github-app-into-a-repository)
To install, you must be an organization owner or have the GitHub App Manager permissions.
    1. Go to
    2. Choose your organization for the app installation.
    3. Select repositories for the app installation.
    4. Click `Install` to complete the app installation in the chosen repositories.
  4. ###  [Define Code Owners files](https://vercel.com/docs/getting-started-with-vercel#define-code-owners-files)[](https://vercel.com/docs/getting-started-with-vercel#define-code-owners-files)
After installation, define Code Owners files in your repository. Pull requests with changes in specified directories will automatically have reviewers added.
Start by adding a `.vercel.approvers` file in a directory in your repository. List GitHub usernames or team names in the file, each on a new line:
.vercel.approvers
```
@username1
@org/team1
```

Then, run the [`validate`](https://vercel.com/docs/code-owners/cli#validate) command to check the syntax and merge your changes into your repository:
Terminal
![](https://7nyt0uhk7sse4zvn.public.blob.vercel-storage.com/docs-assets/static/topics/icons/pnpm.svg)pnpm bun yarn npm
```
pnpm dlx vercel-code-owners validate
```

```
yarn dlx vercel-code-owners validate
```

```
npx vercel-code-owners validate
```

```
bunx vercel-code-owners validate
```

  5. ###  [Test Code Owners on a new pull request](https://vercel.com/docs/getting-started-with-vercel#test-code-owners-on-a-new-pull-request)[](https://vercel.com/docs/getting-started-with-vercel#test-code-owners-on-a-new-pull-request)
With the `.vercel.approvers` file merged into the main branch, test the flow by modifying any file within the same or child directory. Create a pull request as usual, and the system will automatically add one of the listed users as a reviewer.
  6. ###  [Add the Code Owners check as required](https://vercel.com/docs/getting-started-with-vercel#add-the-code-owners-check-as-required)[](https://vercel.com/docs/getting-started-with-vercel#add-the-code-owners-check-as-required)
This step is optional
By default, GitHub checks are optional and won't block merging. To make the Code Owners check mandatory, go to `Settings > Branches > [Edit] > Require status checks to pass before merging` in your repository settings.
