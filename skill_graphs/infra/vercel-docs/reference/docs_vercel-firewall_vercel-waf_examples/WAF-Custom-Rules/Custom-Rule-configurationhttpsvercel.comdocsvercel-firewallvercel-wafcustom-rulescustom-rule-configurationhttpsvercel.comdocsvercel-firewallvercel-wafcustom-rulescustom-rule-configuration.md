##  [Custom Rule configuration](https://vercel.com/docs/vercel-firewall/vercel-waf/custom-rules#custom-rule-configuration)[](https://vercel.com/docs/vercel-firewall/vercel-waf/custom-rules#custom-rule-configuration)
You can create multiple Custom Rules for the same project. Each rule can perform the following actions according to one or more logical condition(s) that you set based on the value of specific [parameters](https://vercel.com/docs/security/vercel-waf/rule-configuration) in the incoming request:
  * [log](https://vercel.com/docs/vercel-firewall/firewall-concepts#log)
  * [deny](https://vercel.com/docs/vercel-firewall/firewall-concepts#deny)
  * [challenge](https://vercel.com/docs/vercel-firewall/firewall-concepts#challenge)
  * [bypass](https://vercel.com/docs/vercel-firewall/firewall-concepts#bypass)
  * redirect


You can save, delete, or disable a rule at any time and these actions have immediate effect. You also have the ability to re-order the precedence of each custom rule.
