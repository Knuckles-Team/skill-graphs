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
# Menu Bar
A visually persistent menu common in desktop applications that provides quick access to a consistent set of commands.
FileEditViewProfiles
index.jsxindex.jsxstyles.cssstyles.css
CSS

```

import * as React from "react";

import { Menubar } from "radix-ui";

import {
	CheckIcon,
	ChevronRightIcon,
	DotFilledIcon,
} from "@radix-ui/react-icons";

import "./styles.css";

const RADIO_ITEMS = ["Andy", "Benoît", "Luis"];

const CHECK_ITEMS = ["Always Show Bookmarks Bar", "Always Show Full URLs"];

const MenubarDemo = () => {

	const [checkedSelection, setCheckedSelection] = React.useState([

		CHECK_ITEMS[1],

	]);

	const [radioSelection, setRadioSelection] = React.useState(RADIO_ITEMS[2]);

	return (

		<Menubar.Root className="MenubarRoot">

			<Menubar.Menu>

				<Menubar.Trigger className="MenubarTrigger">File</Menubar.Trigger>

				<Menubar.Portal>

					<Menubar.Content
						className="MenubarContent"
						align="start"
						sideOffset={5}
						alignOffset={-3}
					>

						<Menubar.Item className="MenubarItem">

							New Tab <div className="RightSlot">⌘ T</div>

						</Menubar.Item>

						<Menubar.Item className="MenubarItem">

							New Window <div className="RightSlot">⌘ N</div>

						</Menubar.Item>

						<Menubar.Item className="MenubarItem" disabled>

							New Incognito Window

						</Menubar.Item>

						<Menubar.Separator className="MenubarSeparator" />

						<Menubar.Sub>

							<Menubar.SubTrigger className="MenubarSubTrigger">

								Share

								<div className="RightSlot">

									<ChevronRightIcon />

								</div>

							</Menubar.SubTrigger>

							<Menubar.Portal>

								<Menubar.SubContent
									className="MenubarSubContent"
									alignOffset={-5}
								>

									<Menubar.Item className="MenubarItem">

										Email Link

									</Menubar.Item>

									<Menubar.Item className="MenubarItem">Messages</Menubar.Item>

									<Menubar.Item className="MenubarItem">Notes</Menubar.Item>

								</Menubar.SubContent>

							</Menubar.Portal>

						</Menubar.Sub>

						<Menubar.Separator className="MenubarSeparator" />

						<Menubar.Item className="MenubarItem">

							Print… <div className="RightSlot">⌘ P</div>

						</Menubar.Item>

					</Menubar.Content>

				</Menubar.Portal>

			</Menubar.Menu>

			<Menubar.Menu>

				<Menubar.Trigger className="MenubarTrigger">Edit</Menubar.Trigger>

				<Menubar.Portal>

					<Menubar.Content
						className="MenubarContent"
						align="start"
						sideOffset={5}
						alignOffset={-3}
					>

						<Menubar.Item className="MenubarItem">

							Undo <div className="RightSlot">⌘ Z</div>

						</Menubar.Item>

						<Menubar.Item className="MenubarItem">

							Redo <div className="RightSlot">⇧ ⌘ Z</div>

						</Menubar.Item>

						<Menubar.Separator className="MenubarSeparator" />

						<Menubar.Sub>

							<Menubar.SubTrigger className="MenubarSubTrigger">

								Find

								<div className="RightSlot">

									<ChevronRightIcon />

								</div>

							</Menubar.SubTrigger>

							<Menubar.Portal>

								<Menubar.SubContent
									className="MenubarSubContent"
									alignOffset={-5}
								>

									<Menubar.Item className="MenubarItem">

										Search the web…

									</Menubar.Item>

									<Menubar.Separator className="MenubarSeparator" />

									<Menubar.Item className="MenubarItem">Find…</Menubar.Item>

									<Menubar.Item className="MenubarItem">Find Next</Menubar.Item>

									<Menubar.Item className="MenubarItem">

										Find Previous

									</Menubar.Item>

								</Menubar.SubContent>

							</Menubar.Portal>

						</Menubar.Sub>

						<Menubar.Separator className="MenubarSeparator" />

						<Menubar.Item className="MenubarItem">Cut</Menubar.Item>

						<Menubar.Item className="MenubarItem">Copy</Menubar.Item>

						<Menubar.Item className="MenubarItem">Paste</Menubar.Item>

					</Menubar.Content>

				</Menubar.Portal>

			</Menubar.Menu>

			<Menubar.Menu>

				<Menubar.Trigger className="MenubarTrigger">View</Menubar.Trigger>

				<Menubar.Portal>

					<Menubar.Content
						className="MenubarContent"
						align="start"
						sideOffset={5}
						alignOffset={-14}
					>

						{CHECK_ITEMS.map((item) => (

							<Menubar.CheckboxItem
								className="MenubarCheckboxItem inset"
								key={item}
								checked={checkedSelection.includes(item)}
								onCheckedChange={() =>
									setCheckedSelection((current) =>
										current.includes(item)
											? current.filter((el) => el !== item)
											: current.concat(item),
									)
								}
							>

								<Menubar.ItemIndicator className="MenubarItemIndicator">

									<CheckIcon />

								</Menubar.ItemIndicator>

								{item}

							</Menubar.CheckboxItem>

						))}

						<Menubar.Separator className="MenubarSeparator" />

						<Menubar.Item className="MenubarItem inset">

							Reload <div className="RightSlot">⌘ R</div>

						</Menubar.Item>

						<Menubar.Item className="MenubarItem inset" disabled>

							Force Reload <div className="RightSlot">⇧ ⌘ R</div>

						</Menubar.Item>

						<Menubar.Separator className="MenubarSeparator" />

						<Menubar.Item className="MenubarItem inset">

							Toggle Fullscreen

						</Menubar.Item>

						<Menubar.Separator className="MenubarSeparator" />

						<Menubar.Item className="MenubarItem inset">

							Hide Sidebar

						</Menubar.Item>

					</Menubar.Content>

				</Menubar.Portal>

			</Menubar.Menu>

			<Menubar.Menu>

				<Menubar.Trigger className="MenubarTrigger">Profiles</Menubar.Trigger>

				<Menubar.Portal>

					<Menubar.Content
						className="MenubarContent"
						align="start"
						sideOffset={5}
						alignOffset={-14}
					>

						<Menubar.RadioGroup
							value={radioSelection}
							onValueChange={setRadioSelection}
						>

							{RADIO_ITEMS.map((item) => (

								<Menubar.RadioItem
									className="MenubarRadioItem inset"
									key={item}
									value={item}
								>

									<Menubar.ItemIndicator className="MenubarItemIndicator">

										<DotFilledIcon />

									</Menubar.ItemIndicator>

									{item}

								</Menubar.RadioItem>

							))}

							<Menubar.Separator className="MenubarSeparator" />

							<Menubar.Item className="MenubarItem inset">Edit…</Menubar.Item>

							<Menubar.Separator className="MenubarSeparator" />

							<Menubar.Item className="MenubarItem inset">

								Add Profile…

							</Menubar.Item>

						</Menubar.RadioGroup>

					</Menubar.Content>

				</Menubar.Portal>

			</Menubar.Menu>

		</Menubar.Root>

	);

};

export default MenubarDemo;

Expand code

```

## Features
  * Can be controlled or uncontrolled.
  * Supports submenus with configurable reading direction.
  * Supports items, labels, groups of items.
  * Supports checkable items (single or multiple).
  * Customize side, alignment, offsets, collision handling.
  * Optionally render a pointing arrow.
  * Focus is fully managed.
  * Full keyboard navigation.
  * Typeahead support.

## Component Reference Links
Version: 1.1.17
Size:
[View as Markdown](https://www.radix-ui.com/primitives/docs/components/menubar.md)
## [Anatomy](https://www.radix-ui.com/primitives/docs/components/menubar#anatomy)
Import all parts and piece them together.

```

import { Menubar } from "radix-ui";

export default () => (

	<Menubar.Root>

		<Menubar.Menu>

			<Menubar.Trigger />

			<Menubar.Portal>

				<Menubar.Content>

					<Menubar.Label />

					<Menubar.Item />

					<Menubar.Group>

						<Menubar.Item />

					</Menubar.Group>

					<Menubar.CheckboxItem>

						<Menubar.ItemIndicator />

					</Menubar.CheckboxItem>

					<Menubar.RadioGroup>

						<Menubar.RadioItem>

							<Menubar.ItemIndicator />

						</Menubar.RadioItem>

					</Menubar.RadioGroup>

					<Menubar.Sub>

						<Menubar.SubTrigger />

						<Menubar.Portal>

							<Menubar.SubContent />

						</Menubar.Portal>

					</Menubar.Sub>

					<Menubar.Separator />

					<Menubar.Arrow />

				</Menubar.Content>

			</Menubar.Portal>

		</Menubar.Menu>

	</Menubar.Root>

);

```

## [API Reference](https://www.radix-ui.com/primitives/docs/components/menubar#api-reference)
### [Root](https://www.radix-ui.com/primitives/docs/components/menubar#root)
Contains all the parts of a menubar.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
|  `defaultValue` Prop description  | `string`  | No default value  |
|  `value` Prop description  | `string`  | No default value  |
|  `onValueChange` Prop description  |  `function` See full type  | No default value  |
|  `dir` Prop description  |  `enum` See full type  | No default value  |
|  `loop` Prop description  | `boolean`  | `false`  |
### [Menu](https://www.radix-ui.com/primitives/docs/components/menubar#menu)
A top level menu item, contains a trigger with content combination.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
|  `value` Prop description  | `string`  | No default value  |
### [Trigger](https://www.radix-ui.com/primitives/docs/components/menubar#trigger)
The button that toggles the content. By default, the `Menubar.Content` will position itself against the trigger.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
| Data attribute  | Values  |
| --- | --- |
| `[data-state]`  | `"open"  | "closed" `  |
| `[data-highlighted]`  | Present when highlighted  |
| `[data-disabled]`  | Present when disabled  |
### [Portal](https://www.radix-ui.com/primitives/docs/components/menubar#portal)
When used, portals the content part into the `body`.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `forceMount` Prop description  | `boolean`  | No default value  |
|  `container` Prop description  | `HTMLElement`  | `document.body`  |
### [Content](https://www.radix-ui.com/primitives/docs/components/menubar#content)
The component that pops out when a menu is open.
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
| CSS Variable  | Description  |
| --- | --- |
| `--radix-menubar-content-transform-origin`  | The `transform-origin` computed from the content and arrow positions/offsets  |
| `--radix-menubar-content-available-width`  | The remaining width between the trigger and the boundary edge  |
| `--radix-menubar-content-available-height`  | The remaining height between the trigger and the boundary edge  |
| `--radix-menubar-trigger-width`  | The width of the trigger  |
| `--radix-menubar-trigger-height`  | The height of the trigger  |
### [Arrow](https://www.radix-ui.com/primitives/docs/components/menubar#arrow)
An optional arrow element to render alongside a menubar menu. This can be used to help visually link the trigger with the `Menubar.Content`. Must be rendered inside `Menubar.Content`.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
|  `width` Prop description  | `number`  | `10`  |
|  `height` Prop description  | `number`  | `5`  |
### [Item](https://www.radix-ui.com/primitives/docs/components/menubar#item)
The component that contains the menubar items.
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
### [Group](https://www.radix-ui.com/primitives/docs/components/menubar#group)
Used to group multiple `Menubar.Item`s.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
### [Label](https://www.radix-ui.com/primitives/docs/components/menubar#label)
Used to render a label. It won't be focusable using arrow keys.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
### [CheckboxItem](https://www.radix-ui.com/primitives/docs/components/menubar#checkboxitem)
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
| `[data-state]`  | `"checked"  | "unchecked" `  |
| `[data-highlighted]`  | Present when highlighted  |
| `[data-disabled]`  | Present when disabled  |
### [RadioGroup](https://www.radix-ui.com/primitives/docs/components/menubar#radiogroup)
Used to group multiple `Menubar.RadioItem`s.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
|  `value` Prop description  | `string`  | No default value  |
|  `onValueChange` Prop description  |  `function` See full type  | No default value  |
### [RadioItem](https://www.radix-ui.com/primitives/docs/components/menubar#radioitem)
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
| `[data-state]`  | `"checked"  | "unchecked" `  |
| `[data-highlighted]`  | Present when highlighted  |
| `[data-disabled]`  | Present when disabled  |
### [ItemIndicator](https://www.radix-ui.com/primitives/docs/components/menubar#itemindicator)
Renders when the parent `Menubar.CheckboxItem` or `Menubar.RadioItem` is checked. You can style this element directly, or you can use it as a wrapper to put an icon into, or both.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
|  `forceMount` Prop description  | `boolean`  | No default value  |
| Data attribute  | Values  |
| --- | --- |
| `[data-state]`  | `"checked"  | "unchecked" `  |
### [Separator](https://www.radix-ui.com/primitives/docs/components/menubar#separator)
Used to visually separate items in a menubar menu.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
### [Sub](https://www.radix-ui.com/primitives/docs/components/menubar#sub)
Contains all the parts of a submenu.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `defaultOpen` Prop description  | `boolean`  | No default value  |
|  `open` Prop description  | `boolean`  | No default value  |
|  `onOpenChange` Prop description  |  `function` See full type  | No default value  |
### [SubTrigger](https://www.radix-ui.com/primitives/docs/components/menubar#subtrigger)
An item that opens a submenu. Must be rendered inside `Menubar.Sub`.
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
### [SubContent](https://www.radix-ui.com/primitives/docs/components/menubar#subcontent)
The component that pops out when a submenu is open. Must be rendered inside `Menubar.Sub`.
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
| CSS Variable  | Description  |
| --- | --- |
| `--radix-menubar-content-transform-origin`  | The `transform-origin` computed from the content and arrow positions/offsets  |
| `--radix-menubar-content-available-width`  | The remaining width between the trigger and the boundary edge  |
| `--radix-menubar-content-available-height`  | The remaining height between the trigger and the boundary edge  |
| `--radix-menubar-trigger-width`  | The width of the trigger  |
| `--radix-menubar-trigger-height`  | The height of the trigger  |
## [Examples](https://www.radix-ui.com/primitives/docs/components/menubar#examples)
### [With submenus](https://www.radix-ui.com/primitives/docs/components/menubar#with-submenus)
You can create submenus by using `Menubar.Sub` in combination with its parts.

```

<Menubar.Root>

	<Menubar.Menu>

		<Menubar.Trigger>…</Menubar.Trigger>

		<Menubar.Portal>

			<Menubar.Content>

				<Menubar.Item>…</Menubar.Item>

				<Menubar.Item>…</Menubar.Item>

				<Menubar.Separator />

				<Menubar.Sub>

					<Menubar.SubTrigger>Sub menu →</Menubar.SubTrigger>

					<Menubar.Portal>

						<Menubar.SubContent>

							<Menubar.Item>Sub menu item</Menubar.Item>

							<Menubar.Item>Sub menu item</Menubar.Item>

							<Menubar.Arrow />

						</Menubar.SubContent>

					</Menubar.Portal>

				</Menubar.Sub>

				<Menubar.Separator />

				<Menubar.Item>…</Menubar.Item>

			</Menubar.Content>

		</Menubar.Portal>

	</Menubar.Menu>

</Menubar.Root>

```

### [With disabled items](https://www.radix-ui.com/primitives/docs/components/menubar#with-disabled-items)
You can add special styles to disabled items via the `data-disabled` attribute.

```

// index.jsx

import { Menubar } from "radix-ui";

import "./styles.css";

export default () => (

	<Menubar.Root>

		<Menubar.Menu>

			<Menubar.Trigger>…</Menubar.Trigger>

			<Menubar.Portal>

				<Menubar.Content>

					<Menubar.Item className="MenubarItem" disabled>

						…

					</Menubar.Item>

					<Menubar.Item className="MenubarItem">…</Menubar.Item>

				</Menubar.Content>

			</Menubar.Portal>

		</Menubar.Menu>

	</Menubar.Root>

);

```

```

/* styles.css */

.MenubarItem[data-disabled] {

	color: gainsboro;

}

```

### [With separators](https://www.radix-ui.com/primitives/docs/components/menubar#with-separators)
Use the `Separator` part to add a separator between items.

```

<Menubar.Root>

	<Menubar.Menu>

		<Menubar.Trigger>…</Menubar.Trigger>

		<Menubar.Portal>

			<Menubar.Content>

				<Menubar.Item>…</Menubar.Item>

				<Menubar.Separator />

				<Menubar.Item>…</Menubar.Item>

				<Menubar.Separator />

				<Menubar.Item>…</Menubar.Item>

			</Menubar.Content>

		</Menubar.Portal>

	</Menubar.Menu>

</Menubar.Root>

```

### [With labels](https://www.radix-ui.com/primitives/docs/components/menubar#with-labels)
Use the `Label` part to help label a section.

```

<Menubar.Root>

	<Menubar.Menu>

		<Menubar.Trigger>…</Menubar.Trigger>

		<Menubar.Portal>

			<Menubar.Content>

				<Menubar.Label>Label</Menubar.Label>

				<Menubar.Item>…</Menubar.Item>

				<Menubar.Item>…</Menubar.Item>

				<Menubar.Item>…</Menubar.Item>

			</Menubar.Content>

		</Menubar.Portal>

	</Menubar.Menu>

</Menubar.Root>

```

### [With checkbox items](https://www.radix-ui.com/primitives/docs/components/menubar#with-checkbox-items)
Use the `CheckboxItem` part to add an item that can be checked.

```

import * as React from "react";

import { CheckIcon } from "@radix-ui/react-icons";

import { Menubar } from "radix-ui";

export default () => {

	const [checked, setChecked] = React.useState(true);

	return (

		<Menubar.Root>

			<Menubar.Menu>

				<Menubar.Trigger>…</Menubar.Trigger>

				<Menubar.Portal>

					<Menubar.Content>

						<Menubar.Item>…</Menubar.Item>

						<Menubar.Item>…</Menubar.Item>

						<Menubar.Separator />

						<Menubar.CheckboxItem
							checked={checked}
							onCheckedChange={setChecked}
						>

							<Menubar.ItemIndicator>

								<CheckIcon />

							</Menubar.ItemIndicator>

							Checkbox item

						</Menubar.CheckboxItem>

					</Menubar.Content>

				</Menubar.Portal>

			</Menubar.Menu>

		</Menubar.Root>

	);

};

```

### [With radio items](https://www.radix-ui.com/primitives/docs/components/menubar#with-radio-items)
Use the `RadioGroup` and `RadioItem` parts to add an item that can be checked amongst others.

```

import * as React from "react";

import { CheckIcon } from "@radix-ui/react-icons";

import { Menubar } from "radix-ui";

export default () => {

	const [color, setColor] = React.useState("blue");

	return (

		<Menubar.Root>

			<Menubar.Menu>

				<Menubar.Trigger>…</Menubar.Trigger>

				<Menubar.Portal>

					<Menubar.Content>

						<Menubar.RadioGroup value={color} onValueChange={setColor}>

							<Menubar.RadioItem value="red">

								<Menubar.ItemIndicator>

									<CheckIcon />

								</Menubar.ItemIndicator>

								Red

							</Menubar.RadioItem>

							<Menubar.RadioItem value="blue">

								<Menubar.ItemIndicator>

									<CheckIcon />

								</Menubar.ItemIndicator>

								Blue

							</Menubar.RadioItem>

						</Menubar.RadioGroup>

					</Menubar.Content>

				</Menubar.Portal>

			</Menubar.Menu>

		</Menubar.Root>

	);

};

```

### [With complex items](https://www.radix-ui.com/primitives/docs/components/menubar#with-complex-items)
You can add extra decorative elements in the `Item` parts, such as images.

```

import { Menubar } from "radix-ui";

export default () => (

	<Menubar.Root>

		<Menubar.Menu>

			<Menubar.Trigger>…</Menubar.Trigger>

			<Menubar.Portal>

				<Menubar.Content>

					<Menubar.Item>

						<img src="…" />

						Adolfo Hess

					</Menubar.Item>

					<Menubar.Item>

						<img src="…" />

						Miyah Myles

					</Menubar.Item>

				</Menubar.Content>

			</Menubar.Portal>

		</Menubar.Menu>

	</Menubar.Root>

);

```

### [Constrain the content/sub-content size](https://www.radix-ui.com/primitives/docs/components/menubar#constrain-the-contentsub-content-size)
You may want to constrain the width of the content (or sub-content) so that it matches the trigger (or sub-trigger) width. You may also want to constrain its height to not exceed the viewport.
We expose several CSS custom properties such as `--radix-menubar-trigger-width` and `--radix-menubar-content-available-height` to support this. Use them to constrain the content dimensions.

```

// index.jsx

import { Menubar } from "radix-ui";

import "./styles.css";

export default () => (

	<Menubar.Root>

		<Menubar.Trigger>…</Menubar.Trigger>

		<Menubar.Portal>

			<Menubar.Content className="MenubarContent" sideOffset={5}>

				…

			</Menubar.Content>

		</Menubar.Portal>

	</Menubar.Root>

);

```

```

/* styles.css */

.MenubarContent {

	width: var(--radix-menubar-trigger-width);

	max-height: var(--radix-menubar-content-available-height);

}

```

### [Origin-aware animations](https://www.radix-ui.com/primitives/docs/components/menubar#origin-aware-animations)
We expose a CSS custom property `--radix-menubar-content-transform-origin`. Use it to animate the content from its computed origin based on `side`, `sideOffset`, `align`, `alignOffset` and any collisions.

```

// index.jsx

import { Menubar } from "radix-ui";

import "./styles.css";

export default () => (

	<Menubar.Root>

		<Menubar.Menu>

			<Menubar.Trigger>…</Menubar.Trigger>

			<Menubar.Portal>

				<Menubar.Content className="MenubarContent">…</Menubar.Content>

			</Menubar.Portal>

		</Menubar.Menu>

	</Menubar.Root>

);

```

```

/* styles.css */

.MenubarContent {

	transform-origin: var(--radix-menubar-content-transform-origin);

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

### [Collision-aware animations](https://www.radix-ui.com/primitives/docs/components/menubar#collision-aware-animations)
We expose `data-side` and `data-align` attributes. Their values will change at runtime to reflect collisions. Use them to create collision and direction-aware animations.

```

// index.jsx

import { Menubar } from "radix-ui";

import "./styles.css";

export default () => (

	<Menubar.Root>

		<Menubar.Menu>

			<Menubar.Trigger>…</Menubar.Trigger>

			<Menubar.Portal>

				<Menubar.Content className="MenubarContent">…</Menubar.Content>

			</Menubar.Portal>

		</Menubar.Menu>

	</Menubar.Root>

);

```

```

/* styles.css */

.MenubarContent {

	animation-duration: 0.6s;

	animation-timing-function: cubic-bezier(0.16, 1, 0.3, 1);

}

.MenubarContent[data-side="top"] {

	animation-name: slideUp;

}

.MenubarContent[data-side="bottom"] {

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

## [Accessibility](https://www.radix-ui.com/primitives/docs/components/menubar#accessibility)
Adheres to the
### [Keyboard Interactions](https://www.radix-ui.com/primitives/docs/components/menubar#keyboard-interactions)
| Key  | Description  |
| --- | --- |
| `Space`  | When focus is on `Menubar.Trigger`, opens the menubar and focuses the first item.
When focus is on an item, activates the focused item.  |
| `Enter`  | When focus is on `Menubar.Trigger`, opens the associated menu.
When focus is on an item, activates the focused item.  |
| `ArrowDown`  | When focus is on `Menubar.Trigger`, opens the associated menu.
When focus is on an item, moves focus to the next item.  |
| `ArrowUp`  | When focus is on an item, moves focus to the previous item.  |
|  `ArrowRight``ArrowLeft`  | When focus is on a `Menubar.Trigger`, moves focus to the next or previous item.
When focus is on a `Menubar.SubTrigger`, opens or closes the submenu depending on reading direction.
When focus is within a `Menubar.Content`, opens the next menu in the menubar.  |
| `Esc`  | Closes the currently open menu and moves focus to its `Menubar.Trigger`.  |
#### Quick nav
  * [Anatomy](https://www.radix-ui.com/primitives/docs/components/menubar#anatomy)
  * [API Reference](https://www.radix-ui.com/primitives/docs/components/menubar#api-reference)
  * [Root](https://www.radix-ui.com/primitives/docs/components/menubar#root)
  * [Menu](https://www.radix-ui.com/primitives/docs/components/menubar#menu)
  * [Trigger](https://www.radix-ui.com/primitives/docs/components/menubar#trigger)
  * [Portal](https://www.radix-ui.com/primitives/docs/components/menubar#portal)
  * [Content](https://www.radix-ui.com/primitives/docs/components/menubar#content)
  * [Arrow](https://www.radix-ui.com/primitives/docs/components/menubar#arrow)
  * [Item](https://www.radix-ui.com/primitives/docs/components/menubar#item)
  * [Group](https://www.radix-ui.com/primitives/docs/components/menubar#group)
  * [Label](https://www.radix-ui.com/primitives/docs/components/menubar#label)
  * [CheckboxItem](https://www.radix-ui.com/primitives/docs/components/menubar#checkboxitem)
  * [RadioGroup](https://www.radix-ui.com/primitives/docs/components/menubar#radiogroup)
  * [RadioItem](https://www.radix-ui.com/primitives/docs/components/menubar#radioitem)
  * [ItemIndicator](https://www.radix-ui.com/primitives/docs/components/menubar#itemindicator)
  * [Separator](https://www.radix-ui.com/primitives/docs/components/menubar#separator)
  * [Sub](https://www.radix-ui.com/primitives/docs/components/menubar#sub)
  * [SubTrigger](https://www.radix-ui.com/primitives/docs/components/menubar#subtrigger)
  * [SubContent](https://www.radix-ui.com/primitives/docs/components/menubar#subcontent)
  * [Examples](https://www.radix-ui.com/primitives/docs/components/menubar#examples)
  * [With submenus](https://www.radix-ui.com/primitives/docs/components/menubar#with-submenus)
  * [With disabled items](https://www.radix-ui.com/primitives/docs/components/menubar#with-disabled-items)
  * [With separators](https://www.radix-ui.com/primitives/docs/components/menubar#with-separators)
  * [With labels](https://www.radix-ui.com/primitives/docs/components/menubar#with-labels)
  * [With checkbox items](https://www.radix-ui.com/primitives/docs/components/menubar#with-checkbox-items)
  * [With radio items](https://www.radix-ui.com/primitives/docs/components/menubar#with-radio-items)
  * [With complex items](https://www.radix-ui.com/primitives/docs/components/menubar#with-complex-items)
  * [Constrain the content/sub-content size](https://www.radix-ui.com/primitives/docs/components/menubar#constrain-the-contentsub-content-size)
  * [Origin-aware animations](https://www.radix-ui.com/primitives/docs/components/menubar#origin-aware-animations)
  * [Collision-aware animations](https://www.radix-ui.com/primitives/docs/components/menubar#collision-aware-animations)
  * [Accessibility](https://www.radix-ui.com/primitives/docs/components/menubar#accessibility)
  * [Keyboard Interactions](https://www.radix-ui.com/primitives/docs/components/menubar#keyboard-interactions)

Previous[Label](https://www.radix-ui.com/primitives/docs/components/label)
Next[Navigation Menu](https://www.radix-ui.com/primitives/docs/components/navigation-menu)
