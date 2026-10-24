##  [`beforeSend`](https://vercel.com/docs/query#beforesend)[](https://vercel.com/docs/query#beforesend)
With the `beforeSend` function, you can modify or filter out the event data before it's sent to Vercel. You can use this to redact sensitive data or to avoid sending certain events.
For instance, if you wish to ignore events from a specific URL or modify them, you can do so with this option.
```
// Example usage of beforeSend
beforeSend: (data) => {
  if (data.url.includes('/sensitive-path')) {
    return null; // this will ignore the event
  }
  return data; // this will send the event as is
};
```
