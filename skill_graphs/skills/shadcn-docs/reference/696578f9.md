Monorepo - shadcn/ui Toggle Menu Menu Home Docs Components Blocks Charts Directory Create Search documentation... Search... 117k Toggle theme New Sections Introduction Components Installation Theming CLI RTL Skills MCP Server Registry Forms Changelog Components Accordion Alert Alert Dialog Aspect Ratio Avatar Badge Breadcrumb Button Button Group Calendar Card Carousel Chart Checkbox Collapsible Combobox Command Context Menu Data Table Date Picker Dialog Direction Drawer Dropdown Menu Empty Field Hover Card Input Input Group Input OTP Item Kbd Label Menubar Native Select Navigation Menu Pagination Popover Progress Radio Group Resizable Scroll Area Select Separator Sheet Sidebar Skeleton Slider Sonner Spinner Switch Table Tabs Textarea Toast Toggle Toggle Group Tooltip Typography Get Started Installation components.json Package Imports Theming Dark Mode CLI Monorepo Skills JavaScript Figma llms.txt Legacy Docs Forms React Hook Form TanStack Form Formisch Registry Introduction Getting Started GitHub Registries Registry Directory Examples Namespaces Authentication MCP Server Open in v0 API Reference registry.json registry-item.json Monorepo Copy Page Previous Next Using shadcn/ui components and CLI in a monorepo. Until now, using shadcn/ui in a monorepo was a bit of a pain. You could add
components using the CLI, but you had to manage where the components
were installed and manually fix import paths.
 With the new monorepo support in the CLI, we&#x27;ve made it a lot easier to use
shadcn/ui in a monorepo.
 The CLI now understands the monorepo structure and will install the components,
dependencies and registry dependencies to the correct paths and handle imports
for you.
 Getting started #
 Create a new monorepo project # To create a new monorepo project, run the init command with the --monorepo flag. pnpm npm yarn bun pnpm dlx shadcn@latest init --monorepo Copy Then select the template you want to use. Copy ? Select a template ›
 ❯ Next.js
 Vite
 TanStack Start
 React Router
 Astro This will create a new monorepo project with two workspaces: web and ui ,
and Turborepo as the build system. Everything is set up for you, so you can start adding components to your project. Add components to your project # To add components to your project, run the add command in the path of your app . Copy cd apps/web pnpm npm yarn bun pnpm dlx shadcn@latest add [COMPONENT] Copy The CLI will figure out what type of component you are adding and install the
correct files to the correct path. For example, if you run npx shadcn@latest add button , the CLI will install the button component under packages/ui and update the import path for components in apps/web . If you run npx shadcn@latest add login-01 , the CLI will install the button , label , input and card components under packages/ui and the login-form component under apps/web/components . Importing components # You can import components from the @workspace/ui package as follows: Copy import { Button } from &quot;@workspace/ui/components/button&quot; You can also import hooks and utilities from the @workspace/ui package. Copy import { useTheme } from &quot;@workspace/ui/hooks/use-theme&quot;
 import { cn } from &quot;@workspace/ui/lib/utils&quot;
 File Structure #
 When you create a new monorepo project, the CLI will create the following file structure:
 Copy apps
 └── web # Your app goes here.
 ├── app
 │ └── page.tsx
 ├── components
 │ └── login-form.tsx
 ├── components.json
 └── package.json
 packages
 └── ui # Your components and dependencies are installed here.
 ├── src
 │ ├── components
 │ │ └── button.tsx
 │ ├── hooks
 │ ├── lib
 │ │ └── utils.ts
 │ └── styles
 │ └── globals.css
 ├── components.json
 └── package.json
 package.json
 turbo.json
 Requirements #

 Every workspace must have a components.json file. A package.json file tells npm how to install the dependencies. A components.json file tells the CLI how and where to install components.

 The components.json file must properly define aliases for the workspace. This tells the CLI how to import components, hooks, utilities, etc.

 apps/web/components.json Copy {
 &quot;$schema&quot; : &quot;https://ui.shadcn.com/schema.json&quot; ,
 &quot;style&quot; : &quot;radix-nova&quot; ,
 &quot;rsc&quot; : true ,
 &quot;tsx&quot; : true ,
 &quot;tailwind&quot; : {
 &quot;config&quot; : &quot;&quot; ,
 &quot;css&quot; : &quot;../../packages/ui/src/styles/globals.css&quot; ,
 &quot;baseColor&quot; : &quot;neutral&quot; ,
 &quot;cssVariables&quot; : true
 },
 &quot;iconLibrary&quot; : &quot;lucide&quot; ,
 &quot;aliases&quot; : {
 &quot;components&quot; : &quot;@/components&quot; ,
 &quot;hooks&quot; : &quot;@/hooks&quot; ,
 &quot;lib&quot; : &quot;@/lib&quot; ,
 &quot;utils&quot; : &quot;@workspace/ui/lib/utils&quot; ,
 &quot;ui&quot; : &quot;@workspace/ui/components&quot;
 }
 }
 packages/ui/components.json Copy {
 &quot;$schema&quot; : &quot;https://ui.shadcn.com/schema.json&quot; ,
 &quot;style&quot; : &quot;radix-nova&quot; ,
 &quot;rsc&quot; : true ,
 &quot;tsx&quot; : true ,
 &quot;tailwind&quot; : {
 &quot;config&quot; : &quot;&quot; ,
 &quot;css&quot; : &quot;src/styles/globals.css&quot; ,
 &quot;baseColor&quot; : &quot;neutral&quot; ,
 &quot;cssVariables&quot; : true
 },
 &quot;iconLibrary&quot; : &quot;lucide&quot; ,
 &quot;aliases&quot; : {
 &quot;components&quot; : &quot;@workspace/ui/components&quot; ,
 &quot;utils&quot; : &quot;@workspace/ui/lib/utils&quot; ,
 &quot;hooks&quot; : &quot;@workspace/ui/hooks&quot; ,
 &quot;lib&quot; : &quot;@workspace/ui/lib&quot; ,
 &quot;ui&quot; : &quot;@workspace/ui/components&quot;
 }
 }

 Ensure you have the same style , iconLibrary and baseColor in both components.json files.

 For Tailwind CSS v4, leave the tailwind config empty in the components.json file.

 By following these requirements, the CLI will be able to install ui components, blocks, libs and hooks to the correct paths and handle imports for you.
 package.json#imports works well for package-local aliases inside a
workspace, for example inside packages/ui . For shared workspace imports such
as @workspace/ui/components , keep explicit aliases in components.json . The
CLI uses those aliases to route files across workspace boundaries.
 Using package.json#imports #
 For a monorepo that uses package imports and does not rely on
 tsconfig.json paths , use:

 local #... aliases for files inside each workspace
 workspace package exports for shared imports such as
 @workspace/ui/components

 For example, an app workspace can use local package imports:
 apps/web/package.json Copy {
 &quot;name&quot; : &quot;web&quot; ,
 &quot;private&quot; : true ,
 &quot;type&quot; : &quot;module&quot; ,
 &quot;imports&quot; : {
 &quot;#components/*&quot; : &quot;./src/components/*.tsx&quot; ,
 &quot;#lib/*&quot; : &quot;./src/lib/*.ts&quot; ,
 &quot;#hooks/*&quot; : &quot;./src/hooks/*.ts&quot;
 },
 &quot;dependencies&quot; : {
 &quot;@workspace/ui&quot; : &quot;workspace:*&quot;
 }
 }
 apps/web/components.json Copy {
 &quot;aliases&quot; : {
 &quot;components&quot; : &quot;#components&quot; ,
 &quot;ui&quot; : &quot;@workspace/ui/components&quot; ,
 &quot;lib&quot; : &quot;#lib&quot; ,
 &quot;hooks&quot; : &quot;#hooks&quot; ,
 &quot;utils&quot; : &quot;@workspace/ui/lib/utils&quot;
 }
 }
 And the shared UI package can expose its install targets with exports :
 packages/ui/package.json Copy {
 &quot;name&quot; : &quot;@workspace/ui&quot; ,
 &quot;private&quot; : true ,
 &quot;type&quot; : &quot;module&quot; ,
 &quot;imports&quot; : {
 &quot;#components/*&quot; : &quot;./src/components/*.tsx&quot; ,
 &quot;#lib/*&quot; : &quot;./src/lib/*.ts&quot; ,
 &quot;#hooks/*&quot; : &quot;./src/hooks/*.ts&quot;
 },
 &quot;exports&quot; : {
 &quot;./globals.css&quot; : &quot;./src/styles/globals.css&quot; ,
 &quot;./components/*&quot; : &quot;./src/components/*.tsx&quot; ,
 &quot;./lib/*&quot; : &quot;./src/lib/*.ts&quot; ,
 &quot;./hooks/*&quot; : &quot;./src/hooks/*.ts&quot;
 }
 }
 packages/ui/components.json Copy {
 &quot;aliases&quot; : {
 &quot;components&quot; : &quot;#components&quot; ,
 &quot;ui&quot; : &quot;#components&quot; ,
 &quot;lib&quot; : &quot;#lib&quot; ,
 &quot;hooks&quot; : &quot;#hooks&quot; ,
 &quot;utils&quot; : &quot;#lib/utils&quot;
 }
 }
 In this setup:

 files added from the app to the shared UI package are routed through
 @workspace/ui/...
 files added inside packages/ui use the package-local #... aliases
 the shared package must export any path referenced by another workspace

 For framework-specific package import setup, see the package imports guide . CLI Skills On This Page Getting started Create a new monorepo project Add components to your project Importing components File Structure Requirements Using package.json#imports Deploy your shadcn/ui app on Vercel Trusted by OpenAI, Sonos, Adobe, and more. Vercel provides tools and infrastructure to deploy apps and features at scale. Deploy Now Deploy to Vercel Built by shadcn at Vercel . The source code is available on GitHub . Get Code
