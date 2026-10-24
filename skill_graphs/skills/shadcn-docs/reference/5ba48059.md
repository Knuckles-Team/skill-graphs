Collapsible - shadcn/ui Toggle Menu Menu Home Docs Components Blocks Charts Directory Create Search documentation... Search... 117k Toggle theme New Sections Introduction Components Installation Theming CLI RTL Skills MCP Server Registry Forms Changelog Components Accordion Alert Alert Dialog Aspect Ratio Avatar Badge Breadcrumb Button Button Group Calendar Card Carousel Chart Checkbox Collapsible Combobox Command Context Menu Data Table Date Picker Dialog Direction Drawer Dropdown Menu Empty Field Hover Card Input Input Group Input OTP Item Kbd Label Menubar Native Select Navigation Menu Pagination Popover Progress Radio Group Resizable Scroll Area Select Separator Sheet Sidebar Skeleton Slider Sonner Spinner Switch Table Tabs Textarea Toast Toggle Toggle Group Tooltip Typography Get Started Installation components.json Package Imports Theming Dark Mode CLI Monorepo Skills JavaScript Figma llms.txt Legacy Docs Forms React Hook Form TanStack Form Formisch Registry Introduction Getting Started GitHub Registries Registry Directory Examples Namespaces Authentication MCP Server Open in v0 API Reference registry.json registry-item.json Collapsible Copy Page Previous Next An interactive component which expands/collapses a panel. Radix UI Base UI Radix UI Order #4189 Toggle details Status Shipped Copy "use client"

 import * as React from "react" View Code
 Installation #
 Command Manual pnpm npm yarn bun pnpm dlx shadcn@latest add collapsible Copy
 Usage #
 Copy import {
 Collapsible,
 CollapsibleContent,
 CollapsibleTrigger,
 } from &quot;@/components/ui/collapsible&quot;
 Copy &lt; Collapsible &gt;
 &lt; CollapsibleTrigger &gt;Can I use this in my project?&lt;/ CollapsibleTrigger &gt;
 &lt; CollapsibleContent &gt;
 Yes. Free to use for personal and commercial projects. No attribution
 required.
 &lt;/ CollapsibleContent &gt;
 &lt;/ Collapsible &gt;
 Composition #
 Use the following composition to build a Collapsible :
 Copy Collapsible
 ├── CollapsibleTrigger
 └── CollapsibleContent
 Controlled State #
 Use the open and onOpenChange props to control the state.
 Copy import * as React from &quot;react&quot;

 export function Example () {
 const [ open , setOpen ] = React. useState ( false )

 return (
 &lt; Collapsible open = { open } onOpenChange = { setOpen } &gt;
 &lt; CollapsibleTrigger &gt;Toggle&lt;/ CollapsibleTrigger &gt;
 &lt; CollapsibleContent &gt;Content&lt;/ CollapsibleContent &gt;
 &lt;/ Collapsible &gt;
 )
 }
 Examples #
 Basic #
 Product details Copy import { ChevronDownIcon } from "@/registry/icons/__lucide__"
 import { Button } from "@/components/ui/button"
 import { Card, CardContent } from "@/components/ui/card" View Code
 Settings Panel #
 Use a trigger button to reveal additional settings.
 Radius Set the corner radius of the element. Radius X Radius Y Copy "use client"

 import * as React from "react" View Code
 File Tree #
 Use nested collapsibles to build a file tree.
 Explorer Outline components lib hooks types public app.tsx layout.tsx globals.css package.json tsconfig.json README.md .gitignore Copy import { ChevronRightIcon, FileIcon, FolderIcon } from "lucide-react"

 import { Button } from "@/components/ui/button" View Code
 RTL #
 To enable RTL support in shadcn/ui, see the RTL configuration guide .
 Arabic (العربية) ▼ Toggle الطلب #4189 Toggle details الحالة تم الشحن Copy "use client"

 import * as React from "react" View Code
 API Reference #
 See the Radix UI documentation for more information. Checkbox Combobox On This Page Installation Usage Composition Controlled State Examples Basic Settings Panel File Tree RTL API Reference Deploy your shadcn/ui app on Vercel Trusted by OpenAI, Sonos, Adobe, and more. Vercel provides tools and infrastructure to deploy apps and features at scale. Deploy Now Deploy to Vercel Built by shadcn at Vercel . The source code is available on GitHub . Get Code
