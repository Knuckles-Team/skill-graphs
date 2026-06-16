# Start a workflow with static summary and details
handle = client.start_workflow(
  'YourWorkflow',
  'workflow input',
  id: 'your-workflow-id',
  task_queue: 'your-task-queue',
  static_summary: 'Order processing for customer #12345',
  static_details: 'Processing premium order with expedited shipping'
)
```

`static_summary:` is a single-line description that appears in the Workflow list view, limited to 200 bytes.
`static_details:` can be multi-line and provides more comprehensive information that appears in the Workflow details view, with a larger limit of 20K bytes.

The input format is standard Markdown excluding images, HTML, and scripts.

You can also use `execute_workflow` for synchronous execution:

```ruby
