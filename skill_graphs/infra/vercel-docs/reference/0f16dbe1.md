# Code Approvers
Last updated September 24, 2025
Code Owners are available on [Enterprise plans](https://vercel.com/docs/plans/enterprise)
Code Approvers are a list of
You can enable Code Approvers for a directory by adding a `.vercel.approvers` file to that directory in your codebase. For example, this `.vercel.approvers` file defines the GitHub team `vercel/ui-team` as an approver for the `packages/design` directory:
packages/design/.vercel.approvers
```
@vercel/ui-team
```

When a team is declared as an approver, all members of that team will be able to approve changes to the directory or file and at least one member of the team must approve the changes.
