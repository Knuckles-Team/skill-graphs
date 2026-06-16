Pagination - shadcn/ui Toggle Menu Menu Home Docs Components Blocks Charts Directory Create Search documentation... Search... 117k Toggle theme New Sections Introduction Components Installation Theming CLI RTL Skills MCP Server Registry Forms Changelog Components Accordion Alert Alert Dialog Aspect Ratio Avatar Badge Breadcrumb Button Button Group Calendar Card Carousel Chart Checkbox Collapsible Combobox Command Context Menu Data Table Date Picker Dialog Direction Drawer Dropdown Menu Empty Field Hover Card Input Input Group Input OTP Item Kbd Label Menubar Native Select Navigation Menu Pagination Popover Progress Radio Group Resizable Scroll Area Select Separator Sheet Sidebar Skeleton Slider Sonner Spinner Switch Table Tabs Textarea Toast Toggle Toggle Group Tooltip Typography Get Started Installation components.json Package Imports Theming Dark Mode CLI Monorepo Skills JavaScript Figma llms.txt Legacy Docs Forms React Hook Form TanStack Form Formisch Registry Introduction Getting Started GitHub Registries Registry Directory Examples Namespaces Authentication MCP Server Open in v0 API Reference registry.json registry-item.json Pagination Copy Page Previous Next Pagination with page navigation, next and previous links. Radix UI Base UI Radix UI Previous 1 2 3 More pages Next Copy import {
 Pagination,
 PaginationContent, View Code
 Installation #
 Command Manual pnpm npm yarn bun pnpm dlx shadcn@latest add pagination Copy
 Usage #
 Copy import {
 Pagination,
 PaginationContent,
 PaginationEllipsis,
 PaginationItem,
 PaginationLink,
 PaginationNext,
 PaginationPrevious,
 } from &quot;@/components/ui/pagination&quot;
 Copy &lt; Pagination &gt;
 &lt; PaginationContent &gt;
 &lt; PaginationItem &gt;
 &lt; PaginationPrevious href = &quot;#&quot; /&gt;
 &lt;/ PaginationItem &gt;
 &lt; PaginationItem &gt;
 &lt; PaginationLink href = &quot;#&quot; &gt;1&lt;/ PaginationLink &gt;
 &lt;/ PaginationItem &gt;
 &lt; PaginationItem &gt;
 &lt; PaginationLink href = &quot;#&quot; isActive &gt;
 2
 &lt;/ PaginationLink &gt;
 &lt;/ PaginationItem &gt;
 &lt; PaginationItem &gt;
 &lt; PaginationLink href = &quot;#&quot; &gt;3&lt;/ PaginationLink &gt;
 &lt;/ PaginationItem &gt;
 &lt; PaginationItem &gt;
 &lt; PaginationEllipsis /&gt;
 &lt;/ PaginationItem &gt;
 &lt; PaginationItem &gt;
 &lt; PaginationNext href = &quot;#&quot; /&gt;
 &lt;/ PaginationItem &gt;
 &lt;/ PaginationContent &gt;
 &lt;/ Pagination &gt;
 Composition #
 Use the following composition to build a Pagination :
 Copy Pagination
 └── PaginationContent
 ├── PaginationItem
 │ └── PaginationPrevious
 ├── PaginationItem
 │ └── PaginationLink
 ├── PaginationItem
 │ └── PaginationEllipsis
 └── PaginationItem
 └── PaginationNext
 Examples #
 Simple #
 A simple pagination with only page numbers.
 1 2 3 4 5 Copy import {
 Pagination,
 PaginationContent, View Code
 Icons Only #
 Use just the previous and next buttons without page numbers. This is useful for data tables with a rows per page selector.
 Rows per page Previous Next Copy import { Field, FieldLabel } from "@/components/ui/field"
 import {
 Pagination, View Code
 Next.js #
 By default the &lt;PaginationLink /&gt; component will render an &lt;a /&gt; tag.
 To use the Next.js &lt;Link /&gt; component, make the following updates to pagination.tsx .
 Copy + import Link from &quot;next/link&quot;

 - type PaginationLinkProps = ... &amp; React.ComponentProps&lt;&quot;a&quot;&gt;
 + type PaginationLinkProps = ... &amp; React.ComponentProps&lt; typeof Link &gt;

 const PaginationLink = ({...props }: ) =&gt; (
 &lt;PaginationItem&gt;
 - &lt;a&gt;
 + &lt;Link&gt;
 // ...
 - &lt;/a&gt;
 + &lt;/Link&gt;
 &lt;/PaginationItem&gt;
 )

 Note: We are making updates to the cli to automatically do this for you.
 RTL #
 To enable RTL support in shadcn/ui, see the RTL configuration guide .
 Arabic (العربية) ▼ Toggle السابق ١ ٢ ٣ More pages التالي Copy "use client"

 import * as React from "react" View Code
 Changelog #
 RTL Support #
 If you&#x27;re upgrading from a previous version of the Pagination component, you&#x27;ll need to apply the following updates to add the text prop:
 Update PaginationPrevious . Copy function PaginationPrevious({
 className,
 + text = &quot;Previous&quot;,
 ...props
 - }: React.ComponentProps&lt;typeof PaginationLink&gt;) {
 + }: React.ComponentProps&lt;typeof PaginationLink&gt; &amp; { text?: string }) {
 return (
 &lt;PaginationLink
 aria-label=&quot;Go to previous page&quot;
 size=&quot;default&quot;
 className={cn(&quot;cn-pagination-previous&quot;, className)}
 {...props}
 &gt;
 &lt;ChevronLeftIcon /&gt;
 &lt;span className=&quot;cn-pagination-previous-text hidden sm:block&quot;&gt;
 - Previous
 + {text}
 &lt;/span&gt;
 &lt;/PaginationLink&gt;
 )
 } Update PaginationNext . Copy function PaginationNext({
 className,
 + text = &quot;Next&quot;,
 ...props
 - }: React.ComponentProps&lt;typeof PaginationLink&gt;) {
 + }: React.ComponentProps&lt;typeof PaginationLink&gt; &amp; { text?: string }) {
 return (
 &lt;PaginationLink
 aria-label=&quot;Go to next page&quot;
 size=&quot;default&quot;
 className={cn(&quot;cn-pagination-next&quot;, className)}
 {...props}
 &gt;
 - &lt;span className=&quot;cn-pagination-next-text hidden sm:block&quot;&gt;Next&lt;/span&gt;
 + &lt;span className=&quot;cn-pagination-next-text hidden sm:block&quot;&gt;{text}&lt;/span&gt;
 &lt;ChevronRightIcon /&gt;
 &lt;/PaginationLink&gt;
 )
 } Navigation Menu Popover On This Page Installation Usage Composition Examples Simple Icons Only Next.js RTL Changelog RTL Support Deploy your shadcn/ui app on Vercel Trusted by OpenAI, Sonos, Adobe, and more. Vercel provides tools and infrastructure to deploy apps and features at scale. Deploy Now Deploy to Vercel Built by shadcn at Vercel . The source code is available on GitHub . Get Code
