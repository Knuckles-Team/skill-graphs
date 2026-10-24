##  [Image generation](https://vercel.com/docs/ai-gateway/capabilities#image-generation)[](https://vercel.com/docs/ai-gateway/capabilities#image-generation)
Generate images using AI models through a single API. Requests route to the best available provider, with authentication and response formatting handled automatically.
```
import { gateway } from '@ai-sdk/gateway';
import { experimental_generateImage as generateImage } from 'ai';

const { image } = await generateImage({
  model: gateway.imageModel('openai/dall-e-3'),
  prompt: 'A serene mountain landscape at sunset',
});
```

Supported providers include OpenAI (DALL-E), Google (Imagen), and multimodal LLMs with image capabilities. See the [Image Generation docs](https://vercel.com/docs/ai-gateway/capabilities/image-generation) for implementation details.
