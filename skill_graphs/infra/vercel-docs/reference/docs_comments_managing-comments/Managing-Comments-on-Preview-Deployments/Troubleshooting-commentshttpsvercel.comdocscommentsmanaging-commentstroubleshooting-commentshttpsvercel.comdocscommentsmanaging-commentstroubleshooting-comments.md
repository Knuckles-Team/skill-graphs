##  [Troubleshooting comments](https://vercel.com/docs/comments/managing-comments#troubleshooting-comments)[](https://vercel.com/docs/comments/managing-comments#troubleshooting-comments)
Sometimes, issues appear on a webpage for certain browsers and devices, but not for others. It's also possible for users to leave comments on a preview while viewing an outdated deployment.
To get around this issue, you can select the screen icon beside a commenter's name to copy their session info to your clipboard. Doing so will yield a JSON object similar to the following:
session-data
```
{
  "browserInfo": {
    "ua": "Mozilla/5.0 (Macintosh; Intel Mac OS X 9_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
    "browser": {
      "name": "Chrome",
      "version": "106.0.0.0",
      "major": "106"
    },
    "engine": {
      "name": "Blink",
      "version": "106.0.0.0"
    },
    "os": {
      "name": "Mac OS",
      "version": "10.15.7"
    },
    "device": {},
    "cpu": {}
  },
  "screenWidth": 1619,
  "screenHeight": 1284,
  "devicePixelRatio": 1.7999999523162842,
  "deploymentUrl": "vercel-site-7p6d5t8vq.vercel.sh"
}
```

On desktop, you can hover your cursor over a comment's timestamp to view less detailed session information at a glance, including:
  * Browser name and version
  * Window dimensions in pixels
  * Device pixel ratio
  * Which deployment they were viewing

![A comment's browsing session information.](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fpreview-deployments%2Fcomments%2Fdebug-info-light.png&w=1920&q=75)![A comment's browsing session information.](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fpreview-deployments%2Fcomments%2Fdebug-info-dark.png&w=1920&q=75)A comment's browsing session information.
* * *
[ Previous Using Comments ](https://vercel.com/docs/comments/using-comments)[ Next Integrations ](https://vercel.com/docs/comments/integrations)
Was this helpful?
Send
On this page
  * [Resolve comments](https://vercel.com/docs/comments/managing-comments#resolve-comments)
  * [Notifications](https://vercel.com/docs/comments/managing-comments#notifications)
  * [Customizing notifications for deployments](https://vercel.com/docs/comments/managing-comments#customizing-notifications-for-deployments)
  * [Customizing thread notifications](https://vercel.com/docs/comments/managing-comments#customizing-thread-notifications)
  * [Dashboard notifications](https://vercel.com/docs/comments/managing-comments#dashboard-notifications)
  * [Email](https://vercel.com/docs/comments/managing-comments#email)
  * [Slack](https://vercel.com/docs/comments/managing-comments#slack)
  * [Troubleshooting comments](https://vercel.com/docs/comments/managing-comments#troubleshooting-comments)


Copy as MarkdownGive feedbackAsk AI about this page
