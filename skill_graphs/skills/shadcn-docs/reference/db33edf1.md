JavaScript - shadcn/ui Toggle Menu Menu Home Docs Components Blocks Charts Directory Create Search documentation... Search... 117k Toggle theme New Sections Introduction Components Installation Theming CLI RTL Skills MCP Server Registry Forms Changelog Components Accordion Alert Alert Dialog Aspect Ratio Avatar Badge Breadcrumb Button Button Group Calendar Card Carousel Chart Checkbox Collapsible Combobox Command Context Menu Data Table Date Picker Dialog Direction Drawer Dropdown Menu Empty Field Hover Card Input Input Group Input OTP Item Kbd Label Menubar Native Select Navigation Menu Pagination Popover Progress Radio Group Resizable Scroll Area Select Separator Sheet Sidebar Skeleton Slider Sonner Spinner Switch Table Tabs Textarea Toast Toggle Toggle Group Tooltip Typography Get Started Installation components.json Package Imports Theming Dark Mode CLI Monorepo Skills JavaScript Figma llms.txt Legacy Docs Forms React Hook Form TanStack Form Formisch Registry Introduction Getting Started GitHub Registries Registry Directory Examples Namespaces Authentication MCP Server Open in v0 API Reference registry.json registry-item.json JavaScript Copy Page Previous Next How to use shadcn/ui with JavaScript This project and the components are written in TypeScript. We recommend using TypeScript for your project as well.
 However we provide a JavaScript version of the components as well. The JavaScript version is available via the cli .
 To opt-out of TypeScript, you can use the tsx flag in your components.json file.
 components.json Copy {
 &quot;style&quot; : &quot;new-york&quot; ,
 &quot;rsc&quot; : false ,
 &quot;tsx&quot; : false ,
 &quot;tailwind&quot; : {
 &quot;config&quot; : &quot;&quot; ,
 &quot;css&quot; : &quot;src/app/globals.css&quot; ,
 &quot;baseColor&quot; : &quot;zinc&quot; ,
 &quot;cssVariables&quot; : true
 },
 &quot;iconLibrary&quot; : &quot;lucide&quot; ,
 &quot;aliases&quot; : {
 &quot;components&quot; : &quot;@/components&quot; ,
 &quot;utils&quot; : &quot;@/lib/utils&quot; ,
 &quot;ui&quot; : &quot;@/components/ui&quot; ,
 &quot;lib&quot; : &quot;@/lib&quot; ,
 &quot;hooks&quot; : &quot;@/hooks&quot;
 }
 }
 To configure import aliases, you can use the following jsconfig.json :
 jsconfig.json Copy {
 &quot;compilerOptions&quot; : {
 &quot;paths&quot; : {
 &quot;@/*&quot; : [ &quot;./*&quot; ]
 }
 }
 } Skills Figma Deploy your shadcn/ui app on Vercel Trusted by OpenAI, Sonos, Adobe, and more. Vercel provides tools and infrastructure to deploy apps and features at scale. Deploy Now Deploy to Vercel Built by shadcn at Vercel . The source code is available on GitHub . Get Code
