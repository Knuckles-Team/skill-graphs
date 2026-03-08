##  [Unique Options](https://vercel.com/docs/cli/redeploy#unique-options)[](https://vercel.com/docs/cli/redeploy#unique-options)
These are options that only apply to the `vercel redeploy` command.
###  [No Wait](https://vercel.com/docs/cli/redeploy#no-wait)[](https://vercel.com/docs/cli/redeploy#no-wait)
The `--no-wait` option does not wait for a deployment to finish before exiting from the `redeploy` command.
terminal
```
vercel redeploy https://example-app-6vd6bhoqt.vercel.app --no-wait
```

Using the `vercel redeploy` command with the `--no-wait` option.
###  [target](https://vercel.com/docs/cli/redeploy#target)[](https://vercel.com/docs/cli/redeploy#target)
Use the `--target` option to define the environment you want to redeploy to. This could be production, preview, or a [custom environment](https://vercel.com/docs/deployments/environments#custom-environments).
terminal
```
vercel redeploy https://example-app-6vd6bhoqt.vercel.app --target=staging
```
