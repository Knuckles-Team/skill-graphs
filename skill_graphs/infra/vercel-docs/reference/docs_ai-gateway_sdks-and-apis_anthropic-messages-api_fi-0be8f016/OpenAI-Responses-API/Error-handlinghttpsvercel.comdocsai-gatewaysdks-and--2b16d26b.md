##  [Error handling](https://vercel.com/docs/ai-gateway/sdks-and-apis/responses#error-handling)[](https://vercel.com/docs/ai-gateway/sdks-and-apis/responses#error-handling)
The API returns standard HTTP status codes and error responses.
###  [Common error codes](https://vercel.com/docs/ai-gateway/sdks-and-apis/responses#common-error-codes)[](https://vercel.com/docs/ai-gateway/sdks-and-apis/responses#common-error-codes)
  * `400 Bad Request` - Invalid request parameters
  * `401 Unauthorized` - Invalid or missing authentication
  * `403 Forbidden` - Insufficient permissions
  * `404 Not Found` - Model or endpoint not found
  * `429 Too Many Requests` - Rate limit exceeded
  * `500 Internal Server Error` - Server error


###  [Error response format](https://vercel.com/docs/ai-gateway/sdks-and-apis/responses#error-response-format)[](https://vercel.com/docs/ai-gateway/sdks-and-apis/responses#error-response-format)
When an error occurs, the API returns a JSON object with details about what went wrong.
```
{
  "error": {
    "type": "invalid_request_error",
    "message": "At least one user message is required in the input"
  }
}
```

* * *
[ Previous AI SDK ](https://vercel.com/docs/ai-gateway/sdks-and-apis/ai-sdk)[ Next OpenAI Chat Completions API ](https://vercel.com/docs/ai-gateway/sdks-and-apis/openai-chat-completions)
Was this helpful?
Send
On this page
  * [Getting started](https://vercel.com/docs/ai-gateway/sdks-and-apis/responses#getting-started)
  * [Streaming](https://vercel.com/docs/ai-gateway/sdks-and-apis/responses#streaming)
  * [Tool calling](https://vercel.com/docs/ai-gateway/sdks-and-apis/responses#tool-calling)
  * [Structured output](https://vercel.com/docs/ai-gateway/sdks-and-apis/responses#structured-output)
  * [Reasoning](https://vercel.com/docs/ai-gateway/sdks-and-apis/responses#reasoning)
  * [Parameters](https://vercel.com/docs/ai-gateway/sdks-and-apis/responses#parameters)
  * [Required](https://vercel.com/docs/ai-gateway/sdks-and-apis/responses#required)
  * [Optional](https://vercel.com/docs/ai-gateway/sdks-and-apis/responses#optional)
  * [Error handling](https://vercel.com/docs/ai-gateway/sdks-and-apis/responses#error-handling)
  * [Common error codes](https://vercel.com/docs/ai-gateway/sdks-and-apis/responses#common-error-codes)
  * [Error response format](https://vercel.com/docs/ai-gateway/sdks-and-apis/responses#error-response-format)


Copy as MarkdownGive feedbackAsk AI about this page
[AI Gateway](https://vercel.com/docs/ai-gateway)
[SDKs & APIs](https://vercel.com/docs/ai-gateway/sdks-and-apis)
OpenAI Responses API
