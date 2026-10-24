##  [When to use this rule type](https://vercel.com/docs/getting-started-with-vercel#when-to-use-this-rule-type)[](https://vercel.com/docs/getting-started-with-vercel#when-to-use-this-rule-type)
  * Performance
    * You want to prevent importing packages that are known to increase the size of your client side code
    * You want to prevent using a package that is known to perform poorly in specific environments
  * Security
    * You want to disallow client-side code from depending on a file that exposes secrets
  * Error prevention
    * You want to prevent errors by disallowing server-side code from importing a module where some methods require browser APIs
