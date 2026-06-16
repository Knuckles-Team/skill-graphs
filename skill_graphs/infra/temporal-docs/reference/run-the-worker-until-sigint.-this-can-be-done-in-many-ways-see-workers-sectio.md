# Run the worker until SIGINT. This can be done in many ways, see "Workers" section for details.
worker.run(shutdown_signals: ['SIGINT'])
```

Run the Worker:

```bash
ruby worker.rb
```

### 4. Execute the Workflow

Now that your Worker is running, it's time to start a Workflow Execution.

Create a separate file called starter.rb:

```ruby
require 'temporalio/client'
require_relative 'say_hello_workflow'
