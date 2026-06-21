##  [Get started](https://vercel.com/docs/vercel-firewall/vercel-waf/rate-limiting#get-started)[](https://vercel.com/docs/vercel-firewall/vercel-waf/rate-limiting#get-started)
  1. From your [dashboard](https://vercel.com/dashboard/), select the project that you'd like to configure rate limiting for. Then open Firewall in the sidebar
  2. Select Configure on the top right of the Firewall overview page. Then, select + New Rule
  3. Complete the fields for the rule as follows
    1. Type a name to help you identify the purpose of this rule for future reference
    2. In the Configure section, add as many If conditions as needed:
All conditions must be true for the action to happen.
![](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fsecurity%2Fvercel-waf-custom-rule-configure-light.png&w=1920&q=75)![](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fsecurity%2Fvercel-waf-custom-rule-configure-dark.png&w=1920&q=75)
    3. For the Then action, select Rate Limit
       * If this is the first time you are creating a rate limit rule, you will need to review the Rate Limiting Pricing dialog and select Continue
    4. Select Fixed Window (all plans) or Token Bucket (Enterprise) for the limiting strategy

![](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fsecurity%2Fvercel-waf-rate-limit-light.png&w=2048&q=75)![](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fsecurity%2Fvercel-waf-rate-limit-dark.png&w=2048&q=75)
  1. Update the Time Window field as needed (defaults to 60s) and the Request Limit field as needed (defaults to 100 requests)
     * The Request Limit defines the maximum number of requests allowed in the selected time window from a common source
  2. Select the key(s) from the request's source that you want to match against
  3. For the Then action, you can leave the Default (429) action or choose between Log, Deny and Challenge
The Log action will not perform any blocks. You can use it to first monitor the effect before applying a rate limit or block action.
  4. Select Save Rule
  5. Apply the changes:
     * When you make any change, you will see a Review Changes button appear or update on the top right with the number of changes requested
     * Select Review Changes and review the changes to be applied
     * Select Publish to apply the changes to your production deployment
  6. Go to the Firewall overview page, select your Custom Rule from the traffic grouping drop-down and select the parameter(s) related to the condition(s) of your Custom Rule to observe the traffic and check whether it's working as expected:

![](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fsecurity%2Fwaf-overview-custom-rule-light.png&w=3840&q=75)![](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fsecurity%2Fwaf-overview-custom-rule-dark.png&w=3840&q=75)
