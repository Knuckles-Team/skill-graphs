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
# Toast
A succinct message that is displayed temporarily.
Add to calendar
index.jsxindex.jsxstyles.cssstyles.css
CSS

```

import * as React from "react";

import { Toast } from "radix-ui";

import "./styles.css";

const ToastDemo = () => {

	const [open, setOpen] = React.useState(false);

	const eventDateRef = React.useRef(new Date());

	const timerRef = React.useRef(0);

	React.useEffect(() => {

		return () => clearTimeout(timerRef.current);

	}, []);

	return (

		<Toast.Provider swipeDirection="right">

			<button
				className="Button large violet"
				onClick={() => {
					setOpen(false);
					window.clearTimeout(timerRef.current);
					timerRef.current = window.setTimeout(() => {
						eventDateRef.current = oneWeekAway(new Date());
						setOpen(true);
					}, 100);
				}}
			>

				Add to calendar

			</button>

			<Toast.Root className="ToastRoot" open={open} onOpenChange={setOpen}>

				<Toast.Title className="ToastTitle">Scheduled: Catch up</Toast.Title>

				<Toast.Description asChild>

					<time
						className="ToastDescription"
						dateTime={eventDateRef.current.toISOString()}
					>

						{prettyDate(eventDateRef.current)}

					</time>

				</Toast.Description>

				<Toast.Action
					className="ToastAction"
					asChild
					altText="Goto schedule to undo"
				>

					<button className="Button small green">Undo</button>

				</Toast.Action>

			</Toast.Root>

			<Toast.Viewport className="ToastViewport" />

		</Toast.Provider>

	);

};

function oneWeekAway(date) {

	const now = new Date(date);

	const inOneWeek = now.setDate(now.getDate() + 7);

	return new Date(inOneWeek);

}

function prettyDate(date) {

	return new Intl.DateTimeFormat("en-US", {

		dateStyle: "full",

		timeStyle: "short",

	}).format(date);

}

export default ToastDemo;

Expand code

```

## Features
  * Automatically closes.
  * Pauses closing on hover, focus and window blur.
  * Supports hotkey to jump to toast viewport.
  * Supports closing via swipe gesture.
  * Exposes CSS variables for swipe gesture animations.
  * Can be controlled or uncontrolled.

## Component Reference Links
Version: 1.2.16
Size:
[View as Markdown](https://www.radix-ui.com/primitives/docs/components/toast.md)
## [Anatomy](https://www.radix-ui.com/primitives/docs/components/toast#anatomy)
Import the component.

```

import { Toast } from "radix-ui";

export default () => (

	<Toast.Provider>

		<Toast.Root>

			<Toast.Title />

			<Toast.Description />

			<Toast.Action />

			<Toast.Close />

		</Toast.Root>

		<Toast.Viewport />

	</Toast.Provider>

);

```

## [API Reference](https://www.radix-ui.com/primitives/docs/components/toast#api-reference)
### [Provider](https://www.radix-ui.com/primitives/docs/components/toast#provider)
The provider that wraps your toasts and toast viewport. It usually wraps the application.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `duration` Prop description  | `number`  | `5000`  |
|  `label*` Prop description  | `string`  | `"Notification"`  |
|  `swipeDirection` Prop description  |  `enum` See full type  | `"right"`  |
|  `swipeThreshold` Prop description  | `number`  | `50`  |
|  `announcerContainer` Prop description  |  `Element` See full type  | `document.body`  |
### [Viewport](https://www.radix-ui.com/primitives/docs/components/toast#viewport)
The fixed area where toasts appear. Users can jump to the viewport by pressing a hotkey. It is up to you to ensure the discoverability of the hotkey for keyboard users.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
|  `hotkey` Prop description  | `string[]`  | `["F8"]`  |
|  `label` Prop description  | `string`  | `"Notifications ({hotkey})"`  |
### [Root](https://www.radix-ui.com/primitives/docs/components/toast#root)
The toast that automatically closes. It should not be held open to [acquire a user response](https://www.radix-ui.com/primitives/docs/components/toast#action).
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
|  `type` Prop description  |  `enum` See full type  | `"foreground"`  |
|  `duration` Prop description  | `number`  | No default value  |
|  `defaultOpen` Prop description  | `boolean`  | `true`  |
|  `open` Prop description  | `boolean`  | No default value  |
|  `onOpenChange` Prop description  |  `function` See full type  | No default value  |
|  `onEscapeKeyDown` Prop description  |  `function` See full type  | No default value  |
|  `onPause` Prop description  |  `function` See full type  | No default value  |
|  `onResume` Prop description  |  `function` See full type  | No default value  |
|  `onSwipeStart` Prop description  |  `function` See full type  | No default value  |
|  `onSwipeMove` Prop description  |  `function` See full type  | No default value  |
|  `onSwipeEnd` Prop description  |  `function` See full type  | No default value  |
|  `onSwipeCancel` Prop description  |  `function` See full type  | No default value  |
|  `forceMount` Prop description  | `boolean`  | No default value  |
| Data attribute  | Values  |
| --- | --- |
| `[data-state]`  | `"open"  | "closed" `  |
| `[data-swipe]`  | `"start"  | "move"  | "cancel"  | "end" `  |
| `[data-swipe-direction]`  | `"up"  | "down"  | "left"  | "right" `  |
| CSS Variable  | Description  |
| --- | --- |
| `--radix-toast-swipe-move-x`  | The offset position of the toast when horizontally swiping  |
| `--radix-toast-swipe-move-y`  | The offset position of the toast when vertically swiping  |
| `--radix-toast-swipe-end-x`  | The offset end position of the toast after horizontally swiping  |
| `--radix-toast-swipe-end-y`  | The offset end position of the toast after vertically swiping  |
### [Title](https://www.radix-ui.com/primitives/docs/components/toast#title)
An optional title for the toast.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
### [Description](https://www.radix-ui.com/primitives/docs/components/toast#description)
The toast message.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
### [Action](https://www.radix-ui.com/primitives/docs/components/toast#action)
An action that is safe to ignore to ensure users are not expected to complete tasks with unexpected side effects as a result of a
When obtaining a user response is necessary, portal an [`AlertDialog`](https://www.radix-ui.com/primitives/docs/components/alert-dialog) styled as a toast into the viewport instead.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
|  `altText*` Prop description  | `string`  | No default value  |
### [Close](https://www.radix-ui.com/primitives/docs/components/toast#close)
A button that allows users to dismiss the toast before its duration has elapsed.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
## [Examples](https://www.radix-ui.com/primitives/docs/components/toast#examples)
### [Custom hotkey](https://www.radix-ui.com/primitives/docs/components/toast#custom-hotkey)
Override the default hotkey using the `event.code` value for each key from

```

<Toast.Provider>

	{/* ... */}

	<Toast.Viewport hotkey={["altKey", "KeyT"]} />

</Toast.Provider>

```

### [Custom duration](https://www.radix-ui.com/primitives/docs/components/toast#custom-duration)
Customise the duration of a toast to override the provider value.

```

<Toast.Root duration={3000}>

	<Toast.Description>Saved!</Toast.Description>

</Toast.Root>

```

### [Duplicate toasts](https://www.radix-ui.com/primitives/docs/components/toast#duplicate-toasts)
When a toast must appear every time a user clicks a button, use state to render multiple instances of the same toast (see below). Alternatively, you can abstract the parts to create your own [imperative API](https://www.radix-ui.com/primitives/docs/components/toast#imperative-api).

```

export default () => {

	const [savedCount, setSavedCount] = React.useState(0);

	return (

		<div>

			<form onSubmit={() => setSavedCount((count) => count + 1)}>

				{/* ... */}

				<button>save</button>

			</form>

			{Array.from({ length: savedCount }).map((_, index) => (

				<Toast.Root key={index}>

					<Toast.Description>Saved!</Toast.Description>

				</Toast.Root>

			))}

		</div>

	);

};

```

### [Animating swipe gesture](https://www.radix-ui.com/primitives/docs/components/toast#animating-swipe-gesture)
Combine `--radix-toast-swipe-move-[x|y]` and `--radix-toast-swipe-end-[x|y]` CSS variables with `data-swipe="[start|move|cancel|end]"` attributes to animate a swipe to close gesture. Here's an example:

```

// index.jsx

import { Toast } from "radix-ui";

import "./styles.css";

export default () => (

	<Toast.Provider swipeDirection="right">

		<Toast.Root className="ToastRoot">...</Toast.Root>

		<Toast.Viewport />

	</Toast.Provider>

);

```

```

/* styles.css */

.ToastRoot[data-swipe="move"] {

	transform: translateX(var(--radix-toast-swipe-move-x));

}

.ToastRoot[data-swipe="cancel"] {

	transform: translateX(0);

	transition: transform 200ms ease-out;

}

.ToastRoot[data-swipe="end"] {

	animation: slideRight 100ms ease-out;

}

@keyframes slideRight {

	from {

		transform: translateX(var(--radix-toast-swipe-end-x));

	}

	to {

		transform: translateX(100%);

	}

}

```

## [Accessibility](https://www.radix-ui.com/primitives/docs/components/toast#accessibility)
Adheres to the
### [Sensitivity](https://www.radix-ui.com/primitives/docs/components/toast#sensitivity)
Control the sensitivity of the toast for screen readers using the `type` prop.
For toasts that are the result of a user action, choose `foreground`. Toasts generated from background tasks should use `background`.
#### Foreground
Foreground toasts are announced immediately. Assistive technologies may choose to clear previously queued messages when a foreground toast appears. Try to avoid stacking distinct foreground toasts at the same time.
#### Background
Background toasts are announced at the next graceful opportunity, for example, when the screen reader has finished reading its current sentence. They do not clear queued messages so overusing them can be perceived as a laggy user experience for screen reader users when used in response to a user interaction.

```

<Toast.Root type="foreground">

	<Toast.Description>File removed successfully.</Toast.Description>

	<Toast.Close>Dismiss</Toast.Close>

</Toast.Root>

<Toast.Root type="background">

	<Toast.Description>We've just released Radix 1.0.</Toast.Description>

	<Toast.Close>Dismiss</Toast.Close>

</Toast.Root>

```

### [Alternative action](https://www.radix-ui.com/primitives/docs/components/toast#alternative-action)
Use the `altText` prop on the `Action` to instruct an alternative way of actioning the toast to screen reader users.
You can direct the user to a permanent place in your application where they can action it or implement your own custom hotkey logic. If implementing the latter, use `foreground` type to announce immediately and increase the duration to give the user ample time.

```

<Toast.Root type="background">

	<Toast.Title>Upgrade Available!</Toast.Title>

	<Toast.Description>We've just released Radix 1.0.</Toast.Description>

	<Toast.Action altText="Goto account settings to upgrade">

		Upgrade

	</Toast.Action>

	<Toast.Close>Dismiss</Toast.Close>

</Toast.Root>

<Toast.Root type="foreground" duration={10000}>

	<Toast.Description>File removed successfully.</Toast.Description>

	<Toast.Action altText="Undo (Alt+U)">

		Undo <kbd>Alt</kbd>+<kbd>U</kbd>

	</Toast.Action>

	<Toast.Close>Dismiss</Toast.Close>

</Toast.Root>

```

### [Close icon button](https://www.radix-ui.com/primitives/docs/components/toast#close-icon-button)
When providing an icon (or font icon), remember to label it correctly for screen reader users.

```

<Toast.Root type="foreground">

	<Toast.Description>Saved!</Toast.Description>

	<Toast.Close aria-label="Close">

		<span aria-hidden>×</span>

	</Toast.Close>

</Toast.Root>

```

### [Keyboard Interactions](https://www.radix-ui.com/primitives/docs/components/toast#keyboard-interactions)
| Key  | Description  |
| --- | --- |
| `F8`  | Focuses toasts viewport.  |
| `Tab`  | Moves focus to the next focusable element.  |
| `Shift + Tab`  | Moves focus to the previous focusable element.  |
| `Space`  | When focus is on a `Toast.Action` or `Toast.Close`, closes the toast.  |
| `Enter`  | When focus is on a `Toast.Action` or `Toast.Close`, closes the toast.  |
| `Esc`  | When focus is on a `Toast`, closes the toast.  |
## [Custom APIs](https://www.radix-ui.com/primitives/docs/components/toast#custom-apis)
### [Abstract parts](https://www.radix-ui.com/primitives/docs/components/toast#abstract-parts)
Create your own API by abstracting the primitive parts into your own component.
#### Usage

```

import { Toast } from "./your-toast";

export default () => (

	<Toast title="Upgrade available" content="We've just released Radix 3.0!">

		<button onClick={handleUpgrade}>Upgrade</button>

	</Toast>

);

```

#### Implementation

```

// your-toast.jsx

import { Toast as ToastPrimitive } from "radix-ui";

export const Toast = ({ title, content, children, ...props }) => {

	return (

		<ToastPrimitive.Root {...props}>

			{title && <ToastPrimitive.Title>{title}</ToastPrimitive.Title>}

			<ToastPrimitive.Description>{content}</ToastPrimitive.Description>

			{children && (

				<ToastPrimitive.Action asChild>{children}</ToastPrimitive.Action>

			)}

			<ToastPrimitive.Close aria-label="Close">

				<span aria-hidden>×</span>

			</ToastPrimitive.Close>

		</ToastPrimitive.Root>

	);

};

```

### [Imperative API](https://www.radix-ui.com/primitives/docs/components/toast#imperative-api)
Create your own imperative API to allow [toast duplication](https://www.radix-ui.com/primitives/docs/components/toast#duplicate-toasts) if preferred.
#### Usage

```

import { Toast } from "./your-toast";

export default () => {

	const savedRef = React.useRef();

	return (

		<div>

			<form onSubmit={() => savedRef.current.publish()}>

				{/* ... */}

				<button>Save</button>

			</form>

			<Toast ref={savedRef}>Saved successfully!</Toast>

		</div>

	);

};

```

#### Implementation

```

// your-toast.jsx

import * as React from "react";

import { Toast as ToastPrimitive } from "radix-ui";

export const Toast = React.forwardRef((props, forwardedRef) => {

	const { children, ...toastProps } = props;

	const [count, setCount] = React.useState(0);

	React.useImperativeHandle(forwardedRef, () => ({

		publish: () => setCount((count) => count + 1),

	}));

	return (

		<>

			{Array.from({ length: count }).map((_, index) => (

				<ToastPrimitive.Root key={index} {...toastProps}>

					<ToastPrimitive.Description>{children}</ToastPrimitive.Description>

					<ToastPrimitive.Close>Dismiss</ToastPrimitive.Close>

				</ToastPrimitive.Root>

			))}

		</>

	);

});

```

#### Quick nav
  * [Anatomy](https://www.radix-ui.com/primitives/docs/components/toast#anatomy)
  * [API Reference](https://www.radix-ui.com/primitives/docs/components/toast#api-reference)
  * [Provider](https://www.radix-ui.com/primitives/docs/components/toast#provider)
  * [Viewport](https://www.radix-ui.com/primitives/docs/components/toast#viewport)
  * [Root](https://www.radix-ui.com/primitives/docs/components/toast#root)
  * [Title](https://www.radix-ui.com/primitives/docs/components/toast#title)
  * [Description](https://www.radix-ui.com/primitives/docs/components/toast#description)
  * [Action](https://www.radix-ui.com/primitives/docs/components/toast#action)
  * [Close](https://www.radix-ui.com/primitives/docs/components/toast#close)
  * [Examples](https://www.radix-ui.com/primitives/docs/components/toast#examples)
  * [Custom hotkey](https://www.radix-ui.com/primitives/docs/components/toast#custom-hotkey)
  * [Custom duration](https://www.radix-ui.com/primitives/docs/components/toast#custom-duration)
  * [Duplicate toasts](https://www.radix-ui.com/primitives/docs/components/toast#duplicate-toasts)
  * [Animating swipe gesture](https://www.radix-ui.com/primitives/docs/components/toast#animating-swipe-gesture)
  * [Accessibility](https://www.radix-ui.com/primitives/docs/components/toast#accessibility)
  * [Sensitivity](https://www.radix-ui.com/primitives/docs/components/toast#sensitivity)
  * [Alternative action](https://www.radix-ui.com/primitives/docs/components/toast#alternative-action)
  * [Close icon button](https://www.radix-ui.com/primitives/docs/components/toast#close-icon-button)
  * [Keyboard Interactions](https://www.radix-ui.com/primitives/docs/components/toast#keyboard-interactions)
  * [Custom APIs](https://www.radix-ui.com/primitives/docs/components/toast#custom-apis)
  * [Abstract parts](https://www.radix-ui.com/primitives/docs/components/toast#abstract-parts)
  * [Imperative API](https://www.radix-ui.com/primitives/docs/components/toast#imperative-api)

Previous[Tabs](https://www.radix-ui.com/primitives/docs/components/tabs)
Next[Toggle](https://www.radix-ui.com/primitives/docs/components/toggle)
