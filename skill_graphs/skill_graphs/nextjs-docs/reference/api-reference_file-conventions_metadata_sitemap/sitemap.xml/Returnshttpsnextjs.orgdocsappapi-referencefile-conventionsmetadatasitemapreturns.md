## Returns[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/sitemap#returns)
The default function exported from `sitemap.(xml|ts|js)` should return an array of objects with the following properties:
```
type Sitemap = Array<{
  url: string
  lastModified?: string | Date
  changeFrequency?:
    | 'always'
    | 'hourly'
    | 'daily'
    | 'weekly'
    | 'monthly'
    | 'yearly'
    | 'never'
  priority?: number
  alternates?: {
    languages?: Languages<string>
  }
}>
```
