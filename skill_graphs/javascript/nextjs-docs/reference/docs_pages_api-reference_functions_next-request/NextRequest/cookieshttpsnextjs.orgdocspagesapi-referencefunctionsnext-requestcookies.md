##  `cookies`[](https://nextjs.org/docs/pages/api-reference/functions/next-request#cookies)
Read or mutate the
###  `set(name, value)`[](https://nextjs.org/docs/pages/api-reference/functions/next-request#setname-value)
Given a name, set a cookie with the given value on the request.
```
// Given incoming request /home
// Set a cookie to hide the banner
// request will have a `Set-Cookie:show-banner=false;path=/home` header
request.cookies.set('show-banner', 'false')
```

###  `get(name)`[](https://nextjs.org/docs/pages/api-reference/functions/next-request#getname)
Given a cookie name, return the value of the cookie. If the cookie is not found, `undefined` is returned. If multiple cookies are found, the first one is returned.
```
// Given incoming request /home
// { name: 'show-banner', value: 'false', Path: '/home' }
request.cookies.get('show-banner')
```

###  `getAll()`[](https://nextjs.org/docs/pages/api-reference/functions/next-request#getall)
Given a cookie name, return the values of the cookie. If no name is given, return all cookies on the request.
```
// Given incoming request /home
// [
//   { name: 'experiments', value: 'new-pricing-page', Path: '/home' },
//   { name: 'experiments', value: 'winter-launch', Path: '/home' },
// ]
request.cookies.getAll('experiments')
// Alternatively, get all cookies for the request
request.cookies.getAll()
```

###  `delete(name)`[](https://nextjs.org/docs/pages/api-reference/functions/next-request#deletename)
Given a cookie name, delete the cookie from the request.
```
// Returns true for deleted, false is nothing is deleted
request.cookies.delete('experiments')
```

###  `has(name)`[](https://nextjs.org/docs/pages/api-reference/functions/next-request#hasname)
Given a cookie name, return `true` if the cookie exists on the request.
```
// Returns true if cookie exists, false if it does not
request.cookies.has('experiments')
```

###  `clear()`[](https://nextjs.org/docs/pages/api-reference/functions/next-request#clear)
Remove all cookies from the request.
```
request.cookies.clear()
```
