Date Picker - shadcn/ui Toggle Menu Menu Home Docs Components Blocks Charts Directory Create Search documentation... Search... 117k Toggle theme New Sections Introduction Components Installation Theming CLI RTL Skills MCP Server Registry Forms Changelog Components Accordion Alert Alert Dialog Aspect Ratio Avatar Badge Breadcrumb Button Button Group Calendar Card Carousel Chart Checkbox Collapsible Combobox Command Context Menu Data Table Date Picker Dialog Direction Drawer Dropdown Menu Empty Field Hover Card Input Input Group Input OTP Item Kbd Label Menubar Native Select Navigation Menu Pagination Popover Progress Radio Group Resizable Scroll Area Select Separator Sheet Sidebar Skeleton Slider Sonner Spinner Switch Table Tabs Textarea Toast Toggle Toggle Group Tooltip Typography Get Started Installation components.json Package Imports Theming Dark Mode CLI Monorepo Skills JavaScript Figma llms.txt Legacy Docs Forms React Hook Form TanStack Form Formisch Registry Introduction Getting Started GitHub Registries Registry Directory Examples Namespaces Authentication MCP Server Open in v0 API Reference registry.json registry-item.json Date Picker Copy Page Previous Next A date picker component with range and presets. Radix UI Base UI Radix UI Pick a date Copy "use client"

 import * as React from "react" View Code
 Installation #
 The Date Picker is built using a composition of the &lt;Popover /&gt; and the &lt;Calendar /&gt; components.
 See installation instructions for the Popover and the Calendar components.
 Usage #
 components/example-date-picker.tsx Copy &quot;use client&quot;

 import * as React from &quot;react&quot;
 import { format } from &quot;date-fns&quot;
 import { Calendar as CalendarIcon } from &quot;lucide-react&quot;

 import { cn } from &quot;@/lib/utils&quot;
 import { Button } from &quot;@/components/ui/button&quot;
 import { Calendar } from &quot;@/components/ui/calendar&quot;
 import {
 Popover,
 PopoverContent,
 PopoverTrigger,
 } from &quot;@/components/ui/popover&quot;

 export function DatePickerDemo () {
 const [ date , setDate ] = React. useState &lt; Date &gt;()

 return (
 &lt; Popover &gt;
 &lt; PopoverTrigger asChild &gt;
 &lt; Button
 variant = &quot;outline&quot;
 data-empty = { ! date }
 className = &quot;w-[280px] justify-start text-left font-normal data-[empty=true]:text-muted-foreground&quot;
 &gt;
 &lt; CalendarIcon /&gt;
 { date ? format (date, &quot;PPP&quot; ) : &lt; span &gt;Pick a date&lt;/ span &gt; }
 &lt;/ Button &gt;
 &lt;/ PopoverTrigger &gt;
 &lt; PopoverContent className = &quot;w-auto p-0&quot; &gt;
 &lt; Calendar mode = &quot;single&quot; selected = { date } onSelect = { setDate } /&gt;
 &lt;/ PopoverContent &gt;
 &lt;/ Popover &gt;
 )
 }
 See the React DayPicker documentation for more information.
 Composition #
 A date picker is built from Popover and Calendar (there is no DatePicker root component):
 Copy Popover
 ├── PopoverTrigger
 └── PopoverContent
 └── Calendar
 Examples #
 Basic #
 A basic date picker component.
 Date Pick a date Copy "use client"

 import * as React from "react" View Code
 Range Picker #
 A date picker component for selecting a range of dates.
 Date Picker Range Jan 20, 2026 - Feb 09, 2026 Copy "use client"

 import * as React from "react" View Code
 Date of Birth #
 A date picker component for selecting a date of birth. This component includes a dropdown caption layout for date and month selection.
 Date of birth Select date Copy "use client"

 import * as React from "react" View Code
 Input #
 A date picker component with an input field for selecting a date.
 Subscription Date Select date Copy "use client"

 import * as React from "react" View Code
 Time Picker #
 A date picker component with a time input field for selecting a time.
 Date Select date Time Copy "use client"

 import * as React from "react" View Code
 Natural Language Picker #
 This component uses the chrono-node library to parse natural language dates.
 Schedule Date Select date Your post will be published on June 18, 2026 . Copy "use client"

 import * as React from "react" View Code
 RTL #
 To enable RTL support in shadcn/ui, see the RTL configuration guide .
 Arabic (العربية) ▼ Toggle اختر تاريخًا Copy "use client"

 import * as React from "react" View Code Data Table Dialog On This Page Installation Usage Composition Examples Basic Range Picker Date of Birth Input Time Picker Natural Language Picker RTL Deploy your shadcn/ui app on Vercel Trusted by OpenAI, Sonos, Adobe, and more. Vercel provides tools and infrastructure to deploy apps and features at scale. Deploy Now Deploy to Vercel Built by shadcn at Vercel . The source code is available on GitHub . Get Code
