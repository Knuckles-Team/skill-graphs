##  `cookies`[](https://nextjs.org/docs/app/api-reference/functions/next-response#cookies)
Read or mutate the
###  `set(name, value)`[](https://nextjs.org/docs/app/api-reference/functions/next-response#setname-value)
Given a name, set a cookie with the given value on the response.
```
// Given incoming request /home
let response = NextResponse.next()
// Set a cookie to hide the banner
response.cookies.set('show-banner', 'false')
// Response will have a `Set-Cookie:show-banner=false;path=/home` header
return response
```

###  `get(name)`[](https://nextjs.org/docs/app/api-reference/functions/next-response#getname)
Given a cookie name, return the value of the cookie. If the cookie is not found, `undefined` is returned. If multiple cookies are found, the first one is returned.
```
// Given incoming request /home
let response = NextResponse.next()
// { name: 'show-banner', value: 'false', Path: '/home' }
response.cookies.get('show-banner')
```

###  `getAll()`[](https://nextjs.org/docs/app/api-reference/functions/next-response#getall)
Given a cookie name, return the values of the cookie. If no name is given, return all cookies on the response.
```
// Given incoming request /home
let response = NextResponse.next()
// [
//   { name: 'experiments', value: 'new-pricing-page', Path: '/home' },
//   { name: 'experiments', value: 'winter-launch', Path: '/home' },
// ]
response.cookies.getAll('experiments')
// Alternatively, get all cookies for the response
response.cookies.getAll()
```

###  `has(name)`[](https://nextjs.org/docs/app/api-reference/functions/next-response#hasname)
Given a cookie name, return `true` if the cookie exists on the response.
```
// Given incoming request /home
let response = NextResponse.next()
// Returns true if cookie exists, false if it does not
response.cookies.has('experiments')
```

###  `delete(name)`[](https://nextjs.org/docs/app/api-reference/functions/next-response#deletename)
Given a cookie name, delete the cookie from the response.
```
// Given incoming request /home
let response = NextResponse.next()
// Returns true for deleted, false if nothing is deleted
response.cookies.delete('experiments')
```
