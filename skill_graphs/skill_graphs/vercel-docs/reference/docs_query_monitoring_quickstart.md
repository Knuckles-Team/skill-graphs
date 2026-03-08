[Query](https://vercel.com/docs/query)
[Monitoring](https://vercel.com/docs/query/monitoring)
Getting Started
[Query](https://vercel.com/docs/query)
[Monitoring](https://vercel.com/docs/query/monitoring)
Getting Started
# Monitoring Quickstart
Last updated January 7, 2026
Monitoring is now [deprecated](https://vercel.com/docs/query/monitoring#monitoring-sunset). It is no longer available for Pro users or Enterprise customers who subscribed to Observability Plus after June 2025.
[Observability Plus](https://vercel.com/docs/observability/observability-plus) includes [Observability Query](https://vercel.com/docs/observability/query) for monitoring your project.
##  [Prerequisites](https://vercel.com/docs/query/monitoring/quickstart#prerequisites)[](https://vercel.com/docs/query/monitoring/quickstart#prerequisites)
  * Make sure you upgrade to [Pro](https://vercel.com/docs/plans/pro-plan) or [Enterprise](https://vercel.com/docs/plans/enterprise) plan.
  * Pro and Enterprise teams should [Upgrade to Observability Plus](https://vercel.com/docs/observability#enabling-observability-plus) to access Monitoring.


##  [Create a new query](https://vercel.com/docs/query/monitoring/quickstart#create-a-new-query)[](https://vercel.com/docs/query/monitoring/quickstart#create-a-new-query)
In the following guide you will learn how to view the most requested posts on your website.
  1. ###  [Go to the dashboard](https://vercel.com/docs/query/monitoring/quickstart#go-to-the-dashboard)[](https://vercel.com/docs/query/monitoring/quickstart#go-to-the-dashboard)
    1. Open [Observability](https://vercel.com/d?to=%2F%5Bteam%5D%2F%5Bproject%5D%2Fobservability&title=Go+to+Observability) in the sidebar from your Vercel [dashboard](https://vercel.com/dashboard)
    2. Click the Create New Query button to open the query builder
    3. Click the Edit Query button to configure your query with clauses
  2. ###  [Add Visualize clause](https://vercel.com/docs/query/monitoring/quickstart#add-visualize-clause)[](https://vercel.com/docs/query/monitoring/quickstart#add-visualize-clause)
The [Visualize](https://vercel.com/docs/observability/monitoring/monitoring-reference#visualize%22) clause specifies which field in your query will be calculated. Set the Visualize clause to `requests` to monitor the most popular posts on your website.
Click the Run Query button, and the [Monitoring chart](https://vercel.com/docs/observability/monitoring#monitoring-chart) will display the total number of requests made.
  3. ###  [Add Where clause](https://vercel.com/docs/query/monitoring/quickstart#add-where-clause)[](https://vercel.com/docs/query/monitoring/quickstart#add-where-clause)
To filter the query data, use the [Where](https://vercel.com/docs/observability/monitoring/monitoring-reference#where) clause and specify the conditions you want to match against. You can use a combination of [variables and operators](https://vercel.com/docs/observability/monitoring/monitoring-reference#where) to fetch the most requested posts. Add the following query statement to the Where clause:
```
host = 'my-site.com' and like(request_path, '/posts%')
```

This query retrieves data with a host field of `my-site.com` and a `request_path` field that starts with /posts.
The `%` character can be used as a wildcard to match any sequence of characters after `/posts`, allowing you to capture all `request_path` values that start with that substring.
  4. ###  [Add Group By clause](https://vercel.com/docs/query/monitoring/quickstart#add-group-by-clause)[](https://vercel.com/docs/query/monitoring/quickstart#add-group-by-clause)
Define a criteria that groups the data based on the selected attributes. The grouping mechanism is supported through the [Group By](https://vercel.com/docs/observability/monitoring/monitoring-reference#group-by) clause.
Set the Group By clause to `request_path`.
With Visualize, Where, and Group By fields set, the [Monitoring chart](https://vercel.com/docs/observability/monitoring#monitoring-chart) now shows the sum of `requests` that are filtered based on the `request_path`.
  5. ###  [Add Limit clause](https://vercel.com/docs/query/monitoring/quickstart#add-limit-clause)[](https://vercel.com/docs/query/monitoring/quickstart#add-limit-clause)
To control the number of results returned by the query, use the [Limit](https://vercel.com/docs/observability/monitoring/monitoring-reference#limit) clause and specify the desired number of results. You can choose from a few options, such as 5, 10, 25, 50, or 100 query results. For this example, set the limit to 5 query results.
  6. ###  [Save and Run Query](https://vercel.com/docs/query/monitoring/quickstart#save-and-run-query)[](https://vercel.com/docs/query/monitoring/quickstart#save-and-run-query)
Save your query and click the **Run Query** button to generate the final results. The Monitoring chart will display a comprehensive view of the top 5 most requested posts on your website.


* * *
[ Previous Monitoring ](https://vercel.com/docs/query/monitoring)[ Next Monitoring Reference ](https://vercel.com/docs/query/monitoring/monitoring-reference)
Was this helpful?
Send
