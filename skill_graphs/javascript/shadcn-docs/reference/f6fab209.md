Table - shadcn/ui Toggle Menu Menu Home Docs Components Blocks Charts Directory Create Search documentation... Search... 117k Toggle theme New Sections Introduction Components Installation Theming CLI RTL Skills MCP Server Registry Forms Changelog Components Accordion Alert Alert Dialog Aspect Ratio Avatar Badge Breadcrumb Button Button Group Calendar Card Carousel Chart Checkbox Collapsible Combobox Command Context Menu Data Table Date Picker Dialog Direction Drawer Dropdown Menu Empty Field Hover Card Input Input Group Input OTP Item Kbd Label Menubar Native Select Navigation Menu Pagination Popover Progress Radio Group Resizable Scroll Area Select Separator Sheet Sidebar Skeleton Slider Sonner Spinner Switch Table Tabs Textarea Toast Toggle Toggle Group Tooltip Typography Get Started Installation components.json Package Imports Theming Dark Mode CLI Monorepo Skills JavaScript Figma llms.txt Legacy Docs Forms React Hook Form TanStack Form Formisch Registry Introduction Getting Started GitHub Registries Registry Directory Examples Namespaces Authentication MCP Server Open in v0 API Reference registry.json registry-item.json Table Copy Page Previous Next A responsive table component. Radix UI Base UI Radix UI A list of your recent invoices. Invoice Status Method Amount INV001 Paid Credit Card $250.00 INV002 Pending PayPal $150.00 INV003 Unpaid Bank Transfer $350.00 INV004 Paid Credit Card $450.00 INV005 Paid PayPal $550.00 INV006 Pending Bank Transfer $200.00 INV007 Unpaid Credit Card $300.00 Total $2,500.00 Copy import {
 Table,
 TableBody, View Code
 Installation #
 Command Manual pnpm npm yarn bun pnpm dlx shadcn@latest add table Copy
 Usage #
 Copy import {
 Table,
 TableBody,
 TableCaption,
 TableCell,
 TableHead,
 TableHeader,
 TableRow,
 } from &quot;@/components/ui/table&quot;
 Copy &lt; Table &gt;
 &lt; TableCaption &gt;A list of your recent invoices.&lt;/ TableCaption &gt;
 &lt; TableHeader &gt;
 &lt; TableRow &gt;
 &lt; TableHead className = &quot;w-[100px]&quot; &gt;Invoice&lt;/ TableHead &gt;
 &lt; TableHead &gt;Status&lt;/ TableHead &gt;
 &lt; TableHead &gt;Method&lt;/ TableHead &gt;
 &lt; TableHead className = &quot;text-right&quot; &gt;Amount&lt;/ TableHead &gt;
 &lt;/ TableRow &gt;
 &lt;/ TableHeader &gt;
 &lt; TableBody &gt;
 &lt; TableRow &gt;
 &lt; TableCell className = &quot;font-medium&quot; &gt;INV001&lt;/ TableCell &gt;
 &lt; TableCell &gt;Paid&lt;/ TableCell &gt;
 &lt; TableCell &gt;Credit Card&lt;/ TableCell &gt;
 &lt; TableCell className = &quot;text-right&quot; &gt;$250.00&lt;/ TableCell &gt;
 &lt;/ TableRow &gt;
 &lt;/ TableBody &gt;
 &lt;/ Table &gt;
 Composition #
 Use the following composition to build a Table :
 Copy Table
 ├── TableCaption
 ├── TableHeader
 │ └── TableRow
 │ ├── TableHead
 │ ├── TableHead
 │ ├── TableHead
 │ └── TableHead
 ├── TableBody
 │ ├── TableRow
 │ │ ├── TableCell
 │ │ ├── TableCell
 │ │ ├── TableCell
 │ │ └── TableCell
 │ └── TableRow
 │ ├── TableCell
 │ ├── TableCell
 │ ├── TableCell
 │ └── TableCell
 └── TableFooter
 Examples #
 Footer #
 Use the &lt;TableFooter /&gt; component to add a footer to the table.
 A list of your recent invoices. Invoice Status Method Amount INV001 Paid Credit Card $250.00 INV002 Pending PayPal $150.00 INV003 Unpaid Bank Transfer $350.00 Total $2,500.00 Copy import {
 Table,
 TableBody, View Code
 Actions #
 A table showing actions for each row using a &lt;DropdownMenu /&gt; component.
 Product Price Actions Wireless Mouse $29.99 Open menu Mechanical Keyboard $129.99 Open menu USB-C Hub $49.99 Open menu Copy import { MoreHorizontalIcon } from "lucide-react"

 import { Button } from "@/components/ui/button" View Code
 Data Table #
 You can use the &lt;Table /&gt; component to build more complex data tables. Combine it with @tanstack/react-table to create tables with sorting, filtering and pagination.
 See the Data Table documentation for more information.
 You can also see an example of a data table in the Tasks demo.
 RTL #
 To enable RTL support in shadcn/ui, see the RTL configuration guide .
 Arabic (العربية) ▼ Toggle قائمة بفواتيرك الأخيرة. الفاتورة الحالة الطريقة المبلغ INV001 مدفوع بطاقة ائتمانية $250.00 INV002 قيد الانتظار PayPal $150.00 INV003 غير مدفوع تحويل بنكي $350.00 INV004 مدفوع بطاقة ائتمانية $450.00 INV005 مدفوع PayPal $550.00 INV006 قيد الانتظار تحويل بنكي $200.00 INV007 غير مدفوع بطاقة ائتمانية $300.00 المجموع $2,500.00 Copy "use client"

 import * as React from "react" View Code Switch Tabs On This Page Installation Usage Composition Examples Footer Actions Data Table RTL Deploy your shadcn/ui app on Vercel Trusted by OpenAI, Sonos, Adobe, and more. Vercel provides tools and infrastructure to deploy apps and features at scale. Deploy Now Deploy to Vercel Built by shadcn at Vercel . The source code is available on GitHub . Get Code
