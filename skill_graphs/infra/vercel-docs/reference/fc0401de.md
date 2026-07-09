##  [KlingAI](https://vercel.com/docs/ai-gateway/models-and-providers#klingai)[](https://vercel.com/docs/ai-gateway/models-and-providers#klingai)
KlingAI offers text-to-video with standard and professional quality modes. Audio generation requires v2.6+ models. Duration is 5-10 seconds.
###  [KlingAI models](https://vercel.com/docs/ai-gateway/models-and-providers#klingai-models)[](https://vercel.com/docs/ai-gateway/models-and-providers#klingai-models)
Model | Description
---|---
`klingai/kling-v3.0-t2v` | Multi-shot generation, 15s clips, enhanced consistency
`klingai/kling-v2.6-t2v` | Audio-visual co-generation, cinematic motion
`klingai/kling-v2.5-turbo-t2v` | Faster generation, lower cost
###  [KlingAI parameters](https://vercel.com/docs/ai-gateway/models-and-providers#klingai-parameters)[](https://vercel.com/docs/ai-gateway/models-and-providers#klingai-parameters)
Parameter | Type | Required | Description
---|---|---|---
`prompt` | `string` | Yes | Text description of the video to generate. Max 2500 characters.
`aspectRatio` | `string` | No | Aspect ratio (`'16:9'`, `'9:16'`, `'1:1'`). Defaults to `'16:9'`.
`duration` | `number` | No | Video length in seconds. 5 or 10 for v2.x, 3-15 for v3.0. Defaults to `5`.
`providerOptions.klingai.mode` |  `'std'` | `'pro'` | No |  `'std'` for standard quality. `'pro'` for professional quality. Defaults to `'std'`.
`providerOptions.klingai.negativePrompt` | `string` | No | What to avoid in the video. Max 2500 characters.
`providerOptions.klingai.sound` |  `'on'` | `'off'` | No | Generate audio. Defaults to `'off'`. Requires v2.6+.
`providerOptions.klingai.cfgScale` | `number` | No | Prompt adherence (0-1). Higher = stricter. Defaults to `0.5`. Not supported on v2.x.
`providerOptions.klingai.voiceList` | `array` | No | Voice IDs for speech. Max 2 voices. Requires v3.0+ with `sound: 'on'`.
`providerOptions.klingai.multiShot` | `boolean` | No | Enable multi-shot generation. Requires v3.0+. See [KlingAI multi-shot](https://vercel.com/docs/ai-gateway/models-and-providers#klingai-multi-shot).
`providerOptions.klingai.watermarkInfo` | `object` | No | Set `{ enabled: true }` to generate watermarked result.
`providerOptions.klingai.pollIntervalMs` | `number` | No | How often to check task status. Defaults to `5000`.
`providerOptions.klingai.pollTimeoutMs` | `number` | No | Maximum wait time. Defaults to `600000` (10 minutes).
###  [KlingAI example](https://vercel.com/docs/ai-gateway/models-and-providers#klingai-example)[](https://vercel.com/docs/ai-gateway/models-and-providers#klingai-example)
klingai-text-to-video.ts
```
import { experimental_generateVideo as generateVideo } from 'ai';
import fs from 'node:fs';

const result = await generateVideo({
  model: 'klingai/kling-v2.6-t2v',
  prompt: 'A chicken flying into the sunset in the style of 90s anime',
  aspectRatio: '16:9',
  duration: 5,
  providerOptions: {
    klingai: {
      mode: 'std',
    },
  },
});

fs.writeFileSync('output.mp4', result.videos[0].uint8Array);
```

###  [KlingAI camera control](https://vercel.com/docs/ai-gateway/models-and-providers#klingai-camera-control)[](https://vercel.com/docs/ai-gateway/models-and-providers#klingai-camera-control)
Control camera movement during video generation.
Parameter | Type | Required | Description
---|---|---|---
`providerOptions.klingai.cameraControl.type` | `string` | Yes | Camera movement type. See options below.
`providerOptions.klingai.cameraControl.config` | `object` | No | Movement configuration. Required when `type` is `'simple'`.
Camera movement types:
Type | Description | Config required
---|---|---
`'simple'` | Basic movement with one axis | Yes
`'down_back'` | Camera descends and moves backward | No
`'forward_up'` | Camera moves forward and tilts up | No
`'right_turn_forward'` | Rotate right then move forward | No
`'left_turn_forward'` | Rotate left then move forward | No
Simple camera config options (use only one, set others to 0):
Config | Range | Description
---|---|---
`horizontal` | [-10, 10] | Camera translation along x-axis. Negative = left.
`vertical` | [-10, 10] | Camera translation along y-axis. Negative = down.
`pan` | [-10, 10] | Camera rotation around y-axis. Negative = left.
`tilt` | [-10, 10] | Camera rotation around x-axis. Negative = down.
`roll` | [-10, 10] | Camera rotation around z-axis. Negative = counter-clockwise.
`zoom` | [-10, 10] | Focal length change. Negative = narrower FOV.
camera-control.ts
```
import { experimental_generateVideo as generateVideo } from 'ai';
import fs from 'node:fs';

const result = await generateVideo({
  model: 'klingai/kling-v2.6-t2v',
  prompt: 'A serene mountain landscape at sunset',
  aspectRatio: '16:9',
  providerOptions: {
    klingai: {
      mode: 'std',
      cameraControl: {
        type: 'simple',
        config: {
          zoom: 5,
          horizontal: 0,
          vertical: 0,
          pan: 0,
          tilt: 0,
          roll: 0,
        },
      },
    },
  },
});

fs.writeFileSync('output.mp4', result.videos[0].uint8Array);
```

###  [KlingAI multi-shot](https://vercel.com/docs/ai-gateway/models-and-providers#klingai-multi-shot)[](https://vercel.com/docs/ai-gateway/models-and-providers#klingai-multi-shot)
Generate videos with multiple storyboard shots, each with its own prompt and duration. Requires Kling v3.0+ models.
Parameter | Type | Required | Description
---|---|---|---
`providerOptions.klingai.multiShot` | `boolean` | Yes | Set to `true` to enable multi-shot generation
`providerOptions.klingai.shotType` | `string` | No | Set to `'customize'` for custom shot durations
`providerOptions.klingai.multiPrompt` | `array` | Yes | Array of shot configurations
`providerOptions.klingai.multiPrompt[].index` | `number` | Yes | Shot order (starting from 1)
`providerOptions.klingai.multiPrompt[].prompt` | `string` | Yes | Text description for this shot
`providerOptions.klingai.multiPrompt[].duration` | `string` | Yes | Duration in seconds for this shot
multi-shot.ts
```
import { experimental_generateVideo as generateVideo } from 'ai';
import fs from 'node:fs';

const result = await generateVideo({
  model: 'klingai/kling-v3.0-t2v',
  prompt: '',
  aspectRatio: '16:9',
  duration: 10,
  providerOptions: {
    klingai: {
      mode: 'pro',
      multiShot: true,
      shotType: 'customize',
      multiPrompt: [
        {
          index: 1,
          prompt: 'A sunrise over a calm ocean, warm golden light.',
          duration: '4',
        },
        {
          index: 2,
          prompt: 'A flock of seagulls take flight from the beach.',
          duration: '3',
        },
        {
          index: 3,
          prompt: 'Waves crash against rocky cliffs at sunset.',
          duration: '3',
        },
      ],
      sound: 'on',
    },
  },
});

fs.writeFileSync('output.mp4', result.videos[0].uint8Array);
```

* * *
