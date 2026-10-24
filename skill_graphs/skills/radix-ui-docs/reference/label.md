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
Components
# Label
Renders an accessible label associated with controls.
First name
index.jsxindex.jsxstyles.cssstyles.css
CSS

```

import * as React from "react";

import { Label } from "radix-ui";

import "./styles.css";

const LabelDemo = () => (

	<div
		style={{
			display: "flex",
			padding: "0 20px",
			flexWrap: "wrap",
			gap: 15,
			alignItems: "center",
		}}
	>

		<Label.Root className="LabelRoot" htmlFor="firstName">

			First name

		</Label.Root>

		<input
			className="Input"
			type="text"
			id="firstName"
			defaultValue="Pedro Duarte"
		/>

	</div>

);

export default LabelDemo;

Expand code

```

## Features
  * Text selection is prevented when double clicking label.
  * Supports nested controls.

## Component Reference Links
Version: 2.1.9
Size:
[View as Markdown](https://www.radix-ui.com/primitives/docs/components/label.md)
## [Anatomy](https://www.radix-ui.com/primitives/docs/components/label#anatomy)
Import the component.

```

import { Label } from "radix-ui";

export default () => <Label.Root />;

```

## [API Reference](https://www.radix-ui.com/primitives/docs/components/label#api-reference)
### [Root](https://www.radix-ui.com/primitives/docs/components/label#root)
Contains the content for the label.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
|  `htmlFor` Prop description  | `string`  | No default value  |
## [Accessibility](https://www.radix-ui.com/primitives/docs/components/label#accessibility)
This component is based on the native `label` element, it will automatically apply the correct labelling when wrapping controls or using the `htmlFor` attribute. For your own custom controls to work correctly, ensure they use native elements such as `button` or `input` as a base.
#### Quick nav
  * [Anatomy](https://www.radix-ui.com/primitives/docs/components/label#anatomy)
  * [API Reference](https://www.radix-ui.com/primitives/docs/components/label#api-reference)
  * [Root](https://www.radix-ui.com/primitives/docs/components/label#root)
  * [Accessibility](https://www.radix-ui.com/primitives/docs/components/label#accessibility)

Previous[Hover Card](https://www.radix-ui.com/primitives/docs/components/hover-card)
Next[Menubar](https://www.radix-ui.com/primitives/docs/components/menubar)
