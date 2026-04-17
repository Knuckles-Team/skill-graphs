##  [Sharing flag overrides](https://vercel.com/docs/flags/flags-explorer#sharing-flag-overrides)[](https://vercel.com/docs/flags/flags-explorer#sharing-flag-overrides)
Any overrides you apply from Vercel Toolbar usually apply to your browser session only. However, you can recommend overrides to team members by either:
  * [Setting overrides as recommended for a given branch](https://vercel.com/docs/flags/flags-explorer#branch-based-recommendations)
  * Explicitly [sharing a set of overrides through a URL](https://vercel.com/docs/flags/flags-explorer#url-based-recommendations) with a team member


###  [Branch based recommendations](https://vercel.com/docs/flags/flags-explorer#branch-based-recommendations)[](https://vercel.com/docs/flags/flags-explorer#branch-based-recommendations)
This workflow is great when you start working on a new feature in a branch, as the recommended overrides will travel with the branch from local development through to the preview deployment.
  1. First configure the overrides you would like to share as usual
  2. Then, select the chevron next to the branch name at the top
  3. Choose Save Recommendations to recommend these overrides to any team member visiting your branch locally or on a preview deployment


When a team member visits that branch they will get a notification suggesting to apply the overrides you recommended. Notifications are displayed on all preview deployments, but not on your production deployment.
###  [URL based recommendations](https://vercel.com/docs/flags/flags-explorer#url-based-recommendations)[](https://vercel.com/docs/flags/flags-explorer#url-based-recommendations)
This workflow is great when you want to share once-off overrides with team members to reproduce a bug under certain conditions or to share a new feature.
  1. First configure the overrides you would like to share as usual
  2. Choose Share to copy a link to the page you are on, along with a query parameter containing your overrides


You can send this link to team members. When they visit the link they will get a notification suggesting to apply the overrides you shared.
