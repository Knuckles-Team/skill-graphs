##  [Setting up Vercel](https://vercel.com/docs/getting-started-with-vercel#setting-up-vercel)[](https://vercel.com/docs/getting-started-with-vercel#setting-up-vercel)
Now that your local environment is set up, you can configure Vercel to use the private registry.
  1. Create a [Vercel authentication token](https://vercel.com/docs/rest-api#creating-an-access-token) on the [Tokens](https://vercel.com/account/tokens) page
  2. To set the newly created token in Vercel, navigate to the [Environment Variables](https://vercel.com/docs/environment-variables) settings for your Project
  3. Add a new environment variable with the name `VERCEL_TOKEN`, and set the value to the token you created above. We recommend using a [Sensitive Environmental Variable](https://vercel.com/docs/environment-variables/sensitive-environment-variables) for storing this token
  4. Add a new environment variable with the name `NPM_RC`, and set the value to the following:


```
@vercel-private:registry=https://vercel-private-registry.vercel.sh/registry
//vercel-private-registry.vercel.sh/:_authToken=${VERCEL_TOKEN}
```

If you already have an `NPM_RC` environment variable, you can append the above to that existing value.
Vercel should now be able to install packages from the private registry when building your Project.
