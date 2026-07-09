# REQUIRE_DOCS_ON_EXPORTED_FUNCTIONS
Last updated March 4, 2025
Conformance is available on [Enterprise plans](https://vercel.com/docs/plans/enterprise)
This rule is available from version 1.8.0.
Adding JSDoc to exported functions helps engineers to quickly understand the purpose and application of those functions when reviewing or using them.
This is particularly important in packages where the source code may be minified and/or obfuscated, and can save users time by avoiding the need to find usage information in external documentation.
For more information on JSDoc, see
Additionally, for non-TypeScript projects, JSDoc can be used to declare type information for function parameters and return values. For packages, these declarations can provide type information for both JavaScript and TypeScript consumers.
