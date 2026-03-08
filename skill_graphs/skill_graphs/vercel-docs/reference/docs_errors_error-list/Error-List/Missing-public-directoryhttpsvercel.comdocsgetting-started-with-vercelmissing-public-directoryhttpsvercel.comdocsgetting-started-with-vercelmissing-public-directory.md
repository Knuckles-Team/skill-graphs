##  [Missing public directory](https://vercel.com/docs/getting-started-with-vercel#missing-public-directory)[](https://vercel.com/docs/getting-started-with-vercel#missing-public-directory)
The [build step](https://vercel.com/docs/deployments/configure-a-build) will result in an error if the output directory is missing, empty, or invalid (for example, it is not a directory). To resolve this error, you can try the following steps:
  * Make sure the [output directory](https://vercel.com/docs/deployments/configure-a-build#output-directory) is specified correctly in project settings
  * If the output directory is correct, check the build command ([documentation](https://vercel.com/docs/deployments/configure-a-build#build-command)) or the [root directory](https://vercel.com/docs/deployments/configure-a-build#root-directory))
  * Try running the build command locally and make sure that the files are correctly generated in the specified output directory
