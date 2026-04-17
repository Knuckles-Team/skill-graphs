[Skip to content](https://vite.dev/guide/#VPContent)
[![Vite](https://vite.dev/assets/vite-dark.D2ACe7TL.svg)![Vite](https://vite.dev/assets/vite-light.t8GCa_VF.svg)](https://vite.dev/)
Main Navigation [Guide](https://vite.dev/guide/)[Config](https://vite.dev/config/)[Plugins](https://vite.dev/plugins/)
Resources
[Team](https://vite.dev/team)
[Blog](https://vite.dev/blog)
[Releases](https://vite.dev/releases)
[Discord Chat](https://chat.vite.dev)
v7.3.1
[Unreleased Docs](https://main.vite.dev)
[Vite 6 Docs](https://v6.vite.dev)
[Vite 5 Docs](https://v5.vite.dev)
[Vite 4 Docs](https://v4.vite.dev)
[Vite 3 Docs](https://v3.vite.dev)
[Vite 2 Docs](https://v2.vite.dev)
Search
English
[简体中文](https://cn.vite.dev/guide/)
[日本語](https://ja.vite.dev/guide/)
[Español](https://es.vite.dev/guide/)
[Português](https://pt.vite.dev/guide/)
[한국어](https://ko.vite.dev/guide/)
[Deutsch](https://de.vite.dev/guide/)
[فارسی](https://fa.vite.dev/guide/)
Appearance
[](https://chat.vite.dev)
English
[简体中文](https://cn.vite.dev/guide/)
[日本語](https://ja.vite.dev/guide/)
[Español](https://es.vite.dev/guide/)
[Português](https://pt.vite.dev/guide/)
[한국어](https://ko.vite.dev/guide/)
[Deutsch](https://de.vite.dev/guide/)
[فارسی](https://fa.vite.dev/guide/)
[](https://chat.vite.dev)
Menu
On this page
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
[Rolldown ](https://vite.dev/guide/rolldown)
[Migration from v6 ](https://vite.dev/guide/migration)
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
  * [Overview](https://vite.dev/guide/#overview "Overview")
  * [Browser Support](https://vite.dev/guide/#browser-support "Browser Support")
  * [Trying Vite Online](https://vite.dev/guide/#trying-vite-online "Trying Vite Online")
  * [Scaffolding Your First Vite Project](https://vite.dev/guide/#scaffolding-your-first-vite-project "Scaffolding Your First Vite Project")
  * [Community Templates](https://vite.dev/guide/#community-templates "Community Templates")
  * [Manual Installation](https://vite.dev/guide/#manual-installation "Manual Installation")
  * [index.html and Project Root](https://vite.dev/guide/#index-html-and-project-root "index.html and Project Root")
  * [Command Line Interface](https://vite.dev/guide/#command-line-interface "Command Line Interface")
  * [Using Unreleased Commits](https://vite.dev/guide/#using-unreleased-commits "Using Unreleased Commits")
  * [Community](https://vite.dev/guide/#community "Community")


Are you an LLM? You can read better optimized documentation at /guide.md for this page in Markdown format
# Getting Started [​](https://vite.dev/guide/#getting-started)
## Overview [​](https://vite.dev/guide/#overview)
Vite (French word for "quick", pronounced `/vit/`
  * A dev server that provides [rich feature enhancements](https://vite.dev/guide/features) over [Hot Module Replacement (HMR)](https://vite.dev/guide/features#hot-module-replacement).
  * A build command that bundles your code with


Vite is opinionated and comes with sensible defaults out of the box. Read about what's possible in the [Features Guide](https://vite.dev/guide/features). Support for frameworks or integration with other tools is possible through [Plugins](https://vite.dev/guide/using-plugins). The [Config Section](https://vite.dev/config/) explains how to adapt Vite to your project if needed.
Vite is also highly extensible via its [Plugin API](https://vite.dev/guide/api-plugin) and [JavaScript API](https://vite.dev/guide/api-javascript) with full typing support.
You can learn more about the rationale behind the project in the [Why Vite](https://vite.dev/guide/why) section.
## Browser Support [​](https://vite.dev/guide/#browser-support)
During development, Vite assumes that a modern browser is used. This means the browser supports most of the latest JavaScript and CSS features. For that reason, Vite sets
For production builds, Vite by default targets [Building for Production](https://vite.dev/guide/build) section for more details.
## Trying Vite Online [​](https://vite.dev/guide/#trying-vite-online)
You can try Vite online on `vite.new/{template}` to select which framework to use.
The supported template presets are:
JavaScript | TypeScript
---|---
|
|
|
|
|
|
|
|
## Scaffolding Your First Vite Project [​](https://vite.dev/guide/#scaffolding-your-first-vite-project)
npmYarnpnpmBunDeno
bash```
$ npm create vite@latest
```

bash```
$ yarn create vite
```

bash```
$ pnpm create vite
```

bash```
$ bun create vite
```

bash```
$ deno init --npm vite
```

Then follow the prompts!
Compatibility Note
Vite requires
Using create vite with command line options
You can also directly specify the project name and the template you want to use via additional command line options. For example, to scaffold a Vite + Vue project, run:
npmYarnpnpmBunDeno
bash```
# npm 7+, extra double-dash is needed:
$ npm create vite@latest my-vue-app -- --template vue
```

bash```
$ yarn create vite my-vue-app --template vue
```

bash```
$ pnpm create vite my-vue-app --template vue
```

bash```
$ bun create vite my-vue-app --template vue
```

bash```
$ deno init --npm vite my-vue-app --template vue
```

See `vanilla`, `vanilla-ts`, `vue`, `vue-ts`, `react`, `react-ts`, `react-swc`, `react-swc-ts`, `preact`, `preact-ts`, `lit`, `lit-ts`, `svelte`, `svelte-ts`, `solid`, `solid-ts`, `qwik`, `qwik-ts`.
You can use `.` for the project name to scaffold in the current directory.
To create a project without interactive prompts, you can use the `--no-interactive` flag.
## Community Templates [​](https://vite.dev/guide/#community-templates)
create-vite is a tool to quickly start a project from a basic template for popular frameworks. Check out Awesome Vite for
For a template at `https://github.com/user/project`, you can try it out online using `https://github.stackblitz.com/user/project` (adding `.stackblitz` after `github` to the URL of the project).
You can also use a tool like `main` as the default branch, you can create a local copy using:
bash```
npx degit user/project#main my-project
cd my-project

npm install
npm run dev
```

## Manual Installation [​](https://vite.dev/guide/#manual-installation)
In your project, you can install the `vite` CLI using:
npmYarnpnpmBunDeno
bash```
$ npm install -D vite
```

bash```
$ yarn add -D vite
```

bash```
$ pnpm add -D vite
```

bash```
$ bun add -D vite
```

bash```
$ deno add -D npm:vite
```

And create an `index.html` file like this:
html```
<p>Hello Vite!</p>
```

Then run the appropriate CLI command in your terminal:
npmYarnpnpmBunDeno
bash```
$ npx vite
```

bash```
$ yarn vite
```

bash```
$ pnpm vite
```

bash```
$ bunx vite
```

bash```
$ deno run -A npm:vite
```

The `index.html` will be served on `http://localhost:5173`.
##  `index.html` and Project Root [​](https://vite.dev/guide/#index-html-and-project-root)
One thing you may have noticed is that in a Vite project, `index.html` is front-and-central instead of being tucked away inside `public`. This is intentional: during development Vite is a server, and `index.html` is the entry point to your application.
Vite treats `index.html` as source code and part of the module graph. It resolves `<script type="module" src="...">` that references your JavaScript source code. Even inline `<script type="module">` and CSS referenced via `<link href>` also enjoy Vite-specific features. In addition, URLs inside `index.html` are automatically rebased so there's no need for special `%PUBLIC_URL%` placeholders.
Similar to static http servers, Vite has the concept of a "root directory" which your files are served from. You will see it referenced as `<root>` throughout the rest of the docs. Absolute URLs in your source code will be resolved using the project root as base, so you can write code as if you are working with a normal static file server (except way more powerful!). Vite is also capable of handling dependencies that resolve to out-of-root file system locations, which makes it usable even in a monorepo-based setup.
Vite also supports [multi-page apps](https://vite.dev/guide/build#multi-page-app) with multiple `.html` entry points.
#### Specifying Alternative Root [​](https://vite.dev/guide/#specifying-alternative-root)
Running `vite` starts the dev server using the current working directory as root. You can specify an alternative root with `vite serve some/sub/dir`. Note that Vite will also resolve [its config file (i.e. `vite.config.js`)](https://vite.dev/config/#configuring-vite) inside the project root, so you'll need to move it if the root is changed.
## Command Line Interface [​](https://vite.dev/guide/#command-line-interface)
In a project where Vite is installed, you can use the `vite` binary in your npm scripts, or run it directly with `npx vite`. Here are the default npm scripts in a scaffolded Vite project:
package.json
json```
{
  "scripts": {
    "dev": "vite", // start dev server, aliases: `vite dev`, `vite serve`
    "build": "vite build", // build for production
    "preview": "vite preview" // locally preview production build
  }
}
```

You can specify additional CLI options like `--port` or `--open`. For a full list of CLI options, run `npx vite --help` in your project.
Learn more about the [Command Line Interface](https://vite.dev/guide/cli)
## Using Unreleased Commits [​](https://vite.dev/guide/#using-unreleased-commits)
If you can't wait for a new release to test the latest features, you can install a specific commit of Vite with
npmYarnpnpmBun
bash```
$ npm install -D https://pkg.pr.new/vite@SHA
```

bash```
$ yarn add -D https://pkg.pr.new/vite@SHA
```

bash```
$ pnpm add -D https://pkg.pr.new/vite@SHA
```

bash```
$ bun add -D https://pkg.pr.new/vite@SHA
```

Replace `SHA` with any of
Alternatively, you can also clone the
bash```
git clone https://github.com/vitejs/vite.git
cd vite
pnpm install
cd packages/vite
pnpm run build
pnpm link --global # use your preferred package manager for this step
```

Then go to your Vite based project and run `pnpm link --global vite` (or the package manager that you used to link `vite` globally). Now restart the development server to ride on the bleeding edge!
To learn more about how and when Vite does releases, check out the [Releases](https://vite.dev/releases) documentation.
Dependencies using Vite
To replace the Vite version used by dependencies transitively, you should use
## Community [​](https://vite.dev/guide/#community)
If you have questions or need help, reach out to the community at [Discord](https://chat.vite.dev) and
Pager
[Next pagePhilosophy](https://vite.dev/guide/philosophy)
© 2025 VoidZero Inc. and Vite contributors. (f9b66fb3)
