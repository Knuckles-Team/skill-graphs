[Skip to content](https://mui.com/material-ui/customization/how-to-customize/#main-content)
[](https://mui.com/)
Search…`Ctrl+K`3
# How to customize
Learn how to customize Material UI components by taking advantage of different strategies for specific use cases.
![ads via Carbon](https://ad.double-click.net/ddm/trackimp/N718679.452584BUYSELLADS.COM/B29332811.421611897;dc_trk_aid=613858979;dc_trk_cid=235700574;ord=177300365;dc_lat=;dc_rdid=;tag_for_child_directed_treatment=;tfua=;gdpr=$;gdpr_consent=$;ltd=;dc_tdv=1)
Material UI provides several different ways to customize a component's styles. Your specific context will determine which one is ideal. From narrowest to broadest use case, here are the options:
  1. [One-off customization](https://mui.com/material-ui/customization/how-to-customize/#1-one-off-customization)
  2. [Reusable component](https://mui.com/material-ui/customization/how-to-customize/#2-reusable-component)
  3. [Global theme overrides](https://mui.com/material-ui/customization/how-to-customize/#3-global-theme-overrides)
  4. [Global CSS override](https://mui.com/material-ui/customization/how-to-customize/#4-global-css-override)


## [1. One-off customization](https://mui.com/material-ui/customization/how-to-customize/#1-one-off-customization)
To change the styles of _one single instance_ of a component, you can use one of the following options:
### [The `sx` prop](https://mui.com/material-ui/customization/how-to-customize/#the-sx-prop)
The [`sx` prop](https://mui.com/system/getting-started/the-sx-prop/) is the best option for adding style overrides to a single instance of a component in most cases. It can be used with all Material UI components.
JSTS
Expand code
Copy(or Ctrl + C)
```
<Slider defaultValue={30} sx={{ width: 300, color: 'success.main' }} />

```
<Slider defaultValue={30} sx={{ width: 300, color: 'success.main' }} />
Press `Enter` to start editing
### [Overriding nested component styles](https://mui.com/material-ui/customization/how-to-customize/#overriding-nested-component-styles)
To customize a specific part of a component, you can use the class name provided by Material UI inside the `sx` prop. As an example, let's say you want to change the `Slider` component's thumb from a circle to a square.
First, use your browser's dev tools to identify the class for the component slot you want to override.
The styles injected into the DOM by Material UI rely on class names that all [follow a standard pattern](https://v6.mui.com/system/styles/advanced/#class-names): `[hash]-Mui[Component name]-[name of the slot]`.
In this case, the styles are applied with `.css-ae2u5c-MuiSlider-thumb` but you only really need to target the `.MuiSlider-thumb`, where `Slider` is the component and `thumb` is the slot. Use this class name to write a CSS selector within the `sx` prop (`& .MuiSlider-thumb`), and add your overrides.
![dev-tools](https://mui.com/static/images/customization/dev-tools.png)
JSTS
Expand code
Copy(or Ctrl + C)
```
<Slider
  defaultValue={30}
  sx={{
    width: 300,
    color: 'success.main',
    '& .MuiSlider-thumb': {
      borderRadius: '1px',
    },
  }}
/>

```
<Slider defaultValue={30} sx={{ width: 300, color: 'success.main', '& .MuiSlider-thumb': { borderRadius: '1px', }, }} />
Press `Enter` to start editing
These class names can't be used as CSS selectors because they are unstable.
### [Overriding styles with class names](https://mui.com/material-ui/customization/how-to-customize/#overriding-styles-with-class-names)
If you want to override a component's styles using custom classes, you can use the `className` prop, available on each component. To override the styles of a specific part of the component, use the global classes provided by Material UI, as described in the previous section **"Overriding nested component styles"** under the [`sx` prop section](https://mui.com/material-ui/customization/how-to-customize/#the-sx-prop).
Visit the [Style library interoperability](https://mui.com/material-ui/integrations/interoperability/) guide to find examples of this approach using different styling libraries.
### [State classes](https://mui.com/material-ui/customization/how-to-customize/#state-classes)
States like _hover_ , _focus_ , _disabled_ and _selected_ , are styled with a higher CSS specificity. To customize them, you'll need to **increase specificity**.
Here is an example with the _disabled_ state and the `Button` component using a pseudo-class (`:disabled`):
```
.Button {
  color: black;
}

/* Increase the specificity */
.Button:disabled {
  color: white;
}

```
CopyCopied(or Ctrl + C)
```
<Button disabled className="Button">

```
CopyCopied(or Ctrl + C)
You can't always use a CSS pseudo-class, as the state doesn't exist in the web specification. Let's take the `MenuItem` component and its _selected_ state as an example. In this situation, you can use Material UI's **state classes** , which act just like CSS pseudo-classes. Target the `.Mui-selected` global class name to customize the special state of the `MenuItem` component:
```
.MenuItem {
  color: black;
}

/* Increase the specificity */
.MenuItem.Mui-selected {
  color: blue;
}

```
CopyCopied(or Ctrl + C)
```
<MenuItem selected className="MenuItem">

```
CopyCopied(or Ctrl + C)
If you'd like to learn more about this topic, we recommend checking out
#### Why do I need to increase specificity to override one component state?
CSS pseudo-classes have a high level of specificity. For consistency with native elements, Material UI's state classes have the same level of specificity as CSS pseudo-classes, making it possible to target an individual component's state.
#### What custom state classes are available in Material UI?
You can rely on the following [global class names](https://v6.mui.com/system/styles/advanced/#class-names) generated by Material UI:
State | Global class name
---|---
active | `.Mui-active`
checked | `.Mui-checked`
completed | `.Mui-completed`
disabled | `.Mui-disabled`
error | `.Mui-error`
expanded | `.Mui-expanded`
focus visible | `.Mui-focusVisible`
focused | `.Mui-focused`
readOnly | `.Mui-readOnly`
required | `.Mui-required`
selected | `.Mui-selected`
Never apply styles directly to state class names. This will impact all components with unclear side-effects. Always target a state class together with a component.
```
/* ❌ NOT OK */
.Mui-error {
  color: red;
}

/* ✅ OK */
.MuiOutlinedInput-root.Mui-error {
  color: red;
}

```
CopyCopied(or Ctrl + C)
## [2. Reusable component](https://mui.com/material-ui/customization/how-to-customize/#2-reusable-component)
To reuse the same overrides in different locations across your application, create a reusable component using the [`styled()`](https://mui.com/system/styled/) utility:
JSTS
Collapse code
Copy(or Ctrl + C)
```
import Slider, { SliderProps } from '@mui/material/Slider';
import { alpha, styled } from '@mui/material/styles';

const SuccessSlider = styled(Slider)<SliderProps>(({ theme }) => ({
  width: 300,
  color: theme.palette.success.main,
  '& .MuiSlider-thumb': {
    '&:hover, &.Mui-focusVisible': {
      boxShadow: `0px 0px 0px 8px ${alpha(theme.palette.success.main, 0.16)}`,
    },
    '&.Mui-active': {
      boxShadow: `0px 0px 0px 14px ${alpha(theme.palette.success.main, 0.16)}`,
    },
  },
}));

export default function StyledCustomization() {
  return <SuccessSlider defaultValue={30} />;
}

```
import Slider, { SliderProps } from '@mui/material/Slider'; import { alpha, styled } from '@mui/material/styles'; const SuccessSlider = styled(Slider)<SliderProps>(({ theme }) => ({ width: 300, color: theme.palette.success.main, '& .MuiSlider-thumb': { '&:hover, &.Mui-focusVisible': { boxShadow: `0px 0px 0px 8px ${alpha(theme.palette.success.main, 0.16)}`, }, '&.Mui-active': { boxShadow: `0px 0px 0px 14px ${alpha(theme.palette.success.main, 0.16)}`, }, }, })); export default function StyledCustomization() { return <SuccessSlider defaultValue={30} />; }
Press `Enter` to start editing
### [Dynamic overrides](https://mui.com/material-ui/customization/how-to-customize/#dynamic-overrides)
The `styled()` utility lets you add dynamic styles based on a component's props. You can do this with **dynamic CSS** or **CSS variables**.
#### Dynamic CSS
If you are using TypeScript, you will need to update the prop's types of the new component.
Success
JSTS
Show code
```
import * as React from 'react';
import { styled } from '@mui/material/styles';
import Slider, { SliderProps } from '@mui/material/Slider';

interface StyledSliderProps extends SliderProps {
  success?: boolean;
}

const StyledSlider = styled(Slider, {
  shouldForwardProp: (prop) => prop !== 'success',
})<StyledSliderProps>(({ success, theme }) => ({
  ...(success &&
    {
      // the overrides added when the new prop is used
    }),
}));

```
CopyCopied(or Ctrl + C)
#### CSS variables
Success
JSTS
Expand code
Copy(or Ctrl + C)
```
<React.Fragment>
  <FormControlLabel
    control={
      <Switch
        checked={vars === successVars}
        onChange={handleChange}
        color="primary"
        value="dynamic-class-name"
      />
    }
    label="Success"
  />
  <CustomSlider style={vars} defaultValue={30} sx={{ mt: 1 }} />
</React.Fragment>

```
<React.Fragment> <FormControlLabel control={ <Switch checked={vars === successVars} onChange={handleChange} color="primary" value="dynamic-class-name" /> } label="Success" /> <CustomSlider style={vars} defaultValue={30} sx={{ mt: 1 }} /> </React.Fragment>
Press `Enter` to start editing
## [3. Global theme overrides](https://mui.com/material-ui/customization/how-to-customize/#3-global-theme-overrides)
Material UI provides theme tools for managing style consistency between all components across your user interface. Visit the [Component theming customization](https://mui.com/material-ui/customization/theme-components/) page for more details.
## [4. Global CSS override](https://mui.com/material-ui/customization/how-to-customize/#4-global-css-override)
To add global baseline styles for some of the HTML elements, use the `GlobalStyles` component. Here is an example of how you can override styles for the `h1` elements:
# Grey h1 element
JSTS
Expand code
Copy(or Ctrl + C)
```
<React.Fragment>
  <GlobalStyles styles={{ h1: { color: 'grey' } }} />
  <h1>Grey h1 element</h1>
</React.Fragment>

```
<React.Fragment> <GlobalStyles styles={{ h1: { color: 'grey' } }} /> <h1>Grey h1 element</h1> </React.Fragment>
Press `Enter` to start editing
The `styles` prop in the `GlobalStyles` component supports a callback in case you need to access the theme.
# Grey h1 element
JSTS
Expand code
Copy(or Ctrl + C)
```
<React.Fragment>
  <GlobalStyles
    styles={(theme) => ({
      h1: { color: theme.palette.primary.main },
    })}
  />
  <h1>Grey h1 element</h1>
</React.Fragment>

```
<React.Fragment> <GlobalStyles styles={(theme) => ({ h1: { color: theme.palette.primary.main }, })} /> <h1>Grey h1 element</h1> </React.Fragment>
Press `Enter` to start editing
If you are already using the [CssBaseline](https://mui.com/material-ui/react-css-baseline/) component for setting baseline styles, you can also add these global styles as overrides for this component. Here is how you can achieve the same by using this approach.
# Grey h1 element
JSTS
Expand code
Copy(or Ctrl + C)
```
<ThemeProvider theme={theme}>
  <CssBaseline />
  <h1>Grey h1 element</h1>
</ThemeProvider>

```
<ThemeProvider theme={theme}> <CssBaseline /> <h1>Grey h1 element</h1> </ThemeProvider>
Press `Enter` to start editing
The `styleOverrides` key in the `MuiCssBaseline` component slot also supports callback from which you can access the theme. Here is how you can achieve the same by using this approach.
# h1 element
JSTS
Expand code
Copy(or Ctrl + C)
```
<ThemeProvider theme={theme}>
  <CssBaseline />
  <h1>h1 element</h1>
</ThemeProvider>

```
<ThemeProvider theme={theme}> <CssBaseline /> <h1>h1 element</h1> </ThemeProvider>
Press `Enter` to start editing
It is a good practice to hoist the `<GlobalStyles />` to a static constant, to avoid rerendering. This will ensure that the `<style>` tag generated would not recalculate on each render.
```
 import * as React from 'react';
 import GlobalStyles from '@mui/material/GlobalStyles';

+const inputGlobalStyles = <GlobalStyles styles={...} />;

 function Input(props) {
   return (
     <React.Fragment>
-      <GlobalStyles styles={...} />
+      {inputGlobalStyles}
       <input {...props} />
     </React.Fragment>
   )
 }

```
CopyCopied(or Ctrl + C)
## [API](https://mui.com/material-ui/customization/how-to-customize/#api)
See the documentation below for a complete reference to all of the props and classes available to the components mentioned here.
  * [`<GlobalStyles />`](https://mui.com/material-ui/api/global-styles/)


Was this page helpful?
* * *
[](https://mui.com/material-ui/api/zoom/)[Overriding component structure](https://mui.com/material-ui/customization/overriding-component-structure/)
* * *
[](https://mui.com/)
•
[Blog ](https://mui.com/blog/)
•
[Store ](https://mui.com/store/)
[](https://mui.com/r/discord/ "Discord")[](https://mui.com/feed/blog/rss.xml "RSS Feed")
Contents
  * [1. One-off customization](https://mui.com/material-ui/customization/how-to-customize/#1-one-off-customization)
    * [The sx prop](https://mui.com/material-ui/customization/how-to-customize/#the-sx-prop)
    * [Overriding nested component styles](https://mui.com/material-ui/customization/how-to-customize/#overriding-nested-component-styles)
    * [Overriding styles with class names](https://mui.com/material-ui/customization/how-to-customize/#overriding-styles-with-class-names)
    * [State classes](https://mui.com/material-ui/customization/how-to-customize/#state-classes)
  * [2. Reusable component](https://mui.com/material-ui/customization/how-to-customize/#2-reusable-component)
    * [Dynamic overrides](https://mui.com/material-ui/customization/how-to-customize/#dynamic-overrides)
  * [3. Global theme overrides](https://mui.com/material-ui/customization/how-to-customize/#3-global-theme-overrides)
  * [4. Global CSS override](https://mui.com/material-ui/customization/how-to-customize/#4-global-css-override)
  * [API](https://mui.com/material-ui/customization/how-to-customize/#api)


[Become a Diamond sponsor](https://mui.com/material-ui/discover-more/backers/#diamond-sponsors)
###### Cookie Preferences
We use cookies to understand site usage and improve our content. This includes third-party analytics.
Allow analyticsEssential only
[](https://mui.com/)
Material UIv7.3.9
  * [](https://mui.com/material-ui/getting-started/)
  * [](https://mui.com/material-ui/all-components/)
  * [](https://mui.com/material-ui/api/accordion/)
  * [](https://mui.com/material-ui/customization/how-to-customize/)
    * [How to customize](https://mui.com/material-ui/customization/how-to-customize/)
    * [Overriding component structure](https://mui.com/material-ui/customization/overriding-component-structure/)
    * [Dark mode](https://mui.com/material-ui/customization/dark-mode/)
    * [Color](https://mui.com/material-ui/customization/color/)
    * [Right-to-left](https://mui.com/material-ui/customization/right-to-left/)
    * [Shadow DOM](https://mui.com/material-ui/customization/shadow-dom/)
    * Theme
      * [Default theme viewer](https://mui.com/material-ui/customization/default-theme/)
      * [Customizing the theme](https://mui.com/material-ui/customization/theming/)
      * [Creating themed components](https://mui.com/material-ui/customization/creating-themed-components/)
      * [Components](https://mui.com/material-ui/customization/theme-components/)
    * Tokens
      * [Palette](https://mui.com/material-ui/customization/palette/)
      * [Typography](https://mui.com/material-ui/customization/typography/)
      * [Spacing](https://mui.com/material-ui/customization/spacing/)
      * [Shape](https://mui.com/material-ui/customization/shape/)
      * [Breakpoints](https://mui.com/material-ui/customization/breakpoints/)
      * [Container queriesNew](https://mui.com/material-ui/customization/container-queries/)
      * [Density](https://mui.com/material-ui/customization/density/)
      * [z-index](https://mui.com/material-ui/customization/z-index/)
      * [Transitions](https://mui.com/material-ui/customization/transitions/)
    * Css variables
New
      * [Overview](https://mui.com/material-ui/customization/css-theme-variables/overview/)
      * [Basic usage](https://mui.com/material-ui/customization/css-theme-variables/usage/)
      * [Native color](https://mui.com/material-ui/customization/css-theme-variables/native-color/)
      * [Advanced configuration](https://mui.com/material-ui/customization/css-theme-variables/configuration/)
    * Styles
      * [Cascade layersNew](https://mui.com/material-ui/customization/css-layers/)
  * [](https://mui.com/material-ui/guides/building-extensible-themes/)
  * [](https://mui.com/material-ui/integrations/tailwindcss/tailwindcss-v4/)
  * [](https://mui.com/material-ui/experimental-api/classname-generator/)
  * [](https://mui.com/material-ui/migration/upgrade-to-grid-v2/)
  * [](https://mui.com/material-ui/discover-more/showcase/)
  * [](https://mui.com/material-ui/design-resources/material-ui-for-figma/)
  * [](https://mui.com/store/%3Futm_source=docs&utm_medium=referral&utm_campaign=sidenav/)
