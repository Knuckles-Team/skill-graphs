##  [Community runtimes](https://vercel.com/docs/functions/runtimes#community-runtimes)[](https://vercel.com/docs/functions/runtimes#community-runtimes)
If you would like to use a language that Vercel does not support by default, you can use a community runtime by setting the [`functions` property](https://vercel.com/docs/project-configuration#functions) in `vercel.json`. For more information on configuring other runtimes, see [Configuring your function runtime](https://vercel.com/docs/functions/configuring-functions/runtime#other-runtimes).
The following community runtimes are recommended by Vercel:
Runtime | Runtime Module | Docs
---|---|---
Bash | `vercel-bash` |
Deno | `vercel-deno` |
PHP | `vercel-php` |
You can create a community runtime by using the [Build Output API](https://vercel.com/docs/build-output-api/v3).
