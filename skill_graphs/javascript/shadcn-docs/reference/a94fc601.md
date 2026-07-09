Namespaces - shadcn/ui Toggle Menu Menu Home Docs Components Blocks Charts Directory Create Search documentation... Search... 117k Toggle theme New Sections Introduction Components Installation Theming CLI RTL Skills MCP Server Registry Forms Changelog Components Accordion Alert Alert Dialog Aspect Ratio Avatar Badge Breadcrumb Button Button Group Calendar Card Carousel Chart Checkbox Collapsible Combobox Command Context Menu Data Table Date Picker Dialog Direction Drawer Dropdown Menu Empty Field Hover Card Input Input Group Input OTP Item Kbd Label Menubar Native Select Navigation Menu Pagination Popover Progress Radio Group Resizable Scroll Area Select Separator Sheet Sidebar Skeleton Slider Sonner Spinner Switch Table Tabs Textarea Toast Toggle Toggle Group Tooltip Typography Get Started Installation components.json Package Imports Theming Dark Mode CLI Monorepo Skills JavaScript Figma llms.txt Legacy Docs Forms React Hook Form TanStack Form Formisch Registry Introduction Getting Started GitHub Registries Registry Directory Examples Namespaces Authentication MCP Server Open in v0 API Reference registry.json registry-item.json Namespaces Copy Page Previous Next Configure and use multiple resource registries with namespace support. Namespaced registries let you configure multiple resource sources in one project. This means you can install components, libraries, utilities, AI prompts, configuration files, and other resources from various registries, whether they&#x27;re public, third-party, or your own custom private libraries.
 Table of Contents #

 Overview
 Decentralized Namespace System
 Getting Started
 Registry Naming Convention
 Configuration
 Authentication &amp; Security
 Versioning
 Dependency Resolution
 Built-in Registries
 CLI Commands
 Error Handling
 Creating Your Own Registry
 Example Configurations
 Technical Details
 Best Practices
 Troubleshooting

 Overview #
 Registry namespaces are prefixed with @ and provide a way to organize and reference resources from different sources. Resources can be any type of content: components, libraries, utilities, hooks, AI prompts, configuration files, themes, and more. For example:

 @shadcn/button - UI component from the shadcn registry
 @v0/dashboard - Dashboard component from the v0 registry
 @ai-elements/input - AI prompt input from an AI elements registry
 @acme/auth-utils - Authentication utilities from your company&#x27;s private registry
 @ai/chatbot-rules - AI prompt rules from an AI resources registry
 @themes/dark-mode - Theme configuration from a themes registry

 Decentralized Namespace System #
 We intentionally designed the namespace system to be decentralized. There is a central open source registry index for open source namespaces but you are free to create and use any namespace you want.
 This decentralized approach gives you complete flexibility to organize your resources however makes sense for your organization.
 You can create multiple registries for different purposes:
 components.json Copy {
 &quot;registries&quot; : {
 &quot;@acme-ui&quot; : &quot;https://registry.acme.com/ui/{name}.json&quot; ,
 &quot;@acme-docs&quot; : &quot;https://registry.acme.com/docs/{name}.json&quot; ,
 &quot;@acme-ai&quot; : &quot;https://registry.acme.com/ai/{name}.json&quot; ,
 &quot;@acme-themes&quot; : &quot;https://registry.acme.com/themes/{name}.json&quot; ,
 &quot;@acme-internal&quot; : {
 &quot;url&quot; : &quot;https://internal.acme.com/registry/{name}.json&quot; ,
 &quot;headers&quot; : {
 &quot;Authorization&quot; : &quot;Bearer ${INTERNAL_TOKEN}&quot;
 }
 }
 }
 }
 This allows you to:

 Organize by type : Separate UI components, documentation, AI resources, etc.
 Organize by team : Different teams can maintain their own registries
 Organize by visibility : Public vs. private resources
 Organize by version : Stable vs. experimental registries
 No naming conflicts : Since there&#x27;s no central authority, you don&#x27;t need to worry about namespace collisions

 Examples of Multi-Registry Setups #
 By Resource Type #
 components.json Copy {
 &quot;@components&quot; : &quot;https://cdn.company.com/components/{name}.json&quot; ,
 &quot;@hooks&quot; : &quot;https://cdn.company.com/hooks/{name}.json&quot; ,
 &quot;@utils&quot; : &quot;https://cdn.company.com/utils/{name}.json&quot; ,
 &quot;@prompts&quot; : &quot;https://cdn.company.com/ai-prompts/{name}.json&quot;
 }
 By Team or Department #
 components.json Copy {
 &quot;@design&quot; : &quot;https://create.company.com/registry/{name}.json&quot; ,
 &quot;@engineering&quot; : &quot;https://eng.company.com/registry/{name}.json&quot; ,
 &quot;@marketing&quot; : &quot;https://marketing.company.com/registry/{name}.json&quot;
 }
 By Stability #
 components.json Copy {
 &quot;@stable&quot; : &quot;https://registry.company.com/stable/{name}.json&quot; ,
 &quot;@latest&quot; : &quot;https://registry.company.com/beta/{name}.json&quot; ,
 &quot;@experimental&quot; : &quot;https://registry.company.com/experimental/{name}.json&quot;
 }

 Getting Started #
 Installing Resources #
 Once configured, you can install resources using the namespace syntax:
 pnpm npm yarn bun pnpm dlx shadcn@latest add @v0/dashboard Copy
 or multiple resources at once:
 pnpm npm yarn bun pnpm dlx shadcn@latest add @acme/header @lib/auth-utils @ai/chatbot-rules Copy
 Quick Configuration #
 Add registries to your components.json :
 components.json Copy {
 &quot;registries&quot; : {
 &quot;@v0&quot; : &quot;https://v0.dev/chat/b/{name}&quot; ,
 &quot;@acme&quot; : &quot;https://registry.acme.com/resources/{name}.json&quot;
 }
 }
 Then start installing:
 pnpm npm yarn bun pnpm dlx shadcn@latest add @acme/button Copy

 Registry Naming Convention #
 Registry names must follow these rules:

 Start with @ symbol
 Contain only alphanumeric characters, hyphens, and underscores
 Examples of valid names: @v0 , @acme-ui , @my_company

 The pattern for referencing resources is: @namespace/resource-name

 GitHub and Namespaces #
 GitHub registry addresses and namespaces solve different problems.
 Use a GitHub address when the registry is a public GitHub repository and you
want users to install without configuring components.json .
 pnpm npm yarn bun pnpm dlx shadcn@latest add acme/ui/button Copy
 Use a namespace when you want a stable alias, custom hosting, authentication,
request headers, query parameters or private registry support.
 pnpm npm yarn bun pnpm dlx shadcn@latest add @acme/button Copy
 See the GitHub registry docs for more information.

 Configuration #
 Namespaced registries are configured in your components.json file under the registries field.
 Basic Configuration #
 The simplest way to configure a registry is with a URL template string:
 components.json Copy {
 &quot;registries&quot; : {
 &quot;@v0&quot; : &quot;https://v0.dev/chat/b/{name}&quot; ,
 &quot;@acme&quot; : &quot;https://registry.acme.com/resources/{name}.json&quot; ,
 &quot;@lib&quot; : &quot;https://lib.company.com/utilities/{name}&quot; ,
 &quot;@ai&quot; : &quot;https://ai-resources.com/r/{name}.json&quot;
 }
 }

 Note: The {name} placeholder in the URL is automatically parsed and replaced with the resource name when you run npx shadcn@latest add @namespace/resource-name . For example, @acme/button becomes https://registry.acme.com/resources/button.json . See URL Pattern System for more details.

 Advanced Configuration #
 For registries that require authentication or additional parameters, use the object format:
 components.json Copy {
 &quot;registries&quot; : {
 &quot;@private&quot; : {
 &quot;url&quot; : &quot;https://api.company.com/registry/{name}.json&quot; ,
 &quot;headers&quot; : {
 &quot;Authorization&quot; : &quot;Bearer ${REGISTRY_TOKEN}&quot; ,
 &quot;X-API-Key&quot; : &quot;${API_KEY}&quot;
 },
 &quot;params&quot; : {
 &quot;version&quot; : &quot;latest&quot; ,
 &quot;format&quot; : &quot;json&quot;
 }
 }
 }
 }

 Note: Environment variables in the format ${VAR_NAME} are automatically expanded from your environment (process.env). This works in URLs, headers, and params. For example, ${REGISTRY_TOKEN} will be replaced with the value of process.env.REGISTRY_TOKEN . See Authentication &amp; Security for more details on using environment variables.

 URL Pattern System #
 Registry URLs support the following placeholders:
 {name} Placeholder (required) #
 The {name} placeholder is replaced with the resource name:
 components.json Copy {
 &quot;@acme&quot; : &quot;https://registry.acme.com/{name}.json&quot;
 }
 When installing @acme/button , the URL becomes: https://registry.acme.com/button.json
When installing @acme/auth-utils , the URL becomes: https://registry.acme.com/auth-utils.json
 {style} Placeholder (optional) #
 The {style} placeholder is replaced with the current style configuration:
 Copy {
 &quot;@themes&quot; : &quot;https://registry.example.com/{style}/{name}.json&quot;
 }
 With style set to new-york , installing @themes/card resolves to: https://registry.example.com/new-york/card.json
 The style placeholder is optional. Use this when you want to serve different versions of the same resource. For example, you can serve a different version of a component for each style.

 Authentication &amp; Security #
 Environment Variables #
 Use environment variables to securely store credentials:
 components.json Copy {
 &quot;registries&quot; : {
 &quot;@private&quot; : {
 &quot;url&quot; : &quot;https://api.company.com/registry/{name}.json&quot; ,
 &quot;headers&quot; : {
 &quot;Authorization&quot; : &quot;Bearer ${REGISTRY_TOKEN}&quot;
 }
 }
 }
 }
 Then set the environment variable:
 .env.local Copy REGISTRY_TOKEN = your_secret_token_here
 Authentication Methods #
 Bearer Token (OAuth 2.0) #
 Copy {
 &quot;@github&quot; : {
 &quot;url&quot; : &quot;https://api.github.com/repos/org/registry/contents/{name}.json&quot; ,
 &quot;headers&quot; : {
 &quot;Authorization&quot; : &quot;Bearer ${GITHUB_TOKEN}&quot;
 }
 }
 }
 API Key in Headers #
 components.json Copy {
 &quot;@private&quot; : {
 &quot;url&quot; : &quot;https://api.company.com/registry/{name}&quot; ,
 &quot;headers&quot; : {
 &quot;X-API-Key&quot; : &quot;${API_KEY}&quot;
 }
 }
 }
 Basic Authentication #
 components.json Copy {
 &quot;@internal&quot; : {
 &quot;url&quot; : &quot;https://registry.company.com/{name}.json&quot; ,
 &quot;headers&quot; : {
 &quot;Authorization&quot; : &quot;Basic ${BASE64_CREDENTIALS}&quot;
 }
 }
 }
 Query Parameter Authentication #
 components.json Copy {
 &quot;@secure&quot; : {
 &quot;url&quot; : &quot;https://registry.example.com/{name}.json&quot; ,
 &quot;params&quot; : {
 &quot;api_key&quot; : &quot;${API_KEY}&quot; ,
 &quot;client_id&quot; : &quot;${CLIENT_ID}&quot; ,
 &quot;signature&quot; : &quot;${REQUEST_SIGNATURE}&quot;
 }
 }
 }
 Multiple Authentication Methods #
 Some registries require multiple authentication methods:
 components.json Copy {
 &quot;@enterprise&quot; : {
 &quot;url&quot; : &quot;https://api.enterprise.com/v2/registry/{name}&quot; ,
 &quot;headers&quot; : {
 &quot;Authorization&quot; : &quot;Bearer ${ACCESS_TOKEN}&quot; ,
 &quot;X-API-Key&quot; : &quot;${API_KEY}&quot; ,
 &quot;X-Workspace-Id&quot; : &quot;${WORKSPACE_ID}&quot;
 },
 &quot;params&quot; : {
 &quot;version&quot; : &quot;latest&quot;
 }
 }
 }
 Security Considerations #
 When working with namespaced registries, especially third-party or public ones, security is paramount. Here&#x27;s how we handle security:
 Resource Validation #
 All resources fetched from registries are validated against our registry item schema before installation. This ensures:

 Structure validation : Resources must conform to the expected JSON schema
 Type safety : Resource types are validated ( registry:ui , registry:lib , etc.)
 No arbitrary code execution : Resources are data files, not executable scripts

 Environment Variable Security #
 Environment variables used for authentication are:

 Never logged : The CLI never logs or displays environment variable values
 Expanded at runtime : Variables are only expanded when needed, not stored
 Isolated per registry : Each registry maintains its own authentication context

 Example of secure configuration:
 components.json Copy {
 &quot;registries&quot; : {
 &quot;@private&quot; : {
 &quot;url&quot; : &quot;https://api.company.com/registry/{name}.json&quot; ,
 &quot;headers&quot; : {
 &quot;Authorization&quot; : &quot;Bearer ${PRIVATE_REGISTRY_TOKEN}&quot;
 }
 }
 }
 }
 Never commit actual tokens to version control. Use .env.local :
 .env.local Copy PRIVATE_REGISTRY_TOKEN = actual_token_here
 HTTPS Enforcement #
 We strongly recommend using HTTPS for all registry URLs:

 Encrypted transport : Prevents man-in-the-middle attacks
 Certificate validation : Ensures you&#x27;re connecting to the legitimate registry
 Credential protection : Headers and tokens are encrypted in transit

 components.json Copy {
 &quot;registries&quot; : {
 &quot;@secure&quot; : &quot;https://registry.example.com/{name}.json&quot; , // ✅ Good
 &quot;@insecure&quot; : &quot;http://registry.example.com/{name}.json&quot; // ❌ Avoid
 }
 }
 Content Security #
 Resources from registries are treated as data, not code:

 JSON parsing only : Resources must be valid JSON
 Schema validation : Must match the registry item schema
 File path restrictions : Files can only be written to configured paths
 No script execution : The CLI doesn&#x27;t execute any code from registry resources

 Registry Trust Model #
 The namespace system operates on a trust model:

 You trust what you install : Only add registries you trust to your configuration
 Explicit configuration : Registries must be explicitly configured in components.json
 No automatic registry discovery : The CLI never automatically adds registries
 Dependency transparency : All dependencies are clearly listed in registry items

 Best Practices for Registry Operators #
 If you&#x27;re running your own registry:

 Use HTTPS always : Never serve registry content over HTTP
 Implement authentication : Require API keys or tokens for private registries
 Rate limiting : Protect your registry from abuse
 Content validation : Validate resources before serving them

 Example secure registry setup:
 components.json Copy {
 &quot;@company&quot; : {
 &quot;url&quot; : &quot;https://registry.company.com/v1/{name}.json&quot; ,
 &quot;headers&quot; : {
 &quot;Authorization&quot; : &quot;Bearer ${COMPANY_TOKEN}&quot; ,
 &quot;X-Registry-Version&quot; : &quot;1.0&quot;
 }
 }
 }
 Inspecting Resources Before Installation #
 The CLI provides transparency about what&#x27;s being installed. You can see the payload of a registry item using the following command:
 pnpm npm yarn bun pnpm dlx shadcn@latest view @acme/button Copy
 This will output the payload of the registry item to the console.

 Dependency Resolution #
 Basic Dependency Resolution #
 Resources can have dependencies across different registries:
 registry-item.json Copy {
 &quot;name&quot; : &quot;dashboard&quot; ,
 &quot;type&quot; : &quot;registry:block&quot; ,
 &quot;registryDependencies&quot; : [
 &quot;@shadcn/card&quot; , // From default registry
 &quot;@v0/chart&quot; , // From v0 registry
 &quot;@acme/data-table&quot; , // From acme registry
 &quot;@lib/data-fetcher&quot; , // Utility library
 &quot;@ai/analytics-prompt&quot; // AI prompt resource
 ]
 }
 The CLI automatically resolves and installs all dependencies from their respective registries.
 Advanced Dependency Resolution #
 Understanding how dependencies are resolved internally is important if you&#x27;re developing registries or need to customize third-party resources.
 How Resolution Works #
 When you run npx shadcn@latest add @namespace/resource , the CLI does the following:

 Clears registry context to start fresh
 Fetches the main resource from the specified registry
 Recursively resolves dependencies from their respective registries
 Applies topological sorting to ensure proper installation order
 Deduplicates files based on target paths (last one wins)
 Deep merges configurations (tailwind, cssVars, css, envVars)

 This means that if you run the following command:
 pnpm npm yarn bun pnpm dlx shadcn@latest add @acme/auth @custom/login-form Copy
 The login-form.ts from @custom/login-form will override the login-form.ts from @acme/auth because it&#x27;s resolved last.
 Overriding Third-Party Resources #
 You can leverage the dependency resolution process to override any third-party resource by adding them to your custom resource under registryDependencies and overriding with your own custom values.
 Example: Customizing a Third-Party Button #
 Let&#x27;s say you want to customize a button from a vendor registry:
 1. Original vendor button ( @vendor/button ):
 button.json Copy {
 &quot;name&quot; : &quot;button&quot; ,
 &quot;type&quot; : &quot;registry:ui&quot; ,
 &quot;files&quot; : [
 {
 &quot;path&quot; : &quot;components/ui/button.tsx&quot; ,
 &quot;type&quot; : &quot;registry:ui&quot; ,
 &quot;content&quot; : &quot;// Vendor&#x27;s button implementation \n export function Button() { ... }&quot;
 }
 ],
 &quot;cssVars&quot; : {
 &quot;light&quot; : {
 &quot;--button-bg&quot; : &quot;blue&quot;
 }
 }
 }
 2. Create your custom override ( @my-company/custom-button ):
 custom-button.json Copy {
 &quot;name&quot; : &quot;custom-button&quot; ,
 &quot;type&quot; : &quot;registry:ui&quot; ,
 &quot;registryDependencies&quot; : [
 &quot;@vendor/button&quot; // Import original first
 ],
 &quot;cssVars&quot; : {
 &quot;light&quot; : {
 &quot;--button-bg&quot; : &quot;purple&quot; // Override the color
 }
 }
 }
 3. Install your custom version :
 pnpm npm yarn bun pnpm dlx shadcn@latest add @my-company/custom-button Copy
 This installs the original button from @vendor/button and then overrides the cssVars with your own custom values.
 Advanced Override Patterns #
 Extending Without Replacing #
 Keep the original and add extensions:
 extended-table.json Copy {
 &quot;name&quot; : &quot;extended-table&quot; ,
 &quot;registryDependencies&quot; : [ &quot;@vendor/table&quot; ],
 &quot;files&quot; : [
 {
 &quot;path&quot; : &quot;components/ui/table-extended.tsx&quot; ,
 &quot;content&quot; : &quot;import { Table } from &#x27;@vendor/table&#x27; \n // Add your extensions \n export function ExtendedTable() { ... }&quot;
 }
 ]
 }
 This will install the original table from @vendor/table and then add your extensions to components/ui/table-extended.tsx .
 Partial Override (Multi-file Resources) #
 Override only specific files from a complex component:
 custom-auth.json Copy {
 &quot;name&quot; : &quot;custom-auth&quot; ,
 &quot;registryDependencies&quot; : [
 &quot;@vendor/auth&quot; // Has multiple files
 ],
 &quot;files&quot; : [
 {
 &quot;path&quot; : &quot;lib/auth-server.ts&quot; ,
 &quot;type&quot; : &quot;registry:lib&quot; ,
 &quot;content&quot; : &quot;// Your custom auth server&quot;
 }
 ]
 }
 Resolution Order Example #
 When you install @custom/dashboard that depends on multiple resources:
 dashboard.json Copy {
 &quot;name&quot; : &quot;dashboard&quot; ,
 &quot;registryDependencies&quot; : [
 &quot;@shadcn/card&quot; , // 1. Resolved first
 &quot;@vendor/chart&quot; , // 2. Resolved second
 &quot;@custom/card&quot; // 3. Resolved last (overrides @shadcn/card)
 ]
 }
 Resolution order:

 @shadcn/card - installs to components/ui/card.tsx
 @vendor/chart - installs to components/ui/chart.tsx
 @custom/card - overwrites components/ui/card.tsx (if same target)

 Key Resolution Features #

 Source Tracking : Each resource knows which registry it came from, avoiding naming conflicts
 Circular Dependency Prevention : Automatically detects and prevents circular dependencies
 Smart Installation Order : Dependencies are installed first, then the resources that use them

 Versioning #
 You can implement versioning for your registry resources using query parameters. This allows users to pin specific versions or use different release channels.
 Basic Version Parameter #
 components.json Copy {
 &quot;@versioned&quot; : {
 &quot;url&quot; : &quot;https://registry.example.com/{name}&quot; ,
 &quot;params&quot; : {
 &quot;version&quot; : &quot;v2&quot;
 }
 }
 }
 This resolves @versioned/button to: https://registry.example.com/button?version=v2
 Dynamic Version Selection #
 Use environment variables to control versions across your project:
 components.json Copy {
 &quot;@stable&quot; : {
 &quot;url&quot; : &quot;https://registry.company.com/{name}&quot; ,
 &quot;params&quot; : {
 &quot;version&quot; : &quot;${REGISTRY_VERSION}&quot;
 }
 }
 }
 This allows you to:

 Set REGISTRY_VERSION=v1.2.3 in production
 Override per environment (dev, staging, prod)

 Semantic Versioning #
 Implement semantic versioning with range support:
 components.json Copy {
 &quot;@npm-style&quot; : {
 &quot;url&quot; : &quot;https://registry.example.com/{name}&quot; ,
 &quot;params&quot; : {
 &quot;semver&quot; : &quot;^2.0.0&quot; ,
 &quot;prerelease&quot; : &quot;${ALLOW_PRERELEASE}&quot;
 }
 }
 }
 Version Resolution Best Practices #

 Use environment variables for version control across environments
 Provide sensible defaults using the ${VAR:-default} syntax
 Document version schemes clearly for registry users
 Support version pinning for reproducible builds
 Implement version discovery endpoints (e.g., /versions/{name} )
 Cache versioned resources appropriately with proper cache headers

 CLI Commands #
 The shadcn CLI provides several commands for working with namespaced registries:
 Adding Resources #
 Install resources from any configured registry:
 Copy # Install from a specific registry
 npx shadcn@latest add @v0/dashboard

 # Install multiple resources
 npx shadcn@latest add @acme/button @lib/utils @ai/prompt

 # Install from URL directly
 npx shadcn@latest add https://registry.example.com/button.json

 # Install from local file
 npx shadcn@latest add ./local-registry/button.json
 Viewing Resources #
 Inspect registry items before installation:
 Copy # View a resource from a registry
 npx shadcn@latest view @acme/button

 # View multiple resources
 npx shadcn@latest view @v0/dashboard @shadcn/card

 # View from URL
 npx shadcn@latest view https://registry.example.com/button.json
 The view command displays:

 Resource metadata (name, type, description)
 Dependencies and registry dependencies
 File contents that will be installed
 CSS variables and Tailwind configuration
 Required environment variables

 Searching Registries #
 Search for available resources in registries:
 Copy # Search a specific registry
 npx shadcn@latest search @v0

 # Search with query
 npx shadcn@latest search @acme --query &quot;auth&quot;

 # Search multiple registries
 npx shadcn@latest search @v0 @acme @lib

 # Limit results
 npx shadcn@latest search @v0 --limit 10 --offset 20

 # List all items (alias for search)
 npx shadcn@latest list @acme
 Search results include:

 Resource name and type
 Description
 Registry source

 Error Handling #
 Registry Not Configured #
 If you reference a registry that isn&#x27;t configured:
 pnpm npm yarn bun pnpm dlx shadcn@latest add @non-existent/component Copy
 Error:
 Copy Unknown registry &quot;@non-existent&quot;. Make sure it is defined in components.json as follows:
 {
 &quot;registries&quot;: {
 &quot;@non-existent&quot;: &quot;[URL_TO_REGISTRY]&quot;
 }
 }
 Missing Environment Variables #
 If required environment variables are not set:
 Copy Registry &quot;@private&quot; requires the following environment variables:

 • REGISTRY_TOKEN

 Set the required environment variables to your .env or .env.local file.
 Resource Not Found #
 404 Not Found:
 Copy The item at https://registry.company.com/button.json was not found. It may not exist at the registry.
 This usually means:

 The resource name is misspelled
 The resource doesn&#x27;t exist in the registry
 The registry URL pattern is incorrect

 Authentication Failures #
 401 Unauthorized:
 Copy You are not authorized to access the item at https://api.company.com/button.json
 Check your authentication credentials and environment variables.
 403 Forbidden:
 Copy Access forbidden for https://api.company.com/button.json
 Verify your API key has the necessary permissions.

 Creating Your Own Registry #
 To make your registry compatible with the namespace system, you can serve any type of resource - components, libraries, utilities, AI prompts, themes, configurations, or any other shareable code/content:

 Implement the registry item schema : Your registry must return JSON that conforms to the registry item schema .

 Support the URL pattern : Include {name} in your URL template where the resource name will be inserted.

 Define resource types : Use appropriate type fields to identify your resources (e.g., registry:ui , registry:lib , registry:ai , registry:theme , etc.).

 Handle authentication (if needed): Accept authentication via headers or query parameters.

 Document your namespace : Provide clear instructions for users to configure your registry:

 components.json Copy {
 &quot;registries&quot; : {
 &quot;@your-registry&quot; : &quot;https://your-domain.com/r/{name}.json&quot;
 }
 }

 Technical Details #
 Parser Pattern #
 The namespace parser uses the following regex pattern:
 namespace-parser.js Copy / ^( @ [ a-zA-Z0-9 ](?:[ a-zA-Z0-9-_ ] * [ a-zA-Z0-9 ]) ? ) \/ (. + )$ /
 This ensures valid namespace formatting and proper component name extraction.
 Resolution Process #

 Parse : Extract namespace and component name from @namespace/component
 Lookup : Find registry configuration for @namespace
 Build URL : Replace placeholders with actual values
 Set Headers : Apply authentication headers if configured
 Fetch : Retrieve component from the resolved URL
 Validate : Ensure response matches registry item schema
 Resolve Dependencies : Recursively fetch any registry dependencies

 Cross-Registry Dependencies #
 When a component has dependencies from different registries, the resolver:

 Maintains separate authentication contexts for each registry
 Resolves each dependency from its respective source
 Deduplicates files based on target paths
 Merges configurations (tailwind, cssVars, etc.) from all sources

 Best Practices #

 Use environment variables for sensitive data like API keys and tokens
 Namespace your registry with a unique, descriptive name
 Document authentication requirements clearly for users
 Implement proper error responses with helpful messages
 Cache registry responses when possible to improve performance
 Support style variants if your components have multiple themes

 Troubleshooting #
 Resources not found #

 Verify the registry URL is correct and accessible
 Check that the {name} placeholder is included in the URL
 Ensure the resource exists in the registry
 Confirm the resource type matches what the registry provides

 Authentication issues #

 Confirm environment variables are set correctly
 Verify API keys/tokens are valid and not expired
 Check that headers are being sent in the correct format

 Dependency conflicts #

 Review resources with the same name from different registries
 Use fully qualified names ( @namespace/resource ) to avoid ambiguity
 Check for circular dependencies between registries
 Ensure resource types are compatible when mixing registries
 Examples Authentication On This Page Table of Contents Overview Decentralized Namespace System Examples of Multi-Registry Setups By Resource Type By Team or Department By Stability Getting Started Installing Resources Quick Configuration Registry Naming Convention GitHub and Namespaces Configuration Basic Configuration Advanced Configuration URL Pattern System {name} Placeholder (required) {style} Placeholder (optional) Authentication &amp; Security Environment Variables Authentication Methods Bearer Token (OAuth 2.0) API Key in Headers Basic Authentication Query Parameter Authentication Multiple Authentication Methods Security Considerations Resource Validation Environment Variable Security HTTPS Enforcement Content Security Registry Trust Model Best Practices for Registry Operators Inspecting Resources Before Installation Dependency Resolution Basic Dependency Resolution Advanced Dependency Resolution How Resolution Works Overriding Third-Party Resources Example: Customizing a Third-Party Button Advanced Override Patterns Extending Without Replacing Partial Override (Multi-file Resources) Resolution Order Example Key Resolution Features Versioning Basic Version Parameter Dynamic Version Selection Semantic Versioning Version Resolution Best Practices CLI Commands Adding Resources Viewing Resources Searching Registries Error Handling Registry Not Configured Missing Environment Variables Resource Not Found Authentication Failures Creating Your Own Registry Technical Details Parser Pattern Resolution Process Cross-Registry Dependencies Best Practices Troubleshooting Resources not found Authentication issues Dependency conflicts Deploy your shadcn/ui app on Vercel Trusted by OpenAI, Sonos, Adobe, and more. Vercel provides tools and infrastructure to deploy apps and features at scale. Deploy Now Deploy to Vercel Built by shadcn at Vercel . The source code is available on GitHub . Get Code
