[Environment Variables](https://vercel.com/docs/environment-variables)
Framework Environment Variables
[Environment Variables](https://vercel.com/docs/environment-variables)
Framework Environment Variables
# Framework environment variables
Last updated July 18, 2025
Frameworks typically use a prefix in order to expose environment variables to the browser.
The following prefixed environment variables will be available during the build step, based on the project's selected [framework preset](https://vercel.com/docs/deployments/configure-a-build#framework-preset).
##  [Using prefixed framework environment variables locally](https://vercel.com/docs/environment-variables/framework-environment-variables#using-prefixed-framework-environment-variables-locally)[](https://vercel.com/docs/environment-variables/framework-environment-variables#using-prefixed-framework-environment-variables-locally)
Many frontend frameworks require prefixes on environment variable names to make them available to the client, such as `NEXT_PUBLIC_` for Next.js or `PUBLIC_` for SvelteKit. Vercel adds these prefixes automatically for your production and preview deployments, but not for your local development environment.
Framework environment variables are not prefixed when pulled into your local development environment with `vercel env pull`. For example, `VERCEL_ENV` will not be prefixed to `NEXT_PUBLIC_VERCEL_ENV`.
To use framework-prefixed environment variables locally:
  1. [Define them in your project settings](https://vercel.com/docs/environment-variables#creating-environment-variables) with the appropriate prefix
  2. Scope them to `Development`
  3. Pull them into your local environment with Vercel CLI using the `vercel env pull` command


##  [Framework environment variables](https://vercel.com/docs/environment-variables/framework-environment-variables#framework-environment-variables)[](https://vercel.com/docs/environment-variables/framework-environment-variables#framework-environment-variables)
Next.jsNuxtCreate React AppGatsby.jsSolidStart (v0)SvelteKit (v0)AstroSolidStart (v1)Vue.jsRedwoodJSHydrogen (v1)ViteSanity (v3)Sanity
###  [NEXT_PUBLIC_VERCEL_ENV](https://vercel.com/docs/environment-variables/framework-environment-variables#NEXT_PUBLIC_VERCEL_ENV)[](https://vercel.com/docs/environment-variables/framework-environment-variables#NEXT_PUBLIC_VERCEL_ENV)
The [environment](https://vercel.com/docs/environment-variables#environments) that the app is deployed and running on. The value can be either `production`, `preview`, or `development`.
.env
```


NEXT_PUBLIC_VERCEL_ENV=production


```

###  [NEXT_PUBLIC_VERCEL_TARGET_ENV](https://vercel.com/docs/environment-variables/framework-environment-variables#NEXT_PUBLIC_VERCEL_TARGET_ENV)[](https://vercel.com/docs/environment-variables/framework-environment-variables#NEXT_PUBLIC_VERCEL_TARGET_ENV)
The [system or custom environment](https://vercel.com/docs/environment-variables#environments) that the app is deployed and running on. The value can be either `production`, `preview`, `development`, or the name of a [custom environment](https://vercel.com/docs/deployments/environments#custom-environments).
.env
```


NEXT_PUBLIC_VERCEL_TARGET_ENV=production


```

###  [NEXT_PUBLIC_VERCEL_URL](https://vercel.com/docs/environment-variables/framework-environment-variables#NEXT_PUBLIC_VERCEL_URL)[](https://vercel.com/docs/environment-variables/framework-environment-variables#NEXT_PUBLIC_VERCEL_URL)
The domain name of the [generated deployment URL](https://vercel.com/docs/deployments/generated-urls). Example: `*.vercel.app`. The value **does not** include the protocol scheme `https://`.
.env
```


NEXT_PUBLIC_VERCEL_URL=my-site.vercel.app


```

###  [NEXT_PUBLIC_VERCEL_BRANCH_URL](https://vercel.com/docs/environment-variables/framework-environment-variables#NEXT_PUBLIC_VERCEL_BRANCH_URL)[](https://vercel.com/docs/environment-variables/framework-environment-variables#NEXT_PUBLIC_VERCEL_BRANCH_URL)
The domain name of the [generated Git branch URL](https://vercel.com/docs/deployments/generated-urls#url-with-git-branch). Example: `*-git-*.vercel.app`. The value **does not** include the protocol scheme `https://`.
.env
```


NEXT_PUBLIC_VERCEL_BRANCH_URL=my-site-git-improve-about-page.vercel.app


```

###  [NEXT_PUBLIC_VERCEL_PROJECT_PRODUCTION_URL](https://vercel.com/docs/environment-variables/framework-environment-variables#NEXT_PUBLIC_VERCEL_PROJECT_PRODUCTION_URL)[](https://vercel.com/docs/environment-variables/framework-environment-variables#NEXT_PUBLIC_VERCEL_PROJECT_PRODUCTION_URL)
A production domain name of the project. We select the shortest production custom domain, or vercel.app domain if no custom domain is available. Note, that this is always set, even in preview deployments. This is useful to reliably generate links that point to production such as OG-image URLs. The value **does not** include the protocol scheme `https://`.
.env
```


NEXT_PUBLIC_VERCEL_PROJECT_PRODUCTION_URL=my-site.com


```

###  [NEXT_PUBLIC_VERCEL_GIT_PROVIDER](https://vercel.com/docs/environment-variables/framework-environment-variables#NEXT_PUBLIC_VERCEL_GIT_PROVIDER)[](https://vercel.com/docs/environment-variables/framework-environment-variables#NEXT_PUBLIC_VERCEL_GIT_PROVIDER)
The Git Provider the deployment is triggered from.
.env
```


NEXT_PUBLIC_VERCEL_GIT_PROVIDER=github


```

###  [NEXT_PUBLIC_VERCEL_GIT_REPO_SLUG](https://vercel.com/docs/environment-variables/framework-environment-variables#NEXT_PUBLIC_VERCEL_GIT_REPO_SLUG)[](https://vercel.com/docs/environment-variables/framework-environment-variables#NEXT_PUBLIC_VERCEL_GIT_REPO_SLUG)
The origin repository the deployment is triggered from.
.env
```


NEXT_PUBLIC_VERCEL_GIT_REPO_SLUG=my-site


```

###  [NEXT_PUBLIC_VERCEL_GIT_REPO_OWNER](https://vercel.com/docs/environment-variables/framework-environment-variables#NEXT_PUBLIC_VERCEL_GIT_REPO_OWNER)[](https://vercel.com/docs/environment-variables/framework-environment-variables#NEXT_PUBLIC_VERCEL_GIT_REPO_OWNER)
The account that owns the repository the deployment is triggered from.
.env
```


NEXT_PUBLIC_VERCEL_GIT_REPO_OWNER=acme


```

###  [NEXT_PUBLIC_VERCEL_GIT_REPO_ID](https://vercel.com/docs/environment-variables/framework-environment-variables#NEXT_PUBLIC_VERCEL_GIT_REPO_ID)[](https://vercel.com/docs/environment-variables/framework-environment-variables#NEXT_PUBLIC_VERCEL_GIT_REPO_ID)
The ID of the repository the deployment is triggered from.
.env
```


NEXT_PUBLIC_VERCEL_GIT_REPO_ID=117716146


```

###  [NEXT_PUBLIC_VERCEL_GIT_COMMIT_REF](https://vercel.com/docs/environment-variables/framework-environment-variables#NEXT_PUBLIC_VERCEL_GIT_COMMIT_REF)[](https://vercel.com/docs/environment-variables/framework-environment-variables#NEXT_PUBLIC_VERCEL_GIT_COMMIT_REF)
The git branch of the commit the deployment was triggered by.
.env
```


NEXT_PUBLIC_VERCEL_GIT_COMMIT_REF=improve-about-page


```

###  [NEXT_PUBLIC_VERCEL_GIT_COMMIT_SHA](https://vercel.com/docs/environment-variables/framework-environment-variables#NEXT_PUBLIC_VERCEL_GIT_COMMIT_SHA)[](https://vercel.com/docs/environment-variables/framework-environment-variables#NEXT_PUBLIC_VERCEL_GIT_COMMIT_SHA)
The git
.env
```


NEXT_PUBLIC_VERCEL_GIT_COMMIT_SHA=fa1eade47b73733d6312d5abfad33ce9e4068081


```

###  [NEXT_PUBLIC_VERCEL_GIT_COMMIT_MESSAGE](https://vercel.com/docs/environment-variables/framework-environment-variables#NEXT_PUBLIC_VERCEL_GIT_COMMIT_MESSAGE)[](https://vercel.com/docs/environment-variables/framework-environment-variables#NEXT_PUBLIC_VERCEL_GIT_COMMIT_MESSAGE)
The message attached to the commit the deployment was triggered by. The message is truncated if it exceeds 2048 bytes.
.env
```


NEXT_PUBLIC_VERCEL_GIT_COMMIT_MESSAGE=Update about page


```

###  [NEXT_PUBLIC_VERCEL_GIT_COMMIT_AUTHOR_LOGIN](https://vercel.com/docs/environment-variables/framework-environment-variables#NEXT_PUBLIC_VERCEL_GIT_COMMIT_AUTHOR_LOGIN)[](https://vercel.com/docs/environment-variables/framework-environment-variables#NEXT_PUBLIC_VERCEL_GIT_COMMIT_AUTHOR_LOGIN)
The username attached to the author of the commit that the project was deployed by.
.env
```


NEXT_PUBLIC_VERCEL_GIT_COMMIT_AUTHOR_LOGIN=johndoe


```

###  [NEXT_PUBLIC_VERCEL_GIT_COMMIT_AUTHOR_NAME](https://vercel.com/docs/environment-variables/framework-environment-variables#NEXT_PUBLIC_VERCEL_GIT_COMMIT_AUTHOR_NAME)[](https://vercel.com/docs/environment-variables/framework-environment-variables#NEXT_PUBLIC_VERCEL_GIT_COMMIT_AUTHOR_NAME)
The name attached to the author of the commit that the project was deployed by.
.env
```


NEXT_PUBLIC_VERCEL_GIT_COMMIT_AUTHOR_NAME=John Doe


```

###  [NEXT_PUBLIC_VERCEL_GIT_PULL_REQUEST_ID](https://vercel.com/docs/environment-variables/framework-environment-variables#NEXT_PUBLIC_VERCEL_GIT_PULL_REQUEST_ID)[](https://vercel.com/docs/environment-variables/framework-environment-variables#NEXT_PUBLIC_VERCEL_GIT_PULL_REQUEST_ID)
The pull request id the deployment was triggered by. If a deployment is created on a branch before a pull request is made, this value will be an empty string.
.env
```


NEXT_PUBLIC_VERCEL_GIT_PULL_REQUEST_ID=23


```

###  [NUXT_ENV_VERCEL_ENV](https://vercel.com/docs/environment-variables/framework-environment-variables#NUXT_ENV_VERCEL_ENV)[](https://vercel.com/docs/environment-variables/framework-environment-variables#NUXT_ENV_VERCEL_ENV)
The [environment](https://vercel.com/docs/environment-variables#environments) that the app is deployed and running on. The value can be either `production`, `preview`, or `development`.
.env
```


NUXT_ENV_VERCEL_ENV=production


```

###  [NUXT_ENV_VERCEL_TARGET_ENV](https://vercel.com/docs/environment-variables/framework-environment-variables#NUXT_ENV_VERCEL_TARGET_ENV)[](https://vercel.com/docs/environment-variables/framework-environment-variables#NUXT_ENV_VERCEL_TARGET_ENV)
The [system or custom environment](https://vercel.com/docs/environment-variables#environments) that the app is deployed and running on. The value can be either `production`, `preview`, `development`, or the name of a [custom environment](https://vercel.com/docs/deployments/environments#custom-environments).
.env
```


NUXT_ENV_VERCEL_TARGET_ENV=production


```

###  [NUXT_ENV_VERCEL_URL](https://vercel.com/docs/environment-variables/framework-environment-variables#NUXT_ENV_VERCEL_URL)[](https://vercel.com/docs/environment-variables/framework-environment-variables#NUXT_ENV_VERCEL_URL)
The domain name of the [generated deployment URL](https://vercel.com/docs/deployments/generated-urls). Example: `*.vercel.app`. The value **does not** include the protocol scheme `https://`.
.env
```


NUXT_ENV_VERCEL_URL=my-site.vercel.app


```

###  [NUXT_ENV_VERCEL_BRANCH_URL](https://vercel.com/docs/environment-variables/framework-environment-variables#NUXT_ENV_VERCEL_BRANCH_URL)[](https://vercel.com/docs/environment-variables/framework-environment-variables#NUXT_ENV_VERCEL_BRANCH_URL)
The domain name of the [generated Git branch URL](https://vercel.com/docs/deployments/generated-urls#url-with-git-branch). Example: `*-git-*.vercel.app`. The value **does not** include the protocol scheme `https://`.
.env
```


NUXT_ENV_VERCEL_BRANCH_URL=my-site-git-improve-about-page.vercel.app


```

###  [NUXT_ENV_VERCEL_PROJECT_PRODUCTION_URL](https://vercel.com/docs/environment-variables/framework-environment-variables#NUXT_ENV_VERCEL_PROJECT_PRODUCTION_URL)[](https://vercel.com/docs/environment-variables/framework-environment-variables#NUXT_ENV_VERCEL_PROJECT_PRODUCTION_URL)
A production domain name of the project. We select the shortest production custom domain, or vercel.app domain if no custom domain is available. Note, that this is always set, even in preview deployments. This is useful to reliably generate links that point to production such as OG-image URLs. The value **does not** include the protocol scheme `https://`.
.env
```


NUXT_ENV_VERCEL_PROJECT_PRODUCTION_URL=my-site.com


```

###  [NUXT_ENV_VERCEL_GIT_PROVIDER](https://vercel.com/docs/environment-variables/framework-environment-variables#NUXT_ENV_VERCEL_GIT_PROVIDER)[](https://vercel.com/docs/environment-variables/framework-environment-variables#NUXT_ENV_VERCEL_GIT_PROVIDER)
The Git Provider the deployment is triggered from.
.env
```


NUXT_ENV_VERCEL_GIT_PROVIDER=github


```

###  [NUXT_ENV_VERCEL_GIT_REPO_SLUG](https://vercel.com/docs/environment-variables/framework-environment-variables#NUXT_ENV_VERCEL_GIT_REPO_SLUG)[](https://vercel.com/docs/environment-variables/framework-environment-variables#NUXT_ENV_VERCEL_GIT_REPO_SLUG)
The origin repository the deployment is triggered from.
.env
```


NUXT_ENV_VERCEL_GIT_REPO_SLUG=my-site


```

###  [NUXT_ENV_VERCEL_GIT_REPO_OWNER](https://vercel.com/docs/environment-variables/framework-environment-variables#NUXT_ENV_VERCEL_GIT_REPO_OWNER)[](https://vercel.com/docs/environment-variables/framework-environment-variables#NUXT_ENV_VERCEL_GIT_REPO_OWNER)
The account that owns the repository the deployment is triggered from.
.env
```


NUXT_ENV_VERCEL_GIT_REPO_OWNER=acme


```

###  [NUXT_ENV_VERCEL_GIT_REPO_ID](https://vercel.com/docs/environment-variables/framework-environment-variables#NUXT_ENV_VERCEL_GIT_REPO_ID)[](https://vercel.com/docs/environment-variables/framework-environment-variables#NUXT_ENV_VERCEL_GIT_REPO_ID)
The ID of the repository the deployment is triggered from.
.env
```


NUXT_ENV_VERCEL_GIT_REPO_ID=117716146


```

###  [NUXT_ENV_VERCEL_GIT_COMMIT_REF](https://vercel.com/docs/environment-variables/framework-environment-variables#NUXT_ENV_VERCEL_GIT_COMMIT_REF)[](https://vercel.com/docs/environment-variables/framework-environment-variables#NUXT_ENV_VERCEL_GIT_COMMIT_REF)
The git branch of the commit the deployment was triggered by.
.env
```


NUXT_ENV_VERCEL_GIT_COMMIT_REF=improve-about-page


```

###  [NUXT_ENV_VERCEL_GIT_COMMIT_SHA](https://vercel.com/docs/environment-variables/framework-environment-variables#NUXT_ENV_VERCEL_GIT_COMMIT_SHA)[](https://vercel.com/docs/environment-variables/framework-environment-variables#NUXT_ENV_VERCEL_GIT_COMMIT_SHA)
The git
.env
```


NUXT_ENV_VERCEL_GIT_COMMIT_SHA=fa1eade47b73733d6312d5abfad33ce9e4068081


```

###  [NUXT_ENV_VERCEL_GIT_COMMIT_MESSAGE](https://vercel.com/docs/environment-variables/framework-environment-variables#NUXT_ENV_VERCEL_GIT_COMMIT_MESSAGE)[](https://vercel.com/docs/environment-variables/framework-environment-variables#NUXT_ENV_VERCEL_GIT_COMMIT_MESSAGE)
The message attached to the commit the deployment was triggered by. The message is truncated if it exceeds 2048 bytes.
.env
```


NUXT_ENV_VERCEL_GIT_COMMIT_MESSAGE=Update about page


```

###  [NUXT_ENV_VERCEL_GIT_COMMIT_AUTHOR_LOGIN](https://vercel.com/docs/environment-variables/framework-environment-variables#NUXT_ENV_VERCEL_GIT_COMMIT_AUTHOR_LOGIN)[](https://vercel.com/docs/environment-variables/framework-environment-variables#NUXT_ENV_VERCEL_GIT_COMMIT_AUTHOR_LOGIN)
The username attached to the author of the commit that the project was deployed by.
.env
```


NUXT_ENV_VERCEL_GIT_COMMIT_AUTHOR_LOGIN=johndoe


```

###  [NUXT_ENV_VERCEL_GIT_COMMIT_AUTHOR_NAME](https://vercel.com/docs/environment-variables/framework-environment-variables#NUXT_ENV_VERCEL_GIT_COMMIT_AUTHOR_NAME)[](https://vercel.com/docs/environment-variables/framework-environment-variables#NUXT_ENV_VERCEL_GIT_COMMIT_AUTHOR_NAME)
The name attached to the author of the commit that the project was deployed by.
.env
```


NUXT_ENV_VERCEL_GIT_COMMIT_AUTHOR_NAME=John Doe


```

###  [NUXT_ENV_VERCEL_GIT_PULL_REQUEST_ID](https://vercel.com/docs/environment-variables/framework-environment-variables#NUXT_ENV_VERCEL_GIT_PULL_REQUEST_ID)[](https://vercel.com/docs/environment-variables/framework-environment-variables#NUXT_ENV_VERCEL_GIT_PULL_REQUEST_ID)
The pull request id the deployment was triggered by. If a deployment is created on a branch before a pull request is made, this value will be an empty string.
.env
```


NUXT_ENV_VERCEL_GIT_PULL_REQUEST_ID=23


```

###  [REACT_APP_VERCEL_ENV](https://vercel.com/docs/environment-variables/framework-environment-variables#REACT_APP_VERCEL_ENV)[](https://vercel.com/docs/environment-variables/framework-environment-variables#REACT_APP_VERCEL_ENV)
The [environment](https://vercel.com/docs/environment-variables#environments) that the app is deployed and running on. The value can be either `production`, `preview`, or `development`.
.env
```


REACT_APP_VERCEL_ENV=production


```

###  [REACT_APP_VERCEL_TARGET_ENV](https://vercel.com/docs/environment-variables/framework-environment-variables#REACT_APP_VERCEL_TARGET_ENV)[](https://vercel.com/docs/environment-variables/framework-environment-variables#REACT_APP_VERCEL_TARGET_ENV)
The [system or custom environment](https://vercel.com/docs/environment-variables#environments) that the app is deployed and running on. The value can be either `production`, `preview`, `development`, or the name of a [custom environment](https://vercel.com/docs/deployments/environments#custom-environments).
.env
```


REACT_APP_VERCEL_TARGET_ENV=production


```

###  [REACT_APP_VERCEL_URL](https://vercel.com/docs/environment-variables/framework-environment-variables#REACT_APP_VERCEL_URL)[](https://vercel.com/docs/environment-variables/framework-environment-variables#REACT_APP_VERCEL_URL)
The domain name of the [generated deployment URL](https://vercel.com/docs/deployments/generated-urls). Example: `*.vercel.app`. The value **does not** include the protocol scheme `https://`.
.env
```


REACT_APP_VERCEL_URL=my-site.vercel.app


```

###  [REACT_APP_VERCEL_BRANCH_URL](https://vercel.com/docs/environment-variables/framework-environment-variables#REACT_APP_VERCEL_BRANCH_URL)[](https://vercel.com/docs/environment-variables/framework-environment-variables#REACT_APP_VERCEL_BRANCH_URL)
The domain name of the [generated Git branch URL](https://vercel.com/docs/deployments/generated-urls#url-with-git-branch). Example: `*-git-*.vercel.app`. The value **does not** include the protocol scheme `https://`.
.env
```


REACT_APP_VERCEL_BRANCH_URL=my-site-git-improve-about-page.vercel.app


```

###  [REACT_APP_VERCEL_PROJECT_PRODUCTION_URL](https://vercel.com/docs/environment-variables/framework-environment-variables#REACT_APP_VERCEL_PROJECT_PRODUCTION_URL)[](https://vercel.com/docs/environment-variables/framework-environment-variables#REACT_APP_VERCEL_PROJECT_PRODUCTION_URL)
A production domain name of the project. We select the shortest production custom domain, or vercel.app domain if no custom domain is available. Note, that this is always set, even in preview deployments. This is useful to reliably generate links that point to production such as OG-image URLs. The value **does not** include the protocol scheme `https://`.
.env
```


REACT_APP_VERCEL_PROJECT_PRODUCTION_URL=my-site.com


```

###  [REACT_APP_VERCEL_GIT_PROVIDER](https://vercel.com/docs/environment-variables/framework-environment-variables#REACT_APP_VERCEL_GIT_PROVIDER)[](https://vercel.com/docs/environment-variables/framework-environment-variables#REACT_APP_VERCEL_GIT_PROVIDER)
The Git Provider the deployment is triggered from.
.env
```


REACT_APP_VERCEL_GIT_PROVIDER=github


```

###  [REACT_APP_VERCEL_GIT_REPO_SLUG](https://vercel.com/docs/environment-variables/framework-environment-variables#REACT_APP_VERCEL_GIT_REPO_SLUG)[](https://vercel.com/docs/environment-variables/framework-environment-variables#REACT_APP_VERCEL_GIT_REPO_SLUG)
The origin repository the deployment is triggered from.
.env
```


REACT_APP_VERCEL_GIT_REPO_SLUG=my-site


```

###  [REACT_APP_VERCEL_GIT_REPO_OWNER](https://vercel.com/docs/environment-variables/framework-environment-variables#REACT_APP_VERCEL_GIT_REPO_OWNER)[](https://vercel.com/docs/environment-variables/framework-environment-variables#REACT_APP_VERCEL_GIT_REPO_OWNER)
The account that owns the repository the deployment is triggered from.
.env
```


REACT_APP_VERCEL_GIT_REPO_OWNER=acme


```

###  [REACT_APP_VERCEL_GIT_REPO_ID](https://vercel.com/docs/environment-variables/framework-environment-variables#REACT_APP_VERCEL_GIT_REPO_ID)[](https://vercel.com/docs/environment-variables/framework-environment-variables#REACT_APP_VERCEL_GIT_REPO_ID)
The ID of the repository the deployment is triggered from.
.env
```


REACT_APP_VERCEL_GIT_REPO_ID=117716146


```

###  [REACT_APP_VERCEL_GIT_COMMIT_REF](https://vercel.com/docs/environment-variables/framework-environment-variables#REACT_APP_VERCEL_GIT_COMMIT_REF)[](https://vercel.com/docs/environment-variables/framework-environment-variables#REACT_APP_VERCEL_GIT_COMMIT_REF)
The git branch of the commit the deployment was triggered by.
.env
```


REACT_APP_VERCEL_GIT_COMMIT_REF=improve-about-page


```

###  [REACT_APP_VERCEL_GIT_COMMIT_SHA](https://vercel.com/docs/environment-variables/framework-environment-variables#REACT_APP_VERCEL_GIT_COMMIT_SHA)[](https://vercel.com/docs/environment-variables/framework-environment-variables#REACT_APP_VERCEL_GIT_COMMIT_SHA)
The git
.env
```


REACT_APP_VERCEL_GIT_COMMIT_SHA=fa1eade47b73733d6312d5abfad33ce9e4068081


```

###  [REACT_APP_VERCEL_GIT_COMMIT_MESSAGE](https://vercel.com/docs/environment-variables/framework-environment-variables#REACT_APP_VERCEL_GIT_COMMIT_MESSAGE)[](https://vercel.com/docs/environment-variables/framework-environment-variables#REACT_APP_VERCEL_GIT_COMMIT_MESSAGE)
The message attached to the commit the deployment was triggered by. The message is truncated if it exceeds 2048 bytes.
.env
```


REACT_APP_VERCEL_GIT_COMMIT_MESSAGE=Update about page


```

###  [REACT_APP_VERCEL_GIT_COMMIT_AUTHOR_LOGIN](https://vercel.com/docs/environment-variables/framework-environment-variables#REACT_APP_VERCEL_GIT_COMMIT_AUTHOR_LOGIN)[](https://vercel.com/docs/environment-variables/framework-environment-variables#REACT_APP_VERCEL_GIT_COMMIT_AUTHOR_LOGIN)
The username attached to the author of the commit that the project was deployed by.
.env
```


REACT_APP_VERCEL_GIT_COMMIT_AUTHOR_LOGIN=johndoe


```

###  [REACT_APP_VERCEL_GIT_COMMIT_AUTHOR_NAME](https://vercel.com/docs/environment-variables/framework-environment-variables#REACT_APP_VERCEL_GIT_COMMIT_AUTHOR_NAME)[](https://vercel.com/docs/environment-variables/framework-environment-variables#REACT_APP_VERCEL_GIT_COMMIT_AUTHOR_NAME)
The name attached to the author of the commit that the project was deployed by.
.env
```


REACT_APP_VERCEL_GIT_COMMIT_AUTHOR_NAME=John Doe


```

###  [REACT_APP_VERCEL_GIT_PULL_REQUEST_ID](https://vercel.com/docs/environment-variables/framework-environment-variables#REACT_APP_VERCEL_GIT_PULL_REQUEST_ID)[](https://vercel.com/docs/environment-variables/framework-environment-variables#REACT_APP_VERCEL_GIT_PULL_REQUEST_ID)
The pull request id the deployment was triggered by. If a deployment is created on a branch before a pull request is made, this value will be an empty string.
.env
```


REACT_APP_VERCEL_GIT_PULL_REQUEST_ID=23


```

###  [GATSBY_VERCEL_ENV](https://vercel.com/docs/environment-variables/framework-environment-variables#GATSBY_VERCEL_ENV)[](https://vercel.com/docs/environment-variables/framework-environment-variables#GATSBY_VERCEL_ENV)
The [environment](https://vercel.com/docs/environment-variables#environments) that the app is deployed and running on. The value can be either `production`, `preview`, or `development`.
.env
```


GATSBY_VERCEL_ENV=production


```

###  [GATSBY_VERCEL_TARGET_ENV](https://vercel.com/docs/environment-variables/framework-environment-variables#GATSBY_VERCEL_TARGET_ENV)[](https://vercel.com/docs/environment-variables/framework-environment-variables#GATSBY_VERCEL_TARGET_ENV)
The [system or custom environment](https://vercel.com/docs/environment-variables#environments) that the app is deployed and running on. The value can be either `production`, `preview`, `development`, or the name of a [custom environment](https://vercel.com/docs/deployments/environments#custom-environments).
.env
```


GATSBY_VERCEL_TARGET_ENV=production


```

###  [GATSBY_VERCEL_URL](https://vercel.com/docs/environment-variables/framework-environment-variables#GATSBY_VERCEL_URL)[](https://vercel.com/docs/environment-variables/framework-environment-variables#GATSBY_VERCEL_URL)
The domain name of the [generated deployment URL](https://vercel.com/docs/deployments/generated-urls). Example: `*.vercel.app`. The value **does not** include the protocol scheme `https://`.
.env
```


GATSBY_VERCEL_URL=my-site.vercel.app


```

###  [GATSBY_VERCEL_BRANCH_URL](https://vercel.com/docs/environment-variables/framework-environment-variables#GATSBY_VERCEL_BRANCH_URL)[](https://vercel.com/docs/environment-variables/framework-environment-variables#GATSBY_VERCEL_BRANCH_URL)
The domain name of the [generated Git branch URL](https://vercel.com/docs/deployments/generated-urls#url-with-git-branch). Example: `*-git-*.vercel.app`. The value **does not** include the protocol scheme `https://`.
.env
```


GATSBY_VERCEL_BRANCH_URL=my-site-git-improve-about-page.vercel.app


```

###  [GATSBY_VERCEL_PROJECT_PRODUCTION_URL](https://vercel.com/docs/environment-variables/framework-environment-variables#GATSBY_VERCEL_PROJECT_PRODUCTION_URL)[](https://vercel.com/docs/environment-variables/framework-environment-variables#GATSBY_VERCEL_PROJECT_PRODUCTION_URL)
A production domain name of the project. We select the shortest production custom domain, or vercel.app domain if no custom domain is available. Note, that this is always set, even in preview deployments. This is useful to reliably generate links that point to production such as OG-image URLs. The value **does not** include the protocol scheme `https://`.
.env
```


GATSBY_VERCEL_PROJECT_PRODUCTION_URL=my-site.com


```

###  [GATSBY_VERCEL_GIT_PROVIDER](https://vercel.com/docs/environment-variables/framework-environment-variables#GATSBY_VERCEL_GIT_PROVIDER)[](https://vercel.com/docs/environment-variables/framework-environment-variables#GATSBY_VERCEL_GIT_PROVIDER)
The Git Provider the deployment is triggered from.
.env
```


GATSBY_VERCEL_GIT_PROVIDER=github


```

###  [GATSBY_VERCEL_GIT_REPO_SLUG](https://vercel.com/docs/environment-variables/framework-environment-variables#GATSBY_VERCEL_GIT_REPO_SLUG)[](https://vercel.com/docs/environment-variables/framework-environment-variables#GATSBY_VERCEL_GIT_REPO_SLUG)
The origin repository the deployment is triggered from.
.env
```


GATSBY_VERCEL_GIT_REPO_SLUG=my-site


```

###  [GATSBY_VERCEL_GIT_REPO_OWNER](https://vercel.com/docs/environment-variables/framework-environment-variables#GATSBY_VERCEL_GIT_REPO_OWNER)[](https://vercel.com/docs/environment-variables/framework-environment-variables#GATSBY_VERCEL_GIT_REPO_OWNER)
The account that owns the repository the deployment is triggered from.
.env
```


GATSBY_VERCEL_GIT_REPO_OWNER=acme


```

###  [GATSBY_VERCEL_GIT_REPO_ID](https://vercel.com/docs/environment-variables/framework-environment-variables#GATSBY_VERCEL_GIT_REPO_ID)[](https://vercel.com/docs/environment-variables/framework-environment-variables#GATSBY_VERCEL_GIT_REPO_ID)
The ID of the repository the deployment is triggered from.
.env
```


GATSBY_VERCEL_GIT_REPO_ID=117716146


```

###  [GATSBY_VERCEL_GIT_COMMIT_REF](https://vercel.com/docs/environment-variables/framework-environment-variables#GATSBY_VERCEL_GIT_COMMIT_REF)[](https://vercel.com/docs/environment-variables/framework-environment-variables#GATSBY_VERCEL_GIT_COMMIT_REF)
The git branch of the commit the deployment was triggered by.
.env
```


GATSBY_VERCEL_GIT_COMMIT_REF=improve-about-page


```

###  [GATSBY_VERCEL_GIT_COMMIT_SHA](https://vercel.com/docs/environment-variables/framework-environment-variables#GATSBY_VERCEL_GIT_COMMIT_SHA)[](https://vercel.com/docs/environment-variables/framework-environment-variables#GATSBY_VERCEL_GIT_COMMIT_SHA)
The git
.env
```


GATSBY_VERCEL_GIT_COMMIT_SHA=fa1eade47b73733d6312d5abfad33ce9e4068081


```

###  [GATSBY_VERCEL_GIT_COMMIT_MESSAGE](https://vercel.com/docs/environment-variables/framework-environment-variables#GATSBY_VERCEL_GIT_COMMIT_MESSAGE)[](https://vercel.com/docs/environment-variables/framework-environment-variables#GATSBY_VERCEL_GIT_COMMIT_MESSAGE)
The message attached to the commit the deployment was triggered by. The message is truncated if it exceeds 2048 bytes.
.env
```


GATSBY_VERCEL_GIT_COMMIT_MESSAGE=Update about page


```

###  [GATSBY_VERCEL_GIT_COMMIT_AUTHOR_LOGIN](https://vercel.com/docs/environment-variables/framework-environment-variables#GATSBY_VERCEL_GIT_COMMIT_AUTHOR_LOGIN)[](https://vercel.com/docs/environment-variables/framework-environment-variables#GATSBY_VERCEL_GIT_COMMIT_AUTHOR_LOGIN)
The username attached to the author of the commit that the project was deployed by.
.env
```


GATSBY_VERCEL_GIT_COMMIT_AUTHOR_LOGIN=johndoe


```

###  [GATSBY_VERCEL_GIT_COMMIT_AUTHOR_NAME](https://vercel.com/docs/environment-variables/framework-environment-variables#GATSBY_VERCEL_GIT_COMMIT_AUTHOR_NAME)[](https://vercel.com/docs/environment-variables/framework-environment-variables#GATSBY_VERCEL_GIT_COMMIT_AUTHOR_NAME)
The name attached to the author of the commit that the project was deployed by.
.env
```


GATSBY_VERCEL_GIT_COMMIT_AUTHOR_NAME=John Doe


```

###  [GATSBY_VERCEL_GIT_PULL_REQUEST_ID](https://vercel.com/docs/environment-variables/framework-environment-variables#GATSBY_VERCEL_GIT_PULL_REQUEST_ID)[](https://vercel.com/docs/environment-variables/framework-environment-variables#GATSBY_VERCEL_GIT_PULL_REQUEST_ID)
The pull request id the deployment was triggered by. If a deployment is created on a branch before a pull request is made, this value will be an empty string.
.env
```


GATSBY_VERCEL_GIT_PULL_REQUEST_ID=23


```

###  [VITE_VERCEL_ENV](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_ENV)[](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_ENV)
The [environment](https://vercel.com/docs/environment-variables#environments) that the app is deployed and running on. The value can be either `production`, `preview`, or `development`.
.env
```


VITE_VERCEL_ENV=production


```

###  [VITE_VERCEL_TARGET_ENV](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_TARGET_ENV)[](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_TARGET_ENV)
The [system or custom environment](https://vercel.com/docs/environment-variables#environments) that the app is deployed and running on. The value can be either `production`, `preview`, `development`, or the name of a [custom environment](https://vercel.com/docs/deployments/environments#custom-environments).
.env
```


VITE_VERCEL_TARGET_ENV=production


```

###  [VITE_VERCEL_URL](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_URL)[](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_URL)
The domain name of the [generated deployment URL](https://vercel.com/docs/deployments/generated-urls). Example: `*.vercel.app`. The value **does not** include the protocol scheme `https://`.
.env
```


VITE_VERCEL_URL=my-site.vercel.app


```

###  [VITE_VERCEL_BRANCH_URL](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_BRANCH_URL)[](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_BRANCH_URL)
The domain name of the [generated Git branch URL](https://vercel.com/docs/deployments/generated-urls#url-with-git-branch). Example: `*-git-*.vercel.app`. The value **does not** include the protocol scheme `https://`.
.env
```


VITE_VERCEL_BRANCH_URL=my-site-git-improve-about-page.vercel.app


```

###  [VITE_VERCEL_PROJECT_PRODUCTION_URL](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_PROJECT_PRODUCTION_URL)[](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_PROJECT_PRODUCTION_URL)
A production domain name of the project. We select the shortest production custom domain, or vercel.app domain if no custom domain is available. Note, that this is always set, even in preview deployments. This is useful to reliably generate links that point to production such as OG-image URLs. The value **does not** include the protocol scheme `https://`.
.env
```


VITE_VERCEL_PROJECT_PRODUCTION_URL=my-site.com


```

###  [VITE_VERCEL_GIT_PROVIDER](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_GIT_PROVIDER)[](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_GIT_PROVIDER)
The Git Provider the deployment is triggered from.
.env
```


VITE_VERCEL_GIT_PROVIDER=github


```

###  [VITE_VERCEL_GIT_REPO_SLUG](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_GIT_REPO_SLUG)[](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_GIT_REPO_SLUG)
The origin repository the deployment is triggered from.
.env
```


VITE_VERCEL_GIT_REPO_SLUG=my-site


```

###  [VITE_VERCEL_GIT_REPO_OWNER](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_GIT_REPO_OWNER)[](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_GIT_REPO_OWNER)
The account that owns the repository the deployment is triggered from.
.env
```


VITE_VERCEL_GIT_REPO_OWNER=acme


```

###  [VITE_VERCEL_GIT_REPO_ID](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_GIT_REPO_ID)[](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_GIT_REPO_ID)
The ID of the repository the deployment is triggered from.
.env
```


VITE_VERCEL_GIT_REPO_ID=117716146


```

###  [VITE_VERCEL_GIT_COMMIT_REF](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_GIT_COMMIT_REF)[](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_GIT_COMMIT_REF)
The git branch of the commit the deployment was triggered by.
.env
```


VITE_VERCEL_GIT_COMMIT_REF=improve-about-page


```

###  [VITE_VERCEL_GIT_COMMIT_SHA](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_GIT_COMMIT_SHA)[](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_GIT_COMMIT_SHA)
The git
.env
```


VITE_VERCEL_GIT_COMMIT_SHA=fa1eade47b73733d6312d5abfad33ce9e4068081


```

###  [VITE_VERCEL_GIT_COMMIT_MESSAGE](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_GIT_COMMIT_MESSAGE)[](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_GIT_COMMIT_MESSAGE)
The message attached to the commit the deployment was triggered by. The message is truncated if it exceeds 2048 bytes.
.env
```


VITE_VERCEL_GIT_COMMIT_MESSAGE=Update about page


```

###  [VITE_VERCEL_GIT_COMMIT_AUTHOR_LOGIN](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_GIT_COMMIT_AUTHOR_LOGIN)[](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_GIT_COMMIT_AUTHOR_LOGIN)
The username attached to the author of the commit that the project was deployed by.
.env
```


VITE_VERCEL_GIT_COMMIT_AUTHOR_LOGIN=johndoe


```

###  [VITE_VERCEL_GIT_COMMIT_AUTHOR_NAME](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_GIT_COMMIT_AUTHOR_NAME)[](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_GIT_COMMIT_AUTHOR_NAME)
The name attached to the author of the commit that the project was deployed by.
.env
```


VITE_VERCEL_GIT_COMMIT_AUTHOR_NAME=John Doe


```

###  [VITE_VERCEL_GIT_PULL_REQUEST_ID](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_GIT_PULL_REQUEST_ID)[](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_GIT_PULL_REQUEST_ID)
The pull request id the deployment was triggered by. If a deployment is created on a branch before a pull request is made, this value will be an empty string.
.env
```


VITE_VERCEL_GIT_PULL_REQUEST_ID=23


```

###  [VITE_VERCEL_ENV](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_ENV)[](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_ENV)
The [environment](https://vercel.com/docs/environment-variables#environments) that the app is deployed and running on. The value can be either `production`, `preview`, or `development`.
.env
```


VITE_VERCEL_ENV=production


```

###  [VITE_VERCEL_TARGET_ENV](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_TARGET_ENV)[](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_TARGET_ENV)
The [system or custom environment](https://vercel.com/docs/environment-variables#environments) that the app is deployed and running on. The value can be either `production`, `preview`, `development`, or the name of a [custom environment](https://vercel.com/docs/deployments/environments#custom-environments).
.env
```


VITE_VERCEL_TARGET_ENV=production


```

###  [VITE_VERCEL_URL](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_URL)[](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_URL)
The domain name of the [generated deployment URL](https://vercel.com/docs/deployments/generated-urls). Example: `*.vercel.app`. The value **does not** include the protocol scheme `https://`.
.env
```


VITE_VERCEL_URL=my-site.vercel.app


```

###  [VITE_VERCEL_BRANCH_URL](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_BRANCH_URL)[](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_BRANCH_URL)
The domain name of the [generated Git branch URL](https://vercel.com/docs/deployments/generated-urls#url-with-git-branch). Example: `*-git-*.vercel.app`. The value **does not** include the protocol scheme `https://`.
.env
```


VITE_VERCEL_BRANCH_URL=my-site-git-improve-about-page.vercel.app


```

###  [VITE_VERCEL_PROJECT_PRODUCTION_URL](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_PROJECT_PRODUCTION_URL)[](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_PROJECT_PRODUCTION_URL)
A production domain name of the project. We select the shortest production custom domain, or vercel.app domain if no custom domain is available. Note, that this is always set, even in preview deployments. This is useful to reliably generate links that point to production such as OG-image URLs. The value **does not** include the protocol scheme `https://`.
.env
```


VITE_VERCEL_PROJECT_PRODUCTION_URL=my-site.com


```

###  [VITE_VERCEL_GIT_PROVIDER](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_GIT_PROVIDER)[](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_GIT_PROVIDER)
The Git Provider the deployment is triggered from.
.env
```


VITE_VERCEL_GIT_PROVIDER=github


```

###  [VITE_VERCEL_GIT_REPO_SLUG](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_GIT_REPO_SLUG)[](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_GIT_REPO_SLUG)
The origin repository the deployment is triggered from.
.env
```


VITE_VERCEL_GIT_REPO_SLUG=my-site


```

###  [VITE_VERCEL_GIT_REPO_OWNER](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_GIT_REPO_OWNER)[](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_GIT_REPO_OWNER)
The account that owns the repository the deployment is triggered from.
.env
```


VITE_VERCEL_GIT_REPO_OWNER=acme


```

###  [VITE_VERCEL_GIT_REPO_ID](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_GIT_REPO_ID)[](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_GIT_REPO_ID)
The ID of the repository the deployment is triggered from.
.env
```


VITE_VERCEL_GIT_REPO_ID=117716146


```

###  [VITE_VERCEL_GIT_COMMIT_REF](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_GIT_COMMIT_REF)[](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_GIT_COMMIT_REF)
The git branch of the commit the deployment was triggered by.
.env
```


VITE_VERCEL_GIT_COMMIT_REF=improve-about-page


```

###  [VITE_VERCEL_GIT_COMMIT_SHA](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_GIT_COMMIT_SHA)[](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_GIT_COMMIT_SHA)
The git
.env
```


VITE_VERCEL_GIT_COMMIT_SHA=fa1eade47b73733d6312d5abfad33ce9e4068081


```

###  [VITE_VERCEL_GIT_COMMIT_MESSAGE](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_GIT_COMMIT_MESSAGE)[](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_GIT_COMMIT_MESSAGE)
The message attached to the commit the deployment was triggered by. The message is truncated if it exceeds 2048 bytes.
.env
```


VITE_VERCEL_GIT_COMMIT_MESSAGE=Update about page


```

###  [VITE_VERCEL_GIT_COMMIT_AUTHOR_LOGIN](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_GIT_COMMIT_AUTHOR_LOGIN)[](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_GIT_COMMIT_AUTHOR_LOGIN)
The username attached to the author of the commit that the project was deployed by.
.env
```


VITE_VERCEL_GIT_COMMIT_AUTHOR_LOGIN=johndoe


```

###  [VITE_VERCEL_GIT_COMMIT_AUTHOR_NAME](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_GIT_COMMIT_AUTHOR_NAME)[](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_GIT_COMMIT_AUTHOR_NAME)
The name attached to the author of the commit that the project was deployed by.
.env
```


VITE_VERCEL_GIT_COMMIT_AUTHOR_NAME=John Doe


```

###  [VITE_VERCEL_GIT_PULL_REQUEST_ID](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_GIT_PULL_REQUEST_ID)[](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_GIT_PULL_REQUEST_ID)
The pull request id the deployment was triggered by. If a deployment is created on a branch before a pull request is made, this value will be an empty string.
.env
```


VITE_VERCEL_GIT_PULL_REQUEST_ID=23


```

###  [PUBLIC_VERCEL_ENV](https://vercel.com/docs/environment-variables/framework-environment-variables#PUBLIC_VERCEL_ENV)[](https://vercel.com/docs/environment-variables/framework-environment-variables#PUBLIC_VERCEL_ENV)
The [environment](https://vercel.com/docs/environment-variables#environments) that the app is deployed and running on. The value can be either `production`, `preview`, or `development`.
.env
```


PUBLIC_VERCEL_ENV=production


```

###  [PUBLIC_VERCEL_TARGET_ENV](https://vercel.com/docs/environment-variables/framework-environment-variables#PUBLIC_VERCEL_TARGET_ENV)[](https://vercel.com/docs/environment-variables/framework-environment-variables#PUBLIC_VERCEL_TARGET_ENV)
The [system or custom environment](https://vercel.com/docs/environment-variables#environments) that the app is deployed and running on. The value can be either `production`, `preview`, `development`, or the name of a [custom environment](https://vercel.com/docs/deployments/environments#custom-environments).
.env
```


PUBLIC_VERCEL_TARGET_ENV=production


```

###  [PUBLIC_VERCEL_URL](https://vercel.com/docs/environment-variables/framework-environment-variables#PUBLIC_VERCEL_URL)[](https://vercel.com/docs/environment-variables/framework-environment-variables#PUBLIC_VERCEL_URL)
The domain name of the [generated deployment URL](https://vercel.com/docs/deployments/generated-urls). Example: `*.vercel.app`. The value **does not** include the protocol scheme `https://`.
.env
```


PUBLIC_VERCEL_URL=my-site.vercel.app


```

###  [PUBLIC_VERCEL_BRANCH_URL](https://vercel.com/docs/environment-variables/framework-environment-variables#PUBLIC_VERCEL_BRANCH_URL)[](https://vercel.com/docs/environment-variables/framework-environment-variables#PUBLIC_VERCEL_BRANCH_URL)
The domain name of the [generated Git branch URL](https://vercel.com/docs/deployments/generated-urls#url-with-git-branch). Example: `*-git-*.vercel.app`. The value **does not** include the protocol scheme `https://`.
.env
```


PUBLIC_VERCEL_BRANCH_URL=my-site-git-improve-about-page.vercel.app


```

###  [PUBLIC_VERCEL_PROJECT_PRODUCTION_URL](https://vercel.com/docs/environment-variables/framework-environment-variables#PUBLIC_VERCEL_PROJECT_PRODUCTION_URL)[](https://vercel.com/docs/environment-variables/framework-environment-variables#PUBLIC_VERCEL_PROJECT_PRODUCTION_URL)
A production domain name of the project. We select the shortest production custom domain, or vercel.app domain if no custom domain is available. Note, that this is always set, even in preview deployments. This is useful to reliably generate links that point to production such as OG-image URLs. The value **does not** include the protocol scheme `https://`.
.env
```


PUBLIC_VERCEL_PROJECT_PRODUCTION_URL=my-site.com


```

###  [PUBLIC_VERCEL_GIT_PROVIDER](https://vercel.com/docs/environment-variables/framework-environment-variables#PUBLIC_VERCEL_GIT_PROVIDER)[](https://vercel.com/docs/environment-variables/framework-environment-variables#PUBLIC_VERCEL_GIT_PROVIDER)
The Git Provider the deployment is triggered from.
.env
```


PUBLIC_VERCEL_GIT_PROVIDER=github


```

###  [PUBLIC_VERCEL_GIT_REPO_SLUG](https://vercel.com/docs/environment-variables/framework-environment-variables#PUBLIC_VERCEL_GIT_REPO_SLUG)[](https://vercel.com/docs/environment-variables/framework-environment-variables#PUBLIC_VERCEL_GIT_REPO_SLUG)
The origin repository the deployment is triggered from.
.env
```


PUBLIC_VERCEL_GIT_REPO_SLUG=my-site


```

###  [PUBLIC_VERCEL_GIT_REPO_OWNER](https://vercel.com/docs/environment-variables/framework-environment-variables#PUBLIC_VERCEL_GIT_REPO_OWNER)[](https://vercel.com/docs/environment-variables/framework-environment-variables#PUBLIC_VERCEL_GIT_REPO_OWNER)
The account that owns the repository the deployment is triggered from.
.env
```


PUBLIC_VERCEL_GIT_REPO_OWNER=acme


```

###  [PUBLIC_VERCEL_GIT_REPO_ID](https://vercel.com/docs/environment-variables/framework-environment-variables#PUBLIC_VERCEL_GIT_REPO_ID)[](https://vercel.com/docs/environment-variables/framework-environment-variables#PUBLIC_VERCEL_GIT_REPO_ID)
The ID of the repository the deployment is triggered from.
.env
```


PUBLIC_VERCEL_GIT_REPO_ID=117716146


```

###  [PUBLIC_VERCEL_GIT_COMMIT_REF](https://vercel.com/docs/environment-variables/framework-environment-variables#PUBLIC_VERCEL_GIT_COMMIT_REF)[](https://vercel.com/docs/environment-variables/framework-environment-variables#PUBLIC_VERCEL_GIT_COMMIT_REF)
The git branch of the commit the deployment was triggered by.
.env
```


PUBLIC_VERCEL_GIT_COMMIT_REF=improve-about-page


```

###  [PUBLIC_VERCEL_GIT_COMMIT_SHA](https://vercel.com/docs/environment-variables/framework-environment-variables#PUBLIC_VERCEL_GIT_COMMIT_SHA)[](https://vercel.com/docs/environment-variables/framework-environment-variables#PUBLIC_VERCEL_GIT_COMMIT_SHA)
The git
.env
```


PUBLIC_VERCEL_GIT_COMMIT_SHA=fa1eade47b73733d6312d5abfad33ce9e4068081


```

###  [PUBLIC_VERCEL_GIT_COMMIT_MESSAGE](https://vercel.com/docs/environment-variables/framework-environment-variables#PUBLIC_VERCEL_GIT_COMMIT_MESSAGE)[](https://vercel.com/docs/environment-variables/framework-environment-variables#PUBLIC_VERCEL_GIT_COMMIT_MESSAGE)
The message attached to the commit the deployment was triggered by. The message is truncated if it exceeds 2048 bytes.
.env
```


PUBLIC_VERCEL_GIT_COMMIT_MESSAGE=Update about page


```

###  [PUBLIC_VERCEL_GIT_COMMIT_AUTHOR_LOGIN](https://vercel.com/docs/environment-variables/framework-environment-variables#PUBLIC_VERCEL_GIT_COMMIT_AUTHOR_LOGIN)[](https://vercel.com/docs/environment-variables/framework-environment-variables#PUBLIC_VERCEL_GIT_COMMIT_AUTHOR_LOGIN)
The username attached to the author of the commit that the project was deployed by.
.env
```


PUBLIC_VERCEL_GIT_COMMIT_AUTHOR_LOGIN=johndoe


```

###  [PUBLIC_VERCEL_GIT_COMMIT_AUTHOR_NAME](https://vercel.com/docs/environment-variables/framework-environment-variables#PUBLIC_VERCEL_GIT_COMMIT_AUTHOR_NAME)[](https://vercel.com/docs/environment-variables/framework-environment-variables#PUBLIC_VERCEL_GIT_COMMIT_AUTHOR_NAME)
The name attached to the author of the commit that the project was deployed by.
.env
```


PUBLIC_VERCEL_GIT_COMMIT_AUTHOR_NAME=John Doe


```

###  [PUBLIC_VERCEL_GIT_PULL_REQUEST_ID](https://vercel.com/docs/environment-variables/framework-environment-variables#PUBLIC_VERCEL_GIT_PULL_REQUEST_ID)[](https://vercel.com/docs/environment-variables/framework-environment-variables#PUBLIC_VERCEL_GIT_PULL_REQUEST_ID)
The pull request id the deployment was triggered by. If a deployment is created on a branch before a pull request is made, this value will be an empty string.
.env
```


PUBLIC_VERCEL_GIT_PULL_REQUEST_ID=23


```

###  [VITE_VERCEL_ENV](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_ENV)[](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_ENV)
The [environment](https://vercel.com/docs/environment-variables#environments) that the app is deployed and running on. The value can be either `production`, `preview`, or `development`.
.env
```


VITE_VERCEL_ENV=production


```

###  [VITE_VERCEL_TARGET_ENV](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_TARGET_ENV)[](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_TARGET_ENV)
The [system or custom environment](https://vercel.com/docs/environment-variables#environments) that the app is deployed and running on. The value can be either `production`, `preview`, `development`, or the name of a [custom environment](https://vercel.com/docs/deployments/environments#custom-environments).
.env
```


VITE_VERCEL_TARGET_ENV=production


```

###  [VITE_VERCEL_URL](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_URL)[](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_URL)
The domain name of the [generated deployment URL](https://vercel.com/docs/deployments/generated-urls). Example: `*.vercel.app`. The value **does not** include the protocol scheme `https://`.
.env
```


VITE_VERCEL_URL=my-site.vercel.app


```

###  [VITE_VERCEL_BRANCH_URL](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_BRANCH_URL)[](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_BRANCH_URL)
The domain name of the [generated Git branch URL](https://vercel.com/docs/deployments/generated-urls#url-with-git-branch). Example: `*-git-*.vercel.app`. The value **does not** include the protocol scheme `https://`.
.env
```


VITE_VERCEL_BRANCH_URL=my-site-git-improve-about-page.vercel.app


```

###  [VITE_VERCEL_PROJECT_PRODUCTION_URL](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_PROJECT_PRODUCTION_URL)[](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_PROJECT_PRODUCTION_URL)
A production domain name of the project. We select the shortest production custom domain, or vercel.app domain if no custom domain is available. Note, that this is always set, even in preview deployments. This is useful to reliably generate links that point to production such as OG-image URLs. The value **does not** include the protocol scheme `https://`.
.env
```


VITE_VERCEL_PROJECT_PRODUCTION_URL=my-site.com


```

###  [VITE_VERCEL_GIT_PROVIDER](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_GIT_PROVIDER)[](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_GIT_PROVIDER)
The Git Provider the deployment is triggered from.
.env
```


VITE_VERCEL_GIT_PROVIDER=github


```

###  [VITE_VERCEL_GIT_REPO_SLUG](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_GIT_REPO_SLUG)[](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_GIT_REPO_SLUG)
The origin repository the deployment is triggered from.
.env
```


VITE_VERCEL_GIT_REPO_SLUG=my-site


```

###  [VITE_VERCEL_GIT_REPO_OWNER](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_GIT_REPO_OWNER)[](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_GIT_REPO_OWNER)
The account that owns the repository the deployment is triggered from.
.env
```


VITE_VERCEL_GIT_REPO_OWNER=acme


```

###  [VITE_VERCEL_GIT_REPO_ID](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_GIT_REPO_ID)[](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_GIT_REPO_ID)
The ID of the repository the deployment is triggered from.
.env
```


VITE_VERCEL_GIT_REPO_ID=117716146


```

###  [VITE_VERCEL_GIT_COMMIT_REF](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_GIT_COMMIT_REF)[](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_GIT_COMMIT_REF)
The git branch of the commit the deployment was triggered by.
.env
```


VITE_VERCEL_GIT_COMMIT_REF=improve-about-page


```

###  [VITE_VERCEL_GIT_COMMIT_SHA](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_GIT_COMMIT_SHA)[](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_GIT_COMMIT_SHA)
The git
.env
```


VITE_VERCEL_GIT_COMMIT_SHA=fa1eade47b73733d6312d5abfad33ce9e4068081


```

###  [VITE_VERCEL_GIT_COMMIT_MESSAGE](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_GIT_COMMIT_MESSAGE)[](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_GIT_COMMIT_MESSAGE)
The message attached to the commit the deployment was triggered by. The message is truncated if it exceeds 2048 bytes.
.env
```


VITE_VERCEL_GIT_COMMIT_MESSAGE=Update about page


```

###  [VITE_VERCEL_GIT_COMMIT_AUTHOR_LOGIN](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_GIT_COMMIT_AUTHOR_LOGIN)[](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_GIT_COMMIT_AUTHOR_LOGIN)
The username attached to the author of the commit that the project was deployed by.
.env
```


VITE_VERCEL_GIT_COMMIT_AUTHOR_LOGIN=johndoe


```

###  [VITE_VERCEL_GIT_COMMIT_AUTHOR_NAME](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_GIT_COMMIT_AUTHOR_NAME)[](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_GIT_COMMIT_AUTHOR_NAME)
The name attached to the author of the commit that the project was deployed by.
.env
```


VITE_VERCEL_GIT_COMMIT_AUTHOR_NAME=John Doe


```

###  [VITE_VERCEL_GIT_PULL_REQUEST_ID](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_GIT_PULL_REQUEST_ID)[](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_GIT_PULL_REQUEST_ID)
The pull request id the deployment was triggered by. If a deployment is created on a branch before a pull request is made, this value will be an empty string.
.env
```


VITE_VERCEL_GIT_PULL_REQUEST_ID=23


```

###  [VUE_APP_VERCEL_ENV](https://vercel.com/docs/environment-variables/framework-environment-variables#VUE_APP_VERCEL_ENV)[](https://vercel.com/docs/environment-variables/framework-environment-variables#VUE_APP_VERCEL_ENV)
The [environment](https://vercel.com/docs/environment-variables#environments) that the app is deployed and running on. The value can be either `production`, `preview`, or `development`.
.env
```


VUE_APP_VERCEL_ENV=production


```

###  [VUE_APP_VERCEL_TARGET_ENV](https://vercel.com/docs/environment-variables/framework-environment-variables#VUE_APP_VERCEL_TARGET_ENV)[](https://vercel.com/docs/environment-variables/framework-environment-variables#VUE_APP_VERCEL_TARGET_ENV)
The [system or custom environment](https://vercel.com/docs/environment-variables#environments) that the app is deployed and running on. The value can be either `production`, `preview`, `development`, or the name of a [custom environment](https://vercel.com/docs/deployments/environments#custom-environments).
.env
```


VUE_APP_VERCEL_TARGET_ENV=production


```

###  [VUE_APP_VERCEL_URL](https://vercel.com/docs/environment-variables/framework-environment-variables#VUE_APP_VERCEL_URL)[](https://vercel.com/docs/environment-variables/framework-environment-variables#VUE_APP_VERCEL_URL)
The domain name of the [generated deployment URL](https://vercel.com/docs/deployments/generated-urls). Example: `*.vercel.app`. The value **does not** include the protocol scheme `https://`.
.env
```


VUE_APP_VERCEL_URL=my-site.vercel.app


```

###  [VUE_APP_VERCEL_BRANCH_URL](https://vercel.com/docs/environment-variables/framework-environment-variables#VUE_APP_VERCEL_BRANCH_URL)[](https://vercel.com/docs/environment-variables/framework-environment-variables#VUE_APP_VERCEL_BRANCH_URL)
The domain name of the [generated Git branch URL](https://vercel.com/docs/deployments/generated-urls#url-with-git-branch). Example: `*-git-*.vercel.app`. The value **does not** include the protocol scheme `https://`.
.env
```


VUE_APP_VERCEL_BRANCH_URL=my-site-git-improve-about-page.vercel.app


```

###  [VUE_APP_VERCEL_PROJECT_PRODUCTION_URL](https://vercel.com/docs/environment-variables/framework-environment-variables#VUE_APP_VERCEL_PROJECT_PRODUCTION_URL)[](https://vercel.com/docs/environment-variables/framework-environment-variables#VUE_APP_VERCEL_PROJECT_PRODUCTION_URL)
A production domain name of the project. We select the shortest production custom domain, or vercel.app domain if no custom domain is available. Note, that this is always set, even in preview deployments. This is useful to reliably generate links that point to production such as OG-image URLs. The value **does not** include the protocol scheme `https://`.
.env
```


VUE_APP_VERCEL_PROJECT_PRODUCTION_URL=my-site.com


```

###  [VUE_APP_VERCEL_GIT_PROVIDER](https://vercel.com/docs/environment-variables/framework-environment-variables#VUE_APP_VERCEL_GIT_PROVIDER)[](https://vercel.com/docs/environment-variables/framework-environment-variables#VUE_APP_VERCEL_GIT_PROVIDER)
The Git Provider the deployment is triggered from.
.env
```


VUE_APP_VERCEL_GIT_PROVIDER=github


```

###  [VUE_APP_VERCEL_GIT_REPO_SLUG](https://vercel.com/docs/environment-variables/framework-environment-variables#VUE_APP_VERCEL_GIT_REPO_SLUG)[](https://vercel.com/docs/environment-variables/framework-environment-variables#VUE_APP_VERCEL_GIT_REPO_SLUG)
The origin repository the deployment is triggered from.
.env
```


VUE_APP_VERCEL_GIT_REPO_SLUG=my-site


```

###  [VUE_APP_VERCEL_GIT_REPO_OWNER](https://vercel.com/docs/environment-variables/framework-environment-variables#VUE_APP_VERCEL_GIT_REPO_OWNER)[](https://vercel.com/docs/environment-variables/framework-environment-variables#VUE_APP_VERCEL_GIT_REPO_OWNER)
The account that owns the repository the deployment is triggered from.
.env
```


VUE_APP_VERCEL_GIT_REPO_OWNER=acme


```

###  [VUE_APP_VERCEL_GIT_REPO_ID](https://vercel.com/docs/environment-variables/framework-environment-variables#VUE_APP_VERCEL_GIT_REPO_ID)[](https://vercel.com/docs/environment-variables/framework-environment-variables#VUE_APP_VERCEL_GIT_REPO_ID)
The ID of the repository the deployment is triggered from.
.env
```


VUE_APP_VERCEL_GIT_REPO_ID=117716146


```

###  [VUE_APP_VERCEL_GIT_COMMIT_REF](https://vercel.com/docs/environment-variables/framework-environment-variables#VUE_APP_VERCEL_GIT_COMMIT_REF)[](https://vercel.com/docs/environment-variables/framework-environment-variables#VUE_APP_VERCEL_GIT_COMMIT_REF)
The git branch of the commit the deployment was triggered by.
.env
```


VUE_APP_VERCEL_GIT_COMMIT_REF=improve-about-page


```

###  [VUE_APP_VERCEL_GIT_COMMIT_SHA](https://vercel.com/docs/environment-variables/framework-environment-variables#VUE_APP_VERCEL_GIT_COMMIT_SHA)[](https://vercel.com/docs/environment-variables/framework-environment-variables#VUE_APP_VERCEL_GIT_COMMIT_SHA)
The git
.env
```


VUE_APP_VERCEL_GIT_COMMIT_SHA=fa1eade47b73733d6312d5abfad33ce9e4068081


```

###  [VUE_APP_VERCEL_GIT_COMMIT_MESSAGE](https://vercel.com/docs/environment-variables/framework-environment-variables#VUE_APP_VERCEL_GIT_COMMIT_MESSAGE)[](https://vercel.com/docs/environment-variables/framework-environment-variables#VUE_APP_VERCEL_GIT_COMMIT_MESSAGE)
The message attached to the commit the deployment was triggered by. The message is truncated if it exceeds 2048 bytes.
.env
```


VUE_APP_VERCEL_GIT_COMMIT_MESSAGE=Update about page


```

###  [VUE_APP_VERCEL_GIT_COMMIT_AUTHOR_LOGIN](https://vercel.com/docs/environment-variables/framework-environment-variables#VUE_APP_VERCEL_GIT_COMMIT_AUTHOR_LOGIN)[](https://vercel.com/docs/environment-variables/framework-environment-variables#VUE_APP_VERCEL_GIT_COMMIT_AUTHOR_LOGIN)
The username attached to the author of the commit that the project was deployed by.
.env
```


VUE_APP_VERCEL_GIT_COMMIT_AUTHOR_LOGIN=johndoe


```

###  [VUE_APP_VERCEL_GIT_COMMIT_AUTHOR_NAME](https://vercel.com/docs/environment-variables/framework-environment-variables#VUE_APP_VERCEL_GIT_COMMIT_AUTHOR_NAME)[](https://vercel.com/docs/environment-variables/framework-environment-variables#VUE_APP_VERCEL_GIT_COMMIT_AUTHOR_NAME)
The name attached to the author of the commit that the project was deployed by.
.env
```


VUE_APP_VERCEL_GIT_COMMIT_AUTHOR_NAME=John Doe


```

###  [VUE_APP_VERCEL_GIT_PULL_REQUEST_ID](https://vercel.com/docs/environment-variables/framework-environment-variables#VUE_APP_VERCEL_GIT_PULL_REQUEST_ID)[](https://vercel.com/docs/environment-variables/framework-environment-variables#VUE_APP_VERCEL_GIT_PULL_REQUEST_ID)
The pull request id the deployment was triggered by. If a deployment is created on a branch before a pull request is made, this value will be an empty string.
.env
```


VUE_APP_VERCEL_GIT_PULL_REQUEST_ID=23


```

###  [REDWOOD_ENV_VERCEL_ENV](https://vercel.com/docs/environment-variables/framework-environment-variables#REDWOOD_ENV_VERCEL_ENV)[](https://vercel.com/docs/environment-variables/framework-environment-variables#REDWOOD_ENV_VERCEL_ENV)
The [environment](https://vercel.com/docs/environment-variables#environments) that the app is deployed and running on. The value can be either `production`, `preview`, or `development`.
.env
```


REDWOOD_ENV_VERCEL_ENV=production


```

###  [REDWOOD_ENV_VERCEL_TARGET_ENV](https://vercel.com/docs/environment-variables/framework-environment-variables#REDWOOD_ENV_VERCEL_TARGET_ENV)[](https://vercel.com/docs/environment-variables/framework-environment-variables#REDWOOD_ENV_VERCEL_TARGET_ENV)
The [system or custom environment](https://vercel.com/docs/environment-variables#environments) that the app is deployed and running on. The value can be either `production`, `preview`, `development`, or the name of a [custom environment](https://vercel.com/docs/deployments/environments#custom-environments).
.env
```


REDWOOD_ENV_VERCEL_TARGET_ENV=production


```

###  [REDWOOD_ENV_VERCEL_URL](https://vercel.com/docs/environment-variables/framework-environment-variables#REDWOOD_ENV_VERCEL_URL)[](https://vercel.com/docs/environment-variables/framework-environment-variables#REDWOOD_ENV_VERCEL_URL)
The domain name of the [generated deployment URL](https://vercel.com/docs/deployments/generated-urls). Example: `*.vercel.app`. The value **does not** include the protocol scheme `https://`.
.env
```


REDWOOD_ENV_VERCEL_URL=my-site.vercel.app


```

###  [REDWOOD_ENV_VERCEL_BRANCH_URL](https://vercel.com/docs/environment-variables/framework-environment-variables#REDWOOD_ENV_VERCEL_BRANCH_URL)[](https://vercel.com/docs/environment-variables/framework-environment-variables#REDWOOD_ENV_VERCEL_BRANCH_URL)
The domain name of the [generated Git branch URL](https://vercel.com/docs/deployments/generated-urls#url-with-git-branch). Example: `*-git-*.vercel.app`. The value **does not** include the protocol scheme `https://`.
.env
```


REDWOOD_ENV_VERCEL_BRANCH_URL=my-site-git-improve-about-page.vercel.app


```

###  [REDWOOD_ENV_VERCEL_PROJECT_PRODUCTION_URL](https://vercel.com/docs/environment-variables/framework-environment-variables#REDWOOD_ENV_VERCEL_PROJECT_PRODUCTION_URL)[](https://vercel.com/docs/environment-variables/framework-environment-variables#REDWOOD_ENV_VERCEL_PROJECT_PRODUCTION_URL)
A production domain name of the project. We select the shortest production custom domain, or vercel.app domain if no custom domain is available. Note, that this is always set, even in preview deployments. This is useful to reliably generate links that point to production such as OG-image URLs. The value **does not** include the protocol scheme `https://`.
.env
```


REDWOOD_ENV_VERCEL_PROJECT_PRODUCTION_URL=my-site.com


```

###  [REDWOOD_ENV_VERCEL_GIT_PROVIDER](https://vercel.com/docs/environment-variables/framework-environment-variables#REDWOOD_ENV_VERCEL_GIT_PROVIDER)[](https://vercel.com/docs/environment-variables/framework-environment-variables#REDWOOD_ENV_VERCEL_GIT_PROVIDER)
The Git Provider the deployment is triggered from.
.env
```


REDWOOD_ENV_VERCEL_GIT_PROVIDER=github


```

###  [REDWOOD_ENV_VERCEL_GIT_REPO_SLUG](https://vercel.com/docs/environment-variables/framework-environment-variables#REDWOOD_ENV_VERCEL_GIT_REPO_SLUG)[](https://vercel.com/docs/environment-variables/framework-environment-variables#REDWOOD_ENV_VERCEL_GIT_REPO_SLUG)
The origin repository the deployment is triggered from.
.env
```


REDWOOD_ENV_VERCEL_GIT_REPO_SLUG=my-site


```

###  [REDWOOD_ENV_VERCEL_GIT_REPO_OWNER](https://vercel.com/docs/environment-variables/framework-environment-variables#REDWOOD_ENV_VERCEL_GIT_REPO_OWNER)[](https://vercel.com/docs/environment-variables/framework-environment-variables#REDWOOD_ENV_VERCEL_GIT_REPO_OWNER)
The account that owns the repository the deployment is triggered from.
.env
```


REDWOOD_ENV_VERCEL_GIT_REPO_OWNER=acme


```

###  [REDWOOD_ENV_VERCEL_GIT_REPO_ID](https://vercel.com/docs/environment-variables/framework-environment-variables#REDWOOD_ENV_VERCEL_GIT_REPO_ID)[](https://vercel.com/docs/environment-variables/framework-environment-variables#REDWOOD_ENV_VERCEL_GIT_REPO_ID)
The ID of the repository the deployment is triggered from.
.env
```


REDWOOD_ENV_VERCEL_GIT_REPO_ID=117716146


```

###  [REDWOOD_ENV_VERCEL_GIT_COMMIT_REF](https://vercel.com/docs/environment-variables/framework-environment-variables#REDWOOD_ENV_VERCEL_GIT_COMMIT_REF)[](https://vercel.com/docs/environment-variables/framework-environment-variables#REDWOOD_ENV_VERCEL_GIT_COMMIT_REF)
The git branch of the commit the deployment was triggered by.
.env
```


REDWOOD_ENV_VERCEL_GIT_COMMIT_REF=improve-about-page


```

###  [REDWOOD_ENV_VERCEL_GIT_COMMIT_SHA](https://vercel.com/docs/environment-variables/framework-environment-variables#REDWOOD_ENV_VERCEL_GIT_COMMIT_SHA)[](https://vercel.com/docs/environment-variables/framework-environment-variables#REDWOOD_ENV_VERCEL_GIT_COMMIT_SHA)
The git
.env
```


REDWOOD_ENV_VERCEL_GIT_COMMIT_SHA=fa1eade47b73733d6312d5abfad33ce9e4068081


```

###  [REDWOOD_ENV_VERCEL_GIT_COMMIT_MESSAGE](https://vercel.com/docs/environment-variables/framework-environment-variables#REDWOOD_ENV_VERCEL_GIT_COMMIT_MESSAGE)[](https://vercel.com/docs/environment-variables/framework-environment-variables#REDWOOD_ENV_VERCEL_GIT_COMMIT_MESSAGE)
The message attached to the commit the deployment was triggered by. The message is truncated if it exceeds 2048 bytes.
.env
```


REDWOOD_ENV_VERCEL_GIT_COMMIT_MESSAGE=Update about page


```

###  [REDWOOD_ENV_VERCEL_GIT_COMMIT_AUTHOR_LOGIN](https://vercel.com/docs/environment-variables/framework-environment-variables#REDWOOD_ENV_VERCEL_GIT_COMMIT_AUTHOR_LOGIN)[](https://vercel.com/docs/environment-variables/framework-environment-variables#REDWOOD_ENV_VERCEL_GIT_COMMIT_AUTHOR_LOGIN)
The username attached to the author of the commit that the project was deployed by.
.env
```


REDWOOD_ENV_VERCEL_GIT_COMMIT_AUTHOR_LOGIN=johndoe


```

###  [REDWOOD_ENV_VERCEL_GIT_COMMIT_AUTHOR_NAME](https://vercel.com/docs/environment-variables/framework-environment-variables#REDWOOD_ENV_VERCEL_GIT_COMMIT_AUTHOR_NAME)[](https://vercel.com/docs/environment-variables/framework-environment-variables#REDWOOD_ENV_VERCEL_GIT_COMMIT_AUTHOR_NAME)
The name attached to the author of the commit that the project was deployed by.
.env
```


REDWOOD_ENV_VERCEL_GIT_COMMIT_AUTHOR_NAME=John Doe


```

###  [REDWOOD_ENV_VERCEL_GIT_PULL_REQUEST_ID](https://vercel.com/docs/environment-variables/framework-environment-variables#REDWOOD_ENV_VERCEL_GIT_PULL_REQUEST_ID)[](https://vercel.com/docs/environment-variables/framework-environment-variables#REDWOOD_ENV_VERCEL_GIT_PULL_REQUEST_ID)
The pull request id the deployment was triggered by. If a deployment is created on a branch before a pull request is made, this value will be an empty string.
.env
```


REDWOOD_ENV_VERCEL_GIT_PULL_REQUEST_ID=23


```

###  [PUBLIC_VERCEL_ENV](https://vercel.com/docs/environment-variables/framework-environment-variables#PUBLIC_VERCEL_ENV)[](https://vercel.com/docs/environment-variables/framework-environment-variables#PUBLIC_VERCEL_ENV)
The [environment](https://vercel.com/docs/environment-variables#environments) that the app is deployed and running on. The value can be either `production`, `preview`, or `development`.
.env
```


PUBLIC_VERCEL_ENV=production


```

###  [PUBLIC_VERCEL_TARGET_ENV](https://vercel.com/docs/environment-variables/framework-environment-variables#PUBLIC_VERCEL_TARGET_ENV)[](https://vercel.com/docs/environment-variables/framework-environment-variables#PUBLIC_VERCEL_TARGET_ENV)
The [system or custom environment](https://vercel.com/docs/environment-variables#environments) that the app is deployed and running on. The value can be either `production`, `preview`, `development`, or the name of a [custom environment](https://vercel.com/docs/deployments/environments#custom-environments).
.env
```


PUBLIC_VERCEL_TARGET_ENV=production


```

###  [PUBLIC_VERCEL_URL](https://vercel.com/docs/environment-variables/framework-environment-variables#PUBLIC_VERCEL_URL)[](https://vercel.com/docs/environment-variables/framework-environment-variables#PUBLIC_VERCEL_URL)
The domain name of the [generated deployment URL](https://vercel.com/docs/deployments/generated-urls). Example: `*.vercel.app`. The value **does not** include the protocol scheme `https://`.
.env
```


PUBLIC_VERCEL_URL=my-site.vercel.app


```

###  [PUBLIC_VERCEL_BRANCH_URL](https://vercel.com/docs/environment-variables/framework-environment-variables#PUBLIC_VERCEL_BRANCH_URL)[](https://vercel.com/docs/environment-variables/framework-environment-variables#PUBLIC_VERCEL_BRANCH_URL)
The domain name of the [generated Git branch URL](https://vercel.com/docs/deployments/generated-urls#url-with-git-branch). Example: `*-git-*.vercel.app`. The value **does not** include the protocol scheme `https://`.
.env
```


PUBLIC_VERCEL_BRANCH_URL=my-site-git-improve-about-page.vercel.app


```

###  [PUBLIC_VERCEL_PROJECT_PRODUCTION_URL](https://vercel.com/docs/environment-variables/framework-environment-variables#PUBLIC_VERCEL_PROJECT_PRODUCTION_URL)[](https://vercel.com/docs/environment-variables/framework-environment-variables#PUBLIC_VERCEL_PROJECT_PRODUCTION_URL)
A production domain name of the project. We select the shortest production custom domain, or vercel.app domain if no custom domain is available. Note, that this is always set, even in preview deployments. This is useful to reliably generate links that point to production such as OG-image URLs. The value **does not** include the protocol scheme `https://`.
.env
```


PUBLIC_VERCEL_PROJECT_PRODUCTION_URL=my-site.com


```

###  [PUBLIC_VERCEL_GIT_PROVIDER](https://vercel.com/docs/environment-variables/framework-environment-variables#PUBLIC_VERCEL_GIT_PROVIDER)[](https://vercel.com/docs/environment-variables/framework-environment-variables#PUBLIC_VERCEL_GIT_PROVIDER)
The Git Provider the deployment is triggered from.
.env
```


PUBLIC_VERCEL_GIT_PROVIDER=github


```

###  [PUBLIC_VERCEL_GIT_REPO_SLUG](https://vercel.com/docs/environment-variables/framework-environment-variables#PUBLIC_VERCEL_GIT_REPO_SLUG)[](https://vercel.com/docs/environment-variables/framework-environment-variables#PUBLIC_VERCEL_GIT_REPO_SLUG)
The origin repository the deployment is triggered from.
.env
```


PUBLIC_VERCEL_GIT_REPO_SLUG=my-site


```

###  [PUBLIC_VERCEL_GIT_REPO_OWNER](https://vercel.com/docs/environment-variables/framework-environment-variables#PUBLIC_VERCEL_GIT_REPO_OWNER)[](https://vercel.com/docs/environment-variables/framework-environment-variables#PUBLIC_VERCEL_GIT_REPO_OWNER)
The account that owns the repository the deployment is triggered from.
.env
```


PUBLIC_VERCEL_GIT_REPO_OWNER=acme


```

###  [PUBLIC_VERCEL_GIT_REPO_ID](https://vercel.com/docs/environment-variables/framework-environment-variables#PUBLIC_VERCEL_GIT_REPO_ID)[](https://vercel.com/docs/environment-variables/framework-environment-variables#PUBLIC_VERCEL_GIT_REPO_ID)
The ID of the repository the deployment is triggered from.
.env
```


PUBLIC_VERCEL_GIT_REPO_ID=117716146


```

###  [PUBLIC_VERCEL_GIT_COMMIT_REF](https://vercel.com/docs/environment-variables/framework-environment-variables#PUBLIC_VERCEL_GIT_COMMIT_REF)[](https://vercel.com/docs/environment-variables/framework-environment-variables#PUBLIC_VERCEL_GIT_COMMIT_REF)
The git branch of the commit the deployment was triggered by.
.env
```


PUBLIC_VERCEL_GIT_COMMIT_REF=improve-about-page


```

###  [PUBLIC_VERCEL_GIT_COMMIT_SHA](https://vercel.com/docs/environment-variables/framework-environment-variables#PUBLIC_VERCEL_GIT_COMMIT_SHA)[](https://vercel.com/docs/environment-variables/framework-environment-variables#PUBLIC_VERCEL_GIT_COMMIT_SHA)
The git
.env
```


PUBLIC_VERCEL_GIT_COMMIT_SHA=fa1eade47b73733d6312d5abfad33ce9e4068081


```

###  [PUBLIC_VERCEL_GIT_COMMIT_MESSAGE](https://vercel.com/docs/environment-variables/framework-environment-variables#PUBLIC_VERCEL_GIT_COMMIT_MESSAGE)[](https://vercel.com/docs/environment-variables/framework-environment-variables#PUBLIC_VERCEL_GIT_COMMIT_MESSAGE)
The message attached to the commit the deployment was triggered by. The message is truncated if it exceeds 2048 bytes.
.env
```


PUBLIC_VERCEL_GIT_COMMIT_MESSAGE=Update about page


```

###  [PUBLIC_VERCEL_GIT_COMMIT_AUTHOR_LOGIN](https://vercel.com/docs/environment-variables/framework-environment-variables#PUBLIC_VERCEL_GIT_COMMIT_AUTHOR_LOGIN)[](https://vercel.com/docs/environment-variables/framework-environment-variables#PUBLIC_VERCEL_GIT_COMMIT_AUTHOR_LOGIN)
The username attached to the author of the commit that the project was deployed by.
.env
```


PUBLIC_VERCEL_GIT_COMMIT_AUTHOR_LOGIN=johndoe


```

###  [PUBLIC_VERCEL_GIT_COMMIT_AUTHOR_NAME](https://vercel.com/docs/environment-variables/framework-environment-variables#PUBLIC_VERCEL_GIT_COMMIT_AUTHOR_NAME)[](https://vercel.com/docs/environment-variables/framework-environment-variables#PUBLIC_VERCEL_GIT_COMMIT_AUTHOR_NAME)
The name attached to the author of the commit that the project was deployed by.
.env
```


PUBLIC_VERCEL_GIT_COMMIT_AUTHOR_NAME=John Doe


```

###  [PUBLIC_VERCEL_GIT_PULL_REQUEST_ID](https://vercel.com/docs/environment-variables/framework-environment-variables#PUBLIC_VERCEL_GIT_PULL_REQUEST_ID)[](https://vercel.com/docs/environment-variables/framework-environment-variables#PUBLIC_VERCEL_GIT_PULL_REQUEST_ID)
The pull request id the deployment was triggered by. If a deployment is created on a branch before a pull request is made, this value will be an empty string.
.env
```


PUBLIC_VERCEL_GIT_PULL_REQUEST_ID=23


```

###  [VITE_VERCEL_ENV](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_ENV)[](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_ENV)
The [environment](https://vercel.com/docs/environment-variables#environments) that the app is deployed and running on. The value can be either `production`, `preview`, or `development`.
.env
```


VITE_VERCEL_ENV=production


```

###  [VITE_VERCEL_TARGET_ENV](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_TARGET_ENV)[](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_TARGET_ENV)
The [system or custom environment](https://vercel.com/docs/environment-variables#environments) that the app is deployed and running on. The value can be either `production`, `preview`, `development`, or the name of a [custom environment](https://vercel.com/docs/deployments/environments#custom-environments).
.env
```


VITE_VERCEL_TARGET_ENV=production


```

###  [VITE_VERCEL_URL](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_URL)[](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_URL)
The domain name of the [generated deployment URL](https://vercel.com/docs/deployments/generated-urls). Example: `*.vercel.app`. The value **does not** include the protocol scheme `https://`.
.env
```


VITE_VERCEL_URL=my-site.vercel.app


```

###  [VITE_VERCEL_BRANCH_URL](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_BRANCH_URL)[](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_BRANCH_URL)
The domain name of the [generated Git branch URL](https://vercel.com/docs/deployments/generated-urls#url-with-git-branch). Example: `*-git-*.vercel.app`. The value **does not** include the protocol scheme `https://`.
.env
```


VITE_VERCEL_BRANCH_URL=my-site-git-improve-about-page.vercel.app


```

###  [VITE_VERCEL_PROJECT_PRODUCTION_URL](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_PROJECT_PRODUCTION_URL)[](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_PROJECT_PRODUCTION_URL)
A production domain name of the project. We select the shortest production custom domain, or vercel.app domain if no custom domain is available. Note, that this is always set, even in preview deployments. This is useful to reliably generate links that point to production such as OG-image URLs. The value **does not** include the protocol scheme `https://`.
.env
```


VITE_VERCEL_PROJECT_PRODUCTION_URL=my-site.com


```

###  [VITE_VERCEL_GIT_PROVIDER](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_GIT_PROVIDER)[](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_GIT_PROVIDER)
The Git Provider the deployment is triggered from.
.env
```


VITE_VERCEL_GIT_PROVIDER=github


```

###  [VITE_VERCEL_GIT_REPO_SLUG](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_GIT_REPO_SLUG)[](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_GIT_REPO_SLUG)
The origin repository the deployment is triggered from.
.env
```


VITE_VERCEL_GIT_REPO_SLUG=my-site


```

###  [VITE_VERCEL_GIT_REPO_OWNER](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_GIT_REPO_OWNER)[](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_GIT_REPO_OWNER)
The account that owns the repository the deployment is triggered from.
.env
```


VITE_VERCEL_GIT_REPO_OWNER=acme


```

###  [VITE_VERCEL_GIT_REPO_ID](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_GIT_REPO_ID)[](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_GIT_REPO_ID)
The ID of the repository the deployment is triggered from.
.env
```


VITE_VERCEL_GIT_REPO_ID=117716146


```

###  [VITE_VERCEL_GIT_COMMIT_REF](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_GIT_COMMIT_REF)[](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_GIT_COMMIT_REF)
The git branch of the commit the deployment was triggered by.
.env
```


VITE_VERCEL_GIT_COMMIT_REF=improve-about-page


```

###  [VITE_VERCEL_GIT_COMMIT_SHA](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_GIT_COMMIT_SHA)[](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_GIT_COMMIT_SHA)
The git
.env
```


VITE_VERCEL_GIT_COMMIT_SHA=fa1eade47b73733d6312d5abfad33ce9e4068081


```

###  [VITE_VERCEL_GIT_COMMIT_MESSAGE](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_GIT_COMMIT_MESSAGE)[](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_GIT_COMMIT_MESSAGE)
The message attached to the commit the deployment was triggered by. The message is truncated if it exceeds 2048 bytes.
.env
```


VITE_VERCEL_GIT_COMMIT_MESSAGE=Update about page


```

###  [VITE_VERCEL_GIT_COMMIT_AUTHOR_LOGIN](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_GIT_COMMIT_AUTHOR_LOGIN)[](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_GIT_COMMIT_AUTHOR_LOGIN)
The username attached to the author of the commit that the project was deployed by.
.env
```


VITE_VERCEL_GIT_COMMIT_AUTHOR_LOGIN=johndoe


```

###  [VITE_VERCEL_GIT_COMMIT_AUTHOR_NAME](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_GIT_COMMIT_AUTHOR_NAME)[](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_GIT_COMMIT_AUTHOR_NAME)
The name attached to the author of the commit that the project was deployed by.
.env
```


VITE_VERCEL_GIT_COMMIT_AUTHOR_NAME=John Doe


```

###  [VITE_VERCEL_GIT_PULL_REQUEST_ID](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_GIT_PULL_REQUEST_ID)[](https://vercel.com/docs/environment-variables/framework-environment-variables#VITE_VERCEL_GIT_PULL_REQUEST_ID)
The pull request id the deployment was triggered by. If a deployment is created on a branch before a pull request is made, this value will be an empty string.
.env
```


VITE_VERCEL_GIT_PULL_REQUEST_ID=23


```

###  [SANITY_STUDIO_VERCEL_ENV](https://vercel.com/docs/environment-variables/framework-environment-variables#SANITY_STUDIO_VERCEL_ENV)[](https://vercel.com/docs/environment-variables/framework-environment-variables#SANITY_STUDIO_VERCEL_ENV)
The [environment](https://vercel.com/docs/environment-variables#environments) that the app is deployed and running on. The value can be either `production`, `preview`, or `development`.
.env
```


SANITY_STUDIO_VERCEL_ENV=production


```

###  [SANITY_STUDIO_VERCEL_TARGET_ENV](https://vercel.com/docs/environment-variables/framework-environment-variables#SANITY_STUDIO_VERCEL_TARGET_ENV)[](https://vercel.com/docs/environment-variables/framework-environment-variables#SANITY_STUDIO_VERCEL_TARGET_ENV)
The [system or custom environment](https://vercel.com/docs/environment-variables#environments) that the app is deployed and running on. The value can be either `production`, `preview`, `development`, or the name of a [custom environment](https://vercel.com/docs/deployments/environments#custom-environments).
.env
```


SANITY_STUDIO_VERCEL_TARGET_ENV=production


```

###  [SANITY_STUDIO_VERCEL_URL](https://vercel.com/docs/environment-variables/framework-environment-variables#SANITY_STUDIO_VERCEL_URL)[](https://vercel.com/docs/environment-variables/framework-environment-variables#SANITY_STUDIO_VERCEL_URL)
The domain name of the [generated deployment URL](https://vercel.com/docs/deployments/generated-urls). Example: `*.vercel.app`. The value **does not** include the protocol scheme `https://`.
.env
```


SANITY_STUDIO_VERCEL_URL=my-site.vercel.app


```

###  [SANITY_STUDIO_VERCEL_BRANCH_URL](https://vercel.com/docs/environment-variables/framework-environment-variables#SANITY_STUDIO_VERCEL_BRANCH_URL)[](https://vercel.com/docs/environment-variables/framework-environment-variables#SANITY_STUDIO_VERCEL_BRANCH_URL)
The domain name of the [generated Git branch URL](https://vercel.com/docs/deployments/generated-urls#url-with-git-branch). Example: `*-git-*.vercel.app`. The value **does not** include the protocol scheme `https://`.
.env
```


SANITY_STUDIO_VERCEL_BRANCH_URL=my-site-git-improve-about-page.vercel.app


```

###  [SANITY_STUDIO_VERCEL_PROJECT_PRODUCTION_URL](https://vercel.com/docs/environment-variables/framework-environment-variables#SANITY_STUDIO_VERCEL_PROJECT_PRODUCTION_URL)[](https://vercel.com/docs/environment-variables/framework-environment-variables#SANITY_STUDIO_VERCEL_PROJECT_PRODUCTION_URL)
A production domain name of the project. We select the shortest production custom domain, or vercel.app domain if no custom domain is available. Note, that this is always set, even in preview deployments. This is useful to reliably generate links that point to production such as OG-image URLs. The value **does not** include the protocol scheme `https://`.
.env
```


SANITY_STUDIO_VERCEL_PROJECT_PRODUCTION_URL=my-site.com


```

###  [SANITY_STUDIO_VERCEL_GIT_PROVIDER](https://vercel.com/docs/environment-variables/framework-environment-variables#SANITY_STUDIO_VERCEL_GIT_PROVIDER)[](https://vercel.com/docs/environment-variables/framework-environment-variables#SANITY_STUDIO_VERCEL_GIT_PROVIDER)
The Git Provider the deployment is triggered from.
.env
```


SANITY_STUDIO_VERCEL_GIT_PROVIDER=github


```

###  [SANITY_STUDIO_VERCEL_GIT_REPO_SLUG](https://vercel.com/docs/environment-variables/framework-environment-variables#SANITY_STUDIO_VERCEL_GIT_REPO_SLUG)[](https://vercel.com/docs/environment-variables/framework-environment-variables#SANITY_STUDIO_VERCEL_GIT_REPO_SLUG)
The origin repository the deployment is triggered from.
.env
```


SANITY_STUDIO_VERCEL_GIT_REPO_SLUG=my-site


```

###  [SANITY_STUDIO_VERCEL_GIT_REPO_OWNER](https://vercel.com/docs/environment-variables/framework-environment-variables#SANITY_STUDIO_VERCEL_GIT_REPO_OWNER)[](https://vercel.com/docs/environment-variables/framework-environment-variables#SANITY_STUDIO_VERCEL_GIT_REPO_OWNER)
The account that owns the repository the deployment is triggered from.
.env
```


SANITY_STUDIO_VERCEL_GIT_REPO_OWNER=acme


```

###  [SANITY_STUDIO_VERCEL_GIT_REPO_ID](https://vercel.com/docs/environment-variables/framework-environment-variables#SANITY_STUDIO_VERCEL_GIT_REPO_ID)[](https://vercel.com/docs/environment-variables/framework-environment-variables#SANITY_STUDIO_VERCEL_GIT_REPO_ID)
The ID of the repository the deployment is triggered from.
.env
```


SANITY_STUDIO_VERCEL_GIT_REPO_ID=117716146


```

###  [SANITY_STUDIO_VERCEL_GIT_COMMIT_REF](https://vercel.com/docs/environment-variables/framework-environment-variables#SANITY_STUDIO_VERCEL_GIT_COMMIT_REF)[](https://vercel.com/docs/environment-variables/framework-environment-variables#SANITY_STUDIO_VERCEL_GIT_COMMIT_REF)
The git branch of the commit the deployment was triggered by.
.env
```


SANITY_STUDIO_VERCEL_GIT_COMMIT_REF=improve-about-page


```

###  [SANITY_STUDIO_VERCEL_GIT_COMMIT_SHA](https://vercel.com/docs/environment-variables/framework-environment-variables#SANITY_STUDIO_VERCEL_GIT_COMMIT_SHA)[](https://vercel.com/docs/environment-variables/framework-environment-variables#SANITY_STUDIO_VERCEL_GIT_COMMIT_SHA)
The git
.env
```


SANITY_STUDIO_VERCEL_GIT_COMMIT_SHA=fa1eade47b73733d6312d5abfad33ce9e4068081


```

###  [SANITY_STUDIO_VERCEL_GIT_COMMIT_MESSAGE](https://vercel.com/docs/environment-variables/framework-environment-variables#SANITY_STUDIO_VERCEL_GIT_COMMIT_MESSAGE)[](https://vercel.com/docs/environment-variables/framework-environment-variables#SANITY_STUDIO_VERCEL_GIT_COMMIT_MESSAGE)
The message attached to the commit the deployment was triggered by. The message is truncated if it exceeds 2048 bytes.
.env
```


SANITY_STUDIO_VERCEL_GIT_COMMIT_MESSAGE=Update about page


```

###  [SANITY_STUDIO_VERCEL_GIT_COMMIT_AUTHOR_LOGIN](https://vercel.com/docs/environment-variables/framework-environment-variables#SANITY_STUDIO_VERCEL_GIT_COMMIT_AUTHOR_LOGIN)[](https://vercel.com/docs/environment-variables/framework-environment-variables#SANITY_STUDIO_VERCEL_GIT_COMMIT_AUTHOR_LOGIN)
The username attached to the author of the commit that the project was deployed by.
.env
```


SANITY_STUDIO_VERCEL_GIT_COMMIT_AUTHOR_LOGIN=johndoe


```

###  [SANITY_STUDIO_VERCEL_GIT_COMMIT_AUTHOR_NAME](https://vercel.com/docs/environment-variables/framework-environment-variables#SANITY_STUDIO_VERCEL_GIT_COMMIT_AUTHOR_NAME)[](https://vercel.com/docs/environment-variables/framework-environment-variables#SANITY_STUDIO_VERCEL_GIT_COMMIT_AUTHOR_NAME)
The name attached to the author of the commit that the project was deployed by.
.env
```


SANITY_STUDIO_VERCEL_GIT_COMMIT_AUTHOR_NAME=John Doe


```

###  [SANITY_STUDIO_VERCEL_GIT_PULL_REQUEST_ID](https://vercel.com/docs/environment-variables/framework-environment-variables#SANITY_STUDIO_VERCEL_GIT_PULL_REQUEST_ID)[](https://vercel.com/docs/environment-variables/framework-environment-variables#SANITY_STUDIO_VERCEL_GIT_PULL_REQUEST_ID)
The pull request id the deployment was triggered by. If a deployment is created on a branch before a pull request is made, this value will be an empty string.
.env
```


SANITY_STUDIO_VERCEL_GIT_PULL_REQUEST_ID=23


```

###  [SANITY_STUDIO_VERCEL_ENV](https://vercel.com/docs/environment-variables/framework-environment-variables#SANITY_STUDIO_VERCEL_ENV)[](https://vercel.com/docs/environment-variables/framework-environment-variables#SANITY_STUDIO_VERCEL_ENV)
The [environment](https://vercel.com/docs/environment-variables#environments) that the app is deployed and running on. The value can be either `production`, `preview`, or `development`.
.env
```


SANITY_STUDIO_VERCEL_ENV=production


```

###  [SANITY_STUDIO_VERCEL_TARGET_ENV](https://vercel.com/docs/environment-variables/framework-environment-variables#SANITY_STUDIO_VERCEL_TARGET_ENV)[](https://vercel.com/docs/environment-variables/framework-environment-variables#SANITY_STUDIO_VERCEL_TARGET_ENV)
The [system or custom environment](https://vercel.com/docs/environment-variables#environments) that the app is deployed and running on. The value can be either `production`, `preview`, `development`, or the name of a [custom environment](https://vercel.com/docs/deployments/environments#custom-environments).
.env
```


SANITY_STUDIO_VERCEL_TARGET_ENV=production


```

###  [SANITY_STUDIO_VERCEL_URL](https://vercel.com/docs/environment-variables/framework-environment-variables#SANITY_STUDIO_VERCEL_URL)[](https://vercel.com/docs/environment-variables/framework-environment-variables#SANITY_STUDIO_VERCEL_URL)
The domain name of the [generated deployment URL](https://vercel.com/docs/deployments/generated-urls). Example: `*.vercel.app`. The value **does not** include the protocol scheme `https://`.
.env
```


SANITY_STUDIO_VERCEL_URL=my-site.vercel.app


```

###  [SANITY_STUDIO_VERCEL_BRANCH_URL](https://vercel.com/docs/environment-variables/framework-environment-variables#SANITY_STUDIO_VERCEL_BRANCH_URL)[](https://vercel.com/docs/environment-variables/framework-environment-variables#SANITY_STUDIO_VERCEL_BRANCH_URL)
The domain name of the [generated Git branch URL](https://vercel.com/docs/deployments/generated-urls#url-with-git-branch). Example: `*-git-*.vercel.app`. The value **does not** include the protocol scheme `https://`.
.env
```


SANITY_STUDIO_VERCEL_BRANCH_URL=my-site-git-improve-about-page.vercel.app


```

###  [SANITY_STUDIO_VERCEL_PROJECT_PRODUCTION_URL](https://vercel.com/docs/environment-variables/framework-environment-variables#SANITY_STUDIO_VERCEL_PROJECT_PRODUCTION_URL)[](https://vercel.com/docs/environment-variables/framework-environment-variables#SANITY_STUDIO_VERCEL_PROJECT_PRODUCTION_URL)
A production domain name of the project. We select the shortest production custom domain, or vercel.app domain if no custom domain is available. Note, that this is always set, even in preview deployments. This is useful to reliably generate links that point to production such as OG-image URLs. The value **does not** include the protocol scheme `https://`.
.env
```


SANITY_STUDIO_VERCEL_PROJECT_PRODUCTION_URL=my-site.com


```

###  [SANITY_STUDIO_VERCEL_GIT_PROVIDER](https://vercel.com/docs/environment-variables/framework-environment-variables#SANITY_STUDIO_VERCEL_GIT_PROVIDER)[](https://vercel.com/docs/environment-variables/framework-environment-variables#SANITY_STUDIO_VERCEL_GIT_PROVIDER)
The Git Provider the deployment is triggered from.
.env
```


SANITY_STUDIO_VERCEL_GIT_PROVIDER=github


```

###  [SANITY_STUDIO_VERCEL_GIT_REPO_SLUG](https://vercel.com/docs/environment-variables/framework-environment-variables#SANITY_STUDIO_VERCEL_GIT_REPO_SLUG)[](https://vercel.com/docs/environment-variables/framework-environment-variables#SANITY_STUDIO_VERCEL_GIT_REPO_SLUG)
The origin repository the deployment is triggered from.
.env
```


SANITY_STUDIO_VERCEL_GIT_REPO_SLUG=my-site


```

###  [SANITY_STUDIO_VERCEL_GIT_REPO_OWNER](https://vercel.com/docs/environment-variables/framework-environment-variables#SANITY_STUDIO_VERCEL_GIT_REPO_OWNER)[](https://vercel.com/docs/environment-variables/framework-environment-variables#SANITY_STUDIO_VERCEL_GIT_REPO_OWNER)
The account that owns the repository the deployment is triggered from.
.env
```


SANITY_STUDIO_VERCEL_GIT_REPO_OWNER=acme


```

###  [SANITY_STUDIO_VERCEL_GIT_REPO_ID](https://vercel.com/docs/environment-variables/framework-environment-variables#SANITY_STUDIO_VERCEL_GIT_REPO_ID)[](https://vercel.com/docs/environment-variables/framework-environment-variables#SANITY_STUDIO_VERCEL_GIT_REPO_ID)
The ID of the repository the deployment is triggered from.
.env
```


SANITY_STUDIO_VERCEL_GIT_REPO_ID=117716146


```

###  [SANITY_STUDIO_VERCEL_GIT_COMMIT_REF](https://vercel.com/docs/environment-variables/framework-environment-variables#SANITY_STUDIO_VERCEL_GIT_COMMIT_REF)[](https://vercel.com/docs/environment-variables/framework-environment-variables#SANITY_STUDIO_VERCEL_GIT_COMMIT_REF)
The git branch of the commit the deployment was triggered by.
.env
```


SANITY_STUDIO_VERCEL_GIT_COMMIT_REF=improve-about-page


```

###  [SANITY_STUDIO_VERCEL_GIT_COMMIT_SHA](https://vercel.com/docs/environment-variables/framework-environment-variables#SANITY_STUDIO_VERCEL_GIT_COMMIT_SHA)[](https://vercel.com/docs/environment-variables/framework-environment-variables#SANITY_STUDIO_VERCEL_GIT_COMMIT_SHA)
The git
.env
```


SANITY_STUDIO_VERCEL_GIT_COMMIT_SHA=fa1eade47b73733d6312d5abfad33ce9e4068081


```

###  [SANITY_STUDIO_VERCEL_GIT_COMMIT_MESSAGE](https://vercel.com/docs/environment-variables/framework-environment-variables#SANITY_STUDIO_VERCEL_GIT_COMMIT_MESSAGE)[](https://vercel.com/docs/environment-variables/framework-environment-variables#SANITY_STUDIO_VERCEL_GIT_COMMIT_MESSAGE)
The message attached to the commit the deployment was triggered by. The message is truncated if it exceeds 2048 bytes.
.env
```


SANITY_STUDIO_VERCEL_GIT_COMMIT_MESSAGE=Update about page


```

###  [SANITY_STUDIO_VERCEL_GIT_COMMIT_AUTHOR_LOGIN](https://vercel.com/docs/environment-variables/framework-environment-variables#SANITY_STUDIO_VERCEL_GIT_COMMIT_AUTHOR_LOGIN)[](https://vercel.com/docs/environment-variables/framework-environment-variables#SANITY_STUDIO_VERCEL_GIT_COMMIT_AUTHOR_LOGIN)
The username attached to the author of the commit that the project was deployed by.
.env
```


SANITY_STUDIO_VERCEL_GIT_COMMIT_AUTHOR_LOGIN=johndoe


```

###  [SANITY_STUDIO_VERCEL_GIT_COMMIT_AUTHOR_NAME](https://vercel.com/docs/environment-variables/framework-environment-variables#SANITY_STUDIO_VERCEL_GIT_COMMIT_AUTHOR_NAME)[](https://vercel.com/docs/environment-variables/framework-environment-variables#SANITY_STUDIO_VERCEL_GIT_COMMIT_AUTHOR_NAME)
The name attached to the author of the commit that the project was deployed by.
.env
```


SANITY_STUDIO_VERCEL_GIT_COMMIT_AUTHOR_NAME=John Doe


```

###  [SANITY_STUDIO_VERCEL_GIT_PULL_REQUEST_ID](https://vercel.com/docs/environment-variables/framework-environment-variables#SANITY_STUDIO_VERCEL_GIT_PULL_REQUEST_ID)[](https://vercel.com/docs/environment-variables/framework-environment-variables#SANITY_STUDIO_VERCEL_GIT_PULL_REQUEST_ID)
The pull request id the deployment was triggered by. If a deployment is created on a branch before a pull request is made, this value will be an empty string.
.env
```


SANITY_STUDIO_VERCEL_GIT_PULL_REQUEST_ID=23


```

* * *
[ Previous Environment Variables ](https://vercel.com/docs/environment-variables)[ Next Manage Across Environments ](https://vercel.com/docs/environment-variables/manage-across-environments)
Was this helpful?
Send
[Environment Variables](https://vercel.com/docs/environment-variables)
Framework Environment Variables
# Sensitive environment variables
Last updated October 7, 2025
Sensitive environment variables are [environment variables](https://vercel.com/docs/environment-variables) whose values are non-readable once created. They help protect sensitive information stored in environment variables, such as API keys.
To mark an existing environment variable as sensitive, remove and re-add it with the Sensitive option enabled. Once you mark it as sensitive, Vercel stores the variable in an unreadable format. This is only possible for environment variables in the [production](https://vercel.com/docs/deployments/environments#production-environment) and [preview](https://vercel.com/docs/deployments/environments#preview-environment-pre-production) environments.
Both [project environment variables](https://vercel.com/docs/environment-variables) and [shared environment variables](https://vercel.com/docs/environment-variables/shared-environment-variables) can be marked as sensitive.
##  [Creating sensitive environment variables](https://vercel.com/docs/environment-variables/framework-environment-variables#creating-sensitive-environment-variables)[](https://vercel.com/docs/environment-variables/framework-environment-variables#creating-sensitive-environment-variables)
You can only create sensitive environment variables in the preview and production environments.
DashboardcURLSDK
Sensitive environment variables can be created at the project or team level:
  1. Go to the Vercel [dashboard](https://vercel.com/d?to=%2Fdashboard&title=Open+Dashboard) and select your team from the team switcher. Click on the Settings section in the sidebar and then select Environment Variables from the left navigation. To create sensitive environment variables at the project-level, select the project from your [dashboard](https://vercel.com/d?to=%2Fdashboard&title=Open+Dashboard) and then and click the Settings section in the sidebar.
  2. At the top of the form, toggle the Sensitive switch to Enabled. If the Development environment is selected, you will be unable to enable the switch.
  3. Fill in the details to create a new environment variable.
  4. In the environment variable table, sensitive environment variables are marked with a "Sensitive" tag:

![Sensitive environment variables labeled with a 'Sensitive' tag on the dashboard.](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fprojects%2Fenvironment-variables%2Flisted-sev.png&w=3840&q=75)![Sensitive environment variables labeled with a 'Sensitive' tag on the dashboard.](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fprojects%2Fenvironment-variables%2Flisted-sev-dark.png&w=3840&q=75)Sensitive environment variables labeled with a 'Sensitive' tag on the dashboard.
To create an Authorization Bearer token, see the [access token](https://vercel.com/docs/rest-api/reference/welcome#creating-an-access-token) section of the API documentation.
cURL
```
curl --request POST \
  --url https://api.vercel.com/v10/projects/<project-id-or-name>/env \
  --header "Authorization: Bearer $VERCEL_TOKEN" \
  --header "Content-Type: application/json" \
  --data '[
    {
      "key": "<env-key-1>",
      "value": "<env-value-1>",
      "type": "sensitive",
      "target": ["<target-environment>"],
      "gitBranch": "<git-branch>",
      "comment": "<comment>",
      "customEnvironmentIds": ["<custom-env-id>"]
    }
  ]'
```

To create an Authorization Bearer token, see the [access token](https://vercel.com/docs/rest-api/reference/welcome#creating-an-access-token) section of the API documentation.
createProjectEnv
```
import { Vercel } from '@vercel/sdk';

const vercel = new Vercel({
  bearerToken: '<YOUR_BEARER_TOKEN_HERE>',
});

async function run() {
  const result = await vercel.projects.createProjectEnv({
    idOrName: '<project-id-or-name>',
    requestBody: {
      key: '<env-key-1>',
      value: '<env-value-1>',
      type: 'sensitive',
      target: ['<target-environment>'],
      gitBranch: '<git-branch>',
      comment: '<comment>',
      customEnvironmentIds: ['<custom-env-id>'],
    },
  });

  // Handle the result
  console.log(result);
}

run();
```

##  [Edit sensitive environment variables](https://vercel.com/docs/environment-variables/framework-environment-variables#edit-sensitive-environment-variables)[](https://vercel.com/docs/environment-variables/framework-environment-variables#edit-sensitive-environment-variables)
You can edit the value and [environment](https://vercel.com/docs/environment-variables#environments) for a sensitive environment variable. You cannot edit the key of a sensitive environment variable.
  1. From your [dashboard](https://vercel.com/dashboard), go to the team or project's Settings section in the sidebar and select [Environment Variables](https://vercel.com/d?to=%2F%5Bteam%5D%2F%5Bproject%5D%2Fsettings%2Fenvironment-variables&title=Go+to+Environment+Variables) from the left navigation. Find your environment variable in the list.
  2. Click Edit from the three-dot menu in the environment variables list
  3. Provide a new value for the sensitive environment variable. The current value is hidden.
  4. Select the environment(s) for the sensitive environment variable.
  5. After making the change, click the Save button.


##  [Environment variables policy](https://vercel.com/docs/environment-variables/framework-environment-variables#environment-variables-policy)[](https://vercel.com/docs/environment-variables/framework-environment-variables#environment-variables-policy)
Users with the [owner](https://vercel.com/docs/rbac/access-roles#owner-role) role can set a team-wide environment variable policy for creating environment variables. Once enabled, all newly created environment variables in the [Production](https://vercel.com/docs/deployments/environments#production-environment) and/or [Preview](https://vercel.com/docs/deployments/environments#preview-environment-pre-production) environments will be sensitive environment variables.
  1. From the [dashboard](https://vercel.com/dashboard), ensure your team is selected in the team switcher and open Settings in the sidebar.
  2. From the left navigation, click Security & Privacy.
  3. From the Environment Variable Policies section, toggle the Enforce Sensitive Environment Variables switch to Enabled:

![Set environment variable policy from your team's Security settings.](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fprojects%2Fenvironment-variables%2Fenv-var-policies-2.png&w=1920&q=75)![Set environment variable policy from your team's Security settings.](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fprojects%2Fenvironment-variables%2Fenv-var-policies-dark-2.png&w=1920&q=75)Set environment variable policy from your team's Security settings.
* * *
[ Previous Environment Variables ](https://vercel.com/docs/environment-variables)[ Next Manage Across Environments ](https://vercel.com/docs/environment-variables/manage-across-environments)
Was this helpful?
Send
