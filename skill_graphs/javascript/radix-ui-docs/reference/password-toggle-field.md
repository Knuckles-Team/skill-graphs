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
# Password Toggle Field
A password input field with an integrated button to toggle the value's visibility.
index.jsxindex.jsxstyles.cssstyles.css
CSS

```

import * as React from "react";

import { unstable_PasswordToggleField as PasswordToggleField } from "radix-ui";

import { EyeClosedIcon, EyeOpenIcon } from "@radix-ui/react-icons";

const PasswordToggleFieldDemo = () => (

	<PasswordToggleField.Root>

		<div className="Root">

			<PasswordToggleField.Input className="Input" />

			<PasswordToggleField.Toggle className="Toggle">

				<PasswordToggleField.Icon
					visible={<EyeOpenIcon />}
					hidden={<EyeClosedIcon />}
				/>

			</PasswordToggleField.Toggle>

		</div>

	</PasswordToggleField.Root>

);

export default PasswordToggleFieldDemo;

Expand code

```

## Features
  * Returns focus to the input when toggling with a pointer
  * Maintains button focus when toggling with keyboard or virtual navigation
  * Resets visibility to hidden after form submission to prevent accidental storage
  * Implicit accessible labeling for icon-based toggle buttons

## Component Reference Links
Version: 0.1.4
Size:
[View as Markdown](https://www.radix-ui.com/primitives/docs/components/password-toggle-field.md)
## [Anatomy](https://www.radix-ui.com/primitives/docs/components/password-toggle-field#anatomy)
Import all parts and piece them together.

```

import { unstable_PasswordToggleField as PasswordToggleField } from "radix-ui";

import { EyeClosedIcon, EyeOpenIcon } from "@radix-ui/react-icons";

export default () => (

	<PasswordToggleField.Root>

		<PasswordToggleField.Input />

		<PasswordToggleField.Toggle>

			<PasswordToggleField.Icon
				visible={<EyeOpenIcon />}
				hidden={<EyeClosedIcon />}
			/>

		</PasswordToggleField.Toggle>

	</PasswordToggleField.Root>

);

```

## [API Reference](https://www.radix-ui.com/primitives/docs/components/password-toggle-field#api-reference)
### [Root](https://www.radix-ui.com/primitives/docs/components/password-toggle-field#root)
Contains all the parts of a password toggle field.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `id` Prop description  | `string`  | No default value  |
|  `visible` Prop description  | `boolean`  | No default value  |
|  `defaultVisible` Prop description  | `boolean`  | No default value  |
|  `onVisiblityChange` Prop description  |  `function` See full type  | No default value  |
### [Input](https://www.radix-ui.com/primitives/docs/components/password-toggle-field#input)
Renders a the input containing the password value.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
|  `autoComplete` Prop description  |  `enum` See full type  | `"current-password"`  |
### [Toggle](https://www.radix-ui.com/primitives/docs/components/password-toggle-field#toggle)
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
### [Slot](https://www.radix-ui.com/primitives/docs/components/password-toggle-field#slot)
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `render` Prop description  |  `function` See full type  | No default value  |
|  `visible` Prop description  | `boolean`  | No default value  |
|  `hidden` Prop description  | `boolean`  | No default value  |
### [Icon](https://www.radix-ui.com/primitives/docs/components/password-toggle-field#icon)
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
|  `visible*` Prop description  | `boolean`  | No default value  |
|  `hidden*` Prop description  | `boolean`  | No default value  |
## [Examples](https://www.radix-ui.com/primitives/docs/components/password-toggle-field#examples)
### [Basic usage](https://www.radix-ui.com/primitives/docs/components/password-toggle-field#basic-usage)

```

<PasswordToggleField.Root>

	<PasswordToggleField.Input />

	<PasswordToggleField.Toggle>

		<PasswordToggleField.Icon
			visible={<EyeOpenIcon />}
			hidden={<EyeClosedIcon />}
		/>

	</PasswordToggleField.Toggle>

</PasswordToggleField.Root>

```

### [With `Slot`](https://www.radix-ui.com/primitives/docs/components/password-toggle-field#with-slot)

```

<PasswordToggleField.Root>

	<PasswordToggleField.Input />

	<PasswordToggleField.Toggle>

		<PasswordToggleField.Slot visible="🙊" hidden="🙈" />

	</PasswordToggleField.Toggle>

</PasswordToggleField.Root>

```

### [With `Slot` + `render` prop](https://www.radix-ui.com/primitives/docs/components/password-toggle-field#with-slot--render-prop)

```

<PasswordToggleField.Root>

	<PasswordToggleField.Input />

	<PasswordToggleField.Toggle>

		<PasswordToggleField.Slot
			render={({ visible }) => (
				<svg aria-hidden viewBox="0 0 2 2" xmlns="http://www.w3.org/2000/svg">
					<path d={visible ? "M1 1 L2 2" : "M2 1 L1 2"} />
				</svg>
			)}
		/>

	</PasswordToggleField.Toggle>

</PasswordToggleField.Root>

```

#### Quick nav
  * [Anatomy](https://www.radix-ui.com/primitives/docs/components/password-toggle-field#anatomy)
  * [API Reference](https://www.radix-ui.com/primitives/docs/components/password-toggle-field#api-reference)
  * [Root](https://www.radix-ui.com/primitives/docs/components/password-toggle-field#root)
  * [Input](https://www.radix-ui.com/primitives/docs/components/password-toggle-field#input)
  * [Toggle](https://www.radix-ui.com/primitives/docs/components/password-toggle-field#toggle)
  * [Slot](https://www.radix-ui.com/primitives/docs/components/password-toggle-field#slot)
  * [Icon](https://www.radix-ui.com/primitives/docs/components/password-toggle-field#icon)
  * [Examples](https://www.radix-ui.com/primitives/docs/components/password-toggle-field#examples)
  * [Basic usage](https://www.radix-ui.com/primitives/docs/components/password-toggle-field#basic-usage)
  * [With Slot](https://www.radix-ui.com/primitives/docs/components/password-toggle-field#with-slot)
  * [With Slot + render prop](https://www.radix-ui.com/primitives/docs/components/password-toggle-field#with-slot--render-prop)

Previous[One-Time Password Field](https://www.radix-ui.com/primitives/docs/components/one-time-password-field)
Next[Popover](https://www.radix-ui.com/primitives/docs/components/popover)
