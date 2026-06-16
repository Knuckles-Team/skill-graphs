Remix - shadcn/ui Toggle Menu Menu Home Docs Components Blocks Charts Directory Create Search documentation... Search... 117k Toggle theme New Sections Introduction Components Installation Theming CLI RTL Skills MCP Server Registry Forms Changelog Components Accordion Alert Alert Dialog Aspect Ratio Avatar Badge Breadcrumb Button Button Group Calendar Card Carousel Chart Checkbox Collapsible Combobox Command Context Menu Data Table Date Picker Dialog Direction Drawer Dropdown Menu Empty Field Hover Card Input Input Group Input OTP Item Kbd Label Menubar Native Select Navigation Menu Pagination Popover Progress Radio Group Resizable Scroll Area Select Separator Sheet Sidebar Skeleton Slider Sonner Spinner Switch Table Tabs Textarea Toast Toggle Toggle Group Tooltip Typography Get Started Installation components.json Package Imports Theming Dark Mode CLI Monorepo Skills JavaScript Figma llms.txt Legacy Docs Forms React Hook Form TanStack Form Formisch Registry Introduction Getting Started GitHub Registries Registry Directory Examples Namespaces Authentication MCP Server Open in v0 API Reference registry.json registry-item.json Remix Copy Page Previous Next Adding dark mode to your Remix app. Modify your tailwind.css file # Add :root[class~=&quot;dark&quot;] to your tailwind.css file. This will allow you to use the dark class on your html element to apply dark mode styles. app/tailwind.css Copy .dark ,
 :root [ class ~= &quot;dark&quot; ] {
 ...;
 } Install remix-themes # Start by installing remix-themes : pnpm npm yarn bun pnpm add remix-themes Copy Create a session storage and theme session resolver # app/sessions.server.tsx Copy import { createThemeSessionResolver } from &quot;remix-themes&quot;

 // You can default to &#x27;development&#x27; if process.env.NODE_ENV is not set
 const isProduction = process.env. NODE_ENV === &quot;production&quot;

 const sessionStorage = createCookieSessionStorage ({
 cookie: {
 name: &quot;theme&quot; ,
 path: &quot;/&quot; ,
 httpOnly: true ,
 sameSite: &quot;lax&quot; ,
 secrets: [ &quot;s3cr3t&quot; ],
 // Set domain and secure only if in production
 ... (isProduction
 ? { domain: &quot;your-production-domain.com&quot; , secure: true }
 : {}),
 },
 })

 export const themeSessionResolver = createThemeSessionResolver (sessionStorage) Set up Remix Themes # Add the ThemeProvider to your root layout. app/root.tsx Copy import clsx from &quot;clsx&quot;
 import { PreventFlashOnWrongTheme, ThemeProvider, useTheme } from &quot;remix-themes&quot;

 import { themeSessionResolver } from &quot;./sessions.server&quot;

 // Return the theme from the session storage using the loader
 export async function loader ({ request } : LoaderFunctionArgs ) {
 const { getTheme } = await themeSessionResolver (request)
 return {
 theme: getTheme (),
 }
 }
 // Wrap your app with ThemeProvider.
 // `specifiedTheme` is the stored theme in the session storage.
 // `themeAction` is the action name that&#x27;s used to change the theme in the session storage.
 export default function AppWithProviders () {
 const data = useLoaderData &lt; typeof loader&gt;()
 return (
 &lt; ThemeProvider specifiedTheme = { data.theme } themeAction = &quot;/action/set-theme&quot; &gt;
 &lt; App /&gt;
 &lt;/ ThemeProvider &gt;
 )
 }

 export function App () {
 const data = useLoaderData &lt; typeof loader&gt;()
 const [ theme ] = useTheme ()
 return (
 &lt; html lang = &quot;en&quot; className = { clsx (theme) } &gt;
 &lt; head &gt;
 &lt; meta charSet = &quot;utf-8&quot; /&gt;
 &lt; meta name = &quot;viewport&quot; content = &quot;width=device-width, initial-scale=1&quot; /&gt;
 &lt; Meta /&gt;
 &lt; PreventFlashOnWrongTheme ssrTheme = { Boolean (data.theme) } /&gt;
 &lt; Links /&gt;
 &lt;/ head &gt;
 &lt; body &gt;
 &lt; Outlet /&gt;
 &lt; ScrollRestoration /&gt;
 &lt; Scripts /&gt;
 &lt; LiveReload /&gt;
 &lt;/ body &gt;
 &lt;/ html &gt;
 )
 } Add an action route # Create a file in /routes/action.set-theme.ts . Ensure that you pass the filename to the ThemeProvider component. This route is used to store the preferred theme in the session storage when the user changes it. app/routes/action.set-theme.ts Copy import { createThemeAction } from &quot;remix-themes&quot;

 import { themeSessionResolver } from &quot;./sessions.server&quot;

 export const action = createThemeAction (themeSessionResolver) Add a mode toggle # Place a mode toggle on your site to toggle between light and dark mode. components/mode-toggle.tsx Copy import { Moon, Sun } from &quot;lucide-react&quot;
 import { Theme, useTheme } from &quot;remix-themes&quot;

 import { Button } from &quot;./ui/button&quot;
 import {
 DropdownMenu,
 DropdownMenuContent,
 DropdownMenuItem,
 DropdownMenuTrigger,
 } from &quot;./ui/dropdown-menu&quot;

 export function ModeToggle () {
 const [, setTheme ] = useTheme ()

 return (
 &lt; DropdownMenu &gt;
 &lt; DropdownMenuTrigger asChild &gt;
 &lt; Button variant = &quot;ghost&quot; size = &quot;icon&quot; &gt;
 &lt; Sun className = &quot;h-[1.2rem] w-[1.2rem] scale-100 rotate-0 transition-all dark:scale-0 dark:-rotate-90&quot; /&gt;
 &lt; Moon className = &quot;absolute h-[1.2rem] w-[1.2rem] scale-0 rotate-90 transition-all dark:scale-100 dark:rotate-0&quot; /&gt;
 &lt; span className = &quot;sr-only&quot; &gt;Toggle theme&lt;/ span &gt;
 &lt;/ Button &gt;
 &lt;/ DropdownMenuTrigger &gt;
 &lt; DropdownMenuContent align = &quot;end&quot; &gt;
 &lt; DropdownMenuItem onClick = { () =&gt; setTheme (Theme. LIGHT ) } &gt;
 Light
 &lt;/ DropdownMenuItem &gt;
 &lt; DropdownMenuItem onClick = { () =&gt; setTheme (Theme. DARK ) } &gt;
 Dark
 &lt;/ DropdownMenuItem &gt;
 &lt;/ DropdownMenuContent &gt;
 &lt;/ DropdownMenu &gt;
 )
 } Astro TanStack Start On This Page Modify your tailwind.css file Install remix-themes Create a session storage and theme session resolver Set up Remix Themes Add an action route Add a mode toggle Deploy your shadcn/ui app on Vercel Trusted by OpenAI, Sonos, Adobe, and more. Vercel provides tools and infrastructure to deploy apps and features at scale. Deploy Now Deploy to Vercel Built by shadcn at Vercel . The source code is available on GitHub . Get Code
