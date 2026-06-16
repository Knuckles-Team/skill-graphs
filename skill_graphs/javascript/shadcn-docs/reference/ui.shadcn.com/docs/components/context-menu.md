Context Menu - shadcn/ui Toggle Menu Menu Home Docs Components Blocks Charts Directory Create Search documentation... Search... 117k Toggle theme New Sections Introduction Components Installation Theming CLI RTL Skills MCP Server Registry Forms Changelog Components Accordion Alert Alert Dialog Aspect Ratio Avatar Badge Breadcrumb Button Button Group Calendar Card Carousel Chart Checkbox Collapsible Combobox Command Context Menu Data Table Date Picker Dialog Direction Drawer Dropdown Menu Empty Field Hover Card Input Input Group Input OTP Item Kbd Label Menubar Native Select Navigation Menu Pagination Popover Progress Radio Group Resizable Scroll Area Select Separator Sheet Sidebar Skeleton Slider Sonner Spinner Switch Table Tabs Textarea Toast Toggle Toggle Group Tooltip Typography Get Started Installation components.json Package Imports Theming Dark Mode CLI Monorepo Skills JavaScript Figma llms.txt Legacy Docs Forms React Hook Form TanStack Form Formisch Registry Introduction Getting Started GitHub Registries Registry Directory Examples Namespaces Authentication MCP Server Open in v0 API Reference registry.json registry-item.json Context Menu Copy Page Previous Next Displays a menu of actions triggered by a right click. Radix UI Base UI Radix UI Right click here Long press here Copy import {
 ContextMenu,
 ContextMenuCheckboxItem, View Code
 Installation #
 Command Manual pnpm npm yarn bun pnpm dlx shadcn@latest add context-menu Copy
 Usage #
 Copy import {
 ContextMenu,
 ContextMenuContent,
 ContextMenuItem,
 ContextMenuTrigger,
 } from &quot;@/components/ui/context-menu&quot;
 Copy &lt; ContextMenu &gt;
 &lt; ContextMenuTrigger &gt;Right click here&lt;/ ContextMenuTrigger &gt;
 &lt; ContextMenuContent &gt;
 &lt; ContextMenuItem &gt;Profile&lt;/ ContextMenuItem &gt;
 &lt; ContextMenuItem &gt;Billing&lt;/ ContextMenuItem &gt;
 &lt; ContextMenuItem &gt;Team&lt;/ ContextMenuItem &gt;
 &lt; ContextMenuItem &gt;Subscription&lt;/ ContextMenuItem &gt;
 &lt;/ ContextMenuContent &gt;
 &lt;/ ContextMenu &gt;
 Composition #
 Use the following composition to build a ContextMenu :
 Copy ContextMenu
 ├── ContextMenuTrigger
 └── ContextMenuContent
 ├── ContextMenuGroup
 │ ├── ContextMenuLabel
 │ ├── ContextMenuItem
 │ └── ContextMenuItem
 ├── ContextMenuSeparator
 ├── ContextMenuGroup
 │ ├── ContextMenuLabel
 │ ├── ContextMenuCheckboxItem
 │ └── ContextMenuCheckboxItem
 ├── ContextMenuSeparator
 ├── ContextMenuGroup
 │ ├── ContextMenuLabel
 │ └── ContextMenuRadioGroup
 │ ├── ContextMenuRadioItem
 │ └── ContextMenuRadioItem
 └── ContextMenuSub
 ├── ContextMenuSubTrigger
 └── ContextMenuSubContent
 └── ContextMenuGroup
 ├── ContextMenuItem
 └── ContextMenuItem
 Examples #
 Basic #
 A simple context menu with a few actions.
 Right click here Long press here Copy import {
 ContextMenu,
 ContextMenuContent, View Code
 Submenu #
 Use ContextMenuSub to nest secondary actions.
 Right click here Long press here Copy import {
 ContextMenu,
 ContextMenuContent, View Code
 Shortcuts #
 Add ContextMenuShortcut to show keyboard hints.
 Right click here Long press here Copy import {
 ContextMenu,
 ContextMenuContent, View Code
 Groups #
 Group related actions and separate them with dividers.
 Right click here Long press here Copy import {
 ContextMenu,
 ContextMenuContent, View Code
 Icons #
 Combine icons with labels for quick scanning.
 Right click here Long press here Copy import {
 ClipboardPasteIcon,
 CopyIcon, View Code
 Checkboxes #
 Use ContextMenuCheckboxItem for toggles.
 Right click here Long press here Copy import {
 ContextMenu,
 ContextMenuCheckboxItem, View Code
 Radio #
 Use ContextMenuRadioItem for exclusive choices.
 Right click here Long press here Copy "use client"

 import * as React from "react" View Code
 Destructive #
 Use variant=&quot;destructive&quot; to style the menu item as destructive.
 Right click here Long press here Copy import { PencilIcon, ShareIcon, TrashIcon } from "lucide-react"

 import { View Code
 RTL #
 To enable RTL support in shadcn/ui, see the RTL configuration guide .
 Arabic (العربية) ▼ Toggle انقر بزر الماوس الأيمن هنا اضغط مطولاً هنا Copy "use client"

 import * as React from "react" View Code
 API Reference #
 See the Radix UI documentation for more information. Command Data Table On This Page Installation Usage Composition Examples Basic Submenu Shortcuts Groups Icons Checkboxes Radio Destructive RTL API Reference Deploy your shadcn/ui app on Vercel Trusted by OpenAI, Sonos, Adobe, and more. Vercel provides tools and infrastructure to deploy apps and features at scale. Deploy Now Deploy to Vercel Built by shadcn at Vercel . The source code is available on GitHub . Get Code
