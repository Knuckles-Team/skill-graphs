##  [Unique Options](https://vercel.com/docs/cli/build#unique-options)[](https://vercel.com/docs/cli/build#unique-options)
These are options that only apply to the `vercel build` command.
###  [Production](https://vercel.com/docs/cli/build#production)[](https://vercel.com/docs/cli/build#production)
The `--prod` option can be specified when you want to build the Vercel Project using Production Environment Variables. By default, the Preview Environment Variables will be used.
terminal
```
vercel build --prod
```

Using the `vercel build` command with the `--prod` option.
###  [Yes](https://vercel.com/docs/cli/build#yes)[](https://vercel.com/docs/cli/build#yes)
The `--yes` option can be used to bypass the confirmation prompt and automatically pull environment variables and Project Settings if not found locally.
terminal
```
vercel build --yes
```

Using the `vercel build` command with the `--yes` option.
###  [target](https://vercel.com/docs/cli/build#target)[](https://vercel.com/docs/cli/build#target)
Use the `--target` option to define the environment you want to build against. This could be production, preview, or a [custom environment](https://vercel.com/docs/deployments/environments#custom-environments).
terminal
```
vercel build --target=staging
```

###  [Output](https://vercel.com/docs/cli/build#output)[](https://vercel.com/docs/cli/build#output)
The `--output` option specifies a custom directory where the build artifacts will be written to, instead of the default `.vercel/output` directory.
terminal
```
vercel build --output ./custom-output
```

Using the `vercel build` command with the `--output` option to specify a custom output directory.
