## Customizing Plugins[](https://nextjs.org/docs/pages/guides/post-css#customizing-plugins)
> **Warning** : When you define a custom PostCSS configuration file, Next.js **completely disables** the [default behavior](https://nextjs.org/docs/pages/guides/post-css#default-behavior). Be sure to manually configure all the features you need compiled, including `npm install postcss-flexbugs-fixes postcss-preset-env`.
To customize the PostCSS configuration, create a `postcss.config.json` file in the root of your project.
This is the default configuration used by Next.js:
postcss.config.json
```
{
  "plugins": [
    "postcss-flexbugs-fixes",
    [
      "postcss-preset-env",
      {
        "autoprefixer": {
          "flexbox": "no-2009"
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

> **Good to know** : Next.js also allows the file to be named `.postcssrc.json`, or, to be read from the `postcss` key in `package.json`.
It is also possible to configure PostCSS with a `postcss.config.js` file, which is useful when you want to conditionally include plugins based on environment:
postcss.config.js
```
module.exports = {
  plugins:
    process.env.NODE_ENV === 'production'
      ? [
          'postcss-flexbugs-fixes',
          [
            'postcss-preset-env',
            {
              autoprefixer: {
                flexbox: 'no-2009',
              },
              stage: 3,
              features: {
                'custom-properties': false,
              },
            },
          ],
        ]
      : [
          // No transformations in development
        ],
}
```

> **Good to know** : Next.js also allows the file to be named `.postcssrc.js`.
Do **not use`require()`** to import the PostCSS Plugins. Plugins must be provided as strings.
> **Good to know** : If your `postcss.config.js` needs to support other non-Next.js tools in the same project, you must use the interoperable object-based format instead:
> ```
module.exports = {
  plugins: {
    'postcss-flexbugs-fixes': {},
    'postcss-preset-env': {
      autoprefixer: {
        flexbox: 'no-2009',
      },
      stage: 3,
      features: {
        'custom-properties': false,
      },
    },
  },
}
```

Was this helpful?
Send
* * *
* * *
#### Resources
[Docs](https://nextjs.org/docs)[Support Policy](https://nextjs.org/support-policy)[Learn](https://nextjs.org/learn)[Showcase](https://nextjs.org/showcase)[Blog](https://nextjs.org/blog)[Team](https://nextjs.org/team)[Next.js Conf](https://nextjs.org/conf)[Evals](https://nextjs.org/evals)
#### More
[Telemetry](https://nextjs.org/telemetry)[Governance](https://nextjs.org/governance)
#### About Vercel
#### Legal
Cookie Preferences
#### Subscribe to our newsletter
Stay updated on new releases and features, guides, and case studies.
Subscribe
© 2026 Vercel, Inc.
* * *
* * *
