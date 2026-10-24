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
# Tooltip
A popup that displays information related to an element when the element receives keyboard focus or the mouse hovers over it.
index.jsxindex.jsxstyles.cssstyles.css
CSS

```

import * as React from "react";

import { Tooltip } from "radix-ui";

import { PlusIcon } from "@radix-ui/react-icons";

import "./styles.css";

const TooltipDemo = () => {

	return (

		<Tooltip.Provider>

			<Tooltip.Root>

				<Tooltip.Trigger asChild>

					<button className="IconButton">

						<PlusIcon />

					</button>

				</Tooltip.Trigger>

				<Tooltip.Portal>

					<Tooltip.Content className="TooltipContent" sideOffset={5}>

						Add to library

						<Tooltip.Arrow className="TooltipArrow" />

					</Tooltip.Content>

				</Tooltip.Portal>

			</Tooltip.Root>

		</Tooltip.Provider>

	);

};

export default TooltipDemo;

Expand code

```

## Features
  * Provider to control display delay globally.
  * Opens when the trigger is focused or hovered.
  * Closes when the trigger is activated or when pressing escape.
  * Supports custom timings.

## Component Reference Links
Version: 1.2.9
Size:
[View as Markdown](https://www.radix-ui.com/primitives/docs/components/tooltip.md)
## [Anatomy](https://www.radix-ui.com/primitives/docs/components/tooltip#anatomy)
Import all parts and piece them together.

```

import { Tooltip } from "radix-ui";

export default () => (

	<Tooltip.Provider>

		<Tooltip.Root>

			<Tooltip.Trigger />

			<Tooltip.Portal>

				<Tooltip.Content>

					<Tooltip.Arrow />

				</Tooltip.Content>

			</Tooltip.Portal>

		</Tooltip.Root>

	</Tooltip.Provider>

);

```

## [API Reference](https://www.radix-ui.com/primitives/docs/components/tooltip#api-reference)
### [Provider](https://www.radix-ui.com/primitives/docs/components/tooltip#provider)
Wraps your app to provide global functionality to your tooltips.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `delayDuration` Prop description  | `number`  | `700`  |
|  `skipDelayDuration` Prop description  | `number`  | `300`  |
|  `disableHoverableContent` Prop description  | `boolean`  | No default value  |
### [Root](https://www.radix-ui.com/primitives/docs/components/tooltip#root)
Contains all the parts of a tooltip.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `defaultOpen` Prop description  | `boolean`  | No default value  |
|  `open` Prop description  | `boolean`  | No default value  |
|  `onOpenChange` Prop description  |  `function` See full type  | No default value  |
|  `delayDuration` Prop description  | `number`  | `700`  |
|  `disableHoverableContent` Prop description  | `boolean`  | No default value  |
### [Trigger](https://www.radix-ui.com/primitives/docs/components/tooltip#trigger)
The button that toggles the tooltip. By default, the `Tooltip.Content` will position itself against the trigger.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
| Data attribute  | Values  |
| --- | --- |
| `[data-state]`  | `"closed"  | "delayed-open"  | "instant-open" `  |
### [Portal](https://www.radix-ui.com/primitives/docs/components/tooltip#portal)
When used, portals the content part into the `body`.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `forceMount` Prop description  | `boolean`  | No default value  |
|  `container` Prop description  | `HTMLElement`  | `document.body`  |
### [Content](https://www.radix-ui.com/primitives/docs/components/tooltip#content)
The component that pops out when the tooltip is open.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
|  `aria-label` Prop description  | `string`  | No default value  |
|  `onEscapeKeyDown` Prop description  |  `function` See full type  | No default value  |
|  `onPointerDownOutside` Prop description  |  `function` See full type  | No default value  |
|  `forceMount` Prop description  | `boolean`  | No default value  |
|  `side` Prop description  |  `enum` See full type  | `"top"`  |
|  `sideOffset` Prop description  | `number`  | `0`  |
|  `align` Prop description  |  `enum` See full type  | `"center"`  |
|  `alignOffset` Prop description  | `number`  | `0`  |
|  `avoidCollisions` Prop description  | `boolean`  | `true`  |
|  `collisionBoundary` Prop description  |  `Boundary` See full type  | `[]`  |
|  `collisionPadding` Prop description  |  `number | Padding` See full type  | `0`  |
|  `arrowPadding` Prop description  | `number`  | `0`  |
|  `sticky` Prop description  |  `enum` See full type  | `"partial"`  |
|  `hideWhenDetached` Prop description  | `boolean`  | `false`  |
| Data attribute  | Values  |
| --- | --- |
| `[data-state]`  | `"closed"  | "delayed-open"  | "instant-open" `  |
| `[data-side]`  | `"left"  | "right"  | "bottom"  | "top" `  |
| `[data-align]`  | `"start"  | "end"  | "center" `  |
| CSS Variable  | Description  |
| --- | --- |
| `--radix-tooltip-content-transform-origin`  | The `transform-origin` computed from the content and arrow positions/offsets  |
| `--radix-tooltip-content-available-width`  | The remaining width between the trigger and the boundary edge  |
| `--radix-tooltip-content-available-height`  | The remaining height between the trigger and the boundary edge  |
| `--radix-tooltip-trigger-width`  | The width of the trigger  |
| `--radix-tooltip-trigger-height`  | The height of the trigger  |
### [Arrow](https://www.radix-ui.com/primitives/docs/components/tooltip#arrow)
An optional arrow element to render alongside the tooltip. This can be used to help visually link the trigger with the `Tooltip.Content`. Must be rendered inside `Tooltip.Content`.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
|  `width` Prop description  | `number`  | `10`  |
|  `height` Prop description  | `number`  | `5`  |
## [Examples](https://www.radix-ui.com/primitives/docs/components/tooltip#examples)
### [Configure globally](https://www.radix-ui.com/primitives/docs/components/tooltip#configure-globally)
Use the `Provider` to control `delayDuration` and `skipDelayDuration` globally.

```

import { Tooltip } from "radix-ui";

export default () => (

	<Tooltip.Provider delayDuration={800} skipDelayDuration={500}>

		<Tooltip.Root>

			<Tooltip.Trigger>…</Tooltip.Trigger>

			<Tooltip.Content>…</Tooltip.Content>

		</Tooltip.Root>

		<Tooltip.Root>

			<Tooltip.Trigger>…</Tooltip.Trigger>

			<Tooltip.Content>…</Tooltip.Content>

		</Tooltip.Root>

	</Tooltip.Provider>

);

```

### [Show instantly](https://www.radix-ui.com/primitives/docs/components/tooltip#show-instantly)
Use the `delayDuration` prop to control the time it takes for the tooltip to open.

```

import { Tooltip } from "radix-ui";

export default () => (

	<Tooltip.Root delayDuration={0}>

		<Tooltip.Trigger>…</Tooltip.Trigger>

		<Tooltip.Content>…</Tooltip.Content>

	</Tooltip.Root>

);

```

### [Constrain the content size](https://www.radix-ui.com/primitives/docs/components/tooltip#constrain-the-content-size)
You may want to constrain the width of the content so that it matches the trigger width. You may also want to constrain its height to not exceed the viewport.
We expose several CSS custom properties such as `--radix-tooltip-trigger-width` and `--radix-tooltip-content-available-height` to support this. Use them to constrain the content dimensions.

```

// index.jsx

import { Tooltip } from "radix-ui";

import "./styles.css";

export default () => (

	<Tooltip.Root>

		<Tooltip.Trigger>…</Tooltip.Trigger>

		<Tooltip.Portal>

			<Tooltip.Content className="TooltipContent" sideOffset={5}>

				…

			</Tooltip.Content>

		</Tooltip.Portal>

	</Tooltip.Root>

);

```

```

/* styles.css */

.TooltipContent {

	width: var(--radix-tooltip-trigger-width);

	max-height: var(--radix-tooltip-content-available-height);

}

```

### [Origin-aware animations](https://www.radix-ui.com/primitives/docs/components/tooltip#origin-aware-animations)
We expose a CSS custom property `--radix-tooltip-content-transform-origin`. Use it to animate the content from its computed origin based on `side`, `sideOffset`, `align`, `alignOffset` and any collisions.

```

// index.jsx

import { Tooltip } from "radix-ui";

import "./styles.css";

export default () => (

	<Tooltip.Root>

		<Tooltip.Trigger>…</Tooltip.Trigger>

		<Tooltip.Content className="TooltipContent">…</Tooltip.Content>

	</Tooltip.Root>

);

```

```

/* styles.css */

.TooltipContent {

	transform-origin: var(--radix-tooltip-content-transform-origin);

	animation: scaleIn 0.5s ease-out;

}

@keyframes scaleIn {

	from {

		opacity: 0;

		transform: scale(0);

	}

	to {

		opacity: 1;

		transform: scale(1);

	}

}

```

### [Collision-aware animations](https://www.radix-ui.com/primitives/docs/components/tooltip#collision-aware-animations)
We expose `data-side` and `data-align` attributes. Their values will change at runtime to reflect collisions. Use them to create collision and direction-aware animations.

```

// index.jsx

import { Tooltip } from "radix-ui";

import "./styles.css";

export default () => (

	<Tooltip.Root>

		<Tooltip.Trigger>…</Tooltip.Trigger>

		<Tooltip.Content className="TooltipContent">…</Tooltip.Content>

	</Tooltip.Root>

);

```

```

/* styles.css */

.TooltipContent {

	animation-duration: 0.6s;

	animation-timing-function: cubic-bezier(0.16, 1, 0.3, 1);

}

.TooltipContent[data-side="top"] {

	animation-name: slideUp;

}

.TooltipContent[data-side="bottom"] {

	animation-name: slideDown;

}

@keyframes slideDown {

	from {

		opacity: 0;

		transform: translateY(-10px);

	}

	to {

		opacity: 1;

		transform: translateY(0);

	}

}

@keyframes slideUp {

	from {

		opacity: 0;

		transform: translateY(10px);

	}

	to {

		opacity: 1;

		transform: translateY(0);

	}

}

```

## [Accessibility](https://www.radix-ui.com/primitives/docs/components/tooltip#accessibility)
### [Keyboard Interactions](https://www.radix-ui.com/primitives/docs/components/tooltip#keyboard-interactions)
| Key  | Description  |
| --- | --- |
| `Tab`  | Opens/closes the tooltip without delay.  |
| `Space`  | If open, closes the tooltip without delay.  |
| `Enter`  | If open, closes the tooltip without delay.  |
| `Escape`  | If open, closes the tooltip without delay.  |
## [Custom APIs](https://www.radix-ui.com/primitives/docs/components/tooltip#custom-apis)
Create your own API by abstracting the primitive parts into your own component.
### [Abstract parts and introduce a content prop](https://www.radix-ui.com/primitives/docs/components/tooltip#abstract-parts-and-introduce-a-content-prop)
This example abstracts all of the `Tooltip` parts and introduces a new `content` prop.
#### Usage

```

import { Tooltip } from "./your-tooltip";

export default () => (

	<Tooltip content="Tooltip content">

		<button>Tooltip trigger</button>

	</Tooltip>

);

```

#### Implementation
Use the [`asChild` prop](https://www.radix-ui.com/primitives/docs/guides/composition) to convert the trigger part into a slottable area. It will replace the trigger with the child that gets passed to it.

```

// your-tooltip.jsx

import * as React from "react";

import { Tooltip as TooltipPrimitive } from "radix-ui";

export function Tooltip({
	children,
	content,
	open,
	defaultOpen,
	onOpenChange,
	...props
}) {

	return (

		<TooltipPrimitive.Root
			open={open}
			defaultOpen={defaultOpen}
			onOpenChange={onOpenChange}
		>

			<TooltipPrimitive.Trigger asChild>

				{children}

			</TooltipPrimitive.Trigger>

			<TooltipPrimitive.Content side="top" align="center" {...props}>

				{content}

				<TooltipPrimitive.Arrow width={11} height={5} />

			</TooltipPrimitive.Content>

		</TooltipPrimitive.Root>

	);

}

```

#### Quick nav
  * [Anatomy](https://www.radix-ui.com/primitives/docs/components/tooltip#anatomy)
  * [API Reference](https://www.radix-ui.com/primitives/docs/components/tooltip#api-reference)
  * [Provider](https://www.radix-ui.com/primitives/docs/components/tooltip#provider)
  * [Root](https://www.radix-ui.com/primitives/docs/components/tooltip#root)
  * [Trigger](https://www.radix-ui.com/primitives/docs/components/tooltip#trigger)
  * [Portal](https://www.radix-ui.com/primitives/docs/components/tooltip#portal)
  * [Content](https://www.radix-ui.com/primitives/docs/components/tooltip#content)
  * [Arrow](https://www.radix-ui.com/primitives/docs/components/tooltip#arrow)
  * [Examples](https://www.radix-ui.com/primitives/docs/components/tooltip#examples)
  * [Configure globally](https://www.radix-ui.com/primitives/docs/components/tooltip#configure-globally)
  * [Show instantly](https://www.radix-ui.com/primitives/docs/components/tooltip#show-instantly)
  * [Constrain the content size](https://www.radix-ui.com/primitives/docs/components/tooltip#constrain-the-content-size)
  * [Origin-aware animations](https://www.radix-ui.com/primitives/docs/components/tooltip#origin-aware-animations)
  * [Collision-aware animations](https://www.radix-ui.com/primitives/docs/components/tooltip#collision-aware-animations)
  * [Accessibility](https://www.radix-ui.com/primitives/docs/components/tooltip#accessibility)
  * [Keyboard Interactions](https://www.radix-ui.com/primitives/docs/components/tooltip#keyboard-interactions)
  * [Custom APIs](https://www.radix-ui.com/primitives/docs/components/tooltip#custom-apis)
  * [Abstract parts and introduce a content prop](https://www.radix-ui.com/primitives/docs/components/tooltip#abstract-parts-and-introduce-a-content-prop)

Previous[Toolbar](https://www.radix-ui.com/primitives/docs/components/toolbar)
Next[Accessible Icon](https://www.radix-ui.com/primitives/docs/utilities/accessible-icon)
