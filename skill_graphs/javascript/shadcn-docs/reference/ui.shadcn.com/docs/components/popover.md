Popover - shadcn/ui Toggle Menu Menu Home Docs Components Blocks Charts Directory Create Search documentation... Search... 117k Toggle theme New Sections Introduction Components Installation Theming CLI RTL Skills MCP Server Registry Forms Changelog Components Accordion Alert Alert Dialog Aspect Ratio Avatar Badge Breadcrumb Button Button Group Calendar Card Carousel Chart Checkbox Collapsible Combobox Command Context Menu Data Table Date Picker Dialog Direction Drawer Dropdown Menu Empty Field Hover Card Input Input Group Input OTP Item Kbd Label Menubar Native Select Navigation Menu Pagination Popover Progress Radio Group Resizable Scroll Area Select Separator Sheet Sidebar Skeleton Slider Sonner Spinner Switch Table Tabs Textarea Toast Toggle Toggle Group Tooltip Typography Get Started Installation components.json Package Imports Theming Dark Mode CLI Monorepo Skills JavaScript Figma llms.txt Legacy Docs Forms React Hook Form TanStack Form Formisch Registry Introduction Getting Started GitHub Registries Registry Directory Examples Namespaces Authentication MCP Server Open in v0 API Reference registry.json registry-item.json Popover Copy Page Previous Next Displays rich content in a portal, triggered by a button. Radix UI Base UI Radix UI Open popover Copy import { Button } from "@/components/ui/button"
 import { Input } from "@/components/ui/input"
 import { Label } from "@/components/ui/label" View Code
 Installation #
 Command Manual pnpm npm yarn bun pnpm dlx shadcn@latest add popover Copy
 Usage #
 Copy import {
 Popover,
 PopoverContent,
 PopoverDescription,
 PopoverHeader,
 PopoverTitle,
 PopoverTrigger,
 } from &quot;@/components/ui/popover&quot;
 Copy &lt; Popover &gt;
 &lt; PopoverTrigger asChild &gt;
 &lt; Button variant = &quot;outline&quot; &gt;Open Popover&lt;/ Button &gt;
 &lt;/ PopoverTrigger &gt;
 &lt; PopoverContent &gt;
 &lt; PopoverHeader &gt;
 &lt; PopoverTitle &gt;Title&lt;/ PopoverTitle &gt;
 &lt; PopoverDescription &gt;Description text here.&lt;/ PopoverDescription &gt;
 &lt;/ PopoverHeader &gt;
 &lt;/ PopoverContent &gt;
 &lt;/ Popover &gt;
 Composition #
 Use the following composition to build a Popover :
 Copy Popover
 ├── PopoverTrigger
 └── PopoverContent
 Examples #
 Basic #
 A simple popover with a header, title, and description.
 Open Popover Copy import { Button } from "@/components/ui/button"
 import {
 Popover, View Code
 Align #
 Use the align prop on PopoverContent to control the horizontal alignment.
 Start Center End Copy import { Button } from "@/components/ui/button"
 import {
 Popover, View Code
 With Form #
 A popover with form fields inside.
 Open Popover Copy import { Button } from "@/components/ui/button"
 import { Field, FieldGroup, FieldLabel } from "@/components/ui/field"
 import { Input } from "@/components/ui/input" View Code
 RTL #
 To enable RTL support in shadcn/ui, see the RTL configuration guide .
 Arabic (العربية) ▼ Toggle يسار أعلى أسفل يمين Copy "use client"

 import { View Code
 API Reference #
 See the Radix UI Popover documentation. Pagination Progress On This Page Installation Usage Composition Examples Basic Align With Form RTL API Reference Deploy your shadcn/ui app on Vercel Trusted by OpenAI, Sonos, Adobe, and more. Vercel provides tools and infrastructure to deploy apps and features at scale. Deploy Now Deploy to Vercel Built by shadcn at Vercel . The source code is available on GitHub . Get Code
