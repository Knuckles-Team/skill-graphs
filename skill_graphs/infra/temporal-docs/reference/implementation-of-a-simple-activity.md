# Implementation of a simple activity
class SayHelloActivity < Temporalio::Activity::Definition
  def execute(name)
    "Hello, #{name}!"
  end
end
```

### 2. Create the Workflow

Create a Workflow file (say_hello_workflow.rb):

```ruby
require 'temporalio/workflow'
require_relative 'say_hello_activity'

class SayHelloWorkflow < Temporalio::Workflow::Definition
  def execute(name)
    Temporalio::Workflow.execute_activity(
      SayHelloActivity,
      name,
      schedule_to_close_timeout: 300
    )
  end
end
```

### 3. Create and Run the Worker

With your Activity and Workflow defined, you need a Worker to execute them. Workers are a crucial part of your Temporal
application as they're what actually execute the tasks defined in your Workflows and Activities. For more information on
Workers, see [Understanding Temporal](/evaluate/understanding-temporal#workers) and a
[deep dive into Workers](/workers).

Create a Worker file (worker.rb):

```ruby
require 'temporalio/client'
require 'temporalio/worker'
require_relative 'say_hello_activity'
require_relative 'say_hello_workflow'
