## Adding Presets and Plugins[](https://nextjs.org/docs/pages/guides/babel#adding-presets-and-plugins)
To start, you only need to define a `.babelrc` file (or `babel.config.js`) in the root directory of your project. If such a file is found, it will be considered as the _source of truth_ , and therefore it needs to define what Next.js needs as well, which is the `next/babel` preset.
Here's an example `.babelrc` file:
.babelrc
```
{
  "presets": ["next/babel"],
  "plugins": []
}
```

You can `next/babel`.
To add presets/plugins **without configuring them** , you can do it this way:
.babelrc
```
{
  "presets": ["next/babel"],
  "plugins": ["@babel/plugin-proposal-do-expressions"]
}
```
