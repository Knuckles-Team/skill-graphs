## Context Object[](https://nextjs.org/docs/pages/api-reference/functions/get-initial-props#context-object)
`getInitialProps` receives a single argument called `context`, which is an object with the following properties:
Name | Description
---|---
`pathname` | Current route, the path of the page in `/pages`
`query` | Query string of the URL, parsed as an object
`asPath` |  `String` of the actual path (including the query) shown in the browser
`req` |
`res` |
`err` | Error object if any error is encountered during the rendering
