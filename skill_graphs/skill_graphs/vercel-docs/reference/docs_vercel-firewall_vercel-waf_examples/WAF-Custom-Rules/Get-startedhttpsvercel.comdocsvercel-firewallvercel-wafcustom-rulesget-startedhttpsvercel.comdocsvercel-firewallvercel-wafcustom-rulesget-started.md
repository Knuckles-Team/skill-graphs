##  [Get started](https://vercel.com/docs/vercel-firewall/vercel-waf/custom-rules#get-started)[](https://vercel.com/docs/vercel-firewall/vercel-waf/custom-rules#get-started)
Learn how to create, test, and apply a Custom Rule.
  1. From your [dashboard](https://vercel.com/dashboard), select the project you'd like to configure, then open [Firewall](https://vercel.com/d?to=%2F%5Bteam%5D%2F%5Bproject%5D%2Ffirewall&title=Go+to+Firewall) in the sidebar
  2. Select ⋯ > Configure on the top right of the Firewall overview page
  3. Select Add New... > Rule to start creating a new rule
  4. Type a name to help you identify the purpose of this rule for future reference
  5. In the Configure section, add as many If conditions as needed. For each condition you add, choose how you will combine it with the previous condition using the AND (Both conditions need to be met) or the OR operator (One of the conditions need to be met).
![](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fsecurity%2Fvercel-waf-custom-rule-configure-and-or-light.png&w=2048&q=75)![](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fsecurity%2Fvercel-waf-custom-rule-configure-and-or-dark.png&w=2048&q=75)
  6. Select Log for the Then action
     * For Rate Limit, review [WAF Rate Limiting](https://vercel.com/docs/security/vercel-waf/rate-limiting#get-started)
  7. Select Save Rule to apply it
  8. Apply the changes:
     * When you make any change, you will see a Review Changes button appear or update on the top right with the number of changes requested
     * Select Review Changes and review the changes to be applied
     * Select Publish to apply the changes to your production deployment
  9. Go to the Firewall overview page, select your Custom Rule from the traffic grouping drop-down and select the parameter(s) related to the condition(s) of your Custom Rule to observe the traffic:
![](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fsecurity%2Fwaf-overview-custom-rule-light.png&w=3840&q=75)![](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fsecurity%2Fwaf-overview-custom-rule-dark.png&w=3840&q=75)
  10. If you are satisfied with the traffic behavior, select Configure
  11. Select the Custom Rule that you created
  12. Update the Then action to Challenge, Deny or Bypass as needed
  13. Select Save Rule to apply it
  14. Apply the changes with the Review Changes button


Review [Common Examples](https://vercel.com/docs/security/vercel-waf/examples) for the application of specific rules in common situations.
