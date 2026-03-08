## Why This Error Occurred[](https://nextjs.org/docs/messages/missing-suspense-with-csr-bailout#why-this-error-occurred)
Reading search parameters through `useSearchParams()` without a Suspense boundary will opt the entire page into client-side rendering. This could cause your page to be blank until the client-side JavaScript has loaded.
