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
# Slider
An input where the user selects a value from within a given range.
index.jsxindex.jsxstyles.cssstyles.css
CSS

```

import * as React from "react";

import { Slider } from "radix-ui";

import "./styles.css";

const SliderDemo = () => (

	<form>

		<Slider.Root className="SliderRoot" defaultValue={[50]} max={100} step={1}>

			<Slider.Track className="SliderTrack">

				<Slider.Range className="SliderRange" />

			</Slider.Track>

			<Slider.Thumb className="SliderThumb" aria-label="Volume" />

		</Slider.Root>

	</form>

);

export default SliderDemo;

Expand code

```

## Features
  * Can be controlled or uncontrolled.
  * Supports multiple thumbs.
  * Supports a minimum value between thumbs.
  * Supports touch or click on track to update value.
  * Supports Right to Left direction.
  * Full keyboard navigation.

## Component Reference Links
Version: 1.4.0
Size:
[View as Markdown](https://www.radix-ui.com/primitives/docs/components/slider.md)
## [Anatomy](https://www.radix-ui.com/primitives/docs/components/slider#anatomy)
Import all parts and piece them together.

```

import { Slider } from "radix-ui";

export default () => (

	<Slider.Root>

		<Slider.Track>

			<Slider.Range />

		</Slider.Track>

		<Slider.Thumb />

	</Slider.Root>

);

```

## [API Reference](https://www.radix-ui.com/primitives/docs/components/slider#api-reference)
### [Root](https://www.radix-ui.com/primitives/docs/components/slider#root)
Contains all the parts of a slider. It will render an `input` for each thumb when used within a `form` to ensure events propagate correctly.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
|  `defaultValue` Prop description  | `number[]`  | No default value  |
|  `value` Prop description  | `number[]`  | No default value  |
|  `onValueChange` Prop description  |  `function` See full type  | No default value  |
|  `onValueCommit` Prop description  |  `function` See full type  | No default value  |
|  `name` Prop description  | `string`  | No default value  |
|  `disabled` Prop description  | `boolean`  | `false`  |
|  `orientation` Prop description  |  `enum` See full type  | `"horizontal"`  |
|  `dir` Prop description  |  `enum` See full type  | No default value  |
|  `inverted` Prop description  | `boolean`  | `false`  |
|  `min` Prop description  | `number`  | `0`  |
|  `max` Prop description  | `number`  | `100`  |
|  `step` Prop description  | `number`  | `1`  |
|  `minStepsBetweenThumbs` Prop description  | `number`  | `0`  |
|  `form` Prop description  | `string`  | No default value  |
| Data attribute  | Values  |
| --- | --- |
| `[data-disabled]`  | Present when disabled  |
| `[data-orientation]`  | `"vertical"  | "horizontal" `  |
### [Track](https://www.radix-ui.com/primitives/docs/components/slider#track)
The track that contains the `Slider.Range`.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
| Data attribute  | Values  |
| --- | --- |
| `[data-disabled]`  | Present when disabled  |
| `[data-orientation]`  | `"vertical"  | "horizontal" `  |
### [Range](https://www.radix-ui.com/primitives/docs/components/slider#range)
The range part. Must live inside `Slider.Track`.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
| Data attribute  | Values  |
| --- | --- |
| `[data-disabled]`  | Present when disabled  |
| `[data-orientation]`  | `"vertical"  | "horizontal" `  |
### [Thumb](https://www.radix-ui.com/primitives/docs/components/slider#thumb)
A draggable thumb. You can render multiple thumbs.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
| Data attribute  | Values  |
| --- | --- |
| `[data-disabled]`  | Present when disabled  |
| `[data-orientation]`  | `"vertical"  | "horizontal" `  |
## [Examples](https://www.radix-ui.com/primitives/docs/components/slider#examples)
### [Vertical orientation](https://www.radix-ui.com/primitives/docs/components/slider#vertical-orientation)
Use the `orientation` prop to create a vertical slider.

```

// index.jsx

import { Slider } from "radix-ui";

import "./styles.css";

export default () => (

	<Slider.Root
		className="SliderRoot"
		defaultValue={[50]}
		orientation="vertical"
	>

		<Slider.Track className="SliderTrack">

			<Slider.Range className="SliderRange" />

		</Slider.Track>

		<Slider.Thumb className="SliderThumb" />

	</Slider.Root>

);

```

```

/* styles.css */

.SliderRoot {

	position: relative;

	display: flex;

	align-items: center;

}

.SliderRoot[data-orientation="vertical"] {

	flex-direction: column;

	width: 20px;

	height: 100px;

}

.SliderTrack {

	position: relative;

	flex-grow: 1;

	background-color: grey;

}

.SliderTrack[data-orientation="vertical"] {

	width: 3px;

}

.SliderRange {

	position: absolute;

	background-color: black;

}

.SliderRange[data-orientation="vertical"] {

	width: 100%;

}

.SliderThumb {

	display: block;

	width: 20px;

	height: 20px;

	background-color: black;

}

```

### [Create a range](https://www.radix-ui.com/primitives/docs/components/slider#create-a-range)
Add multiple thumbs and values to create a range slider.

```

import { Slider } from "radix-ui";

export default () => (

	<Slider.Root defaultValue={[25, 75]}>

		<Slider.Track>

			<Slider.Range />

		</Slider.Track>

		<Slider.Thumb />

		<Slider.Thumb />

	</Slider.Root>

);

```

### [Define step size](https://www.radix-ui.com/primitives/docs/components/slider#define-step-size)
Use the `step` prop to increase the stepping interval.

```

import { Slider } from "radix-ui";

export default () => (

	<Slider.Root defaultValue={[50]} step={10}>

		<Slider.Track>

			<Slider.Range />

		</Slider.Track>

		<Slider.Thumb />

	</Slider.Root>

);

```

### [Prevent thumb overlap](https://www.radix-ui.com/primitives/docs/components/slider#prevent-thumb-overlap)
Use `minStepsBetweenThumbs` to avoid thumbs with equal values.

```

import { Slider } from "radix-ui";

export default () => (

	<Slider.Root defaultValue={[25, 75]} step={10} minStepsBetweenThumbs={1}>

		<Slider.Track>

			<Slider.Range />

		</Slider.Track>

		<Slider.Thumb />

		<Slider.Thumb />

	</Slider.Root>

);

```

## [Accessibility](https://www.radix-ui.com/primitives/docs/components/slider#accessibility)
Adheres to the
### [Keyboard Interactions](https://www.radix-ui.com/primitives/docs/components/slider#keyboard-interactions)
| Key  | Description  |
| --- | --- |
| `ArrowRight`  | Increments/decrements by the `step` value depending on `orientation`.  |
| `ArrowLeft`  | Increments/decrements by the `step` value depending on `orientation`.  |
| `ArrowUp`  | Increases the value by the `step` amount.  |
| `ArrowDown`  | Decreases the value by the `step` amount.  |
| `PageUp`  | Increases the value by a larger `step`.  |
| `PageDown`  | Decreases the value by a larger `step`.  |
| `Shift + ArrowUp`  | Increases the value by a larger `step`.  |
| `Shift + ArrowDown`  | Decreases the value by a larger `step`.  |
| `Home`  | Sets the value to its minimum.  |
| `End`  | Sets the value to its maximum.  |
## [Custom APIs](https://www.radix-ui.com/primitives/docs/components/slider#custom-apis)
Create your own API by abstracting the primitive parts into your own component.
### [Abstract all parts](https://www.radix-ui.com/primitives/docs/components/slider#abstract-all-parts)
This example abstracts all of the `Slider` parts so it can be used as a self closing element.
#### Usage

```

import { Slider } from "./your-slider";

export default () => <Slider defaultValue={[25]} />;

```

#### Implementation

```

// your-slider.jsx

import { Slider as SliderPrimitive } from "radix-ui";

export const Slider = React.forwardRef((props, forwardedRef) => {

	const value = props.value || props.defaultValue;

	return (

		<SliderPrimitive.Slider {...props} ref={forwardedRef}>

			<SliderPrimitive.Track>

				<SliderPrimitive.Range />

			</SliderPrimitive.Track>

			{value.map((_, i) => (

				<SliderPrimitive.Thumb key={i} />

			))}

		</SliderPrimitive.Slider>

	);

});

```

## [Caveats](https://www.radix-ui.com/primitives/docs/components/slider#caveats)
### [Mouse events are not fired](https://www.radix-ui.com/primitives/docs/components/slider#mouse-events-are-not-fired)
Because of `onMouseDown` and `onMouseUp` event handlers won't be fired:

```

<Slider.Root
	onMouseDown={() => console.log("onMouseDown")}
	onMouseUp={() => console.log("onMouseUp")}
>

	…

</Slider.Root>

```

We recommend using pointer events instead (eg. `onPointerDown`, `onPointerUp`). Regardless of the above limitation, these events are better suited for cross-platform/device handling as they are fired for all pointer input types (mouse, touch, pen, etc.).
#### Quick nav
  * [Anatomy](https://www.radix-ui.com/primitives/docs/components/slider#anatomy)
  * [API Reference](https://www.radix-ui.com/primitives/docs/components/slider#api-reference)
  * [Root](https://www.radix-ui.com/primitives/docs/components/slider#root)
  * [Track](https://www.radix-ui.com/primitives/docs/components/slider#track)
  * [Range](https://www.radix-ui.com/primitives/docs/components/slider#range)
  * [Thumb](https://www.radix-ui.com/primitives/docs/components/slider#thumb)
  * [Examples](https://www.radix-ui.com/primitives/docs/components/slider#examples)
  * [Vertical orientation](https://www.radix-ui.com/primitives/docs/components/slider#vertical-orientation)
  * [Create a range](https://www.radix-ui.com/primitives/docs/components/slider#create-a-range)
  * [Define step size](https://www.radix-ui.com/primitives/docs/components/slider#define-step-size)
  * [Prevent thumb overlap](https://www.radix-ui.com/primitives/docs/components/slider#prevent-thumb-overlap)
  * [Accessibility](https://www.radix-ui.com/primitives/docs/components/slider#accessibility)
  * [Keyboard Interactions](https://www.radix-ui.com/primitives/docs/components/slider#keyboard-interactions)
  * [Custom APIs](https://www.radix-ui.com/primitives/docs/components/slider#custom-apis)
  * [Abstract all parts](https://www.radix-ui.com/primitives/docs/components/slider#abstract-all-parts)
  * [Caveats](https://www.radix-ui.com/primitives/docs/components/slider#caveats)
  * [Mouse events are not fired](https://www.radix-ui.com/primitives/docs/components/slider#mouse-events-are-not-fired)

Previous[Separator](https://www.radix-ui.com/primitives/docs/components/separator)
Next[Switch](https://www.radix-ui.com/primitives/docs/components/switch)
