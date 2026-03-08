##  [Getting started](https://vercel.com/docs/agent-resources/integrations-for-models/replicate#getting-started)[](https://vercel.com/docs/agent-resources/integrations-for-models/replicate#getting-started)
The Vercel Replicate integration can be accessed through the AI tab on your [Vercel dashboard](https://vercel.com/dashboard).
###  [Prerequisites](https://vercel.com/docs/agent-resources/integrations-for-models/replicate#prerequisites)[](https://vercel.com/docs/agent-resources/integrations-for-models/replicate#prerequisites)
To follow this guide, you'll need the following:
  * An existing [Vercel project](https://vercel.com/docs/projects/overview#creating-a-project)
  * The latest version of [Vercel CLI](https://vercel.com/docs/cli#installing-vercel-cli)
Terminal
![](https://7nyt0uhk7sse4zvn.public.blob.vercel-storage.com/docs-assets/static/topics/icons/pnpm.svg)pnpm bun yarn npm
```
pnpm i -g vercel@latest
```

```
yarn global add vercel@latest
```

```
npm i -g vercel@latest
```

```
bun add -g vercel@latest
```



###  [Add the provider to your project](https://vercel.com/docs/agent-resources/integrations-for-models/replicate#add-the-provider-to-your-project)[](https://vercel.com/docs/agent-resources/integrations-for-models/replicate#add-the-provider-to-your-project)
####  [Using the dashboard](https://vercel.com/docs/agent-resources/integrations-for-models/replicate#using-the-dashboard)[](https://vercel.com/docs/agent-resources/integrations-for-models/replicate#using-the-dashboard)
  1. Navigate to the AI tab in your [Vercel dashboard](https://vercel.com/dashboard)
  2. Select Replicate from the list of providers, and press Add
  3. Review the provider information, and press Add Provider
  4. You can now select which projects the provider will have access to. You can choose from All Projects or Specific Projects
     * If you select Specific Projects, you'll be prompted to select the projects you want to connect to the provider. The list will display projects associated with your scoped team
     * Multiple projects can be selected during this step
  5. Select the Connect to Project button
  6. You'll be redirected to the provider's website to complete the connection process
  7. Once the connection is complete, you'll be redirected back to the Vercel dashboard, and the provider integration dashboard page. From here you can manage your provider settings, view usage, and more
  8. Pull the environment variables into your project using [Vercel CLI](https://vercel.com/docs/cli/env)
terminal
```
vercel env pull
```

  9. Install the providers package
Terminal
![](https://7nyt0uhk7sse4zvn.public.blob.vercel-storage.com/docs-assets/static/topics/icons/pnpm.svg)pnpm bun yarn npm
```
pnpm i replicate
```

```
yarn add replicate
```

```
npm i replicate
```

```
bun add replicate
```

  10. Connect your project using the code below:
app/api/predictions/route.ts
Next.js (/app) Next.js (/pages) SvelteKit Other frameworks
```
import { NextResponse } from 'next/server';import Replicate from 'replicate';
const replicate = new Replicate({  auth: process.env.REPLICATE_API_TOKEN,});
// In production and preview deployments (on Vercel), the VERCEL_URL environment variable is set.// In development (on your local machine), the NGROK_HOST environment variable is set.const WEBHOOK_HOST = process.env.VERCEL_URL  ? `https://${process.env.VERCEL_URL}`  : process.env.NGROK_HOST;
export async function POST(request) {  if (!process.env.REPLICATE_API_TOKEN) {    throw new Error(      'The REPLICATE_API_TOKEN environment variable is not set. See README.md for instructions on how to set it.',    );  }
  const { prompt } = await request.json();
  const options = {    version: '8beff3369e81422112d93b89ca01426147de542cd4684c244b673b105188fe5f',    input: { prompt },  };
  if (WEBHOOK_HOST) {    options.webhook = `${WEBHOOK_HOST}/api/webhooks`;    options.webhook_events_filter = ['start', 'completed'];  }
  // A prediction is the result you get when you run a model, including the input, output, and other details  const prediction = await replicate.predictions.create(options);
  if (prediction?.error) {    return NextResponse.json({ detail: prediction.error }, { status: 500 });  }
  return NextResponse.json(prediction, { status: 201 });}
// app/api/predictions/[id]/route.ts
import { NextResponse } from 'next/server';import Replicate from 'replicate';
const replicate = new Replicate({  auth: process.env.REPLICATE_API_TOKEN,});
// Poll for the prediction's statusexport async function GET(request, { params }) {  const { id } = params;  const prediction = await replicate.predictions.get(id);
  if (prediction?.error) {    return NextResponse.json({ detail: prediction.error }, { status: 500 });  }
  return NextResponse.json(prediction);}

```

```
import Replicate from 'replicate';
const replicate = new Replicate({  auth: process.env.REPLICATE_API_TOKEN,});
export default async function handler(req, res) {  if (!process.env.REPLICATE_API_TOKEN) {    throw new Error(      'The REPLICATE_API_TOKEN environment variable is not set. See README.md for instructions on how to set it.',    );  }
  const prediction = await replicate.predictions.create({    version: '8beff3369e81422112d93b89ca01426147de542cd4684c244b673b105188fe5f',    input: { prompt: req.body.prompt },  });
  if (prediction?.error) {    res.statusCode = 500;    res.end(JSON.stringify({ detail: prediction.error }));    return;  }
  res.statusCode = 201;  res.end(JSON.stringify(prediction));}
// app/api/predictions/[id]/route.ts
import { NextResponse } from 'next/server';import Replicate from 'replicate';
const replicate = new Replicate({  auth: process.env.REPLICATE_API_TOKEN,});
// Poll for the prediction's statusexport default async function handler(req, res) {  const { id } = req.query;  const prediction = await replicate.predictions.get(id);
  if (prediction?.error) {    return NextResponse.json({ detail: prediction.error }, { status: 500 });  }
  return NextResponse.json(prediction);}

```

```
import Replicate from 'replicate';
import { env } from '$env/dynamic/private';
import type { RequestHandler } from './$types';
const replicate = new Replicate({  auth: env.REPLICATE_API_KEY || '',});
export const POST = (async ({ request }) => {  const { prompt } = await request.json();
  const [output] = await replicate.run('black-forest-labs/flux-schnell', {    input: {      prompt,    },  });
  return new Response({ output });}) satisfies RequestHandler;

```

```
import Replicate from 'replicate';
const replicate = new Replicate({  auth: process.env.REPLICATE_API_TOKEN,});
const model = 'black-forest-labs/flux-schnell';const input = {  prompt: 'a cat holding a sign that says hello world',};const output = await replicate.run(model, { input });
console.log(output);

```
