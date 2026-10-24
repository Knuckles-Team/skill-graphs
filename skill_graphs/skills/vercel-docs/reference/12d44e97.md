##  [Supported endpoints](https://vercel.com/docs/ai-gateway/agent-quickstart#supported-endpoints)[](https://vercel.com/docs/ai-gateway/agent-quickstart#supported-endpoints)
The AI Gateway supports the following Chat Completions API endpoints:
  * [`GET /models`](https://vercel.com/docs/ai-gateway/agent-quickstart#list-models) - List available models
  * [`GET /models/{model}`](https://vercel.com/docs/ai-gateway/agent-quickstart#retrieve-model) - Retrieve a specific model
  * [`POST /chat/completions`](https://vercel.com/docs/ai-gateway/sdks-and-apis/openai-chat-completions/chat-completions) - Create chat completions with support for streaming, attachments, [tool calls](https://vercel.com/docs/ai-gateway/sdks-and-apis/openai-chat-completions/tool-calls), and [structured outputs](https://vercel.com/docs/ai-gateway/sdks-and-apis/openai-chat-completions/structured-outputs)
  * [`POST /embeddings`](https://vercel.com/docs/ai-gateway/sdks-and-apis/openai-chat-completions/embeddings) - Generate vector embeddings


For advanced features, see:
  * [Advanced configuration](https://vercel.com/docs/ai-gateway/sdks-and-apis/openai-chat-completions/advanced) - Reasoning, provider options, model fallbacks, BYOK, and prompt caching
  * [Image generation](https://vercel.com/docs/ai-gateway/sdks-and-apis/openai-chat-completions/image-generation) - Generate images using multimodal models
  * [Direct REST API usage](https://vercel.com/docs/ai-gateway/sdks-and-apis/openai-chat-completions/rest-api) - Use the API without client libraries
