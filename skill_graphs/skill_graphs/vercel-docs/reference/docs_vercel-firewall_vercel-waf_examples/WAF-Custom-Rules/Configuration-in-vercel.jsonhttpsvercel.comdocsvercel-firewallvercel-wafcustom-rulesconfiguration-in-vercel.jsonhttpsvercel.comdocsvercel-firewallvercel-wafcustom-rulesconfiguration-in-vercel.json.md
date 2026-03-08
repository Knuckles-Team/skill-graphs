##  [Configuration in vercel.json](https://vercel.com/docs/vercel-firewall/vercel-waf/custom-rules#configuration-in-vercel.json)[](https://vercel.com/docs/vercel-firewall/vercel-waf/custom-rules#configuration-in-vercel.json)
You can configure custom WAF rules directly in your `vercel.json` file using the `routes` property. This allows you to define firewall rules as part of your deployment configuration.
###  [Supported actions](https://vercel.com/docs/vercel-firewall/vercel-waf/custom-rules#supported-actions)[](https://vercel.com/docs/vercel-firewall/vercel-waf/custom-rules#supported-actions)
When configuring WAF rules in `vercel.json`, you can use the following actions:
  * challenge: Challenge the request with a security check
  * deny: Block the request entirely


This is a subset of the actions available in the dashboard - `log`, `bypass`, and `redirect` actions are not supported in `vercel.json` configuration.
###  [Example configuration](https://vercel.com/docs/vercel-firewall/vercel-waf/custom-rules#example-configuration)[](https://vercel.com/docs/vercel-firewall/vercel-waf/custom-rules#example-configuration)
The following example shows how to deny requests that contain a specific header:
vercel.json
```
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "routes": [
    {
      "src": "/(.*)",
      "has": [
        {
          "type": "header",
          "key": "x-react-router-prerender-data"
        }
      ],
      "mitigate": {
        "action": "deny"
      }
    }
  ]
}
```

In this example:
  * The route matches all paths (`/(.*)`)
  * The `has` condition checks for the presence of a specific header
  * The `mitigate` property specifies the action to take (deny the request)


###  [Route configuration](https://vercel.com/docs/vercel-firewall/vercel-waf/custom-rules#route-configuration)[](https://vercel.com/docs/vercel-firewall/vercel-waf/custom-rules#route-configuration)
For complete documentation on route configuration options, including `has`, `missing`, and other conditional matching properties, see the [routes documentation](https://vercel.com/docs/project-configuration#routes).
* * *
[ Previous Web Application Firewall ](https://vercel.com/docs/vercel-firewall/vercel-waf)[ Next Rate Limiting ](https://vercel.com/docs/vercel-firewall/vercel-waf/rate-limiting)
Was this helpful?
Send
On this page
  * [Access roles](https://vercel.com/docs/vercel-firewall/vercel-waf/custom-rules#access-roles)
  * [Custom Rule configuration](https://vercel.com/docs/vercel-firewall/vercel-waf/custom-rules#custom-rule-configuration)
  * [Custom Rule execution](https://vercel.com/docs/vercel-firewall/vercel-waf/custom-rules#custom-rule-execution)
  * [Persistent actions](https://vercel.com/docs/vercel-firewall/vercel-waf/custom-rules#persistent-actions)
  * [Enable persistent actions](https://vercel.com/docs/vercel-firewall/vercel-waf/custom-rules#enable-persistent-actions)
  * [Best practices for applying rules](https://vercel.com/docs/vercel-firewall/vercel-waf/custom-rules#best-practices-for-applying-rules)
  * [Get started](https://vercel.com/docs/vercel-firewall/vercel-waf/custom-rules#get-started)
  * [Configuration in vercel.json](https://vercel.com/docs/vercel-firewall/vercel-waf/custom-rules#configuration-in-vercel.json)
  * [Supported actions](https://vercel.com/docs/vercel-firewall/vercel-waf/custom-rules#supported-actions)
  * [Example configuration](https://vercel.com/docs/vercel-firewall/vercel-waf/custom-rules#example-configuration)
  * [Route configuration](https://vercel.com/docs/vercel-firewall/vercel-waf/custom-rules#route-configuration)


Copy as MarkdownGive feedbackAsk AI about this page
[Firewall](https://vercel.com/docs/vercel-firewall)
[Web Application Firewall](https://vercel.com/docs/vercel-firewall/vercel-waf)
Custom Rules
