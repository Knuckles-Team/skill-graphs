Drawer - shadcn/ui Toggle Menu Menu Home Docs Components Blocks Charts Directory Create Search documentation... Search... 117k Toggle theme New Sections Introduction Components Installation Theming CLI RTL Skills MCP Server Registry Forms Changelog Components Accordion Alert Alert Dialog Aspect Ratio Avatar Badge Breadcrumb Button Button Group Calendar Card Carousel Chart Checkbox Collapsible Combobox Command Context Menu Data Table Date Picker Dialog Direction Drawer Dropdown Menu Empty Field Hover Card Input Input Group Input OTP Item Kbd Label Menubar Native Select Navigation Menu Pagination Popover Progress Radio Group Resizable Scroll Area Select Separator Sheet Sidebar Skeleton Slider Sonner Spinner Switch Table Tabs Textarea Toast Toggle Toggle Group Tooltip Typography Get Started Installation components.json Package Imports Theming Dark Mode CLI Monorepo Skills JavaScript Figma llms.txt Legacy Docs Forms React Hook Form TanStack Form Formisch Registry Introduction Getting Started GitHub Registries Registry Directory Examples Namespaces Authentication MCP Server Open in v0 API Reference registry.json registry-item.json Drawer Copy Page Previous Next A drawer component for React. Radix UI Base UI Radix UI Open Drawer Copy "use client"

 import * as React from "react" View Code
 About #
 Drawer is built on top of Vaul by emilkowalski .
 Installation #
 Command Manual pnpm npm yarn bun pnpm dlx shadcn@latest add drawer Copy
 Usage #
 Copy import {
 Drawer,
 DrawerClose,
 DrawerContent,
 DrawerDescription,
 DrawerFooter,
 DrawerHeader,
 DrawerTitle,
 DrawerTrigger,
 } from &quot;@/components/ui/drawer&quot;
 Copy &lt; Drawer &gt;
 &lt; DrawerTrigger &gt;Open&lt;/ DrawerTrigger &gt;
 &lt; DrawerContent &gt;
 &lt; DrawerHeader &gt;
 &lt; DrawerTitle &gt;Are you absolutely sure?&lt;/ DrawerTitle &gt;
 &lt; DrawerDescription &gt;This action cannot be undone.&lt;/ DrawerDescription &gt;
 &lt;/ DrawerHeader &gt;
 &lt; DrawerFooter &gt;
 &lt; Button &gt;Submit&lt;/ Button &gt;
 &lt; DrawerClose &gt;
 &lt; Button variant = &quot;outline&quot; &gt;Cancel&lt;/ Button &gt;
 &lt;/ DrawerClose &gt;
 &lt;/ DrawerFooter &gt;
 &lt;/ DrawerContent &gt;
 &lt;/ Drawer &gt;
 Composition #
 Use the following composition to build a Drawer :
 Copy Drawer
 ├── DrawerTrigger
 └── DrawerContent
 ├── DrawerHeader
 │ ├── DrawerTitle
 │ └── DrawerDescription
 └── DrawerFooter
 Examples #
 Scrollable Content #
 Keep actions visible while the content scrolls.
 Scrollable Content Copy import { Button } from "@/components/ui/button"
 import {
 Drawer, View Code
 Sides #
 Use the direction prop to set the side of the drawer. Available options are top , right , bottom , and left .
 top right bottom left Copy import { Button } from "@/components/ui/button"
 import {
 Drawer, View Code
 Responsive Dialog #
 You can combine the Dialog and Drawer components to create a responsive dialog. This renders a Dialog component on desktop and a Drawer on mobile.
 Edit Profile Copy "use client"

 import * as React from "react" View Code
 RTL #
 To enable RTL support in shadcn/ui, see the RTL configuration guide .
 Arabic (العربية) ▼ Toggle فتح الدرج Copy "use client"

 import * as React from "react" View Code
 API Reference #
 See the Vaul documentation for the full API reference. Direction Dropdown Menu On This Page About Installation Usage Composition Examples Scrollable Content Sides Responsive Dialog RTL API Reference Deploy your shadcn/ui app on Vercel Trusted by OpenAI, Sonos, Adobe, and more. Vercel provides tools and infrastructure to deploy apps and features at scale. Deploy Now Deploy to Vercel Built by shadcn at Vercel . The source code is available on GitHub . Get Code
