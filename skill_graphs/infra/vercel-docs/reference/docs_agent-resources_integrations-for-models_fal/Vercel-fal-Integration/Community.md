## Community
  * [Open source program](https://vercel.com/open-source-program)
  * [Events](https://vercel.com/events)
  * [Shipped on Vercel](https://vercel.com/shipped)


[](https://vercel.com/home)

Select a display theme: systemlightdark
app/api/fal/proxy/route.ts
Next.js (/app) Next.js (/pages) SvelteKit Other frameworks
```
import { route } from '@fal-ai/serverless-proxy/nextjs';
export const { GET, POST } = route;

```

```
export { handler as default } from '@fal-ai/serverless-proxy/nextjs';

```

```
import { createRequestHandler } from '@fal-ai/serverless-proxy/svelte';import { FAL_KEY } from '$env/static/private';
export const { GET, POST } = createRequestHandler({ credentials: FAL_KEY });

```

```
import * as fal from '@fal-ai/serverless-client';
fal.config({  credentials: process.env.FAL_KEY,});
//const output = await fal.run('fal-ai/fast-sdxl', {  input: {    prompt:      'an astronaut riding a horse on mars, hd, dramatic lighting, detailed',  },});
console.log(output);

```

Terminal
![](https://7nyt0uhk7sse4zvn.public.blob.vercel-storage.com/docs-assets/static/topics/icons/pnpm.svg)pnpm bun yarn npm
```
pnpm i @fal-ai/client
```

```
yarn add @fal-ai/client
```

```
npm i @fal-ai/client
```

```
bun add @fal-ai/client
```

```
pnpm i @fal-ai/client
```

app/api/fal/proxy/route.ts
Next.js (/app) Next.js (/pages) SvelteKit Other frameworks
```
import { route } from '@fal-ai/serverless-proxy/nextjs';
export const { GET, POST } = route;

```

```
export { handler as default } from '@fal-ai/serverless-proxy/nextjs';

```

```
import { createRequestHandler } from '@fal-ai/serverless-proxy/svelte';import { FAL_KEY } from '$env/static/private';
export const { GET, POST } = createRequestHandler({ credentials: FAL_KEY });

```

```
import * as fal from '@fal-ai/serverless-client';
fal.config({  credentials: process.env.FAL_KEY,});
//const output = await fal.run('fal-ai/fast-sdxl', {  input: {    prompt:      'an astronaut riding a horse on mars, hd, dramatic lighting, detailed',  },});
console.log(output);

```

```
import { route } from '@fal-ai/serverless-proxy/nextjs';
export const { GET, POST } = route;

```

Terminal
![](https://7nyt0uhk7sse4zvn.public.blob.vercel-storage.com/docs-assets/static/topics/icons/pnpm.svg)pnpm bun yarn npm
```
pnpm i @fal-ai/client
```

```
yarn add @fal-ai/client
```

```
npm i @fal-ai/client
```

```
bun add @fal-ai/client
```
