Kbd - shadcn/ui Toggle Menu Menu Home Docs Components Blocks Charts Directory Create Search documentation... Search... 117k Toggle theme New Sections Introduction Components Installation Theming CLI RTL Skills MCP Server Registry Forms Changelog Components Accordion Alert Alert Dialog Aspect Ratio Avatar Badge Breadcrumb Button Button Group Calendar Card Carousel Chart Checkbox Collapsible Combobox Command Context Menu Data Table Date Picker Dialog Direction Drawer Dropdown Menu Empty Field Hover Card Input Input Group Input OTP Item Kbd Label Menubar Native Select Navigation Menu Pagination Popover Progress Radio Group Resizable Scroll Area Select Separator Sheet Sidebar Skeleton Slider Sonner Spinner Switch Table Tabs Textarea Toast Toggle Toggle Group Tooltip Typography Get Started Installation components.json Package Imports Theming Dark Mode CLI Monorepo Skills JavaScript Figma llms.txt Legacy Docs Forms React Hook Form TanStack Form Formisch Registry Introduction Getting Started GitHub Registries Registry Directory Examples Namespaces Authentication MCP Server Open in v0 API Reference registry.json registry-item.json Kbd Copy Page Previous Next Used to display textual user input from keyboard. Radix UI Base UI Radix UI ⌘ ⇧ ⌥ ⌃ Ctrl + B Copy import { Kbd, KbdGroup } from "@/components/ui/kbd"

 export function KbdDemo () { View Code
 Installation #
 Command Manual pnpm npm yarn bun pnpm dlx shadcn@latest add kbd Copy
 Usage #
 Copy import { Kbd } from &quot;@/components/ui/kbd&quot;
 Copy &lt; Kbd &gt;Ctrl&lt;/ Kbd &gt;
 Composition #
 Use the following composition to build Kbd and KbdGroup :
 Copy Kbd
 KbdGroup
 ├── Kbd
 └── Kbd
 Examples #
 Group #
 Use the KbdGroup component to group keyboard keys together.
 Use Ctrl + B Ctrl + K to open the command palette Copy import { Kbd, KbdGroup } from "@/components/ui/kbd"

 export function KbdGroupExample () { View Code
 Button #
 Use the Kbd component inside a Button component to display a keyboard key inside a button.
 Accept ⏎ Copy import { Button } from "@/components/ui/button"
 import { Kbd } from "@/components/ui/kbd"
 View Code
 Tooltip #
 You can use the Kbd component inside a Tooltip component to display a tooltip with a keyboard key.
 Save Print Copy import { Button } from "@/components/ui/button"
 import { ButtonGroup } from "@/components/ui/button-group"
 import { Kbd, KbdGroup } from "@/components/ui/kbd" View Code
 Input Group #
 You can use the Kbd component inside a InputGroupAddon component to display a keyboard key inside an input group.
 ⌘ K Copy import { SearchIcon } from "lucide-react"

 import { View Code
 RTL #
 To enable RTL support in shadcn/ui, see the RTL configuration guide .
 Arabic (العربية) ▼ Toggle ⌘ ⇧ ⌥ ⌃ Ctrl + B Copy "use client"

 import * as React from "react" View Code
 API Reference #
 Kbd #
 Use the Kbd component to display a keyboard key.
 Prop Type Default className string ``
 Copy &lt; Kbd &gt;Ctrl&lt;/ Kbd &gt;
 KbdGroup #
 Use the KbdGroup component to group Kbd components together.
 Prop Type Default className string ``
 Copy &lt; KbdGroup &gt;
 &lt; Kbd &gt;Ctrl&lt;/ Kbd &gt;
 &lt; Kbd &gt;B&lt;/ Kbd &gt;
 &lt;/ KbdGroup &gt; Item Label On This Page Installation Usage Composition Examples Group Button Tooltip Input Group RTL API Reference Kbd KbdGroup Deploy your shadcn/ui app on Vercel Trusted by OpenAI, Sonos, Adobe, and more. Vercel provides tools and infrastructure to deploy apps and features at scale. Deploy Now Deploy to Vercel Built by shadcn at Vercel . The source code is available on GitHub . Get Code
