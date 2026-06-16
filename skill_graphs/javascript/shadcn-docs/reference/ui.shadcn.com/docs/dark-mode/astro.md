Astro - shadcn/ui Toggle Menu Menu Home Docs Components Blocks Charts Directory Create Search documentation... Search... 117k Toggle theme New Sections Introduction Components Installation Theming CLI RTL Skills MCP Server Registry Forms Changelog Components Accordion Alert Alert Dialog Aspect Ratio Avatar Badge Breadcrumb Button Button Group Calendar Card Carousel Chart Checkbox Collapsible Combobox Command Context Menu Data Table Date Picker Dialog Direction Drawer Dropdown Menu Empty Field Hover Card Input Input Group Input OTP Item Kbd Label Menubar Native Select Navigation Menu Pagination Popover Progress Radio Group Resizable Scroll Area Select Separator Sheet Sidebar Skeleton Slider Sonner Spinner Switch Table Tabs Textarea Toast Toggle Toggle Group Tooltip Typography Get Started Installation components.json Package Imports Theming Dark Mode CLI Monorepo Skills JavaScript Figma llms.txt Legacy Docs Forms React Hook Form TanStack Form Formisch Registry Introduction Getting Started GitHub Registries Registry Directory Examples Namespaces Authentication MCP Server Open in v0 API Reference registry.json registry-item.json Astro Copy Page Previous Next Adding dark mode to your astro app. Create an inline theme script #
 src/pages/index.astro Copy ---
 import &#x27;../styles/globals.css&#x27;
 ---

 &lt; script is:inline &gt;
 const getThemePreference = () =&gt; {
 if ( typeof localStorage !== &#x27;undefined&#x27; &amp;&amp; localStorage. getItem ( &#x27;theme&#x27; )) {
 return localStorage. getItem ( &#x27;theme&#x27; );
 }
 return window. matchMedia ( &#x27;(prefers-color-scheme: dark)&#x27; ).matches ? &#x27;dark&#x27; : &#x27;light&#x27; ;
 };
 const isDark = getThemePreference () === &#x27;dark&#x27; ;
 document.documentElement.classList[isDark ? &#x27;add&#x27; : &#x27;remove&#x27; ]( &#x27;dark&#x27; );

 if ( typeof localStorage !== &#x27;undefined&#x27; ) {
 const observer = new MutationObserver (() =&gt; {
 const isDark = document.documentElement.classList. contains ( &#x27;dark&#x27; );
 localStorage. setItem ( &#x27;theme&#x27; , isDark ? &#x27;dark&#x27; : &#x27;light&#x27; );
 });
 observer. observe (document.documentElement, { attributes: true , attributeFilter: [ &#x27;class&#x27; ] });
 }
 &lt;/ script &gt;

 &lt; html lang = &quot;en&quot; &gt;
 &lt; body &gt;
 &lt; h1 &gt;Astro&lt;/ h1 &gt;
 &lt;/ body &gt;
 &lt;/ html &gt;
 Add a mode toggle #
 src/components/ModeToggle.tsx Copy import * as React from &quot;react&quot;
 import { Moon, Sun } from &quot;lucide-react&quot;

 import { Button } from &quot;@/components/ui/button&quot;
 import {
 DropdownMenu,
 DropdownMenuContent,
 DropdownMenuItem,
 DropdownMenuTrigger,
 } from &quot;@/components/ui/dropdown-menu&quot;

 export function ModeToggle () {
 const [ theme , setThemeState ] = React.useState &lt;
 &quot;theme-light&quot; | &quot;dark&quot; | &quot;system&quot;
 &gt; ( &quot;theme-light&quot; )

 React. useEffect (() =&gt; {
 const isDarkMode = document.documentElement.classList. contains ( &quot;dark&quot; )
 setThemeState (isDarkMode ? &quot;dark&quot; : &quot;theme-light&quot; )
 }, [])

 React. useEffect (() =&gt; {
 const isDark =
 theme === &quot;dark&quot; ||
 (theme === &quot;system&quot; &amp;&amp;
 window. matchMedia ( &quot;(prefers-color-scheme: dark)&quot; ).matches)
 document.documentElement.classList[isDark ? &quot;add&quot; : &quot;remove&quot; ]( &quot;dark&quot; )
 }, [theme])

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
 &lt; DropdownMenuItem onClick = { () =&gt; setThemeState ( &quot;theme-light&quot; ) } &gt;
 Light
 &lt;/ DropdownMenuItem &gt;
 &lt; DropdownMenuItem onClick = { () =&gt; setThemeState ( &quot;dark&quot; ) } &gt;
 Dark
 &lt;/ DropdownMenuItem &gt;
 &lt; DropdownMenuItem onClick = { () =&gt; setThemeState ( &quot;system&quot; ) } &gt;
 System
 &lt;/ DropdownMenuItem &gt;
 &lt;/ DropdownMenuContent &gt;
 &lt;/ DropdownMenu &gt;
 )
 }
 Display the mode toggle #
 Place a mode toggle on your site to toggle between light and dark mode.
 src/pages/index.astro Copy ---
 import &#x27;../styles/globals.css&#x27;
 import { ModeToggle } from &#x27;@/components/ModeToggle&#x27; ;
 ---

 &lt;!-- Inline script --&gt;

 &lt; html lang = &quot;en&quot; &gt;
 &lt; body &gt;
 &lt; h1 &gt;Astro&lt;/ h1 &gt;
 &lt; ModeToggle client:load /&gt;
 &lt;/ body &gt;
 &lt;/ html &gt; Vite Remix On This Page Create an inline theme script Add a mode toggle Display the mode toggle Deploy your shadcn/ui app on Vercel Trusted by OpenAI, Sonos, Adobe, and more. Vercel provides tools and infrastructure to deploy apps and features at scale. Deploy Now Deploy to Vercel Built by shadcn at Vercel . The source code is available on GitHub . Get Code
