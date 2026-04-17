##  [Modifiers](https://vercel.com/docs/getting-started-with-vercel#modifiers)[](https://vercel.com/docs/getting-started-with-vercel#modifiers)
Modifiers enhance the behavior of Code Owners by giving more control over the behavior of approvals and reviewer selection. The available modifiers are:
  * [silent](https://vercel.com/docs/getting-started-with-vercel#silent)
  * [notify](https://vercel.com/docs/getting-started-with-vercel#notify)
  * [optional](https://vercel.com/docs/getting-started-with-vercel#optional)
  * [team](https://vercel.com/docs/getting-started-with-vercel#team)
  * [members](https://vercel.com/docs/getting-started-with-vercel#members-default)
    * [not](https://vercel.com/docs/getting-started-with-vercel#excluding-team-members-from-review)
  * [required](https://vercel.com/docs/getting-started-with-vercel#required)


Modifiers are appended to the end of a line to modify the behavior of the owner listed for that line:
.vercel.approvers
```
# Approver with no modifier
@owner1
# Approver with optional modifier
@owner2:optional
```

###  [`silent`](https://vercel.com/docs/getting-started-with-vercel#silent)[](https://vercel.com/docs/getting-started-with-vercel#silent)
The user or team is an owner for the provided code but is never requested for review. If the user is a non-silent approver in another `.vercel.approvers` file that is closer to the changed files in the directory structure, then they will still be requested for review. The `:silent` modifier can be useful when there's an individual that should be able to approve code, but does not want to receive requests, such as a manager or an old team member.
.vercel.approvers
```
# This person will never be requested to review code but can still approve for owners coverage.
@owner:silent
```

###  [`notify`](https://vercel.com/docs/getting-started-with-vercel#notify)[](https://vercel.com/docs/getting-started-with-vercel#notify)
The user or team is always notified through a comment on the pull request. These owners may still be requested for review as part of [reviewer selection](https://vercel.com/docs/getting-started-with-vercel#reviewer-selection), but will still be notified even if not requested. This can be useful for teams that want to be notified on every pull request that affects their code.
.vercel.approvers
```
# my-team is always notified even if leerob is selected as the reviewer.
@vercel/my-team:notify
@leerob
```

###  [`optional`](https://vercel.com/docs/getting-started-with-vercel#optional)[](https://vercel.com/docs/getting-started-with-vercel#optional)
The user or team is never requested for review, and they are ignored as owners when computing review requirements. The owner can still approve files they have coverage over, including those that have other owners.
This can be useful while in the process of adding code owners to an existing repository or when you want to designate an owner for a directory but not block pull request reviewers on this person or team.
.vercel.approvers
```
@owner:optional
```

###  [`members` (default)](https://vercel.com/docs/getting-started-with-vercel#members-default)[](https://vercel.com/docs/getting-started-with-vercel#members-default)
The `:members` modifier can be used with GitHub teams to select an individual member of the team for reviewer rather than assigning it to the entire team. This can be useful when teams want to distribute the code review load across everyone on the team. This is the default behavior for team owners if the [`:team`](https://vercel.com/docs/getting-started-with-vercel#team) modifier is not specified.
.vercel.approvers
```
# An individual from the @acme/eng-team will be requested as a reviewer.
@acme/eng-team:members
```

####  [Excluding team members from review](https://vercel.com/docs/getting-started-with-vercel#excluding-team-members-from-review)[](https://vercel.com/docs/getting-started-with-vercel#excluding-team-members-from-review)
The `:not` modifier can be used with `:members` to exclude certain individuals on the team from review. This can be useful when there is someone on the team who shouldn't be selected for reviews, such as a person who is out of office or someone who doesn't review code every day.
.vercel.approvers
```
# An individual from the @acme/eng-team, except for leerob will be requested as a reviewer.
@acme/eng-team:members:not(leerob)
# Both leerob and mknichel will not be requested for review.
@acme/eng-team:members:not(leerob):not(mknichel)
```

###  [`team`](https://vercel.com/docs/getting-started-with-vercel#team)[](https://vercel.com/docs/getting-started-with-vercel#team)
The `:team` modifier can be used with GitHub teams to request the entire team for review instead of individual members from the team. This modifier must be used with team owners and can not be used with the [`:members`](https://vercel.com/docs/getting-started-with-vercel#members-default) modifier.
.vercel.approvers
```
# The @acme/eng-team will be requested as a reviewer.
@acme/eng-team:team
```

###  [`required`](https://vercel.com/docs/getting-started-with-vercel#required)[](https://vercel.com/docs/getting-started-with-vercel#required)
This user or team is always notified (through a comment) and is a required approver on the pull request regardless of the approvals coverage of other owners. Since the owner specified with `:required` is always required regardless of the owners hierarchy, this should be rarely used because it can make some changes such as global refactorings challenging. `:required` should be usually reserved for highly sensitive changes, such as security, privacy, billing, or critical systems.
Most of the time you don't need to specify required approvers. Non-modified approvers are usually enough so that correct reviews are enforced.
.vercel.approvers
```
# Always notified and are required reviewers.
# The check won't pass until both `owner1` and `owner2` approve.
@owner1:required
@owner2:required
```

When you specify a team as a required reviewer only one member of that team is required to approve.
.vercel.approvers
```
# The team is notified and are required reviewers.
# The check won't pass until one member of the team approves.
@vercel/my-team:required
```
