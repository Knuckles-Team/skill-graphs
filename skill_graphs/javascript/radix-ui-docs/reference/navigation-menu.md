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
# Navigation Menu
A collection of links for navigating websites.
  * Learn
  * Overview

index.jsxindex.jsxstyles.cssstyles.css
CSS

```

import * as React from "react";

import { NavigationMenu } from "radix-ui";

import classNames from "classnames";

import { CaretDownIcon } from "@radix-ui/react-icons";

import "./styles.css";

const NavigationMenuDemo = () => {

	return (

		<NavigationMenu.Root className="NavigationMenuRoot">

			<NavigationMenu.List className="NavigationMenuList">

				<NavigationMenu.Item>

					<NavigationMenu.Trigger className="NavigationMenuTrigger">

						Learn <CaretDownIcon className="CaretDown" aria-hidden />

					</NavigationMenu.Trigger>

					<NavigationMenu.Content className="NavigationMenuContent">

						<ul className="List one">

							<li style={{ gridRow: "span 3" }}>

								<NavigationMenu.Link asChild>

									<a className="Callout" href="#">

										<svg
											aria-hidden
											width="38"
											height="38"
											viewBox="0 0 25 25"
											fill="white"
										>

											<path d="M12 25C7.58173 25 4 21.4183 4 17C4 12.5817 7.58173 9 12 9V25Z"></path>

											<path d="M12 0H4V8H12V0Z"></path>

											<path d="M17 8C19.2091 8 21 6.20914 21 4C21 1.79086 19.2091 0 17 0C14.7909 0 13 1.79086 13 4C13 6.20914 14.7909 8 17 8Z"></path>

										</svg>

										<div className="CalloutHeading">Radix Primitives</div>

										<p className="CalloutText">

											Unstyled, accessible components for React.

										</p>

									</a>

								</NavigationMenu.Link>

							</li>

							<ListItem href="https://stitches.dev/" title="Stitches">

								CSS-in-JS with best-in-class developer experience.

							</ListItem>

							<ListItem href="/colors" title="Colors">

								Beautiful, thought-out palettes with auto dark mode.

							</ListItem>

							<ListItem href="https://icons.radix-ui.com/" title="Icons">

								A crisp set of 15x15 icons, balanced and consistent.

							</ListItem>

						</ul>

					</NavigationMenu.Content>

				</NavigationMenu.Item>

				<NavigationMenu.Item>

					<NavigationMenu.Trigger className="NavigationMenuTrigger">

						Overview <CaretDownIcon className="CaretDown" aria-hidden />

					</NavigationMenu.Trigger>

					<NavigationMenu.Content className="NavigationMenuContent">

						<ul className="List two">

							<ListItem
								title="Introduction"
								href="/primitives/docs/overview/introduction"
							>

								Build high-quality, accessible design systems and web apps.

							</ListItem>

							<ListItem
								title="Getting started"
								href="/primitives/docs/overview/getting-started"
							>

								A quick tutorial to get you up and running with Radix

								Primitives.

							</ListItem>

							<ListItem title="Styling" href="/primitives/docs/guides/styling">

								Unstyled and compatible with any styling solution.

							</ListItem>

							<ListItem
								title="Animation"
								href="/primitives/docs/guides/animation"
							>

								Use CSS keyframes or any animation library of your choice.

							</ListItem>

							<ListItem
								title="Accessibility"
								href="/primitives/docs/overview/accessibility"
							>

								Tested in a range of browsers and assistive technologies.

							</ListItem>

							<ListItem
								title="Releases"
								href="/primitives/docs/overview/releases"
							>

								Radix Primitives releases and their changelogs.

							</ListItem>

						</ul>

					</NavigationMenu.Content>

				</NavigationMenu.Item>

				<NavigationMenu.Item>

					<NavigationMenu.Link
						className="NavigationMenuLink"
						href="https://github.com/radix-ui"
					>

						Github

					</NavigationMenu.Link>

				</NavigationMenu.Item>

				<NavigationMenu.Indicator className="NavigationMenuIndicator">

					<div className="Arrow" />

				</NavigationMenu.Indicator>

			</NavigationMenu.List>

			<div className="ViewportPosition">

				<NavigationMenu.Viewport className="NavigationMenuViewport" />

			</div>

		</NavigationMenu.Root>

	);

};

const ListItem = React.forwardRef(function ListItem(

	{ className, children, title, ...props },
	forwardedRef,

) {

	return (

		<li>

			<NavigationMenu.Link asChild>

				<a
					className={classNames("ListItemLink", className)}
					{...props}
					ref={forwardedRef}
				>

					<div className="ListItemHeading">{title}</div>

					<p className="ListItemText">{children}</p>

				</a>

			</NavigationMenu.Link>

		</li>

	);

});

export default NavigationMenuDemo;

Expand code

```

## Features
  * Can be controlled or uncontrolled.
  * Flexible layout structure with managed tab focus.
  * Supports submenus.
  * Optional active item indicator.
  * Full keyboard navigation.
  * Exposes CSS variables for advanced animation.
  * Supports custom timings.

## Component Reference Links
Version: 1.2.15
Size:
[View as Markdown](https://www.radix-ui.com/primitives/docs/components/navigation-menu.md)
## [Anatomy](https://www.radix-ui.com/primitives/docs/components/navigation-menu#anatomy)
Import all parts and piece them together.

```

import { NavigationMenu } from "radix-ui";

export default () => (

	<NavigationMenu.Root>

		<NavigationMenu.List>

			<NavigationMenu.Item>

				<NavigationMenu.Trigger />

				<NavigationMenu.Content>

					<NavigationMenu.Link />

				</NavigationMenu.Content>

			</NavigationMenu.Item>

			<NavigationMenu.Item>

				<NavigationMenu.Link />

			</NavigationMenu.Item>

			<NavigationMenu.Item>

				<NavigationMenu.Trigger />

				<NavigationMenu.Content>

					<NavigationMenu.Sub>

						<NavigationMenu.List />

						<NavigationMenu.Viewport />

					</NavigationMenu.Sub>

				</NavigationMenu.Content>

			</NavigationMenu.Item>

			<NavigationMenu.Indicator />

		</NavigationMenu.List>

		<NavigationMenu.Viewport />

	</NavigationMenu.Root>

);

```

## [API Reference](https://www.radix-ui.com/primitives/docs/components/navigation-menu#api-reference)
### [Root](https://www.radix-ui.com/primitives/docs/components/navigation-menu#root)
Contains all the parts of a navigation menu.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `defaultValue` Prop description  | `string`  | No default value  |
|  `value` Prop description  | `string`  | No default value  |
|  `onValueChange` Prop description  |  `function` See full type  | No default value  |
|  `delayDuration` Prop description  | `number`  | `200`  |
|  `skipDelayDuration` Prop description  | `number`  | `300`  |
|  `dir` Prop description  |  `enum` See full type  | No default value  |
|  `orientation` Prop description  |  `enum` See full type  | `"horizontal"`  |
| Data attribute  | Values  |
| --- | --- |
| `[data-orientation]`  | `"vertical"  | "horizontal" `  |
### [Sub](https://www.radix-ui.com/primitives/docs/components/navigation-menu#sub)
Signifies a submenu. Use it in place of the root part when nested to create a submenu.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `defaultValue` Prop description  | `string`  | No default value  |
|  `value` Prop description  | `string`  | No default value  |
|  `onValueChange` Prop description  |  `function` See full type  | No default value  |
|  `orientation` Prop description  |  `enum` See full type  | `"horizontal"`  |
| Data attribute  | Values  |
| --- | --- |
| `[data-orientation]`  | `"vertical"  | "horizontal" `  |
### [List](https://www.radix-ui.com/primitives/docs/components/navigation-menu#list)
Contains the top level menu items.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
| Data attribute  | Values  |
| --- | --- |
| `[data-orientation]`  | `"vertical"  | "horizontal" `  |
### [Item](https://www.radix-ui.com/primitives/docs/components/navigation-menu#item)
A top level menu item, contains a link or trigger with content combination.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
|  `value` Prop description  | `string`  | No default value  |
### [Trigger](https://www.radix-ui.com/primitives/docs/components/navigation-menu#trigger)
The button that toggles the content.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
| Data attribute  | Values  |
| --- | --- |
| `[data-state]`  | `"open"  | "closed" `  |
| `[data-disabled]`  | Present when disabled  |
### [Content](https://www.radix-ui.com/primitives/docs/components/navigation-menu#content)
Contains the content associated with each trigger.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
|  `onEscapeKeyDown` Prop description  |  `function` See full type  | No default value  |
|  `onPointerDownOutside` Prop description  |  `function` See full type  | No default value  |
|  `onFocusOutside` Prop description  |  `function` See full type  | No default value  |
|  `onInteractOutside` Prop description  |  `function` See full type  | No default value  |
|  `forceMount` Prop description  | `boolean`  | No default value  |
| Data attribute  | Values  |
| --- | --- |
| `[data-state]`  | `"open"  | "closed" `  |
| `[data-motion]`  | `"to-start"  | "to-end"  | "from-start"  | "from-end" `  |
| `[data-orientation]`  | `"vertical"  | "horizontal" `  |
### [Link](https://www.radix-ui.com/primitives/docs/components/navigation-menu#link)
A navigational link.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
|  `active` Prop description  | `boolean`  | `false`  |
|  `onSelect` Prop description  |  `function` See full type  | No default value  |
| Data attribute  | Values  |
| --- | --- |
| `[data-active]`  | Present when active  |
### [Indicator](https://www.radix-ui.com/primitives/docs/components/navigation-menu#indicator)
An optional indicator element that renders below the list, is used to highlight the currently active trigger.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
|  `forceMount` Prop description  | `boolean`  | No default value  |
| Data attribute  | Values  |
| --- | --- |
| `[data-state]`  | `"visible"  | "hidden" `  |
| `[data-orientation]`  | `"vertical"  | "horizontal" `  |
### [Viewport](https://www.radix-ui.com/primitives/docs/components/navigation-menu#viewport)
An optional viewport element that is used to render active content outside of the list.
| Prop  | Type  | Default  |
| --- | --- | --- |
|  `asChild` Prop description  | `boolean`  | `false`  |
|  `forceMount` Prop description  | `boolean`  | No default value  |
| Data attribute  | Values  |
| --- | --- |
| `[data-state]`  | `"open"  | "closed" `  |
| `[data-orientation]`  | `"vertical"  | "horizontal" `  |
| CSS Variable  | Description  |
| --- | --- |
| `--radix-navigation-menu-viewport-width`  | The width of the viewport when visible/hidden, computed from the active content  |
| `--radix-navigation-menu-viewport-height`  | The height of the viewport when visible/hidden, computed from the active content  |
## [Examples](https://www.radix-ui.com/primitives/docs/components/navigation-menu#examples)
### [Vertical](https://www.radix-ui.com/primitives/docs/components/navigation-menu#vertical)
You can create a vertical menu by using the `orientation` prop.

```

<NavigationMenu.Root orientation="vertical">

	<NavigationMenu.List>

		<NavigationMenu.Item>

			<NavigationMenu.Trigger>Item one</NavigationMenu.Trigger>

			<NavigationMenu.Content>Item one content</NavigationMenu.Content>

		</NavigationMenu.Item>

		<NavigationMenu.Item>

			<NavigationMenu.Trigger>Item two</NavigationMenu.Trigger>

			<NavigationMenu.Content>Item Two content</NavigationMenu.Content>

		</NavigationMenu.Item>

	</NavigationMenu.List>

</NavigationMenu.Root>

```

### [Flexible layouts](https://www.radix-ui.com/primitives/docs/components/navigation-menu#flexible-layouts)
Use the `Viewport` part when you need extra control over where `Content` is rendered. This can be helpful when your design requires an adjusted DOM structure or if you need flexibility to achieve [advanced animation](https://www.radix-ui.com/primitives/docs/components/navigation-menu#advanced-animation). Tab focus will be maintained automatically.

```

<NavigationMenu.Root>

	<NavigationMenu.List>

		<NavigationMenu.Item>

			<NavigationMenu.Trigger>Item one</NavigationMenu.Trigger>

			<NavigationMenu.Content>Item one content</NavigationMenu.Content>

		</NavigationMenu.Item>

		<NavigationMenu.Item>

			<NavigationMenu.Trigger>Item two</NavigationMenu.Trigger>

			<NavigationMenu.Content>Item two content</NavigationMenu.Content>

		</NavigationMenu.Item>

	</NavigationMenu.List>

	{/* NavigationMenu.Content will be rendered here when active */}

	<NavigationMenu.Viewport />

</NavigationMenu.Root>

```

### [With indicator](https://www.radix-ui.com/primitives/docs/components/navigation-menu#with-indicator)
You can use the optional `Indicator` part to highlight the currently active `Trigger`, this is useful when you want to provide an animated visual cue such as an arrow or highlight to accompany the `Viewport`.

```

// index.jsx

import { NavigationMenu } from "radix-ui";

import "./styles.css";

export default () => (

	<NavigationMenu.Root>

		<NavigationMenu.List>

			<NavigationMenu.Item>

				<NavigationMenu.Trigger>Item one</NavigationMenu.Trigger>

				<NavigationMenu.Content>Item one content</NavigationMenu.Content>

			</NavigationMenu.Item>

			<NavigationMenu.Item>

				<NavigationMenu.Trigger>Item two</NavigationMenu.Trigger>

				<NavigationMenu.Content>Item two content</NavigationMenu.Content>

			</NavigationMenu.Item>

			<NavigationMenu.Indicator className="NavigationMenuIndicator" />

		</NavigationMenu.List>

		<NavigationMenu.Viewport />

	</NavigationMenu.Root>

);

```

```

/* styles.css */

.NavigationMenuIndicator {

	background-color: grey;

}

.NavigationMenuIndicator[data-orientation="horizontal"] {

	height: 3px;

	transition:

		width,

		transform,

		250ms ease;

}

```

### [With submenus](https://www.radix-ui.com/primitives/docs/components/navigation-menu#with-submenus)
Create a submenu by nesting your `NavigationMenu` and using the `Sub` part in place of its `Root`. Submenus work differently to `Root` navigation menus and are similar to [`Tabs`](https://www.radix-ui.com/primitives/docs/components/tabs) in that one item should always be active, so be sure to assign and set a `defaultValue`.

```

<NavigationMenu.Root>

	<NavigationMenu.List>

		<NavigationMenu.Item>

			<NavigationMenu.Trigger>Item one</NavigationMenu.Trigger>

			<NavigationMenu.Content>Item one content</NavigationMenu.Content>

		</NavigationMenu.Item>

		<NavigationMenu.Item>

			<NavigationMenu.Trigger>Item two</NavigationMenu.Trigger>

			<NavigationMenu.Content>

				<NavigationMenu.Sub defaultValue="sub1">

					<NavigationMenu.List>

						<NavigationMenu.Item value="sub1">

							<NavigationMenu.Trigger>Sub item one</NavigationMenu.Trigger>

							<NavigationMenu.Content>

								Sub item one content

							</NavigationMenu.Content>

						</NavigationMenu.Item>

						<NavigationMenu.Item value="sub2">

							<NavigationMenu.Trigger>Sub item two</NavigationMenu.Trigger>

							<NavigationMenu.Content>

								Sub item two content

							</NavigationMenu.Content>

						</NavigationMenu.Item>

					</NavigationMenu.List>

				</NavigationMenu.Sub>

			</NavigationMenu.Content>

		</NavigationMenu.Item>

	</NavigationMenu.List>

</NavigationMenu.Root>

```

### [With client side routing](https://www.radix-ui.com/primitives/docs/components/navigation-menu#with-client-side-routing)
If you need to use the `Link` component provided by your routing package then we recommend composing with `NavigationMenu.Link` via a custom component. This will ensure accessibility and consistent keyboard control is maintained. Here's an example using Next.js:

```

// index.jsx

import { usePathname } from "next/navigation";

import NextLink from "next/link";

import { NavigationMenu } from "radix-ui";

import "./styles.css";

const Link = ({ href, ...props }) => {

	const pathname = usePathname();

	const isActive = href === pathname;

	return (

		<NavigationMenu.Link asChild active={isActive}>

			<NextLink href={href} className="NavigationMenuLink" {...props} />

		</NavigationMenu.Link>

	);

};

export default () => (

	<NavigationMenu.Root>

		<NavigationMenu.List>

			<NavigationMenu.Item>

				<Link href="/">Home</Link>

			</NavigationMenu.Item>

			<NavigationMenu.Item>

				<Link href="/about">About</Link>

			</NavigationMenu.Item>

		</NavigationMenu.List>

	</NavigationMenu.Root>

);

```

```

/* styles.css */

.NavigationMenuLink {

	text-decoration: none;

}

.NavigationMenuLink[data-active] {

	text-decoration: "underline";

}

```

### [Advanced animation](https://www.radix-ui.com/primitives/docs/components/navigation-menu#advanced-animation)
We expose `--radix-navigation-menu-viewport-[width|height]` and `data-motion['from-start'|'to-start'|'from-end'|'to-end']` attributes to allow you to animate `Viewport` size and `Content` position based on the enter/exit direction.
Combining these with `position: absolute;` allows you to create smooth overlapping animation effects when moving between items.

```

// index.jsx

import { NavigationMenu } from "radix-ui";

import "./styles.css";

export default () => (

	<NavigationMenu.Root>

		<NavigationMenu.List>

			<NavigationMenu.Item>

				<NavigationMenu.Trigger>Item one</NavigationMenu.Trigger>

				<NavigationMenu.Content className="NavigationMenuContent">

					Item one content

				</NavigationMenu.Content>

			</NavigationMenu.Item>

			<NavigationMenu.Item>

				<NavigationMenu.Trigger>Item two</NavigationMenu.Trigger>

				<NavigationMenu.Content className="NavigationMenuContent">

					Item two content

				</NavigationMenu.Content>

			</NavigationMenu.Item>

		</NavigationMenu.List>

		<NavigationMenu.Viewport className="NavigationMenuViewport" />

	</NavigationMenu.Root>

);

```

```

/* styles.css */

.NavigationMenuContent {

	position: absolute;

	top: 0;

	left: 0;

	animation-duration: 250ms;

	animation-timing-function: ease;

}

.NavigationMenuContent[data-motion="from-start"] {

	animation-name: enterFromLeft;

}

.NavigationMenuContent[data-motion="from-end"] {

	animation-name: enterFromRight;

}

.NavigationMenuContent[data-motion="to-start"] {

	animation-name: exitToLeft;

}

.NavigationMenuContent[data-motion="to-end"] {

	animation-name: exitToRight;

}

.NavigationMenuViewport {

	position: relative;

	width: var(--radix-navigation-menu-viewport-width);

	height: var(--radix-navigation-menu-viewport-height);

	transition:

		width,

		height,

		250ms ease;

}

@keyframes enterFromRight {

	from {

		opacity: 0;

		transform: translateX(200px);

	}

	to {

		opacity: 1;

		transform: translateX(0);

	}

}

@keyframes enterFromLeft {

	from {

		opacity: 0;

		transform: translateX(-200px);

	}

	to {

		opacity: 1;

		transform: translateX(0);

	}

}

@keyframes exitToRight {

	from {

		opacity: 1;

		transform: translateX(0);

	}

	to {

		opacity: 0;

		transform: translateX(200px);

	}

}

@keyframes exitToLeft {

	from {

		opacity: 1;

		transform: translateX(0);

	}

	to {

		opacity: 0;

		transform: translateX(-200px);

	}

}

```

## [Accessibility](https://www.radix-ui.com/primitives/docs/components/navigation-menu#accessibility)
Adheres to the
### [Differences to menubar](https://www.radix-ui.com/primitives/docs/components/navigation-menu#differences-to-menubar)
`NavigationMenu` should not be confused with `menubar`, although this primitive shares the name `menu` in the colloquial sense to refer to a set of navigation links, it does not use the WAI-ARIA `menu` role. This is because `menu` and `menubars` behave like native operating system menus most commonly found in desktop application windows, as such they feature complex functionality like composite focus management and first-character navigation.
These features are often considered
See the W3C
### [Link usage and aria-current](https://www.radix-ui.com/primitives/docs/components/navigation-menu#link-usage-and-aria-current)
It's important to use `NavigationMenu.Link` for all navigational links within a menu, this not only applies to the main list but also within any content rendered via `NavigationMenu.Content`. This will ensure consistent keyboard interactions and accessibility while also giving access to the `active` prop for setting `aria-current` and the active styles. See [this example](https://www.radix-ui.com/primitives/docs/components/navigation-menu#with-client-side-routing) for more information on usage with third party routing components.
### [Keyboard Interactions](https://www.radix-ui.com/primitives/docs/components/navigation-menu#keyboard-interactions)
| Key  | Description  |
| --- | --- |
|  `Space``Enter`  | When focus is on `NavigationMenu.Trigger`, opens the content.  |
| `Tab`  | Moves focus to the next focusable element.  |
| `ArrowDown`  | When `horizontal` and focus is on an open `NavigationMenu.Trigger`, moves focus into `NavigationMenu.Content`.
Moves focus to the next `NavigationMenu.Trigger` or `NavigationMenu.Link`.  |
| `ArrowUp`  | Moves focus to the previous `NavigationMenu.Trigger` or `NavigationMenu.Link`.  |
|  `ArrowRight``ArrowLeft`  | When `vertical` and focus is on an open `NavigationMenu.Trigger`, moves focus into its `NavigationMenu.Content`.
Moves focus to the next / previous `NavigationMenu.Trigger` or `NavigationMenu.Link`.  |
|  `Home``End`  | Moves focus to the first/last `NavigationMenu.Trigger` or `NavigationMenu.Link`.  |
| `Esc`  | Closes open `NavigationMenu.Content` and moves focus to its `NavigationMenu.Trigger`.  |
#### Quick nav
  * [Anatomy](https://www.radix-ui.com/primitives/docs/components/navigation-menu#anatomy)
  * [API Reference](https://www.radix-ui.com/primitives/docs/components/navigation-menu#api-reference)
  * [Root](https://www.radix-ui.com/primitives/docs/components/navigation-menu#root)
  * [Sub](https://www.radix-ui.com/primitives/docs/components/navigation-menu#sub)
  * [List](https://www.radix-ui.com/primitives/docs/components/navigation-menu#list)
  * [Item](https://www.radix-ui.com/primitives/docs/components/navigation-menu#item)
  * [Trigger](https://www.radix-ui.com/primitives/docs/components/navigation-menu#trigger)
  * [Content](https://www.radix-ui.com/primitives/docs/components/navigation-menu#content)
  * [Link](https://www.radix-ui.com/primitives/docs/components/navigation-menu#link)
  * [Indicator](https://www.radix-ui.com/primitives/docs/components/navigation-menu#indicator)
  * [Viewport](https://www.radix-ui.com/primitives/docs/components/navigation-menu#viewport)
  * [Examples](https://www.radix-ui.com/primitives/docs/components/navigation-menu#examples)
  * [Vertical](https://www.radix-ui.com/primitives/docs/components/navigation-menu#vertical)
  * [Flexible layouts](https://www.radix-ui.com/primitives/docs/components/navigation-menu#flexible-layouts)
  * [With indicator](https://www.radix-ui.com/primitives/docs/components/navigation-menu#with-indicator)
  * [With submenus](https://www.radix-ui.com/primitives/docs/components/navigation-menu#with-submenus)
  * [With client side routing](https://www.radix-ui.com/primitives/docs/components/navigation-menu#with-client-side-routing)
  * [Advanced animation](https://www.radix-ui.com/primitives/docs/components/navigation-menu#advanced-animation)
  * [Accessibility](https://www.radix-ui.com/primitives/docs/components/navigation-menu#accessibility)
  * [Differences to menubar](https://www.radix-ui.com/primitives/docs/components/navigation-menu#differences-to-menubar)
  * [Link usage and aria-current](https://www.radix-ui.com/primitives/docs/components/navigation-menu#link-usage-and-aria-current)
  * [Keyboard Interactions](https://www.radix-ui.com/primitives/docs/components/navigation-menu#keyboard-interactions)

Previous[Menubar](https://www.radix-ui.com/primitives/docs/components/menubar)
Next[One-Time Password Field](https://www.radix-ui.com/primitives/docs/components/one-time-password-field)
