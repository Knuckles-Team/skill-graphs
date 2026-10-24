Evaluate documentation
Evaluate on the Hub
# Evaluate
🏡 View all docs AWS Trainium & Inferentia Accelerate Argilla AutoTrain Bitsandbytes Chat UI Dataset viewer Datasets Deploying on AWS Diffusers Distilabel Evaluate Google Cloud Google TPUs Gradio Hub Hub Python Library Huggingface.js Inference Endpoints (dedicated) Inference Providers Kernels LeRobot Leaderboards Lighteval Microsoft Azure Optimum PEFT Reachy Mini Safetensors Sentence Transformers TRL Tasks Text Embeddings Inference Text Generation Inference Tokenizers Trackio Transformers Transformers.js smolagents timm
Search documentation
`Ctrl+K`
main v0.4.6 v0.3.0 v0.2.3 v0.1.2 EN
Get started
[🤗 Evaluate ](https://huggingface.co/docs/evaluate/index)
Tutorials
[Installation ](https://huggingface.co/docs/evaluate/installation)[A quick tour ](https://huggingface.co/docs/evaluate/a_quick_tour)
How-to guides
[Choosing the right metric ](https://huggingface.co/docs/evaluate/choosing_a_metric)[Adding new evaluations ](https://huggingface.co/docs/evaluate/creating_and_sharing)[Using the evaluator ](https://huggingface.co/docs/evaluate/base_evaluator)[Using the evaluator with custom pipelines ](https://huggingface.co/docs/evaluate/custom_evaluator)[Creating an EvaluationSuite ](https://huggingface.co/docs/evaluate/evaluation_suite)
Using 🤗 Evaluate with other ML frameworks
[Transformers ](https://huggingface.co/docs/evaluate/transformers_integrations)[Keras and Tensorflow ](https://huggingface.co/docs/evaluate/keras_integrations)[scikit-learn ](https://huggingface.co/docs/evaluate/sklearn_integrations)
Conceptual guides
[Types of evaluations ](https://huggingface.co/docs/evaluate/types_of_evaluations)[Considerations for model evaluation ](https://huggingface.co/docs/evaluate/considerations)
Reference
[Main classes ](https://huggingface.co/docs/evaluate/package_reference/main_classes)[Loading methods ](https://huggingface.co/docs/evaluate/package_reference/loading_methods)[Saving methods ](https://huggingface.co/docs/evaluate/package_reference/saving_methods)[Hub methods ](https://huggingface.co/docs/evaluate/package_reference/hub_methods)[Evaluator classes ](https://huggingface.co/docs/evaluate/package_reference/evaluator_classes)[Visualization methods ](https://huggingface.co/docs/evaluate/package_reference/visualization_methods)[Logging methods ](https://huggingface.co/docs/evaluate/package_reference/logging_methods)
![Hugging Face's logo](https://huggingface.co/front/assets/huggingface_logo-noborder.svg)
Join the Hugging Face community
and get access to the augmented documentation experience
Collaborate on models, datasets and Spaces
Faster examples with accelerated inference
Switch between documentation themes
[Sign Up](https://huggingface.co/join)
to get started
#  [](https://huggingface.co/docs/evaluate/index#evaluate-on-the-hub) Evaluate on the Hub

![Evaluate on the Hub banner](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/evaluate-docs/evaluate-on-hub-banner.png)

You can evaluate AI models on the Hub in multiple ways and this page will guide you through the different options:
  * **Community Leaderboards** bring together the best models for a given task or domain and make them accessible to everyone by ranking them.
  * **Model Cards** provide a comprehensive overview of a model’s capabilities from the author’s perspective.
  * **Libraries and Packages** give you the tools to evaluate your models on the Hub.


##  [](https://huggingface.co/docs/evaluate/index#community-leaderboards) Community Leaderboards
Community leaderboards show how a model performs on a given task or domain. For example, there are leaderboards for question answering, reasoning, classification, vision, and audio. If you’re tackling a new task, you can use a leaderboard to see how a model performs on it.
Here are some examples of community leaderboards:
Leaderboard | Model Type | Description
---|---|---
[MTEB](https://huggingface.co/spaces/mteb/leaderboard) | Embedding | The Massive Text Embedding Benchmark leaderboard compares 100+ text and image embedding models across 1000+ languages. Refer to the publication of each selectable benchmark for details on metrics, languages, tasks, and task types. Anyone is welcome to add a model, add benchmarks, help improve zero-shot annotations, or propose other changes to the leaderboard.
[GAIA](https://huggingface.co/spaces/gaia-benchmark/leaderboard) | Agentic | GAIA is a benchmark which aims at evaluating next-generation LLMs (LLMs with augmented capabilities due to added tooling, efficient prompting, access to search, etc). (See
[OpenVLM Leaderboard](https://huggingface.co/spaces/opencompass/open_vlm_leaderboard) | Vision Language Models | The OpenVLM Leaderboard evaluates 272+ Vision-Language Models (including GPT-4v, Gemini, QwenVLPlus, LLaVA) across 31 different multi-modal benchmarks using the VLMEvalKit framework. It focuses on open-source VLMs and publicly available API models.
[Open ASR Leaderboard](https://huggingface.co/spaces/hf-audio/open_asr_leaderboard) | Audio | The Open ASR Leaderboard ranks and evaluates speech recognition models on the Hugging Face Hub. Models are ranked based on their Average WER, from lowest to highest.
[LLM-Perf Leaderboard](https://huggingface.co/spaces/llm-perf/leaderboard) | LLM Performance | The 🤗 LLM-Perf Leaderboard 🏋️ is a leaderboard at the intersection of quality and performance. Its aim is to benchmark the performance (latency, throughput, memory & energy) of Large Language Models (LLMs) with different hardware, backends and optimizations using Optimum-Benchmark.
There are many more leaderboards on the Hub. Check out all the leaderboards via this [search](https://huggingface.co/spaces?category=model-benchmarking) or use this [dedicated Space](https://huggingface.co/spaces/OpenEvals/find-a-leaderboard) to find a leaderboard for your task.
##  [](https://huggingface.co/docs/evaluate/index#model-cards) Model Cards
Model cards provide an overview of a model’s capabilities evaluated by the community or the model’s author. They are a great way to understand a model’s capabilities and limitations.
![Qwen model card](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/evaluate-docs/qwen-model-card.png)
Unlike leaderboards, model card evaluation scores are often created by the author, rather than by the community.
For information on reporting results, see details on [the Model Card Evaluation Results metadata](https://huggingface.co/docs/hub/en/model-cards#evaluation-results).
##  [](https://huggingface.co/docs/evaluate/index#libraries-and-packages) Libraries and packages
There are a number of open-source libraries and packages that you can use to evaluate your models on the Hub. These are useful if you want to evaluate a custom model or performance on a custom evaluation task.
###  [](https://huggingface.co/docs/evaluate/index#lighteval) LightEval
LightEval is a library for evaluating LLMs. It is designed to be comprehensive and customizable. Visit the LightEval
For more recent evaluation approaches that are popular on the Hugging Face Hub that are currently more actively maintained, check out
###  [](https://huggingface.co/docs/evaluate/index#-evaluate) 🤗 Evaluate
A library for easily evaluating machine learning models and datasets.
With a single line of code, you get access to dozens of evaluation methods for different domains (NLP, Computer Vision, Reinforcement Learning, and more!). Be it on your local machine or in a distributed training setup, you can evaluate your models in a consistent and reproducible way!
Visit the 🤗 Evaluate [organization](https://huggingface.co/evaluate-metric) for a full list of available metrics. Each metric has a dedicated Space with an interactive demo for how to use the metric, and a documentation card detailing the metrics limitations and usage.
[Tutorials Learn the basics and become familiar with loading, computing, and saving with 🤗 Evaluate. Start here if you are using 🤗 Evaluate for the first time!](https://huggingface.co/docs/evaluate/installation) [How-to guides Practical guides to help you achieve a specific goal. Take a look at these guides to learn how to use 🤗 Evaluate to solve real-world problems.](https://huggingface.co/docs/evaluate/choosing_a_metric) [Conceptual guides High-level explanations for building a better understanding of important topics such as considerations going into evaluating a model or dataset and the difference between metrics, measurements, and comparisons.](https://huggingface.co/docs/evaluate/types_of_evaluations) [Reference Technical descriptions of how 🤗 Evaluate classes and methods work.](https://huggingface.co/docs/evaluate/package_reference/main_classes)
[Installation→](https://huggingface.co/docs/evaluate/installation)
[Evaluate on the Hub](https://huggingface.co/docs/evaluate/index#evaluate-on-the-hub)[Community Leaderboards](https://huggingface.co/docs/evaluate/index#community-leaderboards)[Model Cards](https://huggingface.co/docs/evaluate/index#model-cards)[Libraries and packages](https://huggingface.co/docs/evaluate/index#libraries-and-packages)[LightEval](https://huggingface.co/docs/evaluate/index#lighteval)[🤗 Evaluate](https://huggingface.co/docs/evaluate/index#-evaluate)
