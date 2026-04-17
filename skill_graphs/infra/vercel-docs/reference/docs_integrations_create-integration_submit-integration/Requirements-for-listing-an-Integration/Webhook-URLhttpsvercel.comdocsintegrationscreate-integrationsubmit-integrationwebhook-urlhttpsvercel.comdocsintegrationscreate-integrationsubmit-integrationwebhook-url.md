##  [Webhook URL](https://vercel.com/docs/integrations/create-integration/submit-integration#webhook-url)[](https://vercel.com/docs/integrations/create-integration/submit-integration#webhook-url)
  * Required: No


With your integration, you can listen for events on the Vercel platform through Webhooks. The following events are available:
###  [Deployment events](https://vercel.com/docs/integrations/create-integration/submit-integration#deployment-events)[](https://vercel.com/docs/integrations/create-integration/submit-integration#deployment-events)
The following events are available for deployments:
  * [`deployment.created`](https://vercel.com/docs/webhooks/webhooks-api#deployment.created)
  * [`deployment.error`](https://vercel.com/docs/webhooks/webhooks-api#deployment.error)
  * [`deployment.canceled`](https://vercel.com/docs/webhooks/webhooks-api#deployment.canceled)
  * [`deployment.succeeded`](https://vercel.com/docs/webhooks/webhooks-api#deployment.succeeded)


###  [Configuration events](https://vercel.com/docs/integrations/create-integration/submit-integration#configuration-events)[](https://vercel.com/docs/integrations/create-integration/submit-integration#configuration-events)
The following events are available for configurations:
  * [`integration-configuration.permission-upgraded`](https://vercel.com/docs/webhooks/webhooks-api#integration-configuration.permission-upgraded)
  * [`integration-configuration.removed`](https://vercel.com/docs/webhooks/webhooks-api#integration-configuration.removed)
  * [`integration-configuration.scope-change-confirmed`](https://vercel.com/docs/webhooks/webhooks-api#integration-configuration.scope-change-confirmed)
  * [`integration-configuration.transferred`](https://vercel.com/docs/webhooks/webhooks-api#integration-configuration.transferred)


###  [Domain events](https://vercel.com/docs/integrations/create-integration/submit-integration#domain-events)[](https://vercel.com/docs/integrations/create-integration/submit-integration#domain-events)
The following events are available for domains:
  * [`domain.created`](https://vercel.com/docs/webhooks/webhooks-api#domain.created)


###  [Project events](https://vercel.com/docs/integrations/create-integration/submit-integration#project-events)[](https://vercel.com/docs/integrations/create-integration/submit-integration#project-events)
The following events are available for projects:
  * [`project.created`](https://vercel.com/docs/webhooks/webhooks-api#project.created)
  * [`project.removed`](https://vercel.com/docs/webhooks/webhooks-api#project.removed)


###  [Check events](https://vercel.com/docs/integrations/create-integration/submit-integration#check-events)[](https://vercel.com/docs/integrations/create-integration/submit-integration#check-events)
The following events are available for checks:
  * [`deployment.ready`](https://vercel.com/docs/webhooks/webhooks-api#deployment-ready)
  * [`deployment.check-rerequested`](https://vercel.com/docs/webhooks/webhooks-api#deployment-check-rerequested)


See the [Webhooks](https://vercel.com/docs/webhooks) documentation to learn more.
