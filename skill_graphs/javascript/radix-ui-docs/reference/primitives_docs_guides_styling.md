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
# Styling
Radix Primitives are unstyled—and compatible with any styling solution—giving you complete control over styling.
## [Styling overview](https://www.radix-ui.com/primitives/docs/guides/styling#styling-overview)
### [Functional styles](https://www.radix-ui.com/primitives/docs/guides/styling#functional-styles)
You are in control of all aspects of styling, including functional styles. For example—by default—a [Dialog Overlay](https://www.radix-ui.com/primitives/docs/components/dialog) won't cover the entire viewport. You're responsible for adding those styles, plus any presentation styles.
### [Classes](https://www.radix-ui.com/primitives/docs/guides/styling#classes)
All components and their parts accept a `className` prop. This class will be passed through to the DOM element. You can use it in CSS as expected.
### [Data attributes](https://www.radix-ui.com/primitives/docs/guides/styling#data-attributes)
When components are stateful, their state will be exposed in a `data-state` attribute. For example, when an [Accordion Item](https://www.radix-ui.com/primitives/docs/components/accordion) is opened, it includes a `data-state="open"` attribute.
## [Styling with CSS](https://www.radix-ui.com/primitives/docs/guides/styling#styling-with-css)
### [Styling a part](https://www.radix-ui.com/primitives/docs/guides/styling#styling-a-part)
You can style a component part by targeting the `className` that you provide.

```

import * as React from "react";

import { Accordion } from "radix-ui";

import "./styles.css";

export const AccordionDemo = () => (

	<Accordion.Root>

		<Accordion.Item className="AccordionItem" value="item-1" />

		{/* … */}

	</Accordion.Root>

);

```

### [Styling a state](https://www.radix-ui.com/primitives/docs/guides/styling#styling-a-state)
You can style a component state by targeting its `data-state` attribute.

```

.AccordionItem {

	border-bottom: 1px solid gainsboro;

}

.AccordionItem[data-state="open"] {

	border-bottom-width: 2px;

}

```

## [Styling with CSS-in-JS](https://www.radix-ui.com/primitives/docs/guides/styling#styling-with-css-in-js)
The examples below are using
### [Styling a part](https://www.radix-ui.com/primitives/docs/guides/styling#styling-a-part-1)
Most CSS-in-JS libraries export a function for passing components and their styles. You can provide the Radix primitive component directly.

```

import * as React from "react";

import { Accordion } from "radix-ui";

import styled from "styled-components";

const StyledItem = styled(Accordion.Item)`
  border-bottom: 1px solid gainsboro;
`;

export const AccordionDemo = () => (

	<Accordion.Root>

		<StyledItem value="item-1" />

		{/* … */}

	</Accordion.Root>

);

```

### [Styling a state](https://www.radix-ui.com/primitives/docs/guides/styling#styling-a-state-1)
You can style a component state by targeting its `data-state` attribute.

```

import { Accordion } from "radix-ui";

import styled from "styled-components";

const StyledItem = styled(Accordion.Item)`
	border-bottom: 1px solid gainsboro;

	&[data-state="open"] {
		border-bottom-width: 2px;
	}
`;

```

## [Extending a primitive](https://www.radix-ui.com/primitives/docs/guides/styling#extending-a-primitive)
Extending a primitive is done the same way you extend any React component.

```

import * as React from "react";

import { Accordion as AccordionPrimitive } from "radix-ui";

const AccordionItem = React.forwardRef<

	React.ElementRef<typeof AccordionPrimitive.Item>,

	React.ComponentPropsWithoutRef<typeof AccordionPrimitive.Item>

>((props, forwardedRef) => (

	<AccordionPrimitive.Item {...props} ref={forwardedRef} />

));

AccordionItem.displayName = "AccordionItem";

```

## [Summary](https://www.radix-ui.com/primitives/docs/guides/styling#summary)
Radix Primitives were designed to encapsulate accessibility concerns and other complex functionalities, while ensuring you retain complete control over styling.
For convenience, stateful components include a `data-state` attribute.
#### Quick nav
  * [Styling overview](https://www.radix-ui.com/primitives/docs/guides/styling#styling-overview)
  * [Functional styles](https://www.radix-ui.com/primitives/docs/guides/styling#functional-styles)
  * [Classes](https://www.radix-ui.com/primitives/docs/guides/styling#classes)
  * [Data attributes](https://www.radix-ui.com/primitives/docs/guides/styling#data-attributes)
  * [Styling with CSS](https://www.radix-ui.com/primitives/docs/guides/styling#styling-with-css)
  * [Styling a part](https://www.radix-ui.com/primitives/docs/guides/styling#styling-a-part)
  * [Styling a state](https://www.radix-ui.com/primitives/docs/guides/styling#styling-a-state)
  * [Styling with CSS-in-JS](https://www.radix-ui.com/primitives/docs/guides/styling#styling-with-css-in-js)
  * [Styling a part](https://www.radix-ui.com/primitives/docs/guides/styling#styling-a-part-1)
  * [Styling a state](https://www.radix-ui.com/primitives/docs/guides/styling#styling-a-state-1)
  * [Extending a primitive](https://www.radix-ui.com/primitives/docs/guides/styling#extending-a-primitive)
  * [Summary](https://www.radix-ui.com/primitives/docs/guides/styling#summary)

Previous[Releases](https://www.radix-ui.com/primitives/docs/overview/releases)
Next[Animation](https://www.radix-ui.com/primitives/docs/guides/animation)
