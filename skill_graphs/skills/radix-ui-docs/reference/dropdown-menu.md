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
# Dropdown Menu
Displays a menu to the user—such as a set of actions or functions—triggered by a button.
index.jsxindex.jsxstyles.cssstyles.css
CSS

```

import * as React from "react";

import { DropdownMenu } from "radix-ui";

import {
	HamburgerMenuIcon,
	DotFilledIcon,
	CheckIcon,
	ChevronRightIcon,
} from "@radix-ui/react-icons";

import "./styles.css";

const DropdownMenuDemo = () => {

	const [bookmarksChecked, setBookmarksChecked] = React.useState(true);

	const [urlsChecked, setUrlsChecked] = React.useState(false);

	const [person, setPerson] = React.useState("pedro");

	return (

		<DropdownMenu.Root>

			<DropdownMenu.Trigger asChild>

				<button className="IconButton" aria-label="Customise options">

					<HamburgerMenuIcon />

				</button>

			</DropdownMenu.Trigger>

			<DropdownMenu.Portal>

				<DropdownMenu.Content className="DropdownMenuContent" sideOffset={5}>

					<DropdownMenu.Item className="DropdownMenuItem">

						New Tab <div className="RightSlot">⌘+T</div>

					</DropdownMenu.Item>

					<DropdownMenu.Item className="DropdownMenuItem">

						New Window <div className="RightSlot">⌘+N</div>

					</DropdownMenu.Item>

					<DropdownMenu.Item className="DropdownMenuItem" disabled>

						New Private Window <div className="RightSlot">⇧+⌘+N</div>

					</DropdownMenu.Item>

					<DropdownMenu.Sub>

						<DropdownMenu.SubTrigger className="DropdownMenuSubTrigger">

							More Tools

							<div className="RightSlot">

								<ChevronRightIcon />

							</div>

						</DropdownMenu.SubTrigger>

						<DropdownMenu.Portal>

							<DropdownMenu.SubContent
								className="DropdownMenuSubContent"
								sideOffset={2}
								alignOffset={-5}
							>

								<DropdownMenu.Item className="DropdownMenuItem">

									Save Page As… <div className="RightSlot">⌘+S</div>

								</DropdownMenu.Item>

								<DropdownMenu.Item className="DropdownMenuItem">

									Create Shortcut…

								</DropdownMenu.Item>

								<DropdownMenu.Item className="DropdownMenuItem">

									Name Window…

								</DropdownMenu.Item>

								<DropdownMenu.Separator className="DropdownMenu.Separator" />

								<DropdownMenu.Item className="DropdownMenuItem">

									Developer Tools

								</DropdownMenu.Item>

							</DropdownMenu.SubContent>

						</DropdownMenu.Portal>

					</DropdownMenu.Sub>

					<DropdownMenu.Separator className="DropdownMenuSeparator" />

					<DropdownMenu.CheckboxItem
						className="DropdownMenuCheckboxItem"
						checked={bookmarksChecked}
						onCheckedChange={setBookmarksChecked}
					>

						<DropdownMenu.ItemIndicator className="DropdownMenuItemIndicator">

							<CheckIcon />

						</DropdownMenu.ItemIndicator>

						Show Bookmarks <div className="RightSlot">⌘+B</div>

					</DropdownMenu.CheckboxItem>

					<DropdownMenu.CheckboxItem
						className="DropdownMenuCheckboxItem"
						checked={urlsChecked}
						onCheckedChange={setUrlsChecked}
					>

						<DropdownMenu.ItemIndicator className="DropdownMenuItemIndicator">

							<CheckIcon />

						</DropdownMenu.ItemIndicator>

						Show Full URLs

					</DropdownMenu.CheckboxItem>

					<DropdownMenu.Separator className="DropdownMenuSeparator" />

					<DropdownMenu.Label className="DropdownMenuLabel">

						People

					</DropdownMenu.Label>

					<DropdownMenu.RadioGroup value={person} onValueChange={setPerson}>

						<DropdownMenu.RadioItem
							className="DropdownMenuRadioItem"
							value="pedro"
						>

							<DropdownMenu.ItemIndicator className="DropdownMenuItemIndicator">

								<DotFilledIcon />

							</DropdownMenu.ItemIndicator>

							Pedro Duarte

						</DropdownMenu.RadioItem>

						<DropdownMenu.RadioItem
							className="DropdownMenuRadioItem"
							value="colm"
						>

							<DropdownMenu.ItemIndicator className="DropdownMenuItemIndicator">

								<DotFilledIcon />

							</DropdownMenu.ItemIndicator>

							Colm Tuite

						</DropdownMenu.RadioItem>

					</DropdownMenu.RadioGroup>

					<DropdownMenu.Arrow className="DropdownMenuArrow" />

				</DropdownMenu.Content>

			</DropdownMenu.Portal>

		</DropdownMenu.Root>

	);

};

export default DropdownMenuDemo;

Expand code

```

## Features
  * Can be controlled or uncontrolled.
  * Supports submenus with configurable reading direction.
  * Supports items, labels, groups of items.
  * Supports checkable items (single or multiple) with optional indeterminate state.
  * Supports modal and non-modal modes.
  * Customize side, alignment, offsets, collision handling.
  * Optionally render a pointing arrow.
  * Focus is fully managed.
  * Full keyboard navigation.
  * Typeahead support.
  * Dismissing and layering behavior is highly customizable.

## Component Reference Links
Version: 2.1.17
Size:
[View as Markdown](https://www.radix-ui.com/primitives/docs/components/dropdown-menu.md)
## [Anatomy](https://www.radix-ui.com/primitives/docs/components/dropdown-menu#anatomy)
Import all parts and piece them together.

```

import { DropdownMenu } from "radix-ui";

export default () => (

	<DropdownMenu.Root>

		<DropdownMenu.Trigger />

		<DropdownMenu.Portal>

			<DropdownMenu.Content>

				<DropdownMenu.Label />

				<DropdownMenu.Item />

				<DropdownMenu.Group>

					<DropdownMenu.Item />

				</DropdownMenu.Group>

				<DropdownMenu.CheckboxItem>

					<DropdownMenu.ItemIndicator />

				</DropdownMenu.CheckboxItem>

				<DropdownMenu.RadioGroup>

					<DropdownMenu.RadioItem>

						<DropdownMenu.ItemIndicator />

					</DropdownMenu.RadioItem>

				</DropdownMenu.RadioGroup>

				<DropdownMenu.Sub>

					<DropdownMenu.SubTrigger />

					<DropdownMenu.Portal>

						<DropdownMenu.SubContent />

					</DropdownMenu.Portal>

				</DropdownMenu.Sub>

				<DropdownMenu.Separator />

				<DropdownMenu.Arrow />

			</DropdownMenu.Content>

		</DropdownMenu.Portal>

	</DropdownMenu.Root>

);

```

## [API Reference](https://www.radix-ui.com/primitives/docs/components/dropdown-menu#api-reference)
### [Root](https://www.radix-ui.com/primitives/docs/components/dropdown-menu#root)
Contains all the parts of a dropdown menu.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `defaultOpen` Prop description  | `boolean`  | No default value  |
|  `open` Prop description  | `boolean`  | No default value  |
|  `onOpenChange` Prop description  |  `function` See full type  | No default value  |
|  `modal` Prop description  | `boolean`  | `true`  |
|  `dir` Prop description  |  `enum` See full type  | No default value  |
### [Trigger](https://www.radix-ui.com/primitives/docs/components/dropdown-menu#trigger)
The button that toggles the dropdown menu. By default, the `DropdownMenu.Content` will position itself against the trigger.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
| Data attribute  | Values  |
| --- | --- |
| `[data-state]`  | `"open"  | "closed" `  |
| `[data-disabled]`  | Present when disabled  |
### [Portal](https://www.radix-ui.com/primitives/docs/components/dropdown-menu#portal)
When used, portals the content part into the `body`.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `forceMount` Prop description  | `boolean`  | No default value  |
|  `container` Prop description  | `HTMLElement`  | `document.body`  |
### [Content](https://www.radix-ui.com/primitives/docs/components/dropdown-menu#content)
The component that pops out when the dropdown menu is open.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
|  `loop` Prop description  | `boolean`  | `false`  |
|  `onCloseAutoFocus` Prop description  |  `function` See full type  | No default value  |
|  `onEscapeKeyDown` Prop description  |  `function` See full type  | No default value  |
|  `onPointerDownOutside` Prop description  |  `function` See full type  | No default value  |
|  `onFocusOutside` Prop description  |  `function` See full type  | No default value  |
|  `onInteractOutside` Prop description  |  `function` See full type  | No default value  |
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
| `[data-orientation]`  | `"vertical"  | "horizontal" `  |
| CSS Variable  | Description  |
| --- | --- |
| `--radix-dropdown-menu-content-transform-origin`  | The `transform-origin` computed from the content and arrow positions/offsets  |
| `--radix-dropdown-menu-content-available-width`  | The remaining width between the trigger and the boundary edge  |
| `--radix-dropdown-menu-content-available-height`  | The remaining height between the trigger and the boundary edge  |
| `--radix-dropdown-menu-trigger-width`  | The width of the trigger  |
| `--radix-dropdown-menu-trigger-height`  | The height of the trigger  |
### [Arrow](https://www.radix-ui.com/primitives/docs/components/dropdown-menu#arrow)
An optional arrow element to render alongside the dropdown menu. This can be used to help visually link the trigger with the `DropdownMenu.Content`. Must be rendered inside `DropdownMenu.Content`.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
|  `width` Prop description  | `number`  | `10`  |
|  `height` Prop description  | `number`  | `5`  |
### [Item](https://www.radix-ui.com/primitives/docs/components/dropdown-menu#item)
The component that contains the dropdown menu items.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
|  `disabled` Prop description  | `boolean`  | No default value  |
|  `onSelect` Prop description  |  `function` See full type  | No default value  |
|  `textValue` Prop description  | `string`  | No default value  |
| Data attribute  | Values  |
| --- | --- |
| `[data-orientation]`  | `"vertical"  | "horizontal" `  |
| `[data-highlighted]`  | Present when highlighted  |
| `[data-disabled]`  | Present when disabled  |
### [Group](https://www.radix-ui.com/primitives/docs/components/dropdown-menu#group)
Used to group multiple `DropdownMenu.Item`s.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
### [Label](https://www.radix-ui.com/primitives/docs/components/dropdown-menu#label)
Used to render a label. It won't be focusable using arrow keys.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
### [CheckboxItem](https://www.radix-ui.com/primitives/docs/components/dropdown-menu#checkboxitem)
An item that can be controlled and rendered like a checkbox.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
|  `checked` Prop description  | `boolean | 'indeterminate'`  | No default value  |
|  `onCheckedChange` Prop description  |  `function` See full type  | No default value  |
|  `disabled` Prop description  | `boolean`  | No default value  |
|  `onSelect` Prop description  |  `function` See full type  | No default value  |
|  `textValue` Prop description  | `string`  | No default value  |
| Data attribute  | Values  |
| --- | --- |
| `[data-state]`  | `"checked"  | "unchecked"  | "indeterminate" `  |
| `[data-highlighted]`  | Present when highlighted  |
| `[data-disabled]`  | Present when disabled  |
### [RadioGroup](https://www.radix-ui.com/primitives/docs/components/dropdown-menu#radiogroup)
Used to group multiple `DropdownMenu.RadioItem`s.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
|  `value` Prop description  | `string`  | No default value  |
|  `onValueChange` Prop description  |  `function` See full type  | No default value  |
### [RadioItem](https://www.radix-ui.com/primitives/docs/components/dropdown-menu#radioitem)
An item that can be controlled and rendered like a radio.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
|  `value*` Prop description  | `string`  | No default value  |
|  `disabled` Prop description  | `boolean`  | No default value  |
|  `onSelect` Prop description  |  `function` See full type  | No default value  |
|  `textValue` Prop description  | `string`  | No default value  |
| Data attribute  | Values  |
| --- | --- |
| `[data-state]`  | `"checked"  | "unchecked"  | "indeterminate" `  |
| `[data-highlighted]`  | Present when highlighted  |
| `[data-disabled]`  | Present when disabled  |
### [ItemIndicator](https://www.radix-ui.com/primitives/docs/components/dropdown-menu#itemindicator)
Renders when the parent `DropdownMenu.CheckboxItem` or `DropdownMenu.RadioItem` is checked. You can style this element directly, or you can use it as a wrapper to put an icon into, or both.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
|  `forceMount` Prop description  | `boolean`  | No default value  |
| Data attribute  | Values  |
| --- | --- |
| `[data-state]`  | `"checked"  | "unchecked"  | "indeterminate" `  |
### [Separator](https://www.radix-ui.com/primitives/docs/components/dropdown-menu#separator)
Used to visually separate items in the dropdown menu.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
### [Sub](https://www.radix-ui.com/primitives/docs/components/dropdown-menu#sub)
Contains all the parts of a submenu.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `defaultOpen` Prop description  | `boolean`  | No default value  |
|  `open` Prop description  | `boolean`  | No default value  |
|  `onOpenChange` Prop description  |  `function` See full type  | No default value  |
### [SubTrigger](https://www.radix-ui.com/primitives/docs/components/dropdown-menu#subtrigger)
An item that opens a submenu. Must be rendered inside `DropdownMenu.Sub`.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
|  `disabled` Prop description  | `boolean`  | No default value  |
|  `textValue` Prop description  | `string`  | No default value  |
| Data attribute  | Values  |
| --- | --- |
| `[data-state]`  | `"open"  | "closed" `  |
| `[data-highlighted]`  | Present when highlighted  |
| `[data-disabled]`  | Present when disabled  |
| CSS Variable  | Description  |
| --- | --- |
| `--radix-dropdown-menu-content-transform-origin`  | The `transform-origin` computed from the content and arrow positions/offsets  |
| `--radix-dropdown-menu-content-available-width`  | The remaining width between the trigger and the boundary edge  |
| `--radix-dropdown-menu-content-available-height`  | The remaining height between the trigger and the boundary edge  |
| `--radix-dropdown-menu-trigger-width`  | The width of the trigger  |
| `--radix-dropdown-menu-trigger-height`  | The height of the trigger  |
### [SubContent](https://www.radix-ui.com/primitives/docs/components/dropdown-menu#subcontent)
The component that pops out when a submenu is open. Must be rendered inside `DropdownMenu.Sub`.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
|  `loop` Prop description  | `boolean`  | `false`  |
|  `onEscapeKeyDown` Prop description  |  `function` See full type  | No default value  |
|  `onPointerDownOutside` Prop description  |  `function` See full type  | No default value  |
|  `onFocusOutside` Prop description  |  `function` See full type  | No default value  |
|  `onInteractOutside` Prop description  |  `function` See full type  | No default value  |
|  `forceMount` Prop description  | `boolean`  | No default value  |
|  `sideOffset` Prop description  | `number`  | `0`  |
|  `align` Prop description  |  `enum` See full type  | `"start"`  |
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
| `[data-orientation]`  | `"vertical"  | "horizontal" `  |
## [Examples](https://www.radix-ui.com/primitives/docs/components/dropdown-menu#examples)
### [With submenus](https://www.radix-ui.com/primitives/docs/components/dropdown-menu#with-submenus)
You can create submenus by using `DropdownMenu.Sub` in combination with its parts.

```

<DropdownMenu.Root>

	<DropdownMenu.Trigger>…</DropdownMenu.Trigger>

	<DropdownMenu.Portal>

		<DropdownMenu.Content>

			<DropdownMenu.Item>…</DropdownMenu.Item>

			<DropdownMenu.Item>…</DropdownMenu.Item>

			<DropdownMenu.Separator />

			<DropdownMenu.Sub>

				<DropdownMenu.SubTrigger>Sub menu →</DropdownMenu.SubTrigger>

				<DropdownMenu.Portal>

					<DropdownMenu.SubContent>

						<DropdownMenu.Item>Sub menu item</DropdownMenu.Item>

						<DropdownMenu.Item>Sub menu item</DropdownMenu.Item>

						<DropdownMenu.Arrow />

					</DropdownMenu.SubContent>

				</DropdownMenu.Portal>

			</DropdownMenu.Sub>

			<DropdownMenu.Separator />

			<DropdownMenu.Item>…</DropdownMenu.Item>

		</DropdownMenu.Content>

	</DropdownMenu.Portal>

</DropdownMenu.Root>

```

### [With disabled items](https://www.radix-ui.com/primitives/docs/components/dropdown-menu#with-disabled-items)
You can add special styles to disabled items via the `data-disabled` attribute.

```

// index.jsx

import { DropdownMenu } from "radix-ui";

import "./styles.css";

export default () => (

	<DropdownMenu.Root>

		<DropdownMenu.Trigger>…</DropdownMenu.Trigger>

		<DropdownMenu.Portal>

			<DropdownMenu.Content>

				<DropdownMenu.Item className="DropdownMenuItem" disabled>

					…

				</DropdownMenu.Item>

				<DropdownMenu.Item className="DropdownMenuItem">…</DropdownMenu.Item>

			</DropdownMenu.Content>

		</DropdownMenu.Portal>

	</DropdownMenu.Root>

);

```

```

/* styles.css */

.DropdownMenuItem[data-disabled] {

	color: gainsboro;

}

```

### [With separators](https://www.radix-ui.com/primitives/docs/components/dropdown-menu#with-separators)
Use the `Separator` part to add a separator between items.

```

<DropdownMenu.Root>

	<DropdownMenu.Trigger>…</DropdownMenu.Trigger>

	<DropdownMenu.Portal>

		<DropdownMenu.Content>

			<DropdownMenu.Item>…</DropdownMenu.Item>

			<DropdownMenu.Separator />

			<DropdownMenu.Item>…</DropdownMenu.Item>

			<DropdownMenu.Separator />

			<DropdownMenu.Item>…</DropdownMenu.Item>

		</DropdownMenu.Content>

	</DropdownMenu.Portal>

</DropdownMenu.Root>

```

### [With labels](https://www.radix-ui.com/primitives/docs/components/dropdown-menu#with-labels)
Use the `Label` part to help label a section.

```

<DropdownMenu.Root>

	<DropdownMenu.Trigger>…</DropdownMenu.Trigger>

	<DropdownMenu.Portal>

		<DropdownMenu.Content>

			<DropdownMenu.Label>Label</DropdownMenu.Label>

			<DropdownMenu.Item>…</DropdownMenu.Item>

			<DropdownMenu.Item>…</DropdownMenu.Item>

			<DropdownMenu.Item>…</DropdownMenu.Item>

		</DropdownMenu.Content>

	</DropdownMenu.Portal>

</DropdownMenu.Root>

```

### [With checkbox items](https://www.radix-ui.com/primitives/docs/components/dropdown-menu#with-checkbox-items)
Use the `CheckboxItem` part to add an item that can be checked.

```

import * as React from "react";

import { CheckIcon } from "@radix-ui/react-icons";

import { DropdownMenu } from "radix-ui";

export default () => {

	const [checked, setChecked] = React.useState(true);

	return (

		<DropdownMenu.Root>

			<DropdownMenu.Trigger>…</DropdownMenu.Trigger>

			<DropdownMenu.Portal>

				<DropdownMenu.Content>

					<DropdownMenu.Item>…</DropdownMenu.Item>

					<DropdownMenu.Item>…</DropdownMenu.Item>

					<DropdownMenu.Separator />

					<DropdownMenu.CheckboxItem
						checked={checked}
						onCheckedChange={setChecked}
					>

						<DropdownMenu.ItemIndicator>

							<CheckIcon />

						</DropdownMenu.ItemIndicator>

						Checkbox item

					</DropdownMenu.CheckboxItem>

				</DropdownMenu.Content>

			</DropdownMenu.Portal>

		</DropdownMenu.Root>

	);

};

```

### [With radio items](https://www.radix-ui.com/primitives/docs/components/dropdown-menu#with-radio-items)
Use the `RadioGroup` and `RadioItem` parts to add an item that can be checked amongst others.

```

import * as React from "react";

import { CheckIcon } from "@radix-ui/react-icons";

import { DropdownMenu } from "radix-ui";

export default () => {

	const [color, setColor] = React.useState("blue");

	return (

		<DropdownMenu.Root>

			<DropdownMenu.Trigger>…</DropdownMenu.Trigger>

			<DropdownMenu.Portal>

				<DropdownMenu.Content>

					<DropdownMenu.RadioGroup value={color} onValueChange={setColor}>

						<DropdownMenu.RadioItem value="red">

							<DropdownMenu.ItemIndicator>

								<CheckIcon />

							</DropdownMenu.ItemIndicator>

							Red

						</DropdownMenu.RadioItem>

						<DropdownMenu.RadioItem value="blue">

							<DropdownMenu.ItemIndicator>

								<CheckIcon />

							</DropdownMenu.ItemIndicator>

							Blue

						</DropdownMenu.RadioItem>

						<DropdownMenu.RadioItem value="green">

							<DropdownMenu.ItemIndicator>

								<CheckIcon />

							</DropdownMenu.ItemIndicator>

							Green

						</DropdownMenu.RadioItem>

					</DropdownMenu.RadioGroup>

				</DropdownMenu.Content>

			</DropdownMenu.Portal>

		</DropdownMenu.Root>

	);

};

```

### [With complex items](https://www.radix-ui.com/primitives/docs/components/dropdown-menu#with-complex-items)
You can add extra decorative elements in the `Item` parts, such as images.

```

import { DropdownMenu } from "radix-ui";

export default () => (

	<DropdownMenu.Root>

		<DropdownMenu.Trigger>…</DropdownMenu.Trigger>

		<DropdownMenu.Portal>

			<DropdownMenu.Content>

				<DropdownMenu.Item>

					<img src="…" />

					Adolfo Hess

				</DropdownMenu.Item>

				<DropdownMenu.Item>

					<img src="…" />

					Miyah Myles

				</DropdownMenu.Item>

			</DropdownMenu.Content>

		</DropdownMenu.Portal>

	</DropdownMenu.Root>

);

```

### [Constrain the content/sub-content size](https://www.radix-ui.com/primitives/docs/components/dropdown-menu#constrain-the-contentsub-content-size)
You may want to constrain the width of the content (or sub-content) so that it matches the trigger (or sub-trigger) width. You may also want to constrain its height to not exceed the viewport.
We expose several CSS custom properties such as `--radix-dropdown-menu-trigger-width` and `--radix-dropdown-menu-content-available-height` to support this. Use them to constrain the content dimensions.

```

// index.jsx

import { DropdownMenu } from "radix-ui";

import "./styles.css";

export default () => (

	<DropdownMenu.Root>

		<DropdownMenu.Trigger>…</DropdownMenu.Trigger>

		<DropdownMenu.Portal>

			<DropdownMenu.Content className="DropdownMenuContent" sideOffset={5}>

				…

			</DropdownMenu.Content>

		</DropdownMenu.Portal>

	</DropdownMenu.Root>

);

```

```

/* styles.css */

.DropdownMenuContent {

	width: var(--radix-dropdown-menu-trigger-width);

	max-height: var(--radix-dropdown-menu-content-available-height);

}

```

### [Origin-aware animations](https://www.radix-ui.com/primitives/docs/components/dropdown-menu#origin-aware-animations)
We expose a CSS custom property `--radix-dropdown-menu-content-transform-origin`. Use it to animate the content from its computed origin based on `side`, `sideOffset`, `align`, `alignOffset` and any collisions.

```

// index.jsx

import { DropdownMenu } from "radix-ui";

import "./styles.css";

export default () => (

	<DropdownMenu.Root>

		<DropdownMenu.Trigger>…</DropdownMenu.Trigger>

		<DropdownMenu.Portal>

			<DropdownMenu.Content className="DropdownMenuContent">

				…

			</DropdownMenu.Content>

		</DropdownMenu.Portal>

	</DropdownMenu.Root>

);

```

```

/* styles.css */

.DropdownMenuContent {

	transform-origin: var(--radix-dropdown-menu-content-transform-origin);

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

### [Collision-aware animations](https://www.radix-ui.com/primitives/docs/components/dropdown-menu#collision-aware-animations)
We expose `data-side` and `data-align` attributes. Their values will change at runtime to reflect collisions. Use them to create collision and direction-aware animations.

```

// index.jsx

import { DropdownMenu } from "radix-ui";

import "./styles.css";

export default () => (

	<DropdownMenu.Root>

		<DropdownMenu.Trigger>…</DropdownMenu.Trigger>

		<DropdownMenu.Portal>

			<DropdownMenu.Content className="DropdownMenuContent">

				…

			</DropdownMenu.Content>

		</DropdownMenu.Portal>

	</DropdownMenu.Root>

);

```

```

/* styles.css */

.DropdownMenuContent {

	animation-duration: 0.6s;

	animation-timing-function: cubic-bezier(0.16, 1, 0.3, 1);

}

.DropdownMenuContent[data-side="top"] {

	animation-name: slideUp;

}

.DropdownMenuContent[data-side="bottom"] {

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

## [Accessibility](https://www.radix-ui.com/primitives/docs/components/dropdown-menu#accessibility)
Adheres to the
### [Keyboard Interactions](https://www.radix-ui.com/primitives/docs/components/dropdown-menu#keyboard-interactions)
| Key  | Description  |
| --- | --- |
| `Space`  | When focus is on `DropdownMenu.Trigger`, opens the dropdown menu and focuses the first item.
When focus is on an item, activates the focused item.  |
| `Enter`  | When focus is on `DropdownMenu.Trigger`, opens the dropdown menu and focuses the first item.
When focus is on an item, activates the focused item.  |
| `ArrowDown`  | When focus is on `DropdownMenu.Trigger`, opens the dropdown menu.
When focus is on an item, moves focus to the next item.  |
| `ArrowUp`  | When focus is on an item, moves focus to the previous item.  |
|  `ArrowRight``ArrowLeft`  | When focus is on `DropdownMenu.SubTrigger`, opens or closes the submenu depending on reading direction.  |
| `Esc`  | Closes the dropdown menu and moves focus to `DropdownMenu.Trigger`.  |
## [Custom APIs](https://www.radix-ui.com/primitives/docs/components/dropdown-menu#custom-apis)
Create your own API by abstracting the primitive parts into your own component.
### [Abstract the arrow and item indicators](https://www.radix-ui.com/primitives/docs/components/dropdown-menu#abstract-the-arrow-and-item-indicators)
This example abstracts the `DropdownMenu.Arrow` and `DropdownMenu.ItemIndicator` parts. It also wraps implementation details for `CheckboxItem` and `RadioItem`.
#### Usage

```

import {
	DropdownMenu,
	DropdownMenuTrigger,
	DropdownMenuContent,
	DropdownMenuLabel,
	DropdownMenuItem,
	DropdownMenuGroup,
	DropdownMenuCheckboxItem,
	DropdownMenuRadioGroup,
	DropdownMenuRadioItem,
	DropdownMenuSeparator,
} from "./your-dropdown-menu";

export default () => (

	<DropdownMenu>

		<DropdownMenuTrigger>DropdownMenu trigger</DropdownMenuTrigger>

		<DropdownMenuContent>

			<DropdownMenuItem>Item</DropdownMenuItem>

			<DropdownMenuLabel>Label</DropdownMenuLabel>

			<DropdownMenuGroup>Group</DropdownMenuGroup>

			<DropdownMenuCheckboxItem>CheckboxItem</DropdownMenuCheckboxItem>

			<DropdownMenuSeparator>Separator</DropdownMenuSeparator>

			<DropdownMenuRadioGroup>

				<DropdownMenuRadioItem>RadioItem</DropdownMenuRadioItem>

				<DropdownMenuRadioItem>RadioItem</DropdownMenuRadioItem>

			</DropdownMenuRadioGroup>

		</DropdownMenuContent>

	</DropdownMenu>

);

```

#### Implementation

```

// your-dropdown-menu.jsx

import * as React from "react";

import { DropdownMenu as DropdownMenuPrimitive } from "radix-ui";

import { CheckIcon, DividerHorizontalIcon } from "@radix-ui/react-icons";

export const DropdownMenu = DropdownMenuPrimitive.Root;

export const DropdownMenuTrigger = DropdownMenuPrimitive.Trigger;

export const DropdownMenuContent = React.forwardRef(

	({ children, ...props }, forwardedRef) => {

		return (

			<DropdownMenuPrimitive.Portal>

				<DropdownMenuPrimitive.Content {...props} ref={forwardedRef}>

					{children}

					<DropdownMenuPrimitive.Arrow />

				</DropdownMenuPrimitive.Content>

			</DropdownMenuPrimitive.Portal>

		);

	},

);

export const DropdownMenuLabel = DropdownMenuPrimitive.Label;

export const DropdownMenuItem = DropdownMenuPrimitive.Item;

export const DropdownMenuGroup = DropdownMenuPrimitive.Group;

export const DropdownMenuCheckboxItem = React.forwardRef(

	({ children, ...props }, forwardedRef) => {

		return (

			<DropdownMenuPrimitive.CheckboxItem {...props} ref={forwardedRef}>

				{children}

				<DropdownMenuPrimitive.ItemIndicator>

					{props.checked === "indeterminate" && <DividerHorizontalIcon />}

					{props.checked === true && <CheckIcon />}

				</DropdownMenuPrimitive.ItemIndicator>

			</DropdownMenuPrimitive.CheckboxItem>

		);

	},

);

export const DropdownMenuRadioGroup = DropdownMenuPrimitive.RadioGroup;

export const DropdownMenuRadioItem = React.forwardRef(

	({ children, ...props }, forwardedRef) => {

		return (

			<DropdownMenuPrimitive.RadioItem {...props} ref={forwardedRef}>

				{children}

				<DropdownMenuPrimitive.ItemIndicator>

					<CheckIcon />

				</DropdownMenuPrimitive.ItemIndicator>

			</DropdownMenuPrimitive.RadioItem>

		);

	},

);

export const DropdownMenuSeparator = DropdownMenuPrimitive.Separator;

```

#### Quick nav
  * [Anatomy](https://www.radix-ui.com/primitives/docs/components/dropdown-menu#anatomy)
  * [API Reference](https://www.radix-ui.com/primitives/docs/components/dropdown-menu#api-reference)
  * [Root](https://www.radix-ui.com/primitives/docs/components/dropdown-menu#root)
  * [Trigger](https://www.radix-ui.com/primitives/docs/components/dropdown-menu#trigger)
  * [Portal](https://www.radix-ui.com/primitives/docs/components/dropdown-menu#portal)
  * [Content](https://www.radix-ui.com/primitives/docs/components/dropdown-menu#content)
  * [Arrow](https://www.radix-ui.com/primitives/docs/components/dropdown-menu#arrow)
  * [Item](https://www.radix-ui.com/primitives/docs/components/dropdown-menu#item)
  * [Group](https://www.radix-ui.com/primitives/docs/components/dropdown-menu#group)
  * [Label](https://www.radix-ui.com/primitives/docs/components/dropdown-menu#label)
  * [CheckboxItem](https://www.radix-ui.com/primitives/docs/components/dropdown-menu#checkboxitem)
  * [RadioGroup](https://www.radix-ui.com/primitives/docs/components/dropdown-menu#radiogroup)
  * [RadioItem](https://www.radix-ui.com/primitives/docs/components/dropdown-menu#radioitem)
  * [ItemIndicator](https://www.radix-ui.com/primitives/docs/components/dropdown-menu#itemindicator)
  * [Separator](https://www.radix-ui.com/primitives/docs/components/dropdown-menu#separator)
  * [Sub](https://www.radix-ui.com/primitives/docs/components/dropdown-menu#sub)
  * [SubTrigger](https://www.radix-ui.com/primitives/docs/components/dropdown-menu#subtrigger)
  * [SubContent](https://www.radix-ui.com/primitives/docs/components/dropdown-menu#subcontent)
  * [Examples](https://www.radix-ui.com/primitives/docs/components/dropdown-menu#examples)
  * [With submenus](https://www.radix-ui.com/primitives/docs/components/dropdown-menu#with-submenus)
  * [With disabled items](https://www.radix-ui.com/primitives/docs/components/dropdown-menu#with-disabled-items)
  * [With separators](https://www.radix-ui.com/primitives/docs/components/dropdown-menu#with-separators)
  * [With labels](https://www.radix-ui.com/primitives/docs/components/dropdown-menu#with-labels)
  * [With checkbox items](https://www.radix-ui.com/primitives/docs/components/dropdown-menu#with-checkbox-items)
  * [With radio items](https://www.radix-ui.com/primitives/docs/components/dropdown-menu#with-radio-items)
  * [With complex items](https://www.radix-ui.com/primitives/docs/components/dropdown-menu#with-complex-items)
  * [Constrain the content/sub-content size](https://www.radix-ui.com/primitives/docs/components/dropdown-menu#constrain-the-contentsub-content-size)
  * [Origin-aware animations](https://www.radix-ui.com/primitives/docs/components/dropdown-menu#origin-aware-animations)
  * [Collision-aware animations](https://www.radix-ui.com/primitives/docs/components/dropdown-menu#collision-aware-animations)
  * [Accessibility](https://www.radix-ui.com/primitives/docs/components/dropdown-menu#accessibility)
  * [Keyboard Interactions](https://www.radix-ui.com/primitives/docs/components/dropdown-menu#keyboard-interactions)
  * [Custom APIs](https://www.radix-ui.com/primitives/docs/components/dropdown-menu#custom-apis)
  * [Abstract the arrow and item indicators](https://www.radix-ui.com/primitives/docs/components/dropdown-menu#abstract-the-arrow-and-item-indicators)

Previous[Dialog](https://www.radix-ui.com/primitives/docs/components/dialog)
Next[Form](https://www.radix-ui.com/primitives/docs/components/form)
