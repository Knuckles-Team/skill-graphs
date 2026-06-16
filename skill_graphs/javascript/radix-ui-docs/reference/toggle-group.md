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
# Toggle Group
A set of two-state buttons that can be toggled on or off.
index.jsxindex.jsxstyles.cssstyles.css
CSS

```

import * as React from "react";

import { ToggleGroup } from "radix-ui";

import {
	TextAlignLeftIcon,
	TextAlignCenterIcon,
	TextAlignRightIcon,
} from "@radix-ui/react-icons";

import "./styles.css";

const ToggleGroupDemo = () => (

	<ToggleGroup.Root
		className="ToggleGroup"
		type="single"
		defaultValue="center"
		aria-label="Text alignment"
	>

		<ToggleGroup.Item
			className="ToggleGroupItem"
			value="left"
			aria-label="Left aligned"
		>

			<TextAlignLeftIcon />

		</ToggleGroup.Item>

		<ToggleGroup.Item
			className="ToggleGroupItem"
			value="center"
			aria-label="Center aligned"
		>

			<TextAlignCenterIcon />

		</ToggleGroup.Item>

		<ToggleGroup.Item
			className="ToggleGroupItem"
			value="right"
			aria-label="Right aligned"
		>

			<TextAlignRightIcon />

		</ToggleGroup.Item>

	</ToggleGroup.Root>

);

export default ToggleGroupDemo;

Expand code

```

## Features
  * Full keyboard navigation.
  * Supports horizontal/vertical orientation.
  * Support single and multiple pressed buttons.
  * Can be controlled or uncontrolled.

## Component Reference Links
Version: 1.1.12
Size:
[View as Markdown](https://www.radix-ui.com/primitives/docs/components/toggle-group.md)
## [Anatomy](https://www.radix-ui.com/primitives/docs/components/toggle-group#anatomy)
Import the component.

```

import { ToggleGroup } from "radix-ui";

export default () => (

	<ToggleGroup.Root>

		<ToggleGroup.Item />

	</ToggleGroup.Root>

);

```

## [API Reference](https://www.radix-ui.com/primitives/docs/components/toggle-group#api-reference)
### [Root](https://www.radix-ui.com/primitives/docs/components/toggle-group#root)
Contains all the parts of a toggle group.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
|  `type*` Prop description  |  `enum` See full type  | No default value  |
|  `value` Prop description  | `string`  | No default value  |
|  `defaultValue` Prop description  | `string`  | No default value  |
|  `onValueChange` Prop description  |  `function` See full type  | No default value  |
|  `value` Prop description  | `string[]`  | `[]`  |
|  `defaultValue` Prop description  | `string[]`  | `[]`  |
|  `onValueChange` Prop description  |  `function` See full type  | No default value  |
|  `disabled` Prop description  | `boolean`  | `false`  |
|  `rovingFocus` Prop description  | `boolean`  | `true`  |
|  `orientation` Prop description  |  `enum` See full type  | `undefined`  |
|  `dir` Prop description  |  `enum` See full type  | No default value  |
|  `loop` Prop description  | `boolean`  | `true`  |
| Data attribute  | Values  |
| --- | --- |
| `[data-orientation]`  | `"vertical"  | "horizontal" `  |
### [Item](https://www.radix-ui.com/primitives/docs/components/toggle-group#item)
An item in the group.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
|  `value*` Prop description  | `string`  | No default value  |
|  `disabled` Prop description  | `boolean`  | No default value  |
| Data attribute  | Values  |
| --- | --- |
| `[data-state]`  | `"on"  | "off" `  |
| `[data-disabled]`  | Present when disabled  |
| `[data-orientation]`  | `"vertical"  | "horizontal" `  |
## [Examples](https://www.radix-ui.com/primitives/docs/components/toggle-group#examples)
### [Ensuring there is always a value](https://www.radix-ui.com/primitives/docs/components/toggle-group#ensuring-there-is-always-a-value)
You can control the component to ensure a value.

```

import * as React from "react";

import { ToggleGroup } from "radix-ui";

export default () => {

	const [value, setValue] = React.useState("left");

	return (

		<ToggleGroup.Root
			type="single"
			value={value}
			onValueChange={(value) => {
				if (value) setValue(value);
			}}
		>

			<ToggleGroup.Item value="left">

				<TextAlignLeftIcon />

			</ToggleGroup.Item>

			<ToggleGroup.Item value="center">

				<TextAlignCenterIcon />

			</ToggleGroup.Item>

			<ToggleGroup.Item value="right">

				<TextAlignRightIcon />

			</ToggleGroup.Item>

		</ToggleGroup.Root>

	);

};

```

## [Accessibility](https://www.radix-ui.com/primitives/docs/components/toggle-group#accessibility)
Uses
### [Keyboard Interactions](https://www.radix-ui.com/primitives/docs/components/toggle-group#keyboard-interactions)
| Key  | Description  |
| --- | --- |
| `Tab`  | Moves focus to either the pressed item or the first item in the group.  |
| `Space`  | Activates/deactivates the item.  |
| `Enter`  | Activates/deactivates the item.  |
| `ArrowDown`  | Moves focus to the next item in the group.  |
| `ArrowRight`  | Moves focus to the next item in the group.  |
| `ArrowUp`  | Moves focus to the previous item in the group.  |
| `ArrowLeft`  | Moves focus to the previous item in the group.  |
| `Home`  | Moves focus to the first item.  |
| `End`  | Moves focus to the last item.  |
#### Quick nav
  * [Anatomy](https://www.radix-ui.com/primitives/docs/components/toggle-group#anatomy)
  * [API Reference](https://www.radix-ui.com/primitives/docs/components/toggle-group#api-reference)
  * [Root](https://www.radix-ui.com/primitives/docs/components/toggle-group#root)
  * [Item](https://www.radix-ui.com/primitives/docs/components/toggle-group#item)
  * [Examples](https://www.radix-ui.com/primitives/docs/components/toggle-group#examples)
  * [Ensuring there is always a value](https://www.radix-ui.com/primitives/docs/components/toggle-group#ensuring-there-is-always-a-value)
  * [Accessibility](https://www.radix-ui.com/primitives/docs/components/toggle-group#accessibility)
  * [Keyboard Interactions](https://www.radix-ui.com/primitives/docs/components/toggle-group#keyboard-interactions)

Previous[Toggle](https://www.radix-ui.com/primitives/docs/components/toggle)
Next[Toolbar](https://www.radix-ui.com/primitives/docs/components/toolbar)
