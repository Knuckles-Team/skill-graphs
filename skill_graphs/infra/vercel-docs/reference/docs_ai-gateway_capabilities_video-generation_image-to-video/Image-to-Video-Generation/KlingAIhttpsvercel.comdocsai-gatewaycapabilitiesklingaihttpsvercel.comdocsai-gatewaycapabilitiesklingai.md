##  [KlingAI](https://vercel.com/docs/ai-gateway/capabilities#klingai)[](https://vercel.com/docs/ai-gateway/capabilities#klingai)
KlingAI's image-to-video models animate images with standard or professional quality modes.
###  [KlingAI models](https://vercel.com/docs/ai-gateway/capabilities#klingai-models)[](https://vercel.com/docs/ai-gateway/capabilities#klingai-models)
Model | Description
---|---
`klingai/kling-v3.0-i2v` | Multi-shot generation, 15s clips, enhanced consistency
`klingai/kling-v2.6-i2v` | Audio-visual co-generation, cinematic motion
`klingai/kling-v2.5-turbo-i2v` | Faster generation, lower cost
###  [KlingAI parameters](https://vercel.com/docs/ai-gateway/capabilities#klingai-parameters)[](https://vercel.com/docs/ai-gateway/capabilities#klingai-parameters)
Parameter | Type | Required | Description
---|---|---|---
`prompt.image` | `string | Buffer` | Yes | The image to animate. See [image requirements](https://vercel.com/docs/ai-gateway/capabilities#image-requirements) below.
`prompt.text` | `string` | No | Description of the motion. Max 2500 characters.
`duration` | `number` | No | Video length in seconds. 5 or 10 for v2.x, 3-15 for v3.0. Defaults to `5`.
`providerOptions.klingai.mode` |  `'std'` | `'pro'` | No |  `'std'` for standard quality. `'pro'` for professional quality. Defaults to `'std'`.
`providerOptions.klingai.negativePrompt` | `string` | No | What to avoid in the video. Max 2500 characters.
`providerOptions.klingai.cfgScale` | `number` | No | Prompt adherence (0-1). Higher = stricter. Defaults to `0.5`. Not supported on v2.x.
`providerOptions.klingai.sound` |  `'on'` | `'off'` | No | Generate audio. Defaults to `'off'`. Requires v2.6+.
`providerOptions.klingai.voiceList` | `array` | No | Voice IDs for speech. Max 2 voices. Requires v3.0+ with `sound: 'on'`. Cannot coexist with `elementList`. See [voice generation](https://vercel.com/docs/ai-gateway/capabilities#voice-generation).
`providerOptions.klingai.multiShot` | `boolean` | No | Enable multi-shot generation. Requires v3.0+. See [multi-shot](https://vercel.com/docs/ai-gateway/capabilities#multi-shot).
`providerOptions.klingai.elementList` | `array` | No | Reference elements for element control. Up to 3 elements. Requires v3.0+. Cannot coexist with `voiceList`.
`providerOptions.klingai.watermarkInfo` | `object` | No | Set `{ enabled: true }` to generate watermarked result.
`providerOptions.klingai.pollIntervalMs` | `number` | No | How often to check task status. Defaults to `5000`.
`providerOptions.klingai.pollTimeoutMs` | `number` | No | Maximum wait time. Defaults to `600000` (10 minutes).
###  [KlingAI image requirements](https://vercel.com/docs/ai-gateway/capabilities#klingai-image-requirements)[](https://vercel.com/docs/ai-gateway/capabilities#klingai-image-requirements)
The input image (`prompt.image`) must meet these requirements:
  * Formats: `.jpg`, `.jpeg`, `.png`
  * File size: 10MB or less
  * Dimensions: Minimum 300px
  * Aspect ratio: Between 1:2.5 and 2.5:1


When using base64 encoding, submit only the raw base64 string without any prefix:
```
// Correct
const image = 'iVBORw0KGgoAAAANSUhEUgAAAAUA...';

// Incorrect - do not include data: prefix
const image = 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUA...';
```

###  [KlingAI example](https://vercel.com/docs/ai-gateway/capabilities#klingai-example)[](https://vercel.com/docs/ai-gateway/capabilities#klingai-example)
klingai-image-to-video.ts
```
import { experimental_generateVideo as generateVideo } from 'ai';
import fs from 'node:fs';

const result = await generateVideo({
  model: 'klingai/kling-v2.6-i2v',
  prompt: {
    image: 'https://example.com/cat.png',
    text: 'The cat slowly turns its head and blinks',
  },
  duration: 5,
  providerOptions: {
    klingai: {
      mode: 'std',
    },
  },
});

fs.writeFileSync('output.mp4', result.videos[0].uint8Array);
```

###  [KlingAI first and last frame](https://vercel.com/docs/ai-gateway/capabilities#klingai-first-and-last-frame)[](https://vercel.com/docs/ai-gateway/capabilities#klingai-first-and-last-frame)
Generate a video that transitions between a starting and ending image. The model interpolates the motion between the two frames.
Parameter | Type | Required | Description
---|---|---|---
`prompt.image` | `string | Buffer` | Yes | The first frame (starting image).
`providerOptions.klingai.imageTail` | `string | Buffer` | Yes | The last frame (ending image). Same format requirements as `prompt.image`.
When using `imageTail`, the following features are mutually exclusive and cannot be combined:
  * First/last frame (`image` + `imageTail`)
  * Motion brush (`dynamicMasks` / `staticMask`)
  * Camera control (`cameraControl`)


first-last-frame.ts
```
import { experimental_generateVideo as generateVideo } from 'ai';
import fs from 'node:fs';

const firstFrame = fs.readFileSync('start.png');
const lastFrame = fs.readFileSync('end.png');

const result = await generateVideo({
  model: 'klingai/kling-v2.6-i2v',
  prompt: {
    image: firstFrame,
    text: 'Smooth transition between the two scenes',
  },
  providerOptions: {
    klingai: {
      imageTail: lastFrame,
      mode: 'pro',
    },
  },
});

fs.writeFileSync('output.mp4', result.videos[0].uint8Array);
```

###  [KlingAI voice generation](https://vercel.com/docs/ai-gateway/capabilities#klingai-voice-generation)[](https://vercel.com/docs/ai-gateway/capabilities#klingai-voice-generation)
Add speech to your video using voice IDs. Requires v2.6+ models with `sound: 'on'`.
Reference voices in your prompt using `<<<voice_1>>>` syntax, where the number matches the order in `voiceList`:
voice-generation.ts
```
import { experimental_generateVideo as generateVideo } from 'ai';
import fs from 'node:fs';

const result = await generateVideo({
  model: 'klingai/kling-v2.6-i2v',
  prompt: {
    image: 'https://example.com/person.png',
    text: 'The person<<<voice_1>>> says: "Hello, welcome to my channel"',
  },
  providerOptions: {
    klingai: {
      mode: 'std',
      sound: 'on',
      voiceList: [{ voiceId: 'your_voice_id' }],
    },
  },
});

fs.writeFileSync('output.mp4', result.videos[0].uint8Array);
```

You can use up to 2 voices per video. Voice IDs come from KlingAI's voice customization API or system preset voices.
###  [KlingAI camera control](https://vercel.com/docs/ai-gateway/capabilities#klingai-camera-control)[](https://vercel.com/docs/ai-gateway/capabilities#klingai-camera-control)
Control camera movement during video generation. This is mutually exclusive with first/last frame and motion brush features.
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
  model: 'klingai/kling-v2.6-i2v',
  prompt: {
    image: 'https://example.com/landscape.png',
    text: 'A serene mountain landscape',
  },
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

###  [KlingAI motion brush](https://vercel.com/docs/ai-gateway/capabilities#klingai-motion-brush)[](https://vercel.com/docs/ai-gateway/capabilities#klingai-motion-brush)
Control which parts of the image move and how using mask images. This is mutually exclusive with first/last frame and camera control features.
Parameter | Type | Required | Description
---|---|---|---
`providerOptions.klingai.staticMask` | `string` | No | Mask image for areas that should remain static.
`providerOptions.klingai.dynamicMasks` | `array` | No | Array of dynamic mask configurations (up to 6).
`providerOptions.klingai.dynamicMasks[].mask` | `string` | Yes | Mask image for areas that should move.
`providerOptions.klingai.dynamicMasks[].trajectories` | `array` | Yes | Motion path coordinates. 2-77 points for 5s video.
Mask requirements:
  * Same format as input image (`.jpg`, `.jpeg`, `.png`)
  * Aspect ratio must match the input image
  * All masks (`staticMask` and `dynamicMasks[].mask`) must have identical resolution


Trajectory coordinates use the bottom-left corner of the image as origin. More points create more accurate paths.
motion-brush.ts
```
import { experimental_generateVideo as generateVideo } from 'ai';
import fs from 'node:fs';

const result = await generateVideo({
  model: 'klingai/kling-v2.6-i2v',
  prompt: {
    image: 'https://example.com/scene.png',
    text: 'A ball bouncing across the scene',
  },
  providerOptions: {
    klingai: {
      mode: 'std',
      dynamicMasks: [
        {
          mask: 'https://example.com/ball-mask.png',
          trajectories: [
            { x: 100, y: 200 },
            { x: 200, y: 300 },
            { x: 300, y: 200 },
            { x: 400, y: 300 },
          ],
        },
      ],
    },
  },
});

fs.writeFileSync('output.mp4', result.videos[0].uint8Array);
```

###  [KlingAI multi-shot](https://vercel.com/docs/ai-gateway/capabilities#klingai-multi-shot)[](https://vercel.com/docs/ai-gateway/capabilities#klingai-multi-shot)
Generate videos with multiple storyboard shots, combining a start frame image with per-shot prompts. Requires Kling v3.0+ models.
Parameter | Type | Required | Description
---|---|---|---
`providerOptions.klingai.multiShot` | `boolean` | Yes | Set to `true` to enable multi-shot generation
`providerOptions.klingai.shotType` | `string` | No | Set to `'customize'` for custom shot durations
`providerOptions.klingai.multiPrompt` | `array` | Yes | Array of shot configurations
`providerOptions.klingai.multiPrompt[].index` | `number` | Yes | Shot order (starting from 1)
`providerOptions.klingai.multiPrompt[].prompt` | `string` | Yes | Text description for this shot
`providerOptions.klingai.multiPrompt[].duration` | `string` | Yes | Duration in seconds for this shot
multi-shot-i2v.ts
```
import { experimental_generateVideo as generateVideo } from 'ai';
import fs from 'node:fs';

const result = await generateVideo({
  model: 'klingai/kling-v3.0-i2v',
  prompt: {
    image: 'https://example.com/start-frame.png',
    text: '',
  },
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
          prompt: 'The character looks up at the sky.',
          duration: '4',
        },
        {
          index: 2,
          prompt: 'A bird flies across the frame.',
          duration: '3',
        },
        {
          index: 3,
          prompt: 'The character smiles and waves.',
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
