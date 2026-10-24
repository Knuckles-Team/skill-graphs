##  [Error handling](https://vercel.com/docs/ai-gateway/sdks-and-apis/openresponses#error-handling)[](https://vercel.com/docs/ai-gateway/sdks-and-apis/openresponses#error-handling)
The API returns standard HTTP status codes and error responses.
###  [Common error codes](https://vercel.com/docs/ai-gateway/sdks-and-apis/openresponses#common-error-codes)[](https://vercel.com/docs/ai-gateway/sdks-and-apis/openresponses#common-error-codes)
  * `400 Bad Request` - Invalid request parameters
  * `401 Unauthorized` - Invalid or missing authentication
  * `403 Forbidden` - Insufficient permissions
  * `404 Not Found` - Model or endpoint not found
  * `429 Too Many Requests` - Rate limit exceeded
  * `500 Internal Server Error` - Server error


###  [Error response format](https://vercel.com/docs/ai-gateway/sdks-and-apis/openresponses#error-response-format)[](https://vercel.com/docs/ai-gateway/sdks-and-apis/openresponses#error-response-format)
When an error occurs, the API returns a JSON object with details about what went wrong.
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
[ Previous Anthropic Messages API ](https://vercel.com/docs/ai-gateway/sdks-and-apis/anthropic-messages-api)[ Next Text Generation ](https://vercel.com/docs/ai-gateway/sdks-and-apis/openresponses/text-generation)
Was this helpful?
Send
On this page
  * [Base URL](https://vercel.com/docs/ai-gateway/sdks-and-apis/openresponses#base-url)
  * [Authentication](https://vercel.com/docs/ai-gateway/sdks-and-apis/openresponses#authentication)
  * [Supported features](https://vercel.com/docs/ai-gateway/sdks-and-apis/openresponses#supported-features)
  * [Getting started](https://vercel.com/docs/ai-gateway/sdks-and-apis/openresponses#getting-started)
  * [Parameters](https://vercel.com/docs/ai-gateway/sdks-and-apis/openresponses#parameters)
  * [Required parameters](https://vercel.com/docs/ai-gateway/sdks-and-apis/openresponses#required-parameters)
  * [Optional parameters](https://vercel.com/docs/ai-gateway/sdks-and-apis/openresponses#optional-parameters)
  * [Example with parameters](https://vercel.com/docs/ai-gateway/sdks-and-apis/openresponses#example-with-parameters)
  * [Error handling](https://vercel.com/docs/ai-gateway/sdks-and-apis/openresponses#error-handling)
  * [Common error codes](https://vercel.com/docs/ai-gateway/sdks-and-apis/openresponses#common-error-codes)
  * [Error response format](https://vercel.com/docs/ai-gateway/sdks-and-apis/openresponses#error-response-format)


Copy as MarkdownGive feedbackAsk AI about this page
