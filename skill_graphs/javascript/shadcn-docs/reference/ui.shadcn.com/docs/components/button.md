Button - shadcn/ui Toggle Menu Menu Home Docs Components Blocks Charts Directory Create Search documentation... Search... 117k Toggle theme New Sections Introduction Components Installation Theming CLI RTL Skills MCP Server Registry Forms Changelog Components Accordion Alert Alert Dialog Aspect Ratio Avatar Badge Breadcrumb Button Button Group Calendar Card Carousel Chart Checkbox Collapsible Combobox Command Context Menu Data Table Date Picker Dialog Direction Drawer Dropdown Menu Empty Field Hover Card Input Input Group Input OTP Item Kbd Label Menubar Native Select Navigation Menu Pagination Popover Progress Radio Group Resizable Scroll Area Select Separator Sheet Sidebar Skeleton Slider Sonner Spinner Switch Table Tabs Textarea Toast Toggle Toggle Group Tooltip Typography Get Started Installation components.json Package Imports Theming Dark Mode CLI Monorepo Skills JavaScript Figma llms.txt Legacy Docs Forms React Hook Form TanStack Form Formisch Registry Introduction Getting Started GitHub Registries Registry Directory Examples Namespaces Authentication MCP Server Open in v0 API Reference registry.json registry-item.json Button Copy Page Previous Next Displays a button or a component that looks like a button. Radix UI Base UI Radix UI Button Copy import { ArrowUpIcon } from "lucide-react"

 import { Button } from "@/components/ui/button" View Code
 Installation #
 Command Manual pnpm npm yarn bun pnpm dlx shadcn@latest add button Copy
 Usage #
 Copy import { Button } from &quot;@/components/ui/button&quot;
 Copy &lt; Button variant = &quot;outline&quot; &gt;Button&lt;/ Button &gt;
 Cursor #
 Tailwind v4 switched from cursor: pointer to cursor: default for the button component.
 If you want to keep the cursor: pointer behavior, add the following code to your CSS file:
 You can also enable this during project setup with npx shadcn@latest init --pointer .
 globals.css Copy @layer base {
 button :not ( :disabled ),
 [ role = &quot;button&quot; ] :not ( :disabled ) {
 cursor : pointer ;
 }
 }
 Examples #
 Size #
 Use the size prop to change the size of the button.
 Extra Small Small Default Large Copy import { ArrowUpRightIcon } from "lucide-react"

 import { Button } from "@/components/ui/button" View Code
 Default #
 Button Copy import { Button } from "@/components/ui/button"

 export function ButtonDefault () { View Code
 Outline #
 Outline Copy import { Button } from "@/components/ui/button"

 export function ButtonOutline () { View Code
 Secondary #
 Secondary Copy import { Button } from "@/components/ui/button"

 export function ButtonSecondary () { View Code
 Ghost #
 Ghost Copy import { Button } from "@/components/ui/button"

 export function ButtonGhost () { View Code
 Destructive #
 Destructive Copy import { Button } from "@/components/ui/button"

 export function ButtonDestructive () { View Code
 Link #
 Link Copy import { Button } from "@/components/ui/button"

 export function ButtonLink () { View Code
 Icon #
 Copy import { CircleFadingArrowUpIcon } from "lucide-react"

 import { Button } from "@/components/ui/button" View Code
 With Icon #
 Remember to add the data-icon=&quot;inline-start&quot; or data-icon=&quot;inline-end&quot; attribute to the icon for the correct spacing.
 New Branch Copy import { IconGitBranch } from "@tabler/icons-react"

 import { Button } from "@/components/ui/button" View Code
 Rounded #
 Use the rounded-full class to make the button rounded.
 Copy import { ArrowUpIcon } from "lucide-react"

 import { Button } from "@/components/ui/button" View Code
 Spinner #
 Render a &lt;Spinner /&gt; component inside the button to show a loading state. Remember to add the data-icon=&quot;inline-start&quot; or data-icon=&quot;inline-end&quot; attribute to the spinner for the correct spacing.
 Generating Downloading Copy import { Button } from "@/components/ui/button"
 import { Spinner } from "@/components/ui/spinner"
 View Code
 Button Group #
 To create a button group, use the ButtonGroup component. See the Button Group documentation for more details.
 Archive Report Snooze Copy "use client"

 import * as React from "react" View Code
 As Child #
 You can use the asChild prop on &lt;Button /&gt; to make another component look like a button. Here&#x27;s an example of a link that looks like a button.
 Login Copy import Link from "next/link"

 import { Button } from "@/components/ui/button" View Code
 RTL #
 To enable RTL support in shadcn/ui, see the RTL configuration guide .
 Arabic (العربية) ▼ Toggle زر حذف إرسال جاري التحميل Copy "use client"

 import { ArrowRightIcon, PlusIcon } from "lucide-react" View Code
 API Reference #
 Button #
 The Button component is a wrapper around the button element that adds a variety of styles and functionality.
 Prop Type Default variant &quot;default&quot; | &quot;outline&quot; | &quot;ghost&quot; | &quot;destructive&quot; | &quot;secondary&quot; | &quot;link&quot; &quot;default&quot; size &quot;default&quot; | &quot;xs&quot; | &quot;sm&quot; | &quot;lg&quot; | &quot;icon&quot; | &quot;icon-xs&quot; | &quot;icon-sm&quot; | &quot;icon-lg&quot; &quot;default&quot; asChild boolean false Breadcrumb Button Group On This Page Installation Usage Cursor Examples Size Default Outline Secondary Ghost Destructive Link Icon With Icon Rounded Spinner Button Group As Child RTL API Reference Button Deploy your shadcn/ui app on Vercel Trusted by OpenAI, Sonos, Adobe, and more. Vercel provides tools and infrastructure to deploy apps and features at scale. Deploy Now Deploy to Vercel Built by shadcn at Vercel . The source code is available on GitHub . Get Code
