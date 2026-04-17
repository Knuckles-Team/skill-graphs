# use cache
Last updated February 27, 2026
The `use cache` directive allows you to mark a route, React component, or a function as cacheable. It can be used at the top of a file to indicate that all exports in the file should be cached, or inline at the top of function or component to cache the return value.
> **Good to know:**
>   * To use cookies or headers, read them outside cached scopes and pass values as arguments. This is the preferred pattern.
>   * If the in-memory cache isn't sufficient for runtime data, [`'use cache: remote'`](https://nextjs.org/docs/app/api-reference/directives/use-cache-remote) allows platforms to provide a dedicated cache handler, though it requires a network roundtrip to check the cache and typically incurs platform fees.
>   * For compliance requirements or when you can't refactor to pass runtime data as arguments to a `use cache` scope, see [`'use cache: private'`](https://nextjs.org/docs/app/api-reference/directives/use-cache-private).
>
