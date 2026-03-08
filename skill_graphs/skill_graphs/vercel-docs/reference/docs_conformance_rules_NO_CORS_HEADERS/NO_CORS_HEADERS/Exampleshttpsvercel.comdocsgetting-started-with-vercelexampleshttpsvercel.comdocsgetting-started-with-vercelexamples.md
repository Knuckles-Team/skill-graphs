##  [Examples](https://vercel.com/docs/getting-started-with-vercel#examples)[](https://vercel.com/docs/getting-started-with-vercel#examples)
The examples below are common approaches to settings CORS headers in JavaScript applications. All of these examples will be caught by this rule.
```
response.headers.set('Access-Control-Allow-Origin', '*');

const headers = {
  'Access-Control-Allow-Credentials': true,
};

const options = {
  headers: [
    {
      key: 'Access-Control-Max-Age',
      value: 600,
    },
  ],
};

const headers = new Headers();
headers.append('Access-Control-Allow-Methods', '*');
```

Additionally, this rule will catch partial matches, such as a template literal. In this example, the rule will match the `"Access-Control-"` part of the template literal.
```
const headers = new Headers();
headers.append(`Access-Control-${HEADER_TYPE}`, '*');
```
