## Why This Error Occurred[](https://nextjs.org/docs/messages/next-dynamic-modules#why-this-error-occurred)
The ability to load multiple modules at once has been deprecated in `next/dynamic` to be closer to React's implementation (`React.lazy` and `Suspense`).
Updating code that relies on this behavior is relatively straightforward! We've provided an example of a before/after to help you migrate your application:
