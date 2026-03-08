# ESLINT_CONFIGURATION
Last updated April 23, 2025
Conformance is available on [Enterprise plans](https://vercel.com/docs/plans/enterprise)
This rule requires that:
  * An ESLint config exists in the current workspace.
  * A script to run ESLint exists in `package.json` in the current workspace.
  * `reportUnusedDisableDirectives` is set to `true`, which detects and can autofix unused ESLint disable comments.
  * `root` is set to `true`, which ensures that workspaces don't inherit unintended rules and configuration from ESLint configuration files in parent directories.
