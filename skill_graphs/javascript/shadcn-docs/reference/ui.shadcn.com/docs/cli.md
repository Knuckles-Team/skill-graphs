shadcn - shadcn/ui Toggle Menu Menu Home Docs Components Blocks Charts Directory Create Search documentation... Search... 117k Toggle theme New Sections Introduction Components Installation Theming CLI RTL Skills MCP Server Registry Forms Changelog Components Accordion Alert Alert Dialog Aspect Ratio Avatar Badge Breadcrumb Button Button Group Calendar Card Carousel Chart Checkbox Collapsible Combobox Command Context Menu Data Table Date Picker Dialog Direction Drawer Dropdown Menu Empty Field Hover Card Input Input Group Input OTP Item Kbd Label Menubar Native Select Navigation Menu Pagination Popover Progress Radio Group Resizable Scroll Area Select Separator Sheet Sidebar Skeleton Slider Sonner Spinner Switch Table Tabs Textarea Toast Toggle Toggle Group Tooltip Typography Get Started Installation components.json Package Imports Theming Dark Mode CLI Monorepo Skills JavaScript Figma llms.txt Legacy Docs Forms React Hook Form TanStack Form Formisch Registry Introduction Getting Started GitHub Registries Registry Directory Examples Namespaces Authentication MCP Server Open in v0 API Reference registry.json registry-item.json shadcn Copy Page Previous Next Use the shadcn CLI to add components to your project. init #
 Use the init command to initialize configuration and dependencies for an existing project, or create a new project with --name .
 The init command installs dependencies, adds the cn util and configures CSS variables for the project.
 pnpm npm yarn bun pnpm dlx shadcn@latest init Copy
 Options
 Copy Usage: shadcn init [options] [components...]

 initialize your project and install dependencies

 Arguments:
 components names, url or local path to component

 Options:
 -t, --template &lt; templat e &gt; the template to use. (next, vite, start, react-router, laravel, astro )
 -b, --base &lt; bas e &gt; the component library to use. (radix, base )
 -p, --preset [name] use a preset configuration
 -y, --yes skip confirmation prompt. (default: true )
 -d, --defaults use default configuration: --template=next --preset=nova (default: false )
 -f, --force force overwrite of existing configuration. (default: false )
 -c, --cwd &lt; cw d &gt; the working directory. defaults to the current directory.
 -n, --name &lt; nam e &gt; the name for the new project.
 -s, --silent mute output. (default: false )
 --css-variables use css variables for theming. (default: true )
 --no-css-variables do not use css variables for theming.
 --monorepo scaffold a monorepo project.
 --no-monorepo skip the monorepo prompt.
 --rtl enable RTL support.
 --no-rtl disable RTL support.
 --pointer enable pointer cursor for buttons.
 --no-pointer disable pointer cursor for buttons.
 --reinstall re-install existing UI components.
 --no-reinstall do not re-install existing UI components.
 -h, --help display help for command
 The create command is an alias for init :
 pnpm npm yarn bun pnpm dlx shadcn@latest create Copy

 add #
 Use the add command to add components and dependencies to your project.
 pnpm npm yarn bun pnpm dlx shadcn@latest add [component] Copy
 Options
 Copy Usage: shadcn add [options] [components...]

 add a component to your project

 Arguments:
 components name, url or local path to component

 Options:
 -y, --yes skip confirmation prompt. (default: false )
 -o, --overwrite overwrite existing files. (default: false )
 -c, --cwd &lt; cw d &gt; the working directory. defaults to the current directory.
 -a, --all add all available components (default: false )
 -p, --path &lt; pat h &gt; the path to add the component to.
 -s, --silent mute output. (default: false )
 --dry-run preview changes without writing files. (default: false )
 --diff [path] show diff for a file.
 --view [path] show file contents.
 -h, --help display help for command

 apply #
 Use the apply command to apply a preset to an existing project.
 pnpm npm yarn bun pnpm dlx shadcn@latest apply a2r6bw Copy
 You can apply only the theme or fonts from a preset without reinstalling UI components:
 pnpm npm yarn bun pnpm dlx shadcn@latest apply a2r6bw --only theme Copy
 Supported values for --only are theme and font .
 Options
 Copy Usage: shadcn apply [options] [preset]

 apply a preset to an existing project

 Arguments:
 preset the preset to apply

 Options:
 --preset &lt; prese t &gt; preset configuration to apply
 --only [parts] apply only parts of a preset: theme, font
 -y, --yes skip confirmation prompt. (default: false )
 -c, --cwd &lt; cw d &gt; the working directory. defaults to the current directory.
 -s, --silent mute output. (default: false )
 -h, --help display help for command

 preset #
 Use the preset command to inspect preset codes and resolve the preset for an existing project.
 pnpm npm yarn bun pnpm dlx shadcn@latest preset decode a2r6bw Copy
 preset decode #
 Use preset decode to decode a preset code.
 pnpm npm yarn bun pnpm dlx shadcn@latest preset decode a2r6bw Copy
 Options
 Copy Usage: shadcn preset decode [options] &lt; code &gt;

 decode a preset code

 Arguments:
 code the preset code to decode

 Options:
 --json output as JSON. (default: false )
 -h, --help display help for command
 preset resolve #
 Use preset resolve to resolve the preset from the current project.
 pnpm npm yarn bun pnpm dlx shadcn@latest preset resolve Copy
 The preset info command is an alias for preset resolve :
 pnpm npm yarn bun pnpm dlx shadcn@latest preset info Copy
 Options
 Copy Usage: shadcn preset resolve | info [options]

 resolve a preset from your project

 Options:
 -c, --cwd &lt; cw d &gt; the working directory. defaults to the current directory.
 --json output as JSON. (default: false )
 -h, --help display help for command
 preset url #
 Use preset url to print the create URL for a preset code.
 pnpm npm yarn bun pnpm dlx shadcn@latest preset url a2r6bw Copy
 Options
 Copy Usage: shadcn preset url [options] &lt; code &gt;

 get the create URL for a preset code

 Arguments:
 code the preset code

 Options:
 -h, --help display help for command
 preset open #
 Use preset open to open a preset code in the browser.
 pnpm npm yarn bun pnpm dlx shadcn@latest preset open a2r6bw Copy
 Options
 Copy Usage: shadcn preset open [options] &lt; code &gt;

 open a preset code in the browser

 Arguments:
 code the preset code

 Options:
 -h, --help display help for command

 view #
 Use the view command to view items from the registry before installing them.
 pnpm npm yarn bun pnpm dlx shadcn@latest view [item] Copy
 You can view multiple items at once:
 pnpm npm yarn bun pnpm dlx shadcn@latest view button card dialog Copy
 Or view items from namespaced registries:
 pnpm npm yarn bun pnpm dlx shadcn@latest view @acme/auth @v0/dashboard Copy
 Options
 Copy Usage: shadcn view [options] &lt; items... &gt;

 view items from the registry

 Arguments:
 items the item names or URLs to view

 Options:
 -c, --cwd &lt; cw d &gt; the working directory. defaults to the current directory.
 -h, --help display help for command

 search #
 Use the search command to search for items from registries.
 pnpm npm yarn bun pnpm dlx shadcn@latest search [registry] Copy
 You can search with a query:
 pnpm npm yarn bun pnpm dlx shadcn@latest search @shadcn -q &quot;button&quot; Copy
 Or search multiple registries at once:
 pnpm npm yarn bun pnpm dlx shadcn@latest search @shadcn @v0 @acme Copy
 The list command is an alias for search :
 pnpm npm yarn bun pnpm dlx shadcn@latest list @acme Copy
 Options
 Copy Usage: shadcn search | list [options] &lt; registries... &gt;

 search items from registries

 Arguments:
 registries the registry names or urls to search items from. Names
 must be prefixed with @.

 Options:
 -c, --cwd &lt; cw d &gt; the working directory. defaults to the current directory.
 -q, --query &lt; quer y &gt; query string
 -l, --limit &lt; numbe r &gt; maximum number of items to display per registry (default: &quot;100&quot; )
 -o, --offset &lt; numbe r &gt; number of items to skip (default: &quot;0&quot; )
 -h, --help display help for command

 build #
 Use the build command to generate the registry JSON files.
 pnpm npm yarn bun pnpm dlx shadcn@latest build Copy
 This command reads the registry.json file and generates the registry JSON files in the public/r directory.
 Options
 Copy Usage: shadcn build [options] [registry]

 build components for a shadcn registry

 Arguments:
 registry path to registry.json file (default: &quot;./registry.json&quot; )

 Options:
 -o, --output &lt; pat h &gt; destination directory for json files (default: &quot;./public/r&quot; )
 -c, --cwd &lt; cw d &gt; the working directory. defaults to the current directory.
 -h, --help display help for command
 To customize the output directory, use the --output option.
 pnpm npm yarn bun pnpm dlx shadcn@latest build --output ./public/registry Copy

 docs #
 Use the docs command to fetch documentation and API references for components.
 pnpm npm yarn bun pnpm dlx shadcn@latest docs [component] Copy
 Options
 Copy Usage: shadcn docs [options] [component]

 fetch documentation and API references for components

 Arguments:
 component the component to get docs for

 Options:
 -c, --cwd &lt; cw d &gt; the working directory. defaults to the current directory.
 -b, --base &lt; bas e &gt; the base to use either &#x27;base&#x27; or &#x27;radix&#x27;. defaults to project base.
 --json output as JSON. (default: false )
 -h, --help display help for command

 info #
 Use the info command to get information about your project.
 pnpm npm yarn bun pnpm dlx shadcn@latest info Copy
 Options
 Copy Usage: shadcn info [options]

 get information about your project

 Options:
 -c, --cwd &lt; cw d &gt; the working directory. defaults to the current directory.
 --json output as JSON. (default: false )
 -h, --help display help for command

 migrate #
 Use the migrate command to run migrations on your project.
 pnpm npm yarn bun pnpm dlx shadcn@latest migrate [migration] Copy
 Available Migrations
 Migration Description icons Migrate your UI components to a different icon library. radix Migrate to radix-ui. rtl Migrate your components to support RTL (right-to-left).
 Options
 Copy Usage: shadcn migrate [options] [migration] [path]

 run a migration.

 Arguments:
 migration the migration to run.
 path optional path or glob pattern to migrate.

 Options:
 -c, --cwd &lt; cw d &gt; the working directory. defaults to the current directory.
 -l, --list list all migrations. (default: false )
 -y, --yes skip confirmation prompt. (default: false )
 -h, --help display help for command

 migrate rtl #
 The rtl migration transforms your components to support RTL (right-to-left) languages.
 pnpm npm yarn bun pnpm dlx shadcn@latest migrate rtl Copy
 This will:

 Update components.json to set rtl: true
 Transform physical CSS properties to logical equivalents (e.g., ml-4 → ms-4 , text-left → text-start )
 Add rtl: variants where needed (e.g., space-x-4 → space-x-4 rtl:space-x-reverse )

 Migrate specific files
 You can migrate specific files or use glob patterns:
 Copy # Migrate a specific file
 npx shadcn@latest migrate rtl src/components/ui/button.tsx

 # Migrate files matching a glob pattern
 npx shadcn@latest migrate rtl &quot;src/components/ui/**&quot;
 If no path is provided, the migration will transform all files in your ui directory (from components.json ).

 migrate radix #
 The radix migration updates your imports from individual @radix-ui/react-* packages to the unified radix-ui package.
 pnpm npm yarn bun pnpm dlx shadcn@latest migrate radix Copy
 This will:

 Transform imports from @radix-ui/react-* to radix-ui
 Add the radix-ui package to your package.json

 Before
 Copy import * as DialogPrimitive from &quot;@radix-ui/react-dialog&quot;
 import * as SelectPrimitive from &quot;@radix-ui/react-select&quot;
 After
 Copy import { Dialog as DialogPrimitive, Select as SelectPrimitive } from &quot;radix-ui&quot;
 Migrate specific files
 You can migrate specific files or use glob patterns:
 Copy # Migrate a specific file.
 npx shadcn@latest migrate radix src/components/ui/dialog.tsx

 # Migrate files matching a glob pattern.
 npx shadcn@latest migrate radix &quot;src/components/ui/**&quot;
 If no path is provided, the migration will transform all files in your ui directory (from components.json ).
 Once complete, you can remove any unused @radix-ui/react-* packages from your package.json .

 eject #
 When you run init , shadcn adds @import &quot;shadcn/tailwind.css&quot; to your global CSS file. This import provides shared Tailwind v4 utilities such as custom variants ( data-open: , data-closed: , etc.) and accordion animations.
 Use the eject command to inline shadcn/tailwind.css into your global CSS file and remove the shadcn dependency from your project.
 Note: This action is irreversible. After ejecting, future shadcn CLI
updates to shadcn/tailwind.css will not apply automatically.
 pnpm npm yarn bun pnpm dlx shadcn@latest eject Copy
 Before
 Copy @import &quot;tailwindcss&quot; ;
 @import &quot;tw-animate-css&quot; ;
 @import &quot;shadcn/tailwind.css&quot; ;
 After
 Copy @import &quot;tailwindcss&quot; ;
 @import &quot;tw-animate-css&quot; ;
 /* ejected from shadcn@4.8.3 */
 @theme inline {
 @keyframes accordion-down {
 from {
 height : 0 ;
 }
 to {
 height : var (
 --radix-accordion-content-height ,
 var ( --accordion-panel-height , auto )
 );
 }
 }
 }

 @custom-variant data-open {
 &amp; :where ([ data-state = &quot;open&quot; ]),
 &amp; :where ([ data-open ] :not ([ data-open = &quot;false&quot; ])) {
 @ slot ;
 }
 }

 @utility no-scrollbar {
 -ms-overflow-style: none;
 scrollbar-width : none;

 &amp; ::-webkit-scrollbar {
 display : none ;
 }
 }
 Monorepo
 In a monorepo, run the command from the workspace that contains your components.json and global CSS file:
 pnpm npm yarn bun pnpm dlx shadcn@latest eject -c packages/ui Copy
 Options
 Copy Usage: shadcn eject [options]

 inline shadcn/tailwind.css and remove the shadcn dependency

 Options:
 -c, --cwd &lt; cw d &gt; the working directory. defaults to the current directory.
 -y, --yes skip confirmation prompt. (default: false )
 -s, --silent mute output. (default: false )
 -h, --help display help for command RTL Monorepo On This Page init add apply preset preset decode preset resolve preset url preset open view search build docs info migrate migrate rtl migrate radix eject Deploy your shadcn/ui app on Vercel Trusted by OpenAI, Sonos, Adobe, and more. Vercel provides tools and infrastructure to deploy apps and features at scale. Deploy Now Deploy to Vercel Built by shadcn at Vercel . The source code is available on GitHub . Get Code
