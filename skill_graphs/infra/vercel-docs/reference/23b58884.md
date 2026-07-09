##  [ByteDance Seedance](https://vercel.com/docs/ai-gateway/models-and-providers#bytedance-seedance)[](https://vercel.com/docs/ai-gateway/models-and-providers#bytedance-seedance)
ByteDance's Seedance models generate high-quality videos from text prompts with optional synchronized audio and a draft mode for low-cost previews. All models output MP4 at 24fps.
###  [Seedance models](https://vercel.com/docs/ai-gateway/models-and-providers#seedance-models)[](https://vercel.com/docs/ai-gateway/models-and-providers#seedance-models)
Model | Description
---|---
`bytedance/seedance-v1.5-pro` | Latest model with audio sync and draft mode. 4-12s, up to 1080p
`bytedance/seedance-v1.0-pro` | Previous generation. 2-12s, up to 1080p
`bytedance/seedance-v1.0-pro-fast` | Optimized for speed and cost. 2-12s
`bytedance/seedance-v1.0-lite-t2v` | Lightweight text-to-video. 2-12s, up to 1080p
###  [Seedance parameters](https://vercel.com/docs/ai-gateway/models-and-providers#seedance-parameters)[](https://vercel.com/docs/ai-gateway/models-and-providers#seedance-parameters)
Parameter | Type | Required | Description
---|---|---|---
`prompt` | `string` | Yes | Text description of the video to generate
`aspectRatio` | `string` | No | Aspect ratio (`'16:9'`, `'4:3'`, `'1:1'`, `'3:4'`, `'9:16'`, `'21:9'`)
`resolution` | `string` | No | Resolution (`'854x480'`, `'1280x720'`, `'1920x1080'`)
`duration` | `number` | No | Video length in seconds. v1.5: 4-12s. v1.0: 2-12s
`providerOptions.bytedance.watermark` | `boolean` | No | Add a watermark to the video
`providerOptions.bytedance.generateAudio` | `boolean` | No | Generate synchronized audio. Seedance v1.5 Pro only
`providerOptions.bytedance.cameraFixed` | `boolean` | No | Fix the camera position during generation
`providerOptions.bytedance.draft` | `boolean` | No | Generate a 480p preview for fast iteration. Seedance v1.5 Pro only
`providerOptions.bytedance.serviceTier` |  `'default'` | `'flex'` | No |  `'default'` for online inference. `'flex'` for offline at 50% cost, higher latency
`providerOptions.bytedance.pollIntervalMs` | `number` | No | How often to check task status. Defaults to `3000`
`providerOptions.bytedance.pollTimeoutMs` | `number` | No | Maximum wait time. Defaults to `300000` (5 minutes)
###  [Seedance example](https://vercel.com/docs/ai-gateway/models-and-providers#seedance-example)[](https://vercel.com/docs/ai-gateway/models-and-providers#seedance-example)
seedance-text-to-video.ts
```
import { experimental_generateVideo as generateVideo } from 'ai';
import fs from 'node:fs';

const result = await generateVideo({
  model: 'bytedance/seedance-v1.5-pro',
  prompt: 'A chicken flying into the sunset in the style of 90s anime',
  resolution: '1280x720',
  duration: 5,
  providerOptions: {
    bytedance: {
      pollTimeoutMs: 600000,
    },
  },
});

fs.writeFileSync('output.mp4', result.videos[0].uint8Array);
```

###  [Seedance text-to-video with audio](https://vercel.com/docs/ai-gateway/models-and-providers#seedance-text-to-video-with-audio)[](https://vercel.com/docs/ai-gateway/models-and-providers#seedance-text-to-video-with-audio)
Generate video with synchronized audio. Requires Seedance v1.5 Pro.
seedance-text-to-video-audio.ts
```
import { experimental_generateVideo as generateVideo } from 'ai';
import fs from 'node:fs';

const result = await generateVideo({
  model: 'bytedance/seedance-v1.5-pro',
  prompt:
    'A thunderstorm rolling over a vast wheat field, lightning illuminating the clouds, rain beginning to fall',
  resolution: '1280x720',
  duration: 5,
  providerOptions: {
    bytedance: {
      generateAudio: true,
      pollTimeoutMs: 600000,
    },
  },
});

fs.writeFileSync('output.mp4', result.videos[0].uint8Array);
```

Video generation can take several minutes. Set `pollTimeoutMs` to at least 10 minutes (600000ms) for reliable operation.
* * *
* * *
[ Previous Agent Quickstart ](https://vercel.com/docs/ai-gateway/agent-quickstart)[ Next Provider Options ](https://vercel.com/docs/ai-gateway/models-and-providers/provider-options)
Was this helpful?
Send
On this page
  * [Google Veo](https://vercel.com/docs/ai-gateway/models-and-providers#google-veo)
  * [Veo models](https://vercel.com/docs/ai-gateway/models-and-providers#veo-models)
  * [Veo parameters](https://vercel.com/docs/ai-gateway/models-and-providers#veo-parameters)
  * [Veo example](https://vercel.com/docs/ai-gateway/models-and-providers#veo-example)
  * [KlingAI](https://vercel.com/docs/ai-gateway/models-and-providers#klingai)
  * [KlingAI models](https://vercel.com/docs/ai-gateway/models-and-providers#klingai-models)
  * [KlingAI parameters](https://vercel.com/docs/ai-gateway/models-and-providers#klingai-parameters)
  * [KlingAI example](https://vercel.com/docs/ai-gateway/models-and-providers#klingai-example)
  * [KlingAI camera control](https://vercel.com/docs/ai-gateway/models-and-providers#klingai-camera-control)
  * [KlingAI multi-shot](https://vercel.com/docs/ai-gateway/models-and-providers#klingai-multi-shot)
  * [Wan](https://vercel.com/docs/ai-gateway/models-and-providers#wan)
  * [Wan models](https://vercel.com/docs/ai-gateway/models-and-providers#wan-models)
  * [Wan parameters](https://vercel.com/docs/ai-gateway/models-and-providers#wan-parameters)
  * [Wan example](https://vercel.com/docs/ai-gateway/models-and-providers#wan-example)
  * [Grok Imagine Video](https://vercel.com/docs/ai-gateway/models-and-providers#grok-imagine-video)
  * [Grok models](https://vercel.com/docs/ai-gateway/models-and-providers#grok-models)
  * [Grok parameters](https://vercel.com/docs/ai-gateway/models-and-providers#grok-parameters)
  * [Grok example](https://vercel.com/docs/ai-gateway/models-and-providers#grok-example)
  * [ByteDance Seedance](https://vercel.com/docs/ai-gateway/models-and-providers#bytedance-seedance)
  * [Seedance models](https://vercel.com/docs/ai-gateway/models-and-providers#seedance-models)
  * [Seedance parameters](https://vercel.com/docs/ai-gateway/models-and-providers#seedance-parameters)
  * [Seedance example](https://vercel.com/docs/ai-gateway/models-and-providers#seedance-example)
  * [Seedance text-to-video with audio](https://vercel.com/docs/ai-gateway/models-and-providers#seedance-text-to-video-with-audio)


Copy as MarkdownGive feedbackAsk AI about this page
