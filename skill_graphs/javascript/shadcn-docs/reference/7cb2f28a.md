Breadcrumb - shadcn/ui Toggle Menu Menu Home Docs Components Blocks Charts Directory Create Search documentation... Search... 117k Toggle theme New Sections Introduction Components Installation Theming CLI RTL Skills MCP Server Registry Forms Changelog Components Accordion Alert Alert Dialog Aspect Ratio Avatar Badge Breadcrumb Button Button Group Calendar Card Carousel Chart Checkbox Collapsible Combobox Command Context Menu Data Table Date Picker Dialog Direction Drawer Dropdown Menu Empty Field Hover Card Input Input Group Input OTP Item Kbd Label Menubar Native Select Navigation Menu Pagination Popover Progress Radio Group Resizable Scroll Area Select Separator Sheet Sidebar Skeleton Slider Sonner Spinner Switch Table Tabs Textarea Toast Toggle Toggle Group Tooltip Typography Get Started Installation components.json Package Imports Theming Dark Mode CLI Monorepo Skills JavaScript Figma llms.txt Legacy Docs Forms React Hook Form TanStack Form Formisch Registry Introduction Getting Started GitHub Registries Registry Directory Examples Namespaces Authentication MCP Server Open in v0 API Reference registry.json registry-item.json Breadcrumb Copy Page Previous Next Displays the path to the current resource using a hierarchy of links. Radix UI Base UI Radix UI Home More Toggle menu Components Breadcrumb Copy import Link from "next/link"

 import { View Code
 Installation #
 Command Manual pnpm npm yarn bun pnpm dlx shadcn@latest add breadcrumb Copy
 Usage #
 Copy import {
 Breadcrumb,
 BreadcrumbItem,
 BreadcrumbLink,
 BreadcrumbList,
 BreadcrumbPage,
 BreadcrumbSeparator,
 } from &quot;@/components/ui/breadcrumb&quot;
 Copy &lt; Breadcrumb &gt;
 &lt; BreadcrumbList &gt;
 &lt; BreadcrumbItem &gt;
 &lt; BreadcrumbLink href = &quot;/&quot; &gt;Home&lt;/ BreadcrumbLink &gt;
 &lt;/ BreadcrumbItem &gt;
 &lt; BreadcrumbSeparator /&gt;
 &lt; BreadcrumbItem &gt;
 &lt; BreadcrumbLink href = &quot;/components&quot; &gt;Components&lt;/ BreadcrumbLink &gt;
 &lt;/ BreadcrumbItem &gt;
 &lt; BreadcrumbSeparator /&gt;
 &lt; BreadcrumbItem &gt;
 &lt; BreadcrumbPage &gt;Breadcrumb&lt;/ BreadcrumbPage &gt;
 &lt;/ BreadcrumbItem &gt;
 &lt;/ BreadcrumbList &gt;
 &lt;/ Breadcrumb &gt;
 Composition #
 Use the following composition to build a Breadcrumb :
 Copy Breadcrumb
 └── BreadcrumbList
 ├── BreadcrumbItem
 │ └── BreadcrumbLink
 ├── BreadcrumbSeparator
 ├── BreadcrumbItem
 │ └── BreadcrumbLink
 ├── BreadcrumbSeparator
 └── BreadcrumbItem
 └── BreadcrumbPage
 Examples #
 Basic #
 A basic breadcrumb with a home link and a components link.
 Home Components Breadcrumb Copy import {
 Breadcrumb,
 BreadcrumbItem, View Code
 Custom separator #
 Use a custom component as children for &lt;BreadcrumbSeparator /&gt; to create a custom separator.
 Home Components Breadcrumb Copy import Link from "next/link"
 import { DotIcon } from "lucide-react"
 View Code
 Dropdown #
 You can compose &lt;BreadcrumbItem /&gt; with a &lt;DropdownMenu /&gt; to create a dropdown in the breadcrumb.
 Home Components Breadcrumb Copy import Link from "next/link"
 import { ChevronDownIcon, DotIcon } from "lucide-react"
 View Code
 Collapsed #
 We provide a &lt;BreadcrumbEllipsis /&gt; component to show a collapsed state when the breadcrumb is too long.
 Home More Components Breadcrumb Copy import Link from "next/link"

 import { View Code
 Link component #
 To use a custom link component from your routing library, you can use the asChild prop on &lt;BreadcrumbLink /&gt; .
 Home Components Breadcrumb Copy import Link from "next/link"

 import { View Code
 RTL #
 To enable RTL support in shadcn/ui, see the RTL configuration guide .
 Arabic (العربية) ▼ Toggle الرئيسية المكونات مسار التنقل Copy "use client"

 import * as React from "react" View Code
 API Reference #
 Breadcrumb #
 The Breadcrumb component is the root navigation element that wraps all breadcrumb components.
 Prop Type Default className string -
 BreadcrumbList #
 The BreadcrumbList component displays the ordered list of breadcrumb items.
 Prop Type Default className string -
 BreadcrumbItem #
 The BreadcrumbItem component wraps individual breadcrumb items.
 Prop Type Default className string -
 BreadcrumbLink #
 The BreadcrumbLink component displays a clickable link in the breadcrumb.
 Prop Type Default className string -
 BreadcrumbPage #
 The BreadcrumbPage component displays the current page in the breadcrumb (non-clickable).
 Prop Type Default className string -
 BreadcrumbSeparator #
 The BreadcrumbSeparator component displays a separator between breadcrumb items. You can pass custom children to override the default separator icon.
 Prop Type Default children React.ReactNode - className string -
 BreadcrumbEllipsis #
 The BreadcrumbEllipsis component displays an ellipsis indicator for collapsed breadcrumb items.
 Prop Type Default className string - Badge Button On This Page Installation Usage Composition Examples Basic Custom separator Dropdown Collapsed Link component RTL API Reference Breadcrumb BreadcrumbList BreadcrumbItem BreadcrumbLink BreadcrumbPage BreadcrumbSeparator BreadcrumbEllipsis Deploy your shadcn/ui app on Vercel Trusted by OpenAI, Sonos, Adobe, and more. Vercel provides tools and infrastructure to deploy apps and features at scale. Deploy Now Deploy to Vercel Built by shadcn at Vercel . The source code is available on GitHub . Get Code
