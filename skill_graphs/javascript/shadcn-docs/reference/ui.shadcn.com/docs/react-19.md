Next.js 15 + React 19 - shadcn/ui Toggle Menu Menu Home Docs Components Blocks Charts Directory Create Search documentation... Search... 117k Toggle theme New Sections Introduction Components Installation Theming CLI RTL Skills MCP Server Registry Forms Changelog Components Accordion Alert Alert Dialog Aspect Ratio Avatar Badge Breadcrumb Button Button Group Calendar Card Carousel Chart Checkbox Collapsible Combobox Command Context Menu Data Table Date Picker Dialog Direction Drawer Dropdown Menu Empty Field Hover Card Input Input Group Input OTP Item Kbd Label Menubar Native Select Navigation Menu Pagination Popover Progress Radio Group Resizable Scroll Area Select Separator Sheet Sidebar Skeleton Slider Sonner Spinner Switch Table Tabs Textarea Toast Toggle Toggle Group Tooltip Typography Get Started Installation components.json Package Imports Theming Dark Mode CLI Monorepo Skills JavaScript Figma llms.txt Legacy Docs Forms React Hook Form TanStack Form Formisch Registry Introduction Getting Started GitHub Registries Registry Directory Examples Namespaces Authentication MCP Server Open in v0 API Reference registry.json registry-item.json Next.js 15 + React 19 Copy Page Previous Next Using shadcn/ui with Next.js 15 and React 19. Update: We have added full support for React 19 and Tailwind v4 in the
 latest release. This guide might be outdated. Proceed with caution.
 TL;DR #
 If you&#x27;re using npm , you can install shadcn/ui dependencies with a flag. The shadcn CLI will prompt you to select a flag when you run it. No flags required for pnpm, bun, or yarn.
 See Upgrade Status for the status of React 19 support for each package.
 What&#x27;s happening? #
 React 19 is now rc and is tested and supported in the latest Next.js 15 release .
 To support React 19, package maintainers will need to test and update their packages to include React 19 as a peer dependency. This is already in progress .
 Copy &quot;peerDependencies&quot;: {
 - &quot;react&quot;: &quot;^16.8 || ^17.0 || ^18.0&quot;,
 + &quot;react&quot;: &quot;^16.8 || ^17.0 || ^18.0 || ^19.0 &quot;,
 - &quot;react-dom&quot;: &quot;^16.8 || ^17.0 || ^18.0&quot;
 + &quot;react-dom&quot;: &quot;^16.8 || ^17.0 || ^18.0 || ^19.0 &quot;
 },
 You can check if a package lists React 19 as a peer dependency by running
 npm info &lt;package&gt; peerDependencies .
 In the meantime, if you are installing a package that does not list React 19 as a peer dependency, you will see an error message like this:
 Copy npm error code ERESOLVE
 npm error ERESOLVE unable to resolve dependency tree
 npm error
 npm error While resolving: my-app@0.1.0
 npm error Found: react@19.0.0-rc-69d4b800-20241021
 npm error node_modules/react
 npm error react@&quot;19.0.0-rc-69d4b800-20241021&quot; from the root project
 Note: This is npm only. PNPM and Bun will only show a silent warning.
 How to fix this #
 Solution 1: --force or --legacy-peer-deps #
 You can force install a package with the --force or the --legacy-peer-deps flag.
 Copy npm i &lt; packag e &gt; --force

 npm i &lt; packag e &gt; --legacy-peer-deps
 This will install the package and ignore the peer dependency warnings.
 What do the --force and --legacy-peer-deps flag do?
 Solution 2: Use React 18 #
 You can downgrade react and react-dom to version 18, which is compatible with the package you are installing and upgrade when the dependency is updated.
 Copy npm i react@18 react-dom@18
 Whichever solution you choose, make sure you test your app thoroughly to ensure
there are no regressions.
 Using shadcn/ui on Next.js 15 #
 Using pnpm, bun, or yarn #
 Follow the instructions in the installation guide to install shadcn/ui. No flags are needed.
 Using npm #
 When you run npx shadcn@latest init -d , you will be prompted to select an option to resolve the peer dependency issues.
 Copy It looks like you are using React 19.
 Some packages may fail to install due to peer dependency issues (see https://ui.shadcn.com/react-19 ).

 ? How would you like to proceed ? › - Use arrow-keys. Return to submit.
 ❯ Use --force
 Use --legacy-peer-deps
 You can then run the command with the flag you choose.
 Adding components #
 The process for adding components is the same as above. Select a flag to resolve the peer dependency issues.
 Remember to always test your app after installing new dependencies.
 Upgrade Status #
 To make it easy for you to track the progress of the upgrade, here is a table with the React 19 support status for the shadcn/ui dependencies.

 ✅ - Works with React 19 using npm, pnpm, and bun.
 🚧 - Works with React 19 using pnpm and bun. Requires flag for npm. PR is in progress.

 Package Status Note radix-ui ✅ lucide-react ✅ class-variance-authority ✅ Does not list React 19 as a peer dependency. tailwindcss-animate ✅ Does not list React 19 as a peer dependency. embla-carousel-react ✅ recharts ✅ See note below react-hook-form ✅ react-resizable-panels ✅ sonner ✅ react-day-picker ✅ Works with flag for npm. Work to upgrade to v9 in progress. input-otp ✅ vaul ✅ @radix-ui/react-icons ✅ See PR #194 cmdk ✅
 If you have any questions, please open an issue on GitHub.
 Recharts #
 To use recharts with React 19, you will need to override the react-is dependency.
 Add the following to your package.json package.json Copy &quot;overrides&quot; : {
 &quot;react-is&quot; : &quot;^19.0.0-rc-69d4b800-20241021&quot;
 } Note: the react-is version needs to match the version of React 19 you are using. The above is an example. Run npm install --legacy-peer-deps Your project is ready! Tailwind v4 On This Page TL;DR What&#x27;s happening? How to fix this Solution 1: --force or --legacy-peer-deps Solution 2: Use React 18 Using shadcn/ui on Next.js 15 Using pnpm, bun, or yarn Using npm Adding components Upgrade Status Recharts Deploy your shadcn/ui app on Vercel Trusted by OpenAI, Sonos, Adobe, and more. Vercel provides tools and infrastructure to deploy apps and features at scale. Deploy Now Deploy to Vercel Built by shadcn at Vercel . The source code is available on GitHub . Get Code
