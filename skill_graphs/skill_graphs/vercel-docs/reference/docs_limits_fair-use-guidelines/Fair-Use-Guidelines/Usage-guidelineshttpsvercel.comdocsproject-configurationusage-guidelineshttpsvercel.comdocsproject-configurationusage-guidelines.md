##  [Usage guidelines](https://vercel.com/docs/project-configuration#usage-guidelines)[](https://vercel.com/docs/project-configuration#usage-guidelines)
As a guideline for our community, we expect most users to fall within the below ranges for each plan. We will notify you if your usage is an outlier. Our goal is to be as permissive as possible while not allowing an unreasonable burden on our infrastructure. Where possible, we'll reach out to you ahead of any action we take to address unreasonable usage and work with you to correct it.
###  [Typical monthly usage guidelines](https://vercel.com/docs/project-configuration#typical-monthly-usage-guidelines)[](https://vercel.com/docs/project-configuration#typical-monthly-usage-guidelines)
| Hobby | Pro
---|---|---
Fast Data Transfer | Up to 100 GB | Up to 1 TB
Fast Origin Transfer | Up to 10 GB | Up to 100 GB
Function Execution | Up to 100 GB-Hrs | Up to 1000 GB-Hrs
Build Execution | Up to 100 Hrs | Up to 400 Hrs
[Image transformations](https://vercel.com/docs/image-optimization/limits-and-pricing#image-transformations) | Up to 5K transformations/month | Up to 10K transformations/month
[Image cache reads](https://vercel.com/docs/image-optimization/limits-and-pricing#image-cache-reads) | Up to 300K reads/month | Up to 600K reads/month
[Image cache writes](https://vercel.com/docs/image-optimization/limits-and-pricing#image-cache-writes) | Up to 100K writes/month | Up to 200K writes/month
Storage | [Edge Config](https://vercel.com/docs/edge-config/edge-config-limits) | [Edge Config](https://vercel.com/docs/edge-config/edge-config-limits)
For Teams on the Pro plan, you can pay for [additional usage](https://vercel.com/docs/limits/fair-use-guidelines#additional-resources) as you go.
###  [Other guidelines](https://vercel.com/docs/project-configuration#other-guidelines)[](https://vercel.com/docs/project-configuration#other-guidelines)
Middleware with the `edge` runtime configured CPU Limits - Middleware with the `edge` runtime configured can use no more than 50ms of CPU time on average. This limitation refers to the actual net CPU time, not the execution time. For example, when you are blocked from talking to the network, the time spent waiting for a response does not count toward CPU time limitations.
For [on-demand concurrent builds](https://vercel.com/docs/builds/managing-builds#on-demand-concurrent-builds), there is a fair usage limit of 500 concurrent builds per team. If you exceed this limit, any new on-demand build request will be queued until your total concurrent builds goes below 500.
###  [Additional resources](https://vercel.com/docs/project-configuration#additional-resources)[](https://vercel.com/docs/project-configuration#additional-resources)
For members of our Pro plan, we offer a pay-as-you-go model for additional usage, giving you greater flexibility and control over your usage. The typical monthly usage guidelines above are still applicable, while extra usage will be automatically charged at the following rates:
| Pro
---|---
Fast Data Transfer | [Regionally priced](https://vercel.com/docs/pricing/regional-pricing)
Fast Origin Transfer | [Regionally priced](https://vercel.com/docs/pricing/regional-pricing)
Function Execution | $0.60 per 1 GB-Hrs increment
[Image Optimization Source Images](https://vercel.com/docs/image-optimization/legacy-pricing#source-images) | $5 per 1000 increment
###  [Commercial usage](https://vercel.com/docs/project-configuration#commercial-usage)[](https://vercel.com/docs/project-configuration#commercial-usage)
Hobby teams are restricted to non-commercial personal use only. All commercial usage of the platform requires either a Pro or Enterprise plan.
Commercial usage is defined as any [Deployment](https://vercel.com/docs/deployments) that is used for the purpose of financial gain of anyone involved in any part of the production of the project, including a paid employee or consultant writing the code. Examples of this include, but are not limited to, the following:
  * Any method of requesting or processing payment from visitors of the site
  * Advertising the sale of a product or service
  * Receiving payment to create, update, or host the site
  * Affiliate linking is the primary purpose of the site
  * The inclusion of advertisements, including but not limited to online advertising platforms like Google AdSense


Asking for Donations **does not** fall under commercial usage.
If you are unsure whether or not your site would be defined as commercial usage, please [contact the Vercel Support team](https://vercel.com/help#issues).
###  [General Limits](https://vercel.com/docs/project-configuration#general-limits)[](https://vercel.com/docs/project-configuration#general-limits)
[Take a look at our Limits documentation](https://vercel.com/docs/limits#general-limits) for the limits we apply to all accounts.
###  [Learn More](https://vercel.com/docs/project-configuration#learn-more)[](https://vercel.com/docs/project-configuration#learn-more)
Circumventing or otherwise misusing Vercel's limits or usage guidelines is a violation of our fair use guidelines.
For further information regarding these guidelines and acceptable use of our services, refer to our [Terms of Service](https://vercel.com/legal/terms#fair-use) or your Enterprise Service Agreement.
* * *
[ Previous Observability/ Debug Cache Issues ](https://vercel.com/docs/cdn-cache/debug-cache-issues)[ Next vercel.json ](https://vercel.com/docs/project-configuration/vercel-json)
Was this helpful?
Send
On this page
  * [Examples of fair use](https://vercel.com/docs/project-configuration#examples-of-fair-use)
  * [Never fair use](https://vercel.com/docs/project-configuration#never-fair-use)
  * [Usage guidelines](https://vercel.com/docs/project-configuration#usage-guidelines)
  * [Typical monthly usage guidelines](https://vercel.com/docs/project-configuration#typical-monthly-usage-guidelines)
  * [Other guidelines](https://vercel.com/docs/project-configuration#other-guidelines)
  * [Additional resources](https://vercel.com/docs/project-configuration#additional-resources)
  * [Commercial usage](https://vercel.com/docs/project-configuration#commercial-usage)
  * [General Limits](https://vercel.com/docs/project-configuration#general-limits)
  * [Learn More](https://vercel.com/docs/project-configuration#learn-more)


Copy as MarkdownGive feedbackAsk AI about this page
