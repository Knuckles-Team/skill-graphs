##  [Error handling](https://vercel.com/docs/ai-gateway/sdks-and-apis/openai-chat-completions#error-handling)[](https://vercel.com/docs/ai-gateway/sdks-and-apis/openai-chat-completions#error-handling)
The API returns standard HTTP status codes and error responses:
###  [Common error codes](https://vercel.com/docs/ai-gateway/sdks-and-apis/openai-chat-completions#common-error-codes)[](https://vercel.com/docs/ai-gateway/sdks-and-apis/openai-chat-completions#common-error-codes)
  * `400 Bad Request`: Invalid request parameters
  * `401 Unauthorized`: Invalid or missing authentication
  * `403 Forbidden`: Insufficient permissions
  * `404 Not Found`: Model or endpoint not found
  * `429 Too Many Requests`: Rate limit exceeded
  * `500 Internal Server Error`: Server error


###  [Error response format](https://vercel.com/docs/ai-gateway/sdks-and-apis/openai-chat-completions#error-response-format)[](https://vercel.com/docs/ai-gateway/sdks-and-apis/openai-chat-completions#error-response-format)
```
{
  "error": {
    "message": "Invalid request: missing required parameter 'model'",
    "type": "invalid_request_error",
    "param": "model",
    "code": "missing_parameter"
  }
}
```

* * *
[ Previous OpenAI Responses API ](https://vercel.com/docs/ai-gateway/sdks-and-apis/responses)[ Next Chat Completions ](https://vercel.com/docs/ai-gateway/sdks-and-apis/openai-chat-completions/chat-completions)
Was this helpful?
Send
On this page
  * [Base URL](https://vercel.com/docs/ai-gateway/sdks-and-apis/openai-chat-completions#base-url)
  * [Authentication](https://vercel.com/docs/ai-gateway/sdks-and-apis/openai-chat-completions#authentication)
  * [Supported endpoints](https://vercel.com/docs/ai-gateway/sdks-and-apis/openai-chat-completions#supported-endpoints)
  * [Integration with existing tools](https://vercel.com/docs/ai-gateway/sdks-and-apis/openai-chat-completions#integration-with-existing-tools)
  * [OpenAI client libraries](https://vercel.com/docs/ai-gateway/sdks-and-apis/openai-chat-completions#openai-client-libraries)
  * [AI SDK](https://vercel.com/docs/ai-gateway/sdks-and-apis/openai-chat-completions#ai-sdk)
  * [List models](https://vercel.com/docs/ai-gateway/sdks-and-apis/openai-chat-completions#list-models)
  * [Retrieve model](https://vercel.com/docs/ai-gateway/sdks-and-apis/openai-chat-completions#retrieve-model)
  * [Error handling](https://vercel.com/docs/ai-gateway/sdks-and-apis/openai-chat-completions#error-handling)
  * [Common error codes](https://vercel.com/docs/ai-gateway/sdks-and-apis/openai-chat-completions#common-error-codes)
  * [Error response format](https://vercel.com/docs/ai-gateway/sdks-and-apis/openai-chat-completions#error-response-format)


Copy as MarkdownGive feedbackAsk AI about this page
[AI Gateway](https://vercel.com/docs/ai-gateway)
[SDKs & APIs](https://vercel.com/docs/ai-gateway/sdks-and-apis)
OpenAI Chat Completions API
