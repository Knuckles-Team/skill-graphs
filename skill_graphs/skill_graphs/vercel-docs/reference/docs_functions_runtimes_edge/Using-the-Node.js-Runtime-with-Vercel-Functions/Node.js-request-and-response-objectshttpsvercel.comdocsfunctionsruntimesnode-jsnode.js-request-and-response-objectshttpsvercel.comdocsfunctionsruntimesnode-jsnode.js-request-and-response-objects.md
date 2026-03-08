##  [Node.js request and response objects](https://vercel.com/docs/functions/runtimes/node-js#node.js-request-and-response-objects)[](https://vercel.com/docs/functions/runtimes/node-js#node.js-request-and-response-objects)
Each request to a Node.js Vercel Function gives access to Request and Response objects. These objects are the
###  [Node.js helpers](https://vercel.com/docs/functions/runtimes/node-js#node.js-helpers)[](https://vercel.com/docs/functions/runtimes/node-js#node.js-helpers)
Vercel additionally provides helper methods inside of the Request and Response objects passed to Node.js Vercel Functions. These methods are:
method | description | object
---|---|---
`request.query` | An object containing the request's `{}` if the request does not have a query string. | Request
`request.cookies` | An object containing the cookies sent by the request, or `{}` if the request contains no cookies. | Request
[`request.body`](https://vercel.com/docs/functions/runtimes/node-js#node.js-request-and-response-objects) | An object containing the body sent by the request, or `null` if no body is sent. | Request
`response.status(code)` | A function to set the status code sent with the response where `code` must be a valid `response` for chaining. | Response
`response.send(body)` | A function to set the content of the response where `body` can be a `string`, an `object` or a `Buffer`. | Response
`response.json(obj)` | A function to send a JSON response where `obj` is the JSON object to send. | Response
`response.redirect(url)` | A function to redirect to the URL derived from the specified path with status code "307 Temporary Redirect". | Response
`response.redirect(statusCode, url)` | A function to redirect to the URL derived from the specified path, with specified  | Response
The following Node.js Vercel Function example showcases the use of `request.query`, `request.cookies` and `request.body` helpers:
api/hello.ts
```
import { VercelRequest, VercelResponse } from "@vercel/node";

module.exports = (request: VercelRequest, response: VercelResponse) => {
  let who = 'anonymous';

  if (request.body && request.body.who) {
    who = request.body.who;
  } else if (request.query.who) {
    who = request.query.who;
  } else if (request.cookies.who) {
    who = request.cookies.who;
  }

  response.status(200).send(`Hello ${who}!`);
};
```

Example Node.js Vercel Function using the `request.query`, `request.cookies`, and `request.body` helpers. It returns greetings for the user specified using `request.send()`.
If needed, you can opt-out of Vercel providing `helpers` using [advanced configuration](https://vercel.com/docs/functions/runtimes/node-js#disabling-helpers-for-node.js).
###  [Request body](https://vercel.com/docs/functions/runtimes/node-js#request-body)[](https://vercel.com/docs/functions/runtimes/node-js#request-body)
We populate the `request.body` property with a parsed version of the content sent with the request when possible.
We follow a set of rules on the `Content-type` header sent by the request to do so:
`Content-Type` header | Value of `request.body`
---|---
No header | `undefined`
`application/json` | An object representing the parsed JSON sent by the request.
`application/x-www-form-urlencoded` | An object representing the parsed data sent by with the request.
`text/plain` | A string containing the text sent by the request.
`application/octet-stream` | A
With the `request.body` helper, you can build applications without extra dependencies or having to parse the content of the request manually.
The `request.body` helper is set using a
When the request body contains malformed JSON, accessing `request.body` will throw an error. You can catch that error by wrapping `request.body` with
api/hello.ts
```
try {
  request.body;
} catch (error) {
  return response.status(400).json({ error: 'My custom 400 error' });
}
```

Catching the error thrown by `request.body` with
###  [Cancelled Requests](https://vercel.com/docs/functions/runtimes/node-js#cancelled-requests)[](https://vercel.com/docs/functions/runtimes/node-js#cancelled-requests)
Request cancellation must be enabled on a per-route basis. See [Functions API Reference](https://vercel.com/docs/functions/functions-api-reference#cancel-requests) for more information.
You can listen for the `error` event on the request object to detect request cancellation:
api/cancel.ts
```
import { VercelRequest, VercelResponse } from '@vercel/node';

export default async (request: VercelRequest, response: VercelResponse) => {
  let cancelled = false;
  request.on('error', (error) => {
    if (error.message === 'aborted') {
      console.log('request aborted');
    }
    cancelled = true;
  });

  response.writeHead(200);

  for (let i = 1; i < 5; i++) {
    if (cancelled) {
      // the response must be explicitly ended
      response.end();
      return;
    }

    response.write(`Count: ${i}\n`);

    await new Promise((resolve) => setTimeout(resolve, 1000));
  }

  response.end('All done!');
};
```
