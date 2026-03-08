##  [Notifications](https://vercel.com/docs/comments/managing-comments#notifications)[](https://vercel.com/docs/comments/managing-comments#notifications)
By default, the activity within a comment thread triggers a notification for all participants in the thread. PR owners will also receive notifications for all newly-created comment threads.
Activities that trigger a notification include:
  * Someone creating a comment thread
  * Someone replying in a comment thread you have enabled notifications for or participated in
  * Someone resolving a comment thread you're receiving notifications for


Whenever there's new activity within a comment thread, you'll receive a new notification. Notifications can be sent to:
  * [Your Vercel Dashboard](https://vercel.com/docs/comments/managing-comments#dashboard-notifications)
  * [Email](https://vercel.com/docs/comments/managing-comments#email)
  * [Slack](https://vercel.com/docs/comments/managing-comments#slack)


###  [Customizing notifications for deployments](https://vercel.com/docs/comments/managing-comments#customizing-notifications-for-deployments)[](https://vercel.com/docs/comments/managing-comments#customizing-notifications-for-deployments)
To customize notifications for a deployment:
  1. Visit the deployment
  2. Log into the Vercel toolbar
  3. Select the Menu button (☰)
  4. Select Preferences (⚙)
  5. In the dropdown beside Notifications, select:
     * Never: To disable notifications
     * All: To enable notifications
     * Replies and Mentions: To enable only some notifications


###  [Customizing thread notifications](https://vercel.com/docs/comments/managing-comments#customizing-thread-notifications)[](https://vercel.com/docs/comments/managing-comments#customizing-thread-notifications)
You can manage notifications for threads in the Inbox:
  1. Select the three dots (ellipses) near the top of the first comment in a thread
  2. Select Unfollow to mute the thread, or Follow to subscribe to the thread


###  [Dashboard notifications](https://vercel.com/docs/comments/managing-comments#dashboard-notifications)[](https://vercel.com/docs/comments/managing-comments#dashboard-notifications)
While logged into Vercel, select the notification bell icon and open Comments in the sidebar to see new Comments notifications. To view specific comments, you can:
  * Filter based on:
    * Author
    * Status
    * Project
    * Page
    * Branch
  * Search: Search for comments containing specific text


Comments left on pages with query params in the URL may not appear on the page when you visit the base URL. Filter by page and search with a `*` wildcard to see all pages with similar URLs. For example, you might search for `/docs/conformance/rules/req*`.
You can also resolve comments from your notifications.
To reply to a comment, or view the deployment it was made on, select it and select the link to the deployment.
###  [Email](https://vercel.com/docs/comments/managing-comments#email)[](https://vercel.com/docs/comments/managing-comments#email)
Email notifications will be sent to the email address associated with your Vercel account. Multiple notifications within a short period will be batched into a single email.
###  [Slack](https://vercel.com/docs/comments/managing-comments#slack)[](https://vercel.com/docs/comments/managing-comments#slack)
When you configure Vercel's Slack integration, comment threads on linked branches will create Slack threads. New activity on Slack or in the comment thread will be reflected on both platforms. See [our Slack integration docs](https://vercel.com/docs/comments/integrations#commenting-in-slack) to learn more.
