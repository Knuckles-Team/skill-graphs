##  [Parameters](https://vercel.com/docs/ai-gateway/sdks-and-apis/responses#parameters)[](https://vercel.com/docs/ai-gateway/sdks-and-apis/responses#parameters)
###  [Required](https://vercel.com/docs/ai-gateway/sdks-and-apis/responses#required)[](https://vercel.com/docs/ai-gateway/sdks-and-apis/responses#required)
Parameter | Type | Description
---|---|---
`model` | string | Model ID in `provider/model` format (e.g., `openai/gpt-5.4`, `anthropic/claude-sonnet-4.6`)
`input` | string or array | A text string or array of input items (messages, function calls, function call outputs)
###  [Optional](https://vercel.com/docs/ai-gateway/sdks-and-apis/responses#optional)[](https://vercel.com/docs/ai-gateway/sdks-and-apis/responses#optional)
Parameter | Type | Description
---|---|---
`stream` | boolean | Stream tokens via server-sent events. Defaults to `false`
`max_output_tokens` | integer | Maximum number of tokens to generate
`temperature` | number | Controls randomness (0-2). Lower values are more deterministic
`top_p` | number | Nucleus sampling (0-1)
`presence_penalty` | number | Penalizes tokens that already appear in the text so far
`frequency_penalty` | number | Penalizes tokens based on their frequency in the text so far
`instructions` | string | System-level instructions for the model
`tools` | array | Tool definitions for function calling
`tool_choice` | string or object | Tool selection: `auto`, `required`, `none`, or a specific function
`parallel_tool_calls` | boolean | Allows the model to call multiple tools in a single turn
`allowed_tools` | array | Subset of tool names the model can use for this request
`reasoning` | object | Reasoning config with `effort` (`none`, `minimal`, `low`, `medium`, `high`, `xhigh`). OpenAI models also support `summary` (`detailed`, `auto`, `concise`) to receive a text summary of the model's reasoning
`text` | object | Output format config, including `json_schema` and `json_object` for structured output
`truncation` | string | Truncation strategy for long inputs: `auto` or `disabled`
`previous_response_id` | string | ID of a previous response for multi-turn conversations
`store` | boolean | Stores the response for later retrieval
`metadata` | object | Up to 16 key-value pairs for tracking (keys max 64 chars, values max 512 chars)
`caching` | string | Enables prompt caching. Only `auto` is supported
`prompt_cache_key` | string | Key to identify cached prompts (max 64 characters)
