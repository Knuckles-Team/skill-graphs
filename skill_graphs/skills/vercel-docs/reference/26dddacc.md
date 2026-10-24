##  [Access group behavior](https://vercel.com/docs/rbac/access-groups#access-group-behavior)[](https://vercel.com/docs/rbac/access-groups#access-group-behavior)
When configuring Access Groups, there are some key things to be aware of:
  * Team roles cannot be overridden. An Access Group manages project roles only
  * Only a subset of team role and project role combinations are valid:
    * [Owner](https://vercel.com/docs/rbac/access-roles#owner-role), [Member](https://vercel.com/docs/rbac/access-roles#member-role), [Billing](https://vercel.com/docs/rbac/access-roles#billing-role), [Viewer Pro](https://vercel.com/docs/rbac/access-roles#viewer-pro-role), [Viewer Enterprise](https://vercel.com/docs/rbac/access-roles#viewer-enterprise-role): All project role assignments are ignored
    * [Developer](https://vercel.com/docs/rbac/access-roles#developer-role): [Admin](https://vercel.com/docs/rbac/access-roles#project-administrators) assignment is valid on selected projects. [Project Developer](https://vercel.com/docs/rbac/access-roles#project-developer) and [Project Viewer](https://vercel.com/docs/rbac/access-roles#project-viewer) role assignments are ignored
    * [Contributor](https://vercel.com/docs/rbac/access-roles#contributor-role): `Admin`, `Project Developer`, or `Project Viewer` roles are valid in selected projects
  * When a `Contributor` belongs to multiple access groups the computed role will be:
    * `Admin` permissions in the project if any of the access groups they get assigned has a project mapping to `Admin`
    * `Project Developer` permissions in the project if any of the access groups they get assigned has a project mapping to `Project Developer` and there is none to `Admin` for that project
    * `Project Viewer` permissions in the project if any of the access groups they get assigned has a project mapping to `Project Viewer` and there is none to `Admin` and none to `Project Developer` for that project
  * When a `Developer` belongs to multiple access groups the role assignation will be:
    * `Admin` permissions in the project if any of the access groups they get assigned has a project mapping to Admin
    * In all other cases the member will have `Developer` permissions
  * Access Group assignations are not deleted when a team role gets changed. This allows a temporal increase of permissions without having to modify all Access Group assignations
  * Direct project assignations also affect member roles. Consider these examples:
    * A direct project assignment assigns a member as `Admin`. That member is within an Access Group that assigns `Developer`. The computed role is `Admin`.
    * A direct project assignment assigns a member as `Developer`. That member is within an Access Group that assigns `Admin`. The computed role is `Admin`.


Contributors and Developers can increase their level of permissions in a project but they can never reduce their level of permissions
