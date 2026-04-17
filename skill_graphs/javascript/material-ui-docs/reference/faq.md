[Skip to content](https://mui.com/material-ui/getting-started/faq/#main-content)
[](https://mui.com/)
Search…`Ctrl+K`3
# Frequently Asked Questions
Stuck on a particular problem? Check some of these common gotchas first in the FAQ.
If you still can't find what you're looking for, you can refer to our [support page](https://mui.com/material-ui/getting-started/support/).
## [MUI is an awesome organization. How can I support it?](https://mui.com/material-ui/getting-started/faq/#mui-is-an-awesome-organization-how-can-i-support-it)
There are many ways to support us:
  * **Spread the word**. Evangelize MUI's products by [linking to mui.com](https://mui.com/) on your website—every backlink matters. Follow us on
  * **Give us feedback**. Tell us what is going well or where there is improvement opportunities. Please upvote (👍) the issues that you are the most interested in seeing solved.
  * **Help new users**. You can answer questions on
  * **Make changes happen**.
    * Edit the documentation. At the bottom of every page, you can find an "Edit this page" button.
    * Report bugs or missing features by
    * Review and comment on existing
  * **Support us financially on**. If you use Material UI in a commercial project and would like to support its continued development by becoming a Sponsor, or in a side or hobby project and would like to become a Backer, you can do so through Open Collective. All funds donated are managed transparently, and Sponsors receive recognition in the README and on the homepage.


## [Why do the fixed positioned elements move when a modal is opened?](https://mui.com/material-ui/getting-started/faq/#why-do-the-fixed-positioned-elements-move-when-a-modal-is-opened)
Scrolling is blocked as soon as a modal is opened. This prevents interacting with the background when the modal should be the only interactive content. However, removing the scrollbar can make your **fixed positioned elements** move. In this situation, you can apply a global `.mui-fixed` class name to tell Material UI to handle those elements.
## [How can I disable the ripple effect globally?](https://mui.com/material-ui/getting-started/faq/#how-can-i-disable-the-ripple-effect-globally)
The ripple effect is exclusively coming from the `BaseButton` component. You can disable the ripple effect globally by providing the following in your theme:
```
import { createTheme } from '@mui/material';

const theme = createTheme({
  components: {
    // Name of the component ⚛️
    MuiButtonBase: {
      defaultProps: {
        // The props to apply
        disableRipple: true, // No more ripple, on the whole application 💣!
      },
    },
  },
});

```
CopyCopied(or Ctrl + C)
## [How can I disable transitions globally?](https://mui.com/material-ui/getting-started/faq/#how-can-i-disable-transitions-globally)
Material UI uses the same theme helper for creating all its transitions. Therefore you can disable all transitions by overriding the helper in your theme:
```
import { createTheme } from '@mui/material';

const theme = createTheme({
  transitions: {
    // So `transition: none;` gets applied everywhere
    create: () => 'none',
  },
});

```
CopyCopied(or Ctrl + C)
It can be useful to disable transitions during visual testing or to improve performance on low-end devices.
You can go one step further by disabling all transitions and animations effects:
```
import { createTheme } from '@mui/material';

const theme = createTheme({
  components: {
    // Name of the component ⚛️
    MuiCssBaseline: {
      styleOverrides: {
        '*, *::before, *::after': {
          transition: 'none !important',
          animation: 'none !important',
        },
      },
    },
  },
});

```
CopyCopied(or Ctrl + C)
Notice that the usage of `CssBaseline` is required for the above approach to work. If you choose not to use it, you can still disable transitions and animations by including these CSS rules:
```
*,
*::before,
*::after {
  transition: 'none !important';
  animation: 'none !important';
}

```
CopyCopied(or Ctrl + C)
## [Do I have to use Emotion to style my app?](https://mui.com/material-ui/getting-started/faq/#do-i-have-to-use-emotion-to-style-my-app)
No, it's not required. But if you are using the default styled engine (`@mui/styled-engine`) the Emotion dependency comes built in, so carries no additional bundle size overhead.
Perhaps, however, you're adding some Material UI components to an app that already uses another styling solution, or are already familiar with a different API, and don't want to learn a new one? In that case, head over to the [Style library interoperability](https://mui.com/material-ui/integrations/interoperability/) section to learn how to restyle Material UI components with alternative style libraries.
## [When should I use inline-style vs. CSS?](https://mui.com/material-ui/getting-started/faq/#when-should-i-use-inline-style-vs-css)
As a rule of thumb, only use inline-styles for dynamic style properties. The CSS alternative provides more advantages, such as:
  * auto-prefixing
  * better debugging
  * media queries
  * keyframes


## [How do I use react-router?](https://mui.com/material-ui/getting-started/faq/#how-do-i-use-react-router)
Visit the guide about [integration with third-party routing libraries](https://mui.com/material-ui/integrations/routing/), like react-router or Next.js, for more details.
## [How can I access the DOM element?](https://mui.com/material-ui/getting-started/faq/#how-can-i-access-the-dom-element)
All Material UI components that should render something in the DOM forward their ref to the underlying DOM component. This means that you can get DOM elements by reading the ref attached to Material UI components:
```
// or a ref setter function
const ref = React.createRef();
// render
<Button ref={ref} />;
// usage
const element = ref.current;

```
CopyCopied(or Ctrl + C)
If you're not sure if the Material UI component in question forwards its ref you can check the API documentation under "Props." You should find the message below, like in the [Button API](https://mui.com/material-ui/api/button/#props).
> The ref is forwarded to the root element.
## [My App doesn't render correctly on the server](https://mui.com/material-ui/getting-started/faq/#my-app-doesnt-render-correctly-on-the-server)
If it doesn't work, in 99% of cases it's a configuration issue. A missing property, a wrong call order, or a missing component – server-side rendering is strict about configuration.
The best way to find out what's wrong is to compare your project to an **already working setup**. Check out the [reference implementations](https://mui.com/material-ui/guides/server-rendering/#reference-implementations), bit by bit.
## [Why are the colors I am seeing different from what I see here?](https://mui.com/material-ui/getting-started/faq/#why-are-the-colors-i-am-seeing-different-from-what-i-see-here)
The documentation site is using a custom theme. Hence, the color palette is different from the default theme that Material UI ships. Please refer to [this page](https://mui.com/material-ui/customization/theming/) to learn about theme customization.
## [Why does component X require a DOM node in a prop instead of a ref object?](https://mui.com/material-ui/getting-started/faq/#why-does-component-x-require-a-dom-node-in-a-prop-instead-of-a-ref-object)
Components like the [Portal](https://mui.com/material-ui/api/portal/#props) or [Popper](https://mui.com/material-ui/api/popper/#props) require a DOM node in the `container` or `anchorEl` prop respectively. It seems convenient to simply pass a ref object in those props and let Material UI access the current value.
This works in a simple scenario:
```
function App() {
  const container = React.useRef(null);

  return (
    <div className="App">
      <Portal container={container}>
        <span>portaled children</span>
      </Portal>
      <div ref={container} />
    </div>
  );
}

```
CopyCopied(or Ctrl + C)
where `Portal` would only mount the children into the container when `container.current` is available. Here is a naive implementation of Portal:
```
function Portal({ children, container }) {
  const [node, setNode] = React.useState(null);

  React.useEffect(() => {
    setNode(container.current);
  }, [container]);

  if (node === null) {
    return null;
  }
  return ReactDOM.createPortal(children, node);
}

```
CopyCopied(or Ctrl + C)
With this simple heuristic `Portal` might re-render after it mounts because refs are up-to-date before any effects run. However, just because a ref is up-to-date doesn't mean it points to a defined instance. If the ref is attached to a ref forwarding component it is not clear when the DOM node will be available. In the example above, the `Portal` would run an effect once, but might not re-render because `ref.current` is still `null`. This is especially apparent for React.lazy components in Suspense. The above implementation could also not account for a change in the DOM node.
This is why a prop is required to the actual DOM node so that React can take care of determining when the `Portal` should re-render:
```
function App() {
  const [container, setContainer] = React.useState(null);
  const handleRef = React.useCallback(
    (instance) => setContainer(instance),
    [setContainer],
  );

  return (
    <div className="App">
      <Portal container={container}>
        <span>Portaled</span>
      </Portal>
      <div ref={handleRef} />
    </div>
  );
}

```
CopyCopied(or Ctrl + C)
## [What's the clsx dependency for?](https://mui.com/material-ui/getting-started/faq/#whats-the-clsx-dependency-for)
`className` strings conditionally, out of an object with keys being the class strings, and values being booleans.
Instead of writing:
```
// let disabled = false, selected = true;

return (
  <div
    className={`MuiButton-root ${disabled ? 'Mui-disabled' : ''} ${
      selected ? 'Mui-selected' : ''
    }`}
  />
);

```
CopyCopied(or Ctrl + C)
you can do:
```
import clsx from 'clsx';

return (
  <div
    className={clsx('MuiButton-root', {
      'Mui-disabled': disabled,
      'Mui-selected': selected,
    })}
  />
);

```
CopyCopied(or Ctrl + C)
## [I cannot use components as selectors in the styled() utility. What should I do?](https://mui.com/material-ui/getting-started/faq/#i-cannot-use-components-as-selectors-in-the-styled-utility-what-should-i-do)
If you are getting the error: `TypeError: Cannot convert a Symbol value to a string`, take a look at the [styled()](https://mui.com/system/styled/#how-to-use-components-selector-api) docs page for instructions on how you can fix this.
## [How can I contribute to the free templates?](https://mui.com/material-ui/getting-started/faq/#how-can-i-contribute-to-the-free-templates)
The templates are built using a
### [Template page](https://mui.com/material-ui/getting-started/faq/#template-page)
Create a new page in the `docs/pages/material-ui/getting-started/templates/<name>.js` directory with the following code:
```
import * as React from 'react';
import AppTheme from 'docs/src/modules/components/AppTheme';
import TemplateFrame from 'docs/src/modules/components/TemplateFrame';
import Template from 'docs/data/material/getting-started/templates/<name>/<Template>';

export default function Page() {
  return (
    <AppTheme>
      <TemplateFrame>
        <Template />
      </TemplateFrame>
    </AppTheme>
  );
}

```
CopyCopied(or Ctrl + C)
Then create a template file at `docs/data/material/getting-started/templates/<name>/<Template>.tsx` (add more files if needed):
> Note: The `<Template>` must be a pascal case string of the `<name>` folder.
### [Shared theme](https://mui.com/material-ui/getting-started/faq/#shared-theme)
The template must use `AppTheme` from `../shared-theme/AppTheme` to ensure a consistent look and feel across all templates.
If the template includes custom-themed components, such as the dashboard template with MUI X themed components, pass them to the `AppTheme`'s `themedComponents` prop:
```
import AppTheme from '../shared-theme/AppTheme';

const xThemeComponents = {
  ...chartsCustomizations,
  ...dataGridCustomizations,
  ...datePickersCustomizations,
  ...treeViewCustomizations,
};

export default function Dashboard(props: { disableCustomTheme?: boolean }) {
  return (
    <AppTheme {...props} themeComponents={xThemeComponents}>...</AppTheme>
  )
}

```
CopyCopied(or Ctrl + C)
### [Color mode toggle](https://mui.com/material-ui/getting-started/faq/#color-mode-toggle)
The shared theme provides 2 appearance of the color mode toggle, `ColorModeSelect` and `ColorModeIconDropdown`. You can use either of them in your template, it will be hidden within the `TemplateFrame` but will be visible in the CodeSandbox and StackBlitz.
### [Template frame](https://mui.com/material-ui/getting-started/faq/#template-frame)
If the template has a sidebar or a header that needs to stick to the top, refer to the CSS variable `--template-frame-height` to adjust.
For example, the dashboard template has a fixed header that needs to be accounted for the template frame height:
```
<AppBar
  position="fixed"
  sx={{
    top: 'var(--template-frame-height, 0px)',
    // ...other styles
  }}
>

```
CopyCopied(or Ctrl + C)
This will make the `AppBar` stay below the `TemplateFrame` in a preview mode but stick to the top in the CodeSandbox and StackBlitz.
## [[legacy] I have several instances of styles on the page](https://mui.com/material-ui/getting-started/faq/#legacy-i-have-several-instances-of-styles-on-the-page)
If you are seeing a warning message in the console like the one below, you probably have several instances of `@mui/styles` initialized on the page.
It looks like there are several instances of `@mui/styles` initialized in this application. This may cause theme propagation issues, broken class names, specificity issues, and make your application bigger without a good reason.
### [Possible reasons](https://mui.com/material-ui/getting-started/faq/#possible-reasons)
There are several common reasons for this to happen:
  * You have another `@mui/styles` library somewhere in your dependencies.
  * You have a monorepo structure for your project (for example, lerna or yarn workspaces) and `@mui/styles` module is a dependency in more than one package (this one is more or less the same as the previous one).
  * You have several applications that are using `@mui/styles` running on the same page (for example, several entry points in webpack are loaded on the same page).


### [Duplicated module in node_modules](https://mui.com/material-ui/getting-started/faq/#duplicated-module-in-node-modules)
If you think that the issue may be in the duplication of the @mui/styles module somewhere in your dependencies, there are several ways to check this. You can use `npm ls @mui/styles`, `yarn list @mui/styles` or `find -L ./node_modules | grep /@mui/styles/package.json` commands in your application folder.
If none of these commands identified the duplication, try analyzing your bundle for multiple instances of @mui/styles. You can just check your bundle source, or use a tool like
If you identified that duplication is the issue that you are encountering there are several things you can try to solve it:
If you are using npm you can try running `npm dedupe`. This command searches the local dependencies and tries to simplify the structure by moving common dependencies further up the tree.
If you are using webpack, you can change the way it will
```
 resolve: {
+  alias: {
+    '@mui/styles': path.resolve(appFolder, 'node_modules', '@mui/styles'),
+  },
 },

```
CopyCopied(or Ctrl + C)
### [Running multiple applications on one page](https://mui.com/material-ui/getting-started/faq/#running-multiple-applications-on-one-page)
If you have several applications running on one page, consider using one @mui/styles module for all of them. If you are using webpack, you can use
```
  module.exports = {
    entry: {
+     vendor: ['@mui/styles'],
      app1: './src/app.1.js',
      app2: './src/app.2.js',
    },
    plugins: [
+     new webpack.optimize.CommonsChunkPlugin({
+       name: 'vendor',
+       minChunks: Infinity,
+     }),
    ]
  }

```
CopyCopied(or Ctrl + C)
## [[legacy] Why aren't my components rendering correctly in production builds?](https://mui.com/material-ui/getting-started/faq/#legacy-why-arent-my-components-rendering-correctly-in-production-builds)
The #1 reason this happens is likely due to class name conflicts once your code is in a production bundle. For Material UI to work, the `className` values of all components on a page must be generated by a single instance of the [class name generator](https://v6.mui.com/system/styles/advanced/#class-names).
To correct this issue, all components on the page need to be initialized such that there is only ever **one class name generator** among them.
You could end up accidentally using two class name generators in a variety of scenarios:
  * You accidentally **bundle** two versions of `@mui/styles`. You might have a dependency not correctly setting Material UI as a peer dependency.
  * You are using `StylesProvider` for a **subset** of your React tree.
  * You are using a bundler and it is splitting code in a way that causes multiple class name generator instances to be created.


If you are using webpack with the
Overall, it's simple to recover from this problem by wrapping each Material UI application with [`StylesProvider`](https://v6.mui.com/system/styles/api/#stylesprovider) components at the top of their component trees **and using a single class name generator shared among them**.
### [[legacy] CSS works only on first load and goes missing](https://mui.com/material-ui/getting-started/faq/#legacy-css-works-only-on-first-load-and-goes-missing)
The CSS is only generated on the first load of the page. Then, the CSS is missing on the server for consecutive requests.
#### Action to Take
The styling solution relies on a cache, the _sheets manager_ , to only inject the CSS once per component type (if you use two buttons, you only need the CSS of the button one time). You need to create **a new`sheets` instance for each request**.
Example of fix:
```
-// Create a sheets instance.
-const sheets = new ServerStyleSheets();

 function handleRender(req, res) {
+  // Create a sheets instance.
+  const sheets = new ServerStyleSheets();

   //…

   // Render the component to a string.
   const html = ReactDOMServer.renderToString(

```
CopyCopied(or Ctrl + C)
### [[legacy] React class name hydration mismatch](https://mui.com/material-ui/getting-started/faq/#legacy-react-class-name-hydration-mismatch)
Prop className did not match.
There is a class name mismatch between the client and the server. It might work for the first request. Another symptom is that the styling changes between initial page load and the downloading of the client scripts.
#### Action to Take
The class names value relies on the concept of [class name generator](https://v6.mui.com/system/styles/advanced/#class-names). The whole page needs to be rendered with **a single generator**. This generator needs to behave identically on the server and on the client. For instance:
  * You need to provide a new class name generator for each request. But you shouldn't share a `createGenerateClassName()` between different requests:
Example of fix:
```
-// Create a new class name generator.
-const generateClassName = createGenerateClassName();

 function handleRender(req, res) {
+  // Create a new class name generator.
+  const generateClassName = createGenerateClassName();

   //…

   // Render the component to a string.
   const html = ReactDOMServer.renderToString(

```
CopyCopied(or Ctrl + C)
  * You need to verify that your client and server are running the **exactly the same version** of Material UI. It is possible that a mismatch of even minor versions can cause styling problems. To check version numbers, run `npm list @mui/styles` in the environment where you build your application and also in your deployment environment.
You can also ensure the same version in different environments by specifying a specific Material UI version in the dependencies of your package.json.
_example of fix (package.json):_
```
  "dependencies": {
    ...
-   "@mui/styles": "^5.0.0",
+   "@mui/styles": "5.0.0",
    ...
  },

```
CopyCopied(or Ctrl + C)
  * You need to make sure that the server and the client share the same `process.env.NODE_ENV` value.


Was this page helpful?
* * *
[](https://mui.com/material-ui/getting-started/design-resources/)[Supported components](https://mui.com/material-ui/getting-started/supported-components/)
* * *
[](https://mui.com/)
•
[Blog ](https://mui.com/blog/)
•
[Store ](https://mui.com/store/)
[](https://mui.com/r/discord/ "Discord")[](https://mui.com/feed/blog/rss.xml "RSS Feed")
Contents
  * [MUI is an awesome organization. How can I support it?](https://mui.com/material-ui/getting-started/faq/#mui-is-an-awesome-organization-how-can-i-support-it)
  * [Why do the fixed positioned elements move when a modal is opened?](https://mui.com/material-ui/getting-started/faq/#why-do-the-fixed-positioned-elements-move-when-a-modal-is-opened)
  * [How can I disable the ripple effect globally?](https://mui.com/material-ui/getting-started/faq/#how-can-i-disable-the-ripple-effect-globally)
  * [How can I disable transitions globally?](https://mui.com/material-ui/getting-started/faq/#how-can-i-disable-transitions-globally)
  * [Do I have to use Emotion to style my app?](https://mui.com/material-ui/getting-started/faq/#do-i-have-to-use-emotion-to-style-my-app)
  * [When should I use inline-style vs. CSS?](https://mui.com/material-ui/getting-started/faq/#when-should-i-use-inline-style-vs-css)
  * [How do I use react-router?](https://mui.com/material-ui/getting-started/faq/#how-do-i-use-react-router)
  * [How can I access the DOM element?](https://mui.com/material-ui/getting-started/faq/#how-can-i-access-the-dom-element)
  * [My App doesn't render correctly on the server](https://mui.com/material-ui/getting-started/faq/#my-app-doesnt-render-correctly-on-the-server)
  * [Why are the colors I am seeing different from what I see here?](https://mui.com/material-ui/getting-started/faq/#why-are-the-colors-i-am-seeing-different-from-what-i-see-here)
  * [Why does component X require a DOM node in a prop instead of a ref object?](https://mui.com/material-ui/getting-started/faq/#why-does-component-x-require-a-dom-node-in-a-prop-instead-of-a-ref-object)
  * [What's the clsx dependency for?](https://mui.com/material-ui/getting-started/faq/#whats-the-clsx-dependency-for)
  * [I cannot use components as selectors in the styled(​) utility. What should I do?](https://mui.com/material-ui/getting-started/faq/#i-cannot-use-components-as-selectors-in-the-styled-utility-what-should-i-do)
  * [How can I contribute to the free templates?](https://mui.com/material-ui/getting-started/faq/#how-can-i-contribute-to-the-free-templates)
    * [Template page](https://mui.com/material-ui/getting-started/faq/#template-page)
    * [Shared theme](https://mui.com/material-ui/getting-started/faq/#shared-theme)
    * [Color mode toggle](https://mui.com/material-ui/getting-started/faq/#color-mode-toggle)
    * [Template frame](https://mui.com/material-ui/getting-started/faq/#template-frame)
  * [[legacy] I have several instances of styles on the page](https://mui.com/material-ui/getting-started/faq/#legacy-i-have-several-instances-of-styles-on-the-page)
    * [Possible reasons](https://mui.com/material-ui/getting-started/faq/#possible-reasons)
    * [Duplicated module in node_modules](https://mui.com/material-ui/getting-started/faq/#duplicated-module-in-node-modules)
    * [Running multiple applications on one page](https://mui.com/material-ui/getting-started/faq/#running-multiple-applications-on-one-page)
  * [[legacy] Why aren't my components rendering correctly in production builds?](https://mui.com/material-ui/getting-started/faq/#legacy-why-arent-my-components-rendering-correctly-in-production-builds)
    * [[legacy] CSS works only on first load and goes missing](https://mui.com/material-ui/getting-started/faq/#legacy-css-works-only-on-first-load-and-goes-missing)
    * [[legacy] React class name hydration mismatch](https://mui.com/material-ui/getting-started/faq/#legacy-react-class-name-hydration-mismatch)


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
