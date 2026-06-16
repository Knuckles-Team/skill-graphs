Badge - shadcn/ui Toggle Menu Menu Home Docs Components Blocks Charts Directory Create Search documentation... Search... 117k Toggle theme New Sections Introduction Components Installation Theming CLI RTL Skills MCP Server Registry Forms Changelog Components Accordion Alert Alert Dialog Aspect Ratio Avatar Badge Breadcrumb Button Button Group Calendar Card Carousel Chart Checkbox Collapsible Combobox Command Context Menu Data Table Date Picker Dialog Direction Drawer Dropdown Menu Empty Field Hover Card Input Input Group Input OTP Item Kbd Label Menubar Native Select Navigation Menu Pagination Popover Progress Radio Group Resizable Scroll Area Select Separator Sheet Sidebar Skeleton Slider Sonner Spinner Switch Table Tabs Textarea Toast Toggle Toggle Group Tooltip Typography Get Started Installation components.json Package Imports Theming Dark Mode CLI Monorepo Skills JavaScript Figma llms.txt Legacy Docs Forms React Hook Form TanStack Form Formisch Registry Introduction Getting Started GitHub Registries Registry Directory Examples Namespaces Authentication MCP Server Open in v0 API Reference registry.json registry-item.json Badge Copy Page Previous Next Displays a badge or a component that looks like a badge. Radix UI Base UI Radix UI Badge Secondary Destructive Outline Copy import { Badge } from "@/components/ui/badge"

 export function BadgeDemo () { View Code
 Installation #
 Command Manual pnpm npm yarn bun pnpm dlx shadcn@latest add badge Copy
 Usage #
 Copy import { Badge } from &quot;@/components/ui/badge&quot;
 Copy &lt; Badge variant = &quot;default | outline | secondary | destructive&quot; &gt;Badge&lt;/ Badge &gt;
 Examples #
 Variants #
 Use the variant prop to change the variant of the badge.
 Default Secondary Destructive Outline Ghost Copy import { Badge } from "@/components/ui/badge"

 export function BadgeVariants () { View Code
 With Icon #
 You can render an icon inside the badge. Use data-icon=&quot;inline-start&quot; to render the icon on the left and data-icon=&quot;inline-end&quot; to render the icon on the right.
 Verified Bookmark Copy import { BadgeCheck, BookmarkIcon } from "lucide-react"

 import { Badge } from "@/components/ui/badge" View Code
 With Spinner #
 You can render a spinner inside the badge. Remember to add the data-icon=&quot;inline-start&quot; or data-icon=&quot;inline-end&quot; prop to the spinner.
 Deleting Generating Copy import { Badge } from "@/components/ui/badge"
 import { Spinner } from "@/components/ui/spinner"
 View Code
 Link #
 Use the asChild prop to render a link as a badge.
 Open Link Copy import { ArrowUpRightIcon } from "lucide-react"

 import { Badge } from "@/components/ui/badge" View Code
 Custom Colors #
 You can customize the colors of a badge by adding custom classes such as bg-green-50 dark:bg-green-800 to the Badge component.
 Blue Green Sky Purple Red Copy import { Badge } from "@/components/ui/badge"

 export function BadgeCustomColors () { View Code
 RTL #
 To enable RTL support in shadcn/ui, see the RTL configuration guide .
 Arabic (العربية) ▼ Toggle شارة ثانوي مدمر مخطط متحقق إشارة مرجعية Copy "use client"

 import * as React from "react" View Code
 API Reference #
 Badge #
 The Badge component displays a badge or a component that looks like a badge.
 Prop Type Default variant &quot;default&quot; | &quot;secondary&quot; | &quot;destructive&quot; | &quot;outline&quot; | &quot;ghost&quot; | &quot;link&quot; &quot;default&quot; className string - Avatar Breadcrumb On This Page Installation Usage Examples Variants With Icon With Spinner Link Custom Colors RTL API Reference Badge Deploy your shadcn/ui app on Vercel Trusted by OpenAI, Sonos, Adobe, and more. Vercel provides tools and infrastructure to deploy apps and features at scale. Deploy Now Deploy to Vercel Built by shadcn at Vercel . The source code is available on GitHub . Get Code
