# Vercel Authentication
Last updated September 15, 2025
Vercel Authentication is available on [all plans](https://vercel.com/docs/plans)
Those with the [owner](https://vercel.com/docs/rbac/access-roles#owner-role), [member](https://vercel.com/docs/rbac/access-roles#member-role) and [admin](https://vercel.com/docs/rbac/access-roles#admin-role) roles can manage Vercel Authentication
Vercel Authentication lets you restrict access to your public and non-public deployments. It is the recommended approach to protecting your deployments, and available on all plans. When enabled, it allows only users with deployment access to view and comment on your site.
Users attempting to access the deployment will encounter a Vercel login redirect. If already logged into Vercel, Vercel will authenticate them automatically.
After login, users are redirected and a cookie is set in the browser if they have view access. If the user does not have access to view the deployment, they will be redirected to [request access](https://vercel.com/docs/activity-log#access-requests).
