##  [Getting started](https://vercel.com/docs/query#getting-started)[](https://vercel.com/docs/query#getting-started)
To start using Query, you first need to [enable Observability Plus](https://vercel.com/docs/query#enable-observability-plus). Then, you can [create a new query](https://vercel.com/docs/query#create-a-new-query) based on the metrics you want to analyze.
###  [Enable Observability Plus](https://vercel.com/docs/query#enable-observability-plus)[](https://vercel.com/docs/query#enable-observability-plus)
Enabling and disabling Observability Plus are available on [Enterprise](https://vercel.com/docs/plans/enterprise) and [Pro](https://vercel.com/docs/plans/pro) plans
Those with the [owner](https://vercel.com/docs/rbac/access-roles#owner-role) role can access this feature
  * Pro and Enterprise teams should [Upgrade to Observability Plus](https://vercel.com/docs/observability#enabling-observability-plus) to edit queries in modal.
  * Free observability users can still open a query, but they cannot modify any filters or create new queries.


[Enterprise](https://vercel.com/docs/plans/enterprise) teams can [contact sales](https://vercel.com/contact/sales) to get a customized plan based on their requirements.
###  [Create a new query](https://vercel.com/docs/query#create-a-new-query)[](https://vercel.com/docs/query#create-a-new-query)
  1. ###  [Access the Observability dashboard](https://vercel.com/docs/query#access-the-observability-dashboard)[](https://vercel.com/docs/query#access-the-observability-dashboard)
     * At the Team level: Go to the [Vercel dashboard](https://vercel.com/d?to=%2Fdashboard&title=Open+Dashboard) and click the Observability section in the sidebar
     * At the Project level: Go to the [Vercel dashboard](https://vercel.com/d?to=%2Fdashboard&title=Open+Dashboard), select the project you would like to monitor from the team switcher, and click the Observability section in the sidebar
  2. ###  [Initiate a new query](https://vercel.com/docs/query#initiate-a-new-query)[](https://vercel.com/docs/query#initiate-a-new-query)
     * Start a new query: In the Observability section, click the
     * Select a data source: Under "Visualize", select the [metric](https://vercel.com/docs/observability/query/query-reference#metric) you want to analyze such as edge requests, serverless function invocations, external API requests, or other events.
  3. ###  [Define query parameters](https://vercel.com/docs/query#define-query-parameters)[](https://vercel.com/docs/query#define-query-parameters)
     * Select the data aggregation: Select how you would like the values of your selected metric to be compiled such as sum, percentage, or per second.
     * Set Time Range: Select the time frame for the data you want to query. This can be a predefined range like "Last 24 hours" or a custom range.
     * Filter Data: Apply filters to narrow down the data. You can filter by a list of [fields](https://vercel.com/docs/query/reference#group-by-and-where-fields) such as project, path, WAF rule, edge region, etc.
  4. ###  [Visualize query](https://vercel.com/docs/query#visualize-query)[](https://vercel.com/docs/query#visualize-query)
     * View the results: The graph below the filter updates automatically as you change the filters.
     * Adjust as Needed: Refine your query parameters if needed to get precise insights.
  5. ###  [Save and share query](https://vercel.com/docs/query#save-and-share-query)[](https://vercel.com/docs/query#save-and-share-query)
     * Save the query: Once you are satisfied with your query, you can save it by clicking Add to Notebook.
     * Select a notebook: Select an existing [notebook](https://vercel.com/docs/notebooks) from the dropdown.
     * Share Query: You can share the saved query from the notebook with team members by clicking on the Share with team button.
