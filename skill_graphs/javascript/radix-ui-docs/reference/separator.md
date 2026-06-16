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
# Separator
Visually or semantically separates content.
Radix Primitives
An open-source UI component library.
Blog
Docs
Source
index.jsxindex.jsxstyles.cssstyles.css
CSS

```

import * as React from "react";

import { Separator } from "radix-ui";

import "./styles.css";

const SeparatorDemo = () => (

	<div style={{ width: "100%", maxWidth: 300, margin: "0 15px" }}>

		<div className="Text" style={{ fontWeight: 500 }}>

			Radix Primitives

		</div>

		<div className="Text">An open-source UI component library.</div>

		<Separator.Root className="SeparatorRoot" style={{ margin: "15px 0" }} />

		<div style={{ display: "flex", height: 20, alignItems: "center" }}>

			<div className="Text">Blog</div>

			<Separator.Root
				className="SeparatorRoot"
				decorative
				orientation="vertical"
				style={{ margin: "0 15px" }}
			/>

			<div className="Text">Docs</div>

			<Separator.Root
				className="SeparatorRoot"
				decorative
				orientation="vertical"
				style={{ margin: "0 15px" }}
			/>

			<div className="Text">Source</div>

		</div>

	</div>

);

export default SeparatorDemo;

Expand code

```

## Features
  * Supports horizontal and vertical orientations.

## Component Reference Links
Version: 1.1.9
Size:
[View as Markdown](https://www.radix-ui.com/primitives/docs/components/separator.md)
## [Anatomy](https://www.radix-ui.com/primitives/docs/components/separator#anatomy)
Import all parts and piece them together.

```

import { Separator } from "radix-ui";

export default () => <Separator.Root />;

```

## [API Reference](https://www.radix-ui.com/primitives/docs/components/separator#api-reference)
### [Root](https://www.radix-ui.com/primitives/docs/components/separator#root)
The separator.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
|  `orientation` Prop description  |  `enum` See full type  | `"horizontal"`  |
|  `decorative` Prop description  | `boolean`  | No default value  |
| Data attribute  | Values  |
| --- | --- |
| `[data-orientation]`  | `"vertical"  | "horizontal" `  |
## [Accessibility](https://www.radix-ui.com/primitives/docs/components/separator#accessibility)
Adheres to the
#### Quick nav
  * [Anatomy](https://www.radix-ui.com/primitives/docs/components/separator#anatomy)
  * [API Reference](https://www.radix-ui.com/primitives/docs/components/separator#api-reference)
  * [Root](https://www.radix-ui.com/primitives/docs/components/separator#root)
  * [Accessibility](https://www.radix-ui.com/primitives/docs/components/separator#accessibility)

Previous[Select](https://www.radix-ui.com/primitives/docs/components/select)
Next[Slider](https://www.radix-ui.com/primitives/docs/components/slider)
