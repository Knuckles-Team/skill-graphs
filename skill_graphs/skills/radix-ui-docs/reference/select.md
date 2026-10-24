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
# Select
Displays a list of options for the user to pick from—triggered by a button.
Select a fruit…
index.jsxindex.jsxstyles.cssstyles.css
CSS

```

import * as React from "react";

import { Select } from "radix-ui";

import classnames from "classnames";

import {
	CheckIcon,
	ChevronDownIcon,
	ChevronUpIcon,
} from "@radix-ui/react-icons";

import "./styles.css";

const SelectDemo = () => (

	<Select.Root>

		<Select.Trigger className="SelectTrigger" aria-label="Food">

			<Select.Value placeholder="Select a fruit…" />

			<Select.Icon className="SelectIcon">

				<ChevronDownIcon />

			</Select.Icon>

		</Select.Trigger>

		<Select.Portal>

			<Select.Content className="SelectContent">

				<Select.ScrollUpButton className="SelectScrollButton">

					<ChevronUpIcon />

				</Select.ScrollUpButton>

				<Select.Viewport className="SelectViewport">

					<Select.Group>

						<Select.Label className="SelectLabel">Fruits</Select.Label>

						<SelectItem value="apple">Apple</SelectItem>

						<SelectItem value="banana">Banana</SelectItem>

						<SelectItem value="blueberry">Blueberry</SelectItem>

						<SelectItem value="grapes">Grapes</SelectItem>

						<SelectItem value="pineapple">Pineapple</SelectItem>

					</Select.Group>

					<Select.Separator className="SelectSeparator" />

					<Select.Group>

						<Select.Label className="SelectLabel">Vegetables</Select.Label>

						<SelectItem value="aubergine">Aubergine</SelectItem>

						<SelectItem value="broccoli">Broccoli</SelectItem>

						<SelectItem value="carrot" disabled>

							Carrot

						</SelectItem>

						<SelectItem value="courgette">Courgette</SelectItem>

						<SelectItem value="leek">Leek</SelectItem>

					</Select.Group>

					<Select.Separator className="SelectSeparator" />

					<Select.Group>

						<Select.Label className="SelectLabel">Meat</Select.Label>

						<SelectItem value="beef">Beef</SelectItem>

						<SelectItem value="chicken">Chicken</SelectItem>

						<SelectItem value="lamb">Lamb</SelectItem>

						<SelectItem value="pork">Pork</SelectItem>

					</Select.Group>

				</Select.Viewport>

				<Select.ScrollDownButton className="SelectScrollButton">

					<ChevronDownIcon />

				</Select.ScrollDownButton>

			</Select.Content>

		</Select.Portal>

	</Select.Root>

);

const SelectItem = React.forwardRef(function SelectItem(

	{ children, className, ...props },
	forwardedRef,

) {

	return (

		<Select.Item
			className={classnames("SelectItem", className)}
			{...props}
			ref={forwardedRef}
		>

			<Select.ItemText>{children}</Select.ItemText>

			<Select.ItemIndicator className="SelectItemIndicator">

				<CheckIcon />

			</Select.ItemIndicator>

		</Select.Item>

	);

});

export default SelectDemo;

Expand code

```

## Features
  * Can be controlled or uncontrolled.
  * Offers 2 positioning modes.
  * Supports items, labels, groups of items.
  * Focus is fully managed.
  * Full keyboard navigation.
  * Supports custom placeholder.
  * Typeahead support.
  * Supports Right to Left direction.

## Component Reference Links
Version: 2.3.0
Size:
[View as Markdown](https://www.radix-ui.com/primitives/docs/components/select.md)
## [Anatomy](https://www.radix-ui.com/primitives/docs/components/select#anatomy)
Import all parts and piece them together.

```

import { Select } from "radix-ui";

export default () => (

	<Select.Root>

		<Select.Trigger>

			<Select.Value />

			<Select.Icon />

		</Select.Trigger>

		<Select.Portal>

			<Select.Content>

				<Select.ScrollUpButton />

				<Select.Viewport>

					<Select.Item>

						<Select.ItemText />

						<Select.ItemIndicator />

					</Select.Item>

					<Select.Group>

						<Select.Label />

						<Select.Item>

							<Select.ItemText />

							<Select.ItemIndicator />

						</Select.Item>

					</Select.Group>

					<Select.Separator />

				</Select.Viewport>

				<Select.ScrollDownButton />

				<Select.Arrow />

			</Select.Content>

		</Select.Portal>

	</Select.Root>

);

```

## [API Reference](https://www.radix-ui.com/primitives/docs/components/select#api-reference)
### [Root](https://www.radix-ui.com/primitives/docs/components/select#root)
Contains all the parts of a select.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `defaultValue` Prop description  | `string`  | No default value  |
|  `value` Prop description  | `string`  | No default value  |
|  `onValueChange` Prop description  |  `function` See full type  | No default value  |
|  `defaultOpen` Prop description  | `boolean`  | No default value  |
|  `open` Prop description  | `boolean`  | No default value  |
|  `onOpenChange` Prop description  |  `function` See full type  | No default value  |
|  `dir` Prop description  |  `enum` See full type  | No default value  |
|  `name` Prop description  | `string`  | No default value  |
|  `disabled` Prop description  | `boolean`  | No default value  |
|  `required` Prop description  | `boolean`  | No default value  |
### [Trigger](https://www.radix-ui.com/primitives/docs/components/select#trigger)
The button that toggles the select. The `Select.Content` will position itself by aligning over the trigger.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
| Data attribute  | Values  |
| --- | --- |
| `[data-state]`  | `"open"  | "closed" `  |
| `[data-disabled]`  | Present when disabled  |
| `[data-placeholder]`  | Present when has placeholder  |
### [Value](https://www.radix-ui.com/primitives/docs/components/select#value)
The part that reflects the selected value. By default the selected item's text will be rendered. if you require more control, you can instead control the select and pass your own `children`. It should not be styled to ensure correct positioning. An optional `placeholder` prop is also available for when the select has no value.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
|  `placeholder` Prop description  | `ReactNode`  | No default value  |
### [Icon](https://www.radix-ui.com/primitives/docs/components/select#icon)
A small icon often displayed next to the value as a visual affordance for the fact it can be open. By default renders ▼ but you can use your own icon via `asChild` or use `children`.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
### [Portal](https://www.radix-ui.com/primitives/docs/components/select#portal)
When used, portals the content part into the `body`.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `container` Prop description  | `HTMLElement`  | `document.body`  |
### [Content](https://www.radix-ui.com/primitives/docs/components/select#content)
The component that pops out when the select is open.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
|  `onCloseAutoFocus` Prop description  |  `function` See full type  | No default value  |
|  `onEscapeKeyDown` Prop description  |  `function` See full type  | No default value  |
|  `onPointerDownOutside` Prop description  |  `function` See full type  | No default value  |
|  `position` Prop description  |  `enum` See full type  | `"item-aligned"`  |
|  `side` Prop description  |  `enum` See full type  | `"bottom"`  |
|  `sideOffset` Prop description  | `number`  | `0`  |
|  `align` Prop description  |  `enum` See full type  | `"start"`  |
|  `alignOffset` Prop description  | `number`  | `0`  |
|  `avoidCollisions` Prop description  | `boolean`  | `true`  |
|  `collisionBoundary` Prop description  |  `Boundary` See full type  | `[]`  |
|  `collisionPadding` Prop description  |  `number | Padding` See full type  | `10`  |
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
| `--radix-select-content-transform-origin`  | The `transform-origin` computed from the content and arrow positions/offsets. Only present when `position="popper"`.  |
| `--radix-select-content-available-width`  | The remaining width between the trigger and the boundary edge. Only present when `position="popper"`.  |
| `--radix-select-content-available-height`  | The remaining height between the trigger and the boundary edge. Only present when `position="popper"`.  |
| `--radix-select-trigger-width`  | The width of the trigger. Only present when `position="popper"`.  |
| `--radix-select-trigger-height`  | The height of the trigger. Only present when `position="popper"`.  |
### [Viewport](https://www.radix-ui.com/primitives/docs/components/select#viewport)
The scrolling viewport that contains all of the items.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
### [Item](https://www.radix-ui.com/primitives/docs/components/select#item)
The component that contains the select items.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
|  `value*` Prop description  | `string`  | No default value  |
|  `disabled` Prop description  | `boolean`  | No default value  |
|  `textValue` Prop description  | `string`  | No default value  |
| Data attribute  | Values  |
| --- | --- |
| `[data-state]`  | `"checked"  | "unchecked" `  |
| `[data-highlighted]`  | Present when highlighted  |
| `[data-disabled]`  | Present when disabled  |
### [ItemText](https://www.radix-ui.com/primitives/docs/components/select#itemtext)
The textual part of the item. It should only contain the text you want to see in the trigger when that item is selected. It should not be styled to ensure correct positioning.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
### [ItemIndicator](https://www.radix-ui.com/primitives/docs/components/select#itemindicator)
Renders when the item is selected. You can style this element directly, or you can use it as a wrapper to put an icon into, or both.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
### [ScrollUpButton](https://www.radix-ui.com/primitives/docs/components/select#scrollupbutton)
An optional button used as an affordance to show the viewport overflow as well as functionally enable scrolling upwards.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
### [ScrollDownButton](https://www.radix-ui.com/primitives/docs/components/select#scrolldownbutton)
An optional button used as an affordance to show the viewport overflow as well as functionally enable scrolling downwards.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
### [Group](https://www.radix-ui.com/primitives/docs/components/select#group)
Used to group multiple items. use in conjunction with `Select.Label` to ensure good accessibility via automatic labelling.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
### [Label](https://www.radix-ui.com/primitives/docs/components/select#label)
Used to render the label of a group. It won't be focusable using arrow keys.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
### [Separator](https://www.radix-ui.com/primitives/docs/components/select#separator)
Used to visually separate items in the select.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
### [Arrow](https://www.radix-ui.com/primitives/docs/components/select#arrow)
An optional arrow element to render alongside the content. This can be used to help visually link the trigger with the `Select.Content`. Must be rendered inside `Select.Content`. Only available when `position` is set to `popper`.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
|  `width` Prop description  | `number`  | `10`  |
|  `height` Prop description  | `number`  | `5`  |
## [Examples](https://www.radix-ui.com/primitives/docs/components/select#examples)
### [Change the positioning mode](https://www.radix-ui.com/primitives/docs/components/select#change-the-positioning-mode)
By default, `Select` will behave similarly to a native MacOS menu by positioning `Select.Content` relative to the active item. If you would prefer an alternative positioning approach similar to `Popover` or `DropdownMenu` then you can set `position` to `popper` and make use of additional alignment options such as `side`, `sideOffset` and more.

```

// index.jsx

import { Select } from "radix-ui";

export default () => (

	<Select.Root>

		<Select.Trigger>…</Select.Trigger>

		<Select.Portal>

			<Select.Content position="popper" sideOffset={5}>

				…

			</Select.Content>

		</Select.Portal>

	</Select.Root>

);

```

### [Constrain the content size](https://www.radix-ui.com/primitives/docs/components/select#constrain-the-content-size)
When using `position="popper"` on `Select.Content`, you may want to constrain the width of the content so that it matches the trigger width. You may also want to constrain its height to not exceed the viewport.
We expose several CSS custom properties such as `--radix-select-trigger-width` and `--radix-select-content-available-height` to support this. Use them to constrain the content dimensions.

```

// index.jsx

import { Select } from "radix-ui";

import "./styles.css";

export default () => (

	<Select.Root>

		<Select.Trigger>…</Select.Trigger>

		<Select.Portal>

			<Select.Content
				className="SelectContent"
				position="popper"
				sideOffset={5}
			>

				…

			</Select.Content>

		</Select.Portal>

	</Select.Root>

);

```

```

/* styles.css */

.SelectContent {

	width: var(--radix-select-trigger-width);

	max-height: var(--radix-select-content-available-height);

}

```

### [With disabled items](https://www.radix-ui.com/primitives/docs/components/select#with-disabled-items)
You can add special styles to disabled items via the `data-disabled` attribute.

```

// index.jsx

import { Select } from "radix-ui";

import "./styles.css";

export default () => (

	<Select.Root>

		<Select.Trigger>…</Select.Trigger>

		<Select.Portal>

			<Select.Content>

				<Select.Viewport>

					<Select.Item className="SelectItem" disabled>

						…

					</Select.Item>

					<Select.Item>…</Select.Item>

					<Select.Item>…</Select.Item>

				</Select.Viewport>

			</Select.Content>

		</Select.Portal>

	</Select.Root>

);

```

```

/* styles.css */

.SelectItem[data-disabled] {

	color: "gainsboro";

}

```

### [With a placeholder](https://www.radix-ui.com/primitives/docs/components/select#with-a-placeholder)
You can use the `placeholder` prop on `Value` for when the select has no value. There's also a `data-placeholder` attribute on `Trigger` to help with styling.

```

// index.jsx

import { Select } from "radix-ui";

import "./styles.css";

export default () => (

	<Select.Root>

		<Select.Trigger className="SelectTrigger">

			<Select.Value placeholder="Pick an option" />

			<Select.Icon />

		</Select.Trigger>

		<Select.Portal>

			<Select.Content>…</Select.Content>

		</Select.Portal>

	</Select.Root>

);

```

```

/* styles.css */

.SelectTrigger[data-placeholder] {

	color: "gainsboro";

}

```

### [With separators](https://www.radix-ui.com/primitives/docs/components/select#with-separators)
Use the `Separator` part to add a separator between items.

```

<Select.Root>

	<Select.Trigger>…</Select.Trigger>

	<Select.Portal>

		<Select.Content>

			<Select.Viewport>

				<Select.Item>…</Select.Item>

				<Select.Item>…</Select.Item>

				<Select.Item>…</Select.Item>

				<Select.Separator />

				<Select.Item>…</Select.Item>

				<Select.Item>…</Select.Item>

			</Select.Viewport>

		</Select.Content>

	</Select.Portal>

</Select.Root>

```

### [With grouped items](https://www.radix-ui.com/primitives/docs/components/select#with-grouped-items)
Use the `Group` and `Label` parts to group items in a section.

```

<Select.Root>

	<Select.Trigger>…</Select.Trigger>

	<Select.Portal>

		<Select.Content>

			<Select.Viewport>

				<Select.Group>

					<Select.Label>Label</Select.Label>

					<Select.Item>…</Select.Item>

					<Select.Item>…</Select.Item>

					<Select.Item>…</Select.Item>

				</Select.Group>

			</Select.Viewport>

		</Select.Content>

	</Select.Portal>

</Select.Root>

```

### [With complex items](https://www.radix-ui.com/primitives/docs/components/select#with-complex-items)
You can use custom content in your items.

```

import { Select } from "radix-ui";

export default () => (

	<Select.Root>

		<Select.Trigger>…</Select.Trigger>

		<Select.Portal>

			<Select.Content>

				<Select.Viewport>

					<Select.Item>

						<Select.ItemText>

							<img src="…" />

							Adolfo Hess

						</Select.ItemText>

						<Select.ItemIndicator>…</Select.ItemIndicator>

					</Select.Item>

					<Select.Item>…</Select.Item>

					<Select.Item>…</Select.Item>

				</Select.Viewport>

			</Select.Content>

		</Select.Portal>

	</Select.Root>

);

```

### [Controlling the value displayed in the trigger](https://www.radix-ui.com/primitives/docs/components/select#controlling-the-value-displayed-in-the-trigger)
By default the trigger will automatically display the selected item `ItemText`'s content. You can control what appears by chosing to put things inside/outside the `ItemText` part.
If you need more flexibility, you can control the component using `value`/`onValueChange` props and passing `children` to `SelectValue`. Remember to make sure what you put in there is accessible.

```

const countries = { france: "🇫🇷", "united-kingdom": "🇬🇧", spain: "🇪🇸" };

export default () => {

	const [value, setValue] = React.useState("france");

	return (

		<Select.Root value={value} onValueChange={setValue}>

			<Select.Trigger>

				<Select.Value aria-label={value}>

					{countries[value]}

				</Select.Value>

				<Select.Icon />

			</Select.Trigger>

			<Select.Portal>

			<Select.Content>

				<Select.Viewport>

					<Select.Item value="france">

						<Select.ItemText>France</Select.ItemText>

						<Select.ItemIndicator>…</Select.ItemIndicator>

					</Select.Item>

					<Select.Item value="united-kingdom">

						<Select.ItemText>United Kingdom</Select.ItemText>

						<Select.ItemIndicator>…</Select.ItemIndicator>

					</Select.Item>

					<Select.Item value="spain">

						<Select.ItemText>Spain</Select.ItemText>

						<Select.ItemIndicator>…</Select.ItemIndicator>

					</Select.Item>

				</Select.Viewport>

			</Select.Content>

			</Select.Portal>

		</Select.Root>

	);

};

```

### [With custom scrollbar](https://www.radix-ui.com/primitives/docs/components/select#with-custom-scrollbar)
The native scrollbar is hidden by default as we recommend using the `ScrollUpButton` and `ScrollDownButton` parts for the best UX. If you do not want to use these parts, compose your select with our [Scroll Area](https://www.radix-ui.com/primitives/docs/components/scroll-area) primitive.

```

// index.jsx

import { Select, ScrollArea } from "radix-ui";

import "./styles.css";

export default () => (

	<Select.Root>

		<Select.Trigger>…</Select.Trigger>

		<Select.Portal>

			<Select.Content>

				<ScrollArea.Root className="ScrollAreaRoot" type="auto">

					<Select.Viewport asChild>

						<ScrollArea.Viewport className="ScrollAreaViewport">

							<StyledItem>…</StyledItem>

							<StyledItem>…</StyledItem>

							<StyledItem>…</StyledItem>

						</ScrollArea.Viewport>

					</Select.Viewport>

					<ScrollArea.Scrollbar
						className="ScrollAreaScrollbar"
						orientation="vertical"
					>

						<ScrollArea.Thumb className="ScrollAreaThumb" />

					</ScrollArea.Scrollbar>

				</ScrollArea.Root>

			</Select.Content>

		</Select.Portal>

	</Select.Root>

);

```

```

/* styles.css */

.ScrollAreaRoot {

	width: 100%;

	height: 100%;

}

.ScrollAreaViewport {

	width: 100%;

	height: 100%;

}

.ScrollAreaScrollbar {

	width: 4px;

	padding: 5px 2px;

}

.ScrollAreaThumb {

	background: rgba(0, 0, 0, 0.3);

	border-radius: 3px;

}

```

## [Accessibility](https://www.radix-ui.com/primitives/docs/components/select#accessibility)
Adheres to the
See the W3C
### [Keyboard Interactions](https://www.radix-ui.com/primitives/docs/components/select#keyboard-interactions)
| Key  | Description  |
| --- | --- |
| `Space`  | When focus is on `Select.Trigger`, opens the select and focuses the selected item.
When focus is on an item, selects the focused item.  |
| `Enter`  | When focus is on `Select.Trigger`, opens the select and focuses the first item.
When focus is on an item, selects the focused item.  |
| `ArrowDown`  | When focus is on `Select.Trigger`, opens the select.
When focus is on an item, moves focus to the next item.  |
| `ArrowUp`  | When focus is on `Select.Trigger`, opens the select.
When focus is on an item, moves focus to the previous item.  |
| `Esc`  | Closes the select and moves focus to `Select.Trigger`.  |
### [Labelling](https://www.radix-ui.com/primitives/docs/components/select#labelling)
Use our [Label](https://www.radix-ui.com/primitives/docs/components/label) component in order to offer a visual and accessible label for the select.

```

import { Select, Label } from "radix-ui";

export default () => (

	<>

		<Label>

			Country

			<Select.Root>…</Select.Root>

		</Label>

		{/* or */}

		<Label htmlFor="country">Country</Label>

		<Select.Root>

			<Select.Trigger id="country">…</Select.Trigger>

			<Select.Portal>

				<Select.Content>…</Select.Content>

			</Select.Portal>

		</Select.Root>

	</>

);

```

## [Custom APIs](https://www.radix-ui.com/primitives/docs/components/select#custom-apis)
Create your own API by abstracting the primitive parts into your own component.
### [Abstract down to `Select` and `SelectItem`](https://www.radix-ui.com/primitives/docs/components/select#abstract-down-to-select-and-selectitem)
This example abstracts most of the parts.
#### Usage

```

import { Select, SelectItem } from "./your-select";

export default () => (

	<Select defaultValue="2">

		<SelectItem value="1">Item 1</SelectItem>

		<SelectItem value="2">Item 2</SelectItem>

		<SelectItem value="3">Item 3</SelectItem>

	</Select>

);

```

#### Implementation

```

// your-select.jsx

import * as React from "react";

import { Select as SelectPrimitive } from "radix-ui";

import {
	CheckIcon,
	ChevronDownIcon,
	ChevronUpIcon,
} from "@radix-ui/react-icons";

export const Select = React.forwardRef(

	({ children, ...props }, forwardedRef) => {

		return (

			<SelectPrimitive.Root {...props}>

				<SelectPrimitive.Trigger ref={forwardedRef}>

					<SelectPrimitive.Value />

					<SelectPrimitive.Icon>

						<ChevronDownIcon />

					</SelectPrimitive.Icon>

				</SelectPrimitive.Trigger>

				<SelectPrimitive.Portal>

					<SelectPrimitive.Content>

						<SelectPrimitive.ScrollUpButton>

							<ChevronUpIcon />

						</SelectPrimitive.ScrollUpButton>

						<SelectPrimitive.Viewport>{children}</SelectPrimitive.Viewport>

						<SelectPrimitive.ScrollDownButton>

							<ChevronDownIcon />

						</SelectPrimitive.ScrollDownButton>

					</SelectPrimitive.Content>

				</SelectPrimitive.Portal>

			</SelectPrimitive.Root>

		);

	},

);

export const SelectItem = React.forwardRef(

	({ children, ...props }, forwardedRef) => {

		return (

			<SelectPrimitive.Item {...props} ref={forwardedRef}>

				<SelectPrimitive.ItemText>{children}</SelectPrimitive.ItemText>

				<SelectPrimitive.ItemIndicator>

					<CheckIcon />

				</SelectPrimitive.ItemIndicator>

			</SelectPrimitive.Item>

		);

	},

);

```

#### Quick nav
  * [Anatomy](https://www.radix-ui.com/primitives/docs/components/select#anatomy)
  * [API Reference](https://www.radix-ui.com/primitives/docs/components/select#api-reference)
  * [Root](https://www.radix-ui.com/primitives/docs/components/select#root)
  * [Trigger](https://www.radix-ui.com/primitives/docs/components/select#trigger)
  * [Value](https://www.radix-ui.com/primitives/docs/components/select#value)
  * [Icon](https://www.radix-ui.com/primitives/docs/components/select#icon)
  * [Portal](https://www.radix-ui.com/primitives/docs/components/select#portal)
  * [Content](https://www.radix-ui.com/primitives/docs/components/select#content)
  * [Viewport](https://www.radix-ui.com/primitives/docs/components/select#viewport)
  * [Item](https://www.radix-ui.com/primitives/docs/components/select#item)
  * [ItemText](https://www.radix-ui.com/primitives/docs/components/select#itemtext)
  * [ItemIndicator](https://www.radix-ui.com/primitives/docs/components/select#itemindicator)
  * [ScrollUpButton](https://www.radix-ui.com/primitives/docs/components/select#scrollupbutton)
  * [ScrollDownButton](https://www.radix-ui.com/primitives/docs/components/select#scrolldownbutton)
  * [Group](https://www.radix-ui.com/primitives/docs/components/select#group)
  * [Label](https://www.radix-ui.com/primitives/docs/components/select#label)
  * [Separator](https://www.radix-ui.com/primitives/docs/components/select#separator)
  * [Arrow](https://www.radix-ui.com/primitives/docs/components/select#arrow)
  * [Examples](https://www.radix-ui.com/primitives/docs/components/select#examples)
  * [Change the positioning mode](https://www.radix-ui.com/primitives/docs/components/select#change-the-positioning-mode)
  * [Constrain the content size](https://www.radix-ui.com/primitives/docs/components/select#constrain-the-content-size)
  * [With disabled items](https://www.radix-ui.com/primitives/docs/components/select#with-disabled-items)
  * [With a placeholder](https://www.radix-ui.com/primitives/docs/components/select#with-a-placeholder)
  * [With separators](https://www.radix-ui.com/primitives/docs/components/select#with-separators)
  * [With grouped items](https://www.radix-ui.com/primitives/docs/components/select#with-grouped-items)
  * [With complex items](https://www.radix-ui.com/primitives/docs/components/select#with-complex-items)
  * [Controlling the value displayed in the trigger](https://www.radix-ui.com/primitives/docs/components/select#controlling-the-value-displayed-in-the-trigger)
  * [With custom scrollbar](https://www.radix-ui.com/primitives/docs/components/select#with-custom-scrollbar)
  * [Accessibility](https://www.radix-ui.com/primitives/docs/components/select#accessibility)
  * [Keyboard Interactions](https://www.radix-ui.com/primitives/docs/components/select#keyboard-interactions)
  * [Labelling](https://www.radix-ui.com/primitives/docs/components/select#labelling)
  * [Custom APIs](https://www.radix-ui.com/primitives/docs/components/select#custom-apis)
  * [Abstract down to Select and SelectItem](https://www.radix-ui.com/primitives/docs/components/select#abstract-down-to-select-and-selectitem)

Previous[Scroll Area](https://www.radix-ui.com/primitives/docs/components/scroll-area)
Next[Separator](https://www.radix-ui.com/primitives/docs/components/separator)
