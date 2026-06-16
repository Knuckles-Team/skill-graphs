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
# Context Menu
Displays a menu located at the pointer, triggered by a right click or a long press.
Right-click here.
index.jsxindex.jsxstyles.cssstyles.css
CSS

```

import * as React from "react";

import { ContextMenu } from "radix-ui";

import {
	DotFilledIcon,
	CheckIcon,
	ChevronRightIcon,
} from "@radix-ui/react-icons";

import "./styles.css";

const ContextMenuDemo = () => {

	const [bookmarksChecked, setBookmarksChecked] = React.useState(true);

	const [urlsChecked, setUrlsChecked] = React.useState(false);

	const [person, setPerson] = React.useState("pedro");

	return (

		<ContextMenu.Root>

			<ContextMenu.Trigger className="ContextMenuTrigger">

				Right-click here.

			</ContextMenu.Trigger>

			<ContextMenu.Portal>

				<ContextMenu.Content
					className="ContextMenuContent"
					sideOffset={5}
					align="end"
				>

					<ContextMenu.Item className="ContextMenuItem">

						Back <div className="RightSlot">⌘+[</div>

					</ContextMenu.Item>

					<ContextMenu.Item className="ContextMenuItem" disabled>

						Forward <div className="RightSlot">⌘+]</div>

					</ContextMenu.Item>

					<ContextMenu.Item className="ContextMenuItem">

						Reload <div className="RightSlot">⌘+R</div>

					</ContextMenu.Item>

					<ContextMenu.Sub>

						<ContextMenu.SubTrigger className="ContextMenuSubTrigger">

							More Tools

							<div className="RightSlot">

								<ChevronRightIcon />

							</div>

						</ContextMenu.SubTrigger>

						<ContextMenu.Portal>

							<ContextMenu.SubContent
								className="ContextMenuSubContent"
								sideOffset={2}
								alignOffset={-5}
							>

								<ContextMenu.Item className="ContextMenuItem">

									Save Page As… <div className="RightSlot">⌘+S</div>

								</ContextMenu.Item>

								<ContextMenu.Item className="ContextMenuItem">

									Create Shortcut…

								</ContextMenu.Item>

								<ContextMenu.Item className="ContextMenuItem">

									Name Window…

								</ContextMenu.Item>

								<ContextMenu.Separator className="ContextMenuSeparator" />

								<ContextMenu.Item className="ContextMenuItem">

									Developer Tools

								</ContextMenu.Item>

							</ContextMenu.SubContent>

						</ContextMenu.Portal>

					</ContextMenu.Sub>

					<ContextMenu.Separator className="ContextMenuSeparator" />

					<ContextMenu.CheckboxItem
						className="ContextMenuCheckboxItem"
						checked={bookmarksChecked}
						onCheckedChange={setBookmarksChecked}
					>

						<ContextMenu.ItemIndicator className="ContextMenuItemIndicator">

							<CheckIcon />

						</ContextMenu.ItemIndicator>

						Show Bookmarks <div className="RightSlot">⌘+B</div>

					</ContextMenu.CheckboxItem>

					<ContextMenu.CheckboxItem
						className="ContextMenuCheckboxItem"
						checked={urlsChecked}
						onCheckedChange={setUrlsChecked}
					>

						<ContextMenu.ItemIndicator className="ContextMenuItemIndicator">

							<CheckIcon />

						</ContextMenu.ItemIndicator>

						Show Full URLs

					</ContextMenu.CheckboxItem>

					<ContextMenu.Separator className="ContextMenuSeparator" />

					<ContextMenu.Label className="ContextMenuLabel">

						People

					</ContextMenu.Label>

					<ContextMenu.RadioGroup value={person} onValueChange={setPerson}>

						<ContextMenu.RadioItem
							className="ContextMenuRadioItem"
							value="pedro"
						>

							<ContextMenu.ItemIndicator className="ContextMenuItemIndicator">

								<DotFilledIcon />

							</ContextMenu.ItemIndicator>

							Pedro Duarte

						</ContextMenu.RadioItem>

						<ContextMenu.RadioItem
							className="ContextMenuRadioItem"
							value="colm"
						>

							<ContextMenu.ItemIndicator className="ContextMenuItemIndicator">

								<DotFilledIcon />

							</ContextMenu.ItemIndicator>

							Colm Tuite

						</ContextMenu.RadioItem>

					</ContextMenu.RadioGroup>

				</ContextMenu.Content>

			</ContextMenu.Portal>

		</ContextMenu.Root>

	);

};

export default ContextMenuDemo;

Expand code

```

## Features
  * Supports submenus with configurable reading direction.
  * Supports items, labels, groups of items.
  * Supports checkable items (single or multiple) with optional indeterminate state.
  * Supports modal and non-modal modes.
  * Customize side, alignment, offsets, collision handling.
  * Focus is fully managed.
  * Full keyboard navigation.
  * Typeahead support.
  * Dismissing and layering behavior is highly customizable.
  * Triggers with a long press on touch devices

## Component Reference Links
Version: 2.3.0
Size:
[View as Markdown](https://www.radix-ui.com/primitives/docs/components/context-menu.md)
## [Anatomy](https://www.radix-ui.com/primitives/docs/components/context-menu#anatomy)
Import all parts and piece them together.

```

import { ContextMenu } from "radix-ui";

export default () => (

	<ContextMenu.Root>

		<ContextMenu.Trigger />

		<ContextMenu.Portal>

			<ContextMenu.Content>

				<ContextMenu.Label />

				<ContextMenu.Item />

				<ContextMenu.Group>

					<ContextMenu.Item />

				</ContextMenu.Group>

				<ContextMenu.CheckboxItem>

					<ContextMenu.ItemIndicator />

				</ContextMenu.CheckboxItem>

				<ContextMenu.RadioGroup>

					<ContextMenu.RadioItem>

						<ContextMenu.ItemIndicator />

					</ContextMenu.RadioItem>

				</ContextMenu.RadioGroup>

				<ContextMenu.Sub>

					<ContextMenu.SubTrigger />

					<ContextMenu.Portal>

						<ContextMenu.SubContent />

					</ContextMenu.Portal>

				</ContextMenu.Sub>

				<ContextMenu.Separator />

			</ContextMenu.Content>

		</ContextMenu.Portal>

	</ContextMenu.Root>

);

```

## [API Reference](https://www.radix-ui.com/primitives/docs/components/context-menu#api-reference)
Adheres to the
### [Root](https://www.radix-ui.com/primitives/docs/components/context-menu#root)
Contains all the parts of a context menu.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `dir` Prop description  |  `enum` See full type  | No default value  |
|  `open` Prop description  | `boolean`  | No default value  |
|  `onOpenChange` Prop description  |  `function` See full type  | No default value  |
|  `modal` Prop description  | `boolean`  | `true`  |
### [Trigger](https://www.radix-ui.com/primitives/docs/components/context-menu#trigger)
The area that opens the context menu. Wrap it around the target you want the context menu to open from when right-clicking (or using the relevant keyboard shortcuts).
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
|  `disabled` Prop description  | `boolean`  | `false`  |
| Data attribute  | Values  |
| --- | --- |
| `[data-state]`  | `"open"  | "closed" `  |
### [Portal](https://www.radix-ui.com/primitives/docs/components/context-menu#portal)
When used, portals the content part into the `body`.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `forceMount` Prop description  | `boolean`  | No default value  |
|  `container` Prop description  | `HTMLElement`  | `document.body`  |
### [Content](https://www.radix-ui.com/primitives/docs/components/context-menu#content)
The component that pops out in an open context menu.
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
|  `alignOffset` Prop description  | `number`  | `0`  |
|  `avoidCollisions` Prop description  | `boolean`  | `true`  |
|  `collisionBoundary` Prop description  |  `Boundary` See full type  | `[]`  |
|  `collisionPadding` Prop description  |  `number | Padding` See full type  | `0`  |
|  `sticky` Prop description  |  `enum` See full type  | `"partial"`  |
|  `hideWhenDetached` Prop description  | `boolean`  | `false`  |
| Data attribute  | Values  |
| --- | --- |
| `[data-state]`  | `"open"  | "closed" `  |
| `[data-side]`  | `"left"  | "right"  | "bottom"  | "top" `  |
| `[data-align]`  | `"start"  | "end"  | "center" `  |
| CSS Variable  | Description  |
| --- | --- |
| `--radix-context-menu-content-transform-origin`  | The `transform-origin` computed from the content and arrow positions/offsets  |
| `--radix-context-menu-content-available-width`  | The remaining width between the trigger and the boundary edge  |
| `--radix-context-menu-content-available-height`  | The remaining height between the trigger and the boundary edge  |
| `--radix-context-menu-trigger-width`  | The width of the trigger  |
| `--radix-context-menu-trigger-height`  | The height of the trigger  |
### [Arrow](https://www.radix-ui.com/primitives/docs/components/context-menu#arrow)
An optional arrow element to render alongside a submenu. This can be used to help visually link the trigger item with the `ContextMenu.Content`. Must be rendered inside `ContextMenu.Content`.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
|  `width` Prop description  | `number`  | `10`  |
|  `height` Prop description  | `number`  | `5`  |
### [Item](https://www.radix-ui.com/primitives/docs/components/context-menu#item)
The component that contains the context menu items.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
|  `disabled` Prop description  | `boolean`  | No default value  |
|  `onSelect` Prop description  |  `function` See full type  | No default value  |
|  `textValue` Prop description  | `string`  | No default value  |
| Data attribute  | Values  |
| --- | --- |
| `[data-highlighted]`  | Present when highlighted  |
| `[data-disabled]`  | Present when disabled  |
### [Group](https://www.radix-ui.com/primitives/docs/components/context-menu#group)
Used to group multiple `ContextMenu.Item`s.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
### [Label](https://www.radix-ui.com/primitives/docs/components/context-menu#label)
Used to render a label. It won't be focusable using arrow keys.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
### [CheckboxItem](https://www.radix-ui.com/primitives/docs/components/context-menu#checkboxitem)
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
### [RadioGroup](https://www.radix-ui.com/primitives/docs/components/context-menu#radiogroup)
Used to group multiple `ContextMenu.RadioItem`s.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
|  `value` Prop description  | `string`  | No default value  |
|  `onValueChange` Prop description  |  `function` See full type  | No default value  |
### [RadioItem](https://www.radix-ui.com/primitives/docs/components/context-menu#radioitem)
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
### [ItemIndicator](https://www.radix-ui.com/primitives/docs/components/context-menu#itemindicator)
Renders when the parent `ContextMenu.CheckboxItem` or `ContextMenu.RadioItem` is checked. You can style this element directly, or you can use it as a wrapper to put an icon into, or both.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
|  `forceMount` Prop description  | `boolean`  | No default value  |
| Data attribute  | Values  |
| --- | --- |
| `[data-state]`  | `"checked"  | "unchecked"  | "indeterminate" `  |
### [Separator](https://www.radix-ui.com/primitives/docs/components/context-menu#separator)
Used to visually separate items in the context menu.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
### [Sub](https://www.radix-ui.com/primitives/docs/components/context-menu#sub)
Contains all the parts of a submenu.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `defaultOpen` Prop description  | `boolean`  | No default value  |
|  `open` Prop description  | `boolean`  | No default value  |
|  `onOpenChange` Prop description  |  `function` See full type  | No default value  |
### [SubTrigger](https://www.radix-ui.com/primitives/docs/components/context-menu#subtrigger)
An item that opens a submenu. Must be rendered inside `ContextMenu.Sub`.
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
### [SubContent](https://www.radix-ui.com/primitives/docs/components/context-menu#subcontent)
The component that pops out when a submenu is open. Must be rendered inside `ContextMenu.Sub`.
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
| CSS Variable  | Description  |
| --- | --- |
| `--radix-context-menu-content-transform-origin`  | The `transform-origin` computed from the content and arrow positions/offsets  |
| `--radix-context-menu-content-available-width`  | The remaining width between the trigger and the boundary edge  |
| `--radix-context-menu-content-available-height`  | The remaining height between the trigger and the boundary edge  |
| `--radix-context-menu-trigger-width`  | The width of the trigger  |
| `--radix-context-menu-trigger-height`  | The height of the trigger  |
## [Examples](https://www.radix-ui.com/primitives/docs/components/context-menu#examples)
### [With submenus](https://www.radix-ui.com/primitives/docs/components/context-menu#with-submenus)
You can create submenus by using `ContextMenu.Sub` in combination with its parts.

```

<ContextMenu.Root>

	<ContextMenu.Trigger>…</ContextMenu.Trigger>

	<ContextMenu.Portal>

		<ContextMenu.Content>

			<ContextMenu.Item>…</ContextMenu.Item>

			<ContextMenu.Item>…</ContextMenu.Item>

			<ContextMenu.Separator />

			<ContextMenu.Sub>

				<ContextMenu.SubTrigger>Sub menu →</ContextMenu.SubTrigger>

				<ContextMenu.Portal>

					<ContextMenu.SubContent>

						<ContextMenu.Item>Sub menu item</ContextMenu.Item>

						<ContextMenu.Item>Sub menu item</ContextMenu.Item>

						<ContextMenu.Arrow />

					</ContextMenu.SubContent>

				</ContextMenu.Portal>

			</ContextMenu.Sub>

			<ContextMenu.Separator />

			<ContextMenu.Item>…</ContextMenu.Item>

		</ContextMenu.Content>

	</ContextMenu.Portal>

</ContextMenu.Root>

```

### [With disabled items](https://www.radix-ui.com/primitives/docs/components/context-menu#with-disabled-items)
You can add special styles to disabled items via the `data-disabled` attribute.

```

// index.jsx

import { ContextMenu } from "radix-ui";

import "./styles.css";

export default () => (

	<ContextMenu.Root>

		<ContextMenu.Trigger>…</ContextMenu.Trigger>

		<ContextMenu.Portal>

			<ContextMenu.Content>

				<ContextMenu.Item className="ContextMenuItem" disabled>

					…

				</ContextMenu.Item>

				<ContextMenu.Item className="ContextMenuItem">…</ContextMenu.Item>

			</ContextMenu.Content>

		</ContextMenu.Portal>

	</ContextMenu.Root>

);

```

```

/* styles.css */

.ContextMenuItem[data-disabled] {

	color: gainsboro;

}

```

### [With separators](https://www.radix-ui.com/primitives/docs/components/context-menu#with-separators)
Use the `Separator` part to add a separator between items.

```

<ContextMenu.Root>

	<ContextMenu.Trigger>…</ContextMenu.Trigger>

	<ContextMenu.Portal>

		<ContextMenu.Content>

			<ContextMenu.Item>…</ContextMenu.Item>

			<ContextMenu.Separator />

			<ContextMenu.Item>…</ContextMenu.Item>

			<ContextMenu.Separator />

			<ContextMenu.Item>…</ContextMenu.Item>

		</ContextMenu.Content>

	</ContextMenu.Portal>

</ContextMenu.Root>

```

### [With labels](https://www.radix-ui.com/primitives/docs/components/context-menu#with-labels)
Use the `Label` part to help label a section.

```

<ContextMenu.Root>

	<ContextMenu.Trigger>…</ContextMenu.Trigger>

	<ContextMenu.Portal>

		<ContextMenu.Content>

			<ContextMenu.Label>Label</ContextMenu.Label>

			<ContextMenu.Item>…</ContextMenu.Item>

			<ContextMenu.Item>…</ContextMenu.Item>

			<ContextMenu.Item>…</ContextMenu.Item>

		</ContextMenu.Content>

	</ContextMenu.Portal>

</ContextMenu.Root>

```

### [With checkbox items](https://www.radix-ui.com/primitives/docs/components/context-menu#with-checkbox-items)
Use the `CheckboxItem` part to add an item that can be checked.

```

import * as React from "react";

import { CheckIcon } from "@radix-ui/react-icons";

import { ContextMenu } from "radix-ui";

export default () => {

	const [checked, setChecked] = React.useState(true);

	return (

		<ContextMenu.Root>

			<ContextMenu.Trigger>…</ContextMenu.Trigger>

			<ContextMenu.Portal>

				<ContextMenu.Content>

					<ContextMenu.Item>…</ContextMenu.Item>

					<ContextMenu.Item>…</ContextMenu.Item>

					<ContextMenu.Separator />

					<ContextMenu.CheckboxItem
						checked={checked}
						onCheckedChange={setChecked}
					>

						<ContextMenu.ItemIndicator>

							<CheckIcon />

						</ContextMenu.ItemIndicator>

						Checkbox item

					</ContextMenu.CheckboxItem>

				</ContextMenu.Content>

			</ContextMenu.Portal>

		</ContextMenu.Root>

	);

};

```

### [With radio items](https://www.radix-ui.com/primitives/docs/components/context-menu#with-radio-items)
Use the `RadioGroup` and `RadioItem` parts to add an item that can be checked amongst others.

```

import * as React from "react";

import { CheckIcon } from "@radix-ui/react-icons";

import { ContextMenu } from "radix-ui";

export default () => {

	const [color, setColor] = React.useState("blue");

	return (

		<ContextMenu.Root>

			<ContextMenu.Trigger>…</ContextMenu.Trigger>

			<ContextMenu.Portal>

				<ContextMenu.Content>

					<ContextMenu.RadioGroup value={color} onValueChange={setColor}>

						<ContextMenu.RadioItem value="red">

							<ContextMenu.ItemIndicator>

								<CheckIcon />

							</ContextMenu.ItemIndicator>

							Red

						</ContextMenu.RadioItem>

						<ContextMenu.RadioItem value="blue">

							<ContextMenu.ItemIndicator>

								<CheckIcon />

							</ContextMenu.ItemIndicator>

							Blue

						</ContextMenu.RadioItem>

						<ContextMenu.RadioItem value="green">

							<ContextMenu.ItemIndicator>

								<CheckIcon />

							</ContextMenu.ItemIndicator>

							Green

						</ContextMenu.RadioItem>

					</ContextMenu.RadioGroup>

				</ContextMenu.Content>

			</ContextMenu.Portal>

		</ContextMenu.Root>

	);

};

```

### [With complex items](https://www.radix-ui.com/primitives/docs/components/context-menu#with-complex-items)
You can add extra decorative elements in the `Item` parts, such as images.

```

import { ContextMenu } from "radix-ui";

export default () => (

	<ContextMenu.Root>

		<ContextMenu.Trigger>…</ContextMenu.Trigger>

		<ContextMenu.Portal>

			<ContextMenu.Content>

				<ContextMenu.Item>

					<img src="…" />

					Adolfo Hess

				</ContextMenu.Item>

				<ContextMenu.Item>

					<img src="…" />

					Miyah Myles

				</ContextMenu.Item>

			</ContextMenu.Content>

		</ContextMenu.Portal>

	</ContextMenu.Root>

);

```

### [Constrain the content/sub-content size](https://www.radix-ui.com/primitives/docs/components/context-menu#constrain-the-contentsub-content-size)
You may want to constrain the width of the content (or sub-content) so that it matches the trigger (or sub-trigger) width. You may also want to constrain its height to not exceed the viewport.
We expose several CSS custom properties such as `--radix-context-menu-trigger-width` and `--radix-context-menu-content-available-height` to support this. Use them to constrain the content dimensions.

```

// index.jsx

import { ContextMenu } from "radix-ui";

import "./styles.css";

export default () => (

	<ContextMenu.Root>

		<ContextMenu.Trigger>…</ContextMenu.Trigger>

		<ContextMenu.Portal>

			<ContextMenu.Content className="ContextMenuContent">

				…

			</ContextMenu.Content>

		</ContextMenu.Portal>

	</ContextMenu.Root>

);

```

```

/* styles.css */

.ContextMenuContent {

	width: var(--radix-context-menu-trigger-width);

	max-height: var(--radix-context-menu-content-available-height);

}

```

### [Origin-aware animations](https://www.radix-ui.com/primitives/docs/components/context-menu#origin-aware-animations)
We expose a CSS custom property `--radix-context-menu-content-transform-origin`. Use it to animate the content from its computed origin based on `side`, `sideOffset`, `align`, `alignOffset` and any collisions.

```

// index.jsx

import { ContextMenu } from "radix-ui";

import "./styles.css";

export default () => (

	<ContextMenu.Root>

		<ContextMenu.Trigger>…</ContextMenu.Trigger>

		<ContextMenu.Portal>

			<ContextMenu.Content className="ContextMenuContent">

				…

			</ContextMenu.Content>

		</ContextMenu.Portal>

	</ContextMenu.Root>

);

```

```

/* styles.css */

.ContextMenuContent {

	transform-origin: var(--radix-context-menu-content-transform-origin);

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

### [Collision-aware animations](https://www.radix-ui.com/primitives/docs/components/context-menu#collision-aware-animations)
We expose `data-side` and `data-align` attributes. Their values will change at runtime to reflect collisions. Use them to create collision and direction-aware animations.

```

// index.jsx

import { ContextMenu } from "radix-ui";

import "./styles.css";

export default () => (

	<ContextMenu.Root>

		<ContextMenu.Trigger>…</ContextMenu.Trigger>

		<ContextMenu.Portal>

			<ContextMenu.Content className="ContextMenuContent">

				…

			</ContextMenu.Content>

		</ContextMenu.Portal>

	</ContextMenu.Root>

);

```

```

/* styles.css */

.ContextMenuContent {

	animation-duration: 0.6s;

	animation-timing-function: cubic-bezier(0.16, 1, 0.3, 1);

}

.ContextMenuContent[data-side="top"] {

	animation-name: slideUp;

}

.ContextMenuContent[data-side="bottom"] {

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

## [Accessibility](https://www.radix-ui.com/primitives/docs/components/context-menu#accessibility)
Uses
### [Keyboard Interactions](https://www.radix-ui.com/primitives/docs/components/context-menu#keyboard-interactions)
| Key  | Description  |
| --- | --- |
| `Space`  | Activates the focused item.  |
| `Enter`  | Activates the focused item.  |
| `ArrowDown`  | Moves focus to the next item.  |
| `ArrowUp`  | Moves focus to the previous item.  |
|  `ArrowRight``ArrowLeft`  | When focus is on `ContextMenu.SubTrigger`, opens or closes the submenu depending on reading direction.  |
| `Esc`  | Closes the context menu  |
#### Quick nav
  * [Anatomy](https://www.radix-ui.com/primitives/docs/components/context-menu#anatomy)
  * [API Reference](https://www.radix-ui.com/primitives/docs/components/context-menu#api-reference)
  * [Root](https://www.radix-ui.com/primitives/docs/components/context-menu#root)
  * [Trigger](https://www.radix-ui.com/primitives/docs/components/context-menu#trigger)
  * [Portal](https://www.radix-ui.com/primitives/docs/components/context-menu#portal)
  * [Content](https://www.radix-ui.com/primitives/docs/components/context-menu#content)
  * [Arrow](https://www.radix-ui.com/primitives/docs/components/context-menu#arrow)
  * [Item](https://www.radix-ui.com/primitives/docs/components/context-menu#item)
  * [Group](https://www.radix-ui.com/primitives/docs/components/context-menu#group)
  * [Label](https://www.radix-ui.com/primitives/docs/components/context-menu#label)
  * [CheckboxItem](https://www.radix-ui.com/primitives/docs/components/context-menu#checkboxitem)
  * [RadioGroup](https://www.radix-ui.com/primitives/docs/components/context-menu#radiogroup)
  * [RadioItem](https://www.radix-ui.com/primitives/docs/components/context-menu#radioitem)
  * [ItemIndicator](https://www.radix-ui.com/primitives/docs/components/context-menu#itemindicator)
  * [Separator](https://www.radix-ui.com/primitives/docs/components/context-menu#separator)
  * [Sub](https://www.radix-ui.com/primitives/docs/components/context-menu#sub)
  * [SubTrigger](https://www.radix-ui.com/primitives/docs/components/context-menu#subtrigger)
  * [SubContent](https://www.radix-ui.com/primitives/docs/components/context-menu#subcontent)
  * [Examples](https://www.radix-ui.com/primitives/docs/components/context-menu#examples)
  * [With submenus](https://www.radix-ui.com/primitives/docs/components/context-menu#with-submenus)
  * [With disabled items](https://www.radix-ui.com/primitives/docs/components/context-menu#with-disabled-items)
  * [With separators](https://www.radix-ui.com/primitives/docs/components/context-menu#with-separators)
  * [With labels](https://www.radix-ui.com/primitives/docs/components/context-menu#with-labels)
  * [With checkbox items](https://www.radix-ui.com/primitives/docs/components/context-menu#with-checkbox-items)
  * [With radio items](https://www.radix-ui.com/primitives/docs/components/context-menu#with-radio-items)
  * [With complex items](https://www.radix-ui.com/primitives/docs/components/context-menu#with-complex-items)
  * [Constrain the content/sub-content size](https://www.radix-ui.com/primitives/docs/components/context-menu#constrain-the-contentsub-content-size)
  * [Origin-aware animations](https://www.radix-ui.com/primitives/docs/components/context-menu#origin-aware-animations)
  * [Collision-aware animations](https://www.radix-ui.com/primitives/docs/components/context-menu#collision-aware-animations)
  * [Accessibility](https://www.radix-ui.com/primitives/docs/components/context-menu#accessibility)
  * [Keyboard Interactions](https://www.radix-ui.com/primitives/docs/components/context-menu#keyboard-interactions)

Previous[Collapsible](https://www.radix-ui.com/primitives/docs/components/collapsible)
Next[Dialog](https://www.radix-ui.com/primitives/docs/components/dialog)
