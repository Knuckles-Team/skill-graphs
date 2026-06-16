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
# Radio Group
A set of checkable buttons—known as radio buttons—where no more than one of the buttons can be checked at a time.
Default
Comfortable
Compact
index.jsxindex.jsxstyles.cssstyles.css
CSS

```

import * as React from "react";

import { RadioGroup } from "radix-ui";

import "./styles.css";

const RadioGroupDemo = () => (

	<form>

		<RadioGroup.Root
			className="RadioGroupRoot"
			defaultValue="default"
			aria-label="View density"
		>

			<div style={{ display: "flex", alignItems: "center" }}>

				<RadioGroup.Item className="RadioGroupItem" value="default" id="r1">

					<RadioGroup.Indicator className="RadioGroupIndicator" />

				</RadioGroup.Item>

				<label className="Label" htmlFor="r1">

					Default

				</label>

			</div>

			<div style={{ display: "flex", alignItems: "center" }}>

				<RadioGroup.Item className="RadioGroupItem" value="comfortable" id="r2">

					<RadioGroup.Indicator className="RadioGroupIndicator" />

				</RadioGroup.Item>

				<label className="Label" htmlFor="r2">

					Comfortable

				</label>

			</div>

			<div style={{ display: "flex", alignItems: "center" }}>

				<RadioGroup.Item className="RadioGroupItem" value="compact" id="r3">

					<RadioGroup.Indicator className="RadioGroupIndicator" />

				</RadioGroup.Item>

				<label className="Label" htmlFor="r3">

					Compact

				</label>

			</div>

		</RadioGroup.Root>

	</form>

);

export default RadioGroupDemo;

Expand code

```

## Features
  * Full keyboard navigation.
  * Supports horizontal/vertical orientation.
  * Can be controlled or uncontrolled.

## Component Reference Links
Version: 1.4.0
Size:
[View as Markdown](https://www.radix-ui.com/primitives/docs/components/radio-group.md)
## [Anatomy](https://www.radix-ui.com/primitives/docs/components/radio-group#anatomy)
Import all parts and piece them together.

```

import { RadioGroup } from "radix-ui";

export default () => (

	<RadioGroup.Root>

		<RadioGroup.Item>

			<RadioGroup.Indicator />

		</RadioGroup.Item>

	</RadioGroup.Root>

);

```

## [API Reference](https://www.radix-ui.com/primitives/docs/components/radio-group#api-reference)
### [Root](https://www.radix-ui.com/primitives/docs/components/radio-group#root)
Contains all the parts of a radio group.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
|  `defaultValue` Prop description  | `string`  | No default value  |
|  `value` Prop description  | `string`  | No default value  |
|  `onValueChange` Prop description  |  `function` See full type  | No default value  |
|  `disabled` Prop description  | `boolean`  | No default value  |
|  `name` Prop description  | `string`  | No default value  |
|  `required` Prop description  | `boolean`  | No default value  |
|  `orientation` Prop description  |  `enum` See full type  | `undefined`  |
|  `dir` Prop description  |  `enum` See full type  | No default value  |
|  `loop` Prop description  | `boolean`  | `true`  |
| Data attribute  | Values  |
| --- | --- |
| `[data-disabled]`  | Present when disabled  |
### [Item](https://www.radix-ui.com/primitives/docs/components/radio-group#item)
An item in the group that can be checked. An `input` will also render when used within a `form` to ensure events propagate correctly.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
|  `value` Prop description  | `string`  | No default value  |
|  `disabled` Prop description  | `boolean`  | No default value  |
|  `required` Prop description  | `boolean`  | No default value  |
| Data attribute  | Values  |
| --- | --- |
| `[data-state]`  | `"checked"  | "unchecked" `  |
| `[data-disabled]`  | Present when disabled  |
### [Indicator](https://www.radix-ui.com/primitives/docs/components/radio-group#indicator)
Renders when the radio item is in a checked state. You can style this element directly, or you can use it as a wrapper to put an icon into, or both.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
|  `forceMount` Prop description  | `boolean`  | No default value  |
| Data attribute  | Values  |
| --- | --- |
| `[data-state]`  | `"checked"  | "unchecked" `  |
| `[data-disabled]`  | Present when disabled  |
## [Accessibility](https://www.radix-ui.com/primitives/docs/components/radio-group#accessibility)
Adheres to the
### [Keyboard Interactions](https://www.radix-ui.com/primitives/docs/components/radio-group#keyboard-interactions)
| Key  | Description  |
| --- | --- |
| `Tab`  | Moves focus to either the checked radio item or the first radio item in the group.  |
| `Space`  | When focus is on an unchecked radio item, checks it.  |
| `ArrowDown`  | Moves focus and checks the next radio item in the group.  |
| `ArrowRight`  | Moves focus and checks the next radio item in the group.  |
| `ArrowUp`  | Moves focus to the previous radio item in the group.  |
| `ArrowLeft`  | Moves focus to the previous radio item in the group.  |
#### Quick nav
  * [Anatomy](https://www.radix-ui.com/primitives/docs/components/radio-group#anatomy)
  * [API Reference](https://www.radix-ui.com/primitives/docs/components/radio-group#api-reference)
  * [Root](https://www.radix-ui.com/primitives/docs/components/radio-group#root)
  * [Item](https://www.radix-ui.com/primitives/docs/components/radio-group#item)
  * [Indicator](https://www.radix-ui.com/primitives/docs/components/radio-group#indicator)
  * [Accessibility](https://www.radix-ui.com/primitives/docs/components/radio-group#accessibility)
  * [Keyboard Interactions](https://www.radix-ui.com/primitives/docs/components/radio-group#keyboard-interactions)

Previous[Progress](https://www.radix-ui.com/primitives/docs/components/progress)
Next[Scroll Area](https://www.radix-ui.com/primitives/docs/components/scroll-area)
