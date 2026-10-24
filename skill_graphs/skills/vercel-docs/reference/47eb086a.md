# Performing a rolling release deployment
Last updated March 8, 2026
Use this guide to gradually roll out a new production deployment using rolling releases. You'll configure traffic stages, monitor for errors between stages, and either complete the rollout or abort if problems arise.
This guide requires a [linked Vercel project](https://vercel.com/docs/cli/project-linking). Run `vercel link` in your project directory if you haven't already. Rolling releases require a Pro or Enterprise plan.
