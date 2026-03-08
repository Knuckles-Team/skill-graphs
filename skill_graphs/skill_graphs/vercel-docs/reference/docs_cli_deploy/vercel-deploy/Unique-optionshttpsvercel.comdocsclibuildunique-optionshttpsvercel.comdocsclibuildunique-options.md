##  [Unique options](https://vercel.com/docs/cli/build#unique-options)[](https://vercel.com/docs/cli/build#unique-options)
These are options that only apply to the `vercel` command.
###  [Prebuilt](https://vercel.com/docs/cli/build#prebuilt)[](https://vercel.com/docs/cli/build#prebuilt)
The `--prebuilt` option can be used to upload and deploy the results of a previous `vc build` execution located in the .vercel/output directory. See [vercel build](https://vercel.com/docs/cli/build) and [Build Output API](https://vercel.com/docs/build-output-api/v3) for more details.
####  [When not to use --prebuilt](https://vercel.com/docs/cli/build#when-not-to-use---prebuilt)[](https://vercel.com/docs/cli/build#when-not-to-use---prebuilt)
When using the `--prebuilt` flag, no deployment ID will be made available for supported frameworks (like Next.js) to use, which means [Skew Protection](https://vercel.com/docs/skew-protection) will not be enabled. Additionally, [System Environment Variables](https://vercel.com/docs/environment-variables/system-environment-variables) will be missing at build time, so frameworks that rely on them at build time may not function correctly.
Prebuilt deployments cannot use `dpl_` as a user configured deployment ID name.
If you need Skew Protection or System Environment Variables, do not use the `--prebuilt` flag or use Git-based deployments.
terminal
```
vercel --prebuilt
```

You should also consider using the [archive](https://vercel.com/docs/cli/deploy#archive) option to minimize the number of files uploaded and avoid hitting upload limits:
terminal
```
# Build the project locally
vercel build

# Deploy the pre-built project, archiving it as a .tgz file
vercel deploy --prebuilt --archive=tgz
```

This example uses the `vercel build` command to build your project locally. It then uses the `--prebuilt` and `--archive=tgz` options on the `deploy` command to compress the build output and then deploy it.
###  [Build env](https://vercel.com/docs/cli/build#build-env)[](https://vercel.com/docs/cli/build#build-env)
The `--build-env` option, shorthand `-b`, can be used to provide environment variables to the [build step](https://vercel.com/docs/deployments/configure-a-build).
terminal
```
vercel --build-env KEY1=value1 --build-env KEY2=value2
```

Using the `vercel` command with the `--build-env` option.
###  [Yes](https://vercel.com/docs/cli/build#yes)[](https://vercel.com/docs/cli/build#yes)
The `--yes` option can be used to skip questions you are asked when setting up a new Vercel project. The questions will be answered with the provided defaults, inferred from `vercel.json` and the folder name.
terminal
```
vercel --yes
```

Using the `vercel` command with the `--yes` option.
###  [Env](https://vercel.com/docs/cli/build#env)[](https://vercel.com/docs/cli/build#env)
The `--env` option, shorthand `-e`, can be used to provide [environment variables](https://vercel.com/docs/environment-variables) at runtime.
terminal
```
vercel --env KEY1=value1 --env KEY2=value2
```

Using the `vercel` command with the `--env` option.
###  [Name](https://vercel.com/docs/cli/build#name)[](https://vercel.com/docs/cli/build#name)
The `--name` option has been deprecated in favor of [Vercel project linking](https://vercel.com/docs/cli/project-linking), which allows you to link a Vercel project to your local codebase when you run `vercel`.
The `--name` option, shorthand `-n`, can be used to provide a Vercel project name for a deployment.
terminal
```
vercel --name foo
```

Using the `vercel` command with the `--name` option.
###  [Prod](https://vercel.com/docs/cli/build#prod)[](https://vercel.com/docs/cli/build#prod)
The `--prod` option can be used to create a deployment for a production domain specified in the Vercel project dashboard.
terminal
```
vercel --prod
```

Using the `vercel` command with the `--prod` option.
###  [Skip Domain](https://vercel.com/docs/cli/build#skip-domain)[](https://vercel.com/docs/cli/build#skip-domain)
This CLI option will override the [Auto-assign Custom Production Domains](https://vercel.com/docs/deployments/promoting-a-deployment#staging-and-promoting-a-production-deployment) project setting.
Must be used with [`--prod`](https://vercel.com/docs/cli/build#prod). The `--skip-domain` option will disable the automatic promotion (aliasing) of the relevant domains to a new production deployment. You can use [`vercel promote`](https://vercel.com/docs/cli/promote) to complete the domain-assignment process later.
terminal
```
vercel --prod --skip-domain
```

Using the `vercel` command with the `--skip-domain` option.
###  [Public](https://vercel.com/docs/cli/build#public)[](https://vercel.com/docs/cli/build#public)
The `--public` option can be used to ensure the source code is publicly available at the `/_src` path.
terminal
```
vercel --public
```

Using the `vercel` command with the `--public` option.
###  [Regions](https://vercel.com/docs/cli/build#regions)[](https://vercel.com/docs/cli/build#regions)
The `--regions` option can be used to specify which [regions](https://vercel.com/docs/regions) the deployments [Vercel functions](https://vercel.com/docs/functions) should run in.
terminal
```
vercel --regions sfo1
```

Using the `vercel` command with the `--regions` option.
###  [No wait](https://vercel.com/docs/cli/build#no-wait)[](https://vercel.com/docs/cli/build#no-wait)
The `--no-wait` option does not wait for a deployment to finish before exiting from the `deploy` command.
terminal
```
vercel --no-wait
```

###  [Force](https://vercel.com/docs/cli/build#force)[](https://vercel.com/docs/cli/build#force)
The `--force` option, shorthand `-f`, is used to force a new deployment without the [build cache](https://vercel.com/docs/deployments/troubleshoot-a-build#what-is-cached).
terminal
```
vercel --force
```

###  [With cache](https://vercel.com/docs/cli/build#with-cache)[](https://vercel.com/docs/cli/build#with-cache)
The `--with-cache` option is used to retain the [build cache](https://vercel.com/docs/deployments/troubleshoot-a-build#what-is-cached) when using `--force`.
terminal
```
vercel --force --with-cache
```

###  [Archive](https://vercel.com/docs/cli/build#archive)[](https://vercel.com/docs/cli/build#archive)
The `--archive` option compresses the deployment code into one or more files before uploading it. This option should be used when deployments include thousands of files to avoid rate limits such as the [files limit](https://vercel.com/docs/limits#files).
In some cases, `--archive` makes deployments slower. This happens because the caching of source files to optimize file uploads in future deployments is negated when source files are archived.
terminal
```
vercel deploy --archive=tgz
```

###  [Logs](https://vercel.com/docs/cli/build#logs)[](https://vercel.com/docs/cli/build#logs)
The `--logs` option, shorthand `-l`, also prints the build logs.
terminal
```
vercel deploy --logs
```

Using the `vercel deploy` command with the `--logs` option, to view logs from the build process.
###  [Meta](https://vercel.com/docs/cli/build#meta)[](https://vercel.com/docs/cli/build#meta)
The `--meta` option, shorthand `-m`, is used to add metadata to the deployment.
terminal
```
vercel deploy --meta KEY1=value1
```

Deployments can be filtered using this data with [`vercel list   --meta`](https://vercel.com/docs/cli/list#meta).
###  [target](https://vercel.com/docs/cli/build#target)[](https://vercel.com/docs/cli/build#target)
Use the `--target` option to define the environment you want to deploy to. This could be production, preview, or a [custom environment](https://vercel.com/docs/deployments/environments#custom-environments).
terminal
```
vercel deploy --target=staging
```

###  [Guidance](https://vercel.com/docs/cli/build#guidance)[](https://vercel.com/docs/cli/build#guidance)
The `--guidance` option displays suggested next steps and commands after deployment completes. This can help you discover relevant CLI commands for common post-deployment tasks.
terminal
```
vercel deploy --guidance
```

Using the `vercel deploy` command with the `--guidance` option to receive command suggestions.
