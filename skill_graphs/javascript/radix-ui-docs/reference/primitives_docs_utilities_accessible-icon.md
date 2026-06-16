[Radix Homepage](https://www.radix-ui.com/)
[Radix Homepage](https://www.radix-ui.com/)
[ThemesThemes](https://www.radix-ui.com/)[PrimitivesPrimitives](https://www.radix-ui.com/primitives)[IconsIcons](https://www.radix-ui.com/icons)[ColorsColors](https://www.radix-ui.com/colors)
[Documentation](https://www.radix-ui.com/primitives/docs)[Case studies](https://www.radix-ui.com/primitives/case-studies)[Blog](https://www.radix-ui.com/blog)
Search
`/`
#### Overview
[Introduction](https://www.radix-ui.com/primitives/docs/overview/introduction)[Getting started](https://www.radix-ui.com/primitives/docs/overview/getting-started)[Accessibility](https://www.radix-ui.com/primitives/docs/overview/accessibility)[Releases](https://www.radix-ui.com/primitives/docs/overview/releases)
#### Guides
[Styling](https://www.radix-ui.com/primitives/docs/guides/styling)[Animation](https://www.radix-ui.com/primitives/docs/guides/animation)[Composition](https://www.radix-ui.com/primitives/docs/guides/composition)[Server-side rendering](https://www.radix-ui.com/primitives/docs/guides/server-side-rendering)
#### Components
[Accordion](https://www.radix-ui.com/primitives/docs/components/accordion)[Alert Dialog](https://www.radix-ui.com/primitives/docs/components/alert-dialog)[Aspect Ratio](https://www.radix-ui.com/primitives/docs/components/aspect-ratio)[Avatar](https://www.radix-ui.com/primitives/docs/components/avatar)[Checkbox](https://www.radix-ui.com/primitives/docs/components/checkbox)[Collapsible](https://www.radix-ui.com/primitives/docs/components/collapsible)[Context Menu](https://www.radix-ui.com/primitives/docs/components/context-menu)[Dialog](https://www.radix-ui.com/primitives/docs/components/dialog)[Dropdown Menu](https://www.radix-ui.com/primitives/docs/components/dropdown-menu)[Form Preview](https://www.radix-ui.com/primitives/docs/components/form)[Hover Card](https://www.radix-ui.com/primitives/docs/components/hover-card)[Label](https://www.radix-ui.com/primitives/docs/components/label)[Menubar](https://www.radix-ui.com/primitives/docs/components/menubar)[Navigation Menu](https://www.radix-ui.com/primitives/docs/components/navigation-menu)[One-Time Password Field Preview](https://www.radix-ui.com/primitives/docs/components/one-time-password-field)[Password Toggle Field Preview](https://www.radix-ui.com/primitives/docs/components/password-toggle-field)[Popover](https://www.radix-ui.com/primitives/docs/components/popover)[Progress](https://www.radix-ui.com/primitives/docs/components/progress)[Radio Group](https://www.radix-ui.com/primitives/docs/components/radio-group)[Scroll Area](https://www.radix-ui.com/primitives/docs/components/scroll-area)[Select](https://www.radix-ui.com/primitives/docs/components/select)[Separator](https://www.radix-ui.com/primitives/docs/components/separator)[Slider](https://www.radix-ui.com/primitives/docs/components/slider)[Switch](https://www.radix-ui.com/primitives/docs/components/switch)[Tabs](https://www.radix-ui.com/primitives/docs/components/tabs)[Toast](https://www.radix-ui.com/primitives/docs/components/toast)[Toggle](https://www.radix-ui.com/primitives/docs/components/toggle)[Toggle Group](https://www.radix-ui.com/primitives/docs/components/toggle-group)[Toolbar](https://www.radix-ui.com/primitives/docs/components/toolbar)[Tooltip](https://www.radix-ui.com/primitives/docs/components/tooltip)
#### Utilities
[Accessible Icon](https://www.radix-ui.com/primitives/docs/utilities/accessible-icon)[Direction Provider](https://www.radix-ui.com/primitives/docs/utilities/direction-provider)[Portal](https://www.radix-ui.com/primitives/docs/utilities/portal)[Slot](https://www.radix-ui.com/primitives/docs/utilities/slot)[Visually Hidden](https://www.radix-ui.com/primitives/docs/utilities/visually-hidden)
Utilities
# Accessible Icon
Makes icons accessible by adding a label.
## Features
  * Quickly make any icon accessible by wrapping it and providing a meaningful label.
  * No visual difference, but announced correctly by screen readers.

## Component Reference Links
Version: 1.1.9
Size:
[View as Markdown](https://www.radix-ui.com/primitives/docs/utilities/accessible-icon.md)
## [Anatomy](https://www.radix-ui.com/primitives/docs/utilities/accessible-icon#anatomy)
Import the component.

```

import { AccessibleIcon } from "radix-ui";

export default () => <AccessibleIcon.Root />;

```

## [API Reference](https://www.radix-ui.com/primitives/docs/utilities/accessible-icon#api-reference)
### [Root](https://www.radix-ui.com/primitives/docs/utilities/accessible-icon#root)
Contains the icon to make accessible.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `label*` Prop description  | `string`  | No default value  |
## [Accessibility](https://www.radix-ui.com/primitives/docs/utilities/accessible-icon#accessibility)
Most icons or icon systems come with no accessibility built-in. For example, the same visual **cross** icon may in fact mean **"close"** or **"delete"**. This component lets you give meaning to icons used throughout your app.
This is built with [Visually Hidden](https://www.radix-ui.com/primitives/docs/utilities/visually-hidden).
#### Quick nav
  * [Anatomy](https://www.radix-ui.com/primitives/docs/utilities/accessible-icon#anatomy)
  * [API Reference](https://www.radix-ui.com/primitives/docs/utilities/accessible-icon#api-reference)
  * [Root](https://www.radix-ui.com/primitives/docs/utilities/accessible-icon#root)
  * [Accessibility](https://www.radix-ui.com/primitives/docs/utilities/accessible-icon#accessibility)

Previous[Tooltip](https://www.radix-ui.com/primitives/docs/components/tooltip)
Next[Direction Provider](https://www.radix-ui.com/primitives/docs/utilities/direction-provider)
