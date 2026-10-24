# TYPESCRIPT_CONFIGURATION
Last updated March 4, 2025
Conformance is available on [Enterprise plans](https://vercel.com/docs/plans/enterprise)
Using TypeScript in a workspace requires a few items to be set up correctly:
  * There should be a `tsconfig.json` file at the root of the workspace.
  * The `tsconfig.json` should extend from the repo's shared `tsconfig.json` file.
  * The `tsconfig.json` file should specify a `tsBuildInfoFile` to speed up incremental compilation.
  * The `tsconfig.json` file should have certain compiler options set for improved type safety.
  * The workspace should have a `type-check` command that runs the TypeScript compiler to check for type issues.


These changes will ensure that the TypeScript compiler picks up the right compiler settings for the project and that the TypeScript type checking will run when the `type-check` command is run for the entire repository.
