##  [Firewall Alerts](https://vercel.com/docs/audit-log#firewall-alerts)[](https://vercel.com/docs/audit-log#firewall-alerts)
Firewall Alerts are available on [all plans](https://vercel.com/docs/plans)
###  [How alerts work](https://vercel.com/docs/audit-log#how-alerts-work)[](https://vercel.com/docs/audit-log#how-alerts-work)
To help protect your site effectively, you can configure alerts to be notified of potential security threats and firewall actions. To do so, you can either create a webhook and subscribe to the listener URL or subscribe to the event through the Vercel Slack app.
###  [DDoS attack alerts](https://vercel.com/docs/audit-log#ddos-attack-alerts)[](https://vercel.com/docs/audit-log#ddos-attack-alerts)
When Vercel's [DDoS Mitigation](https://vercel.com/docs/security/ddos-mitigation) detects malicious traffic on your site that exceeds 100,000 requests over a 10-minute period, an alert is generated.
To receive notifications from these alerts, you can use one of the following methods:
  * Create a [webhook](https://vercel.com/docs/webhooks) and subscribe to the URL to receive notifications
    1. Follow the [configure a webhook](https://vercel.com/docs/webhooks#configure-a-webhook) guide to create a webhook with the Attack Detected Firewall Event checked and the specific project(s) you would like to be notified about
    2. Subscribe to the created webhook URL
  * Use the [Vercel Slack app](https://vercel.com/marketplace/slack) to enable notifications for Attack Detected Firewall Events
    1. Add the Slack app for your team by following the [Use the Vercel Slack app](https://vercel.com/docs/comments/integrations#use-the-vercel-slack-app) guide
    2. Subscribe your team to DDoS attack alerts using your [`team_id`](https://vercel.com/docs/accounts#find-your-team-id)
       * Use the command `/vercel subscribe {team_id} firewall_attack`
    3. Review the [Vercel Slack app command reference](https://vercel.com/docs/comments/integrations#vercel-slack-app-command-reference) for additional options.


* * *
[ Previous Overview ](https://vercel.com/docs/security)[ Next Firewall ](https://vercel.com/docs/vercel-firewall)
Was this helpful?
Send
On this page
  * [Overview](https://vercel.com/docs/audit-log#overview)
  * [Traffic](https://vercel.com/docs/audit-log#traffic)
  * [Firewall Alerts](https://vercel.com/docs/audit-log#firewall-alerts)
  * [How alerts work](https://vercel.com/docs/audit-log#how-alerts-work)
  * [DDoS attack alerts](https://vercel.com/docs/audit-log#ddos-attack-alerts)


Copy as MarkdownGive feedbackAsk AI about this page
