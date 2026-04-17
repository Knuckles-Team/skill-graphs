##  [Create your first Vercel Function](https://vercel.com/docs/functions#create-your-first-vercel-function)[](https://vercel.com/docs/functions#create-your-first-vercel-function)
Copy the code below to create your first function:
api/hello.ts
TypeScript JavaScript
```
export default {
  fetch(request: Request) {
    return new Response('Hello from Vercel!');
  },
};
```

```
export default {
  fetch(request) {
    return new Response('Hello from Vercel!');
  },
};
```

While using `fetch` is the recommended way to create a Vercel Function, you can still use HTTP methods like `GET` and `POST`.
app/api/hello/route.ts
TypeScript JavaScript
Next.js (/app) Next.js (/pages) Other frameworks
```
export function GET(request: Request) {
  return new Response('Hello from Vercel!');
}
```

```
export function GET(request) {
  return new Response('Hello from Vercel!');
}
```

```
export function GET(request: Request) {
  return new Response('Hello from Vercel!');
}
```

```
export function GET(request) {
  return new Response('Hello from Vercel!');
}
```

```
export function GET(request: Request) {
  return new Response('Hello from Vercel!');
}
```

```
export function GET(request) {
  return new Response('Hello from Vercel!');
}
```

To learn more, see the [quickstart](https://vercel.com/docs/functions/quickstart) or [deploy a template](https://vercel.com/templates).
