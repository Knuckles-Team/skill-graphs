[![](https://vite.dev/assets/footer-background.BIgtbvhx.jpg) ![Vite icon](data:image/svg+xml,%3csvg%20viewBox='0%200%2023%2014'%20fill='none'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20d='M20.7482%200H18.8887C21.641%203.93959%2021.6571%2010.0462%2018.8887%2014H20.7482C23.516%2010.0462%2023.4999%203.93959%2020.7482%200Z'%20fill='white'/%3e%3cpath%20d='M2.07027%203.05176e-05C-0.682028%203.93963%20-0.698142%2010.0463%202.07027%2014H3.92985C1.16208%2010.0463%201.1782%203.93963%203.92985%203.05176e-05H2.07027Z'%20fill='white'/%3e%3cpath%20d='M12.0135%2013.6771C11.815%2013.9298%2011.4089%2013.7892%2011.4089%2013.4683V10.3853C11.4089%2010.0114%2011.106%209.70849%2010.7321%209.70849H7.32818C7.05295%209.70849%206.89245%209.39716%207.05295%209.1735L9.29089%206.04026C9.61124%205.59228%209.29089%204.96963%208.73979%204.96963H4.62036C4.34513%204.96963%204.18463%204.65831%204.34512%204.43464L7.24632%200.372579C7.31013%200.283628%207.41262%200.230774%207.52155%200.230774H16.1671C16.4424%200.230774%2016.6029%200.5421%2016.4424%200.765765L14.2044%203.89901C13.8841%204.34698%2014.2044%204.96963%2014.7555%204.96963H18.1595C18.4418%204.96963%2018.6004%205.29514%2018.4257%205.51751L12.0142%2013.6777L12.0135%2013.6771Z'%20fill='white'/%3e%3c/svg%3e)Cloudflare supports Vite's mission ](https://vite.dev/blog/cloudflare-supports-vite)
[Skip to content](https://vite.dev/guide/backend-integration#VPContent)
[![Vite](https://vite.dev/assets/vite-dark.D2ACe7TL.svg)![Vite](https://vite.dev/assets/vite-light.t8GCa_VF.svg)](https://vite.dev/)
Main Navigation [Guide](https://vite.dev/guide/)[Config](https://vite.dev/config/)[Plugins](https://vite.dev/plugins/)
Resources
[Team](https://vite.dev/team)
[Blog](https://vite.dev/blog)
[Releases](https://vite.dev/releases)
[Acknowledgements](https://vite.dev/acknowledgements)
[Plugin Registry](https://registry.vite.dev/plugins)
[Discord Chat](https://chat.vite.dev)
v8.0.16
[Unreleased Docs](https://main.vite.dev)
[Vite 7 Docs](https://v7.vite.dev)
[Vite 6 Docs](https://v6.vite.dev)
[Vite 5 Docs](https://v5.vite.dev)
[Vite 4 Docs](https://v4.vite.dev)
[Vite 3 Docs](https://v3.vite.dev)
[Vite 2 Docs](https://v2.vite.dev)
Search`⌘``Ctrl``K`
English
[简体中文](https://cn.vite.dev/guide/backend-integration)
[日本語](https://ja.vite.dev/guide/backend-integration)
[Español](https://es.vite.dev/guide/backend-integration)
[Português](https://pt.vite.dev/guide/backend-integration)
[한국어](https://ko.vite.dev/guide/backend-integration)
[Deutsch](https://de.vite.dev/guide/backend-integration)
[فارسی](https://fa.vite.dev/guide/backend-integration)
Appearance
[](https://chat.vite.dev)
English
[简体中文](https://cn.vite.dev/guide/backend-integration)
[日本語](https://ja.vite.dev/guide/backend-integration)
[Español](https://es.vite.dev/guide/backend-integration)
[Português](https://pt.vite.dev/guide/backend-integration)
[한국어](https://ko.vite.dev/guide/backend-integration)
[Deutsch](https://de.vite.dev/guide/backend-integration)
[فارسی](https://fa.vite.dev/guide/backend-integration)
[](https://chat.vite.dev)
Menu
Return to top
Sidebar Navigation
## Introduction
[Getting Started ](https://vite.dev/guide/)
[Philosophy ](https://vite.dev/guide/philosophy)
[Why Vite ](https://vite.dev/guide/why)
## Guide
[Features ](https://vite.dev/guide/features)
[CLI ](https://vite.dev/guide/cli)
[Using Plugins ](https://vite.dev/guide/using-plugins)
[Dependency Pre-Bundling ](https://vite.dev/guide/dep-pre-bundling)
[Static Asset Handling ](https://vite.dev/guide/assets)
[Building for Production ](https://vite.dev/guide/build)
[Deploying a Static Site ](https://vite.dev/guide/static-deploy)
[Env Variables and Modes ](https://vite.dev/guide/env-and-mode)
[Server-Side Rendering (SSR) ](https://vite.dev/guide/ssr)
[Backend Integration ](https://vite.dev/guide/backend-integration)
[Troubleshooting ](https://vite.dev/guide/troubleshooting)
[Performance ](https://vite.dev/guide/performance)
[Migration from v7 ](https://vite.dev/guide/migration)
[Breaking Changes ](https://vite.dev/changes/)
## APIs
[Plugin API ](https://vite.dev/guide/api-plugin)
[HMR API ](https://vite.dev/guide/api-hmr)
[JavaScript API ](https://vite.dev/guide/api-javascript)
[Config Reference ](https://vite.dev/config/)
## Environment API
[Introduction ](https://vite.dev/guide/api-environment)
[Environment Instances ](https://vite.dev/guide/api-environment-instances)
[Plugins ](https://vite.dev/guide/api-environment-plugins)
[Frameworks ](https://vite.dev/guide/api-environment-frameworks)
[Runtimes ](https://vite.dev/guide/api-environment-runtimes)
On this page

Are you an LLM? You can read better optimized documentation at /guide/backend-integration.md for this page in Markdown format
# Backend Integration [​](https://vite.dev/guide/backend-integration#backend-integration)
Note
If you want to serve the HTML using a traditional backend (e.g. Rails, Laravel) but use Vite for serving assets, check for existing integrations listed in
If you need a custom integration, you can follow the steps in this guide to configure it manually.
  1. In your Vite config, configure the entry and enable build manifest:
vite.config.js
js
```
export default

defineConfig

({

server

: {

cors

: {
      // the origin you will be accessing via browser

origin

: 'http://my-backend.example.com',
    },
  },

build

: {
    // generate .vite/manifest.json in outDir

manifest

: true,

rolldownOptions

: {
      // overwrite default .html entry

input

: '/path/to/main.js',
    },
  },
})
```

If you haven't disabled the [module preload polyfill](https://vite.dev/config/build-options#build-polyfillmodulepreload), you also need to import the polyfill in your entry
js
```
// add the beginning of your app entry
import 'vite/modulepreload-polyfill'
```

  2. For development, inject the following in your server's HTML template (substitute `http://localhost:5173` with the local URL Vite is running at):
html
```
<!-- if development -->
<script type="module" src="http://localhost:5173/@vite/client"></script>
<script type="module" src="http://localhost:5173/main.js"></script>
```

In order to properly serve assets, you have two options:
     * Make sure the server is configured to proxy static assets requests to the Vite server
     * Set [`server.origin`](https://vite.dev/config/server-options#server-origin) so that generated asset URLs will be resolved using the back-end server URL instead of a relative path
This is needed for assets such as images to load properly.
Note if you are using React with `@vitejs/plugin-react`, you'll also need to add this before the above scripts, since the plugin is not able to modify the HTML you are serving (substitute `http://localhost:5173` with the local URL Vite is running at):
html
```
<script type="module">
  import RefreshRuntime from 'http://localhost:5173/@react-refresh'
  RefreshRuntime.injectIntoGlobalHook(window)
  window.$RefreshReg$ = () => {}
  window.$RefreshSig$ = () => (type) => type
  window.__vite_plugin_react_preamble_installed__ = true
</script>
```

  3. For production, after running `vite build`, a `.vite/manifest.json` file will be generated alongside other asset files. An example manifest file looks like this:
.vite/manifest.json
json
```
{
  "_shared-B7PI925R.js": {
    "file": "assets/shared-B7PI925R.js",
    "name": "shared",
    "css": ["assets/shared-ChJ_j-JJ.css"]
  },
  "_shared-ChJ_j-JJ.css": {
    "file": "assets/shared-ChJ_j-JJ.css",
    "src": "_shared-ChJ_j-JJ.css"
  },
  "logo.svg": {
    "file": "assets/logo-BuPIv-2h.svg",
    "src": "logo.svg"
  },
  "baz.js": {
    "file": "assets/baz-B2H3sXNv.js",
    "name": "baz",
    "src": "baz.js",
    "isDynamicEntry": true
  },
  "views/bar.js": {
    "file": "assets/bar-gkvgaI9m.js",
    "name": "bar",
    "src": "views/bar.js",
    "isEntry": true,
    "imports": ["_shared-B7PI925R.js"],
    "dynamicImports": ["baz.js"]
  },
  "views/foo.js": {
    "file": "assets/foo-BRBmoGS9.js",
    "name": "foo",
    "src": "views/foo.js",
    "isEntry": true,
    "imports": ["_shared-B7PI925R.js"],
    "css": ["assets/foo-5UjPuW-k.css"]
  }
}
```

The manifest maps source files to their build outputs and dependencies:
manifest foo views/foo.js(entry)shared _shared-B7PI925R.js(common chunk)foo->shared importsfoocss foo.cssfoo->foocss cssbar views/bar.js(entry)bar->shared importsbaz baz.js(dynamic import)bar->baz dynamicImportssharedcss shared.cssshared->sharedcss csslogo logo.svg(asset)
manifest foo views/foo.js(entry)shared _shared-B7PI925R.js(common chunk)foo->shared importsfoocss foo.cssfoo->foocss cssbar views/bar.js(entry)bar->shared importsbaz baz.js(dynamic import)bar->baz dynamicImportssharedcss shared.cssshared->sharedcss csslogo logo.svg(asset)
The manifest has a `Record<name, chunk>` structure where each chunk follows the `ManifestChunk` interface:
ts
```
interface ManifestChunk {
  /**
   * The input file name of this chunk / asset if known
   */
  src?: string
  /**
   * The output file name of this chunk / asset
   */
  file: string
  /**
   * The list of CSS files imported by this chunk
   */
  css?: string[]
  /**
   * The list of asset files imported by this chunk, excluding CSS files
   */
  assets?: string[]
  /**
   * Whether this chunk or asset is an entry point
   */
  isEntry?: boolean
  /**
   * The name of this chunk / asset if known
   */
  name?: string
  /**
   * Whether this chunk is a dynamic entry point
   *
   * This field is only present in JS chunks.
   */
  isDynamicEntry?: boolean
  /**
   * The list of statically imported chunks by this chunk
   *
   * The values are the keys of the manifest. This field is only present in JS chunks.
   */
  imports?: string[]
  /**
   * The list of dynamically imported chunks by this chunk
   *
   * The values are the keys of the manifest. This field is only present in JS chunks.
   */
  dynamicImports?: string[]
}
```

Each entry in the manifest represents one of the following:
     * **Entry chunks** : Generated from files specified in `isEntry: true` and their key is the relative src path from project root.
     * **Dynamic entry chunks** : Generated from dynamic imports. These chunks have `isDynamicEntry: true` and their key is the relative src path from project root.
     * **Non-entry chunks** : Their key is the base name of the generated file prefixed with `_`.
     * **Asset chunks** : Generated from imported assets like images, fonts. Their key is the relative src path from project root.
     * **CSS files** : When [`build.cssCodeSplit`](https://vite.dev/config/build-options#build-csscodesplit) is `false`, a single CSS file is generated with the key `style.css`. When `build.cssCodeSplit` is not `false`, the key is generated similar to JS chunks (i.e. entry chunks will not have `_` prefix and non-entry chunks will have `_` prefix).
JS chunks (chunks other than assets or CSS) will contain information on their static and dynamic imports (both are keys that map to the corresponding chunk in the manifest). Chunks also list their corresponding CSS and asset files if they have any.
  4. You can use this file to render links or preload directives with hashed filenames.
Here is an example HTML template to render the proper links. The syntax here is for explanation only, substitute with your server templating language. The `importedChunks` function is for illustration and isn't provided by Vite.
html
```
<!-- if production -->

<!-- for cssFile of manifest[name].css -->
<link rel="stylesheet" href="/{{ cssFile }}" />

<!-- for chunk of importedChunks(manifest, name) -->
<!-- for cssFile of chunk.css -->
<link rel="stylesheet" href="/{{ cssFile }}" />

<script type="module" src="/{{ manifest[name].file }}"></script>

<!-- for chunk of importedChunks(manifest, name) -->
<link rel="modulepreload" href="/{{ chunk.file }}" />
```

Specifically, a backend generating HTML should include the following tags given a manifest file and an entry point. Note that following this order is recommended for optimal performance:
    1. A `<link rel="stylesheet">` tag for each file in the entry point chunk's `css` list (if it exists)
    2. Recursively follow all chunks in the entry point's `imports` list and include a `<link rel="stylesheet">` tag for each CSS file of each imported chunk's `css` list (if it exists).
    3. A tag for the `file` key of the entry point chunk. This can be `<script type="module">` for JavaScript, `<link rel="stylesheet">` for CSS.
    4. Optionally, `<link rel="modulepreload">` tag for the `file` of each imported JavaScript chunk, again recursively following the imports starting from the entry point chunk.
Following the above example manifest, for the entry point `views/foo.js` the following tags should be included in production:
html
```
<link rel="stylesheet" href="assets/foo-5UjPuW-k.css" />
<link rel="stylesheet" href="assets/shared-ChJ_j-JJ.css" />
<script type="module" src="assets/foo-BRBmoGS9.js"></script>
<!-- optional -->
<link rel="modulepreload" href="assets/shared-B7PI925R.js" />
```

While the following should be included for the entry point `views/bar.js`:
html
```
<link rel="stylesheet" href="assets/shared-ChJ_j-JJ.css" />
<script type="module" src="assets/bar-gkvgaI9m.js"></script>
<!-- optional -->
<link rel="modulepreload" href="assets/shared-B7PI925R.js" />
```

Pseudo implementation of `importedChunks`
An example pseudo implementation of `importedChunks` in TypeScript (This will need to be adapted for your programming language and templating language):
ts
```
import type { Manifest, ManifestChunk } from 'vite'

export default function importedChunks(
  manifest: Manifest,
  name: string,
): ManifestChunk[] {
  const seen = new Set<string>()

  function getImportedChunks(chunk: ManifestChunk): ManifestChunk[] {
    const chunks: ManifestChunk[] = []
    for (const file of chunk.imports ?? []) {
      const importee = manifest[file]
      if (seen.has(file)) {
        continue
      }
      seen.add(file)

      chunks.push(...getImportedChunks(importee))
      chunks.push(importee)
    }

    return chunks
  }

  return getImportedChunks(manifest[name])
}
```

Pager
[Previous pageServer-Side Rendering (SSR)](https://vite.dev/guide/ssr)
[Next pageTroubleshooting](https://vite.dev/guide/troubleshooting)
© 2019-present VoidZero Inc. and Vite contributors. (012eb452)
