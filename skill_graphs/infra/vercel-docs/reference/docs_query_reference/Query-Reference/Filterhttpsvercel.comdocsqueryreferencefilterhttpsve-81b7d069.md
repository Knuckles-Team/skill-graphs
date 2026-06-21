##  [Filter](https://vercel.com/docs/query/reference#filter)[](https://vercel.com/docs/query/reference#filter)
The filter bar defines the conditions to filter your query data. It only fetches data that meets a specified condition based on several [fields](https://vercel.com/docs/query/monitoring/monitoring-reference#group-by-and-where-fields) and operators:
Operator | Description |
---|---|---
`is`, `is not` | The operator that allows you to specify a single value |
`is any of `, `is not any of` | The operator that allows you to specify multiple values. For example, `host in ('vercel.com', 'nextjs.com')` |
`startsWith` | Filter data values that begin with some specific characters |
`endsWith` | Filter data values that end with specific characters |
`>,>=,<,<=` | Numerical operators that allow numerical comparisons |
