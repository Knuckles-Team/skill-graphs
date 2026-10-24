##  [Video generation](https://vercel.com/docs/ai-gateway/capabilities#video-generation)[](https://vercel.com/docs/ai-gateway/capabilities#video-generation)
Generate videos from text prompts, images, or video input using AI models through a single API. Control resolution, duration, aspect ratio, and audio generation across providers.
```
import { experimental_generateVideo as generateVideo } from 'ai';

const { videos } = await generateVideo({
  model: 'google/veo-3.1-generate-001',
  prompt: 'A serene mountain landscape at sunset with clouds drifting by',
  aspectRatio: '16:9',
  resolution: '1920x1080',
  duration: 8,
});
```

Supported providers include Google (Veo 3.1), KlingAI (motion control), and Wan. See the [Video Generation docs](https://vercel.com/docs/ai-gateway/capabilities/video-generation) for implementation details.
