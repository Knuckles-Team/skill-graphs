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
Guides
# Composition
Use the `asChild` prop to compose Radix's functionality onto alternative element types or your own React components.
All Radix primitive parts that render a DOM element accept an `asChild` prop. When `asChild` is set to `true`, Radix will not render a default DOM element, instead cloning the part's child and passing it the props and behavior required to make it functional.
## [Changing the element type](https://www.radix-ui.com/primitives/docs/guides/composition#changing-the-element-type)
In the majority of cases you shouldn’t need to modify the element type as Radix has been designed to provide the most appropriate defaults. However, there are cases where it is helpful to do so.
A good example is with `Tooltip.Trigger`. By default this part is rendered as a `button`, though you may want to add a tooltip to a link (`a` tag) as well. Let's see how you can achieve this using `asChild`:

```

import * as React from "react";

import { Tooltip } from "radix-ui";

export default () => (

	<Tooltip.Root>

		<Tooltip.Trigger asChild>

			<a href="https://www.radix-ui.com/">Radix UI</a>

		</Tooltip.Trigger>

		<Tooltip.Portal>…</Tooltip.Portal>

	</Tooltip.Root>

);

```

> If you do decide to change the underlying element type, it is your responsibility to ensure it remains accessible and functional. In the case of `Tooltip.Trigger` for example, it must be a focusable element that can respond to pointer and keyboard events. If you were to switch it to a `div`, it would no longer be accessible.
In reality, you will rarely modify the underlying DOM element like we've seen above. Instead it's more common to use your own React components. This is especially true for most `Trigger` parts, as you usually want to compose the functionality with the custom buttons and links in your design system.
## [Composing with your own React components](https://www.radix-ui.com/primitives/docs/guides/composition#composing-with-your-own-react-components)
This works exactly the same as above, you pass `asChild` to the part and then wrap your own component with it. However, there are a few gotchas to be aware of.
### [Your component must spread props](https://www.radix-ui.com/primitives/docs/guides/composition#your-component-must-spread-props)
When Radix clones your component, it will pass its own props and event handlers to make it functional and accessible. If your component doesn't support those props, it will break.
This is done by spreading all of the props onto the underlying DOM node.

```

// before

const MyButton = () => <button />;

// after

const MyButton = (props) => <button {...props} />;

```

We recommend always doing this so that you are not concerned with implementation details (ie. which props/events to accept). We find this is good practice for "leaf" components in general.
> Similarly to when changing the element type directly, it is your responsibility to ensure the element type rendered by your custom component remains accessible and functional.
### [Your component must forward ref](https://www.radix-ui.com/primitives/docs/guides/composition#your-component-must-forward-ref)
Additionally, Radix will sometimes need to attach a `ref` to your component (for example to measure its size). If your component doesn't accept a `ref`, then it will break.
This is done using `React.forwardRef` (read more on

```

// before

const MyButton = (props) => <button {...props} />;

// after

const MyButton = React.forwardRef((props, forwardedRef) => (

	<button {...props} ref={forwardedRef} />

));

```

Whilst this isn't necessary for **all** parts, we recommend always doing it so that you are not concerned with implementation details. This is also generally good practice anyway for leaf components.
## [Composing multiple primitives](https://www.radix-ui.com/primitives/docs/guides/composition#composing-multiple-primitives)
`asChild` can be used as deeply as you need to. This means it is a great way to compose multiple primitive's behavior together. Here is an example of how you can compose `Tooltip.Trigger` and `Dialog.Trigger` together with your own button:

```

import * as React from "react";

import { Dialog, Tooltip } from "radix-ui";

const MyButton = React.forwardRef((props, forwardedRef) => (

	<button {...props} ref={forwardedRef} />

));

export default () => {

	return (

		<Dialog.Root>

			<Tooltip.Root>

				<Tooltip.Trigger asChild>

					<Dialog.Trigger asChild>

						<MyButton>Open dialog</MyButton>

					</Dialog.Trigger>

				</Tooltip.Trigger>

				<Tooltip.Portal>…</Tooltip.Portal>

			</Tooltip.Root>

			<Dialog.Portal>...</Dialog.Portal>

		</Dialog.Root>

	);

};

```

#### Quick nav
  * [Changing the element type](https://www.radix-ui.com/primitives/docs/guides/composition#changing-the-element-type)
  * [Composing with your own React components](https://www.radix-ui.com/primitives/docs/guides/composition#composing-with-your-own-react-components)
  * [Your component must spread props](https://www.radix-ui.com/primitives/docs/guides/composition#your-component-must-spread-props)
  * [Your component must forward ref](https://www.radix-ui.com/primitives/docs/guides/composition#your-component-must-forward-ref)
  * [Composing multiple primitives](https://www.radix-ui.com/primitives/docs/guides/composition#composing-multiple-primitives)

Previous[Animation](https://www.radix-ui.com/primitives/docs/guides/animation)
Next[Server-side rendering](https://www.radix-ui.com/primitives/docs/guides/server-side-rendering)
