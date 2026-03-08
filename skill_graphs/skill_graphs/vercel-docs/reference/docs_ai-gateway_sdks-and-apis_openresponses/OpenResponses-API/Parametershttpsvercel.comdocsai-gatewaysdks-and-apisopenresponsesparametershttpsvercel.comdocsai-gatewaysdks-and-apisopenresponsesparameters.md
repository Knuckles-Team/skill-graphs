##  [Parameters](https://vercel.com/docs/ai-gateway/sdks-and-apis/openresponses#parameters)[](https://vercel.com/docs/ai-gateway/sdks-and-apis/openresponses#parameters)
###  [Required parameters](https://vercel.com/docs/ai-gateway/sdks-and-apis/openresponses#required-parameters)[](https://vercel.com/docs/ai-gateway/sdks-and-apis/openresponses#required-parameters)
  * `model` (string): The model ID in `provider/model` format (e.g., `openai/gpt-5.4`, `anthropic/claude-sonnet-4.6`)
  * `input` (array): Array of message objects containing `type`, `role`, and `content` fields


###  [Optional parameters](https://vercel.com/docs/ai-gateway/sdks-and-apis/openresponses#optional-parameters)[](https://vercel.com/docs/ai-gateway/sdks-and-apis/openresponses#optional-parameters)
  * `stream` (boolean): Stream the response. Defaults to `false`
  * `temperature` (number): Controls randomness. Range: 0-2
  * `top_p` (number): Nucleus sampling. Range: 0-1
  * `max_output_tokens` (integer): Maximum tokens to generate
  * `tools` (array): Tool definitions for function calling
  * `tool_choice` (string): Tool selection mode: `auto`, `required`, or `none`
  * `reasoning` (object): Reasoning configuration with `effort` level
  * `providerOptions` (object): Provider-specific options for gateway configuration


###  [Example with parameters](https://vercel.com/docs/ai-gateway/sdks-and-apis/openresponses#example-with-parameters)[](https://vercel.com/docs/ai-gateway/sdks-and-apis/openresponses#example-with-parameters)
This example shows how to combine multiple parameters to control the model's behavior, set up fallbacks, and enable reasoning.
parameters-example.ts
```
const response = await fetch('https://ai-gateway.vercel.sh/v1/responses', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    Authorization: `Bearer ${process.env.AI_GATEWAY_API_KEY}`,
  },
  body: JSON.stringify({
    model: 'anthropic/claude-sonnet-4.6', // provider/model format
    input: [
      {
        type: 'message',
        role: 'user',
        content: 'Explain neural networks.',
      },
    ],
    stream: true, // stream tokens as generated
    max_output_tokens: 500, // limit response length
    reasoning: {
      effort: 'medium', // reasoning depth
    },
    providerOptions: {
      gateway: {
        models: ['anthropic/claude-sonnet-4.6', 'openai/gpt-5.4'], // fallbacks
      },
    },
  }),
});
```
