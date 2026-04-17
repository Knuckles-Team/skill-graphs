##  [Deploying from local build (prebuilt)](https://vercel.com/docs/cli/deploying-from-cli#deploying-from-local-build-prebuilt)[](https://vercel.com/docs/cli/deploying-from-cli#deploying-from-local-build-prebuilt)
You can build Vercel projects locally to inspect the build outputs before they are [deployed](https://vercel.com/docs/cli/deploy). This is a great option for producing builds for Vercel that do not share your source code with the platform.
It's also useful for debugging build outputs.
terminal
```
vercel build
```

Using the `vercel` command to deploy and write stdout to a text file.
This produces `.vercel/output` in the [Build Output API](https://vercel.com/docs/build-output-api/v3) format. You can review the output, then [deploy](https://vercel.com/docs/cli/deploy) with:
terminal
```
vercel deploy --prebuilt
```

Deploy the build outputs in `.vercel/output` produced by `vercel build`.
Review the [When not to use --prebuilt](https://vercel.com/docs/cli/deploy#when-not-to-use---prebuilt) section to understand when you should not use the `--prebuilt` flag.
See more details at [Build Output API](https://vercel.com/docs/build-output-api/v3).
###  [Relevant commands](https://vercel.com/docs/cli/deploying-from-cli#relevant-commands)[](https://vercel.com/docs/cli/deploying-from-cli#relevant-commands)
  * [build](https://vercel.com/docs/cli/build)
  * [deploy](https://vercel.com/docs/cli/deploy)


* * *
[ Previous CLI ](https://vercel.com/docs/cli)[ Next Project Linking ](https://vercel.com/docs/cli/project-linking)
Was this helpful?
Send
On this page
  * [Deploying from source](https://vercel.com/docs/cli/deploying-from-cli#deploying-from-source)
  * [Relevant commands](https://vercel.com/docs/cli/deploying-from-cli#relevant-commands)
  * [Deploying a staged production build](https://vercel.com/docs/cli/deploying-from-cli#deploying-a-staged-production-build)
  * [Relevant commands](https://vercel.com/docs/cli/deploying-from-cli#relevant-commands)
  * [Deploying from local build (prebuilt)](https://vercel.com/docs/cli/deploying-from-cli#deploying-from-local-build-prebuilt)
  * [Relevant commands](https://vercel.com/docs/cli/deploying-from-cli#relevant-commands)


Copy as MarkdownGive feedbackAsk AI about this page
