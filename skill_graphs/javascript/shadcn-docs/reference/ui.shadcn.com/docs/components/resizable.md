Resizable - shadcn/ui Toggle Menu Menu Home Docs Components Blocks Charts Directory Create Search documentation... Search... 117k Toggle theme New Sections Introduction Components Installation Theming CLI RTL Skills MCP Server Registry Forms Changelog Components Accordion Alert Alert Dialog Aspect Ratio Avatar Badge Breadcrumb Button Button Group Calendar Card Carousel Chart Checkbox Collapsible Combobox Command Context Menu Data Table Date Picker Dialog Direction Drawer Dropdown Menu Empty Field Hover Card Input Input Group Input OTP Item Kbd Label Menubar Native Select Navigation Menu Pagination Popover Progress Radio Group Resizable Scroll Area Select Separator Sheet Sidebar Skeleton Slider Sonner Spinner Switch Table Tabs Textarea Toast Toggle Toggle Group Tooltip Typography Get Started Installation components.json Package Imports Theming Dark Mode CLI Monorepo Skills JavaScript Figma llms.txt Legacy Docs Forms React Hook Form TanStack Form Formisch Registry Introduction Getting Started GitHub Registries Registry Directory Examples Namespaces Authentication MCP Server Open in v0 API Reference registry.json registry-item.json Resizable Copy Page Previous Next Accessible resizable panel groups and layouts with keyboard support. Radix UI Base UI Radix UI One Two Three Copy import {
 ResizableHandle,
 ResizablePanel, View Code
 About #
 The Resizable component is built on top of react-resizable-panels by bvaughn .
 Installation #
 Command Manual pnpm npm yarn bun pnpm dlx shadcn@latest add resizable Copy
 Usage #
 Copy import {
 ResizableHandle,
 ResizablePanel,
 ResizablePanelGroup,
 } from &quot;@/components/ui/resizable&quot;
 Copy &lt; ResizablePanelGroup orientation = &quot;horizontal&quot; &gt;
 &lt; ResizablePanel &gt;One&lt;/ ResizablePanel &gt;
 &lt; ResizableHandle /&gt;
 &lt; ResizablePanel &gt;Two&lt;/ ResizablePanel &gt;
 &lt;/ ResizablePanelGroup &gt;
 Composition #
 Use the following composition to build a ResizablePanelGroup :
 Copy ResizablePanelGroup
 ├── ResizablePanel
 ├── ResizableHandle
 └── ResizablePanel
 Examples #
 Vertical #
 Use orientation=&quot;vertical&quot; for vertical resizing.
 Header Content Copy import {
 ResizableHandle,
 ResizablePanel, View Code
 Handle #
 Use the withHandle prop on ResizableHandle to show a visible handle.
 Sidebar Content Copy import {
 ResizableHandle,
 ResizablePanel, View Code
 RTL #
 To enable RTL support in shadcn/ui, see the RTL configuration guide .
 Arabic (العربية) ▼ Toggle واحد اثنان ثلاثة Copy "use client"

 import * as React from "react" View Code
 API Reference #
 See the react-resizable-panels documentation.
 Changelog #
 2025-02-02 react-resizable-panels v4 #
 Updated to react-resizable-panels v4. See the v4.0.0 release notes for full details.
 If you&#x27;re using react-resizable-panels primitives directly, note the following changes:
 v3 v4 PanelGroup Group PanelResizeHandle Separator direction prop orientation prop defaultSize={50} defaultSize=&quot;50%&quot; onLayout onLayoutChange ImperativePanelHandle PanelImperativeHandle ref prop on Panel panelRef prop data-panel-group-direction aria-orientation
 The shadcn/ui wrapper components ( ResizablePanelGroup , ResizablePanel ,
 ResizableHandle ) remain unchanged. Radio Group Scroll Area On This Page About Installation Usage Composition Examples Vertical Handle RTL API Reference Changelog 2025-02-02 react-resizable-panels v4 Deploy your shadcn/ui app on Vercel Trusted by OpenAI, Sonos, Adobe, and more. Vercel provides tools and infrastructure to deploy apps and features at scale. Deploy Now Deploy to Vercel Built by shadcn at Vercel . The source code is available on GitHub . Get Code
