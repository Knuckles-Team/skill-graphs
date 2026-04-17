##  [Reading and writing files](https://vercel.com/docs/getting-started-with-vercel#reading-and-writing-files)[](https://vercel.com/docs/getting-started-with-vercel#reading-and-writing-files)
You can read and write server files with Nuxt on Vercel. One way to do this is by using Nitro with Vercel Functions and a Redis driver such as the `server/assets` get included by default.
To access server assets, you can use Nitro's
server/api/storage.ts
TypeScript
TypeScript JavaScript Bash
```
export default defineEventHandler(async () => {
  // https://nitro.unjs.io/guide/assets#server-assets
  const assets = useStorage('assets:server');
  const users = await assets.getItem('users.json');
  return {
    users,
  };
});
```

To write files, mount
First, [install Upstash Redis from the Vercel Marketplace](https://vercel.com/marketplace/upstash) to get your Redis credentials.
Then update your `nuxt.config.ts` file:
nuxt.config.ts
TypeScript
TypeScript JavaScript Bash
```
export default defineNuxtConfig({
  $production: {
    nitro: {
      storage: {
        data: { driver: 'upstash' },
      },
    },
  },
});
```

Use with the storage API.
server/api/storage.ts
TypeScript
TypeScript JavaScript Bash
```
export default defineEventHandler(async (event) => {
  const dataStorage = useStorage('data');
  await dataStorage.setItem('hello', 'world');
  return {
    hello: await dataStorage.getItem('hello'),
  };
});
```
