##  [How the scores are determined](https://vercel.com/docs/logs#how-the-scores-are-determined)[](https://vercel.com/docs/logs#how-the-scores-are-determined)
Vercel calculates performance scores using real-world data obtained from the [First Contentful Paint (FCP)](https://vercel.com/docs/logs#first-contentful-paint-fcp)) a score ranging from 0 to 100. The score is determined based on where the raw metric value falls within a log-normal distribution derived from actual website performance data.
For instance, if
The Real Experience Score is a weighted average of all individual metric scores. Vercel has assigned each metric a specific weighting, which best represents user's perceived performance on mobile and desktop devices.
Device type
Mobile Desktop
Metric | Value | Score | Weight
---|---|---|---
FCP |  s | 89 | 15%
LCP |  s | 93 | 30%
INP |  ms | 96 | 30%
CLS |  | 84 | 25%
Real Experience Score
Gauge showing computed score and metrics 91FCPFirst Contentful paint. Good <= 1.8s, Improvable <= 3sLCPLarge Contentful Paint. Good <= 2.5s, Improvable <= 4sINPInteraction to Next Paint. Good <= 200ms, Improvable <= 500msCLSCumulative Layout Shift. Good <= 0.1, Improvable <= 0.25
