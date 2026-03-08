Menu
Menu
# NEXTJS_SAFE_SVG_IMAGES
Last updated March 4, 2025
Conformance is available on [Enterprise plans](https://vercel.com/docs/plans/enterprise)
SVG can do many of the same things that HTML/JS/CSS can, meaning that it can be dangerous to execute SVG as this can lead to vulnerabilities without proper
##  [How to fix](https://vercel.com/docs/conformance/rules/NEXTJS_SAFE_SVG_IMAGES#how-to-fix)[](https://vercel.com/docs/conformance/rules/NEXTJS_SAFE_SVG_IMAGES#how-to-fix)
If you need to serve SVG images with the default Image Optimization API, you can set `dangerouslyAllowSVG` inside your `next.config.js`:
next.config.js
```
module.exports = {
  images: {
    dangerouslyAllowSVG: true,
    contentDispositionType: 'attachment',
    contentSecurityPolicy: "default-src 'self'; script-src 'none'; sandbox;",
  },
};
```

In addition, it is strongly recommended to also set `contentDispositionType` to force the browser to download the image, as well as `contentSecurityPolicy` to prevent scripts embedded in the image from executing.
* * *
Was this helpful?
Send
