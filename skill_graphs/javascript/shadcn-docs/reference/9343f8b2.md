Combobox - shadcn/ui Toggle Menu Menu Home Docs Components Blocks Charts Directory Create Search documentation... Search... 117k Toggle theme New Sections Introduction Components Installation Theming CLI RTL Skills MCP Server Registry Forms Changelog Components Accordion Alert Alert Dialog Aspect Ratio Avatar Badge Breadcrumb Button Button Group Calendar Card Carousel Chart Checkbox Collapsible Combobox Command Context Menu Data Table Date Picker Dialog Direction Drawer Dropdown Menu Empty Field Hover Card Input Input Group Input OTP Item Kbd Label Menubar Native Select Navigation Menu Pagination Popover Progress Radio Group Resizable Scroll Area Select Separator Sheet Sidebar Skeleton Slider Sonner Spinner Switch Table Tabs Textarea Toast Toggle Toggle Group Tooltip Typography Get Started Installation components.json Package Imports Theming Dark Mode CLI Monorepo Skills JavaScript Figma llms.txt Legacy Docs Forms React Hook Form TanStack Form Formisch Registry Introduction Getting Started GitHub Registries Registry Directory Examples Namespaces Authentication MCP Server Open in v0 API Reference registry.json registry-item.json Combobox Copy Page Previous Next Autocomplete input with a list of suggestions. Radix UI Base UI Radix UI Copy "use client"

 import { View Code
 Installation #
 Command Manual pnpm npm yarn bun pnpm dlx shadcn@latest add combobox Copy
 Usage #
 Copy import {
 Combobox,
 ComboboxContent,
 ComboboxEmpty,
 ComboboxInput,
 ComboboxItem,
 ComboboxList,
 } from &quot;@/components/ui/combobox&quot;
 Copy const frameworks = [ &quot;Next.js&quot; , &quot;SvelteKit&quot; , &quot;Nuxt.js&quot; , &quot;Remix&quot; , &quot;Astro&quot; ]

 export function ExampleCombobox () {
 return (
 &lt; Combobox items = { frameworks } &gt;
 &lt; ComboboxInput placeholder = &quot;Select a framework&quot; /&gt;
 &lt; ComboboxContent &gt;
 &lt; ComboboxEmpty &gt;No items found.&lt;/ ComboboxEmpty &gt;
 &lt; ComboboxList &gt;
 { ( item ) =&gt; (
 &lt; ComboboxItem key = { item } value = { item } &gt;
 { item }
 &lt;/ ComboboxItem &gt;
 ) }
 &lt;/ ComboboxList &gt;
 &lt;/ ComboboxContent &gt;
 &lt;/ Combobox &gt;
 )
 }
 Composition #
 Simple #
 A single-line input and a flat list (see Basic ).
 Copy Combobox
 ├── ComboboxInput
 └── ComboboxContent
 ├── ComboboxEmpty
 └── ComboboxList
 ├── ComboboxItem
 └── ComboboxItem
 With chips #
 Multi-select with multiple , chips, and a chips input (see Multiple ).
 Copy Combobox
 ├── ComboboxChips
 │ ├── ComboboxValue
 │ │ └── ComboboxChip
 │ └── ComboboxChipsInput
 └── ComboboxContent
 ├── ComboboxEmpty
 └── ComboboxList
 ├── ComboboxItem
 └── ComboboxItem
 With groups and collection #
 Nested items per group using ComboboxCollection inside each ComboboxGroup , with a separator between groups (see Groups ).
 Copy Combobox
 ├── ComboboxInput
 └── ComboboxContent
 ├── ComboboxEmpty
 └── ComboboxList
 ├── ComboboxGroup
 │ ├── ComboboxLabel
 │ └── ComboboxCollection
 │ ├── ComboboxItem
 │ └── ComboboxItem
 ├── ComboboxSeparator
 └── ComboboxGroup
 ├── ComboboxLabel
 └── ComboboxCollection
 ├── ComboboxItem
 └── ComboboxItem
 Custom Items #
 Use itemToStringValue when your items are objects.
 Copy import * as React from &quot;react&quot;

 import {
 Combobox,
 ComboboxContent,
 ComboboxEmpty,
 ComboboxInput,
 ComboboxItem,
 ComboboxList,
 } from &quot;@/components/ui/combobox&quot;

 type Framework = {
 label : string
 value : string
 }

 const frameworks : Framework [] = [
 { label: &quot;Next.js&quot; , value: &quot;next&quot; },
 { label: &quot;SvelteKit&quot; , value: &quot;sveltekit&quot; },
 { label: &quot;Nuxt&quot; , value: &quot;nuxt&quot; },
 ]

 export function ExampleComboboxCustomItems () {
 return (
 &lt; Combobox
 items = { frameworks }
 itemToStringValue = { ( framework ) =&gt; framework.label }
 &gt;
 &lt; ComboboxInput placeholder = &quot;Select a framework&quot; /&gt;
 &lt; ComboboxContent &gt;
 &lt; ComboboxEmpty &gt;No items found.&lt;/ ComboboxEmpty &gt;
 &lt; ComboboxList &gt;
 { ( framework ) =&gt; (
 &lt; ComboboxItem key = { framework.value } value = { framework } &gt;
 { framework.label }
 &lt;/ ComboboxItem &gt;
 ) }
 &lt;/ ComboboxList &gt;
 &lt;/ ComboboxContent &gt;
 &lt;/ Combobox &gt;
 )
 }
 Multiple Selection #
 Use multiple with chips for multi-select behavior.
 Copy import * as React from &quot;react&quot;

 import {
 Combobox,
 ComboboxChip,
 ComboboxChips,
 ComboboxChipsInput,
 ComboboxContent,
 ComboboxEmpty,
 ComboboxInput,
 ComboboxItem,
 ComboboxList,
 ComboboxValue,
 } from &quot;@/components/ui/combobox&quot;

 const frameworks = [ &quot;Next.js&quot; , &quot;SvelteKit&quot; , &quot;Nuxt.js&quot; , &quot;Remix&quot; , &quot;Astro&quot; ]

 export function ExampleComboboxMultiple () {
 const [ value , setValue ] = React. useState &lt; string []&gt;([])

 return (
 &lt; Combobox
 items = { frameworks }
 multiple
 value = { value }
 onValueChange = { setValue }
 &gt;
 &lt; ComboboxChips &gt;
 &lt; ComboboxValue &gt;
 { value. map (( item ) =&gt; (
 &lt; ComboboxChip key = { item } &gt; { item } &lt;/ ComboboxChip &gt;
 )) }
 &lt;/ ComboboxValue &gt;
 &lt; ComboboxChipsInput placeholder = &quot;Add framework&quot; /&gt;
 &lt;/ ComboboxChips &gt;
 &lt; ComboboxContent &gt;
 &lt; ComboboxEmpty &gt;No items found.&lt;/ ComboboxEmpty &gt;
 &lt; ComboboxList &gt;
 { ( item ) =&gt; (
 &lt; ComboboxItem key = { item } value = { item } &gt;
 { item }
 &lt;/ ComboboxItem &gt;
 ) }
 &lt;/ ComboboxList &gt;
 &lt;/ ComboboxContent &gt;
 &lt;/ Combobox &gt;
 )
 }
 Examples #
 Basic #
 A simple combobox with a list of frameworks.
 Copy "use client"

 import { View Code
 Multiple #
 A combobox with multiple selection using multiple and ComboboxChips .
 Next.js Copy "use client"

 import * as React from "react" View Code
 Clear Button #
 Use the showClear prop to show a clear button.
 Copy "use client"

 import { View Code
 Groups #
 Use ComboboxGroup and ComboboxSeparator to group items.
 Copy "use client"

 import { View Code
 Custom Items #
 You can render a custom component inside ComboboxItem .
 Copy "use client"

 import { View Code
 Invalid #
 Use the aria-invalid prop to make the combobox invalid.
 Copy "use client"

 import { View Code
 Disabled #
 Use the disabled prop to disable the combobox.
 Copy "use client"

 import { View Code
 Auto Highlight #
 Use the autoHighlight prop to automatically highlight the first item on filter.
 Copy "use client"

 import { View Code
 Popup #
 You can trigger the combobox from a button or any other component by using the render prop. Move the ComboboxInput inside the ComboboxContent .
 Select country Copy "use client"

 import { Button } from "@/components/ui/button" View Code
 Input Group #
 You can add an addon to the combobox by using the InputGroupAddon component inside the ComboboxInput .
 Copy "use client"

 import { GlobeIcon } from "lucide-react" View Code
 RTL #
 To enable RTL support in shadcn/ui, see the RTL configuration guide .
 Arabic (العربية) ▼ Toggle الفئات التكنولوجيا Copy "use client"

 import * as React from "react" View Code
 API Reference #
 See the Base UI documentation for more information. Collapsible Command On This Page Installation Usage Composition Simple With chips With groups and collection Custom Items Multiple Selection Examples Basic Multiple Clear Button Groups Custom Items Invalid Disabled Auto Highlight Popup Input Group RTL API Reference Deploy your shadcn/ui app on Vercel Trusted by OpenAI, Sonos, Adobe, and more. Vercel provides tools and infrastructure to deploy apps and features at scale. Deploy Now Deploy to Vercel Built by shadcn at Vercel . The source code is available on GitHub . Get Code
