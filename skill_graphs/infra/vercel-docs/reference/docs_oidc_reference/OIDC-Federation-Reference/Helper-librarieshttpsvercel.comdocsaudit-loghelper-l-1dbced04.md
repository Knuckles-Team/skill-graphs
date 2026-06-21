##  [Helper libraries](https://vercel.com/docs/audit-log#helper-libraries)[](https://vercel.com/docs/audit-log#helper-libraries)
Vercel provides helper libraries to make it easier to exchange the OIDC token for short-lived credentials with your cloud provider. They are available from the
###  [AWS SDK credentials provider](https://vercel.com/docs/audit-log#aws-sdk-credentials-provider)[](https://vercel.com/docs/audit-log#aws-sdk-credentials-provider)
`awsCredentialsProvider()` is a helper function that returns a function that can be used as the `credentials` property of the AWS SDK client. It exchanges the OIDC token for short-lived credentials with AWS by calling the `AssumeRoleWithWebIdentity` operation.
####  [AWS S3 usage example](https://vercel.com/docs/audit-log#aws-s3-usage-example)[](https://vercel.com/docs/audit-log#aws-s3-usage-example)
```
import { awsCredentialsProvider } from '@vercel/oidc-aws-credentials-provider';
import * as s3 from '@aws-sdk/client-s3';

const s3client = new s3.S3Client({
  region: process.env.AWS_REGION!,
  credentials: awsCredentialsProvider({
    roleArn: process.env.AWS_ROLE_ARN!,
  }),
});
```

###  [Other cloud providers](https://vercel.com/docs/audit-log#other-cloud-providers)[](https://vercel.com/docs/audit-log#other-cloud-providers)
`getVercelOidcToken()` returns the OIDC token from the `VERCEL_OIDC_TOKEN` environment variable in builds and local development environments or the `x-vercel-oidc-token` in Vercel functions.
####  [Azure / CosmosDB example](https://vercel.com/docs/audit-log#azure-/-cosmosdb-example)[](https://vercel.com/docs/audit-log#azure-/-cosmosdb-example)
```
import { getVercelOidcToken } from '@vercel/oidc';
import { ClientAssertionCredential } from '@azure/identity';
import { CosmosClient } from '@azure/cosmos';

const credentialsProvider = new ClientAssertionCredential(
  process.env.AZURE_TENANT_ID,
  process.env.AZURE_CLIENT_ID,
  getVercelOidcToken,
);

const cosmosClient = new CosmosClient({
  endpoint: process.env.COSMOS_DB_ENDPOINT,
  aadCredentials: credentialsProvider,
});
```

In the Vercel function environments, you cannot execute the `getVercelOidcToken()` function directly at the module level because the token is only available in the `Request` object as the `x-vercel-oidc-token` header.
