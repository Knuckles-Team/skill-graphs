# Run an evaluation with multimodal content
Source: https://docs.langchain.com/langsmith/evaluate-with-attachments

Learn how to create dataset examples with file attachments and use them in prompts and evaluators when running LangSmith evaluations with multimodal content.

LangSmith lets you create dataset examples with file attachments, like images, audio files, or documents, and use them in your prompts and evaluators when running evaluations with multimodal content.

While you can include multimodal data in your examples by base64 encoding it, this approach is inefficient—the encoded data takes up more space than the original binary files, resulting in slower transfers to and from LangSmith. Using attachments instead provides two key benefits:

* Faster upload and download speeds due to more efficient binary file transfers.
* Enhanced visualization of different file types in the LangSmith UI.

This guide covers how to create examples with attachments, build multimodal prompts and evaluators that use those attachments, and run evaluations with multimodal content. Select either the [**UI**](#ui) or [**SDK**](#sdk) tab to get started.

**Choose your preferred method:**

<Tabs>
  <Tab title="UI" icon="click">
    ## 1. Create examples with attachments

    You can add examples with attachments to a dataset in a few different ways.

    #### From existing runs

    When adding runs to a LangSmith dataset, attachments can be selectively propagated from the source run to the destination example. To learn more, please see [Manage datasets in application](/langsmith/manage-datasets-in-application#manually-from-a-tracing-project).

    <img alt="Add trace with attachments to dataset" />

    #### From scratch

    You can create examples with attachments directly from the LangSmith UI. Click the `+ Example` button in the `Examples` tab of the dataset UI. Then upload attachments using the "Upload Files" button:

    <img alt="Create example with attachments" />

    Once uploaded, you can view examples with attachments in the LangSmith UI. Each attachment will be rendered with a preview for easy inspection. <img alt="Attachments with examples" />

    ## 2. Create a multimodal prompt

    The LangSmith UI allows you to include attachments in your prompts when evaluating multimodal models:

    First, click the file icon in the message where you want to add multimodal content. Next, add a template variable for the attachment(s) you want to include for each example.

    * If you want to include a specific attachment, you can use the suggested variable name, such as `{{attachment.file_name}}`, this will map the file with `file_name` in the attachment list to pass it to the evaluator
    * If you want to include all attachments, use the `{{attachments}}` variable.

      <img alt="Adding multimodal variable" />

    ## 3. Define custom evaluators

    You can create evaluators that use multimodal content from your dataset examples.

    <Note>
      Evaluators must use a model that supports both the input modality and structured output. For audio attachments, this is currently only Gemini. Image and PDF attachments work with any vision-capable model that returns structured output.
    </Note>

    Since your dataset already has examples with attachments (added in step 1), you can reference them directly in your evaluator. To do so:

    1. Select **+ Evaluator** from the dataset page.
    2. In the **Template variables** editor, add a variable for the attachment(s) to include:

       * If you want to include a specific attachment, you can use the suggested variable name, such as `{{attachment.file_name}}`, this will map the file with `file_name` in the attachment list to pass it to the evaluator.
       * If you want to include all attachments, use the `{{attachments}}` variable.

       <img alt="Create evaluator modal with an audio attachment selected for output variable." />

       <img alt="Create evaluator modal with an audio attachment selected for output variable." />

    The evaluator can then use these attachments along with the model's outputs to judge quality. For example, you could create an evaluator that:

    * Checks if an image description matches the actual image content.
    * Verifies if a transcription accurately reflects the audio.
    * Validates if extracted text from a PDF is correct.

    You can also create text-only evaluators that don't use attachments but evaluate the model's text output:

    * OCR → text correction: Use a vision model to extract text from a document, then evaluate the accuracy of the extracted output.
    * Speech-to-text → transcription quality: Use a voice model to transcribe audio to text, then evaluate the transcription against your reference.

    <Tip>
      If your traces contain base64-encoded multimodal content in their inputs or outputs (for example, if you followed the [log multimodal traces](/langsmith/log-multimodal-traces) guide), you don't need attachments to evaluate them. Use standard variable mapping—such as `{{input}}` or `{{output}}`—in your evaluator prompt, and the base64 content will be passed correctly to the LLM evaluator for visualization and evaluation.
    </Tip>

    For more information on defining custom evaluators, see the [LLM as Judge](/langsmith/llm-as-judge) guide.

    ## 4. Update examples with attachments

    <Note>
      Attachments are limited to 20MB in size in the UI.
    </Note>

    When editing an example in the UI, you can:

    * Upload new attachments
    * Rename and delete attachments
    * Reset attachments to their previous state using the quick reset button

    Changes are not saved until you click submit.

    <img alt="Attachment editing" />
  </Tab>

  <Tab title="SDK" icon="code">
    ## 1. Create examples with attachments

    To upload examples with attachments using the SDK, use the [create\_examples](https://docs.smith.langchain.com/reference/python/client/langsmith.client.Client#langsmith.client.Client.create_examples) / [update\_examples](https://docs.smith.langchain.com/reference/python/client/langsmith.client.Client#langsmith.client.Client.update_examples) Python methods or the [uploadExamplesMultipart](https://docs.smith.langchain.com/reference/js/classes/client.Client#uploadexamplesmultipart) / [updateExamplesMultipart](https://docs.smith.langchain.com/reference/js/classes/client.Client#updateexamplesmultipart) TypeScript methods.

    #### Python

    Requires `langsmith>=0.3.13`

    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    import requests
    import uuid
    from pathlib import Path
    from langsmith import Client

    # Publicly available test files
    pdf_url = "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf"
    wav_url = "https://openaiassets.blob.core.windows.net/$web/API/docs/audio/alloy.wav"
    img_url = "https://www.w3.org/Graphics/PNG/nurbcup2si.png"

    # Fetch the files as bytes
    pdf_bytes = requests.get(pdf_url).content
    wav_bytes = requests.get(wav_url).content
    img_bytes = requests.get(img_url).content

    # Create the dataset
    ls_client = Client()
    dataset_name = "attachment-test-dataset"
    dataset = ls_client.create_dataset(
      dataset_name=dataset_name,
      description="Test dataset for evals with publicly available attachments",
    )

    inputs = {
      "audio_question": "What is in this audio clip?",
      "image_question": "What is in this image?",
    }

    outputs = {
      "audio_answer": "The sun rises in the east and sets in the west. This simple fact has been observed by humans for thousands of years.",
      "image_answer": "A mug with a blanket over it.",
    }

    # Define an example with attachments
    example_id = uuid.uuid4()
    example = {
      "id": example_id,
      "inputs": inputs,
      "outputs": outputs,
      "attachments": {
          "my_pdf": {"mime_type": "application/pdf", "data": pdf_bytes},
          "my_wav": {"mime_type": "audio/wav", "data": wav_bytes},
          "my_img": {"mime_type": "image/png", "data": img_bytes},
          # Example of an attachment specified via a local file path:
          # "my_local_img": {"mime_type": "image/png", "data": Path(__file__).parent / "my_local_img.png"},
      },
    }

    # Create the example
    ls_client.create_examples(
      dataset_id=dataset.id,
      examples=[example],
      # Uncomment this flag if you'd like to upload attachments from local files:
      # dangerously_allow_filesystem=True
    )
    ```

    #### TypeScript

    Requires version >= 0.2.13

    You can use the `uploadExamplesMultipart` method to upload examples with attachments.

    Note that this is a different method from the standard `createExamples` method, which currently does not support attachments. Each attachment requires either a `Uint8Array` or an `ArrayBuffer` as the data type.

    * `Uint8Array`: Useful for handling binary data directly.
    * `ArrayBuffer`: Represents fixed-length binary data, which can be converted to `Uint8Array` as needed.

    Note that you cannot directly pass in a file path in the TypeScript SDK, as accessing local files is not supported in all runtime environments.

    ```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    import { Client } from "langsmith";
    import { v4 as uuid4 } from "uuid";

    // Publicly available test files
    const pdfUrl = "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf";
    const wavUrl = "https://openaiassets.blob.core.windows.net/$web/API/docs/audio/alloy.wav";
    const pngUrl = "https://www.w3.org/Graphics/PNG/nurbcup2si.png";

    // Helper function to fetch file as ArrayBuffer
    async function fetchArrayBuffer(url: string): Promise<ArrayBuffer> {
      const response = await fetch(url);
      if (!response.ok) {
        throw new Error(`Failed to fetch ${url}: ${response.statusText}`);
      }
      return response.arrayBuffer();
    }

    // Fetch files as ArrayBuffer
    const pdfArrayBuffer = await fetchArrayBuffer(pdfUrl);
    const wavArrayBuffer = await fetchArrayBuffer(wavUrl);
    const pngArrayBuffer = await fetchArrayBuffer(pngUrl);

    // Create the LangSmith client (Ensure LANGSMITH_API_KEY is set in env)
    const langsmithClient = new Client();

    // Create a unique dataset name
    const datasetName = "attachment-test-dataset:" + uuid4().substring(0, 8);

    // Create the dataset
    const dataset = await langsmithClient.createDataset(datasetName, {
      description: "Test dataset for evals with publicly available attachments",
    });

    // Define the example with attachments
    const exampleId = uuid4();
    const example = {
      id: exampleId,
      inputs: {
          audio_question: "What is in this audio clip?",
          image_question: "What is in this image?",
      },
      outputs: {
          audio_answer: "The sun rises in the east and sets in the west. This simple fact has been observed by humans for thousands of years.",
          image_answer: "A mug with a blanket over it.",
      },
      attachments: {
        my_pdf: {
          mimeType: "application/pdf",
          data: pdfArrayBuffer
        },
        my_wav: {
          mimeType: "audio/wav",
          data: wavArrayBuffer
        },
        my_img: {
          mimeType: "image/png",
          data: pngArrayBuffer
        },
      },
    };

    // Upload the example with attachments to the dataset
    await langsmithClient.uploadExamplesMultipart(dataset.id, [example]);
    ```

    <Info>
      Along with being passed in as bytes, attachments can be specified as paths to local files. To do so pass in a path for the attachment `data` value and specify arg `dangerously_allow_filesystem=True`:

      ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      client.create_examples(..., dangerously_allow_filesystem=True)
      ```
    </Info>

    ## 2. Run evaluations

    ### Define a target function

    Now that we have a dataset that includes examples with attachments, we can define a target function to run over these examples. The following example simply uses OpenAI's GPT-4o model to answer questions about an image and an audio clip.

    #### Python

    The target function you are evaluating must have two positional arguments in order to consume the attachments associated with the example, the first must be called `inputs` and the second must be called `attachments`.

    * The `inputs` argument is a dictionary that contains the input data for the example, excluding the attachments.
    * The `attachments` argument is a dictionary that maps the attachment name to a dictionary containing a presigned url, mime\_type, and a reader of the bytes content of the file. You can use either the presigned url or the reader to get the file contents. Each value in the attachments dictionary is a dictionary with the following structure:

    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    {
        "presigned_url": str,
        "mime_type": str,
        "reader": BinaryIO
    }
    ```

    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    from langsmith.wrappers import wrap_openai
    import base64
    from openai import OpenAI

    client = wrap_openai(OpenAI())

    # Define target function that uses attachments
    def file_qa(inputs, attachments):
        # Read the audio bytes from the reader and encode them in base64
        audio_reader = attachments["my_wav"]["reader"]
        audio_b64 = base64.b64encode(audio_reader.read()).decode('utf-8')

        audio_completion = client.chat.completions.create(
            model="gpt-4o-audio-preview",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": inputs["audio_question"]
                        },
                        {
                            "type": "input_audio",
                            "input_audio": {
                                "data": audio_b64,
                                "format": "wav"
                            }
                        }
                    ]
                }
            ]
        )

        # Most models support taking in an image URL directly in addition to base64 encoded images
        # You can pipe the image pre-signed URL directly to the model
        image_url = attachments["my_img"]["presigned_url"]
        image_completion = client.chat.completions.create(
            model="gpt-5.4-mini",
            messages=[
              {
                "role": "user",
                "content": [
                  {"type": "text", "text": inputs["image_question"]},
                  {
                    "type": "image_url",
                    "image_url": {
                      "url": image_url,
                    },
                  },
                ],
              }
            ],
        )

        return {
            "audio_answer": audio_completion.choices[0].message.content,
            "image_answer": image_completion.choices[0].message.content,
        }
    ```

    #### TypeScript

    In the TypeScript SDK, the `config` argument is used to pass in the attachments to the target function if `includeAttachments` is set to `true`.

    The `config` will contain `attachments` which is an object mapping the attachment name to an object of the form:

    ```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    {
      presigned_url: string,
      mime_type: string,
    }
    ```

    ```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    import OpenAI from "openai";
    import { wrapOpenAI } from "langsmith/wrappers";

    const client: any = wrapOpenAI(new OpenAI());

    async function fileQA(inputs: Record<string, any>, config?: Record<string, any>) {
      const presignedUrl = config?.attachments?.["my_wav"]?.presigned_url;
      if (!presignedUrl) {
        throw new Error("No presigned URL provided for audio.");
      }

      const response = await fetch(presignedUrl);
      if (!response.ok) {
        throw new Error(`Failed to fetch audio: ${response.statusText}`);
      }

      const arrayBuffer = await response.arrayBuffer();
      const uint8Array = new Uint8Array(arrayBuffer);
      const audioB64 = Buffer.from(uint8Array).toString("base64");

      const audioCompletion = await client.chat.completions.create({
        model: "gpt-4o-audio-preview",
        messages: [
          {
            role: "user",
            content: [
              { type: "text", text: inputs["audio_question"] },
              {
                type: "input_audio",
                input_audio: {
                  data: audioB64,
                  format: "wav",
                },
              },
            ],
          },
        ],
      });

      const imageUrl = config?.attachments?.["my_img"]?.presigned_url
      const imageCompletion = await client.chat.completions.create({
        model: "gpt-5.4-mini",
        messages: [
          {
            role: "user",
            content: [
              { type: "text", text: inputs["image_question"] },
              {
                type: "image_url",
                image_url: {
                  url: imageUrl,
                },
              },
            ],
          },
        ],
      });

      return {
        audio_answer: audioCompletion.choices[0].message.content,
        image_answer: imageCompletion.choices[0].message.content,
      };
    }
    ```

    ### Define custom evaluators

    <Note>You can also define a multimodal evaluator in the UI that references these attachment inputs and outputs. UI-based evaluators run automatically on every experiment—including those invoked from the SDK. For instructions, refer to the [**UI**](#ui) tab.</Note>

    The exact same rules apply as above to determine whether the evaluator should receive attachments.

    The evaluator below uses an LLM to judge if the reasoning and the answer are consistent. To learn more about how to define llm-based evaluators, please see [How to define an LLM-as-a-judge evaluator](/langsmith/llm-as-judge).

    <CodeGroup>
      ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      # Assumes you've installed pydantic
      from pydantic import BaseModel

      def valid_image_description(outputs: dict, attachments: dict) -> bool:
        """Use an LLM to judge if the image description and images are consistent."""
        instructions = """
        Does the description of the following image make sense?
        Please carefully review the image and the description to determine if the description is valid.
        """

        class Response(BaseModel):
            description_is_valid: bool

        image_url = attachments["my_img"]["presigned_url"]
        response = client.beta.chat.completions.parse(
            model="gpt-5.5",
            messages=[
                {
                    "role": "system",
                    "content": instructions
                },
                {
                    "role": "user",
                    "content": [
                        {"type": "image_url", "image_url": {"url": image_url}},
                        {"type": "text", "text": outputs["image_answer"]}
                    ]
                }
            ],
            response_format=Response
        )
        return response.choices[0].message.parsed.description_is_valid

      ls_client.evaluate(
        file_qa,
        data=dataset_name,
        evaluators=[valid_image_description],
      )
      ```

      ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import { zodResponseFormat } from 'openai/helpers/zod';
      import { z } from 'zod';
      import { evaluate } from "langsmith/evaluation";

      const DescriptionResponse = z.object({
        description_is_valid: z.boolean(),
      });

      async function validImageDescription({
        outputs,
        attachments,
      }: {
        outputs?: any;
        attachments?: any;
      }): Promise<{ key: string; score: boolean}> {
        const instructions = `Does the description of the following image make sense?
      Please carefully review the image and the description to determine if the description is valid.`;

        const imageUrl = attachments?.["my_img"]?.presigned_url
        const completion = await client.beta.chat.completions.parse({
            model: "gpt-5.5",
            messages: [
                {
                    role: "system",
                    content: instructions,
                },
                {
                    role: "user",
                    content: [
                        { type: "image_url", image_url: { url: imageUrl } },
                        { type: "text", text: outputs?.image_answer },
                    ],
                },
            ],
            response_format: zodResponseFormat(DescriptionResponse, 'imageResponse'),
        });

        const score: boolean = completion.choices[0]?.message?.parsed?.description_is_valid ?? false;
        return { key: "valid_image_description", score };
      }

      const resp = await evaluate(fileQA, {
        data: datasetName,
        // Need to pass flag to include attachments
        includeAttachments: true,
        evaluators: [validImageDescription],
        client: langsmithClient
      });
      ```
    </CodeGroup>

    ## 3. Update examples with attachments

    In the code above, we showed how to add examples with attachments to a dataset. It is also possible to update these same examples using the SDK.

    As with existing examples, datasets are versioned when you update them with attachments. Therefore, you can navigate to the dataset version history to see the changes made to each example. To learn more, please see [Create and manage datasets in the UI](/langsmith/manage-datasets-in-application).

    When updating an example with attachments, you can update attachments in a few different ways:

    * Pass in new attachments
    * Rename existing attachments
    * Delete existing attachments

    Note that:

    * Any existing attachments that are not explicitly renamed or retained **will be deleted**.
    * An error will be raised if you pass in a non-existent attachment name to `retain` or `rename`.
    * New attachments take precedence over existing attachments in case the same attachment name appears in the `attachments` and `attachment_operations` fields.

    <CodeGroup>
      ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      example_update = {
        "id": example_id,
        "attachments": {
            # These are net new attachments
            "my_new_file": ("text/plain", b"foo bar"),
        },
        "inputs": inputs,
        "outputs": outputs,
        # Any attachments not in rename/retain will be deleted.
        # In this case, that would be "my_img" if we uploaded it.
        "attachments_operations": {
            # Retained attachments will stay exactly the same
            "retain": ["my_pdf"],
            # Renaming attachments preserves the original data
            "rename": {
                "my_wav": "my_new_wav",
            }
        },
      }

      ls_client.update_examples(dataset_id=dataset.id, updates=[example_update])
      ```

      ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import { ExampleUpdateWithAttachments } from "langsmith/schemas";

      const exampleUpdate: ExampleUpdateWithAttachments = {
        id: exampleId,
        attachments: {
          // These are net new attachments
          "my_new_file": {
            mimeType: "text/plain",
            data: Buffer.from("foo bar")
          },
        },
        attachments_operations: {
          // Retained attachments will stay exactly the same
          retain: ["my_img"],
          // Renaming attachments preserves the original data
          rename: {
            "my_wav": "my_new_wav",
          },
          // Any attachments not in rename/retain will be deleted
          // In this case, that would be "my_pdf"
        },
      };

      await langsmithClient.updateExamplesMultipart(dataset.id, [exampleUpdate]);
      ```
    </CodeGroup>
  </Tab>
</Tabs>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/evaluate-with-attachments.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# How to evaluate with OpenTelemetry
Source: https://docs.langchain.com/langsmith/evaluate-with-opentelemetry

This guide shows you how to run an evaluation using OpenTelemetry tracing with LangSmith.

<Info>
  [Evaluations](/langsmith/evaluation-concepts#evaluation-lifecycle) | [Datasets](/langsmith/evaluation-concepts#datasets) | [Trace with OpenTelemetry](/langsmith/trace-with-opentelemetry)
</Info>

If you're already using OpenTelemetry for tracing your LLM application, you can run evaluations by routing traces to an experiment session. This approach is useful when you want to evaluate applications that are instrumented with OpenTelemetry but don't use the LangSmith SDK's [`evaluate()`](https://reference.langchain.com/python/langsmith/client/Client/evaluate) function.

## Overview

When evaluating with OpenTelemetry, you need to:

1. Create an experiment session in LangSmith.
2. Configure OpenTelemetry to send traces to LangSmith.
3. Add specific span attributes to link traces to the experiment and dataset examples.
4. Run your application for each example in the dataset.

## Prerequisites

This guide assumes you have:

* An application instrumented with OpenTelemetry that sends traces to LangSmith.
* A dataset created in LangSmith with examples to evaluate. You can create a dataset via the [LangSmith UI](/langsmith/evaluation-concepts#datasets) or via the [SDK](/langsmith/manage-datasets-programmatically).

This tutorial uses Strands agents as example implementations, but the approach works with any OpenTelemetry-instrumentation.

Install dependencies:

<CodeGroup>
  ```bash Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  pip install langsmith strands-agents strands-agents-tools opentelemetry-sdk opentelemetry-exporter-otlp
  ```

  ```bash TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  npm install langsmith @strands-agents/sdk @opentelemetry/api @opentelemetry/sdk-trace-node @opentelemetry/sdk-trace-base @opentelemetry/exporter-trace-otlp-http @opentelemetry/resources
  ```
</CodeGroup>

Set the following environment variables:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}

# Tracing configuration
LANGSMITH_ENDPOINT="https://api.smith.langchain.com"
LANGSMITH_API_KEY="<your-langsmith-api-key>"
OTEL_EXPORTER_OTLP_ENDPOINT = "https://api.smith.langchain.com/otel/"

# AWS Credentials
AWS_ACCESS_KEY_ID="<your-aws-access-key-id>"
AWS_SECRET_ACCESS_KEY="<your-aws-secret-access-key>"
AWS_REGION_NAME="<your-aws-region>"
```

<Note>
  If you're [self-hosting LangSmith](/langsmith/self-hosted), replace `OTEL_EXPORTER_OTLP_ENDPOINT` with your self-hosted URL and append `/api/v1/otel`. For example: `OTEL_EXPORTER_OTLP_ENDPOINT = "https://ai-company.com/api/v1/otel"`.

  Replace `LANGSMITH_ENDPOINT` with your LangSmith API endpoint. For example: `LANGSMITH_ENDPOINT = "https://ai-company.com/api/v1"`.
</Note>

## Step 1. Create an experiment session

This guide assumes that a dataset has been created in LangSmith with examples to evaluate. You can create a dataset via the [LangSmith UI](/langsmith/evaluation-concepts#datasets) or via the [SDK](/langsmith/manage-datasets-programmatically).

An experiment session groups all evaluation traces together. Create one using the LangSmith client:

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langsmith import Client

  # Initialize LangSmith client
  client = Client()

  experiment_name = "strands-agent-experiment"
  # Assumes a dataset has been created. You can find the dataset ID in the LangSmith UI or via the SDK.
  dataset_id = "<your-dataset-id>"

  # Create an experiment session linked to the dataset
  project = client.create_project(
      project_name=experiment_name,
      reference_dataset_id=dataset_id
  )

  experiment_id = str(project.id)
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { Client } from "langsmith";

  // Initialize LangSmith client
  const client = new Client({
    apiKey: process.env.LANGSMITH_API_KEY,
  });

  const experimentName = "strands-agent-experiment";
  const datasetId = "your-dataset-id";

  // Create an experiment session linked to the dataset
  const project = await client.createProject({
    projectName: experimentName,
    referenceDatasetId: datasetId,
  });

  const experimentId = project.id;
  ```
</CodeGroup>

Additionally, you can create evaluators in the LangSmith UI and bind them to your dataset. For evaluators defined in the UI and bound to your dataset, they will automatically run on experiment traces.

To learn more about evaluators, see [Evaluators](/langsmith/evaluation-concepts#evaluators).

## Step 2. Define an application and configure OpenTelemetry

First, you need an application that uses OpenTelemetry for tracing. This example uses a Strands agent, but you can use any OpenTelemetry-instrumented application. Set up OpenTelemetry to route traces to your experiment session by including the experiment ID in the OTEL headers. The general idea in this step is to have an agent or application that has been instrumented with OpenTelemetry.

<Note>
  TypeScript examples are not provided for this step as the `Strands TypeScript SDK` does not currently support `OpenTelemetry` observability (as of February 2026).
</Note>

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import os
  from strands import Agent
  from strands_tools import file_read, file_write, python_repl, shell, journal
  from strands.telemetry import StrandsTelemetry

  # Set OTEL headers with experiment ID as the project
  api_key = os.getenv('LANGSMITH_API_KEY')
  os.environ['OTEL_EXPORTER_OTLP_HEADERS'] = f"x-api-key={api_key},Langsmith-Project={experiment_id}"

  # Initialize telemetry
  strands_telemetry = StrandsTelemetry()
  strands_telemetry.setup_otlp_exporter()

  # Create an agent (Strands automatically creates OTel spans)
  agent = Agent(
      tools=[file_read, file_write, python_repl, shell, journal],
      system_prompt="You are an Expert Software Developer.",
      model="us.anthropic.claude-sonnet-4-20250514-v1:0",
  )
  ```
</CodeGroup>

For details on setting up OpenTelemetry tracing with LangSmith, see [Trace with OpenTelemetry](/langsmith/trace-with-opentelemetry).

## Step 3. Set up key span attributes

Add the required span attributes to each application run. These attributes link each trace to the experiment and the specific dataset example.

The following attributes are relevant for experiment evaluation:

| Attribute                        | Purpose                                           |
| -------------------------------- | ------------------------------------------------- |
| `langsmith.trace.session_id`     | Routes the trace to your experiment session       |
| `langsmith.reference_example_id` | Links the trace to a specific dataset example     |
| `langsmith.span.kind`            | Sets the span type (e.g., "llm", "chain", "tool") |
| `inputs`                         | Records the input to your application             |
| `outputs`                        | Records the output from your application          |

For a complete list of supported OpenTelemetry attributes, see [Trace with OpenTelemetry](/langsmith/trace-with-opentelemetry#supported-opentelemetry-attribute-and-event-mapping).

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from opentelemetry import trace

  def evaluate_with_opentelemetry(agent, example_id: str, example_input: str, experiment_id: str):
      tracer = trace.get_tracer(__name__)

      # Wrapper span to add experiment metadata
      with tracer.start_as_current_span("experiment_evaluation") as span:
          # Route trace to the experiment
          span.set_attribute("langsmith.trace.session_id", experiment_id)

          # Link trace to the specific dataset example
          span.set_attribute("langsmith.reference_example_id", example_id)

          # Record input
          span.set_attribute("inputs", example_input)

          # Run the application
          response = agent(example_input)

          # Record output
          output_text = getattr(response, "output", str(response))
          span.set_attribute("outputs", output_text)

          return output_text
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { trace, Span } from "@opentelemetry/api";

  async function evaluateWithAgent(
    agent: Agent,
    exampleId: string,
    exampleInput: string,
    experimentId: string
  ): Promise<string> {
    const tracer = trace.getTracer("experiment-runner");

    return await tracer.startActiveSpan(
      "experiment_evaluation",
      async (span: Span) => {
        try {
          // Route trace to the experiment
          span.setAttribute("langsmith.trace.session_id", experimentId);

          // Link trace to the specific dataset example
          span.setAttribute("langsmith.reference_example_id", exampleId);

          // Record input
          span.setAttribute("inputs", exampleInput);

          // Run the application
          const result = await agent.invoke(exampleInput);
          // Record output
          const response = String(result);
          span.setAttribute("outputs", response);

          return response;
        } finally {
          span.end();
        }
      }
    );
  }
  ```
</CodeGroup>

## Step 4. Run evaluation by iterating through dataset examples

Each experiment run creates traces in LangSmith that are linked to your dataset examples.

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  # Iterate through dataset examples
  for example in client.list_examples(dataset_name=dataset_name):

      # Extract input from the example inputs dictionary
      # Adjust the key based on your dataset structure
      # (e.g., "input", "question", etc.)
      example_input = example.inputs.get("input")

      evaluate_with_opentelemetry(
          agent=agent,
          example_id=str(example.id),
          example_input=str(example_input),
          experiment_id=experiment_id
      )
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  // Iterate through dataset examples
  for await (const example of client.listExamples({ datasetName })) {
    // Extract input from the example inputs dictionary
    // Adjust the key based on your dataset structure
    // (e.g., "input", "question", etc.)
    const exampleInput = example.inputs.input;

    await evaluateWithAgent(
      agent,
      example.id,
      String(exampleInput),
      experimentId
    );
  }
  ```
</CodeGroup>

After running the evaluation, you can [analyze the experiment](/langsmith/analyze-an-experiment) in the LangSmith UI to see:

* Individual trace details for each example
* Evaluator scores and feedback
* Comparisons between different experiment runs

Navigate to your experiment in the [LangSmith UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-evaluate-with-opentelemetry) to analyze the results.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/evaluate-with-opentelemetry.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# How to retry failed runs in experiments (Python only)
Source: https://docs.langchain.com/langsmith/evaluate-with-retry

When running [evaluations](/langsmith/evaluation-concepts#evaluation-lifecycle) on large [datasets](/langsmith/evaluation-concepts#datasets), you may encounter failures on a small subset of examples due to rate limits, network issues, or other transient errors. Rather than re-running the entire evaluation, you can identify and retry only the failed examples on an [experiment](/langsmith/evaluation-concepts#experiment).

This guide shows an approach to build retry logic into your evaluation workflow and to retry only the failed examples. You can use the `error_handling='ignore'` parameter to skip logging errored runs, then automatically identify unsuccessful examples and re-run them in Python.

## Step 1. Run the initial evaluation

Run the initial evaluation, ignoring errors to  prevent errored runs from being logged:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langsmith import Client

client = Client()

# Run initial evaluation, ignoring errors

# error_handling='ignore' prevents errored runs from being logged
results = await client.aevaluate(
    target,
    data="dataset",
    evaluators=[your_evaluators],
    error_handling='ignore'
)
```

## Step 2. Retry on failed examples and log to same experiment

Fetch all the unsuccessful examples:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}

# Identify unsuccessful examples
runs = client.list_runs(project_name=results.experiment_name)
successful_example_ids = [r.reference_example_id for r in runs]
unsuccessful_examples = (e for e in client.list_examples(dataset_name="dataset") if e.id not in successful_examples)
```

Next, re-run all the failed examples and log them to the same experiment:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}

# Retry only the failed examples, log
results_retry = await client.aevaluate(
    target,
    unsuccessful_examples,
    evaluators=[your_evaluators],
    experiment=results.experiment_name,
    error_handling='ignore'
)
```

## Related topics

* [Run an evaluation](/langsmith/evaluate-llm-application)
* [Run an evaluation asynchronously](/langsmith/evaluation-async)
* [Handle model rate limits](/langsmith/rate-limiting)
* [Experiment configuration](/langsmith/experiment-configuration)
* [Evaluate existing experiment](/langsmith/evaluate-existing-experiment)

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/evaluate-with-retry.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# LangSmith Evaluation
Source: https://docs.langchain.com/langsmith/evaluation

LangSmith supports two types of evaluations based on when and where they run:

<CardGroup>
  <Card title="Offline Evaluation" icon="flask">
    **Test before you ship**

    Run evaluations on curated datasets during development to compare versions, benchmark performance, and catch regressions.
  </Card>

  <Card title="Online Evaluation" icon="radar">
    **Monitor in production**

    Evaluate real user interactions in real-time to detect issues and measure quality on live traffic.
  </Card>
</CardGroup>

## Evaluation workflow

<Tabs>
  <Tab title="Offline evaluation flow">
    <Steps>
      <Step title="Create a dataset">
        Create a [dataset](/langsmith/manage-datasets) with <Tooltip>[examples](/langsmith/evaluation-concepts#examples)</Tooltip> from manually curated test cases, historical production traces, or synthetic data generation.
      </Step>

      <Step title="Define evaluators">
        Create <Tooltip>[evaluators](/langsmith/evaluation-concepts#evaluators)</Tooltip> to score performance:

        * [Human](/langsmith/evaluation-concepts#human) review
        * [Code](/langsmith/evaluation-concepts#code) rules
        * [LLM-as-judge](/langsmith/llm-as-judge)
        * [Pairwise](/langsmith/evaluate-pairwise) comparison
      </Step>

      <Step title="Run an experiment">
        Execute your application on the dataset to create an <Tooltip>[experiment](/langsmith/evaluation-concepts#experiment)</Tooltip>. Configure [repetitions, concurrency, and caching](/langsmith/experiment-configuration) to optimize runs.
      </Step>

      <Step title="Analyze results">
        Compare experiments for [benchmarking](/langsmith/evaluation-types#benchmarking), [unit tests](/langsmith/evaluation-types#unit-tests), [regression tests](/langsmith/evaluation-types#regression-tests), or [backtesting](/langsmith/evaluation-types#backtesting).
      </Step>
    </Steps>
  </Tab>

  <Tab title="Online evaluation flow">
    <Steps>
      <Step title="Deploy your application">
        Each interaction creates a <Tooltip>[run](/langsmith/evaluation-concepts#runs)</Tooltip> without reference outputs.
      </Step>

      <Step title="Configure online evaluators">
        Set up [evaluators](/langsmith/online-evaluations-llm-as-judge) to run automatically on production traces: safety checks, format validation, quality heuristics, and reference-free LLM-as-judge. Apply [filters and sampling rates](/langsmith/online-evaluations-llm-as-judge#configure-a-sampling-rate) to control costs.
      </Step>

      <Step title="Monitor in real-time">
        Evaluators run automatically on [runs](/langsmith/evaluation-concepts#runs) or <Tooltip>[threads](/langsmith/online-evaluations-multi-turn)</Tooltip>, providing real-time monitoring, anomaly detection, and alerting.
      </Step>

      <Step title="Establish a feedback loop">
        Add failing production traces to your [dataset](/langsmith/manage-datasets), create targeted evaluators, validate fixes with offline experiments, and redeploy.
      </Step>
    </Steps>
  </Tab>
</Tabs>

<Tip>
  For more on the differences between offline and online evaluation, refer to the [Evaluation concepts](/langsmith/evaluation-concepts#quick-reference-offline-vs-online-evaluation) page.
</Tip>

## Get started

<Columns>
  <Card title="Evaluation quickstart" icon="rocket" href="/langsmith/evaluation-quickstart">
    Get started with offline evaluation.
  </Card>

  <Card title="Manage datasets" icon="database" href="/langsmith/manage-datasets">
    Create and manage datasets for evaluation through the UI or SDK.
  </Card>

  <Card title="Run offline evaluations" icon="microscope" href="/langsmith/evaluate-llm-application">
    Explore evaluation types, techniques, and frameworks for comprehensive testing.
  </Card>

  <Card title="Analyze results" icon="chart-bar" href="/langsmith/analyze-an-experiment">
    View and analyze evaluation results, compare experiments, filter data, and export findings.
  </Card>

  <Card title="Run online evaluations" icon="radar" href="/langsmith/online-evaluations-llm-as-judge">
    Monitor production quality in real-time from the Observability tab.
  </Card>

  <Card title="Follow tutorials" icon="book" href="/langsmith/evaluate-chatbot-tutorial">
    Learn by following step-by-step tutorials, from simple chatbots to complex agent evaluations.
  </Card>
</Columns>

<Note>
  To set up a LangSmith instance, visit the [Platform setup section](/langsmith/platform-setup) to choose between cloud, hybrid, or self-hosted. All options include observability, evaluation, prompt engineering, and deployment.
</Note>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/evaluation.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
