Aspect Ratio - shadcn/ui Toggle Menu Menu Home Docs Components Blocks Charts Directory Create Search documentation... Search... 117k Toggle theme New Sections Introduction Components Installation Theming CLI RTL Skills MCP Server Registry Forms Changelog Components Accordion Alert Alert Dialog Aspect Ratio Avatar Badge Breadcrumb Button Button Group Calendar Card Carousel Chart Checkbox Collapsible Combobox Command Context Menu Data Table Date Picker Dialog Direction Drawer Dropdown Menu Empty Field Hover Card Input Input Group Input OTP Item Kbd Label Menubar Native Select Navigation Menu Pagination Popover Progress Radio Group Resizable Scroll Area Select Separator Sheet Sidebar Skeleton Slider Sonner Spinner Switch Table Tabs Textarea Toast Toggle Toggle Group Tooltip Typography Get Started Installation components.json Package Imports Theming Dark Mode CLI Monorepo Skills JavaScript Figma llms.txt Legacy Docs Forms React Hook Form TanStack Form Formisch Registry Introduction Getting Started GitHub Registries Registry Directory Examples Namespaces Authentication MCP Server Open in v0 API Reference registry.json registry-item.json Aspect Ratio Copy Page Previous Next Displays content within a desired ratio. Radix UI Base UI Radix UI Copy import Image from "next/image"

 import { AspectRatio } from "@/components/ui/aspect-ratio" View Code
 Installation #
 Command Manual pnpm npm yarn bun pnpm dlx shadcn@latest add aspect-ratio Copy
 Usage #
 Copy import { AspectRatio } from &quot;@/components/ui/aspect-ratio&quot;
 Copy &lt; AspectRatio ratio = { 16 / 9 } &gt;
 &lt; Image src = &quot;...&quot; alt = &quot;Image&quot; className = &quot;rounded-md object-cover&quot; /&gt;
 &lt;/ AspectRatio &gt;
 Examples #
 Square #
 A square aspect ratio component using the ratio={1 / 1} prop. This is useful for displaying images in a square format.
 Copy import Image from "next/image"

 import { AspectRatio } from "@/components/ui/aspect-ratio" View Code
 Portrait #
 A portrait aspect ratio component using the ratio={9 / 16} prop. This is useful for displaying images in a portrait format.
 Copy import Image from "next/image"

 import { AspectRatio } from "@/components/ui/aspect-ratio" View Code
 RTL #
 To enable RTL support in shadcn/ui, see the RTL configuration guide .
 Arabic (العربية) ▼ Toggle منظر طبيعي جميل Copy "use client"

 import * as React from "react" View Code
 API Reference #
 AspectRatio #
 The AspectRatio component displays content within a desired ratio.
 Prop Type Default Required ratio number - Yes className string - No
 For more information, see the Radix UI documentation . Alert Dialog Avatar On This Page Installation Usage Examples Square Portrait RTL API Reference AspectRatio Deploy your shadcn/ui app on Vercel Trusted by OpenAI, Sonos, Adobe, and more. Vercel provides tools and infrastructure to deploy apps and features at scale. Deploy Now Deploy to Vercel Built by shadcn at Vercel . The source code is available on GitHub . Get Code
