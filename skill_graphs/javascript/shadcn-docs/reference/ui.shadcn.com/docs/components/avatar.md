Avatar - shadcn/ui Toggle Menu Menu Home Docs Components Blocks Charts Directory Create Search documentation... Search... 117k Toggle theme New Sections Introduction Components Installation Theming CLI RTL Skills MCP Server Registry Forms Changelog Components Accordion Alert Alert Dialog Aspect Ratio Avatar Badge Breadcrumb Button Button Group Calendar Card Carousel Chart Checkbox Collapsible Combobox Command Context Menu Data Table Date Picker Dialog Direction Drawer Dropdown Menu Empty Field Hover Card Input Input Group Input OTP Item Kbd Label Menubar Native Select Navigation Menu Pagination Popover Progress Radio Group Resizable Scroll Area Select Separator Sheet Sidebar Skeleton Slider Sonner Spinner Switch Table Tabs Textarea Toast Toggle Toggle Group Tooltip Typography Get Started Installation components.json Package Imports Theming Dark Mode CLI Monorepo Skills JavaScript Figma llms.txt Legacy Docs Forms React Hook Form TanStack Form Formisch Registry Introduction Getting Started GitHub Registries Registry Directory Examples Namespaces Authentication MCP Server Open in v0 API Reference registry.json registry-item.json Avatar Copy Page Previous Next An image element with a fallback for representing the user. Radix UI Base UI Radix UI CN ER CN LR ER +3 Copy import {
 Avatar,
 AvatarBadge, View Code
 Installation #
 Command Manual pnpm npm yarn bun pnpm dlx shadcn@latest add avatar Copy
 Usage #
 Copy import { Avatar, AvatarFallback, AvatarImage } from &quot;@/components/ui/avatar&quot;
 Copy &lt; Avatar &gt;
 &lt; AvatarImage src = &quot;https://github.com/shadcn.png&quot; /&gt;
 &lt; AvatarFallback &gt;CN&lt;/ AvatarFallback &gt;
 &lt;/ Avatar &gt;
 Composition #
 Use the following composition to build an Avatar :
 Copy Avatar
 ├── AvatarImage
 ├── AvatarFallback
 └── AvatarBadge
 Use the following composition to build an AvatarGroup :
 Copy AvatarGroup
 ├── Avatar
 │ ├── AvatarImage
 │ ├── AvatarFallback
 │ └── AvatarBadge
 ├── Avatar
 │ ├── AvatarImage
 │ ├── AvatarFallback
 │ └── AvatarBadge
 └── AvatarGroupCount
 Examples #
 Basic #
 A basic avatar component with an image and a fallback.
 CN Copy import {
 Avatar,
 AvatarFallback, View Code
 Badge #
 Use the AvatarBadge component to add a badge to the avatar. The badge is positioned at the bottom right of the avatar.
 CN Copy import {
 Avatar,
 AvatarBadge, View Code
 Use the className prop to add custom styles to the badge such as custom colors, sizes, etc.
 Copy &lt; Avatar &gt;
 &lt; AvatarImage src = &quot;https://github.com/shadcn.png&quot; alt = &quot;@shadcn&quot; /&gt;
 &lt; AvatarFallback &gt;CN&lt;/ AvatarFallback &gt;
 &lt; AvatarBadge className = &quot;bg-green-600 dark:bg-green-800&quot; /&gt;
 &lt;/ Avatar &gt;
 Badge with Icon #
 You can also use an icon inside &lt;AvatarBadge&gt; .
 PP Copy import { PlusIcon } from "lucide-react"

 import { View Code
 Avatar Group #
 Use the AvatarGroup component to add a group of avatars.
 CN LR ER Copy import {
 Avatar,
 AvatarFallback, View Code
 Avatar Group Count #
 Use &lt;AvatarGroupCount&gt; to add a count to the group.
 CN LR ER +3 Copy import {
 Avatar,
 AvatarFallback, View Code
 Avatar Group with Icon #
 You can also use an icon inside &lt;AvatarGroupCount&gt; .
 CN LR ER Copy import { PlusIcon } from "lucide-react"

 import { View Code
 Sizes #
 Use the size prop to change the size of the avatar.
 CN CN CN Copy import {
 Avatar,
 AvatarFallback, View Code
 Dropdown #
 You can use the Avatar component as a trigger for a dropdown menu.
 CN Copy import {
 Avatar,
 AvatarFallback, View Code
 RTL #
 To enable RTL support in shadcn/ui, see the RTL configuration guide .
 Arabic (العربية) ▼ Toggle CN ER CN LR ER +٣ Copy "use client"

 import * as React from "react" View Code
 API Reference #
 Avatar #
 The Avatar component is the root component that wraps the avatar image and fallback.
 Prop Type Default size &quot;default&quot; | &quot;sm&quot; | &quot;lg&quot; &quot;default&quot; className string -
 AvatarImage #
 The AvatarImage component displays the avatar image. It accepts all Radix UI Avatar Image props.
 Prop Type Default src string - alt string - className string -
 AvatarFallback #
 The AvatarFallback component displays a fallback when the image fails to load. It accepts all Radix UI Avatar Fallback props.
 Prop Type Default className string -
 AvatarBadge #
 The AvatarBadge component displays a badge indicator on the avatar, typically positioned at the bottom right.
 Prop Type Default className string -
 AvatarGroup #
 The AvatarGroup component displays a group of avatars with overlapping styling.
 Prop Type Default className string -
 AvatarGroupCount #
 The AvatarGroupCount component displays a count indicator in an avatar group, typically showing the number of additional avatars.
 Prop Type Default className string -
 For more information about Radix UI Avatar props, see the Radix UI documentation . Aspect Ratio Badge On This Page Installation Usage Composition Examples Basic Badge Badge with Icon Avatar Group Avatar Group Count Avatar Group with Icon Sizes Dropdown RTL API Reference Avatar AvatarImage AvatarFallback AvatarBadge AvatarGroup AvatarGroupCount Deploy your shadcn/ui app on Vercel Trusted by OpenAI, Sonos, Adobe, and more. Vercel provides tools and infrastructure to deploy apps and features at scale. Deploy Now Deploy to Vercel Built by shadcn at Vercel . The source code is available on GitHub . Get Code
