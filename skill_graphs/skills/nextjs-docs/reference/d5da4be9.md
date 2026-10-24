## IDE Plugin[](https://nextjs.org/docs/app/api-reference/config/typescript#ide-plugin)
Next.js includes a custom TypeScript plugin and type checker, which VSCode and other code editors can use for advanced type-checking and auto-completion.
You can enable the plugin in VS Code by:
  1. Opening the command palette (`Ctrl/⌘` + `Shift` + `P`)
  2. Searching for "TypeScript: Select TypeScript Version"
  3. Selecting "Use Workspace Version"

![TypeScript Command Palette](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Flight%2Ftypescript-command-palette.png&w=3840&q=75)![TypeScript Command Palette](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Fdark%2Ftypescript-command-palette.png&w=3840&q=75)
Now, when editing files, the custom plugin will be enabled. When running `next build`, the custom type checker will be used.
The TypeScript plugin can help with:
  * Warning if invalid values for [segment config options](https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config) are passed.
  * Showing available options and in-context documentation.
  * Ensuring the `'use client'` directive is used correctly.
  * Ensuring client hooks (like `useState`) are only used in Client Components.


> **🎥 Watch:** Learn about the built-in TypeScript plugin →
