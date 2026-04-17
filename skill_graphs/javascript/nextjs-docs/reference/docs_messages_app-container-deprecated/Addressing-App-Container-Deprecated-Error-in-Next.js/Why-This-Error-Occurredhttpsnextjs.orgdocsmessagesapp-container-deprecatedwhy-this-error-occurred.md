## Why This Error Occurred[](https://nextjs.org/docs/messages/app-container-deprecated#why-this-error-occurred)
The "App Container Deprecated" error usually occurs when you are using the `<Container>` component in your custom `<App>` (`pages/_app.js`). Prior to version `9.0.4` of Next.js, the `<Container>` component was used to handle scrolling to hashes.
From version `9.0.4` onwards, this functionality was moved up the component tree, rendering the `<Container>` component unnecessary in your custom `<App>`.
