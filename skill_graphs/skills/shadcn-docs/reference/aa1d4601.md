registry.json - shadcn/ui Toggle Menu Menu Home Docs Components Blocks Charts Directory Create Search documentation... Search... 117k Toggle theme New Sections Introduction Components Installation Theming CLI RTL Skills MCP Server Registry Forms Changelog Components Accordion Alert Alert Dialog Aspect Ratio Avatar Badge Breadcrumb Button Button Group Calendar Card Carousel Chart Checkbox Collapsible Combobox Command Context Menu Data Table Date Picker Dialog Direction Drawer Dropdown Menu Empty Field Hover Card Input Input Group Input OTP Item Kbd Label Menubar Native Select Navigation Menu Pagination Popover Progress Radio Group Resizable Scroll Area Select Separator Sheet Sidebar Skeleton Slider Sonner Spinner Switch Table Tabs Textarea Toast Toggle Toggle Group Tooltip Typography Get Started Installation components.json Package Imports Theming Dark Mode CLI Monorepo Skills JavaScript Figma llms.txt Legacy Docs Forms React Hook Form TanStack Form Formisch Registry Introduction Getting Started GitHub Registries Registry Directory Examples Namespaces Authentication MCP Server Open in v0 API Reference registry.json registry-item.json registry.json Copy Page Previous Next Schema for running your own component registry. The registry.json schema is used to define your custom component registry.
 registry.json Copy {
 &quot;$schema&quot; : &quot;https://ui.shadcn.com/schema/registry.json&quot; ,
 &quot;name&quot; : &quot;shadcn&quot; ,
 &quot;homepage&quot; : &quot;https://ui.shadcn.com&quot; ,
 &quot;items&quot; : [
 {
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
 &quot;files&quot; : [
 {
 &quot;path&quot; : &quot;registry/default/hello-world/hello-world.tsx&quot; ,
 &quot;type&quot; : &quot;registry:component&quot;
 }
 ]
 }
 ]
 }
 You can also organize a large registry across multiple registry.json files
using include .

 registry.json Copy {
 &quot;$schema&quot; : &quot;https://ui.shadcn.com/schema/registry.json&quot; ,
 &quot;name&quot; : &quot;acme&quot; ,
 &quot;homepage&quot; : &quot;https://acme.com&quot; ,
 &quot;include&quot; : [
 &quot;components/ui/registry.json&quot; ,
 &quot;hooks/registry.json&quot;
 ]
 }
 Public GitHub repositories use the same source registry format. The CLI reads
the root registry.json , resolves include , and installs files from the
repository. See the GitHub registry docs for more
information.
 Definitions #
 You can see the JSON Schema for registry.json here .
 $schema #
 The $schema property is used to specify the schema for the registry.json file.
 registry.json Copy {
 &quot;$schema&quot; : &quot;https://ui.shadcn.com/schema/registry.json&quot;
 }
 name #
 The name property is used to specify the name of your registry. This is used for data attributes and other metadata.
 registry.json Copy {
 &quot;name&quot; : &quot;acme&quot;
 }
 homepage #
 The homepage of your registry. This is used for data attributes and other metadata.
 registry.json Copy {
 &quot;homepage&quot; : &quot;https://acme.com&quot;
 }
 include #
 The include property is used to compose a registry from other registry.json
files.

 registry.json Copy {
 &quot;include&quot; : [
 &quot;components/ui/registry.json&quot; ,
 &quot;hooks/registry.json&quot;
 ]
 }
 Each include path must be a relative path to an explicit registry.json file.
Folder shorthand is not supported.

 registry.json Copy {
 &quot;include&quot; : [
 &quot;components/ui/registry.json&quot;
 ]
 }
 Included registry.json files may omit name and homepage . These fields are
required only on the root registry.json .
 components/ui/registry.json Copy {
 &quot;$schema&quot; : &quot;https://ui.shadcn.com/schema/registry.json&quot; ,
 &quot;items&quot; : [
 {
 &quot;name&quot; : &quot;button&quot; ,
 &quot;type&quot; : &quot;registry:ui&quot; ,
 &quot;files&quot; : [
 {
 &quot;path&quot; : &quot;button.tsx&quot; ,
 &quot;type&quot; : &quot;registry:ui&quot;
 }
 ]
 }
 ]
 }
 When shadcn build resolves includes, item file paths are read relative to the
 registry.json file that declares the item. The generated registry output is
flattened and does not contain include .
 Registry item names must be unique across the resolved registry, including all
included files.
 items #
 The items in your registry. Each item must implement the registry-item schema specification .
 registry.json Copy {
 &quot;items&quot; : [
 {
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
 &quot;files&quot; : [
 {
 &quot;path&quot; : &quot;registry/default/hello-world/hello-world.tsx&quot; ,
 &quot;type&quot; : &quot;registry:component&quot;
 }
 ]
 }
 ]
 }
 The root registry.json must define at least one of items or include . If
 items is omitted, it defaults to an empty array.
 See the registry-item schema documentation for more information. API Reference registry-item.json On This Page Definitions $schema name homepage include items Deploy your shadcn/ui app on Vercel Trusted by OpenAI, Sonos, Adobe, and more. Vercel provides tools and infrastructure to deploy apps and features at scale. Deploy Now Deploy to Vercel Built by shadcn at Vercel . The source code is available on GitHub . Get Code
