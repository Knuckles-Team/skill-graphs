## Default Behavior[](https://nextjs.org/docs/pages/guides/post-css#default-behavior)
Next.js compiles CSS for its [built-in CSS support](https://nextjs.org/docs/app/getting-started/css) using PostCSS.
Out of the box, with no configuration, Next.js compiles CSS with the following transformations:
  * New CSS features are automatically compiled for Internet Explorer 11 compatibility:


By default, **not compiled** for IE11 support.
To compile
```
/* autoprefixer grid: autoplace */
```

You can also enable IE11 support for ["Customizing Plugins"](https://nextjs.org/docs/pages/guides/post-css#customizing-plugins) below for more information.
Click to view the configuration to enable CSS Grid Layout
postcss.config.json
```
{
  "plugins": [
    "postcss-flexbugs-fixes",
    [
      "postcss-preset-env",
      {
        "autoprefixer": {
          "flexbox": "no-2009",
          "grid": "autoplace"
        },
        "stage": 3,
        "features": {
          "custom-properties": false
        }
      }
    ]
  ]
}
```

CSS variables are not compiled because it is
