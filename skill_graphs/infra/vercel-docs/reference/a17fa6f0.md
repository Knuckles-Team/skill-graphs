##  [Error handling](https://vercel.com/docs/ai-gateway/agent-quickstart#error-handling)[](https://vercel.com/docs/ai-gateway/agent-quickstart#error-handling)
The API returns standard HTTP status codes and error responses:
###  [Common error codes](https://vercel.com/docs/ai-gateway/agent-quickstart#common-error-codes)[](https://vercel.com/docs/ai-gateway/agent-quickstart#common-error-codes)
  * `400 Bad Request`: Invalid request parameters
  * `401 Unauthorized`: Invalid or missing authentication
  * `403 Forbidden`: Insufficient permissions
  * `404 Not Found`: Model or endpoint not found
  * `429 Too Many Requests`: Rate limit exceeded
  * `500 Internal Server Error`: Server error


###  [Error response format](https://vercel.com/docs/ai-gateway/agent-quickstart#error-response-format)[](https://vercel.com/docs/ai-gateway/agent-quickstart#error-response-format)
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
[ Previous Getting Started ](https://vercel.com/docs/ai-gateway/getting-started)[ Next Models & Providers ](https://vercel.com/docs/ai-gateway/models-and-providers)
Was this helpful?
Send
On this page
  * [Base URL](https://vercel.com/docs/ai-gateway/agent-quickstart#base-url)
  * [Authentication](https://vercel.com/docs/ai-gateway/agent-quickstart#authentication)
  * [Supported endpoints](https://vercel.com/docs/ai-gateway/agent-quickstart#supported-endpoints)
  * [Integration with existing tools](https://vercel.com/docs/ai-gateway/agent-quickstart#integration-with-existing-tools)
  * [OpenAI client libraries](https://vercel.com/docs/ai-gateway/agent-quickstart#openai-client-libraries)
  * [AI SDK](https://vercel.com/docs/ai-gateway/agent-quickstart#ai-sdk)
  * [List models](https://vercel.com/docs/ai-gateway/agent-quickstart#list-models)
  * [Retrieve model](https://vercel.com/docs/ai-gateway/agent-quickstart#retrieve-model)
  * [Error handling](https://vercel.com/docs/ai-gateway/agent-quickstart#error-handling)
  * [Common error codes](https://vercel.com/docs/ai-gateway/agent-quickstart#common-error-codes)
  * [Error response format](https://vercel.com/docs/ai-gateway/agent-quickstart#error-response-format)


Copy as MarkdownGive feedbackAsk AI about this page
