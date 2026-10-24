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
# Animation
Animate Radix Primitives with CSS keyframes or the JavaScript animation library of your choice.
Adding animation to Radix Primitives should feel similar to any other component, but there are some caveats noted here in regards to exiting animations with JS animation libraries.
## [Animating with CSS animation](https://www.radix-ui.com/primitives/docs/guides/animation#animating-with-css-animation)
The simplest way to animate Primitives is with CSS.
You can use CSS animation to animate both mount and unmount phases. The latter is possible because the Radix Primitives will suspend unmount while your animation plays out.

```

@keyframes fadeIn {

	from {

		opacity: 0;

	}

	to {

		opacity: 1;

	}

}

@keyframes fadeOut {

	from {

		opacity: 1;

	}

	to {

		opacity: 0;

	}

}

.DialogOverlay[data-state="open"],
.DialogContent[data-state="open"] {

	animation: fadeIn 300ms ease-out;

}

.DialogOverlay[data-state="closed"],
.DialogContent[data-state="closed"] {

	animation: fadeOut 300ms ease-in;

}

```

## [Delegating unmounting for JavaScript Animation](https://www.radix-ui.com/primitives/docs/guides/animation#delegating-unmounting-for-javascript-animation)
When many stateful Primitives are hidden from view, they are actually removed from the React Tree, and their elements removed from the DOM. JavaScript animation libraries need control of the unmounting phase, so we provide the `forceMount` prop on many components to allow consumers to delegate the mounting and unmounting of children based on the animation state determined by those libraries.
For example, if you want to use React Spring to animate a `Dialog`, you would do so by conditionally rendering the dialog `Overlay` and `Content` parts based on the animation state from one of its hooks like `useTransition`:

```

import { Dialog } from "radix-ui";

import { useTransition, animated, config } from "react-spring";

function Example() {

	const [open, setOpen] = React.useState(false);

	const transitions = useTransition(open, {

		from: { opacity: 0, y: -10 },

		enter: { opacity: 1, y: 0 },

		leave: { opacity: 0, y: 10 },

		config: config.stiff,

	});

	return (

		<Dialog.Root open={open} onOpenChange={setOpen}>

			<Dialog.Trigger>Open Dialog</Dialog.Trigger>

			{transitions((styles, item) =>

				item ? (

					<>

						<Dialog.Overlay forceMount asChild>

							<animated.div
								style={{
									opacity: styles.opacity,
								}}
							/>

						</Dialog.Overlay>

						<Dialog.Content forceMount asChild>

							<animated.div style={styles}>

								<h1>Hello from inside the Dialog!</h1>

								<Dialog.Close>close</Dialog.Close>

							</animated.div>

						</Dialog.Content>

					</>

				) : null,

			)}

		</Dialog.Root>

	);

}

```

#### Quick nav
  * [Animating with CSS animation](https://www.radix-ui.com/primitives/docs/guides/animation#animating-with-css-animation)
  * [Delegating unmounting for JavaScript Animation](https://www.radix-ui.com/primitives/docs/guides/animation#delegating-unmounting-for-javascript-animation)

Previous[Styling](https://www.radix-ui.com/primitives/docs/guides/styling)
Next[Composition](https://www.radix-ui.com/primitives/docs/guides/composition)
