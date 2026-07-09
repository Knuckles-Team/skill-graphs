Menubar - shadcn/ui Toggle Menu Menu Home Docs Components Blocks Charts Directory Create Search documentation... Search... 117k Toggle theme New Sections Introduction Components Installation Theming CLI RTL Skills MCP Server Registry Forms Changelog Components Accordion Alert Alert Dialog Aspect Ratio Avatar Badge Breadcrumb Button Button Group Calendar Card Carousel Chart Checkbox Collapsible Combobox Command Context Menu Data Table Date Picker Dialog Direction Drawer Dropdown Menu Empty Field Hover Card Input Input Group Input OTP Item Kbd Label Menubar Native Select Navigation Menu Pagination Popover Progress Radio Group Resizable Scroll Area Select Separator Sheet Sidebar Skeleton Slider Sonner Spinner Switch Table Tabs Textarea Toast Toggle Toggle Group Tooltip Typography Get Started Installation components.json Package Imports Theming Dark Mode CLI Monorepo Skills JavaScript Figma llms.txt Legacy Docs Forms React Hook Form TanStack Form Formisch Registry Introduction Getting Started GitHub Registries Registry Directory Examples Namespaces Authentication MCP Server Open in v0 API Reference registry.json registry-item.json Menubar Copy Page Previous Next A visually persistent menu common in desktop applications that provides quick access to a consistent set of commands. Radix UI Base UI Radix UI File Edit View Profiles Copy import {
 Menubar,
 MenubarCheckboxItem, View Code
 Installation #
 Command Manual pnpm npm yarn bun pnpm dlx shadcn@latest add menubar Copy
 Usage #
 Copy import {
 Menubar,
 MenubarContent,
 MenubarGroup,
 MenubarItem,
 MenubarMenu,
 MenubarSeparator,
 MenubarShortcut,
 MenubarTrigger,
 } from &quot;@/components/ui/menubar&quot;
 Copy &lt; Menubar &gt;
 &lt; MenubarMenu &gt;
 &lt; MenubarTrigger &gt;File&lt;/ MenubarTrigger &gt;
 &lt; MenubarContent &gt;
 &lt; MenubarGroup &gt;
 &lt; MenubarItem &gt;
 New Tab &lt; MenubarShortcut &gt;⌘T&lt;/ MenubarShortcut &gt;
 &lt;/ MenubarItem &gt;
 &lt; MenubarItem &gt;New Window&lt;/ MenubarItem &gt;
 &lt;/ MenubarGroup &gt;
 &lt; MenubarSeparator /&gt;
 &lt; MenubarGroup &gt;
 &lt; MenubarItem &gt;Share&lt;/ MenubarItem &gt;
 &lt; MenubarItem &gt;Print&lt;/ MenubarItem &gt;
 &lt;/ MenubarGroup &gt;
 &lt;/ MenubarContent &gt;
 &lt;/ MenubarMenu &gt;
 &lt;/ Menubar &gt;
 Composition #
 Use the following composition to build a Menubar :
 Copy Menubar
 ├── MenubarMenu
 │ ├── MenubarTrigger
 │ └── MenubarContent
 │ ├── MenubarGroup
 │ │ ├── MenubarLabel
 │ │ ├── MenubarItem
 │ │ └── MenubarItem
 │ ├── MenubarSeparator
 │ ├── MenubarGroup
 │ │ ├── MenubarLabel
 │ │ ├── MenubarCheckboxItem
 │ │ └── MenubarCheckboxItem
 │ ├── MenubarSeparator
 │ ├── MenubarGroup
 │ │ ├── MenubarLabel
 │ │ └── MenubarRadioGroup
 │ │ ├── MenubarRadioItem
 │ │ └── MenubarRadioItem
 │ └── MenubarSub
 │ ├── MenubarSubTrigger
 │ └── MenubarSubContent
 │ └── MenubarGroup
 │ ├── MenubarLabel
 │ ├── MenubarItem
 │ └── MenubarItem
 └── MenubarMenu
 ├── MenubarTrigger
 └── MenubarContent
 └── MenubarGroup
 ├── MenubarLabel
 ├── MenubarItem
 └── MenubarItem
 Examples #
 Checkbox #
 Use MenubarCheckboxItem for toggleable options.
 View Format Copy import {
 Menubar,
 MenubarCheckboxItem, View Code
 Radio #
 Use MenubarRadioGroup and MenubarRadioItem for single-select options.
 Profiles Theme Copy "use client"

 import * as React from "react" View Code
 Submenu #
 Use MenubarSub , MenubarSubTrigger , and MenubarSubContent for nested menus.
 File Edit Copy import {
 Menubar,
 MenubarContent, View Code
 With Icons #
 File More Copy import {
 FileIcon,
 FolderIcon, View Code
 RTL #
 To enable RTL support in shadcn/ui, see the RTL configuration guide .
 Arabic (العربية) ▼ Toggle ملف تعديل عرض الملفات الشخصية Copy "use client"

 import * as React from "react" View Code
 API Reference #
 See the Radix UI Menubar documentation. Label Native Select On This Page Installation Usage Composition Examples Checkbox Radio Submenu With Icons RTL API Reference Deploy your shadcn/ui app on Vercel Trusted by OpenAI, Sonos, Adobe, and more. Vercel provides tools and infrastructure to deploy apps and features at scale. Deploy Now Deploy to Vercel Built by shadcn at Vercel . The source code is available on GitHub . Get Code
