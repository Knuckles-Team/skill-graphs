# Quickstart

Configure your local development environment to get started developing with Temporal.

<SetupSteps>
<SetupStep code={
  <>
    <CodeSnippet language="bash">
    java -version
    </CodeSnippet>
  </>
}>
## Install the Java JDK

Make sure you have the Java JDK installed. You can either download a copy directly from Oracle or select an OpenJDK
distribution from your preferred vendor.

You'll also need either Maven or Gradle installed.

**If you don't have Maven:** [Download](https://maven.apache.org/download.cgi) and
[install](https://maven.apache.org/install.html) from Apache.org, or use Homebrew: `brew install maven`.

**If you don't have Gradle:** [Download](https://gradle.org/install/) from Gradle.org, use
[IntelliJ IDEA](https://www.jetbrains.com/idea/) (bundled), or use Homebrew: `brew install gradle`.

</SetupStep>

<SetupStep code={
<>
<Tabs groupId="build-tool" queryString>
<TabItem value="maven" label="Maven">

<CodeSnippet language="bash">mkdir temporal-java-project</CodeSnippet>
<CodeSnippet language="bash">cd temporal-java-project</CodeSnippet>
<CodeSnippet language="bash">
  mvn archetype:generate -DgroupId=helloworkflow -DartifactId=temporal-hello-world
  -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false
</CodeSnippet>
<CodeSnippet language="bash">cd temporal-hello-world</CodeSnippet>

</TabItem>
<TabItem value="gradle" label="Gradle">

<CodeSnippet language="bash">mkdir temporal-hello-world</CodeSnippet>
<CodeSnippet language="bash">cd temporal-hello-world</CodeSnippet>
<CodeSnippet language="bash">
  gradle init --type java-application --project-name temporal-hello-world --package helloworkflow
</CodeSnippet>

</TabItem>
</Tabs>
</>
}>

## Create a Project

Now that you have your build tool installed, create a project to manage your dependencies and build your Temporal
application.

Choose your build tool to create the appropriate project structure. For Maven, this creates a standard project with the
necessary directories and a basic pom.xml file. For Gradle, this creates a project with build.gradle and the standard
Gradle directory structure.

</SetupStep>

<SetupStep code={
<>
<Tabs groupId="build-tool" queryString>
<TabItem value="maven" label="Maven">

<CodeSnippet language="xml">
{`<dependencies>
  <!--
    Temporal dependencies needed to compile, build,
    test, and run Temporal's Java SDK
  -->

  <!--
    SDK
  -->

<dependency>
  <groupId>io.temporal</groupId>
  <artifactId>temporal-sdk</artifactId>
  <version>1.33.0</version>
</dependency>

  <dependency>
    <!--
      Testing
    -->
    <groupId>io.temporal</groupId>
    <artifactId>temporal-testing</artifactId>
    <version>1.33.0</version>
    <scope>test</scope>
  </dependency>
</dependencies>`}
</CodeSnippet>

</TabItem>
<TabItem value="gradle" label="Gradle">

<CodeSnippet language="groovy">
{`plugins {
    id 'application'
}

repositories { mavenCentral() }

dependencies {
    implementation 'io.temporal:temporal-sdk:1.33.0'
    testImplementation 'io.temporal:temporal-testing:1.33.0'
}

// Define the main class for the application
application { mainClass = 'helloworkflow.Starter' }

// Helper tasks to run the worker and the starter
tasks.register('runWorker', JavaExec) {
    group = 'application'
    description = 'Run the Temporal worker'
    classpath = sourceSets.main.runtimeClasspath
    mainClass = 'helloworkflow.SayHelloWorker'
}

tasks.register('runStarter', JavaExec) {
    group = 'application'
    description = 'Run the workflow starter'
    classpath = sourceSets.main.runtimeClasspath
    mainClass = 'helloworkflow.Starter'
}`}

</CodeSnippet>

<CodeSnippet language="bash">
./gradlew build
</CodeSnippet>
</TabItem>
</Tabs>
</>
}>

## Add Temporal Java SDK Dependencies

Now add the Temporal SDK dependencies to your project configuration file.

For Maven, add the following dependencies to your `pom.xml` file. For Gradle, add the following lines to your
`build.gradle` file.

Next, you'll configure a local Temporal Service for development.

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

- The Temporal Java SDK is properly installed
- Your local Temporal Service is running
- You can successfully create and execute Workflows and Activities
- The communication between components is functioning correctly

### 1. Create the Activity Interface

Create an Activity interface file (GreetActivities.java):

_Note that all files for this quickstart will be created under src/main/java/helloworkflow._

```java
package helloworkflow;

@ActivityInterface
public interface GreetActivities {

    @ActivityMethod
    String greet(String name);

}
```

An Activity is a method that executes a single, well-defined action (either short or long running), which often involve
interacting with the outside world, such as sending emails, making network requests, writing to a database, or calling
an API, which are prone to failure. If an Activity fails, Temporal automatically retries it based on your configuration.

You define Activities in Java as an annotated interface, and its implementation.

### 2. Create the Activity Implementation

Create an Activity implementation file (GreetActivitiesImpl.java):

```java
package helloworkflow;

public class GreetActivitiesImpl implements GreetActivities {

    @Override
    public String greet(String name) {
      return "Hello " + name;
    }

}
```

### 3. Create the Workflow

Create a Workflow file (SayHelloWorkflow.java):

```java
package helloworkflow;

@WorkflowInterface
public interface SayHelloWorkflow {

    @WorkflowMethod
    String sayHello(String name);

}
```

Workflows orchestrate Activities and contain the application logic. Temporal Workflows are resilient. They can run and
keep running for years, even if the underlying infrastructure fails. If the application itself crashes, Temporal will
automatically recreate its pre-failure state so it can continue right where it left off.

You define Workflows in Java as an annotated interface, and its implementation.

### 4. Create the Workflow Implementation

Create a Workflow implementation file (SayHelloWorkflowImpl.java):

```java
package helloworkflow;

public class SayHelloWorkflowImpl implements SayHelloWorkflow {

    private final GreetActivities activities = Workflow.newActivityStub(
      GreetActivities.class,
      ActivityOptions.newBuilder()
        .setStartToCloseTimeout(Duration.ofSeconds(5))
        .build()
    );

    @Override
    public String sayHello(String name) {
      return activities.greet(name);
    }

}
```

### 5. Create and Run the Worker

Create a Worker file (SayHelloWorker.java):

```java
package helloworkflow;

public class SayHelloWorker {

    public static void main(String[] args) {

      WorkflowServiceStubs service = WorkflowServiceStubs.newLocalServiceStubs();
      WorkflowClient client = WorkflowClient.newInstance(service);
      WorkerFactory factory = WorkerFactory.newInstance(client);

      Worker worker = factory.newWorker("my-task-queue");
      worker.registerWorkflowImplementationTypes(SayHelloWorkflowImpl.class);
      worker.registerActivitiesImplementations(new GreetActivitiesImpl());

      System.out.println("Starting SayHelloWorker for task queue 'my-task-queue'...");

      factory.start();

    }

}
```

With your Activity and Workflow defined, you need a Worker to execute them.

Open a new terminal and run the Worker:

<Tabs>
<TabItem value="maven" label="Maven">

```bash
cd temporal-hello-world
mvn compile exec:java -Dexec.mainClass="helloworkflow.SayHelloWorker"
```

</TabItem>
<TabItem value="gradle" label="Gradle">

```bash
./gradlew runWorker
```

</TabItem>
</Tabs>

A Worker polls a Task Queue, that you configure it to poll, looking for work to do. Once the Worker dequeues a Workflow
or Activity task from the Task Queue, it then executes that task.

Workers are a crucial part of your Temporal application as they're what actually execute the tasks defined in your
Workflows and Activities. For more information on Workers, see
[Understanding Temporal](/evaluate/understanding-temporal#workers) and a [deep dive into Workers](/workers).

### 6. Execute the Workflow

Now that your Worker is running, it's time to start a Workflow Execution.

This final step will validate that everything is working correctly with your file labeled `Starter.java`.

Create a separate file called `Starter.java`:

```java
package helloworkflow;

public class Starter {
    public static void main(String[] args) {
        WorkflowServiceStubs service = WorkflowServiceStubs.newLocalServiceStubs();
        WorkflowClient client = WorkflowClient.newInstance(service);

        SayHelloWorkflow workflow = client.newWorkflowStub(
            SayHelloWorkflow.class,
            WorkflowOptions.newBuilder()
                .setTaskQueue("my-task-queue")
                .setWorkflowId("say-hello-workflow-id")
                .build()
        );

        String result = workflow.sayHello("Temporal");
        System.out.println("Workflow result: " + result);

        service.shutdown();
        service.awaitTermination(10, java.util.concurrent.TimeUnit.SECONDS);
    }
}
```

While your worker is still running, open a new terminal and run:

<Tabs>
<TabItem value="maven" label="Maven">

```bash
cd temporal-hello-world
mvn compile exec:java -Dexec.mainClass="helloworkflow.Starter"
```

</TabItem>
<TabItem value="gradle" label="Gradle">

```bash
./gradlew runStarter
```

</TabItem>
</Tabs>

### Verify Success

If everything is working correctly, you should see:

- Worker processing the workflow and activity
- Output: `Workflow result: Hello Temporal`
- Workflow Execution details in the [Temporal Web UI](http://localhost:8233)

<CallToAction href="https://learn.temporal.io/getting_started/java/first_program_in_java/">
  Run your first Temporal Application
  Create a basic Workflow and run it with the Temporal Java SDK
</CallToAction>

<CallToAction href="https://learn.temporal.io/courses/">
  Take a Temporal 101 course
  Learn Temporal concepts and build your first application with a guided course
</CallToAction>

---

## Worker Versioning (Legacy) - Java SDK

## How to use Worker Versioning in Java (Deprecated) {/* #worker-versioning */}

:::caution

This section is for a deprecated Worker Versioning API. Please redirect your attention to [Worker Versioning](/production-deployment/worker-deployments/worker-versioning).

See the [Pre-release README](https://github.com/temporalio/temporal/blob/main/docs/worker-versioning.md) for more information.

:::
A Build ID corresponds to a deployment. If you don't already have one, we recommend a hash of the code--such as a Git SHA--combined with a human-readable timestamp.
To use Worker Versioning, you need to pass a Build ID to your Java Worker and opt in to Worker Versioning.

### Assign a Build ID to your Worker and opt in to Worker Versioning

You should understand assignment rules before completing this step.
See the [Worker Versioning Pre-release README](https://github.com/temporalio/temporal/blob/main/docs/worker-versioning.md) for more information.

To enable Worker Versioning for your worker, assign the Build ID--perhaps from an environment variable--and turn it on.

```java
// ...
WorkerOptions workerOptions = WorkerOptions.newBuilder()
    .setBuildId(buildId)
    .setUseBuildIdForVersioning(true)
    // ...
    .build();
Worker w = workerFactory.newWorker("your_task_queue_name", workerOptions);
// ...
```

:::warning

Importantly, when you start this Worker, it won't receive any tasks until you set up assignment rules.

:::

### Specify versions for Activities, Child Workflows, and Continue-as-New

:::caution

Java support for this feature is under construction!

:::

By default, Activities, Child Workflows, and Continue-as-New Workflows are run on the build of the workflow that created them if they are also configured to run on the same Task Queue.
When configured to run on a separate Task Queue, they will default to using the current assignment rules.

If you want to override this behavior, you can specify your intent via the `setVersioningIntent` method on the `ActivityOptions`, `ChildWorkflowOptions`, or `ContinueAsNewOptions` objects.

For example, if you want an Activity to use the latest assignment rules rather than inheriting from its parent:

```java
// ...
private final MyActivity activity =
    Workflow.newActivityStub(
        MyActivity.class,
        ActivityOptions.newBuilder()
          .setScheduleToCloseTimeout(Duration.ofSeconds(10))
          .setVersioningIntent(VersioningIntent.VERSIONING_INTENT_USE_ASSIGNMENT_RULES)
          // ...other options
          .build()
    );
// ...
```

### Tell the Task Queue about your Worker's Build ID (Deprecated)

:::caution

This section is for a deprecated Worker Versioning API. Please redirect your attention to [Worker Versioning](/production-deployment/worker-deployments/worker-versioning).

:::

Now you can use the SDK (or the Temporal CLI) to tell the Task Queue about your Worker's Build ID.
You might want to do this as part of your CI deployment process.

```java
// ...
workflowClient.updateWorkerBuildIdCompatability(
    "your_task_queue_name", BuildIdOperation.newIdInNewDefaultSet("deadbeef"));
```

This code adds the `deadbeef` Build ID to the Task Queue as the sole version in a new version set, which becomes the default for the queue.
New Workflows execute on Workers with this Build ID, and existing ones will continue to process by appropriately compatible Workers.

If, instead, you want to add the Build ID to an existing compatible set, you can do this:

```java
// ...
workflowClient.updateWorkerBuildIdCompatability(
    "your_task_queue_name", BuildIdOperation.newCompatibleVersion("deadbeef", "some-existing-build-id"));
```

This code adds `deadbeef` to the existing compatible set containing `some-existing-build-id` and marks it as the new default Build ID for that set.

You can also promote an existing Build ID in a set to be the default for that set:

```java
// ...
workflowClient.updateWorkerBuildIdCompatability(
    "your_task_queue_name", BuildIdOperation.promoteBuildIdWithinSet("deadbeef"));
```

You can also promote an entire set to become the default set for the queue. New Workflows will start using that set's default.

```java
// ...
workflowClient.updateWorkerBuildIdCompatability(
    "your_task_queue_name", BuildIdOperation.promoteSetByBuildId("deadbeef"));
```

---

## Workers - Java SDK

![Java SDK Banner](/img/assets/banner-java-temporal.png)

## Workers

- [Run Worker processes](/develop/java/workers/run-worker-process)

---

## Worker processes - Java SDK

## How to run Worker Processes {/* #run-a-dev-worker */}

The [Worker Process](/workers#worker-process) is where Workflow Functions and Activity Functions are executed.

- Each [Worker Entity](/workers#worker-entity) in the Worker Process must register the exact Workflow Types and Activity Types it may execute.
- Each Worker Entity must also associate itself with exactly one [Task Queue](/task-queue).
- Each Worker Entity polling the same Task Queue must be registered with the same Workflow Types and Activity Types.

A [Worker Entity](/workers#worker-entity) is the component within a Worker Process that listens to a specific Task Queue.

Although multiple Worker Entities can be in a single Worker Process, a single Worker Entity Worker Process may be perfectly sufficient.
For more information, see the [Worker tuning guide](/develop/worker-performance).

A Worker Entity contains a Workflow Worker and/or an Activity Worker, which makes progress on Workflow Executions and Activity Executions, respectively.

Use the `newWorker` method on an instance of a [`WorkerFactory`](https://www.javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/worker/WorkerFactory.html) to create a new Worker in Java.

A single Worker Entity can contain many Worker Objects.
Call the `start()` method on the instance of the `WorkerFactory` to start all the Workers created in this process.

```java
// ...

public class YourWorker {

  public static void main(String[] args) {

    WorkflowServiceStubs service = WorkflowServiceStubs.newLocalServiceStubs();
    WorkflowClient client = WorkflowClient.newInstance(service);
    WorkerFactory factory = WorkerFactory.newInstance(client);
    Worker yourWorker = factory.newWorker("your_task_queue");

    // Register Workflow
    // and/or register Activities

    factory.start();
  }
}
```

After creating the Worker entity, register all Workflow Types and all Activity Types that the Worker can execute.
A Worker can be registered with just Workflows, just Activities, or both.

**Operation guides:**

- [How to tune Workers](/develop/worker-performance)

## How to register types {/* #register-types */}

All Workers listening to the same Task Queue name must be registered to handle the exact same Workflows Types and Activity Types.

If a Worker polls a Task for a Workflow Type or Activity Type it does not know about, it fails that Task.
However, the failure of the Task does not cause the associated Workflow Execution to fail.

Use `worker.registerWorkflowImplementationTypes` to register Workflow Type and `worker.registerActivitiesImplementations` to register Activity implementation with Workers.

For Workflows, the Workflow Type is registered with a Worker.
A Workflow Type can be registered only once per Worker entity.
If you define multiple Workflow implementations of the same type, you get an exception at the time of registration.

For Activities, Activity implementation instances are registered with a Worker because they are stateless and thread-safe.
You can pass any number of dependencies in the Activity implementation constructor, such as the database connections, services, etc.

The following example shows how to register a Workflow and an Activity with a Worker.

```java
Worker worker = workerFactory.newWorker("your_task_queue");
...
// Register Workflow
worker.registerWorkflowImplementationTypes(GreetingWorkflowImpl.class);
// Register Activity
worker.registerActivitiesImplementations(new GreetingActivitiesImpl());
```

When you register a single instance of an Activity, you can have multiple instances of Workflow Executions calling the same Activity.
Activity code must be thread-safe because the same instance of the Activity code is run for every Workflow Execution that calls it.

For `DynamicWorkflow`, only one Workflow implementation that extends `DynamicWorkflow` can be registered with a Worker.
The following example shows how to register the `DynamicWorkflow` and `DynamicActivity` implementation with a Worker.

```java
  public static void main(String[] arg) {

    WorkflowServiceStubs service = WorkflowServiceStubs.newInstance();
    WorkflowClient client = WorkflowClient.newInstance(service);
    WorkerFactory factory = WorkerFactory.newInstance(client);
    Worker worker = factory.newWorker(TASK_QUEUE);

    /* Register the Dynamic Workflow implementation with the Worker. Workflow implementations
    ** must be known to the Worker at runtime to dispatch Workflow Tasks.
    */
    worker.registerWorkflowImplementationTypes(DynamicGreetingWorkflowImpl.class);

    // Start all the Workers that are in this process.
    factory.start();

    /* Create the Workflow stub. Note that the Workflow Type is not explicitly registered with the Worker. */
    WorkflowOptions workflowOptions =
        WorkflowOptions.newBuilder().setTaskQueue(TASK_QUEUE).setWorkflowId(WORKFLOW_ID).build();
    WorkflowStub workflow = client.newUntypedWorkflowStub("DynamicWF", workflowOptions);
    /**
     * Register Dynamic Activity implementation with the Worker. Since Activities are stateless
     * and thread-safe, we need to register a shared instance.
    */
    worker.registerActivitiesImplementations(new DynamicGreetingActivityImpl());

    /* Start Workflow Execution and immmediately send Signal. Pass in the Workflow args and Signal args. */
    workflow.signalWithStart("greetingSignal", new Object[] {"John"}, new Object[] {"Hello"});

    // Wait for the Workflow to finish getting the results.
    String result = workflow.getResult(String.class);

    System.out.println(result);

    System.exit(0);
  }
}
```

You can register multiple type-specific Workflow implementations alongside a single `DynamicWorkflow` implementation.
You can register only one Activity instance that implements `DynamicActivity` with a Worker.

---

## Workflow basics - Java SDK

## How to develop a Workflow {/* #develop-workflows */}

Workflows are the fundamental unit of a Temporal Application, and it all starts with the development of a [Workflow Definition](/workflow-definition).

In the Temporal Java SDK programming model, a Workflow Definition comprises a Workflow interface annotated with `@WorkflowInterface` and a Workflow implementation that implements the Workflow interface.

The Workflow interface is a Java interface and is annotated with `@WorkflowInterface`.
Each Workflow interface must have only one method annotated with `@WorkflowMethod`.

```java
// Workflow interface
@WorkflowInterface
public interface YourWorkflow {

    @WorkflowMethod
    String yourWFMethod(Arguments args);
}
```

However, when using dynamic Workflows, do not specify a `@WorkflowMethod`, and implement the `DynamicWorkflow` directly in the Workflow implementation code.

The `@WorkflowMethod` identifies the method that is the starting point of the Workflow Execution.
The Workflow Execution completes when this method completes.

You can create [interface inheritance hierarchies](#interface-inheritance) to reuse components across other Workflow interfaces.
The interface inheritance approach does not apply to `@WorkflowMethod` annotations.

A Workflow implementation implements a Workflow interface.

```java
// Define the Workflow implementation which implements our getGreeting Workflow method.
  public static class GreetingWorkflowImpl implements GreetingWorkflow {
      ...
    }
  }
```

To call Activities in your Workflow, call the Activity implementation.

Use `ExternalWorkflowStub` to start or send Signals from within a Workflow to other running Workflow Executions.

You can also invoke other Workflows as Child Workflows with `Workflow.newChildWorkflowStub()` or `Workflow.newUntypedChildWorkflowStub()` within a Workflow Definition.

## Workflow interface inheritance {/* #interface-inheritance */}

Workflow interfaces can form inheritance hierarchies.
It may be useful for creating reusable components across multiple
Workflow interfaces.
For example imagine a UI or CLI button that allows a `retryNow` Signal on any Workflow. To implement this feature you can redesign an interface like the following:

```java
public interface Retryable {
    @SignalMethod
    void retryNow();
}

@WorkflowInterface
public interface FileProcessingWorkflow extends Retryable {

    @WorkflowMethod
    String processFile(Arguments args);

    @QueryMethod(name="history")
