#  org.tensorflow Stay organized with collections  Save and categorize content based on your preferences.
Defines classes to build, save, load and execute TensorFlow models.  **Warning:** This API is deprecated and will be removed in a future version of TensorFlow after [the replacement](https://tensorflow.org/java) is stable.
To get started, see the [ installation instructions.](https://tensorflow.org/install/lang_java_legacy)
The [LabelImage](https://www.tensorflow.org/code/tensorflow/java/src/main/java/org/tensorflow/examples/LabelImage.java) example demonstrates use of this API to classify images using a pre-trained
  * Graph construction: using the OperationBuilder class to construct a graph to decode, resize and normalize a JPEG image.
  * Model loading: Using Graph.importGraphDef() to load a pre-trained Inception model.
  * Graph execution: Using a Session to execute the graphs and find the best label for an image.


Additional examples can be found in the
### Interfaces
[ExecutionEnvironment](https://www.tensorflow.org/api_docs/java/org/tensorflow/ExecutionEnvironment) | Defines an environment for creating and executing TensorFlow `Operation[](https://www.tensorflow.org/api_docs/java/org/tensorflow/Operation)`s.
---|---
[Graph.WhileSubgraphBuilder](https://www.tensorflow.org/api_docs/java/org/tensorflow/Graph.WhileSubgraphBuilder) | Used to instantiate an abstract class which overrides the buildSubgraph method to build a conditional or body subgraph for a while loop.
[Operand](https://www.tensorflow.org/api_docs/java/org/tensorflow/Operand)<T> | Interface implemented by operands of a TensorFlow operation.
[Operation](https://www.tensorflow.org/api_docs/java/org/tensorflow/Operation) | Performs computation on Tensors.
[OperationBuilder](https://www.tensorflow.org/api_docs/java/org/tensorflow/OperationBuilder) | A builder for `Operation[](https://www.tensorflow.org/api_docs/java/org/tensorflow/Operation)`s.
### Classes
[EagerSession](https://www.tensorflow.org/api_docs/java/org/tensorflow/EagerSession) | An environment for executing TensorFlow operations eagerly.
---|---
[EagerSession.Options](https://www.tensorflow.org/api_docs/java/org/tensorflow/EagerSession.Options) |
[Graph](https://www.tensorflow.org/api_docs/java/org/tensorflow/Graph) | A data flow graph representing a TensorFlow computation.
[GraphOperation](https://www.tensorflow.org/api_docs/java/org/tensorflow/GraphOperation) | Implementation for an `Operation[](https://www.tensorflow.org/api_docs/java/org/tensorflow/Operation)` added as a node to a `Graph[](https://www.tensorflow.org/api_docs/java/org/tensorflow/Graph)`.
[GraphOperationBuilder](https://www.tensorflow.org/api_docs/java/org/tensorflow/GraphOperationBuilder) | An `OperationBuilder[](https://www.tensorflow.org/api_docs/java/org/tensorflow/OperationBuilder)` for adding `GraphOperation[](https://www.tensorflow.org/api_docs/java/org/tensorflow/GraphOperation)`s to a `Graph[](https://www.tensorflow.org/api_docs/java/org/tensorflow/Graph)`.
[Output](https://www.tensorflow.org/api_docs/java/org/tensorflow/Output)<T> | A symbolic handle to a tensor produced by an `Operation[](https://www.tensorflow.org/api_docs/java/org/tensorflow/Operation)`.
[SavedModelBundle](https://www.tensorflow.org/api_docs/java/org/tensorflow/SavedModelBundle) | SavedModelBundle represents a model loaded from storage.
[SavedModelBundle.Loader](https://www.tensorflow.org/api_docs/java/org/tensorflow/SavedModelBundle.Loader) | Options for loading a SavedModel.
[Server](https://www.tensorflow.org/api_docs/java/org/tensorflow/Server) | An in-process TensorFlow server, for use in distributed training.
[Session](https://www.tensorflow.org/api_docs/java/org/tensorflow/Session) | Driver for `Graph[](https://www.tensorflow.org/api_docs/java/org/tensorflow/Graph)` execution.
[Session.Run](https://www.tensorflow.org/api_docs/java/org/tensorflow/Session.Run) | Output tensors and metadata obtained when executing a session.
[Session.Runner](https://www.tensorflow.org/api_docs/java/org/tensorflow/Session.Runner) | Run `Operation[](https://www.tensorflow.org/api_docs/java/org/tensorflow/Operation)`s and evaluate `Tensors[](https://www.tensorflow.org/api_docs/java/org/tensorflow/Tensor)`.
[Shape](https://www.tensorflow.org/api_docs/java/org/tensorflow/Shape) | The possibly partially known shape of a tensor produced by an operation.
[Tensor](https://www.tensorflow.org/api_docs/java/org/tensorflow/Tensor)<T> | A statically typed multi-dimensional array whose elements are of a type described by T.
[TensorFlow](https://www.tensorflow.org/api_docs/java/org/tensorflow/TensorFlow) | Static utility methods describing the TensorFlow runtime.
[Tensors](https://www.tensorflow.org/api_docs/java/org/tensorflow/Tensors) | Type-safe factory methods for creating `Tensor[](https://www.tensorflow.org/api_docs/java/org/tensorflow/Tensor)` objects.
### Enums
[DataType](https://www.tensorflow.org/api_docs/java/org/tensorflow/DataType) | Represents the type of elements in a `Tensor[](https://www.tensorflow.org/api_docs/java/org/tensorflow/Tensor)` as an enum.
---|---
[EagerSession.DevicePlacementPolicy](https://www.tensorflow.org/api_docs/java/org/tensorflow/EagerSession.DevicePlacementPolicy) | Controls how to act when we try to run an operation on a given device but some input tensors are not on that device.
[EagerSession.ResourceCleanupStrategy](https://www.tensorflow.org/api_docs/java/org/tensorflow/EagerSession.ResourceCleanupStrategy) | Controls how TensorFlow resources are cleaned up when they are no longer needed.
### Exceptions
[TensorFlowException](https://www.tensorflow.org/api_docs/java/org/tensorflow/TensorFlowException) | Unchecked exception thrown when executing TensorFlow Graphs.
---|---
Except as otherwise noted, the content of this page is licensed under the
Last updated 2022-02-12 UTC.
[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2022-02-12 UTC."],[],[]]
  * ### Stay connected
    * [ Blog ](https://blog.tensorflow.org)
    * [ Forum ](https://discuss.tensorflow.org)
  * ### Support
    * [ Brand guidelines ](https://www.tensorflow.org/extras/tensorflow_brand_guidelines.pdf)
    * [ Cite TensorFlow ](https://www.tensorflow.org/about/bib)


  * [ Manage cookies ](https://www.tensorflow.org/api_docs/java/org/tensorflow/package-summary)
  * Sign up for the TensorFlow newsletter [ Subscribe ](https://www.tensorflow.org/subscribe)


  * English
  * Español
  * Español – América Latina
  * Français
  * Indonesia
  * Italiano
  * Polski
  * Português
  * Português – Brasil
  * Tiếng Việt
  * Türkçe
  * Русский
  * עברית
  * العربيّة
  * فارسی
  * हिंदी
  * বাংলা
  * ภาษาไทย
  * 中文 – 简体
  * 日本語
  * 한국어
