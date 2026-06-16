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
# Hover Card
For sighted users to preview content available behind a link.
index.jsxindex.jsxstyles.cssstyles.css
CSS

```

import * as React from "react";

import { HoverCard } from "radix-ui";

import "./styles.css";

const HoverCardDemo = () => (

	<HoverCard.Root>

		<HoverCard.Trigger asChild>

			<a
				className="ImageTrigger"
				href="https://twitter.com/radix_ui"
				target="_blank"
				rel="noreferrer noopener"
			>

				<img
					className="Image normal"
					src="https://pbs.twimg.com/profile_images/1337055608613253126/r_eiMp2H_400x400.png"
					alt="Radix UI"
				/>

			</a>

		</HoverCard.Trigger>

		<HoverCard.Portal>

			<HoverCard.Content className="HoverCardContent" sideOffset={5}>

				<div style={{ display: "flex", flexDirection: "column", gap: 7 }}>

					<img
						className="Image large"
						src="https://pbs.twimg.com/profile_images/1337055608613253126/r_eiMp2H_400x400.png"
						alt="Radix UI"
					/>

					<div style={{ display: "flex", flexDirection: "column", gap: 15 }}>

						<div>

							<div className="Text bold">Radix</div>

							<div className="Text faded">@radix_ui</div>

						</div>

						<div className="Text">

							Components, icons, colors, and templates for building

							high-quality, accessible UI. Free and open-source.

						</div>

						<div style={{ display: "flex", gap: 15 }}>

							<div style={{ display: "flex", gap: 5 }}>

								<div className="Text bold">0</div>{" "}

								<div className="Text faded">Following</div>

							</div>

							<div style={{ display: "flex", gap: 5 }}>

								<div className="Text bold">2,900</div>{" "}

								<div className="Text faded">Followers</div>

							</div>

						</div>

					</div>

				</div>

				<HoverCard.Arrow className="HoverCardArrow" />

			</HoverCard.Content>

		</HoverCard.Portal>

	</HoverCard.Root>

);

export default HoverCardDemo;

Expand code

```

## Features
  * Can be controlled or uncontrolled.
  * Customize side, alignment, offsets, collision handling.
  * Optionally render a pointing arrow.
  * Supports custom open and close delays.
  * Ignored by screen readers.

## Component Reference Links
Version: 1.1.16
Size:
[View as Markdown](https://www.radix-ui.com/primitives/docs/components/hover-card.md)
## [Anatomy](https://www.radix-ui.com/primitives/docs/components/hover-card#anatomy)
Import all parts and piece them together.

```

import { HoverCard } from "radix-ui";

export default () => (

	<HoverCard.Root>

		<HoverCard.Trigger />

		<HoverCard.Portal>

			<HoverCard.Content>

				<HoverCard.Arrow />

			</HoverCard.Content>

		</HoverCard.Portal>

	</HoverCard.Root>

);

```

## [API Reference](https://www.radix-ui.com/primitives/docs/components/hover-card#api-reference)
### [Root](https://www.radix-ui.com/primitives/docs/components/hover-card#root)
Contains all the parts of a hover card.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `defaultOpen` Prop description  | `boolean`  | No default value  |
|  `open` Prop description  | `boolean`  | No default value  |
|  `onOpenChange` Prop description  |  `function` See full type  | No default value  |
|  `openDelay` Prop description  | `number`  | `700`  |
|  `closeDelay` Prop description  | `number`  | `300`  |
### [Trigger](https://www.radix-ui.com/primitives/docs/components/hover-card#trigger)
The link that opens the hover card when hovered.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
| Data attribute  | Values  |
| --- | --- |
| `[data-state]`  | `"open"  | "closed" `  |
### [Portal](https://www.radix-ui.com/primitives/docs/components/hover-card#portal)
When used, portals the content part into the `body`.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `forceMount` Prop description  | `boolean`  | No default value  |
|  `container` Prop description  | `HTMLElement`  | `document.body`  |
### [Content](https://www.radix-ui.com/primitives/docs/components/hover-card#content)
The component that pops out when the hover card is open.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
|  `forceMount` Prop description  | `boolean`  | No default value  |
|  `side` Prop description  |  `enum` See full type  | `"bottom"`  |
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
| `[data-state]`  | `"open"  | "closed" `  |
| `[data-side]`  | `"left"  | "right"  | "bottom"  | "top" `  |
| `[data-align]`  | `"start"  | "end"  | "center" `  |
| CSS Variable  | Description  |
| --- | --- |
| `--radix-hover-card-content-transform-origin`  | The `transform-origin` computed from the content and arrow positions/offsets  |
| `--radix-hover-card-content-available-width`  | The remaining width between the trigger and the boundary edge  |
| `--radix-hover-card-content-available-height`  | The remaining height between the trigger and the boundary edge  |
| `--radix-hover-card-trigger-width`  | The width of the trigger  |
| `--radix-hover-card-trigger-height`  | The height of the trigger  |
### [Arrow](https://www.radix-ui.com/primitives/docs/components/hover-card#arrow)
An optional arrow element to render alongside the hover card. This can be used to help visually link the trigger with the `HoverCard.Content`. Must be rendered inside `HoverCard.Content`.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
|  `width` Prop description  | `number`  | `10`  |
|  `height` Prop description  | `number`  | `5`  |
## [Examples](https://www.radix-ui.com/primitives/docs/components/hover-card#examples)
### [Show instantly](https://www.radix-ui.com/primitives/docs/components/hover-card#show-instantly)
Use the `openDelay` prop to control the time it takes for the hover card to open.

```

import { HoverCard } from "radix-ui";

export default () => (

	<HoverCard.Root openDelay={0}>

		<HoverCard.Trigger>…</HoverCard.Trigger>

		<HoverCard.Content>…</HoverCard.Content>

	</HoverCard.Root>

);

```

### [Constrain the content size](https://www.radix-ui.com/primitives/docs/components/hover-card#constrain-the-content-size)
You may want to constrain the width of the content so that it matches the trigger width. You may also want to constrain its height to not exceed the viewport.
We expose several CSS custom properties such as `--radix-hover-card-trigger-width` and `--radix-hover-card-content-available-height` to support this. Use them to constrain the content dimensions.

```

// index.jsx

import { HoverCard } from "radix-ui";

import "./styles.css";

export default () => (

	<HoverCard.Root>

		<HoverCard.Trigger>…</HoverCard.Trigger>

		<HoverCard.Portal>

			<HoverCard.Content className="HoverCardContent" sideOffset={5}>

				…

			</HoverCard.Content>

		</HoverCard.Portal>

	</HoverCard.Root>

);

```

```

/* styles.css */

.HoverCardContent {

	width: var(--radix-hover-card-trigger-width);

	max-height: var(--radix-hover-card-content-available-height);

}

```

### [Origin-aware animations](https://www.radix-ui.com/primitives/docs/components/hover-card#origin-aware-animations)
We expose a CSS custom property `--radix-hover-card-content-transform-origin`. Use it to animate the content from its computed origin based on `side`, `sideOffset`, `align`, `alignOffset` and any collisions.

```

// index.jsx

import { HoverCard } from "radix-ui";

import "./styles.css";

export default () => (

	<HoverCard.Root>

		<HoverCard.Trigger>…</HoverCard.Trigger>

		<HoverCard.Content className="HoverCardContent">…</HoverCard.Content>

	</HoverCard.Root>

);

```

```

/* styles.css */

.HoverCardContent {

	transform-origin: var(--radix-hover-card-content-transform-origin);

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

### [Collision-aware animations](https://www.radix-ui.com/primitives/docs/components/hover-card#collision-aware-animations)
We expose `data-side` and `data-align` attributes. Their values will change at runtime to reflect collisions. Use them to create collision and direction-aware animations.

```

// index.jsx

import { HoverCard } from "radix-ui";

import "./styles.css";

export default () => (

	<HoverCard.Root>

		<HoverCard.Trigger>…</HoverCard.Trigger>

		<HoverCard.Content className="HoverCardContent">…</HoverCard.Content>

	</HoverCard.Root>

);

```

```

/* styles.css */

.HoverCardContent {

	animation-duration: 0.6s;

	animation-timing-function: cubic-bezier(0.16, 1, 0.3, 1);

}

.HoverCardContent[data-side="top"] {

	animation-name: slideUp;

}

.HoverCardContent[data-side="bottom"] {

	animation-name: slideDown;

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

```

## [Accessibility](https://www.radix-ui.com/primitives/docs/components/hover-card#accessibility)
The hover card is intended for sighted users only, the content will be inaccessible to keyboard users.
### [Keyboard Interactions](https://www.radix-ui.com/primitives/docs/components/hover-card#keyboard-interactions)
| Key  | Description  |
| --- | --- |
| `Tab`  | Opens/closes the hover card.  |
| `Enter`  | Opens the hover card link  |
#### Quick nav
  * [Anatomy](https://www.radix-ui.com/primitives/docs/components/hover-card#anatomy)
  * [API Reference](https://www.radix-ui.com/primitives/docs/components/hover-card#api-reference)
  * [Root](https://www.radix-ui.com/primitives/docs/components/hover-card#root)
  * [Trigger](https://www.radix-ui.com/primitives/docs/components/hover-card#trigger)
  * [Portal](https://www.radix-ui.com/primitives/docs/components/hover-card#portal)
  * [Content](https://www.radix-ui.com/primitives/docs/components/hover-card#content)
  * [Arrow](https://www.radix-ui.com/primitives/docs/components/hover-card#arrow)
  * [Examples](https://www.radix-ui.com/primitives/docs/components/hover-card#examples)
  * [Show instantly](https://www.radix-ui.com/primitives/docs/components/hover-card#show-instantly)
  * [Constrain the content size](https://www.radix-ui.com/primitives/docs/components/hover-card#constrain-the-content-size)
  * [Origin-aware animations](https://www.radix-ui.com/primitives/docs/components/hover-card#origin-aware-animations)
  * [Collision-aware animations](https://www.radix-ui.com/primitives/docs/components/hover-card#collision-aware-animations)
  * [Accessibility](https://www.radix-ui.com/primitives/docs/components/hover-card#accessibility)
  * [Keyboard Interactions](https://www.radix-ui.com/primitives/docs/components/hover-card#keyboard-interactions)

Previous[Form](https://www.radix-ui.com/primitives/docs/components/form)
Next[Label](https://www.radix-ui.com/primitives/docs/components/label)
