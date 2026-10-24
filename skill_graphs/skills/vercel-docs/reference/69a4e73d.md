##  [Using `@vercel/firewall`](https://vercel.com/docs/vercel-firewall/ddos-mitigation#using-@vercel/firewall)[](https://vercel.com/docs/vercel-firewall/ddos-mitigation#using-@vercel/firewall)
  1. ###  [Create a `@vercel/firewall` rule](https://vercel.com/docs/vercel-firewall/ddos-mitigation#create-a-@vercel/firewall-rule)[](https://vercel.com/docs/vercel-firewall/ddos-mitigation#create-a-@vercel/firewall-rule)
    1. From your [dashboard](https://vercel.com/dashboard/), select the project that you'd like to configure rate limiting for. Then open Firewall in the sidebar
    2. Select Configure on the top right of the Firewall overview page. Then, select + New Rule
    3. Complete the fields for the rule as follows
      1. Type a name such as "Firewall api rule"
      2. In the Configure section, for the first If condition, select `@vercel/firewall`
      3. Use `update-object` as the Rate limit ID
      4. Use the default values for Rate Limit and Then
    4. Select Save Rule
    5. Apply the changes:
       * When you make any change, you will see a Review Changes button appear or update on the top right with the number of changes requested
       * Select Review Changes and review the changes to be applied
       * Select Publish to apply the changes to your production deployment
  2. ###  [Configure rate limiting in code](https://vercel.com/docs/vercel-firewall/ddos-mitigation#configure-rate-limiting-in-code)[](https://vercel.com/docs/vercel-firewall/ddos-mitigation#configure-rate-limiting-in-code)
You can now use the Rate limit ID `update-object` set up above with `@vercel/firewall` to rate limit any request based on your own conditions. In the example below, you rate limit a request based on its IP.
rate-limit.ts
```
import { checkRateLimit } from '@vercel/firewall';

export async function POST(request: Request) {
  const { rateLimited } = await checkRateLimit('update-object', { request });
  if (rateLimited) {
    return new Response(
      JSON.stringify({
        error: 'Rate limit exceeded',
      }),
      {
        status: 429,
        headers: {
          'Content-Type': 'application/json',
        },
      },
    );
  }
  // Otherwise, continue with other tasks
}
```

  3. ###  [Test in a preview deployment](https://vercel.com/docs/vercel-firewall/ddos-mitigation#test-in-a-preview-deployment)[](https://vercel.com/docs/vercel-firewall/ddos-mitigation#test-in-a-preview-deployment)
For your code to run when deployed in a preview deployment, you need to:
     * Enable [Protection Bypass for Automation](https://vercel.com/docs/security/deployment-protection/methods-to-bypass-deployment-protection/protection-bypass-automation) in your project
     * Ensure [System Environment Variables are automatically exposed](https://vercel.com/docs/environment-variables/system-environment-variables#system-environment-variables)
