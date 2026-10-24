##  [Google Veo](https://vercel.com/docs/ai-gateway/capabilities#google-veo)[](https://vercel.com/docs/ai-gateway/capabilities#google-veo)
Google's Veo models support image-to-video generation, animating a starting image into a video.
###  [Veo models](https://vercel.com/docs/ai-gateway/capabilities#veo-models)[](https://vercel.com/docs/ai-gateway/capabilities#veo-models)
Model | Description
---|---
`google/veo-3.1-generate-001` | Latest model with audio
`google/veo-3.1-fast-generate-001` | Fast generation
`google/veo-3.0-generate-001` | Previous generation, 1080p max
`google/veo-3.0-fast-generate-001` | Faster generation, lower quality
###  [Veo parameters](https://vercel.com/docs/ai-gateway/capabilities#veo-parameters)[](https://vercel.com/docs/ai-gateway/capabilities#veo-parameters)
Parameter | Type | Required | Description
---|---|---|---
`prompt.image` | `string` | Yes | URL or base64-encoded image to animate
`prompt.text` | `string` | No | Description of the motion or animation
`duration` |  `4` | `6` | `8` | No | Video length in seconds. Defaults to 8
`resolution` | `string` | No | Resolution (`'720p'`, `'1080p'`). Defaults to `'720p'`
`providerOptions.vertex.generateAudio` | `boolean` | No | Generate audio alongside the video
`providerOptions.vertex.resizeMode` |  `'pad'` | `'crop'` | No | How to resize the image to fit video dimensions. Defaults to `'pad'`
`providerOptions.vertex.enhancePrompt` | `boolean` | No | Use Gemini to enhance prompts. Defaults to `true`
`providerOptions.vertex.negativePrompt` | `string` | No | What to discourage in the generated video
`providerOptions.vertex.personGeneration` |  `'dont_allow'` | `'allow_adult'` | `'allow_all'` | No | Whether to allow person generation. Defaults to `'allow_adult'`
`providerOptions.vertex.pollIntervalMs` | `number` | No | How often to check task status. Defaults to `5000`
`providerOptions.vertex.pollTimeoutMs` | `number` | No | Maximum wait time. Defaults to `600000` (10 minutes)
###  [Veo example](https://vercel.com/docs/ai-gateway/capabilities#veo-example)[](https://vercel.com/docs/ai-gateway/capabilities#veo-example)
veo-image-to-video.ts
```
import { experimental_generateVideo as generateVideo } from 'ai';
import fs from 'node:fs';

const result = await generateVideo({
  model: 'google/veo-3.1-generate-001',
  prompt: {
    image: 'https://example.com/landscape.png',
    text: 'Camera slowly pans across the scene as clouds drift by',
  },
  resolution: '1080p',
  providerOptions: {
    vertex: {
      resizeMode: 'crop',
      generateAudio: true,
    },
  },
});

fs.writeFileSync('output.mp4', result.videos[0].uint8Array);
```

* * *
