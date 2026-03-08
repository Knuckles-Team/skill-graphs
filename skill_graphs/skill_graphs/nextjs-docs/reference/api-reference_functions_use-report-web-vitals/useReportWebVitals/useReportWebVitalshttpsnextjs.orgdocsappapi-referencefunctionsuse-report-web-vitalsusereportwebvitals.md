## useReportWebVitals[](https://nextjs.org/docs/app/api-reference/functions/use-report-web-vitals#usereportwebvitals)
The `metric` object passed as the hook's argument consists of a number of properties:
  * `id`: Unique identifier for the metric in the context of the current page load
  * `name`: The name of the performance metric. Possible values include names of [Web Vitals](https://nextjs.org/docs/app/api-reference/functions/use-report-web-vitals#web-vitals) metrics (TTFB, FCP, LCP, FID, CLS) specific to a web application.
  * `delta`: The difference between the current value and the previous value of the metric. The value is typically in milliseconds and represents the change in the metric's value over time.
  * `entries`: An array of
  * `navigationType`: Indicates the navigation type that triggered metric collection. Values are derived from `"navigate"`, `"reload"`, `"prerender"`, `"back-forward"` (normalized from `"back_forward"`), `"back-forward-cache"` (BFCache restore), and `"restore"` (page restored after discard).
  * `rating`: A qualitative rating of the metric value, providing an assessment of the performance. Possible values are `"good"`, `"needs-improvement"`, and `"poor"`. The rating is typically determined by comparing the metric value against predefined thresholds that indicate acceptable or suboptimal performance.
  * `value`: The actual value or duration of the performance entry, typically in milliseconds. The value provides a quantitative measure of the performance aspect being tracked by the metric. The source of the value depends on the specific metric being measured and can come from various
