Tabs - shadcn/ui Toggle Menu Menu Home Docs Components Blocks Charts Directory Create Search documentation... Search... 117k Toggle theme New Sections Introduction Components Installation Theming CLI RTL Skills MCP Server Registry Forms Changelog Components Accordion Alert Alert Dialog Aspect Ratio Avatar Badge Breadcrumb Button Button Group Calendar Card Carousel Chart Checkbox Collapsible Combobox Command Context Menu Data Table Date Picker Dialog Direction Drawer Dropdown Menu Empty Field Hover Card Input Input Group Input OTP Item Kbd Label Menubar Native Select Navigation Menu Pagination Popover Progress Radio Group Resizable Scroll Area Select Separator Sheet Sidebar Skeleton Slider Sonner Spinner Switch Table Tabs Textarea Toast Toggle Toggle Group Tooltip Typography Get Started Installation components.json Package Imports Theming Dark Mode CLI Monorepo Skills JavaScript Figma llms.txt Legacy Docs Forms React Hook Form TanStack Form Formisch Registry Introduction Getting Started GitHub Registries Registry Directory Examples Namespaces Authentication MCP Server Open in v0 API Reference registry.json registry-item.json Tabs Copy Page Previous Next A set of layered sections of content—known as tab panels—that are displayed one at a time. Radix UI Base UI Radix UI Overview Analytics Reports Settings Overview View your key metrics and recent project activity. Track progress across all your active projects. You have 12 active projects and 3 pending tasks. Copy import {
 Card,
 CardContent, View Code
 Installation #
 Command Manual pnpm npm yarn bun pnpm dlx shadcn@latest add tabs Copy
 Usage #
 Copy import { Tabs, TabsContent, TabsList, TabsTrigger } from &quot;@/components/ui/tabs&quot;
 Copy &lt; Tabs defaultValue = &quot;account&quot; className = &quot;w-[400px]&quot; &gt;
 &lt; TabsList &gt;
 &lt; TabsTrigger value = &quot;account&quot; &gt;Account&lt;/ TabsTrigger &gt;
 &lt; TabsTrigger value = &quot;password&quot; &gt;Password&lt;/ TabsTrigger &gt;
 &lt;/ TabsList &gt;
 &lt; TabsContent value = &quot;account&quot; &gt;Make changes to your account here.&lt;/ TabsContent &gt;
 &lt; TabsContent value = &quot;password&quot; &gt;Change your password here.&lt;/ TabsContent &gt;
 &lt;/ Tabs &gt;
 Composition #
 Use the following composition to build Tabs :
 Copy Tabs
 ├── TabsList
 │ ├── TabsTrigger
 │ └── TabsTrigger
 ├── TabsContent
 └── TabsContent
 Examples #
 Line #
 Use the variant=&quot;line&quot; prop on TabsList for a line style.
 Overview Analytics Reports Copy import { Tabs, TabsList, TabsTrigger } from "@/components/ui/tabs"

 export function TabsLine () { View Code
 Vertical #
 Use orientation=&quot;vertical&quot; for vertical tabs.
 Account Password Notifications Copy import { Tabs, TabsList, TabsTrigger } from "@/components/ui/tabs"

 export function TabsVertical () { View Code
 Disabled #
 Home Disabled Copy import { Tabs, TabsList, TabsTrigger } from "@/components/ui/tabs"

 export function TabsDisabled () { View Code
 Icons #
 Preview Code Copy import { AppWindowIcon, CodeIcon } from "lucide-react"

 import { Tabs, TabsList, TabsTrigger } from "@/components/ui/tabs" View Code
 RTL #
 To enable RTL support in shadcn/ui, see the RTL configuration guide .
 Arabic (العربية) ▼ Toggle نظرة عامة التحليلات التقارير الإعدادات نظرة عامة عرض مقاييسك الرئيسية وأنشطة المشروع الأخيرة. تتبع التقدم عبر جميع مشاريعك النشطة. لديك ١٢ مشروعًا نشطًا و٣ مهام معلقة. Copy "use client"

 import * as React from "react" View Code
 API Reference #
 See the Radix Tabs documentation. Table Textarea On This Page Installation Usage Composition Examples Line Vertical Disabled Icons RTL API Reference Deploy your shadcn/ui app on Vercel Trusted by OpenAI, Sonos, Adobe, and more. Vercel provides tools and infrastructure to deploy apps and features at scale. Deploy Now Deploy to Vercel Built by shadcn at Vercel . The source code is available on GitHub . Get Code
