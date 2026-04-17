##  [Persistent actions](https://vercel.com/docs/vercel-firewall/vercel-waf/custom-rules#persistent-actions)[](https://vercel.com/docs/vercel-firewall/vercel-waf/custom-rules#persistent-actions)
Persistent Actions are available on [Enterprise](https://vercel.com/docs/plans/enterprise) and [Pro](https://vercel.com/docs/plans/pro) plans
When a custom rule blocks a client's request, future requests that do not match the rule's condition from the same client, are allowed through. If you want to deny all requests from the client whose first request was blocked, you will need to identify who this client is through [traffic monitoring](https://vercel.com/docs/security/vercel-waf#traffic-monitoring) and create an IP Address rule for that purpose.
With persistent actions, you can automatically block potential bad actors by adding a time-based block to the Challenge or Deny action of your custom rule. When you do so, any client whose request is challenged or denied, will be blocked for a period of time that you specify.
Notes about this time-based block:
  * It is applied to the IP address of the client that originally triggered the rule to match.
  * It happens before the firewall processes the request, so that none of the requests blocked by persistent actions count towards your [CDN](https://vercel.com/docs/cdn) and traffic usage.


###  [Enable persistent actions](https://vercel.com/docs/vercel-firewall/vercel-waf/custom-rules#enable-persistent-actions)[](https://vercel.com/docs/vercel-firewall/vercel-waf/custom-rules#enable-persistent-actions)
You can enable persistent actions for any challenge, deny or rate limit action when you create or edit a custom rule. From your project's page in the dashboard:
  1. Open [Firewall](https://vercel.com/d?to=%2F%5Bteam%5D%2F%5Bproject%5D%2Ffirewall&title=Go+to+Firewall) in the sidebar followed by Configure on the top right of the Firewall overview page.
  2. Select a Custom Rule you would like to edit from the list or select + New Rule and follow the [steps](https://vercel.com/docs/vercel-firewall/vercel-waf/custom-rules#get-started) for configuring a rule.


When you select challenge, deny or rate limit for the [action](https://vercel.com/docs/vercel-firewall/vercel-waf/rule-configuration#actions) dropdown (Then) of any condition, you will see an additional dropdown for timeframe (for) that defaults to 1 minute. You have the following options:
  1. Select a time value from the available options
  2. Remove the timeframe (If you don't want to enable persistent actions)


Once you're happy with the changes:
  1. Select Save Rule to apply it
  2. Apply the changes with the Review Changes button
