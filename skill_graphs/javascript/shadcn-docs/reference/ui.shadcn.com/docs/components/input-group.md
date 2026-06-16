Input Group - shadcn/ui Toggle Menu Menu Home Docs Components Blocks Charts Directory Create Search documentation... Search... 117k Toggle theme New Sections Introduction Components Installation Theming CLI RTL Skills MCP Server Registry Forms Changelog Components Accordion Alert Alert Dialog Aspect Ratio Avatar Badge Breadcrumb Button Button Group Calendar Card Carousel Chart Checkbox Collapsible Combobox Command Context Menu Data Table Date Picker Dialog Direction Drawer Dropdown Menu Empty Field Hover Card Input Input Group Input OTP Item Kbd Label Menubar Native Select Navigation Menu Pagination Popover Progress Radio Group Resizable Scroll Area Select Separator Sheet Sidebar Skeleton Slider Sonner Spinner Switch Table Tabs Textarea Toast Toggle Toggle Group Tooltip Typography Get Started Installation components.json Package Imports Theming Dark Mode CLI Monorepo Skills JavaScript Figma llms.txt Legacy Docs Forms React Hook Form TanStack Form Formisch Registry Introduction Getting Started GitHub Registries Registry Directory Examples Namespaces Authentication MCP Server Open in v0 API Reference registry.json registry-item.json Input Group Copy Page Previous Next Add addons, buttons, and helper content to inputs. Radix UI Base UI Radix UI 12 results Copy import { Search } from "lucide-react"

 import { View Code
 Installation #
 Command Manual pnpm npm yarn bun pnpm dlx shadcn@latest add input-group Copy
 Usage #
 Copy import {
 InputGroup,
 InputGroupAddon,
 InputGroupButton,
 InputGroupInput,
 InputGroupText,
 InputGroupTextarea,
 } from &quot;@/components/ui/input-group&quot;
 Copy &lt; InputGroup &gt;
 &lt; InputGroupInput placeholder = &quot;Search...&quot; /&gt;
 &lt; InputGroupAddon &gt;
 &lt; SearchIcon /&gt;
 &lt;/ InputGroupAddon &gt;
 &lt;/ InputGroup &gt;
 Composition #
 Use the following composition to build an InputGroup :
 Copy InputGroup
 ├── InputGroupInput or InputGroupTextarea
 ├── InputGroupAddon
 ├── InputGroupButton
 └── InputGroupText
 Align #
 Use the align prop on InputGroupAddon to position the addon relative to the input.
 For proper focus management, InputGroupAddon should always be placed after
 InputGroupInput or InputGroupTextarea in the DOM. Use the align prop to
visually position the addon.
 inline-start #
 Use align=&quot;inline-start&quot; to position the addon at the start of the input. This is the default.
 Input Icon positioned at the start. Copy import { SearchIcon } from "lucide-react"

 import { View Code
 inline-end #
 Use align=&quot;inline-end&quot; to position the addon at the end of the input.
 Input Icon positioned at the end. Copy import { EyeOffIcon } from "lucide-react"

 import { View Code
 block-start #
 Use align=&quot;block-start&quot; to position the addon above the input.
 Input Full Name Header positioned above the input. Textarea script.js Copy Header positioned above the textarea. Copy import { CopyIcon, FileCodeIcon } from "lucide-react"

 import { View Code
 block-end #
 Use align=&quot;block-end&quot; to position the addon below the input.
 Input USD Footer positioned below the input. Textarea 0/280 Post Footer positioned below the textarea. Copy import {
 Field,
 FieldDescription, View Code
 Examples #
 Icon #
 Copy import {
 CheckIcon,
 CreditCardIcon, View Code
 Text #
 $ USD https:// .com @company.com 120 characters left Copy import {
 InputGroup,
 InputGroupAddon, View Code
 Button #
 https:// Search Copy "use client"

 import * as React from "react" View Code
 Kbd #
 ⌘K Copy import { SearchIcon } from "lucide-react"

 import { View Code
 Dropdown #
 Search In... Copy import { ChevronDownIcon, MoreHorizontal } from "lucide-react"

 import { View Code
 Spinner #
 Saving... Please wait... Copy import { LoaderIcon } from "lucide-react"

 import { View Code
 Textarea #
 Line 1, Column 1 Run script.js Copy import {
 IconBrandJavascript,
 IconCopy, View Code
 Custom Input #
 Add the data-slot=&quot;input-group-control&quot; attribute to your custom input for automatic focus state handling.
 Here&#x27;s an example of a custom resizable textarea from a third-party library.
 Submit Copy "use client"

 import TextareaAutosize from "react-textarea-autosize" View Code
 RTL #
 To enable RTL support in shadcn/ui, see the RTL configuration guide .
 Arabic (العربية) ▼ Toggle ١٢ نتيجة جاري الحفظ... منطقة النص ٠/٢٨٠ نشر تذييل موضع أسفل منطقة النص. Copy "use client"

 import * as React from "react" View Code
 API Reference #
 InputGroup #
 The main component that wraps inputs and addons.
 Prop Type Default className string
 Copy &lt; InputGroup &gt;
 &lt; InputGroupInput /&gt;
 &lt; InputGroupAddon /&gt;
 &lt;/ InputGroup &gt;
 InputGroupAddon #
 Displays icons, text, buttons, or other content alongside inputs.
 Focus Navigation For proper focus navigation, the InputGroupAddon component should be placed
after the input. Set the align prop to position the addon.
 Prop Type Default align &quot;inline-start&quot; | &quot;inline-end&quot; | &quot;block-start&quot; | &quot;block-end&quot; &quot;inline-start&quot; className string
 Copy &lt; InputGroupAddon align = &quot;inline-end&quot; &gt;
 &lt; SearchIcon /&gt;
 &lt;/ InputGroupAddon &gt;
 For &lt;InputGroupInput /&gt; , use the inline-start or inline-end alignment. For &lt;InputGroupTextarea /&gt; , use the block-start or block-end alignment.
 The InputGroupAddon component can have multiple InputGroupButton components and icons.
 Copy &lt; InputGroupAddon &gt;
 &lt; InputGroupButton &gt;Button&lt;/ InputGroupButton &gt;
 &lt; InputGroupButton &gt;Button&lt;/ InputGroupButton &gt;
 &lt;/ InputGroupAddon &gt;
 InputGroupButton #
 Displays buttons within input groups.
 Prop Type Default size &quot;xs&quot; | &quot;icon-xs&quot; | &quot;sm&quot; | &quot;icon-sm&quot; &quot;xs&quot; variant &quot;default&quot; | &quot;destructive&quot; | &quot;outline&quot; | &quot;secondary&quot; | &quot;ghost&quot; | &quot;link&quot; &quot;ghost&quot; className string
 Copy &lt; InputGroupButton &gt;Button&lt;/ InputGroupButton &gt;
 &lt; InputGroupButton size = &quot;icon-xs&quot; aria-label = &quot;Copy&quot; &gt;
 &lt; CopyIcon /&gt;
 &lt;/ InputGroupButton &gt;
 InputGroupInput #
 Replacement for &lt;Input /&gt; when building input groups. This component has the input group styles pre-applied and uses the unified data-slot=&quot;input-group-control&quot; for focus state handling.
 Prop Type Default className string
 All other props are passed through to the underlying &lt;Input /&gt; component.
 Copy &lt; InputGroup &gt;
 &lt; InputGroupInput placeholder = &quot;Enter text...&quot; /&gt;
 &lt; InputGroupAddon &gt;
 &lt; SearchIcon /&gt;
 &lt;/ InputGroupAddon &gt;
 &lt;/ InputGroup &gt;
 InputGroupTextarea #
 Replacement for &lt;Textarea /&gt; when building input groups. This component has the textarea group styles pre-applied and uses the unified data-slot=&quot;input-group-control&quot; for focus state handling.
 Prop Type Default className string
 All other props are passed through to the underlying &lt;Textarea /&gt; component.
 Copy &lt; InputGroup &gt;
 &lt; InputGroupTextarea placeholder = &quot;Enter message...&quot; /&gt;
 &lt; InputGroupAddon align = &quot;block-end&quot; &gt;
 &lt; InputGroupButton &gt;Send&lt;/ InputGroupButton &gt;
 &lt;/ InputGroupAddon &gt;
 &lt;/ InputGroup &gt;
 Changelog #
 2025-10-06 InputGroup #
 Add the min-w-0 class to the InputGroup component. See diff . Input Input OTP On This Page Installation Usage Composition Align inline-start inline-end block-start block-end Examples Icon Text Button Kbd Dropdown Spinner Textarea Custom Input RTL API Reference InputGroup InputGroupAddon InputGroupButton InputGroupInput InputGroupTextarea Changelog 2025-10-06 InputGroup Deploy your shadcn/ui app on Vercel Trusted by OpenAI, Sonos, Adobe, and more. Vercel provides tools and infrastructure to deploy apps and features at scale. Deploy Now Deploy to Vercel Built by shadcn at Vercel . The source code is available on GitHub . Get Code
