Build faster with Premium Chakra UI Components 💎
[Learn more](https://pro.chakra-ui.com?utm_source=chakra-ui.com)
[Skip to Content](https://chakra-ui.com/docs/get-started/installation#chakra-skip-nav)
[](https://chakra-ui.com/)[Docs](https://chakra-ui.com/docs/get-started/installation)[Showcase](https://chakra-ui.com/showcase)[Blog](https://chakra-ui.com/blog)[Guides](https://chakra-ui.com/guides)
3.36.0Search...`⌘K`
[Get Started ](https://chakra-ui.com/docs/get-started/installation)[Components ](https://chakra-ui.com/docs/components/concepts/overview)[Charts ](https://chakra-ui.com/docs/charts/installation)[Styling ](https://chakra-ui.com/docs/styling/overview)[Theming ](https://chakra-ui.com/docs/theming/overview)
[](https://chakra-ui.com/)
  1. Overview
  2. Installation

Overview
[Installation](https://chakra-ui.com/docs/get-started/installation)[Migration](https://chakra-ui.com/docs/get-started/migration)[CLI](https://chakra-ui.com/docs/get-started/cli)[Figma](https://chakra-ui.com/docs/get-started/figma)[Contributing](https://chakra-ui.com/docs/get-started/contributing)[Playground](https://chakra-ui.com/playground)
AI for Agents
[MCP Server](https://chakra-ui.com/docs/get-started/ai/mcp-server)[LLMs.txt](https://chakra-ui.com/docs/get-started/ai/llms)[AI Skillsnew](https://chakra-ui.com/docs/get-started/ai/skills)
Frameworks
[Next.js (App)](https://chakra-ui.com/docs/get-started/frameworks/next-app)[Next.js (Pages)](https://chakra-ui.com/docs/get-started/frameworks/next-pages)[Remix](https://chakra-ui.com/docs/get-started/frameworks/remix)[Storybook](https://chakra-ui.com/docs/get-started/frameworks/storybook)[TanStack Router](https://chakra-ui.com/docs/get-started/frameworks/tanstack-router)[Vite](https://chakra-ui.com/docs/get-started/frameworks/vite)
Environments
[Shadow DOM](https://chakra-ui.com/docs/get-started/environments/shadow-dom)[Iframe](https://chakra-ui.com/docs/get-started/environments/iframe)
# Installation
How to install and set up Chakra UI in your project
AI TipWant to skip the docs? Use our [Agent Skills](https://chakra-ui.com/docs/get-started/ai/skills)
Copy Page
## [Framework Guide](https://chakra-ui.com/docs/get-started/installation#framework-guide)
Chakra UI works in your favorite framework. We've put together step-by-step guides for these frameworks
[ Next.js Easily add Chakra UI with Next.js app ](https://chakra-ui.com/docs/get-started/frameworks/next-app)[ Vite Use Chakra UI with Vite ](https://chakra-ui.com/docs/get-started/frameworks/vite)
The minimum Node.js version required is 20.x
## [Styling roadmap](https://chakra-ui.com/docs/get-started/installation#styling-roadmap)
Today, Chakra UI uses Emotion at runtime.
Our long-term direction is a zero-runtime styling model inspired by Panda CSS, rolled out in phases so existing apps can keep upgrading safely.
If you want to help, see the [contributing guide](https://chakra-ui.com/docs/get-started/contributing) and open discussions or PRs for docs, migration tooling, and real-world adoption feedback.
## [Installation](https://chakra-ui.com/docs/get-started/installation#installation)
To manually set up Chakra UI in your project, follow the steps below.
1
### [Install `@chakra-ui/react`](https://chakra-ui.com/docs/get-started/installation#install-chakra-uireact)

```
npm i @chakra-ui/react @emotion/react
```

2
### [Add snippets](https://chakra-ui.com/docs/get-started/installation#add-snippets)
Snippets are pre-built components that you can use to build your UI faster. Using the `@chakra-ui/cli` you can add snippets to your project.

```
npx @chakra-ui/cli snippet add
```

3
### [Setup provider](https://chakra-ui.com/docs/get-started/installation#setup-provider)
Wrap your application with the `Provider` component generated in the `components/ui/provider` component at the root of your application.
This provider composes the following:
  * `ChakraProvider` from `@chakra-ui/react` for the styling system
  * `ThemeProvider` from `next-themes` for color mode

```
import { Provider } from "@/components/ui/provider"

function App({ Component, pageProps }) {
  return (
    <Provider>
      <Component {...pageProps} />
    </Provider>
  )
}
```

4
### [Update tsconfig](https://chakra-ui.com/docs/get-started/installation#update-tsconfig)
If you're using TypeScript, you need to update the `compilerOptions` in the tsconfig file to include the following options:

```
{
  "compilerOptions": {
    "module": "ESNext",
    "moduleResolution": "Bundler",
    "skipLibCheck": true,
    "paths": {
      "@/*": ["./src/*"]
    }
  }
}
```

If you're using JavaScript, create a `jsconfig.json` file and add the above code to the file.
5
### [Enjoy!](https://chakra-ui.com/docs/get-started/installation#enjoy)
With the power of the snippets and the primitive components from Chakra UI, you can build your UI faster.

```
import { Button, HStack } from "@chakra-ui/react"

const Demo = () => {
  return (
    <HStack>
      <Button>Click me</Button>
      <Button>Click me</Button>
    </HStack>
  )
}
```

## [Learn](https://chakra-ui.com/docs/get-started/installation#learn)
Watch our official courses and dive into dozens of videos that will teach you everything you need to know about Chakra UI, from basics to advanced concepts.
## [Contribute](https://chakra-ui.com/docs/get-started/installation#contribute)
Whether you're a beginner or advanced Chakra UI user, joining our community is the best way to connect with like-minded people who build great products with the library.
[ Next Migration ](https://chakra-ui.com/docs/get-started/migration)
On this page
[Framework Guide](https://chakra-ui.com/docs/get-started/installation#framework-guide)[Styling roadmap](https://chakra-ui.com/docs/get-started/installation#styling-roadmap)[Installation](https://chakra-ui.com/docs/get-started/installation#installation)[Install @chakra-ui/react](https://chakra-ui.com/docs/get-started/installation#install-chakra-uireact)[Add snippets](https://chakra-ui.com/docs/get-started/installation#add-snippets)[Setup provider](https://chakra-ui.com/docs/get-started/installation#setup-provider)[Update tsconfig](https://chakra-ui.com/docs/get-started/installation#update-tsconfig)[Enjoy!](https://chakra-ui.com/docs/get-started/installation#enjoy)[Learn](https://chakra-ui.com/docs/get-started/installation#learn)[Contribute](https://chakra-ui.com/docs/get-started/installation#contribute)
Scroll to top
[ Master Chakra UI Learn how to build design systems with hands-on examples and expert guidance Watch Now ](https://mastery.chakra-ui.com)
