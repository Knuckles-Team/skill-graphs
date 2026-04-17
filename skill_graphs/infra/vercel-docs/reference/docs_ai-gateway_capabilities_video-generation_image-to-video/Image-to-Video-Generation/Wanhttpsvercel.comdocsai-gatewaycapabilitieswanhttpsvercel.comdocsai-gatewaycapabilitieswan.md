##  [Wan](https://vercel.com/docs/ai-gateway/capabilities#wan)[](https://vercel.com/docs/ai-gateway/capabilities#wan)
Wan offers image-to-video with standard and flash variants. Both support audio generation. Wan requires image URLs (not buffers). Use [Vercel Blob](https://vercel.com/docs/vercel-blob) to host local images.
###  [Wan models](https://vercel.com/docs/ai-gateway/capabilities#wan-models)[](https://vercel.com/docs/ai-gateway/capabilities#wan-models)
Model | Description
---|---
`alibaba/wan-v2.6-i2v` | Standard model with audio
`alibaba/wan-v2.6-i2v-flash` | Fast generation
###  [Wan parameters](https://vercel.com/docs/ai-gateway/capabilities#wan-parameters)[](https://vercel.com/docs/ai-gateway/capabilities#wan-parameters)
Parameter | Type | Required | Description
---|---|---|---
`prompt.image` | `string` | Yes | URL of the image to animate (URLs only, not buffers)
`prompt.text` | `string` | Yes | Description of the motion or animation
`resolution` | `string` | No |  `'1280x720'` or `'1920x1080'`
`duration` | `number` | No | 2-15 seconds
`providerOptions.alibaba.audio` | `boolean` | No | Generate audio. Standard models default to `true`, flash models default to `false`
`providerOptions.alibaba.negativePrompt` | `string` | No | What to avoid in the video. Max 500 characters
`providerOptions.alibaba.audioUrl` | `string` | No | URL to audio file for audio-video sync (WAV/MP3, 3-30s, max 15MB)
`providerOptions.alibaba.watermark` | `boolean` | No | Add watermark to the video. Defaults to `false`
`providerOptions.alibaba.pollIntervalMs` | `number` | No | How often to check task status. Defaults to `5000`
`providerOptions.alibaba.pollTimeoutMs` | `number` | No | Maximum wait time. Defaults to `600000` (10 minutes)
###  [Wan example](https://vercel.com/docs/ai-gateway/capabilities#wan-example)[](https://vercel.com/docs/ai-gateway/capabilities#wan-example)
wan-image-to-video.ts
```
import { experimental_generateVideo as generateVideo } from 'ai';
import fs from 'node:fs';

const result = await generateVideo({
  model: 'alibaba/wan-v2.6-i2v-flash',
  prompt: {
    image: 'https://example.com/cat.png',
    text: 'The cat waves hello and smiles',
  },
  duration: 5,
  providerOptions: {
    alibaba: {
      audio: true,
    },
  },
});

fs.writeFileSync('output.mp4', result.videos[0].uint8Array);
```

* * *
