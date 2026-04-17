[Skip to content](https://mui.com/material-ui/getting-started/installation/#main-content)
[](https://mui.com/)
Search…`Ctrl+K`3
# Installation
Install Material UI, the world's most popular React UI framework.
## [Default installation](https://mui.com/material-ui/getting-started/installation/#default-installation)
Run one of the following commands to add Material UI to your project:
npmpnpmyarn
Copy(or Ctrl + C)
```
npm install @mui/material @emotion/react @emotion/styled
```

### [Peer dependencies](https://mui.com/material-ui/getting-started/installation/#peer-dependencies)
Please note that
```
"peerDependencies": {
  "react": "^17.0.0 || ^18.0.0 || ^19.0.0",
  "react-dom": "^17.0.0 || ^18.0.0 || ^19.0.0"
},

```
CopyCopied(or Ctrl + C)
### [React 18 and below](https://mui.com/material-ui/getting-started/installation/#react-18-and-below)
If you are using React 18 or below, you need to set up a resolution of `react-is` package to the same version as the `react` you are using.
For example, if you are using `react@18.3.1`, do the following steps:
  1. Install `react-is@18.3.1`.


npmpnpmyarn
Copy(or Ctrl + C)
```
npm install react-is@18.3.1
```

  1. Set the resolutions or overrides in the `package.json`.


npmpnpmyarn
Copy(or Ctrl + C)
```
{
  …
  "overrides": {
    "react-is": "^18.3.1"
  }
}
```

#### Why is this needed?
Material UI uses `react-is@19`, which changed how React elements are identified.
If you're on React 18 or below, mismatched versions of `react-is` can cause runtime errors in prop type checks. Forcing `react-is` to match your React version prevents these errors.
## [With styled-components](https://mui.com/material-ui/getting-started/installation/#with-styled-components)
Material UI uses
npmpnpmyarn
Copy(or Ctrl + C)
```
npm install @mui/material @mui/styled-engine-sc styled-components
```

Next, follow the [styled-components how-to guide](https://mui.com/material-ui/integrations/styled-components/) to properly configure your bundler to support `@mui/styled-engine-sc`.
As of late 2021, **not compatible** with server-rendered Material UI projects. This is because `babel-plugin-styled-components` isn't able to work with the `styled()` utility inside `@mui` packages. See
We **strongly recommend** using Emotion for SSR projects.
## [Roboto font](https://mui.com/material-ui/getting-started/installation/#roboto-font)
Material UI uses the
npmpnpmyarn
Copy(or Ctrl + C)
```
npm install @fontsource/roboto
```

Then you can import it in your entry point like this:
```
import '@fontsource/roboto/300.css';
import '@fontsource/roboto/400.css';
import '@fontsource/roboto/500.css';
import '@fontsource/roboto/700.css';

```
CopyCopied(or Ctrl + C)
Fontsource can be configured to load specific subsets, weights and styles. Material UI's default typography configuration relies only on the 300, 400, 500, and 700 font weights.
### [Google Web Fonts](https://mui.com/material-ui/getting-started/installation/#google-web-fonts)
To install Roboto through the Google Web Fonts CDN, add the following code inside your project's `<head />` tag:
```
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link
  rel="stylesheet"
  href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap"
/>

```
CopyCopied(or Ctrl + C)
## [Icons](https://mui.com/material-ui/getting-started/installation/#icons)
To use the [font Icon component](https://mui.com/material-ui/icons/#icon-font-icons) or the prebuilt SVG Material Icons (such as those found in the [icon demos](https://mui.com/material-ui/icons/)), you must first install the
npmpnpmyarn
Copy(or Ctrl + C)
```
npm install @mui/icons-material
```

### [Google Web Fonts](https://mui.com/material-ui/getting-started/installation/#google-web-fonts-2)
To install the Material Icons font in your project using the Google Web Fonts CDN, add the following code snippet inside your project's `<head />` tag:
To use the font `Icon` component, you must first add the [some instructions](https://mui.com/material-ui/icons/#icon-font-icons) on how to do so. For instance, via Google Web Fonts:
```
<link
  rel="stylesheet"
  href="https://fonts.googleapis.com/icon?family=Material+Icons"
/>

```
CopyCopied(or Ctrl + C)
## [CDN](https://mui.com/material-ui/getting-started/installation/#cdn)
You can start using Material UI right away with minimal front-end infrastructure by installing it via CDN, which is a great option for rapid prototyping.
Follow
We do _not_ recommend using this approach in production. It requires the client to download the entire library—regardless of which components are actually used—which negatively impacts performance and bandwidth utilization.
Was this page helpful?
* * *
[](https://mui.com/material-ui/getting-started/)[Usage](https://mui.com/material-ui/getting-started/usage/)
* * *
[](https://mui.com/)
•
[Blog ](https://mui.com/blog/)
•
[Store ](https://mui.com/store/)
[](https://mui.com/r/discord/ "Discord")[](https://mui.com/feed/blog/rss.xml "RSS Feed")
Contents
  * [Default installation](https://mui.com/material-ui/getting-started/installation/#default-installation)
    * [Peer dependencies](https://mui.com/material-ui/getting-started/installation/#peer-dependencies)
    * [React 18 and below](https://mui.com/material-ui/getting-started/installation/#react-18-and-below)
  * [With styled-components](https://mui.com/material-ui/getting-started/installation/#with-styled-components)
  * [Roboto font](https://mui.com/material-ui/getting-started/installation/#roboto-font)
    * [Google Web Fonts](https://mui.com/material-ui/getting-started/installation/#google-web-fonts)
  * [Icons](https://mui.com/material-ui/getting-started/installation/#icons)
    * [Google Web Fonts](https://mui.com/material-ui/getting-started/installation/#google-web-fonts-2)
  * [CDN](https://mui.com/material-ui/getting-started/installation/#cdn)


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
