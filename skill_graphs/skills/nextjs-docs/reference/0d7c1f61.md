# Middleware Upgrade Guide
As we work on improving Middleware for General Availability (GA), we've made some changes to the Middleware APIs (and how you define Middleware in your application) based on your feedback.
This upgrade guide will help you understand the changes, why they were made, and how to migrate your existing Middleware to the new API. The guide is for Next.js developers who:
  * Currently use the beta Next.js Middleware features
  * Choose to upgrade to the next stable version of Next.js (`v12.2`)


You can start upgrading your Middleware usage today with the latest release (`npm i next@latest`).
> **Note** : These changes described in this guide are included in Next.js `12.2`. You can keep your current site structure, including nested Middleware, until you move to `12.2` (or a `canary` build of Next.js).
If you have ESLint configured, you will need to run `npm i eslint-config-next@latest --save-dev` to upgrade your ESLint configuration to ensure the same version is being used as the Next.js version. You might also need to restart VSCode for the changes to take effect.
