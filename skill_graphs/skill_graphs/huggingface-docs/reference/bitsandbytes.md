Bitsandbytes documentation
bitsandbytes
# Bitsandbytes
🏡 View all docs AWS Trainium & Inferentia Accelerate Argilla AutoTrain Bitsandbytes Chat UI Dataset viewer Datasets Deploying on AWS Diffusers Distilabel Evaluate Google Cloud Google TPUs Gradio Hub Hub Python Library Huggingface.js Inference Endpoints (dedicated) Inference Providers Kernels LeRobot Leaderboards Lighteval Microsoft Azure Optimum PEFT Reachy Mini Safetensors Sentence Transformers TRL Tasks Text Embeddings Inference Text Generation Inference Tokenizers Trackio Transformers Transformers.js smolagents timm
Search documentation
`Ctrl+K`
main v0.49.2 v0.48.2 v0.47.0 v0.46.0 v0.45.4 v0.44.1 v0.43.3 v0.42.0 EN
Get started
[bitsandbytes ](https://huggingface.co/docs/bitsandbytes/index)[Installation ](https://huggingface.co/docs/bitsandbytes/installation)[Quickstart ](https://huggingface.co/docs/bitsandbytes/quickstart)
Usage Guides
[8-bit optimizers ](https://huggingface.co/docs/bitsandbytes/optimizers)[FSDP-QLoRA ](https://huggingface.co/docs/bitsandbytes/fsdp_qlora)[Integrations ](https://huggingface.co/docs/bitsandbytes/integrations)[Troubleshoot ](https://huggingface.co/docs/bitsandbytes/errors)[Contribute ](https://huggingface.co/docs/bitsandbytes/contributing)[FAQs ](https://huggingface.co/docs/bitsandbytes/faqs)
Explanation
[8-bit optimizers ](https://huggingface.co/docs/bitsandbytes/explanations/optimizers)[Papers, resources & how to cite ](https://huggingface.co/docs/bitsandbytes/explanations/resources)
API reference
[Functional ](https://huggingface.co/docs/bitsandbytes/reference/functional)
Optimizers
[Overview ](https://huggingface.co/docs/bitsandbytes/reference/optim/optim_overview)[AdaGrad ](https://huggingface.co/docs/bitsandbytes/reference/optim/adagrad)[Adam ](https://huggingface.co/docs/bitsandbytes/reference/optim/adam)[AdamW ](https://huggingface.co/docs/bitsandbytes/reference/optim/adamw)[AdEMAMix ](https://huggingface.co/docs/bitsandbytes/reference/optim/ademamix)[LAMB ](https://huggingface.co/docs/bitsandbytes/reference/optim/lamb)[LARS ](https://huggingface.co/docs/bitsandbytes/reference/optim/lars)[Lion ](https://huggingface.co/docs/bitsandbytes/reference/optim/lion)[RMSprop ](https://huggingface.co/docs/bitsandbytes/reference/optim/rmsprop)[SGD ](https://huggingface.co/docs/bitsandbytes/reference/optim/sgd)
Modules
[LLM.int8() ](https://huggingface.co/docs/bitsandbytes/reference/nn/linear8bit)[4-bit quantizer ](https://huggingface.co/docs/bitsandbytes/reference/nn/linear4bit)[Embedding ](https://huggingface.co/docs/bitsandbytes/reference/nn/embeddings)
![Hugging Face's logo](https://huggingface.co/front/assets/huggingface_logo-noborder.svg)
Join the Hugging Face community
and get access to the augmented documentation experience
Collaborate on models, datasets and Spaces
Faster examples with accelerated inference
Switch between documentation themes
[Sign Up](https://huggingface.co/join)
to get started
Copy page
#  [](https://huggingface.co/docs/bitsandbytes/index#bitsandbytes) bitsandbytes
bitsandbytes enables accessible large language models via k-bit quantization for PyTorch. bitsandbytes provides three main features for dramatically reducing memory consumption for inference and training:
  * 8-bit optimizers uses block-wise quantization to maintain 32-bit performance at a small fraction of the memory cost.
  * LLM.int8() or 8-bit quantization enables large language model inference with only half the required memory and without any performance degradation. This method is based on vector-wise quantization to quantize most features to 8-bits and separately treating outliers with 16-bit matrix multiplication.
  * QLoRA or 4-bit quantization enables large language model training with several memory-saving techniques that don’t compromise performance. This method quantizes a model to 4-bits and inserts a small set of trainable low-rank adaptation (LoRA) weights to allow training.


#  [](https://huggingface.co/docs/bitsandbytes/index#license) License
bitsandbytes is MIT licensed.
[Installation→](https://huggingface.co/docs/bitsandbytes/installation)
[bitsandbytes](https://huggingface.co/docs/bitsandbytes/index#bitsandbytes)
