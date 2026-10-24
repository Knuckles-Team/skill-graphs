## Caching[](https://nextjs.org/docs/pages/api-reference/file-conventions/public-folder#caching)
Next.js cannot safely cache assets in the `public` folder because they may change. The default caching headers applied are:
```
Cache-Control: public, max-age=0
```
