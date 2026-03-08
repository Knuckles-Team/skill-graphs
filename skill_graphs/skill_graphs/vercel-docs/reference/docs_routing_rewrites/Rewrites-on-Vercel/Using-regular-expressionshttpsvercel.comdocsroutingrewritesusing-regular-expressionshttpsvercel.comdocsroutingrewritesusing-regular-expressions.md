##  [Using regular expressions](https://vercel.com/docs/routing/rewrites#using-regular-expressions)[](https://vercel.com/docs/routing/rewrites#using-regular-expressions)
For more complex patterns, you can use regular expressions with capture groups:
```
{
  "rewrites": [
    {
      "source": "^/articles/(\\d{4})/(\\d{2})/(.+)$",
      "destination": "/archive?year=$1&month=$2&slug=$3"
    }
  ]
}
```

This converts `/articles/2023/05/hello-world` to `/archive?year=2023&month=05&slug=hello-world`.
You can also use named capture groups:
```
{
  "rewrites": [
    {
      "source": "^/products/(?<category>[a-z]+)/(?<id>\\d+)$",
      "destination": "/shop?category=$category&item=$id"
    }
  ]
}
```

This converts `/products/shirts/123` to `/shop?category=shirts&item=123`.
