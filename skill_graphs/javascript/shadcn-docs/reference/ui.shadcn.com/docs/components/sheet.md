Sheet - shadcn/ui Toggle Menu Menu Home Docs Components Blocks Charts Directory Create Search documentation... Search... 117k Toggle theme New Sections Introduction Components Installation Theming CLI RTL Skills MCP Server Registry Forms Changelog Components Accordion Alert Alert Dialog Aspect Ratio Avatar Badge Breadcrumb Button Button Group Calendar Card Carousel Chart Checkbox Collapsible Combobox Command Context Menu Data Table Date Picker Dialog Direction Drawer Dropdown Menu Empty Field Hover Card Input Input Group Input OTP Item Kbd Label Menubar Native Select Navigation Menu Pagination Popover Progress Radio Group Resizable Scroll Area Select Separator Sheet Sidebar Skeleton Slider Sonner Spinner Switch Table Tabs Textarea Toast Toggle Toggle Group Tooltip Typography Get Started Installation components.json Package Imports Theming Dark Mode CLI Monorepo Skills JavaScript Figma llms.txt Legacy Docs Forms React Hook Form TanStack Form Formisch Registry Introduction Getting Started GitHub Registries Registry Directory Examples Namespaces Authentication MCP Server Open in v0 API Reference registry.json registry-item.json Sheet Copy Page Previous Next Extends the Dialog component to display content that complements the main content of the screen. Radix UI Base UI Radix UI Open Copy import { Button } from "@/components/ui/button"
 import { Input } from "@/components/ui/input"
 import { Label } from "@/components/ui/label" View Code
 Installation #
 Command Manual pnpm npm yarn bun pnpm dlx shadcn@latest add sheet Copy
 Usage #
 Copy import {
 Sheet,
 SheetClose,
 SheetContent,
 SheetDescription,
 SheetFooter,
 SheetHeader,
 SheetTitle,
 SheetTrigger,
 } from &quot;@/components/ui/sheet&quot;
 Copy &lt; Sheet &gt;
 &lt; SheetTrigger &gt;Open&lt;/ SheetTrigger &gt;
 &lt; SheetContent &gt;
 &lt; SheetHeader &gt;
 &lt; SheetTitle &gt;Are you absolutely sure?&lt;/ SheetTitle &gt;
 &lt; SheetDescription &gt;This action cannot be undone.&lt;/ SheetDescription &gt;
 &lt;/ SheetHeader &gt;
 &lt;/ SheetContent &gt;
 &lt;/ Sheet &gt;
 Composition #
 Use the following composition to build a Sheet :
 Copy Sheet
 ├── SheetTrigger
 └── SheetContent
 ├── SheetHeader
 │ ├── SheetTitle
 │ └── SheetDescription
 └── SheetFooter
 Examples #
 Side #
 Use the side prop on SheetContent to set the edge of the screen where the sheet appears. Values are top , right , bottom , or left .
 top right bottom left Copy import { Button } from "@/components/ui/button"
 import {
 Sheet, View Code
 No Close Button #
 Use showCloseButton={false} on SheetContent to hide the close button.
 Open Sheet Copy import { Button } from "@/components/ui/button"
 import {
 Sheet, View Code
 RTL #
 To enable RTL support in shadcn/ui, see the RTL configuration guide .
 Arabic (العربية) ▼ Toggle فتح Copy "use client"

 import { View Code
 API Reference #
 See the Radix UI Dialog documentation. Separator Sidebar On This Page Installation Usage Composition Examples Side No Close Button RTL API Reference Deploy your shadcn/ui app on Vercel Trusted by OpenAI, Sonos, Adobe, and more. Vercel provides tools and infrastructure to deploy apps and features at scale. Deploy Now Deploy to Vercel Built by shadcn at Vercel . The source code is available on GitHub . Get Code
