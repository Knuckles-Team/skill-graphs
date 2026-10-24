Vite - shadcn/ui Toggle Menu Menu Home Docs Components Blocks Charts Directory Create Search documentation... Search... 117k Toggle theme New Sections Introduction Components Installation Theming CLI RTL Skills MCP Server Registry Forms Changelog Components Accordion Alert Alert Dialog Aspect Ratio Avatar Badge Breadcrumb Button Button Group Calendar Card Carousel Chart Checkbox Collapsible Combobox Command Context Menu Data Table Date Picker Dialog Direction Drawer Dropdown Menu Empty Field Hover Card Input Input Group Input OTP Item Kbd Label Menubar Native Select Navigation Menu Pagination Popover Progress Radio Group Resizable Scroll Area Select Separator Sheet Sidebar Skeleton Slider Sonner Spinner Switch Table Tabs Textarea Toast Toggle Toggle Group Tooltip Typography Get Started Installation components.json Package Imports Theming Dark Mode CLI Monorepo Skills JavaScript Figma llms.txt Legacy Docs Forms React Hook Form TanStack Form Formisch Registry Introduction Getting Started GitHub Registries Registry Directory Examples Namespaces Authentication MCP Server Open in v0 API Reference registry.json registry-item.json Vite Copy Page Previous Next Install and configure shadcn/ui for Vite. Choose the setup that matches your starting point.
 Use shadcn/create Build your preset and generate a Vite project command. Use the CLI Scaffold a new Vite project directly from the terminal. Existing Project Configure shadcn/ui manually in an existing Vite project.

 Use shadcn/create #
 Build Your Preset # Open shadcn/create and build your preset visually. Choose your style, colors, fonts, icons, and more. Open shadcn/create Create Project # Click Create Project , choose your package manager, and copy the generated command. The generated command will look similar to this: pnpm npm yarn bun pnpm dlx shadcn@latest init --preset [CODE] --template vite Copy The exact command will include your selected options such as --base , --monorepo , or --rtl . Add Components # Add the Card component to your project: pnpm npm yarn bun pnpm dlx shadcn@latest add card Copy If you created a monorepo, run the command from apps/web or specify the workspace from the repo root: pnpm npm yarn bun pnpm dlx shadcn@latest add card -c apps/web Copy The command above will add the Card component to your project. You can then import it like this: src/App.tsx Copy import {
 Card,
 CardContent,
 CardDescription,
 CardHeader,
 CardTitle,
 } from &quot;@/components/ui/card&quot;

 function App () {
 return (
 &lt; Card className = &quot;max-w-sm&quot; &gt;
 &lt; CardHeader &gt;
 &lt; CardTitle &gt;Project Overview&lt;/ CardTitle &gt;
 &lt; CardDescription &gt;
 Track progress and recent activity for your Vite app.
 &lt;/ CardDescription &gt;
 &lt;/ CardHeader &gt;
 &lt; CardContent &gt;
 Your design system is ready. Start building your next component.
 &lt;/ CardContent &gt;
 &lt;/ Card &gt;
 )
 }

 export default App If you created a monorepo, update apps/web/src/App.tsx and import from @workspace/ui/components/card instead.

 Use the CLI #
 Create Project # Run the init command to scaffold a new Vite project. Follow the prompts to configure your project: base, preset, monorepo, and more. pnpm npm yarn bun pnpm dlx shadcn@latest init -t vite Copy For a monorepo project, use --monorepo flag: pnpm npm yarn bun pnpm dlx shadcn@latest init -t vite --monorepo Copy Add Components # Add the Card component to your project: pnpm npm yarn bun pnpm dlx shadcn@latest add card Copy If you created a monorepo, run the command from apps/web or specify the workspace from the repo root: pnpm npm yarn bun pnpm dlx shadcn@latest add card -c apps/web Copy The command above will add the Card component to your project. You can then import it like this: src/App.tsx Copy import {
 Card,
 CardContent,
 CardDescription,
 CardHeader,
 CardTitle,
 } from &quot;@/components/ui/card&quot;

 function App () {
 return (
 &lt; Card className = &quot;max-w-sm&quot; &gt;
 &lt; CardHeader &gt;
 &lt; CardTitle &gt;Project Overview&lt;/ CardTitle &gt;
 &lt; CardDescription &gt;
 Track progress and recent activity for your Vite app.
 &lt;/ CardDescription &gt;
 &lt;/ CardHeader &gt;
 &lt; CardContent &gt;
 Your design system is ready. Start building your next component.
 &lt;/ CardContent &gt;
 &lt;/ Card &gt;
 )
 }

 export default App If you created a monorepo, update apps/web/src/App.tsx and import from @workspace/ui/components/card instead.

 Existing Project #
 Create Project # If you need a new Vite project, create one first and select the React + TypeScript template. Otherwise, skip this step. pnpm npm yarn bun pnpm create vite@latest Copy Add Tailwind CSS # If your project already has Tailwind CSS configured, skip this step. pnpm npm yarn bun pnpm add tailwindcss @tailwindcss/vite Copy Replace everything in src/index.css with the following: src/index.css Copy @import &quot;tailwindcss&quot; ; Edit tsconfig.json file # If your project already has the @/* alias configured, skip this step. Vite splits TypeScript configuration across multiple files. Add the baseUrl and paths properties to the compilerOptions section of tsconfig.json and tsconfig.app.json : tsconfig.json Copy {
 &quot;files&quot; : [],
 &quot;references&quot; : [
 {
 &quot;path&quot; : &quot;./tsconfig.app.json&quot;
 },
 {
 &quot;path&quot; : &quot;./tsconfig.node.json&quot;
 }
 ],
 &quot;compilerOptions&quot; : {
 &quot;baseUrl&quot; : &quot;.&quot; ,
 &quot;paths&quot; : {
 &quot;@/*&quot; : [ &quot;./src/*&quot; ]
 }
 }
 } Edit tsconfig.app.json file # Add the same alias to tsconfig.app.json so your editor can resolve imports: tsconfig.app.json Copy {
 &quot;compilerOptions&quot; : {
 // ...
 &quot;baseUrl&quot; : &quot;.&quot; ,
 &quot;paths&quot; : {
 &quot;@/*&quot; : [
 &quot;./src/*&quot;
 ]
 }
 // ...
 }
 } Update vite.config.ts # Install @types/node and update vite.config.ts so Vite can resolve the @ alias: pnpm npm yarn bun pnpm add -D @types/node Copy vite.config.ts Copy import path from &quot;path&quot;
 import tailwindcss from &quot;@tailwindcss/vite&quot;
 import react from &quot;@vitejs/plugin-react&quot;
 import { defineConfig } from &quot;vite&quot;

 // https://vite.dev/config/
 export default defineConfig ({
 plugins: [ react (), tailwindcss ()] ,
 resolve: {
 alias: {
 &quot;@&quot; : path. resolve (__dirname, &quot;./src&quot; ),
 },
 } ,
 }) Run the CLI # Run the shadcn init command to set up shadcn/ui in your project: pnpm npm yarn bun pnpm dlx shadcn@latest init Copy Add Components # You can now start adding components to your project. pnpm npm yarn bun pnpm dlx shadcn@latest add button Copy The command above will add the Button component to your project. You can then import it like this: src/App.tsx Copy import { Button } from &quot;@/components/ui/button&quot;

 function App () {
 return (
 &lt; div className = &quot;flex min-h-svh flex-col items-center justify-center&quot; &gt;
 &lt; Button &gt;Click me&lt;/ Button &gt;
 &lt;/ div &gt;
 )
 }

 export default App Next.js Laravel On This Page Use shadcn/create Build Your Preset Create Project Add Components Use the CLI Create Project Add Components Existing Project Create Project Add Tailwind CSS Edit tsconfig.json file Edit tsconfig.app.json file Update vite.config.ts Run the CLI Add Components Deploy your shadcn/ui app on Vercel Trusted by OpenAI, Sonos, Adobe, and more. Vercel provides tools and infrastructure to deploy apps and features at scale. Deploy Now Deploy to Vercel Built by shadcn at Vercel . The source code is available on GitHub . Get Code
