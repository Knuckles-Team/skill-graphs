##  [Grok Imagine Video](https://vercel.com/docs/ai-gateway/capabilities#grok-imagine-video)[](https://vercel.com/docs/ai-gateway/capabilities#grok-imagine-video)
Grok Imagine Video (by xAI) can animate images into videos. The output defaults to the input image's aspect ratio. If you specify `aspectRatio`, it will override this and stretch the image to the desired ratio.
###  [Grok models](https://vercel.com/docs/ai-gateway/capabilities#grok-models)[](https://vercel.com/docs/ai-gateway/capabilities#grok-models)
Model | Duration | Resolution
---|---|---
`xai/grok-imagine-video` | 1-15s | 480p, 720p
###  [Grok parameters](https://vercel.com/docs/ai-gateway/capabilities#grok-parameters)[](https://vercel.com/docs/ai-gateway/capabilities#grok-parameters)
Parameter | Type | Required | Description
---|---|---|---
`prompt.image` | `string` | Yes | URL of the image to animate
`prompt.text` | `string` | No | Description of the motion or animation
`duration` | `number` | No | Video length in seconds (1-15)
`aspectRatio` | `string` | No | Override the input image's aspect ratio (stretches the image)
`providerOptions.xai.resolution` |  `'480p'` | `'720p'` | No | Video resolution. Defaults to 480p
`providerOptions.xai.pollIntervalMs` | `number` | No | How often to check task status. Defaults to `5000`
`providerOptions.xai.pollTimeoutMs` | `number` | No | Maximum wait time. Defaults to `600000` (10 minutes)
###  [Grok example](https://vercel.com/docs/ai-gateway/capabilities#grok-example)[](https://vercel.com/docs/ai-gateway/capabilities#grok-example)
grok-image-to-video.ts
```
import { experimental_generateVideo as generateVideo } from 'ai';
import fs from 'node:fs';

const result = await generateVideo({
  model: 'xai/grok-imagine-video',
  prompt: {
    image: 'https://example.com/cat.png',
    text: 'The cat slowly turns its head and blinks',
  },
  duration: 5,
  providerOptions: {
    xai: {
      pollTimeoutMs: 600000,
    },
  },
});

fs.writeFileSync('output.mp4', result.videos[0].uint8Array);
```

* * *
