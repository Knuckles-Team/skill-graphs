# Exclude Files from Deployments with .vercelignore
Last updated March 12, 2025
The `.vercelignore` file can be used to specify files and directories that should be excluded from the deployment process when using Vercel. This file works similarly to a `.gitignore` file, but it is specific to Vercel.
The `.vercelignore` file should be placed in the root directory of your project and should contain a list of files and directories, one per line, that should be excluded from deployment. For example, to prevent an `/image` directory and `/private.html` file within a project from being uploaded to Vercel, you would add them to the `.vercelignore` file like this:
.vercelignore
```
image
private.html
```
