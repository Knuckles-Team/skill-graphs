##  [Wildcard Approvers](https://vercel.com/docs/getting-started-with-vercel#wildcard-approvers)[](https://vercel.com/docs/getting-started-with-vercel#wildcard-approvers)
If you would like to allow a certain directory or file to be approved by anyone, you can use the wildcard owner `*`. This is useful for files that are not owned by a specific team or individual. The wildcard owner cannot be used with [modifiers](https://vercel.com/docs/getting-started-with-vercel#modifiers).
.vercel.approvers
```
# Changes to the `pnpm-lock.yaml` file in the current directory can be approved by anyone.
pnpm-lock.yaml *

# Changes to any README in the current directory or its subdirectories can be approved by anyone.
**/readme.md *

```

* * *
[ Previous Vercel Documentation ](https://vercel.com/docs)[ Next Projects and Deployments ](https://vercel.com/docs/getting-started-with-vercel/projects-deployments)
Was this helpful?
Send
On this page
  * [Enforcing Code Approvals](https://vercel.com/docs/getting-started-with-vercel#enforcing-code-approvals)
  * [Inheritance](https://vercel.com/docs/getting-started-with-vercel#inheritance)
  * [Reviewer Selection](https://vercel.com/docs/getting-started-with-vercel#reviewer-selection)
  * [Bypassing Reviewer Selection](https://vercel.com/docs/getting-started-with-vercel#bypassing-reviewer-selection)
  * [Modifiers](https://vercel.com/docs/getting-started-with-vercel#modifiers)
  * [silent](https://vercel.com/docs/getting-started-with-vercel#silent)
  * [notify](https://vercel.com/docs/getting-started-with-vercel#notify)
  * [optional](https://vercel.com/docs/getting-started-with-vercel#optional)
  * [members (default)](https://vercel.com/docs/getting-started-with-vercel#members-default)
  * [Excluding team members from review](https://vercel.com/docs/getting-started-with-vercel#excluding-team-members-from-review)
  * [team](https://vercel.com/docs/getting-started-with-vercel#team)
  * [required](https://vercel.com/docs/getting-started-with-vercel#required)
  * [Patterns](https://vercel.com/docs/getting-started-with-vercel#patterns)
  * [Directory (default)](https://vercel.com/docs/getting-started-with-vercel#directory-default)
  * [Current Directory Pattern](https://vercel.com/docs/getting-started-with-vercel#current-directory-pattern)
  * [Globstar Pattern](https://vercel.com/docs/getting-started-with-vercel#globstar-pattern)
  * [Specifying multiple owners for the same pattern](https://vercel.com/docs/getting-started-with-vercel#specifying-multiple-owners-for-the-same-pattern)
  * [Wildcard Approvers](https://vercel.com/docs/getting-started-with-vercel#wildcard-approvers)


Copy as MarkdownGive feedbackAsk AI about this page
