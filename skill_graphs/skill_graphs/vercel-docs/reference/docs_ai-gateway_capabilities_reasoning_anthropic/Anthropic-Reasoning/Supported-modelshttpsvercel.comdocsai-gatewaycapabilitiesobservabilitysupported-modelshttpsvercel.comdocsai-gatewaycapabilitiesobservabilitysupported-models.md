##  [Supported models](https://vercel.com/docs/ai-gateway/capabilities/observability#supported-models)[](https://vercel.com/docs/ai-gateway/capabilities/observability#supported-models)
###  [Adaptive thinking (Claude 4.6)](https://vercel.com/docs/ai-gateway/capabilities/observability#adaptive-thinking-claude-4.6)[](https://vercel.com/docs/ai-gateway/capabilities/observability#adaptive-thinking-claude-4.6)
These models use `thinking: { type: 'adaptive' }`. Claude dynamically decides when and how much to think.
Model | Effort levels | Default
---|---|---
`anthropic/claude-opus-4.6` |  `low`, `medium`, `high`, `max` | `high`
`anthropic/claude-sonnet-4.6` |  `low`, `medium`, `high` | `high`
The `max` effort level is only available on Claude Opus 4.6. Requests using `max` on other models return an error.
###  [Extended thinking (Claude 4 and earlier)](https://vercel.com/docs/ai-gateway/capabilities/observability#extended-thinking-claude-4-and-earlier)[](https://vercel.com/docs/ai-gateway/capabilities/observability#extended-thinking-claude-4-and-earlier)
These models use `thinking: { type: 'enabled', budgetTokens: N }` to set a fixed token budget for thinking.
  * `anthropic/claude-opus-4.5`
  * `anthropic/claude-opus-4.1`
  * `anthropic/claude-opus-4`
  * `anthropic/claude-sonnet-4.5`
  * `anthropic/claude-sonnet-4`
  * `anthropic/claude-haiku-4.5`


###  [Adaptive vs. manual thinking](https://vercel.com/docs/ai-gateway/capabilities/observability#adaptive-vs.-manual-thinking)[](https://vercel.com/docs/ai-gateway/capabilities/observability#adaptive-vs.-manual-thinking)
  * Adaptive thinking (Claude 4.6): Use `thinking: { type: 'adaptive' }`. Claude decides when and how much to think. At `high` effort (default), Claude almost always thinks. At lower effort levels, it may skip thinking for simpler problems.
  * Manual thinking (Claude 4, Opus 4.5): Use `thinking: { type: 'enabled', budgetTokens: N }` to set a fixed token budget for thinking.


Manual thinking with `type: 'enabled'` and `budgetTokens` is deprecated on Claude 4.6 models. It still works but will be removed in a future release. Use adaptive thinking instead.
For more details, see the
