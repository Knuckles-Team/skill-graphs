##  [Configure your AWS account](https://vercel.com/docs/security#configure-your-aws-account)[](https://vercel.com/docs/security#configure-your-aws-account)
  1. ###  [Create an OIDC identity provider](https://vercel.com/docs/security#create-an-oidc-identity-provider)[](https://vercel.com/docs/security#create-an-oidc-identity-provider)
    1. Navigate to the
    2. Navigate to IAM then Identity Providers
    3. Select Add Provider
    4. Select OpenID Connect from the provider type
    5. Enter the Provider URL, the URL will depend on the issuer mode setting:
       * Team: `https://oidc.vercel.com/[TEAM_SLUG]`, replacing `[TEAM_SLUG]` with the path from your Vercel team URL
       * Global: `https://oidc.vercel.com`
    6. Enter `https://vercel.com/[TEAM_SLUG]` in the Audience field, replacing `[TEAM_SLUG]` with the path from your Vercel team URL
    7. Select Add Provider
![Add provider values for the Global issuer mode setting. For the Team issuer mode setting, set the Provider URL to https://vercel.com/\[TEAM_SLUG\]](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Foidc-tokens%2Faws-create-id-provider.png&w=1080&q=75)![Add provider values for the Global issuer mode setting. For the Team issuer mode setting, set the Provider URL to https://vercel.com/\[TEAM_SLUG\]](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Foidc-tokens%2Faws-create-id-provider.png&w=1080&q=75)Add provider values for the Global issuer mode setting. For the Team issuer mode setting, set the Provider URL to https://vercel.com/[TEAM_SLUG]
  2. ###  [Create an IAM role](https://vercel.com/docs/security#create-an-iam-role)[](https://vercel.com/docs/security#create-an-iam-role)
To use AWS OIDC Federation you must have an
Here is an example of a trust policy using the Team issuer mode:
trust-policy.json
```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Federated": "arn:aws:iam::[YOUR AWS ACCOUNT ID]:oidc-provider/oidc.vercel.com/[TEAM_SLUG]"
      },
      "Action": "sts:AssumeRoleWithWebIdentity",
      "Condition": {
        "StringEquals": {
          "oidc.vercel.com/[TEAM_SLUG]:sub": "owner:[TEAM SLUG]:project:[PROJECT NAME]:environment:production",
          "oidc.vercel.com/[TEAM_SLUG]:aud": "https://vercel.com/[TEAM SLUG]"
        }
      }
    }
  ]
}
```

The above policy's conditions are quite strict. It requires the `aud` sub `sub` claims to match exactly, but it's possible to configure less strict trust policies conditions:
trust-policy.json
```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Federated": "arn:aws:iam::[YOUR AWS ACCOUNT ID]:oidc-provider/oidc.vercel.com/[TEAM_SLUG]"
      },
      "Action": "sts:AssumeRoleWithWebIdentity",
      "Condition": {
        "StringEquals": {
          "oidc.vercel.com/[TEAM_SLUG]:aud": "https://vercel.com/[TEAM SLUG]"
        },
        "StringLike": {
          "oidc.vercel.com/[TEAM_SLUG]:sub": [
            "owner:[TEAM SLUG]:project:*:environment:preview",
            "owner:[TEAM SLUG]:project:*:environment:production"
          ]
        }
      }
    }
  ]
}
```

This policy allows any project matched by the `*` that are targeted to `preview` and `production` but not `development`.
  3. ###  [Define the role ARN as environment variable](https://vercel.com/docs/security#define-the-role-arn-as-environment-variable)[](https://vercel.com/docs/security#define-the-role-arn-as-environment-variable)
Once you have created the role, copy the [declare it as an environment variable](https://vercel.com/docs/environment-variables#creating-environment-variables) in your Vercel project with key name `AWS_ROLE_ARN`.
.env.local
```
AWS_ROLE_ARN=arn:aws:iam::accountid:user/username
```

You are now ready to connect to your AWS resource in your project's code. Review the examples below.
