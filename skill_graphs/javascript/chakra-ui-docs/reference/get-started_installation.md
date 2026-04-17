Build faster with Premium Chakra UI Components 💎
[Learn more](https://pro.chakra-ui.com?utm_source=chakra-ui.com)
[Skip to Content](https://chakra-ui.com/docs/get-started/installation#chakra-skip-nav)
  1. Overview
  2. Installation


# Installation
How to install and set up Chakra UI in your project
AI TipWant to skip the docs? Use the [MCP Server](https://chakra-ui.com/docs/get-started/ai/mcp-server)
## [Framework Guide](https://chakra-ui.com/docs/get-started/installation#framework-guide)
Chakra UI works in your favorite framework. We've put together step-by-step guides for these frameworks
[ Next.js Easily add Chakra UI with Next.js app ](https://chakra-ui.com/docs/get-started/frameworks/next-app)[ Vite Use Chakra UI with Vite ](https://chakra-ui.com/docs/get-started/frameworks/vite)
The minimum node version required is Node.20.x
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
