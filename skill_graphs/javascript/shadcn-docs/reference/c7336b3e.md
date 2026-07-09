Dropdown Menu - shadcn/ui Toggle Menu Menu Home Docs Components Blocks Charts Directory Create Search documentation... Search... 117k Toggle theme New Sections Introduction Components Installation Theming CLI RTL Skills MCP Server Registry Forms Changelog Components Accordion Alert Alert Dialog Aspect Ratio Avatar Badge Breadcrumb Button Button Group Calendar Card Carousel Chart Checkbox Collapsible Combobox Command Context Menu Data Table Date Picker Dialog Direction Drawer Dropdown Menu Empty Field Hover Card Input Input Group Input OTP Item Kbd Label Menubar Native Select Navigation Menu Pagination Popover Progress Radio Group Resizable Scroll Area Select Separator Sheet Sidebar Skeleton Slider Sonner Spinner Switch Table Tabs Textarea Toast Toggle Toggle Group Tooltip Typography Get Started Installation components.json Package Imports Theming Dark Mode CLI Monorepo Skills JavaScript Figma llms.txt Legacy Docs Forms React Hook Form TanStack Form Formisch Registry Introduction Getting Started GitHub Registries Registry Directory Examples Namespaces Authentication MCP Server Open in v0 API Reference registry.json registry-item.json Dropdown Menu Copy Page Previous Next Displays a menu to the user — such as a set of actions or functions — triggered by a button. Radix UI Base UI Radix UI Open Copy import { Button } from "@/components/ui/button"
 import {
 DropdownMenu, View Code
 Installation #
 Command Manual pnpm npm yarn bun pnpm dlx shadcn@latest add dropdown-menu Copy
 Usage #
 Copy import { Button } from &quot;@/components/ui/button&quot;
 import {
 DropdownMenu,
 DropdownMenuContent,
 DropdownMenuGroup,
 DropdownMenuItem,
 DropdownMenuLabel,
 DropdownMenuSeparator,
 DropdownMenuTrigger,
 } from &quot;@/components/ui/dropdown-menu&quot;
 Copy &lt; DropdownMenu &gt;
 &lt; DropdownMenuTrigger asChild &gt;
 &lt; Button variant = &quot;outline&quot; &gt;Open&lt;/ Button &gt;
 &lt;/ DropdownMenuTrigger &gt;
 &lt; DropdownMenuContent &gt;
 &lt; DropdownMenuGroup &gt;
 &lt; DropdownMenuLabel &gt;My Account&lt;/ DropdownMenuLabel &gt;
 &lt; DropdownMenuItem &gt;Profile&lt;/ DropdownMenuItem &gt;
 &lt; DropdownMenuItem &gt;Billing&lt;/ DropdownMenuItem &gt;
 &lt;/ DropdownMenuGroup &gt;
 &lt; DropdownMenuSeparator /&gt;
 &lt; DropdownMenuGroup &gt;
 &lt; DropdownMenuItem &gt;Team&lt;/ DropdownMenuItem &gt;
 &lt; DropdownMenuItem &gt;Subscription&lt;/ DropdownMenuItem &gt;
 &lt;/ DropdownMenuGroup &gt;
 &lt;/ DropdownMenuContent &gt;
 &lt;/ DropdownMenu &gt;
 Composition #
 Use the following composition to build a DropdownMenu :
 Copy DropdownMenu
 ├── DropdownMenuTrigger
 └── DropdownMenuContent
 ├── DropdownMenuGroup
 │ ├── DropdownMenuLabel
 │ ├── DropdownMenuItem
 │ └── DropdownMenuItem
 ├── DropdownMenuSeparator
 ├── DropdownMenuGroup
 │ ├── DropdownMenuLabel
 │ ├── DropdownMenuCheckboxItem
 │ └── DropdownMenuCheckboxItem
 ├── DropdownMenuSeparator
 ├── DropdownMenuGroup
 │ ├── DropdownMenuLabel
 │ └── DropdownMenuRadioGroup
 │ ├── DropdownMenuRadioItem
 │ └── DropdownMenuRadioItem
 └── DropdownMenuSub
 ├── DropdownMenuSubTrigger
 └── DropdownMenuSubContent
 └── DropdownMenuGroup
 ├── DropdownMenuLabel
 ├── DropdownMenuItem
 └── DropdownMenuItem
 Examples #
 Basic #
 A basic dropdown menu with labels and separators.
 Open Copy import { Button } from "@/components/ui/button"
 import {
 DropdownMenu, View Code
 Submenu #
 Use DropdownMenuSub to nest secondary actions.
 Open Copy import { Button } from "@/components/ui/button"
 import {
 DropdownMenu, View Code
 Shortcuts #
 Add DropdownMenuShortcut to show keyboard hints.
 Open Copy import { Button } from "@/components/ui/button"
 import {
 DropdownMenu, View Code
 Icons #
 Combine icons with labels for quick scanning.
 Open Copy import {
 CreditCardIcon,
 LogOutIcon, View Code
 Checkboxes #
 Use DropdownMenuCheckboxItem for toggles.
 Open Copy "use client"

 import * as React from "react" View Code
 Checkboxes Icons #
 Add icons to checkbox items.
 Notifications Copy "use client"

 import * as React from "react" View Code
 Radio Group #
 Use DropdownMenuRadioGroup for exclusive choices.
 Open Copy "use client"

 import * as React from "react" View Code
 Radio Icons #
 Show radio options with icons.
 Payment Method Copy "use client"

 import * as React from "react" View Code
 Destructive #
 Use variant=&quot;destructive&quot; for irreversible actions.
 Actions Copy import { PencilIcon, ShareIcon, TrashIcon } from "lucide-react"

 import { Button } from "@/components/ui/button" View Code
 Avatar #
 An account switcher dropdown triggered by an avatar.
 LR Copy import {
 BadgeCheckIcon,
 BellIcon, View Code
 Complex #
 A richer example combining groups, icons, and submenus.
 Complex Menu Copy "use client"

 import * as React from "react" View Code
 RTL #
 To enable RTL support in shadcn/ui, see the RTL configuration guide .
 Arabic (العربية) ▼ Toggle افتح القائمة Copy "use client"

 import * as React from "react" View Code
 API Reference #
 See the Radix UI documentation for the full API reference. Drawer Empty On This Page Installation Usage Composition Examples Basic Submenu Shortcuts Icons Checkboxes Checkboxes Icons Radio Group Radio Icons Destructive Avatar Complex RTL API Reference Deploy your shadcn/ui app on Vercel Trusted by OpenAI, Sonos, Adobe, and more. Vercel provides tools and infrastructure to deploy apps and features at scale. Deploy Now Deploy to Vercel Built by shadcn at Vercel . The source code is available on GitHub . Get Code
