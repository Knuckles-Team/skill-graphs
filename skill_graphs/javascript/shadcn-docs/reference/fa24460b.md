Next.js - shadcn/ui Toggle Menu Menu Home Docs Components Blocks Charts Directory Create Search documentation... Search... 117k Toggle theme New Sections Introduction Components Installation Theming CLI RTL Skills MCP Server Registry Forms Changelog Components Accordion Alert Alert Dialog Aspect Ratio Avatar Badge Breadcrumb Button Button Group Calendar Card Carousel Chart Checkbox Collapsible Combobox Command Context Menu Data Table Date Picker Dialog Direction Drawer Dropdown Menu Empty Field Hover Card Input Input Group Input OTP Item Kbd Label Menubar Native Select Navigation Menu Pagination Popover Progress Radio Group Resizable Scroll Area Select Separator Sheet Sidebar Skeleton Slider Sonner Spinner Switch Table Tabs Textarea Toast Toggle Toggle Group Tooltip Typography Get Started Installation components.json Package Imports Theming Dark Mode CLI Monorepo Skills JavaScript Figma llms.txt Legacy Docs Forms React Hook Form TanStack Form Formisch Registry Introduction Getting Started GitHub Registries Registry Directory Examples Namespaces Authentication MCP Server Open in v0 API Reference registry.json registry-item.json Next.js Copy Page Previous Next Adding dark mode to your Next.js app. Install next-themes # Start by installing next-themes : pnpm npm yarn bun pnpm add next-themes Copy Create a theme provider # components/theme-provider.tsx Copy &quot;use client&quot;

 import * as React from &quot;react&quot;
 import { ThemeProvider as NextThemesProvider } from &quot;next-themes&quot;

 export function ThemeProvider ({
 children ,
 ... props
 } : React . ComponentProps &lt; typeof NextThemesProvider&gt;) {
 return &lt; NextThemesProvider { ... props } &gt; { children } &lt;/ NextThemesProvider &gt;
 } Wrap your root layout # Add the ThemeProvider to your root layout and add the suppressHydrationWarning prop to the html tag. app/layout.tsx Copy import { ThemeProvider } from &quot;@/components/theme-provider&quot;

 export default function RootLayout ({ children } : RootLayoutProps ) {
 return (
 &lt;&gt;
 &lt; html lang = &quot;en&quot; suppressHydrationWarning &gt;
 &lt; head /&gt;
 &lt; body &gt;
 &lt; ThemeProvider
 attribute = &quot;class&quot;
 defaultTheme = &quot;system&quot;
 enableSystem
 disableTransitionOnChange
 &gt;
 { children }
 &lt;/ ThemeProvider &gt;
 &lt;/ body &gt;
 &lt;/ html &gt;
 &lt;/&gt;
 )
 } Add a mode toggle # Place a mode toggle on your site to toggle between light and dark mode. Toggle theme Copy "use client"

 import * as React from "react" View Code Dark Mode Vite On This Page Install next-themes Create a theme provider Wrap your root layout Add a mode toggle Deploy your shadcn/ui app on Vercel Trusted by OpenAI, Sonos, Adobe, and more. Vercel provides tools and infrastructure to deploy apps and features at scale. Deploy Now Deploy to Vercel Built by shadcn at Vercel . The source code is available on GitHub . Get Code
