##  [Using global `turbo`](https://vercel.com/docs/deployment-retention#using-global-turbo)[](https://vercel.com/docs/deployment-retention#using-global-turbo)
Turborepo is also available globally when you deploy on Vercel, which means that you do not have to add `turbo` as a dependency in your application.
Thanks to [build command](https://vercel.com/docs/deployments/configure-a-build#build-command) can be as straightforward as:
```
turbo build
```

The appropriate [root directory](https://vercel.com/docs/deployments/configure-a-build#root-directory).
To override this behavior and use a specific version of Turborepo, install the desired version of `turbo` in your project.
