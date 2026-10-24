# Task Queue Names

The Temporal Service maintains a set of Task Queues, which Workers poll to see
what work needs to be done. Each Task Queue is identified by a name, which is
provided to the Temporal Service when launching a Workflow Execution.

<Tabs groupId="start-workflow-configure-worker-by-sdk" queryString>

<TabItem value="python" label="Python">

**Excerpt of code used to start the Workflow in Python**

```python
client = await Client.connect("localhost:7233", namespace="default")
