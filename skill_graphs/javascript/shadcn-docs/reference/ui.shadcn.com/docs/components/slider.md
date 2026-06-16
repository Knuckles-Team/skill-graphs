Slider - shadcn/ui Toggle Menu Menu Home Docs Components Blocks Charts Directory Create Search documentation... Search... 117k Toggle theme New Sections Introduction Components Installation Theming CLI RTL Skills MCP Server Registry Forms Changelog Components Accordion Alert Alert Dialog Aspect Ratio Avatar Badge Breadcrumb Button Button Group Calendar Card Carousel Chart Checkbox Collapsible Combobox Command Context Menu Data Table Date Picker Dialog Direction Drawer Dropdown Menu Empty Field Hover Card Input Input Group Input OTP Item Kbd Label Menubar Native Select Navigation Menu Pagination Popover Progress Radio Group Resizable Scroll Area Select Separator Sheet Sidebar Skeleton Slider Sonner Spinner Switch Table Tabs Textarea Toast Toggle Toggle Group Tooltip Typography Get Started Installation components.json Package Imports Theming Dark Mode CLI Monorepo Skills JavaScript Figma llms.txt Legacy Docs Forms React Hook Form TanStack Form Formisch Registry Introduction Getting Started GitHub Registries Registry Directory Examples Namespaces Authentication MCP Server Open in v0 API Reference registry.json registry-item.json Slider Copy Page Previous Next An input where the user selects a value from within a given range. Radix UI Base UI Radix UI Copy import { Slider } from "@/components/ui/slider"

 export function SliderDemo () { View Code
 Installation #
 Command Manual pnpm npm yarn bun pnpm dlx shadcn@latest add slider Copy
 Usage #
 Copy import { Slider } from &quot;@/components/ui/slider&quot;
 Copy &lt; Slider defaultValue = { [ 33 ] } max = { 100 } step = { 1 } /&gt;
 Examples #
 Range #
 Use an array with two values for a range slider.
 Copy import { Slider } from "@/components/ui/slider"

 export function SliderRange () { View Code
 Multiple Thumbs #
 Use an array with multiple values for multiple thumbs.
 Copy import { Slider } from "@/components/ui/slider"

 export function SliderMultiple () { View Code
 Vertical #
 Use orientation=&quot;vertical&quot; for a vertical slider.
 Copy import { Slider } from "@/components/ui/slider"

 export function SliderVertical () { View Code
 Controlled #
 Temperature 0.3, 0.7 Copy "use client"

 import * as React from "react" View Code
 Disabled #
 Use the disabled prop to disable the slider.
 Copy import { Slider } from "@/components/ui/slider"

 export function SliderDisabled () { View Code
 RTL #
 To enable RTL support in shadcn/ui, see the RTL configuration guide .
 Arabic (العربية) ▼ Toggle Copy "use client"

 import * as React from "react" View Code
 API Reference #
 See the Radix UI Slider documentation. Skeleton Sonner On This Page Installation Usage Examples Range Multiple Thumbs Vertical Controlled Disabled RTL API Reference Deploy your shadcn/ui app on Vercel Trusted by OpenAI, Sonos, Adobe, and more. Vercel provides tools and infrastructure to deploy apps and features at scale. Deploy Now Deploy to Vercel Built by shadcn at Vercel . The source code is available on GitHub . Get Code
