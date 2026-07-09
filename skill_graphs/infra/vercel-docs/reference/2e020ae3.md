##  [Wan](https://vercel.com/docs/ai-gateway/models-and-providers#wan)[](https://vercel.com/docs/ai-gateway/models-and-providers#wan)
Wan (by Alibaba) offers text-to-video with native audio generation and prompt enhancement. Use `resolution` parameter (e.g., `'1280x720'`), not `aspectRatio`.
###  [Wan models](https://vercel.com/docs/ai-gateway/models-and-providers#wan-models)[](https://vercel.com/docs/ai-gateway/models-and-providers#wan-models)
Model | Description
---|---
`alibaba/wan-v2.6-t2v` | Latest model with native audio
`alibaba/wan-v2.5-t2v-preview` | Preview model
###  [Wan parameters](https://vercel.com/docs/ai-gateway/models-and-providers#wan-parameters)[](https://vercel.com/docs/ai-gateway/models-and-providers#wan-parameters)
Parameter | Type | Required | Description
---|---|---|---
`prompt` | `string` | Yes | Text description of the video to generate
`resolution` | `string` | No | v2.6: `'1280x720'` or `'1920x1080'`. v2.5: also supports `'848x480'`
`duration` | `number` | No | v2.6: 2-15s. v2.5: 5s or 10s only. Defaults to 5
`providerOptions.alibaba.promptExtend` | `boolean` | No | Enhance prompt for better quality. Defaults to `true`
`providerOptions.alibaba.negativePrompt` | `string` | No | What to avoid in the video. Max 500 characters
`providerOptions.alibaba.audioUrl` | `string` | No | URL to audio file for audio-video sync (WAV/MP3, 3-30s, max 15MB). v2.5 only
`providerOptions.alibaba.shotType` |  `'single'` | `'multi'` | No |  `'multi'` enables multi-shot cinematic narrative. v2.6 only
`providerOptions.alibaba.watermark` | `boolean` | No | Add watermark to the video. Defaults to `false`
`providerOptions.alibaba.pollIntervalMs` | `number` | No | How often to check task status. Defaults to `5000`
`providerOptions.alibaba.pollTimeoutMs` | `number` | No | Maximum wait time. Defaults to `600000` (10 minutes)
###  [Wan example](https://vercel.com/docs/ai-gateway/models-and-providers#wan-example)[](https://vercel.com/docs/ai-gateway/models-and-providers#wan-example)
wan-text-to-video.ts
```
import { experimental_generateVideo as generateVideo } from 'ai';
import fs from 'node:fs';

const result = await generateVideo({
  model: 'alibaba/wan-v2.6-t2v',
  prompt: 'A chicken flying into the sunset in the style of 90s anime',
  resolution: '1280x720',
  duration: 5,
  providerOptions: {
    alibaba: {
      promptExtend: true,
    },
  },
});

fs.writeFileSync('output.mp4', result.videos[0].uint8Array);
```

* * *
