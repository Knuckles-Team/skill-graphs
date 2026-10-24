Build faster with Premium Chakra UI Components 💎
[Learn more](https://pro.chakra-ui.com?utm_source=chakra-ui.com)
[Skip to Content](https://chakra-ui.com/docs/charts/installation#chakra-skip-nav)
[](https://chakra-ui.com/)[Docs](https://chakra-ui.com/docs/get-started/installation)[Showcase](https://chakra-ui.com/showcase)[Blog](https://chakra-ui.com/blog)[Guides](https://chakra-ui.com/guides)
3.36.0Search...`⌘K`
[Get Started ](https://chakra-ui.com/docs/get-started/installation)[Components ](https://chakra-ui.com/docs/components/concepts/overview)[Charts ](https://chakra-ui.com/docs/charts/installation)[Styling ](https://chakra-ui.com/docs/styling/overview)[Theming ](https://chakra-ui.com/docs/theming/overview)
[](https://chakra-ui.com/)
  1. Overview
  2. Installation

Overview
[Installation](https://chakra-ui.com/docs/charts/installation)[useChart](https://chakra-ui.com/docs/charts/use-chart)[Axis (X and Y)](https://chakra-ui.com/docs/charts/axes)[Cartesian Grid](https://chakra-ui.com/docs/charts/cartesian-grid)
Charts
[Area Chart](https://chakra-ui.com/docs/charts/area-chart)[Bar Chart](https://chakra-ui.com/docs/charts/bar-chart)[Bar List](https://chakra-ui.com/docs/charts/bar-list)[Bar Segment](https://chakra-ui.com/docs/charts/bar-segment)[Donut Chart](https://chakra-ui.com/docs/charts/donut-chart)[Line Chart](https://chakra-ui.com/docs/charts/line-chart)[Pie Chart](https://chakra-ui.com/docs/charts/pie-chart)[Radar Chart](https://chakra-ui.com/docs/charts/radar-chart)[Scatter Chart](https://chakra-ui.com/docs/charts/scatter-chart)[Sparkline](https://chakra-ui.com/docs/charts/sparkline)
# Charts
Creating beautiful charts with recharts and Chakra UI
AI TipWant to skip the docs? Use our [Agent Skills](https://chakra-ui.com/docs/get-started/ai/skills)
Copy Page
Charts are designed to look great out of the box, seamlessly integrating with other Chakra UI's theming system. The charts are built on top of
## [Installation](https://chakra-ui.com/docs/charts/installation#installation)
Run the following command to install the charts and its peer dependencies.

```
npm i @chakra-ui/charts recharts
```

## [Usage](https://chakra-ui.com/docs/charts/installation#usage)
1
### [Import the charts component](https://chakra-ui.com/docs/charts/installation#import-the-charts-component)
In most cases, you need to import the `Chart` and `useChart` hook from the `@chakra-ui/charts` package, then combine them with the components `recharts`

```
import { Chart, useChart } from "@chakra-ui/charts"
import { Bar, BarChart, XAxis, YAxis } from "recharts"
```

2
### [Define chart data](https://chakra-ui.com/docs/charts/installation#define-chart-data)
Pass the chart data to the `useChart` hook to create a chart instance.
Learn more about the [`useChart`](https://chakra-ui.com/docs/charts/use-chart) hook.

```
const chart = useChart({
  data: [
    { month: "January", value: 100 },
    { month: "February", value: 200 },
  ],
})
```

3
### [Render the chart](https://chakra-ui.com/docs/charts/installation#render-the-chart)
Depending on the chart type you need from the `recharts` library, wrap the chart component within the `Chart.Root` component.

```
<Chart.Root chart={chart}>
  <BarChart data={chart.data}>
    {chart.series.map((item) => (
      <Bar
        key={item.name}
        dataKey={chart.key(item.name)}
        fill={chart.color(item.color)}
      />
    ))}
  </BarChart>
</Chart.Root>
```

## [Customization](https://chakra-ui.com/docs/charts/installation#customization)
The charts component is built on top of
### [Colors](https://chakra-ui.com/docs/charts/installation#colors)
The `useChart` hook provides a `color` function that you can use to query semantic colors for the chart component from `recharts`.

```
<CartesianGrid stroke={chart.color("border.muted")} />
```

### [Formatters](https://chakra-ui.com/docs/charts/installation#formatters)
The `useChart` hook provides a `formatDate` and `formatNumber` function that you can use to format the date and number respectively. This is useful for formatting the x, y axis labels and tooltips.

```
// format the x-axis labels
<XAxis tickFormatter={chart.formatDate({ month: "short", day: "2-digit" })} />

// format the y-axis labels
<YAxis tickFormatter={chart.formatNumber({ maximumFractionDigits: 1 })} />
```

## [FAQ](https://chakra-ui.com/docs/charts/installation#faq)
### ["lanes" is read-only error with React 19](https://chakra-ui.com/docs/charts/installation#lanes-is-read-only-error-with-react-19)
This error occurs when using recharts 3.6+ with React 19 due to a bug in
Add an override to your `package.json`:
pnpmnpmyarn

```
{
  "pnpm": {
    "overrides": {
      "immer": ">=11.0.1"
    }
  }
}
```

```
{
  "overrides": {
    "immer": ">=11.0.1"
  }
}
```

```
{
  "resolutions": {
    "immer": ">=11.0.1"
  }
}
```

Then run your package manager's install command to apply the change.
### [ResponsiveContainer vs responsive prop](https://chakra-ui.com/docs/charts/installation#responsivecontainer-vs-responsive-prop)
Use the `responsive` prop on the chart component instead of wrapping it in `ResponsiveContainer`. The `responsive` prop (available in recharts 3.3+) is the recommended approach and avoids React 19 compatibility issues that `ResponsiveContainer` can trigger due to its resize-based state updates.

```
<Chart.Root chart={chart}>
  <BarChart data={chart.data} responsive>
    {/* ... */}
  </BarChart>
</Chart.Root>
```

[ Previous Theme ](https://chakra-ui.com/docs/components/theme)[ Next useChart ](https://chakra-ui.com/docs/charts/use-chart)
On this page
[Installation](https://chakra-ui.com/docs/charts/installation#installation)[Usage](https://chakra-ui.com/docs/charts/installation#usage)[Import the charts component](https://chakra-ui.com/docs/charts/installation#import-the-charts-component)[Define chart data](https://chakra-ui.com/docs/charts/installation#define-chart-data)[Render the chart](https://chakra-ui.com/docs/charts/installation#render-the-chart)[Customization](https://chakra-ui.com/docs/charts/installation#customization)[Colors](https://chakra-ui.com/docs/charts/installation#colors)[Formatters](https://chakra-ui.com/docs/charts/installation#formatters)[FAQ](https://chakra-ui.com/docs/charts/installation#faq)["lanes" is read-only error with React 19](https://chakra-ui.com/docs/charts/installation#lanes-is-read-only-error-with-react-19)[ResponsiveContainer vs responsive prop](https://chakra-ui.com/docs/charts/installation#responsivecontainer-vs-responsive-prop)
Scroll to top
[ Master Chakra UI Learn how to build design systems with hands-on examples and expert guidance Watch Now ](https://mastery.chakra-ui.com)
