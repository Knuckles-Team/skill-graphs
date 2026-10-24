Toggle Group - shadcn/ui Toggle Menu Menu Home Docs Components Blocks Charts Directory Create Search documentation... Search... 117k Toggle theme New Sections Introduction Components Installation Theming CLI RTL Skills MCP Server Registry Forms Changelog Components Accordion Alert Alert Dialog Aspect Ratio Avatar Badge Breadcrumb Button Button Group Calendar Card Carousel Chart Checkbox Collapsible Combobox Command Context Menu Data Table Date Picker Dialog Direction Drawer Dropdown Menu Empty Field Hover Card Input Input Group Input OTP Item Kbd Label Menubar Native Select Navigation Menu Pagination Popover Progress Radio Group Resizable Scroll Area Select Separator Sheet Sidebar Skeleton Slider Sonner Spinner Switch Table Tabs Textarea Toast Toggle Toggle Group Tooltip Typography Get Started Installation components.json Package Imports Theming Dark Mode CLI Monorepo Skills JavaScript Figma llms.txt Legacy Docs Forms React Hook Form TanStack Form Formisch Registry Introduction Getting Started GitHub Registries Registry Directory Examples Namespaces Authentication MCP Server Open in v0 API Reference registry.json registry-item.json Toggle Group Copy Page Previous Next A set of two-state buttons that can be toggled on or off. Radix UI Base UI Radix UI Copy import { Bold, Italic, Underline } from "lucide-react"

 import { View Code
 Installation #
 Command Manual pnpm npm yarn bun pnpm dlx shadcn@latest add toggle-group Copy
 Usage #
 Copy import { ToggleGroup, ToggleGroupItem } from &quot;@/components/ui/toggle-group&quot;
 Copy &lt; ToggleGroup type = &quot;single&quot; &gt;
 &lt; ToggleGroupItem value = &quot;a&quot; &gt;A&lt;/ ToggleGroupItem &gt;
 &lt; ToggleGroupItem value = &quot;b&quot; &gt;B&lt;/ ToggleGroupItem &gt;
 &lt; ToggleGroupItem value = &quot;c&quot; &gt;C&lt;/ ToggleGroupItem &gt;
 &lt;/ ToggleGroup &gt;
 Composition #
 Use the following composition to build a ToggleGroup :
 Copy ToggleGroup
 ├── ToggleGroupItem
 └── ToggleGroupItem
 Examples #
 Outline #
 Use variant=&quot;outline&quot; for an outline style.
 All Missed Copy import {
 ToggleGroup,
 ToggleGroupItem, View Code
 Size #
 Use the size prop to change the size of the toggle group.
 Top Bottom Left Right Top Bottom Left Right Copy import {
 ToggleGroup,
 ToggleGroupItem, View Code
 Spacing #
 Use spacing to add spacing between toggle group items.
 Top Bottom Left Right Copy import {
 ToggleGroup,
 ToggleGroupItem, View Code
 Vertical #
 Use orientation=&quot;vertical&quot; for vertical toggle groups.
 Copy import { BoldIcon, ItalicIcon, UnderlineIcon } from "lucide-react"

 import { View Code
 Disabled #
 Copy import { Bold, Italic, Underline } from "lucide-react"

 import { View Code
 Custom #
 A custom toggle group example.
 Font Weight Aa Light Aa Normal Aa Medium Aa Bold Use font- normal to set the font weight. Copy "use client"

 import * as React from "react" View Code
 RTL #
 To enable RTL support in shadcn/ui, see the RTL configuration guide .
 Arabic (العربية) ▼ Toggle قائمة شبكة بطاقات Copy "use client"

 import { View Code
 API Reference #
 See the Radix Toggle Group documentation.
 Changelog #
 2026-05-17 Default Spacing #
 Changed the default spacing from 0 to 2 so toggle groups render with space between items by default. Use spacing={0} for connected items. Toggle Tooltip On This Page Installation Usage Composition Examples Outline Size Spacing Vertical Disabled Custom RTL API Reference Changelog 2026-05-17 Default Spacing Deploy your shadcn/ui app on Vercel Trusted by OpenAI, Sonos, Adobe, and more. Vercel provides tools and infrastructure to deploy apps and features at scale. Deploy Now Deploy to Vercel Built by shadcn at Vercel . The source code is available on GitHub . Get Code
