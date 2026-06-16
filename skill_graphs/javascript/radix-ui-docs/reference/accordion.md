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
# Accordion
A vertically stacked set of interactive headings that each reveal an associated section of content.
### Is it accessible?
Yes. It adheres to the WAI-ARIA design pattern.
### Is it unstyled?
### Can it be animated?
index.jsxindex.jsxstyles.cssstyles.css
CSS

```

import * as React from "react";

import { Accordion } from "radix-ui";

import classNames from "classnames";

import { ChevronDownIcon } from "@radix-ui/react-icons";

import "./styles.css";

const AccordionDemo = () => (

	<Accordion.Root
		className="AccordionRoot"
		type="single"
		defaultValue="item-1"
		collapsible
	>

		<Accordion.Item className="AccordionItem" value="item-1">

			<AccordionTrigger>Is it accessible?</AccordionTrigger>

			<AccordionContent>

				Yes. It adheres to the WAI-ARIA design pattern.

			</AccordionContent>

		</Accordion.Item>

		<Accordion.Item className="AccordionItem" value="item-2">

			<AccordionTrigger>Is it unstyled?</AccordionTrigger>

			<AccordionContent>

				Yes. It&apos;s unstyled by default, giving you freedom over the look and

				feel.

			</AccordionContent>

		</Accordion.Item>

		<Accordion.Item className="AccordionItem" value="item-3">

			<AccordionTrigger>Can it be animated?</AccordionTrigger>

			<Accordion.Content className="AccordionContent">

				<div className="AccordionContentText">

					Yes! You can animate the Accordion with CSS or JavaScript.

				</div>

			</Accordion.Content>

		</Accordion.Item>

	</Accordion.Root>

);

const AccordionTrigger = React.forwardRef(function AccordionTrigger(

	{ children, className, ...props },
	forwardedRef,

) {

	return (

		<Accordion.Header className="AccordionHeader">

			<Accordion.Trigger
				className={classNames("AccordionTrigger", className)}
				{...props}
				ref={forwardedRef}
			>

				{children}

				<ChevronDownIcon className="AccordionChevron" aria-hidden />

			</Accordion.Trigger>

		</Accordion.Header>

	);

});

const AccordionContent = React.forwardRef(function AccordionContent(

	{ children, className, ...props },
	forwardedRef,

) {

	return (

		<Accordion.Content
			className={classNames("AccordionContent", className)}
			{...props}
			ref={forwardedRef}
		>

			<div className="AccordionContentText">{children}</div>

		</Accordion.Content>

	);

});

export default AccordionDemo;

Expand code

```

## Features
  * Full keyboard navigation.
  * Supports horizontal/vertical orientation.
  * Supports Right to Left direction.
  * Can expand one or multiple items.
  * Can be controlled or uncontrolled.

## Component Reference Links
Version: 1.2.13
Size:
[View as Markdown](https://www.radix-ui.com/primitives/docs/components/accordion.md)
## [Anatomy](https://www.radix-ui.com/primitives/docs/components/accordion#anatomy)
Import all parts and piece them together.

```

import { Accordion } from "radix-ui";

export default () => (

	<Accordion.Root>

		<Accordion.Item>

			<Accordion.Header>

				<Accordion.Trigger />

			</Accordion.Header>

			<Accordion.Content />

		</Accordion.Item>

	</Accordion.Root>

);

```

## [API Reference](https://www.radix-ui.com/primitives/docs/components/accordion#api-reference)
### [Root](https://www.radix-ui.com/primitives/docs/components/accordion#root)
Contains all the parts of an accordion.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
|  `type*` Prop description  |  `enum` See full type  | No default value  |
|  `value` Prop description  | `string`  | No default value  |
|  `defaultValue` Prop description  | `string`  | No default value  |
|  `onValueChange` Prop description  |  `function` See full type  | No default value  |
|  `value` Prop description  | `string[]`  | `[]`  |
|  `defaultValue` Prop description  | `string[]`  | `[]`  |
|  `onValueChange` Prop description  |  `function` See full type  | No default value  |
|  `collapsible` Prop description  | `boolean`  | `false`  |
|  `disabled` Prop description  | `boolean`  | `false`  |
|  `dir` Prop description  |  `enum` See full type  | `"ltr"`  |
|  `orientation` Prop description  |  `enum` See full type  | `"vertical"`  |
| Data attribute  | Values  |
| --- | --- |
| `[data-orientation]`  | `"vertical"  | "horizontal" `  |
### [Item](https://www.radix-ui.com/primitives/docs/components/accordion#item)
Contains all the parts of a collapsible section.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
|  `disabled` Prop description  | `boolean`  | `false`  |
|  `value*` Prop description  | `string`  | No default value  |
| Data attribute  | Values  |
| --- | --- |
| `[data-state]`  | `"open"  | "closed" `  |
| `[data-disabled]`  | Present when disabled  |
| `[data-orientation]`  | `"vertical"  | "horizontal" `  |
### [Header](https://www.radix-ui.com/primitives/docs/components/accordion#header)
Wraps an `Accordion.Trigger`. Use the `asChild` prop to update it to the appropriate heading level for your page.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
| Data attribute  | Values  |
| --- | --- |
| `[data-state]`  | `"open"  | "closed" `  |
| `[data-disabled]`  | Present when disabled  |
| `[data-orientation]`  | `"vertical"  | "horizontal" `  |
### [Trigger](https://www.radix-ui.com/primitives/docs/components/accordion#trigger)
Toggles the collapsed state of its associated item. It should be nested inside of an `Accordion.Header`.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
| Data attribute  | Values  |
| --- | --- |
| `[data-state]`  | `"open"  | "closed" `  |
| `[data-disabled]`  | Present when disabled  |
| `[data-orientation]`  | `"vertical"  | "horizontal" `  |
### [Content](https://www.radix-ui.com/primitives/docs/components/accordion#content)
Contains the collapsible content for an item.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
|  `forceMount` Prop description  | `boolean`  | No default value  |
| Data attribute  | Values  |
| --- | --- |
| `[data-state]`  | `"open"  | "closed" `  |
| `[data-disabled]`  | Present when disabled  |
| `[data-orientation]`  | `"vertical"  | "horizontal" `  |
| CSS Variable  | Description  |
| --- | --- |
| `--radix-accordion-content-width`  | The width of the content when it opens/closes  |
| `--radix-accordion-content-height`  | The height of the content when it opens/closes  |
## [Examples](https://www.radix-ui.com/primitives/docs/components/accordion#examples)
### [Expanded by default](https://www.radix-ui.com/primitives/docs/components/accordion#expanded-by-default)
Use the `defaultValue` prop to define the open item by default.

```

<Accordion.Root type="single" defaultValue="item-2">

	<Accordion.Item value="item-1">…</Accordion.Item>

	<Accordion.Item value="item-2">…</Accordion.Item>

</Accordion.Root>

```

### [Allow collapsing all items](https://www.radix-ui.com/primitives/docs/components/accordion#allow-collapsing-all-items)
Use the `collapsible` prop to allow all items to close.

```

<Accordion.Root type="single" collapsible>

	<Accordion.Item value="item-1">…</Accordion.Item>

	<Accordion.Item value="item-2">…</Accordion.Item>

</Accordion.Root>

```

### [Multiple items open at the same time](https://www.radix-ui.com/primitives/docs/components/accordion#multiple-items-open-at-the-same-time)
Set the `type` prop to `multiple` to enable opening multiple items at once.

```

<Accordion.Root type="multiple">

	<Accordion.Item value="item-1">…</Accordion.Item>

	<Accordion.Item value="item-2">…</Accordion.Item>

</Accordion.Root>

```

### [Rotated icon when open](https://www.radix-ui.com/primitives/docs/components/accordion#rotated-icon-when-open)
You can add extra decorative elements, such as chevrons, and rotate it when the item is open.

```

// index.jsx

import { Accordion } from "radix-ui";

import { ChevronDownIcon } from "@radix-ui/react-icons";

import "./styles.css";

export default () => (

	<Accordion.Root type="single">

		<Accordion.Item value="item-1">

			<Accordion.Header>

				<Accordion.Trigger className="AccordionTrigger">

					<span>Trigger text</span>

					<ChevronDownIcon className="AccordionChevron" aria-hidden />

				</Accordion.Trigger>

			</Accordion.Header>

			<Accordion.Content>…</Accordion.Content>

		</Accordion.Item>

	</Accordion.Root>

);

```

```

/* styles.css */

.AccordionChevron {

	transition: transform 300ms;

}

.AccordionTrigger[data-state="open"] > .AccordionChevron {

	transform: rotate(180deg);

}

```

### [Horizontal orientation](https://www.radix-ui.com/primitives/docs/components/accordion#horizontal-orientation)
Use the `orientation` prop to create a horizontal accordion.

```

<Accordion.Root orientation="horizontal">

	<Accordion.Item value="item-1">…</Accordion.Item>

	<Accordion.Item value="item-2">…</Accordion.Item>

</Accordion.Root>

```

### [Animating content size](https://www.radix-ui.com/primitives/docs/components/accordion#animating-content-size)
Use the `--radix-accordion-content-width` and/or `--radix-accordion-content-height` CSS variables to animate the size of the content when it opens/closes:

```

// index.jsx

import { Accordion } from "radix-ui";

import "./styles.css";

export default () => (

	<Accordion.Root type="single">

		<Accordion.Item value="item-1">

			<Accordion.Header>…</Accordion.Header>

			<Accordion.Content className="AccordionContent">…</Accordion.Content>

		</Accordion.Item>

	</Accordion.Root>

);

```

```

/* styles.css */

.AccordionContent {

	overflow: hidden;

}

.AccordionContent[data-state="open"] {

	animation: slideDown 300ms ease-out;

}

.AccordionContent[data-state="closed"] {

	animation: slideUp 300ms ease-out;

}

@keyframes slideDown {

	from {

		height: 0;

	}

	to {

		height: var(--radix-accordion-content-height);

	}

}

@keyframes slideUp {

	from {

		height: var(--radix-accordion-content-height);

	}

	to {

		height: 0;

	}

}

```

## [Accessibility](https://www.radix-ui.com/primitives/docs/components/accordion#accessibility)
Adheres to the
### [Keyboard Interactions](https://www.radix-ui.com/primitives/docs/components/accordion#keyboard-interactions)
| Key  | Description  |
| --- | --- |
| `Space`  | When focus is on an `Accordion.Trigger` of a collapsed section, expands the section.  |
| `Enter`  | When focus is on an `Accordion.Trigger` of a collapsed section, expands the section.  |
| `Tab`  | Moves focus to the next focusable element.  |
| `Shift + Tab`  | Moves focus to the previous focusable element.  |
| `ArrowDown`  | Moves focus to the next `Accordion.Trigger` when `orientation` is `vertical`.  |
| `ArrowUp`  | Moves focus to the previous `Accordion.Trigger` when `orientation` is `vertical`.  |
| `ArrowRight`  | Moves focus to the next `Accordion.Trigger` when `orientation` is `horizontal`.  |
| `ArrowLeft`  | Moves focus to the previous `Accordion.Trigger` when `orientation` is `horizontal`.  |
| `Home`  | When focus is on an `Accordion.Trigger`, moves focus to the first `Accordion.Trigger`.  |
| `End`  | When focus is on an `Accordion.Trigger`, moves focus to the last `Accordion.Trigger`.  |
#### Quick nav
  * [Anatomy](https://www.radix-ui.com/primitives/docs/components/accordion#anatomy)
  * [API Reference](https://www.radix-ui.com/primitives/docs/components/accordion#api-reference)
  * [Root](https://www.radix-ui.com/primitives/docs/components/accordion#root)
  * [Item](https://www.radix-ui.com/primitives/docs/components/accordion#item)
  * [Header](https://www.radix-ui.com/primitives/docs/components/accordion#header)
  * [Trigger](https://www.radix-ui.com/primitives/docs/components/accordion#trigger)
  * [Content](https://www.radix-ui.com/primitives/docs/components/accordion#content)
  * [Examples](https://www.radix-ui.com/primitives/docs/components/accordion#examples)
  * [Expanded by default](https://www.radix-ui.com/primitives/docs/components/accordion#expanded-by-default)
  * [Allow collapsing all items](https://www.radix-ui.com/primitives/docs/components/accordion#allow-collapsing-all-items)
  * [Multiple items open at the same time](https://www.radix-ui.com/primitives/docs/components/accordion#multiple-items-open-at-the-same-time)
  * [Rotated icon when open](https://www.radix-ui.com/primitives/docs/components/accordion#rotated-icon-when-open)
  * [Horizontal orientation](https://www.radix-ui.com/primitives/docs/components/accordion#horizontal-orientation)
  * [Animating content size](https://www.radix-ui.com/primitives/docs/components/accordion#animating-content-size)
  * [Accessibility](https://www.radix-ui.com/primitives/docs/components/accordion#accessibility)
  * [Keyboard Interactions](https://www.radix-ui.com/primitives/docs/components/accordion#keyboard-interactions)

Previous[Server-side rendering](https://www.radix-ui.com/primitives/docs/guides/server-side-rendering)
Next[Alert Dialog](https://www.radix-ui.com/primitives/docs/components/alert-dialog)
