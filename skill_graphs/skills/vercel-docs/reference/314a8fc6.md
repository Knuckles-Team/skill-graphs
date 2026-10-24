##  [Examples](https://vercel.com/docs/security#examples)[](https://vercel.com/docs/security#examples)
In the following examples, you create a [Vercel function](https://vercel.com/docs/functions/quickstart#create-a-vercel-function) in the Vercel project where you have defined the OIDC role ARN environment variable. The function will connect to a specific resource in your AWS backend using OIDC and perform a specific action using the AWS SDK.
###  [List objects in an AWS S3 bucket](https://vercel.com/docs/security#list-objects-in-an-aws-s3-bucket)[](https://vercel.com/docs/security#list-objects-in-an-aws-s3-bucket)
Install the following packages:
Terminal
![](https://7nyt0uhk7sse4zvn.public.blob.vercel-storage.com/docs-assets/static/topics/icons/pnpm.svg)pnpm bun yarn npm
```
pnpm i @aws-sdk/client-s3 @vercel/functions
```

```
yarn add @aws-sdk/client-s3 @vercel/functions
```

```
npm i @aws-sdk/client-s3 @vercel/functions
```

```
bun add @aws-sdk/client-s3 @vercel/functions
```

In the API route for the function, use the AWS SDK for JavaScript to list objects in an S3 bucket with the following code:
/api/aws-s3/route.ts
```
import * as S3 from '@aws-sdk/client-s3';
import { awsCredentialsProvider } from '@vercel/oidc-aws-credentials-provider';

const AWS_REGION = process.env.AWS_REGION!;
const AWS_ROLE_ARN = process.env.AWS_ROLE_ARN!;
const S3_BUCKET_NAME = process.env.S3_BUCKET_NAME!;

// Initialize the S3 Client
const s3client = new S3.S3Client({
  region: AWS_REGION,
  // Use the Vercel AWS SDK credentials provider
  credentials: awsCredentialsProvider({
    roleArn: AWS_ROLE_ARN,
  }),
});

export async function GET() {
  const result = await s3client.send(
    new S3.ListObjectsV2Command({
      Bucket: S3_BUCKET_NAME,
    }),
  );
  return result?.Contents?.map((object) => object.Key) ?? [];
}
```

Vercel sends the OIDC token to the SDK using the `awsCredentialsProvider` function from `@vercel/functions`.
###  [Query an AWS RDS instance](https://vercel.com/docs/security#query-an-aws-rds-instance)[](https://vercel.com/docs/security#query-an-aws-rds-instance)
Install the following packages:
Terminal
![](https://7nyt0uhk7sse4zvn.public.blob.vercel-storage.com/docs-assets/static/topics/icons/pnpm.svg)pnpm bun yarn npm
```
pnpm i @aws-sdk/rds-signer @vercel/functions pg
```

```
yarn add @aws-sdk/rds-signer @vercel/functions pg
```

```
npm i @aws-sdk/rds-signer @vercel/functions pg
```

```
bun add @aws-sdk/rds-signer @vercel/functions pg
```

In the API route for the function, use the AWS SDK for JavaScript to perform a database `SELECT` query from an AWS RDS instance with the following code:
/api/aws-rds/route.ts
```
import { awsCredentialsProvider } from '@vercel/oidc-aws-credentials-provider';
import { Signer } from '@aws-sdk/rds-signer';
import { Pool } from 'pg';

const RDS_PORT = parseInt(process.env.RDS_PORT!);
const RDS_HOSTNAME = process.env.RDS_HOSTNAME!;
const RDS_DATABASE = process.env.RDS_DATABASE!;
const RDS_USERNAME = process.env.RDS_USERNAME!;
const AWS_REGION = process.env.AWS_REGION!;
const AWS_ROLE_ARN = process.env.AWS_ROLE_ARN!;

// Initialize the RDS Signer
const signer = new Signer({
  // Use the Vercel AWS SDK credentials provider
  credentials: awsCredentialsProvider({
    roleArn: AWS_ROLE_ARN,
  }),
  region: AWS_REGION,
  port: RDS_PORT,
  hostname: RDS_HOSTNAME,
  username: RDS_USERNAME,
});

// Initialize the Postgres Pool
const pool = new Pool({
  password: signer.getAuthToken,
  user: RDS_USERNAME,
  host: RDS_HOSTNAME,
  database: RDS_DATABASE,
  port: RDS_PORT,
});

// Export the route handler
export async function GET() {
  try {
    const client = await pool.connect();
    const { rows } = await client.query('SELECT * FROM my_table');
    return Response.json(rows);
  } finally {
    client.release();
  }
}
```

* * *
[ Previous Pricing/ Spend Management ](https://vercel.com/docs/spend-management)[ Next Security & Compliance Measures ](https://vercel.com/docs/security/compliance)
Was this helpful?
Send
On this page
  * [Configure your AWS account](https://vercel.com/docs/security#configure-your-aws-account)
  * [Create an OIDC identity provider](https://vercel.com/docs/security#create-an-oidc-identity-provider)
  * [Create an IAM role](https://vercel.com/docs/security#create-an-iam-role)
  * [Define the role ARN as environment variable](https://vercel.com/docs/security#define-the-role-arn-as-environment-variable)
  * [Examples](https://vercel.com/docs/security#examples)
  * [List objects in an AWS S3 bucket](https://vercel.com/docs/security#list-objects-in-an-aws-s3-bucket)
  * [Query an AWS RDS instance](https://vercel.com/docs/security#query-an-aws-rds-instance)


Copy as MarkdownGive feedbackAsk AI about this page
