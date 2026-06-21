##  [How it works](https://vercel.com/docs/flags/vercel-flags#how-it-works)[](https://vercel.com/docs/flags/vercel-flags#how-it-works)
###  [Flags and SDKs](https://vercel.com/docs/flags/vercel-flags#flags-and-sdks)[](https://vercel.com/docs/flags/vercel-flags#flags-and-sdks)
Every flag belongs to a Vercel project. Create flags in the [dashboard](https://vercel.com/docs/flags/vercel-flags/dashboard), then evaluate them in your application using one of the available [SDKs](https://vercel.com/docs/flags/vercel-flags/sdks):
  * [Flags SDK](https://vercel.com/docs/flags/vercel-flags/sdks/flags-sdk): The recommended option for Next.js and SvelteKit. Framework-native, with full TypeScript support.
  * [OpenFeature](https://vercel.com/docs/flags/vercel-flags/sdks/openfeature): A vendor-neutral standard. Use the OpenFeature API while Vercel manages your flags.
  * [Core library](https://vercel.com/docs/flags/vercel-flags/sdks/core): Direct access to the evaluation engine for full control or unsupported frameworks.


Follow the [quickstart guide](https://vercel.com/docs/flags/vercel-flags/quickstart) to set up your first flag.
###  [Entities and targeting](https://vercel.com/docs/flags/vercel-flags#entities-and-targeting)[](https://vercel.com/docs/flags/vercel-flags#entities-and-targeting)
By default, a flag returns the same value for everyone. To personalize behavior, define entities that represent the things your application knows about, like users, teams, or devices. Then create targeting rules that reference entity attributes, such as enabling a flag for users on the Enterprise plan.
For more information on entities, see [Entities](https://vercel.com/docs/flags/vercel-flags/dashboard/entities).
###  [Segments](https://vercel.com/docs/flags/vercel-flags#segments)[](https://vercel.com/docs/flags/vercel-flags#segments)
Segments are reusable groups of users based on entity attributes. Define a segment once and apply it to any flag. When you update a segment's rules, every flag using it updates automatically.
For more information on segments, see [Segments](https://vercel.com/docs/flags/vercel-flags/dashboard/segments).
###  [Drafts](https://vercel.com/docs/flags/vercel-flags#drafts)[](https://vercel.com/docs/flags/vercel-flags#drafts)
Drafts bridge your code and your dashboard. Define a flag in code, deploy, and Vercel detects it through the Flags Discovery endpoint and surfaces it as a draft. Promote the draft when you're ready to configure targeting.
For more information on drafts, see [Draft Flags](https://vercel.com/docs/flags/vercel-flags/dashboard/drafts).
###  [Flags Explorer](https://vercel.com/docs/flags/vercel-flags#flags-explorer)[](https://vercel.com/docs/flags/vercel-flags#flags-explorer)
The Flags Explorer is built into the Vercel Toolbar and lets you view and override feature flags in your browser without affecting other users.
For more information on the Flags Explorer, see [Flags Explorer](https://vercel.com/docs/flags/flags-explorer).
###  [Embedded definitions](https://vercel.com/docs/flags/vercel-flags#embedded-definitions)[](https://vercel.com/docs/flags/vercel-flags#embedded-definitions)
The SDK can fetch your flag definitions once at build time and bundle them into the deployment. This guarantees every function uses the same snapshot during the build, and provides a runtime fallback if the Vercel Flags service is temporarily unreachable.
Learn more about [embedded definitions](https://vercel.com/docs/flags/vercel-flags/sdks/core#embedded-definitions).
