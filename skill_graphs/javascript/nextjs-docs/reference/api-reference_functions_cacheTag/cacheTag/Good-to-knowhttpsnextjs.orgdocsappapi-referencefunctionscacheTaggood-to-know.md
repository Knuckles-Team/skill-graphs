## Good to know[](https://nextjs.org/docs/app/api-reference/functions/cacheTag#good-to-know)
  * **Idempotent Tags** : Applying the same tag multiple times has no additional effect.
  * **Multiple Tags** : You can assign multiple tags to a single cache entry by passing multiple string values to `cacheTag`.


```
cacheTag('tag-one', 'tag-two')
```

  * **Limits** : The max length for a custom tag is 256 characters and the max tag items is 128.
