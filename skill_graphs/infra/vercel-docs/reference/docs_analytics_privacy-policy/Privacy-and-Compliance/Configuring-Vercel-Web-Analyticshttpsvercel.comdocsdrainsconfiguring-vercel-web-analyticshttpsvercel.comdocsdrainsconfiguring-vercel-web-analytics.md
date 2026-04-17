##  [Configuring Vercel Web Analytics](https://vercel.com/docs/drains#configuring-vercel-web-analytics)[](https://vercel.com/docs/drains#configuring-vercel-web-analytics)
Some URLs and query parameters can include sensitive data and personal information (i.e. user ID, token, order ID or any other information that can individually identify a person). You have the ability to configure Vercel Web Analytics in a manner that suits your security and privacy needs to ensure that no personal information is collected in your custom events or page views, if desired.
For example, automatic page view tracking may track personal information `https://acme.com/[name of individual]/invoice/[12345]`. You can modify the URL by passing in the `beforeSend` function. For more information see our documentation on [redacting sensitive data](https://vercel.com/docs/analytics/redacting-sensitive-data).
For [custom events](https://vercel.com/docs/analytics/custom-events), you may want to prevent sending sensitive or personal information, such as email addresses, to Vercel.
* * *
[ Previous Speed Insights ](https://vercel.com/docs/speed-insights)[ Next Using Drains ](https://vercel.com/docs/drains/using-drains)
Was this helpful?
Send
On this page
  * [Data collected](https://vercel.com/docs/drains#data-collected)
  * [Visitor identification and data storage](https://vercel.com/docs/drains#visitor-identification-and-data-storage)
  * [Data point information](https://vercel.com/docs/drains#data-point-information)
  * [Configuring Vercel Web Analytics](https://vercel.com/docs/drains#configuring-vercel-web-analytics)


Copy as MarkdownGive feedbackAsk AI about this page
