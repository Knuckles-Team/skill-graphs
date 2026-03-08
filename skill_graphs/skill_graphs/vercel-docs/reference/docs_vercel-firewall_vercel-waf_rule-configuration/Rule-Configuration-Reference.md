# Rule Configuration Reference
Last updated April 21, 2025
For each custom rule that you create, you can configure one or more conditions with [parameters](https://vercel.com/docs/vercel-firewall/vercel-waf/rule-configuration#parameters) from the incoming traffic that you compare with specific values using [operators](https://vercel.com/docs/vercel-firewall/vercel-waf/rule-configuration#operators). For each new condition, you can choose how you combine it with the previous condition using the AND (Both conditions need to be met) or the OR operator (One of the conditions need to be met).
You also specify an [action](https://vercel.com/docs/vercel-firewall/vercel-waf/rule-configuration#actions) executed when all the conditions are met.
