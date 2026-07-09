## Improving local dev performance[](https://nextjs.org/docs/app/guides/local-development#improving-local-dev-performance)
### 1. Check your computer's antivirus[](https://nextjs.org/docs/app/guides/local-development#1-check-your-computers-antivirus)
Antivirus software can slow down file access. While this is more common on Windows machines, this can be an issue for any system with an antivirus tool installed.
On Windows, you can add your project to the
  1. Open the **"Windows Security"** application and then select **"Virus & threat protection"** → **"Manage settings"** → **"Add or remove exclusions"**.
  2. Add a **"Folder"** exclusion. Select your project folder.


On macOS, you can disable
  1. Run `sudo spctl developer-mode enable-terminal` in your terminal.
  2. Open the **"System Settings"** app and then select **"Privacy & Security"** → **"Developer Tools"**.
  3. Ensure your terminal is listed and enabled. If you're using a third-party terminal like iTerm or Ghostty, add that to the list.
  4. Restart your terminal.

![Screenshot of macOS System Settings showing the Privacy & Security pane](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Flight%2Fmacos-gatekeeper-privacy-and-security.png&w=1920&q=75)![Screenshot of macOS System Settings showing the Privacy & Security pane](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Fdark%2Fmacos-gatekeeper-privacy-and-security.png&w=1920&q=75) ![Screenshot of macOS System Settings showing the Developer Tools options](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Flight%2Fmacos-gatekeeper-developer-tools.png&w=1920&q=75)![Screenshot of macOS System Settings showing the Developer Tools options](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Fdark%2Fmacos-gatekeeper-developer-tools.png&w=1920&q=75)
If you or your employer have configured any other Antivirus solutions on your system, you should inspect the relevant settings for those products.
### 2. Update Next.js and use Turbopack[](https://nextjs.org/docs/app/guides/local-development#2-update-nextjs-and-use-turbopack)
Make sure you're using the latest version of Next.js. Each new version often includes performance improvements.
Turbopack is now the default bundler for Next.js development and provides significant performance improvements over webpack.
pnpmnpmyarnbun
Terminal
```
pnpm add next@latest
pnpm dev  # Turbopack is used by default
```

If you need to use Webpack instead of Turbopack, you can opt-in:
pnpmnpmyarnbun
Terminal
```
pnpm dev --webpack
```

[Learn more about Turbopack](https://nextjs.org/blog/turbopack-for-development-stable). See our [upgrade guides](https://nextjs.org/docs/app/guides/upgrading) and codemods for more information.
### 3. Check your imports[](https://nextjs.org/docs/app/guides/local-development#3-check-your-imports)
The way you import code can greatly affect compilation and bundling time. Learn more about [optimizing package bundling](https://nextjs.org/docs/app/guides/package-bundling) and explore tools like
#### Icon libraries[](https://nextjs.org/docs/app/guides/local-development#icon-libraries)
Libraries like `@material-ui/icons`, `@phosphor-icons/react`, or `react-icons` can import thousands of icons, even if you only use a few. Try to import only the icons you need:
```
// Instead of this:
import { TriangleIcon } from '@phosphor-icons/react'

// Do this:
import { TriangleIcon } from '@phosphor-icons/react/dist/csr/Triangle'
```

You can often find what import pattern to use in the documentation for the icon library you're using. This example follows
Libraries like `react-icons` includes many different icon sets. Choose one set and stick with that set.
For example, if your application uses `react-icons` and imports all of these:
  * `pi` (Phosphor Icons)
  * `md` (Material Design Icons)
  * `tb` (tabler-icons)
  * `cg` (cssgg)


Combined they will be tens of thousands of modules that the compiler has to handle, even if you only use a single import from each.
#### Barrel files[](https://nextjs.org/docs/app/guides/local-development#barrel-files)
"Barrel files" are files that export many items from other files. They can slow down builds because the compiler has to parse them to find if there are side-effects in the module scope by using the import.
Try to import directly from specific files when possible.
#### Optimize package imports[](https://nextjs.org/docs/app/guides/local-development#optimize-package-imports)
Next.js can automatically optimize imports for certain packages. If you are using packages that utilize barrel files, add them to your `next.config.js`:
```
module.exports = {
  experimental: {
    optimizePackageImports: ['package-name'],
  },
}
```

Turbopack automatically analyzes imports and optimizes them. It does not require this configuration.
### 4. Check your Tailwind CSS setup[](https://nextjs.org/docs/app/guides/local-development#4-check-your-tailwind-css-setup)
If you're using Tailwind CSS, make sure it's set up correctly.
A common mistake is configuring your `content` array in a way which includes `node_modules` or other large directories of files that should not be scanned.
Tailwind CSS version 3.4.8 or newer will warn you about settings that might slow down your build.
  1. In your `tailwind.config.js`, be specific about which files to scan:
```
module.exports = {
  content: [
    './src/**/*.{js,ts,jsx,tsx}', // Good
    // This might be too broad
    // It will match `packages/**/node_modules` too
    // '../../packages/**/*.{js,ts,jsx,tsx}',
  ],
}
```

  2. Avoid scanning unnecessary files:
```
module.exports = {
  content: [
    // Better - only scans the 'src' folder
    '../../packages/ui/src/**/*.{js,ts,jsx,tsx}',
  ],
}
```



### 5. Check custom webpack settings[](https://nextjs.org/docs/app/guides/local-development#5-check-custom-webpack-settings)
If you've added custom webpack settings, they might be slowing down compilation.
Consider if you really need them for local development. You can optionally only include certain tools for production builds, or explore using the default Turbopack bundler and configuring [loaders](https://nextjs.org/docs/app/api-reference/config/next-config-js/turbopack#configuring-webpack-loaders) instead.
### 6. Optimize memory usage[](https://nextjs.org/docs/app/guides/local-development#6-optimize-memory-usage)
If your app is very large, it might need more memory.
[Learn more about optimizing memory usage](https://nextjs.org/docs/app/guides/memory-usage).
### 7. Server Components and data fetching[](https://nextjs.org/docs/app/guides/local-development#7-server-components-and-data-fetching)
Changes to Server Components cause the entire page to re-render locally in order to show the new changes, which includes fetching new data for the component.
The experimental `serverComponentsHmrCache` option allows you to cache `fetch` responses in Server Components across Hot Module Replacement (HMR) refreshes in local development. This results in faster responses and reduced costs for billed API calls.
[Learn more about the experimental option](https://nextjs.org/docs/app/api-reference/config/next-config-js/serverComponentsHmrCache).
### 8. Consider local development over Docker[](https://nextjs.org/docs/app/guides/local-development#8-consider-local-development-over-docker)
If you're using Docker for development on Mac or Windows, you may experience significantly slower performance compared to running Next.js locally.
Docker's filesystem access on Mac and Windows can cause Hot Module Replacement (HMR) to take seconds or even minutes, while the same application runs with fast HMR when developed locally.
This performance difference is due to how Docker handles filesystem operations outside of Linux environments. For the best development experience:
  * Use local development (`npm run dev` or `pnpm dev`) instead of Docker during development
  * Reserve Docker for production deployments and testing production builds
  * If you must use Docker for development, consider using Docker on a Linux machine or VM


[Learn more about Docker deployment](https://nextjs.org/docs/app/getting-started/deploying#docker) for production use.
