##  [Directory sync](https://vercel.com/docs/rbac/access-groups#directory-sync)[](https://vercel.com/docs/rbac/access-groups#directory-sync)
If you use [Directory sync](https://vercel.com/docs/security/directory-sync), you are able to map a Directory Group with an Access Group. This will grant all users that belong to the Directory Group access to the projects that get assigned in the Access Group.
Some things to note:
  * The final role the user will have in a specific project will depend on the mappings of all Access Groups the user belongs to
  * Assignations using directory sync can lead to `Owners`, `Members` `Billing` and `Viewers` being part of an Access Group dependent on these mappings. In this scenario, access groups assignations will get ignored
  * When a Directory Group is mapped to an Access Group, members of that group will default to `Contributor` role at team level. This is unless another Directory Group assignation overrides the team role


* * *
[ Previous Access Roles ](https://vercel.com/docs/rbac/access-roles)[ Next Managing Team Members ](https://vercel.com/docs/rbac/managing-team-members)
Was this helpful?
Send
On this page
  * [Create an access group](https://vercel.com/docs/rbac/access-groups#create-an-access-group)
  * [Edit projects of an access group](https://vercel.com/docs/rbac/access-groups#edit-projects-of-an-access-group)
  * [Add and remove members from an access group](https://vercel.com/docs/rbac/access-groups#add-and-remove-members-from-an-access-group)
  * [Modifying access groups for a single team member](https://vercel.com/docs/rbac/access-groups#modifying-access-groups-for-a-single-team-member)
  * [Access group behavior](https://vercel.com/docs/rbac/access-groups#access-group-behavior)
  * [Directory sync](https://vercel.com/docs/rbac/access-groups#directory-sync)


Copy as MarkdownGive feedbackAsk AI about this page
