## Why This Error Occurred[](https://nextjs.org/docs/messages/no-async-client-component#why-this-error-occurred)
The error occurs when you try to define a Client Component as an async function. React Client Components
```
'use client'

// This will cause an error
async function ClientComponent() {
  // ...
}
```
