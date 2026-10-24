remix/ui/popover
[Overview](https://api.remix.run/api/remix/ui/popover/overview/)
Interfaces
[PopoverContext](https://api.remix.run/api/remix/ui/popover/interface/PopoverContext/)[PopoverHideRequest](https://api.remix.run/api/remix/ui/popover/interface/PopoverHideRequest/)[PopoverProps](https://api.remix.run/api/remix/ui/popover/interface/PopoverProps/)[PopoverSurfaceOptions](https://api.remix.run/api/remix/ui/popover/interface/PopoverSurfaceOptions/)
remix/ui/scroll-lock
[Overview](https://api.remix.run/api/remix/ui/scroll-lock/overview/)
remix/ui/select
[Overview](https://api.remix.run/api/remix/ui/select/overview/)
Types
[SelectOptionProps](https://api.remix.run/api/remix/ui/select/type/SelectOptionProps/)
Interfaces
[SelectContextProps](https://api.remix.run/api/remix/ui/select/interface/SelectContextProps/)[SelectProps](https://api.remix.run/api/remix/ui/select/interface/SelectProps/)
remix/ui/separator
[Overview](https://api.remix.run/api/remix/ui/separator/overview/)
remix/ui/server
[Overview](https://api.remix.run/api/remix/ui/server/overview/)
Interfaces
[RenderToStreamOptions](https://api.remix.run/api/remix/ui/server/interface/RenderToStreamOptions/)[ResolveFrameContext](https://api.remix.run/api/remix/ui/server/interface/ResolveFrameContext/)
Functions
[renderToStream](https://api.remix.run/api/remix/ui/server/function/renderToStream/)[renderToString](https://api.remix.run/api/remix/ui/server/function/renderToString/)
remix/ui/test
[Overview](https://api.remix.run/api/remix/ui/test/overview/)
Interfaces
[RenderOptions](https://api.remix.run/api/remix/ui/test/interface/RenderOptions/)[RenderResult](https://api.remix.run/api/remix/ui/test/interface/RenderResult/)
Functions
[render](https://api.remix.run/api/remix/ui/test/function/render/)
remix/ui/theme
[Overview](https://api.remix.run/api/remix/ui/theme/overview/)
Types
[CreateThemeOptions](https://api.remix.run/api/remix/ui/theme/type/CreateThemeOptions/)[GlyphContract](https://api.remix.run/api/remix/ui/theme/type/GlyphContract/)[ThemeComponent](https://api.remix.run/api/remix/ui/theme/type/ThemeComponent/)[ThemeMix](https://api.remix.run/api/remix/ui/theme/type/ThemeMix/)[ThemeStyleProps](https://api.remix.run/api/remix/ui/theme/type/ThemeStyleProps/)[ThemeUtility](https://api.remix.run/api/remix/ui/theme/type/ThemeUtility/)[ThemeValue](https://api.remix.run/api/remix/ui/theme/type/ThemeValue/)[ThemeValues](https://api.remix.run/api/remix/ui/theme/type/ThemeValues/)[ThemeVars](https://api.remix.run/api/remix/ui/theme/type/ThemeVars/)
# Welcome to Remix 3!
Remix is a batteries-included, ultra-productive, zero-dependency, bundler-free framework, ready for development in a model-first world. Remix 3 is built on the following principles:
  1. **Model-First Development.** AI fundamentally shifts the human-computer interaction model for both user experience and developer workflows. Optimize the source code, documentation, tooling, and abstractions for LLMs. Additionally, develop abstractions for applications to use models in the product itself, not just as a tool to develop it.
  2. **Build on Web APIs.** Sharing abstractions across the stack greatly reduces the amount of context switching, both for humans and machines. Build on the foundation of Web APIs and JavaScript because it is the only full stack ecosystem.
  3. **Religiously Runtime.** Designing for bundlers/compilers/typegen (and any pre-runtime static analysis) leads to poor API design that eventually pollutes the entire system. All packages must be designed with no expectation of static analysis and all tests must run without bundling. Because browsers are involved, --import loaders for simple transformations like TypeScript and JSX are permissible.
  4. **Avoid Dependencies.** Dependencies lock you into somebody else's roadmap. Choose them wisely, wrap them completely, and expect to replace most of them with our own package eventually. The goal is zero.
  5. **Demand Composition.** Abstractions should be single-purpose and replaceable. A composable abstraction is easy to add and remove from an existing program. Every package must be useful and documented independent of any other context. New features should first be attempted as a new package. If impossible, attempt to break up the existing package to make it more composable. However, tightly coupled modules that almost always change together in both directions should be moved to the same package.
  6. **Distribute Cohesively.** Extremely composable ecosystems are difficult to learn and use. Remix will be distributed as a single remix package for both distribution and documentation.

docs and examples licensed under mit©2026 Shopify, Inc.
