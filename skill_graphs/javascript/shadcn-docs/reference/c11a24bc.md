Chart - shadcn/ui Toggle Menu Menu Home Docs Components Blocks Charts Directory Create Search documentation... Search... 117k Toggle theme New Sections Introduction Components Installation Theming CLI RTL Skills MCP Server Registry Forms Changelog Components Accordion Alert Alert Dialog Aspect Ratio Avatar Badge Breadcrumb Button Button Group Calendar Card Carousel Chart Checkbox Collapsible Combobox Command Context Menu Data Table Date Picker Dialog Direction Drawer Dropdown Menu Empty Field Hover Card Input Input Group Input OTP Item Kbd Label Menubar Native Select Navigation Menu Pagination Popover Progress Radio Group Resizable Scroll Area Select Separator Sheet Sidebar Skeleton Slider Sonner Spinner Switch Table Tabs Textarea Toast Toggle Toggle Group Tooltip Typography Get Started Installation components.json Package Imports Theming Dark Mode CLI Monorepo Skills JavaScript Figma llms.txt Legacy Docs Forms React Hook Form TanStack Form Formisch Registry Introduction Getting Started GitHub Registries Registry Directory Examples Namespaces Authentication MCP Server Open in v0 API Reference registry.json registry-item.json Chart Copy Page Previous Next Beautiful charts. Built using Recharts. Copy and paste into your apps. Radix UI Base UI Radix UI Updated: The chart component now uses Recharts v3. If you&#x27;re upgrading existing chart code, see Updating to Recharts v3 .
 Bar Chart - Interactive Showing total visitors for the last 3 months Desktop 7,324 Mobile 7,250
 Introducing Charts . A collection of chart components that you can copy and paste into your apps.
 Charts are designed to look great out of the box. They work well with the other components and are fully customizable to fit your project.
 Browse the Charts Library .
 Component #
 We use Recharts under the hood.
 We designed the chart component with composition in mind. You build your charts using Recharts components and only bring in custom components, such as ChartTooltip , when and where you need it .
 Copy import { Bar, BarChart } from &quot;recharts&quot;

 import { ChartContainer , ChartTooltipContent } from &quot;@/components/ui/chart&quot;

 export function MyChart () {
 return (
 &lt; ChartContainer &gt;
 &lt; BarChart data = { data } &gt;
 &lt; Bar dataKey = &quot;value&quot; /&gt;
 &lt; ChartTooltip content = { &lt; ChartTooltipContent /&gt; } /&gt;
 &lt;/ BarChart &gt;
 &lt;/ ChartContainer &gt;
 )
 }
 We do not wrap Recharts. This means you&#x27;re not locked into an abstraction. When a new Recharts version is released, you can follow the official upgrade path to upgrade your charts.
 The components are yours .
 Updating to Recharts v3 #
 If you&#x27;re updating older chart code to Recharts v3:

 Use var(--chart-1) instead of hsl(var(--chart-1)) when you reference chart tokens from your CSS variables.
 Use ChartTooltip.defaultIndex for initial tooltip state only. Keep persistent active shapes in your own chart state.
 Remove layout from &lt;Bar&gt; when the parent &lt;BarChart&gt; already defines it.
 Keep a height, min-h-* , or aspect-* on ChartContainer so ResponsiveContainer can measure on first render.

 Installation #
 Command Manual pnpm npm yarn bun pnpm dlx shadcn@latest add chart Copy
 Your First Chart #
 Let&#x27;s build your first chart. We&#x27;ll build a bar chart, add a grid, axis, tooltip and legend.
 Start by defining your data The following data represents the number of desktop and mobile users for each month. Note: Your data can be in any shape. You are not limited to the shape of the data below. Use the dataKey prop to map your data to the chart. components/example-chart.tsx Copy const chartData = [
 { month: &quot;January&quot; , desktop: 186 , mobile: 80 },
 { month: &quot;February&quot; , desktop: 305 , mobile: 200 },
 { month: &quot;March&quot; , desktop: 237 , mobile: 120 },
 { month: &quot;April&quot; , desktop: 73 , mobile: 190 },
 { month: &quot;May&quot; , desktop: 209 , mobile: 130 },
 { month: &quot;June&quot; , desktop: 214 , mobile: 140 },
 ] Define your chart config The chart config holds configuration for the chart. This is where you place human-readable strings, such as labels, icons and color tokens for theming. components/example-chart.tsx Copy import { type ChartConfig } from &quot;@/components/ui/chart&quot;

 const chartConfig = {
 desktop: {
 label: &quot;Desktop&quot; ,
 color: &quot;#2563eb&quot; ,
 },
 mobile: {
 label: &quot;Mobile&quot; ,
 color: &quot;#60a5fa&quot; ,
 },
 } satisfies ChartConfig Build your chart You can now build your chart using Recharts components. Important: Remember to set a min-h-[VALUE] on the ChartContainer component. This is required for the chart to be responsive. Copy "use client"

 import { Bar, BarChart } from "recharts" View Code
 Add a Grid #
 Let&#x27;s add a grid to the chart.
 Import the CartesianGrid component. Copy import { Bar, BarChart, CartesianGrid } from &quot;recharts&quot; Add the CartesianGrid component to your chart. Copy &lt; ChartContainer config = { chartConfig } className = &quot;min-h-[200px] w-full&quot; &gt;
 &lt; BarChart accessibilityLayer data = { chartData } &gt;
 &lt; CartesianGrid vertical = { false } /&gt;
 &lt; Bar dataKey = &quot;desktop&quot; fill = &quot;var(--color-desktop)&quot; radius = { 4 } /&gt;
 &lt; Bar dataKey = &quot;mobile&quot; fill = &quot;var(--color-mobile)&quot; radius = { 4 } /&gt;
 &lt;/ BarChart &gt;
 &lt;/ ChartContainer &gt; Copy "use client"

 import { Bar, BarChart, CartesianGrid } from "recharts" View Code
 Add an Axis #
 To add an x-axis to the chart, we&#x27;ll use the XAxis component.
 Import the XAxis component. Copy import { Bar, BarChart, CartesianGrid, XAxis } from &quot;recharts&quot; Add the XAxis component to your chart. Copy &lt; ChartContainer config = { chartConfig } className = &quot;h-[200px] w-full&quot; &gt;
 &lt; BarChart accessibilityLayer data = { chartData } &gt;
 &lt; CartesianGrid vertical = { false } /&gt;
 &lt; XAxis
 dataKey = &quot;month&quot;
 tickLine = { false }
 tickMargin = { 10 }
 axisLine = { false }
 tickFormatter = { ( value ) =&gt; value. slice ( 0 , 3 ) }
 /&gt;
 &lt; Bar dataKey = &quot;desktop&quot; fill = &quot;var(--color-desktop)&quot; radius = { 4 } /&gt;
 &lt; Bar dataKey = &quot;mobile&quot; fill = &quot;var(--color-mobile)&quot; radius = { 4 } /&gt;
 &lt;/ BarChart &gt;
 &lt;/ ChartContainer &gt; Copy "use client"

 import { Bar, BarChart, CartesianGrid, XAxis } from "recharts" View Code
 Add Tooltip #
 So far we&#x27;ve only used components from Recharts. They look great out of the box thanks to some customization in the chart component.
 To add a tooltip, we&#x27;ll use the custom ChartTooltip and ChartTooltipContent components from chart .
 Import the ChartTooltip and ChartTooltipContent components. Copy import { ChartTooltip, ChartTooltipContent } from &quot;@/components/ui/chart&quot; Add the components to your chart. Copy &lt; ChartContainer config = { chartConfig } className = &quot;h-[200px] w-full&quot; &gt;
 &lt; BarChart accessibilityLayer data = { chartData } &gt;
 &lt; CartesianGrid vertical = { false } /&gt;
 &lt; XAxis
 dataKey = &quot;month&quot;
 tickLine = { false }
 tickMargin = { 10 }
 axisLine = { false }
 tickFormatter = { ( value ) =&gt; value. slice ( 0 , 3 ) }
 /&gt;
 &lt; ChartTooltip content = { &lt; ChartTooltipContent /&gt; } /&gt;
 &lt; Bar dataKey = &quot;desktop&quot; fill = &quot;var(--color-desktop)&quot; radius = { 4 } /&gt;
 &lt; Bar dataKey = &quot;mobile&quot; fill = &quot;var(--color-mobile)&quot; radius = { 4 } /&gt;
 &lt;/ BarChart &gt;
 &lt;/ ChartContainer &gt; Copy "use client"

 import { Bar, BarChart, CartesianGrid, XAxis } from "recharts" View Code Hover to see the tooltips. Easy, right? Two components, and we&#x27;ve got a beautiful tooltip.
 Add Legend #
 We&#x27;ll do the same for the legend. We&#x27;ll use the ChartLegend and ChartLegendContent components from chart .
 Import the ChartLegend and ChartLegendContent components. Copy import { ChartLegend, ChartLegendContent } from &quot;@/components/ui/chart&quot; Add the components to your chart. Copy &lt; ChartContainer config = { chartConfig } className = &quot;h-[200px] w-full&quot; &gt;
 &lt; BarChart accessibilityLayer data = { chartData } &gt;
 &lt; CartesianGrid vertical = { false } /&gt;
 &lt; XAxis
 dataKey = &quot;month&quot;
 tickLine = { false }
 tickMargin = { 10 }
 axisLine = { false }
 tickFormatter = { ( value ) =&gt; value. slice ( 0 , 3 ) }
 /&gt;
 &lt; ChartTooltip content = { &lt; ChartTooltipContent /&gt; } /&gt;
 &lt; ChartLegend content = { &lt; ChartLegendContent /&gt; } /&gt;
 &lt; Bar dataKey = &quot;desktop&quot; fill = &quot;var(--color-desktop)&quot; radius = { 4 } /&gt;
 &lt; Bar dataKey = &quot;mobile&quot; fill = &quot;var(--color-mobile)&quot; radius = { 4 } /&gt;
 &lt;/ BarChart &gt;
 &lt;/ ChartContainer &gt; Copy "use client"

 import { Bar, BarChart, CartesianGrid, XAxis } from "recharts" View Code
 Done. You&#x27;ve built your first chart! What&#x27;s next?

 Themes and Colors
 Tooltip
 Legend

 Chart Config #
 The chart config is where you define the labels, icons and colors for a chart.
 It is intentionally decoupled from chart data.
 This allows you to share config and color tokens between charts. It can also work independently for cases where your data or color tokens live remotely or in a different format.
 Copy import { Monitor } from &quot;lucide-react&quot;

 import { type ChartConfig } from &quot;@/components/ui/chart&quot;

 const chartConfig = {
 desktop: {
 label: &quot;Desktop&quot; ,
 icon: Monitor,
 // A color like &#x27;hsl(220, 98%, 61%)&#x27; or &#x27;var(--color-name)&#x27;
 color: &quot;#2563eb&quot; ,
 // OR a theme object with &#x27;light&#x27; and &#x27;dark&#x27; keys
 theme: {
 light: &quot;#2563eb&quot; ,
 dark: &quot;#dc2626&quot; ,
 },
 },
 } satisfies ChartConfig
 Theming #
 Charts have built-in support for theming. You can use css variables (recommended) or color values in any color format, such as hex, hsl or oklch.
 CSS Variables #
 Define your colors in your css file app/globals.css Copy @layer base {
 :root {
 --chart-1 : oklch ( 0.646 0.222 41.116 );
 --chart-2 : oklch ( 0.6 0.118 184.704 );
 }

 .dark {
 --chart-1 : oklch ( 0.488 0.243 264.376 );
 --chart-2 : oklch ( 0.696 0.17 162.48 );
 }
 } Add the color to your chartConfig components/example-chart.tsx Copy const chartConfig = {
 desktop: {
 label: &quot;Desktop&quot; ,
 color: &quot;var(--chart-1)&quot; ,
 },
 mobile: {
 label: &quot;Mobile&quot; ,
 color: &quot;var(--chart-2)&quot; ,
 },
 } satisfies ChartConfig
 hex, hsl or oklch #
 You can also define your colors directly in the chart config. Use the color format you prefer.
 components/example-chart.tsx Copy const chartConfig = {
 desktop: {
 label: &quot;Desktop&quot; ,
 color: &quot;#2563eb&quot; ,
 },
 mobile: {
 label: &quot;Mobile&quot; ,
 color: &quot;hsl(220, 98%, 61%)&quot; ,
 },
 tablet: {
 label: &quot;Tablet&quot; ,
 color: &quot;oklch(0.5 0.2 240)&quot; ,
 },
 laptop: {
 label: &quot;Laptop&quot; ,
 color: &quot;var(--chart-2)&quot; ,
 },
 } satisfies ChartConfig
 Using Colors #
 To use the theme colors in your chart, reference the colors using the format var(--color-KEY) .
 Components #
 Copy &lt; Bar dataKey = &quot;desktop&quot; fill = &quot;var(--color-desktop)&quot; /&gt;
 Chart Data #
 components/example-chart.tsx Copy const chartData = [
 { browser: &quot;chrome&quot; , visitors: 275 , fill: &quot;var(--color-chrome)&quot; },
 { browser: &quot;safari&quot; , visitors: 200 , fill: &quot;var(--color-safari)&quot; },
 ]
 Tailwind #
 components/example-chart.tsx Copy &lt; LabelList className = &quot;fill-(--color-desktop)&quot; /&gt;
 Tooltip #
 A chart tooltip contains a label, name, indicator and value. You can use a combination of these to customize your tooltip.
 Label Page Views Desktop 186 Mobile 80 Name Chrome 1,286 Firefox 1,000 Page Views Desktop 12,486 Indicator Chrome 1,286
 You can turn on/off any of these using the hideLabel , hideIndicator props and customize the indicator style using the indicator prop.
 Use labelKey and nameKey to use a custom key for the tooltip label and name.
 Chart comes with the &lt;ChartTooltip&gt; and &lt;ChartTooltipContent&gt; components. You can use these two components to add custom tooltips to your chart.
 components/example-chart.tsx Copy import { ChartTooltip, ChartTooltipContent } from &quot;@/components/ui/chart&quot;
 components/example-chart.tsx Copy &lt; ChartTooltip content = { &lt; ChartTooltipContent /&gt; } /&gt;
 Props #
 Use the following props to customize the tooltip.
 Prop Type Description labelKey string The config or data key to use for the label. nameKey string The config or data key to use for the name. indicator dot line or dashed The indicator style for the tooltip. hideLabel boolean Whether to hide the label. hideIndicator boolean Whether to hide the indicator.
 Colors #
 Colors are automatically referenced from the chart config.
 Custom #
 To use a custom key for tooltip label and names, use the labelKey and nameKey props.
 Copy const chartData = [
 { browser : &quot;chrome&quot; , visitors: 187 , fill: &quot;var(--color-chrome)&quot; },
 { browser : &quot;safari&quot; , visitors: 200 , fill: &quot;var(--color-safari)&quot; },
 ]

 const chartConfig = {
 visitors: {
 label: &quot;Total Visitors&quot; ,
 },
 chrome: {
 label: &quot;Chrome&quot; ,
 color: &quot;var(--chart-1)&quot; ,
 },
 safari: {
 label: &quot;Safari&quot; ,
 color: &quot;var(--chart-2)&quot; ,
 },
 } satisfies ChartConfig
 components/example-chart.tsx Copy &lt; ChartTooltip
 content = { &lt; ChartTooltipContent labelKey = &quot;visitors&quot; nameKey = &quot;browser&quot; /&gt; }
 /&gt;
 This will use Total Visitors for label and Chrome and Safari for the tooltip names.
 Legend #
 You can use the custom &lt;ChartLegend&gt; and &lt;ChartLegendContent&gt; components to add a legend to your chart.
 components/example-chart.tsx Copy import { ChartLegend, ChartLegendContent } from &quot;@/components/ui/chart&quot;
 components/example-chart.tsx Copy &lt; ChartLegend content = { &lt; ChartLegendContent /&gt; } /&gt;
 Colors #
 Colors are automatically referenced from the chart config.
 Custom #
 To use a custom key for legend names, use the nameKey prop.
 Copy const chartData = [
 { browser : &quot;chrome&quot; , visitors: 187 , fill: &quot;var(--color-chrome)&quot; },
 { browser : &quot;safari&quot; , visitors: 200 , fill: &quot;var(--color-safari)&quot; },
 ]

 const chartConfig = {
 chrome: {
 label: &quot;Chrome&quot; ,
 color: &quot;var(--chart-1)&quot; ,
 },
 safari: {
 label: &quot;Safari&quot; ,
 color: &quot;var(--chart-2)&quot; ,
 },
 } satisfies ChartConfig
 components/example-chart.tsx Copy &lt; ChartLegend content = { &lt; ChartLegendContent nameKey = &quot;browser&quot; /&gt; } /&gt;
 This will use Chrome and Safari for the legend names.
 Accessibility #
 You can turn on the accessibilityLayer prop to add an accessible layer to your chart.
 This prop adds keyboard access and screen reader support to your charts.
 components/example-chart.tsx Copy &lt; LineChart accessibilityLayer /&gt;
 RTL #
 To enable RTL support in shadcn/ui, see the RTL configuration guide .
 Arabic (العربية) ▼ Toggle Copy "use client"

 import { Bar, BarChart, CartesianGrid, XAxis } from "recharts" View Code Carousel Checkbox On This Page Component Updating to Recharts v3 Installation Your First Chart Add a Grid Add an Axis Add Tooltip Add Legend Chart Config Theming CSS Variables hex, hsl or oklch Using Colors Components Chart Data Tailwind Tooltip Props Colors Custom Legend Colors Custom Accessibility RTL Deploy your shadcn/ui app on Vercel Trusted by OpenAI, Sonos, Adobe, and more. Vercel provides tools and infrastructure to deploy apps and features at scale. Deploy Now Deploy to Vercel Built by shadcn at Vercel . The source code is available on GitHub . Get Code
