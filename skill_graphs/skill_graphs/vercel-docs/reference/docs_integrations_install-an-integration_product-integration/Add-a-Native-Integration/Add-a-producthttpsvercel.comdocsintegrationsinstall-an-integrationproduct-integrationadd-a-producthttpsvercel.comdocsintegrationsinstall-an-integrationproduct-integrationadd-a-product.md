##  [Add a product](https://vercel.com/docs/integrations/install-an-integration/product-integration#add-a-product)[](https://vercel.com/docs/integrations/install-an-integration/product-integration#add-a-product)
  1. From the [Vercel dashboard](https://vercel.com/dashboard), open [Integrations](https://vercel.com/d?to=%2F%5Bteam%5D%2F%7E%2Fintegrations&title=Go+to+Integrations) in the sidebar and then the Browse Marketplace button. You can also go directly to the [Integrations Marketplace](https://vercel.com/integrations).
  2. Under the Native Integrations section, select an integration that you would like to install. You can see the details of the integration, the products available, and the pricing plans for each product.
  3. From the integration's detail page, select Install.
  4. Review the dialog showing the products available for this integration and a summary of the billing plans for each. Select Install.
  5. Then, select a pricing plan option and select Continue. The specific options available in this step depend on the type of product and the integration provider. For example, for a storage database product, you may need to select a Region for your database deployment before you can select a plan. For an AI service, you may need to select a pre-payment billing plan.
  6. Provide additional information in the next step like Database Name. Review the details and select Create. Once the integration has been installed, you are taken to the relevant integration page in the Vercel dashboard. For a storage product, this is Storage in the sidebar. You will see details about the database, pricing plan, and connection steps for your project.


###  [Using the CLI](https://vercel.com/docs/integrations/install-an-integration/product-integration#using-the-cli)[](https://vercel.com/docs/integrations/install-an-integration/product-integration#using-the-cli)
You can install integrations and provision resources directly from the command line using [`vercel integration add`](https://vercel.com/docs/cli/integration#vercel-integration-add). In the example command below, you install a [Neon integration](https://vercel.com/marketplace/neon):
terminal
```
vercel integration add neon
```

The CLI supports both interactive and non-interactive workflows. For non-interactive usage (useful for CI pipelines and AI agents), provide options as flags:
terminal
```
vercel integration add neon --name my-database --plan pro -e production -e preview
```

Run `vercel integration add <integration-name> --help` to see integration-specific options like available metadata keys and billing plans.
See the [CLI reference](https://vercel.com/docs/cli/integration#vercel-integration-add) for the full list of options.
