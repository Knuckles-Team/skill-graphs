##  [Production deployment cannot be redeployed](https://vercel.com/docs/getting-started-with-vercel#production-deployment-cannot-be-redeployed)[](https://vercel.com/docs/getting-started-with-vercel#production-deployment-cannot-be-redeployed)
You cannot redeploy a production deployment if a more recent one exists.
The reason is that redeploying an old production deployment would result in overwriting the most recent source code you have deployed to production.
To force an explicit overwrite of the current production deployment, select Promote instead.
