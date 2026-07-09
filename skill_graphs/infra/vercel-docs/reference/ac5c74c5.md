##  [Deploying from source](https://vercel.com/docs/cli/deploying-from-cli#deploying-from-source)[](https://vercel.com/docs/cli/deploying-from-cli#deploying-from-source)
The `vercel` command is used to [deploy](https://vercel.com/docs/cli/deploy) Vercel Projects and can be used from either the root of the Vercel Project directory or by providing a path.
terminal
```
vercel
```

Deploys the current Vercel project, when run from the Vercel Project root.
You can alternatively use the [`vercel deploy` command](https://vercel.com/docs/cli/deploy) for the same effect, if you want to be more explicit.
terminal
```
vercel [path-to-project]
```

Deploys the Vercel project found at the provided path, when it's a Vercel Project root.
When deploying, stdout is always the Deployment URL.
terminal
```
vercel > deployment-url.txt
```

Writes the Deployment URL output from the `deploy` command to a text file.
###  [Relevant commands](https://vercel.com/docs/cli/deploying-from-cli#relevant-commands)[](https://vercel.com/docs/cli/deploying-from-cli#relevant-commands)
  * [deploy](https://vercel.com/docs/cli/deploy)
