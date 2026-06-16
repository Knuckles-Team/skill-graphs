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
# Checkbox
A control that allows the user to toggle between checked and not checked.
Accept terms and conditions.
index.jsxindex.jsxstyles.cssstyles.css
CSS

```

import * as React from "react";

import { Checkbox } from "radix-ui";

import { CheckIcon } from "@radix-ui/react-icons";

import "./styles.css";

const CheckboxDemo = () => (

	<form>

		<div style={{ display: "flex", alignItems: "center" }}>

			<Checkbox.Root className="CheckboxRoot" defaultChecked id="c1">

				<Checkbox.Indicator className="CheckboxIndicator">

					<CheckIcon />

				</Checkbox.Indicator>

			</Checkbox.Root>

			<label className="Label" htmlFor="c1">

				Accept terms and conditions.

			</label>

		</div>

	</form>

);

export default CheckboxDemo;

Expand code

```

## Features
  * Supports indeterminate state.
  * Full keyboard navigation.
  * Can be controlled or uncontrolled.

## Component Reference Links
Version: 1.3.4
Size:
[View as Markdown](https://www.radix-ui.com/primitives/docs/components/checkbox.md)
## [Anatomy](https://www.radix-ui.com/primitives/docs/components/checkbox#anatomy)
Import all parts and piece them together.

```

import { Checkbox } from "radix-ui";

export default () => (

	<Checkbox.Root>

		<Checkbox.Indicator />

	</Checkbox.Root>

);

```

## [API Reference](https://www.radix-ui.com/primitives/docs/components/checkbox#api-reference)
### [Root](https://www.radix-ui.com/primitives/docs/components/checkbox#root)
Contains all the parts of a checkbox. An `input` will also render when used within a `form` to ensure events propagate correctly.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
|  `defaultChecked` Prop description  | `boolean | 'indeterminate'`  | No default value  |
|  `checked` Prop description  | `boolean | 'indeterminate'`  | No default value  |
|  `onCheckedChange` Prop description  |  `function` See full type  | No default value  |
|  `disabled` Prop description  | `boolean`  | No default value  |
|  `required` Prop description  | `boolean`  | No default value  |
|  `name` Prop description  | `string`  | No default value  |
|  `value` Prop description  | `string`  | `on`  |
| Data attribute  | Values  |
| --- | --- |
| `[data-state]`  | `"checked"  | "unchecked"  | "indeterminate" `  |
| `[data-disabled]`  | Present when disabled  |
### [Indicator](https://www.radix-ui.com/primitives/docs/components/checkbox#indicator)
Renders when the checkbox is in a checked or indeterminate state. You can style this element directly, or you can use it as a wrapper to put an icon into, or both.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
|  `forceMount` Prop description  | `boolean`  | No default value  |
| Data attribute  | Values  |
| --- | --- |
| `[data-state]`  | `"checked"  | "unchecked"  | "indeterminate" `  |
| `[data-disabled]`  | Present when disabled  |
## [Examples](https://www.radix-ui.com/primitives/docs/components/checkbox#examples)
### [Indeterminate](https://www.radix-ui.com/primitives/docs/components/checkbox#indeterminate)
You can set the checkbox to `indeterminate` by taking control of its state.

```

import { DividerHorizontalIcon, CheckIcon } from "@radix-ui/react-icons";

import { Checkbox } from "radix-ui";

export default () => {

	const [checked, setChecked] = React.useState("indeterminate");

	return (

		<>

			<StyledCheckbox checked={checked} onCheckedChange={setChecked}>

				<Checkbox.Indicator>

					{checked === "indeterminate" && <DividerHorizontalIcon />}

					{checked === true && <CheckIcon />}

				</Checkbox.Indicator>

			</StyledCheckbox>

			<button
				type="button"
				onClick={() =>
					setChecked((prevIsChecked) =>
						prevIsChecked === "indeterminate" ? false : "indeterminate",
					)
				}
			>

				Toggle indeterminate

			</button>

		</>

	);

};

```

## [Accessibility](https://www.radix-ui.com/primitives/docs/components/checkbox#accessibility)
Adheres to the
### [Keyboard Interactions](https://www.radix-ui.com/primitives/docs/components/checkbox#keyboard-interactions)
| Key  | Description  |
| --- | --- |
| `Space`  | Checks/unchecks the checkbox.  |
#### Quick nav
  * [Anatomy](https://www.radix-ui.com/primitives/docs/components/checkbox#anatomy)
  * [API Reference](https://www.radix-ui.com/primitives/docs/components/checkbox#api-reference)
  * [Root](https://www.radix-ui.com/primitives/docs/components/checkbox#root)
  * [Indicator](https://www.radix-ui.com/primitives/docs/components/checkbox#indicator)
  * [Examples](https://www.radix-ui.com/primitives/docs/components/checkbox#examples)
  * [Indeterminate](https://www.radix-ui.com/primitives/docs/components/checkbox#indeterminate)
  * [Accessibility](https://www.radix-ui.com/primitives/docs/components/checkbox#accessibility)
  * [Keyboard Interactions](https://www.radix-ui.com/primitives/docs/components/checkbox#keyboard-interactions)

Previous[Avatar](https://www.radix-ui.com/primitives/docs/components/avatar)
Next[Collapsible](https://www.radix-ui.com/primitives/docs/components/collapsible)
