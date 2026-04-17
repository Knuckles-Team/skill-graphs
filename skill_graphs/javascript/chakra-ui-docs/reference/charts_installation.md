Build faster with Premium Chakra UI Components 💎
[Learn more](https://pro.chakra-ui.com?utm_source=chakra-ui.com)
[Skip to Content](https://chakra-ui.com/docs/charts/installation#chakra-skip-nav)
  1. Overview
  2. Installation


# Charts
Creating beautiful charts with recharts and Chakra UI
AI TipWant to skip the docs? Use the [MCP Server](https://chakra-ui.com/docs/get-started/ai/mcp-server)
Esther
5.02K subscribers
[](https://chakra-ui.com/docs/charts/installation)
Esther
Search
Watch later
Share
Copy link
Info
Shopping
Tap to unmute
If playback doesn't begin shortly, try restarting your device.
More videos
## More videos
You're signed out
Videos you watch may be added to the TV's watch history and influence TV recommendations. To avoid this, cancel and sign in to YouTube on your computer.
CancelConfirm
Share
Include playlist
An error occurred while retrieving sharing information. Please try again later.
0:00
0:00 / 0:58
•Live
•
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

[Previous](https://chakra-ui.com/docs/components/theme)[ Next useChart ](https://chakra-ui.com/docs/charts/use-chart)
