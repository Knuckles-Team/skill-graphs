Build faster with Premium Chakra UI Components 💎
[Learn more](https://pro.chakra-ui.com?utm_source=chakra-ui.com)
[Skip to Content](https://chakra-ui.com/docs/theming/overview#chakra-skip-nav)
[](https://chakra-ui.com/)[Docs](https://chakra-ui.com/docs/get-started/installation)[Showcase](https://chakra-ui.com/showcase)[Blog](https://chakra-ui.com/blog)[Guides](https://chakra-ui.com/guides)
3.34.0Search...`⌘K`
[Get Started ](https://chakra-ui.com/docs/get-started/installation)[Components ](https://chakra-ui.com/docs/components/concepts/overview)[Charts ](https://chakra-ui.com/docs/charts/installation)[Styling ](https://chakra-ui.com/docs/styling/overview)[Theming ](https://chakra-ui.com/docs/theming/overview)
[](https://chakra-ui.com/)
  1. Concepts
  2. Overview


Concepts
[Overview](https://chakra-ui.com/docs/theming/overview)[Tokens](https://chakra-ui.com/docs/theming/tokens)[Semantic Tokens](https://chakra-ui.com/docs/theming/semantic-tokens)[Recipes](https://chakra-ui.com/docs/theming/recipes)[Slot Recipes](https://chakra-ui.com/docs/theming/slot-recipes)
Design Tokens
[Animations](https://chakra-ui.com/docs/theming/animations)[Aspect Ratios](https://chakra-ui.com/docs/theming/aspect-ratios)[Breakpoints](https://chakra-ui.com/docs/theming/breakpoints)[Colors](https://chakra-ui.com/docs/theming/colors)[Cursors](https://chakra-ui.com/docs/theming/cursors)[Radii](https://chakra-ui.com/docs/theming/radii)[Shadows](https://chakra-ui.com/docs/theming/shadows)[Sizes](https://chakra-ui.com/docs/theming/sizes)[Spacing](https://chakra-ui.com/docs/theming/spacing)[Typography](https://chakra-ui.com/docs/theming/typography)[Z-Index](https://chakra-ui.com/docs/theming/z-index)
Compositions
[Text Styles](https://chakra-ui.com/docs/theming/text-styles)[Layer Styles](https://chakra-ui.com/docs/theming/layer-styles)
Customization
[Overview](https://chakra-ui.com/docs/theming/customization/overview)[Animations](https://chakra-ui.com/docs/theming/customization/animations)[Breakpoints](https://chakra-ui.com/docs/theming/customization/breakpoints)[Colors](https://chakra-ui.com/docs/theming/customization/colors)[Conditions](https://chakra-ui.com/docs/theming/customization/conditions)[CSS Variables](https://chakra-ui.com/docs/theming/customization/css-variables)[Global CSS](https://chakra-ui.com/docs/theming/customization/global-css)[Recipes](https://chakra-ui.com/docs/theming/customization/recipes)[Sizes](https://chakra-ui.com/docs/theming/customization/sizes)[Spacing](https://chakra-ui.com/docs/theming/customization/spacing)[Utilities](https://chakra-ui.com/docs/theming/customization/utilities)
# Overview
A guide for configuring the Chakra UI theming system.
AI TipWant to skip the docs? Use the [MCP Server](https://chakra-ui.com/docs/get-started/ai/mcp-server)
## [Architecture](https://chakra-ui.com/docs/theming/overview#architecture)
The Chakra UI theming system is built around the API of
Here's a quick overview of how the system is structured to provide a performant and extensible styling system:
  * Define the styling system configuration using the `defineConfig` function
  * Create the styling engine using the `createSystem` function
  * Pass the styling engine to the `ChakraProvider` component


```
import {
  ChakraProvider,
  createSystem,
  defaultConfig,
  defineConfig,
} from "@chakra-ui/react"

const config = defineConfig({
  theme: {
    tokens: {
      colors: {},
    },
  },
})

const system = createSystem(defaultConfig, config)

export default function App() {
  return (
    <ChakraProvider value={system}>
      <Box>Hello World</Box>
    </ChakraProvider>
  )
}
```

## [Config](https://chakra-ui.com/docs/theming/overview#config)
The Chakra UI system is configured using the `defineConfig` function. This function accepts a configuration object that allows you to customize the styling system's behavior.
After a config is defined, it is passed to the `createSystem` function to create the styling engine.
### [cssVarsRoot](https://chakra-ui.com/docs/theming/overview#cssvarsroot)
`cssVarsRoot` is the root element where the token CSS variables will be applied.
theme.ts
```
const config = defineConfig({
  cssVarsRoot: ":where(:root, :host)",
})

export default createSystem(defaultConfig, config)
```

### [cssVarsPrefix](https://chakra-ui.com/docs/theming/overview#cssvarsprefix)
`cssVarsPrefix` is the prefix used for the token CSS variables.
theme.ts
```
const config = defineConfig({
  cssVarsPrefix: "ck",
})

export default createSystem(defaultConfig, config)
```

### [globalCss](https://chakra-ui.com/docs/theming/overview#globalcss)
`globalCss` is used to apply global styles to the system.
theme.ts
```
const config = defineConfig({
  globalCss: {
    "html, body": {
      margin: 0,
      padding: 0,
    },
  },
})

export default createSystem(defaultConfig, config)
```

### [preflight](https://chakra-ui.com/docs/theming/overview#preflight)
`preflight` is used to apply css reset styles to the system.
theme.ts
```
const config = defineConfig({
  preflight: false,
})

export default createSystem(defaultConfig, config)
```

Alternatively, you can use the `preflight` config property to apply css reset styles to the system. This is useful if you want to apply css reset styles to a specific element.
theme.ts
```
const config = defineConfig({
  preflight: {
    scope: ".chakra-reset",
  },
})

export default createSystem(defaultConfig, config)
```

### [theme](https://chakra-ui.com/docs/theming/overview#theme)
Use the `theme` config property to define the system theme. This property accepts the following properties:
  * `breakpoints`: for defining breakpoints
  * `keyframes`: for defining css keyframes animations
  * `tokens`: for defining tokens
  * `semanticTokens`: for defining semantic tokens
  * `textStyles`: for defining typography styles
  * `layerStyles`: for defining layer styles
  * `animationStyles`: for defining animation styles
  * `recipes`: for defining component recipes
  * `slotRecipes`: for defining component slot recipes


theme.ts
```
const config = defineConfig({
  theme: {
    breakpoints: {
      sm: "320px",
      md: "768px",
      lg: "960px",
      xl: "1200px",
    },
    tokens: {
      colors: {
        red: "#EE0F0F",
      },
    },
    semanticTokens: {
      colors: {
        danger: { value: "{colors.red}" },
      },
    },
    keyframes: {
      spin: {
        from: { transform: "rotate(0deg)" },
        to: { transform: "rotate(360deg)" },
      },
    },
  },
})

export default createSystem(defaultConfig, config)
```

### [conditions](https://chakra-ui.com/docs/theming/overview#conditions)
Use the `conditions` config property to define custom selectors and media query conditions for use in the system.
theme.ts
```
const config = defineConfig({
  conditions: {
    cqSm: "@container(min-width: 320px)",
    child: "& > *",
  },
})

export default createSystem(defaultConfig, config)
```

Sample usage:
```
<Box mt="40px" _cqSm={{ mt: "0px" }}>
  <Text>Hello World</Text>
</Box>
```

### [strictTokens](https://chakra-ui.com/docs/theming/overview#stricttokens)
Use the `strictTokens` config property to enforce the usage of only design tokens. This will throw a TS error if you try to use a token that is not defined in the theme.
theme.ts
```
const config = defineConfig({
  strictTokens: true,
})

export default createSystem(defaultConfig, config)
```

```
// ❌ This will throw a TS error
<Box color="#4f343e">Hello World</Box>

// ✅ This will work
<Box color="red.400">Hello World</Box>
```

If you use TypeScript with `strictTokens`, run the [CLI `typegen` command](https://chakra-ui.com/docs/get-started/cli#chakra-typegen) in local development and CI/CD so token typings stay in sync with your theme.
## [TypeScript](https://chakra-ui.com/docs/theming/overview#typescript)
When you configure the system (colors, space, fonts, etc.), the CLI generates type definitions to keep your theme in sync with `@chakra-ui/react`. This provides a type-safe API and autocompletion.
See the [CLI docs](https://chakra-ui.com/docs/get-started/cli#chakra-typegen) for how to run typegen in postinstall, CI, and monorepos.
```
npx @chakra-ui/cli typegen ./theme.ts
```

## [System](https://chakra-ui.com/docs/theming/overview#system)
After a config is defined, it is passed to the `createSystem` function to create the styling engine. The returned `system` is framework-agnostic JavaScript styling engine that can be used to style components.
```
const system = createSystem(defaultConfig, config)
```

The system includes the following properties:
### [token](https://chakra-ui.com/docs/theming/overview#token)
The token function is used to get a raw token value, or css variable.
```
const system = createSystem(defaultConfig, config)

// raw token
system.token("colors.red.200")
// => "#EE0F0F"

// token with fallback
system.token("colors.pink.240", "#000")
// => "#000"
```

Use the `token.var` function to get the css variable:
```
// css variable
system.token.var("colors.red.200")
// => "var(--chakra-colors-red-200)"

// token with fallback
system.token.var("colors.pink.240", "colors.red.200")
// => "var(--chakra-colors-red-200)"
```

It's important to note that `semanticTokens` always return a css variable, regardless of whether you use `token` or `token.var`. This is because semantic tokens change based on the theme.
```
// semantic token
system.token("colors.danger")
// => "var(--chakra-colors-danger)"

system.token.var("colors.danger")
// => "var(--chakra-colors-danger)"
```

### [tokens](https://chakra-ui.com/docs/theming/overview#tokens)
```
const system = createSystem(defaultConfig, config)

system.tokens.getVar("colors.red.200")
// => "var(--chakra-colors-red-200)"

system.tokens.expandReferenceInValue("3px solid {colors.red.200}")
// => "3px solid var(--chakra-colors-red-200)"

system.tokens.cssVarMap
// => Map { "colors": Map { "red.200": "var(--chakra-colors-red-200)" } }

system.tokens.flatMap
// => Map { "colors.red.200": "var(--chakra-colors-red-200)" }
```

### [css](https://chakra-ui.com/docs/theming/overview#css)
The `css` function is used to convert chakra style objects to CSS style object that can be passed to `emotion` or `styled-components` or any other styling library.
```
const system = createSystem(defaultConfig, config)

system.css({
  color: "red.200",
  bg: "blue.200",
})

// => { color: "var(--chakra-colors-red-200)", background: "var(--chakra-colors-blue-200)" }
```

### [cva](https://chakra-ui.com/docs/theming/overview#cva)
The `cva` function is used to create component recipes. It returns a function that, when called with a set of props, returns a style object.
```
const system = createSystem(defaultConfig, config)

const button = system.cva({
  base: {
    color: "white",
    bg: "blue.500",
  },
  variants: {
    outline: {
      color: "blue.500",
      bg: "transparent",
      border: "1px solid",
    },
  },
})

button({ variant: "outline" })
// => { color: "blue.500", bg: "transparent", border: "1px solid" }
```

### [sva](https://chakra-ui.com/docs/theming/overview#sva)
The `sva` function is used to create component slot recipes. It returns a function that, when called with a set of props, returns a style object for each slot.
```
const system = createSystem(defaultConfig, config)

const alert = system.sva({
  slots: ["title", "description", "icon"],
  base: {
    title: { color: "white" },
    description: { color: "white" },
    icon: { color: "white" },
  },
  variants: {
    status: {
      info: {
        title: { color: "blue.500" },
        description: { color: "blue.500" },
        icon: { color: "blue.500" },
      },
    },
  },
})

alert({ status: "info" })
// => { title: { color: "blue.500" }, description: { color: "blue.500" }, icon: { color: "blue.500" } }
```

### [isValidProperty](https://chakra-ui.com/docs/theming/overview#isvalidproperty)
The `isValidProperty` function is used to check if a property is valid.
```
const system = createSystem(defaultConfig, config)

system.isValidProperty("color")
// => true

system.isValidProperty("background")
// => true

system.isValidProperty("invalid")
// => false
```

### [splitCssProps](https://chakra-ui.com/docs/theming/overview#splitcssprops)
The `splitCssProps` function is used to split the props into css props and non-css props.
```
const system = createSystem(defaultConfig, config)

system.splitCssProps({
  color: "red.200",
  bg: "blue.200",
  "aria-label": "Hello World",
})
// => [{ color: "red.200", bg: "blue.200" }, { "aria-label": "Hello World" }]
```

### [breakpoints](https://chakra-ui.com/docs/theming/overview#breakpoints)
The `breakpoints` property is used to query breakpoints.
```
const system = createSystem(defaultConfig, config)

system.breakpoints.up("sm")
// => "@media (min-width: 320px)"

system.breakpoints.down("sm")
// => "@media (max-width: 319px)"

system.breakpoints.only("md")
// => "@media (min-width: 320px) and (max-width: 768px)"

system.breakpoints.keys()
// => ["sm", "md", "lg", "xl"]
```

## [Tokens](https://chakra-ui.com/docs/theming/overview#tokens-1)
To learn more about tokens, please refer to the [tokens](https://chakra-ui.com/docs/theming/tokens) section.
## [Recipes](https://chakra-ui.com/docs/theming/overview#recipes)
To learn more about recipes, please refer to the [recipes](https://chakra-ui.com/docs/theming/recipes) section.
[Previous](https://chakra-ui.com/docs/styling/style-props/typography)[ Next Tokens ](https://chakra-ui.com/docs/theming/tokens)
On this page
[Architecture](https://chakra-ui.com/docs/theming/overview#architecture)[Config](https://chakra-ui.com/docs/theming/overview#config)[cssVarsRoot](https://chakra-ui.com/docs/theming/overview#cssvarsroot)[cssVarsPrefix](https://chakra-ui.com/docs/theming/overview#cssvarsprefix)[globalCss](https://chakra-ui.com/docs/theming/overview#globalcss)[preflight](https://chakra-ui.com/docs/theming/overview#preflight)[theme](https://chakra-ui.com/docs/theming/overview#theme)[conditions](https://chakra-ui.com/docs/theming/overview#conditions)[strictTokens](https://chakra-ui.com/docs/theming/overview#stricttokens)[TypeScript](https://chakra-ui.com/docs/theming/overview#typescript)[System](https://chakra-ui.com/docs/theming/overview#system)[token](https://chakra-ui.com/docs/theming/overview#token)[tokens](https://chakra-ui.com/docs/theming/overview#tokens)[css](https://chakra-ui.com/docs/theming/overview#css)[cva](https://chakra-ui.com/docs/theming/overview#cva)[sva](https://chakra-ui.com/docs/theming/overview#sva)[isValidProperty](https://chakra-ui.com/docs/theming/overview#isvalidproperty)[splitCssProps](https://chakra-ui.com/docs/theming/overview#splitcssprops)[breakpoints](https://chakra-ui.com/docs/theming/overview#breakpoints)[Tokens](https://chakra-ui.com/docs/theming/overview#tokens-1)[Recipes](https://chakra-ui.com/docs/theming/overview#recipes)
Scroll to top
[ Master Chakra UI Learn how to build design systems with hands-on examples and expert guidance ](https://mastery.chakra-ui.com)
