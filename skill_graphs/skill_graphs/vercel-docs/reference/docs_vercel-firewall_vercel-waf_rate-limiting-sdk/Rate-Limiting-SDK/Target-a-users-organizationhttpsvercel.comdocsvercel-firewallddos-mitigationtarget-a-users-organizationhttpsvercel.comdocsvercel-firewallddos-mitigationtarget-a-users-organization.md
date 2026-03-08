##  [Target a user's organization](https://vercel.com/docs/vercel-firewall/ddos-mitigation#target-a-user's-organization)[](https://vercel.com/docs/vercel-firewall/ddos-mitigation#target-a-user's-organization)
For example, you can include an additional filter for a request header and check whether this header matches a key from the user's authentication, to apply the rate limit. This filter is not possible in the custom rule dashboard.
###  [Update the custom rule filters](https://vercel.com/docs/vercel-firewall/ddos-mitigation#update-the-custom-rule-filters)[](https://vercel.com/docs/vercel-firewall/ddos-mitigation#update-the-custom-rule-filters)
Edit the custom rule in the dashboard and add an If condition with the following values, and click Save Rule:
  * Filter dropdown: #Request Header
  * Value: `xrr-internal-header`
  * Operator: Equals
  * Match value: `internal`


###  [Use the `rateLimitKey` in code](https://vercel.com/docs/vercel-firewall/ddos-mitigation#use-the-ratelimitkey-in-code)[](https://vercel.com/docs/vercel-firewall/ddos-mitigation#use-the-ratelimitkey-in-code)
Use the following code to apply the rate limit only to users of the organization.
rate-limit.ts
```
import { checkRateLimit } from '@vercel/firewall';
import { authenticateUser } from './auth';

export async function POST(request: Request) {
  const auth = await authenticateUser(request);
  const { rateLimited } = await checkRateLimit('update-object', {
    request,
    rateLimitKey: auth.orgId,
  });
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
}
```

* * *
[ Previous Firewall Concepts ](https://vercel.com/docs/vercel-firewall/firewall-concepts)[ Next Attack Challenge Mode ](https://vercel.com/docs/vercel-firewall/attack-challenge-mode)
Was this helpful?
Send
On this page
  * [Using @vercel/firewall](https://vercel.com/docs/vercel-firewall/ddos-mitigation#using-@vercel/firewall)
  * [Create a @vercel/firewall rule](https://vercel.com/docs/vercel-firewall/ddos-mitigation#create-a-@vercel/firewall-rule)
  * [Configure rate limiting in code](https://vercel.com/docs/vercel-firewall/ddos-mitigation#configure-rate-limiting-in-code)
  * [Test in a preview deployment](https://vercel.com/docs/vercel-firewall/ddos-mitigation#test-in-a-preview-deployment)
  * [Target a user's organization](https://vercel.com/docs/vercel-firewall/ddos-mitigation#target-a-user's-organization)
  * [Update the custom rule filters](https://vercel.com/docs/vercel-firewall/ddos-mitigation#update-the-custom-rule-filters)
  * [Use the rateLimitKey in code](https://vercel.com/docs/vercel-firewall/ddos-mitigation#use-the-ratelimitkey-in-code)


Copy as MarkdownGive feedbackAsk AI about this page
