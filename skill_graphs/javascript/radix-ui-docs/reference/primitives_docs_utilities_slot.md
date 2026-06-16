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
# Slot
Merges its props onto its immediate child.
## Features
  * Can be used to support your own `asChild` prop.

## Component Reference Links
Version: 1.2.5
Size:
[View as Markdown](https://www.radix-ui.com/primitives/docs/utilities/slot.md)
## [Anatomy](https://www.radix-ui.com/primitives/docs/utilities/slot#anatomy)
Import the component.

```

import { Slot } from "radix-ui";

export default () => (

	<Slot.Root>

		<div>Hello</div>

	</Slot.Root>

);

```

## [Basic example](https://www.radix-ui.com/primitives/docs/utilities/slot#basic-example)
Use to create your own `asChild` API.
When your component has a single children element:

```

// your-button.jsx

import * as React from "react";

import { Slot } from "radix-ui";

function Button({ asChild, ...props }) {

	const Comp = asChild ? Slot.Root : "button";

	return <Comp {...props} />;

}

```

Use `Slottable` when your component has multiple children to pass the props to the correct element:

```

// your-button.jsx

import * as React from "react";

import { Slot } from "radix-ui";

function Button({ asChild, children, leftElement, rightElement, ...props }) {

	const Comp = asChild ? Slot.Root : "button";

	return (

		<Comp {...props}>

			{leftElement}

			<Slot.Slottable>{children}</Slot.Slottable>

			{rightElement}

		</Comp>

	);

}

```

### [Usage](https://www.radix-ui.com/primitives/docs/utilities/slot#usage)

```

import { Button } from "./your-button";

export default () => (

	<Button asChild>

		<a href="/contact">Contact</a>

	</Button>

);

```

### [Event handlers](https://www.radix-ui.com/primitives/docs/utilities/slot#event-handlers)
Any prop that starts with `on` (e.g., `onClick`) is considered an event handler.
When merging event handlers, `Slot` will create a new function where the child handler takes precedence over the slot handler.
If one of the event handlers relies on `event.defaultPrevented` make sure that the order is correct.

```

import { Slot } from "radix-ui";

export default () => (

	<Slot.Root
		onClick={(event) => {
			if (!event.defaultPrevented)
				console.log("Not logged because default is prevented.");
		}}
	>

		<button onClick={(event) => event.preventDefault()} />

	</Slot.Root>

);

```

#### Quick nav
  * [Anatomy](https://www.radix-ui.com/primitives/docs/utilities/slot#anatomy)
  * [Basic example](https://www.radix-ui.com/primitives/docs/utilities/slot#basic-example)
  * [Usage](https://www.radix-ui.com/primitives/docs/utilities/slot#usage)
  * [Event handlers](https://www.radix-ui.com/primitives/docs/utilities/slot#event-handlers)

Previous[Portal](https://www.radix-ui.com/primitives/docs/utilities/portal)
Next[Visually Hidden](https://www.radix-ui.com/primitives/docs/utilities/visually-hidden)
