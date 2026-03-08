# Enabling and Disabling Comments
Last updated September 24, 2025
Comments are enabled by default for all preview deployments on all new projects. By default, only members of [your Vercel team](https://vercel.com/docs/accounts/create-a-team) can contribute comments.
The comments toolbar will only render on sites with HTML set as the `Content-Type`. Additionally, on Next.js sites, the comments toolbar will only render on Next.js pages and not on API routes or static files.
###  [At the account level](https://vercel.com/docs/comments/how-comments-work#at-the-account-level)[](https://vercel.com/docs/comments/how-comments-work#at-the-account-level)
You can enable or disable comments at the account level with certain permissions:
  1. Navigate to [your Vercel dashboard](https://vercel.com/d?to=%2Fdashboard&title=Open+Dashboard) and make sure that you have selected your team from the team switcher.
  2. From your [dashboard](https://vercel.com/d?to=%2Fdashboard&title=Open+Dashboard), open Settings in the sidebar.
  3. In the General section, find Vercel Toolbar.
  4. Under each environment (Preview and Production), select either On or Off from the dropdown to determine the visibility of the Vercel Toolbar for that environment.
  5. You can optionally choose to allow the setting to be overridden at the project level.

![The dashboard setting to enable or disable the toolbar at the team level.](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fteam-level-toolbar-management-light.png&w=1920&q=75)![The dashboard setting to enable or disable the toolbar at the team level.](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fteam-level-toolbar-management-dark.png&w=1920&q=75)The dashboard setting to enable or disable the toolbar at the team level.
###  [At the project level](https://vercel.com/docs/comments/how-comments-work#at-the-project-level)[](https://vercel.com/docs/comments/how-comments-work#at-the-project-level)
  1. From your [dashboard](https://vercel.com/dashboard), select the project you want to enable or disable Vercel Toolbar for.
  2. Navigate to [General](https://vercel.com/d?to=%2F%5Bteam%5D%2F%5Bproject%5D%2Fsettings%2Fgeneral&title=Go+to+General+settings) in Settings.
  3. Find Vercel Toolbar.
  4. Under each environment (Preview and Production), select either an option from the dropdown to determine the visibility of Vercel Toolbar for that environment. The options are:
     * Default: Respect team-level visibility settings.
     * On: Enable the toolbar for the environment.
     * Off: Disable the toolbar for the environment.

![The dashboard setting to enable or disable the toolbar in a project.](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fproject-level-toolbar-management-light.png&w=1920&q=75)![The dashboard setting to enable or disable the toolbar in a project.](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fproject-level-toolbar-management-dark.png&w=1920&q=75)The dashboard setting to enable or disable the toolbar in a project.
###  [At the session or interface level](https://vercel.com/docs/comments/how-comments-work#at-the-session-or-interface-level)[](https://vercel.com/docs/comments/how-comments-work#at-the-session-or-interface-level)
To disable comments for the current browser session, you must [disable the toolbar](https://vercel.com/docs/vercel-toolbar/managing-toolbar#disable-toolbar-for-session).
###  [With environment variables](https://vercel.com/docs/comments/how-comments-work#with-environment-variables)[](https://vercel.com/docs/comments/how-comments-work#with-environment-variables)
You can enable or disable comments for specific branches or environments with [preview environment variables](https://vercel.com/docs/vercel-toolbar/managing-toolbar#enable-or-disable-the-toolbar-for-a-specific-branch).
See [Managing the toolbar](https://vercel.com/docs/vercel-toolbar/managing-toolbar) for more information.
###  [In production and localhost](https://vercel.com/docs/comments/how-comments-work#in-production-and-localhost)[](https://vercel.com/docs/comments/how-comments-work#in-production-and-localhost)
To use comments in a production deployment, or link comments in your local development environment to a preview deployment, see [our docs on using comments in production and localhost](https://vercel.com/docs/vercel-toolbar/in-production-and-localhost).
See [Managing the toolbar](https://vercel.com/docs/vercel-toolbar/managing-toolbar) for more information.
