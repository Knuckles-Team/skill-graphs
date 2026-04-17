## Image files (.ico, .jpg, .png)[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons#image-files-ico-jpg-png)
Use an image file to set an app icon by placing a `favicon`, `icon`, or `apple-icon` image file within your `/app` directory. The `favicon` image can only be located in the top level of `app/`.
Next.js will evaluate the file and automatically add the appropriate tags to your app's `<head>` element.
File convention | Supported file types | Valid locations
---|---|---
[`favicon`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons#favicon) | `.ico` | `app/`
[`icon`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons#icon) |  `.ico`, `.jpg`, `.jpeg`, `.png`, `.svg` | `app/**/*`
[`apple-icon`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons#apple-icon) |  `.jpg`, `.jpeg`, `.png` | `app/**/*`
###  `favicon`[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons#favicon)
Add a `favicon.ico` image file to the root `/app` route segment.
<head> output
```
<link rel="icon" href="/favicon.ico" sizes="any" />
```

###  `icon`[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons#icon)
Add an `icon.(ico|jpg|jpeg|png|svg)` image file.
<head> output
```
<link
  rel="icon"
  href="/icon?<generated>"
  type="image/<generated>"
  sizes="<generated>"
/>
```

###  `apple-icon`[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons#apple-icon)
Add an `apple-icon.(jpg|jpeg|png)` image file.
<head> output
```
<link
  rel="apple-touch-icon"
  href="/apple-icon?<generated>"
  type="image/<generated>"
  sizes="<generated>"
/>
```

> **Good to know** :
>   * You can set multiple icons by adding a number suffix to the file name. For example, `icon1.png`, `icon2.png`, etc. Numbered files will sort lexically.
>   * Favicons can only be set in the root `/app` segment. If you need more granularity, you can use [`icon`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons#icon).
>   * The appropriate `<link>` tags and attributes such as `rel`, `href`, `type`, and `sizes` are determined by the icon type and metadata of the evaluated file.
>   * For example, a 32 by 32px `.png` file will have `type="image/png"` and `sizes="32x32"` attributes.
>   * `sizes="any"` is added to icons when the extension is `.svg` or the image size of the file is not determined. More details in this
>
