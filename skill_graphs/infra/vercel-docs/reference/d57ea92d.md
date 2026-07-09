# REQUIRE_NODE_VERSION_FILE
Last updated March 4, 2025
Conformance is available on [Enterprise plans](https://vercel.com/docs/plans/enterprise)
This rule is available from version 1.2.0.
Using a Node.js version file (`.node-version` or `.nvmrc`) ensures that all developers and tooling (e.g., CI systems) use the same version of Node.js. This practice helps to avoid inconsistencies between environments and can even prevent bugs from being shipped to production.
As another benefit, committing a Node.js version file improves developer experience, as many Node.js version management tools can automatically detect and use the version defined in the file. This includes
This rule also validates to ensure that the version in the file is defined in a way that is compatible with common tooling.
By default, this rule is disabled. To enable it, refer to [customizing Conformance](https://vercel.com/docs/conformance/customize).
