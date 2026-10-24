# Start workflow with the search attribute set
handle = my_client.start_workflow(
  MyWorkflow, 'some-input',
  id: 'my-workflow-id', task_queue: 'my-task-queue',
  search_attributes: Temporalio::SearchAttributes.new({ MY_KEYWORD_KEY => 'some-value' })
)
```

### Upsert Search Attributes {/* #upsert-search-attributes */}

You can upsert Search Attributes to add, update, or remove Search Attributes from within Workflow code.

To upsert custom Search Attributes, use the [`upsert_search_attributes`](https://ruby.temporal.io/Temporalio/Workflow.html#upsert_search_attributes-class_method) method with a set of updates.
Keys should be predefined for reuse.

```ruby
