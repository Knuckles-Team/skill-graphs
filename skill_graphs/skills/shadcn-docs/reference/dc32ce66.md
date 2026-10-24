Astro - shadcn/ui Toggle Menu Menu Home Docs Components Blocks Charts Directory Create Search documentation... Search... 117k Toggle theme New Sections Introduction Components Installation Theming CLI RTL Skills MCP Server Registry Forms Changelog Components Accordion Alert Alert Dialog Aspect Ratio Avatar Badge Breadcrumb Button Button Group Calendar Card Carousel Chart Checkbox Collapsible Combobox Command Context Menu Data Table Date Picker Dialog Direction Drawer Dropdown Menu Empty Field Hover Card Input Input Group Input OTP Item Kbd Label Menubar Native Select Navigation Menu Pagination Popover Progress Radio Group Resizable Scroll Area Select Separator Sheet Sidebar Skeleton Slider Sonner Spinner Switch Table Tabs Textarea Toast Toggle Toggle Group Tooltip Typography Get Started Installation components.json Package Imports Theming Dark Mode CLI Monorepo Skills JavaScript Figma llms.txt Legacy Docs Forms React Hook Form TanStack Form Formisch Registry Introduction Getting Started GitHub Registries Registry Directory Examples Namespaces Authentication MCP Server Open in v0 API Reference registry.json registry-item.json Astro Copy Page Previous Next Install and configure shadcn/ui for Astro. Choose the setup that matches your starting point.
 Use shadcn/create Build your preset and generate an Astro project command. Use the CLI Scaffold a new Astro project directly from the terminal. Existing Project Configure shadcn/ui manually in an existing Astro project.

 Use shadcn/create #
 Build Your Preset # Open shadcn/create and build your preset visually. Choose your style, colors, fonts, icons, and more. Open shadcn/create Create Project # Click Create Project , choose your package manager, and copy the generated command. The generated command will look similar to this: pnpm npm yarn bun pnpm dlx shadcn@latest init --preset [CODE] --template astro Copy The exact command will include your selected options such as --base , --monorepo , or --rtl . Add Components # Add the Card component to your project: pnpm npm yarn bun pnpm dlx shadcn@latest add card Copy If you created a monorepo, run the command from apps/web or specify the workspace from the repo root: pnpm npm yarn bun pnpm dlx shadcn@latest add card -c apps/web Copy The command above will add the Card component to your project. You can then import it like this: src/pages/index.astro Copy ---
 import Layout from &quot;@/layouts/main.astro&quot;
 import {
 Card,
 CardContent,
 CardDescription,
 CardHeader,
 CardTitle,
 } from &quot;@/components/ui/card&quot;
 ---

 &lt; Layout &gt;
 &lt; Card className = &quot;max-w-sm&quot; &gt;
 &lt; CardHeader &gt;
 &lt; CardTitle &gt;Project Overview&lt;/ CardTitle &gt;
 &lt; CardDescription &gt;
 Track progress and recent activity for your Astro app.
 &lt;/ CardDescription &gt;
 &lt;/ CardHeader &gt;
 &lt; CardContent &gt;
 Your design system is ready. Start building your next component.
 &lt;/ CardContent &gt;
 &lt;/ Card &gt;
 &lt;/ Layout &gt; If you created a monorepo, update apps/web/src/pages/index.astro and import from @workspace/ui/components/card instead. The monorepo layout at apps/web/src/layouts/main.astro already imports @workspace/ui/globals.css for you.

 Use the CLI #
 Create Project # Run the init command to scaffold a new Astro project. Follow the prompts to configure your project: base, preset, monorepo, and more. pnpm npm yarn bun pnpm dlx shadcn@latest init -t astro Copy For a monorepo project, use --monorepo flag: pnpm npm yarn bun pnpm dlx shadcn@latest init -t astro --monorepo Copy Add Components # Add the Card component to your project: pnpm npm yarn bun pnpm dlx shadcn@latest add card Copy If you created a monorepo, run the command from apps/web or specify the workspace from the repo root: pnpm npm yarn bun pnpm dlx shadcn@latest add card -c apps/web Copy The command above will add the Card component to your project. You can then import it like this: src/pages/index.astro Copy ---
 import Layout from &quot;@/layouts/main.astro&quot;
 import {
 Card,
 CardContent,
 CardDescription,
 CardHeader,
 CardTitle,
 } from &quot;@/components/ui/card&quot;
 ---

 &lt; Layout &gt;
 &lt; Card className = &quot;max-w-sm&quot; &gt;
 &lt; CardHeader &gt;
 &lt; CardTitle &gt;Project Overview&lt;/ CardTitle &gt;
 &lt; CardDescription &gt;
 Track progress and recent activity for your Astro app.
 &lt;/ CardDescription &gt;
 &lt;/ CardHeader &gt;
 &lt; CardContent &gt;
 Your design system is ready. Start building your next component.
 &lt;/ CardContent &gt;
 &lt;/ Card &gt;
 &lt;/ Layout &gt; If you created a monorepo, update apps/web/src/pages/index.astro and import from @workspace/ui/components/card instead. The monorepo layout at apps/web/src/layouts/main.astro already imports @workspace/ui/globals.css for you.

 Existing Project #
 Create Project # If you need a new Astro project, create one first. Otherwise, skip this step. pnpm npm yarn bun pnpm create astro@latest astro-app -- --template with-tailwindcss --install --add react --git Copy This command sets up Tailwind CSS and the React integration for you. If you&#x27;re adding shadcn/ui to an older or custom Astro app, make sure both are configured before continuing. The Tailwind starter loads your global stylesheet through src/layouts/main.astro . Keep that layout in place, or make sure your page imports @/styles/global.css . Edit tsconfig.json file # If your project already has the @/* alias configured, skip this step. Add the following code to the tsconfig.json file to resolve paths: tsconfig.json Copy {
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
 } Run the CLI # Run the shadcn init command to set up your project: pnpm npm yarn bun pnpm dlx shadcn@latest init Copy Add Components # You can now start adding components to your project. pnpm npm yarn bun pnpm dlx shadcn@latest add button Copy The command above will add the Button component to your project. You can then import it like this: src/pages/index.astro Copy ---
 import Layout from &quot;@/layouts/main.astro&quot;
 import { Button } from &quot;@/components/ui/button&quot;
 ---

 &lt; Layout &gt;
 &lt; div class = &quot;grid h-screen place-items-center content-center&quot; &gt;
 &lt; Button &gt;Button&lt;/ Button &gt;
 &lt;/ div &gt;
 &lt;/ Layout &gt; Remix TanStack Start On This Page Use shadcn/create Build Your Preset Create Project Add Components Use the CLI Create Project Add Components Existing Project Create Project Edit tsconfig.json file Run the CLI Add Components Deploy your shadcn/ui app on Vercel Trusted by OpenAI, Sonos, Adobe, and more. Vercel provides tools and infrastructure to deploy apps and features at scale. Deploy Now Deploy to Vercel Built by shadcn at Vercel . The source code is available on GitHub . Get Code
