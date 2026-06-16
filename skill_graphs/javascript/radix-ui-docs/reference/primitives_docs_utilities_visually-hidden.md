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
# Visually Hidden
Hides content from the screen in an accessible way.
## Features
  * Visually hides content while preserving it for assistive technology.

## Component Reference Links
Version: 1.2.5
Size:
[View as Markdown](https://www.radix-ui.com/primitives/docs/utilities/visually-hidden.md)
## [Anatomy](https://www.radix-ui.com/primitives/docs/utilities/visually-hidden#anatomy)
Import the component.

```

import { VisuallyHidden } from "radix-ui";

export default () => <VisuallyHidden.Root />;

```

## [Basic example](https://www.radix-ui.com/primitives/docs/utilities/visually-hidden#basic-example)
Use the visually hidden primitive.

```

import { VisuallyHidden } from "radix-ui";

import { GearIcon } from "@radix-ui/react-icons";

export default () => (

	<button>

		<GearIcon />

		<VisuallyHidden.Root>Settings</VisuallyHidden.Root>

	</button>

);

```

## [API Reference](https://www.radix-ui.com/primitives/docs/utilities/visually-hidden#api-reference)
### [Root](https://www.radix-ui.com/primitives/docs/utilities/visually-hidden#root)
Anything you put inside this component will be hidden from the screen but will be announced by screen readers.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
## [Accessibility](https://www.radix-ui.com/primitives/docs/utilities/visually-hidden#accessibility)
This is useful in certain scenarios as an alternative to traditional labelling with `aria-label` or `aria-labelledby`.
#### Quick nav
  * [Anatomy](https://www.radix-ui.com/primitives/docs/utilities/visually-hidden#anatomy)
  * [Basic example](https://www.radix-ui.com/primitives/docs/utilities/visually-hidden#basic-example)
  * [API Reference](https://www.radix-ui.com/primitives/docs/utilities/visually-hidden#api-reference)
  * [Root](https://www.radix-ui.com/primitives/docs/utilities/visually-hidden#root)
  * [Accessibility](https://www.radix-ui.com/primitives/docs/utilities/visually-hidden#accessibility)

Previous[Slot](https://www.radix-ui.com/primitives/docs/utilities/slot)
