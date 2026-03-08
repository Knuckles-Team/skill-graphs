## [Events](https://laravel.com/docs/12.x/ai-sdk#events)
The Laravel AI SDK dispatches a variety of [events](https://laravel.com/docs/12.x/events), including:
  * `AddingFileToStore`
  * `AgentPrompted`
  * `AgentStreamed`
  * `AudioGenerated`
  * `CreatingStore`
  * `EmbeddingsGenerated`
  * `FileAddedToStore`
  * `FileDeleted`
  * `FileRemovedFromStore`
  * `FileStored`
  * `GeneratingAudio`
  * `GeneratingEmbeddings`
  * `GeneratingImage`
  * `GeneratingTranscription`
  * `ImageGenerated`
  * `InvokingTool`
  * `PromptingAgent`
  * `RemovingFileFromStore`
  * `Reranked`
  * `Reranking`
  * `StoreCreated`
  * `StoringFile`
  * `StreamingAgent`
  * `ToolInvoked`
  * `TranscriptionGenerated`


You can listen to any of these events to log or store AI SDK usage information.
Copy as markdown
  * [ Introduction ](https://laravel.com/docs/12.x/ai-sdk#introduction)
  * [ Installation ](https://laravel.com/docs/12.x/ai-sdk#installation)
    * [ Configuration ](https://laravel.com/docs/12.x/ai-sdk#configuration)
    * [ Custom Base URLs ](https://laravel.com/docs/12.x/ai-sdk#custom-base-urls)
    * [ Provider Support ](https://laravel.com/docs/12.x/ai-sdk#provider-support)
  * [ Agents ](https://laravel.com/docs/12.x/ai-sdk#agents)
    * [ Prompting ](https://laravel.com/docs/12.x/ai-sdk#prompting)
    * [ Conversation Context ](https://laravel.com/docs/12.x/ai-sdk#conversation-context)
    * [ Structured Output ](https://laravel.com/docs/12.x/ai-sdk#structured-output)
    * [ Attachments ](https://laravel.com/docs/12.x/ai-sdk#attachments)
    * [ Streaming ](https://laravel.com/docs/12.x/ai-sdk#streaming)
    * [ Broadcasting ](https://laravel.com/docs/12.x/ai-sdk#broadcasting)
    * [ Queueing ](https://laravel.com/docs/12.x/ai-sdk#queueing)
    * [ Tools ](https://laravel.com/docs/12.x/ai-sdk#tools)
    * [ Provider Tools ](https://laravel.com/docs/12.x/ai-sdk#provider-tools)
    * [ Middleware ](https://laravel.com/docs/12.x/ai-sdk#middleware)
    * [ Anonymous Agents ](https://laravel.com/docs/12.x/ai-sdk#anonymous-agents)
    * [ Agent Configuration ](https://laravel.com/docs/12.x/ai-sdk#agent-configuration)
  * [ Images ](https://laravel.com/docs/12.x/ai-sdk#images)
  * [ Audio (TTS) ](https://laravel.com/docs/12.x/ai-sdk#audio)
  * [ Transcription (STT) ](https://laravel.com/docs/12.x/ai-sdk#transcription)
  * [ Embeddings ](https://laravel.com/docs/12.x/ai-sdk#embeddings)
    * [ Querying Embeddings ](https://laravel.com/docs/12.x/ai-sdk#querying-embeddings)
    * [ Caching Embeddings ](https://laravel.com/docs/12.x/ai-sdk#caching-embeddings)
  * [ Reranking ](https://laravel.com/docs/12.x/ai-sdk#reranking)
  * [ Files ](https://laravel.com/docs/12.x/ai-sdk#files)
  * [ Vector Stores ](https://laravel.com/docs/12.x/ai-sdk#vector-stores)
    * [ Adding Files to Stores ](https://laravel.com/docs/12.x/ai-sdk#adding-files-to-stores)
  * [ Failover ](https://laravel.com/docs/12.x/ai-sdk#failover)
  * [ Testing ](https://laravel.com/docs/12.x/ai-sdk#testing)
    * [ Agents ](https://laravel.com/docs/12.x/ai-sdk#testing-agents)
    * [ Images ](https://laravel.com/docs/12.x/ai-sdk#testing-images)
    * [ Audio ](https://laravel.com/docs/12.x/ai-sdk#testing-audio)
    * [ Transcriptions ](https://laravel.com/docs/12.x/ai-sdk#testing-transcriptions)
    * [ Embeddings ](https://laravel.com/docs/12.x/ai-sdk#testing-embeddings)
    * [ Reranking ](https://laravel.com/docs/12.x/ai-sdk#testing-reranking)
    * [ Files ](https://laravel.com/docs/12.x/ai-sdk#testing-files)
    * [ Vector Stores ](https://laravel.com/docs/12.x/ai-sdk#testing-vector-stores)
  * [ Events ](https://laravel.com/docs/12.x/ai-sdk#events)


[ ![Laravel Forge](https://laravel.com/images/ads/forge-logo.svg) Server management made simple for any PHP app Learn more  ](https://forge.laravel.com)
[ ![Laravel Cloud](https://laravel.com/images/ads/cloud-logo.svg) The fastest way to deploy and scale Laravel apps Learn more  ](https://cloud.laravel.com)
[ ![Laravel Nightwatch](https://laravel.com/images/ads/nightwatch-logo.svg) First-class monitoring and deep insights for Laravel apps Learn more  ](https://nightwatch.laravel.com)
[ ![Laravel Boost](https://laravel.com/images/ads/boost-logo.svg) Supercharge your AI development with essential context Learn more  ](https://laravel.com/ai/boost)
Laravel is the most productive way to
build, deploy, and monitor software.
  * © 2026 Laravel
  * [ Legal ](https://laravel.com/legal)
  * [ Status ](https://status.laravel.com/)


####  Products
  * [ Cloud ](https://cloud.laravel.com)
  * [ Forge ](https://forge.laravel.com)
  * [ Nightwatch ](https://nightwatch.laravel.com)
  * [ Vapor ](https://vapor.laravel.com)
  * [ Nova ](https://nova.laravel.com)


####  Packages
  * [ Cashier ](https://laravel.com/docs/cashier)
  * [ Dusk ](https://laravel.com/docs/dusk)
  * [ Horizon ](https://laravel.com/docs/horizon)
  * [ Octane ](https://laravel.com/docs/octane)
  * [ Scout ](https://laravel.com/docs/scout)
  * [ Pennant ](https://laravel.com/docs/pennant)
  * [ Pint ](https://laravel.com/docs/pint)
  * [ Sail ](https://laravel.com/docs/sail)
  * [ Sanctum ](https://laravel.com/docs/sanctum)
  * [ Socialite ](https://laravel.com/docs/socialite)
  * [ Telescope ](https://laravel.com/docs/telescope)
  * [ Pulse ](https://laravel.com/docs/pulse)
  * [ Reverb ](https://laravel.com/docs/reverb)
  * [ Echo ](https://laravel.com/docs/broadcasting)


####  Resources
  * [ Documentation ](https://laravel.com/docs)
  * [ Starter Kits ](https://laravel.com/starter-kits)
  * [ Release Notes ](https://laravel.com/docs/releases)
  * [ Blog ](https://laravel.com/blog)
  * [ Community ](https://laravel.com/community)
  * [ Learn ](https://laravel.com/learn)
  * [ Careers ](https://laravel.com/careers)
  * [ Trust ](https://trust.laravel.com)


####  Partners
  *   * [Redberry](https://partners.laravel.com/partners/redberry)
  * [Tighten](https://partners.laravel.com/partners/tighten)
  * [Curotec](https://partners.laravel.com/partners/curotec)
  * [Kirschbaum](https://partners.laravel.com/partners/kirschbaum)
  * [Active Logic](https://partners.laravel.com/partners/active-logic)
  * [byte5](https://partners.laravel.com/partners/byte5)
  * [Vehikl](https://partners.laravel.com/partners/vehikl)
  * [Jump24](https://partners.laravel.com/partners/jump24)
  * [ More Partners ](https://partners.laravel.com)
