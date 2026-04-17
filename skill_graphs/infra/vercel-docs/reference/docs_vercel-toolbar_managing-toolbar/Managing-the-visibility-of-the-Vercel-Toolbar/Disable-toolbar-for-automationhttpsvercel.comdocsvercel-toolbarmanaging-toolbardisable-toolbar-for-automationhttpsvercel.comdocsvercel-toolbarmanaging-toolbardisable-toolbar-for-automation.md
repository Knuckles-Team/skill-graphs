##  [Disable toolbar for automation](https://vercel.com/docs/vercel-toolbar/managing-toolbar#disable-toolbar-for-automation)[](https://vercel.com/docs/vercel-toolbar/managing-toolbar#disable-toolbar-for-automation)
You can use the `x-vercel-skip-toolbar` header to prevent interference with automated end-to-end tests:
  1. Add the `x-vercel-skip-toolbar` header to the request sent to [the preview deployment URL](https://vercel.com/docs/deployments/environments#preview-environment-pre-production#preview-urls)
  2. Optionally, you can assign the value `1` to the header. However, presence of the header itself triggers Vercel to disable the toolbar
