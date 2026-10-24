...
    // In main
    WorkflowOptions options = WorkflowOptions.newBuilder()
        .setWorkflowId(workflowID)
        .setTaskQueue(Constants.TASK_QUEUE_NAME)
        .setTypedSearchAttributes(generateSearchAttributes())
        .build();

    PizzaWorkflow workflow = client.newWorkflowStub(PizzaWorkflow.class, options);
...

    // Further down in the file
    private static Map<String, Object> generateSearchAttributes(){
        return SearchAttributes.newBuilder().set(Constants.IS_ORDER_FAILED, false).build();
    }
```

Each `SearchAttribute` object represents a custom attribute name, and the value is a [`SearchAttributeKey`](https://www.javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/common/SearchAttributeKey.html#forBoolean(java.lang.String)) representing a specific type. Currently the following types are supported:

- Boolean
- Double
- Long
- KeyWord
- KeyWordList
- Text

In this example `isOrderFailed` is set as a Search Attribute. This attribute is
useful for querying Workflows based on the success/failure of customer orders.

### How to upsert Search Attributes {/* #upsert-search-attributes */}

Within the Workflow code, you can dynamically add or update Search Attributes using [`upsertTypedSearchAttributes`](https://www.javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/workflow/Workflow.html#upsertTypedSearchAttributes(io.temporal.common.SearchAttributeUpdate...)).
This method is particularly useful for Workflows whose attributes need to change based on internal logic or external events.

```java

  ...

  // Existing Workflow Logic

  Map<String, Object> searchAttribute = new HashMap<>();

  Distance distance;
  try {
    distance = activities.getDistance(address);
    searchAttribute.put("isOrderFailed", false);
    Workflow.upsertTypedSearchAttributes(Constants.IS_ORDER_FAILED.valueSet(false));
  } catch (NullPointerException e) {
    searchAttribute.put("isOrderFailed", true);
    Workflow.upsertTypedSearchAttributes(Constants.IS_ORDER_FAILED.valueSet(true));
    throw new NullPointerException("Unable to get distance");
  }
```

### How to remove a Search Attribute from a Workflow {/* #remove-search-attribute */}

To remove a Search Attribute that was previously set, set it to an empty Map.

```java
    // In a shared constants file, so all files have access

    public static final SearchAttributeKey<Boolean> IS_ORDER_FAILED = SearchAttributeKey.forBoolean("isOrderFailed");

    ...

    Workflow.upsertTypedSearchAttributes(Constants.IS_ORDER_FAILED.valueUnset());
```

---

## Set up your local with the Java SDK
