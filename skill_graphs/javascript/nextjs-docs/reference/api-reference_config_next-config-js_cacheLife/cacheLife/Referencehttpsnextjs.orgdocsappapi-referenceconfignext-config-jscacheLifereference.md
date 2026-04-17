## Reference[](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheLife#reference)
The configuration object has key values with the following format:
**Property** | **Value** | **Description** | **Requirement**
---|---|---|---
`stale` | `number` | Duration the client should cache a value without checking the server. | Optional
`revalidate` | `number` | Frequency at which the cache should refresh on the server; stale values may be served while revalidating. | Optional
`expire` | `number` | Maximum duration for which a value can remain stale before switching to dynamic. | Optional - Must be longer than `revalidate`
