Getting Started - shadcn/ui Toggle Menu Menu Home Docs Components Blocks Charts Directory Create Search documentation... Search... 117k Toggle theme New Sections Introduction Components Installation Theming CLI RTL Skills MCP Server Registry Forms Changelog Components Accordion Alert Alert Dialog Aspect Ratio Avatar Badge Breadcrumb Button Button Group Calendar Card Carousel Chart Checkbox Collapsible Combobox Command Context Menu Data Table Date Picker Dialog Direction Drawer Dropdown Menu Empty Field Hover Card Input Input Group Input OTP Item Kbd Label Menubar Native Select Navigation Menu Pagination Popover Progress Radio Group Resizable Scroll Area Select Separator Sheet Sidebar Skeleton Slider Sonner Spinner Switch Table Tabs Textarea Toast Toggle Toggle Group Tooltip Typography Get Started Installation components.json Package Imports Theming Dark Mode CLI Monorepo Skills JavaScript Figma llms.txt Legacy Docs Forms React Hook Form TanStack Form Formisch Registry Introduction Getting Started GitHub Registries Registry Directory Examples Namespaces Authentication MCP Server Open in v0 API Reference registry.json registry-item.json Getting Started Copy Page Previous Next Learn how to get setup and run your own component registry. This guide will walk you through the process of setting up your own registry. It assumes you already have a project with components, hooks, utilities or other files you would like to distribute.
 If you have an existing public GitHub repository, you can turn it into a
registry by adding a registry.json file at the root. See
 GitHub Registries for details.
 If you&#x27;re starting a new registry project, you can use the registry template as a starting point. We have already configured it for you.
 Requirements #
 You are free to design and publish your custom registry as you see fit. The only requirement is that your registry catalog and registry items must conform to the registry schema specification and registry-item schema specification .
 Your registry can be a Next.js, Vite, Vue, Svelte, PHP or any other framework as long as it supports serving JSON over HTTP. It can also be a public GitHub repository with a registry.json file at the root.
 If you&#x27;d like to see an example of a registry, we have a template project for you to use as a starting point.
 registry.json #
 The registry.json is the entry point for the registry. It contains the registry&#x27;s name, homepage, and defines all the items present in the registry.
 Your registry must have this file (or JSON payload) present at the root of the registry endpoint. The registry endpoint is the URL where your registry is hosted.
 Here&#x27;s an example registry.json file:
 registry.json Copy {
 &quot;$schema&quot; : &quot;https://ui.shadcn.com/schema/registry.json&quot; ,
 &quot;name&quot; : &quot;acme&quot; ,
 &quot;homepage&quot; : &quot;https://acme.com&quot; ,
 &quot;items&quot; : [
 {
 &quot;name&quot; : &quot;button&quot; ,
 &quot;type&quot; : &quot;registry:ui&quot; ,
 &quot;title&quot; : &quot;Button&quot; ,
 &quot;description&quot; : &quot;A simple button component.&quot; ,
 &quot;files&quot; : [
 {
 &quot;path&quot; : &quot;components/ui/button.tsx&quot; ,
 &quot;type&quot; : &quot;registry:ui&quot;
 }
 ]
 }
 ]
 }
 Structure your registry #
 You can structure your source registry in one of two ways:

 Define all items in a single root registry.json .
 Use a root registry.json with include to compose multiple registry.json files.

 Option A: Single registry.json #
 Create a registry.json file in the root of your project. Add all your registry items to the items array. This is the simplest way to define a registry.
 registry.json Copy {
 &quot;$schema&quot; : &quot;https://ui.shadcn.com/schema/registry.json&quot; ,
 &quot;name&quot; : &quot;acme&quot; ,
 &quot;homepage&quot; : &quot;https://acme.com&quot; ,
 &quot;items&quot; : [
 {
 &quot;name&quot; : &quot;button&quot; ,
 &quot;type&quot; : &quot;registry:ui&quot; ,
 &quot;title&quot; : &quot;Button&quot; ,
 &quot;description&quot; : &quot;A simple button component.&quot; ,
 &quot;files&quot; : [
 {
 &quot;path&quot; : &quot;components/ui/button.tsx&quot; ,
 &quot;type&quot; : &quot;registry:ui&quot;
 }
 ]
 },
 {
 &quot;name&quot; : &quot;hello-world&quot; ,
 &quot;type&quot; : &quot;registry:block&quot; ,
 &quot;title&quot; : &quot;Hello World&quot; ,
 &quot;description&quot; : &quot;A simple hello world component.&quot; ,
 &quot;registryDependencies&quot; : [ &quot;button&quot; ],
 &quot;files&quot; : [
 {
 &quot;path&quot; : &quot;registry/default/hello-world/hello-world.tsx&quot; ,
 &quot;type&quot; : &quot;registry:component&quot;
 }
 ]
 }
 ]
 }
 This registry.json file must conform to the registry schema specification .
 Option B: Using include #
 For larger registries, you can use include to compose your source registry
from multiple registry.json files.
 Copy registry.json
 components
 └── ui
 ├── button.tsx
 ├── input.tsx
 └── registry.json
 hooks
 ├── registry.json
 ├── use-media-query.ts
 └── use-toggle.ts
 The root registry.json defines the registry metadata and includes the nested
registry files.

 registry.json Copy {
 &quot;$schema&quot; : &quot;https://ui.shadcn.com/schema/registry.json&quot; ,
 &quot;name&quot; : &quot;acme&quot; ,
 &quot;homepage&quot; : &quot;https://acme.com&quot; ,
 &quot;include&quot; : [
 &quot;components/ui/registry.json&quot; ,
 &quot;hooks/registry.json&quot;
 ]
 }
 Included registry.json files are valid registry files for composition and may
omit name and homepage . Only the root registry.json must define the
registry metadata.
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
 },
 {
 &quot;name&quot; : &quot;input&quot; ,
 &quot;type&quot; : &quot;registry:ui&quot; ,
 &quot;files&quot; : [
 {
 &quot;path&quot; : &quot;input.tsx&quot; ,
 &quot;type&quot; : &quot;registry:ui&quot;
 }
 ]
 }
 ]
 }
 hooks/registry.json Copy {
 &quot;$schema&quot; : &quot;https://ui.shadcn.com/schema/registry.json&quot; ,
 &quot;items&quot; : [
 {
 &quot;name&quot; : &quot;use-toggle&quot; ,
 &quot;type&quot; : &quot;registry:hook&quot; ,
 &quot;files&quot; : [
 {
 &quot;path&quot; : &quot;use-toggle.ts&quot; ,
 &quot;type&quot; : &quot;registry:hook&quot;
 }
 ]
 },
 {
 &quot;name&quot; : &quot;use-media-query&quot; ,
 &quot;type&quot; : &quot;registry:hook&quot; ,
 &quot;files&quot; : [
 {
 &quot;path&quot; : &quot;use-media-query.ts&quot; ,
 &quot;type&quot; : &quot;registry:hook&quot;
 }
 ]
 }
 ]
 }
 When using include , file paths are relative to the registry.json file that
declares the item.
 Add an item #
 Create a UI component #
 Add your first item. Here&#x27;s an example of a simple &lt;Button /&gt; component:
 components/ui/button.tsx Copy import * as React from &quot;react&quot;

 export function Button ( props : React . ComponentProps &lt; &quot;button&quot; &gt;) {
 return (
 &lt; button
 { ... props }
 className = &quot;rounded-md bg-neutral-900 px-4 py-2 text-sm font-medium text-white&quot;
 /&gt;
 )
 }
 Note: This example places the component in the components/ui directory.
You can place it anywhere in your project as long as you set the correct path
in the registry.json file.
 Copy components
 └── ui
 └── button.tsx
 Add the item to the registry #
 To add your component to the registry, add an item definition to registry.json .
If you are using include , add the item to the included registry.json file
that owns the component. For example, add a UI component to
 components/ui/registry.json .
 registry.json Copy {
 &quot;$schema&quot; : &quot;https://ui.shadcn.com/schema/registry.json&quot; ,
 &quot;name&quot; : &quot;acme&quot; ,
 &quot;homepage&quot; : &quot;https://acme.com&quot; ,
 &quot;items&quot; : [
 {
 &quot;name&quot; : &quot;button&quot; ,
 &quot;type&quot; : &quot;registry:ui&quot; ,
 &quot;title&quot; : &quot;Button&quot; ,
 &quot;description&quot; : &quot;A simple button component.&quot; ,
 &quot;files&quot; : [
 {
 &quot;path&quot; : &quot;components/ui/button.tsx&quot; ,
 &quot;type&quot; : &quot;registry:ui&quot;
 }
 ]
 }
 ]
 }
 You define your registry item by adding a name , type , title , description and files .
 For every file you add, you must specify the path and type of the file. In a single-file registry, the path is relative to the root of your project. When using include , the path is relative to the registry.json file that declares the item. The type is the type of the file.
 You can read more about the registry item schema and file types in the registry item schema docs .
 Serve your registry #
 You can serve your registry as static JSON files or from dynamic route handlers.
 Option A: Static JSON files #
 Run the build command to generate static registry JSON files.
 pnpm npm yarn bun pnpm dlx shadcn@latest build Copy
 If your source registry uses include , shadcn build resolves the included
registries and writes a flattened registry to your output directory. The
generated registry.json does not contain include .
 Note: By default, the build command will generate the registry JSON files
in public/r e.g public/r/button.json . You can change the output directory by passing the --output option. See the shadcn build command for more information.
 If you&#x27;re running your registry on Next.js, you can serve these files by running
the next server. The command might differ for other frameworks.
 pnpm npm yarn bun pnpm dev Copy
 Your files will now be served at http://localhost:3000/r/[NAME].json eg. http://localhost:3000/r/button.json .
 Option B: Dynamic route handlers #
 If you want to serve registry JSON from your source registry.json at request
time, use the producer-side loader APIs from shadcn/registry .
 Install shadcn as a runtime dependency:
 pnpm npm yarn bun pnpm add shadcn Copy
 Use loadRegistry to serve the registry catalog.
 app/r/registry.json/route.ts Copy import { loadRegistry } from &quot;shadcn/registry&quot;

 export async function GET () {
 try {
 const registry = await loadRegistry ()

 return Response. json (registry)
 } catch (error) {
 console. error (error)

 return Response. json ({ error: &quot;Failed to load registry.&quot; }, { status: 500 })
 }
 }
 Use loadRegistryItem to serve individual registry items.
 app/r/[name].json/route.ts Copy import { loadRegistryItem, RegistryItemNotFoundError } from &quot;shadcn/registry&quot;

 export async function GET (
 _request : Request ,
 context : {
 params : Promise &lt;{
 name : string
 }&gt;
 }
 ) {
 const { name } = await context.params

 try {
 const item = await loadRegistryItem (name)

 return Response. json (item)
 } catch (error) {
 if (error instanceof RegistryItemNotFoundError ) {
 return Response. json (
 { error: `Registry item &quot;${ name }&quot; was not found.` },
 { status: 404 }
 )
 }

 console. error (error)

 return Response. json (
 { error: &quot;Failed to load registry item.&quot; },
 { status: 500 }
 )
 }
 }
 Both loaders resolve include before returning JSON, so route handlers can use
the same source registry.json structure without running shadcn build .
 Content negotiation
 Test your registry #
 After your registry is being served, test it with the same CLI commands that
other developers will use.
 Using URL #
 Use the catalog URL for commands that discover items, like list and search .
Use item URLs for commands that read or install a specific item, like view and
 add .
 List items #
 Start by confirming that the registry catalog can be discovered.
 pnpm npm yarn bun pnpm dlx shadcn@latest list http://localhost:3000/r/registry.json Copy
 Search items #
 Search the registry by query.
 pnpm npm yarn bun pnpm dlx shadcn@latest search http://localhost:3000/r/registry.json --query button Copy
 View an item #
 Then view one registry item by name.
 pnpm npm yarn bun pnpm dlx shadcn@latest view http://localhost:3000/r/button.json Copy
 Add an item #
 To test the install flow, run add from a project where you want to install the
item.
 pnpm npm yarn bun pnpm dlx shadcn@latest add http://localhost:3000/r/button.json Copy
 Using namespace #
 Add the registry #
 You can also test your registry with a namespace. From a project with a
 components.json file, add your registry URL template to the project.
 pnpm npm yarn bun pnpm dlx shadcn@latest registry add @acme=http://localhost:3000/r/{name}.json Copy
 The {name} placeholder must resolve to an item JSON file. For example,
 @acme/button resolves to http://localhost:3000/r/button.json . The catalog is
still served separately at http://localhost:3000/r/registry.json .
 List items #
 Then list the items in your registry.
 pnpm npm yarn bun pnpm dlx shadcn@latest list @acme Copy
 Search items #
 Search the registry by query.
 pnpm npm yarn bun pnpm dlx shadcn@latest search @acme --query button Copy
 View an item #
 View one registry item by name.
 pnpm npm yarn bun pnpm dlx shadcn@latest view @acme/button Copy
 Add an item #
 To test the install flow, run add from a project where you want to install the
item.
 pnpm npm yarn bun pnpm dlx shadcn@latest add @acme/button Copy
 See the Namespaced Registries docs for more
information.
 Publish your registry #
 To make your registry available to other developers, publish your project to a
public URL. Once deployed, users can install items directly from item URLs, or
they can add your registry as a namespace in their project.
 Share namespace setup instructions #
 If you want users to install items with a namespace like @acme/button , tell
them to add your registry URL template to their project. The {name}
placeholder is replaced by the item name when the CLI resolves the registry
item.
 The template must resolve to item JSON files. For example, @acme/button
resolves to https://acme.com/r/button.json . Your registry catalog should still
be served separately at https://acme.com/r/registry.json .
 They can add the namespace with the CLI.
 pnpm npm yarn bun pnpm dlx shadcn@latest registry add @acme=https://acme.com/r/{name}.json Copy
 Or they can add it manually under the registries field in their
 components.json file.
 components.json Copy {
 &quot;registries&quot; : {
 &quot;@acme&quot; : &quot;https://acme.com/r/{name}.json&quot;
 }
 }
 Users can then consume items from your registry by namespace.
 pnpm npm yarn bun pnpm dlx shadcn@latest add @acme/button Copy
 Add your namespace to the registry index #
 If your registry is open source and publicly available, you can submit your
namespace to the official registry index. This lets users add your namespace by
name instead of pasting the full URL template.
 See the Registry Index docs for the submission
requirements.
 Guidelines #
 Here are some guidelines to follow when building components for a registry.

 Place your registry item in the registry/[STYLE]/[NAME] directory. I&#x27;m using default as an example. It can be anything you want as long as it&#x27;s nested under the registry directory.
 For blocks, the following properties are required: name , description , type and files .
 It is recommended to add a proper name and description to your registry item. This helps LLMs understand the component and its purpose.
 Make sure to list all registry dependencies in registryDependencies . A registry dependency is an item address such as button , @acme/input-form , acme/ui/button or http://localhost:3000/r/editor.json .
 Make sure to list all dependencies in dependencies . A dependency is the name of the package in the registry eg. zod , sonner , etc. To set a version, you can use the name@version format eg. zod@^3.20.0 .
 Imports should always use the @/registry path. eg. import { HelloWorld } from &quot;@/registry/default/hello-world/hello-world&quot;
 Ideally, place your files within a registry item in components , hooks , lib directories.
 Introduction GitHub Registries On This Page Requirements registry.json Structure your registry Option A: Single registry.json Option B: Using include Add an item Create a UI component Add the item to the registry Serve your registry Option A: Static JSON files Option B: Dynamic route handlers Request headers Root hosting Test your registry Using URL List items Search items View an item Add an item Using namespace Add the registry List items Search items View an item Add an item Publish your registry Share namespace setup instructions Add your namespace to the registry index Guidelines Deploy your shadcn/ui app on Vercel Trusted by OpenAI, Sonos, Adobe, and more. Vercel provides tools and infrastructure to deploy apps and features at scale. Deploy Now Deploy to Vercel Built by shadcn at Vercel . The source code is available on GitHub . Get Code
