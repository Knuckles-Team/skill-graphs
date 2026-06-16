components.json - shadcn/ui Toggle Menu Menu Home Docs Components Blocks Charts Directory Create Search documentation... Search... 117k Toggle theme New Sections Introduction Components Installation Theming CLI RTL Skills MCP Server Registry Forms Changelog Components Accordion Alert Alert Dialog Aspect Ratio Avatar Badge Breadcrumb Button Button Group Calendar Card Carousel Chart Checkbox Collapsible Combobox Command Context Menu Data Table Date Picker Dialog Direction Drawer Dropdown Menu Empty Field Hover Card Input Input Group Input OTP Item Kbd Label Menubar Native Select Navigation Menu Pagination Popover Progress Radio Group Resizable Scroll Area Select Separator Sheet Sidebar Skeleton Slider Sonner Spinner Switch Table Tabs Textarea Toast Toggle Toggle Group Tooltip Typography Get Started Installation components.json Package Imports Theming Dark Mode CLI Monorepo Skills JavaScript Figma llms.txt Legacy Docs Forms React Hook Form TanStack Form Formisch Registry Introduction Getting Started GitHub Registries Registry Directory Examples Namespaces Authentication MCP Server Open in v0 API Reference registry.json registry-item.json components.json Copy Page Previous Next Configuration for your project. The components.json file holds configuration for your project.
 We use it to understand how your project is set up and how to generate components customized for your project.
 Note: The `components.json` file is optional It is only required if you&#x27;re using the CLI to add components to your
project. If you&#x27;re using the copy and paste method, you don&#x27;t need this file.
 You can create a components.json file in your project by running the following command:
 pnpm npm yarn bun pnpm dlx shadcn@latest init Copy
 See the CLI section for more information.
 $schema #
 You can see the JSON Schema for components.json here .
 components.json Copy {
 &quot;$schema&quot; : &quot;https://ui.shadcn.com/schema.json&quot;
 }
 style #
 The style for your components. This cannot be changed after initialization.
 components.json Copy {
 &quot;style&quot; : &quot;new-york&quot;
 }
 The default style has been deprecated. Use the new-york style instead.
 tailwind #
 Configuration to help the CLI understand how Tailwind CSS is set up in your project.
 See the installation section for how to set up Tailwind CSS.
 tailwind.config #
 Path to where your tailwind.config.js file is located. For Tailwind CSS v4, leave this blank.
 components.json Copy {
 &quot;tailwind&quot; : {
 &quot;config&quot; : &quot;tailwind.config.js&quot; | &quot;tailwind.config.ts&quot;
 }
 }
 tailwind.css #
 Path to the CSS file that imports Tailwind CSS into your project.
 components.json Copy {
 &quot;tailwind&quot; : {
 &quot;css&quot; : &quot;styles/global.css&quot;
 }
 }
 tailwind.baseColor #
 This is used to generate the default theme tokens for your components. This cannot be changed after initialization.
 components.json Copy {
 &quot;tailwind&quot; : {
 &quot;baseColor&quot; : &quot;neutral&quot; | &quot;stone&quot; | &quot;zinc&quot; | &quot;mauve&quot; | &quot;olive&quot; | &quot;mist&quot; | &quot;taupe&quot;
 }
 }
 tailwind.cssVariables #
 We use and recommend CSS variables for theming.
 Set tailwind.cssVariables to true to generate semantic theme tokens like background , foreground , and primary . Set it to false to generate inline Tailwind color utilities instead.
 components.json Copy {
 &quot;tailwind&quot; : {
 &quot;cssVariables&quot; : ` true ` | ` false `
 }
 }
 For more information, see the theming docs .
 This cannot be changed after initialization. To switch between CSS variables and utility classes, you&#x27;ll have to delete and re-install your components.
 tailwind.prefix #
 The prefix to use for your Tailwind CSS utility classes. Components will be added with this prefix.
 components.json Copy {
 &quot;tailwind&quot; : {
 &quot;prefix&quot; : &quot;tw-&quot;
 }
 }
 rsc #
 Whether or not to enable support for React Server Components.
 The CLI automatically adds a use client directive to client components when set to true .
 components.json Copy {
 &quot;rsc&quot; : ` true ` | ` false `
 }
 tsx #
 Choose between TypeScript or JavaScript components.
 Setting this option to false allows components to be added as JavaScript with the .jsx file extension.
 components.json Copy {
 &quot;tsx&quot; : ` true ` | ` false `
 }
 aliases #
 The CLI uses these values to place generated components in the correct location and rewrite imports.
 You can back these aliases with either:

 compilerOptions.paths in your tsconfig.json or jsconfig.json
 package.json#imports with TypeScript package import resolution enabled

 The aliases in components.json are still required when using the CLI. They tell the CLI which import roots map to components , ui , lib , hooks , and utils .
 Important: If you&#x27;re using package imports, enable
 resolvePackageJsonImports and use moduleResolution: &quot;bundler&quot; in your
 tsconfig.json . If you&#x27;re using paths , make sure your aliases include the
 src directory when applicable.
 Using tsconfig or jsconfig paths #
 tsconfig.json Copy {
 &quot;compilerOptions&quot; : {
 &quot;baseUrl&quot; : &quot;.&quot; ,
 &quot;paths&quot; : {
 &quot;@/*&quot; : [ &quot;./src/*&quot; ]
 }
 }
 }
 Using package.json#imports #
 Recommended setup for a single-package app:
 package.json Copy {
 &quot;imports&quot; : {
 &quot;#components/*&quot; : &quot;./src/components/*.tsx&quot; ,
 &quot;#lib/*&quot; : &quot;./src/lib/*.ts&quot; ,
 &quot;#hooks/*&quot; : &quot;./src/hooks/*.ts&quot;
 }
 }
 tsconfig.json Copy {
 &quot;compilerOptions&quot; : {
 &quot;moduleResolution&quot; : &quot;bundler&quot; ,
 &quot;resolvePackageJsonImports&quot; : true
 }
 }
 components.json Copy {
 &quot;aliases&quot; : {
 &quot;components&quot; : &quot;#components&quot; ,
 &quot;ui&quot; : &quot;#components/ui&quot; ,
 &quot;lib&quot; : &quot;#lib&quot; ,
 &quot;hooks&quot; : &quot;#hooks&quot; ,
 &quot;utils&quot; : &quot;#lib/utils&quot;
 }
 }
 The aliases in components.json still tell the CLI where to place
 components , ui , lib , hooks , and utils . package.json#imports
provides the runtime and TypeScript resolution for those #... specifiers.
 The matched imports target also controls whether generated #... imports keep
file extensions:

 &quot;#components/*&quot;: &quot;./src/components/*&quot; preserves source extensions and can
generate imports like
 #components/button.tsx
 &quot;#components/*&quot;: &quot;./src/components/*.tsx&quot; strips source extensions and
generates imports like
 #components/button

 For monorepos, see the monorepo docs . Local
workspace aliases can use package.json#imports , while shared workspace
imports such as @workspace/ui/components are resolved from the target
package&#x27;s exports .
 For framework-specific setup, see the package imports guide .
 aliases.utils #
 Import alias for your utility functions.
 components.json Copy {
 &quot;aliases&quot; : {
 &quot;utils&quot; : &quot;@/lib/utils&quot;
 }
 }
 aliases.components #
 Import alias for your components.
 components.json Copy {
 &quot;aliases&quot; : {
 &quot;components&quot; : &quot;@/components&quot;
 }
 }
 aliases.ui #
 Import alias for ui components.
 The CLI will use the aliases.ui value to determine where to place your ui components. Use this config if you want to customize the installation directory for your ui components.
 components.json Copy {
 &quot;aliases&quot; : {
 &quot;ui&quot; : &quot;@/app/ui&quot;
 }
 }
 aliases.lib #
 Import alias for lib functions such as format-date or generate-id .
 components.json Copy {
 &quot;aliases&quot; : {
 &quot;lib&quot; : &quot;@/lib&quot;
 }
 }
 aliases.hooks #
 Import alias for hooks such as use-media-query or use-toast .
 components.json Copy {
 &quot;aliases&quot; : {
 &quot;hooks&quot; : &quot;@/hooks&quot;
 }
 }
 registries #
 Configure multiple resource registries for your project. This allows you to install components, libraries, utilities, and other resources from various sources including private registries.
 See the Namespaced Registries documentation for detailed information.
 Basic Configuration #
 Configure registries with URL templates:
 components.json Copy {
 &quot;registries&quot; : {
 &quot;@v0&quot; : &quot;https://v0.dev/chat/b/{name}&quot; ,
 &quot;@acme&quot; : &quot;https://registry.acme.com/{name}.json&quot; ,
 &quot;@internal&quot; : &quot;https://internal.company.com/{name}.json&quot;
 }
 }
 The {name} placeholder is replaced with the resource name when installing.
 Advanced Configuration with Authentication #
 For private registries that require authentication:
 components.json Copy {
 &quot;registries&quot; : {
 &quot;@private&quot; : {
 &quot;url&quot; : &quot;https://api.company.com/registry/{name}.json&quot; ,
 &quot;headers&quot; : {
 &quot;Authorization&quot; : &quot;Bearer ${REGISTRY_TOKEN}&quot; ,
 &quot;X-API-Key&quot; : &quot;${API_KEY}&quot;
 },
 &quot;params&quot; : {
 &quot;version&quot; : &quot;latest&quot;
 }
 }
 }
 }
 Environment variables in the format ${VAR_NAME} are automatically expanded from your environment.
 Using Namespaced Registries #
 Once configured, install resources using the namespace syntax:
 Copy # Install from a configured registry
 npx shadcn@latest add @v0/dashboard

 # Install from private registry
 npx shadcn@latest add @private/button

 # Install multiple resources
 npx shadcn@latest add @acme/header @internal/auth-utils
 Example: Multiple Registry Setup #
 components.json Copy {
 &quot;registries&quot; : {
 &quot;@shadcn&quot; : &quot;https://ui.shadcn.com/r/{name}.json&quot; ,
 &quot;@company-ui&quot; : {
 &quot;url&quot; : &quot;https://registry.company.com/ui/{name}.json&quot; ,
 &quot;headers&quot; : {
 &quot;Authorization&quot; : &quot;Bearer ${COMPANY_TOKEN}&quot;
 }
 },
 &quot;@team&quot; : {
 &quot;url&quot; : &quot;https://team.company.com/{name}.json&quot; ,
 &quot;params&quot; : {
 &quot;team&quot; : &quot;frontend&quot; ,
 &quot;version&quot; : &quot;${REGISTRY_VERSION}&quot;
 }
 }
 }
 }
 This configuration allows you to:

 Install public components from shadcn/ui
 Access private company UI components with authentication
 Use team-specific resources with versioning

 For more information about authentication, see the Authentication documentation. Installation Package Imports On This Page $schema style tailwind tailwind.config tailwind.css tailwind.baseColor tailwind.cssVariables tailwind.prefix rsc tsx aliases Using tsconfig or jsconfig paths Using package.json#imports aliases.utils aliases.components aliases.ui aliases.lib aliases.hooks registries Basic Configuration Advanced Configuration with Authentication Using Namespaced Registries Example: Multiple Registry Setup Deploy your shadcn/ui app on Vercel Trusted by OpenAI, Sonos, Adobe, and more. Vercel provides tools and infrastructure to deploy apps and features at scale. Deploy Now Deploy to Vercel Built by shadcn at Vercel . The source code is available on GitHub . Get Code
