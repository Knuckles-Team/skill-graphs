##  [Tracked events](https://vercel.com/docs/observability#tracked-events)[](https://vercel.com/docs/observability#tracked-events)
Vercel tracks the following event types for Observability:
  * Edge Requests
  * Vercel Function Invocations
  * External API Requests
  * Routing Middleware Invocations
  * AI Gateway Requests


Vercel creates one or more of these events each time a request is made to your site. Depending on your application and configuration a single request to Vercel might be:
  * 1 edge request event if it's cached.
  * 1 Edge Request, 1 Middleware, 1 Function Invocation, 2 External API calls, and 1 AI Gateway request, for a total of 6 events.
  * 1 edge request event if it's a static asset.


Vercel tracks events at the team level, counting them across all projects in the team.
