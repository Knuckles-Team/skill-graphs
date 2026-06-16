Button Group - shadcn/ui Toggle Menu Menu Home Docs Components Blocks Charts Directory Create Search documentation... Search... 117k Toggle theme New Sections Introduction Components Installation Theming CLI RTL Skills MCP Server Registry Forms Changelog Components Accordion Alert Alert Dialog Aspect Ratio Avatar Badge Breadcrumb Button Button Group Calendar Card Carousel Chart Checkbox Collapsible Combobox Command Context Menu Data Table Date Picker Dialog Direction Drawer Dropdown Menu Empty Field Hover Card Input Input Group Input OTP Item Kbd Label Menubar Native Select Navigation Menu Pagination Popover Progress Radio Group Resizable Scroll Area Select Separator Sheet Sidebar Skeleton Slider Sonner Spinner Switch Table Tabs Textarea Toast Toggle Toggle Group Tooltip Typography Get Started Installation components.json Package Imports Theming Dark Mode CLI Monorepo Skills JavaScript Figma llms.txt Legacy Docs Forms React Hook Form TanStack Form Formisch Registry Introduction Getting Started GitHub Registries Registry Directory Examples Namespaces Authentication MCP Server Open in v0 API Reference registry.json registry-item.json Button Group Copy Page Previous Next A container that groups related buttons together with consistent styling. Radix UI Base UI Radix UI Archive Report Snooze Copy "use client"

 import * as React from "react" View Code
 Installation #
 Command Manual pnpm npm yarn bun pnpm dlx shadcn@latest add button-group Copy
 Usage #
 Copy import {
 ButtonGroup,
 ButtonGroupSeparator,
 ButtonGroupText,
 } from &quot;@/components/ui/button-group&quot;
 Copy &lt; ButtonGroup &gt;
 &lt; Button &gt;Button 1&lt;/ Button &gt;
 &lt; Button &gt;Button 2&lt;/ Button &gt;
 &lt;/ ButtonGroup &gt;
 Composition #
 Use the following composition to build a ButtonGroup :
 Copy ButtonGroup
 ├── Button or Input
 ├── ButtonGroupSeparator
 └── ButtonGroupText
 Accessibility #

 The ButtonGroup component has the role attribute set to group .
 Use Tab to navigate between the buttons in the group.
 Use aria-label or aria-labelledby to label the button group.

 Copy &lt; ButtonGroup aria-label = &quot;Button group&quot; &gt;
 &lt; Button &gt;Button 1&lt;/ Button &gt;
 &lt; Button &gt;Button 2&lt;/ Button &gt;
 &lt;/ ButtonGroup &gt;
 ButtonGroup vs ToggleGroup #

 Use the ButtonGroup component when you want to group buttons that perform an action.
 Use the ToggleGroup component when you want to group buttons that toggle a state.

 Examples #
 Orientation #
 Set the orientation prop to change the button group layout.
 Copy import { MinusIcon, PlusIcon } from "lucide-react"

 import { Button } from "@/components/ui/button" View Code
 Size #
 Control the size of buttons using the size prop on individual buttons.
 Small Button Group Default Button Group Large Button Group Copy import { PlusIcon } from "lucide-react"

 import { Button } from "@/components/ui/button" View Code
 Nested #
 Nest &lt;ButtonGroup&gt; components to create button groups with spacing.
 Copy import { AudioLinesIcon, PlusIcon } from "lucide-react"

 import { Button } from "@/components/ui/button" View Code
 Separator #
 The ButtonGroupSeparator component visually divides buttons within a group.
 Buttons with variant outline do not need a separator since they have a border. For other variants, a separator is recommended to improve the visual hierarchy.
 Copy Paste Copy import { Button } from "@/components/ui/button"
 import {
 ButtonGroup, View Code
 Split #
 Create a split button group by adding two buttons separated by a ButtonGroupSeparator .
 Button Copy import { IconPlus } from "@tabler/icons-react"

 import { Button } from "@/components/ui/button" View Code
 Input #
 Wrap an Input component with buttons.
 Copy import { SearchIcon } from "lucide-react"

 import { Button } from "@/components/ui/button" View Code
 Input Group #
 Wrap an InputGroup component to create complex input layouts.
 Copy "use client"

 import * as React from "react" View Code
 Dropdown Menu #
 Create a split button group with a DropdownMenu component.
 Follow Copy "use client"

 import { View Code
 Select #
 Pair with a Select component.
 $ Copy "use client"

 import * as React from "react" View Code
 Popover #
 Use with a Popover component.
 Copilot Copy import { BotIcon, ChevronDownIcon } from "lucide-react"

 import { Button } from "@/components/ui/button" View Code
 RTL #
 To enable RTL support in shadcn/ui, see the RTL configuration guide .
 Arabic (العربية) ▼ Toggle أرشفة تقرير تأجيل Copy "use client"

 import * as React from "react" View Code
 API Reference #
 ButtonGroup #
 The ButtonGroup component is a container that groups related buttons together with consistent styling.
 Prop Type Default orientation &quot;horizontal&quot; | &quot;vertical&quot; &quot;horizontal&quot;
 Copy &lt; ButtonGroup &gt;
 &lt; Button &gt;Button 1&lt;/ Button &gt;
 &lt; Button &gt;Button 2&lt;/ Button &gt;
 &lt;/ ButtonGroup &gt;
 Nest multiple button groups to create complex layouts with spacing. See the nested example for more details.
 Copy &lt; ButtonGroup &gt;
 &lt; ButtonGroup /&gt;
 &lt; ButtonGroup /&gt;
 &lt;/ ButtonGroup &gt;
 ButtonGroupSeparator #
 The ButtonGroupSeparator component visually divides buttons within a group.
 Prop Type Default orientation &quot;horizontal&quot; | &quot;vertical&quot; &quot;vertical&quot;
 Copy &lt; ButtonGroup &gt;
 &lt; Button &gt;Button 1&lt;/ Button &gt;
 &lt; ButtonGroupSeparator /&gt;
 &lt; Button &gt;Button 2&lt;/ Button &gt;
 &lt;/ ButtonGroup &gt;
 ButtonGroupText #
 Use this component to display text within a button group.
 Prop Type Default asChild boolean false
 Copy &lt; ButtonGroup &gt;
 &lt; ButtonGroupText &gt;Text&lt;/ ButtonGroupText &gt;
 &lt; Button &gt;Button&lt;/ Button &gt;
 &lt;/ ButtonGroup &gt;
 Use the asChild prop to render a custom component as the text, for example a label.
 Copy import { ButtonGroupText } from &quot;@/components/ui/button-group&quot;
 import { Label } from &quot;@/components/ui/label&quot;

 export function ButtonGroupTextDemo () {
 return (
 &lt; ButtonGroup &gt;
 &lt; ButtonGroupText asChild &gt;
 &lt; Label htmlFor = &quot;name&quot; &gt;Text&lt;/ Label &gt;
 &lt;/ ButtonGroupText &gt;
 &lt; Input placeholder = &quot;Type something here...&quot; id = &quot;name&quot; /&gt;
 &lt;/ ButtonGroup &gt;
 )
 } Button Calendar On This Page Installation Usage Composition Accessibility ButtonGroup vs ToggleGroup Examples Orientation Size Nested Separator Split Input Input Group Dropdown Menu Select Popover RTL API Reference ButtonGroup ButtonGroupSeparator ButtonGroupText Deploy your shadcn/ui app on Vercel Trusted by OpenAI, Sonos, Adobe, and more. Vercel provides tools and infrastructure to deploy apps and features at scale. Deploy Now Deploy to Vercel Built by shadcn at Vercel . The source code is available on GitHub . Get Code
