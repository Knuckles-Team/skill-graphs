##  [Who can access protected deployments?](https://vercel.com/docs/activity-log#who-can-access-protected-deployments)[](https://vercel.com/docs/activity-log#who-can-access-protected-deployments)
  * Logged in [team members](https://vercel.com/docs/rbac/access-roles#team-level-roles) with at least a viewer role ([Viewer Pro](https://vercel.com/docs/rbac/access-roles#viewer-pro-role) or [Viewer Enterprise](https://vercel.com/docs/rbac/access-roles#viewer-enterprise-role))
  * Logged in [project members](https://vercel.com/docs/rbac/access-roles#project-level-roles) with at least the [project Viewer](https://vercel.com/docs/rbac/access-roles#project-viewer) role
  * Logged in members of an [access group](https://vercel.com/docs/rbac/access-groups) that has access to the project the deployment belongs to
  * Logged in Vercel users who have been [granted access](https://vercel.com/docs/activity-log#access-requests)
  * Anyone who has been given a [Shareable Link](https://vercel.com/docs/security/deployment-protection/methods-to-bypass-deployment-protection/sharable-links) to the deployment
  * Tools using the [protection bypass for automation](https://vercel.com/docs/security/deployment-protection/methods-to-bypass-deployment-protection/protection-bypass-automation) header
