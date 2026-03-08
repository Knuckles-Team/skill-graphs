##  [Where](https://vercel.com/docs/logs#where)[](https://vercel.com/docs/logs#where)
The `Where` clause defines the conditions to filter your query data. It only fetches data that meets a specified condition based on several [fields](https://vercel.com/docs/query/monitoring/monitoring-reference#group-by-and-where-fields) and operators:
Operator | Description |
---|---|---
`=` | The operator that allows you to specify a single value |
`in` | The operator that allows you to specify multiple values. For example, `host in ('vercel.com', 'nextjs.com')` |
`and` | The operator that displays a query result if all the filter conditions are `TRUE` |
`or` | The operator that displays a query result if at least one of the filter conditions are `TRUE` |
`not` | The operator that displays a query result if the filter condition(s) is `NOT TRUE` |
`like` | The operator used to search a specified pattern. This is case-sensitive. For example, `host like 'acme.com'`. You can also use `_` to match any single character and `%` to match any substrings. For example, `host like 'acme_.com'` will match with `acme1.com`, `acme2.com`, and `acme3.com`. `host like 'acme%'` will also have the same matches. To do a case-insensitive search, use `ilike` |
`startsWith` | Filter data values that begin with some specific characters |
`match` | The operator used to search for patterns based on a regular expression (`match(user_agent, 'Chrome/97.*')` |
String literals must be surrounded by single quotes. For example, `host =   'vercel.com'`.
