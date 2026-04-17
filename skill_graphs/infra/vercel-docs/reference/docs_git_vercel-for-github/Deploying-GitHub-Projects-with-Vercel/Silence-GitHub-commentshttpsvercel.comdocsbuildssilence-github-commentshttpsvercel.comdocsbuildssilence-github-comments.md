##  [Silence GitHub comments](https://vercel.com/docs/builds#silence-github-comments)[](https://vercel.com/docs/builds#silence-github-comments)
By default, comments from the Vercel GitHub bot will appear on your pull requests and commits. You can silence these comments in your project's settings:
  1. From the Vercel [dashboard](https://vercel.com/dashboard), select your project
  2. From the Settings tab, select Git
  3. Under Connected Git Repository, toggle the switches to your preference


If you had previously used the, now deprecated, [`github.silent`](https://vercel.com/docs/project-configuration/git-configuration#github.silent) property in your project configuration, we'll automatically adjust the setting for you.
It is currently not possible to prevent comments for specific branches.
