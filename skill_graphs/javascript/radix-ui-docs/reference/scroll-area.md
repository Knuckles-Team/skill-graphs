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
# Scroll Area
Augments native scroll functionality for custom, cross-browser styling.
Tags
v1.2.0-beta.50
v1.2.0-beta.49
v1.2.0-beta.48
v1.2.0-beta.47
v1.2.0-beta.46
v1.2.0-beta.45
v1.2.0-beta.44
v1.2.0-beta.43
v1.2.0-beta.42
v1.2.0-beta.41
v1.2.0-beta.40
v1.2.0-beta.39
v1.2.0-beta.38
v1.2.0-beta.37
v1.2.0-beta.36
v1.2.0-beta.35
v1.2.0-beta.34
v1.2.0-beta.33
v1.2.0-beta.32
v1.2.0-beta.31
v1.2.0-beta.30
v1.2.0-beta.29
v1.2.0-beta.28
v1.2.0-beta.27
v1.2.0-beta.26
v1.2.0-beta.25
v1.2.0-beta.24
v1.2.0-beta.23
v1.2.0-beta.22
v1.2.0-beta.21
v1.2.0-beta.20
v1.2.0-beta.19
v1.2.0-beta.18
v1.2.0-beta.17
v1.2.0-beta.16
v1.2.0-beta.15
v1.2.0-beta.14
v1.2.0-beta.13
v1.2.0-beta.12
v1.2.0-beta.11
v1.2.0-beta.10
v1.2.0-beta.9
v1.2.0-beta.8
v1.2.0-beta.7
v1.2.0-beta.6
v1.2.0-beta.5
v1.2.0-beta.4
v1.2.0-beta.3
v1.2.0-beta.2
v1.2.0-beta.1
index.jsxindex.jsxstyles.cssstyles.css
CSS

```

import * as React from "react";

import { ScrollArea } from "radix-ui";

import "./styles.css";

const TAGS = Array.from({ length: 50 }).map(

	(_, i, a) => `v1.2.0-beta.${a.length - i}`,

);

const ScrollAreaDemo = () => (

	<ScrollArea.Root className="ScrollAreaRoot">

		<ScrollArea.Viewport className="ScrollAreaViewport">

			<div style={{ padding: "15px 20px" }}>

				<div className="Text">Tags</div>

				{TAGS.map((tag) => (

					<div className="Tag" key={tag}>

						{tag}

					</div>

				))}

			</div>

		</ScrollArea.Viewport>

		<ScrollArea.Scrollbar
			className="ScrollAreaScrollbar"
			orientation="vertical"
		>

			<ScrollArea.Thumb className="ScrollAreaThumb" />

		</ScrollArea.Scrollbar>

		<ScrollArea.Scrollbar
			className="ScrollAreaScrollbar"
			orientation="horizontal"
		>

			<ScrollArea.Thumb className="ScrollAreaThumb" />

		</ScrollArea.Scrollbar>

		<ScrollArea.Corner className="ScrollAreaCorner" />

	</ScrollArea.Root>

);

export default ScrollAreaDemo;

Expand code

```

## Features
  * Scrollbar sits on top of the scrollable content, taking up no space.
  * Scrolling is native; no underlying position movements via CSS transformations.
  * Shims pointer behaviors only when interacting with the controls, so keyboard controls are unaffected.
  * Supports Right to Left direction.

## Component Reference Links
Version: 1.2.11
Size:
[View as Markdown](https://www.radix-ui.com/primitives/docs/components/scroll-area.md)
## [Anatomy](https://www.radix-ui.com/primitives/docs/components/scroll-area#anatomy)
Import all parts and piece them together.

```

import { ScrollArea } from "radix-ui";

export default () => (

	<ScrollArea.Root>

		<ScrollArea.Viewport />

		<ScrollArea.Scrollbar orientation="horizontal">

			<ScrollArea.Thumb />

		</ScrollArea.Scrollbar>

		<ScrollArea.Scrollbar orientation="vertical">

			<ScrollArea.Thumb />

		</ScrollArea.Scrollbar>

		<ScrollArea.Corner />

	</ScrollArea.Root>

);

```

## [API Reference](https://www.radix-ui.com/primitives/docs/components/scroll-area#api-reference)
### [Root](https://www.radix-ui.com/primitives/docs/components/scroll-area#root)
Contains all the parts of a scroll area.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
|  `type` Prop description  |  `enum` See full type  | `"hover"`  |
|  `scrollHideDelay` Prop description  | `number`  | `600`  |
|  `dir` Prop description  |  `enum` See full type  | No default value  |
|  `nonce` Prop description  | `string`  | No default value  |
### [Viewport](https://www.radix-ui.com/primitives/docs/components/scroll-area#viewport)
The viewport area of the scroll area.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
### [Scrollbar](https://www.radix-ui.com/primitives/docs/components/scroll-area#scrollbar)
The vertical scrollbar. Add a second `Scrollbar` with an `orientation` prop to enable horizontal scrolling.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
|  `forceMount` Prop description  | `boolean`  | No default value  |
|  `orientation` Prop description  |  `enum` See full type  | `vertical`  |
| Data attribute  | Values  |
| --- | --- |
| `[data-state]`  | `"visible"  | "hidden" `  |
| `[data-orientation]`  | `"vertical"  | "horizontal" `  |
### [Thumb](https://www.radix-ui.com/primitives/docs/components/scroll-area#thumb)
The thumb to be used in `ScrollArea.Scrollbar`.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
| Data attribute  | Values  |
| --- | --- |
| `[data-state]`  | `"visible"  | "hidden" `  |
### [Corner](https://www.radix-ui.com/primitives/docs/components/scroll-area#corner)
The corner where both vertical and horizontal scrollbars meet.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
## [Accessibility](https://www.radix-ui.com/primitives/docs/components/scroll-area#accessibility)
In most cases, it's best to rely on native scrolling and work with the customization options available in CSS. When that isn't enough, `ScrollArea` provides additional customizability while maintaining the browser's native scroll behavior (as well as accessibility features, like keyboard scrolling).
### [Keyboard Interactions](https://www.radix-ui.com/primitives/docs/components/scroll-area#keyboard-interactions)
Scrolling via keyboard is supported by default because the component relies on native scrolling. Specific keyboard interactions may differ between platforms, so we do not specify them here or add specific event listeners to handle scrolling via key events.
#### Quick nav
  * [Anatomy](https://www.radix-ui.com/primitives/docs/components/scroll-area#anatomy)
  * [API Reference](https://www.radix-ui.com/primitives/docs/components/scroll-area#api-reference)
  * [Root](https://www.radix-ui.com/primitives/docs/components/scroll-area#root)
  * [Viewport](https://www.radix-ui.com/primitives/docs/components/scroll-area#viewport)
  * [Scrollbar](https://www.radix-ui.com/primitives/docs/components/scroll-area#scrollbar)
  * [Thumb](https://www.radix-ui.com/primitives/docs/components/scroll-area#thumb)
  * [Corner](https://www.radix-ui.com/primitives/docs/components/scroll-area#corner)
  * [Accessibility](https://www.radix-ui.com/primitives/docs/components/scroll-area#accessibility)
  * [Keyboard Interactions](https://www.radix-ui.com/primitives/docs/components/scroll-area#keyboard-interactions)

Previous[Radio Group](https://www.radix-ui.com/primitives/docs/components/radio-group)
Next[Select](https://www.radix-ui.com/primitives/docs/components/select)
