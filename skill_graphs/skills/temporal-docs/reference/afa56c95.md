# Quickstart

Configure your local development environment to get started developing with Temporal.

<SetupSteps>
<SetupStep code={
  <>
    <CodeSnippet language="bash">
    php -v
    </CodeSnippet>
  </>
}>

## Install PHP

Make sure you have PHP installed.

**If you don't have PHP:** Visit the official website to [download and install](https://www.php.net/downloads.php) it.

### GRPC extension

GRPC extension is required to work with RoadRunner application server.

**If you don't have `ext-grpc` installed:** Visit the official website to
[download and install](https://docs.cloud.google.com/php/docs/reference/help/grpc) it.

:::tip GRPC Installation Tip

On macOS with Apple Silicon (M1/M2/M3/M4) and PHP 8.3, `pecl install grpc` may appear to hang or install indefinitely.
If this happens, try installing a specific version:

```bash
pecl install channel://pecl.php.net/grpc-1.78.0RC2
```

Note: You can find the latest versions at [pecl.php.net/package/grpc](https://pecl.php.net/package/grpc).

:::

</SetupStep>

<SetupStep code={
<>
<CodeSnippet language="bash">
mkdir temporal-hello-world
</CodeSnippet>
<CodeSnippet language="bash">
cd temporal-hello-world
</CodeSnippet>
<CodeSnippet language="bash">
composer init --name="myproject/quickstart" -n
</CodeSnippet>
</>
}>

## Create a Project

Now that you have PHP installed, create a project to manage your dependencies and build your Temporal application.

</SetupStep>

<SetupStep code={
<>
<CodeSnippet language="bash">
composer require temporal/sdk
</CodeSnippet>
<CodeSnippet language="json">
{`{
    "name": "myproject/quickstart",
    "require": {
        "temporal/sdk": "^2.16"
    },
    "autoload": {
        "psr-4": {
            "App\\\\": "src/"
        }
    }
}`}
</CodeSnippet>
<CodeSnippet language="bash">
composer dump-autoload
</CodeSnippet>
</>
}>

## Add Temporal PHP SDK and Configure Autoloading

Install the Temporal SDK, then add PSR-4 autoloading to your `composer.json` so PHP can find your Workflow and Activity
classes.

Your final `composer.json` should look like this. After updating, run `composer dump-autoload` to regenerate the
autoloader.

</SetupStep>

<SetupStep code={
<>
  <Tabs>
    <TabItem value="cli" label="CLI">
      Download RoadRunner with the following command:
      <CodeSnippet language="bash">
        ./vendor/bin/rr get
      </CodeSnippet>
      When prompted "Do you want create default '.rr.yaml' configuration file?", answer yes. You'll replace it with the proper config in the next step.
    </TabItem>
    <TabItem value="dload" label="DLoad">
      Install DLoad package manager using Composer
      <CodeSnippet language="bash">
        composer require --dev internal/dload
      </CodeSnippet>
      Create a configuration file named `dload.xml` with the following content:
      <CodeSnippet language="xml">
        {`<?xml version="1.0"?>
<dload xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:noNamespaceSchemaLocation="vendor/internal/dload/dload.xsd"
       temp-dir="./runtime"
>
    <actions>
        <download software="rr" version="^2025.1.6"/>
    </actions>
</dload>
`}
      </CodeSnippet>
      Finally, download the RoadRunner binary:
      <CodeSnippet language="bash">
        ./vendor/bin/dload
      </CodeSnippet>
    </TabItem>
  </Tabs>
</>
}>

## Install RoadRunner application server

Install [RoadRunner application server](https://github.com/roadrunner-server/roadrunner). It starts and manages your PHP
processes that run Temporal Workers, and connects them to the Temporal Service over gRPC.

See [RoadRunner installation instructions](https://docs.roadrunner.dev/docs/general/install) to learn about other
installation methods.

</SetupStep>

<SetupStep code={
<>
<CodeSnippet language="yml">
  {`version: "3"

rpc: listen: tcp://127.0.0.1:6001

server: command: "php worker.php"

temporal: address: "127.0.0.1:7233"

logs: level: info `}

</CodeSnippet>
</>
}>

Create a simple configuration file named `.rr.yaml` with the following content:

</SetupStep>

<SetupStep code={
<>
<Tabs>
<TabItem value="macos" label="macOS" default>

        Install the Temporal CLI using Homebrew:
        <CodeSnippet language="bash">
        brew install temporal
        </CodeSnippet>
      </TabItem>

      <TabItem value="windows" label="Windows">
        Download the Temporal CLI archive for your architecture:

          Windows amd64
          Windows arm64

        Extract it and add <code>temporal.exe</code> to your PATH.
      </TabItem>

      <TabItem value="linux" label="Linux">
        Download the Temporal CLI for your architecture:

          Linux amd64
          Linux arm64

        Extract the archive and move the <code>temporal</code> binary into your PATH, for example:
        <CodeSnippet language="bash">
        sudo mv temporal /usr/local/bin
        </CodeSnippet>
      </TabItem>
    </Tabs>

</>
}>

## Install Temporal CLI and start the development server

The fastest way to get a development version of the Temporal Service running on your local machine is to use
[Temporal CLI](https://docs.temporal.io/cli).

Choose your operating system to install Temporal CLI:

</SetupStep>

<SetupStep code={
<>
  Add one more download action to the configuration file
  <CodeSnippet language="xml">
    {`<download software="temporal" version="^1.5"/>`}
  </CodeSnippet>
  The final configuration file should look like this:
  <CodeSnippet language="xml">
    {`<?xml version="1.0"?>
<dload xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:noNamespaceSchemaLocation="vendor/internal/dload/dload.xsd"
       temp-dir="./runtime"
>
    <actions>
        <download software="rr" version="^2025.1.6"/>
        <download software="temporal" version="^1.5"/>
    </actions>
</dload>
`}
  </CodeSnippet>
</>
}>

### DLoad package manager

Consider using DLoad to delegate all installation and updating processes to the package manager.

</SetupStep>

<SetupStep code={
<>

After installing, open a new Terminal. Keep this running in the background:
<CodeSnippet language="bash">temporal server start-dev</CodeSnippet>

Change the Web UI port
The Temporal Web UI may be on a different port in some examples or tutorials. To change the port for the Web UI, use the <code>--ui-port</code> option when starting the server:
<CodeSnippet language="bash">
temporal server start-dev --ui-port 8080
</CodeSnippet>
The Temporal Web UI will now be available at http://localhost:8080.

</>
}>

## Start the development server

Once you've installed Temporal CLI and added it to your PATH, open a new Terminal window and run the following command.

This command starts a local Temporal Service. It starts the Web UI, creates the default Namespace, and uses an in-memory
database.

The Temporal Service will be available on localhost:7233. The Temporal Web UI will be available at
http://localhost:8233.

Leave the local Temporal Service running as you work through tutorials and other projects. You can stop the Temporal
Service at any time by pressing CTRL+C.

Once you have everything installed, you're ready to build apps with Temporal on your local machine.

</SetupStep>
</SetupSteps>
## Run Hello World: Test Your Installation

Now let's verify your setup is working by creating and running a complete Temporal application with both a Workflow and
Activity.

This test will confirm that:

- The Temporal PHP SDK is properly installed
- Your local Temporal Service is running
- You can successfully create and execute Workflows and Activities
- The communication between components is functioning correctly

### 1. Create the Activity

Create an Activity file (`src/GreetingActivity.php`):

```php
<?php
declare(strict_types=1);

namespace App;

use Temporal\Activity\ActivityInterface;
use Temporal\Activity\ActivityMethod;

#[ActivityInterface]
class GreetingActivity
{
    #[ActivityMethod]
    public function greet(string $name): string
    {
        return "Hello, $name!";
    }
}
```

An Activity is a method that executes a single, well-defined action (either short or long-running), which often involves
interacting with the outside world, such as sending emails, making network requests, writing to a database, or calling
an API, which is prone to failure. If an Activity fails, Temporal automatically retries it based on your configuration.

You define Activities in PHP as classes annotated with the `Temporal\Activity\ActivityInterface` attribute.

Each method used in workflow classes should be annotated with `Temporal\Activity\ActivityMethod`.

### 2. Create the Workflow

Create a Workflow file (`src/SayHelloWorkflow.php`):

```php
<?php
declare(strict_types=1);

namespace App;

use Temporal\Activity\ActivityOptions;
use Temporal\Workflow;
use Temporal\Workflow\WorkflowInterface;
use Temporal\Workflow\WorkflowMethod;

#[WorkflowInterface]
class SayHelloWorkflow
{
    #[WorkflowMethod]
    public function sayHello(string $name)
    {
        $activity = Workflow::newActivityStub(
            GreetingActivity::class,
            ActivityOptions::new()
                ->withStartToCloseTimeout(5),
        );

        return yield $activity->greet($name);
    }
}
```

### 3. Create a Worker file

Create a Worker file (`worker.php`, under project root directory):

```php
<?php
declare(strict_types=1);

use Temporal\WorkerFactory;

ini_set('display_errors', 'stderr');
require "vendor/autoload.php";

$factory = WorkerFactory::create();

$worker = $factory->newWorker();

// Register Workflows
$worker->registerWorkflowTypes(\App\SayHelloWorkflow::class);
// Register Activities
$worker->registerActivity(\App\GreetingActivity::class);

$factory->run();
```

#### Run the Worker

Previously, we created a Worker that executes Workflow and Activity tasks.

Now, start the RoadRunner application server to run the Worker by opening up a new terminal window and running this
command:

```bash
./rr serve
```

A Worker polls a Task Queue, that you configure it to poll, looking for work to do. Once the Worker dequeues a Workflow
or Activity task from the Task Queue, it then executes the task.

Workers are a crucial part of your Temporal application as they're what actually execute the tasks defined in your
Workflows and Activities. For more information on Workers, see
[Understanding Temporal](/evaluate/understanding-temporal#workers) and a [deep dive into Workers](/workers).

### 5. Execute the Workflow

Now that your Worker is running, it's time to start a Workflow Execution.

This final step will validate that everything is working correctly with your file labeled `client.php`.

Create a separate file called `client.php`:

```php
<?php
declare(strict_types=1);

use Temporal\Client\GRPC\ServiceClient;
use Temporal\Client\WorkflowClient;

ini_set('display_errors', 'stderr');
require "vendor/autoload.php";

$client = new WorkflowClient(
    ServiceClient::create('localhost:7233'),
);

$workflowStub = $client->newWorkflowStub(\App\SayHelloWorkflow::class);
$result = $workflowStub->sayHello('Temporal');

echo "Result: {$result}\n";
```

While your Worker is still running, open a new terminal and run:

```bash
php client.php
```

### Verify Success

If everything is working correctly, you should see:

- Worker processing the workflow and activity
- Output: `Result: Hello, Temporal!`
- Workflow Execution details in the [Temporal Web UI](http://localhost:8233)

<CallToAction href="https://learn.temporal.io/getting_started/php/hello_world_in_php/">
  Run your first Temporal Application
  Create a basic Workflow and run it with the Temporal PHP SDK
</CallToAction>

<CallToAction href="https://learn.temporal.io/courses/">
  Take a Temporal 101 course
  Learn Temporal concepts and build your first application with a guided course
</CallToAction>

---

## Workers - PHP SDK

![PHP SDK Banner](/img/assets/banner-php-temporal.png)

## Workers

- [Run Worker processes](/develop/php/workers/run-worker-process)

---

## Run Worker processes - PHP SDK

## How to run Worker Processes {/* #run-a-dev-worker */}

The [Worker Process](/workers#worker-process) is where Workflow Functions and Activity Functions are executed.

- Each [Worker Entity](/workers#worker-entity) in the Worker Process must register the exact Workflow Types and Activity Types it may execute.
- Each Worker Entity must also associate itself with exactly one [Task Queue](/task-queue).
- Each Worker Entity polling the same Task Queue must be registered with the same Workflow Types and Activity Types.

A [Worker Entity](/workers#worker-entity) is the component within a Worker Process that listens to a specific Task Queue.

Although multiple Worker Entities can be in a single Worker Process, a single Worker Entity Worker Process may be perfectly sufficient.
For more information, see the [Worker tuning guide](/develop/worker-performance).

A Worker Entity contains a Workflow Worker and/or an Activity Worker, which makes progress on Workflow Executions and Activity Executions, respectively.

The [RoadRunner application server](https://roadrunner.dev/) will launch multiple Temporal PHP Worker processes based on provided `.rr.yaml` configuration.

Each Worker might connect to one or multiple Task Queues.
Workers poll the _Temporal Service_ for tasks, perform those tasks, and communicate task execution results back to the _Temporal Service_.

Worker code is developed, deployed, and operated by Temporal customers.
To create a worker use `Temporal\WorkerFactory`:

```php
<?php

declare(strict_types=1);

use Temporal\WorkerFactory;

ini_set('display_errors', 'stderr');
include "vendor/autoload.php";

// factory initiates and runs task queue specific activity and workflow workers
$factory = WorkerFactory::create();

// Worker that listens on a Task Queue and hosts both workflow and activity implementations.
$worker = $factory->newWorker();

// Workflows are stateful. So you need a type to create instances.
$worker->registerWorkflowTypes(App\DemoWorkflow::class);

// Activities are stateless and thread safe. So a shared instance is used.
$worker->registerActivity(App\DemoActivity::class);

// In case an activity class requires some external dependencies provide a callback - factory
// that creates or builds a new activity instance. The factory should be a callable which accepts
// an instance of ReflectionClass with an activity class which should be created.
$worker->registerActivity(App\DemoActivity::class, fn(ReflectionClass $class) => $container->create($class->getName()));

// start primary loop
$factory->run();
```

You can configure task queue name using first argument of `WorkerFactory`->`newWorker`:

```php
$worker = $factory->newWorker('your-task-queue');
```

As mentioned preceding, you can create as many Task Queue connections inside a single Worker Process as you need.

To configure additional WorkerOptions use `Temporal\Worker\WorkerOptions`:

```php
use Temporal\Worker\WorkerOptions;

$worker = $factory->newWorker(
    'your-task-queue',
    WorkerOptions::new()
        ->withMaxConcurrentWorkflowTaskPollers(10)
);
```

Make sure to point the Worker file in application server configuration:

```yaml
rpc:
  listen: tcp://127.0.0.1:6001

server:
  command: 'php worker.php'

temporal:
  address: 'temporal:7233'
  activities:
    num_workers: 10
```

> You can serve HTTP endpoints using the same server setup.

To provide the [API key](/cloud/api-keys) to RoadRunner use a `ServiceCredentials` DTO when creating the WorkerFactory:

```php
use Temporal\Worker\ServiceCredentials;

$workerFactory = \Temporal\WorkerFactory::create(
    credentials: ServiceCredentials::create()->withApiKey('your-api-key'),
);
```

[How to configure connection to a Temporal Cloud](/develop/php/client/temporal-client#connect-to-temporal-cloud)

### How to register types {/* #register-types */}

All Workers listening to the same Task Queue name must be registered to handle the exact same Workflows Types and Activity Types.

If a Worker polls a Task for a Workflow Type or Activity Type it does not know about, it fails that Task.
However, the failure of the Task does not cause the associated Workflow Execution to fail.

Worker listens on a Task Queue and hosts both Workflow and Activity implementations:

```php
// Workflows are stateful. So you need a type to create instances:
$worker->registerWorkflowTypes(App\DemoWorkflow::class);
// Activities are stateless and thread safe:
$worker->registerActivity(App\DemoActivity::class);
```

In case an activity class requires some external dependencies provide a callback - factory
that creates or builds a new activity instance. The factory should be a callable which accepts
an instance of ReflectionClass with an activity class which should be created.

```php
$worker->registerActivity(
    App\DemoActivity::class,
    fn(ReflectionClass $class) => $container->create($class->getName())
);
```

If you want to clean up some resources after activity is done, you may register a finalizer. This callback is called
after each activity invocation:

```php
$worker->registerActivityFinalizer(fn() => $kernel->shutdown());
```

---

## Workflow Basics - PHP SDK

## How to develop a basic Workflow {/* #develop-workflows */}

Workflows are the fundamental unit of a Temporal Application, and it all starts with the development of a [Workflow Definition](/workflow-definition).

In the Temporal PHP SDK programming model, Workflows are a class method. Classes must implement interfaces that are annotated with `#[WorkflowInterface]`. The method that is the Workflow must be annotated with `#[WorkflowMethod]`.

```php
use Temporal\Workflow\YourWorkflowInterface;
use Temporal\Workflow\WorkflowMethod;

#[WorkflowInterface]
interface FileProcessingWorkflow
{
    #[WorkflowMethod]
    public function processFile(Argument $args);

}
```

### How to define Workflow parameters {/* #workflow-parameters */}

Temporal Workflows may have any number of custom parameters.
However, we strongly recommend that objects are used as parameters, so that the object's individual fields may be altered without breaking the signature of the Workflow.
All Workflow Definition parameters must be serializable.

A method annotated with `#[WorkflowMethod]` can have any number of parameters.

We recommend passing a single parameter that contains all the input fields to allow for adding fields in a backward-compatible manner.

Note that all inputs should be serializable to a byte array using the provided [DataConverter](https://github.com/temporalio/sdk-php/blob/master/src/DataConverter/DataConverterInterface.php) interface.
The default implementation uses a JSON serializer, but an alternative implementation can be easily configured.
You can create a custom object and pass it to the Workflow method, as shown in the following example:

```php
#[WorkflowInterface]
interface FileProcessingWorkflow {
    #[WorkflowMethod]
    public function processFile(Argument $args);
}
```

### How to define Workflow return parameters {/* #workflow-return-values */}

Workflow return values must also be serializable.
Returning results, returning errors, or throwing exceptions is fairly idiomatic in each language that is supported.
However, Temporal APIs that must be used to get the result of a Workflow Execution will only ever receive one of either the result or the error.

A Workflow method returns a Generator.
To properly typecast the Workflow's return value in the client code, use the `#[ReturnType()]` attribute.

```php
#[WorkflowInterface]
interface FileProcessingWorkflow {

    #[WorkflowMethod]
    #[ReturnType("string")]
    public function processFile(Argument $args);
}
```

### How to customize your Workflow Type {/* #workflow-type */}

Workflows have a Type that are referred to as the Workflow name.

The following examples demonstrate how to set a custom name for your Workflow Type.

To customize a Workflow Type, use the `WorkflowMethod` attribute to specify the name of Workflow.

```php
#[WorkflowMethod(name)]
```

If a Workflow Type is not specified, then Workflow Type defaults to the interface name, which is `YourWorkflowDefinitionInterface` in this case.

```php
#[WorkflowInterface]
interface YourWorkflowDefinitionInterface
{
    #[WorkflowMethod]
    public function processFile(Argument $args);
}
```

### How to develop Workflow logic {/* #workflow-logic-requirements */}

Workflow logic is constrained by [deterministic execution requirements](/workflow-definition#deterministic-constraints). Each Temporal SDK provides a set of APIs that can be used inside your Workflow to interact with application code outside the Workflow. used inside your Workflow to interact with external (to the Workflow) application code.

\*\*Temporal uses the [Microsoft Azure Event Sourcing pattern](https://docs.microsoft.com/en-us/azure/architecture/patterns/event-sourcing) to recover the state of a Workflow object including its local variable values.

In essence, every time a Workflow state has to be restored, its code is re-executed from the beginning.
When replaying, side effects (such as Activity invocations) are ignored because they are already recorded in the Workflow event history.
When writing Workflow logic, the replay is not visible, so the code should be written since it executes only once.
This design puts the following constraints on the Workflow implementation:

- Do not use any mutable global variables because multiple instances of Workflows are executed in parallel.
- Do not call any non-deterministic functions like non seeded random or `UUID` directly from the Workflow code.

Always do the following in the Workflow implementation code:

- Don't perform any IO or service calls as they are not usually deterministic. Use Activities for this.
- Only use `Workflow::now()` to get the current time inside a Workflow.
- Call `yield Workflow::timer()` instead of `sleep()`.
- Do not use any blocking SPL provided by PHP (i.e. `fopen`, `PDO`, etc) in **Workflow code**.
- Use `yield Workflow::getVersion()` when making any changes to the Workflow code. Without this, any deployment of updated Workflow code
  might break already open Workflows.
- Don't access configuration APIs directly from a Workflow because changes in the configuration might affect a Workflow Execution path.
  Pass it as an argument to a Workflow function or use an Activity to load it.

Workflow method arguments and return values are serializable to a byte array using the provided [DataConverter](https://www.javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/common/converter/DataConverter.html) interface.
The default implementation uses JSON serializer, but you can use any alternative serialization mechanism.

Make sure to annotate your `WorkflowMethod` using `ReturnType` to specify concrete return type.

> You can not use the default return type declaration as Workflow methods are generators.

The values passed to Workflows through invocation parameters or returned through a result value are recorded in the execution history.
The entire execution history is transferred from the Temporal service to Workflow workers with every event that the Workflow logic needs to process.
A large execution history can thus adversely impact the performance of your Workflow.
Therefore, be mindful of the amount of data that you transfer via Activity invocation parameters or return values.
Otherwise, no additional limitations exist on Activity implementations.\*\*

---

## Cancel a Workflow - PHP SDK

## Cancel an Activity from a Workflow {/* #cancel-an-activity */}

Canceling an Activity from within a Workflow requires that the Activity Execution sends Heartbeats and sets a Heartbeat
Timeout. If the Heartbeat is not invoked, the Activity cannot receive a cancellation request. When any non-immediate
Activity is executed, the Activity Execution should send Heartbeats and set a
[Heartbeat Timeout](/encyclopedia/detecting-activity-failures#heartbeat-timeout) to ensure that the server knows it is
still working.

When an Activity is canceled, an error is raised in the Activity at the next available opportunity. If cleanup logic
needs to be performed, it can be done in a `finally` clause or inside a caught cancel error. However, for the Activity
to appear canceled the exception needs to be re-raised.

:::note

Unlike regular Activities, [Local Activities](/local-activity) can be canceled if they don't send Heartbeats. Local
Activities are handled locally, and all the information needed to handle the cancellation logic is available in the same
Worker process.

:::

## Reset a Workflow Execution {/* #reset */}

Resetting a Workflow Execution terminates the current Workflow Execution and starts a new Workflow Execution from a
point you specify in its Event History. Use reset when a Workflow is blocked due to a non-deterministic error or other
issues that prevent it from completing.

When you reset a Workflow, the Event History up to the reset point is copied to the new Workflow Execution, and the
Workflow resumes from that point with the current code. Reset only works if you've fixed the underlying issue, such as
removing non-deterministic code. Any progress made after the reset point will be discarded. Provide a reason when
resetting, as it will be recorded in the Event History.

<Tabs>

<TabItem value="web-ui" label="Web UI">

1. Navigate to the Workflow Execution details page,
2. Click the **Reset** button in the top right dropdown menu,
3. Select the Event ID to reset to,
4. Provide a reason for the reset,
5. Confirm the reset.

The Web UI shows available reset points and creates a link to the new Workflow Execution after the reset completes.
