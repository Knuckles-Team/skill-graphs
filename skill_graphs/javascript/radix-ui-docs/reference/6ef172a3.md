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
Overview
# Releases
Radix Primitives releases and their changelogs.
## [June 6, 2026](https://www.radix-ui.com/primitives/docs/overview/releases#june-6-2026)
This release introduces new composition APIs, a controlled Context Menu, and a number of bug fixes and performance improvements across primitives.
### [Context Menu](https://www.radix-ui.com/primitives/docs/overview/releases#context-menu)
Added support for a controlled `open` prop on [`ContextMenu.Root`](https://www.radix-ui.com/primitives/docs/components/context-menu#root). This is intended for reading the open state and closing the menu programmatically. We discourage opening the menu programmatically, since opening it depends on user interaction to position the menu correctly.

```

function ControlledContextMenu() {

	const [open, setOpen] = React.useState(false);

	return (

		<ContextMenu.Root open={open} onOpenChange={setOpen}>

			<ContextMenu.Trigger>Open</ContextMenu.Trigger>

			<ContextMenu.Content>

				<button type="button" onClick={() => setOpen(false)}>

					Close me

				</button>

				<ContextMenu.Item>Item 1</ContextMenu.Item>

				<ContextMenu.Item>Item 2</ContextMenu.Item>

			</ContextMenu.Content>

		</ContextMenu.Root>

	);

}

```

We also fixed a bug where submenus remained expanded after re-opening on long-press touch events.
### [New unstable composition parts](https://www.radix-ui.com/primitives/docs/overview/releases#new-unstable-composition-parts)
Several form-control primitives now expose their previously internal composition, so you can directly access and recompose the visually hidden inputs they render for form submission. Each component continues to render these parts by default, and the new parts are exported with the `unstable_` prefix.
  * **Radio Group** — `unstable_ItemProvider`, `unstable_ItemTrigger`, and `unstable_ItemBubbleInput`
  * **Select** — `unstable_Provider` and `unstable_BubbleInput`
  * **Slider** — `unstable_ThumbProvider`, `unstable_ThumbTrigger`, and `unstable_BubbleInput`
  * **Switch** — `unstable_Provider`, `unstable_Trigger`, and `unstable_BubbleInput`

```

import { Switch } from "radix-ui";

function ExampleSwitch() {

	return (

		<Switch.unstable_Provider>

			<Switch.unstable_Trigger>

				<Switch.Thumb />

			</Switch.unstable_Trigger>

			{/* the hidden input is now exposed and can be omitted if not needed */}

			<Switch.unstable_BubbleInput />

		</Switch.unstable_Provider>

	);

}

```

### [Select](https://www.radix-ui.com/primitives/docs/overview/releases#select)
  * Added support for presence-based exit animations.
  * Fixed the bubble hidden input so that it submits an empty string when no value is selected.
  * Fixed Select closing unexpectedly after touch-scrolling its content when rendered inside an open shadow DOM.
  * Fixed `Select.Value` logging invalid prop errors when used with both `asChild` and a placeholder.

### [Slider](https://www.radix-ui.com/primitives/docs/overview/releases#slider)
  * Added `focusVisible` support for non-keyboard interactions with slider thumbs, for progressively enabling styles using `:focus-visible` alongside programmatic focus management.
  * Fixed a bug where very small `step` values made the thumbs unresponsive.
  * Fixed focus bugs for sliders in a scrollable context.

### [Slot](https://www.radix-ui.com/primitives/docs/overview/releases#slot)
  * Added support for nested `Slottable` items via a render prop. This allows a slotted element to be wrapped while still merging Slot props and refs onto it.
  * Fixed an infinite re-render loop in React 19 caused by `Slot` creating a new ref callback on every render.
  * Improved error messages for invalid slot children.

### [Dialog](https://www.radix-ui.com/primitives/docs/overview/releases#dialog)
  * Fixed a bug where iOS text selection and editing on HTML inputs within dialogs were broken.
  * Fixed a bug causing disabled pointer events in closed dialogs.

### [One-Time Password Field](https://www.radix-ui.com/primitives/docs/overview/releases#one-time-password-field)
  * Fixed pasting in environments that do not support the legacy `"Text"` clipboard format by reading the pasted value as `"text/plain"`.
  * Fixed issues with focus management in React 19.2+.
  * Ensured that pasted values exceeding the field length are truncated.

### [Tooltip](https://www.radix-ui.com/primitives/docs/overview/releases#tooltip)
  * Fixed a runtime error when an event target is a non-Node entity.
  * Fixed a bug so that `skipDelayDuration={0}` works as expected. Previously, the open delay could still be skipped when moving between triggers.

### [Other updates](https://www.radix-ui.com/primitives/docs/overview/releases#other-updates)
  * Added an `align` prop to the `SubContent` part of [Dropdown Menu](https://www.radix-ui.com/primitives/docs/components/dropdown-menu#subcontent), [Context Menu](https://www.radix-ui.com/primitives/docs/components/context-menu#subcontent), and [Menubar](https://www.radix-ui.com/primitives/docs/components/menubar#subcontent) to control the direction the submenu appears from its anchor item.
  * Added an `announcerContainer` prop to [`Toast.Provider`](https://www.radix-ui.com/primitives/docs/components/toast#provider) so you can specify a container for toast announcements.
  * Exposed `data-side` and `data-align` attributes on the Popper anchor element.
  * Added an `align` prop to `Menu.SubContent`.
  * Fixed a missing `data-state` attribute for Scroll Area scrollbars.
  * Fixed a "Maximum update depth exceeded" bug for pages with a large number of popper instances, as well as a similar bug in `Presence` under React 19.
  * Now uses React's built-in `useSyncExternalStore` (React 18+) instead of the CJS-only shim, which previously crashed ESM-only browser bundles when importing some components.
  * Fixed triggers referencing non-existent elements via `aria-controls` when their content is removed from the DOM – .
  * Improved focus-guard performance when opening overlays by caching the shared guard pair and only writing to the DOM when their edge position changes.
  * Added missing `use client` directives to modules causing errors in RSC.

## [August 13, 2025](https://www.radix-ui.com/primitives/docs/overview/releases#august-13-2025)
### [One-Time Password Field](https://www.radix-ui.com/primitives/docs/overview/releases#one-time-password-field-1)
  * Fixed a bug so that all input elements are disabled when the `Root` component is disabled.
  * Fixed a bug with iOS Chrome autocomplete – .

### [Other updates](https://www.radix-ui.com/primitives/docs/overview/releases#other-updates-1)
  * Fixed a Popper bug causing infinite render loops.
  * Ensured the `animationend` event is handled correctly when the keyframe has escapable characters – .
  * Fixed how Slot components interact with lazy React components in React 19. In the case of a lazy component instance, the resulting promise is now consumed to render the desired component.
  * Fixed several Toast accessibility issues, including removing `aria-hidden` from focusable elements, removing `role=status` from the list item element, and removing a redundant default `aria-atomic`.
  * Added `displayName` to internal context objects for improved debugging.

## [May 20, 2025](https://www.radix-ui.com/primitives/docs/overview/releases#may-20-2025)
  * Dependency maintenance release with no user-facing API changes.

## [May 6, 2025](https://www.radix-ui.com/primitives/docs/overview/releases#may-6-2025)
  * Dependency maintenance release with no user-facing API changes.

## [May 5, 2025](https://www.radix-ui.com/primitives/docs/overview/releases#may-5-2025)
This release introduces a brand new primitive in preview: [`PasswordToggleField`](https://www.radix-ui.com/primitives/docs/components/password-toggle-field).
This new primitive provides components for rendering a password input alongside a button to toggle its visibility. Aside from its primary functionality, it also includes:
  * Returning focus to the input when toggling with a pointer
  * Maintaining focus when toggling with keyboard or virtual navigation
  * Resetting visibility to hidden after form submission to prevent accidental storage
  * Implicit accessible labeling for icon-based toggle buttons

This API is currently unstable, and we hope you'll help us test it out! Import the primitive using the `unstable_` prefix.

```

import { unstable_PasswordToggleField as PasswordToggleField } from "radix-ui";

export function PasswordField() {

	return (

		<PasswordToggleField.Root>

			<PasswordToggleField.Input />

			<PasswordToggleField.Toggle>

				<PasswordToggleField.Icon
					visible={<EyeOpenIcon />}
					hidden={<EyeClosedIcon />}
				/>

			</PasswordToggleField.Toggle>

		</PasswordToggleField.Root>

	);

}

```

### [Other updates](https://www.radix-ui.com/primitives/docs/overview/releases#other-updates-2)
  * Add unstable `Provider`, `Trigger` and `BubbleInput` parts to Checkbox (
  * Update default input type to `text` and pass to the underlying input element (

## [April 22, 2025](https://www.radix-ui.com/primitives/docs/overview/releases#april-22-2025)
  * Update the dependency for `use-sync-external-store` to ensure entrypoint is valid –

## [April 17, 2025](https://www.radix-ui.com/primitives/docs/overview/releases#april-17-2025)
This release introduces a brand new primitive in preview: [`OneTimePasswordField`](https://www.radix-ui.com/primitives/docs/components/one-time-password-field).
This new group of components are designed to implement a common design pattern for one-time password fields displayed as separate input fields for each character. This UI is deceptively complex to implement in such a way that interactions follow user expectations. The new primitive handles all of this complexity for you, including:
  * Keyboard navigation mimicking the behavior of a single input field
  * Overriding values on paste
  * Password manager autofill support
  * Input validation for numeric and alphanumeric values
  * Auto-submit on completion
  * Focus management
  * Hidden input to provide a single value to form data

As this is a preview release, **the API is currently unstable**. We hope you'll help us test it out and let us know how it goes.
Import the primitive using the `unstable_` prefix.

```

import { unstable_OneTimePasswordField as OneTimePasswordField } from "radix-ui";

export function Verify() {

	return (

		<OneTimePasswordField.Root>

			<OneTimePasswordField.Input />

			<OneTimePasswordField.Input />

			<OneTimePasswordField.Input />

			<OneTimePasswordField.Input />

			<OneTimePasswordField.Input />

			<OneTimePasswordField.Input />

			<OneTimePasswordField.HiddenInput />

		</OneTimePasswordField.Root>

	);

}

```

### [Other updates](https://www.radix-ui.com/primitives/docs/overview/releases#other-updates-3)
  * All form controls with internal bubble inputs now use the Radix `Primitive` component by default. This will allow us to expose these components in a future release so users can better control this behavior in the future.
  * Minor improvements to `useControllableState` to enhance performance, reduce surface area for bugs, and log warnings when misused

## [April 8, 2025](https://www.radix-ui.com/primitives/docs/overview/releases#april-8-2025)
  * Improved rendering performance for the Tooltip provider –
  * Ensure Tooltip is closed when `pointerdown` is fired on the trigger –
  * Add support for `crossOrigin` in Avatar images –
  * Fix Avatar flashing when an image is already cached –
  * Improve `displayName` for better debugging of slottable components –

## [February 5, 2025](https://www.radix-ui.com/primitives/docs/overview/releases#february-5-2025)
  * Updated dependencies to remove peer dependency warnings for `react` and `react-dom` –
  * Skip forwarding refs to `SlotClone` when the child is a `Fragment` –

## [January 22, 2025](https://www.radix-ui.com/primitives/docs/overview/releases#january-22-2025)
  * Added a `radix-ui` package that exposes the latest version of all Radix Primitives from a single place. This tree-shakable entrypoint makes it easier to bring in whatever components you need and keep them up-to-date without worrying about conflicting or duplicate dependencies.
  * Updated `aria-hidden` and `react-remove-scroll` dependencies for the following components:
    * Alert Dialog
    * Context Menu
    * Dialog
    * Dropdown Menu
    * Hover Card
    * Menubar
    * Navigation Menu
    * Popover
    * Select
    * Toast
    * Tooltip

## [October 1, 2024](https://www.radix-ui.com/primitives/docs/overview/releases#october-1-2024)
# Alert Dialog
1.1.2
  * Fix `allowPinchZoom` bug for trackpad users –

# Avatar
1.1.1
  * Check for `referrerPolicy` when checking the image loading status –

# Checkbox
1.1.2
  * Fix a bug where `defaultChecked` unexpectedly changed for uncontrolled checkboxes –
  * Forward the `form` prop to the bubble input element to fix non-parent form submissions –

# Dialog
1.1.2
  * Fix `allowPinchZoom` bug for trackpad users –

# Radio Group
1.2.1
  * Forward the `form` prop to the bubble input element to fix non-parent form submissions –

# Scroll Area
1.2.0
  * Fix `asChild` prop not working as expected on the `Viewport` –
  * Update internal styles to fix other issues with `Viewport` –

# Select
2.1.2
  * Fix error thrown when items are initially undefined –
  * Fix several bugs for touch devices –
  * Forward the `form` prop to the bubble input element to fix non-parent form submissions –
  * Fix position bug where popover may start off-screen for long items –

# Slider
1.2.1
  * Forward the root `form` prop to each thumb's bubble input element to fix non-parent form submissions –

# Switch
1.1.1
  * Forward the `form` prop to the bubble input element to fix non-parent form submissions –

# Toast
1.2.2
  * Fix incorrect focus when `hotkey` is an empty array –

## [June 28, 2024](https://www.radix-ui.com/primitives/docs/overview/releases#june-28-2024)
# Checkbox
1.1.1
  * Export `CheckedState` type

# Tooltip
1.1.2
  * Export `TooltipProviderProps` type

## [June 21, 2024](https://www.radix-ui.com/primitives/docs/overview/releases#june-21-2024)
# Portal
1.1.1
  * Add a missing internal utility to `package.json`. The corresponding packages that provide a Portal part also received a patch update. –

## [June 19, 2024](https://www.radix-ui.com/primitives/docs/overview/releases#june-19-2024)
# All primitives

Released minor versions for all primitives with the following changes:
  * Full React 19 compatability –
  * Full RSC compatibility –
  * Internal build tooling changes – –
  * Update and pin `react-remove-scroll` dependency version to avoid double scrollbar bugs in edge cases –
  * Don’t scroll menu items in response to hover –
  * Make sure that components that close on Escape key press capture the corresponding keyboard event. This way you can call `stopPropagation` in `onEscapeKeyDown` if you need more control rendering Radix components within another component that closes on Escape key press.
  * Make sure that components with roving focus do not interfere with browser or system hotkeys, such as back navigation –
  * Make sure that components that support `hideWhenDetached` prop do not allow interactions with hidden content – –

# Dialog
1.1.0
  * Log an error when an accessible title via the `Dialog.Title` part is missing –
  * Log a warning when an accessible description via the `Dialog.Description` part is missing –

# Label
2.1.0
  * Make sure that the component doesn’t interfere when clicking on the spinner of a number input

# Navigation Menu
1.2.0
  * Remove unsupported `disableOutsidePointerEvents` prop

# Portal
1.1.0
  * Fix hydration error in SSR on the initial render –

# Progress
1.2.0
  * Explicitly allow `value={undefined}` to represent an indeterminate state, matching the current practical behaviour –

# Select
2.1.0
  * Add `nonce` prop to be able to pass CSP nonce to the inline styles –

# Scroll Area
1.1.0
  * Add `nonce` prop to be able to pass CSP nonce to the inline styles –

## [September 25, 2023](https://www.radix-ui.com/primitives/docs/overview/releases#september-25-2023)
# Alert Dialog
1.0.5
  * Fix pointer-events issue when clicking outside –
  * Fix `Portal` part types lying about accepting DOM props –

# Avatar
1.0.4
  * Prevent image flash –

# Context Menu
2.1.5
  * Fix pointer-events issue when clicking outside –
  * Fix `Portal` part types lying about accepting DOM props –

# Dialog
1.0.5
  * Fix pointer-events issue when clicking outside –
  * Fix `Portal` part types lying about accepting DOM props –

# Dropdown Menu
2.0.6
  * Fix pointer-events issue when clicking outside –
  * Fix `Portal` part types lying about accepting DOM props –

# Hover Card
1.0.7
  * Fix pointer-events issue when clicking outside –
  * Fix `Portal` part types lying about accepting DOM props –

# Menubar
1.0.4
  * Fix pointer-events issue when clicking outside –
  * Fix `Portal` part types lying about accepting DOM props –

# Navigation Menu
1.1.4
  * Fix pointer-events issue when clicking outside –
  * Fix `Portal` part types lying about accepting DOM props –

# Popover
1.0.7
  * Fix pointer-events issue when clicking outside –
  * Fix `Portal` part types lying about accepting DOM props –
  * Fix `Popover` nested inside `Dialog` not opening –

# Scroll Area
1.0.5
  * Add `scroll-behavior: smooth` compatibility –

# Select
2.0.0Major
  * **[Breaking]** Add ability to reset to placeholder using `""` `value`. Note that this is only a breaking change if you were using an option with a `value` of `""`. –
  * Fix pointer-events issue when clicking outside –
  * Fix `Portal` part types lying about accepting DOM props –

# Toast
1.1.5
  * Fix pointer-events issue when clicking outside –

# Tooltip
1.0.7
  * Fix pointer-events issue when clicking outside –
  * Fix `Portal` part types lying about accepting DOM props –
  * Fix issue with boundary padding calculations –
  * Add option to always re-position `Content` on the fly –

## [May 26, 2023](https://www.radix-ui.com/primitives/docs/overview/releases#may-26-2023)
This release ensures all of our primitives are ESM compatible. We have also updated to the latest version of
# All primitives
  * Improve ESM compatibility –
  * Fix possible upstream compiler errors (`@types/react` phantom dependency) –

# Context Menu
2.1.4
  * Position content correctly when matching trigger size –

# Dialog
1.0.4
  * Prevent non-modal dialog from re-opening when closing using trigger in Safari –
  * Ensure focus trapping is maintained when the focused item is deleted –

# Dropdown Menu
2.0.5
  * Position content correctly when matching trigger size –

# Hover Card
1.0.6
  * Position content correctly when matching trigger size –

# Menubar
1.0.3
  * Position content correctly when matching trigger size –

# Navigation Menu
1.1.3
  * Do not close when clicking items and meta key is down –

# Popover
1.0.6
  * Position content correctly when matching trigger size –
  * Prevent non-modal popover from re-opening when closing using trigger in Safari –
  * Ensure `--radix-popper-available-width` is calculated correctly when using `collisionBoundary` –

# Select
1.2.2
  * Position content correctly when matching trigger size –
  * Improve scroll buttons touch screen support –

# Slider
1.1.2
  * Clamp thumb position within range –

# Slot
1.0.2
  * Ensure `Slot` can be used in a React Server Component –

# Tooltip
1.0.6
  * Position content correctly when matching trigger size –
  * Improve large content hoverability –

## [March 8, 2023](https://www.radix-ui.com/primitives/docs/overview/releases#march-8-2023)
This release introduces a brand new primitive in preview: [`Form`](https://www.radix-ui.com/primitives/docs/components/form).
# Form
0.0.2Preview
  * New primitive –

## [February 24, 2023](https://www.radix-ui.com/primitives/docs/overview/releases#february-24-2023)
# Checkbox
1.0.2
  * Reset checkbox state when form is reset –

# ContextMenu
2.1.2
  * Expose new CSS custom properties to enable size constraints –
  * Don't exit fullscreen mode when pressing escape to dismiss from submenu –
  * Relax `onCheckedChange` type on `ContextMenu.CheckboxItem` –

# DropdownMenu
2.0.3
  * Expose new CSS custom properties to enable size constraints –
  * Don't exit fullscreen mode when pressing escape to dismiss from submenu –
  * Relax `onCheckedChange` type on `DropdownMenu.CheckboxItem` –

# HoverCard
1.0.4
  * Expose new CSS custom properties to enable size constraints –

# Menubar
1.0.1
  * Expose new CSS custom properties to enable size constraints –
  * Don't exit fullscreen mode when pressing escape to dismiss from submenu –
  * Relax `onCheckedChange` type on `Menubar.CheckboxItem` –

# Popover
1.0.4
  * Expose new CSS custom properties to enable size constraints –

# Tooltip
1.0.4
  * Expose new CSS custom properties to enable size constraints –

## [January 17, 2023](https://www.radix-ui.com/primitives/docs/overview/releases#january-17-2023)
This release introduces a brand new primitive: [`Menubar`](https://www.radix-ui.com/primitives/docs/components/menubar). It also adds support for a highly requested feature for [`Select`](https://www.radix-ui.com/primitives/docs/components/select): the ability to position the content in a similar way to `Popover` or `DropdownMenu`.
# Accordion
1.1.0
  * Add horizontal orientation support with new `orientation` prop, as well as RTL support with `dir` –

# Context Menu
2.1.1
  * Fix consistency issue with RTL positioning –
