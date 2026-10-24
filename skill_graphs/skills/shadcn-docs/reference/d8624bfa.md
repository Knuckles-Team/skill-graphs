registry-item.json - shadcn/ui Toggle Menu Menu Home Docs Components Blocks Charts Directory Create Search documentation... Search... 117k Toggle theme New Sections Introduction Components Installation Theming CLI RTL Skills MCP Server Registry Forms Changelog Components Accordion Alert Alert Dialog Aspect Ratio Avatar Badge Breadcrumb Button Button Group Calendar Card Carousel Chart Checkbox Collapsible Combobox Command Context Menu Data Table Date Picker Dialog Direction Drawer Dropdown Menu Empty Field Hover Card Input Input Group Input OTP Item Kbd Label Menubar Native Select Navigation Menu Pagination Popover Progress Radio Group Resizable Scroll Area Select Separator Sheet Sidebar Skeleton Slider Sonner Spinner Switch Table Tabs Textarea Toast Toggle Toggle Group Tooltip Typography Get Started Installation components.json Package Imports Theming Dark Mode CLI Monorepo Skills JavaScript Figma llms.txt Legacy Docs Forms React Hook Form TanStack Form Formisch Registry Introduction Getting Started GitHub Registries Registry Directory Examples Namespaces Authentication MCP Server Open in v0 API Reference registry.json registry-item.json registry-item.json Copy Page Previous Specification for registry items. The registry-item.json schema is used to define your custom registry items.
 registry-item.json Copy {
 &quot;$schema&quot; : &quot;https://ui.shadcn.com/schema/registry-item.json&quot; ,
 &quot;name&quot; : &quot;hello-world&quot; ,
 &quot;type&quot; : &quot;registry:block&quot; ,
 &quot;title&quot; : &quot;Hello World&quot; ,
 &quot;description&quot; : &quot;A simple hello world component.&quot; ,
 &quot;registryDependencies&quot; : [
 &quot;button&quot; ,
 &quot;@acme/input-form&quot; ,
 &quot;https://example.com/r/foo&quot;
 ],
 &quot;dependencies&quot; : [ &quot;is-even@3.0.0&quot; , &quot;motion&quot; ],
 &quot;devDependencies&quot; : [ &quot;tw-animate-css&quot; ],
 &quot;files&quot; : [
 {
 &quot;path&quot; : &quot;registry/new-york/hello-world/hello-world.tsx&quot; ,
 &quot;type&quot; : &quot;registry:component&quot;
 },
 {
 &quot;path&quot; : &quot;registry/new-york/hello-world/use-hello-world.ts&quot; ,
 &quot;type&quot; : &quot;registry:hook&quot;
 }
 ],
 &quot;cssVars&quot; : {
 &quot;theme&quot; : {
 &quot;font-heading&quot; : &quot;Poppins, sans-serif&quot;
 },
 &quot;light&quot; : {
 &quot;brand&quot; : &quot;oklch(0.205 0.015 18)&quot;
 },
 &quot;dark&quot; : {
 &quot;brand&quot; : &quot;oklch(0.205 0.015 18)&quot;
 }
 }
 }
 See more examples
 Definitions #
 You can see the JSON Schema for registry-item.json here .
 $schema #
 The $schema property is used to specify the schema for the registry-item.json file.
 registry-item.json Copy {
 &quot;$schema&quot; : &quot;https://ui.shadcn.com/schema/registry-item.json&quot;
 }
 name #
 The name of the item. This is used to identify the item in the registry. It should be unique for your registry.
 registry-item.json Copy {
 &quot;name&quot; : &quot;hello-world&quot;
 }
 title #
 A human-readable title for your registry item. Keep it short and descriptive.
 registry-item.json Copy {
 &quot;title&quot; : &quot;Hello World&quot;
 }
 description #
 A description of your registry item. This can be longer and more detailed than the title .
 registry-item.json Copy {
 &quot;description&quot; : &quot;A simple hello world component.&quot;
 }
 type #
 The type property is used to specify the type of your registry item. This is used to determine the type and target path of the item when resolved for a project.
 registry-item.json Copy {
 &quot;type&quot; : &quot;registry:block&quot;
 }
 The following types are supported:
 Type Description registry:base Use for entire design systems. registry:block Use for complex components with multiple files. registry:component Use for simple components. registry:font Use for fonts. registry:lib Use for lib and utils. registry:hook Use for hooks. registry:ui Use for UI components and single-file primitives. registry:page Use for page or file-based routes. registry:file Use for miscellaneous files. registry:style Use for registry styles. eg. new-york . registry:theme Use for themes. registry:item Use for universal registry items.
 author #
 The author property is used to specify the author of the registry item.
 It can be unique to the registry item or the same as the author of the registry.
 registry-item.json Copy {
 &quot;author&quot; : &quot;John Doe &lt;john@doe.com&gt;&quot;
 }
 dependencies #
 The dependencies property is used to specify the dependencies of your registry item. This is for npm packages.
 Use @version to specify the version of your registry item.
 registry-item.json Copy {
 &quot;dependencies&quot; : [
 &quot;@radix-ui/react-accordion&quot; ,
 &quot;zod&quot; ,
 &quot;lucide-react&quot; ,
 &quot;name@1.0.2&quot;
 ]
 }
 devDependencies #
 The devDependencies property is used to specify the dev dependencies of your registry item. These are npm packages that are only needed during development.
 Use @version to specify the version of the package.
 registry-item.json Copy {
 &quot;devDependencies&quot; : [ &quot;tw-animate-css&quot; , &quot;name@1.2.0&quot; ]
 }
 registryDependencies #
 Used for registry dependencies. Each entry is an item address.

 For shadcn/ui registry items such as button , input , select , etc use the name eg. [&#x27;button&#x27;, &#x27;input&#x27;, &#x27;select&#x27;] .
 For namespaced registry items, use @namespace/item-name eg. [&#x27;@acme/input-form&#x27;] .
 For GitHub registry items, use owner/repo/item-name eg. [&#x27;acme/ui/button&#x27;] . For published registries, prefer a tag or full commit SHA eg. [&#x27;acme/ui/button#v1.2.0&#x27;] .
 For custom registry items use the URL of the registry item eg. [&#x27;https://example.com/r/hello-world.json&#x27;] .
 For local registry item files use a file path eg. [&#x27;./hello-world.json&#x27;] .

 registry-item.json Copy {
 &quot;registryDependencies&quot; : [
 &quot;button&quot; ,
 &quot;@acme/input-form&quot; ,
 &quot;acme/ui/button#v1.2.0&quot; ,
 &quot;https://example.com/r/editor.json&quot; ,
 &quot;./editor.json&quot;
 ]
 }
 Note: Bare names keep their existing behavior. button means the built-in
shadcn button item, not an item from the same GitHub repository. For
same-repository GitHub dependencies, use the full GitHub item address.
 Refs are not inherited across dependencies. If a GitHub dependency should be
reproducible, pin that dependency to its own tag or full commit SHA.
 See the GitHub registry docs for more information.
 files #
 The files property is used to specify the files of your registry item. Each file has a path , type and target (optional) property.
 The target property is required for registry:page and registry:file types.
 registry-item.json Copy {
 &quot;files&quot; : [
 {
 &quot;path&quot; : &quot;registry/new-york/hello-world/page.tsx&quot; ,
 &quot;type&quot; : &quot;registry:page&quot; ,
 &quot;target&quot; : &quot;app/hello/page.tsx&quot;
 },
 {
 &quot;path&quot; : &quot;registry/new-york/hello-world/hello-world.tsx&quot; ,
 &quot;type&quot; : &quot;registry:component&quot;
 },
 {
 &quot;path&quot; : &quot;registry/new-york/hello-world/use-hello-world.ts&quot; ,
 &quot;type&quot; : &quot;registry:hook&quot;
 },
 {
 &quot;path&quot; : &quot;registry/new-york/hello-world/.env&quot; ,
 &quot;type&quot; : &quot;registry:file&quot; ,
 &quot;target&quot; : &quot;~/.env&quot;
 }
 ]
 }
 path #
 The path property is used to specify the path to the file in your registry. This path is used by the build script to parse, transform and build the registry JSON payload.
 type #
 The type property is used to specify the type of the file. See the type section for more information.
 target #
 The target property is used to indicate where the file should be placed in a project. This is optional and only required for registry:page and registry:file types.
 By default, the shadcn cli will read a project&#x27;s components.json file to determine the target path. For some files, such as routes or config you can specify the target path manually.
 Use ~ to refer to the root of the project e.g ~/foo.config.js .
 You can also use registry target placeholders to place files under the
directories configured by the user&#x27;s components.json . These placeholders are
only supported at the start of target and are independent of the project&#x27;s
import prefix. For example, @ui/button.tsx works whether the project imports
components with @/ , # , package imports or workspace exports.
 Placeholder Resolves to @components/ aliases.components @ui/ aliases.ui @lib/ aliases.lib @hooks/ aliases.hooks
 Use these placeholders when you want a registry item to install into the
project&#x27;s configured shadcn directories without hardcoding components , src
or workspace package paths. Anything after the placeholder is preserved, so
 @ui/ai/prompt-input.tsx installs under the user&#x27;s configured ui directory
at ai/prompt-input.tsx .
 registry-item.json Copy {
 &quot;files&quot; : [
 {
 &quot;path&quot; : &quot;registry/new-york/example/button.tsx&quot; ,
 &quot;type&quot; : &quot;registry:ui&quot; ,
 &quot;target&quot; : &quot;@ui/button.tsx&quot;
 },
 {
 &quot;path&quot; : &quot;registry/new-york/example/prompt-input.tsx&quot; ,
 &quot;type&quot; : &quot;registry:ui&quot; ,
 &quot;target&quot; : &quot;@ui/ai/prompt-input.tsx&quot;
 },
 {
 &quot;path&quot; : &quot;registry/new-york/example/card.tsx&quot; ,
 &quot;type&quot; : &quot;registry:component&quot; ,
 &quot;target&quot; : &quot;@components/card.tsx&quot;
 },
 {
 &quot;path&quot; : &quot;registry/new-york/example/helper.ts&quot; ,
 &quot;type&quot; : &quot;registry:lib&quot; ,
 &quot;target&quot; : &quot;@lib/helper.ts&quot;
 },
 {
 &quot;path&quot; : &quot;registry/new-york/example/use-demo.ts&quot; ,
 &quot;type&quot; : &quot;registry:hook&quot; ,
 &quot;target&quot; : &quot;@hooks/use-demo.ts&quot;
 }
 ]
 }
 The target property decides where the file is written. It can point to a
different shadcn directory than the file type .
 registry-item.json Copy {
 &quot;files&quot; : [
 {
 &quot;path&quot; : &quot;registry/new-york/example/format-date.ts&quot; ,
 &quot;type&quot; : &quot;registry:ui&quot; ,
 &quot;target&quot; : &quot;@lib/format-date.ts&quot;
 }
 ]
 }
 Unknown placeholders are treated as regular target paths. For example,
 @foo/bar.ts is written as foo/bar.ts . Embedded placeholders such as
 components/@ui/button.tsx are also treated as regular paths.
 @utils/ is not supported because utils points to a file, not a directory.
 tailwind #
 DEPRECATED: Use cssVars.theme instead for Tailwind v4 projects.
 The tailwind property is used for tailwind configuration such as theme , plugins and content .
 You can use the tailwind.config property to add colors, animations and plugins to your registry item.
 registry-item.json Copy {
 &quot;tailwind&quot; : {
 &quot;config&quot; : {
 &quot;theme&quot; : {
 &quot;extend&quot; : {
 &quot;colors&quot; : {
 &quot;brand&quot; : &quot;hsl(var(--brand))&quot;
 },
 &quot;keyframes&quot; : {
 &quot;wiggle&quot; : {
 &quot;0%, 100%&quot; : { &quot;transform&quot; : &quot;rotate(-3deg)&quot; },
 &quot;50%&quot; : { &quot;transform&quot; : &quot;rotate(3deg)&quot; }
 }
 },
 &quot;animation&quot; : {
 &quot;wiggle&quot; : &quot;wiggle 1s ease-in-out infinite&quot;
 }
 }
 }
 }
 }
 }
 cssVars #
 Use to define CSS variables for your registry item.
 registry-item.json Copy {
 &quot;cssVars&quot; : {
 &quot;theme&quot; : {
 &quot;font-heading&quot; : &quot;Poppins, sans-serif&quot;
 },
 &quot;light&quot; : {
 &quot;brand&quot; : &quot;20 14.3% 4.1%&quot; ,
 &quot;radius&quot; : &quot;0.5rem&quot;
 },
 &quot;dark&quot; : {
 &quot;brand&quot; : &quot;20 14.3% 4.1%&quot;
 }
 }
 }
 css #
 Use css to add new rules to the project&#x27;s CSS file eg. @layer base , @layer components , @utility , @keyframes , @plugin , etc.
 registry-item.json Copy {
 &quot;css&quot; : {
 &quot;@plugin @tailwindcss/typography&quot; : {},
 &quot;@plugin foo&quot; : {},
 &quot;@layer base&quot; : {
 &quot;body&quot; : {
 &quot;font-size&quot; : &quot;var(--text-base)&quot; ,
 &quot;line-height&quot; : &quot;1.5&quot;
 }
 },
 &quot;@layer components&quot; : {
 &quot;button&quot; : {
 &quot;background-color&quot; : &quot;var(--color-primary)&quot; ,
 &quot;color&quot; : &quot;var(--color-white)&quot;
 }
 },
 &quot;@utility text-magic&quot; : {
 &quot;font-size&quot; : &quot;var(--text-base)&quot; ,
 &quot;line-height&quot; : &quot;1.5&quot;
 },
 &quot;@keyframes wiggle&quot; : {
 &quot;0%, 100%&quot; : {
 &quot;transform&quot; : &quot;rotate(-3deg)&quot;
 },
 &quot;50%&quot; : {
 &quot;transform&quot; : &quot;rotate(3deg)&quot;
 }
 }
 }
 }
 envVars #
 Use envVars to add environment variables to your registry item.
 registry-item.json Copy {
 &quot;envVars&quot; : {
 &quot;NEXT_PUBLIC_APP_URL&quot; : &quot;http://localhost:4000&quot; ,
 &quot;DATABASE_URL&quot; : &quot;postgresql://postgres:postgres@localhost:5432/postgres&quot; ,
 &quot;OPENAI_API_KEY&quot; : &quot;&quot;
 }
 }
 Environment variables are added to the .env.local or .env file. Existing variables are not overwritten.
 IMPORTANT: Use envVars to add development or example variables. Do NOT use it to add production variables.
 font #
 The font property is required for registry:font items. It configures the font family, provider, import name, CSS variable, and the npm package to install for non-Next.js projects.
 registry-item.json Copy {
 &quot;font&quot; : {
 &quot;family&quot; : &quot;&#x27;Inter Variable&#x27;, sans-serif&quot; ,
 &quot;provider&quot; : &quot;google&quot; ,
 &quot;import&quot; : &quot;Inter&quot; ,
 &quot;variable&quot; : &quot;--font-sans&quot; ,
 &quot;subsets&quot; : [ &quot;latin&quot; ],
 &quot;dependency&quot; : &quot;@fontsource-variable/inter&quot;
 }
 }
 Property Type Required Description family string Yes The CSS font-family value. provider string Yes The font provider. Currently only google is supported. import string Yes The import name for the font from next/font/google . variable string Yes The CSS variable name for the font (e.g., --font-sans , --font-mono ). weight string[] No Array of font weights to include. subsets string[] No Array of font subsets to include. selector string No CSS selector to apply the font to. Defaults to html . dependency string No The npm package to install for non-Next.js projects (e.g., @fontsource-variable/inter ).
 docs #
 Use docs to show custom documentation or message when installing your registry item via the CLI.
 registry-item.json Copy {
 &quot;docs&quot; : &quot;To get an OPENAI_API_KEY, sign up for an account at https://platform.openai.com.&quot;
 }
 categories #
 Use categories to organize your registry item.
 registry-item.json Copy {
 &quot;categories&quot; : [ &quot;sidebar&quot; , &quot;dashboard&quot; ]
 }
 meta #
 Use meta to add additional metadata to your registry item. You can add any key/value pair that you want to be available to the registry item.
 registry-item.json Copy {
 &quot;meta&quot; : { &quot;foo&quot; : &quot;bar&quot; }
 } registry.json On This Page Definitions $schema name title description type author dependencies devDependencies registryDependencies files path type target tailwind cssVars css envVars font docs categories meta Deploy your shadcn/ui app on Vercel Trusted by OpenAI, Sonos, Adobe, and more. Vercel provides tools and infrastructure to deploy apps and features at scale. Deploy Now Deploy to Vercel Built by shadcn at Vercel . The source code is available on GitHub . Get Code
