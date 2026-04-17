##  [Deploying private Git repositories](https://vercel.com/docs/git#deploying-private-git-repositories)[](https://vercel.com/docs/git#deploying-private-git-repositories)
As an additional security measure, commits on private Git repositories (and commits of forks that are targeting those Git repositories) will only be deployed if the commit author also has access to the respective project on Vercel.
Depending on whether the owner of the connected Vercel project is a Hobby or a Pro team, the behavior changes as mentioned in the sections below.
This only applies to commit authors on GitHub organizations, GitLab groups and non-personal Bitbucket workspaces. It does not apply to collaborators on personal Git accounts.
For public Git repositories, [a different behavior](https://vercel.com/docs/git#deploying-forks-of-public-git-repositories) applies.
###  [Using Pro teams](https://vercel.com/docs/git#using-pro-teams)[](https://vercel.com/docs/git#using-pro-teams)
To deploy commits under a Vercel Pro team, the commit author must be a member of the team containing the Vercel project connected to the Git repository.
Membership is verified by finding the Vercel user associated with the commit author through [Login Connections](https://vercel.com/docs/accounts#login-methods-and-connections). If a Vercel user is found, it checks if the account is a member of the Pro team.
If the commit author is not a member, the deployment will be prevented, and the commit author can request to join the team. The team owners will be notified and can accept or decline the membership request on the [Members](https://vercel.com/docs/accounts/team-members-and-roles) page in the team Settings.
If the request is declined, the commit will remain undeployed. If the commit author is accepted as a member of the Pro team, their most recent commit will automatically resume deployment to Vercel.
Commit authors are automatically considered part of the Pro team on Vercel if one of the existing members has connected their account on Vercel with the Git account that created the commit.
###  [Using Hobby teams](https://vercel.com/docs/git#using-hobby-teams)[](https://vercel.com/docs/git#using-hobby-teams)
You cannot deploy to a Hobby team from a private repository in a GitHub organization, GitLab group, or Bitbucket workspace. Consider making the repository public or upgrading to [Pro](https://vercel.com/docs/plans/pro-plan).
To deploy commits under a Hobby team, the commit author must be the owner of the Hobby team containing the Vercel project connected to the Git repository. This is verified by comparing the [Login Connections](https://vercel.com/docs/accounts#login-methods-and-connections) Hobby team's owner with the commit author.
If the commit author is not the owner of the destination Hobby team, the deployment will be prevented, and a recommendation to transfer the project to a Pro team will be displayed on the Git provider.
After transferring the project to a Pro team, commit authors can be added as members of that team. The behavior mentioned in the [section above](https://vercel.com/docs/git#using-pro-teams) will then apply to them whenever they commit.
