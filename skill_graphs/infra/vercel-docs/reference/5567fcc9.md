##  [How to create a flag](https://vercel.com/docs/flags/vercel-flags/dashboard#how-to-create-a-flag)[](https://vercel.com/docs/flags/vercel-flags/dashboard#how-to-create-a-flag)
Project Administrators and Developers can create and manage feature flags.
To create a flag in the dashboard:
  1. From the Flags tab, click the Create Flag button
  2. Enter a Slug for your flag (e.g., `show-new-feature`)
  3. Select the Type (Boolean, String, or Number)


For String and Number flags, you can define the variants your flag returns. Each variant has a value used in code and an optional label shown in the dashboard.
During creation, you can configure which variant each environment receives. Boolean flags default to `true` in Development and `false` in Preview and Production, so your feature is visible while you develop but hidden after merging. You can refine these rules at any time after creating the flag.
When you create a flag, Vercel automatically configures these environment variables for your project:
  * `FLAGS`: Connection string to your Vercel Flags project
  * `FLAGS_SECRET`: Secret key used by the Flags Explorer for overrides


See [Feature Flag Configuration](https://vercel.com/docs/flags/vercel-flags/dashboard/feature-flag) for more information on how to configure individual flags.
