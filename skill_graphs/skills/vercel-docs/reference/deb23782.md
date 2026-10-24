##  [Grok Imagine Video](https://vercel.com/docs/ai-gateway/models-and-providers#grok-imagine-video)[](https://vercel.com/docs/ai-gateway/models-and-providers#grok-imagine-video)
Grok Imagine Video (by xAI) generates videos from text prompts with support for multiple aspect ratios and resolutions. Duration ranges from 1-15 seconds.
###  [Grok models](https://vercel.com/docs/ai-gateway/models-and-providers#grok-models)[](https://vercel.com/docs/ai-gateway/models-and-providers#grok-models)
Model | Duration | Aspect Ratios | Resolution
---|---|---|---
`xai/grok-imagine-video` | 1-15s | 1:1, 16:9, 9:16, 4:3, 3:4, 3:2, 2:3 | 480p, 720p
###  [Grok parameters](https://vercel.com/docs/ai-gateway/models-and-providers#grok-parameters)[](https://vercel.com/docs/ai-gateway/models-and-providers#grok-parameters)
Parameter | Type | Required | Description
---|---|---|---
`prompt` | `string` | Yes | Text description of the video to generate
`aspectRatio` | `string` | No | Aspect ratio (`'16:9'`, `'9:16'`, `'1:1'`, `'4:3'`, `'3:4'`, `'3:2'`, `'2:3'`). Defaults to `'16:9'`
`duration` | `number` | No | Video length in seconds (1-15)
`resolution` | `string` | No | Resolution (`'854x480'` for 480p, `'1280x720'` for 720p). Defaults to 480p
`providerOptions.xai.resolution` |  `'480p'` | `'720p'` | No | Native resolution format. Alternative to standard `resolution` parameter
`providerOptions.xai.pollIntervalMs` | `number` | No | How often to check task status. Defaults to `5000`
`providerOptions.xai.pollTimeoutMs` | `number` | No | Maximum wait time. Defaults to `600000` (10 minutes)
###  [Grok example](https://vercel.com/docs/ai-gateway/models-and-providers#grok-example)[](https://vercel.com/docs/ai-gateway/models-and-providers#grok-example)
grok-imagine-video.ts
```
import { experimental_generateVideo as generateVideo } from 'ai';
import fs from 'node:fs';

const result = await generateVideo({
  model: 'xai/grok-imagine-video',
  prompt: 'A chicken flying into the sunset in the style of 90s anime',
  aspectRatio: '16:9',
  duration: 5,
  providerOptions: {
    xai: {
      pollTimeoutMs: 600000,
    },
  },
});

fs.writeFileSync('output.mp4', result.videos[0].uint8Array);
```

Video generation can take several minutes. Set `pollTimeoutMs` to at least 10 minutes (600000ms) for reliable operation. Generated video URLs are ephemeral and should be downloaded promptly.
* * *
