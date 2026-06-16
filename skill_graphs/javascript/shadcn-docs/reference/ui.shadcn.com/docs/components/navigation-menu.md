Navigation Menu - shadcn/ui Toggle Menu Menu Home Docs Components Blocks Charts Directory Create Search documentation... Search... 117k Toggle theme New Sections Introduction Components Installation Theming CLI RTL Skills MCP Server Registry Forms Changelog Components Accordion Alert Alert Dialog Aspect Ratio Avatar Badge Breadcrumb Button Button Group Calendar Card Carousel Chart Checkbox Collapsible Combobox Command Context Menu Data Table Date Picker Dialog Direction Drawer Dropdown Menu Empty Field Hover Card Input Input Group Input OTP Item Kbd Label Menubar Native Select Navigation Menu Pagination Popover Progress Radio Group Resizable Scroll Area Select Separator Sheet Sidebar Skeleton Slider Sonner Spinner Switch Table Tabs Textarea Toast Toggle Toggle Group Tooltip Typography Get Started Installation components.json Package Imports Theming Dark Mode CLI Monorepo Skills JavaScript Figma llms.txt Legacy Docs Forms React Hook Form TanStack Form Formisch Registry Introduction Getting Started GitHub Registries Registry Directory Examples Namespaces Authentication MCP Server Open in v0 API Reference registry.json registry-item.json Navigation Menu Copy Page Previous Next A collection of links for navigating websites. Radix UI Base UI Radix UI Getting started Components Docs Copy "use client"

 import * as React from "react" View Code
 Installation #
 Command Manual pnpm npm yarn bun pnpm dlx shadcn@latest add navigation-menu Copy
 Usage #
 Copy import {
 NavigationMenu,
 NavigationMenuContent,
 NavigationMenuItem,
 NavigationMenuLink,
 NavigationMenuList,
 NavigationMenuTrigger,
 } from &quot;@/components/ui/navigation-menu&quot;
 Copy &lt; NavigationMenu &gt;
 &lt; NavigationMenuList &gt;
 &lt; NavigationMenuItem &gt;
 &lt; NavigationMenuTrigger &gt;Item One&lt;/ NavigationMenuTrigger &gt;
 &lt; NavigationMenuContent &gt;
 &lt; NavigationMenuLink &gt;Link&lt;/ NavigationMenuLink &gt;
 &lt;/ NavigationMenuContent &gt;
 &lt;/ NavigationMenuItem &gt;
 &lt;/ NavigationMenuList &gt;
 &lt;/ NavigationMenu &gt;
 Composition #
 Use the following composition to build a NavigationMenu :
 Copy NavigationMenu
 ├── NavigationMenuList
 │ ├── NavigationMenuItem
 │ │ ├── NavigationMenuTrigger
 │ │ └── NavigationMenuContent
 │ │ ├── NavigationMenuLink
 │ │ └── NavigationMenuLink
 │ └── NavigationMenuItem
 │ └── NavigationMenuLink
 └── NavigationMenuIndicator
 Link Component #
 Use the asChild prop to compose a custom link component such as Next.js Link .
 Copy import Link from &quot;next/link&quot;

 import {
 NavigationMenuItem,
 NavigationMenuLink,
 navigationMenuTriggerStyle,
 } from &quot;@/components/ui/navigation-menu&quot;

 export function NavigationMenuDemo () {
 return (
 &lt; NavigationMenuItem &gt;
 &lt; NavigationMenuLink asChild className = { navigationMenuTriggerStyle () } &gt;
 &lt; Link href = &quot;/docs&quot; &gt;Documentation&lt;/ Link &gt;
 &lt;/ NavigationMenuLink &gt;
 &lt;/ NavigationMenuItem &gt;
 )
 }
 RTL #
 To enable RTL support in shadcn/ui, see the RTL configuration guide .
 Arabic (العربية) ▼ Toggle البدء المكونات الوثائق Copy "use client"

 import * as React from "react" View Code
 API Reference #
 See the Radix UI Navigation Menu documentation for more information. Native Select Pagination On This Page Installation Usage Composition Link Component RTL API Reference Deploy your shadcn/ui app on Vercel Trusted by OpenAI, Sonos, Adobe, and more. Vercel provides tools and infrastructure to deploy apps and features at scale. Deploy Now Deploy to Vercel Built by shadcn at Vercel . The source code is available on GitHub . Get Code
