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
# Collapsible
An interactive component which expands/collapses a panel.
@peduarte starred 3 repositories
@radix-ui/primitives
index.jsxindex.jsxstyles.cssstyles.css
CSS

```

import * as React from "react";

import { Collapsible } from "radix-ui";

import { RowSpacingIcon, Cross2Icon } from "@radix-ui/react-icons";

import "./styles.css";

const CollapsibleDemo = () => {

	const [open, setOpen] = React.useState(false);

	return (

		<Collapsible.Root
			className="CollapsibleRoot"
			open={open}
			onOpenChange={setOpen}
		>

			<div
				style={{
					display: "flex",
					alignItems: "center",
					justifyContent: "space-between",
				}}
			>

				<span className="Text" style={{ color: "white" }}>

					@peduarte starred 3 repositories

				</span>

				<Collapsible.Trigger asChild>

					<button className="IconButton">

						{open ? <Cross2Icon /> : <RowSpacingIcon />}

					</button>

				</Collapsible.Trigger>

			</div>

			<div className="Repository">

				<span className="Text">@radix-ui/primitives</span>

			</div>

			<Collapsible.Content>

				<div className="Repository">

					<span className="Text">@radix-ui/colors</span>

				</div>

				<div className="Repository">

					<span className="Text">@radix-ui/themes</span>

				</div>

			</Collapsible.Content>

		</Collapsible.Root>

	);

};

export default CollapsibleDemo;

Expand code

```

## Features
  * Full keyboard navigation.
  * Can be controlled or uncontrolled.

## Component Reference Links
Version: 1.1.13
Size:
[View as Markdown](https://www.radix-ui.com/primitives/docs/components/collapsible.md)
## [Anatomy](https://www.radix-ui.com/primitives/docs/components/collapsible#anatomy)
Import the components and piece the parts together.

```

import { Collapsible } from "radix-ui";

export default () => (

	<Collapsible.Root>

		<Collapsible.Trigger />

		<Collapsible.Content />

	</Collapsible.Root>

);

```

## [API Reference](https://www.radix-ui.com/primitives/docs/components/collapsible#api-reference)
### [Root](https://www.radix-ui.com/primitives/docs/components/collapsible#root)
Contains all the parts of a collapsible.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
|  `defaultOpen` Prop description  | `boolean`  | No default value  |
|  `open` Prop description  | `boolean`  | No default value  |
|  `onOpenChange` Prop description  |  `function` See full type  | No default value  |
|  `disabled` Prop description  | `boolean`  | No default value  |
| Data attribute  | Values  |
| --- | --- |
| `[data-state]`  | `"open"  | "closed" `  |
| `[data-disabled]`  | Present when disabled  |
### [Trigger](https://www.radix-ui.com/primitives/docs/components/collapsible#trigger)
The button that toggles the collapsible.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
| Data attribute  | Values  |
| --- | --- |
| `[data-state]`  | `"open"  | "closed" `  |
| `[data-disabled]`  | Present when disabled  |
### [Content](https://www.radix-ui.com/primitives/docs/components/collapsible#content)
The component that contains the collapsible content.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
|  `forceMount` Prop description  | `boolean`  | No default value  |
| Data attribute  | Values  |
| --- | --- |
| `[data-state]`  | `"open"  | "closed" `  |
| `[data-disabled]`  | Present when disabled  |
| CSS Variable  | Description  |
| --- | --- |
| `--radix-collapsible-content-width`  | The width of the content when it opens/closes  |
| `--radix-collapsible-content-height`  | The height of the content when it opens/closes  |
## [Examples](https://www.radix-ui.com/primitives/docs/components/collapsible#examples)
### [Animating content size](https://www.radix-ui.com/primitives/docs/components/collapsible#animating-content-size)
Use the `--radix-collapsible-content-width` and/or `--radix-collapsible-content-height` CSS variables to animate the size of the content when it opens/closes. Here's a demo:

```

// index.jsx

import { Collapsible } from "radix-ui";

import "./styles.css";

export default () => (

	<Collapsible.Root>

		<Collapsible.Trigger>…</Collapsible.Trigger>

		<Collapsible.Content className="CollapsibleContent">

			…

		</Collapsible.Content>

	</Collapsible.Root>

);

```

```

/* styles.css */

.CollapsibleContent {

	overflow: hidden;

}

.CollapsibleContent[data-state="open"] {

	animation: slideDown 300ms ease-out;

}

.CollapsibleContent[data-state="closed"] {

	animation: slideUp 300ms ease-out;

}

@keyframes slideDown {

	from {

		height: 0;

	}

	to {

		height: var(--radix-collapsible-content-height);

	}

}

@keyframes slideUp {

	from {

		height: var(--radix-collapsible-content-height);

	}

	to {

		height: 0;

	}

}

```

## [Accessibility](https://www.radix-ui.com/primitives/docs/components/collapsible#accessibility)
Adheres to the
### [Keyboard Interactions](https://www.radix-ui.com/primitives/docs/components/collapsible#keyboard-interactions)
| Key  | Description  |
| --- | --- |
| `Space`  | Opens/closes the collapsible.  |
| `Enter`  | Opens/closes the collapsible.  |
#### Quick nav
  * [Anatomy](https://www.radix-ui.com/primitives/docs/components/collapsible#anatomy)
  * [API Reference](https://www.radix-ui.com/primitives/docs/components/collapsible#api-reference)
  * [Root](https://www.radix-ui.com/primitives/docs/components/collapsible#root)
  * [Trigger](https://www.radix-ui.com/primitives/docs/components/collapsible#trigger)
  * [Content](https://www.radix-ui.com/primitives/docs/components/collapsible#content)
  * [Examples](https://www.radix-ui.com/primitives/docs/components/collapsible#examples)
  * [Animating content size](https://www.radix-ui.com/primitives/docs/components/collapsible#animating-content-size)
  * [Accessibility](https://www.radix-ui.com/primitives/docs/components/collapsible#accessibility)
  * [Keyboard Interactions](https://www.radix-ui.com/primitives/docs/components/collapsible#keyboard-interactions)

Previous[Checkbox](https://www.radix-ui.com/primitives/docs/components/checkbox)
Next[Context Menu](https://www.radix-ui.com/primitives/docs/components/context-menu)
