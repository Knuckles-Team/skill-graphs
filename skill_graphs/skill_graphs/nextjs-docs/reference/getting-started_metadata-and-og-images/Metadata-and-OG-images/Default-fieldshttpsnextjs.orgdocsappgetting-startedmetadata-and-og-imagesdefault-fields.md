## Default fields[](https://nextjs.org/docs/app/getting-started/metadata-and-og-images#default-fields)
There are two default `meta` tags that are always added even if a route doesn't define metadata:
  * The
  * The


```
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
```

The other metadata fields can be defined with the `Metadata` object (for [static metadata](https://nextjs.org/docs/app/getting-started/metadata-and-og-images#static-metadata)) or the `generateMetadata` function (for [generated metadata](https://nextjs.org/docs/app/getting-started/metadata-and-og-images#generated-metadata)).
