Native Select - shadcn/ui Toggle Menu Menu Home Docs Components Blocks Charts Directory Create Search documentation... Search... 117k Toggle theme New Sections Introduction Components Installation Theming CLI RTL Skills MCP Server Registry Forms Changelog Components Accordion Alert Alert Dialog Aspect Ratio Avatar Badge Breadcrumb Button Button Group Calendar Card Carousel Chart Checkbox Collapsible Combobox Command Context Menu Data Table Date Picker Dialog Direction Drawer Dropdown Menu Empty Field Hover Card Input Input Group Input OTP Item Kbd Label Menubar Native Select Navigation Menu Pagination Popover Progress Radio Group Resizable Scroll Area Select Separator Sheet Sidebar Skeleton Slider Sonner Spinner Switch Table Tabs Textarea Toast Toggle Toggle Group Tooltip Typography Get Started Installation components.json Package Imports Theming Dark Mode CLI Monorepo Skills JavaScript Figma llms.txt Legacy Docs Forms React Hook Form TanStack Form Formisch Registry Introduction Getting Started GitHub Registries Registry Directory Examples Namespaces Authentication MCP Server Open in v0 API Reference registry.json registry-item.json Native Select Copy Page Previous Next A styled native HTML select element with consistent design system integration. Radix UI Base UI Radix UI For a styled select component, see the Select
component.
 Select status Todo In Progress Done Cancelled Copy import {
 NativeSelect,
 NativeSelectOption, View Code
 Installation #
 Command Manual pnpm npm yarn bun pnpm dlx shadcn@latest add native-select Copy
 Usage #
 Copy import {
 NativeSelect,
 NativeSelectOptGroup,
 NativeSelectOption,
 } from &quot;@/components/ui/native-select&quot;
 Copy &lt; NativeSelect &gt;
 &lt; NativeSelectOption value = &quot;&quot; &gt;Select a fruit&lt;/ NativeSelectOption &gt;
 &lt; NativeSelectOption value = &quot;apple&quot; &gt;Apple&lt;/ NativeSelectOption &gt;
 &lt; NativeSelectOption value = &quot;banana&quot; &gt;Banana&lt;/ NativeSelectOption &gt;
 &lt; NativeSelectOption value = &quot;blueberry&quot; &gt;Blueberry&lt;/ NativeSelectOption &gt;
 &lt; NativeSelectOption value = &quot;pineapple&quot; &gt;Pineapple&lt;/ NativeSelectOption &gt;
 &lt;/ NativeSelect &gt;
 Composition #
 Simple #
 Options placed directly under NativeSelect (no NativeSelectOptGroup ).
 Copy NativeSelect
 ├── NativeSelectOption
 ├── NativeSelectOption
 ├── NativeSelectOption
 └── NativeSelectOption
 With groups #
 Use NativeSelectOptGroup to organize options into categories.
 Copy NativeSelect
 ├── NativeSelectOptGroup
 │ ├── NativeSelectOption
 │ └── NativeSelectOption
 └── NativeSelectOptGroup
 ├── NativeSelectOption
 └── NativeSelectOption
 Examples #
 Groups #
 Use NativeSelectOptGroup to organize options into categories.
 Select department Frontend Backend DevOps Sales Rep Account Manager Sales Director Customer Support Product Manager Operations Manager Copy import {
 NativeSelect,
 NativeSelectOptGroup, View Code
 Disabled #
 Add the disabled prop to the NativeSelect component to disable the select.
 Disabled Apple Banana Blueberry Copy import {
 NativeSelect,
 NativeSelectOption, View Code
 Invalid #
 Use aria-invalid to show validation errors and the data-invalid attribute to the Field component for styling.
 Error state Apple Banana Blueberry Copy import {
 NativeSelect,
 NativeSelectOption, View Code
 Native Select vs Select #

 Use NativeSelect for native browser behavior, better performance, or mobile-optimized dropdowns.
 Use Select for custom styling, animations, or complex interactions.

 RTL #
 To enable RTL support in shadcn/ui, see the RTL configuration guide .
 Arabic (العربية) ▼ Toggle اختر الحالة مهام قيد التنفيذ منجز ملغي Copy "use client"

 import * as React from "react" View Code
 API Reference #
 NativeSelect #
 The main select component that wraps the native HTML select element.
 Copy &lt; NativeSelect &gt;
 &lt; NativeSelectOption value = &quot;option1&quot; &gt;Option 1&lt;/ NativeSelectOption &gt;
 &lt; NativeSelectOption value = &quot;option2&quot; &gt;Option 2&lt;/ NativeSelectOption &gt;
 &lt;/ NativeSelect &gt;
 NativeSelectOption #
 Represents an individual option within the select.
 Prop Type Default value string disabled boolean false
 NativeSelectOptGroup #
 Groups related options together for better organization.
 Prop Type Default label string disabled boolean false
 Copy &lt; NativeSelectOptGroup label = &quot;Fruits&quot; &gt;
 &lt; NativeSelectOption value = &quot;apple&quot; &gt;Apple&lt;/ NativeSelectOption &gt;
 &lt; NativeSelectOption value = &quot;banana&quot; &gt;Banana&lt;/ NativeSelectOption &gt;
 &lt;/ NativeSelectOptGroup &gt; Menubar Navigation Menu On This Page Installation Usage Composition Simple With groups Examples Groups Disabled Invalid Native Select vs Select RTL API Reference NativeSelect NativeSelectOption NativeSelectOptGroup Deploy your shadcn/ui app on Vercel Trusted by OpenAI, Sonos, Adobe, and more. Vercel provides tools and infrastructure to deploy apps and features at scale. Deploy Now Deploy to Vercel Built by shadcn at Vercel . The source code is available on GitHub . Get Code
