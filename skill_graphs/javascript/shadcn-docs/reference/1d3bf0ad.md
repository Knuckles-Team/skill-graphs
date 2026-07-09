Next.js - shadcn/ui Toggle Menu Menu Home Docs Components Blocks Charts Directory Create Search documentation... Search... 117k Toggle theme New Sections Introduction Components Installation Theming CLI RTL Skills MCP Server Registry Forms Changelog Components Accordion Alert Alert Dialog Aspect Ratio Avatar Badge Breadcrumb Button Button Group Calendar Card Carousel Chart Checkbox Collapsible Combobox Command Context Menu Data Table Date Picker Dialog Direction Drawer Dropdown Menu Empty Field Hover Card Input Input Group Input OTP Item Kbd Label Menubar Native Select Navigation Menu Pagination Popover Progress Radio Group Resizable Scroll Area Select Separator Sheet Sidebar Skeleton Slider Sonner Spinner Switch Table Tabs Textarea Toast Toggle Toggle Group Tooltip Typography Get Started Installation components.json Package Imports Theming Dark Mode CLI Monorepo Skills JavaScript Figma llms.txt Legacy Docs Forms React Hook Form TanStack Form Formisch Registry Introduction Getting Started GitHub Registries Registry Directory Examples Namespaces Authentication MCP Server Open in v0 API Reference registry.json registry-item.json Next.js Copy Page Previous Next Install and configure shadcn/ui for Next.js. Choose the setup that matches your starting point.
 Use shadcn/create Build your preset and generate a Next.js project command. Use the CLI Scaffold a new Next.js project directly from the terminal. Existing Project Configure shadcn/ui manually in an existing Next.js project.

 Use shadcn/create #
 Build Your Preset # Open shadcn/create and build your preset visually. Choose your style, colors, fonts, icons, and more. Open shadcn/create Create Project # Click Create Project , choose your package manager, and copy the generated command. The generated command will look similar to this: pnpm npm yarn bun pnpm dlx shadcn@latest init --preset [CODE] --template next Copy The exact command will include your selected options such as --base , --monorepo , or --rtl . Add Components # Add the Card component to your project: pnpm npm yarn bun pnpm dlx shadcn@latest add card Copy If you created a monorepo, run the command from apps/web or specify the workspace from the repo root: pnpm npm yarn bun pnpm dlx shadcn@latest add card -c apps/web Copy The command above will add the Card component to your project. You can then import it like this: app/page.tsx Copy import {
 Card,
 CardContent,
 CardDescription,
 CardHeader,
 CardTitle,
 } from &quot;@/components/ui/card&quot;

 export default function Home () {
 return (
 &lt; Card className = &quot;max-w-sm&quot; &gt;
 &lt; CardHeader &gt;
 &lt; CardTitle &gt;Project Overview&lt;/ CardTitle &gt;
 &lt; CardDescription &gt;
 Track progress and recent activity for your Next.js app.
 &lt;/ CardDescription &gt;
 &lt;/ CardHeader &gt;
 &lt; CardContent &gt;
 Your design system is ready. Start building your next component.
 &lt;/ CardContent &gt;
 &lt;/ Card &gt;
 )
 } If you created a monorepo, update apps/web/app/page.tsx and import from @workspace/ui/components/card instead.

 Use the CLI #
 Create Project # Run the init command to scaffold a new Next.js project. Follow the prompts to configure your project: base, preset, monorepo, and more. pnpm npm yarn bun pnpm dlx shadcn@latest init -t next Copy For a monorepo project, use --monorepo flag: pnpm npm yarn bun pnpm dlx shadcn@latest init -t next --monorepo Copy Add Components # Add the Card component to your project: pnpm npm yarn bun pnpm dlx shadcn@latest add card Copy If you created a monorepo, run the command from apps/web or specify the workspace from the repo root: pnpm npm yarn bun pnpm dlx shadcn@latest add card -c apps/web Copy The command above will add the Card component to your project. You can then import it like this: app/page.tsx Copy import {
 Card,
 CardContent,
 CardDescription,
 CardHeader,
 CardTitle,
 } from &quot;@/components/ui/card&quot;

 export default function Home () {
 return (
 &lt; Card className = &quot;max-w-sm&quot; &gt;
 &lt; CardHeader &gt;
 &lt; CardTitle &gt;Project Overview&lt;/ CardTitle &gt;
 &lt; CardDescription &gt;
 Track progress and recent activity for your Next.js app.
 &lt;/ CardDescription &gt;
 &lt;/ CardHeader &gt;
 &lt; CardContent &gt;
 Your design system is ready. Start building your next component.
 &lt;/ CardContent &gt;
 &lt;/ Card &gt;
 )
 } If you created a monorepo, update apps/web/app/page.tsx and import from @workspace/ui/components/card instead.

 Existing Project #
 Create Project # If you need a new Next.js project, create one with create-next-app . Otherwise, skip this step. pnpm npm yarn bun pnpm create next-app@latest Copy Choose the recommended defaults so Tailwind CSS, the App Router, and the default @/* import alias are configured for you. If you prefer a src/ directory, use --src-dir or choose Yes when prompted: pnpm npm yarn bun pnpm create next-app@latest --src-dir Copy With --src-dir , Next.js places your app in src/app and configures the @/* alias to point to ./src/* . Configure Tailwind CSS and Import Aliases # If you created your project with the recommended create-next-app defaults, you can skip this step. If you&#x27;re adding shadcn/ui to an older or custom Next.js app, make sure Tailwind CSS is installed first. You can follow the official Next.js installation guide . Then make sure your tsconfig.json includes the @/* import alias: tsconfig.json Copy {
 &quot;compilerOptions&quot; : {
 &quot;paths&quot; : {
 &quot;@/*&quot; : [ &quot;./*&quot; ]
 }
 }
 } If you used --src-dir , point the alias to ./src/* instead. Run the CLI # Run the shadcn init command to set up shadcn/ui in your project. pnpm npm yarn bun pnpm dlx shadcn@latest init Copy Add Components # You can now start adding components to your project. pnpm npm yarn bun pnpm dlx shadcn@latest add button Copy The command above will add the Button component to your project. You can then import it like this: app/page.tsx Copy import { Button } from &quot;@/components/ui/button&quot;

 export default function Home () {
 return (
 &lt; div className = &quot;flex min-h-svh items-center justify-center&quot; &gt;
 &lt; Button &gt;Click me&lt;/ Button &gt;
 &lt;/ div &gt;
 )
 } If you used --src-dir , add the component to src/app/page.tsx instead. Installation Vite On This Page Use shadcn/create Build Your Preset Create Project Add Components Use the CLI Create Project Add Components Existing Project Create Project Configure Tailwind CSS and Import Aliases Run the CLI Add Components Deploy your shadcn/ui app on Vercel Trusted by OpenAI, Sonos, Adobe, and more. Vercel provides tools and infrastructure to deploy apps and features at scale. Deploy Now Deploy to Vercel Built by shadcn at Vercel . The source code is available on GitHub . Get Code
