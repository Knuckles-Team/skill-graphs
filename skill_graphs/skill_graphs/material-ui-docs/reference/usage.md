[Skip to content](https://mui.com/material-ui/getting-started/usage/#main-content)
[](https://mui.com/)
Search…`Ctrl+K`3
# Usage
Learn the basics of working with Material UI components.
## [Quickstart](https://mui.com/material-ui/getting-started/usage/#quickstart)
After [installation](https://mui.com/material-ui/getting-started/installation/), you can import any Material UI component and start playing around. For example, try changing the `variant` on the [Button](https://mui.com/material-ui/react-button/) to `outlined` to see how the style changes:
Hello world
JSTS
Collapse code
Copy(or Ctrl + C)
```
import Button from '@mui/material/Button';

export default function ButtonUsage() {
  return <Button variant="contained">Hello world</Button>;
}

```
import Button from '@mui/material/Button'; export default function ButtonUsage() { return <Button variant="contained">Hello world</Button>; }
Press `Enter` to start editing
## [Globals](https://mui.com/material-ui/getting-started/usage/#globals)
Since Material UI components are built to function in isolation, they don't require any kind of globally scoped styles. For a better user experience and developer experience, we recommend adding the following globals to your app.
### [Responsive meta tag](https://mui.com/material-ui/getting-started/usage/#responsive-meta-tag)
Material UI is a _mobile-first_ component library—we write code for mobile devices first, and then scale up the components as necessary using CSS media queries.
To ensure proper rendering and touch zooming for all devices, add the responsive viewport meta tag to your `<head>` element:
```
<meta name="viewport" content="initial-scale=1, width=device-width" />

```
CopyCopied(or Ctrl + C)
### [CssBaseline](https://mui.com/material-ui/getting-started/usage/#cssbaseline)
Material UI provides an optional [CssBaseline](https://mui.com/material-ui/react-css-baseline/) component. It fixes some inconsistencies across browsers and devices while providing resets that are better tailored to fit Material UI than alternative global style sheets like
### [Default font](https://mui.com/material-ui/getting-started/usage/#default-font)
Material UI uses the Roboto font by default. See [Installation—Roboto font](https://mui.com/material-ui/getting-started/installation/#roboto-font) for complete details.
Was this page helpful?
* * *
[](https://mui.com/material-ui/getting-started/installation/)[MCP](https://mui.com/material-ui/getting-started/mcp/)
* * *
[](https://mui.com/)
•
[Blog ](https://mui.com/blog/)
•
[Store ](https://mui.com/store/)
[](https://mui.com/r/discord/ "Discord")[](https://mui.com/feed/blog/rss.xml "RSS Feed")
Contents
  * [Quickstart](https://mui.com/material-ui/getting-started/usage/#quickstart)
  * [Globals](https://mui.com/material-ui/getting-started/usage/#globals)
    * [Responsive meta tag](https://mui.com/material-ui/getting-started/usage/#responsive-meta-tag)
    * [CssBaseline](https://mui.com/material-ui/getting-started/usage/#cssbaseline)
    * [Default font](https://mui.com/material-ui/getting-started/usage/#default-font)


[Become a Diamond sponsor](https://mui.com/material-ui/discover-more/backers/#diamond-sponsors)
###### Cookie Preferences
We use cookies to understand site usage and improve our content. This includes third-party analytics.
Allow analyticsEssential only
[](https://mui.com/)
Material UIv7.3.9
  * [](https://mui.com/material-ui/getting-started/)
    * [Overview](https://mui.com/material-ui/getting-started/)
    * [Installation](https://mui.com/material-ui/getting-started/installation/)
    * [Usage](https://mui.com/material-ui/getting-started/usage/)
    * [MCPNew](https://mui.com/material-ui/getting-started/mcp/)
    * [llms.txtNew](https://mui.com/material-ui/llms.txt)
    * [Example projects](https://mui.com/material-ui/getting-started/example-projects/)
    * [Templates](https://mui.com/material-ui/getting-started/templates/)
    * [Learn](https://mui.com/material-ui/getting-started/learn/)
    * [Design resources](https://mui.com/material-ui/getting-started/design-resources/)
    * [FAQs](https://mui.com/material-ui/getting-started/faq/)
    * [Supported components](https://mui.com/material-ui/getting-started/supported-components/)
    * [Supported platforms](https://mui.com/material-ui/getting-started/supported-platforms/)
    * [Support](https://mui.com/material-ui/getting-started/support/)
  * [](https://mui.com/material-ui/all-components/)
  * [](https://mui.com/material-ui/api/accordion/)
  * [](https://mui.com/material-ui/customization/how-to-customize/)
  * [](https://mui.com/material-ui/guides/building-extensible-themes/)
  * [](https://mui.com/material-ui/integrations/tailwindcss/tailwindcss-v4/)
  * [](https://mui.com/material-ui/experimental-api/classname-generator/)
  * [](https://mui.com/material-ui/migration/upgrade-to-grid-v2/)
  * [](https://mui.com/material-ui/discover-more/showcase/)
  * [](https://mui.com/material-ui/design-resources/material-ui-for-figma/)
  * [](https://mui.com/store/%3Futm_source=docs&utm_medium=referral&utm_campaign=sidenav/)
