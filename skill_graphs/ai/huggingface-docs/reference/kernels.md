Kernels documentation
Kernels
# Kernels
🏡 View all docs AWS Trainium & Inferentia Accelerate Argilla AutoTrain Bitsandbytes Chat UI Dataset viewer Datasets Deploying on AWS Diffusers Distilabel Evaluate Google Cloud Google TPUs Gradio Hub Hub Python Library Huggingface.js Inference Endpoints (dedicated) Inference Providers Kernels LeRobot Leaderboards Lighteval Microsoft Azure Optimum PEFT Reachy Mini Safetensors Sentence Transformers TRL Tasks Text Embeddings Inference Text Generation Inference Tokenizers Trackio Transformers Transformers.js smolagents timm
Search documentation
`Ctrl+K`
main EN
Getting started
[Introduction ](https://huggingface.co/docs/kernels/index)[Installation ](https://huggingface.co/docs/kernels/installation)
Using kernels
[Basic Usage ](https://huggingface.co/docs/kernels/basic-usage)[Using Layers ](https://huggingface.co/docs/kernels/layers)[Locking Kernel Versions ](https://huggingface.co/docs/kernels/locking)[Environment Variables ](https://huggingface.co/docs/kernels/env)[FAQ ](https://huggingface.co/docs/kernels/faq)[Migrating from older versions ](https://huggingface.co/docs/kernels/migration)
Building kernels
[Writing Kernels ](https://huggingface.co/docs/kernels/builder/writing-kernels)[Building with Nix ](https://huggingface.co/docs/kernels/builder/nix)[Building with Docker ](https://huggingface.co/docs/kernels/builder/docker)[Local Development ](https://huggingface.co/docs/kernels/builder/local-dev)[Kernel Requirements ](https://huggingface.co/docs/kernels/kernel-requirements)[Security ](https://huggingface.co/docs/kernels/builder/security)[Why Nix? ](https://huggingface.co/docs/kernels/builder/why-nix)[Metal Notes ](https://huggingface.co/docs/kernels/builder/metal)[Build Variants ](https://huggingface.co/docs/kernels/builder/build-variants)
API Reference
[Kernels ](https://huggingface.co/docs/kernels/api/kernels)[Layers ](https://huggingface.co/docs/kernels/api/layers)[Kernels CLI ](https://huggingface.co/docs/kernels/cli)
CLI Reference
[kernels init ](https://huggingface.co/docs/kernels/cli-init)[kernels upload ](https://huggingface.co/docs/kernels/cli-upload)[kernels benchmark ](https://huggingface.co/docs/kernels/cli-benchmark)[kernels check ](https://huggingface.co/docs/kernels/cli-check)[kernels versions ](https://huggingface.co/docs/kernels/cli-versions)[kernels generate-readme ](https://huggingface.co/docs/kernels/cli-generate-readme)[kernels lock ](https://huggingface.co/docs/kernels/cli-lock)[kernels download ](https://huggingface.co/docs/kernels/cli-download)[kernels skills ](https://huggingface.co/docs/kernels/cli-skills)[kernels create-and-upload-card ](https://huggingface.co/docs/kernels/cli-create-and-upload-card)
![Hugging Face's logo](https://huggingface.co/front/assets/huggingface_logo-noborder.svg)
Join the Hugging Face community
and get access to the augmented documentation experience
Collaborate on models, datasets and Spaces
Faster examples with accelerated inference
Switch between documentation themes
[Sign Up](https://huggingface.co/join)
to get started
Copy page
#  [](https://huggingface.co/docs/kernels/index#kernels) Kernels
![kernel-builder logo](https://github.com/user-attachments/assets/64a652f3-0cd3-4829-b3c1-df13f7933569)
The Kernel Hub allows Python libraries and applications to load compute kernels directly from the
  * **Portable** : a kernel can be loaded from paths outside `PYTHONPATH`.
  * **Unique** : multiple versions of the same kernel can be loaded in the same Python process.
  * **Compatible** : kernels must support all recent versions of Python and the different PyTorch build configurations (various CUDA versions and C++ ABIs). Furthermore, older C library versions must be supported.


You can [search for kernels](https://huggingface.co/models?other=kernels) on the Hub.
[Installation→](https://huggingface.co/docs/kernels/installation)
[Kernels](https://huggingface.co/docs/kernels/index#kernels)
