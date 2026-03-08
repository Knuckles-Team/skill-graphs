##  [Creating an Edge Config](https://vercel.com/docs/edge-config/edge-config-dashboard#creating-an-edge-config)[](https://vercel.com/docs/edge-config/edge-config-dashboard#creating-an-edge-config)
###  [At the account level](https://vercel.com/docs/edge-config/edge-config-dashboard#at-the-account-level)[](https://vercel.com/docs/edge-config/edge-config-dashboard#at-the-account-level)
To add an Edge Config at the Hobby team or team level, follow these steps:
  1. Make sure that you are in the correct account or team in your [dashboard](https://vercel.com/d?to=%2Fdashboard&title=Open+Dashboard)
  2. Click on the Storage section in the sidebar
  3. Click the Create Store button
  4. Type a name for your Edge Config in the dialog and click Create. The name shouldn't exceed 32 characters and can only contain alphanumeric letters, "_", and "-".
  5. On creation, you are taken to the `my_edge_config_id` config page. By default, a key-value pair of `"greeting": "hello world"` is created. On the detail page of the newly created Edge Config you can:
     * View and manage stored items
     * Connect projects to and disconnect projects from this Edge Config
     * Generate, copy, and delete tokens associated with this Edge Config


Your Edge Config is now ready to be used. You can also [create an Edge Config at the project level](https://vercel.com/docs/edge-config/edge-config-dashboard#at-the-project-level).
If you're creating a project at the account-level, we won't automatically create a token, connection string, and environment variable until a project has been connected.
###  [At the project level](https://vercel.com/docs/edge-config/edge-config-dashboard#at-the-project-level)[](https://vercel.com/docs/edge-config/edge-config-dashboard#at-the-project-level)
  1. Navigate to your [project](https://vercel.com/docs/projects/overview) page and click on the Edge Config section in the sidebar
  2. Click Create Project Store and type a name slug for your Edge Config in the dialog that opens. The name shouldn't exceed 32 characters and can only contain alphanumeric letters, "_", and "-".
  3. Click Create.
  4. Once created, you can click on the Edge Config to [manage it](https://vercel.com/docs/edge-config/edge-config-dashboard#managing-edge-configs). The following items are automatically created:
     * An environment variable `EDGE_CONFIG` that holds a [connection string](https://vercel.com/docs/edge-config/using-edge-config#using-a-connection-string). If you go to your project's Settings > Environment Variables, you'll see the newly created environment variable.
     * A [read access token](https://vercel.com/docs/edge-config/using-edge-config#creating-a-read-access-token). This token, along with your EDGE CONFIG ID is used to create a [connection string](https://vercel.com/docs/edge-config/using-edge-config#using-a-connection-string). This connection string is saved as the value of your `EDGE_CONFIG` environment variable. Using this enables you to use the SDK in your project to read the contents of the store.
