##  [ByteDance Seedance](https://vercel.com/docs/ai-gateway/capabilities#bytedance-seedance)[](https://vercel.com/docs/ai-gateway/capabilities#bytedance-seedance)
ByteDance's Seedance models animate images into videos with support for first-and-last-frame control, multi-reference images, and optional audio generation. All models output MP4 at 24fps. Seedance requires image URLs (not buffers). Use [Vercel Blob](https://vercel.com/docs/vercel-blob) to host local images.
###  [Seedance models](https://vercel.com/docs/ai-gateway/capabilities#seedance-models)[](https://vercel.com/docs/ai-gateway/capabilities#seedance-models)
Model | Description
---|---
`bytedance/seedance-v1.5-pro` | Latest model with audio sync. First frame and first+last frame. 4-12s, up to 1080p
`bytedance/seedance-v1.0-pro` | First frame and first+last frame. 2-12s, up to 1080p
`bytedance/seedance-v1.0-pro-fast` | First frame only. Optimized for speed. 2-12s
`bytedance/seedance-v1.0-lite-i2v` | First frame, first+last frame, multi-reference (1-4 images). 2-12s, up to 720p
###  [Seedance parameters](https://vercel.com/docs/ai-gateway/capabilities#seedance-parameters)[](https://vercel.com/docs/ai-gateway/capabilities#seedance-parameters)
Parameter | Type | Required | Description
---|---|---|---
`prompt.image` | `string` | Yes | URL of the image to animate (first frame)
`prompt.text` | `string` | No | Description of the motion or animation
`aspectRatio` | `string` | No | Aspect ratio (`'16:9'`, `'4:3'`, `'1:1'`, `'3:4'`, `'9:16'`, `'21:9'`, `'adaptive'`). `'adaptive'` uses the input image's aspect ratio
`resolution` | `string` | No | Resolution (`'854x480'`, `'1280x720'`, `'1920x1080'`). Lite I2V supports up to 720p
`duration` | `number` | No | Video length in seconds. v1.5: 4-12s. v1.0: 2-12s
`providerOptions.bytedance.lastFrameImage` | `string` | No | URL of the last frame image. Enables first+last frame mode. See [first and last frame](https://vercel.com/docs/ai-gateway/capabilities#seedance-first-and-last-frame)
`providerOptions.bytedance.referenceImages` | `string[]` | No | 1-4 reference image URLs. Lite I2V only. See [multi-reference images](https://vercel.com/docs/ai-gateway/capabilities#seedance-multi-reference-images)
`providerOptions.bytedance.generateAudio` | `boolean` | No | Generate synchronized audio. Seedance v1.5 Pro only
`providerOptions.bytedance.watermark` | `boolean` | No | Add a watermark to the video
`providerOptions.bytedance.cameraFixed` | `boolean` | No | Fix the camera position during generation
`providerOptions.bytedance.returnLastFrame` | `boolean` | No | Return the last frame of the generated video. Useful for chaining consecutive videos
`providerOptions.bytedance.serviceTier` |  `'default'` | `'flex'` | No |  `'default'` for online inference. `'flex'` for offline at 50% cost, higher latency
`providerOptions.bytedance.pollIntervalMs` | `number` | No | How often to check task status. Defaults to `3000`
`providerOptions.bytedance.pollTimeoutMs` | `number` | No | Maximum wait time. Defaults to `300000` (5 minutes)
###  [Seedance example](https://vercel.com/docs/ai-gateway/capabilities#seedance-example)[](https://vercel.com/docs/ai-gateway/capabilities#seedance-example)
seedance-image-to-video.ts
```
import { experimental_generateVideo as generateVideo } from 'ai';
import fs from 'node:fs';

const result = await generateVideo({
  model: 'bytedance/seedance-v1.5-pro',
  prompt: {
    image: 'https://example.com/cat.png',
    text: 'The cat slowly turns its head and blinks',
  },
  duration: 5,
  providerOptions: {
    bytedance: {
      pollTimeoutMs: 600000,
    },
  },
});

fs.writeFileSync('output.mp4', result.videos[0].uint8Array);
```

###  [Seedance first and last frame](https://vercel.com/docs/ai-gateway/capabilities#seedance-first-and-last-frame)[](https://vercel.com/docs/ai-gateway/capabilities#seedance-first-and-last-frame)
Generate a video that transitions smoothly between a starting and ending image. Provide the first frame via `prompt.image` and the last frame via `lastFrameImage`.
Parameter | Type | Required | Description
---|---|---|---
`prompt.image` | `string` | Yes | The first frame (starting image)
`providerOptions.bytedance.lastFrameImage` | `string` | Yes | The last frame (ending image). Model transitions between the two frames
Supported by Seedance v1.5 Pro, v1.0 Pro, and v1.0 Lite I2V.
seedance-first-last-frame.ts
```
import { experimental_generateVideo as generateVideo } from 'ai';
import fs from 'node:fs';

const result = await generateVideo({
  model: 'bytedance/seedance-v1.5-pro',
  prompt: {
    image: 'https://example.com/first-frame.jpg',
    text: 'Create a 360-degree orbiting camera shot based on this photo',
  },
  duration: 5,
  providerOptions: {
    bytedance: {
      lastFrameImage: 'https://example.com/last-frame.jpg',
      generateAudio: true,
      watermark: false,
      pollTimeoutMs: 600000,
    },
  },
});

fs.writeFileSync('output.mp4', result.videos[0].uint8Array);
```

###  [Seedance multi-reference images](https://vercel.com/docs/ai-gateway/capabilities#seedance-multi-reference-images)[](https://vercel.com/docs/ai-gateway/capabilities#seedance-multi-reference-images)
Provide 1-4 reference images that the model uses to faithfully reproduce object shapes, colors, and textures. Use `[Image 1]`, `[Image 2]`, etc. in your prompt to reference each image. Requires the `seedance-v1.0-lite-i2v` model.
Parameter | Type | Required | Description
---|---|---|---
`providerOptions.bytedance.referenceImages` | `string[]` | Yes | Array of 1-4 reference image URLs
seedance-multi-reference.ts
```
import { experimental_generateVideo as generateVideo } from 'ai';
import fs from 'node:fs';

const result = await generateVideo({
  model: 'bytedance/seedance-v1.0-lite-i2v',
  prompt:
    'A boy wearing glasses and a blue T-shirt from [Image 1] and a corgi dog from [Image 2], sitting on the lawn from [Image 3], in 3D cartoon style',
  aspectRatio: '16:9',
  duration: 5,
  providerOptions: {
    bytedance: {
      referenceImages: [
        'https://example.com/boy.png',
        'https://example.com/corgi.png',
        'https://example.com/lawn.png',
      ],
      watermark: false,
      pollTimeoutMs: 600000,
    },
  },
});

fs.writeFileSync('output.mp4', result.videos[0].uint8Array);
```

Video generation can take several minutes. Set `pollTimeoutMs` to at least 10 minutes (600000ms) for reliable operation.
* * *
* * *
[ Previous Models & Providers ](https://vercel.com/docs/ai-gateway/models-and-providers)[ Next Observability ](https://vercel.com/docs/ai-gateway/capabilities/observability)
Was this helpful?
Send
On this page
  * [Google Veo](https://vercel.com/docs/ai-gateway/capabilities#google-veo)
  * [Veo models](https://vercel.com/docs/ai-gateway/capabilities#veo-models)
  * [Veo parameters](https://vercel.com/docs/ai-gateway/capabilities#veo-parameters)
  * [Veo example](https://vercel.com/docs/ai-gateway/capabilities#veo-example)
  * [KlingAI](https://vercel.com/docs/ai-gateway/capabilities#klingai)
  * [KlingAI models](https://vercel.com/docs/ai-gateway/capabilities#klingai-models)
  * [KlingAI parameters](https://vercel.com/docs/ai-gateway/capabilities#klingai-parameters)
  * [KlingAI image requirements](https://vercel.com/docs/ai-gateway/capabilities#klingai-image-requirements)
  * [KlingAI example](https://vercel.com/docs/ai-gateway/capabilities#klingai-example)
  * [KlingAI first and last frame](https://vercel.com/docs/ai-gateway/capabilities#klingai-first-and-last-frame)
  * [KlingAI voice generation](https://vercel.com/docs/ai-gateway/capabilities#klingai-voice-generation)
  * [KlingAI camera control](https://vercel.com/docs/ai-gateway/capabilities#klingai-camera-control)
  * [KlingAI motion brush](https://vercel.com/docs/ai-gateway/capabilities#klingai-motion-brush)
  * [KlingAI multi-shot](https://vercel.com/docs/ai-gateway/capabilities#klingai-multi-shot)
  * [Wan](https://vercel.com/docs/ai-gateway/capabilities#wan)
  * [Wan models](https://vercel.com/docs/ai-gateway/capabilities#wan-models)
  * [Wan parameters](https://vercel.com/docs/ai-gateway/capabilities#wan-parameters)
  * [Wan example](https://vercel.com/docs/ai-gateway/capabilities#wan-example)
  * [Grok Imagine Video](https://vercel.com/docs/ai-gateway/capabilities#grok-imagine-video)
  * [Grok models](https://vercel.com/docs/ai-gateway/capabilities#grok-models)
  * [Grok parameters](https://vercel.com/docs/ai-gateway/capabilities#grok-parameters)
  * [Grok example](https://vercel.com/docs/ai-gateway/capabilities#grok-example)
  * [ByteDance Seedance](https://vercel.com/docs/ai-gateway/capabilities#bytedance-seedance)
  * [Seedance models](https://vercel.com/docs/ai-gateway/capabilities#seedance-models)
  * [Seedance parameters](https://vercel.com/docs/ai-gateway/capabilities#seedance-parameters)
  * [Seedance example](https://vercel.com/docs/ai-gateway/capabilities#seedance-example)
  * [Seedance first and last frame](https://vercel.com/docs/ai-gateway/capabilities#seedance-first-and-last-frame)
  * [Seedance multi-reference images](https://vercel.com/docs/ai-gateway/capabilities#seedance-multi-reference-images)


Copy as MarkdownGive feedbackAsk AI about this page
