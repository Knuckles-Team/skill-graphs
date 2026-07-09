##  [Enable or disable the toolbar for a specific branch](https://vercel.com/docs/vercel-toolbar/managing-toolbar#enable-or-disable-the-toolbar-for-a-specific-branch)[](https://vercel.com/docs/vercel-toolbar/managing-toolbar#enable-or-disable-the-toolbar-for-a-specific-branch)
You can use Vercel's [preview environment variables](https://vercel.com/docs/environment-variables#preview-environment-variables) to manage the toolbar for specific branches or environments
To enable the toolbar for an individual branch, add the following to the environment variables for the desired preview branch:
.env
```
VERCEL_PREVIEW_FEEDBACK_ENABLED=1
```

To disable the toolbar for an individual branch, set the above environment variable's value to `0`:
.env
```
VERCEL_PREVIEW_FEEDBACK_ENABLED=0
```
