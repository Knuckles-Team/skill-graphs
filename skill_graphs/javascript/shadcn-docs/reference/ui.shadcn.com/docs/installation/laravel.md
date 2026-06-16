Laravel - shadcn/ui Toggle Menu Menu Home Docs Components Blocks Charts Directory Create Search documentation... Search... 117k Toggle theme New Sections Introduction Components Installation Theming CLI RTL Skills MCP Server Registry Forms Changelog Components Accordion Alert Alert Dialog Aspect Ratio Avatar Badge Breadcrumb Button Button Group Calendar Card Carousel Chart Checkbox Collapsible Combobox Command Context Menu Data Table Date Picker Dialog Direction Drawer Dropdown Menu Empty Field Hover Card Input Input Group Input OTP Item Kbd Label Menubar Native Select Navigation Menu Pagination Popover Progress Radio Group Resizable Scroll Area Select Separator Sheet Sidebar Skeleton Slider Sonner Spinner Switch Table Tabs Textarea Toast Toggle Toggle Group Tooltip Typography Get Started Installation components.json Package Imports Theming Dark Mode CLI Monorepo Skills JavaScript Figma llms.txt Legacy Docs Forms React Hook Form TanStack Form Formisch Registry Introduction Getting Started GitHub Registries Registry Directory Examples Namespaces Authentication MCP Server Open in v0 API Reference registry.json registry-item.json Laravel Copy Page Previous Next Install and configure shadcn/ui for Laravel. The shadcn CLI does not scaffold a new Laravel app. Start by creating a Laravel app with the React starter kit, then choose how you want to configure shadcn/ui.
 Create Project # Create a new Laravel app using the Laravel installer: Copy laravel new my-app If you already have a Laravel app with React and Inertia configured, skip this step. Choose the React starter kit when prompted. For more information, see the official Laravel frontend documentation . Then move into your project directory: Copy cd my-app
 Use shadcn/create Build your preset visually and generate a Laravel init command. Use the CLI Configure shadcn/ui in your Laravel app directly from the terminal.

 Use shadcn/create #
 Build Your Preset # Open shadcn/create and build your preset visually. Choose your style, colors, fonts, icons, and more. Open shadcn/create Run the Command # Click Create Project , choose your package manager, and copy the generated command. The generated command will look similar to this: pnpm npm yarn bun pnpm dlx shadcn@latest init --preset [CODE] --template laravel Copy Run the command from the root of your Laravel app. When asked to overwrite components.json and components, choose Yes . Add Components # Add the Switch component to your project: pnpm npm yarn bun pnpm dlx shadcn@latest add switch Copy The command above will add the Switch component to resources/js/components/ui/switch.tsx . You can then import it like this: resources/js/pages/index.tsx Copy import { Switch } from &quot;@/components/ui/switch&quot;

 const MyPage = () =&gt; {
 return (
 &lt; div &gt;
 &lt; Switch /&gt;
 &lt;/ div &gt;
 )
 }

 export default MyPage

 Use the CLI #
 Run the CLI # Run the shadcn init command from the root of your Laravel app: pnpm npm yarn bun pnpm dlx shadcn@latest init Copy When asked to overwrite components.json and components, choose Yes . Add Components # Add the Switch component to your project: pnpm npm yarn bun pnpm dlx shadcn@latest add switch Copy The command above will add the Switch component to resources/js/components/ui/switch.tsx . You can then import it like this: resources/js/pages/index.tsx Copy import { Switch } from &quot;@/components/ui/switch&quot;

 const MyPage = () =&gt; {
 return (
 &lt; div &gt;
 &lt; Switch /&gt;
 &lt;/ div &gt;
 )
 }

 export default MyPage Vite React Router On This Page Create Project Use shadcn/create Build Your Preset Run the Command Add Components Use the CLI Run the CLI Add Components Deploy your shadcn/ui app on Vercel Trusted by OpenAI, Sonos, Adobe, and more. Vercel provides tools and infrastructure to deploy apps and features at scale. Deploy Now Deploy to Vercel Built by shadcn at Vercel . The source code is available on GitHub . Get Code
