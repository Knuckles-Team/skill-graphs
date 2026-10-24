##  [Middleware](https://vercel.com/docs/getting-started-with-vercel#middleware)[](https://vercel.com/docs/getting-started-with-vercel#middleware)
Middleware is code that executes before a request gets processed. Because Middleware runs before the cache, it's an effective way of providing personalization to statically generated content.
Nuxt has two forms of Middleware:
  * [Server middleware](https://vercel.com/docs/getting-started-with-vercel#nuxt-server-middleware-on-vercel)
  * [Route middleware](https://vercel.com/docs/getting-started-with-vercel#nuxt-route-middleware-on-vercel)


###  [Nuxt server middleware on Vercel](https://vercel.com/docs/getting-started-with-vercel#nuxt-server-middleware-on-vercel)[](https://vercel.com/docs/getting-started-with-vercel#nuxt-server-middleware-on-vercel)
In Nuxt, modules defined in `/server/middleware` will get deployed as
Server middleware is best used to read data from or add data to a request's `context`. Doing so allows you to handle authentication or check a request's params, headers, url,
The following example demonstrates Middleware that:
  * Checks for a cookie
  * Tries to fetch user data from a database based on the request
  * Adds the user's data and the cookie data to the request's context


server/middleware/auth.ts
TypeScript
TypeScript JavaScript Bash
```
import { getUserFromDBbyCookie } from 'some-orm-package';

export default defineEventHandler(async (event) => {
  // The getCookie method is available to all
  // Nuxt routes by default. No need to import.
  const token = getCookie(event, 'session_token');

  // getUserFromDBbyCookie is a placeholder
  // made up for this example. You can fetch
  // data from wherever you want here
  const { user } = await getUserFromDBbyCookie(event.request);

  if (user) {
    event.context.user = user;
    event.context.session_token = token;
  }
});
```

You could then access that data in a page on the frontend with the `useRequestEvent` will return `undefined`.
The following example demonstrates a page fetching data with `useRequestEvent`:
example.vue
TypeScript
TypeScript JavaScript Bash
```
<script>
  const event = useRequestEvent();
  const user = ref(event.context?.user);
</script>

<template>
    <div v-if="user">
      <h1>Hello, {{ user.name }}!</h1>
    </div>
    <div v-else>
      <p>Authentication failed!</p>
    </div>
</template>
```

###  [Nuxt route middleware on Vercel](https://vercel.com/docs/getting-started-with-vercel#nuxt-route-middleware-on-vercel)[](https://vercel.com/docs/getting-started-with-vercel#nuxt-route-middleware-on-vercel)
Nuxt's route middleware runs before navigating to a particular route. While server middleware runs in Nuxt's
Route middleware is best used when you want to do things that server middleware can't, such as redirecting users, or preventing them from navigating to a route.
The following example demonstrates route middleware that redirects users to a secret route:
middleware/redirect.ts
TypeScript
TypeScript JavaScript Bash
```
export default defineNuxtRouteMiddleware((to) => {
  console.log(
    `Heading to ${to.path} - but I think we should go somewhere else...`,
  );

  return navigateTo('/secret');
});
```

By default, route middleware code will only run on pages that specify them. To do so, within the `<script>` tag for a page, you must call the `definePageMeta` method, passing an object with `middleware: 'middleware-filename'` set as an option.
The following example demonstrates a page that runs the above redirect middleware:
redirect.vue
TypeScript
TypeScript JavaScript Bash
```
<script>
definePageMeta({
  middleware: 'redirect'
})
</script>

<template>
  <div>
    You should never see this page
  </div>
</template>
```

To make a middleware global, add the `.global` suffix before the file extension. The following is an example of a basic global middleware file:
example-middleware.global.ts
TypeScript
TypeScript JavaScript Bash
```
export default defineNuxtRouteMiddleware(() => {
  console.log('running global middleware');
});
```

Middleware with Nuxt on Vercel enables you to:
  * Redirect users, and prevent navigation to routes
  * Run authentication checks on the server, and pass results to the frontend
  * Scope middleware to specific routes, or run it on all routes
