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
# Avatar
An image element with a fallback for representing the user.
![Colm Tuite](https://images.unsplash.com/photo-1492633423870-43d1cd2775eb?&w=128&h=128&dpr=2&q=80)![Pedro Duarte](https://images.unsplash.com/photo-1511485977113-f34c92461ad9?ixlib=rb-1.2.1&w=128&h=128&dpr=2&q=80)PD
index.jsxindex.jsxstyles.cssstyles.css
CSS

```

import * as React from "react";

import { Avatar } from "radix-ui";

import "./styles.css";

const AvatarDemo = () => (

	<div style={{ display: "flex", gap: 20 }}>

		<Avatar.Root className="AvatarRoot">

			<Avatar.Image
				className="AvatarImage"
				src="https://images.unsplash.com/photo-1492633423870-43d1cd2775eb?&w=128&h=128&dpr=2&q=80"
				alt="Colm Tuite"
			/>

			<Avatar.Fallback className="AvatarFallback" delayMs={600}>

				CT

			</Avatar.Fallback>

		</Avatar.Root>

		<Avatar.Root className="AvatarRoot">

			<Avatar.Image
				className="AvatarImage"
				src="https://images.unsplash.com/photo-1511485977113-f34c92461ad9?ixlib=rb-1.2.1&w=128&h=128&dpr=2&q=80"
				alt="Pedro Duarte"
			/>

			<Avatar.Fallback className="AvatarFallback" delayMs={600}>

				JD

			</Avatar.Fallback>

		</Avatar.Root>

		<Avatar.Root className="AvatarRoot">

			<Avatar.Fallback className="AvatarFallback">PD</Avatar.Fallback>

		</Avatar.Root>

	</div>

);

export default AvatarDemo;

Expand code

```

## Features
  * Automatic and manual control over when the image renders.
  * Fallback part accepts any children.
  * Optionally delay fallback rendering to avoid content flashing.

## Component Reference Links
Version: 1.1.12
Size:
[View as Markdown](https://www.radix-ui.com/primitives/docs/components/avatar.md)
## [Anatomy](https://www.radix-ui.com/primitives/docs/components/avatar#anatomy)
Import all parts and piece them together.

```

import { Avatar } from "radix-ui";

export default () => (

	<Avatar.Root>

		<Avatar.Image />

		<Avatar.Fallback />

	</Avatar.Root>

);

```

## [API Reference](https://www.radix-ui.com/primitives/docs/components/avatar#api-reference)
### [Root](https://www.radix-ui.com/primitives/docs/components/avatar#root)
Contains all the parts of an avatar.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
### [Image](https://www.radix-ui.com/primitives/docs/components/avatar#image)
The image to render. By default it will only render when it has loaded. You can use the `onLoadingStatusChange` handler if you need more control.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
|  `onLoadingStatusChange` Prop description  |  `function` See full type  | No default value  |
### [Fallback](https://www.radix-ui.com/primitives/docs/components/avatar#fallback)
An element that renders when the image hasn't loaded. This means whilst it's loading, or if there was an error. If you notice a flash during loading, you can provide a `delayMs` prop to delay its rendering so it only renders for those with slower connections. For more control, use the `onLoadingStatusChange` handler on `Avatar.Image`.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
|  `delayMs` Prop description  | `number`  | No default value  |
## [Examples](https://www.radix-ui.com/primitives/docs/components/avatar#examples)
### [Clickable Avatar with tooltip](https://www.radix-ui.com/primitives/docs/components/avatar#clickable-avatar-with-tooltip)
You can compose the Avatar with a [Tooltip](https://www.radix-ui.com/primitives/docs/components/tooltip) to display extra information.

```

import { Avatar, Tooltip } from "radix-ui";

export default () => (

	<Tooltip.Root>

		<Tooltip.Trigger>

			<Avatar.Root>…</Avatar.Root>

		</Tooltip.Trigger>

		<Tooltip.Content side="top">

			Tooltip content

			<Tooltip.Arrow />

		</Tooltip.Content>

	</Tooltip.Root>

);

```

#### Quick nav
  * [Anatomy](https://www.radix-ui.com/primitives/docs/components/avatar#anatomy)
  * [API Reference](https://www.radix-ui.com/primitives/docs/components/avatar#api-reference)
  * [Root](https://www.radix-ui.com/primitives/docs/components/avatar#root)
  * [Image](https://www.radix-ui.com/primitives/docs/components/avatar#image)
  * [Fallback](https://www.radix-ui.com/primitives/docs/components/avatar#fallback)
  * [Examples](https://www.radix-ui.com/primitives/docs/components/avatar#examples)
  * [Clickable Avatar with tooltip](https://www.radix-ui.com/primitives/docs/components/avatar#clickable-avatar-with-tooltip)

Previous[Aspect Ratio](https://www.radix-ui.com/primitives/docs/components/aspect-ratio)
Next[Checkbox](https://www.radix-ui.com/primitives/docs/components/checkbox)
