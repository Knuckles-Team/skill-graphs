##  [Verified bots](https://vercel.com/docs/bot-management#verified-bots)[](https://vercel.com/docs/bot-management#verified-bots)
Vercel maintains and continuously updates a comprehensive directory of known legitimate bots from across the internet. This directory is regularly updated to include new legitimate services as they emerge. [Attack Challenge Mode](https://vercel.com/docs/vercel-firewall/attack-challenge-mode#known-bots-support) and bot protection automatically recognize and allow these bots to pass through without being challenged. You can block access to some or all of these bots by writing [WAF custom rules](https://vercel.com/docs/vercel-firewall/vercel-waf/custom-rules) with the User Agent match condition or Signature-Agent header. To learn how to do this, review [WAF Examples](https://vercel.com/docs/vercel-firewall/vercel-waf/examples).
###  [Bot verification methods](https://vercel.com/docs/bot-management#bot-verification-methods)[](https://vercel.com/docs/bot-management#bot-verification-methods)
To prove that bots are legitimate and verify their claimed identity, several methods are used:
  * IP Address Verification: Checking if requests originate from known IP ranges owned by legitimate bot operators (e.g., Google's Googlebot, Bing's crawler).
  * Reverse DNS Lookup: Performing reverse DNS queries to verify that an IP address resolves back to the expected domain (e.g., an IP claiming to be Googlebot should resolve to `*.googlebot.com` or `*.google.com`).
  * Cryptographic Verification: Using digital signatures to authenticate bot requests through protocols like


###  [Verified bots directory](https://vercel.com/docs/bot-management#verified-bots-directory)[](https://vercel.com/docs/bot-management#verified-bots-directory)
Bot name | Category | Description | Documentation
---|---|---|---
adagiobot | advertising | Adagiobot is a web crawler that analyzes websites for advertising demand optimization, helping publishers maximize revenue through real-time bidding analysis and performance insights. AdagioBot fetches /ads.txt, /app-ads.txt and /sellers.json files to comply with IAB Supply Chain Validation. |
adidxbot | advertising | AdIdxBot is the crawler used by Bing Ads for quality control of ads and their destination websites. It has multiple user agent variants including desktop, iPhone, and Windows Phone versions. |
adsense | advertising | The AdSense crawler visits participating sites in order to provide them with relevant ads. |
adyen-webhook | webhook | Adyen’s webhooks (Notification API) send encrypted, real-time HTTP callbacks for key payment and account events—automating order fulfillment, settlement reconciliation, and risk-management workflows. |
ahrefsbot | search_engine_optimization | Powers the database for both Ahrefs, a marketing intelligence platform, and Yep, an independent, privacy-focused search engine. |
ahrefssiteaudit | search_engine_optimization | Powers Ahrefs’ Site Audit tool. Ahrefs users can use Site Audit to analyze websites and find both technical SEO and on-page SEO issues. |
algolia | search_engine_crawler | The Algolia Crawler extracts content from your site and makes it searchable. |
amazon-adbot | advertising | Amazon AdBot is a crawler used by different advertising services at Amazon to determine a website's content in order to provide relevant and appropriate advertising. Amazon AdBot only crawls websites for which Amazon or an advertiser partner may serve an ad. |
amazon-kendra | ai_assistant | Amazon Kendra is a managed information retrieval and intelligent search service that uses natural language processing and advanced deep learning model. |
amazon-q | ai_assistant | Amazon Q Business is a generative artificial intelligence (generative AI)-powered assistant that you can tailor to your business needs. |
amazonbot | ai_crawler | Amazonbot is Amazon's web crawler used to improve our services, such as enabling Alexa to more accurately answer questions for customers. |
apis-google | search_engine_crawler | Crawling preferences addressed to the APIs-Google user agent affect the delivery of push notification messages by Google APIs. |
apple-podcasts | feed_fetcher | Apple Podcasts crawler that only accesses URLs associated with registered content on Apple Podcasts. Does not follow robots.txt. |
applebot | ai_crawler | Applebot powers search features in Apple's ecosystem (Spotlight, Siri, Safari) and may be used to train Apple's foundation models for generative AI features. |
artemis-web-crawler | feed_fetcher | Artemis is a calm web reader with which you can follow websites and blogs. |
atlassian-jira-webhooks | webhook | Delivers webhook notifications from Jira Cloud when issues, projects, or other resources change. |
rovo | ai_crawler | Crawls and indexes web content for Atlassian Rovo's AI-powered search, chat, and agents. |
baiduspider | search_engine_crawler | Baiduspider is Baidu’s web crawler that indexes websites for inclusion in its Chinese-market search results. |
barkrowler | search_engine_optimization | Barkrowler is Babbar's web crawler that fuels and updates their graph representation of the web, providing SEO tools for the marketing community. |
better-stack | monitor | Better Stack is a platform for monitoring and alerting on your applications. |
bingbot | search_engine_crawler | Bingbot is Microsoft's web crawler used for indexing websites for Bing Search. |
brightbot | monitor | Brightbot is Bright Data's crawler layer that monitors the health of websites and enforces ethical web data collection. It prevents access to non-public information and blocks interactive endpoints that could be abused, acting as a guardian for ethical data collection. |
browserbase | ai_crawler | Runs headless browser automation on behalf of Browserbase customers for web scraping, form submission, and testing. |
buffer-link-preview-bot | preview | Helps Buffer users create better social media posts by generating rich previews when they share links |
ccbot | ai_crawler | CCBot is operated by the Common Crawl Foundation to crawl web content for AI training and research. Common Crawl is a non-profit organization that maintains an open repository of web crawl data that is universally accessible for research and analysis. |
channel3bot | ecommerce | Crawls product detail pages to index content for AI-powered product discovery, routing shoppers to original websites. |
chatgpt-operator | ai_assistant | Handles user-initiated requests from ChatGPT operator accessing external content; not used for automated crawling or AI training. |
chatgpt-user | ai_assistant | Handles user-initiated requests in ChatGPT, accessing external content to provide real-time information; not used for automated crawling or AI training. |
checkly | monitor | Checkly is a platform for monitoring and alerting on your applications. |
chrome-lighthouse | analytics | PageSpeed Insights (PSI) reports on the user experience of a page on both mobile and desktop devices, and provides suggestions on how that page may be improved. |
chrome-privacy-preserving-prefetch-proxy | preview | Chrome's Privacy Preserving Prefetch Proxy service that fetches /.well-known/traffic-advice to enable privacy-preserving prefetch hints. |
claude-searchbot | ai_assistant | Claude-SearchBot navigates the web to improve search result quality for users. It analyzes online content specifically to enhance the relevance and accuracy of search responses. |
claude-user | ai_assistant | Claude-User supports Claude AI users. When individuals ask questions to Claude, it may access websites using a Claude-User agent. |
claudebot | ai_crawler | ClaudeBot helps enhance the utility and safety of our generative AI models by collecting web content that could potentially contribute to their training. |
cookiebot | monitor | Cookiebot automates compliance with cookie laws and helps you manage your cookie consent preferences. |
criteobot | advertising | CriteoBot is a crawler operated by Criteo that analyzes web content to serve relevant contextual ads. The bot respects robots.txt directives and crawl delays, and only accesses publicly available content. |
customerio-webhooks | webhook | Customer.io's webhook service for event-driven marketing automation and customer data platform. |
cybaa-agent | verification | Performs user-initiated security checks on behalf of Cybaa customers, validating security headers, TLS/SSL configuration, and other domain-specific security controls to ensure website compliance and protection. |
dash0-synthetic | monitor | Dash0's Synthetic Monitoring provides proactive, automated insights into the availability and performance of your websites and APIs. |
datadog-synthetic-monitoring-robot | monitor | Datadog's automated monitoring service that performs synthetic tests to verify website availability and performance. |
dataforseobot | search_engine_optimization | DataForSeoBot is a backlink checker bot operated by DataForSEO that crawls websites to build and maintain their backlink database. The bot respects robots.txt directives and crawl delays, and is used to provide SEO data and analytics services. |
detectify | monitor | Detectify is a web security scanner that performs automated security tests on web applications and attack surface monitoring. |
duckassistbot | ai_assistant | DuckAssistBot is a web crawler for DuckDuckGo Search that crawls pages in real-time for AI-assisted answers, which prominently cite their sources. This data is not used in any way to train AI models. |
duckduckbot | search_engine_crawler | DuckDuckBot is a web crawler for DuckDuckGo. DuckDuckBot’s job is to constantly improve search results and offer users the best and most secure search experience possible. |
facebook-webhooks | webhook | Facebook's webhook service that delivers real-time event notifications for Meta platform events and changes. |
facebookexternalhit | preview | Fetches content for shared links on Meta platforms to generate rich previews. |
falbot | webhook | fal.ai's webhook service that delivers asynchronous notifications for AI model processing and generation tasks. |
geedoproductsearchbot | ecommerce | GeedoProductSearch is a web crawler operated by Geedo SIA that indexes product information from e-commerce websites. The crawler respects robots.txt directives and can be configured for crawl speed and behavior through standard crawl-delay settings. |
gemini-deep-research | ai_assistant | Gemini Deep Research is Google's AI-powered research tool that performs comprehensive multi-step research on complex topics, analyzing web content to provide detailed insights and answers. |
github-camo | preview | GitHub's image proxy service |
github-hookshot | webhook | GitHub's webhooks for events like push, pull request, etc. |
google-admob-reward-verification | webhook | Sends server-side verification callbacks to confirm users completed rewarded ad views. |
google-ads-creatives-assistant | ai_assistant | Fetches website content for Google Ads creative generation and enhancement tools. |
google-adsbot | advertising | Google AdsBot is Google's web crawler for quality control of Google Ads. |
google-adwords-instant | advertising | Fetches advertiser landing pages when triggered by user actions in the Google Ads platform. |
google-association-service | verification | Verifies associations between apps and websites for Digital Asset Links. |
google-businesslink-verification | verification | Verifies that business links in Google Business Profile are accessible and return valid HTTP status codes. |
google-cloudvertexbot | ai_assistant | Crawling preferences addressed to the Google-CloudVertexBot user agent affect crawls requested by the site owners' for building Vertex AI Agents. It has no effect on Google Search or other products. |
google-display-ads-bot | advertising | Verifies site eligibility during the AdSense approval process. |
google-docs | preview | Fetches images and page content when users insert links into Google Docs. |
google-extended | ai_crawler | Google-Extended is a standalone product token that web publishers can use to manage whether their sites help improve Gemini Apps and Vertex AI generative APIs, including future generations of models that power those products. Grounding with Google Search on Vertex AI does not use web pages for grounding that have disallowed Google-Extended. Google-Extended does not impact a site's inclusion or ranking in Google Search. |
google-feedfetcher | feed_fetcher | Feedfetcher is used for crawling RSS or Atom feeds for Google News and PubSubHubbub. |
google-image-proxy | preview | Google's image caching proxy service used by Gmail and other Google services to cache and serve images. |
google-inspectiontool | monitor | Crawling preferences addressed to the Google-InspectionTool user agent affect Search testing tools such as the Rich Result Test and URL inspection in Search Console. It has no effect on Google Search or other products. |
google-pagerenderer | preview | Upon user request, Google Page Renderer fetches and renders web pages. |
google-publisher-center | feed_fetcher | Google Publisher Center fetches and processes feeds that publishers explicitly supplied for use in Google News landing pages. |
google-read-aloud | accessibility | Upon user request, Google Read Aloud fetches and reads out web pages using text-to-speech (TTS). |
google-safety | monitor | The Google-Safety user agent handles abuse-specific crawling, such as malware discovery for publicly posted links on Google properties. As such it's unaffected by crawling preferences. |
google-site-verifier | verification | Google Site Verifier fetches Search Console verification tokens. |
google-storebot | ecommerce | Crawling preferences addressed to the Storebot-Google user agent affect all surfaces of Google Shopping (for example, the Shopping tab in Google Search and Google Shopping). |
googlebot | search_engine_crawler | Crawling preferences addressed to the Googlebot user agent affect Google Search (including Discover and all Google Search features), as well as other products such as Google Images, Google Video, Google News, and Discover. |
googleother | search_engine_crawler | Crawling preferences addressed to the GoogleOther user agent don't affect any specific product. GoogleOther is the generic crawler that may be used by various product teams for fetching publicly accessible content from sites. For example, it may be used for one-off crawls for internal research and development. It has no effect on Google Search or other products. |
gpt-actions | ai_assistant | Enables ChatGPT to interact with external APIs and retrieve real-time information from the web in response to user-initiated requests; allows access to up-to-date content without being used for automated crawling or AI training. |
gptbot | ai_crawler | Crawls web content to improve OpenAI's generative AI models and ChatGPT; respects 'robots.txt' directives to exclude sites from training data. |
gtmetrix | monitor | GTmetrix provides metrics and insights for your site's loading speed and performance. |
hetrixtools-uptime-monitoring-bot | monitor | HetrixTools Uptime Monitoring Bot is used by HetrixTools's monitoring services to perform various checks on websites, including uptime and performance monitoring. |
hookdeck | webhook | A reliable Event Gateway for event-driven applications |
hydrozen | monitor | Hydrozen is a tool for monitoring availability of your websites, Cronjobs, APIs, Domains, SSL etc. |
iframely | preview | Fetches your page metadata to generate rich link previews when users share your links across apps, blogs, and news sites, enhancing content visibility and engagement. |
imagesiftbot | ai_crawler | ImageSiftBot is a web crawler that scrapes the internet for publicly available images to support Hive's suite of web intelligence products. |
inngest | webhook | Inngest is a platform for building event-driven applications. |
jobswithgpt | search_engine_crawler | Crawls job-related pages to power jobswithgpt.com, a platform for discovering AI-enhanced career opportunities. |
kernel | ai_crawler | Runs browser automation on behalf of Kernel customers for web agents, automations, and web scraping. |
linkedinbot | preview | LinkedInBot is a bot that renders links shared on LinkedIn. |
logicmonitor | monitor | LogicMonitor SiteMonitor monitors your website's uptime, performance, and availability from multiple global regions. |
lumar | search_engine_optimization | The Lumar website intelligence platform is used by SEO, engineering, marketing and digital operations teams to monitor the performance of their site’s technical health, and ensure a high-performing, revenue-driving website. |
marfeel-audits | monitor | Marfeel's audit crawlers that periodically re-crawl traffic-receiving URLs to detect structured data, meta tags, and HTML issues. |
marfeel-flowcards | preview | Marfeel's crawler that fetches content for Flowcards that load directly from specific URLs. |
marfeel-preview | preview | Marfeel's previewer crawler used to render preview experiences for both mobile and desktop views. |
marfeel-social | social_media | Marfeel's crawler used for social experiences (Facebook, X/Twitter, Telegram, Reddit, LinkedIn). |
meta-externalads | advertising | Crawls the web to improve advertising and business-related products and services. |
meta-externalagent | ai_crawler | The Meta-ExternalAgent crawler crawls the web for use cases such as training AI models or improving products by indexing content directly. |
meta-externalfetcher | user_initiated | The Meta-ExternalFetcher crawler performs user-initiated fetches of individual links to support specific product functions. Because the fetch was initiated by a user, this crawler may bypass robots.txt rules. |
meta-webindexer | ai_crawler | Crawls web content to provide search results for Meta AI users. |
microsoftpreview | preview | MicrosoftPreview generates page snapshots for Microsoft products. It has desktop and mobile variants, with Chrome version dynamically updated to match the latest Microsoft Edge version. |
momenticbot | user_initiated | Momentic is a AI-powered platform for software testing. It allows you to write reliable end-to-end tests for web apps in a simple and intuitive way using natural language. |
adsnaver | search_engine_crawler | Naver's ad crawler that periodically visits registered ad landing pages to collect on-page content for effective ad matching and ranking. It ignores robots.txt for URLs registered in the ad system. |
naver-blueno | preview | Naver's preview-snippet crawler that fetches summary information (titles, descriptions, images) when users insert links in Naver services such as blogs or cafés. It operates on demand and respects robots.txt. |
naverbot | search_engine_crawler | Naver's web crawler (also known as Yeti) is used by Naver, South Korea's largest search engine, to crawl and index web content. |
newrelic-minions | monitor | New Relic Synthetic monitoring infrastructure that performs API checks and virtual browser instances to monitor websites and applications from global locations |
oai-searchbot | ai_assistant | Indexes websites for inclusion in ChatGPT's search results; does not crawl content for AI model training. |
ohdearbot | monitor | OhDearBot is a monitoring bot operated by Oh Dear that performs uptime checks, broken link detection, and mixed content scanning. The bot follows standard crawling practices and throttles requests to minimize server impact. |
paypal | webhook | PayPal delivers real-time event notifications for payments, subscriptions, and account updates. |
perplexity-user | ai_assistant | Handles user-initiated requests in Perplexity, accessing external content to provide real-time information; not used for automated crawling or AI training. |
perplexitybot | ai_assistant | Indexes websites for inclusion in Perplexity's search results; does not crawl content for AI model training. |
petalbot | search_engine_crawler | PetalBot is a web crawler operated by Huawei's Petal Search engine. It crawls both PC and mobile websites to build an index database for Petal search engine and to provide content recommendations for Huawei Assistant and AI Search services. |
pingdom-bot | monitor | Pingdom Bot is used by Pingdom's monitoring services to perform various checks on websites, including uptime and performance monitoring. |
pinterest-bot | search_engine_crawler | Pinterest's web crawler that indexes content for their platform. It crawls websites to collect metadata for Pins, including images, titles, descriptions, and prices. The crawler also helps maintain Pin data accuracy and detect broken links. |
polar-webhooks | webhook | Polar's webhook service delivers real-time event notifications for payment processing, including purchases, subscriptions, cancellations, and refunds. |
pulsepoint-crawler | advertising | A web crawler used by PulsePoint, a digital advertising technology company, for content indexing and ads.txt verification. |
qatech | monitor | The QA.tech web agent browses the website and identifies potential test cases, and executes tests against a web application |
qstash | webhook | QStash is a platform for building event-driven applications. |
quantcastbot | advertising | Quantcast Bot is a web crawler used for advertisement quality assurance and to understand page content for Interest-Based Audiences. |
qwantbot | search_engine_crawler | Crawls and indexes web content for Qwant search engine. |
razorpay-webhook | webhook | Razorpay’s webhooks enable merchants to receive secure, real-time HTTP callbacks for key payment events—automating reconciliation, notifications, and downstream workflows. |
redirect-pizza | monitor | redirect.pizza's destination monitor ensures that the redirect destination URLs are reachable. |
amazon-route-53-health-check-service | monitor | Amazon Route 53 Health Check Service |
ryebot | ecommerce | Powers automated checkout on behalf of shoppers with explicit consent. |
sanity-webhooks | webhook | Sanity's webhook service that delivers real-time event notifications for content changes and other events. |
sansec-security-monitor | monitor | Sansec Security Monitor is a web crawler that monitors online stores for malicious code, data breaches, and digital skimming attacks. |
seekportbot | search_engine_crawler | SeekportBot is the web crawler for Seekport, a German search engine operated by SISTRIX. The bot crawls and indexes web content while respecting robots.txt directives and crawl delays. |
semrush-site-audit | search_engine_optimization | Semrush Site Audit is a powerful website crawler that analyzes the health of a website by checking for on-page and technical SEO issues, including duplicate content, broken links, HTTPS implementation, hreflang attributes, and more. |
semrush | search_engine_optimization | Semrush is a platform for SEO, content marketing, competitor research, PPC and social media marketing. |
sentry-uptime-monitoring-bot | monitor | Sentry's Uptime Monitoring Bot performs health checks on configured URLs to monitor the availability and reliability of web services. |
seobility | search_engine_crawler | Seobility is a browser-based online SEO software that helps you improve your website’s search engine rankings. |
seranking-backlinks | search_engine_optimization | SE Ranking's backlink analysis crawler that discovers and analyzes backlink profiles for SEO research and competitive analysis. |
seznambot | search_engine_crawler | SeznamBot is the web crawler operated by Seznam.cz, the leading Czech search engine. The bot crawls and indexes web content for Seznam's search results, respecting robots.txt directives and crawl delays. |
shapbot | ai_crawler | Crawls and indexes web content to power Parallel's search and content extraction APIs for AI applications. |
site24x7 | monitor | Site24x7 Bot is used by Site24x7's monitoring services to perform various checks on websites, including uptime and performance monitoring. |
stably | monitor | Stably is a QA testing bot that users run to E2E test their websites for functionality testing and protecting user flows against regressions. |
statuscake-pagespeed | monitor | StatusCake Page Speed monitors your page load and render speeds. |
statuscake-ssl | monitor | StatusCake SSL monitors your website certificates for common issues |
statuscake-uptime | monitor | StatusCake monitors the uptime of your website. |
stripe-webhooks | webhook | Stripe's webhook service that delivers real-time event notifications for payment processing and account updates. |
stripebot | analytics | Crawls Stripe merchant websites to collect data for service delivery and financial regulatory compliance. |
svix | webhook | svix is a webhook service for sending events to webhooks. |
termlybot | monitor | Crawls websites to detect and categorize cookies set by first and third parties. |
twitterbot | preview | Fetches content for shared links on X/Twitter to generate rich previews. |
updown-io | monitor | Performs uptime and performance checks on websites. |
uptime-robot | monitor | Uptime Robot is a platform for monitoring and alerting on your applications. |
v0bot | ai_crawler | Bot for v0 services. |
vemetric-favicon-bot | preview | Fetches favicons from websites in the highest quality available. |
vercel-build-container | preview | System-initiated requests made from Vercel's build container during a build | [View](https://vercel.com/docs/builds)
vercel-favicon-bot | preview | Vercel Favicon Bot | [View](https://vercel.com/docs)
vercelflags | monitor | vercel flags | [View](https://vercel.com/docs/feature-flags/flags-explorer)
vercel-screenshot-bot | preview | Vercel Screenshot Bot | [View](https://vercel.com/docs)
verceltracing | monitor | vercel tracing |
yahoo-ad-monitoring | advertising | Yahoo Ad Monitoring crawls landing pages of URLs listed with Yahoo advertising services to analyze content quality, ensure ad relevance, and improve user experience by maintaining accurate ad listings. |
yahoo-slurp | search_engine_crawler | Yahoo! Slurp is the web crawler (robot) used by Yahoo! Search to discover and index web pages for its search engine. |
yandexbot | search_engine_crawler | YandexBot is a web crawler operated by Yandex, a major Russian search engine. |
* * *
[ Previous Firewall ](https://vercel.com/docs/vercel-firewall)[ Next BotID ](https://vercel.com/docs/botid)
Was this helpful?
Send
On this page
  * [How bot management works](https://vercel.com/docs/bot-management#how-bot-management-works)
  * [Methods of bot management and protection](https://vercel.com/docs/bot-management#methods-of-bot-management-and-protection)
  * [Bot protection managed ruleset](https://vercel.com/docs/bot-management#bot-protection-managed-ruleset)
  * [Enable the ruleset](https://vercel.com/docs/bot-management#enable-the-ruleset)
  * [Bot protection ruleset with reverse proxies](https://vercel.com/docs/bot-management#bot-protection-ruleset-with-reverse-proxies)
  * [AI bots managed ruleset](https://vercel.com/docs/bot-management#ai-bots-managed-ruleset)
  * [Enable the ruleset](https://vercel.com/docs/bot-management#enable-the-ruleset)
  * [Verified bots](https://vercel.com/docs/bot-management#verified-bots)
  * [Bot verification methods](https://vercel.com/docs/bot-management#bot-verification-methods)
  * [Verified bots directory](https://vercel.com/docs/bot-management#verified-bots-directory)


Copy as MarkdownGive feedbackAsk AI about this page
