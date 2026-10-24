##  [Reviewer Selection](https://vercel.com/docs/getting-started-with-vercel#reviewer-selection)[](https://vercel.com/docs/getting-started-with-vercel#reviewer-selection)
When a pull request is opened, the Vercel GitHub App will select the approvers for the changed files. `.vercel.approvers` files allow extensive definitions of file mappings to possible approvers. In many cases, there will be multiple approvers for the same changed file. The Vercel GitHub app selects the best reviewers for the pull request based on affinity of `.vercel.approvers` definitions and overall coverage of the changed files.
###  [Bypassing Reviewer Selection](https://vercel.com/docs/getting-started-with-vercel#bypassing-reviewer-selection)[](https://vercel.com/docs/getting-started-with-vercel#bypassing-reviewer-selection)
You can skip automatic assignment of reviewers by adding `[vercel:skip:owners]` to your pull request description.
To request specific reviewers, you can override the automatic selection by including special text in your pull request description:
```
[vercel:approver:@owner1]
[vercel:approver:@owner2]
```

Code Owners will still ensure that the appropriate code owners have approved the pull request before it can pass. Therefore, make sure to select reviewers who provide sufficient coverage for all files in the pull request.
