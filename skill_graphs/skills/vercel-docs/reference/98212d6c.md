##  [Version compatibility](https://vercel.com/docs/ai-gateway/sdks-and-apis/ai-sdk#version-compatibility)[](https://vercel.com/docs/ai-gateway/sdks-and-apis/ai-sdk#version-compatibility)
AI Gateway works with both AI SDK v5 and v6. All core features (text generation, streaming, structured outputs, tool calling) work across both versions.
AI SDK v6 adds support for additional capabilities:
Feature | v5 | v6
---|---|---
Text generation | Yes | Yes
Streaming | Yes | Yes
Structured outputs | Yes | Yes
Tool calling | Yes | Yes
Image generation | Yes | Yes
Video generation | No | Yes
Check your installed version with `npm list ai`. To upgrade, run `npm install ai@latest`. See the
