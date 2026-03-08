## [Testing](https://laravel.com/docs/12.x/billing#testing)
When testing an application that uses Cashier, you may mock the actual HTTP requests to the Stripe API; however, this requires you to partially re-implement Cashier's own behavior. Therefore, we recommend allowing your tests to hit the actual Stripe API. While this is slower, it provides more confidence that your application is working as expected and any slow tests may be placed within their own Pest / PHPUnit testing group.
When testing, remember that Cashier itself already has a great test suite, so you should only focus on testing the subscription and payment flow of your own application and not every underlying Cashier behavior.
To get started, add the **testing** version of your Stripe secret to your `phpunit.xml` file:
```


1<env name="STRIPE_SECRET" value="sk_test_<your-key>"/>




<env name="STRIPE_SECRET" value="sk_test_<your-key>"/>

```

Now, whenever you interact with Cashier while testing, it will send actual API requests to your Stripe testing environment. For convenience, you should pre-fill your Stripe testing account with subscriptions / prices that you may use during testing.
In order to test a variety of billing scenarios, such as credit card denials and failures, you may use the vast range of
Copy as markdown
  * [ Introduction ](https://laravel.com/docs/12.x/billing#introduction)
  * [ Upgrading Cashier ](https://laravel.com/docs/12.x/billing#upgrading-cashier)
  * [ Installation ](https://laravel.com/docs/12.x/billing#installation)
  * [ Configuration ](https://laravel.com/docs/12.x/billing#configuration)
    * [ Billable Model ](https://laravel.com/docs/12.x/billing#billable-model)
    * [ API Keys ](https://laravel.com/docs/12.x/billing#api-keys)
    * [ Currency Configuration ](https://laravel.com/docs/12.x/billing#currency-configuration)
    * [ Tax Configuration ](https://laravel.com/docs/12.x/billing#tax-configuration)
    * [ Logging ](https://laravel.com/docs/12.x/billing#logging)
    * [ Using Custom Models ](https://laravel.com/docs/12.x/billing#using-custom-models)
  * [ Quickstart ](https://laravel.com/docs/12.x/billing#quickstart)
    * [ Selling Products ](https://laravel.com/docs/12.x/billing#quickstart-selling-products)
    * [ Selling Subscriptions ](https://laravel.com/docs/12.x/billing#quickstart-selling-subscriptions)
  * [ Customers ](https://laravel.com/docs/12.x/billing#customers)
    * [ Retrieving Customers ](https://laravel.com/docs/12.x/billing#retrieving-customers)
    * [ Creating Customers ](https://laravel.com/docs/12.x/billing#creating-customers)
    * [ Updating Customers ](https://laravel.com/docs/12.x/billing#updating-customers)
    * [ Balances ](https://laravel.com/docs/12.x/billing#balances)
    * [ Tax IDs ](https://laravel.com/docs/12.x/billing#tax-ids)
    * [ Syncing Customer Data With Stripe ](https://laravel.com/docs/12.x/billing#syncing-customer-data-with-stripe)
    * [ Billing Portal ](https://laravel.com/docs/12.x/billing#billing-portal)
  * [ Payment Methods ](https://laravel.com/docs/12.x/billing#payment-methods)
    * [ Storing Payment Methods ](https://laravel.com/docs/12.x/billing#storing-payment-methods)
    * [ Retrieving Payment Methods ](https://laravel.com/docs/12.x/billing#retrieving-payment-methods)
    * [ Payment Method Presence ](https://laravel.com/docs/12.x/billing#payment-method-presence)
    * [ Updating the Default Payment Method ](https://laravel.com/docs/12.x/billing#updating-the-default-payment-method)
    * [ Adding Payment Methods ](https://laravel.com/docs/12.x/billing#adding-payment-methods)
    * [ Deleting Payment Methods ](https://laravel.com/docs/12.x/billing#deleting-payment-methods)
  * [ Subscriptions ](https://laravel.com/docs/12.x/billing#subscriptions)
    * [ Creating Subscriptions ](https://laravel.com/docs/12.x/billing#creating-subscriptions)
    * [ Checking Subscription Status ](https://laravel.com/docs/12.x/billing#checking-subscription-status)
    * [ Changing Prices ](https://laravel.com/docs/12.x/billing#changing-prices)
    * [ Subscription Quantity ](https://laravel.com/docs/12.x/billing#subscription-quantity)
    * [ Subscriptions With Multiple Products ](https://laravel.com/docs/12.x/billing#subscriptions-with-multiple-products)
    * [ Multiple Subscriptions ](https://laravel.com/docs/12.x/billing#multiple-subscriptions)
    * [ Usage Based Billing ](https://laravel.com/docs/12.x/billing#usage-based-billing)
    * [ Subscription Taxes ](https://laravel.com/docs/12.x/billing#subscription-taxes)
    * [ Subscription Anchor Date ](https://laravel.com/docs/12.x/billing#subscription-anchor-date)
    * [ Canceling Subscriptions ](https://laravel.com/docs/12.x/billing#cancelling-subscriptions)
    * [ Resuming Subscriptions ](https://laravel.com/docs/12.x/billing#resuming-subscriptions)
  * [ Subscription Trials ](https://laravel.com/docs/12.x/billing#subscription-trials)
    * [ With Payment Method Up Front ](https://laravel.com/docs/12.x/billing#with-payment-method-up-front)
    * [ Without Payment Method Up Front ](https://laravel.com/docs/12.x/billing#without-payment-method-up-front)
    * [ Extending Trials ](https://laravel.com/docs/12.x/billing#extending-trials)
  * [ Handling Stripe Webhooks ](https://laravel.com/docs/12.x/billing#handling-stripe-webhooks)
    * [ Defining Webhook Event Handlers ](https://laravel.com/docs/12.x/billing#defining-webhook-event-handlers)
    * [ Verifying Webhook Signatures ](https://laravel.com/docs/12.x/billing#verifying-webhook-signatures)
  * [ Single Charges ](https://laravel.com/docs/12.x/billing#single-charges)
    * [ Simple Charge ](https://laravel.com/docs/12.x/billing#simple-charge)
    * [ Charge With Invoice ](https://laravel.com/docs/12.x/billing#charge-with-invoice)
    * [ Creating Payment Intents ](https://laravel.com/docs/12.x/billing#creating-payment-intents)
    * [ Refunding Charges ](https://laravel.com/docs/12.x/billing#refunding-charges)
  * [ Invoices ](https://laravel.com/docs/12.x/billing#invoices)
    * [ Retrieving Invoices ](https://laravel.com/docs/12.x/billing#retrieving-invoices)
    * [ Upcoming Invoices ](https://laravel.com/docs/12.x/billing#upcoming-invoices)
    * [ Previewing Subscription Invoices ](https://laravel.com/docs/12.x/billing#previewing-subscription-invoices)
    * [ Generating Invoice PDFs ](https://laravel.com/docs/12.x/billing#generating-invoice-pdfs)
  * [ Checkout ](https://laravel.com/docs/12.x/billing#checkout)
    * [ Product Checkouts ](https://laravel.com/docs/12.x/billing#product-checkouts)
    * [ Single Charge Checkouts ](https://laravel.com/docs/12.x/billing#single-charge-checkouts)
    * [ Subscription Checkouts ](https://laravel.com/docs/12.x/billing#subscription-checkouts)
    * [ Collecting Tax IDs ](https://laravel.com/docs/12.x/billing#collecting-tax-ids)
    * [ Guest Checkouts ](https://laravel.com/docs/12.x/billing#guest-checkouts)
  * [ Handling Failed Payments ](https://laravel.com/docs/12.x/billing#handling-failed-payments)
    * [ Confirming Payments ](https://laravel.com/docs/12.x/billing#confirming-payments)
  * [ Strong Customer Authentication (SCA) ](https://laravel.com/docs/12.x/billing#strong-customer-authentication)
    * [ Payments Requiring Additional Confirmation ](https://laravel.com/docs/12.x/billing#payments-requiring-additional-confirmation)
    * [ Off-session Payment Notifications ](https://laravel.com/docs/12.x/billing#off-session-payment-notifications)
  * [ Stripe SDK ](https://laravel.com/docs/12.x/billing#stripe-sdk)
  * [ Testing ](https://laravel.com/docs/12.x/billing#testing)


[ ![Laravel Nightwatch](https://laravel.com/images/ads/nightwatch-logo.svg) First-class monitoring and deep insights for Laravel apps Learn more  ](https://nightwatch.laravel.com)
[ ![Laravel Forge](https://laravel.com/images/ads/forge-logo.svg) Server management made simple for any PHP app Learn more  ](https://forge.laravel.com)
[ ![Laravel Cloud](https://laravel.com/images/ads/cloud-logo.svg) The fastest way to deploy and scale Laravel apps Learn more  ](https://cloud.laravel.com)
[ ![Laravel Boost](https://laravel.com/images/ads/boost-logo.svg) Supercharge your AI development with essential context Learn more  ](https://laravel.com/ai/boost)
Laravel is the most productive way to
build, deploy, and monitor software.
  * © 2026 Laravel
  * [ Legal ](https://laravel.com/legal)
  * [ Status ](https://status.laravel.com/)


####  Products
  * [ Cloud ](https://cloud.laravel.com)
  * [ Forge ](https://forge.laravel.com)
  * [ Nightwatch ](https://nightwatch.laravel.com)
  * [ Vapor ](https://vapor.laravel.com)
  * [ Nova ](https://nova.laravel.com)


####  Packages
  * [ Cashier ](https://laravel.com/docs/cashier)
  * [ Dusk ](https://laravel.com/docs/dusk)
  * [ Horizon ](https://laravel.com/docs/horizon)
  * [ Octane ](https://laravel.com/docs/octane)
  * [ Scout ](https://laravel.com/docs/scout)
  * [ Pennant ](https://laravel.com/docs/pennant)
  * [ Pint ](https://laravel.com/docs/pint)
  * [ Sail ](https://laravel.com/docs/sail)
  * [ Sanctum ](https://laravel.com/docs/sanctum)
  * [ Socialite ](https://laravel.com/docs/socialite)
  * [ Telescope ](https://laravel.com/docs/telescope)
  * [ Pulse ](https://laravel.com/docs/pulse)
  * [ Reverb ](https://laravel.com/docs/reverb)
  * [ Echo ](https://laravel.com/docs/broadcasting)


####  Resources
  * [ Documentation ](https://laravel.com/docs)
  * [ Starter Kits ](https://laravel.com/starter-kits)
  * [ Release Notes ](https://laravel.com/docs/releases)
  * [ Blog ](https://laravel.com/blog)
  * [ Community ](https://laravel.com/community)
  * [ Learn ](https://laravel.com/learn)
  * [ Careers ](https://laravel.com/careers)
  * [ Trust ](https://trust.laravel.com)


####  Partners
  *   * [Vehikl](https://partners.laravel.com/partners/vehikl)
  * [Kirschbaum](https://partners.laravel.com/partners/kirschbaum)
  * [byte5](https://partners.laravel.com/partners/byte5)
  * [Tighten](https://partners.laravel.com/partners/tighten)
  * [Redberry](https://partners.laravel.com/partners/redberry)
  * [Curotec](https://partners.laravel.com/partners/curotec)
  * [Jump24](https://partners.laravel.com/partners/jump24)
  * [Active Logic](https://partners.laravel.com/partners/active-logic)
  * [ More Partners ](https://partners.laravel.com)
