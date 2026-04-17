##  [Parameters](https://vercel.com/docs/ai-gateway/capabilities/observability#parameters)[](https://vercel.com/docs/ai-gateway/capabilities/observability#parameters)
###  [Adaptive thinking (Claude 4.6)](https://vercel.com/docs/ai-gateway/capabilities/observability#adaptive-thinking-claude-4.6)[](https://vercel.com/docs/ai-gateway/capabilities/observability#adaptive-thinking-claude-4.6)
Parameter | Type | Description
---|---|---
`type` | string | Set to `'adaptive'` for Claude 4.6 models
###  [Manual thinking (Claude 4, Opus 4.5)](https://vercel.com/docs/ai-gateway/capabilities/observability#manual-thinking-claude-4-opus-4.5)[](https://vercel.com/docs/ai-gateway/capabilities/observability#manual-thinking-claude-4-opus-4.5)
Parameter | Type | Description
---|---|---
`type` | string | Set to `'enabled'` to enable extended thinking
`budgetTokens` | number | Maximum number of tokens to allocate for thinking
###  [Effort levels](https://vercel.com/docs/ai-gateway/capabilities/observability#effort-levels)[](https://vercel.com/docs/ai-gateway/capabilities/observability#effort-levels)
Level | Description
---|---
`max` | Absolute maximum capability. Opus 4.6 only
`high` | High capability (default). Complex reasoning, difficult coding, agentic tasks
`medium` | Balanced speed, cost, and performance. Recommended default for Sonnet 4.6
`low` | Most efficient. Best for simpler tasks and latency-sensitive workloads
