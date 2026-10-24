##  [Provider behavior](https://vercel.com/docs/ai-gateway/models-and-providers/automatic-caching#provider-behavior)[](https://vercel.com/docs/ai-gateway/models-and-providers/automatic-caching#provider-behavior)
Provider | Caching type |  `caching: 'auto'` effect
---|---|---
OpenAI | Implicit | No change needed. Caching happens automatically.
Google | Implicit | No change needed. Caching happens automatically.
DeepSeek | Implicit | No change needed. Caching happens automatically.
Anthropic | Explicit | Adds `cache_control` breakpoint to static content
Anthropic (via Vertex) | Explicit | Adds `cache_control` breakpoint to static content
MiniMax | Explicit | Adds cache markers to static content
Bedrock | Not supported | No effect
* * *
[ Previous Provider Timeouts ](https://vercel.com/docs/ai-gateway/models-and-providers/provider-timeouts)[ Next Provider Filtering & Ordering ](https://vercel.com/docs/ai-gateway/models-and-providers/provider-filtering-and-ordering)
Was this helpful?
Send
On this page
  * [How it works](https://vercel.com/docs/ai-gateway/models-and-providers/automatic-caching#how-it-works)
  * [Examples](https://vercel.com/docs/ai-gateway/models-and-providers/automatic-caching#examples)
  * [Manual caching](https://vercel.com/docs/ai-gateway/models-and-providers/automatic-caching#manual-caching)
  * [Provider behavior](https://vercel.com/docs/ai-gateway/models-and-providers/automatic-caching#provider-behavior)


Copy as MarkdownGive feedbackAsk AI about this page
