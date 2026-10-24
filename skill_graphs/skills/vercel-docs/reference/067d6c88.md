##  [Tracking an event with custom data](https://vercel.com/docs/notebooks#tracking-an-event-with-custom-data)[](https://vercel.com/docs/notebooks#tracking-an-event-with-custom-data)
You can also pass custom data along with an event. To do so, pass an object with key-value pairs as the second argument to `track()`:
component.ts
TypeScript
TypeScript JavaScript Bash
```
track('Signup', { location: 'footer' });
track('Purchase', { productName: 'Shoes', price: 49.99 });
```

This tracks a "Signup" event that occurred in the "footer" location. The second event tracks a "Purchase" event with product name and a price.
