[Radix Homepage](https://www.radix-ui.com/)
[Radix Homepage](https://www.radix-ui.com/)
[ThemesThemes](https://www.radix-ui.com/)[PrimitivesPrimitives](https://www.radix-ui.com/primitives)[IconsIcons](https://www.radix-ui.com/icons)[ColorsColors](https://www.radix-ui.com/colors)
[Documentation](https://www.radix-ui.com/primitives/docs)[Case studies](https://www.radix-ui.com/primitives/case-studies)[Blog](https://www.radix-ui.com/blog)
`/`
#### Overview
[Introduction](https://www.radix-ui.com/primitives/docs/overview/introduction)[Getting started](https://www.radix-ui.com/primitives/docs/overview/getting-started)[Accessibility](https://www.radix-ui.com/primitives/docs/overview/accessibility)[Releases](https://www.radix-ui.com/primitives/docs/overview/releases)
#### Guides
[Styling](https://www.radix-ui.com/primitives/docs/guides/styling)[Animation](https://www.radix-ui.com/primitives/docs/guides/animation)[Composition](https://www.radix-ui.com/primitives/docs/guides/composition)[Server-side rendering](https://www.radix-ui.com/primitives/docs/guides/server-side-rendering)
#### Components
[Accordion](https://www.radix-ui.com/primitives/docs/components/accordion)[Alert Dialog](https://www.radix-ui.com/primitives/docs/components/alert-dialog)[Aspect Ratio](https://www.radix-ui.com/primitives/docs/components/aspect-ratio)[Avatar](https://www.radix-ui.com/primitives/docs/components/avatar)[Checkbox](https://www.radix-ui.com/primitives/docs/components/checkbox)[Collapsible](https://www.radix-ui.com/primitives/docs/components/collapsible)[Context Menu](https://www.radix-ui.com/primitives/docs/components/context-menu)[Dialog](https://www.radix-ui.com/primitives/docs/components/dialog)[Dropdown Menu](https://www.radix-ui.com/primitives/docs/components/dropdown-menu)[Form Preview](https://www.radix-ui.com/primitives/docs/components/form)[Hover Card](https://www.radix-ui.com/primitives/docs/components/hover-card)[Label](https://www.radix-ui.com/primitives/docs/components/label)[Menubar](https://www.radix-ui.com/primitives/docs/components/menubar)[Navigation Menu](https://www.radix-ui.com/primitives/docs/components/navigation-menu)[One-Time Password Field Preview](https://www.radix-ui.com/primitives/docs/components/one-time-password-field)[Password Toggle Field Preview](https://www.radix-ui.com/primitives/docs/components/password-toggle-field)[Popover](https://www.radix-ui.com/primitives/docs/components/popover)[Progress](https://www.radix-ui.com/primitives/docs/components/progress)[Radio Group](https://www.radix-ui.com/primitives/docs/components/radio-group)[Scroll Area](https://www.radix-ui.com/primitives/docs/components/scroll-area)[Select](https://www.radix-ui.com/primitives/docs/components/select)[Separator](https://www.radix-ui.com/primitives/docs/components/separator)[Slider](https://www.radix-ui.com/primitives/docs/components/slider)[Switch](https://www.radix-ui.com/primitives/docs/components/switch)[Tabs](https://www.radix-ui.com/primitives/docs/components/tabs)[Toast](https://www.radix-ui.com/primitives/docs/components/toast)[Toggle](https://www.radix-ui.com/primitives/docs/components/toggle)[Toggle Group](https://www.radix-ui.com/primitives/docs/components/toggle-group)[Toolbar](https://www.radix-ui.com/primitives/docs/components/toolbar)[Tooltip](https://www.radix-ui.com/primitives/docs/components/tooltip)
#### Utilities
[Accessible Icon](https://www.radix-ui.com/primitives/docs/utilities/accessible-icon)[Direction Provider](https://www.radix-ui.com/primitives/docs/utilities/direction-provider)[Portal](https://www.radix-ui.com/primitives/docs/utilities/portal)[Slot](https://www.radix-ui.com/primitives/docs/utilities/slot)[Visually Hidden](https://www.radix-ui.com/primitives/docs/utilities/visually-hidden)
Overview
# Introduction
An open-source UI component library for building high-quality, accessible design systems and web apps.
Radix Primitives is a low-level UI component library with a focus on accessibility, customization and developer experience. You can use these components either as the base layer of your design system, or adopt them incrementally.
## [Vision](https://www.radix-ui.com/primitives/docs/overview/introduction#vision)
Most of us share similar definitions for common UI patterns like accordion, checkbox, combobox, dialog, dropdown, select, slider, and tooltip. These UI patterns are
However, the implementations provided to us by the web platform are inadequate. They're either non-existent, lacking in functionality, or cannot be customized sufficiently.
So, developers are forced to build custom components; an incredibly difficult task. As a result, most components on the web are inaccessible, non-performant, and lacking important features.
Our goal is to create a well-funded, open-source component library that the community can use to build accessible design systems.
## [Key Features](https://www.radix-ui.com/primitives/docs/overview/introduction#key-features)
### [Accessible](https://www.radix-ui.com/primitives/docs/overview/introduction#accessible)
Components adhere to the [accessibility](https://www.radix-ui.com/primitives/docs/overview/accessibility) overview.
### [Unstyled](https://www.radix-ui.com/primitives/docs/overview/introduction#unstyled)
Components ship without styles, giving you complete control over the look and feel. Components can be styled with any styling solution. Learn more in our [styling](https://www.radix-ui.com/primitives/docs/guides/styling) guide.
### [Opened](https://www.radix-ui.com/primitives/docs/overview/introduction#opened)
Radix Primitives are designed to be customized to suit your needs. Our open component architecture provides you granular access to each component part, so you can wrap them and add your own event listeners, props, or refs.
### [Uncontrolled](https://www.radix-ui.com/primitives/docs/overview/introduction#uncontrolled)
Where applicable, components are uncontrolled by default but can also be controlled, alternatively. All of the behavior wiring is handled internally, so you can get up and running as smoothly as possible, without needing to create any local states.
### [Developer experience](https://www.radix-ui.com/primitives/docs/overview/introduction#developer-experience)
One of our main goals is to provide the best possible developer experience. Radix Primitives provides a fully-typed API. All components share a similar API, creating a consistent and predictable experience. We've also implemented an `asChild` prop, giving users full control over the rendered element.
### [Incremental adoption](https://www.radix-ui.com/primitives/docs/overview/introduction#incremental-adoption)
We recommend installing the `radix-ui` package and importing the primitives you need. This is the simplest way to get started, prevent version conflicts or duplication, and makes it easy to manage updates. The package is tree-shakeable, so you should only ship the components you use.
```


npm install radix-ui


```

```


import { Dialog, DropdownMenu, Tooltip } from "radix-ui";


```

Alternatively, each primitive can be installed individually:
```


npm install @radix-ui/react-dialog




npm install @radix-ui/react-dropdown-menu




npm install @radix-ui/react-tooltip


```

```


import * as Dialog from "@radix-ui/react-dialog";




import * as DropdownMenu from "@radix-ui/react-dropdown-menu";




import * as Tooltip from "@radix-ui/react-tooltip";


```

When installing separately, we recommend updating all Radix packages together to prevent duplication of shared dependencies and keep your bundle size down.
## [Community](https://www.radix-ui.com/primitives/docs/overview/introduction#community)
To get involved with the Radix community, ask questions and share tips,
To receive updates on new primitives, announcements, blog posts, and general Radix tips, follow along on
To file issues, request features, and contribute, check out our GitHub.
#### Quick nav
  * [Vision](https://www.radix-ui.com/primitives/docs/overview/introduction#vision)
  * [Key Features](https://www.radix-ui.com/primitives/docs/overview/introduction#key-features)
  * [Accessible](https://www.radix-ui.com/primitives/docs/overview/introduction#accessible)
  * [Unstyled](https://www.radix-ui.com/primitives/docs/overview/introduction#unstyled)
  * [Opened](https://www.radix-ui.com/primitives/docs/overview/introduction#opened)
  * [Uncontrolled](https://www.radix-ui.com/primitives/docs/overview/introduction#uncontrolled)
  * [Developer experience](https://www.radix-ui.com/primitives/docs/overview/introduction#developer-experience)
  * [Incremental adoption](https://www.radix-ui.com/primitives/docs/overview/introduction#incremental-adoption)
  * [Community](https://www.radix-ui.com/primitives/docs/overview/introduction#community)


Next[Getting started](https://www.radix-ui.com/primitives/docs/overview/getting-started)
