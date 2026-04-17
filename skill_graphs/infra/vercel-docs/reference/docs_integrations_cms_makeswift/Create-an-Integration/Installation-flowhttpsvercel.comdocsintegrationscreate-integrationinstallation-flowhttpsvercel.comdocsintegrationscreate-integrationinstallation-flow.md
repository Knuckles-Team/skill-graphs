##  [Installation flow](https://vercel.com/docs/integrations/create-integration#installation-flow)[](https://vercel.com/docs/integrations/create-integration#installation-flow)
The installation of the integration is a critical component of the developer experience that must cater to all types of developers. While deciding the installation flow you should consider the following:
  * New user flow: Developers should be able to create an account on your service while installing the integration
  * Existing user flow: With existing accounts, developers should sign in as they install the integration. Also, make sure the forgotten password flow doesn't break the installation flow
  * Strong defaults: The installation flow should have minimal steps and have set defaults whenever possible
  * Advanced settings: Provide developers with the ability to override or expand settings when installing the integration


For the installation flow, you should consider adding the following specs:
Spec Name | Required | Spec Notes
---|---|---
Documentation | Yes | Explain the integration and how to use it. Also explain the defaults and how to override them.
Deploy Button | No | Create a [Deploy Button](https://vercel.com/docs/deploy-button) for projects based on a Git repository.
