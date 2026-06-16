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
# Toolbar
A container for grouping a set of controls, such as buttons, toggle groups or dropdown menus.
[Edited 2 hours ago](https://www.radix-ui.com/primitives/docs/components/toolbar)Share
index.jsxindex.jsxstyles.cssstyles.css
CSS

```

import * as React from "react";

import { Toolbar } from "radix-ui";

import {
	StrikethroughIcon,
	TextAlignLeftIcon,
	TextAlignCenterIcon,
	TextAlignRightIcon,
	FontBoldIcon,
	FontItalicIcon,
} from "@radix-ui/react-icons";

import "./styles.css";

const ToolbarDemo = () => (

	<Toolbar.Root className="ToolbarRoot" aria-label="Formatting options">

		<Toolbar.ToggleGroup type="multiple" aria-label="Text formatting">

			<Toolbar.ToggleItem
				className="ToolbarToggleItem"
				value="bold"
				aria-label="Bold"
			>

				<FontBoldIcon />

			</Toolbar.ToggleItem>

			<Toolbar.ToggleItem
				className="ToolbarToggleItem"
				value="italic"
				aria-label="Italic"
			>

				<FontItalicIcon />

			</Toolbar.ToggleItem>

			<Toolbar.ToggleItem
				className="ToolbarToggleItem"
				value="strikethrough"
				aria-label="Strike through"
			>

				<StrikethroughIcon />

			</Toolbar.ToggleItem>

		</Toolbar.ToggleGroup>

		<Toolbar.Separator className="ToolbarSeparator" />

		<Toolbar.ToggleGroup
			type="single"
			defaultValue="center"
			aria-label="Text alignment"
		>

			<Toolbar.ToggleItem
				className="ToolbarToggleItem"
				value="left"
				aria-label="Left aligned"
			>

				<TextAlignLeftIcon />

			</Toolbar.ToggleItem>

			<Toolbar.ToggleItem
				className="ToolbarToggleItem"
				value="center"
				aria-label="Center aligned"
			>

				<TextAlignCenterIcon />

			</Toolbar.ToggleItem>

			<Toolbar.ToggleItem
				className="ToolbarToggleItem"
				value="right"
				aria-label="Right aligned"
			>

				<TextAlignRightIcon />

			</Toolbar.ToggleItem>

		</Toolbar.ToggleGroup>

		<Toolbar.Separator className="ToolbarSeparator" />

		<Toolbar.Link
			className="ToolbarLink"
			href="#"
			target="_blank"
			style={{ marginRight: 10 }}
		>

			Edited 2 hours ago

		</Toolbar.Link>

		<Toolbar.Button className="ToolbarButton" style={{ marginLeft: "auto" }}>

			Share

		</Toolbar.Button>

	</Toolbar.Root>

);

export default ToolbarDemo;

Expand code

```

## Features
  * Full keyboard navigation.

## Component Reference Links
Version: 1.1.12
Size:
[View as Markdown](https://www.radix-ui.com/primitives/docs/components/toolbar.md)
## [Anatomy](https://www.radix-ui.com/primitives/docs/components/toolbar#anatomy)
Import the component.

```

import { Toolbar } from "radix-ui";

export default () => (

	<Toolbar.Root>

		<Toolbar.Button />

		<Toolbar.Separator />

		<Toolbar.Link />

		<Toolbar.ToggleGroup>

			<Toolbar.ToggleItem />

		</Toolbar.ToggleGroup>

	</Toolbar.Root>

);

```

## [API Reference](https://www.radix-ui.com/primitives/docs/components/toolbar#api-reference)
### [Root](https://www.radix-ui.com/primitives/docs/components/toolbar#root)
Contains all the toolbar component parts.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
|  `orientation` Prop description  |  `enum` See full type  | `"horizontal"`  |
|  `dir` Prop description  |  `enum` See full type  | No default value  |
|  `loop` Prop description  | `boolean`  | `true`  |
| Data attribute  | Values  |
| --- | --- |
| `[data-orientation]`  | `"vertical"  | "horizontal" `  |
### [Button](https://www.radix-ui.com/primitives/docs/components/toolbar#button)
A button item.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
| Data attribute  | Values  |
| --- | --- |
| `[data-orientation]`  | `"vertical"  | "horizontal" `  |
### [Link](https://www.radix-ui.com/primitives/docs/components/toolbar#link)
A link item.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
### [ToggleGroup](https://www.radix-ui.com/primitives/docs/components/toolbar#togglegroup)
A set of two-state buttons that can be toggled on or off.
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
| Data attribute  | Values  |
| --- | --- |
| `[data-orientation]`  | `"vertical"  | "horizontal" `  |
### [ToggleItem](https://www.radix-ui.com/primitives/docs/components/toolbar#toggleitem)
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
### [Separator](https://www.radix-ui.com/primitives/docs/components/toolbar#separator)
Used to visually separate items in the toolbar.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
| Data attribute  | Values  |
| --- | --- |
| `[data-orientation]`  | `"vertical"  | "horizontal" `  |
## [Examples](https://www.radix-ui.com/primitives/docs/components/toolbar#examples)
### [Use with other primitives](https://www.radix-ui.com/primitives/docs/components/toolbar#use-with-other-primitives)
All our primitives which expose a `Trigger` part, such as `Dialog`, `AlertDialog`, `Popover`, `DropdownMenu` can be composed within a toolbar by using the [`asChild` prop](https://www.radix-ui.com/primitives/docs/guides/composition).
Here is an example using our `DropdownMenu` primitive.

```

import { Toolbar, DropdownMenu } from "radix-ui";

export default () => (

	<Toolbar.Root>

		<Toolbar.Button>Action 1</Toolbar.Button>

		<Toolbar.Separator />

		<DropdownMenu.Root>

			<Toolbar.Button asChild>

				<DropdownMenu.Trigger>Trigger</DropdownMenu.Trigger>

			</Toolbar.Button>

			<DropdownMenu.Content>…</DropdownMenu.Content>

		</DropdownMenu.Root>

	</Toolbar.Root>

);

```

## [Accessibility](https://www.radix-ui.com/primitives/docs/components/toolbar#accessibility)
Uses
### [Keyboard Interactions](https://www.radix-ui.com/primitives/docs/components/toolbar#keyboard-interactions)
| Key  | Description  |
| --- | --- |
| `Tab`  | Moves focus to the first item in the group.  |
| `Space`  | Activates/deactivates the item.  |
| `Enter`  | Activates/deactivates the item.  |
| `ArrowDown`  | Moves focus to the next item depending on `orientation`.  |
| `ArrowRight`  | Moves focus to the next item depending on `orientation`.  |
| `ArrowUp`  | Moves focus to the previous item depending on `orientation`.  |
| `ArrowLeft`  | Moves focus to the previous item depending on `orientation`.  |
| `Home`  | Moves focus to the first item.  |
| `End`  | Moves focus to the last item.  |
#### Quick nav
  * [Anatomy](https://www.radix-ui.com/primitives/docs/components/toolbar#anatomy)
  * [API Reference](https://www.radix-ui.com/primitives/docs/components/toolbar#api-reference)
  * [Root](https://www.radix-ui.com/primitives/docs/components/toolbar#root)
  * [Button](https://www.radix-ui.com/primitives/docs/components/toolbar#button)
  * [Link](https://www.radix-ui.com/primitives/docs/components/toolbar#link)
  * [ToggleGroup](https://www.radix-ui.com/primitives/docs/components/toolbar#togglegroup)
  * [ToggleItem](https://www.radix-ui.com/primitives/docs/components/toolbar#toggleitem)
  * [Separator](https://www.radix-ui.com/primitives/docs/components/toolbar#separator)
  * [Examples](https://www.radix-ui.com/primitives/docs/components/toolbar#examples)
  * [Use with other primitives](https://www.radix-ui.com/primitives/docs/components/toolbar#use-with-other-primitives)
  * [Accessibility](https://www.radix-ui.com/primitives/docs/components/toolbar#accessibility)
  * [Keyboard Interactions](https://www.radix-ui.com/primitives/docs/components/toolbar#keyboard-interactions)

Previous[Toggle Group](https://www.radix-ui.com/primitives/docs/components/toggle-group)
Next[Tooltip](https://www.radix-ui.com/primitives/docs/components/tooltip)
