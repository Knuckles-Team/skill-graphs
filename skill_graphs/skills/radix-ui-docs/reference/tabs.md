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
# Tabs
A set of layered sections of content—known as tab panels—that are displayed one at a time.
AccountPassword
Make changes to your account here. Click save when you're done.
Name Username
Save changes
index.jsxindex.jsxstyles.cssstyles.css
CSS

```

import * as React from "react";

import { Tabs } from "radix-ui";

import "./styles.css";

const TabsDemo = () => (

	<Tabs.Root className="TabsRoot" defaultValue="tab1">

		<Tabs.List className="TabsList" aria-label="Manage your account">

			<Tabs.Trigger className="TabsTrigger" value="tab1">

				Account

			</Tabs.Trigger>

			<Tabs.Trigger className="TabsTrigger" value="tab2">

				Password

			</Tabs.Trigger>

		</Tabs.List>

		<Tabs.Content className="TabsContent" value="tab1">

			<p className="Text">

				Make changes to your account here. Click save when you&apos;re done.

			</p>

			<fieldset className="Fieldset">

				<label className="Label" htmlFor="name">

					Name

				</label>

				<input className="Input" id="name" defaultValue="Pedro Duarte" />

			</fieldset>

			<fieldset className="Fieldset">

				<label className="Label" htmlFor="username">

					Username

				</label>

				<input className="Input" id="username" defaultValue="@peduarte" />

			</fieldset>

			<div
				style={{ display: "flex", marginTop: 20, justifyContent: "flex-end" }}
			>

				<button className="Button green">Save changes</button>

			</div>

		</Tabs.Content>

		<Tabs.Content className="TabsContent" value="tab2">

			<p className="Text">

				Change your password here. After saving, you&apos;ll be logged out.

			</p>

			<fieldset className="Fieldset">

				<label className="Label" htmlFor="currentPassword">

					Current password

				</label>

				<input className="Input" id="currentPassword" type="password" />

			</fieldset>

			<fieldset className="Fieldset">

				<label className="Label" htmlFor="newPassword">

					New password

				</label>

				<input className="Input" id="newPassword" type="password" />

			</fieldset>

			<fieldset className="Fieldset">

				<label className="Label" htmlFor="confirmPassword">

					Confirm password

				</label>

				<input className="Input" id="confirmPassword" type="password" />

			</fieldset>

			<div
				style={{ display: "flex", marginTop: 20, justifyContent: "flex-end" }}
			>

				<button className="Button green">Change password</button>

			</div>

		</Tabs.Content>

	</Tabs.Root>

);

export default TabsDemo;

Expand code

```

## Features
  * Can be controlled or uncontrolled.
  * Supports horizontal/vertical orientation.
  * Supports automatic/manual activation.
  * Full keyboard navigation.

## Component Reference Links
Version: 1.1.14
Size:
[View as Markdown](https://www.radix-ui.com/primitives/docs/components/tabs.md)
## [Anatomy](https://www.radix-ui.com/primitives/docs/components/tabs#anatomy)
Import all parts and piece them together.

```

import { Tabs } from "radix-ui";

export default () => (

	<Tabs.Root>

		<Tabs.List>

			<Tabs.Trigger />

		</Tabs.List>

		<Tabs.Content />

	</Tabs.Root>

);

```

## [API Reference](https://www.radix-ui.com/primitives/docs/components/tabs#api-reference)
### [Root](https://www.radix-ui.com/primitives/docs/components/tabs#root)
Contains all the tabs component parts.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
|  `defaultValue` Prop description  | `string`  | No default value  |
|  `value` Prop description  | `string`  | No default value  |
|  `onValueChange` Prop description  |  `function` See full type  | No default value  |
|  `orientation` Prop description  |  `enum` See full type  | `"horizontal"`  |
|  `dir` Prop description  |  `enum` See full type  | No default value  |
|  `activationMode` Prop description  |  `enum` See full type  | `"automatic"`  |
| Data attribute  | Values  |
| --- | --- |
| `[data-orientation]`  | `"vertical"  | "horizontal" `  |
### [List](https://www.radix-ui.com/primitives/docs/components/tabs#list)
Contains the triggers that are aligned along the edge of the active content.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
|  `loop` Prop description  | `boolean`  | `true`  |
| Data attribute  | Values  |
| --- | --- |
| `[data-orientation]`  | `"vertical"  | "horizontal" `  |
### [Trigger](https://www.radix-ui.com/primitives/docs/components/tabs#trigger)
The button that activates its associated content.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
|  `value*` Prop description  | `string`  | No default value  |
|  `disabled` Prop description  | `boolean`  | `false`  |
| Data attribute  | Values  |
| --- | --- |
| `[data-state]`  | `"active"  | "inactive" `  |
| `[data-disabled]`  | Present when disabled  |
| `[data-orientation]`  | `"vertical"  | "horizontal" `  |
### [Content](https://www.radix-ui.com/primitives/docs/components/tabs#content)
Contains the content associated with each trigger.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
|  `value*` Prop description  | `string`  | No default value  |
|  `forceMount` Prop description  | `boolean`  | No default value  |
| Data attribute  | Values  |
| --- | --- |
| `[data-state]`  | `"active"  | "inactive" `  |
| `[data-orientation]`  | `"vertical"  | "horizontal" `  |
## [Examples](https://www.radix-ui.com/primitives/docs/components/tabs#examples)
### [Vertical](https://www.radix-ui.com/primitives/docs/components/tabs#vertical)
You can create vertical tabs by using the `orientation` prop.

```

import { Tabs } from "radix-ui";

export default () => (

	<Tabs.Root defaultValue="tab1" orientation="vertical">

		<Tabs.List aria-label="tabs example">

			<Tabs.Trigger value="tab1">One</Tabs.Trigger>

			<Tabs.Trigger value="tab2">Two</Tabs.Trigger>

			<Tabs.Trigger value="tab3">Three</Tabs.Trigger>

		</Tabs.List>

		<Tabs.Content value="tab1">Tab one content</Tabs.Content>

		<Tabs.Content value="tab2">Tab two content</Tabs.Content>

		<Tabs.Content value="tab3">Tab three content</Tabs.Content>

	</Tabs.Root>

);

```

## [Accessibility](https://www.radix-ui.com/primitives/docs/components/tabs#accessibility)
Adheres to the
### [Keyboard Interactions](https://www.radix-ui.com/primitives/docs/components/tabs#keyboard-interactions)
| Key  | Description  |
| --- | --- |
| `Tab`  | When focus moves onto the tabs, focuses the active trigger. When a trigger is focused, moves focus to the active content.  |
| `ArrowDown`  | Moves focus to the next trigger depending on `orientation` and activates its associated content.  |
| `ArrowRight`  | Moves focus to the next trigger depending on `orientation` and activates its associated content.  |
| `ArrowUp`  | Moves focus to the previous trigger depending on `orientation` and activates its associated content.  |
| `ArrowLeft`  | Moves focus to the previous trigger depending on `orientation` and activates its associated content.  |
| `Home`  | Moves focus to the first trigger and activates its associated content.  |
| `End`  | Moves focus to the last trigger and activates its associated content.  |
#### Quick nav
  * [Anatomy](https://www.radix-ui.com/primitives/docs/components/tabs#anatomy)
  * [API Reference](https://www.radix-ui.com/primitives/docs/components/tabs#api-reference)
  * [Root](https://www.radix-ui.com/primitives/docs/components/tabs#root)
  * [List](https://www.radix-ui.com/primitives/docs/components/tabs#list)
  * [Trigger](https://www.radix-ui.com/primitives/docs/components/tabs#trigger)
  * [Content](https://www.radix-ui.com/primitives/docs/components/tabs#content)
  * [Examples](https://www.radix-ui.com/primitives/docs/components/tabs#examples)
  * [Vertical](https://www.radix-ui.com/primitives/docs/components/tabs#vertical)
  * [Accessibility](https://www.radix-ui.com/primitives/docs/components/tabs#accessibility)
  * [Keyboard Interactions](https://www.radix-ui.com/primitives/docs/components/tabs#keyboard-interactions)

Previous[Switch](https://www.radix-ui.com/primitives/docs/components/switch)
Next[Toast](https://www.radix-ui.com/primitives/docs/components/toast)
