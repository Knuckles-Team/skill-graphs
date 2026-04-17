##  [Team and project name changes](https://vercel.com/docs/audit-log#team-and-project-name-changes)[](https://vercel.com/docs/audit-log#team-and-project-name-changes)
If you change the name of your team or project, the claims within the OIDC token will reflect the new names. This can affect your trust and access control policies. You should consider this when you plan to rename your team or project and update your policies accordingly.
AWS roles can support multiple conditions so you can allow access to both the old and new team and project names. The following example shows when the issuer mode is set to global:
aws-trust-policy.json
```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Federated": "arn:aws:iam::[YOUR AWS ACCOUNT ID]:oidc-provider/oidc.vercel.com"
      },
      "Action": "sts:AssumeRoleWithWebIdentity",
      "Condition": {
        "StringEquals": {
          "oidc.vercel.com:aud": [
            "https://vercel.com/[OLD_TEAM_SLUG]",
            "https://vercel.com/[NEW_TEAM_SLUG]"
          ],
          "oidc.vercel.com:sub": [
            "owner:[OLD_TEAM_SLUG]:project:[OLD_PROJECT_NAME]:environment:production",
            "owner:[NEW_TEAM_SLUG]:project:[NEW_PROJECT_NAME]:environment:production"
          ]
        }
      }
    }
  ]
}
```

If your project is using the `team` issuer mode, you will need to create a new OIDC provider and add another statement to the trust policy:
aws-trust-policy.json
```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "OldTeamName",
      "Effect": "Allow",
      "Principal": {
        "Federated": "arn:aws:iam::[YOUR AWS ACCOUNT ID]:oidc-provider/oidc.vercel.com/[OLD_TEAM_SLUG]"
      },
      "Action": "sts:AssumeRoleWithWebIdentity",
      "Condition": {
        "StringEquals": {
          "oidc.vercel.com/[OLD_TEAM_SLUG]:aud": [
            "https://vercel.com/[OLD_TEAM_SLUG]"
          ],
          "oidc.vercel.com/[OLD_TEAM_SLUG]:sub": [
            "owner:[OLD_TEAM_SLUG]:project:[OLD_PROJECT_NAME]:environment:production"
          ]
        }
      }
    },
    {
      "Sid": "NewTeamName",
      "Effect": "Allow",
      "Principal": {
        "Federated": "arn:aws:iam::[YOUR AWS ACCOUNT ID]:oidc-provider/oidc.vercel.com/[NEW_TEAM_SLUG]"
      },
      "Action": "sts:AssumeRoleWithWebIdentity",
      "Condition": {
        "StringEquals": {
          "oidc.vercel.com/[NEW_TEAM_SLUG]:aud": [
            "https://vercel.com/[NEW_TEAM_SLUG]"
          ],
          "oidc.vercel.com/[NEW_TEAM_SLUG]:sub": [
            "owner:[NEW_TEAM_SLUG]:project:[NEW_PROJECT_NAME]:environment:production"
          ]
        }
      }
    }
  ]
}
```
