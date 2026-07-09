##  [Why use Edge Config instead of alternatives?](https://vercel.com/docs/edge-config#why-use-edge-config-instead-of-alternatives)[](https://vercel.com/docs/edge-config#why-use-edge-config-instead-of-alternatives)
There are alternative solutions to Edge Config for handling A/B testing, feature flags, and IP blocking. The following table lays out how those solutions compare to Edge Config:
Edge Config vs alternatives | Read latency | Write latency | Redeployment required | Added risk of downtime
---|---|---|---|---
Edge Config |  Ultra-low |  Varies |  No |  No
Remote JSON files | Varies  | Varies | No  | Yes
Embedded JSON files | Lowest | Highest  | Yes  | No
Environment Variables | Lowest | Highest  | Yes  | No
