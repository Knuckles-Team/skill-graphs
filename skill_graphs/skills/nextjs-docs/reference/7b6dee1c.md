## How `use cache` works[](https://nextjs.org/docs/app/api-reference/directives/use-cache#how-use-cache-works)
### Cache keys[](https://nextjs.org/docs/app/api-reference/directives/use-cache#cache-keys)
A cache entry's key is generated using a serialized version of its inputs, which includes:
  1. **Build ID** - Unique per build, changing this invalidates all cache entries
  2. **Function ID** - A secure hash of the function's location and signature in the codebase
  3. **Serializable arguments** - Props (for components) or function arguments
  4. **HMR refresh hash** (development only) - Invalidates cache on hot module replacement


When a cached function references variables from outer scopes, those variables are automatically captured and bound as arguments, making them part of the cache key.
lib/data.ts
```
async function Component({ userId }: { userId: string }) {
  const getData = async (filter: string) => {
    'use cache'
    // Cache key includes both userId (from closure) and filter (argument)
    return fetch(`/api/users/${userId}/data?filter=${filter}`)
  }

  return getData('active')
}
```

In the snippet above, `userId` is captured from the outer scope and `filter` is passed as an argument, so both become part of the `getData` function's cache key. This means different user and filter combinations will have separate cache entries.
