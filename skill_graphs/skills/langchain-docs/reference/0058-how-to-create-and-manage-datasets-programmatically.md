# How to create and manage datasets programmatically
Source: https://docs.langchain.com/langsmith/manage-datasets-programmatically

You can use the Python and TypeScript SDK to manage datasets programmatically. This includes creating, updating, and deleting datasets, as well as adding examples to them.

## Create a dataset

### Create a dataset from list of values

The most flexible way to make a dataset using the client is by creating examples from a list of inputs and optional outputs. Below is an example.

Note that you can add arbitrary metadata to each example, such as a note or a source. The metadata is stored as a dictionary.

<Check>
  If you have many examples to create, consider using the `create_examples`/`createExamples` method to create multiple examples in a single request. If creating a single example, you can use the `create_example`/`createExample` method.
</Check>

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langsmith import Client

  examples = [
    {
      "inputs": {"question": "What is the largest mammal?"},
      "outputs": {"answer": "The blue whale"},
      "metadata": {"source": "Wikipedia"},
    },
    {
      "inputs": {"question": "What do mammals and birds have in common?"},
      "outputs": {"answer": "They are both warm-blooded"},
      "metadata": {"source": "Wikipedia"},
    },
    {
      "inputs": {"question": "What are reptiles known for?"},
      "outputs": {"answer": "Having scales"},
      "metadata": {"source": "Wikipedia"},
    },
    {
      "inputs": {"question": "What's the main characteristic of amphibians?"},
      "outputs": {"answer": "They live both in water and on land"},
      "metadata": {"source": "Wikipedia"},
    },
  ]

  client = Client()
  dataset_name = "Elementary Animal Questions"

  # Storing inputs in a dataset lets us
  # run chains and LLMs over a shared set of examples.
  dataset = client.create_dataset(
    dataset_name=dataset_name, description="Questions and answers about animal phylogenetics.",
  )

  # Prepare inputs, outputs, and metadata for bulk creation
  client.create_examples(
    dataset_id=dataset.id,
    examples=examples
  )
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { Client } from "langsmith";

  const client = new Client();

  const exampleInputs: [string, string][] = [
    ["What is the largest mammal?", "The blue whale"],
    ["What do mammals and birds have in common?", "They are both warm-blooded"],
    ["What are reptiles known for?", "Having scales"],
    [
      "What's the main characteristic of amphibians?",
      "They live both in water and on land",
    ],
  ];

  const datasetName = "Elementary Animal Questions";

  // Storing inputs in a dataset lets us
  // run chains and LLMs over a shared set of examples.
  const dataset = await client.createDataset(datasetName, {
    description: "Questions and answers about animal phylogenetics",
  });

  // Prepare inputs, outputs, and metadata for bulk creation
  const inputs = exampleInputs.map(([inputPrompt]) => ({ question: inputPrompt }));
  const outputs = exampleInputs.map(([, outputAnswer]) => ({ answer: outputAnswer }));
  const metadata = exampleInputs.map(() => ({ source: "Wikipedia" }));

  // Use the bulk createExamples method
  await client.createExamples({
    inputs,
    outputs,
    metadata,
    datasetId: dataset.id,
  });
  ```

  ```java Java theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import com.langchain.smith.client.LangsmithClient;
  import com.langchain.smith.client.okhttp.LangsmithOkHttpClient;
  import com.langchain.smith.core.JsonValue;
  import com.langchain.smith.errors.UnexpectedStatusCodeException;
  import com.langchain.smith.models.datasets.Dataset;
  import com.langchain.smith.models.datasets.DatasetCreateParams;
  import com.langchain.smith.models.datasets.DatasetListParams;
  import com.langchain.smith.models.examples.bulk.BulkCreateParams;
  import java.util.List;
  import java.util.Map;
  import java.util.stream.Collectors;

  public class CreateDatasetExample {
      public static void main(String[] args) {
          LangsmithClient client = LangsmithOkHttpClient.fromEnv();

          List<String[]> exampleInputs = List.of(
              new String[]{"What is the largest mammal?", "The blue whale"},
              new String[]{"What do mammals and birds have in common?", "They are both warm-blooded"},
              new String[]{"What are reptiles known for?", "Having scales"},
              new String[]{"What's the main characteristic of amphibians?", "They live both in water and on land"}
          );

          String datasetName = "Elementary Animal Questions";

          Dataset dataset;
          try {
              dataset = client.datasets().create(
                  DatasetCreateParams.builder()
                      .name(datasetName)
                      .description("Questions and answers about animal phylogenetics")
                      .build()
              );
          } catch (UnexpectedStatusCodeException e) {
              // Dataset already exists, get it
              if (e.statusCode() == 409) {
                  DatasetListParams listParams = DatasetListParams.builder()
                      .name(datasetName)
                      .build();
                  dataset = client.datasets().list(listParams).items().get(0);
              } else {
                  throw e;
              }
          }

          // Prepare inputs, outputs, and metadata for bulk creation
          List<Map<String, String>> inputs = exampleInputs.stream()
              .map(pair -> {
                  return Maps.of("question", pair[0]);
              })
              .collect(Collectors.toList());

          List<Map<String, String>> outputs = exampleInputs.stream()
              .map(pair -> {
                  return Maps.of("answer", pair[1]);
              })
              .collect(Collectors.toList());

          List<Map<String, String>> metadata = exampleInputs.stream()
              .map(pair -> {
                  return Maps.of("source", "Wikipedia");
              })
              .collect(Collectors.toList());

          // Use the bulk createExamples method
          BulkCreateParams.Builder bulkParamsBuilder = BulkCreateParams.builder();
          for (int i = 0; i < inputs.size(); i++) {
              bulkParamsBuilder.addBody(
                  BulkCreateParams.Body.builder()
                      .datasetId(dataset.id())
                      .inputs(JsonValue.from(inputs.get(i)))
                      .outputs(JsonValue.from(outputs.get(i)))
                      .metadata(JsonValue.from(metadata.get(i)))
                      .build()
              );
          }

          client.examples().bulk().create(bulkParamsBuilder.build());
      }
  }

  ```
</CodeGroup>

### Create a dataset from traces

To create datasets from the runs (spans) of your traces, you can use the same approach. For **many** more examples of how to fetch and filter runs, see the [export traces](/langsmith/export-traces) guide. Below is an example:

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langsmith import Client

  client = Client()
  dataset_name = "Example Dataset"

  # Filter runs to add to the dataset
  runs = client.list_runs(
    project_name="my_project",
    is_root=True,
    error=False,
  )

  dataset = client.create_dataset(dataset_name, description="An example dataset")

  # Prepare inputs and outputs for bulk creation
  examples = [{"inputs": run.inputs, "outputs": run.outputs} for run in runs]

  # Use the bulk create_examples method
  client.create_examples(
    dataset_id=dataset.id,
    examples=examples
  )
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { Client, Run } from "langsmith";

  const client = new Client();
  const datasetName = "Example Dataset";

  // Filter runs to add to the dataset
  const runs: Run[] = [];
  for await (const run of client.listRuns({
    projectName: "my_project",
    isRoot: 1,
    error: false,
  })) {
    runs.push(run);
  }

  const dataset = await client.createDataset(datasetName, {
    description: "An example dataset",
    dataType: "kv",
  });

  // Prepare inputs and outputs for bulk creation
  const inputs = runs.map(run => run.inputs);
  const outputs = runs.map(run => run.outputs ?? {});

  // Use the bulk createExamples method
  await client.createExamples({
    inputs,
    outputs,
    datasetId: dataset.id,
  });
  ```

  ```java Java theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import com.langchain.smith.client.LangsmithClient;
  import com.langchain.smith.client.okhttp.LangsmithOkHttpClient;
  import com.langchain.smith.core.JsonValue;
  import com.langchain.smith.models.datasets.Dataset;
  import com.langchain.smith.models.datasets.DatasetCreateParams;
  import com.langchain.smith.models.examples.bulk.BulkCreateParams;
  import com.langchain.smith.models.runs.RunQueryParams;
  import com.langchain.smith.models.runs.RunQueryResponse;
  import java.util.ArrayList;
  import java.util.List;

  public class CreateDatasetExample {
      public static void main(String[] args) {
          LangsmithClient client = LangsmithOkHttpClient.fromEnv();
          String projectId = System.getenv("LANGSMITH_PROJECT_ID");
          String datasetName = "Example Dataset";

          List<RunQueryResponse.Run> allRuns = new ArrayList<>();
          String cursor = null;
          try {
              do {
                  RunQueryParams.Builder paramsBuilder = RunQueryParams.builder()
                      .addSession(projectId)
                      .isRoot(true)
                      .error(false)
                      .limit(10L);

                  if (cursor != null) {
                      paramsBuilder.cursor(cursor);
                  }

                  RunQueryResponse response = client.runs().query(paramsBuilder.build());
                  allRuns.addAll(response.runs());

                  // Get cursor for next page
                  try {
                      Map<String, JsonValue> cursorProps = response.cursors()._additionalProperties();
                      if (cursorProps != null && cursorProps.containsKey("next")) {
                          JsonValue nextValue = cursorProps.get("next");
                          if (nextValue != null && !nextValue.isNull() && !nextValue.isMissing()) {
                              cursor = nextValue.asString().orElse(null);
                          } else {
                              cursor = null;
                          }
                      } else {
                          cursor = null;
                      }
                  } catch (Exception e) {
                      cursor = null;
                  }
                  if (response.runs().size() < 50) {
                      cursor = null;
                  }
              } while (cursor != null && !cursor.isEmpty());
          } catch (Exception e) {
              System.err.println("Error querying runs: " + e.getMessage());
              e.printStackTrace();
              System.exit(1);
          }

          System.out.println("Total runs found: " + allRuns.size());

          // Create dataset
          Dataset dataset = client.datasets().create(
              DatasetCreateParams.builder()
                  .name(datasetName)
                  .description("An example dataset")
                  .build()
          );

          // Prepare inputs and outputs for bulk creation
          BulkCreateParams.Builder bulkParamsBuilder = BulkCreateParams.builder();
          int examplesWithData = 0;
          for (RunQueryResponse.Run run : allRuns) {
              if (run.inputs().isPresent() && run.outputs().isPresent()) {
                  // Get the additional properties maps which contain the actual data
                  Map<String, JsonValue> inputsMap = run.inputs().get()._additionalProperties();
                  Map<String, JsonValue> outputsMap = run.outputs().get()._additionalProperties();

                  bulkParamsBuilder.addBody(
                      BulkCreateParams.Body.builder()
                          .datasetId(dataset.id())
                          .inputs(JsonValue.from(inputsMap))
                          .outputs(JsonValue.from(outputsMap))
                          .build()
                  );
                  examplesWithData++;
              }
          }

          System.out.println("Prepared " + examplesWithData + " examples from " + allRuns.size() + " runs");

          if (examplesWithData == 0) {
              System.err.println("No runs have both inputs and outputs. Cannot create examples.");
              System.exit(1);
          }

          client.examples().bulk().create(bulkParamsBuilder.build());
          System.out.println("Created " + examplesWithData + " examples in dataset");
      }
  }
  ```
</CodeGroup>

### Create a dataset from a CSV file

In this section, we will demonstrate how you can create a dataset by uploading a CSV file.

First, ensure your CSV file is properly formatted with columns that represent your input and output keys. These keys will be utilized to map your data properly during the upload. You can specify an optional name and description for your dataset. Otherwise, the file name will be used as the dataset name and no description will be provided.

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langsmith import Client
  import os

  client = Client()
  csv_file = 'path/to/your/csvfile.csv'
  input_keys = ['column1', 'column2'] # replace with your input column names
  output_keys = ['output1', 'output2'] # replace with your output column names

  dataset = client.upload_csv(
    csv_file=csv_file,
    input_keys=input_keys,
    output_keys=output_keys,
    name="My CSV Dataset",
    description="Dataset created from a CSV file",
    data_type="kv"
  )
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { Client } from "langsmith";

  const client = new Client();
  const csvFile = 'path/to/your/csvfile.csv';
  const inputKeys = ['column1', 'column2']; // replace with your input column names
  const outputKeys = ['output1', 'output2']; // replace with your output column names

  const dataset = await client.uploadCsv({
    csvFile: csvFile,
    fileName: "My CSV Dataset",
    inputKeys: inputKeys,
    outputKeys: outputKeys,
    description: "Dataset created from a CSV file",
    dataType: "kv"
  });
  ```

  ```java Java theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import com.langchain.smith.client.LangsmithClient;
  import com.langchain.smith.client.okhttp.LangsmithOkHttpClient;
  import com.langchain.smith.models.datasets.Dataset;
  import com.langchain.smith.models.datasets.DatasetUploadParams;
  import com.langchain.smith.models.datasets.DataType;
  import java.nio.file.Path;
  import java.nio.file.Paths;
  import java.util.List;

  LangsmithClient client = LangsmithOkHttpClient.fromEnv();
  Path csvFile = Paths.get("path/to/your/csvfile.csv");
  List<String> inputKeys = List.of("column1", "column2");
  List<String> outputKeys = List.of("output1", "output2");

  Dataset dataset = client.datasets().upload(
      DatasetUploadParams.builder()
          .file(csvFile)
          .inputKeys(inputKeys)
          .outputKeys(outputKeys)
          .name("My CSV Dataset")
          .description("Dataset created from a CSV file")
          .dataType(DataType.KV)
          .build()
  );
  ```
</CodeGroup>

### Create a dataset from pandas DataFrame (Python only)

The python client offers an additional convenience method to upload a dataset from a pandas dataframe.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langsmith import Client
import os
import pandas as pd

client = Client()
df = pd.read_parquet('path/to/your/myfile.parquet')
input_keys = ['column1', 'column2'] # replace with your input column names
output_keys = ['output1', 'output2'] # replace with your output column names

dataset = client.upload_dataframe(
    df=df,
    input_keys=input_keys,
    output_keys=output_keys,
    name="My Parquet Dataset",
    description="Dataset created from a parquet file",
    data_type="kv" # The default
)
```

## Fetch datasets

You can programmatically fetch datasets from LangSmith using the `list_datasets`/`listDatasets` method in the Python and TypeScript SDKs. Below are some common calls.

<Info>
  Initialize the client before running the below code snippets.
</Info>

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langsmith import Client

  client = Client()
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { Client } from "langsmith";

  const client = new Client();
  ```

  ```java Java theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import com.langchain.smith.client.LangsmithClient;
  import com.langchain.smith.client.okhttp.LangsmithOkHttpClient;

  LangsmithClient client = LangsmithOkHttpClient.fromEnv();
  ```
</CodeGroup>

### Query all datasets

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  datasets = client.list_datasets()
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  const datasets = await client.listDatasets();
  ```

  ```java Java theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import com.langchain.smith.models.datasets.DatasetListParams;

  DatasetListParams listParams = DatasetListParams.builder().build();
  var datasets = client.datasets().list(listParams);
  ```
</CodeGroup>

### List datasets by name

If you want to search by the exact name, you can do the following:

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  datasets = client.list_datasets(dataset_name="My Test Dataset 1")
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  const datasets = await client.listDatasets({
    datasetName: "My Test Dataset 1"
  });
  ```

  ```java Java theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import com.langchain.smith.models.datasets.DatasetListParams;

  DatasetListParams listParams = DatasetListParams.builder()
      .name("My Test Dataset 1")
      .build();
  var datasets = client.datasets().list(listParams);
  ```
</CodeGroup>

If you want to do a case-invariant substring search, try the following:

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  datasets = client.list_datasets(dataset_name_contains="some substring")
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  const datasets = await client.listDatasets({
    datasetNameContains: "some substring"
  });
  ```

  ```java Java theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import com.langchain.smith.models.datasets.DatasetListParams;

  DatasetListParams listParams = DatasetListParams.builder()
      .nameContains("some substring")
      .build();
  var datasets = client.datasets().list(listParams);
  ```
</CodeGroup>

### List datasets by type

You can filter datasets by type:

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  datasets = client.list_datasets(data_type="kv")
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  const datasets = await client.listDatasets({
    dataType: "kv"
  });
  ```

  ```java Java theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import com.langchain.smith.models.datasets.DatasetListParams;

  DatasetListParams listParams = DatasetListParams.builder()
      .datatype(DataType.of("kv"))
      .build();
  var datasets = client.datasets().list(listParams);
  ```
</CodeGroup>

## Fetch examples

You can programmatically fetch examples from LangSmith using the `list_examples`/`listExamples` method in the Python and TypeScript SDKs. Below are some common calls.

<Info>
  Initialize the client before running the below code snippets.
</Info>

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langsmith import Client

  client = Client()
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { Client } from "langsmith";

  const client = new Client();
  ```

  ```java Java theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import com.langchain.smith.client.LangsmithClient;
  import com.langchain.smith.client.okhttp.LangsmithOkHttpClient;

  LangsmithClient client = LangsmithOkHttpClient.fromEnv();
  ```
</CodeGroup>

### List all examples for a dataset

You can filter by dataset ID:

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  examples = client.list_examples(dataset_id="c9ace0d8-a82c-4b6c-13d2-83401d68e9ab")
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  const examples = await client.listExamples({
    datasetId: "c9ace0d8-a82c-4b6c-13d2-83401d68e9ab"
  });
  ```

  ```java Java theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import com.langchain.smith.models.examples.ExampleListParams;

  ExampleListParams listParams = ExampleListParams.builder()
      .dataset("c9ace0d8-a82c-4b6c-13d2-83401d68e9ab")
      .build();
  var examples = client.examples().list(listParams);
  ```
</CodeGroup>

Or you can filter by dataset name (this must exactly match the dataset name you want to query)

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  examples = client.list_examples(dataset_name="My Test Dataset")
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  const examples = await client.listExamples({
    datasetName: "My test Dataset"
  });
  ```
</CodeGroup>

### List examples by id

You can also list multiple examples all by ID.

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  example_ids = [
    '734fc6a0-c187-4266-9721-90b7a025751a',
    'd6b4c1b9-6160-4d63-9b61-b034c585074f',
    '4d31df4e-f9c3-4a6e-8b6c-65701c2fed13',
  ]

  examples = client.list_examples(example_ids=example_ids)
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  const exampleIds = [
    "734fc6a0-c187-4266-9721-90b7a025751a",
    "d6b4c1b9-6160-4d63-9b61-b034c585074f",
    "4d31df4e-f9c3-4a6e-8b6c-65701c2fed13",
  ];

  const examples = await client.listExamples({
    exampleIds: exampleIds
  });
  ```

  ```java Java theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import com.langchain.smith.models.examples.ExampleListParams;
  import java.util.List;

  List<String> exampleIds = List.of(
      "734fc6a0-c187-4266-9721-90b7a025751a",
      "d6b4c1b9-6160-4d63-9b61-b034c585074f",
      "4d31df4e-f9c3-4a6e-8b6c-65701c2fed13"
  );

  ExampleListParams listParams = ExampleListParams.builder()
      .id(exampleIds)
      .build();
  var examples = client.examples().list(listParams);
  ```
</CodeGroup>

### List examples by metadata

You can also filter examples by metadata. Below is an example querying for examples with a specific metadata key-value pair. Under the hood, we check to see if the example's metadata contains the key-value pair(s) you specify.

For example, if you have an example with metadata `{"foo": "bar", "baz": "qux"}`, both `{foo: bar}` and `{baz: qux}` would match, as would `{foo: bar, baz: qux}`.

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  examples = client.list_examples(dataset_name=dataset_name, metadata={"foo": "bar"})
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  const examples = await client.listExamples({
    datasetName: datasetName,
    metadata: {foo: "bar"}
  });
  ```

  ```java Java theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import com.langchain.smith.models.examples.ExampleListParams;

  ExampleListParams listParams = ExampleListParams.builder()
      .datasetId(datasetId)
      .metadata("{\"foo\":\"bar\"}")
      .build();
  var examples = client.examples().list(listParams);
  ```
</CodeGroup>

### List examples by structured filter

Similar to how you can use the structured filter query language to [fetch runs](/langsmith/export-traces#use-filter-query-language), you can use it to fetch examples.

<Note>
  This is currently only available in v0.1.83 and later of the Python SDK and v0.1.35 and later of the TypeScript SDK.

  Additionally, the structured filter query language is only supported for `metadata` fields.
</Note>

You can use the `has` operator to fetch examples with metadata fields that contain specific key/value pairs and the `exists` operator to fetch examples with metadata fields that contain a specific key. Additionally, you can chain multiple filters together using the `and` operator and negate a filter using the `not` operator.

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  examples = client.list_examples(
    dataset_name=dataset_name,
    filter='and(not(has(metadata, \'{"foo": "bar"}\')), exists(metadata, "tenant_id"))'
  )
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  const examples = await client.listExamples({
    datasetName: datasetName,
    filter: 'and(not(has(metadata, \'{"foo": "bar"}\')), exists(metadata, "tenant_id"))'
  });
  ```

  ```java Java theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import com.langchain.smith.models.examples.ExampleListParams;

  String filter = "and(not(has(metadata, '{\"foo\": \"bar\"}')), exists(metadata, \"tenant_id\"))";

  ExampleListParams listParams = ExampleListParams.builder()
      .datasetId(datasetId)
      .filter(filter)
      .build();
  var examples = client.examples().list(listParams);
  ```
</CodeGroup>

## Update examples

### Update single example

You can programmatically update examples from LangSmith using the `update_example`/`updateExample` method in the Python and TypeScript SDKs. Below is an example.

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  client.update_example(
    example_id=example.id,
    inputs={"input": "updated input"},
    outputs={"output": "updated output"},
    metadata={"foo": "bar"},
    split="train"
  )
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  await client.updateExample(example.id, {
    inputs: { input: "updated input" },
    outputs: { output: "updated output" },
    metadata: { "foo": "bar" },
    split: "train",
  });
  ```

  ```java Java theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import com.langchain.smith.core.JsonValue;
  import com.langchain.smith.models.examples.ExampleUpdateParams;

   // Create Inputs using the builder
  ExampleUpdateParams.Inputs inputsObj = ExampleUpdateParams.Inputs.builder()
      .putAdditionalProperty("input", JsonValue.from("updated input"))
      .build();

  // Create Outputs using the builder
  ExampleUpdateParams.Outputs outputsObj = ExampleUpdateParams.Outputs.builder()
      .putAdditionalProperty("output", JsonValue.from("updated output"))
      .build();

  // Create Metadata using the builder
  ExampleUpdateParams.Metadata metadataObj = ExampleUpdateParams.Metadata.builder()
      .putAdditionalProperty("foo", JsonValue.from("bar"))
      .build();

  ExampleUpdateParams updateParams = ExampleUpdateParams.builder()
      .inputs(inputsObj)
      .outputs(outputsObj)
      .metadata(metadataObj)
      .split("train")
      .build();

  ExampleUpdateResponse updateResponse = client.examples().update(example.id(), updateParams);
  ```
</CodeGroup>

### Bulk update examples

You can also programmatically update multiple examples in a single request with the `update_examples`/`updateExamples` method in the Python and TypeScript SDKs. Below is an example.

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  client.update_examples(
    example_ids=[example.id, example_2.id],
    inputs=[{"input": "updated input 1"}, {"input": "updated input 2"}],
    outputs=[
        {"output": "updated output 1"},
        {"output": "updated output 2"},
    ],
    metadata=[{"foo": "baz"}, {"foo": "qux"}],
    splits=[["training", "foo"], "training"] # Splits can be arrays or standalone strings
  )
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  await client.updateExamples([
    {
      id: example.id,
      inputs: { input: "updated input 1" },
      outputs: { output: "updated output 1" },
      metadata: { foo: "baz" },
      split: ["training", "foo"] // Splits can be arrays or standalone strings
    },
    {
      id: example2.id,
      inputs: { input: "updated input 2" },
      outputs: { output: "updated output 2" },
      metadata: { foo: "qux" },
      split: "training"
    },
  ]);
  ```

  ```java Java theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  Map<String, String> inputs1 = Map.of("question", "What is the capital of France?")
  Map<String, String> outputs1 = Map.of("answer", "The capital of France is Paris.");
  Map<String, String> metadata1 = Map.of(
      "source", "Wikipedia",
      "difficulty", "easy"
  );

  Map<String, String> inputs2 = Map.of("question", "What is 2 + 2?");
  Map<String, String> outputs2 = Map.of("answer", "The answer is 4.");
  Map<String, String> metadata2 = Map.of(
      "source", "Math textbook",
      "difficulty", "easy");

  BulkPatchAllParams.Builder bulkParamsBuilder = BulkPatchAllParams.builder();

  bulkParamsBuilder.addBody(
      BulkPatchAllParams.Body.builder()
          .id(example1.id())
          .inputs(buildInputs(inputs1))
          .outputs(buildOutputs(outputs1))
          .metadata(buildMetadata(metadata1))
          .splitOfStrings(Arrays.asList("training", "validation"))
          .build()
  );

  bulkParamsBuilder.addBody(
      BulkPatchAllParams.Body.builder()
          .id(example2.id())
          .inputs(buildInputs(inputs2))
          .outputs(buildOutputs(outputs2))
          .metadata(buildMetadata(metadata2))
          .split("test")
          .build()
  );

  client.examples().bulk().patchAll(bulkParamsBuilder.build());
  ```
</CodeGroup>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/manage-datasets-programmatically.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Manage your organization using the API
Source: https://docs.langchain.com/langsmith/manage-organization-by-api

LangSmith's API supports programmatic access via API key to all of the actions available in the UI, with only a few exceptions that are noted in [User-only endpoints](#user-only-endpoints).

<Tip>
  Prefer infrastructure-as-code? Use the [LangSmith Terraform provider](/langsmith/manage-with-terraform) to manage workspaces, roles, members, evaluators, and alerts declaratively.
</Tip>

<Check>
  Before diving into this content, it might be helpful to read the following:

  * [Conceptual guide on organizations and workspaces](/langsmith/administration-overview)
  * [Organization setup how-to guild](/langsmith/set-up-hierarchy#set-up-an-organization)
</Check>

<Note>
  There are a few limitations that will be lifted soon:

  * The LangSmith SDKs do not support these organization management actions yet.
  * Organization-scoped [service keys](/langsmith/administration-overview#service-keys) with Organization Admin permission may be used for these actions.
</Note>

<Warning>
  Use the `X-Tenant-Id` header to specify which workspace to target. If the header is not present, operations will default to the workspace the key was initially created in if it is not organization-scoped.

  **If `X-Tenant-Id` is not specified when accessing workspace-scoped resources with an organization-scoped service key, the request will fail with `403 Forbidden`.**
</Warning>

Some commonly-used endpoints and use cases are listed below. For a complete list of available endpoints, see the [API docs](/langsmith/smith-api-ref). **The `X-Organization-Id` header should be present on all requests, and `X-Tenant-Id` header should be present on requests that are scoped to a particular workspace.**

## Workspaces

* [List workspaces](/langsmith/smith-api/workspaces/list-workspaces)
* [Create workspace](/langsmith/smith-api/workspaces/create-workspace)
* [Update workspace name](/langsmith/smith-api/workspaces/patch-workspace)

## User management

### RBAC

* [List roles](/langsmith/smith-api/orgs/list-organization-roles)
* [List permissions](/langsmith/smith-api/orgs/update-organization-roles)
* [Create role](/langsmith/smith-api/orgs/create-organization-roles)
* [Update role](/langsmith/smith-api/orgs/update-organization-roles)

### Membership management

`List roles` under [RBAC](#rbac) should be used for retrieving role IDs of these operations. `List [organization|workspace] members` endpoints (below) response `"id"`s should be used as `identity_id` in these operations.

Organization level:

* [List active organization members](/langsmith/smith-api/orgs/get-current-active-org-members)
* [List pending organization members](/langsmith/smith-api/orgs/get-current-pending-org-members)
* [Invite a user to the organization and one or more workspaces](/langsmith/smith-api/orgs/add-members-to-current-org-batch). This should be used when the user is not already a member in the organization.
* [Update a user's organization role](/langsmith/smith-api/workspaces/add-member-to-current-workspace)
* [Remove someone from the organization](/langsmith/smith-api/orgs/remove-member-from-current-org)

Workspace level:

* [List workspace members](/langsmith/smith-api/workspaces/get-current-workspace-members)
* [Add a member to a workspace that is already part of the organization](/langsmith/smith-api/workspaces/add-member-to-current-workspace)
* [Update a user's workspace role](/langsmith/smith-api/workspaces/add-member-to-current-workspace)
* [Remove someone from a workspace](/langsmith/smith-api/workspaces/delete-current-workspace-member)

<Note>
  These params should be omitted: `read_only` (deprecated), `password` and `full_name` ([basic auth](/langsmith/authentication-methods) only)
</Note>

## API keys

* [Create a service key](/langsmith/smith-api/api-key/generate-api-key)
* [Update a service key role](/langsmith/smith-api/orgs/update-org-service-key)
* [Delete a service key](/langsmith/smith-api/api-key/delete-api-key)

## Security settings

<Note>
  Organization Admin permissions are required to make these changes.
</Note>

<Note>
  "Shared resources" in this context refer to [public prompts](/langsmith/create-a-prompt#save-your-prompt), [shared runs](/langsmith/manage-trace#share-a-trace), and [shared datasets](/langsmith/manage-datasets#share-a-dataset).
</Note>

<Warning>
  Updating these settings affects **all resources in the organization**.
</Warning>

You can update these settings under the **Settings > Shared** tab for a workspace, or via API:

* [Update organization sharing settings](/langsmith/smith-api/orgs/update-current-organization-info)
  * use `unshare_all` to unshare **ALL** shared resources for the selected workspace - use `disable_public_sharing` to prevent future sharing of resources

These settings are only editable via API:

* [Disable/enable PAT creation](/langsmith/smith-api/orgs/update-current-organization-info) (for self-hosted, available in Helm chart version 0.11.25+)
  * Use `pat_creation_disabled` to disable PAT creation for the entire organization.
  * See the [admin guide](/langsmith/administration-overview#organization-roles) for information about the Organization Viewer role, which cannot create PATs.
  * For self-hosted deployments, you can also [globally disable PAT creation](/langsmith/self-host-user-management#disabling-personal-access-token-creation) across all organizations using an environment variable.

## User-only endpoints

These endpoints are user-scoped and require a logged-in user's JWT, so they should only be executed through the UI.

* `/api-key/current` endpoints: these are related a user's PATs
* `/sso/email-verification/send` (Cloud-only): this endpoint is related to [SAML SSO](/langsmith/user-management)

## Sample code

The sample code below goes through a few common workflows related to organization management. Make sure to make necessary replacements wherever `<replace_me>` is in the code.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import os
import requests

def main():
    api_key = os.environ["LANGSMITH_API_KEY"]
    # LANGSMITH_ORGANIZATION_ID is not a standard environment variable in the SDK, just used for this example
    organization_id = os.environ["LANGSMITH_ORGANIZATION_ID"]
    base_url = os.environ.get("LANGSMITH_ENDPOINT")  # or "https://api.smith.langchain.com". Update appropriately for self-hosted installations or regional SaaS
    headers = {
        "Content-Type": "application/json",
        "X-API-Key": api_key,
        "X-Organization-Id": organization_id,
    }
    session = requests.Session()
    session.headers.update(headers)
    workspaces_path = f"{base_url}/api/v1/workspaces"
    orgs_path = f"{base_url}/api/v1/orgs/current"
    api_keys_path = f"{base_url}/api/v1/api-key"

    # Create a workspace
    workspace_res = session.post(workspaces_path, json={"display_name": "My Workspace"})
    workspace_res.raise_for_status()
    workspace = workspace_res.json()
    workspace_id = workspace["id"]
    new_workspace_headers = {
        "X-Tenant-Id": workspace_id,
    }

    # Grab roles - this includes both organization and workspace roles
    roles_res = session.get(f"{orgs_path}/roles")
    roles_res.raise_for_status()
    roles = roles_res.json()
    # system org roles are 'Organization Admin', 'Organization User'
    # system workspace roles are 'Admin', 'Editor', 'Viewer'
    org_roles_by_name = {role["display_name"]: role for role in roles if role["access_scope"] == "organization"}
    ws_roles_by_name = {role["display_name"]: role for role in roles if role["access_scope"] == "workspace"}

    # Invite a user to the org and the new workspace, as an Editor.
    # workspace_role_id is only allowed if RBAC is enabled (an enterprise feature).
    new_user_email = "<replace_me>"
    new_user_res = session.post(
        f"{orgs_path}/members",
        json={
            "email": new_user_email,
            "role_id": org_roles_by_name["Organization User"]["id"],
            "workspace_ids": [workspace_id],
            "workspace_role_id": ws_roles_by_name["Editor"]["id"],
        },
    )
    new_user_res.raise_for_status()

    # Add a user that already exists in the org to the new workspace, as a Viewer.
    # workspace_role_id is only allowed if RBAC is enabled (an enterprise feature).
    existing_user_email = "<replace_me>"
    org_members_res = session.get(f"{orgs_path}/members")
    org_members_res.raise_for_status()
    org_members = org_members_res.json()
    existing_org_member = next(
        (member for member in org_members["members"] if member["email"] == existing_user_email), None
    )
    existing_user_res = session.post(
        f"{workspaces_path}/current/members",
        json={
            "user_id": existing_org_member["user_id"],
            "workspace_ids": [workspace_id],
            "workspace_role_id": ws_roles_by_name["Viewer"]["id"],
        },
        headers=new_workspace_headers,
    )
    existing_user_res.raise_for_status()

    # List all members of the workspace
    members_res = session.get(f"{workspaces_path}/current/members", headers=new_workspace_headers)
    members_res.raise_for_status()
    members = members_res.json()
    workspace_member = next(
        (member for member in members["members"] if member["email"] == existing_user_email), None
    )

    # Update the user's workspace role to Admin (enterprise-only)
    existing_user_id = workspace_member["id"]
    update_res = session.patch(
        f"{workspaces_path}/current/members/{existing_user_id}",
        json={"role_id": ws_roles_by_name["Admin"]["id"]},
        headers=new_workspace_headers,
    )
    update_res.raise_for_status()

    # Update the user's organization role to Organization Admin
    update_res = session.patch(
        f"{orgs_path}/members/{existing_org_member['id']}",
        json={"role_id": org_roles_by_name["Organization Admin"]["id"]},
    )
    update_res.raise_for_status()

    # Create a new Service key
    api_key_res = session.post(
        api_keys_path,
        json={"description": "my key"},
        headers=new_workspace_headers,
    )
    api_key_res.raise_for_status()
    api_key_json = api_key_res.json()
    api_key = api_key_json["key"]

if __name__ == "__main__":
    main()
```

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/manage-organization-by-api.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Manage prompts
Source: https://docs.langchain.com/langsmith/manage-prompts

Manage prompt versions, environments, and access controls in LangSmith.

LangSmith provides several tools to help you manage your [*prompts*](/langsmith/prompt-engineering-concepts) effectively. This page describes the following features:

* [Environments](#environments) for promoting commits through **Staging** and **Production**.
* [Commit tags](#commit-tags) for version control and environment management.
* [Prompt owners](#prompt-owners) for controlling who can promote commits and delete a prompt.
* [Webhook triggers](#trigger-a-webhook-on-prompt-commit) for automating workflows when prompts are updated.
* [Public prompt hub](#public-prompt-hub) for discovering and using community-created prompts.

## Prompt detail page

Select a prompt from the [**Prompts** table](/langsmith/create-a-prompt#view-your-prompts) to open its detail page, which uses a two-pane layout: commit history and environments appear on the left, and commit details appear on the right.

You can compare a commit with its previous version by toggling **Diff** in the top-right corner.

## Environments

Environments represent named deployment targets, **Staging** and **Production**, that you can assign to specific commits. They let you track which version of a prompt is active in each environment and promote commits between them.

Environments are defined by reserved [commit tags](#commit-tags) (`staging` and `production`) that are managed through the promotion UI rather than the freeform tag picker.

### Promote a commit

Promoting a commit assigns it to an environment. You can promote any commit to Staging or Production.

To promote a commit:

1. Hover over a commit in the left pane to reveal **Promote**, or click **Promote** in the upper-right corner of the page. Select **Staging** or **Production** from the dropdown.
2. A deployment modal opens, showing which commit is currently assigned to that environment and will be replaced.
3. Confirm the promotion. The environment pointer updates immediately.

<Note>
  Promoting a commit to Production does not remove it from Staging. If a commit is in Staging and you promote it to Production, it remains in Staging as well.
</Note>

### Roll back an environment

Each environment maintains an ordered history of which commits were assigned to it and when. To roll back to a previous commit:

1. In the left pane, find the environment you want to roll back.
2. Click the rollback icon for that environment.
3. From the displayed **Rollback history**, select the commit you want to roll back to. The environment pointer will update to that commit.

## Commit tags

[*Commit tags*](/langsmith/prompt-engineering-concepts#tags) are labels that reference a specific [*commit*](/langsmith/prompt-engineering-concepts#commits) in your prompt's version history. They help you mark significant versions and control which versions run in different environments. By referencing tags rather than commit IDs in your code, you can update which version is being used without modifying the code itself.

Each tag references exactly one commit, though you can reassign a tag to point to a different commit.

<Note>
  **Reserved tags:** The `staging` and `production` tags are reserved for environment management and are not enabled in the freeform tag picker. Use the [promotion flow](#promote-a-commit) to assign commits to these environments.
</Note>

<Note>
  **Not to be confused with resource tags**: Commit tags are specific to prompt versioning and reference individual commits in a prompt's history. [Resource tags](/langsmith/set-up-resource-tags) are key-value pairs used to organize workspace resources like projects, datasets, and prompts. While both can use similar naming conventions (like `prod` or `staging`), commit tags control **which version** of a prompt runs, while resource tags help you **organize and filter** resources across your workspace.
</Note>

### Create a tag

To create a tag, select the commit you want to tag in the left pane of the prompt detail page. Click **Tag** at the top right of the right pane. In the dropdown, click **Commit Tag** and enter a name.

### Move a tag

To point a tag to a different commit, select the destination commit in the left pane of the prompt detail page. Click **Tag** at the top right of the right pane. In the dropdown, select the tag you want to move. This automatically updates the tag to point to the new commit.

### Delete a tag

To delete a tag, click **Tag** at the top right of the right pane. (It does not matter which commit is selected). In the dropdown, click the delete icon next to the tag you want to delete. This removes the tag entirely and it will no longer be associated with any commit.

### Use tags in code

Tags provide a stable way to reference specific versions of your prompts in code. Instead of using commit hashes directly, you can reference tags that can be updated without changing your code.

Here is an example of pulling a prompt by tag in Python:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
prompt = client.pull_prompt("joke-generator:production")
