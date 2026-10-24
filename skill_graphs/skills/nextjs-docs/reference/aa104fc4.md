## Image files (.jpg, .png, .gif)[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image#image-files-jpg-png-gif)
Use an image file to set a route segment's shared image by placing an `opengraph-image` or `twitter-image` image file in the segment.
Next.js will evaluate the file and automatically add the appropriate tags to your app's `<head>` element.
File convention | Supported file types
---|---
[`opengraph-image`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image#opengraph-image) |  `.jpg`, `.jpeg`, `.png`, `.gif`
[`twitter-image`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image#twitter-image) |  `.jpg`, `.jpeg`, `.png`, `.gif`
[`opengraph-image.alt`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image#opengraph-imagealttxt) | `.txt`
[`twitter-image.alt`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image#twitter-imagealttxt) | `.txt`
> **Good to know** :
> The `twitter-image` file size must not exceed `opengraph-image` file size must not exceed
###  `opengraph-image`[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image#opengraph-image)
Add an `opengraph-image.(jpg|jpeg|png|gif)` image file to any route segment.
<head> output
```
<meta property="og:image" content="<generated>" />
<meta property="og:image:type" content="<generated>" />
<meta property="og:image:width" content="<generated>" />
<meta property="og:image:height" content="<generated>" />
```

###  `twitter-image`[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image#twitter-image)
Add a `twitter-image.(jpg|jpeg|png|gif)` image file to any route segment.
<head> output
```
<meta name="twitter:image" content="<generated>" />
<meta name="twitter:image:type" content="<generated>" />
<meta name="twitter:image:width" content="<generated>" />
<meta name="twitter:image:height" content="<generated>" />
```

###  `opengraph-image.alt.txt`[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image#opengraph-imagealttxt)
Add an accompanying `opengraph-image.alt.txt` file in the same route segment as the `opengraph-image.(jpg|jpeg|png|gif)` image it's alt text.
opengraph-image.alt.txt
```
About Acme
```

<head> output
```
<meta property="og:image:alt" content="About Acme" />
```

###  `twitter-image.alt.txt`[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image#twitter-imagealttxt)
Add an accompanying `twitter-image.alt.txt` file in the same route segment as the `twitter-image.(jpg|jpeg|png|gif)` image it's alt text.
twitter-image.alt.txt
```
About Acme
```

<head> output
```
<meta property="twitter:image:alt" content="About Acme" />
```
