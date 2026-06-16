Changelog - shadcn/ui Toggle Menu Menu Home Docs Components Blocks Charts Directory Create Search documentation... Search... 117k Toggle theme New Sections Introduction Components Installation Theming CLI RTL Skills MCP Server Registry Forms Changelog Components Accordion Alert Alert Dialog Aspect Ratio Avatar Badge Breadcrumb Button Button Group Calendar Card Carousel Chart Checkbox Collapsible Combobox Command Context Menu Data Table Date Picker Dialog Direction Drawer Dropdown Menu Empty Field Hover Card Input Input Group Input OTP Item Kbd Label Menubar Native Select Navigation Menu Pagination Popover Progress Radio Group Resizable Scroll Area Select Separator Sheet Sidebar Skeleton Slider Sonner Spinner Switch Table Tabs Textarea Toast Toggle Toggle Group Tooltip Typography Get Started Installation components.json Package Imports Theming Dark Mode CLI Monorepo Skills JavaScript Figma llms.txt Legacy Docs Forms React Hook Form TanStack Form Formisch Registry Introduction Getting Started GitHub Registries Registry Directory Examples Namespaces Authentication MCP Server Open in v0 API Reference registry.json registry-item.json Changelog RSS Latest updates and announcements. June 2026 - GitHub Registries You can now turn any public GitHub repository into a registry.
 Add a registry.json file at the root of the repository, define the items you
want to distribute, and users can install them directly from GitHub with the
 shadcn CLI.
 pnpm npm yarn bun pnpm dlx shadcn@latest add &lt;username&gt;/&lt;repo&gt;/&lt;item&gt; Copy
 For example, to install the project-conventions item from the acme/toolkit repository:
 pnpm npm yarn bun pnpm dlx shadcn@latest add acme/toolkit/project-conventions Copy
 GitHub registries are source registries. You do not need to run shadcn build ,
publish generated item JSON files or set up a registry server. The CLI reads the
root registry.json , resolves include entries, finds the requested item and
installs the files declared by that item.
 Distribute anything #
 Registry items are not limited to components. A GitHub registry can distribute
components, hooks, utilities, design tokens, feature kits, project conventions,
agent instructions, testing setup, CI workflows, release workflows, templates,
codemods, migration kits and other project files.
 For example, a repository can expose a project-conventions item that installs
shared docs, editor settings and agent instructions:
 registry.json Copy {
 &quot;$schema&quot; : &quot;https://ui.shadcn.com/schema/registry.json&quot; ,
 &quot;name&quot; : &quot;acme-toolkit&quot; ,
 &quot;homepage&quot; : &quot;https://github.com/acme/toolkit&quot; ,
 &quot;items&quot; : [
 {
 &quot;name&quot; : &quot;project-conventions&quot; ,
 &quot;type&quot; : &quot;registry:item&quot; ,
 &quot;files&quot; : [
 {
 &quot;path&quot; : &quot;AGENTS.md&quot; ,
 &quot;type&quot; : &quot;registry:file&quot; ,
 &quot;target&quot; : &quot;~/AGENTS.md&quot;
 },
 {
 &quot;path&quot; : &quot;.editorconfig&quot; ,
 &quot;type&quot; : &quot;registry:file&quot; ,
 &quot;target&quot; : &quot;~/.editorconfig&quot;
 },
 {
 &quot;path&quot; : &quot;docs/conventions.md&quot; ,
 &quot;type&quot; : &quot;registry:file&quot; ,
 &quot;target&quot; : &quot;~/docs/conventions.md&quot;
 }
 ]
 }
 ]
 }
 Commands #
 GitHub registry addresses work with the same commands as other registry
addresses.
 List items from a GitHub registry:
 pnpm npm yarn bun pnpm dlx shadcn@latest list acme/toolkit Copy
 Search items:
 pnpm npm yarn bun pnpm dlx shadcn@latest search acme/toolkit --query conventions Copy
 View an item:
 pnpm npm yarn bun pnpm dlx shadcn@latest view acme/toolkit/project-conventions Copy
 Install an item:
 pnpm npm yarn bun pnpm dlx shadcn@latest add acme/toolkit/project-conventions Copy
 See the GitHub Registries docs for the full guide. May 2026 - shadcn eject When we added support for both Radix and Base UI, we needed a place for shared Tailwind utilities that both libraries depend on, e.g. custom variants like data-open: and data-closed: and utilities like no-scrollbar .
 We also ran into a few bugs while working on RTL support that were easier to fix in one shared place rather than duplicating across every component.
 So we created shadcn/tailwind.css . When you run init , it adds @import &quot;shadcn/tailwind.css&quot; to your global CSS file. It works just like other CSS imports such as tw-animate-css : a small dependency that is tree-shaken in production and resolved at build time.
 If you prefer not to depend on the shadcn package for that CSS, we&#x27;ve added the shadcn eject command. It inlines shadcn/tailwind.css into your global CSS file and removes the shadcn dependency from your project.
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
 In a monorepo, run the command from the workspace that contains your components.json and global CSS file:
 pnpm npm yarn bun pnpm dlx shadcn@latest eject -c packages/ui Copy
 See the CLI documentation for more details. May 2026 - Introducing Rhea Introducing Rhea, a new shadcn/ui style. A more compact Luma. Smaller spacing. Denser surfaces. Built for focused product interfaces.
 Try Rhea in shadcn/create
 Rhea started from a simple request we&#x27;ve heard a lot: Luma, but more compact. We looked at how people were using the new styles and what they were asking for, and the pattern was clear. A lot of teams wanted the softness and shape of Luma with tighter spacing, smaller controls, and more information density.
 Rhea keeps the same rounded foundation, but makes it more compact for product interfaces where space matters. Buttons, inputs, menus, cards, and lists all sit a little tighter so the UI can carry more without feeling crowded.
 Why a new style? #
 We considered making this a spacing tweak for Luma, but --spacing is a multiplier. Changing it would change what familiar utilities mean across your app. p-2 , w-4 , and m-16 would no longer mean the same size.
 That tradeoff felt wrong. Compactness should not force you to relearn Tailwind&#x27;s spacing scale or wonder whether a utility means something different in one style than another.
 So Rhea is a new style instead. It lets us adjust component sizes, gaps, and density directly while keeping the underlying utility scale predictable.
 Available now in shadcn/create for both Radix and Base UI.
 Try Rhea May 2026 - Registry Include and Validate This release adds two updates for registry authors:

 include for composing large source registries from multiple registry.json
files.
 shadcn registry validate for checking source registries before publishing.

 This makes it easier to maintain source and dynamic registries without keeping
one large registry.json file by hand.
 Registry authors can now organize a large source registry across multiple
 registry.json files and compose them with shadcn build .
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
 }
 ]
 }
 Build output #
 shadcn build resolves included registries and writes a flattened
 registry.json without include . Item file paths are preserved from the root
registry, so a file declared in components/ui/registry.json is written as
 components/ui/button.tsx in the built registry item.
 Validate your registry #
 You can now validate a source registry before publishing or serving it.
 pnpm npm yarn bun pnpm dlx shadcn registry validate Copy
 Validation runs against the source registry files directly. You do not need to
run shadcn build first.
 The command checks the root registry.json , included registry files, item
schema errors, duplicate item names, include rules, and local item file paths.
Validation reports all actionable errors it can find in one run.
 Registry loaders #
 The shadcn/registry package also exports loadRegistry and
 loadRegistryItem for dynamic registry routes.
 app/r/registry.json/route.ts Copy import { loadRegistry } from &quot;shadcn/registry&quot;

 export async function GET () {
 const registry = await loadRegistry ()

 return Response. json (registry)
 }
 app/r/[name].json/route.ts Copy import { loadRegistryItem } from &quot;shadcn/registry&quot;

 export async function GET (
 _ : Request ,
 { params } : { params : Promise &lt;{ name : string }&gt; }
 ) {
 const { name } = await params
 const item = await loadRegistryItem (name)

 return Response. json (item)
 }
 See the registry.json documentation and
 getting started guide
for more details. May 2026 - Package Imports and Target Aliases We&#x27;ve added support for package imports and aliases in files.target in shadcn@4.7.0 .
 Package imports #
 The shadcn CLI now supports package.json#imports for installing components,
rewriting imports, and resolving third-party registries. You can use private
 #... import aliases from your package.json instead of relying only on
 compilerOptions.paths in tsconfig.json .
 package.json Copy {
 &quot;imports&quot; : {
 &quot;#components/*&quot; : &quot;./src/components/*.tsx&quot; ,
 &quot;#lib/*&quot; : &quot;./src/lib/*.ts&quot; ,
 &quot;#hooks/*&quot; : &quot;./src/hooks/*.ts&quot;
 }
 }
 Then use the same roots in components.json :
 components.json Copy {
 &quot;aliases&quot; : {
 &quot;components&quot; : &quot;#components&quot; ,
 &quot;ui&quot; : &quot;#components/ui&quot; ,
 &quot;lib&quot; : &quot;#lib&quot; ,
 &quot;hooks&quot; : &quot;#hooks&quot; ,
 &quot;utils&quot; : &quot;#lib/utils&quot;
 }
 }
 This also works in monorepos where app-local files use package imports and
shared UI files are imported from workspace package exports.
 See the package imports guide for setup details.
 Target aliases #
 Registry items can now use target aliases in files[].target to install files
under the user&#x27;s configured shadcn directories. For example, the following registry item will install the prompt-input.tsx file under the ui/ai directory.
 example.json Copy {
 &quot;files&quot; : [
 {
 &quot;path&quot; : &quot;registry/default/ai/prompt-input.tsx&quot; ,
 &quot;type&quot; : &quot;registry:ui&quot; ,
 &quot;target&quot; : &quot;@ui/ai/prompt-input.tsx&quot;
 }
 ]
 }
 See the registry examples for
more details. More Updates April 2026 shadcn preset April 2026 Pointer Cursor April 2026 Partial Preset Apply April 2026 Introducing Sera April 2026 shadcn apply April 2026 Component Composition March 2026 Introducing Luma March 2026 shadcn/cli v4 February 2026 Blocks for Radix and Base UI February 2026 Unified Radix UI Package January 2026 RTL Support January 2026 Inline Start and End Styles January 2026 Base UI Documentation December 2025 npx shadcn create October 2025 Registry Directory October 2025 New Components September 2025 Registry Index August 2025 shadcn CLI 3.0 and MCP Server July 2025 Universal Registry Items July 2025 Local File Support June 2025 radix-ui Migration June 2025 Calendar Component May 2025 New Site April 2025 MCP April 2025 shadcn 2.5.0 April 2025 Cross-framework Route Support February 2025 Tailwind v4 February 2025 Updated Registry Schema January 2025 Blocks Community December 2024 Monorepo Support November 2024 Icons October 2024 React 19 October 2024 Sidebar August 2024 npx shadcn init April 2024 Lift Mode March 2024 Introducing Blocks March 2024 Breadcrumb and Input OTP December 2023 New Components July 2023 JavaScript June 2023 New CLI, Styles and more On This Page June 2026 - GitHub Registries May 2026 - shadcn eject May 2026 - Introducing Rhea May 2026 - Registry Include and Validate May 2026 - Package Imports and Target Aliases More Updates Deploy your shadcn/ui app on Vercel Trusted by OpenAI, Sonos, Adobe, and more. Vercel provides tools and infrastructure to deploy apps and features at scale. Deploy Now Deploy to Vercel Built by shadcn at Vercel . The source code is available on GitHub . Get Code
