Vite - shadcn/ui Toggle Menu Menu Home Docs Components Blocks Charts Directory Create Search documentation... Search... 117k Toggle theme New Sections Introduction Components Installation Theming CLI RTL Skills MCP Server Registry Forms Changelog Components Accordion Alert Alert Dialog Aspect Ratio Avatar Badge Breadcrumb Button Button Group Calendar Card Carousel Chart Checkbox Collapsible Combobox Command Context Menu Data Table Date Picker Dialog Direction Drawer Dropdown Menu Empty Field Hover Card Input Input Group Input OTP Item Kbd Label Menubar Native Select Navigation Menu Pagination Popover Progress Radio Group Resizable Scroll Area Select Separator Sheet Sidebar Skeleton Slider Sonner Spinner Switch Table Tabs Textarea Toast Toggle Toggle Group Tooltip Typography Get Started Installation components.json Package Imports Theming Dark Mode CLI Monorepo Skills JavaScript Figma llms.txt Legacy Docs Forms React Hook Form TanStack Form Formisch Registry Introduction Getting Started GitHub Registries Registry Directory Examples Namespaces Authentication MCP Server Open in v0 API Reference registry.json registry-item.json Vite Copy Page Previous Next Adding dark mode to your Vite app. Create a theme provider #
 components/theme-provider.tsx Copy import { createContext, useContext, useEffect, useState } from &quot;react&quot;

 type Theme = &quot;dark&quot; | &quot;light&quot; | &quot;system&quot;

 type ThemeProviderProps = {
 children : React . ReactNode
 defaultTheme ?: Theme
 storageKey ?: string
 }

 type ThemeProviderState = {
 theme : Theme
 setTheme : ( theme : Theme ) =&gt; void
 }

 const initialState : ThemeProviderState = {
 theme: &quot;system&quot; ,
 setTheme : () =&gt; null ,
 }

 const ThemeProviderContext = createContext &lt; ThemeProviderState &gt;(initialState)

 export function ThemeProvider ({
 children ,
 defaultTheme = &quot;system&quot; ,
 storageKey = &quot;vite-ui-theme&quot; ,
 ... props
 } : ThemeProviderProps ) {
 const [ theme , setTheme ] = useState &lt; Theme &gt;(
 () =&gt; (localStorage. getItem (storageKey) as Theme ) || defaultTheme
 )

 useEffect (() =&gt; {
 const root = window.document.documentElement

 root.classList. remove ( &quot;light&quot; , &quot;dark&quot; )

 if (theme === &quot;system&quot; ) {
 const systemTheme = window. matchMedia ( &quot;(prefers-color-scheme: dark)&quot; )
 .matches
 ? &quot;dark&quot;
 : &quot;light&quot;

 root.classList. add (systemTheme)
 return
 }

 root.classList. add (theme)
 }, [theme])

 const value = {
 theme,
 setTheme : ( theme : Theme ) =&gt; {
 localStorage. setItem (storageKey, theme)
 setTheme (theme)
 },
 }

 return (
 &lt; ThemeProviderContext.Provider { ... props } value = { value } &gt;
 { children }
 &lt;/ ThemeProviderContext.Provider &gt;
 )
 }

 export const useTheme = () =&gt; {
 const context = useContext (ThemeProviderContext)

 if (context === undefined )
 throw new Error ( &quot;useTheme must be used within a ThemeProvider&quot; )

 return context
 }
 Wrap your root layout #
 Add the ThemeProvider to your root layout.
 App.tsx Copy import { ThemeProvider } from &quot;@/components/theme-provider&quot;

 function App () {
 return (
 &lt; ThemeProvider defaultTheme = &quot;dark&quot; storageKey = &quot;vite-ui-theme&quot; &gt;
 { children }
 &lt;/ ThemeProvider &gt;
 )
 }

 export default App
 Add a mode toggle #
 Place a mode toggle on your site to toggle between light and dark mode.
 components/mode-toggle.tsx Copy import { Moon, Sun } from &quot;lucide-react&quot;

 import { Button } from &quot;@/components/ui/button&quot;
 import {
 DropdownMenu,
 DropdownMenuContent,
 DropdownMenuItem,
 DropdownMenuTrigger,
 } from &quot;@/components/ui/dropdown-menu&quot;
 import { useTheme } from &quot;@/components/theme-provider&quot;

 export function ModeToggle () {
 const { setTheme } = useTheme ()

 return (
 &lt; DropdownMenu &gt;
 &lt; DropdownMenuTrigger asChild &gt;
 &lt; Button variant = &quot;outline&quot; size = &quot;icon&quot; &gt;
 &lt; Sun className = &quot;h-[1.2rem] w-[1.2rem] scale-100 rotate-0 transition-all dark:scale-0 dark:-rotate-90&quot; /&gt;
 &lt; Moon className = &quot;absolute h-[1.2rem] w-[1.2rem] scale-0 rotate-90 transition-all dark:scale-100 dark:rotate-0&quot; /&gt;
 &lt; span className = &quot;sr-only&quot; &gt;Toggle theme&lt;/ span &gt;
 &lt;/ Button &gt;
 &lt;/ DropdownMenuTrigger &gt;
 &lt; DropdownMenuContent align = &quot;end&quot; &gt;
 &lt; DropdownMenuItem onClick = { () =&gt; setTheme ( &quot;light&quot; ) } &gt;
 Light
 &lt;/ DropdownMenuItem &gt;
 &lt; DropdownMenuItem onClick = { () =&gt; setTheme ( &quot;dark&quot; ) } &gt;
 Dark
 &lt;/ DropdownMenuItem &gt;
 &lt; DropdownMenuItem onClick = { () =&gt; setTheme ( &quot;system&quot; ) } &gt;
 System
 &lt;/ DropdownMenuItem &gt;
 &lt;/ DropdownMenuContent &gt;
 &lt;/ DropdownMenu &gt;
 )
 } Next.js Astro On This Page Create a theme provider Wrap your root layout Add a mode toggle Deploy your shadcn/ui app on Vercel Trusted by OpenAI, Sonos, Adobe, and more. Vercel provides tools and infrastructure to deploy apps and features at scale. Deploy Now Deploy to Vercel Built by shadcn at Vercel . The source code is available on GitHub . Get Code
