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
# Alert Dialog
A modal dialog that interrupts the user with important content and expects a response.
Delete account
index.jsxindex.jsxstyles.cssstyles.css
CSS

```

import * as React from "react";

import { AlertDialog } from "radix-ui";

import "./styles.css";

const AlertDialogDemo = () => (

	<AlertDialog.Root>

		<AlertDialog.Trigger asChild>

			<button className="Button violet">Delete account</button>

		</AlertDialog.Trigger>

		<AlertDialog.Portal>

			<AlertDialog.Overlay className="AlertDialogOverlay" />

			<AlertDialog.Content className="AlertDialogContent">

				<AlertDialog.Title className="AlertDialogTitle">

					Are you absolutely sure?

				</AlertDialog.Title>

				<AlertDialog.Description className="AlertDialogDescription">

					This action cannot be undone. This will permanently delete your

					account and remove your data from our servers.

				</AlertDialog.Description>

				<div style={{ display: "flex", gap: 25, justifyContent: "flex-end" }}>

					<AlertDialog.Cancel asChild>

						<button className="Button mauve">Cancel</button>

					</AlertDialog.Cancel>

					<AlertDialog.Action asChild>

						<button className="Button red">Yes, delete account</button>

					</AlertDialog.Action>

				</div>

			</AlertDialog.Content>

		</AlertDialog.Portal>

	</AlertDialog.Root>

);

export default AlertDialogDemo;

Expand code

```

## Features
  * Focus is automatically trapped.
  * Can be controlled or uncontrolled.
  * Manages screen reader announcements with `Title` and `Description` components.
  * Esc closes the component automatically.

## Component Reference Links
Version: 1.1.16
Size:
[View as Markdown](https://www.radix-ui.com/primitives/docs/components/alert-dialog.md)
## [Anatomy](https://www.radix-ui.com/primitives/docs/components/alert-dialog#anatomy)
Import all parts and piece them together.

```

import { AlertDialog } from "radix-ui";

export default () => (

	<AlertDialog.Root>

		<AlertDialog.Trigger />

		<AlertDialog.Portal>

			<AlertDialog.Overlay />

			<AlertDialog.Content>

				<AlertDialog.Title />

				<AlertDialog.Description />

				<AlertDialog.Cancel />

				<AlertDialog.Action />

			</AlertDialog.Content>

		</AlertDialog.Portal>

	</AlertDialog.Root>

);

```

## [API Reference](https://www.radix-ui.com/primitives/docs/components/alert-dialog#api-reference)
### [Root](https://www.radix-ui.com/primitives/docs/components/alert-dialog#root)
Contains all the parts of an alert dialog.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `defaultOpen` Prop description  | `boolean`  | No default value  |
|  `open` Prop description  | `boolean`  | No default value  |
|  `onOpenChange` Prop description  |  `function` See full type  | No default value  |
### [Trigger](https://www.radix-ui.com/primitives/docs/components/alert-dialog#trigger)
A button that opens the dialog.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
| Data attribute  | Values  |
| --- | --- |
| `[data-state]`  | `"open"  | "closed" `  |
### [Portal](https://www.radix-ui.com/primitives/docs/components/alert-dialog#portal)
When used, portals your overlay and content parts into the `body`.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `forceMount` Prop description  | `boolean`  | No default value  |
|  `container` Prop description  | `HTMLElement`  | `document.body`  |
### [Overlay](https://www.radix-ui.com/primitives/docs/components/alert-dialog#overlay)
A layer that covers the inert portion of the view when the dialog is open.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
|  `forceMount` Prop description  | `boolean`  | No default value  |
| Data attribute  | Values  |
| --- | --- |
| `[data-state]`  | `"open"  | "closed" `  |
### [Content](https://www.radix-ui.com/primitives/docs/components/alert-dialog#content)
Contains content to be rendered when the dialog is open.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
|  `forceMount` Prop description  | `boolean`  | No default value  |
|  `onOpenAutoFocus` Prop description  |  `function` See full type  | No default value  |
|  `onCloseAutoFocus` Prop description  |  `function` See full type  | No default value  |
|  `onEscapeKeyDown` Prop description  |  `function` See full type  | No default value  |
| Data attribute  | Values  |
| --- | --- |
| `[data-state]`  | `"open"  | "closed" `  |
### [Cancel](https://www.radix-ui.com/primitives/docs/components/alert-dialog#cancel)
A button that closes the dialog. This button should be distinguished visually from `AlertDialog.Action` buttons.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
### [Action](https://www.radix-ui.com/primitives/docs/components/alert-dialog#action)
A button that closes the dialog. These buttons should be distinguished visually from the `AlertDialog.Cancel` button.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
### [Title](https://www.radix-ui.com/primitives/docs/components/alert-dialog#title)
An accessible name to be announced when the dialog is opened. Alternatively, you can provide `aria-label` or `aria-labelledby` to `AlertDialog.Content` and exclude this component.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
### [Description](https://www.radix-ui.com/primitives/docs/components/alert-dialog#description)
An accessible description to be announced when the dialog is opened. Alternatively, you can provide `aria-describedby` to `AlertDialog.Content` and exclude this component.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
## [Examples](https://www.radix-ui.com/primitives/docs/components/alert-dialog#examples)
### [Close after asynchronous form submission](https://www.radix-ui.com/primitives/docs/components/alert-dialog#close-after-asynchronous-form-submission)
Use the controlled props to programmatically close the Alert Dialog after an async operation has completed.

```

import * as React from "react";

import { AlertDialog } from "radix-ui";

const wait = () => new Promise((resolve) => setTimeout(resolve, 1000));

export default () => {

	const [open, setOpen] = React.useState(false);

	return (

		<AlertDialog.Root open={open} onOpenChange={setOpen}>

			<AlertDialog.Trigger>Open</AlertDialog.Trigger>

			<AlertDialog.Portal>

				<AlertDialog.Overlay />

				<AlertDialog.Content>

					<form
						onSubmit={(event) => {
							wait().then(() => setOpen(false));
							event.preventDefault();
						}}
					>

						{/** some inputs */}

						<button type="submit">Submit</button>

					</form>

				</AlertDialog.Content>

			</AlertDialog.Portal>

		</AlertDialog.Root>

	);

};

```

### [Custom portal container](https://www.radix-ui.com/primitives/docs/components/alert-dialog#custom-portal-container)
Customise the element that your alert dialog portals into.

```

export default () => {

	const [container, setContainer] = React.useState(null);

	return (

		<div>

			<AlertDialog.Root>

				<AlertDialog.Trigger />

				<AlertDialog.Portal container={container}>

					<AlertDialog.Overlay />

					<AlertDialog.Content>...</AlertDialog.Content>

				</AlertDialog.Portal>

			</AlertDialog.Root>

			<div ref={setContainer} />

		</div>

	);

};

```

## [Accessibility](https://www.radix-ui.com/primitives/docs/components/alert-dialog#accessibility)
Adheres to the
### [Keyboard Interactions](https://www.radix-ui.com/primitives/docs/components/alert-dialog#keyboard-interactions)
| Key  | Description  |
| --- | --- |
| `Space`  | Opens/closes the dialog.  |
| `Enter`  | Opens/closes the dialog.  |
| `Tab`  | Moves focus to the next focusable element.  |
| `Shift + Tab`  | Moves focus to the previous focusable element.  |
| `Esc`  | Closes the dialog and moves focus to `AlertDialog.Trigger`.  |
#### Quick nav
  * [Anatomy](https://www.radix-ui.com/primitives/docs/components/alert-dialog#anatomy)
  * [API Reference](https://www.radix-ui.com/primitives/docs/components/alert-dialog#api-reference)
  * [Root](https://www.radix-ui.com/primitives/docs/components/alert-dialog#root)
  * [Trigger](https://www.radix-ui.com/primitives/docs/components/alert-dialog#trigger)
  * [Portal](https://www.radix-ui.com/primitives/docs/components/alert-dialog#portal)
  * [Overlay](https://www.radix-ui.com/primitives/docs/components/alert-dialog#overlay)
  * [Content](https://www.radix-ui.com/primitives/docs/components/alert-dialog#content)
  * [Cancel](https://www.radix-ui.com/primitives/docs/components/alert-dialog#cancel)
  * [Action](https://www.radix-ui.com/primitives/docs/components/alert-dialog#action)
  * [Title](https://www.radix-ui.com/primitives/docs/components/alert-dialog#title)
  * [Description](https://www.radix-ui.com/primitives/docs/components/alert-dialog#description)
  * [Examples](https://www.radix-ui.com/primitives/docs/components/alert-dialog#examples)
  * [Close after asynchronous form submission](https://www.radix-ui.com/primitives/docs/components/alert-dialog#close-after-asynchronous-form-submission)
  * [Custom portal container](https://www.radix-ui.com/primitives/docs/components/alert-dialog#custom-portal-container)
  * [Accessibility](https://www.radix-ui.com/primitives/docs/components/alert-dialog#accessibility)
  * [Keyboard Interactions](https://www.radix-ui.com/primitives/docs/components/alert-dialog#keyboard-interactions)

Previous[Accordion](https://www.radix-ui.com/primitives/docs/components/accordion)
Next[Aspect Ratio](https://www.radix-ui.com/primitives/docs/components/aspect-ratio)
