## Why This Error Occurred[](https://nextjs.org/docs/messages/no-title-in-document-head#why-this-error-occurred)
A `<title>` element was defined within the `Head` component imported from `next/document`, which should only be used for any `<head>` code that is common for all pages. Title tags should be defined at the page-level using `next/head` instead.
