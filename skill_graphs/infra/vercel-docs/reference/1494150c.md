# Google and Vertex Reasoning
Last updated March 8, 2026
The Gemini 2.5, 3, and 3.1 series models use an internal "thinking process" that improves their reasoning and multi-step planning abilities, making them effective for complex tasks like coding, advanced mathematics, and data analysis.
These models are available through both Google AI and Google Vertex AI providers. The thinking configuration is the same — the only difference is using `providerOptions.vertex` instead of `providerOptions.google`. To route through Vertex, configure [Vertex AI credentials](https://vercel.com/docs/ai-gateway/authentication-and-byok/byok) and set the provider order to prefer `vertex`.
  * Gemini 3 and 3.1: Use `thinkingLevel` to control the depth of reasoning
  * Gemini 2.5: Use `thinkingBudget` to set a token limit for thinking
