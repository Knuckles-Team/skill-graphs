# Wait for them all to complete
Temporalio::Workflow::Future.all_of(fut1, fut2, fut3).wait

Temporalio::Workflow.logger.info("Got: #{fut1.result}, #{fut2.result}, #{fut3.result}")
```

Or, say, to wait on the first of 5 activities or a timeout to complete:

```ruby
