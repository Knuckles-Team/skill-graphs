Scroll Area - shadcn/ui Toggle Menu Menu Home Docs Components Blocks Charts Directory Create Search documentation... Search... 117k Toggle theme New Sections Introduction Components Installation Theming CLI RTL Skills MCP Server Registry Forms Changelog Components Accordion Alert Alert Dialog Aspect Ratio Avatar Badge Breadcrumb Button Button Group Calendar Card Carousel Chart Checkbox Collapsible Combobox Command Context Menu Data Table Date Picker Dialog Direction Drawer Dropdown Menu Empty Field Hover Card Input Input Group Input OTP Item Kbd Label Menubar Native Select Navigation Menu Pagination Popover Progress Radio Group Resizable Scroll Area Select Separator Sheet Sidebar Skeleton Slider Sonner Spinner Switch Table Tabs Textarea Toast Toggle Toggle Group Tooltip Typography Get Started Installation components.json Package Imports Theming Dark Mode CLI Monorepo Skills JavaScript Figma llms.txt Legacy Docs Forms React Hook Form TanStack Form Formisch Registry Introduction Getting Started GitHub Registries Registry Directory Examples Namespaces Authentication MCP Server Open in v0 API Reference registry.json registry-item.json Scroll Area Copy Page Previous Next Augments native scroll functionality for custom, cross-browser styling. Radix UI Base UI Radix UI Tags v1.2.0-beta.50 v1.2.0-beta.49 v1.2.0-beta.48 v1.2.0-beta.47 v1.2.0-beta.46 v1.2.0-beta.45 v1.2.0-beta.44 v1.2.0-beta.43 v1.2.0-beta.42 v1.2.0-beta.41 v1.2.0-beta.40 v1.2.0-beta.39 v1.2.0-beta.38 v1.2.0-beta.37 v1.2.0-beta.36 v1.2.0-beta.35 v1.2.0-beta.34 v1.2.0-beta.33 v1.2.0-beta.32 v1.2.0-beta.31 v1.2.0-beta.30 v1.2.0-beta.29 v1.2.0-beta.28 v1.2.0-beta.27 v1.2.0-beta.26 v1.2.0-beta.25 v1.2.0-beta.24 v1.2.0-beta.23 v1.2.0-beta.22 v1.2.0-beta.21 v1.2.0-beta.20 v1.2.0-beta.19 v1.2.0-beta.18 v1.2.0-beta.17 v1.2.0-beta.16 v1.2.0-beta.15 v1.2.0-beta.14 v1.2.0-beta.13 v1.2.0-beta.12 v1.2.0-beta.11 v1.2.0-beta.10 v1.2.0-beta.9 v1.2.0-beta.8 v1.2.0-beta.7 v1.2.0-beta.6 v1.2.0-beta.5 v1.2.0-beta.4 v1.2.0-beta.3 v1.2.0-beta.2 v1.2.0-beta.1 Copy import * as React from "react"

 import { ScrollArea } from "@/components/ui/scroll-area" View Code
 Installation #
 Command Manual pnpm npm yarn bun pnpm dlx shadcn@latest add scroll-area Copy
 Usage #
 Copy import { ScrollArea, ScrollBar } from &quot;@/components/ui/scroll-area&quot;
 Copy &lt; ScrollArea className = &quot;h-[200px] w-[350px] rounded-md border p-4&quot; &gt;
 Your scrollable content here.
 &lt;/ ScrollArea &gt;
 Composition #
 Use the following composition to build a ScrollArea :
 Copy ScrollArea
 └── ScrollBar
 Examples #
 Horizontal #
 Use ScrollBar with orientation=&quot;horizontal&quot; for horizontal scrolling.
 Photo by Ornella Binni Photo by Tom Byrom Photo by Vladimir Malyavko Copy import * as React from "react"
 import Image from "next/image"
 View Code
 RTL #
 To enable RTL support in shadcn/ui, see the RTL configuration guide .
 Arabic (العربية) ▼ Toggle العلامات v1.2.0-beta.50 v1.2.0-beta.49 v1.2.0-beta.48 v1.2.0-beta.47 v1.2.0-beta.46 v1.2.0-beta.45 v1.2.0-beta.44 v1.2.0-beta.43 v1.2.0-beta.42 v1.2.0-beta.41 v1.2.0-beta.40 v1.2.0-beta.39 v1.2.0-beta.38 v1.2.0-beta.37 v1.2.0-beta.36 v1.2.0-beta.35 v1.2.0-beta.34 v1.2.0-beta.33 v1.2.0-beta.32 v1.2.0-beta.31 v1.2.0-beta.30 v1.2.0-beta.29 v1.2.0-beta.28 v1.2.0-beta.27 v1.2.0-beta.26 v1.2.0-beta.25 v1.2.0-beta.24 v1.2.0-beta.23 v1.2.0-beta.22 v1.2.0-beta.21 v1.2.0-beta.20 v1.2.0-beta.19 v1.2.0-beta.18 v1.2.0-beta.17 v1.2.0-beta.16 v1.2.0-beta.15 v1.2.0-beta.14 v1.2.0-beta.13 v1.2.0-beta.12 v1.2.0-beta.11 v1.2.0-beta.10 v1.2.0-beta.9 v1.2.0-beta.8 v1.2.0-beta.7 v1.2.0-beta.6 v1.2.0-beta.5 v1.2.0-beta.4 v1.2.0-beta.3 v1.2.0-beta.2 v1.2.0-beta.1 Copy "use client"

 import * as React from "react" View Code
 API Reference #
 See the Radix UI Scroll Area documentation. Resizable Select On This Page Installation Usage Composition Examples Horizontal RTL API Reference Deploy your shadcn/ui app on Vercel Trusted by OpenAI, Sonos, Adobe, and more. Vercel provides tools and infrastructure to deploy apps and features at scale. Deploy Now Deploy to Vercel Built by shadcn at Vercel . The source code is available on GitHub . Get Code
