##  [Team installations](https://vercel.com/docs/integrations/create-integration/native-integration#team-installations)[](https://vercel.com/docs/integrations/create-integration/native-integration#team-installations)
Team installations are the foundation of native integrations, providing a secure and organized way to connect user teams with specific integrations. You can then enable centralized management and access control to integration resources through the Vercel dashboard.
Installations represent a connection between a Vercel team and your system. They are team-scoped, not user-scoped, meaning they belong to the entire team rather than the individual who installed them. Therefore, if the user who created an installation leaves the team, the installation remains active and accessible to other team members with appropriate permissions.
Because installations are tied to teams and not individual users, use the [Get Account Information endpoint](https://vercel.com/docs/integrations/create-integration/marketplace-api/reference/vercel/get-account-info) to get current team contact information rather than relying on the original installing user's details.
Concept | Definition
---|---
Team installation | The primary connection between a user's team and a specific integration.
[`installationId`](https://vercel.com/docs/integrations/marketplace-api#installations) | The main partition key connecting the user's team to the integration.
###  [Reinstallation behavior](https://vercel.com/docs/integrations/create-integration/native-integration#reinstallation-behavior)[](https://vercel.com/docs/integrations/create-integration/native-integration#reinstallation-behavior)
If a team uninstalls and then reinstalls your integration, Vercel creates a new `installationId`. Treat this as a completely new installation with no assumptions about previous configuration, billing, or resource states from the earlier installation.
###  [Limits](https://vercel.com/docs/integrations/create-integration/native-integration#limits)[](https://vercel.com/docs/integrations/create-integration/native-integration#limits)
Understanding the limits of team installation instances for all types of integrations can help you design a better integration architecture.
A Vercel team can only have one native integration installation at a time. If a team wants to install the integration again, they need to uninstall the existing installation first. This helps maintain clarity in billing and resource management.
Metric | Limit
---|---
[Native integration](https://vercel.com/docs/integrations#native-integrations) installation | A maximum of one installation instance of a specific provider's native integration per team.
[Connectable account integration](https://vercel.com/docs/integrations/create-integration#connectable-account-integrations) installation | A maximum of one installation instance of a specific provider's connectable account integration per team.
A team can have both a native integration installation and a connectable account integration installation for the same integration if you've set up both on the same integration configuration. In this case, there are technically two installations, and you should treat each one as independent even if you can correlate them in your system.
