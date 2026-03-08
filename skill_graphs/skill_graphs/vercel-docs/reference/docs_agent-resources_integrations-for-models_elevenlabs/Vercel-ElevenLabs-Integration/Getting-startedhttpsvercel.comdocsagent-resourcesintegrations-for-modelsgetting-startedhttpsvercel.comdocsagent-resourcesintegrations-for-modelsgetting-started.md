##  [Getting started](https://vercel.com/docs/agent-resources/integrations-for-models#getting-started)[](https://vercel.com/docs/agent-resources/integrations-for-models#getting-started)
The Vercel ElevenLabs integration can be accessed through the AI tab on your [Vercel dashboard](https://vercel.com/dashboard).
###  [Prerequisites](https://vercel.com/docs/agent-resources/integrations-for-models#prerequisites)[](https://vercel.com/docs/agent-resources/integrations-for-models#prerequisites)
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



###  [Add the provider to your project](https://vercel.com/docs/agent-resources/integrations-for-models#add-the-provider-to-your-project)[](https://vercel.com/docs/agent-resources/integrations-for-models#add-the-provider-to-your-project)
####  [Using the dashboard](https://vercel.com/docs/agent-resources/integrations-for-models#using-the-dashboard)[](https://vercel.com/docs/agent-resources/integrations-for-models#using-the-dashboard)
  1. Navigate to the AI tab in your [Vercel dashboard](https://vercel.com/dashboard)
  2. Select ElevenLabs from the list of providers, and press Add
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
pnpm i @elevenlabs/elevenlabs-js
```

```
yarn add @elevenlabs/elevenlabs-js
```

```
npm i @elevenlabs/elevenlabs-js
```

```
bun add @elevenlabs/elevenlabs-js
```

  10. Connect your project using the code below:
index.ts
Other frameworks
```
import { ElevenLabsClient, play } from '@elevenlabs/elevenlabs-js';
const elevenlabs = new ElevenLabsClient({  apiKey: 'YOUR_API_KEY', // Defaults to process.env.ELEVENLABS_API_KEY});
const audio = await elevenlabs.textToSpeech.convert('JBFqnCBsd6RMkjVDRZzb', {  text: 'The first move is what sets everything in motion.',  modelId: 'eleven_multilingual_v2',});
await play(audio);

```
