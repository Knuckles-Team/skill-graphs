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
# Progress
Displays an indicator showing the completion progress of a task, typically displayed as a progress bar.
index.jsxindex.jsxstyles.cssstyles.css
CSS

```

import * as React from "react";

import { Progress } from "radix-ui";

import "./styles.css";

const ProgressDemo = () => {

	const [progress, setProgress] = React.useState(13);

	React.useEffect(() => {

		const timer = setTimeout(() => setProgress(66), 500);

		return () => clearTimeout(timer);

	}, []);

	return (

		<Progress.Root className="ProgressRoot" value={progress}>

			<Progress.Indicator
				className="ProgressIndicator"
				style={{ transform: `translateX(-${100 - progress}%)` }}
			/>

		</Progress.Root>

	);

};

export default ProgressDemo;

Expand code

```

## Features
  * Provides context for assistive technology to read the progress of a task.

## Component Reference Links
Version: 1.1.9
Size:
[View as Markdown](https://www.radix-ui.com/primitives/docs/components/progress.md)
### [Anatomy](https://www.radix-ui.com/primitives/docs/components/progress#anatomy)
Import all parts and piece them together.

```

import { Progress } from "radix-ui";

export default () => (

	<Progress.Root>

		<Progress.Indicator />

	</Progress.Root>

);

```

## [Accessibility](https://www.radix-ui.com/primitives/docs/components/progress#accessibility)
Adheres to the
## [API Reference](https://www.radix-ui.com/primitives/docs/components/progress#api-reference)
### [Root](https://www.radix-ui.com/primitives/docs/components/progress#root)
Contains all of the progress parts.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
|  `value` Prop description  | `number | null`  | No default value  |
|  `max` Prop description  | `number`  | No default value  |
|  `getValueLabel` Prop description  |  `function` See full type  | No default value  |
| Data attribute  | Values  |
| --- | --- |
| `[data-state]`  | `"complete"  | "indeterminate"  | "loading" `  |
| `[data-value]`  | The current value  |
| `[data-max]`  | The max value  |
### [Indicator](https://www.radix-ui.com/primitives/docs/components/progress#indicator)
Used to show the progress visually. It also makes progress accessible to assistive technologies.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
| Data attribute  | Values  |
| --- | --- |
| `[data-state]`  | `"complete"  | "indeterminate"  | "loading" `  |
| `[data-value]`  | The current value  |
| `[data-max]`  | The max value  |
#### Quick nav
  * [Anatomy](https://www.radix-ui.com/primitives/docs/components/progress#anatomy)
  * [Accessibility](https://www.radix-ui.com/primitives/docs/components/progress#accessibility)
  * [API Reference](https://www.radix-ui.com/primitives/docs/components/progress#api-reference)
  * [Root](https://www.radix-ui.com/primitives/docs/components/progress#root)
  * [Indicator](https://www.radix-ui.com/primitives/docs/components/progress#indicator)

Previous[Popover](https://www.radix-ui.com/primitives/docs/components/popover)
Next[Radio Group](https://www.radix-ui.com/primitives/docs/components/radio-group)
