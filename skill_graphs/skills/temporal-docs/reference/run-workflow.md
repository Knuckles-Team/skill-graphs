# Run workflow
result = client.execute_workflow(
  SayHelloWorkflow,
  'Temporal', # This is the input to the workflow
  id: 'my-workflow-id',
  task_queue: 'my-task-queue'
)
puts "Result: #{result}"
```

Then run:

```bash
ruby starter.rb
```

### Verify Success

If everything is working correctly, you should see:

- Worker processing the workflow and activity
- Output: `Workflow result: Hello, Temporal!`
- Workflow Execution details in the [Temporal Web UI](http://localhost:8233)

<CallToAction href="https://learn.temporal.io/getting_started/ruby/first_program_in_ruby/">
  Run your first Temporal Application
  Create a basic Workflow and run it with the Temporal Ruby SDK
</CallToAction>

<CallToAction href="https://learn.temporal.io/courses/">
  Take a Temporal 101 course
  Learn Temporal concepts and build your first application with a guided course
</CallToAction>

---

## Workers - Ruby SDK

![Ruby SDK Banner](/img/assets/banner-ruby-temporal.png)

## Workers

- [Worker processes](/develop/ruby/workers/run-worker-process)

---

## Worker processes - Ruby SDK

## Run Worker Process {/* #run-worker-process */}

The [Worker Process](/workers#worker-process) is where Workflow Functions and Activity Functions are actually executed.
In a Temporal application deployment, you ship and scale as many Workers as you need to handle the load of your Workflows and Activities.

- Each [Worker Entity](/workers#worker-entity) in the Worker Process must register the exact Workflow Types and Activity Types it may execute.
- Each Worker Entity must also associate itself with exactly one [Task Queue](/task-queue).
- Each Worker Entity polling the same Task Queue must be registered with the same Workflow Types and Activity Types.

A [Worker Entity](/workers#worker-entity) is the component within a Worker Process that listens to a specific Task Queue.

A Worker Entity contains a Workflow Worker and/or an Activity Worker, which makes progress on Workflow Executions and Activity Executions, respectively.

Workers are implemented in each Temporal SDK, and can be deployed with just a bit of boilerplate.
To create a Worker, use `Temporalio::Worker.new()`, providing the Worker options which include Task Queue, Workflows, and Activities and more.

The following code example creates a Worker that polls for tasks from the Task Queue and executes the Workflow.
When a Worker is created, it accepts a list of Workflows, a list of Activities, or both.

```ruby
