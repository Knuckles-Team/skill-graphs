TanStack Router - shadcn/ui Toggle Menu Menu Home Docs Components Blocks Charts Directory Create Search documentation... Search... 117k Toggle theme New Sections Introduction Components Installation Theming CLI RTL Skills MCP Server Registry Forms Changelog Components Accordion Alert Alert Dialog Aspect Ratio Avatar Badge Breadcrumb Button Button Group Calendar Card Carousel Chart Checkbox Collapsible Combobox Command Context Menu Data Table Date Picker Dialog Direction Drawer Dropdown Menu Empty Field Hover Card Input Input Group Input OTP Item Kbd Label Menubar Native Select Navigation Menu Pagination Popover Progress Radio Group Resizable Scroll Area Select Separator Sheet Sidebar Skeleton Slider Sonner Spinner Switch Table Tabs Textarea Toast Toggle Toggle Group Tooltip Typography Get Started Installation components.json Package Imports Theming Dark Mode CLI Monorepo Skills JavaScript Figma llms.txt Legacy Docs Forms React Hook Form TanStack Form Formisch Registry Introduction Getting Started GitHub Registries Registry Directory Examples Namespaces Authentication MCP Server Open in v0 API Reference registry.json registry-item.json TanStack Router Copy Page Previous Next Install and configure shadcn/ui for TanStack Router. Create project # Start by creating a new TanStack Router project: pnpm npm yarn bun pnpm create tsrouter-app@latest my-app --template file-router --tailwind --add-ons shadcn Copy Add Components # You can now start adding components to your project. pnpm npm yarn bun pnpm dlx shadcn@latest add button Copy The command above will add the Button component to your project. You can then import it like this: src/routes/index.tsx Copy import { createFileRoute } from &quot;@tanstack/react-router&quot;

 import { Button } from &quot;@/components/ui/button&quot;

 export const Route = createFileRoute ( &quot;/&quot; )({
 component: App,
 })

 function App () {
 return (
 &lt; div &gt;
 &lt; Button &gt;Click me&lt;/ Button &gt;
 &lt;/ div &gt;
 )
 } TanStack Start Manual Installation On This Page Create project Add Components Deploy your shadcn/ui app on Vercel Trusted by OpenAI, Sonos, Adobe, and more. Vercel provides tools and infrastructure to deploy apps and features at scale. Deploy Now Deploy to Vercel Built by shadcn at Vercel . The source code is available on GitHub . Get Code
