##  [Inheritance](https://vercel.com/docs/getting-started-with-vercel#inheritance)[](https://vercel.com/docs/getting-started-with-vercel#inheritance)
Code Approvers are inherited from parent directories. If a directory does not have a `.vercel.approvers` file, then the approvers from the parent directory will be used. Furthermore, even if a directory does have a `.vercel.approvers` file, then the approvers from a parent directory with a `.vercel.approvers` file can also approve the changed files. This structure allows the most specific approver to review most of the code, but allows other approvers who have broader context and approval power to still review and approve the code when appropriate.
To illustrate the inheritance, the following example has two `.vercel.approvers` files.
The first file defines owners for the `packages/design` directory. The `@vercel/ui-team` can approve any change to a file under `packages/design/...`:
packages/design/.vercel.approvers
```
@vercel/ui-team
```

A second `.vercel.approvers` file is declared at the root of the codebase and allows users `elmo` and `oscar` to approve changes to any part of the repository, including the `packages/design` directory.
.vercel.approvers
```
@elmo
@oscar
```

The hierarchical nature of Code Owners enables many configurations in larger codebases, such as allowing individuals to approve cross-cutting changes or creating an escalation path when an approver is unavailable.
