##  [NetworkPolicy class](https://vercel.com/docs/vercel-sandbox/sdk-reference#networkpolicy-class)[](https://vercel.com/docs/vercel-sandbox/sdk-reference#networkpolicy-class)
`NetworkPolicy` instances represent the firewall setup of the sandbox. To learn more, see [network firewall](https://vercel.com/docs/vercel-sandbox/concepts/firewall).
###  [Base modes](https://vercel.com/docs/vercel-sandbox/sdk-reference#base-modes)[](https://vercel.com/docs/vercel-sandbox/sdk-reference#base-modes)
####  [`allow-all`](https://vercel.com/docs/vercel-sandbox/sdk-reference#allow-all)[](https://vercel.com/docs/vercel-sandbox/sdk-reference#allow-all)
The `allow-all` mode is the default applicable policy for sandboxes. It allows all egress traffic, to the Internet and secure-compute environments.
####  [`deny-all`](https://vercel.com/docs/vercel-sandbox/sdk-reference#deny-all)[](https://vercel.com/docs/vercel-sandbox/sdk-reference#deny-all)
The `deny-all` mode can be set to restrict sandbox network access. It blocks all egress traffic, including DNS resolution.
###  [User-defined rules](https://vercel.com/docs/vercel-sandbox/sdk-reference#user-defined-rules)[](https://vercel.com/docs/vercel-sandbox/sdk-reference#user-defined-rules)
####  [`allow`](https://vercel.com/docs/vercel-sandbox/sdk-reference#allow)[](https://vercel.com/docs/vercel-sandbox/sdk-reference#allow)
The `allow` property allows the user to provide a list of website or API domains to allow access to. Traffic identification is based on SNI (server-name indicator), hence only TLS traffic is currently supported. Matching is based on:
  * if the domain does not contain any wildcard `*` segment, only exact matches are accepted.
  * if the domain includes a wildcard `*` as a middle segment (e.g. `www.*.com`), it only matches this one segment.
  * if the domain starts with a wildcard `*` (e.g. `*.google.com`), any subdomain is matched. It will not match the parent domain (e.g. `google.com` here).


Encryption is not intercepted if no transformation rules are defined, allowing end-to-end data confidentiality.
###### `transform`
The `allow` property can be set as an object providing the websites to allow traffic to, with optional additional transformation rules. When such rules are defined, encryption is intercepted to allow request alteration.
Currently supported transformation is header injection, overriding the provided header with the value set, implementing [credential brokering](https://vercel.com/docs/vercel-sandbox/concepts/firewall#credentials-brokering).
Only Pro and Enterprise users can define transformations.
TypeScript
```
// Allow traffic only to the provided websites.
{
  allow: ["ai-gateway.vercel.sh", "google.com"]
}

// Allow traffic to all websites and add transformations to specific ones.
{
  allow: {
    "ai-gateway.vercel.sh": [{
      transform: [{
        headers: {
          "x-api-key": "secret-key"
        }
      }]
    }],
    "*.openai.com": [{
      transform: [{
        headers: {
          "x-api-key": "other-secret-key"
        }
      }]
    }],
    // Optionally allow traffic to all other domains.
    "*": []
  }
}
```

####  [`subnets.allow`](https://vercel.com/docs/vercel-sandbox/sdk-reference#subnets.allow)[](https://vercel.com/docs/vercel-sandbox/sdk-reference#subnets.allow)
`subnets.allow` allows the user to provide a list of address ranges to allow traffic to. If used in combination with `allow`, traffic to those addresses will also bypass domain matching.
It enables users to enable traffic not using TLS, or towards systems where domains cannot be used. Beware of virtual hosting providers which can host many websites behind a given address.
####  [`subnets.deny`](https://vercel.com/docs/vercel-sandbox/sdk-reference#subnets.deny)[](https://vercel.com/docs/vercel-sandbox/sdk-reference#subnets.deny)
`subnets.deny` allows the user to provide a list of address ranges to deny traffic to. Those ranges will always take precedence over `subnets.allow` and domain-based `allow` entries.
It allows the user to deny access to part of their network for instance while allowing access to the Internet in general.
