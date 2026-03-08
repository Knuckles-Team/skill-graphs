## Experimental Features[](https://nextjs.org/docs/architecture/nextjs-compiler#experimental-features)
### SWC Trace profiling[](https://nextjs.org/docs/architecture/nextjs-compiler#swc-trace-profiling)
You can generate SWC's internal transform traces as chromium's
next.config.js
```
module.exports = {
  experimental: {
    swcTraceProfiling: true,
  },
}
```

Once enabled, swc will generate trace named as `swc-trace-profile-${timestamp}.json` under `.next/`. Chromium's trace viewer (chrome://tracing/,
### SWC Plugins (experimental)[](https://nextjs.org/docs/architecture/nextjs-compiler#swc-plugins-experimental)
You can configure swc's transform to use SWC's experimental plugin support written in wasm to customize transformation behavior.
next.config.js
```
module.exports = {
  experimental: {
    swcPlugins: [
      [
        'plugin',
        {
          ...pluginOptions,
        },
      ],
    ],
  },
}
```

`swcPlugins` accepts an array of tuples for configuring plugins. A tuple for the plugin contains the path to the plugin and an object for plugin configuration. The path to the plugin can be an npm module package name or an absolute path to the `.wasm` binary itself.
