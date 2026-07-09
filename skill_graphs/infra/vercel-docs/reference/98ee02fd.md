# Two-factor enforcement
Last updated September 15, 2025
To enhance the security of your Vercel team, you can enforce two-factor authentication (2FA) for all team members. When enabled, members will be required to configure 2FA before they can access team resources.
What to expect:
  * Team members will not be able to access team resources until they have 2FA enabled.
  * Team members will continue to occupy a team seat.
  * Any CI/CD pipeline tokens associated with users without 2FA will cease to work.
  * Managed accounts, like service accounts or bots, will also need to have 2FA enabled.
  * Members without 2FA will be prompted to enable it when visiting the team dashboard.
  * Builds will fail for members without 2FA.
  * Notifications will continue to be sent to members without 2FA.


For more information on how to set up two-factor authentication for your account, see the [two-factor authentication](https://vercel.com/docs/two-factor-authentication) documentation.
