##  [Add a monorepo through Vercel CLI](https://vercel.com/docs/deployment-checks#add-a-monorepo-through-vercel-cli)[](https://vercel.com/docs/deployment-checks#add-a-monorepo-through-vercel-cli)
You should use [Vercel CLI 20.1.0](https://vercel.com/docs/cli#updating-vercel-cli) or newer.
  1. Ensure you're in the root directory of your monorepo. Vercel CLI should not be invoked from the subdirectory.
  2. Run `vercel link` to link multiple Vercel projects at once. To learn more, see the [CLI documentation](https://vercel.com/docs/cli/link#repo-alpha):
Terminal
```
vercel link --repo
```

  3. Once linked, subsequent commands such as `vercel dev` will use the selected Vercel Project. To switch to a different Project in the same monorepo, run `vercel link` again and select the new Project.


Alternatively, you can use `git clone` to create multiple copies of your monorepo in different directories and link each one to a different Vercel Project.
See this
