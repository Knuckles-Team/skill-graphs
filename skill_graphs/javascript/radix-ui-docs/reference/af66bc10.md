
# Dropdown Menu
2.0.2
  * Fix consistency issue with RTL positioning –

# Hover Card
1.0.3
  * Fix consistency issue with RTL positioning –

# Menubar
1.0.0Major
  * New primitive –

# Popover
1.0.3
  * Fix consistency issue with RTL positioning –

# Select
1.2.0
  * Add `position` prop to `Select.Content` to enable popper positioning –

# Tooltip
1.0.3
  * Fix consistency issue with RTL positioning –

## [December 14, 2022](https://www.radix-ui.com/primitives/docs/overview/releases#december-14-2022)
# Context Menu
2.1.0
  * Add `disabled` prop to `ContextMenu.Trigger` –

## [November 15, 2022](https://www.radix-ui.com/primitives/docs/overview/releases#november-15-2022)
# Select
1.1.2
  * Fix invalid `pointerId` in Cypress when running Firefox –

## [October 17, 2022](https://www.radix-ui.com/primitives/docs/overview/releases#october-17-2022)
# Accordion
1.0.1
  * Fix initial animation playback in Firefox and Safari –

# Alert Dialog
1.0.2
  * Fix issue with textarea elements not being scrollable in Firefox –

# Collapsible
1.0.1
  * Fix initial animation playback in Firefox and Safari –

# Context Menu
2.0.1Major
  * **[Breaking]** Add support for indeterminate state on `ContextMenu.CheckboxItem`. Note that this is only a breaking change if you are currently using the `CheckboxItem` part and your codebase is written in TypeScript. –

# Dialog
1.0.2
  * Fix issue with textarea elements not being scrollable in Firefox –

# Dropdown Menu
2.0.1Major
  * **[Breaking]** Add support for indeterminate state on `DropdownMenu.CheckboxItem`. Note that this is only a breaking change if you are currently using the `CheckboxItem` part and your codebase is written in TypeScript. –
  * Correctly pair `DropdownMenu.Trigger` open state with `aria-expanded` when closed –
  * Fix issue with eager selection of items when using `asChild` –
  * Fix issue with dismissing when the component is used in a separate popup window –

# Hover Card
1.0.2
  * Improve text selection experience –

# Label
2.0.0Major
  * **[Breaking]** Remove `useLabelContext` and support for fully custom controls. For native labelling to work, ensure your custom controls are based on native elements such as `button` or `input`. –
  * Improve native behavior by using the native `label` element –

# Navigation Menu
1.1.1
  * Prevent menu from re-opening with the pointer after being dismissed with escape –
  * Add `delayDuration` and `skipDelayDuration` props to `NavigationMenu.Root`. Note that by default, triggers now have a brief delay before opening in order to improve UX, this can be modified using the props provided. –

# Radio Group
1.1.0
  * Add `disabled` prop to `RadioGroup.Root` –
  * Fix issue where `RadioGroup.Root` was focusable when all items were disabled –

# Select
1.1.1
  * Add `disabled` prop to `Select.Root` –
  * Add `required` prop to `Select.Root` –

# Slider
1.1.0
  * Add ability to visually invert the slider using the new `inverted` prop on `Slider.Root` –
  * Add `onValueCommit` prop to `Slider.Root` to better handle discrete value changes –

# Slot
1.0.1
  * Stop eagerly creating callback props –

# Toast
1.1.1
  * Fix regression with screen readers announcing as "group" rather than "status" –
  * Fix regression with `ref` assignments on child elements returning `null` –
  * Add `onPause` and `onResume` props to `Toast.Root` –
  * Fix timer reset issue which would cause toasts to dismiss early in some cases –

# Toolbar
1.0.1
  * Prevent `Toolbar.Item` click handlers firing twice –

# Tooltip
1.0.2
  * Ensure tooltip doesn't open if interacting with the trigger before the open timer expires –

## [July 21, 2022](https://www.radix-ui.com/primitives/docs/overview/releases#july-21-2022)
With this release, we start following semantic versioning strictly. All primitives are now versioned 1.0.0.
We also move the [`Select`](https://www.radix-ui.com/primitives/docs/components/select), [`Toast`](https://www.radix-ui.com/primitives/docs/components/toast) and [`NavigationMenu`](https://www.radix-ui.com/primitives/docs/components/navigation-menu) from preview to stable.
# All primitives
  * Improve support for React 18 –
  * **[Breaking]** Improve RTL performance. You need to use [`DirectionProvider`](https://www.radix-ui.com/primitives/docs/utilities/direction-provider) if you were relying on `dir` attribute inheritance from document (or any element). –

# Alert Dialog
1.0.0Major
  * **[Breaking]** Remove `allowPinchZoom` prop, now defaults to `true` –
  * Improve compatibility with JS animation libraries with `forceMount` on `AlertDialog.Portal` –
  * Fix regressions with page interactivity while/after closing dialog –

# Context Menu
1.0.0Major
  * **[Breaking]** Improve indirect nesting of context menus. Submenus must now be created using explicit parts. –
  * **[Breaking]** Remove `allowPinchZoom` prop, now defaults to `true` –
  * **[Breaking]** Add new `Portal` part. To avoid regressions, use this part if you want portalling behavior. Note that `z-index` isn't managed anymore so you have full control of layering. –
  * **[Breaking]** Remove `offset` on `Arrow` part –
  * **[Breaking]** Rename `collisionTolerance` to `collisionPadding` on `Content` part and accepts a number or a padding object –
  * Fix issue with native context menu appearing in React 18 –
  * Add `data-highlighted` attribute to support styling –
  * Add `data-state` attribute to `Trigger` part –
  * Add `collisionBoundary`, `arrowPadding`, `sticky`, `hideWhenDetached` props on `Content` part –

# Dialog
1.0.0Major
  * **[Breaking]** Remove `allowPinchZoom` prop, now defaults to `true` –
  * Improve compatibility with JS animation libraries with `forceMount` on `Dialog.Portal` –
  * Fix regressions with page interactivity while/after closing dialog –

# Dropdown Menu
1.0.0Major
  * **[Breaking]** Improve indirect nesting of dropdown menus. Submenus must now be created using explicit parts. –
  * **[Breaking]** Remove `allowPinchZoom` prop, now defaults to `true` –
  * **[Breaking]** Add new `Portal` part. To avoid regressions, use this part if you want portalling behavior. Note that `z-index` isn't managed anymore so you have full control of layering. –
  * **[Breaking]** Remove `offset` on `Arrow` part –
  * **[Breaking]** Rename `collisionTolerance` to `collisionPadding` on `Content` part and accepts a number or a padding object –
  * Add `data-highlighted` attribute to support styling –
  * Prevent escape key from exiting fullscreen mode in Firefox & Safari –
  * Add `collisionBoundary`, `arrowPadding`, `sticky`, `hideWhenDetached` props on `Content` part –

# Hover Card
1.0.0Major
  * **[Breaking]** Add new `Portal` part. To avoid regressions, use this part if you want portalling behavior. Note that `z-index` isn't managed anymore so you have full control of layering. –
  * **[Breaking]** Remove `offset` on `Arrow` part –
  * **[Breaking]** Rename `collisionTolerance` to `collisionPadding` on `Content` part and accepts a number or a padding object –
  * Add `collisionBoundary`, `arrowPadding`, `sticky`, `hideWhenDetached` props on `Content` part –

# Navigation Menu
1.0.0Major
  * Ensure menu closes after clicking `NavigationMenu.Link` –
  * Add `onSelect` prop to `NavigationMenu.Link` –

# Popover
1.0.0Major
  * **[Breaking]** Remove `allowPinchZoom` prop, now defaults to `true` –
  * **[Breaking]** Add new `Portal` part. To avoid regressions, use this part if you want portalling behavior. Note that `z-index` isn't managed anymore so you have full control of layering. –
  * **[Breaking]** Remove `offset` on `Arrow` part –
  * **[Breaking]** Rename `collisionTolerance` to `collisionPadding` on `Content` part and accepts a number or a padding object –
  * Add `collisionBoundary`, `arrowPadding`, `sticky`, `hideWhenDetached` props on `Content` part –

# Portal
1.0.0Major
  * **[Breaking]** Note that `z-index` isn't managed anymore so you have full control of layering. The prop to provide a custom container evolves from `containerRef` (ref) to `container` (element). The `data-radix-portal` was removed because you can use `asChild` to control the element. –

# RadioGroup
1.0.0Major
  * Add `aria-required` to root –

# Scroll Area
1.0.0Major
  * `ScrollArea.Thumb` is now animatable –

# Select
1.0.0Major
  * **[Breaking]** Renamed `data-state` values from `active|inactive` to `checked|unchecked` –
  * **[Breaking]** Add new `Portal` part. To avoid regressions, use this part if you want portalling behavior. Note that `z-index` isn't managed anymore so you have full control of layering. –
  * Fix position breaking when using `asChild` on `Select.Content` –
  * Improve trigger/content alignment when `Select.Content` has padding –
  * Fix trigger/content alignment when there are less than 5 items –
  * Support trigger/content alignment when no value is provided –
  * Add `data-highlighted` attribute to support styling –
  * Add support for placeholder via `placeholder` prop on `Select.Value` –
  * Resolve value mismatch with underlying native select –

# Slot
1.0.0Major
  * Fix issue with children ordering when using `Slottable` –

# Tabs
1.0.0Major
  * Add support for lifecycle animation to `Tabs.Content` –

# Toast
1.0.0Major
  * **[Breaking]** The default toast order has changed, they now render top to bottom from oldest to newest –
  * Improve Typescript types when using `asChild` –
  * Fix issue with toast reordering when updating React's `key` prop –
  * Improve compatability with animation libraries –

# Tooltip
1.0.0Major
  * **[Breaking]** Add new `Portal` part. To avoid regressions, use this part if you want portalling behavior. Note that `z-index` isn't managed anymore so you have full control of layering. –
  * **[Breaking]** By default `Tooltip.Content` will remain open when hovering (WCAG 2.1 Content on Hover compliance). `disableHoverableContent` can be supplied to `Tooltip.Provider` to restore previous behavior –
  * **[Breaking]** `side` on `Tooltip.Content` now defaults to `top` –
  * **[Breaking]** `Tooltip.Provider` is now required, you must wrap your app to avoid regressions. –
  * **[Breaking]** Remove `offset` on `Arrow` part –
  * **[Breaking]** Rename `collisionTolerance` to `collisionPadding` on `Content` part and accepts a number or a padding object –
  * Improve layering of tooltip with other primitives –
  * Fix tooltip closing when transforming/animation trigger –
  * Add `collisionBoundary`, `arrowPadding`, `sticky`, `hideWhenDetached` props on `Content` part –

## [February 28, 2022](https://www.radix-ui.com/primitives/docs/overview/releases#february-28-2022)
This release introduces 3 brand new primitives in preview: [`Select`](https://www.radix-ui.com/primitives/docs/components/select), [`Toast`](https://www.radix-ui.com/primitives/docs/components/toast) and [`NavigationMenu`](https://www.radix-ui.com/primitives/docs/components/navigation-menu), whilst also shipping a ton of fixes and improvements.
# Accordion
0.1.6
  * Prevent form submission when pressing `Accordion.Trigger` –
  * Fix animation issue with React 18 –

# Alert Dialog
0.1.7
  * Improve pointer-events management –

# Checkbox
0.1.5
  * Prevent activation via enter key –

# Collapsible
0.1.6
  * Fix animation issue with React 18 –

# Context Menu
0.1.6
  * Prevent `DropdownMenu.TriggerItem` click from firing twice –
  * Improve idle performance –

# Dialog
0.1.7Major
  * Improve pointer-events management –
  * **[Breaking]** `Dialog.Title` is now a required part so will throw an error if not used. `aria-describedby={undefined}` must be passed to `Dialog.Content` if no description is needed. –

# Dropdown Menu
0.1.6
  * Improve composability with `Dialog`/`AlertDialog` –
  * Prevent clicking trigger to close from immediately reopening in non-modal mode –
  * Prevent `DropdownMenu.TriggerItem` click from firing twice –
  * Improve idle performance –

# Navigation Menu
0.1.2Preview
  * New primitive –

# Radio Group
0.1.5
  * Prevent activation via enter key –

# Select
0.1.1Preview
  * New primitive –

# Slider
0.1.4
  * Prevent page scroll when using `Home` and `End` keys –

# Tabs
0.1.5
  * Prevent accidental focus activation via right click –

# Toast
0.1.1Preview
  * New primitive –

# Toggle Group
0.1.5
  * Improve accessibility by using radio role for single toggle group –

## [December 13, 2021](https://www.radix-ui.com/primitives/docs/overview/releases#december-13-2021)
This release focuses on React 18 support and introduces a number of breaking changes to some packages, mostly related to portalling dialogs.
# All primitives
  * **[Breaking]** Deprecate `IdProvider`. Improves support for React 18 going forward and is no longer needed in older versions. Remove from your app to avoid deprecation warnings. –

# Accordion
0.1.5Major
  * Improve React 18 support –
  * Improve dev mode errors with mismatched `type` and `value` props –
  * Prevent `Accordion.Content` height animation on initial page load –

# Alert Dialog
0.1.5Major
  * **[Breaking]** Add new `Portal` part. To avoid regressions, use this part if you want portalling behavior. –
  * **[Breaking]** Support scrolling within `AlertDialog.Overlay`. Move `allowPinchZoom` to root. –
  * Fix `asChild` TypeScript error –

# Collapsible
0.1.5
  * Prevent `Collapsible.Content` height animation on initial page load –

# Dialog
0.1.5Major
  * **[Breaking]** Add new `Portal` part. To avoid regressions, use this part if you want portalling behavior. –
  * **[Breaking]** Support scrolling within `Dialog.Overlay`. Move `allowPinchZoom` to root. –

# Dropdown Menu
0.1.4
  * Prevent disabled trigger from opening menu –

# Hover Card
0.1.3
  * Fix ability to focus `HoverCard` when inside a dialog –

# Radio Group
0.1.4
  * Prevent programmatic focus from changing value –

# Tabs
0.1.4Major
  * **[Breaking]** Change `Tabs.Trigger` to `button` element –
  * Improve TSDocs –

# Toggle Group
0.1.4
  * Remove invalid `aria-orientation` attribute on `role=group` element –

# Toolbar
0.1.4
  * Fix `asChild` TypeScript error –
  * Remove invalid `toolbaritem` role –

# Tooltip
0.1.6Major
  * **[Breaking]** Add new `TooltipProvider` part. You must wrap your app to avoid regressions. –
  * **[Breaking]** Remove `type=button` attribute from `Tooltip.Trigger` –
  * Fix tooltip activation regression –

# Slot
0.1.2
  * Fix `key` warnings –

## [October 15, 2021](https://www.radix-ui.com/primitives/docs/overview/releases#october-15-2021)
# All primitives
  * All primitives are now versioned 0.1.1
  * Fix composability issues between primitives by scoping context –
  * Fix CSS unmount animations –

# Accordion
0.1.1
  * Add new CSS variable to `Accordion.Content` to help with width animations –

# Alert Dialog
0.1.1Major
  * Improve composability with `Dialog` –
  * **[Breaking]** Remove `AlertDialog.Content` `onInteractOutside` prop –

# Dialog
0.1.1
  * Improve composability with `AlertDialog` –
  * Add pinch to zoom support to `DropdownMenu.Content` via `allowPinchZoom` prop –

# Context Menu
0.1.1
  * Add pinch to zoom support to `ContextMenu.Content` via `allowPinchZoom` prop –
  * Prevent scroll via arrow keypress on submenu triggers –

# Collapsible
0.1.1
  * Add new CSS variable to `Collapsible.Content` to help with width animations –

# Checkbox
0.1.1
  * Prevent screen reader virtual cursor from accessing hidden input –

# Dropdown Menu
0.1.1
  * Improve composability with `Tooltip` –
  * Add pinch to zoom support to `DropdownMenu.Content` via `allowPinchZoom` prop –
  * Prevent scroll via arrow keypress on submenu triggers –

# Hover Card
0.1.1
  * Open on focus to improve keyboard support –
  * Compose correct pointer events internally –

# Label
0.1.1
  * Allow its children to prevent event propagation –

# Radio Group
0.1.1
  * Prevent screen reader virtual cursor from accessing hidden inputs –

# Popover
0.1.1
  * Add pinch to zoom support to `Popover.Content` via `allowPinchZoom` prop –

# Slider
0.1.1
  * Fix calculations when value is `0` –

# Switch
0.1.1
  * Prevent screen reader virtual cursor from accessing hidden input –

# Tabs
0.1.1Major
  * **[Breaking]** Unmount content within `Tabs.Content` when tab is inactive –

## [September 7, 2021](https://www.radix-ui.com/primitives/docs/overview/releases#september-7-2021)
# All primitives
  * All primitives moved to **Beta** and are now versioned 0.1.0
  * **[Breaking]** Replace polymorphic `as` prop with `asChild` boolean prop. Learn more about how to [change the rendered element here](https://www.radix-ui.com/primitives/docs/guides/composition) –

# Dialog
0.1.0
  * Improve composability with `DropdownMenu` –

# Dropdown Menu
0.1.0
  * Improve composability with `Dialog` –
  * Re-enable `pointer-events` when closed –
  * Prevent body text from selecting on close (Firefox) –
  * Ensure sub triggers receive focus on click (iOS Safari) –

# Primitive
0.1.0Major
  * **[Breaking]** Deprecate `extendPrimitive` utility –

## [August 4, 2021](https://www.radix-ui.com/primitives/docs/overview/releases#august-4-2021)
# All primitives
  * Improve polymorphic types performance –

# Alert Dialog
0.0.20Major
  * **[Breaking]** Remove `AlertDialog.Content` `onPointerDownOutside` prop –
  * Prevent outside pointer events triggering prematurely on touch devices –

# Context Menu
0.0.24Major
  * Add modality support via `modal` prop –
  * **[Breaking]** Remove `ContextMenu.Content` `disableOutsidePointerEvents` prop –
  * Prevent outside pointer events triggering prematurely on touch devices –

# Dialog
0.0.20
  * Add modality support via `modal` prop –
  * Improve animation rendering in React 18 –
  * Ensure focus is restored to trigger on close when using the `autofocus` attribute on a child element –
  * Prevent outside pointer events triggering prematurely on touch devices –
  * Ensure iOS Safari consistently focuses the first focusable element –

# Dropdown Menu
0.0.23Major
  * Add modality support via `modal` prop –
  * **[Breaking]** Remove `DropdownMenu.Content` `disableOutsideScroll` prop –
  * **[Breaking]** Remove `DropdownMenu.Content` `disableOutsidePointerEvents` prop –
  * Prevent outside pointer events triggering prematurely on touch devices –

# Popover
0.0.20Major
  * Add modality support via `modal` prop –
  * **[Breaking]** Remove `Popover.Content` `disableOutsideScroll` prop –
  * **[Breaking]** Remove `Popover.Content` `disableOutsidePointerEvents` prop –
  * **[Breaking]** Remove `Popover.Content` `trapFocus` prop –
  * Improve animation rendering in React 18 –
  * Ensure focus is restored to trigger on close when using the `autofocus` attribute on a child element –
  * Prevent outside pointer events triggering prematurely on touch devices –
  * Ensure iOS Safari consistently focuses the first focusable element –

# Scroll Area
0.0.16
  * Add `data-state` to `ScrollBar` part –

# Slider
0.0.17
  * Prevent thumb receiving focus when disabled –
  * Prevent focus loss on thumb when using `React.StrictMode` –

## [June 24, 2021](https://www.radix-ui.com/primitives/docs/overview/releases#june-24-2021)
# Context Menu
0.0.23
  * Can now be triggered on touch with a long press –

# Dialog
0.0.19
  * Add optional `Title` and `Description` parts for simpler labelling –

# Scroll Area
0.0.15
  * Add `data-orientation` to `Scrollbar` for styling convenience –
  * Fix `forceMount` type issue on `Scrollbar` –

# Slider
0.0.16
  * Ensure the correct thumb is focused when using keyboard and crossing another thumb –
  * Ensure only one arrow press is needed when crossing another thumb –

# Slot
0.0.12
  * Improve types compatibility –

# Toggle Group
0.0.10
  * Ensure only one click is needed to toggle a single controlled toggle group –
  * Ensure focus behavior is consistent on Safari –

## [June 15, 2021](https://www.radix-ui.com/primitives/docs/overview/releases#june-15-2021)
# All primitives
  * Improve polymorphic types –

# Accordion
0.0.16Major
  * **[Breaking]** Rename `Accordion.Button` to `Accordion.Trigger` –
  * **[Breaking]** Rename `Accordion.Panel` to `Accordion.Content` –
  * **[Breaking]** Rename custom property accordingly (`--radix-accordion-content-height`) –
  * **[Breaking]** `type=“single”` `Accordion` now has a new `collapsible` prop which is `false` by default. This means that the default behavior has now changed. By default a user cannot close all items. –

# Alert Dialog
0.0.18Major
  * **[Breaking]** Allow preventing default in `onPointerDownOutside` without inadvertently preventing focus –

# Checkbox
0.0.16Major
  * **[Breaking]** `onCheckedChange(event)` is now `onCheckedChange(checked: CheckedState)` –
  * Improve compatibility with native form validation –
  * Allow stopping propagation on `Checkbox` `onClick` –
  * Improve compatibility with native `label` –
  * Improve accessibility when wrapped in native `label` –

# Collapsible
0.0.16Major
  * **[Breaking]** Rename `Collapsible.Button` to `Collapsible.Trigger` –

# Context Menu
0.0.22Major
  * Add submenu support –
  * Add `ContextMenu.TriggerItem` –
  * Add `ContextMenu.Arrow` –
  * Add `dir` prop for RTL support with submenus –
  * **[Breaking]** Allow preventing default in `onPointerDownOutside` without inadvertently preventing focus –
  * **[Breaking]** Remove `ContextMenu.Content` `side` prop –
  * **[Breaking]** Remove `ContextMenu.Content` `align` prop –
  * **[Breaking]** If you had `sideOffset` on `ContextMenu.Content` before, you should now use `alignOffset`. This is to standardize vertical alignment for both root and sub-menus. –
  * **[Breaking]** `onFocusOutside` is now a custom event –
  * Improve support of content and item with no padding –
  * Align with WAI-ARIA spec by focusing first item when opening via keyboard –

# Dialog
0.0.18Major
  * **[Breaking]** Allow preventing default in `onPointerDownOutside` without inadvertently preventing focus –

# Dropdown Menu
0.0.21Major
  * Add submenu support –
  * Add `DropdownMenu.TriggerItem` –
  * Add `dir` prop for RTL support with submenus –
  * **[Breaking]** Allow preventing default in `onPointerDownOutside` without inadvertently preventing focus –
  * **[Breaking]** `onFocusOutside` is now a custom event –
  * **[Breaking]** The up arrow no longer opens the menu –
  * Align with WAI-ARIA spec by focusing first item when opening via keyboard –

# Popover
0.0.18Major
  * **[Breaking]** Allow preventing default in `onPointerDownOutside` without inadvertently preventing focus –
  * **[Breaking]** `onFocusOutside` is now a custom event –

# Radio Group
0.0.17Major
  * **[Breaking]** `onValueChange(event)` is now `onValueChange(value: string)` –
  * **[Breaking]** Remove `RadioGroup.Item` `onCheckedChange` prop –
  * Improve compatibility with native form validation –
  * Improve usage within forms –

# Scroll Area
0.0.14Major
  * Brand new version with a simpler API –
  * Improve Safari support –
  * Improve RTL support –
  * Improve touch support –
  * `Scrollbar` mount/unmount can now be animated –
  * Add minimum width/height to thumb so it's always grabbable –
  * Move functional CSS into component to improve DX –
  * Bundle size significantly reduced –
  * **[Breaking]** Remove `overflowX` and `overflowY` props –
  * **[Breaking]** Remove `ScrollAreaButtonStart`, `ScrollAreaButtonEnd` and `ScrollAreaTrack` –
  * **[Breaking]** Rename `scrollbarVisibility` prop to `type`. The values are `auto`, `always`, `scroll` or `hover` –
  * **[Breaking]** Rename `scrollbarVisibilityRestTimeout` prop to `scrollHideDelay` –
  * **[Breaking]** Remove `trackClickBehavior` prop as we've removed built-in animation. Clicking on track always snaps to pointer position –
  * **[Breaking]** `ScrollAreaScrollbarX` and `ScrollAreaScrollbarY` are now `<ScrollAreaScrollbar orientation="horizontal" />` and `<ScrollAreaScrollbar orientation="vertical" />` –
  * Ensure no scrollbars are shown when scrolling is disabled –
  * Ensure children event handlers don't break –
  * Ensure scroll area updates when children content size changes –

# Slider
0.0.15
  * Improve usage within forms –
  * Fix key binding issue in LTR –

# Switch
0.0.14Major
  * **[Breaking]** `onCheckedChange(event)` is now `onCheckedChange(checked: boolean)` –
  * Improve compatibility with native form validation –
  * Improve usage within forms –
  * Improve accessibility when wrapped in native `label` –

# Tabs
0.0.14Major
  * **[Breaking]** Rename `Tabs.Tab` to `Tabs.Trigger` –
  * **[Breaking]** Rename `Tabs.Panel` to `Tabs.Content` –

## [May 3, 2021](https://www.radix-ui.com/primitives/docs/overview/releases#may-3-2021)
# All primitives
  * Improve polymorphic types performance –

# Accordion
0.0.14
  * Ensure only one click is needed to close a single controlled accordion –

# Checkbox
0.0.14Major
  * **[Breaking]** Remove `readOnly` prop –

# Context Menu
0.0.18
  * Add `onOpenChange` prop –

# Dialog
0.0.16
  * Ensure focus position isn't lost when blurring out window and re-focusing it –

# Dropdown Menu
0.0.18Major
  * Take into account non-visible items –
