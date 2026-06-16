# Run the worker
CMD ["python", "worker.py"]
```

Build the Docker image and target the `linux/amd64` architecture:

```bash
docker buildx build \
    --platform linux/amd64 \
    -t your-app .
```

## Publish the Worker Image to Amazon ECR

After building the Docker image, you’re ready to publish it to Amazon ECR.
Make sure that you’re authenticated with AWS, and that you’ve set your `AWS_REGION` and `AWS_ACCOUNT_ID` environment variables:

```bash
export AWS_ACCOUNT_ID=<your_aws_account_id>
export AWS_REGION=<your_aws_region>
```

Create an ECR repository and authenticate ECR with the Docker container client:

```bash
aws ecr create-repository \
    --repository-name your-app
aws ecr get-login-password --region $AWS_REGION | \
    docker login --username AWS --password-stdin \
            $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com
```

After authenticating Docker with ECR, tag your container and publish it:

```bash
docker tag your-app $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/your-app:latest
docker push $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/your-app:latest
```

## Deploy the Workers to EKS

With your Worker containerized, you’re ready to deploy it to EKS. Create a namespace in your EKS cluster. You’ll use the namespace to run your Temporal Workers:

```bash
kubectl create namespace example-namespace
```

Create a `ConfigMap` to hold non-sensitive values that Kubernetes will inject into your Worker deployment.
These enable dynamic routing for instances, Namespaces, and Task Queues.
To set these values, build a `config-map.yaml` file like the following example:

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: temporal-worker-config
  namespace: example-namespace
data:
  TEMPORAL_ADDRESS: "<your-temporal-address>"
  TEMPORAL_NAMESPACE: "<your-temporal-cloud-namespace>"
  TEMPORAL_TASK_QUEUE: "<your-task-queue>"
```

Apply the `ConfigMap` to your namespace:

```bash
kubectl apply -f config-map.yaml \
    --namespace example-namespace
```

For sensitive values, use Kubernetes Secrets.
Create a secret to hold your Temporal API key:

```bash
kubectl create secret generic temporal-secret \
    --from-literal=TEMPORAL_API_KEY=$TEMPORAL_API_KEY \
    --namespace example-namespace
```

With your configuration in place, you can deploy the Worker.
Create a `deployment.yaml` file to configure your Worker image, resources, and secret values.
You can tune the resources and optional configurations you specify to match your deployment needs so they match your production workloads.
Note that the spun-up container reads your Temporal API key from the Kubernetes secret you just created:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
   name: your-app
   namespace: example-namespace
   labels:
      app: your-app
spec:
   selector:
      matchLabels:
         app: your-app
   replicas: 1
   template:
      metadata:
         labels:
            app: your-app
      spec:
         serviceAccountName: your-app
         containers:
            - name: your-app
              image: <your-ecr-image-name>
              env:
                - name: TEMPORAL_ADDRESS
                  valueFrom:
                    configMapKeyRef:
                      name: temporal-worker-config
                      key: TEMPORAL_ADDRESS
                - name: TEMPORAL_NAMESPACE
                  valueFrom:
                    configMapKeyRef:
                      name: temporal-worker-config
                      key: TEMPORAL_NAMESPACE
                - name: TEMPORAL_TASK_QUEUE
                  valueFrom:
                    configMapKeyRef:
                      name: temporal-worker-config
                      key: TEMPORAL_TASK_QUEUE
                - name: TEMPORAL_API_KEY
                  valueFrom:
                    secretKeyRef:
                      name: temporal-secret
                      key: TEMPORAL_API_KEY
              resources:
                limits:
                  cpu: "0.5"
                  memory: "512Mi"
                requests:
                  cpu: "0.2"
                  memory: "256Mi"
```

Apply the `deployment.yaml` file to the EKS cluster:

```bash
kubectl apply -f deployment.yaml \
    --namespace example-namespace
```

## Verify that the Workers are Connected

After deploying your Workers to EKS, confirm that they have connected to Temporal Cloud.
Retrieve the pod listing for the Kubernetes/EKS namespace that you created:

```
kubectl get pods -n example-namespace
```

After listing the pods, access the Worker logs to confirm you’re properly connected to Temporal Cloud:

```
kubectl logs <pod-name> -n example-namespace
```

You confirm connection when you see:

```
Initializing worker...
Starting worker... Waiting for tasks.
```

You have now successfully deployed your Temporal Worker to EKS.

---

## Temporal Worker deployments

A core feature of Temporal is that you are able to deploy your Workers to any infrastructure where your Workflow and Activity code will actually run.
This way, you have total control over your runtime environment, and can be responsive to any security or scaling needs that may arise over time, whether you are using Temporal Cloud or self-hosting a Temporal Service.

If you are just getting started, you want more guidance, or a refresher on Temporal concepts, our [Tutorials and Courses](https://learn.temporal.io/) help by using only one or two Temporal Workers to demonstrate core functionality.
Once you have an understanding of the core concepts, the content in this section will provide clarity on real-world deployments that grow far beyond those examples.

Our Worker Deployments guide provides documentation of Temporal product features that make it easier to scale and revise your Workflows.

[Worker Versioning](/production-deployment/worker-deployments/worker-versioning) is the recommended default for safely
deploying new Workflow code. It allows you to pin Workflows to individual versions of your workers, which are called
Worker Deployment Versions.

If your environment cannot yet support versioned worker deployments, you can fall back to patching Workflow code.
However, new production deployments should prefer Worker Versioning whenever possible.

You can optionally use the Temporal [Worker Controller](/production-deployment/worker-deployments/kubernetes-controller) to programmatically manage and scale your Worker deployments in Kubernetes pods.

This section also covers specific Worker Deployment examples:

- [**Serverless Workers**](/production-deployment/worker-deployments/serverless-workers)
  Deploy Serverless Workers on serverless compute like AWS Lambda.
  Temporal invokes your Worker when Tasks arrive, with no long-lived processes to manage.

- [**Deploy Workers to Amazon EKS**](/production-deployment/worker-deployments/deploy-workers-to-aws-eks)
  Containerize your Worker, publish it to Amazon Elastic Container Registry (ECR), and deploy it to Amazon Elastic Kubernetes Service (EKS) using the Temporal Python SDK.
  This guide covers the full deployment lifecycle and shows how to configure your Worker to connect to Temporal Cloud using Kubernetes-native tools like ConfigMaps and Secrets.
  Running Workers on EKS gives you fine-grained control over scaling, resource allocation, and availability—ideal for production systems that need reliability and flexibility in the cloud.

---

## Temporal Worker Controller

The [Temporal Worker Controller](https://github.com/temporalio/temporal-worker-controller) provides automation to enable rainbow deployments of your Workers by simplifying the tracking of which versions still have active Workflows, managing the lifecycle of versioned Worker deployments, and calling Temporal APIs to update the routing config of Temporal Worker Deployments.
The Temporal Worker Controller makes it simple and safe to deploy Temporal Workers on Kubernetes.

If you run versioned Workers on Kubernetes, the Worker Controller is the recommended way to manage rollouts and autoscaling together.

### Why adopt the Worker Controller?

The traditional approach to revising Temporal Workflows is to add branches using the [Versioning APIs](/workflow-definition#workflow-versioning).
Over time these checks can become a source of technical debt, as safely removing them from a codebase is a careful process that often involves querying all running Workflows.

[Worker Versioning](/production-deployment/worker-deployments/worker-versioning) is a Temporal feature that allows you to pin Workflows to individual versions of your Workers, which are called Worker Deployment Versions.
Using pinning, you will not need to add branching to your Workflows to avoid non-determinism errors.
This allows you to bypass the other Versioning APIs.

The Worker Controller gives you direct, programmatic control over your Worker deployments, and integrates with the [Temporal CLI](/production-deployment/worker-deployments/worker-versioning#rolling-out-changes-with-the-cli).
You do not need to use the Worker Controller to use Worker Versioning, but when used together, Worker Versioning and the Worker Controller can provide more graceful deployments and upgrades, and less need to manually tune your Workers.

Note that in Temporal, **Worker Deployment** is sometimes referred to as **Deployment**, but since the Worker Controller makes significant references to Kubernetes Deployment resource, within this page we will stick to these terms:

- [**Worker Deployment**](/worker-versioning#deployments): A Worker Deployment is a logical service that groups similar Workers together for unified management. Each Deployment has a name (such as your service name) and supports versioning through a series of Worker Deployment Versions.
- [**Worker Deployment Version**](/worker-versioning#deployment-versions): A Worker Deployment Version represents an iteration of a Worker Deployment. Each Deployment Version consists of Workers that share the same code build and environment. When a Worker starts polling for Workflow and Activity Tasks, it reports its Deployment Version to the Temporal Server.
- **Deployment**: A Kubernetes Deployment resource. A Deployment is "versioned" if it is running versioned Temporal workers/pollers.

### Features

- Registration of new Temporal Worker Deployment Versions
- Creation of versioned Deployment resources (that manage the Pods that run your Temporal pollers)
- Deletion of resources associated with drained Worker Deployment Versions
- `Manual`, `AllAtOnce`, and `Progressive` rollouts of new versions
- Ability to specify a "gate" Workflow that must succeed on the new version before routing real traffic to that version
- Autoscaling of versioned Deployments using Kubernetes Horizontal Pod Autoscaler (HPA)

Refer to the [Temporal Worker Controller repo](https://github.com/temporalio/temporal-worker-controller/) for usage details.

## Autoscaling versioned Workers

The Worker Controller can manage autoscaling for versioned Worker Deployments without forcing you to choose between
safe rollout behavior and elastic capacity.

Use the Worker Controller when you need all of the following:

- [Worker Versioning](/production-deployment/worker-deployments/worker-versioning) for safe Workflow code changes
- Kubernetes-native rollout automation
- autoscaling that follows each active Worker Deployment Version separately

Because the Worker Controller uses Kubernetes HPA, you can scale on any metric available to your HPA pipeline,
including:

- CPU and memory utilization
- Task Queue backlog metrics exposed through your metrics pipeline
- slot utilization and other Worker-specific metrics
- custom metrics surfaced through Prometheus or another Kubernetes metrics adapter

### TemporalWorkerOwnedResource

To attach autoscaling or other Kubernetes resources to each Worker Deployment Version, use a
`TemporalWorkerOwnedResource` (TWOR).

A TWOR lets you define a resource template once and have the Worker Controller create a version-specific copy for each
active Worker Deployment Version. This is useful for resources such as:

- `HorizontalPodAutoscaler`
- `PodDisruptionBudget`
- other Kubernetes resources that should track the lifecycle of a versioned Deployment

The Worker Controller manages these resources alongside the versioned Deployments it creates, so they are updated and
cleaned up as versions roll forward and drain.

### Why use this instead of KEDA?

If you are already using the Worker Controller for Worker Versioning, use the Worker Controller for autoscaling as
well. This keeps rollout management and scaling attached to the same versioned Kubernetes Deployments.

KEDA can still be a valid option for non-versioned or legacy worker deployments. However, for versioned Workers, the
Worker Controller is the preferred path because it keeps autoscaling aligned with Worker Deployment Versions.

## Configuring Worker Lifecycles

To use the Temporal Worker Controller, tag your Workers following the guidance for using [Worker Versioning](/production-deployment/worker-deployments/worker-versioning).

Here is an example of a progressive rollout strategy gated on the success of the `HelloWorld` Workflow:

```
rollout:
  strategy: Progressive
  steps:
    - rampPercentage: 1
      pauseDuration: 30s
    - rampPercentage: 10
      pauseDuration: 1m
  gate:
    workflowType: "HelloWorld"
```

As you ship new deployment versions, the Worker Controller automatically detects them and gradually makes that version the new **Current Version** of the Worker deployment it is a part of.
As older pinned Workflows finish executing and deprecated deployment versions become drained, the Worker Controller also frees up resources by sunsetting the `Deployment` resources polling those versions.

When you use autoscaling with the Worker Controller, each active Worker Deployment Version can scale independently while
it is serving traffic. This allows older versions to drain safely while newer versions scale based on live demand.

## Running the Temporal Worker Controller

You can install the Temporal Worker Controller using our Helm chart:

```bash
RELEASE=temporal-worker-controller
NAMESPACE=temporal-system
VERSION=1.0.0

helm install $RELEASE oci://docker.io/temporalio/helm-charts/temporal-worker-controller \
  --version $VERSION \
  --namespace $NAMESPACE \
  --create-namespace

helm install temporal-worker-controller ./helm/temporal-worker-controller \
  --namespace $NAMESPACE \
  --create-namespace
```

Refer to [GitHub](https://github.com/temporalio/temporal-worker-controller/tree/main/helm/temporal-worker-controller/templates) for other Worker Controller deployment templates.

---

## Deploy a Serverless Worker on AWS Lambda

<ReleaseNoteHeader featureName="serverlessWorkers">
  To request access during Pre-release, create a [support ticket](/cloud/support#support-ticket) or contact your account team.
  APIs are experimental and may be subject to backwards-incompatible changes.
  [Sign up for updates](https://temporal.io/pages/serverless-workers-updates) to be notified when Serverless Workers reach Public Preview.
</ReleaseNoteHeader>

This guide walks through deploying a Temporal [Serverless Worker](/serverless-workers) on AWS Lambda.

## Prerequisites {/* #prerequisites */}

- A Temporal Cloud account with an AWS-hosted Namespace, or a self-hosted Temporal Service v1.31.0 or later. The
  Namespace's cloud provider must match the serverless compute provider.
- For self-hosted deployments, complete the
  [self-hosted setup](/production-deployment/worker-deployments/serverless-workers/self-hosted-setup) before following
  this guide.
- Every Workflow must declare a [versioning behavior](/worker-versioning#versioning-behaviors), or the Worker must set a
  default versioning behavior.
- An AWS account with permissions to create and invoke Lambda functions and create IAM roles.
- The AWS-specific steps in this guide require the [`aws` CLI](https://aws.amazon.com/cli/) installed and configured
  with your AWS credentials. You may use other tools to perform the steps, such as the AWS Console or the AWS SDKs.

- The [Go SDK](/develop/go), [Python SDK](/develop/python), or [TypeScript SDK](/develop/typescript), depending on which
  language you are using. Use the tabs to select your language and the rest of the page will update accordingly.

  :::tip

  If you are exploring the Serverless Worker feature and don't have a Workflow ready, you can use a sample from
  the [Go Lambda Worker sample](https://github.com/temporalio/samples-go/tree/main/lambda-worker),
  [Python Lambda Worker sample](https://github.com/temporalio/samples-python/tree/main/lambda_worker), or
  [TypeScript Lambda Worker sample](https://github.com/temporalio/samples-typescript/tree/main/lambda-worker).

  :::

## 1. Write Worker code {/* #write-worker-code */}

Write a Worker that runs inside a Lambda function. The Worker handles the per-invocation lifecycle: connecting to
Temporal, polling for tasks, and gracefully shutting down before the invocation deadline.

<SdkTabs hideUnsupportedLanguages>
<SdkTabs.Go>

Use the Go SDK's `lambdaworker` package.

```go
package main

	lambdaworker "go.temporal.io/sdk/contrib/aws/lambdaworker"
	"go.temporal.io/sdk/worker"
	"go.temporal.io/sdk/workflow"
)

func main() {
	lambdaworker.RunWorker(worker.WorkerDeploymentVersion{
		DeploymentName: "my-app",
		BuildID:        "build-1",
	}, func(opts *lambdaworker.Options) error {
		opts.TaskQueue = "my-task-queue"

		opts.RegisterWorkflowWithOptions(MyWorkflow, workflow.RegisterOptions{
			VersioningBehavior: workflow.VersioningBehaviorPinned,
		})
		opts.RegisterActivity(MyActivity)

		return nil
	})
}
```

Each Workflow must have a [versioning behavior](/worker-versioning#versioning-behaviors), either `AutoUpgrade` or
`Pinned`. Set it per-Workflow at registration time, or set a Worker-level default with `DefaultVersioningBehavior` in
`DeploymentOptions`.

For details on configuration options, Lambda-tuned defaults, and the invocation lifecycle, see
[Serverless Workers - Go SDK](/develop/go/workers/serverless-workers/aws-lambda).

</SdkTabs.Go>
<SdkTabs.Python>

Use the Python SDK's `lambda_worker` contrib package.

```python
from temporalio.common import WorkerDeploymentVersion
from temporalio.contrib.aws.lambda_worker import LambdaWorkerConfig, run_worker

from my_workflows import MyWorkflow
from my_activities import my_activity

def configure(config: LambdaWorkerConfig) -> None:
    config.worker_config["task_queue"] = "my-task-queue"
    config.worker_config["workflows"] = [MyWorkflow]
    config.worker_config["activities"] = [my_activity]

lambda_handler = run_worker(
    WorkerDeploymentVersion(
        deployment_name="my-app",
        build_id="build-1",
    ),
    configure,
)
```

Each Workflow must have a [versioning behavior](/worker-versioning#versioning-behaviors), either `PINNED` or
`AUTO_UPGRADE`. Set it per-Workflow in the `@workflow.defn` decorator, or set a Worker-level default with
`default_versioning_behavior` in the worker config.

```python
from temporalio import workflow
from temporalio.common import VersioningBehavior

@workflow.defn(versioning_behavior=VersioningBehavior.PINNED)
class MyWorkflow:
    @workflow.run
    async def run(self, input: str) -> str:
        ...
```

For details on configuration options, Lambda-tuned defaults, and observability, see
[Serverless Workers - Python SDK](/develop/python/workers/serverless-workers/aws-lambda).

</SdkTabs.Python>
<SdkTabs.TypeScript>

Use the `@temporalio/lambda-worker` package.

```typescript

export const handler = runWorker({ deploymentName: 'my-app', buildId: 'build-1' }, (config) => {
  config.workerOptions.taskQueue = 'my-task-queue';
  config.workerOptions.workflowBundle = {
    codePath: require.resolve('./workflow-bundle.js'),
  };
  config.workerOptions.activities = activities;
  config.workerOptions.workerDeploymentOptions!.defaultVersioningBehavior = 'PINNED';
});
```

Use `workflowBundle` with pre-bundled code instead of `workflowsPath` to avoid webpack bundling overhead on Lambda cold
starts.

Each Workflow must declare a [versioning behavior](/worker-versioning#versioning-behaviors), either `AUTO_UPGRADE` or
`PINNED`. Set it per-Workflow with `setWorkflowOptions` in the Workflow file, or set a default for all Workflows with
`defaultVersioningBehavior` in the configure callback.

For details on configuration options, Lambda-tuned defaults, and observability, see
[Serverless Workers - TypeScript SDK](/develop/typescript/workers/serverless-workers/aws-lambda).

</SdkTabs.TypeScript>
</SdkTabs>

## 2. Deploy Lambda function {/* #deploy-lambda-function */}

Build your Worker for the Lambda runtime, package it as a zip, and deploy it to AWS Lambda.

### i. Build and package {/* #build-and-package */}

<SdkTabs hideUnsupportedLanguages>
<SdkTabs.Go>

Cross-compile for Lambda's Linux runtime:

```bash
GOOS=linux GOARCH=amd64 go build -tags lambda.norpc -o bootstrap ./worker
```

Package the binary into a zip file:

```bash
zip function.zip bootstrap
```

</SdkTabs.Go>
<SdkTabs.Python>

Install dependencies into a local directory for packaging. Use `--platform` to fetch Linux-compatible binaries for the
Lambda runtime:

```bash
pip install --target ./package --platform manylinux2014_x86_64 --only-binary=:all: temporalio
```

To include [OpenTelemetry support](/develop/python/workers/serverless-workers/aws-lambda#add-observability), install
`temporalio[lambda-worker-otel]` instead.

Package the dependencies and your application code into a zip file:

```bash
cd package && zip -r ../function.zip . && cd ..
zip function.zip lambda_function.py my_workflows.py my_activities.py
```

</SdkTabs.Python>
<SdkTabs.TypeScript>

Build the Workflow bundle and compile the project:

```bash
npx ts-node src/scripts/build-workflow-bundle.ts
npx tsc
```

Install production dependencies and package everything into a zip:

```bash
npm install --omit=dev
zip -r function.zip lib/ node_modules/ workflow-bundle.js
```

</SdkTabs.TypeScript>
</SdkTabs>

### ii. Deploy Lambda function {/* #deploy-lambda-function-step */}

Replace the placeholder values and run the following command to create the Lambda function in your AWS environment.

<SdkTabs hideUnsupportedLanguages>
<SdkTabs.Go>

```bash
aws lambda create-function \
  --function-name my-temporal-worker \
  --runtime provided.al2023 \
  --handler bootstrap \
  --role <EXECUTION_ROLE_ARN> \
  --zip-file fileb://function.zip \
  --timeout 600 \
  --memory-size 256 \
  --environment '{"Variables":{"HOME":"/tmp","TEMPORAL_ADDRESS":"<your-temporal-address>:7233","TEMPORAL_NAMESPACE":"<your-namespace>","TEMPORAL_API_KEY":"<your-api-key>"}}'
```

| Parameter         | Description                                                                                   |
| ----------------- | --------------------------------------------------------------------------------------------- |
| `--function-name` | Name of the Lambda function.                                                                  |
| `--runtime`       | Lambda runtime. Use `provided.al2023` for custom Go binaries.                                 |
| `--handler`       | Entry point binary name. Must be `bootstrap` when using the `provided.al2023` custom runtime. |

</SdkTabs.Go>
<SdkTabs.Python>

```bash
aws lambda create-function \
  --function-name my-temporal-worker \
  --runtime python3.13 \
  --handler lambda_function.lambda_handler \
  --role <EXECUTION_ROLE_ARN> \
  --zip-file fileb://function.zip \
  --timeout 600 \
  --memory-size 256 \
  --environment '{"Variables":{"TEMPORAL_ADDRESS":"<your-temporal-address>:7233","TEMPORAL_NAMESPACE":"<your-namespace>","TEMPORAL_API_KEY":"<your-api-key>"}}'
```

| Parameter         | Description                                                                                  |
| ----------------- | -------------------------------------------------------------------------------------------- |
| `--function-name` | Name of the Lambda function.                                                                 |
| `--runtime`       | Lambda runtime. Use `python3.13` or another supported Python version.                        |
| `--handler`       | Entry point in `module.function` format. Must point to the handler returned by `run_worker`. |

</SdkTabs.Python>
<SdkTabs.TypeScript>

```bash
aws lambda create-function \
  --function-name my-temporal-worker \
  --runtime nodejs22.x \
  --handler lib/index.handler \
  --role <EXECUTION_ROLE_ARN> \
  --zip-file fileb://function.zip \
  --timeout 600 \
  --memory-size 256 \
  --environment '{"Variables":{"HOME":"/tmp","TEMPORAL_ADDRESS":"<your-temporal-address>:7233","TEMPORAL_NAMESPACE":"<your-namespace>","TEMPORAL_API_KEY":"<your-api-key>"}}'
```

| Parameter         | Description                                                                               |
| ----------------- | ----------------------------------------------------------------------------------------- |
| `--function-name` | Name of the Lambda function.                                                              |
| `--runtime`       | Lambda runtime. Use `nodejs22.x` or another supported Node.js version (20+).              |
| `--handler`       | Entry point in `module.export` format. Must point to the handler exported by `runWorker`. |

</SdkTabs.TypeScript>
</SdkTabs>

The following parameters apply to all SDKs:

| Parameter                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `--role`                        | ARN of the Lambda [execution role](https://docs.aws.amazon.com/lambda/latest/dg/lambda-intro-execution-role.html), which grants the function permission to run. Trusted principal must be `lambda.amazonaws.com`. This is separate from the role Temporal uses to invoke the function in [Step 3](#configure-iam). The role must have at least the [`AWSLambdaBasicExecutionRole`](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSLambdaBasicExecutionRole.html) managed policy attached. |
| `--zip-file`                    | Path to your packaged deployment zip.                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `--timeout`                     | Invocation deadline in seconds. This is the maximum time each Lambda invocation can run before AWS terminates it. Set this high enough for the Worker to start, process Tasks, and [shut down gracefully](/serverless-workers#worker-lifecycle).                                                                                                                                                                                                                                                              |
| `--memory-size`                 | Memory in MB allocated to each invocation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `TEMPORAL_ADDRESS`              | Temporal frontend address (e.g., `<namespace>.<account>.tmprl.cloud:7233`).                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `TEMPORAL_NAMESPACE`            | Temporal Namespace.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `TEMPORAL_TASK_QUEUE`           | Task Queue name. Overrides the value set in code.                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `TEMPORAL_TLS_CLIENT_CERT_PATH` | Path to the TLS client certificate file for mTLS authentication.                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `TEMPORAL_TLS_CLIENT_KEY_PATH`  | Path to the TLS client key file for mTLS authentication.                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `TEMPORAL_API_KEY`              | API key for API key authentication.                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |

The serverless Worker packages read environment variables and configuration files automatically at startup.
For the full list of supported environment variables, config file format, and profiles, see
[Environment configuration](/develop/environment-configuration).

Sensitive values like TLS keys and API keys should be encrypted at rest. See
[AWS documentation](https://docs.aws.amazon.com/lambda/latest/dg/configuration-envvars-encryption.html) for options.

To update an existing function with new code:

```bash
aws lambda update-function-code \
  --function-name my-temporal-worker \
  --zip-file fileb://function.zip
```

:::caution Lambda versioning best practices

Create a 1-to-1 mapping between each build ID in your Worker code and a
[Lambda function version](https://docs.aws.amazon.com/lambda/latest/dg/configuration-versions.html). If you use an
unversioned Lambda, do not change the Build Id in your Worker code without also creating a new Worker Deployment
Version.

:::

## 3. Configure IAM for Temporal invocation (Cloud only) {/* #configure-iam */}

This section applies to Temporal Cloud. For self-hosted Temporal Service deployments, see
[Self-hosted setup](/production-deployment/worker-deployments/serverless-workers/self-hosted-setup#create-invocation-role)
for IAM configuration with a different CloudFormation template.

Temporal needs permission to invoke your Lambda function. The Temporal server assumes an IAM role in your AWS account to
call `lambda:InvokeFunction`. The trust policy on the role includes an External ID condition to prevent
[confused deputy](https://docs.aws.amazon.com/IAM/latest/UserGuide/confused-deputy.html) attacks.

Deploy the following CloudFormation template to create the invocation role and its permissions.
[Download the template](/files/temporal-cloud-serverless-worker-role.yaml).

| Parameter              | Description                                                                                                                                                                                                        |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `AssumeRoleExternalId` | A string you choose to prevent [confused deputy](https://docs.aws.amazon.com/IAM/latest/UserGuide/confused-deputy.html) attacks. Can be any value. Use the same value when creating the Worker Deployment Version. |
| `LambdaFunctionARNs`   | Comma-separated list of Lambda function ARNs that Temporal may invoke. One role can authorize multiple Worker Lambdas.                                                                                             |
| `RoleName`             | Base name for the created IAM role. Defaults to `Temporal-Cloud-Serverless-Worker`.                                                                                                                                |

<details>
<summary>CloudFormation template</summary>

```yaml
