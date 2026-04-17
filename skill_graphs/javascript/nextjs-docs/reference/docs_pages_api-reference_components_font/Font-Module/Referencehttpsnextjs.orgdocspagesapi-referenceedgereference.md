## Reference[](https://nextjs.org/docs/pages/api-reference/edge#reference)
Key | `font/google` | `font/local` | Type | Required
---|---|---|---|---
[`src`](https://nextjs.org/docs/pages/api-reference/edge#src) |  |  | String or Array of Objects | Yes
[`weight`](https://nextjs.org/docs/pages/api-reference/edge#weight) |  |  | String or Array | Required/Optional
[`style`](https://nextjs.org/docs/pages/api-reference/edge#style) |  |  | String or Array | -
[`subsets`](https://nextjs.org/docs/pages/api-reference/edge#subsets) |  |  | Array of Strings | -
[`axes`](https://nextjs.org/docs/pages/api-reference/edge#axes) |  |  | Array of Strings | -
[`display`](https://nextjs.org/docs/pages/api-reference/edge#display) |  |  | String | -
[`preload`](https://nextjs.org/docs/pages/api-reference/edge#preload) |  |  | Boolean | -
[`fallback`](https://nextjs.org/docs/pages/api-reference/edge#fallback) |  |  | Array of Strings | -
[`adjustFontFallback`](https://nextjs.org/docs/pages/api-reference/edge#adjustfontfallback) |  |  | Boolean or String | -
[`variable`](https://nextjs.org/docs/pages/api-reference/edge#variable) |  |  | String | -
[`declarations`](https://nextjs.org/docs/pages/api-reference/edge#declarations) |  |  | Array of Objects | -
###  `src`[](https://nextjs.org/docs/pages/api-reference/edge#src)
The path of the font file as a string or an array of objects (with type `Array<{path: string, weight?: string, style?: string}>`) relative to the directory where the font loader function is called.
Used in `next/font/local`
  * Required


Examples:
  * `src:'./fonts/my-font.woff2'` where `my-font.woff2` is placed in a directory named `fonts` inside the `app` directory
  * `src:[{path: './inter/Inter-Thin.ttf', weight: '100',},{path: './inter/Inter-Regular.ttf',weight: '400',},{path: './inter/Inter-Bold-Italic.ttf', weight: '700',style: 'italic',},]`
  * if the font loader function is called in `app/page.tsx` using `src:'../styles/fonts/my-font.ttf'`, then `my-font.ttf` is placed in `styles/fonts` at the root of the project


###  `weight`[](https://nextjs.org/docs/pages/api-reference/edge#weight)
The font
  * A string with possible values of the weights available for the specific font or a range of values if it's a
  * An array of weight values if the font is not a `next/font/google` only.


Used in `next/font/google` and `next/font/local`
  * Required if the font being used is **not**


Examples:
  * `weight: '400'`: A string for a single weight value - for the font `'100'`, `'200'`, `'300'`, `'400'`, `'500'`, `'600'`, `'700'`, `'800'`, `'900'` or `'variable'` where `'variable'` is the default)
  * `weight: '100 900'`: A string for the range between `100` and `900` for a variable font
  * `weight: ['100','400','900']`: An array of 3 possible values for a non variable font


###  `style`[](https://nextjs.org/docs/pages/api-reference/edge#style)
The font
  * A string `'normal'`
  * An array of style values if the font is not a `next/font/google` only.


Used in `next/font/google` and `next/font/local`
  * Optional


Examples:
  * `style: 'italic'`: A string - it can be `normal` or `italic` for `next/font/google`
  * `style: 'oblique'`: A string - it can take any value for `next/font/local` but is expected to come from
  * `style: ['italic','normal']`: An array of 2 values for `next/font/google` - the values are from `normal` and `italic`


###  `subsets`[](https://nextjs.org/docs/pages/api-reference/edge#subsets)
The font [preloaded](https://nextjs.org/docs/app/api-reference/components/font#specifying-a-subset). Fonts specified via `subsets` will have a link preload tag injected into the head when the [`preload`](https://nextjs.org/docs/pages/api-reference/edge#preload) option is true, which is the default.
Used in `next/font/google`
  * Optional


Examples:
  * `subsets: ['latin']`: An array with the subset `latin`


You can find a list of all subsets on the Google Fonts page for your font.
###  `axes`[](https://nextjs.org/docs/pages/api-reference/edge#axes)
Some variable fonts have extra `axes` that can be included. By default, only the font weight is included to keep the file size down. The possible values of `axes` depend on the specific font.
Used in `next/font/google`
  * Optional


Examples:
  * `axes: ['slnt']`: An array with value `slnt` for the `Inter` variable font which has `slnt` as additional `axes` as shown `axes` values for your font by using the filter on the `wght`


###  `display`[](https://nextjs.org/docs/pages/api-reference/edge#display)
The font `'auto'`, `'block'`, `'swap'`, `'fallback'` or `'optional'` with default value of `'swap'`.
Used in `next/font/google` and `next/font/local`
  * Optional


Examples:
  * `display: 'optional'`: A string assigned to the `optional` value


###  `preload`[](https://nextjs.org/docs/pages/api-reference/edge#preload)
A boolean value that specifies whether the font should be [preloaded](https://nextjs.org/docs/app/api-reference/components/font#preloading) or not. The default is `true`.
Used in `next/font/google` and `next/font/local`
  * Optional


Examples:
  * `preload: false`


###  `fallback`[](https://nextjs.org/docs/pages/api-reference/edge#fallback)
The fallback font to use if the font cannot be loaded. An array of strings of fallback fonts with no default.
  * Optional


Used in `next/font/google` and `next/font/local`
Examples:
  * `fallback: ['system-ui', 'arial']`: An array setting the fallback fonts to `system-ui` or `arial`


###  `adjustFontFallback`[](https://nextjs.org/docs/pages/api-reference/edge#adjustfontfallback)
  * For `next/font/google`: A boolean value that sets whether an automatic fallback font should be used to reduce `true`.
  * For `next/font/local`: A string or boolean `false` value that sets whether an automatic fallback font should be used to reduce `'Arial'`, `'Times New Roman'` or `false`. The default is `'Arial'`.


Used in `next/font/google` and `next/font/local`
  * Optional


Examples:
  * `adjustFontFallback: false`: for `next/font/google`
  * `adjustFontFallback: 'Times New Roman'`: for `next/font/local`


###  `variable`[](https://nextjs.org/docs/pages/api-reference/edge#variable)
A string value to define the CSS variable name to be used if the style is applied with the [CSS variable method](https://nextjs.org/docs/pages/api-reference/edge#css-variables).
Used in `next/font/google` and `next/font/local`
  * Optional


Examples:
  * `variable: '--my-font'`: The CSS variable `--my-font` is declared


###  `declarations`[](https://nextjs.org/docs/pages/api-reference/edge#declarations)
An array of font face `@font-face` further.
Used in `next/font/local`
  * Optional


Examples:
  * `declarations: [{ prop: 'ascent-override', value: '90%' }]`
