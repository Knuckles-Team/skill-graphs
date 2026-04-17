## Reference[](https://nextjs.org/docs/app/api-reference/cli/next#reference)
The following options are available:
Options | Description
---|---
`-h` or `--help` | Shows all available options
`-v` or `--version` | Outputs the Next.js version number
### Commands[](https://nextjs.org/docs/app/api-reference/cli/next#commands)
The following commands are available:
Command | Description
---|---
[`dev`](https://nextjs.org/docs/app/api-reference/cli/next#next-dev-options) | Starts Next.js in development mode with Hot Module Reloading, error reporting, and more.
[`build`](https://nextjs.org/docs/app/api-reference/cli/next#next-build-options) | Creates an optimized production build of your application. Displaying information about each route.
[`start`](https://nextjs.org/docs/app/api-reference/cli/next#next-start-options) | Starts Next.js in production mode. The application should be compiled with `next build` first.
[`info`](https://nextjs.org/docs/app/api-reference/cli/next#next-info-options) | Prints relevant details about the current system which can be used to report Next.js bugs.
[`telemetry`](https://nextjs.org/docs/app/api-reference/cli/next#next-telemetry-options) | Allows you to enable or disable Next.js' completely anonymous telemetry collection.
[`typegen`](https://nextjs.org/docs/app/api-reference/cli/next#next-typegen-options) | Generates TypeScript definitions for routes, pages, layouts, and route handlers without running a full build.
[`upgrade`](https://nextjs.org/docs/app/api-reference/cli/next#next-upgrade-options) | Upgrades your Next.js application to the latest version.
[`experimental-analyze`](https://nextjs.org/docs/app/api-reference/cli/next#next-experimental-analyze-options) | Analyzes bundle output using Turbopack. Does not produce build artifacts.
> **Good to know** : Running `next` without a command is an alias for `next dev`.
###  `next dev` options[](https://nextjs.org/docs/app/api-reference/cli/next#next-dev-options)
`next dev` starts the application in development mode with Hot Module Reloading (HMR), error reporting, and more. The following options are available when running `next dev`:
Option | Description
---|---
`-h, --help` | Show all available options.
`[directory]` | A directory in which to build the application. If not provided, current directory is used.
`--turbopack` | Force enable [Turbopack](https://nextjs.org/docs/app/api-reference/turbopack) (enabled by default). Also available as `--turbo`.
`--webpack` | Use Webpack instead of the default [Turbopack](https://nextjs.org/docs/app/api-reference/turbopack) bundler for development.
`-p` or `--port <port>` | Specify a port number on which to start the application. Default: 3000, env: PORT
`-H`or `--hostname <hostname>` | Specify a hostname on which to start the application. Useful for making the application available for other devices on the network. Default: 0.0.0.0
`--experimental-https` | Starts the server with HTTPS and generates a self-signed certificate.
`--experimental-https-key <path>` | Path to a HTTPS key file.
`--experimental-https-cert <path>` | Path to a HTTPS certificate file.
`--experimental-https-ca <path>` | Path to a HTTPS certificate authority file.
`--experimental-upload-trace <traceUrl>` | Reports a subset of the debugging trace to a remote HTTP URL.
###  `next build` options[](https://nextjs.org/docs/app/api-reference/cli/next#next-build-options)
`next build` creates an optimized production build of your application. The output displays information about each route. For example:
Terminal
```
Route (app)
┌ ○ /_not-found
└ ƒ /products/[id]

○  (Static)   prerendered as static content
ƒ  (Dynamic)  server-rendered on demand
```

The following options are available for the `next build` command:
Option | Description
---|---
`-h, --help` | Show all available options.
`[directory]` | A directory on which to build the application. If not provided, the current directory will be used.
`--turbopack` | Force enable [Turbopack](https://nextjs.org/docs/app/api-reference/turbopack) (enabled by default). Also available as `--turbo`.
`--webpack` | Build using Webpack.
`-d` or `--debug` | Enables a more verbose build output. With this flag enabled additional build output like rewrites, redirects, and headers will be shown.
|
`--profile` | Enables production
`--no-lint` | Disables linting. _Note: linting will be removed from`next build` in Next 16. If you're using Next 15.5+ with a linter other than `eslint`, linting during build will not occur._
`--no-mangling` | Disables
`--experimental-app-only` | Builds only App Router routes.
`--experimental-build-mode [mode]` | Uses an experimental build mode. (choices: "compile", "generate", default: "default")
`--debug-prerender` | Debug prerender errors in development.
`--debug-build-paths=<patterns>` | Build only specific routes for debugging.
###  `next start` options[](https://nextjs.org/docs/app/api-reference/cli/next#next-start-options)
`next start` starts the application in production mode. The application should be compiled with [`next build`](https://nextjs.org/docs/app/api-reference/cli/next#next-build-options) first.
The following options are available for the `next start` command:
Option | Description
---|---
`-h` or `--help` | Show all available options.
`[directory]` | A directory on which to start the application. If no directory is provided, the current directory will be used.
`-p` or `--port <port>` | Specify a port number on which to start the application. (default: 3000, env: PORT)
`-H` or `--hostname <hostname>` | Specify a hostname on which to start the application (default: 0.0.0.0).
`--keepAliveTimeout <keepAliveTimeout>` | Specify the maximum amount of milliseconds to wait before closing the inactive connections.
###  `next info` options[](https://nextjs.org/docs/app/api-reference/cli/next#next-info-options)
`next info` prints relevant details about the current system which can be used to report Next.js bugs when opening a `next`, `react`, `react-dom`), and more.
The output should look like this:
Terminal
```
Operating System:
  Platform: darwin
  Arch: arm64
  Version: Darwin Kernel Version 23.6.0
  Available memory (MB): 65536
  Available CPU cores: 10
Binaries:
  Node: 20.12.0
  npm: 10.5.0
  Yarn: 1.22.19
  pnpm: 9.6.0
Relevant Packages:
  next: 15.0.0-canary.115 // Latest available version is detected (15.0.0-canary.115).
  eslint-config-next: 14.2.5
  react: 19.0.0-rc
  react-dom: 19.0.0
  typescript: 5.5.4
Next.js Config:
  output: N/A
```

The following options are available for the `next info` command:
Option | Description
---|---
`-h` or `--help` | Show all available options
`--verbose` | Collects additional information for debugging.
###  `next telemetry` options[](https://nextjs.org/docs/app/api-reference/cli/next#next-telemetry-options)
Next.js collects **completely anonymous** telemetry data about general usage. Participation in this anonymous program is optional, and you can opt-out if you prefer not to share information.
The following options are available for the `next telemetry` command:
Option | Description
---|---
`-h, --help` | Show all available options.
`--enable` | Enables Next.js' telemetry collection.
`--disable` | Disables Next.js' telemetry collection.
Learn more about [Telemetry](https://nextjs.org/telemetry).
###  `next typegen` options[](https://nextjs.org/docs/app/api-reference/cli/next#next-typegen-options)
`next typegen` generates TypeScript definitions for your application's routes without performing a full build. This is useful for IDE autocomplete and CI type-checking of route usage.
Previously, route types were only generated during `next dev` or `next build`, which meant running `tsc --noEmit` directly wouldn't validate your route types. Now you can generate types independently and validate them externally:
Terminal
```
# Generate route types first, then validate with TypeScript
next typegen && tsc --noEmit

# Or in CI workflows for type checking without building
next typegen && npm run type-check
```

The following options are available for the `next typegen` command:
Option | Description
---|---
`-h, --help` | Show all available options.
`[directory]` | A directory on which to generate types. If not provided, the current directory will be used.
Output files are written to `<distDir>/types` (typically: `.next/dev/types` or `.next/types`, see [`isolatedDevBuild`](https://nextjs.org/docs/app/api-reference/config/next-config-js/isolatedDevBuild)):
Terminal
```
next typegen
# or for a specific app
next typegen ./apps/web
```

Additionally, `next typegen` generates a `next-env.d.ts` file. We recommend adding `next-env.d.ts` to your `.gitignore` file.
The `next-env.d.ts` file is included into your `tsconfig.json` file, to make Next.js types available to your project.
To ensure `next-env.d.ts` is present before type-checking run `next typegen`. The commands `next dev` and `next build` also generate the `next-env.d.ts` file, but it is often undesirable to run these just to type-check, for example in CI/CD environments.
> **Good to know** : `next typegen` loads your Next.js config (`next.config.js`, `next.config.mjs`, or `next.config.ts`) using the production build phase. Ensure any required environment variables and dependencies are available so the config can load correctly.
###  `next upgrade` options[](https://nextjs.org/docs/app/api-reference/cli/next#next-upgrade-options)
`next upgrade` upgrades your Next.js application to the latest version.
The following options are available for the `next upgrade` command:
Option | Description
---|---
`-h, --help` | Show all available options.
`[directory]` | A directory with the Next.js application to upgrade. If not provided, the current directory will be used.
`--revision <revision>` | Specify a Next.js version or tag to upgrade to (e.g., `latest`, `canary`, `15.0.0`). Defaults to the release channel you have currently installed.
`--verbose` | Show verbose output during the upgrade process.
###  `next experimental-analyze` options[](https://nextjs.org/docs/app/api-reference/cli/next#next-experimental-analyze-options)
`next experimental-analyze` analyzes your application's bundle output using [Turbopack](https://nextjs.org/docs/app/api-reference/turbopack). This command helps you understand the size and composition of your bundles, including JavaScript, CSS, and other assets. This command doesn't produce an application build.
pnpmnpmyarnbun
Terminal
```
pnpm next experimental-analyze
```

By default, the command starts a local server after analysis completes, allowing you to explore your bundle composition in the browser. The analyzer lets you:
  * Filter bundles by route and switch between client and server views
  * View the full import chain showing why a module is included
  * Trace imports across server-to-client component boundaries and dynamic imports


See [Package Bundling](https://nextjs.org/docs/app/guides/package-bundling#optimizing-large-bundles) for optimization strategies.
To write the analysis output to disk without starting the server, use the `--output` flag. The output is written to `.next/diagnostics/analyze` and contains static files that can be copied elsewhere or shared with others:
Terminal
```
# Write output to .next/diagnostics/analyze
npx next experimental-analyze --output

# Copy the output for comparison with a future analysis
cp -r .next/diagnostics/analyze ./analyze-before-refactor
```

The following options are available for the `next experimental-analyze` command:
Option | Description
---|---
`-h, --help` | Show all available options.
`[directory]` | A directory on which to analyze the application. If not provided, the current directory will be used.
`--no-mangling` | Disables
`--profile` | Enables production
`-o, --output` | Write analysis files to disk without starting the server. Output is written to `.next/diagnostics/analyze`.
`--port <port>` | Specify a port number to serve the analyzer on. (default: 4000, env: PORT)
