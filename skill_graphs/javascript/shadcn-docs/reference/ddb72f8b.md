Hover Card - shadcn/ui Toggle Menu Menu Home Docs Components Blocks Charts Directory Create Search documentation... Search... 117k Toggle theme New Sections Introduction Components Installation Theming CLI RTL Skills MCP Server Registry Forms Changelog Components Accordion Alert Alert Dialog Aspect Ratio Avatar Badge Breadcrumb Button Button Group Calendar Card Carousel Chart Checkbox Collapsible Combobox Command Context Menu Data Table Date Picker Dialog Direction Drawer Dropdown Menu Empty Field Hover Card Input Input Group Input OTP Item Kbd Label Menubar Native Select Navigation Menu Pagination Popover Progress Radio Group Resizable Scroll Area Select Separator Sheet Sidebar Skeleton Slider Sonner Spinner Switch Table Tabs Textarea Toast Toggle Toggle Group Tooltip Typography Get Started Installation components.json Package Imports Theming Dark Mode CLI Monorepo Skills JavaScript Figma llms.txt Legacy Docs Forms React Hook Form TanStack Form Formisch Registry Introduction Getting Started GitHub Registries Registry Directory Examples Namespaces Authentication MCP Server Open in v0 API Reference registry.json registry-item.json Hover Card Copy Page Previous Next For sighted users to preview content available behind a link. Radix UI Base UI Radix UI Hover Here Copy import { Button } from "@/components/ui/button"
 import {
 HoverCard, View Code
 Installation #
 Command Manual pnpm npm yarn bun pnpm dlx shadcn@latest add hover-card Copy
 Usage #
 Copy import {
 HoverCard,
 HoverCardContent,
 HoverCardTrigger,
 } from &quot;@/components/ui/hover-card&quot;
 Copy &lt; HoverCard &gt;
 &lt; HoverCardTrigger &gt;Hover&lt;/ HoverCardTrigger &gt;
 &lt; HoverCardContent &gt;
 The React Framework – created and maintained by @vercel.
 &lt;/ HoverCardContent &gt;
 &lt;/ HoverCard &gt;
 Composition #
 Use the following composition to build a HoverCard :
 Copy HoverCard
 ├── HoverCardTrigger
 └── HoverCardContent
 Trigger Delays #
 Use openDelay and closeDelay on the HoverCard to control when the card opens and
closes.
 Copy &lt; HoverCard openDelay = { 100 } closeDelay = { 200 } &gt;
 &lt; HoverCardTrigger &gt;Hover&lt;/ HoverCardTrigger &gt;
 &lt; HoverCardContent &gt;Content&lt;/ HoverCardContent &gt;
 &lt;/ HoverCard &gt;
 Positioning #
 Use the side and align props on HoverCardContent to control placement.
 Copy &lt; HoverCard &gt;
 &lt; HoverCardTrigger &gt;Hover&lt;/ HoverCardTrigger &gt;
 &lt; HoverCardContent side = &quot;top&quot; align = &quot;start&quot; &gt;
 Content
 &lt;/ HoverCardContent &gt;
 &lt;/ HoverCard &gt;
 Examples #
 Basic #
 Hover Here Copy import { Button } from "@/components/ui/button"
 import {
 HoverCard, View Code
 Sides #
 left top bottom right Copy import { Button } from "@/components/ui/button"
 import {
 HoverCard, View Code
 RTL #
 To enable RTL support in shadcn/ui, see the RTL configuration guide .
 Arabic (العربية) ▼ Toggle يسار أعلى أسفل يمين Copy "use client"

 import { View Code
 API Reference #
 See the Radix UI documentation for more information. Field Input On This Page Installation Usage Composition Trigger Delays Positioning Examples Basic Sides RTL API Reference Deploy your shadcn/ui app on Vercel Trusted by OpenAI, Sonos, Adobe, and more. Vercel provides tools and infrastructure to deploy apps and features at scale. Deploy Now Deploy to Vercel Built by shadcn at Vercel . The source code is available on GitHub . Get Code
