Alert Dialog - shadcn/ui Toggle Menu Menu Home Docs Components Blocks Charts Directory Create Search documentation... Search... 117k Toggle theme New Sections Introduction Components Installation Theming CLI RTL Skills MCP Server Registry Forms Changelog Components Accordion Alert Alert Dialog Aspect Ratio Avatar Badge Breadcrumb Button Button Group Calendar Card Carousel Chart Checkbox Collapsible Combobox Command Context Menu Data Table Date Picker Dialog Direction Drawer Dropdown Menu Empty Field Hover Card Input Input Group Input OTP Item Kbd Label Menubar Native Select Navigation Menu Pagination Popover Progress Radio Group Resizable Scroll Area Select Separator Sheet Sidebar Skeleton Slider Sonner Spinner Switch Table Tabs Textarea Toast Toggle Toggle Group Tooltip Typography Get Started Installation components.json Package Imports Theming Dark Mode CLI Monorepo Skills JavaScript Figma llms.txt Legacy Docs Forms React Hook Form TanStack Form Formisch Registry Introduction Getting Started GitHub Registries Registry Directory Examples Namespaces Authentication MCP Server Open in v0 API Reference registry.json registry-item.json Alert Dialog Copy Page Previous Next A modal dialog that interrupts the user with important content and expects a response. Radix UI Base UI Radix UI Show Dialog Copy import {
 AlertDialog,
 AlertDialogAction, View Code
 Installation #
 Command Manual pnpm npm yarn bun pnpm dlx shadcn@latest add alert-dialog Copy
 Usage #
 Copy import {
 AlertDialog,
 AlertDialogAction,
 AlertDialogCancel,
 AlertDialogContent,
 AlertDialogDescription,
 AlertDialogFooter,
 AlertDialogHeader,
 AlertDialogTitle,
 AlertDialogTrigger,
 } from &quot;@/components/ui/alert-dialog&quot;
 Copy &lt; AlertDialog &gt;
 &lt; AlertDialogTrigger asChild &gt;
 &lt; Button variant = &quot;outline&quot; &gt;Show Dialog&lt;/ Button &gt;
 &lt;/ AlertDialogTrigger &gt;
 &lt; AlertDialogContent &gt;
 &lt; AlertDialogHeader &gt;
 &lt; AlertDialogTitle &gt;Are you absolutely sure?&lt;/ AlertDialogTitle &gt;
 &lt; AlertDialogDescription &gt;
 This action cannot be undone. This will permanently delete your account
 from our servers.
 &lt;/ AlertDialogDescription &gt;
 &lt;/ AlertDialogHeader &gt;
 &lt; AlertDialogFooter &gt;
 &lt; AlertDialogCancel &gt;Cancel&lt;/ AlertDialogCancel &gt;
 &lt; AlertDialogAction &gt;Continue&lt;/ AlertDialogAction &gt;
 &lt;/ AlertDialogFooter &gt;
 &lt;/ AlertDialogContent &gt;
 &lt;/ AlertDialog &gt;
 Composition #
 Use the following composition to build an AlertDialog :
 Copy AlertDialog
 ├── AlertDialogTrigger
 └── AlertDialogContent
 ├── AlertDialogHeader
 │ ├── AlertDialogMedia
 │ ├── AlertDialogTitle
 │ └── AlertDialogDescription
 └── AlertDialogFooter
 ├── AlertDialogCancel
 └── AlertDialogAction
 Examples #
 Basic #
 A basic alert dialog with a title, description, and cancel and continue buttons.
 Show Dialog Copy import {
 AlertDialog,
 AlertDialogAction, View Code
 Small #
 Use the size=&quot;sm&quot; prop to make the alert dialog smaller.
 Show Dialog Copy import {
 AlertDialog,
 AlertDialogAction, View Code
 Media #
 Use the AlertDialogMedia component to add a media element such as an icon or image to the alert dialog.
 Share Project Copy import { CircleFadingPlusIcon } from "lucide-react"

 import { View Code
 Small with Media #
 Use the size=&quot;sm&quot; prop to make the alert dialog smaller and the AlertDialogMedia component to add a media element such as an icon or image to the alert dialog.
 Show Dialog Copy import { BluetoothIcon } from "lucide-react"

 import { View Code
 Destructive #
 Use the AlertDialogAction component to add a destructive action button to the alert dialog.
 Delete Chat Copy import { Trash2Icon } from "lucide-react"

 import { View Code
 RTL #
 To enable RTL support in shadcn/ui, see the RTL configuration guide .
 Arabic (العربية) ▼ Toggle إظهار الحوار إظهار الحوار (صغير) Copy "use client"

 import * as React from "react" View Code
 API Reference #
 size #
 Use the size prop on the AlertDialogContent component to control the size of the alert dialog. It accepts the following values:
 Prop Type Default size &quot;default&quot; | &quot;sm&quot; &quot;default&quot;
 For more information about the other components and their props, see the Radix UI documentation . Alert Aspect Ratio On This Page Installation Usage Composition Examples Basic Small Media Small with Media Destructive RTL API Reference size Deploy your shadcn/ui app on Vercel Trusted by OpenAI, Sonos, Adobe, and more. Vercel provides tools and infrastructure to deploy apps and features at scale. Deploy Now Deploy to Vercel Built by shadcn at Vercel . The source code is available on GitHub . Get Code
