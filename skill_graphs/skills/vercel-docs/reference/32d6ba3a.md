##  [Supported models](https://vercel.com/docs/ai-gateway/capabilities/usage#supported-models)[](https://vercel.com/docs/ai-gateway/capabilities/usage#supported-models)
  * `google/gemini-3.1-pro-preview`
  * `google/gemini-3.1-flash-lite-preview`
  * `google/gemini-3-flash`
  * `google/gemini-2.5-pro`
  * `google/gemini-2.5-flash`
  * `google/gemini-2.5-flash-lite`


###  [Thinking levels (Gemini 3 and 3.1)](https://vercel.com/docs/ai-gateway/capabilities/usage#thinking-levels-gemini-3-and-3.1)[](https://vercel.com/docs/ai-gateway/capabilities/usage#thinking-levels-gemini-3-and-3.1)
The `thinkingLevel` parameter controls reasoning behavior. Not all levels are available on every model:
Thinking level | Gemini 3.1 Pro | Gemini 3.1 Flash-Lite | Gemini 3 Flash | Description
---|---|---|---|---
`minimal` | Not supported | Default | Supported | Matches "no thinking" for most queries. The model may still think minimally for complex coding tasks. Best for latency-sensitive workloads.
`low` | Supported | Supported | Supported | Minimizes latency and cost. Best for simple instruction following and chat.
`medium` | Supported | Supported | Supported | Balanced thinking for most tasks.
`high` | Default | Supported | Default | Maximizes reasoning depth. The model may take significantly longer to reach a first output token.
###  [Thinking budgets (Gemini 2.5)](https://vercel.com/docs/ai-gateway/capabilities/usage#thinking-budgets-gemini-2.5)[](https://vercel.com/docs/ai-gateway/capabilities/usage#thinking-budgets-gemini-2.5)
The `thinkingBudget` parameter sets a specific number of thinking tokens. Set `thinkingBudget` to `0` to disable thinking, or `-1` to enable dynamic thinking (the model adjusts based on request complexity).
Use `thinkingLevel` with Gemini 3 and 3.1 models. While `thinkingBudget` is accepted for backwards compatibility, using it with Gemini 3 models may result in unexpected performance.
Model | Default | Range | Disable thinking | Dynamic thinking
---|---|---|---|---
Gemini 2.5 Pro | Dynamic | 128–32,768 | Not supported |  `thinkingBudget: -1` (default)
Gemini 2.5 Flash | Dynamic | 0–24,576 | `thinkingBudget: 0` |  `thinkingBudget: -1` (default)
Gemini 2.5 Flash Lite | Off | 512–24,576 | `thinkingBudget: 0` | `thinkingBudget: -1`
