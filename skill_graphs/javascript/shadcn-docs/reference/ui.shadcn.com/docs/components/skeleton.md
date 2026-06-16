Skeleton - shadcn/ui Toggle Menu Menu Home Docs Components Blocks Charts Directory Create Search documentation... Search... 117k Toggle theme New Sections Introduction Components Installation Theming CLI RTL Skills MCP Server Registry Forms Changelog Components Accordion Alert Alert Dialog Aspect Ratio Avatar Badge Breadcrumb Button Button Group Calendar Card Carousel Chart Checkbox Collapsible Combobox Command Context Menu Data Table Date Picker Dialog Direction Drawer Dropdown Menu Empty Field Hover Card Input Input Group Input OTP Item Kbd Label Menubar Native Select Navigation Menu Pagination Popover Progress Radio Group Resizable Scroll Area Select Separator Sheet Sidebar Skeleton Slider Sonner Spinner Switch Table Tabs Textarea Toast Toggle Toggle Group Tooltip Typography Get Started Installation components.json Package Imports Theming Dark Mode CLI Monorepo Skills JavaScript Figma llms.txt Legacy Docs Forms React Hook Form TanStack Form Formisch Registry Introduction Getting Started GitHub Registries Registry Directory Examples Namespaces Authentication MCP Server Open in v0 API Reference registry.json registry-item.json Skeleton Copy Page Previous Next Use to show a placeholder while content is loading. Radix UI Base UI Radix UI Copy import { Skeleton } from "@/components/ui/skeleton"

 export function SkeletonDemo () { View Code
 Installation #
 Command Manual pnpm npm yarn bun pnpm dlx shadcn@latest add skeleton Copy
 Usage #
 Copy import { Skeleton } from &quot;@/components/ui/skeleton&quot;
 Copy &lt; Skeleton className = &quot;h-[20px] w-[100px] rounded-full&quot; /&gt;
 Examples #
 Avatar #
 Copy import { Skeleton } from "@/components/ui/skeleton"

 export function SkeletonAvatar () { View Code
 Card #
 Copy import { Card, CardContent, CardHeader } from "@/components/ui/card"
 import { Skeleton } from "@/components/ui/skeleton"
 View Code
 Text #
 Copy import { Skeleton } from "@/components/ui/skeleton"

 export function SkeletonText () { View Code
 Form #
 Copy import { Skeleton } from "@/components/ui/skeleton"

 export function SkeletonForm () { View Code
 Table #
 Copy import { Skeleton } from "@/components/ui/skeleton"

 export function SkeletonTable () { View Code
 RTL #
 To enable RTL support in shadcn/ui, see the RTL configuration guide .
 Arabic (العربية) ▼ Toggle Copy "use client"

 import * as React from "react" View Code Sidebar Slider On This Page Installation Usage Examples Avatar Card Text Form Table RTL Deploy your shadcn/ui app on Vercel Trusted by OpenAI, Sonos, Adobe, and more. Vercel provides tools and infrastructure to deploy apps and features at scale. Deploy Now Deploy to Vercel Built by shadcn at Vercel . The source code is available on GitHub . Get Code
