## CacheEntry Type[](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheHandlers#cacheentry-type)
The
```
interface CacheEntry {
  value: ReadableStream<Uint8Array>
  tags: string[]
  stale: number
  timestamp: number
  expire: number
  revalidate: number
}
```

Property | Type | Description
---|---|---
`value` | `ReadableStream<Uint8Array>` | The cached data as a stream.
`tags` | `string[]` | Cache tags (excluding soft tags).
`stale` | `number` | Duration in seconds for client-side staleness.
`timestamp` | `number` | When the entry was created (timestamp in milliseconds).
`expire` | `number` | How long the entry is allowed to be used (in seconds).
`revalidate` | `number` | How long until the entry should be revalidated (in seconds).
> **Good to know** :
>   * The `value` is a
>   * If the stream errors with partial data, your handler must decide whether to keep the partial cache or discard it.
>
