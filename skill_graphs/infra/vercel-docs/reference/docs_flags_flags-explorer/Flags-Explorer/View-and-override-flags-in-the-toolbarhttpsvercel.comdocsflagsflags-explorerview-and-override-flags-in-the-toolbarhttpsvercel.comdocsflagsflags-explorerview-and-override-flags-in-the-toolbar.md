##  [View and override flags in the toolbar](https://vercel.com/docs/flags/flags-explorer#view-and-override-flags-in-the-toolbar)[](https://vercel.com/docs/flags/flags-explorer#view-and-override-flags-in-the-toolbar)
Before you can use with the Flags Explorer, ensure that your team has set up both [feature flags](https://vercel.com/docs/flags/flags-explorer/getting-started) and the [Vercel Toolbar](https://vercel.com/docs/vercel-toolbar/in-production-and-localhost) in the environment you are using,
To see and override feature flags for your application:
  1. You must log into the Vercel Toolbar to interact with your application's feature flag overrides.
  2. Select the Flags Explorer option (
  3. Find the desired feature flag in the modal by scrolling or using the search and filter controls.
  4. Select an override value for the desired feature flag. Note that by default, overrides are not persisted and only affect the user applying them, in the environment in which they were set. To share overrides, see [Sharing flag overrides](https://vercel.com/docs/flags/flags-explorer#sharing-flag-overrides).
  5. Apply the changes. This will trigger a soft reload. If you have applied changes, the Vercel Toolbar will turn blue.
