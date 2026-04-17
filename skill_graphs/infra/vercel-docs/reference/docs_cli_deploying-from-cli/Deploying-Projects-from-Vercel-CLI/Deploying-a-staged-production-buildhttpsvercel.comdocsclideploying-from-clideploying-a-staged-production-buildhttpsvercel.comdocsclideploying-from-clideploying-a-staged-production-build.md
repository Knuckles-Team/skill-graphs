##  [Deploying a staged production build](https://vercel.com/docs/cli/deploying-from-cli#deploying-a-staged-production-build)[](https://vercel.com/docs/cli/deploying-from-cli#deploying-a-staged-production-build)
By default, when you promote a deployment to production, your domain will point to that deployment. If you want to create a production deployment without assigning it to your domain, for example to avoid sending all of your traffic to it, you can:
  1. Turn off the auto-assignment of domains for the current production deployment:


terminal
```
vercel --prod --skip-domain
```

  1. When you are ready, manually promote the staged deployment to production:


terminal
```
vercel promote [deployment-id or url]
```

###  [Relevant commands](https://vercel.com/docs/cli/deploying-from-cli#relevant-commands)[](https://vercel.com/docs/cli/deploying-from-cli#relevant-commands)
  * [promote](https://vercel.com/docs/cli/promote)
  * [deploy](https://vercel.com/docs/cli/deploy)
