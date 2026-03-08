##  [Manual caching](https://vercel.com/docs/ai-gateway/models-and-providers/automatic-caching#manual-caching)[](https://vercel.com/docs/ai-gateway/models-and-providers/automatic-caching#manual-caching)
For fine-grained control over what gets cached, you can manually add cache markers instead of using `caching: 'auto'`. This gives you control over exactly which parts of your prompt are cached.
  * Anthropic Messages API: Add `cache_control: { type: 'ephemeral' }` to specific messages. See the
  * AI SDK: Use the `cacheControl` property on messages. See the
  * OpenAI Chat Completions API: See [prompt caching](https://vercel.com/docs/ai-gateway/sdks-and-apis/openai-chat-completions/advanced#prompt-caching) in the advanced guide.
