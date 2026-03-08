##  [Flags tab sections](https://vercel.com/docs/flags/vercel-flags/dashboard#flags-tab-sections)[](https://vercel.com/docs/flags/vercel-flags/dashboard#flags-tab-sections)
###  [Flags](https://vercel.com/docs/flags/vercel-flags/dashboard#flags)[](https://vercel.com/docs/flags/vercel-flags/dashboard#flags)
Select any flag to configure how it behaves across environments and user groups. You can set static values, add targeting rules that evaluate top to bottom, and track the complete history of changes. Rules can target specific segments or entities, with percentage-based rollouts for gradual releases.
For more information on how to configure individual flags, see [Feature Flag Configuration](https://vercel.com/docs/flags/vercel-flags/dashboard/feature-flag).
###  [Drafts](https://vercel.com/docs/flags/vercel-flags/dashboard#drafts)[](https://vercel.com/docs/flags/vercel-flags/dashboard#drafts)
Drafts are flags that Vercel detects in your code but haven't been created in the dashboard yet. This lets you define flags in code first, then promote them when you're ready to configure targeting. When you create a feature flag from a draft the descriptions and options from your code are pre-filled automatically.
For more information on drafts, see [Draft Flags](https://vercel.com/docs/flags/vercel-flags/dashboard/drafts).
###  [Segments](https://vercel.com/docs/flags/vercel-flags/dashboard#segments)[](https://vercel.com/docs/flags/vercel-flags/dashboard#segments)
Segments let you define reusable groups of users, like "Beta Testers" or "Internal Team." Create a segment once with your targeting rules, then apply it to any flag. When you update a segment, all flags using it update automatically.
For more information on segments, see [Segments](https://vercel.com/docs/flags/vercel-flags/dashboard/segments).
###  [Entities](https://vercel.com/docs/flags/vercel-flags/dashboard#entities)[](https://vercel.com/docs/flags/vercel-flags/dashboard#entities)
Entities define the types and attributes you can target, like User, Team, or Device. By mapping entities to your application data, you can create precise rules like "enable for users on the Enterprise plan" or "show to users in the Engineering department."
For more information on entities, see [Entities](https://vercel.com/docs/flags/vercel-flags/dashboard/entities).
###  [SDK Keys](https://vercel.com/docs/flags/vercel-flags/dashboard#sdk-keys)[](https://vercel.com/docs/flags/vercel-flags/dashboard#sdk-keys)
SDK Keys authenticate your application and determine which environment's configuration is used. Vercel automatically manages keys through the `FLAGS` environment variable, but you can view and rotate them here if needed.
To share flags across projects, such as in a microfrontend setup, create a dedicated SDK Key in one project and add it to the other project's environment variables. See [How to use flags of another project](https://vercel.com/docs/flags/vercel-flags/dashboard/sdk-keys#how-to-use-flags-of-another-project) for details.
For more information on SDK keys, see [SDK Keys](https://vercel.com/docs/flags/vercel-flags/dashboard/sdk-keys).
###  [Archive](https://vercel.com/docs/flags/vercel-flags/dashboard#archive)[](https://vercel.com/docs/flags/vercel-flags/dashboard#archive)
Archive flags when they're no longer needed but you might want to restore them later. Archived flags stop being served and can't be edited while archived, but their configuration is preserved. You can restore a flag with all its previous settings intact, or permanently delete it from the archive.
For more information on archiving flags, see [Archive](https://vercel.com/docs/flags/vercel-flags/dashboard/archive).
