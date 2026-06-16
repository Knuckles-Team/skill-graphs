# You can tag a specific dataset version with a semantic name, like "prod"
client.update_dataset_tag(
    dataset_name=toxic_dataset_name, as_of=initial_time, tag="prod"
)
```

To run an evaluation on a particular tagged version of a dataset, refer to the [Evaluate on a specific dataset version section](#evaluate-on-a-specific-dataset-version).

## Evaluate on a specific dataset version

<Check>
  You may find it helpful to refer to the following content before you read this section:

  * [Version a dataset](#version-a-dataset).
  * [Fetching examples](/langsmith/manage-datasets-programmatically#fetch-examples).
</Check>

### Use `list_examples`

You can use `evaluate` / `aevaluate` to pass in an iterable of examples to evaluate on a particular version of a dataset. Use `list_examples` / `listExamples` to fetch examples from a particular version tag using `as_of` / `asOf` and pass that into the `data` argument.

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langsmith import Client

  ls_client = Client()

  # Assumes actual outputs have a 'class' key.
  # Assumes example outputs have a 'label' key.
  def correct(outputs: dict, reference_outputs: dict) -> bool:
    return outputs["class"] == reference_outputs["label"]

  results = ls_client.evaluate(
      lambda inputs: {"class": "Not toxic"},
      # Pass in filtered data here:
      data=ls_client.list_examples(
        dataset_name="Toxic Queries",
        as_of="latest",  # specify version here
      ),
      evaluators=[correct],
  )
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { evaluate } from "langsmith/evaluation";

  await evaluate((inputs) => labelText(inputs["input"]), {
    data: langsmith.listExamples({
      datasetName: datasetName,
      asOf: "latest",
    }),
    evaluators: [correctLabel],
  });
  ```

  ```java Java theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import com.langchain.smith.models.examples.ExampleListParams;

  ExampleListParams listParams = ExampleListParams.builder()
      .datasetId(datasetId)
      .asOf("latest")
  var examples = client.examples().list(listParams);
  ```
</CodeGroup>

Learn more about how to fetch views of a dataset on the [Create and manage datasets programmatically](/langsmith/manage-datasets-programmatically#fetch-datasets) page.

## Evaluate on a split / filtered view of a dataset

<Check>
  You may find it helpful to refer to the following content before you read this section:

  * [Fetching examples](/langsmith/manage-datasets-programmatically#fetch-examples).
  * [Creating and managing dataset splits](/langsmith/manage-datasets-in-application#create-and-manage-dataset-splits).
</Check>

### Evaluate on a filtered view of a dataset

You can use the `list_examples` / `listExamples` method to [fetch](/langsmith/manage-datasets-programmatically#fetch-examples) a subset of examples from a dataset to evaluate on.

One common workflow is to fetch examples that have a certain metadata key-value pair.

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langsmith import evaluate

  results = evaluate(
      lambda inputs: label_text(inputs["text"]),
      data=client.list_examples(dataset_name=dataset_name, metadata={"desired_key": "desired_value"}),
      evaluators=[correct_label],
      experiment_prefix="Toxic Queries",
  )
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { evaluate } from "langsmith/evaluation";

  await evaluate((inputs) => labelText(inputs["input"]), {
    data: langsmith.listExamples({
      datasetName: datasetName,
      metadata: {"desired_key": "desired_value"},
    }),
    evaluators: [correctLabel],
    experimentPrefix: "Toxic Queries",
  });
  ```

  ```java Java theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import com.langchain.smith.models.examples.ExampleListParams;

  ExampleListParams listParams = ExampleListParams.builder()
      .datasetId(datasetId)
      .metadata("{\"desired_key\":\"desired_value\"}")
      .build();
  var examples = client.examples().list(listParams);
  ```
</CodeGroup>

For more filtering capabilities, refer to this [how-to guide](/langsmith/manage-datasets-programmatically#list-examples-by-structured-filter).

### Evaluate on a dataset split

You can use the `list_examples` / `listExamples` method to evaluate on one or multiple [splits](/langsmith/evaluation-concepts#dataset-organization) of your dataset. The `splits` parameter takes a list of the splits you would like to evaluate.

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langsmith import evaluate

  results = evaluate(
      lambda inputs: label_text(inputs["text"]),
      data=client.list_examples(dataset_name=dataset_name, splits=["test", "training"]),
      evaluators=[correct_label],
      experiment_prefix="Toxic Queries",
  )
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { evaluate } from "langsmith/evaluation";

  await evaluate((inputs) => labelText(inputs["input"]), {
    data: langsmith.listExamples({
      datasetName: datasetName,
      splits: ["test", "training"],
    }),
    evaluators: [correctLabel],
    experimentPrefix: "Toxic Queries",
  });
  ```

  ```java Java theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import com.langchain.smith.models.examples.ExampleListParams;
  import java.util.Arrays;
  import java.util.List;

  List<String> splits = Arrays.asList("test", "training");

  ExampleListParams listParams = ExampleListParams.builder()
      .datasetId(datasetId)
      .splits(splits)
      .build();
  var examples = client.examples().list(listParams);
  ```
</CodeGroup>

For more details on fetching views of a dataset, refer to the guide on [fetching datasets](/langsmith/manage-datasets-programmatically#fetch-datasets).

## Share a dataset

### Share a dataset publicly

<Warning>
  Sharing a dataset publicly will make the **dataset examples, experiments and associated runs, and feedback on this dataset accessible to anyone with the link**, even if they don't have a LangSmith account. Make sure you're not sharing sensitive information.

  This feature is only available in the cloud-hosted version of LangSmith.
</Warning>

From the **Dataset & Experiments** tab, select a dataset, click **⋮** (top right of the page), click **Share Dataset**. This will open a dialog where you can copy the link to the dataset.

<img alt="Share Dataset" />

### Unshare a dataset

1. Click on **Unshare** by clicking on **Public** in the upper right hand corner of any publicly shared dataset, then **Unshare** in the dialog. <img alt="Unshare Dataset" />

2. Navigate to your organization's list of publicly shared datasets, by clicking on **Settings** -> **Shared URLs** or [this link](https://smith.langchain.com/settings/shared), then click on **Unshare** next to the dataset you want to unshare.

<img alt="Unshare Trace List" />

## Export a dataset

You can export your LangSmith dataset to a CSV, JSONL, or [OpenAI's fine tuning format](https://platform.openai.com/docs/guides/fine-tuning#example-format) from the LangSmith UI.

From the **Dataset & Experiments** tab, select a dataset, click **⋮** (top right of the page), click **Download Dataset**.

<img alt="Export Dataset Button" />

## Export filtered traces from experiment to dataset

After running an [offline evaluation](/langsmith/evaluation-concepts#offline-evaluations) in LangSmith, you may want to export [traces](/langsmith/observability-concepts#traces) that met some evaluation criteria to a dataset.

### View experiment traces

<img alt="Export filtered traces" />

To do so, first click on the arrow next to your experiment name. This will direct you to a project that contains the traces generated from your experiment.

<img alt="Export filtered traces" />

From there, you can filter the traces based on your evaluation criteria. In this example, we're filtering for all traces that received an accuracy score greater than 0.5.

<img alt="Export filtered traces" />

After applying the filter on the project, we can multi-select runs to add to the dataset, and click **Add to Dataset**.

<img alt="Export filtered traces" />

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/manage-datasets.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Create and manage datasets in the UI
Source: https://docs.langchain.com/langsmith/manage-datasets-in-application

[*Datasets*](/langsmith/evaluation-concepts#datasets) enable you to perform repeatable evaluations over time using consistent data. Datasets are made up of [*examples*](/langsmith/evaluation-concepts#examples), which store inputs, outputs, and optionally, reference outputs.

This page outlines the various methods for [creating](#create-a-dataset-and-add-examples) and [managing](#manage-a-dataset) datasets in the [UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-manage-datasets-in-application).

## Create a dataset and add examples

The following sections explain the different ways you can create a dataset in LangSmith and add examples to it. Depending on your workflow, you can manually curate examples, automatically capture them from tracing, import files, or even generate synthetic data:

* [Manually from a tracing project](#manually-from-a-tracing-project)
* [Automatically from a tracing project](#automatically-from-a-tracing-project)
* [From examples in an annotation queue](#from-examples-in-an-annotation-queue)
* [From the Playground](#from-the-playground)
* [Import a dataset from a CSV or JSONL file](#import-a-dataset-from-a-csv-or-jsonl-file)
* [Create a new dataset from the dataset page](#create-a-new-dataset-from-the-datasets-%26-experiments-page)
* [Add synthetic examples created by an LLM via the Datasets UI](#add-synthetic-examples-created-by-an-llm)

### Manually from a tracing project

A common pattern for constructing datasets is to convert notable traces from your application into dataset examples. This approach requires that you have [configured tracing to LangSmith](/langsmith/observability-concepts).

<Check>
  A technique to build datasets is to filter the most interesting traces, such as traces that were tagged with poor user feedback, and add them to a dataset. For tips on how to filter traces, refer to the [Filter traces](/langsmith/filter-traces-in-application) guide.
</Check>

There are two ways to add data manually from a tracing project to datasets. Navigate to **Tracing Projects** and select a project.

1. Multi-select runs from the runs table. On the **Runs** tab, multi-select runs. At the bottom of the page, click <Icon icon="database" /> **Add to Dataset**.
2. On the **Runs** tab, select a run from the table. On the individual run details page, select  **Add to** -> **Dataset** in the top right corner.

   When you select a dataset from the run details page, a modal will pop up letting you know if any [transformations](/langsmith/dataset-transformations) were applied or if schema validation failed.

   You can then optionally edit the run before adding it to the dataset.

### Automatically from a tracing project

You can use [run rules](/langsmith/rules) to add traces automatically to a dataset based on certain conditions. For example, you could add all traces that are [tagged](/langsmith/observability-concepts#tags) with a specific use case or have a [low feedback score](/langsmith/observability-concepts#feedback).

### From examples in an annotation queue

<Check>
  If you rely on subject matter experts to build meaningful datasets, use [annotation queues](/langsmith/annotation-queues) to provide a streamlined view for reviewers. Human reviewers can optionally modify the inputs/outputs/reference outputs from a trace before it is added to the dataset.
</Check>

You can optionally configure annotation queues with a default dataset, though you can add runs to any dataset by using the dataset switcher on the bottom of the screen. Once you select the right dataset, click **Add to Dataset** or hit the hot key `D` to add the run to it.

Any modifications you make to the run in your annotation queue will carry over to the dataset, and all metadata associated with the run will also be copied.

<Tip>
  You can also set up rules to add runs that meet specific criteria to an annotation queue using [automation rules](/langsmith/rules).
</Tip>

### From the Playground

On the [**Playground**](/langsmith/prompt-engineering-concepts#playground) page:

1. Select **Set up Evaluation**.

2. Click **+New** if you're starting a new dataset or select from an existing dataset.

   <Note>
     Creating datasets inline in the Playground is not supported for datasets that have nested keys. In order to add/edit examples with nested keys, you must edit [from the datasets page](/langsmith/manage-datasets-in-application#create-a-new-dataset-from-the-datasets-%26-experiments-page).
   </Note>

3. Edit the examples:

   * Use **+Row** to add a new example to the dataset.
   * Delete an example using the **⋮** dropdown on the right-hand side of the table.
   * If you're creating a reference-free dataset, remove the **Reference Output** column using the **x** button in the column. Note that this action is not reversible.

### Import a dataset from a CSV or JSONL file

On the **Datasets & Experiments** page, click **+New Dataset**, then **Import** an existing dataset from CSV or JSONL file.

### Create a new dataset from the datasets & experiments page

1. Navigate to the **Datasets & Experiments** page from the left-hand menu.
2. Click **+ New Dataset**.
3. On the **New Dataset** page, select the **Create from scratch** tab.
4. Add a name and description for the dataset.
5. (Optional) Create a [dataset schema](#create-a-dataset-schema) to validate your dataset.
6. Click **Create**, which will create an empty dataset.
7. To add examples inline, on the dataset's page, go to the **Examples** tab. Click **+ Example**.
8. Define examples in JSON and click **Submit**. For more details on dataset splits, refer to [Create and manage dataset splits](#create-and-manage-dataset-splits).

### Add synthetic examples created by an LLM

If you have existing examples and a [schema](#create-a-dataset-schema) defined on your dataset, when you click **+ Example** there is an option to <Icon icon="sparkles" /> **Add AI-Generated Examples**. This will use an LLM to create [synthetic](/langsmith/evaluation-concepts#building-datasets) examples.

In **Generate examples**, do the following:

1. Click **API Key** in the top right of the pane to set your OpenAI API key as a [workspace secret](/langsmith/administration-overview#workspaces). If your workspace already has an OpenAI API key set, you can skip this step.

2. Select <Tooltip>few-shot examples</Tooltip>: Toggle **Automatic** or **Manual** reference examples. You can select these examples manually from your dataset or use the automatic selection option.

3. Enter the number of synthetic examples you want to generate.

4. Click **Generate**.

   <img alt="The AI-Generated Examples configuration window. Selections for manual and automatic and number of examples to generate." />

   <img alt="The AI-Generated Examples configuration window. Selections for manual and automatic and number of examples to generate." />

5. The examples will appear on the **Select generated examples** page. Choose which examples to add to your dataset, with the option to edit them before finalizing. Click **Save Examples**.

6. Each example will be validated against your specified dataset schema and tagged as **synthetic** in the source metadata.

   <img alt="Select generated examples page with generated examples selected and Save examples button." />

   <img alt="Select generated examples page with generated examples selected and Save examples button." />

## Manage a dataset

### Create a dataset schema

LangSmith datasets store arbitrary JSON objects. We recommend (but do not require) that you define a schema for your dataset to ensure that they conform to a specific JSON schema. Dataset schemas are defined with standard [JSON schema](https://json-schema.org/), with the addition of a few [prebuilt types](/langsmith/dataset-json-types) that make it easier to type common primitives like messages and tools.

Certain fields in your schema have a `+ Transformations` option. Transformations are preprocessing steps that, if enabled, update your examples when you add them to the dataset. For example, the `convert to OpenAI messages` transformation will convert message-like objects, like LangChain messages, to OpenAI message format.

For the full list of available transformations, refer to the [Dataset transformations reference](/langsmith/dataset-transformations).

<Note>
  If you plan to collect production traces in your dataset from LangChain [ChatModels](/oss/python/langchain/models) or from OpenAI calls using the [LangSmith OpenAI wrapper](/langsmith/annotate-code), we offer a prebuilt Chat Model schema that converts messages and tools into industry standard openai formats that can be used downstream with any model for testing. You can also customize the template settings to match your use case.

  Please see the [dataset transformations reference](/langsmith/dataset-transformations) for more information.
</Note>

### Create and manage dataset splits

For an overview of when and why to use splits, refer to [Dataset organization](/langsmith/evaluation-concepts#dataset-organization).

To create and manage splits in the UI:

1. Select examples in your dataset.
2. Click **Add to Split**.
3. From the resulting popup menu, you can select and unselect splits for the selected examples, or create a new split.

<img alt="Add to Split" />

### Edit example metadata

To add metadata to your examples:

1. Click on an example and then click **Edit** on the top right-hand side of the popover.
2. From this page, update or delete existing metadata, or add new metadata.

You may use this to store information about your examples, such as tags or version info, which you can then [group by](/langsmith/analyze-an-experiment#group-results-by-metadata) when analyzing experiment results or [filter by](/langsmith/manage-datasets-programmatically#list-examples-by-metadata) when you call `list_examples` in the SDK.

### Filter examples

You can filter examples by split, metadata key/value or perform full-text search over examples. These filtering options are available to the top left of the examples table:

* **Filter by split**: Select split > Select a split to filter by.
* **Filter by metadata**: Filters > Select **Metadata** from the dropdown > Select the metadata key and value to filter on.
* **Full-text search**: Filters > Select **Full Text** from the dropdown > Enter your search criteria.

You may add multiple filters, and only examples that satisfy all of the filters will be displayed in the table.

<img alt="Filters Applied to Examples" />

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/manage-datasets-in-application.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
