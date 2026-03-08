# Customizing Conformance
Last updated October 23, 2025
Conformance is available on [Enterprise plans](https://vercel.com/docs/plans/enterprise)
The Conformance framework may be customized so that you can manage rules for different workspaces in your repository or to pass configuration to the rules.
To customize Conformance, first define a `conformance.config.jsonc` file in the root of your directory.
Both `conformance.config.jsonc` and `conformance.config.json` are supported, and both support JSONC (JSON with JavaScript-style comments). We recommend using the `.jsonc` extension as it helps other tools (for example, VS Code) to provide syntax highlighting and validation.
