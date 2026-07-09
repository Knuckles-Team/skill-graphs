# NEXTJS_MISSING_MODULARIZE_IMPORTS
Last updated March 4, 2025
Conformance is available on [Enterprise plans](https://vercel.com/docs/plans/enterprise)
This rule has been deprecated as of version [1.10.0](https://vercel.com/docs/conformance/changelog#1.10.0)and will be removed in 1.10.0.
`modularizeImports` is a feature of Next 13 that can reduce dev compilation times when importing packages that are exported as barrel files. Barrel files are convenient ways to export code from a package from a single file to make it straightforward to import any of the code from the package. However, since they export a lot of code from the same file, importing these packages can cause tools to do a lot of additional work analyzing files that are unused in the application.
