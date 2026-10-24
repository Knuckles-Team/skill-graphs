[![Hugging Face's logo](https://huggingface.co/front/assets/huggingface_logo-noborder.svg) Hugging Face](https://huggingface.co/)
  * [](https://huggingface.co/models)
  * [](https://huggingface.co/datasets)
  * [](https://huggingface.co/spaces)
  * [](https://huggingface.co/docs)
  * [](https://huggingface.co/enterprise)
  * [Pricing](https://huggingface.co/pricing)
  * * * *
  * [Log In](https://huggingface.co/login)
  * [Sign Up](https://huggingface.co/join)


Inference Providers documentation
Inference Providers
# Inference Providers
🏡 View all docs AWS Trainium & Inferentia Accelerate Argilla AutoTrain Bitsandbytes Chat UI Dataset viewer Datasets Deploying on AWS Diffusers Distilabel Evaluate Google Cloud Google TPUs Gradio Hub Hub Python Library Huggingface.js Inference Endpoints (dedicated) Inference Providers Kernels LeRobot Leaderboards Lighteval Microsoft Azure Optimum PEFT Reachy Mini Safetensors Sentence Transformers TRL Tasks Text Embeddings Inference Text Generation Inference Tokenizers Trackio Transformers Transformers.js smolagents timm
Search documentation
`Ctrl+K`
main EN
Get Started
[Inference Providers ](https://huggingface.co/docs/inference-providers/index)[Pricing and Billing ](https://huggingface.co/docs/inference-providers/pricing)[Hub integration ](https://huggingface.co/docs/inference-providers/hub-integration)[Security ](https://huggingface.co/docs/inference-providers/security)
Guides
[Your First API Call ](https://huggingface.co/docs/inference-providers/guides/first-api-call)[Building Your First AI App ](https://huggingface.co/docs/inference-providers/guides/building-first-app)[Structured Outputs with LLMs ](https://huggingface.co/docs/inference-providers/guides/structured-output)[Function Calling ](https://huggingface.co/docs/inference-providers/guides/function-calling)[Responses API (beta) ](https://huggingface.co/docs/inference-providers/guides/responses-api)[How to use OpenAI gpt-oss ](https://huggingface.co/docs/inference-providers/guides/gpt-oss)[Build an Image Editor ](https://huggingface.co/docs/inference-providers/guides/image-editor)[Automating Code Review with GitHub Actions ](https://huggingface.co/docs/inference-providers/guides/github-actions-code-review)[Agentic Coding Environments with OpenEnv ](https://huggingface.co/docs/inference-providers/guides/coding-environment)[Evaluating Models with Inspect ](https://huggingface.co/docs/inference-providers/guides/evaluation-inspect-ai)
Integrations
[Overview ](https://huggingface.co/docs/inference-providers/integrations/index)[Add Your Integration ](https://huggingface.co/docs/inference-providers/integrations/adding-integration)[NeMo Data Designer ](https://huggingface.co/docs/inference-providers/integrations/datadesigner)[MacWhisper ](https://huggingface.co/docs/inference-providers/integrations/macwhisper)[OpenCode ](https://huggingface.co/docs/inference-providers/integrations/opencode)[Pi ](https://huggingface.co/docs/inference-providers/integrations/pi)[Vision Agents ](https://huggingface.co/docs/inference-providers/integrations/visionagents)[VS Code with GitHub Copilot ](https://huggingface.co/docs/inference-providers/integrations/vscode)
Inference Tasks
[Chat Completion ](https://huggingface.co/docs/inference-providers/tasks/chat-completion)[Feature Extraction ](https://huggingface.co/docs/inference-providers/tasks/feature-extraction)[Text to Image ](https://huggingface.co/docs/inference-providers/tasks/text-to-image)[Text to Video ](https://huggingface.co/docs/inference-providers/tasks/text-to-video)
Other Tasks
Providers
[Cerebras ](https://huggingface.co/docs/inference-providers/providers/cerebras)[Cohere ](https://huggingface.co/docs/inference-providers/providers/cohere)[Fal AI ](https://huggingface.co/docs/inference-providers/providers/fal-ai)[Featherless AI ](https://huggingface.co/docs/inference-providers/providers/featherless-ai)[Fireworks ](https://huggingface.co/docs/inference-providers/providers/fireworks-ai)[Groq ](https://huggingface.co/docs/inference-providers/providers/groq)[Hyperbolic ](https://huggingface.co/docs/inference-providers/providers/hyperbolic)[HF Inference ](https://huggingface.co/docs/inference-providers/providers/hf-inference)[Novita ](https://huggingface.co/docs/inference-providers/providers/novita)[Nscale ](https://huggingface.co/docs/inference-providers/providers/nscale)[OVHcloud AI Endpoints ](https://huggingface.co/docs/inference-providers/providers/ovhcloud)[Public AI ](https://huggingface.co/docs/inference-providers/providers/publicai)[Replicate ](https://huggingface.co/docs/inference-providers/providers/replicate)[SambaNova ](https://huggingface.co/docs/inference-providers/providers/sambanova)[Scaleway ](https://huggingface.co/docs/inference-providers/providers/scaleway)[Together ](https://huggingface.co/docs/inference-providers/providers/together)[WaveSpeedAI ](https://huggingface.co/docs/inference-providers/providers/wavespeed)[Z.ai ](https://huggingface.co/docs/inference-providers/providers/zai-org)
[Hub API ](https://huggingface.co/docs/inference-providers/hub-api)[Register as an Inference Provider ](https://huggingface.co/docs/inference-providers/register-as-a-provider)
![Hugging Face's logo](https://huggingface.co/front/assets/huggingface_logo-noborder.svg)
Join the Hugging Face community
and get access to the augmented documentation experience
Collaborate on models, datasets and Spaces
Faster examples with accelerated inference
Switch between documentation themes
[Sign Up](https://huggingface.co/join)
to get started
Copy page
#  [](https://huggingface.co/docs/inference-providers/index#inference-providers) Inference Providers
![](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/inference-providers/Inference-providers-banner-light.png) ![](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/inference-providers/Inference-providers-banner-dark.png)
Hugging Face’s Inference Providers give developers access to hundreds of machine learning models, powered by world-class inference providers. They are also integrated into our client SDKs (for JS and Python), making it easy to explore serverless inference of models on your favorite providers.
##  [](https://huggingface.co/docs/inference-providers/index#partners) Partners
Our platform integrates with leading AI infrastructure providers, giving you access to their specialized capabilities through a single, consistent API. Here’s what each partner supports:
Provider | Chat completion (LLM) | Chat completion (VLM) | Feature Extraction | Text to Image | Text to video | Speech to text
---|---|---|---|---|---|---
[Cerebras](https://huggingface.co/docs/inference-providers/providers/cerebras) | ✅ |  |  |  |  |
[Cohere](https://huggingface.co/docs/inference-providers/providers/cohere) | ✅ | ✅ |  |  |  |
[Fal AI](https://huggingface.co/docs/inference-providers/providers/fal-ai) |  |  |  | ✅ | ✅ | ✅
[Featherless AI](https://huggingface.co/docs/inference-providers/providers/featherless-ai) | ✅ | ✅ |  |  |  |
[Fireworks](https://huggingface.co/docs/inference-providers/providers/fireworks-ai) | ✅ | ✅ |  |  |  |
[Groq](https://huggingface.co/docs/inference-providers/providers/groq) | ✅ | ✅ |  |  |  |
[HF Inference](https://huggingface.co/docs/inference-providers/providers/hf-inference) | ✅ | ✅ | ✅ | ✅ |  | ✅
[Hyperbolic](https://huggingface.co/docs/inference-providers/providers/hyperbolic) | ✅ | ✅ |  |  |  |
[Novita](https://huggingface.co/docs/inference-providers/providers/novita) | ✅ | ✅ |  |  | ✅ |
[Nscale](https://huggingface.co/docs/inference-providers/providers/nscale) | ✅ | ✅ |  | ✅ |  |
[OVHcloud AI Endpoints](https://huggingface.co/docs/inference-providers/providers/ovhcloud) | ✅ | ✅ |  |  |  |
[Public AI](https://huggingface.co/docs/inference-providers/providers/publicai) | ✅ |  |  |  |  |
[Replicate](https://huggingface.co/docs/inference-providers/providers/replicate) |  |  |  | ✅ | ✅ | ✅
[SambaNova](https://huggingface.co/docs/inference-providers/providers/sambanova) | ✅ |  | ✅ |  |  |
[Scaleway](https://huggingface.co/docs/inference-providers/providers/scaleway) | ✅ |  | ✅ |  |  |
[Together](https://huggingface.co/docs/inference-providers/providers/together) | ✅ | ✅ |  | ✅ |  |
[WaveSpeedAI](https://huggingface.co/docs/inference-providers/providers/wavespeed) |  |  |  | ✅ | ✅ |
[Z.ai](https://huggingface.co/docs/inference-providers/providers/zai-org) | ✅ | ✅ |  |  |  |
##  [](https://huggingface.co/docs/inference-providers/index#why-choose-inference-providers) Why Choose Inference Providers?
When you build AI applications, it’s tough to manage multiple provider APIs, comparing model performance, and dealing with varying reliability. Inference Providers solves these challenges by offering:
**Instant Access to Cutting-Edge Models** : Go beyond mainstream providers to access thousands of specialized models across multiple AI tasks. Whether you need the latest language models, state-of-the-art image generators, or domain-specific embeddings, you’ll find them here.
**Zero Vendor Lock-in** : Unlike being tied to a single provider’s model catalog, you get access to models from Cerebras, Groq, Together AI, Replicate, and more — all through one consistent interface.
**Production-Ready Performance** : Built for enterprise workloads with the reliability your applications demand.
Here’s what you can build:
  * **Text Generation** : Use Large language models with tool-calling capabilities for chatbots, content generation, and code assistance
  * **Image and Video Generation** : Create custom images and videos, including support for LoRAs and style customization
  * **Search & Retrieval**: State-of-the-art embeddings for semantic search, RAG systems, and recommendation engines
  * **Traditional ML Tasks** : Ready-to-use models for classification, NER, summarization, and speech recognition


⚡ **Get Started for Free** : Inference Providers includes a generous free tier, with additional credits for [Team & Enterprise organizations](https://huggingface.co/enterprise).
##  [](https://huggingface.co/docs/inference-providers/index#key-features) Key Features
  * **🎯 All-in-One API** : A single API for text generation, image generation, document embeddings, NER, summarization, image classification, and more.
  * **🔀 Multi-Provider Support** : Easily run models from top-tier providers like fal, Replicate, Sambanova, Together AI, and others.
  * **🚀 Scalable & Reliable**: Built for high availability and low-latency performance in production environments.
  * **🔧 Developer-Friendly** : Simple requests, fast responses, and a consistent developer experience across Python and JavaScript clients.
  * **👷 Easy to integrate** : Drop-in replacement for the OpenAI chat completions API.
  * **💰 Cost-Effective** : No extra markup on provider rates.


##  [](https://huggingface.co/docs/inference-providers/index#getting-started) Getting Started
Inference Providers works with your existing development workflow. Whether you prefer Python, JavaScript, or direct HTTP calls, we provide native SDKs and OpenAI-compatible APIs to get you up and running quickly.
We’ll walk through a practical example using [openai/gpt-oss-120b](https://huggingface.co/openai/gpt-oss-120b), a state-of-the-art open-weights conversational model.
###  [](https://huggingface.co/docs/inference-providers/index#inference-playground) Inference Playground
Before diving into integration, explore models interactively with our [Inference Playground](https://huggingface.co/playground). Test different [chat completion models](http://huggingface.co/models?inference_provider=all&sort=trending&other=conversational) with your prompts and compare responses to find the perfect fit for your use case.
[![Inference Playground thumbnail](https://cdn-uploads.huggingface.co/production/uploads/5f17f0a0925b9863e28ad517/9_Tgf0Tv65srhBirZQMTp.png)](https://huggingface.co/playground)
###  [](https://huggingface.co/docs/inference-providers/index#authentication) Authentication
You’ll need a Hugging Face token to authenticate your requests. Create one by visiting your [token settings](https://huggingface.co/settings/tokens/new?ownUserPermissions=inference.serverless.write&tokenType=fineGrained) and generating a `fine-grained` token with `Make calls to Inference Providers` permissions.
For complete token management details, see our [security tokens guide](https://huggingface.co/docs/hub/en/security-tokens).
###  [](https://huggingface.co/docs/inference-providers/index#quick-start---llm) Quick Start - LLM
Let’s start with the most common use case: conversational AI using large language models. This section demonstrates how to perform chat completions using DeepSeek V3, showcasing the different ways you can integrate Inference Providers into your applications.
Whether you prefer our native clients, want OpenAI compatibility, or need direct HTTP access, we’ll show you how to get up and running with just a few lines of code.
####  [](https://huggingface.co/docs/inference-providers/index#python) Python
Here are three ways to integrate Inference Providers into your Python applications, from high-level convenience to low-level control:
huggingface_hub
openai
requests
For convenience, the `huggingface_hub` library provides an [`InferenceClient`](https://huggingface.co/docs/huggingface_hub/guides/inference) that automatically handles provider selection and request routing.
In your terminal, install the Hugging Face Hub Python client and log in:
```
pip install huggingface_hub
hf auth login # get a read token from hf.co/settings/tokens
```

You can now use the client with a Python interpreter.
By default, our system automatically selects the fastest available provider for the specified model (equivalent to the `:fastest` policy — highest throughput in tokens per second).
You can change the provider selection policy by appending a policy suffix to the model id: `:cheapest` for the most cost-efficient provider (lowest price per output token), or `:preferred` to follow your preference order in `openai/gpt-oss-120b:cheapest`.
You can also select the provider of your choice by appending the provider name to the model id (e.g. `"openai/gpt-oss-120b:sambanova"`).
```
import os
from huggingface_hub import InferenceClient

client = InferenceClient()

completion = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {
            "role": "user",
            "content": "How many 'G's in 'huggingface'?"
        }
    ],
)

print(completion.choices[0].message)
```

####  [](https://huggingface.co/docs/inference-providers/index#javascript) JavaScript
Integrate Inference Providers into your JavaScript applications with these flexible approaches:
huggingface.js
openai
fetch
Our JavaScript SDK provides a convenient interface with automatic provider selection and TypeScript support.
Install with NPM:
```
npm install @huggingface/inference
```

Then use the client with Javascript.
By default, our system automatically selects the fastest available provider for the specified model (equivalent to the `:fastest` policy — highest throughput in tokens per second).
You can change the provider selection policy by appending a policy suffix to the model id: `:cheapest` for the most cost-efficient provider (lowest price per output token), or `:preferred` to follow your preference order in `openai/gpt-oss-120b:cheapest`.
You can also select the provider of your choice by appending the provider name to the model id (e.g. `"openai/gpt-oss-120b:sambanova"`).
```
import { InferenceClient } from "@huggingface/inference";

const client = new InferenceClient(process.env.HF_TOKEN);

const chatCompletion = await client.chatCompletion({
  model: "openai/gpt-oss-120b:fastest",
  messages: [
    {
      role: "user",
      content: "How many 'G's in 'huggingface'?",
    },
  ],
});

console.log(chatCompletion.choices[0].message);
```

####  [](https://huggingface.co/docs/inference-providers/index#http--curl) HTTP / cURL
For testing, debugging, or integrating with any HTTP client, here’s the raw REST API format.
By default, our system automatically selects the fastest available provider for the specified model (equivalent to the `:fastest` policy — highest throughput in tokens per second).
You can change the provider selection policy by appending a policy suffix to the model id: `:cheapest` for the most cost-efficient provider (lowest price per output token), or `:preferred` to follow your preference order in `openai/gpt-oss-120b:cheapest`.
You can also select the provider of your choice by appending the provider name to the model id (e.g. `"openai/gpt-oss-120b:sambanova"`).
```
curl https://router.huggingface.co/v1/chat/completions \
    -H "Authorization: Bearer $HF_TOKEN" \
    -H 'Content-Type: application/json' \
    -d '{
        "messages": [
            {
                "role": "user",
                "content": "How many G in huggingface?"
            }
        ],
        "model": "openai/gpt-oss-120b:fastest",
        "stream": false
    }'
```

###  [](https://huggingface.co/docs/inference-providers/index#quick-start---text-to-image-generation) Quick Start - Text-to-Image Generation
Let’s explore how to generate images from text prompts using Inference Providers. We’ll use [black-forest-labs/FLUX.1-dev](https://huggingface.co/black-forest-labs/FLUX.1-dev), a state-of-the-art diffusion model that produces highly detailed, photorealistic images.
####  [](https://huggingface.co/docs/inference-providers/index#python) Python
Use the `huggingface_hub` library for the simplest image generation experience with automatic provider selection:
```
import os
from huggingface_hub import InferenceClient

client = InferenceClient(api_key=os.environ["HF_TOKEN"])

image = client.text_to_image(
    prompt="A serene lake surrounded by mountains at sunset, photorealistic style",
    model="black-forest-labs/FLUX.1-dev"
)

# Save the generated image
image.save("generated_image.png")
```

####  [](https://huggingface.co/docs/inference-providers/index#javascript) JavaScript
Use our JavaScript SDK for streamlined image generation with TypeScript support:
```
import { InferenceClient } from "@huggingface/inference";
import fs from "fs";

const client = new InferenceClient(process.env.HF_TOKEN);

const imageBlob = await client.textToImage({
  model: "black-forest-labs/FLUX.1-dev",
  inputs:
    "A serene lake surrounded by mountains at sunset, photorealistic style",
});

// Save the image
const buffer = Buffer.from(await imageBlob.arrayBuffer());
fs.writeFileSync("generated_image.png", buffer);
```

##  [](https://huggingface.co/docs/inference-providers/index#provider-selection) Provider Selection
The Inference Providers API acts as a unified proxy layer that sits between your application and multiple AI providers. Understanding how provider selection works is crucial for optimizing performance, cost, and reliability in your applications.
###  [](https://huggingface.co/docs/inference-providers/index#api-as-a-proxy-service) API as a Proxy Service
When using Inference Providers, your requests go through Hugging Face’s proxy infrastructure, which provides several key benefits:
  * **Unified Authentication & Billing**: Use a single Hugging Face token for all providers
  * **Automatic Failover** : When using automatic provider selection (`provider="auto"`), requests are automatically routed to alternative providers if the primary provider is flagged as unavailable by our validation system
  * **Consistent Interface through client libraries** : When using our client libraries, the same request format works across different providers


Because the API acts as a proxy, the exact HTTP request may vary between providers as each provider has their own API requirements and response formats. **When using our official client libraries** (JavaScript or Python), these provider-specific differences are handled automatically whether you use `provider="auto"` or specify a particular provider.
###  [](https://huggingface.co/docs/inference-providers/index#client-side-provider-selection-inference-clients) Client-Side Provider Selection (Inference Clients)
When using the Hugging Face inference clients (JavaScript or Python), you can explicitly specify a provider or let the system choose automatically. The client then formats the HTTP request to match the selected provider’s API requirements.
javascript
python
```
import { InferenceClient } from "@huggingface/inference";

const client = new InferenceClient(process.env.HF_TOKEN);

// Explicit provider selection
await client.chatCompletion({
  model: "deepseek-ai/DeepSeek-R1",
  provider: "sambanova", // Specific provider
  messages: [{ role: "user", content: "Hello!" }],
});

// Automatic provider selection (default: "auto")
await client.chatCompletion({
  model: "deepseek-ai/DeepSeek-R1",
  // Defaults to "auto" selection of the provider
  // provider="auto",
  messages: [{ role: "user", content: "Hello!" }],
});
```

**Provider Selection Policy:**
  * `provider: "auto"` (default): Selects the first available provider for the model, sorted by your preference order in
  * `provider: "specific-provider"`: Forces use of a specific provider (e.g., “together”, “replicate”, “fal-ai”, …).


###  [](https://huggingface.co/docs/inference-providers/index#alternative-openai-compatible-chat-completions-endpoint-chat-only) Alternative: OpenAI-Compatible Chat Completions Endpoint (Chat Only)
If you prefer to work with familiar OpenAI APIs or want to migrate existing chat completion code with minimal changes, we offer a drop-in compatible endpoint that handles all provider selection automatically on the server side.
By default, the fastest available provider is selected for the model (highest throughput in tokens per second). This is equivalent to appending `:fastest` to the model name. You can change that policy by adding a suffix to the model name:
  * `:cheapest` selects the most cost-efficient provider for the model (lowest price per output tokens)
  * `:preferred` selects the first available provider sorted by your preference order in


**Note** : This OpenAI-compatible endpoint is currently available for chat completion tasks only. For other tasks like text-to-image, embeddings, or speech processing, use the Hugging Face inference clients shown above.
javascript
python
```
import { OpenAI } from "openai";

const client = new OpenAI({
  baseURL: "https://router.huggingface.co/v1",
  apiKey: process.env.HF_TOKEN,
});

const completion = await client.chat.completions.create({
  model: "deepseek-ai/DeepSeek-R1:fastest",
  messages: [{ role: "user", content: "Hello!" }],
});
```

This endpoint can also be requested through direct HTTP access, making it suitable for integration with various HTTP clients and applications that need to interact with the chat completion service directly.
```
curl https://router.huggingface.co/v1/chat/completions \
  -H "Authorization: Bearer $HF_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "deepseek-ai/DeepSeek-R1:fastest",
    "messages": [
      {
        "role": "user",
        "content": "Hello!"
      }
    ]
  }'
```

**Key Features:**
  * **Server-Side Provider Selection** : The server automatically selects the fastest available provider by default (`:fastest` policy)
  * **Model Listing** : GET `/v1/models` returns available models across all providers
  * **OpenAI SDK Compatibility** : Works with existing OpenAI client libraries
  * **Chat Tasks Only** : Limited to conversational workloads


###  [](https://huggingface.co/docs/inference-providers/index#choosing-the-right-approach) Choosing the Right Approach
**Use Inference Clients when:**
  * You need support for all task types (text-to-image, speech, embeddings, etc.)
  * You want explicit control over provider selection
  * You’re building applications that use multiple AI tasks


**Use OpenAI-Compatible Endpoint when:**
  * You’re only doing chat completions
  * You want to migrate existing OpenAI-based code with minimal changes
  * You prefer server-side provider management


**Use Direct HTTP when:**
  * You’re implementing custom request logic
  * You need fine-grained control over the request/response cycle
  * You’re working in environments without available client libraries


##  [](https://huggingface.co/docs/inference-providers/index#next-steps) Next Steps
Now that you understand the basics, explore these resources to make the most of Inference Providers:
  * **[Announcement Blog Post](https://huggingface.co/blog/inference-providers)** : Learn more about the launch of Inference Providers
  * **[Pricing and Billing](https://huggingface.co/docs/inference-providers/pricing)** : Understand costs and billing of Inference Providers
  * **[Hub Integration](https://huggingface.co/docs/inference-providers/hub-integration)** : Learn how Inference Providers are integrated with the Hugging Face Hub
  * **[Register as a Provider](https://huggingface.co/docs/inference-providers/register-as-a-provider)** : Requirements to join our partner network as a provider
  * **[Hub API](https://huggingface.co/docs/inference-providers/hub-api)** : Advanced API features and configuration
  * **[API Reference](https://huggingface.co/docs/inference-providers/tasks/index)** : Complete parameter documentation for all supported tasks


[Pricing and Billing→](https://huggingface.co/docs/inference-providers/pricing)
[Inference Providers](https://huggingface.co/docs/inference-providers/index#inference-providers)[Partners](https://huggingface.co/docs/inference-providers/index#partners)[Why Choose Inference Providers?](https://huggingface.co/docs/inference-providers/index#why-choose-inference-providers)[Key Features](https://huggingface.co/docs/inference-providers/index#key-features)[Getting Started](https://huggingface.co/docs/inference-providers/index#getting-started)[Inference Playground](https://huggingface.co/docs/inference-providers/index#inference-playground)[Authentication](https://huggingface.co/docs/inference-providers/index#authentication)[Quick Start - LLM](https://huggingface.co/docs/inference-providers/index#quick-start---llm)[Python](https://huggingface.co/docs/inference-providers/index#python)[JavaScript](https://huggingface.co/docs/inference-providers/index#javascript)[HTTP / cURL](https://huggingface.co/docs/inference-providers/index#http--curl)[Quick Start - Text-to-Image Generation](https://huggingface.co/docs/inference-providers/index#quick-start---text-to-image-generation)[Python](https://huggingface.co/docs/inference-providers/index#python)[JavaScript](https://huggingface.co/docs/inference-providers/index#javascript)[Provider Selection](https://huggingface.co/docs/inference-providers/index#provider-selection)[API as a Proxy Service](https://huggingface.co/docs/inference-providers/index#api-as-a-proxy-service)[Client-Side Provider Selection (Inference Clients)](https://huggingface.co/docs/inference-providers/index#client-side-provider-selection-inference-clients)[Alternative: OpenAI-Compatible Chat Completions Endpoint (Chat Only)](https://huggingface.co/docs/inference-providers/index#alternative-openai-compatible-chat-completions-endpoint-chat-only)[Choosing the Right Approach](https://huggingface.co/docs/inference-providers/index#choosing-the-right-approach)[Next Steps](https://huggingface.co/docs/inference-providers/index#next-steps)
