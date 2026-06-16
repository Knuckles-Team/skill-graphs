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
Overview
# Getting started
A quick tutorial to get you up and running with Radix Primitives.
## [Implementing a Popover](https://www.radix-ui.com/primitives/docs/overview/getting-started#implementing-a-popover)
In this quick tutorial, we will install and style the [Popover](https://www.radix-ui.com/primitives/docs/components/popover) component.
### [1. Install the primitive](https://www.radix-ui.com/primitives/docs/overview/getting-started#1-install-the-primitive)
Install Radix Primitives from your command line.

```

npm install radix-ui@latest

```

### [2. Import the parts](https://www.radix-ui.com/primitives/docs/overview/getting-started#2-import-the-parts)
Import and structure the parts.

```

// index.jsx

import * as React from "react";

import { Popover } from "radix-ui";

const PopoverDemo = () => (

	<Popover.Root>

		<Popover.Trigger>More info</Popover.Trigger>

		<Popover.Portal>

			<Popover.Content>

				Some more info…

				<Popover.Arrow />

			</Popover.Content>

		</Popover.Portal>

	</Popover.Root>

);

export default PopoverDemo;

```

### [3. Add your styles](https://www.radix-ui.com/primitives/docs/overview/getting-started#3-add-your-styles)
Add styles where desired.

```

// index.jsx

import * as React from "react";

import { Popover } from "radix-ui";

import "./styles.css";

const PopoverDemo = () => (

	<Popover.Root>

		<Popover.Trigger className="PopoverTrigger">Show info</Popover.Trigger>

		<Popover.Portal>

			<Popover.Content className="PopoverContent">

				Some content

				<Popover.Arrow className="PopoverArrow" />

			</Popover.Content>

		</Popover.Portal>

	</Popover.Root>

);

export default PopoverDemo;

```

```

/* styles.css */

.PopoverTrigger {

	background-color: white;

	border-radius: 4px;

}

.PopoverContent {

	border-radius: 4px;

	padding: 20px;

	width: 260px;

	background-color: white;

}

.PopoverArrow {

	fill: white;

}

```

### [Demo](https://www.radix-ui.com/primitives/docs/overview/getting-started#demo)
Here's a complete demo.
More info
index.jsxindex.jsxstyles.cssstyles.css

```

import * as React from "react";

import { Popover } from "radix-ui";

import "./styles.css";

const PopoverDemo = () => (

	<Popover.Root>

		<Popover.Trigger className="PopoverTrigger">More info</Popover.Trigger>

		<Popover.Portal>

			<Popover.Content className="PopoverContent" sideOffset={5}>

				Some more info…

				<Popover.Arrow className="PopoverArrow" />

			</Popover.Content>

		</Popover.Portal>

	</Popover.Root>

);

export default PopoverDemo;

Expand code

```

## [Summary](https://www.radix-ui.com/primitives/docs/overview/getting-started#summary)
The steps above outline briefly what's involved in using a Radix Primitive in your application.
These components are low-level enough to give you control over how you want to wrap them. You're free to introduce your own high-level API to better suit the needs of your team and product.
In a few simple steps, we've implemented a fully accessible Popover component, without having to worry about many of its complexities.
  * Adheres to
  * Can be controlled or uncontrolled.
  * Customize side, alignment, offsets, collision handling.
  * Optionally render a pointing arrow.
  * Focus is fully managed and customizable.
  * Dismissing and layering behavior is highly customizable.

#### Quick nav
  * [Implementing a Popover](https://www.radix-ui.com/primitives/docs/overview/getting-started#implementing-a-popover)
  * [1. Install the primitive](https://www.radix-ui.com/primitives/docs/overview/getting-started#1-install-the-primitive)
  * [2. Import the parts](https://www.radix-ui.com/primitives/docs/overview/getting-started#2-import-the-parts)
  * [3. Add your styles](https://www.radix-ui.com/primitives/docs/overview/getting-started#3-add-your-styles)
  * [Demo](https://www.radix-ui.com/primitives/docs/overview/getting-started#demo)
  * [Summary](https://www.radix-ui.com/primitives/docs/overview/getting-started#summary)

Previous[Introduction](https://www.radix-ui.com/primitives/docs/overview/introduction)
Next[Accessibility](https://www.radix-ui.com/primitives/docs/overview/accessibility)
