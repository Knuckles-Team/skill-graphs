Manual Installation - shadcn/ui Toggle Menu Menu Home Docs Components Blocks Charts Directory Create Search documentation... Search... 117k Toggle theme New Sections Introduction Components Installation Theming CLI RTL Skills MCP Server Registry Forms Changelog Components Accordion Alert Alert Dialog Aspect Ratio Avatar Badge Breadcrumb Button Button Group Calendar Card Carousel Chart Checkbox Collapsible Combobox Command Context Menu Data Table Date Picker Dialog Direction Drawer Dropdown Menu Empty Field Hover Card Input Input Group Input OTP Item Kbd Label Menubar Native Select Navigation Menu Pagination Popover Progress Radio Group Resizable Scroll Area Select Separator Sheet Sidebar Skeleton Slider Sonner Spinner Switch Table Tabs Textarea Toast Toggle Toggle Group Tooltip Typography Get Started Installation components.json Package Imports Theming Dark Mode CLI Monorepo Skills JavaScript Figma llms.txt Legacy Docs Forms React Hook Form TanStack Form Formisch Registry Introduction Getting Started GitHub Registries Registry Directory Examples Namespaces Authentication MCP Server Open in v0 API Reference registry.json registry-item.json Manual Installation Copy Page Previous Next Add dependencies to your project manually. Add Tailwind CSS # Components are styled using Tailwind CSS. You need to install Tailwind CSS in your project. Follow the Tailwind CSS installation instructions to get started. Add dependencies # Add the following dependencies to your project: pnpm npm yarn bun pnpm add shadcn class-variance-authority clsx tailwind-merge lucide-react tw-animate-css Copy Configure import aliases # Choose one of the following alias setups. Option A: tsconfig.json paths # tsconfig.json Copy {
 &quot;compilerOptions&quot; : {
 &quot;baseUrl&quot; : &quot;.&quot; ,
 &quot;paths&quot; : {
 &quot;@/*&quot; : [ &quot;./*&quot; ]
 }
 }
 } Option B: package.json#imports # package.json Copy {
 &quot;imports&quot; : {
 &quot;#components/*&quot; : &quot;./src/components/*.tsx&quot; ,
 &quot;#lib/*&quot; : &quot;./src/lib/*.ts&quot; ,
 &quot;#hooks/*&quot; : &quot;./src/hooks/*.ts&quot;
 }
 } tsconfig.json Copy {
 &quot;compilerOptions&quot; : {
 &quot;moduleResolution&quot; : &quot;bundler&quot; ,
 &quot;resolvePackageJsonImports&quot; : true
 }
 } The @ alias is a preference. You can use other aliases if you want. If you
use package.json#imports , keep the matching alias roots in components.json .
See the package imports guide for
framework-specific setup. Configure styles # Add the following to your styles/globals.css file. You can learn more about using CSS variables for theming in the theming section . Expand src/styles/globals.css Copy @import &quot;tailwindcss&quot; ;
 @import &quot;tw-animate-css&quot; ;
 @import &quot;shadcn/tailwind.css&quot; ;

 @custom-variant dark (&amp;:is(.dark *));

 @theme inline {
 --color-background: var(--background);
 --color-foreground: var(--foreground);
 --color-card: var(--card);
 --color-card-foreground: var(--card-foreground);
 --color-popover: var(--popover);
 --color-popover-foreground: var(--popover-foreground);
 --color-primary: var(--primary);
 --color-primary-foreground: var(--primary-foreground);
 --color-secondary: var(--secondary);
 --color-secondary-foreground: var(--secondary-foreground);
 --color-muted: var(--muted);
 --color-muted-foreground: var(--muted-foreground);
 --color-accent: var(--accent);
 --color-accent-foreground: var(--accent-foreground);
 --color-destructive: var(--destructive);
 --color-destructive-foreground: var(--destructive-foreground);
 --color-border: var(--border);
 --color-input: var(--input);
 --color-ring: var(--ring);
 --color-chart-1: var(--chart-1);
 --color-chart-2: var(--chart-2);
 --color-chart-3: var(--chart-3);
 --color-chart-4: var(--chart-4);
 --color-chart-5: var(--chart-5);
 --radius-sm: calc(var(--radius) * 0 .6 );
 --radius-md: calc(var(--radius) * 0 .8 );
 --radius-lg: var(--radius);
 --radius-xl: calc(var(--radius) * 1 .4 );
 --radius-2xl: calc(var(--radius) * 1 .8 );
 --radius-3xl: calc(var(--radius) * 2 .2 );
 --radius-4xl: calc(var(--radius) * 2 .6 );
 --color-sidebar: var(--sidebar);
 --color-sidebar-foreground: var(--sidebar-foreground);
 --color-sidebar-primary: var(--sidebar-primary);
 --color-sidebar-primary-foreground: var(--sidebar-primary-foreground);
 --color-sidebar-accent: var(--sidebar-accent);
 --color-sidebar-accent-foreground: var(--sidebar-accent-foreground);
 --color-sidebar-border: var(--sidebar-border);
 --color-sidebar-ring: var(--sidebar-ring);
 }

 :root {
 --radius : 0.625 rem ;
 --background : oklch ( 1 0 0 );
 --foreground : oklch ( 0.145 0 0 );
 --card : oklch ( 1 0 0 );
 --card-foreground : oklch ( 0.145 0 0 );
 --popover : oklch ( 1 0 0 );
 --popover-foreground : oklch ( 0.145 0 0 );
 --primary : oklch ( 0.205 0 0 );
 --primary-foreground : oklch ( 0.985 0 0 );
 --secondary : oklch ( 0.97 0 0 );
 --secondary-foreground : oklch ( 0.205 0 0 );
 --muted : oklch ( 0.97 0 0 );
 --muted-foreground : oklch ( 0.556 0 0 );
 --accent : oklch ( 0.97 0 0 );
 --accent-foreground : oklch ( 0.205 0 0 );
 --destructive : oklch ( 0.577 0.245 27.325 );
 --border : oklch ( 0.922 0 0 );
 --input : oklch ( 0.922 0 0 );
 --ring : oklch ( 0.708 0 0 );
 --chart-1 : oklch ( 0.646 0.222 41.116 );
 --chart-2 : oklch ( 0.6 0.118 184.704 );
 --chart-3 : oklch ( 0.398 0.07 227.392 );
 --chart-4 : oklch ( 0.828 0.189 84.429 );
 --chart-5 : oklch ( 0.769 0.188 70.08 );
 --sidebar : oklch ( 0.985 0 0 );
 --sidebar-foreground : oklch ( 0.145 0 0 );
 --sidebar-primary : oklch ( 0.205 0 0 );
 --sidebar-primary-foreground : oklch ( 0.985 0 0 );
 --sidebar-accent : oklch ( 0.97 0 0 );
 --sidebar-accent-foreground : oklch ( 0.205 0 0 );
 --sidebar-border : oklch ( 0.922 0 0 );
 --sidebar-ring : oklch ( 0.708 0 0 );
 }

 .dark {
 --background : oklch ( 0.145 0 0 );
 --foreground : oklch ( 0.985 0 0 );
 --card : oklch ( 0.205 0 0 );
 --card-foreground : oklch ( 0.985 0 0 );
 --popover : oklch ( 0.205 0 0 );
 --popover-foreground : oklch ( 0.985 0 0 );
 --primary : oklch ( 0.922 0 0 );
 --primary-foreground : oklch ( 0.205 0 0 );
 --secondary : oklch ( 0.269 0 0 );
 --secondary-foreground : oklch ( 0.985 0 0 );
 --muted : oklch ( 0.269 0 0 );
 --muted-foreground : oklch ( 0.708 0 0 );
 --accent : oklch ( 0.269 0 0 );
 --accent-foreground : oklch ( 0.985 0 0 );
 --destructive : oklch ( 0.704 0.191 22.216 );
 --border : oklch ( 1 0 0 / 10 % );
 --input : oklch ( 1 0 0 / 15 % );
 --ring : oklch ( 0.556 0 0 );
 --chart-1 : oklch ( 0.488 0.243 264.376 );
 --chart-2 : oklch ( 0.696 0.17 162.48 );
 --chart-3 : oklch ( 0.769 0.188 70.08 );
 --chart-4 : oklch ( 0.627 0.265 303.9 );
 --chart-5 : oklch ( 0.645 0.246 16.439 );
 --sidebar : oklch ( 0.205 0 0 );
 --sidebar-foreground : oklch ( 0.985 0 0 );
 --sidebar-primary : oklch ( 0.488 0.243 264.376 );
 --sidebar-primary-foreground : oklch ( 0.985 0 0 );
 --sidebar-accent : oklch ( 0.269 0 0 );
 --sidebar-accent-foreground : oklch ( 0.985 0 0 );
 --sidebar-border : oklch ( 1 0 0 / 10 % );
 --sidebar-ring : oklch ( 0.556 0 0 );
 }

 @layer base {
 * {
 @ apply border-border outline-ring /50;
 }
 body {
 @ apply bg-background text-foreground ;
 }
 } Expand Add a cn helper # lib/utils.ts Copy import { clsx, type ClassValue } from &quot;clsx&quot;
 import { twMerge } from &quot;tailwind-merge&quot;

 export function cn ( ... inputs : ClassValue []) {
 return twMerge ( clsx (inputs))
 } Create a components.json file # Create a components.json file in the root of your project. components.json Copy {
 &quot;$schema&quot; : &quot;https://ui.shadcn.com/schema.json&quot; ,
 &quot;style&quot; : &quot;radix-nova&quot; ,
 &quot;rsc&quot; : false ,
 &quot;tsx&quot; : true ,
 &quot;tailwind&quot; : {
 &quot;config&quot; : &quot;&quot; ,
 &quot;css&quot; : &quot;src/styles/globals.css&quot; ,
 &quot;baseColor&quot; : &quot;neutral&quot; ,
 &quot;cssVariables&quot; : true ,
 &quot;prefix&quot; : &quot;&quot;
 },
 &quot;aliases&quot; : {
 &quot;components&quot; : &quot;@/components&quot; ,
 &quot;utils&quot; : &quot;@/lib/utils&quot; ,
 &quot;ui&quot; : &quot;@/components/ui&quot; ,
 &quot;lib&quot; : &quot;@/lib&quot; ,
 &quot;hooks&quot; : &quot;@/hooks&quot;
 },
 &quot;iconLibrary&quot; : &quot;lucide&quot;
 } If you&#x27;re using package.json#imports , use the corresponding #... aliases instead: components.json Copy {
 &quot;aliases&quot; : {
 &quot;components&quot; : &quot;#components&quot; ,
 &quot;utils&quot; : &quot;#lib/utils&quot; ,
 &quot;ui&quot; : &quot;#components/ui&quot; ,
 &quot;lib&quot; : &quot;#lib&quot; ,
 &quot;hooks&quot; : &quot;#hooks&quot;
 }
 } That&#x27;s it # You can now start adding components to your project. TanStack Router Dark Mode On This Page Add Tailwind CSS Add dependencies Configure import aliases Option A: tsconfig.json paths Option B: package.json#imports Configure styles Add a cn helper Create a components.json file That&#x27;s it Deploy your shadcn/ui app on Vercel Trusted by OpenAI, Sonos, Adobe, and more. Vercel provides tools and infrastructure to deploy apps and features at scale. Deploy Now Deploy to Vercel Built by shadcn at Vercel . The source code is available on GitHub . Get Code
