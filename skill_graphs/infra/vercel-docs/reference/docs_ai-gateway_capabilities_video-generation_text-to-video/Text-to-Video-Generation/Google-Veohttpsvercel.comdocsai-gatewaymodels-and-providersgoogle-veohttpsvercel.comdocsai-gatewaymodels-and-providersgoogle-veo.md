##  [Google Veo](https://vercel.com/docs/ai-gateway/models-and-providers#google-veo)[](https://vercel.com/docs/ai-gateway/models-and-providers#google-veo)
Google's Veo models generate high-quality videos with optional audio.
###  [Veo models](https://vercel.com/docs/ai-gateway/models-and-providers#veo-models)[](https://vercel.com/docs/ai-gateway/models-and-providers#veo-models)
Model | Description
---|---
`google/veo-3.1-generate-001` | Latest model with audio generation
`google/veo-3.1-fast-generate-001` | Fast generation
`google/veo-3.0-generate-001` | Previous generation, 1080p max
`google/veo-3.0-fast-generate-001` | Faster generation, lower quality
###  [Veo parameters](https://vercel.com/docs/ai-gateway/models-and-providers#veo-parameters)[](https://vercel.com/docs/ai-gateway/models-and-providers#veo-parameters)
Parameter | Type | Required | Description
---|---|---|---
`prompt` | `string` | Yes | Text description of the video to generate
`aspectRatio` | `string` | No | Aspect ratio (`'16:9'`, `'9:16'`). Defaults to `'16:9'`
`duration` |  `4` | `6` | `8` | No | Video length in seconds. Defaults to 8
`resolution` | `string` | No | Resolution (`'720p'`, `'1080p'`). Defaults to `'720p'`
`providerOptions.vertex.generateAudio` | `boolean` | No | Generate audio alongside the video. Required for Veo 3 models
`providerOptions.vertex.enhancePrompt` | `boolean` | No | Use Gemini to enhance prompts. Defaults to `true`
`providerOptions.vertex.negativePrompt` | `string` | No | What to discourage in the generated video
`providerOptions.vertex.personGeneration` |  `'dont_allow'` | `'allow_adult'` | `'allow_all'` | No | Whether to allow person generation. Defaults to `'allow_adult'`
`providerOptions.vertex.compressionQuality` |  `'optimized'` | `'lossless'` | No | Compression quality. Defaults to `'optimized'`
`providerOptions.vertex.sampleCount` | `number` | No | Number of output videos (1-4)
`providerOptions.vertex.seed` | `number` | No | Seed for deterministic generation (0-4,294,967,295)
`providerOptions.vertex.gcsOutputDirectory` | `string` | No | Cloud Storage URI to store the generated videos
`providerOptions.vertex.referenceImages` | `array` | No | Reference images for style or asset guidance
`providerOptions.vertex.pollIntervalMs` | `number` | No | How often to check task status. Defaults to `5000`
`providerOptions.vertex.pollTimeoutMs` | `number` | No | Maximum wait time. Defaults to `600000` (10 minutes)
###  [Veo example](https://vercel.com/docs/ai-gateway/models-and-providers#veo-example)[](https://vercel.com/docs/ai-gateway/models-and-providers#veo-example)
veo-text-to-video.ts
```
import { experimental_generateVideo as generateVideo } from 'ai';
import fs from 'node:fs';

const result = await generateVideo({
  model: 'google/veo-3.1-generate-001',
  prompt: 'A pangolin curled on a mossy stone in a glowing bioluminescent forest',
  aspectRatio: '16:9',
  resolution: '1920x1080',
  providerOptions: {
    vertex: {
      generateAudio: true,
    },
  },
});

fs.writeFileSync('output.mp4', result.videos[0].uint8Array);
```

* * *
