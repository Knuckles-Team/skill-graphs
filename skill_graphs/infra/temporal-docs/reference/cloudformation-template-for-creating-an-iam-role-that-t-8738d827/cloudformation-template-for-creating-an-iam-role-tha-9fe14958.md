# CloudFormation template for creating an IAM role that Temporal Cloud can assume to invoke Lambda functions.
AWSTemplateFormatVersion: '2010-09-09'
Description:
  Creates an IAM role that Temporal Cloud can assume to invoke multiple Lambda functions for Serverless Workers.

Parameters:
  AssumeRoleExternalId:
    Type: String
    Description: A string you choose. Can be any value.
    AllowedPattern: '[a-zA-Z0-9_+=,.@-]*'
    MinLength: 5
    MaxLength: 45

  LambdaFunctionARNs:
    Type: CommaDelimitedList
    Description: >-
      Comma-separated list of Lambda function ARNs to invoke (e.g.,
      arn:aws:lambda:us-west-2:123456789012:function:worker-1,arn:aws:lambda:us-west-2:123456789012:function:worker-2)

  RoleName:
    Type: String
    Default: 'Temporal-Cloud-Serverless-Worker'

Metadata:
  AWS::CloudFormation::Interface:
    ParameterGroups:
      - Label:
          default: 'Temporal Cloud Configuration'
        Parameters:
          - AssumeRoleExternalId
      - Label:
          default: 'Lambda Configuration'
        Parameters:
          - LambdaFunctionARNs
          - RoleName
    ParameterLabels:
      AssumeRoleExternalId:
        default: 'External ID'
      LambdaFunctionARNs:
        default: 'Lambda Function ARNs (comma-separated list)'
      RoleName:
        default: 'IAM Role Name'

Resources:
  TemporalCloudServerlessWorker:
    Type: AWS::IAM::Role
    Properties:
      RoleName: !Sub '${RoleName}-${AWS::StackName}'
      AssumeRolePolicyDocument:
        Version: '2012-10-17'
        Statement:
          - Effect: Allow
            Principal:
              AWS:
                [
                  arn:aws:iam::902542641901:role/wci-lambda-invoke,
                  arn:aws:iam::160190466495:role/wci-lambda-invoke,
                  arn:aws:iam::819232936619:role/wci-lambda-invoke,
                  arn:aws:iam::829909441867:role/wci-lambda-invoke,
                  arn:aws:iam::354116250941:role/wci-lambda-invoke,
                ]
            Action: sts:AssumeRole
            Condition:
              StringEquals:
                'sts:ExternalId': [!Ref AssumeRoleExternalId]
      Description: 'The role Temporal Cloud uses to invoke Lambda functions for Serverless Workers'
      MaxSessionDuration: 3600 # 1 hour

  TemporalCloudLambdaInvokePermissions:
    Type: AWS::IAM::Policy
    DependsOn: TemporalCloudServerlessWorker
    Properties:
      PolicyName: 'Temporal-Cloud-Lambda-Invoke-Permissions'
      PolicyDocument:
        Version: '2012-10-17'
        Statement:
          - Effect: Allow
            Action:
              - lambda:InvokeFunction
              - lambda:GetFunction
            Resource: !Ref LambdaFunctionARNs
      Roles:
        - !Sub '${RoleName}-${AWS::StackName}'

Outputs:
  RoleARN:
    Description: The ARN of the IAM role created for Temporal Cloud
    Value: !GetAtt TemporalCloudServerlessWorker.Arn
    Export:
      Name: !Sub '${AWS::StackName}-RoleARN'

  RoleName:
    Description: The name of the IAM role
    Value: !Ref RoleName

  LambdaFunctionARNs:
    Description: The Lambda function ARNs that can be invoked
    Value: !Join [', ', !Ref LambdaFunctionARNs]
```

</details>

Deploy the template:

```bash
aws cloudformation create-stack \
  --stack-name <STACK_NAME> \
  --template-body file://temporal-cloud-serverless-worker-role.yaml \
  --parameters \
    ParameterKey=AssumeRoleExternalId,ParameterValue=<EXTERNAL_ID> \
    ParameterKey=LambdaFunctionARNs,ParameterValue='"<LAMBDA_FUNCTION_ARN>"' \
  --capabilities CAPABILITY_NAMED_IAM \
  --region <AWS_REGION>
```

After the stack finishes creating, retrieve the IAM role ARN from the stack outputs:

```bash
aws cloudformation describe-stacks --stack-name <STACK_NAME> --query 'Stacks[0].Outputs[?OutputKey==`RoleARN`].OutputValue' --output text --region <AWS_REGION>
```

Use this role ARN in your Worker Deployment Version's compute configuration.

## 4. Create Worker Deployment Version {/* #create-worker-deployment-version */}

Create a [Worker Deployment Version](/production-deployment/worker-deployments/worker-versioning) with a compute
provider that points to your Lambda function. The compute configuration tells Temporal how to invoke your Worker: the
provider type (`aws-lambda`), the Lambda function ARN, and the IAM role to assume. The deployment name and build ID must
match the values in your Worker code.

You can create the version using the Temporal UI or the Temporal CLI.

<Tabs groupId="create-version-approach">
<TabItem value="ui" label="Temporal UI">

1. In the Temporal UI, open your Namespace.
2. In the left pane, select **Workers**.
3. Click **Create Worker Deployment** in the upper right corner.
4. Under **Configuration**, enter a **Name** and **Build ID**. These must match the `DeploymentName` and `BuildID` in
   your Worker code.
5. Under **Compute**, select **AWS Lambda** and provide:
   - **Lambda ARN**: the ARN of your Lambda function.
   - **IAM Role ARN**: the ARN of the role Temporal assumes to invoke your Lambda function. This is the role ARN from
     [Step 3](#configure-iam) (output of the CloudFormation stack). This is not the Lambda execution role from
     [Step 2](#deploy-lambda-function) or your own IAM user/role.
   - **External ID**: the same value you passed to the CloudFormation template.
6. Click **Save**.

When you create a version through the UI, the version is automatically set as current. Skip to
[Verify the deployment](#verify-deployment).

</TabItem>
<TabItem value="cli" label="Temporal CLI">

Use the CLI for manual setup, shell scripts, and CI/CD pipelines. When you create a version through the CLI, you must
[set the version as current](#set-current-version) as a separate step.

First, create the Worker Deployment if it does not already exist:

```bash
temporal worker deployment create \
  --namespace <YOUR_NAMESPACE> \
  --name my-app
```

Then create the version with the compute provider configuration:

```bash
temporal worker deployment create-version \
  --namespace <YOUR_NAMESPACE> \
  --deployment-name my-app \
  --build-id build-1 \
  --aws-lambda-function-arn <LAMBDA_FUNCTION_ARN> \
  --aws-lambda-assume-role-arn <INVOCATION_ROLE_ARN> \
  --aws-lambda-assume-role-external-id <EXTERNAL_ID>
```

| Flag                                   | Description                                                                                                                                                                                                                                       |
| -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `--deployment-name`                    | Worker Deployment name. Must match `DeploymentName` in your Worker code.                                                                                                                                                                          |
| `--build-id`                           | Worker Deployment Version build ID. Must match `BuildID` in your Worker code.                                                                                                                                                                     |
| `--aws-lambda-function-arn`            | ARN of the Lambda function Temporal invokes for this version.                                                                                                                                                                                     |
| `--aws-lambda-assume-role-arn`         | IAM role Temporal assumes to invoke the function. This is the `RoleARN` output from the CloudFormation stack in [Step 3](#configure-iam). This is not the Lambda execution role from [Step 2](#deploy-lambda-function) or your own IAM user/role. |
| `--aws-lambda-assume-role-external-id` | External ID configured in the IAM role trust policy.                                                                                                                                                                                              |

</TabItem>
</Tabs>

To verify that Temporal can reach your Lambda function, go to **Workers** > **Deployments** > select your deployment >
open the **Actions** menu on the version and click **Validate Connection**. This checks that Temporal can assume the IAM
role and invoke the function.

## 5. Set version as current {/* #set-current-version */}

If you created the version through the Temporal UI, the version is already current and you can skip this step.

If you used the CLI, set the version as current. Without this step, tasks on the Task Queue will not route to the
version, and Temporal will not invoke the Lambda function.

```bash
temporal worker deployment set-current-version \
  --deployment-name my-app \
  --build-id build-1
```

## 6. Verify deployment {/* #verify-deployment */}

Start a Workflow on the same Task Queue to confirm that Temporal invokes your Lambda Worker.

```bash
temporal workflow start \
  --task-queue my-task-queue \
  --type MyWorkflow \
  --input '"Hello, serverless!"'
```

When the task lands on the Task Queue with no active pollers, Temporal detects the compute provider configuration and
invokes your Lambda function. The Worker starts, connects to Temporal, picks up the task, and processes it.

You can verify the invocation by checking:

- **Temporal UI:** The Workflow execution should show task completions in the event history.
- **AWS CloudWatch Logs:** The Lambda function's log group (`/aws/lambda/my-temporal-worker`) should show invocation
  logs with the Worker startup, task processing, and graceful shutdown.

If the Workflow does not progress or the Lambda is not invoked, see [Troubleshoot Serverless Workers](/troubleshooting/serverless-workers).

---

## Serverless Workers(3)

<ReleaseNoteHeader featureName="serverlessWorkers">
  To request access during Pre-release, create a [support ticket](/cloud/support#support-ticket) or contact your account team.
  APIs are experimental and may be subject to backwards-incompatible changes.
  [Sign up for updates](https://temporal.io/pages/serverless-workers-updates) to be notified when Serverless Workers reach Public Preview.
</ReleaseNoteHeader>

Serverless Workers let you run Temporal Workers on serverless compute like AWS Lambda. Deploy your Worker code to a
serverless provider, configure a compute provider for the Worker Deployment Version, and Temporal invokes the Worker
when Tasks arrive. There are no long-lived processes to provision or scale.

Temporal monitors Task Queues that have a compute provider configured. When a Task arrives and no Worker is polling,
Temporal invokes the configured compute target. The Worker starts, processes available Tasks, and shuts down when the
invocation window ends.

## Supported providers

- [**AWS Lambda**](/production-deployment/worker-deployments/serverless-workers/aws-lambda) - Deploy a Serverless Worker
  as a Lambda function. Temporal assumes an IAM role in your AWS account to invoke the function when Tasks arrive.

---

## Self-hosted setup for Serverless Workers

<ReleaseNoteHeader featureName="serverlessWorkers">
  APIs are experimental and may be subject to backwards-incompatible changes.
</ReleaseNoteHeader>

Serverless Workers require Temporal Service v1.31.0 or later.

This page covers the prerequisites for running [Serverless Workers](/serverless-workers) on a self-hosted Temporal
Service with AWS Lambda:

1. Ensure Lambda can reach the Temporal Service.
2. Enable the Worker Controller Instance (WCI) on the server through dynamic configuration.
3. Provide the server with AWS credentials to assume IAM roles.
4. Create an IAM role in your AWS account that grants Temporal permission to invoke Lambda functions.

Once setup is complete, follow the
[AWS Lambda deployment guide](/production-deployment/worker-deployments/serverless-workers/aws-lambda) to deploy your
Worker.

## Ensure Lambda can reach the Temporal Service {/* #ensure-network-reachability */}

The [Temporal Service frontend](/temporal-service/temporal-server#frontend-service) must be reachable from the Lambda execution
environment. How to achieve this depends on your network setup. If the Temporal Service runs on a private network, you
may need [VPC access for Lambda](https://docs.aws.amazon.com/lambda/latest/dg/configuration-vpc.html), VPC peering, or a
similar mechanism to allow the Lambda function to connect to the Temporal frontend.

## Enable the Worker Controller Instance {/* #enable-worker-controller */}

[WCI](/serverless-workers#how-invocation-works) is the server component that monitors Task Queues and invokes compute
providers. It is disabled by default and must be enabled through
[dynamic configuration](/references/dynamic-configuration).

Add the following keys to your dynamic config file:

```yaml
workercontroller.enabled:
  - value: true

workercontroller.compute_providers.enabled:
  - value:
      - aws-lambda

workercontroller.scaling_algorithms.enabled:
  - value:
      - no-sync
```

To enable WCI for specific Namespaces instead of globally, add a `constraints` section with the
Namespace name under `workercontroller.enabled`. For example, to enable WCI only for `your-namespace`:

```yaml
workercontroller.enabled:
  - value: true
    constraints:
      namespace: 'your-namespace'
```

The Temporal Service watches the dynamic config file for changes and applies updates without a restart.

## Configure AWS credentials {/* #configure-aws-credentials */}

The Temporal Service needs AWS credentials to assume an IAM role that invokes Lambda functions. How you provide
credentials depends on where the Temporal Service runs.

**On AWS infrastructure (EC2, ECS, EKS):** The server uses the attached instance role, task role, or pod role
automatically. No additional credential configuration is needed. The attached role must have `sts:AssumeRole` permission
for the Lambda invocation role created in the next step.

**Outside AWS:** Use [IAM Roles Anywhere](https://aws.amazon.com/iam/roles-anywhere/), or configure static AWS
credentials in the server's environment (not recommended):

```
AWS_ACCESS_KEY_ID=<access-key>
AWS_SECRET_ACCESS_KEY=<secret-key>
AWS_REGION=<region>
```

These credentials must belong to an IAM user or role that has `sts:AssumeRole` permission for the Lambda invocation
role.

## Create the Lambda invocation role {/* #create-invocation-role */}

Temporal invokes Lambda functions by assuming an IAM role in your AWS account. This role needs `lambda:GetFunction` and
`lambda:InvokeFunction` permission on your Worker Lambda functions, and a trust policy that allows the Temporal server's
identity to assume it.

Deploy the following CloudFormation template to create the role.
[Download the template](/files/temporal-self-hosted-serverless-worker-role.yaml). Replace the parameter values in the
command below and run it in your terminal:

```bash
aws cloudformation create-stack \
  --stack-name temporal-serverless-worker \
  --template-body file://temporal-self-hosted-serverless-worker-role.yaml \
  --parameters \
    ParameterKey=TemporalIamRoleArn,ParameterValue=<TEMPORAL_SERVER_ROLE_ARN> \
    ParameterKey=AssumeRoleExternalId,ParameterValue=<EXTERNAL_ID> \
    ParameterKey=LambdaFunctionARNs,ParameterValue='"<LAMBDA_FUNCTION_ARN>"' \
  --capabilities CAPABILITY_NAMED_IAM \
  --region <AWS_REGION>
```

| Parameter              | Description                                                                                                                                                                                                        |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `TemporalIamRoleArn`   | The ARN of the IAM role or user that the Temporal Service runs as. This is the identity the server uses to call `sts:AssumeRole`. To find the ARN, run `aws sts get-caller-identity` in the server's environment.  |
| `AssumeRoleExternalId` | A unique string to prevent [confused deputy](https://docs.aws.amazon.com/IAM/latest/UserGuide/confused-deputy.html) attacks. Choose any value and pass the same value when creating the Worker Deployment Version. |
| `LambdaFunctionARNs`   | Comma-separated list of Lambda function ARNs that Temporal may invoke.                                                                                                                                             |
| `RoleName`             | Base name for the created IAM role. Defaults to `Temporal-Serverless-Worker`.                                                                                                                                      |

<details>
<summary>CloudFormation template</summary>

```yaml
AWSTemplateFormatVersion: '2010-09-09'
Description:
  Creates an IAM role that a self-hosted Temporal Service can assume to invoke Lambda functions for Serverless Workers.

Parameters:
  TemporalIamRoleArn:
    Type: String
    Description: The ARN of the IAM role or user that the Temporal Service runs as.

  AssumeRoleExternalId:
    Type: String
    Description: A unique identifier to prevent confused deputy attacks.
    AllowedPattern: '[a-zA-Z0-9_+=,.@-]*'
    MinLength: 5
    MaxLength: 45

  LambdaFunctionARNs:
    Type: CommaDelimitedList
    Description: >-
      Comma-separated list of Lambda function ARNs to invoke (e.g.,
      arn:aws:lambda:us-west-2:123456789012:function:worker-1,arn:aws:lambda:us-west-2:123456789012:function:worker-2)

  RoleName:
    Type: String
    Default: 'Temporal-Serverless-Worker'

Resources:
  TemporalServerlessWorker:
    Type: AWS::IAM::Role
    Properties:
      RoleName: !Sub '${RoleName}-${AWS::StackName}'
      AssumeRolePolicyDocument:
        Version: '2012-10-17'
        Statement:
          - Effect: Allow
            Principal:
              AWS: [!Ref TemporalIamRoleArn]
            Action: sts:AssumeRole
            Condition:
              StringEquals:
                'sts:ExternalId': [!Ref AssumeRoleExternalId]
      Description: 'The role the Temporal Service uses to invoke Lambda functions for Serverless Workers'
      MaxSessionDuration: 3600

  TemporalLambdaInvokePermissions:
    Type: AWS::IAM::Policy
    DependsOn: TemporalServerlessWorker
    Properties:
      PolicyName: 'Temporal-Lambda-Invoke-Permissions'
      PolicyDocument:
        Version: '2012-10-17'
        Statement:
          - Effect: Allow
            Action:
              - lambda:InvokeFunction
              - lambda:GetFunction
            Resource: !Ref LambdaFunctionARNs
      Roles:
        - !Sub '${RoleName}-${AWS::StackName}'

Outputs:
  RoleARN:
    Description: The ARN of the IAM role created for the Temporal Service
    Value: !GetAtt TemporalServerlessWorker.Arn
    Export:
      Name: !Sub '${AWS::StackName}-RoleARN'

  RoleName:
    Description: The name of the IAM role
    Value: !Ref RoleName

  LambdaFunctionARNs:
    Description: The Lambda function ARNs that can be invoked
    Value: !Join [', ', !Ref LambdaFunctionARNs]
```

</details>

After the stack finishes creating, retrieve the IAM role ARN from the stack outputs:

```bash
aws cloudformation describe-stacks \
  --stack-name temporal-serverless-worker \
  --query 'Stacks[0].Outputs[?OutputKey==`RoleARN`].OutputValue' \
  --output text \
  --region <AWS_REGION>
```

Use this role ARN when creating the Worker Deployment Version.

## Next steps {/* #next-steps */}

Follow the [AWS Lambda deployment guide](/production-deployment/worker-deployments/serverless-workers/aws-lambda) to
write your Worker code, deploy it to Lambda, and create a Worker Deployment Version with the IAM role from the previous
step.

---

## Migrating from Unversioned to Versioned Temporal Workers

This guide will help you implement Worker Versioning when the Temporal Worker Controller isn't used. If you are using the Temporal Worker Controller, follow [this guide](https://github.com/temporalio/temporal-worker-controller/blob/main/docs/migration-to-versioned.md).

## Prerequisites

- Unversioned Temporal Workers currently running in production
- Temporal CLI >= 1.5.0
- Workers that connect to Temporal with Namespace and Task Queue configuration

## Key steps

- Ensure your versioned Worker code is backward-compatible with existing Workflow histories.
- Deploy the versioned Worker. It won't receive Tasks until you activate it.
- Use ramping to gradually shift traffic before full cutover.
- Signal sleeping or idle Workflows to wake them up and migrate them to the versioned Worker.
- Keep unversioned Workers running during the transition period.
- Test thoroughly in a non-production environment before migrating production Workers.

### Step 1: Update your Worker code

Update your Worker initialization to include versioning configuration.

**Before (Unversioned):**

```go
// Worker connects without versioning
worker := worker.New(client, "my-task-queue", worker.Options{})
```

**After (Versioned):**

```go
buildID := os.Getenv("TEMPORAL_WORKER_BUILD_ID")
deploymentName := os.Getenv("TEMPORAL_DEPLOYMENT_NAME")
if buildID == "" || deploymentName == "" {
    // exit with an error
}

workerOptions := worker.Options{
    DeploymentOptions: worker.DeploymentOptions{
        UseVersioning: true,
        Version: worker.WorkerDeploymentVersion{
            DeploymentName: deploymentName,
            BuildID:        buildID,
        },
    },
}
worker := worker.New(client, "my-task-queue", workerOptions)
```

:::info Important

Your versioned Worker code must be fully backward-compatible with existing unversioned Workflow histories to avoid non-determinism errors. Don't make breaking Workflow code changes at this stage.

:::

### Step 2: Deploy your versioned Worker

Deploy your versioned Worker alongside your existing unversioned Workers. The versioned Worker will begin polling but **won't receive any Tasks** until you explicitly activate it via the CLI.

You can verify it's polling by inspecting the Worker Deployment:

```shell
temporal worker deployment describe --name "YourDeploymentName"
```

### Step 3: Gradually ramp traffic (optional, but recommended)

Instead of cutting over all at once, ramp a small percentage of new Workflow executions to the versioned Worker first:

```shell
temporal worker deployment set-ramping-version \
    --deployment-name "YourDeploymentName" \
    --build-id "YourBuildID" \
    --percentage=5
```

Then monitor Workflows on the new version:

```shell
temporal workflow describe -w YourWorkflowID
```

This returns versioning info such as:

```
Versioning Info:

  Behavior               AutoUpgrade
  Version                YourDeploymentName.YourBuildID
  OverrideBehavior       Unspecified
```

Increase the ramp percentage incrementally as you test and see that your Workflows are behaving as expected.

### Step 4: Set the versioned Worker as Current

Once validated, promote the versioned Worker to receive 100% of new Workflow executions:

```shell
temporal worker deployment set-current-version \
    --deployment-name "YourDeploymentName" \
    --build-id "YourBuildID"
```

:::note

Once a Current version is set, **unversioned Workers** will no longer receive any Tasks. Ensure your versioned Workers are healthy before this step.

:::

### Step 5: Migrate unversioned in-flight Workflows

After setting the Current version, unversioned in-flight Workflows aren't dropped. On their next Task execution, they will automatically be routed to the versioned Worker. Once they are queued up on a versioned Worker, they will become either *Pinned* or *AutoUpgrade* depending on the Workflow's versioning behavior annotation.

Sleeping or idle Workflows will not automatically begin to receive the new version information. If you have Workflows that are sleeping or waiting for an event, you must send them a Signal to wake them up so they can be dispatched to the versioned Worker on their next Task execution.

Here's an example of how to Signal all running Workflows at once:

```shell
temporal workflow signal \
    --query "ExecutionStatus='Running'" \
    --name "wake-up" \
    --namespace production \
    --rps 100
```

Once signaled, those Workflows will execute a Workflow Task and be routed to the Current versioned Worker. Keep your unversioned Workers running until all in-flight Workflows have migrated over.

### Step 6: Scale down and clean up unversioned Workers

Once you confirm that all Workflows are handled by versioned Workers, shut down
your old unversioned Worker deployments.

---

## Worker Versioning(Worker-deployments)

Worker Versioning is a Temporal feature that allows you to confidently deploy new changes to the Workflows running on
your Workers without breaking them. Temporal enables this by helping you manage different builds or versions, formally
called [Worker Deployment Versions](/worker-versioning#deployment-versions).

For most teams, Worker Versioning should be the default recommendation for deploying Workflow code changes in
production. If you can run versioned worker deployments, prefer Worker Versioning over patching.

Worker Versioning unlocks important benefits for users of [blue-green or rainbow deployments](#deployment-systems).
