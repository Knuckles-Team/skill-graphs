##  [Working with installation notifications](https://vercel.com/docs/integrations/create-integration/marketplace-api#working-with-installation-notifications)[](https://vercel.com/docs/integrations/create-integration/marketplace-api#working-with-installation-notifications)
Installation notifications appear in the Vercel dashboard to alert users about important information or actions needed for their installation. You can set notifications when creating or updating installations.
###  [Update installation notification](https://vercel.com/docs/integrations/create-integration/marketplace-api#update-installation-notification)[](https://vercel.com/docs/integrations/create-integration/marketplace-api#update-installation-notification)
Update the notification field using the [`PATCH /v1/installations/{installationId}`](https://vercel.com/docs/integrations/create-integration/marketplace-api/reference/vercel/update-installation) endpoint as shown below:
update-installation-notification.ts
```
interface Notification {
  title: string;
  message: string;
  href?: string;
  type?: 'info' | 'warning' | 'error';
}

async function updateInstallationNotification(
  installationId: string,
  notification: Notification
) {
  const response = await fetch(
    `https://api.vercel.com/v1/installations/${installationId}`,
    {
      method: 'PATCH',
      headers: {
        'Authorization': `Bearer ${token}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ notification }),
    }
  );

  if (!response.ok) {
    throw new Error(`Failed to update notification: ${response.statusText}`);
  }

  return response.json();
}

// Example usage with regular URL:
await updateInstallationNotification('icfg_abc123', {
  title: 'Action Required',
  message: 'Please complete your account setup',
  href: 'https://your-integration.com/setup',
  type: 'warning',
});

// Or with SSO-enabled URL for authenticated access:
// href: 'sso:https://your-integration.com/setup',
```

update-installation-notification-response.json
```
{
  "id": "icfg_abc123",
  "notification": {
    "title": "Action Required",
    "message": "Please complete your account setup",
    "href": "https://your-integration.com/setup",
    "type": "warning"
  }
}
```

###  [Notification types](https://vercel.com/docs/integrations/create-integration/marketplace-api#notification-types)[](https://vercel.com/docs/integrations/create-integration/marketplace-api#notification-types)
Use different notification types to indicate severity:
  * `info` - Informational message (default)
  * `warning` - Warning that requires attention
  * `error` - Error that needs immediate action


###  [SSO-enabled notification links](https://vercel.com/docs/integrations/create-integration/marketplace-api#sso-enabled-notification-links)[](https://vercel.com/docs/integrations/create-integration/marketplace-api#sso-enabled-notification-links)
The notification `href` field supports special `sso:` URLs that trigger Single Sign-On before redirecting users to your destination. This ensures users are authenticated before accessing resources on your platform.
Format:
`sso:https://your-integration.com/resource-page `
When a user clicks a notification link with an `sso:` URL:
  1. Vercel initiates the SSO flow (as described in [Vercel initiated SSO](https://vercel.com/docs/integrations/create-integration/marketplace-api#vercel-initiated-sso))
  2. Your provider validates the SSO request via the [SSO Token Exchange](https://vercel.com/docs/integrations/create-integration/marketplace-api/reference/vercel/exchange-sso-token)
  3. The user is redirected to the target URL with authenticated access


Example:
notification-with-sso.ts
```
await updateInstallationNotification('icfg_abc123', {
  title: 'Review your usage',
  message: 'Your monthly usage report is ready',
  href: 'sso:https://your-integration.com/dashboard/usage',
  type: 'info',
});
```

Use `sso:` URLs in notification links when they point to resources that require authentication on your platform. For public pages or general information, use regular HTTPS URLs.
###  [Clear notifications](https://vercel.com/docs/integrations/create-integration/marketplace-api#clear-notifications)[](https://vercel.com/docs/integrations/create-integration/marketplace-api#clear-notifications)
Remove a notification by setting it to `null`:
clear-installation-notification.ts
```
async function clearInstallationNotification(installationId: string) {
  const response = await fetch(
    `https://api.vercel.com/v1/installations/${installationId}`,
    {
      method: 'PATCH',
      headers: {
        'Authorization': `Bearer ${token}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ notification: null }),
    }
  );

  return response.json();
}
```

###  [Get installation with notification](https://vercel.com/docs/integrations/create-integration/marketplace-api#get-installation-with-notification)[](https://vercel.com/docs/integrations/create-integration/marketplace-api#get-installation-with-notification)
You can find the value of the notification field by calling the [`/v1/installations/{installationId}`](https://vercel.com/docs/integrations/create-integration/marketplace-api/reference/partner/get-installation) endpoint as shown below:
get-installation-with-notification.ts
```
async function getInstallation(installationId: string) {
  const response = await fetch(
    `https://api.vercel.com/v1/installations/${installationId}`,
    {
      headers: {
        'Authorization': `Bearer ${token}`,
      },
    }
  );

  const installation = await response.json();

  if (installation.notification) {
    console.log(`Notification: ${installation.notification.title}`);
    console.log(`Message: ${installation.notification.message}`);
  }

  return installation;
}
```
