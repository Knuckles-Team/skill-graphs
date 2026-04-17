## Customizing Target Browsers[](https://nextjs.org/docs/pages/guides/post-css#customizing-target-browsers)
Next.js allows you to configure the target browsers (for
To customize browserslist, create a `browserslist` key in your `package.json` like so:
package.json
```
{
  "browserslist": [">0.3%", "not dead", "not op_mini all"]
}
```

You can use the
